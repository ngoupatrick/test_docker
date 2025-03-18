# dependency layer
FROM python:3.12-slim AS builder

WORKDIR /app

COPY pyproject.toml requirements.txt ./
RUN pip wheel --no-cache-dir --no-deps --wheel-dir wheels -r requirements.txt

COPY src src
RUN pip wheel --no-cache-dir --no-deps --wheel-dir wheels .

# building layer: to run app
FROM python:3.12-slim AS runner

COPY --from=builder /app/wheels /wheels
RUN pip install --no-cache /wheels/* && rm -rf /wheels

EXPOSE 8000

WORKDIR /app
COPY --from=builder /app/src /app/src

#CMD ["sh", "-c", "fastapi run src --port 8000 --host 0.0.0.0"]
CMD ["sh", "-c", "fastapi run src --port ${PORT} --host 0.0.0.0"]