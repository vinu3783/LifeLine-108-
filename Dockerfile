# ── Google Cloud Run Deployment ──
# Python 3.11 slim base
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy and install Python dependencies first (layer caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the full project
COPY . .

# Cloud Run provides PORT env variable — default 8080
ENV PORT=8080

# Expose the port
EXPOSE 8080

# Start with gunicorn + eventlet for SocketIO support
CMD exec gunicorn --worker-class eventlet -w 1 \
    --bind 0.0.0.0:$PORT \
    --timeout 120 \
    --keep-alive 5 \
    simple_app:app
