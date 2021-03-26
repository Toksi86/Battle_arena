import random
import psycopg2


class Thing:

    def __init__(self, name, protection, attack, health):
        self.name = name
        self.protection = protection
        self.attack = attack
        self.health = health

    def __repr__(self):
        return self.name

    @staticmethod
    def create_things():
        thing_objects_list = []

        con = psycopg2.connect(
            database="postgres",
            user="postgres",
            password="admin",
            host="127.0.0.1",
            port="5432"
        )
        cur = con.cursor()
        cur.execute("SELECT * FROM \"Things\"")

        rows = cur.fetchall()

        for row in rows:
            thing_objects_list.append(Thing(row[4], row[1], row[3], row[2]))

        con.close()

        return thing_objects_list


