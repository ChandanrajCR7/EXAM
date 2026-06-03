from app.server import route_payload


def test_health_route_returns_ok():
    status_code, payload = route_payload("/health")

    assert status_code == 200
    assert payload == {"status": "ok", "service": "exam-app"}


def test_unknown_route_returns_not_found():
    status_code, payload = route_payload("/missing")

    assert status_code == 404
    assert payload == {"status": "not_found", "path": "/missing"}