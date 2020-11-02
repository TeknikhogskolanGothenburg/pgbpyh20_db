import sqlite3
from database import DB


class Customer:
    def __init__(self, id, first_name, last_name, email, phone):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone

    def __str__(self):
        return f"{self.first_name}, {self.last_name} has id {self.id} and email {self.email} and phone {self.phone}"

def insert_customer():
    with DB('customers.sql3') as connection:
        first_name = input("Enter a new first name: ")
        last_name = input("Enter a new last name: ")
        email = input("Enter a new email: ")
        phone = input("Enter a new phone number: ")
        cursor = connection.cursor()
        sql_str = """INSERT INTO customers 
            (FirstName, LastName, Email, Phone) 
            VALUES (?, ?, ?, ?)
        """
        cursor.execute(sql_str, (first_name, last_name, email, phone))
        connection.commit()


def show_all_customers():
    with DB('customers.sql3') as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM customers")
        rows = cursor.fetchall()
        for row in rows:
            customer = Customer(*row)
            print(customer)

def get_all_customers_as_objects():
    with DB('customers.sql3') as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM customers")
        rows = cursor.fetchall()
    return [Customer(*row) for row in rows]


def main():
    customers = get_all_customers_as_objects()
    for customer in customers:
        print(customer.first_name)





if __name__ == '__main__':
    main()
