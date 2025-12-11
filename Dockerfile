FROM python:3.12-slim AS builder

# Install build tools only in builder
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    libomp-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

FROM python:3.12-slim

RUN apt-get update && apt-get install -y libomp-dev && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy installed Python packages only (no build tools)
COPY --from=builder /root/.local /root/.local
ENV PATH=/root/.local/bin:$PATH

COPY ./app ./app
COPY .env .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]