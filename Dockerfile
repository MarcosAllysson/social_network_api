FROM python:3.9.5-slim-buster

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get update -y && apt-get install -y gcc python3-dev musl-dev libc-dev gettext

WORKDIR .

# Install dependencies.
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements-dev.txt

# Copy local code to the container image.
COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]