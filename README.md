# VulnDesk Python

Aplicación **Python + Flask + SQLite** intencionalmente vulnerable para pruebas controladas del proyecto Auditor.

> ⚠️ LABORATORIO. No desplegar en Internet ni utilizar datos reales.

## Objetivo

Este repositorio es el tercer banco de pruebas del Evaluador/Auditor. Debe permitir comprobar si una receta aprendida en Java o Node puede reconocer y corregir el mismo patrón vulnerable implementado en Python.

## Stack

- Python 3.11+
- Flask
- SQLite
- Requests

## Ejecución

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/macOS
source .venv/bin/activate

pip install -r requirements.txt
python run.py
```

Abrir:

```
http://localhost:5000
```

Usuarios de laboratorio:

- admin / admin123
- analyst / analyst123
- user / user123

## Vulnerabilidades sembradas

| ID | Vulnerabilidad |
|---|---|
| LAB-SQLI-201 | SQL Injection en login |
| LAB-SQLI-202 | SQL Injection en búsqueda |
| LAB-XSS-201 | Reflected XSS |
| LAB-TRAV-201 | Path Traversal |
| LAB-UPLOAD-201 | Unrestricted File Upload |
| LAB-IDOR-201 | IDOR |
| LAB-AUTHZ-201 | Broken Access Control |
| LAB-REDIR-201 | Open Redirect |
| LAB-CMD-201 | OS Command Injection |
| LAB-SSRF-201 | SSRF |
| LAB-SSTI-201 | Server-Side Template Injection |
| LAB-CRYPTO-201 | Hash MD5 |
| LAB-SECRET-201 | Secretos hardcodeados |
| LAB-SESSION-201 | Secreto de sesión débil |
| LAB-INFO-201 | Exposición de errores |
| LAB-CORS-201 | CORS permisivo |
| LAB-MASS-201 | Mass Assignment / cambio de rol |

Los comentarios `LAB-*` son únicamente la verdad de terreno del laboratorio. El Auditor debe detectar el patrón vulnerable sin depender del comentario.
