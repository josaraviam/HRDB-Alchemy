from config.database import SessionLocal, init_db
from crud.country_crud import add_country, get_country, update_country, delete_country

def main():
    # Inicializar la base de datos
    init_db()

    # Crear una nueva sesión
    session = SessionLocal()

    # Agregar un país
    add_country(session, "MX", "Mexico", 2)

    # Consultar un país
    country = get_country(session, "MX")
    print(f"Country: {country.country_name}, Region ID: {country.region_id}")

    # Actualizar un país
    update_country(session, "MX", new_name="México", new_region_id=3)

    # Eliminar un país
    delete_country(session, "MX")

    # Cerrar la sesión
    session.close()

if __name__ == "__main__":
    main()
