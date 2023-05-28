FROM python:alpine

ENV PYTHONUNBUFFERED=1
#устанавливает флаг для Python, чтобы он выводил данные в стандартный поток вывода без буферизации
ENV PYTHONDONTWRITEBYTECODE=1
#отключает создание .pyc-файлов, чтобы избежать проблем с обновлением кода в контейнере.

WORKDIR /telegram_bot
# директория в контейнере, куда будут копироваться все файлы проекта.

COPY ./requirements.txt ./

# Устанавливаем зависимости и gunicorn
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r ./requirements.txt

COPY ./ ./

RUN chmod -R 777 ./