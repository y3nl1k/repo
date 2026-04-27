CREATE OR REPLACE FUNCTION get_contacts_by_pattern(p text)
RETURNS TABLE(first_name VARCHAR, phone_number VARCHAR) AS $$
BEGIN
    RETURN QUERY SELECT c.first_name, c.phone_number FROM phonebook c
                 WHERE c.first_name ILIKE '%' || p || '%'
                    OR c.phone_number ILIKE '%' || p || '%';
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION get_contacts_paginated(p_limit INT, p_offset INT)
RETURNS TABLE(first_name VARCHAR, phone_number VARCHAR) AS $$
BEGIN
    RETURN QUERY 
    SELECT c.first_name, c.phone_number 
    FROM phonebook c
    ORDER BY c.first_name
    LIMIT p_limit OFFSET p_offset;
END;
$$ LANGUAGE plpgsql;

SELECT * FROM get_contacts_paginated(10, 0);
SELECT * FROM get_contacts_by_pattern('name');