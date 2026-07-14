# force rebuild 4
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Copy application code
COPY ./app /app
COPY ./templates /app/templates
COPY ./static /app/static

# Install required dependencies
RUN pip install fastapi uvicorn jinja2 python-multipart aiofiles

# Expose port (Coolify is gone, so this is direct)
EXPOSE 8000

# Start FastAPI using Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
