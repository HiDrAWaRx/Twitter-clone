# Twitter clone

Realizado con 
- Python 3.11.4
- Django Rest Framework 3.14.0
- MongoDB

### Se modificó el proyecto del siguiente repositorio
https://github.com/initfve/Twitter-clone

### Objetivos
##### En la práctica remota, se espera que puedas:
- Resolver de forma independiente la configuración de un entorno de programación.
- Entender los problemas que surjan.
- Investigar y encontrar la solución previa a la práctica presencial.
- Realizar preguntas sobre ambigüedades de los pedidos.

### Actividades
- Levantar el proyecto.
- Integrar mongo
- Instalar el framework django rest-full e implementarla
- Hacer los siguientes endpoints:
    1. Login
    2. Sign up 🙉
    3. Crear un post 🙊
    4. Crear un comentario 🙈
    5. Encontrar cuántos emojis (los que están en el regex) hay en el texto (esto es para usar RegEx)
    6. Contar cuántas palabras de más de 5 caracteres hay
    7. Contar cuántas palabras están asociadas a sentimientos listados en esta colección: enojo, alegría, duda (miedo, incertidumbre).

### Levantar el proyecto
- Para levantar el proyecto se debe contar con el servicio de MongoDB corriendo en la pc.
- Se debe levantar el entorno virtual
    - (En Windows)
    1. Ir a la carpeta del proyecto y abrir la consola en dicho directorio
    2. Ejecutar la siguiente instrucción: 'venv\Scripts\activate.bat' para correr el entorno virtual
- Una vez corriendo en el entorno virtual, se deben ejecutar los siguientes comandos, en la misma consola, en orden para levantar el proyecto
    1. 'pip manage.py makemigrations'
    2. 'pip manage.py migrate'
    3. 'pip manage.py runserver'

### Endpoints
Los siguientes endpoints fueron probados con la aplicación POSTMAN, luego de levantar el proyecto en python con su entorno virtual.
Estos endpoints se encuentran en el archivo 'Tweets-clone.postman_collection.json' en la raiz del proyecto, para importar.

##### api/v1/signup/
Permite generar un nuevo registro de usuario para el sistema.
```
Payload:
{
    "username": "prueba1",
    "password": "patito2",
    "email": "prueba1@gmail.com",
    "first_name": "pruebanombre",
    "last_name": "pruebaapellido"
}
```
- Tanto el parámetro "username" como "email" se consideran como valores únicos, por lo que al intentar registrar más de una vez el mismo valor, indicará error de la base de datos.


##### api/v1/login/
Permite generar el token de autenticación (JWT) en base a las credenciales de un usuario registrado en el sistema.
```
Payload:
{
    "username": "prueba1",
    "password": "patito2",
}
```

##### >> Los siguientes endpoints necesitan el token JWT para la autenticación del usuario, obtenible en el anterior endpoint, login. El debe estar definido como Bearer Token en el encabezado de la petición. <<

##### api/v1/post/
- (GET) Permite listar la colección de post del sistema bajo el método HTTP "GET"
- (POST) Permite generar un registro nuevo en la colección de post del sistema bajo el método HTTP "POST". Cada post nuevo tiene un id numérico autoincremental para identificarlo:
```
Payload:
{
    "author": "prueba1",
    "content": "siento incertidumbre por la inseguridad, pero siempre alegre siempre positivo"
}
```

##### api/v1/emoji-post-count/
Permite conocer la cantidad de emojis que se encuentran en un post específico, identificado por su id numérico.
```
Payload:
{
    "post_id": 1
}
```

##### api/v1/word-post-count/
Permite conocer la cantidad de palabras de más de 5 caracteres que haya en un post específico, identificado por su id numérico.
```
Payload:
{
    "post_id": 1
}
```

##### api/v1/word-sentiment-post-count/
Permite conocer la cantidad de sentimientos, definidos en un diccionario local, y la cantidad de palabras relacionadas a cada sentimiento que haya en un post específico, identificado por su id numérico.
```
Payload:
{
    "post_id": 1
}
```

Diccionario de sentimientos con palabras relacionadas a cada uno:
```
sentiment_words = {
    'enojo': ['enojo', 'rabia', 'frustración', 'frustrado'],
    'alegría': ['alegría', 'alegre', 'felicidad', 'entusiasmo'],
    'duda': ['miedo', 'incertidumbre', 'preocupación', 'inseguridad']
}
```
 
### TODO
- [ ] Indicar con mayor precisión cuál es el problema que desencadenó el error.
- [ ] Refactorizar lógica de las funciones propias de cada endpoint, para separar en distintos archivos organizados en base a los modelos para evitar que todo esté en el archivo de views.py




