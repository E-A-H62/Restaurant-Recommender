# SEO PROJECT 1

## Authors:
Elena Hernandez and Bryson Turner

## Overview

Hello, in this project, we use the OPENAI API to post and request data in order to find restaurant recommendations.

## Libraries Used:

- MySQL
- Pandas
- SQLAlchemy
- OpenAI
- Unittest
- Coverage

## Code Explained

```python
import pandas as pd
import os
import sqlalchemy as db
from openai import OpenAI


# Retrieve the API key from the environment variable
my_api_key = os.getenv('OPENAI_KEY')


class Project:
    @staticmethod
    def store_db(
        data,
        db_url='sqlite:///data_base_name.db',
        table_name='table_name'
    ):
        df = pd.DataFrame.from_dict(data)
        engine = db.create_engine(db_url)
        df.to_sql(table_name, con=engine, if_exists='replace', index=False)

        with engine.connect() as connection:
            query_result = connection.execute(
                db.text("SELECT * FROM table_name;")
            ).fetchall()
            return pd.DataFrame(query_result)

    def generate_chat(api_key):
        # Create an OpenAI client using the provided API key
        client = OpenAI(api_key=api_key)

        # Specify the model to use and the messages to send
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "You can create organized datatables."
                },
                {"role": "user", "content": (
                    "Generate a table with 10 items. "
                    "The data contains name, age, birthday, "
                    "and nationality."
                )}
            ]
        )

        # Extract and return the content from the API response
        chat_response = completion.choices[0].message.content
        return chat_response

