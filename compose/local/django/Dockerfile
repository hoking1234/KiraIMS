ARG PYTHON_TAG=3.13-slim-bookworm
FROM python:${PYTHON_TAG} AS builder

ARG ENV
ENV DockerHOME=/app  

WORKDIR ${DockerHOME}

RUN apt-get update && apt-get install --no-install-recommends -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY ./backend/requirements . 
RUN pip wheel --no-cache-dir --default-timeout=1000 --no-deps --wheel-dir ${DockerHOME}/wheels -r ${ENV}.txt

FROM python:${PYTHON_TAG}

ARG ENV
ENV DockerHOME=/app
ENV PYTHONUNBUFFERED 1  
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR ${DockerHOME}

RUN apt-get update && apt-get install --no-install-recommends -y \
    libpq-dev \
    netcat-traditional \
    gettext \
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && rm -rf /var/lib/apt/lists/*

COPY ./compose/${ENV}/django/entrypoint /entrypoint
COPY ./compose/${ENV}/django/entrypoint-wsgi /entrypoint-wsgi

RUN chmod +x /entrypoint /entrypoint-wsgi\
    && apt-get update && apt-get install -y dos2unix \
    && dos2unix /entrypoint /entrypoint-wsgi

COPY ./backend/mediafiles /app/mediafiles
COPY ./backend/staticfiles /app/staticfiles
RUN chmod -R 755 /app/mediafiles && chmod -R 777 /app/staticfiles

COPY --from=builder ${DockerHOME}/wheels /wheels
RUN pip install --upgrade pip --no-cache /wheels/* \
    && rm -rf /wheels/ \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
RUN chown -R nobody:nogroup ${DockerHOME}
USER nobody

ENTRYPOINT ["/entrypoint"]
