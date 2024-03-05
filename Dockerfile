FROM python:3.11-slim

WORKDIR /code

# Install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy project files
COPY . .

# Expose the port used by FastAPI (typically 8000)
EXPOSE 8000

# Command to start the service
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--reload"]
