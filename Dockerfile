###############################################
# Base Image
###############################################
FROM python:3.11-alpine3.17 as requirements-stage

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTE$PYSETUP_PATH=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.2.2  \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    PYSETUP_PATH="code" \
    VENV_PATH="/$PYSETUP_PATH/.venv"

USER root

WORKDIR /tmp

RUN pip install poetry

COPY ./pyproject.toml ./poetry.lock* /tmp/

RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

###############################################
# Production Image
###############################################

FROM python:3.11-slim-bullseye

USER root

WORKDIR /$PYSETUP_PATH

RUN pip install --upgrade pip 
    
COPY --from=requirements-stage /tmp/requirements.txt /$PYSETUP_PATH/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /$PYSETUP_PATH/requirements.txt


COPY ./src/app /$PYSETUP_PATH/app


CMD ["gunicorn", "app.main:app", "--workers", "4", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:80"]
