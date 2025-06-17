# StockMiMuj

Este repositorio contiene el Sistema de Stock de la Dirección de Compras

## Requerimientos

- Python 3.10.10

- asgiref==3.5.1

- Django==4.0.4

- django-extensions==3.1.5

- pydotplus==2.0.2

- pyparsing==3.0.9

- sqlparse==0.4.2

- tzdata==2022.1

---

## Clonacion del Repositorio

##### _SSH_

````bash

git@github.com:isfdytdos210/ministerio.git```

Recuerde generar las llaves publicas y privadas ssh si utiliza este metodo.

##### HTTPS

```bash
git clone https://github.com/isfdytdos210/Sistema_De_Gestion_De_Stock.git

````

##### Branches

El repositorio contiene 2 ramas, main y develop. tenga cuidado!

---

## Instalación

##### _Entorno Virtual_

Para la creacion del entorno virtual usaremos el siguiente comando

```bash
pip -m venv "nombre del entorno virtual"
```

##### _Activacion entorno_

```bash
source "nombre_del_entorno"/bin/activate
```

Para la instalacion de los paquetes necesarios tan solo usaremos pip apuntando al requirements.txt

##### _Instalacion paquetes_

```bash
pip install -r requirements.txt
```

Al terminar ya tendremos instalado django y demas paquetes necesarios.

##### Creacion de migraciones

Las migraciones son como registros de cambios que se realizaron en los modelos, el orm detecta los cambios en los modelos y los refleja en las migraciones. para lanzarlo usaremos el siguiente comando

```bash
python3 manage.py makemigrations
```

##### _Reflejar las migraciones en la base de dato_

```bash
python manage.py migrate
```

Con este comando generamos las tablas que dictan las migraciones en la base de datos.

---

## Creacion de una cuenta SuperUsuario

Si todo salio bien, deberiamos crear un superusuario para empezar a usar el sistema con el siguiente comando

```bash
python manage.py createsuperuser
```

---
