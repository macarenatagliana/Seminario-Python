# Seminario-Python

Macarena Tagliana
18731/4

Requisitos
Para poder ejecutar el proyecto, necesitas tener instalado Python 3.x y Jupyter Notebook.


Jupyter Notebook
[pypi.org/projects/notebook](https://pypi.org/project/notebook/)
Es una herramienta muy util, que nos permite escribir texto y codigo, y ejecutarlo dentro del mismo, sin necesidad de acceder a una terminal. Es seguro, y ademas muestra los errores  de codigo en tiempo de ejecucion.

PyPI
pip install notebook

Para ejecutar notebook:
jupyter notebook

Esto abrira jupyter notebook en el navegador, donde se podra ver el codigo y ejecutarlo.

También, ejecutando la linea de comando

pip install -r requirements.txt

se pueden instalar las dependencias utilizadas en el proyecto. 


Venv

Venv es un módulo de Python que permite crear entornos virtuales aislados para cada proyecto. En este proyecto, lo utilizamos para poder trabajar con una version virtual de Python sin que interfiera con nuestro entorno de desarrollo cotidiano, a su vez que podemos instalar librerias independientes de cada proyecto.

comando de activacion
source venv/Scripts/activate

comando para desactivar
deactivate

#TIP PARA LA CORRECCION
Para poder correr el proyecto, en mi caso utilice VSCODE, que a la hora de probar los ejercicios tenia conflictos con Venv, lo cual requiere que tal vez sea necesario cerrar VsCode, volver a abrir, seleccionar venv como entorno de trabajo(si es q no lo selecciona automaticamente), luego ejecutar las lineas donde estan las rutas del proyecto, y luego finalmente, ejecutar el codigo correspondiente al ejercicio.