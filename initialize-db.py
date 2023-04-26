import psycopg2
from configparser import ConfigParser

def config(filename='database.ini', section='postgresql'):
    parser = ConfigParser()
    parser.read(filename) # read config from filename

    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception(f'Section {section} not found in the {filename} file')
    
    return db # return parsed options

try:
    params = config()
    conn = psycopg2.connect(**params)
    cur = conn.cursor()

    cur.execute("select column_name, data_type, character_maximum_length, column_default, is_nullable from INFORMATION_SCHEMA.COLUMNS where table_schema = 'public';")
    
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close
except (Exception, psycopg2.DatabaseError) as err:
    print(f'--{err}--')
finally:
    if conn is not None:
        conn.commit()
        conn.close()