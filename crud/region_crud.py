from models.region import Region

def add_region(session, region_name):
    new_region = Region(region_name=region_name)
    session.add(new_region)
    session.commit()
    return new_region

def get_region(session, region_id):
    return session.query(Region).filter(Region.region_id == region_id).first()

def update_region(session, region_id, new_name=None):
    region = session.query(Region).filter(Region.region_id == region_id).first()
    if region and new_name:
        region.region_name = new_name
        session.commit()
    return region

def delete_region(session, region_id):
    region = session.query(Region).filter(Region.region_id == region_id).first()
    if region:
        session.delete(region)
        session.commit()
