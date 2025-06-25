FROM golang:1.23-alpine AS go
WORKDIR /app
COPY . .
RUN  go build -o service1 main.go
FROM alpine:latest
WORKDIR /app
COPY --from=go /app/service1 .
EXPOSE 8001
CMD ["./service1"]