from flask import Blueprint, jsonify, redirect, request, session

from vulndesk import config

bp = Blueprint("admin", __name__)


@bp.get("/admin")
def admin():
    # LAB-AUTHZ-201: sólo comprueba si existe sesión.
    # No verifica que session["role"] sea ADMIN.
    if "username" not in session:
        return jsonify({"error": "Debes autenticarte"}), 401

    return jsonify({
        "panel": "Administración",
        "current_user": session.get("username"),
        "backup_key": config.BACKUP_KEY,
    })


@bp.get("/go")
def go():
    target = request.args.get("next", "/")

    # LAB-REDIR-201: destino de redirección controlado por el usuario.
    return redirect(target)
