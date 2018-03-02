FROM python:3
ENV PYTHONUNBUFFERED 1
RUN pip install Django==2.0
RUN pip install Pillow
RUN pip install django-webpack-loader
RUN pip install fabric3
RUN mkdir /code

ADD tests/project.json /tmp/project1/.djangoprototyper/

WORKDIR /code

CMD ["python", "tests/test.py"]
