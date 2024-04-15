#Repositorio para Despliegue y Algoritmos Evaluados
Este repositorio contiene todos los archivos necesarios para el despliegue de nuestra aplicación, así como también los algoritmos que hemos evaluado durante el desarrollo.

#Archivos de Despliegue
Dentro de la carpeta '/Server Aplication' encontrarás todos los archivos necesarios para desplegar nuestra aplicación en diferentes entornos. Incluye scripts de configuración, archivos de Docker, y cualquier otro recurso relevante para el despliegue.

Algoritmos Evaluados
Dentro de Model for Predicting Diabetes.ipynb, se encuentran todos los algoritmos que hemos evaluado. 

Requisitos para Desplegar el Entorno Virtual
Para desplegar el entorno virtual y utilizar los archivos proporcionados, necesitarás seguir estos pasos:

Instalación de Python: Asegúrate de tener instalado Python en tu sistema. Puedes descargarlo desde python.org si aún no lo tienes instalado.

Creación del Entorno Virtual: Se recomienda crear un entorno virtual para evitar conflictos entre las dependencias de diferentes proyectos. Puedes crear un entorno virtual utilizando la herramienta virtualenv. Instálala si no la tienes utilizando el siguiente comando:

bash
Copy code
pip install virtualenv
Luego, dentro del directorio del proyecto, crea un nuevo entorno virtual ejecutando:

bash
Copy code
virtualenv venv
Activación del Entorno Virtual: Una vez creado el entorno virtual, actívalo utilizando el comando específico para tu sistema operativo:

En Windows:
bash
Copy code
venv\Scripts\activate
En macOS y Linux:
bash
Copy code
source venv/bin/activate
Instalación de Dependencias: Con el entorno virtual activado, instala las dependencias necesarias ejecutando:

bash
Copy code
pip install -r requirements.txt
Esto instalará todas las bibliotecas y herramientas necesarias para ejecutar nuestra aplicación y los algoritmos evaluados.

¡Una vez completados estos pasos, estarás listo para desplegar la aplicación!
