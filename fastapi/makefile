.PHONY: build run stop destroy sh logs lint tests makemigrations migrate

DOCKER_LOCATION = docker-compose.yml

build:
	docker-compose -f $(DOCKER_LOCATION) up --build
	& alembic upgrade head

run:
	docker-compose -f $(DOCKER_LOCATION) up

stop:
	docker-compose -f $(DOCKER_LOCATION) stop

destroy:
	docker-compose -f $(DOCKER_LOCATION) down

sh: 
	docker-compose -f $(DOCKER_LOCATION) exec fastapi-app sh

logs:
	docker-compose -f $(DOCKER_LOCATION) logs -f fastapi-app

lint:
	isort . && black . && flake8 --exclude=.venv

tests:
	pytest -v

makemigrations:
	docker-compose exec fastapi-app alembic revision --autogenerate -m "migration"

migrate:
	docker-compose exec fastapi-app alembic upgrade head