import psycopg2
from config import load_config

def create_tables():
    commands = (
        """
        CREATE TABLE IF NOT EXISTS phonebook (
            contact_id SERIAL PRIMARY KEY,
            first_name VARCHAR(50) NOT NULL,
            phone_number VARCHAR(20) UNIQUE NOT NULL
        )
        """,
    )
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                for command in commands:
                    cur.execute(command)
                conn.commit()
                print("table created")
    except Exception as error:
        print(error)

if __name__ == '__main__':
    create_tables()