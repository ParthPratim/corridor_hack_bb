FROM python:3.8.16
ARG API_LAYER_PORT

COPY requirements.txt .

RUN apt-get update && \
    apt-get install default-libmysqlclient-dev && \
    pip install -r requirements.txt 

EXPOSE ${API_LAYER_PORT}
CMD cd /api-layer && python manage.py migrate && python manage.py runserver 0.0.0.0:${API_LAYER_PORT}


