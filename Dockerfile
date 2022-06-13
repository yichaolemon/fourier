FROM python:3.8-alpine

WORKDIR /app

RUN pip install Flask && apk add py3-numpy && apk add g++ && pip install numpy

CMD ["python3", "view.py"]
