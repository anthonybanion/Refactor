# Guía de configuración del proyecto FlaskAPI

## 1. Clonar repositorio

```bash
git clone https://github.com/NikoTeLp90/FlaskAPi.git
```

---

## 2. Crear entorno virtual

### En Windows:

1. Ir a la raíz del proyecto (en este caso: `Api Flask/`):

```bash
cd "Api Flask"
```

2. Crear el entorno virtual:

```bash
python -m venv .venv
```

3. Activar el entorno:

```bash
cd .venv\Scripts
cmd.exe
activate
```

4. Volver a la raíz del proyecto:

```bash
cd ../..
```

---

## 3. Configurar la base de datos

Abrir el archivo `__init__.py` dentro de la carpeta `app` y configurar la conexión de SQLAlchemy.

### Ejemplo: Utilización de base local y remota a la vez

```python
# Base principal (local)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_local.sqlite'

# Base secundaria (remota)
# app.config['SQLALCHEMY_BINDS'] = {
#     'remota': 'postgresql://usuario:clave@host:puerto/dbname'
# }

```

---

## 4. Migraciones

### Para una sola base de datos:

```bash
flask db init
flask db migrate
flask db upgrade
```

### Para múltiples bases de datos:

```bash
flask db init
flask db migrate --multidb
flask db upgrade --multidb
```
