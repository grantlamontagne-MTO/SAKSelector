# force rebuild 3
FROM python:3.11-slim

WORKDIR /app

# Copy application code
COPY ./app /app
COPY ./templates /app/templates

# Install required dependencies
RUN pip install fastapi uvicorn jinja2 python-multipart aiofiles

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
