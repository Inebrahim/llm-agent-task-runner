# Simulated LLM agent logic
def run_agent_task(prompt: str) -> str:
    if "weather" in prompt.lower():
        return "The weather is sunny and 25°C."
    elif "time" in prompt.lower():
        return "It's 3:00 PM."
    else:
        return "I'm not sure how to answer that."