FROM python:3.10-slim
ENV PYTHONUNBUFFERED=1
WORKDIR /app_blog
COPY . .

# Install & use pipenv
COPY Pipfile Pipfile.lock ./
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir pipenv && pipenv install --system --ignore-pipfile --deploy --clear
#CMD ["python3", "./manage.py", "makemigrations"]
#CMD ["python3", "./manage.py", "migrate"]
#CMD ["python3", "./manage.py", "runserver", "0.0.0.0:8000"]
