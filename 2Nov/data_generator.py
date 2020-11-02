from database import DB
import random

def create_persons_table():
    with DB('persons_interests.sql3') as connection:
        sql_str = """CREATE TABLE IF NOT EXISTS persons (
            PersonId INTEGER PRIMARY KEY AUTOINCREMENT,
            FirstName VARCHAR(100),
            LastName VARCHAR(100)
        )"""
        cursor = connection.cursor()
        cursor.execute(sql_str)
        connection.commit()

def insert_persons_data():
    female_names = [line.strip() for line in open('female_first.txt', encoding='utf-8').readlines()]
    male_names = [line.strip() for line in open('male_first.txt', encoding='utf-8').readlines()]
    last_names = [line.strip() for line in open('lastnames.txt', encoding='utf-8').readlines()]
    with DB('persons_interests.sql3') as connection:
        for _ in range(1000):
            if random.randrange(0, 2) == 0:
                first_name = random.choice(female_names)
            else:
                first_name = random.choice(male_names)
            last_name = random.choice(last_names)
            sql_str = """INSERT INTO persons (FirstName, LastName) VALUES (?, ?) 
            """
            cursor = connection.cursor()
            cursor.execute(sql_str, (first_name, last_name))
            connection.commit()


def create_interests_table():
    with DB('persons_interests.sql3') as connection:
        sql_str = """CREATE TABLE IF NOT EXISTS interests (
            InterestId INTEGER PRIMARY KEY AUTOINCREMENT,
            Name VARCHAR(100)
        )"""
        cursor = connection.cursor()
        cursor.execute(sql_str)
        connection.commit()

def insert_interests_data():
    hobbies = [line.strip().title() for line in open('hobbies.csv', encoding='utf-8').readlines()]
    with DB('persons_interests.sql3') as connection:
        for hobby in hobbies:
            sql_str = """INSERT INTO interests (Name) VALUES (?)"""
            cursor = connection.cursor()
            cursor.execute(sql_str, (hobby, ))
            connection.commit()


def create_persons_interests_table():
    with DB('persons_interests.sql3') as connection:
        sql_str = """CREATE TABLE IF NOT EXISTS persons_interests (
            PersonInterestId INTEGER PRIMARY KEY AUTOINCREMENT,
            PersonId INTEGER,
            InterestId INTEGER,
            FOREIGN KEY (PersonId) REFERENCES persons(PersonId),
            FOREIGN KEY (InterestId) REFERENCES interests(InterestId)
        )"""
        cursor = connection.cursor()
        cursor.execute(sql_str)
        connection.commit()

def match_person_and_interests():
    sql_get_persons = """SELECT PersonId FROM persons"""
    sql_get_interests = """SELECT InterestId FROM interests"""
    with DB('persons_interests.sql3') as connection:
        cursor = connection.cursor()
        cursor.execute(sql_get_persons)
        person_ids = [id[0] for id in cursor.fetchall()]
        cursor.execute(sql_get_interests)
        interest_ids = [id[0] for id in cursor.fetchall()]
        for person_id in person_ids:
            for _ in range(random.randrange(0, 5)):
                sql_person_interest = """INSERT INTO persons_interests (PersonId, InterestId) VALUES (?, ?)"""
                interest_id = random.choice(interest_ids)
                cursor.execute(sql_person_interest, (person_id, interest_id))
                connection.commit()

def main():
    #create_persons_table()
    #insert_persons_data()
    #create_interests_table()
    #create_persons_interests_table()
    #insert_interests_data()
    match_person_and_interests()

if __name__ == '__main__':
    main()
