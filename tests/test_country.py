import unittest
from config.database import SessionLocal, init_db
from crud.country_crud import add_country, get_country, update_country, delete_country

class TestCountryCRUD(unittest.TestCase):

    def setUp(self):
        self.session = SessionLocal()
        init_db()

    def tearDown(self):
        self.session.close()

    def test_add_country(self):
        country = add_country(self.session, "FR", "France", 1)
        self.assertIsNotNone(country)
        self.assertEqual(country.country_id, "FR")

    def test_get_country(self):
        country = get_country(self.session, "FR")
        self.assertIsNotNone(country)
        self.assertEqual(country.country_name, "France")

    def test_update_country(self):
        update_country(self.session, "FR", new_name="Francia")
        country = get_country(self.session, "FR")
        self.assertEqual(country.country_name, "Francia")

    def test_delete_country(self):
        delete_country(self.session, "FR")
        country = get_country(self.session, "FR")
        self.assertIsNone(country)

if __name__ == "__main__":
    unittest.main()
