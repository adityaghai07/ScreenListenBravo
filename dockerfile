FROM python:3.11-slim

WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install Poetry
RUN pip install poetry

RUN poetry install

# Make port 80 available 
EXPOSE 80

ENV PORT 80

# Run the application
CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
