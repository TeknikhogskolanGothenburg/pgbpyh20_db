from database import DB


def main():
    with DB('customers.sql3') as connection:
        sql_str = """CREATE TABLE orders (
            OrderId INTEGER PRIMARY KEY AUTOINCREMENT,
            OrderDate DATE,
            CustomerId INTEGER
        )"""
        cursor = connection.cursor()
        cursor.execute(sql_str)
        connection.commit()

if __name__ == '__main__':
    main()
