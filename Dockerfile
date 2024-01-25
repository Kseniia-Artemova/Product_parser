# Использование официального образа Python как базового
FROM python:3.11-alpine

# Установка переменных среды для poetry
ENV POETRY_VERSION=1.4.2 \
    POETRY_VIRTUALENVS_CREATE=false \
    APP_HOME=/app \
    RUNNING_IN_DOCKER=true

# Установка Google Chrome
RUN apk --no-cache add chromium chromium-chromedriver

# Установка Poetry
RUN pip install "poetry==$POETRY_VERSION"

# Создание директории приложения
WORKDIR $APP_HOME
VOLUME $APP_HOME

# Копирование файлов зависимостей
COPY poetry.lock pyproject.toml $APP_HOME/

# Установка зависимостей проекта
RUN poetry install --only main

# Копирование исходного кода проекта
COPY . $APP_HOME

# Команда для запуска приложения
CMD ["python", "main.py"]