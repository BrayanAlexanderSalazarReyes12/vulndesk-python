import os
import tempfile

from flask import Blueprint, jsonify, request, send_file

bp = Blueprint("files", __name__)

FILES_DIR = os.path.join(tempfile.gettempdir(), "vulndesk-files")
UPLOADS_DIR = os.path.join(tempfile.gettempdir(), "vulndesk-uploads")

os.makedirs(FILES_DIR, exist_ok=True)
os.makedirs(UPLOADS_DIR, exist_ok=True)

sample_file = os.path.join(FILES_DIR, "manual.txt")
if not os.path.exists(sample_file):
    with open(sample_file, "w", encoding="utf-8") as handle:
        handle.write("Manual de laboratorio VulnDesk Python\n")


@bp.get("/download")
def download():
    filename = request.args.get("file", "manual.txt")

    # LAB-TRAV-201: la ruta final usa entrada del usuario sin confinamiento.
    target = os.path.join(FILES_DIR, filename)

    if not os.path.isfile(target):
        return jsonify({
            "error": "Archivo no encontrado",
            "attempted_path": target,
        }), 404

    return send_file(target)


@bp.post("/upload")
def upload():
    uploaded = request.files.get("file")

    if uploaded is None:
        return jsonify({"error": "Falta archivo"}), 400

    # LAB-UPLOAD-201: no valida extensión, MIME ni sanea el nombre.
    destination = os.path.join(UPLOADS_DIR, uploaded.filename)
    uploaded.save(destination)

    return jsonify({
        "message": "Archivo cargado",
        "filename": uploaded.filename,
        "stored_at": destination,
        "mimetype": uploaded.mimetype,
    })
