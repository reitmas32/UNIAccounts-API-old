# Etapa de construcción
FROM python:3.9-alpine as builder

# Instalar paquetes necesarios para compilar las dependencias
RUN apk add --no-cache postgresql-dev build-base

# Establecer el directorio de trabajo en /app
WORKDIR /app

# Copiar los archivos de la aplicación a la imagen
COPY ./src /app
COPY ./requirements/production.txt /app/requirements.txt

# Instalar las dependencias de compilación
RUN pip install --no-cache-dir -r requirements.txt

# Etapa final
FROM python:3.9-alpine

# Instalar paquetes necesarios para ejecutar la aplicación
RUN apk add --no-cache libpq

# Copiar los archivos de la etapa de construcción a la imagen final
COPY --from=builder /usr/local /usr/local

# Establecer el directorio de trabajo en /app
WORKDIR /app

# Copiar los archivos de la aplicación a la imagen final
COPY ./src /app

RUN flask db init || true && \
    flask db migrate || true && \
    flask db upgrade || true

# Definir el puerto en el que se ejecutará la aplicación Flask
EXPOSE 5000

# Comando para ejecutar la aplicación Flask y especificar el archivo principal
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]