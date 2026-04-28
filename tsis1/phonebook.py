import psycopg2
import csv  
import json
from config import load_config


def insert_contact_advanced(name, phone, email=None, birthday=None, group_name="Other"):
    sql = 'INSERT INTO phonebook (first_name, email, birthday) VALUES (%s, %s, %s) RETURNING contact_id'
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (name, email, birthday))
                contact_id = cur.fetchone()[0]
                cur.execute("CALL add_phone(%s, %s, %s)", (name, phone, 'mobile'))
                cur.execute("CALL move_to_group(%s, %s)", (name, group_name))
                conn.commit()
                print(f"contact {name} added")
    except Exception as e:
        print(f"error with {e}")


def search_contacts_console(query="", group=None, sort='name'):
    sql = "SELECT * FROM search_contacts_advanced(%s, %s, %s)"
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (query, group, sort))
                rows = cur.fetchall()
                return rows
    except Exception as e:
        print(f"error {e}")
        return []
    

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


def get_paginated_list(limit, offset):
    sql = 'SELECT * FROM get_phonebook_paginated(%s, %s)'
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (limit, offset))
                return cur.fetchall()
    except Exception as e:
        print(f"error with {e}")
        return []
    

def run_pagination_menu():
    limit = 5
    offset = 0
    while True:
        rows = get_paginated_list(limit, offset)
        
        print("\n" + "="*50)
        print(f"{'ID':<5} | {'name':<15} | {'group':<10} | {'numbers'}")
        print("-" * 50)
        
        if not rows:
            print("no data left")
        else:
            for r in rows:
                print(f"{r[0]:<5} | {r[1]:<15} | {r[3] or '---':<10} | {r[4] or '---'}")
        
        print("-" * 50)
        cmd = input("\n[n]ext page, [p]rev page, [q]uit to main menu: ").lower()
        
        if cmd == 'n':
            offset += limit
        elif cmd == 'p':
            offset = max(0, offset - limit)
        elif cmd == 'q':
            break


def export_to_json(filename='contacts.json'):
    config = load_config()
    try:
        results = search_contacts_console(query="") 
        
        data_to_export = []
        for row in results:
            data_to_export.append({
                "name": row[1],
                "email": row[2],
                "birthday": str(row[3]) if row[3] else None,
                "group": row[4],
                "phones": row[5].split(', ') if row[5] else []
            })
            
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data_to_export, f, indent=4, ensure_ascii=False)
        print(f"data exported to {filename}")
    except Exception as e:
        print(f"error with {e}")


def import_from_json(filename='contacts.json'):
    config = load_config()
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            contacts = json.load(f)
        for c in contacts:
            name = c['name']
            existing = search_contacts_console(query=name)
            match = next((r for r in existing if r[1] == name), None)
            
            if match:
                choice = input(f"contact '{name}' already exists. skip or override (s/o): ").lower()
                if choice == 's':
                    continue
                elif choice == 'o':
                    delete_contact(name) 
            
            insert_contact_advanced(name, c['phones'][0] if c['phones'] else '', c['email'], c['birthday'], c['group'])
            
        
            if len(c['phones']) > 1:
                for p in c['phones'][1:]:
                    with psycopg2.connect(**config) as conn:
                        with conn.cursor() as cur:
                            cur.execute("CALL add_phone(%s, %s, %s)", (name, p, 'mobile'))
                            conn.commit()
                            
        print("imported from file")
    except Exception as e:
        print(f"error with {e}")
    

def insert_from_csv_extended(filename):
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                with open(filename, 'r', encoding='utf-8') as f:
                    reader = csv.reader(f)
                    for row in reader:
                        name, phone, email, bday, group = row
                        insert_contact_advanced(name, phone, email, bday if bday else None, group)
        print("CSV imported")
    except Exception as e:
        print(f"error with {e}")


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
    while True: 
        print("\n--- phonebook application ---")
        print("1. add new contact")
        print("2. import contacts from CSV")
        print("3. search contact")
        print("4. update contact phone")
        print("5. delete contact")
        print("6. preview with pagination")
        print("7. filter by group")
        print("8. import from json")
        print("9. export to json")
        
        choice = input("\nchoose an option (1-9): ")
        
        if choice == '1':
            name = input("enter first name: ")
            tel = input("enter phone number: ")
            mail = input("enter email: ")
            bday = input("enter birthday: ")
            group = input("enter group name: ")
            insert_contact_advanced(name, tel, mail, bday, group)
        elif choice == '2':
            insert_from_csv_extended('contacts.csv')
        elif choice == '3':
            s = input("enter pattern to search: ")
            print("search by: 1. name; 2. birthday; 3. id")
            sortcho = input("enter number (1-3): ")
            sormap = {'1': 'name', '2': 'birthday', '3': 'id'}
            res = search_contacts_console(query=s, sort=sormap.get(sortcho, 'name'))
            print(res)
        elif choice == '4':
            name = input("enter contact name to update: ")
            new_tel = input("enter new phone number: ")
            update_contact(name, new_tel)
        elif choice == '5':
            name = input("enter name to delete: ")
            delete_contact(name)
        elif choice == '6':
            run_pagination_menu()
        elif choice == '7':
            g = input("enter group name: ")
            res = search_contacts_console(group=g)
            print(res)
        elif choice == '8':
            import_from_json()
        elif choice == '9':
            export_to_json()
        else:
            break
