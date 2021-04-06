FROM python:3.9.4-alpine3.13

# This prevents Python from writing out pyc files
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

WORKDIR /code

RUN pip install --upgrade pip
COPY ./requirements.txt code/requirements.txt
RUN pip install -r code/requirements.txt