import ollama
import json

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


# Tool mapping
TOOLS = {
    "get_weather": get_weather,
    "calculate": calculate
}

# -----------------------------
# STEP 2: AGENT FUNCTION
# -----------------------------

def run_agent(user_input):

    # -----------------------------
    # STEP 2A: ASK LLM WHAT TO DO
    # -----------------------------
    prompt = f"""
You are an AI agent.

Decide the correct action.

Available tools:
1. get_weather(city)
2. calculate(expression)

Respond ONLY in JSON format like:
{{
  "tool": "tool_name",
  "input": "input_value"
}}

If no tool is needed:
{{
  "tool": "none",
  "input": ""
}}

User input: {user_input}
"""

    response = ollama.chat(
        model="llama3",
        messages=[{"role": "user", "content": prompt}]
    )

    reply = response["message"]["content"]

    # -----------------------------
    # STEP 2B: PARSE LLM OUTPUT
    # -----------------------------
    try:
        action = json.loads(reply)
        tool_name = action.get("tool")
        tool_input = action.get("input")

    except Exception:
        return f"⚠️ Failed to parse response:\n{reply}"

    # -----------------------------
    # STEP 2C: EXECUTE TOOL
    # -----------------------------
    if tool_name in TOOLS:
        result = TOOLS[tool_name](tool_input)

        return f"🔧 Tool Used: {tool_name}\n👉 {result}"

    # -----------------------------
    # STEP 2D: NORMAL RESPONSE
    # -----------------------------
    elif tool_name == "none":
        return reply

    else:
        return f"⚠️ Unknown tool: {tool_name}"


# -----------------------------
# STEP 3: RUN LOOP
# -----------------------------

if __name__ == "__main__":
    print("🤖 Level 2 AI Agent (Auto Tool Selection)\nType 'exit' to quit\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            break

        result = run_agent(user_input)
        print("Agent:", result)