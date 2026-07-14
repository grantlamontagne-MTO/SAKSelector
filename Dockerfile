# force rebuild

FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Copy your FastAPI application code
COPY ./app /app

# Copy your templates folder (this was the missing piece)
COPY ./templates /app/templates

# Install dependencies
RUN pip install fastapi uvicorn

# Expose port (Coolify maps this automatically)
EXPOSE 8000

# Start FastAPI using Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
