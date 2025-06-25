FROM python:3.12-slim
WORKDIR /app
COPY . .
RUN pip install flask uv
EXPOSE 8002
CMD ["uv", "run", "app.py"]