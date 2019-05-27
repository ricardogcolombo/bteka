import os
from dotenv import load_dotenv


load_dotenv()
ENV = os.getenv("PYTHON_ENV")

env_path = ".env"

DBPORT = os.getenv("DBPORT")


#  this enviroment values should be defined on your enviroment file
DBHOST = os.getenv("DB_HOST")
DBPORT = os.getenv("DB_PORT")
DBUSER = os.getenv("DB_USER")
DBPASS = os.getenv("DB_PASSWD")
DBNAME = str(os.getenv("DB_DATABASE"))
