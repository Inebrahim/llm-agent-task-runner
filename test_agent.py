from app.agent import run_agent_task

def test_weather_prompt():
    response = run_agent_task("What is the weather?")
    assert "sunny" in response.lower()

def test_time_prompt():
    response = run_agent_task("What time is it?")
    assert "pm" in response.lower() or "am" in response.lower()

def test_unknown_prompt():
    response = run_agent_task("Tell me a joke.")
    assert "not sure" in response.lower()