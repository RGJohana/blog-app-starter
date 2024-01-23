# 😊 Objetivo inicial: Blog App Starter

Este repositorio sirve como un punto de partida para crear una aplicación de blog utilizando Django y Docker. Proporciona una estructura de proyecto básica con configuraciones predefinidas y un entorno Dockerizado para facilitar el desarrollo y la implementación.

# Blog App Starter 🚀

Este repositorio sirve como un punto de partida para crear una aplicación de blog utilizando Django y Docker. Proporciona una estructura de proyecto básica con configuraciones predefinidas y un entorno Dockerizado para facilitar el desarrollo y la implementación.

## Características 🌟

- ✅ Estructura de proyecto Django preconfigurada.
- ✅ Archivo `docker-compose.yml` para orquestar contenedores Docker.
- ✅ Configuración inicial para vistas y URL que muestran la página de inicio del blog.
- ✅ Documentación clara para configurar y ejecutar la aplicación.

## Cómo Usar 🛠️

1. **Clonar este repositorio:**
   ```bash
   git clone https://github.com/tu-usuario/blog-app-starter.git
Sigue las instrucciones detalladas en el archivo README para configurar el entorno y ejecutar la aplicación.

Personaliza y expande la aplicación según tus necesidades.

## Contribuciones 🤝
¡Las contribuciones son más que bienvenidas! Si encuentras mejoras o deseas agregar características adicionales, abre un problema o envía una solicitud de extracción.

## Notas 📝
Este proyecto está diseñado como un punto de partida para el desarrollo de aplicaciones de blog con Django y Docker.

## Pasos de Construcción 🛠️
**1. Crear un entorno virtual con**: 
    ```bash python -m virtualenv portfolio1```

**2.Activar el entorno virtual con:** ```\portfolio1\Scripts\activate``` 

**3.Lanzar el comando para construir el contenedor:** ```docker-compose build```

**4. Lanzar el comando para construir el contenedor:** ```docker-compose up```

**5.En otra terminal entrar al contenedor con el comando:** ```docker exec -i -t onepp_django bash```

**6.Llegar hasta la carpeta back_end con:** ```cd opt```
```cd back_end```

**7. Instalar los requerimientos:** ```pip install -r requirements.txt```

**8. En una tercera terminal entrar al contenedor para correr la app y poder visualizar el mensaje:**
```docker exec -i -t onepp_django bash```

**9. LLegar hasta la carpeta backend e instalar los requerimientos:** 
```cd opt/back_end```

```pip install -r requirements.txt```

**10. Ahora, podrás ver el mensaje:**
¡Hola, esta es la página principal del blog!

# **11. Detener la ejecución del contenedor y servidor🛑**
Tenemos que estar en la terminal que nos muestra los mensajes del servidor, tomada por el contenedor. Tan solo con el comando ctrl + c se detiene la ejecución de nuestro contenedor.

Una forma alternativa es con el siguiente comando en la terminal del host:

```$ docker stop prueba_django```

O también puede ser con docker-compose: Tenemos que estar en la carpeta que contiene el archivo docker-compose.yml y hacer:

```$ docker-compose down```
