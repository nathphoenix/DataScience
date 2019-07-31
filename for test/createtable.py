import psycopg2

try:
    con = psycopg2.connect(database="Learning", user="postgres", password="church75", host="localhost", port=5433)

    with con:

        cur = con.cursor()

        cur.execute("DROP TABLE IF EXISTS cars")
        cur.execute("CREATE TABLE Names(id SERIAL PRIMARY KEY, male_name VARCHAR(255))")
        cur.execute("INSERT INTO cars(name, price) VALUES('Audi', 52642)")
        cur.execute("INSERT INTO cars(name, price) VALUES('Mercedes', 57127)")
        cur.execute("INSERT INTO cars(name, price) VALUES('Skoda', 9000)")
        cur.execute("INSERT INTO cars(name, price) VALUES('Volvo', 29000)")
        cur.execute("INSERT INTO cars(name, price) VALUES('Bentley', 350000)")
        cur.execute("INSERT INTO cars(name, price) VALUES('Citroen', 21000)")
        cur.execute("INSERT INTO cars(name, price) VALUES('Hummer', 41400)")
        cur.execute("INSERT INTO cars(name, price) VALUES('Volkswagen', 21600)")

        print("Databse Table created successfully ")
except (Exception, psycopg2.Error) as error :
    print ("Unable to create databse table ", error)