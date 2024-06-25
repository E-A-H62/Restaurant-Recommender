import pandas as pd
import sqlalchemy as db
import os
import openai
from openai import OpenAI

# Retrieve the API key from the environment variable
my_api_key = os.getenv('OPENAI_KEY')

#TEST
#print(my_api_key)

print(os.getenv('OPENAI_KEY'))

# Create an OpenAPI client using the key from our environment variable
client = OpenAI(
    api_key=my_api_key,
)



# Specify the model to use and the messages to send
completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You can create organized datatables."},
        {"role": "user", "content": "Generate a table with 10 items. The data contains name, age, birthday, and nationality."}
    ]
)
#print(completion.choices[0].message.content) 
chat_response = completion.choices[0].message.content
fake = users = [
  {"id": 1, "name": "Jane Doe", "email": "janedoe@email.com"},
  {"id": 2, "name": "John Doe", "email": "johndoe@email.com"}
]

# Store data in a MySQL database
df = pd.DataFrame.from_dict(fake)
engine = db.create_engine('sqlite:///data_base_name.db')

# Create table if it doesn't exist
df.to_sql('table_name', con=engine, if_exists='replace', index=False)

# Query and manipulate the database
with engine.connect() as connection:
  query_result = connection.execute(db.text("SELECT * FROM table_name;")).fetchall()
  print(pd.DataFrame(query_result))
