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

## Code Explained

```python
import pandas as pd
import sqlalchemy as db
import os
import openai

my_api_key = os.getenv('OPENAI_KEY')

print(os.getenv('OPENAI_KEY'))

client = openai.OpenAI(
    api_key=my_api_key,
)

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You can create organized datatables."},
        {"role": "user", "content": "Generate a table with 10 items. The data contains name, age, birthday, and nationality."}
    ]
)

# print(completion.choices[0].message.content) 
chat_response = completion.choices[0].message.content
fake = users = [
  {"id": 1, "name": "Jane Doe", "email": "janedoe@email.com"},
  {"id": 2, "name": "John Doe", "email": "johndoe@email.com"}
]

df = pd.DataFrame.from_dict(fake)
engine = db.create_engine('sqlite:///data_base_name.db')

df.to_sql('table_name', con=engine, if_exists='replace', index=False)

with engine.connect() as connection:
  query_result = connection.execute(db.text("SELECT * FROM table_name;")).fetchall()
  print(pd.DataFrame(query_result))

