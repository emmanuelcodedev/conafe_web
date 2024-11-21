Recomendación Adicional:

Se recomienda usar un entorno virtual para gestionar las dependencias de manera aislada.
Instalación y Configuración

Sigue los siguientes pasos para configurar el proyecto en tu máquina local.
Clonar el Repositorio

Clona este repositorio en tu máquina local usando Git. Abre la terminal y ejecuta:

git clone https://github.com/<TU-USUARIO>/<TU-REPOSITORIO>.git
cd <nombre-del-repositorio>

Crear y Activar un Entorno Virtual

Para evitar conflictos con otras dependencias de Python, es recomendable usar un entorno virtual.

    En Linux/macOS:

python3 -m venv env
source env/bin/activate

En Windows:

    python -m venv env
    .\env\Scripts\activate

Cuando el entorno virtual esté activado, verás el nombre del entorno entre paréntesis, por ejemplo: (env).
Instalar las Dependencias

Con el entorno virtual activado, instala las dependencias necesarias para el proyecto usando pip:

pip install -r requirements.txt

Esto instalará todos los paquetes listados en el archivo requirements.txt, que generalmente incluye Django y otras dependencias necesarias
Migraciones de Base de Datos

Django necesita crear las tablas de la base de datos antes de que puedas usar la aplicación. Para hacerlo, ejecuta las migraciones:

python manage.py migrate

Este comando creará las tablas necesarias en la base de datos, basándose en las definiciones de los modelos de Django.
Ejecutar el Servidor de Desarrollo

Una vez que todo esté configurado, puedes ejecutar el servidor de desarrollo de Django:

python manage.py runserver

El servidor se iniciará en el puerto 8000 por defecto. Accede a la aplicación desde tu navegador:

http://127.0.0.1:8000/




