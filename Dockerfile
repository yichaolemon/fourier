FROM python:3.8-alpine

WORKDIR /app

RUN pip install Flask

CMD ["python3", "view.py"]
