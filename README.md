# Repositorio para Despliegue y Algoritmos Evaluados
Este repositorio contiene todos los archivos necesarios para el despliegue de nuestra aplicación, así como también los algoritmos que hemos evaluado durante el desarrollo.

# Archivos de Despliegue
Dentro de la carpeta '/Server Aplication' encontrarás todos los archivos necesarios para desplegar nuestra aplicación en un entorno virtual con la libreria FLASK  para el despliegue.

# Algoritmos Evaluados
Dentro de Model for Predicting Diabetes.ipynb, se encuentran todos los algoritmos que hemos evaluado. 

# Requisitos para Desplegar el Entorno Virtual
Para desplegar el entorno virtual y utilizar los archivos proporcionados, necesitarás seguir estos pasos:

Instalación de Python: Asegúrate de tener instalado Python en tu sistema. Puedes descargarlo desde python.org si aún no lo tienes instalado.

Creación del Entorno Virtual: Se recomienda crear un entorno virtual para evitar conflictos entre las dependencias de diferentes proyectos. Puedes crear un entorno virtual utilizando la herramienta virtualenv. Instálala si no la tienes utilizando el siguiente comando:

#!/bin/bash

# 1. Instalación de Python
Asegúrate de tener instalado Python en tu sistema. Puedes descargarlo desde python.org si aún no lo tienes instalado.

# 2. Creación del Entorno Virtual
 Se recomienda crear un entorno virtual para evitar conflictos entre las dependencias de diferentes proyectos. Utilizaremos la herramienta virtualenv.

# Instala virtualenv si no lo tienes
pip install virtualenv

# Crea un nuevo entorno virtual
virtualenv venv

# Activa el entorno virtual
# En Windows
 venv\Scripts\activate
# En macOS y Linux
source venv/bin/activate

# 3. Instalación de Dependencias
 Con el entorno virtual activado, instala las dependencias necesarias.
pip install -r requirements.txt

Esto instalará todas las bibliotecas y herramientas necesarias para ejecutar nuestra aplicación y los algoritmos evaluados.

¡Una vez completados estos pasos, estarás listo para desplegar la aplicación!
