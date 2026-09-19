from flask import Blueprint, jsonify, request

from vulndesk.db import get_connection

bp = Blueprint("users", __name__)


@bp.get("/profile/<int:user_id>")
def profile(user_id):
    # LAB-IDOR-201: el recurso se consulta sólo por el ID solicitado,
    # sin comprobar que pertenezca al usuario autenticado.
    connection = get_connection()
    user = connection.execute(
        """
        SELECT id, username, full_name, email, role
        FROM users
        WHERE id = ?
        """,
        (user_id,),
    ).fetchone()
    connection.close()

    if not user:
        return jsonify({"error": "No encontrado"}), 404

    return jsonify(dict(user))


@bp.put("/profile/<int:user_id>")
def update_profile(user_id):
    payload = request.get_json(silent=True) or {}

    email = payload.get("email", "")
    role = payload.get("role", "USER")

    # LAB-MASS-201: permite que el cliente modifique directamente role.
    connection = get_connection()
    cursor = connection.execute(
        "UPDATE users SET email = ?, role = ? WHERE id = ?",
        (email, role, user_id),
    )
    connection.commit()
    changed = cursor.rowcount
    connection.close()

    return jsonify({
        "updated": changed,
        "id": user_id,
        "email": email,
        "role": role,
    })
