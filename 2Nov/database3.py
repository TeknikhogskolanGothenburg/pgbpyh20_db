from database import DB


def main():
    with DB('chinook.db') as connection:
        sql_str = """SELECT FirstName, LastName, City FROM customers
                        WHERE Country = ?
                          AND State = ?;
        """
        country = input("Enter a country: ")
        state = input("Enter a state in that country: ")
        cursor = connection.cursor()
        cursor.execute(sql_str, (country, state))
        rows = cursor.fetchall()
        for row in rows:
            print(row)


if __name__ == '__main__':
    main()
