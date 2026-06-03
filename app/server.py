import json
import os
from http.server import BaseHTTPRequestHandler, HTTPServer


def route_payload(path: str) -> tuple[int, dict[str, str]]:
    if path in {"/", "/health"}:
        return 200, {"status": "ok", "service": "exam-app"}

    return 404, {"status": "not_found", "path": path}


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:
        status_code, payload = route_payload(self.path)
        body = json.dumps(payload).encode("utf-8")

        self.send_response(status_code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format: str, *args: object) -> None:
        return


def run(host: str = "0.0.0.0", port: int | None = None) -> None:
    server_port = port if port is not None else int(os.getenv("PORT", "8000"))
    server = HTTPServer((host, server_port), RequestHandler)
    print(f"Serving on http://{host}:{server_port}")
    server.serve_forever()
