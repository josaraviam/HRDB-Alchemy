from models.country import Country

def add_country(session, country_id, country_name, region_id):
    new_country = Country(country_id=country_id, country_name=country_name, region_id=region_id)
    session.add(new_country)
    session.commit()

def get_country(session, country_id):
    return session.query(Country).filter(Country.country_id == country_id).first()

def update_country(session, country_id, new_name=None, new_region_id=None):
    country = session.query(Country).filter(Country.country_id == country_id).first()
    if country:
        if new_name:
            country.country_name = new_name
        if new_region_id:
            country.region_id = new_region_id
        session.commit()

def delete_country(session, country_id):
    country = session.query(Country).filter(Country.country_id == country_id).first()
    if country:
        session.delete(country)
        session.commit()
