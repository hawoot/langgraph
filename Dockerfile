FROM python:3.11-slim

WORKDIR /app

# Install production dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy in the source code
COPY . .

# A minimal final command for your web server:
# (You can also rely on docker-compose to define the command.)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
