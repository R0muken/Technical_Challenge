import unittest
from sqlalchemy import create_engine
from activity_dao import ActivityDatabase

TEST_DB_URL = 'sqlite:///test_activity_db.sqlite'


class TestActivityDatabase(unittest.TestCase):
    def setUp(self):
        self.engine = create_engine(TEST_DB_URL)
        self.db = ActivityDatabase(TEST_DB_URL)

    def tearDown(self):
        self.engine.dispose()

    def test_save_and_retrieve_activity(self):
        activity = {"activity_name": "Test Activity",
                    "type": "recreational",
                    "participants": 9,
                    "price": 20.4,
                    "link": "",
                    "key": '1234',
                    "accessibility": 0.5}

        self.db.save_activity(**activity)

        latest_activities = self.db.get_latest_activities(limit=1)

        self.assertTrue(latest_activities)
        latest_activity = latest_activities[0]

        self.assertEqual(latest_activity.activity_name, activity["activity_name"])
        self.assertEqual(latest_activity.type, activity["type"])
        self.assertEqual(latest_activity.participants, activity["participants"])
        self.assertEqual(latest_activity.price, activity["price"])
        self.assertEqual(latest_activity.link, activity["link"])
        self.assertEqual(latest_activity.key, activity["key"])
        self.assertEqual(latest_activity.accessibility, activity["accessibility"])

    def test_exception_handling(self):
        with self.assertRaises(Exception):
            ActivityDatabase("invalid_db_url")

