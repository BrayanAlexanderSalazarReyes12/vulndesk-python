import requests
from flask import Blueprint, jsonify, request

bp = Blueprint("network", __name__)


@bp.get("/fetch")
def fetch_url():
    target = request.args.get("url")

    if not target:
        return jsonify({"error": "Falta el parámetro url"}), 400

    try:
        # LAB-SSRF-201: realiza una solicitud a una URL completamente
        # controlada por el usuario sin allowlist ni bloqueo de redes internas.
        response = requests.get(target, timeout=3)

        return (
            response.text[:20000],
            response.status_code,
            {"Content-Type": "text/plain; charset=utf-8"},
        )
    except Exception as exc:
        return jsonify({
            "target": target,
            "error": str(exc),
        }), 500
