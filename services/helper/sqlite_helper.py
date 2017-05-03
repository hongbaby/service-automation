import sqlite3


def _connect():
    conn = sqlite3.Connection("ec_db")
    return conn

def connect_db(func):
    """Connect to db, used as decorator. """
    def wrapper(*args, **kwargs):
        _connect()
        return func(*args, **kwargs)

    return wrapper

@connect_db
def execute_sql(sql, params=None):
    pass


def insert_row(table_name, *values):
    sql = "INNSERT INTO {} VALUES({})".format(table_name, ','.join(values))

