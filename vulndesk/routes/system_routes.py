import subprocess

from flask import Blueprint, jsonify, request

bp = Blueprint("system", __name__)


@bp.get("/diagnostic")
def diagnostic():
    host = request.args.get("host", "127.0.0.1")

    # LAB-CMD-201: entrada del usuario concatenada a un comando ejecutado
    # mediante shell=True.
    command = "ping -n 1 " + host if subprocess.os.name == "nt" else "ping -c 1 " + host

    try:
        completed = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            timeout=5,
        )

        return (
            completed.stdout
            + "\n"
            + completed.stderr
            + f"\nexit={completed.returncode}"
        ), 200, {"Content-Type": "text/plain; charset=utf-8"}
    except Exception as exc:
        return jsonify({
            "command": command,
            "error": str(exc),
        }), 500
