Conafe Web

    Una plataforma desarrollada en Django para la gestión de empleados, coordinadores y módulos de Conafe.

Este proyecto tiene como objetivo facilitar la gestión interna y la administración de recursos mediante una interfaz web amigable y escalable.
📋 Requisitos Previos

Antes de ejecutar este proyecto, asegúrate de tener instalados los siguientes componentes:

    Python 3.8 o superior
    Virtualenv (opcional, pero recomendado para manejar entornos virtuales)
    Git (para clonar el repositorio, si aplica)
    Pip (gestor de paquetes para Python)

🚀 Instalación y Configuración

Sigue los pasos a continuación para configurar y ejecutar el proyecto en tu máquina local.
1. Clonar el repositorio

Usa el siguiente comando para clonar el proyecto en tu máquina local:

git clone https://github.com/<TU-USUARIO>/<TU-REPOSITORIO>.git
cd conafe_web

2. Crear y activar un entorno virtual

Se recomienda usar un entorno virtual para aislar las dependencias del proyecto:

En Linux/macOS:

python3 -m venv env
source env/bin/activate

En Windows:

python -m venv env
env\Scripts\activate

3. Instalar las dependencias

Instala las dependencias listadas en requirements.txt:

pip install -r requirements.txt

4. Configurar las variables de entorno

Configura las variables de entorno necesarias, incluyendo la configuración de Django:

export DJANGO_SETTINGS_MODULE=web_conafe.settings

En Windows:

set DJANGO_SETTINGS_MODULE=web_conafe.settings

5. Realizar las migraciones de base de datos

Configura la base de datos ejecutando las migraciones:

python manage.py migrate

6. Ejecutar el servidor

Inicia el servidor de desarrollo:

python manage.py runserver

Accede a la aplicación en tu navegador en: http://127.0.0.1:8000.
🛠️ Tecnologías Utilizadas

    Python
    Django
    HTML/CSS
    JavaScript
    Bootstrap (opcional, si lo usaste para el diseño del front-end)

🤝 Cómo Contribuir

Si deseas contribuir a este proyecto, sigue estos pasos:

    Haz un fork del repositorio.
    Crea una nueva rama (git checkout -b feature/nueva-funcionalidad).
    Realiza los cambios necesarios y haz un commit (git commit -m "Descripción de los cambios").
    Envía los cambios a tu fork (git push origin feature/nueva-funcionalidad).
    Abre un Pull Request en este repositorio.

 Asegúrate de activar el entorno virtual con:

source env/bin/activate
