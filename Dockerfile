FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY src/ src/
COPY pyproject.toml .
RUN pip install  .


# Copy the application code
COPY api/ api/
COPY models/ models/
COPY data/ data/


CMD uvicorn api.webapi:my_api --host 0.0.0.0 --port $PORT 