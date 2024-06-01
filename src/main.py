import os

from dotenv import load_dotenv, find_dotenv

from src.domain.goalscorers import Author
from src.utils.conection import connect_to_mysql


def main():
    cnx = connect_to_mysql(attempts=3)

    if cnx and cnx.is_connected():

        with cnx.cursor() as cursor:

            result = cursor.execute("SELECT * FROM author LIMIT 5")

            rows = cursor.fetchall()

            for rows in rows:
                print(rows)


main()
