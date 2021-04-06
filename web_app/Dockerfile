FROM python:3.9


# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV FLASK_APP "web.py"
ENV FLASK_ENV "development"
ENV FLASK_DEBUG True

RUN mkdir /app
WORKDIR /app

RUN pip install --upgrade cryptography

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

run pip install flask_cors

COPY ./src .

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]