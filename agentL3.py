import ollama
import json
import re

# -----------------------------
# STEP 1: TOOLS
# -----------------------------

def get_weather(city: str):
    return f"The weather in {city} is sunny 🌞"


def calculate(expression: str):
    try:
        result = eval(expression, {"__builtins__": None}, {})
        return f"Result: {result}"
    except:
        return "Invalid calculation"


TOOLS = {
    "get_weather": get_weather,
    "calculate": calculate
}

# -----------------------------
# STEP 2: MEMORY STORAGE
# -----------------------------
conversation_history = []

# -----------------------------
# STEP 3: AGENT FUNCTION
# -----------------------------

def run_agent(user_input):

    global conversation_history

    # ✅ ALWAYS store string
    conversation_history.append({
        "role": "user",
        "content": str(user_input)
    })

    # Keep last 10 messages
    conversation_history[:] = conversation_history[-10:]

    # -----------------------------
    # SYSTEM PROMPT
    # -----------------------------
    system_prompt = """
You are an AI agent with memory.

IMPORTANT RULES:
1. You MUST respond ONLY in valid JSON.
2. Do NOT write anything outside JSON.
3. If no tool is needed, set tool = "none".
4. Only use tools when absolutely necessary.

Available tools:
- get_weather(city)
- calculate(expression)

Response format:
{
  "tool": "get_weather OR calculate OR none",
  "input": "string",
  "response": "final answer to user"
}
"""

    messages = [{"role": "system", "content": system_prompt}] + conversation_history

    # -----------------------------
    # CALL OLLAMA
    # -----------------------------
    try:
        response = ollama.chat(
            model="llama3",
            messages=messages
        )
    except Exception as e:
        return f"⚠️ Ollama Error: {str(e)}\n👉 Make sure Ollama is running!"

    reply = response["message"]["content"]

    # -----------------------------
    # SAFE JSON EXTRACTION
    # -----------------------------
    try:
        json_match = re.search(r'\{.*\}', reply, re.DOTALL)

        if not json_match:
            raise ValueError("No JSON found")

        action = json.loads(json_match.group())

    except Exception:
        return f"⚠️ JSON Error:\n{reply}"

    # ✅ FIX: FORCE STRING TYPES
    tool_name = str(action.get("tool", "none"))
    tool_input = str(action.get("input", ""))
    final_response = str(action.get("response", ""))

    # -----------------------------
    # TOOL EXECUTION
    # -----------------------------
    if tool_name in TOOLS:
        tool_result = TOOLS[tool_name](tool_input)
        final_output = f"{final_response}\n🔧 Tool Result: {tool_result}"
    else:
        final_output = final_response

    # -----------------------------
    # SAVE CLEAN MEMORY (STRING ONLY)
    # -----------------------------
    conversation_history.append({
        "role": "assistant",
        "content": str(final_response)
    })

    return final_output


# -----------------------------
# STEP 4: RUN LOOP
# -----------------------------

if __name__ == "__main__":
    print("🤖 Level 3 AI Agent (Memory + Tools)\nType 'exit' to quit\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("👋 Goodbye!")
            break

        result = run_agent(user_input)
        print("Agent:", result)