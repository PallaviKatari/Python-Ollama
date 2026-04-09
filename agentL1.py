import ollama

# -----------------------------
# STEP 1: TOOLS
# -----------------------------

def get_weather(city: str):
    return f"The weather in {city} is sunny 🌞"


def calculate(expression: str):
    try:
        # safer eval
        result = eval(expression, {"__builtins__": None}, {})
        return f"Result: {result}"
    except Exception:
        return "Invalid calculation"


# -----------------------------
# STEP 2: AGENT FUNCTION
# -----------------------------

def run_agent(user_input):

    user_input = user_input.strip()

    # ✅ TOOL 1: WEATHER
    if "weather" in user_input.lower():
        words = user_input.split()
        city = words[-1] if len(words) > 1 else "your city"
        return get_weather(city)

    # ✅ TOOL 2: CALCULATOR
    elif any(op in user_input for op in ["+", "-", "*", "/"]):
        return calculate(user_input)

    # -----------------------------
    # ✅ STEP 3: LOCAL LLM CALL
    # -----------------------------
    try:
        response = ollama.chat(
            model="llama3",   # make sure this model is installed
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant."},
                {"role": "user", "content": user_input}
            ]
        )

        return response["message"]["content"]

    except Exception as e:
        return f"⚠️ Ollama Error: {str(e)}\n👉 Make sure Ollama is running!"


# -----------------------------
# STEP 3: RUN LOOP
# -----------------------------

if __name__ == "__main__":
    print("🤖 Local AI Agent (Ollama) - type 'exit' to quit\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("👋 Goodbye!")
            break

        result = run_agent(user_input)
        print("Agent:", result)