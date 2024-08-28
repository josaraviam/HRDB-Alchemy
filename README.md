# BDD Avanzadas
## Human Resources ORM

Este proyecto es una aplicación ORM en Python utilizando SQLAlchemy para interactuar con una base de datos de recursos humanos.

### Características

- Implementación de operaciones CRUD para las tablas de `countries` y `regions`.
- Conexión a PostgreSQL utilizando variables de entorno.
- Pruebas unitarias para validar las operaciones CRUD.

### Requisitos

- Python 3.12
- PostgreSQL
- Paquetes Python: `SQLAlchemy`, `psycopg2-binary`, `python-dotenv`, `unittest`

### Configuración del Proyecto

1. Clona el repositorio.

2. Crea un archivo `.env` en la raíz del proyecto con tus credenciales de base de datos PostgreSQL:

   ```plaintext
   DB_USER=tu_usuario
   DB_PASSWORD=tu_contraseña
   DB_HOST=localhost
   DB_NAME=hr_database
   DB_PORT=5432

### Usar otra Base de Datos

Si decides usar una base de datos diferente a PostgreSQL, toma en cuenta que deberás cambiar el conector:

El conector de la base de datos es el que varía según el tipo de base de datos que utilices.
1. MySQL/MariaDB: mysql+pymysql://
2. SQLite: sqlite: ///path.db
3. SQL Server: mssql+pyodbc://
4. Oracle: oracle+cx_oracle://