

<!-- local-development:start -->
# Desarrollo local

Puedes abrir este repositorio en VS Code, Antigravity o Sublime Text. El compilador y los servicios necesarios dependen del componente indicado abajo.

## Python

Crea un entorno por aplicación desde PyCharm o la CLI. Python 3.12 es el punto inicial de compatibilidad; no se presume que todo el código o sus paquetes antiguos ya lo soporten.

```powershell
py -3.12 -m venv .venv
```

No se detectó un archivo requirements. Hay que identificar los imports y declarar las dependencias antes de instalarlas.

## Archivos ignorados

`.gitignore` excluye credenciales locales, estado del editor y salidas de las herramientas detectadas. No deja de versionar archivos que ya estaban en Git. Los manifiestos, archivos de bloqueo, recursos fuente y scripts de esquema forman parte del código.
<!-- local-development:end -->

<!-- improvements-20261119:start -->
## Mejoras y verificación funcional (2026-11-19)

- **Mejoras aplicadas:** Compatibilidad multiplataforma Windows/Linux en `02_environ.py` (`HOME`/`USERPROFILE`), ruta robusta relativa al script en `03_read_file.py` e implementación completa del conteo de fallos de autenticación en `05_cout_users.py`.
- **Pruebas ejecutadas:** `python -m unittest discover -s tests -v` (2/2 pruebas aprobadas ejecutando los 5 scripts Python).
<!-- improvements-20261119:end -->
