import unittest
from config.database import SessionLocal, init_db
from crud.region_crud import add_region, get_region, update_region, delete_region

class TestRegionCRUD(unittest.TestCase):

    def setUp(self):
        self.session = SessionLocal()
        init_db()

    def tearDown(self):
        self.session.close()

    def test_add_region(self):
        region = add_region(self.session, "Oceania")
        self.assertIsNotNone(region)
        self.assertEqual(region.region_name, "Oceania")

    def test_get_region(self):
        region = get_region(self.session, 1)
        self.assertIsNotNone(region)
        self.assertEqual(region.region_name, "Oceania")

    def test_update_region(self):
        update_region(self.session, 1, new_name="Oceanía")
        region = get_region(self.session, 1)
        self.assertEqual(region.region_name, "Oceanía")

    def test_delete_region(self):
        delete_region(self.session, 1)
        region = get_region(self.session, 1)
        self.assertIsNone(region)

if __name__ == "__main__":
    unittest.main()
