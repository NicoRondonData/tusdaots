# base image
FROM python:3.10-slim as base

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1
ENV POETRY_VIRTUALENVS_CREATE false

RUN pip install --upgrade pip
# install poetry
RUN curl -sSL https://install.python-poetry.org | python - --version 1.4.2
ENV PATH="/root/.local/bin:$PATH"
RUN pip install poetry
RUN poetry self add poetry-plugin-export
RUN poetry --version

WORKDIR /app
COPY poetry.lock pyproject.toml ./


# linters image
FROM base as linters

RUN poetry install --only linters --no-root
RUN apt-get update && apt-get install -y make

COPY . ./

CMD ["make", "lint.local"]


FROM base as tests

RUN poetry install --with test --no-root
RUN apt-get update && apt-get install -y make

COPY . ./

CMD ["make", "test.local"]

FROM base as development

EXPOSE 8000

ENV DEBUG=1

RUN poetry install --without test,linters --no-root

COPY . ./

CMD uvicorn app.main:app --host 0.0.0.0 --port 8043 --reload

FROM base as production

EXPOSE 8000

RUN poetry install --without test,linters --no-root

COPY . ./

CMD uvicorn app.main:app --host 0.0.0.0 --port 8043
