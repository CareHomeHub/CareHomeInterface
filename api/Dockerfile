from python:3.9
COPY . /app

RUN pip3 install fastapi uvicorn
RUN pip3 install requests
RUN pip3 install -r app/requirements.txt

LABEL maintainer="SouthCoastPy <southcoastpy@gmail.com>" \
      version="0.0.1"

EXPOSE "8000" "7687"

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
