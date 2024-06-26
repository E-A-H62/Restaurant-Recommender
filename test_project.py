import unittest
import pandas as pd
from unittest.mock import patch, MagicMock
from project import Project


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

    @patch('project.OpenAI')
    def test_generate_chat(self, mock_openai):
        # Mock the OpenAI client and its methods
        mock_client = MagicMock()
        mock_completion = MagicMock()
        mock_choice = MagicMock()
        mock_choice.message.content = 'mocked chat response'
        mock_completion.choices = [mock_choice]
        mock_client.chat.completions.create.return_value = mock_completion
        mock_openai.return_value = mock_client
        # Call the method under test
        response = Project.generate_chat('dummy_api_key')
        # Assertions
        self.assertEqual(response, 'mocked chat response')
        mock_openai.assert_called_once_with(api_key='dummy_api_key')
        mock_client.chat.completions.create.assert_called_once_with(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content":
                 "You can create organized datatables."},
                {"role": "user", "content": (
                    "Generate a table with 10 items. "
                    "The data contains name, age, birthday, "
                    "and nationality."
                )}
            ]
        )
