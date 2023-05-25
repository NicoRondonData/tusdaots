APP_NAME = tusdatos

.PHONY: load-env
load-env:
	export $(shell sed 's/=.*//' $(.env))

.PHONY: install
install:
	poetry install
	pre-commit install

## Commands local
.PHONY: lint.local
lint.local:
	poetry run pre-commit run --all-files

.PHONY: run.local
run.local:
	uvicorn app.main:app --host 0.0.0.0 --port 8043 --reload

.PHONY: test.local
test.local:
	poetry run pytest --cov=app tests/app --cov-report=term

## Build images
.PHONY: build.base
build.base:
	DOCKER_BUILDKIT=1 docker build -t $(APP_NAME)-base . --target base

.PHONY: build.linters
build.linters:
	DOCKER_BUILDKIT=1 docker build -t $(APP_NAME)-linters . --target linters

.PHONY: build.tests
build.tests:

	DOCKER_BUILDKIT=1 docker build -t $(APP_NAME)-tests . --target tests

.PHONY: build.dev
build:
	DOCKER_BUILDKIT=1 docker build -t $(APP_NAME)-dev . --target development

## Commands with Docker
.PHONY: makemigrations
makemigrations:
	docker exec -it $(APP_NAME)-dev alembic revision --autogenerate -m "$(name)"

.PHONY: migrate
migrate:
	docker exec -it $(APP_NAME)-dev alembic upgrade head


.PHONY: lint.docker
lint:
	docker run --rm --name $(APP_NAME)-linters $(APP_NAME)-linters:latest

.PHONY: test.docker
test:
	-@docker rm -f $(APP_NAME)-tests 2> /dev/null
	docker run --name $(APP_NAME)-tests $(APP_NAME)-tests:latest
	docker rm -f $(APP_NAME)-tests




.PHONY: run
run:
	-@docker rm -f $(APP_NAME)-dev 2> /dev/null
	docker run  -d -p 8043:8043 --name $(APP_NAME)-dev -v $(PWD):/app $(APP_NAME)-dev

.PHONY: run
echo.run:
	@echo "docker run  -d -p 8043:8043 --name $(APP_NAME)-dev -v $(PWD):/app $(APP_NAME)-dev"



## Delete image
.PHONY: rmi
rmi.base:
	docker rmi -f $(APP_NAME)-base

.PHONY: rmi
rmi.linters:
	docker rmi -f $(APP_NAME)-linters

.PHONY: rmi.tests
rmi.tests:
	docker rmi -f $(APP_NAME)-tests

.PHONY: rmi
rmi:
	docker rmi -f $(APP_NAME)-dev


## Delete container
.PHONY: rmi
rm:
	docker rm -f $(APP_NAME)-dev

.PHONY: rmi.base
rm.base:
	docker rm -f $(APP_NAME)-base


## Show container logs.
.PHONY: logs
logs:
	docker logs --tail 100 -f ${APP_NAME}-dev

.PHONY: lock
lock.local:
	poetry lock --no-update

.PHONY: lock
lock:
	DOCKER_BUILDKIT=1 docker build -t $(APP_NAME)-base --target base .

	docker run --rm --name $(APP_NAME)-base -v $(PWD):/app $(APP_NAME)-base poetry lock --no-update
