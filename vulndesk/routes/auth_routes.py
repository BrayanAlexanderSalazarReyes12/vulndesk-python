from flask import Blueprint, jsonify, request, session

from vulndesk.db import get_connection

bp = Blueprint("auth", __name__)


@bp.post("/login")
def login():
    username = request.form.get("username", "")
    password = request.form.get("password", "")

    # LAB-SQLI-201: entrada del usuario interpolada directamente en SQL.
    sql = (
        "SELECT id, username, full_name, role FROM users "
        f"WHERE username='{username}' AND password='{password}'"
    )

    connection = get_connection()

    try:
        user = connection.execute(sql).fetchone()
    except Exception as exc:
        # LAB-INFO-201: expone SQL y detalles internos al cliente.
        return jsonify({
            "error": str(exc),
            "sql": sql,
        }), 500
    finally:
        connection.close()

    if not user:
        return jsonify({
            "error": "Credenciales incorrectas",
            "username": username,
        }), 401

    # LAB-SESSION-201: usa una clave de sesión débil configurada en la app.
    session["user_id"] = user["id"]
    session["username"] = user["username"]
    session["role"] = user["role"]

    return jsonify({
        "message": "Login correcto",
        "user": dict(user),
    })
