CREATE OR REPLACE PROCEDURE upsert_contact(p_name VARCHAR, p_phone VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    
    IF EXISTS (SELECT 1 FROM phonebook WHERE first_name = p_name) THEN
        UPDATE phonebook SET phone_number = p_phone WHERE first_name = p_name;
    ELSE
        INSERT INTO phonebook(first_name, phone_number) VALUES(p_name, p_phone);
    END IF;
END;
$$;

CREATE OR REPLACE PROCEDURE insert_many_contacts(
    p_names VARCHAR[], 
    p_phones VARCHAR[]
)
LANGUAGE plpgsql AS $$
DECLARE
    i INT;
BEGIN
    FOR i IN 1 .. array_upper(p_names, 1) LOOP
       
        IF length(p_phones[i]) >= 5 THEN
            INSERT INTO phonebook(first_name, phone_number) 
            VALUES(p_names[i], p_phones[i]);
        ELSE
            RAISE NOTICE 'invalid phone for: %', p_names[i];
        END IF;
    END LOOP;
END;
$$;

CREATE OR REPLACE PROCEDURE delete_contact(p_data VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    DELETE FROM phonebook 
    WHERE first_name = p_data OR phone_number = p_data;
END;
$$;

CALL insert_many_contacts('{"name1", "name2", "name3"}', '{"12345", "23456", "34567"}');

CALL upsert_contact('nameee', '1287654');

CALL delete_contact('nameee');