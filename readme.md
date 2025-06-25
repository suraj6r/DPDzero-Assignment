# DevOps Intern Assignment: Nginx Reverse Proxy + Docker

## Project Overview

This project demonstrates how to set up a multi-service application using Docker Compose and an Nginx reverse proxy. It features two backend services — one written in Go and another in Python (Flask) — both running in separate Docker containers. An Nginx container acts as a reverse proxy, routing incoming HTTP requests based on URL paths to the appropriate service.

---

## Architecture

- **service1 (Go app):**  
  Listens on port 8001 inside its container. It provides two endpoints: `/ping` and `/hello`.

- **service2 (Python Flask app):**  
  Listens on port 8002 inside its container. It provides `/ping`, `/hello`, and `/` (root) endpoints.

- **Nginx reverse proxy:**  
  Runs in its own container, listens on port 80 internally (exposed as 8080 on host), and routes traffic as follows:
  
  - Requests to `/service1/*` are forwarded to `service1` with the `/service1` prefix stripped.
  - Requests to `/service2/*` are forwarded to `service2` with the `/service2` prefix stripped.
  - Requests to `/` (root) are forwarded directly to `service2` root endpoint.
  - Redirects are configured for `/service1` and `/service2` without trailing slashes to their trailing-slash URLs.

All containers communicate over Docker's default bridge network.

---

## Routing Details

| URL Path                 | Proxied To          | Notes                                   |
|--------------------------|---------------------|-----------------------------------------|
| `/`                      | service2:8002       | Root requests go to service2            |
| `/service1/ping`         | service1:8001/ping  | service1 handles `/ping` endpoint       |
| `/service1/hello`        | service1:8001/hello | service1 handles `/hello` endpoint      |
| `/service2/ping`         | service2:8002/ping  | service2 `/ping` endpoint               |
| `/service2/hello`        | service2:8002/hello | service2 `/hello` endpoint              |

---

## Key Features

- **Single port access:** All services accessible via `localhost:8080` through Nginx reverse proxy.
- **Path-based routing:** Nginx routes requests based on URL prefixes.
- **Request logging:** Custom Nginx logs capture client IP, timestamp, and request path.
- **Dockerized services:** Each backend service runs in its own container for isolation.
- **Clean modular setup:** Separate Dockerfiles for Go app, Python app, and Nginx proxy.
- **Redirects:** Handles trailing slash normalization via Nginx.

---

## How to Run

```bash
docker-compose up --build

