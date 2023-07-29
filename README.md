# UNIAccounts - Sistema Gestor de Cuentas

![Logo de mi proyecto](https://raw.githubusercontent.com/reitmas32/UNIAccounts-API-old/main/logo-uniaccounts.png)

Bienvenido/a al proyecto UNIAccounts, un Sistema Gestor de Cuentas desarrollado por UNIHacks.

## Descripción

UNIAccounts es una aplicación que proporciona una solución integral para la gestión de cuentas de usuario utilizando autenticación basada en JWT (JSON Web Tokens), Claves Públicas y Privadas, así como API-KEYs para el control de múltiples servicios. El objetivo principal de esta plataforma es ofrecer un sistema seguro y confiable para el registro, inicio de sesión y manejo de cuentas de usuarios en diferentes aplicaciones o servicios.

## Características

- **Autenticación con JWT:** UNIAccounts implementa un mecanismo de autenticación seguro y basado en JSON Web Tokens. Los usuarios pueden obtener un JWT válido al proporcionar sus credenciales y usarlo para acceder a recursos protegidos.

- **Claves Públicas y Privadas:** Para garantizar la seguridad de la información del usuario, UNIAccounts utiliza un sistema de criptografía de clave pública y privada. Esto permite la encriptación segura de datos sensibles y la verificación de la identidad del usuario mediante la firma digital.

- **API-KEYs para Control de Servicios:** Además de la autenticación JWT, UNIAccounts permite generar y utilizar API-KEYs para controlar el acceso a diferentes servicios asociados. Estas claves permiten una gestión más granular de los permisos de usuario para acceder a recursos específicos.

## Instalación y Uso

1. Clona el repositorio desde GitHub: `git clone https://github.com/reitmas32/UNIAccounts-API-old.git`
2. Crear entorno virtual: `python -m venv env/local`
3. Intalar las dependencias de la aplicacion `source venv/bin/activate`
4. Configura las variables de entorno necesarias para el funcionamiento de la aplicación, como las claves públicas y privadas, así como las credenciales para el acceso a la base de datos.
   ```bash
    ENVIRONMENT=
    SECRET_KEY_TOKEN=
    API_KEY=
    SMTP_USER=
    SMTP_PASSWORD=
    SQLALCHEMY_DATABASE_URI=
   ```
5. Hacer las migraciones de la DB
    
    * **flask db init:** This command initializes the migrations directory in the project, creating a folder called migrations in the root of the project.

    * **flask db migrate:** This command detects changes to the models and generates a migration file in the migrations folder.

    * **flask db upgrade:** This command applies the pending migrations to the database schema, creating or updating the tables as necessary.

- Ejecutar Servidor de la API
    ```
    cd src
    ```

    ```python
    flask run
    ```

    Especificar un Puerto

    ```python
    flask run --port=NUMERO_PUERTO
    ```

    Ejecutar el servidor en modo debug

    ```python
    flask run --port=NUMERO_PUERTO --debug
    ```

## Contribuciones

¡Agradecemos las contribuciones a este proyecto! Si deseas colaborar, asegúrate de seguir las directrices para contribuir al código y abrir solicitudes de extracción (Pull Requests). También, puedes reportar problemas o sugerir mejoras a través de las issues en el repositorio de GitHub.

## Contacto

Si tienes alguna pregunta o comentario sobre el proyecto, no dudes en ponerte en contacto con el programador a través de unihacks.mail@gmail.com.

¡Gracias por usar UNIAccounts! Esperamos que esta plataforma sea útil para tus necesidades de gestión de cuentas y autenticación segura.


### **Endpoints Dev Status**
| Method |             Endpoint            | Status |
| ------ |:-------------------------------:| ------:|
| POST   |         /api/v1/signup/         |      ✓ |
| DELETE |         /api/v1/signup/         |      × |
| PUT    |         /api/v1/signin/         |      ✓ |
| GET    |         /api/v1/signin/         |      ✓ |
| POST   | /api/v1/signup-change-password/ |      ✓ |
| PUT    | /api/v1/signup-change-password/ |      ✓ |
