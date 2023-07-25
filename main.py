import os

import psycopg2
from pgvector.psycopg2 import register_vector



connection_string  = os.environ['DB_CONNECTION_STRING']

conn = psycopg2.connect(connection_string)
cur = conn.cursor()

#install pgvector
cur.execute("CREATE EXTENSION IF NOT EXISTS vector");
conn.commit()

# Register the vector type with psycopg2
register_vector(conn)

def create_table():
   # Create table to store embeddings and metadata
   table_create_command = """
   CREATE TABLE embeddings (
               id bigserial primary key, 
               title text,
               url text,
               content text,
               tokens integer,
               embedding vector(1536)
               );
               """

   cur.execute(table_create_command)
   cur.close()
   conn.commit()

