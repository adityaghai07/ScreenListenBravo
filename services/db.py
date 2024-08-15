import psycopg2
from psycopg2 import sql
import os
import dotenv


dotenv.load_dotenv()


DATABASE_URL = os.getenv("DATABASE_URL")



def check_connection():
    try:
        conn = psycopg2.connect(DATABASE_URL)
        print("Connection to PostgreSQL established successfully.")
        conn.close()
    except Exception as e:
        print(f"Error connecting to PostgreSQL: {e}")



def create_company_table(db_params):
    try:
        conn = psycopg2.connect(db_params)
        cur = conn.cursor()

        create_table_query = sql.SQL("""
            CREATE TABLE IF NOT EXISTS company (
                company_name VARCHAR(255),
                description TEXT,
                technology_company BOOLEAN
            );
        """)

        cur.execute(create_table_query)
        conn.commit()
        print("Table 'company' created successfully.")
        
        cur.close()
        conn.close()
    except Exception as e:
        print(f"Error creating table 'company': {e}")


def insert_into_table(table_name, columns, values):
    try:
        conn = psycopg2.connect(DATABASE_URL)
        cur = conn.cursor()

        insert_query = sql.SQL("INSERT INTO {table_name} ({columns}) VALUES ({values})").format(
            table_name=sql.Identifier(table_name),
            columns=sql.SQL(", ").join(map(sql.Identifier, columns)),
            values=sql.SQL(", ").join(sql.Placeholder() * len(values))
        )

        cur.execute(insert_query, values)
        conn.commit()
        print(f"Data inserted successfully into table '{table_name}'.")
        
        cur.close()
        conn.close()
    except Exception as e:
        print(f"Error inserting data into table '{table_name}': {e}")


def print_table(db_params, table_name):
    try:
        conn = psycopg2.connect(db_params)
        cur = conn.cursor()

        select_query = sql.SQL("SELECT * FROM {table_name}").format(
            table_name=sql.Identifier(table_name)
        )

        cur.execute(select_query)
        rows = cur.fetchall()

        for row in rows:
            print(row)
        
        cur.close()
        conn.close()
    except Exception as e:
        print(f"Error printing table '{table_name}': {e}")




#Example Usage 1


# if __name__ == "__main__":
#     check_connection()

    # create_company_table(DATABASE_URL)

    # columns = ['company_name', 'description', 'technology_company']

    # values = ['Apple', 'Apple Inc. is an American multinational technology company that designs, manufactures, and markets consumer electronics, computer software, and online services.', True]


    # insert_into_table('company', columns, values)


    # print_table(DATABASE_URL, 'company')















