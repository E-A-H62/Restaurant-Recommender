# Restaurant Recommender

## Contributing:

Elena Hernandez and Bryson Turner

## Table of Contents
- [Introduction](#introduction)
- [Usage](#usage)
- [Languages Used](#languages-used)
- [Frameworks and Libraries](#frameworks-and-libraries)
- [Code Explanations](#code-explanations)

## Introduction

Hello, in this project, we use the OpenAI API to post and request data to find restaurant recommendations. The tool leverages AI to provide personalized suggestions based on user input.

## Usage

This tool can be used to generate restaurant recommendations tailored to individual preferences. Users simply input their age and preferred cuisine, and the tool returns a list of top-rated restaurants that match their criteria.

Feel free to adjust the descriptions to better suit your project's specifics!

## Languages Used:

- **Python**: The primary programming language used for backend development and interacting with the OpenAI API.
- **HTML**: Used for structuring the web pages and forms.
- **CSS**:  Utilized for styling the web pages and enhancing the visual appearance.
- **JavaScript**: Employed for dynamic content and handling background image changes.

## Frameworks and Libraries

- **Flask**: A lightweight WSGI web application framework used to build the web application and handle routing.
- **Pandas**: A powerful data manipulation and analysis library used for managing and displaying data in tabular form.
- **SQLAlchemy**: An SQL toolkit and Object-Relational Mapping (ORM) library for Python, used to interact with the database.
- **OpenAI**: The OpenAI Python client library used to interact with the OpenAI API for generating restaurant recommendations.
- **Bootstrap**: A front-end framework used to style the web pages and ensure a responsive design.
- **Jinja2**: A templating engine for Python, used by Flask to render HTML templates dynamically.



## Code Explanations

```python
import pandas as pd
import os
import as db
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

