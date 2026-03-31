import psycopg2
import csv
from config import load_config

def insert_contact(first_name, phone_number):
    sql = "INSERT INTO phonebook(first_name, phone_number) VALUES(%s, %s)"
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (first_name, phone_number))
                conn.commit()
                print(f"{first_name} added")
    except Exception as e:
        print(f"error with {e}")

def insert_from_csv(filename):
    
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                with open(filename, 'r', encoding='utf-8') as f:
                    reader = csv.reader(f)
                    for row in reader:
                        cur.execute(
                            "INSERT INTO phonebook(first_name, phone_number) VALUES(%s, %s) ON CONFLICT DO NOTHING",
                            (row[0], row[1])
                        )
                conn.commit()
                print("inserted")
    except Exception as e:
        print(f"CSV error: {e}")

if __name__ == '__main__':
     
    
    name = input("input name: ")
    phone = input("input number: ")
    insert_contact(name, phone)

def update_contact(name, new_phone):
    sql = "UPDATE phonebook SET phone_number = %s WHERE first_name = %s"
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (new_phone, name))
                conn.commit()
                print(f"number for {name} is changed to {new_phone}!")
    except Exception as e:
        print(f"upd error {e}")
    
def find_contacts(search_term):
    sql = "SELECT first_name, phone_number FROM phonebook WHERE first_name LIKE %s"
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (f'%{search_term}%',))
                rows = cur.fetchall()
                print(f"found: {len(rows)}")
                for row in rows:
                    print(f"name: {row[0]}, num: {row[1]}")
    except Exception as e:
        print(f"finding error: {e}")

def delete_contact(name):
    sql = "DELETE FROM phonebook WHERE first_name = %s"
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (name,))
                conn.commit()
                print(f"contact {name} is deleted.")
    except Exception as e:
        print(f"del error: {e}")

if __name__ == '__main__':
    print("\n--- phonebook application ---")
    print("1. add new contact")
    print("2. import contacts from CSV")
    print("3. search contact")
    print("4. update contact phone")
    print("5. delete contact")
    
    choice = input("\nchoose an option (1-5): ")
    
    if choice == '1':
        name = input("enter first name: ")
        tel = input("enter phone number: ")
        insert_contact(name, tel)
    elif choice == '2':
        insert_from_csv('contacts.csv')
    elif choice == '3':
        s = input("enter name to search: ")
        find_contacts(s)
    elif choice == '4':
        name = input("enter contact name to update: ")
        new_tel = input("enter new phone number: ")
        update_contact(name, new_tel)
    elif choice == '5':
        name = input("enter name to delete: ")
        delete_contact(name)

