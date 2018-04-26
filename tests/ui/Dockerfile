FROM python:3
ENV PYTHONUNBUFFERED 1
RUN pip install Django==2.0
RUN pip install Pillow
RUN pip install django-webpack-loader

RUN apt-get update && apt-get -y install curl

RUN curl -sL https://deb.nodesource.com/setup_8.x | bash
RUN apt-get install -y nodejs






RUN mkdir /code
ADD frontend/package.json /code/frontend/
WORKDIR /code/frontend

RUN npm install
RUN npm rebuild node-sass --force




ADD frontend /code/frontend
RUN npm run build


ADD backend /code/backend

WORKDIR /code/backend/

EXPOSE 8000

CMD ["python", "main.py", "--bind=0.0.0.0:8000", "/tmp/testproject1"]
