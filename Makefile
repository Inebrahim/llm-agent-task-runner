run:
	uvicorn app.main:app --reload

test:
	pytest

build:
	docker build -t llm-agent .