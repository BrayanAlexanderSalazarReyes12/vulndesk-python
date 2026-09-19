from flask import Blueprint, render_template_string, request

bp = Blueprint("templates_lab", __name__)


@bp.post("/preview-template")
def preview_template():
    template_text = request.form.get("template", "Hola {{ name }}")
    name = request.form.get("name", "usuario")

    # LAB-SSTI-201: el usuario controla el texto que Jinja interpreta
    # como plantilla del servidor.
    return render_template_string(template_text, name=name)
