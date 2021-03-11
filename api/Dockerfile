from python:3.9
RUN pip3 install fastapi uvicorn
RUN pip install requests
COPY . /app

LABEL maintainer="SouthCoastPy <southcoastpy@gmail.com>" \
      version="0.0.1"

cmd ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "15400"]




