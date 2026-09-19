# VulnDesk Python - Ground Truth Manifest

Este archivo define la verdad de terreno del tercer laboratorio del proyecto Auditor.

## Hallazgos esperados

| ID | CWE orientativo | Archivo | Patrón esperado |
|---|---:|---|---|
| LAB-SQLI-201 | CWE-89 | routes/auth_routes.py | SQL construido con f-string y credenciales |
| LAB-SQLI-202 | CWE-89 | routes/ticket_routes.py | SQL construido con q |
| LAB-XSS-201 | CWE-79 | routes/ticket_routes.py | q escrito directamente en HTML |
| LAB-TRAV-201 | CWE-22 | routes/file_routes.py | Ruta derivada de input sin confinamiento |
| LAB-UPLOAD-201 | CWE-434 | routes/file_routes.py | Upload sin allowlist ni saneamiento |
| LAB-IDOR-201 | CWE-639 | routes/user_routes.py | Perfil consultado por ID sin autorización |
| LAB-AUTHZ-201 | CWE-862 | routes/admin_routes.py | Falta validación del rol ADMIN |
| LAB-REDIR-201 | CWE-601 | routes/admin_routes.py | redirect con destino controlado por usuario |
| LAB-CMD-201 | CWE-78 | routes/system_routes.py | shell=True con comando construido desde input |
| LAB-SSRF-201 | CWE-918 | routes/network_routes.py | requests.get hacia URL del usuario |
| LAB-SSTI-201 | CWE-1336 | routes/template_routes.py | render_template_string con plantilla del usuario |
| LAB-CRYPTO-201 | CWE-327 | weak_crypto.py | Uso de MD5 |
| LAB-SECRET-201 | CWE-798 | config.py | Valores sensibles hardcodeados |
| LAB-SESSION-201 | CWE-321 | config.py/app.py | Flask secret key débil y embebida |
| LAB-INFO-201 | CWE-209 | app.py/auth_routes.py | Error/stack interno expuesto |
| LAB-CORS-201 | CWE-942 | app.py | Access-Control-Allow-Origin: * |
| LAB-MASS-201 | CWE-915 | routes/user_routes.py | role modificable desde el request |

## Matriz de generalización

El objetivo no es que el Auditor memorice sintaxis. Debe reconocer el flujo vulnerable.

| Patrón | Java | Node | Python |
|---|---|---|---|
| SQL Injection | Statement + concatenación | sqlite3 + concatenación | sqlite3 + f-string |
| XSS | PrintWriter | res.send | respuesta HTML directa |
| Command Injection | Runtime.exec | child_process.exec | subprocess.run + shell=True |
| SSRF | URLConnection | fetch | requests.get |
| Path Traversal | new File(base,input) | path.join(base,input) | os.path.join(base,input) |
| Upload inseguro | Part/save | Multer | FileStorage.save |
| Open Redirect | sendRedirect | res.redirect | flask.redirect |
| Control de acceso | HttpSession | req.user | flask.session |

## Qué debe demostrar una receta genérica

Una receta aprobada no debe depender de:

- nombre exacto del archivo;
- nombre de clase o función;
- ruta del endpoint;
- nombre de variable;
- número de línea;
- framework específico salvo cuando la reparación requiera un adaptador tecnológico.

Debe almacenar dos niveles:

```
PATRÓN SEMÁNTICO
    ↓
ESTRATEGIA DE REMEDIACIÓN
    ↓
ADAPTADOR POR LENGUAJE / FRAMEWORK
```

Ejemplo conceptual:

```
SQL_INJECTION
    estrategia:
        consulta parametrizada

    Java/JDBC:
        PreparedStatement

    Node/sqlite3:
        placeholders + parámetros

    Python/sqlite3:
        ? + tuple de parámetros
```

## Secuencia de evaluación recomendada

1. Escanear `vulnport-java`.
2. Corregir y validar vulnerabilidades seleccionadas.
3. Guardar únicamente recetas que pasen el reescaneo.
4. Escanear `vulncommerce-node`.
5. Medir cuántas recetas Java fueron reconocidas y adaptadas.
6. Escanear `vulndesk-python`.
7. Medir nuevamente reutilización/adaptación.
8. Comparar falsos positivos, falsos negativos y regresiones.
9. Una receta sólo se considera generalizada si resuelve variantes no vistas previamente.
