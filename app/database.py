import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL

load_dotenv()

def get_engine():
    url = URL.create(
        "mysql+pymysql",
        username=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        host=os.getenv("MYSQL_HOST", "localhost"),
        port=int(os.getenv("MYSQL_PORT", "3306")),
        database=os.getenv("MYSQL_DATABASE", "querypilot"),
    )
    return create_engine(url, pool_pre_ping=True)

def get_schema(engine):
    query = text("SELECT TABLE_NAME, COLUMN_NAME, DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = DATABASE() ORDER BY TABLE_NAME, ORDINAL_POSITION")
    with engine.connect() as connection:
        rows = connection.execute(query).fetchall()
    schema = {}
    for table_name, column_name, data_type in rows:
        schema.setdefault(table_name, []).append(str(column_name) + " (" + str(data_type) + ")")
    return "\n".join(table + ": " + ", ".join(columns) for table, columns in schema.items())

def execute_query(engine, sql):
    with engine.connect() as connection:
        result = connection.execute(text(sql))
        return [dict(row._mapping) for row in result.fetchall()]
