from flask import Blueprint, request

from vulndesk.db import get_connection

bp = Blueprint("tickets", __name__)


@bp.get("/search")
def search():
    query = request.args.get("q", "")

    # LAB-SQLI-202: búsqueda concatenada directamente a la sentencia SQL.
    sql = (
        "SELECT id, title, owner, priority FROM tickets "
        f"WHERE title LIKE '%{query}%' OR owner LIKE '%{query}%'"
    )

    connection = get_connection()

    try:
        rows = connection.execute(sql).fetchall()
    except Exception as exc:
        connection.close()
        return f"<pre>{exc}</pre>", 500

    connection.close()

    # LAB-XSS-201: query se inserta directamente en HTML sin escape.
    html = f"<h1>Resultados para: {query}</h1><ul>"

    for row in rows:
        html += (
            f"<li>{row['id']} - {row['title']} / "
            f"{row['owner']} / {row['priority']}</li>"
        )

    html += "</ul><p><a href='/'>Volver</a></p>"
    return html
