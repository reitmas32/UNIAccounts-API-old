# UNICA-ManagerAccounts-API
API to Manage UNICA System Accounts

### Informacion referente a migraciones

* **flask db init:** este comando inicializa el directorio de migraciones en el proyecto,creando una carpeta llamada migrations en la raíz del proyecto.

* **flask db migrate:** este comando detecta los cambios en los modelos y genera un archivo  de migración en la carpeta migrations.

* **flask db upgrade:** este comando aplica las migraciones pendientes al esquema de la base de datos, creando o actualizando las tablas según sea necesario.

### Informacion referente a los pre-commit

Si deseas contribuir al proyecto no olvidar pre-formatear tu codigo con ayuda de pre-commit, para ello deberas instalar las configuraciones escribiendo
el siguiente comando:

```bash
pre-commit install
```

Lo anterior hara que antes de que se cargue tu commit, verificara que tu codigo implementado cumpla con ciertos estandares y reglas.


Si deseas verificar todo el codigo

```bash
pre-commit run --all-files
```

Si deseas verificar todo el codigo

```bash
git commit -m "fix: lakdsljflaksjdlkf"  --no-verify
```

### Poner breakpoints


```python
import pudb; pudb.set_trace()
```

### Ejecutar proyecto en local

Se van a la carpeta src

```python
flask run
```

Si quieres especificar el puerto

```python
flask run --port=NUMERO_PUERTO
```

Si quieres que se carguen los cambios que haces instantaneamente

```python
flask run --port=NUMERO_PUERTO --debug
```







## Instructions by Run Server Flask

### **Create Env**
```bash
python -m venv venv
```

### **Activate Env**
```bash
#Linux bash/zsh
source venv/bin/activate

#Windows cmd
venv\Scripts\activate.bat

#Windows PowerShell
venv\Scripts\activate.ps1
```

### **Install dependencies**

```bash
pip3 install -r requirements.txt
```
### **Run Server App**

```bash
# Debug Mode
flask --app src/app --debug run

#Release Mode
flask --app src/app run
```

### **Recommended by Development Run use Docker Compose**
**Note:** Only need this commands by run project
Requirements
- [Docker Compose](https://docs.docker.com/compose/)
```bash
# Run and Build Docker Compose
docker-compose build
docker-compose up
```

### **Run Local DataBase With Docker**
```bash
# Run and Build Image with volumes
docker run -d -p 27017:27017 -v $ABS_ROUTE_OF_PROJECT/UNICA-ManagerAccounts-API/DB:/data/db --name database mongo
```

### **Run Server With Docker**

```bash
# Build Image
docker build -t unica-acounts-api .

#Run Image
docker run -it -p 7000:4000 unica-acounts-api
```

### **Endpoints Dev Status**
| Method |             Endpoint            | Status |
| ------ |:-------------------------------:| ------:|
| POST   |         /api/v1/signup/         |      ✓ |
| DELETE |         /api/v1/signup/         |      × |
| PUT    |         /api/v1/signin/         |      ✓ |
| PUT    |         /api/v1/signout/        |      ✓ |
| GET    |         /api/v1/signin/         |      ✓ |
| POST   | /api/v1/signup-change-password/ |      × |
| PUT    | /api/v1/signup-change-password/ |      × |
