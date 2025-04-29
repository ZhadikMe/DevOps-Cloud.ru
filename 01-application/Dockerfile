FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app.py .

ENV AUTHOR="Default Author"

EXPOSE 8000

CMD ["python", "app.py"]