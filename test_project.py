import unittest
import pandas as pd
import sqlalchemy as db

from unittest.mock import MagicMock
from project import Project
from openai import OpenAI



class TestProject(unittest.TestCase):

    def test_store_db(self):
        fake_data = [
            {"id": 2, "name": "John Doe", "email": "johndoe@email.com"}
        ]

        # Use an in-memory SQLite database for testing
        db_url = 'sqlite:///:memory:'
        table_name = 'table_name'
        
        # Call the function to store data
        result_df = Project.store_db(fake_data, db_url, table_name)
        
        # Create the expected DataFrame
        expected_df = pd.DataFrame(fake_data)
        
        # Ensure the result DataFrame matches the expected DataFrame
        pd.testing.assert_frame_equal(result_df, expected_df)