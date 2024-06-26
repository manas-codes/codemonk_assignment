FROM python:3.11-slim

# Set unbuffered output for python
ENV PYTHONUNBUFFERED 1

# Create app directory
WORKDIR /app

# Install app dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Bundle app source
COPY . .

# Expose port
EXPOSE 8000

# CMD ["python", "manage.py", "makemigrations core"]

# CMD ["python", "manage.py", "migrate"]

# entrypoint to run the django.sh file
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
