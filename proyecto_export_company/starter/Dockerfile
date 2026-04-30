FROM python:3.12-slim

WORKDIR /app

COPY pyproject.toml .

RUN pip install --upgrade pip
RUN pip install fastapi uvicorn

COPY ./src ./src

EXPOSE 8000

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]