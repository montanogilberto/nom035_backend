import pymssql


def connection():
    # Server
    #server = "nom035-dev-db-srv.database.windows.net"
    #database = "nom035-db"
    #username = "nom035admin"
    #password = "ff7;z&tUGZiT9$)CzHoGjZUFN;RVfZeI"

    server = "smartloans.database.windows.net"
    database = "smartloan"
    username = "adminsmart"
    password = "Admin#8605"

    connection_string = {
        "server": server,
        "database": database,
        "user": username,
        "password": password,
        "autocommit": True,
    }

    return pymssql.connect(**connection_string)

