from getpass import getpass
from mysql.connector import connect, Error

try:
    with connect(
        host="localhost",
        user="root",
        password='root',
    ) as connection:
        databases = []
        cursor = connection.cursor()
        show_db_query = "SHOW DATABASES"
        cursor.execute(show_db_query)
        databases = databases + [db[0] for db in cursor]
        if 'information_schema' in databases: databases.remove('information_schema');
        if 'wfo_master' in databases: databases.remove('wfo_master');
        if 'wfo_default' in databases: databases.remove('wfo_default');
        if 'sys' in databases: databases.remove('sys');
        if 'mysql' in databases: databases.remove('mysql');
        if 'performance_schema' in databases: databases.remove('performance_schema');
        filteredDb = [db for db in databases if not db.startswith('perm')]
        print('Cleaning up temporary tenant databases')
        print(filteredDb);

        for db in filteredDb:
            cursor.execute("DROP DATABASE " + db)
except Error as e:
    print(e)
