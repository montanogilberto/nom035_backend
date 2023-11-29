import pymssql


def connection():
    # Server
    server = "nom035-dev-db-srv.database.windows.net"
    database = "nom035-db"
    username = "nom035admin"
    password = "ff7;z&tUGZiT9$)CzHoGjZUFN;RVfZeI"

    connection_string = {
        "server": server,
        "database": database,
        "user": username,
        "password": password,
        "autocommit": True,
    }

    return pymssql.connect(**connection_string)

