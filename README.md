# MULTIPLE DRONES SIMULATOR

# Instalación
1. Crear una carpeta que sirva como workspace de ROS2
2. Hacer un clone dentro del workspace
3. Cambiar el nombre de la carpeta por 'src'
4. Hacer 'colcon build' desde la carpeta de workspace

##  Configurar el dron
En la carpeta 'src/config' crear un archivo 'drone_X.yaml' donde X sea el número del dron y dentro escribir:
```
\drone_X:
  fp:
    ros__parameters:
      max_speed: A
      max_acc: B
```
Donde A y B sean floats que representen la velocidad máxima y la aceleración máxima respectivamente.

## Crear waypoints para un dron
En la carpeta 'src/waypoints' crear un archivo 'drone_X.yaml' donde X sea el número del dron y dentro escribir:
```
\drone_X:
  simulator:
    ros__parameters:
      waypoints: ['Ax;By;Cz', 'Ba;By;Bz', 'Cx;Cy;Cz', ...]
```
Donde waypoints es un vector de strings en que cada string contiene floats separados por ';'. Estos puntos 3D se usarán para crear la ruta del dron.
