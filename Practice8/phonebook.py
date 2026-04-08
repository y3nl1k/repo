import psycopg2
from config import load_config


def find_contacts(srch):
    sql = "SELECT * FROM get_contacts_by_pattern(%s)"
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (srch,))
                rows = cur.fetchall()
                if rows:
                    for row in rows:
                        print(f"name: {row[0]}, num: {row[1]}")
                else:
                    print("not found")
    except Exception as e:
        print(f"error with {e}")

def upsrt(upsname, upsphone):
    sql = "CALL upsert_contact(%s, %s)"
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (upsname, upsphone))
                conn.commit()
                print("upserted")
    except Exception as e:
        print(f"error: {e}")


def bulk(listname, listphone):
    sql = "CALL insert_many_contacts(%s, %s)"
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (listname, listphone))
                conn.commit()
                print(f"list of contacts added")
    except Exception as e:
        print(f"error {e}")
    
def pgnt(lim, offs):
    sql = "SELECT * FROM get_contacts_paginated(%s, %s)"
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:

            with conn.cursor() as cur:
                cur.execute(sql, (lim, offs))
                rows = cur.fetchall()
            
                for row in rows:
                    print(f"name: {row[0]}, num: {row[1]}")
    except Exception as e:
        print(f"finding error: {e}")

def delete_contact(contact):
    sql = "CALL delete_contact(%s)"
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (contact,))
                conn.commit()
                print(f"contact {contact} is deleted.")
    except Exception as e:
        print(f"del error: {e}")

if __name__ == '__main__':

    while True:

        print("\n--- phonebook application ---")
        print("1. search")
        print("2. update or insert a contact")
        print("3. insert a list of contacts")
        print("4. view paginated data")
        print("5. delete contact")
        print("any other symbol to leave")
        
        choice = input("\nchoose an option (1-5): ")
        
        if choice == '1':
            s = input("enter name or number part: ")
        
            find_contacts(s)
        elif choice == '2':
            name=input("enter name: ")
            pho=input("enter phone number: ")
            upsrt(name, pho)
        elif choice == '3':
            names = input("enter names: ").split()
            phones = input("enter numbers: ").split()
            bulk(names, phones)
        elif choice == '4':
            l = int(input("enter num of contacts in each page: "))
            o = int(input("enter the num where u eant to start at: "))
            pgnt(l, o)
        elif choice == '5':
            data = input("enter name or number to delete: ")
            delete_contact(data)
        else:
            break

