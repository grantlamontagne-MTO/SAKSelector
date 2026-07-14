FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy application code
COPY ./app /app
COPY ./templates /app/templates
COPY ./static /app/static

# Completely remove FastAPI + Starlette (if present)
RUN pip uninstall -y fastapi starlette || true

# Install matching versions
RUN pip install \
    fastapi==0.95.2 \
    starlette==0.27.0 \
    uvicorn \
    jinja2 \
    python-multipart \
    aiofiles

# Expose port
EXPOSE 8000

# Run the app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
