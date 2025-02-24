# Dockerfile
FROM python:3.11-slim

# Set apt to noninteractive mode
ENV DEBIAN_FRONTEND=noninteractive

# Set a flag for production (default)
ENV ENVIRONMENT=production

# Install common system packages (if needed)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
 && rm -rf /var/lib/apt/lists/*

# Copy your project files into the image
# (For a simple project, copying everything is acceptable)
COPY . .

# Install Python dependencies (assuming you have requirements.txt)
RUN pip install --no-cache-dir -r requirements.txt

# Set the working directory (inside the container)
WORKDIR /app

# Expose port 8000 (adjust as needed)
EXPOSE 8000

# Define the default command (for production/UAT, this might run your app)
CMD ["python", "src/app.py"]
