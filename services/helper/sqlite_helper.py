import sqlite3

create_suspend_table_sql = """CREATE TABLE IF NOT EXISTS suspend_info (
  member_id       TEXT,
  suspend_date    TEXT,
  resume_date     TEXT,
  suspend_external_id TEXT
)"""


def execute_sql(sql):
    conn = sqlite3.Connection("echelper.db")
    conn.execute(sql)
    conn.commit()
    conn.close()




