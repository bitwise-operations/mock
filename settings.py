import os

MYSQL_USER = os.environ.get("MYSQL_USER", 'root')
MYSQL_PASSWORD = os.environ.get("MYSQL_PASSWORD", 'secret')
MYSQL_HOST = os.environ.get("MYSQL_HOST", '0.0.0.0')
MYSQL_PORT = os.environ.get("MYSQL_PORT", 3306)
MYSQL_DATABASE = os.environ.get("MYSQL_DATABASE", 'mock_server')

DSN = f"mysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}"
