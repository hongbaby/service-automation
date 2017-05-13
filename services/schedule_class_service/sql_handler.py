import pymssql

server = "CNS-ETDEVDB\INST1"
database = "Oboe"


def connect_sqlserver():
    conn = pymssql.connect(server=server, database=database)
    return conn


def execute_sql(sql):
    conn = connect_sqlserver()
    cur = conn.cursor()

    if cur:
        cur.execute(sql)
        execute_list = cur.fetchall()
        conn.close()
        return execute_list

    else:
        raise Exception("Connecting database failed.")
