# В базе 40 вещей, при запуске инициализации появится еще 40

import psycopg2
import random

con = psycopg2.connect(
    database="postgres",
    user="postgres",
    password="admin",
    host="127.0.0.1",
    port="5432"
)

print("Все хорошо, продолжай")

name_things = ['Gloves', 'Boots', 'Helmet', 'Cuirass', 'Ring']
for i in range(40):
    name = random.choice(name_things) + f' {i + 1}'
    protection = round(random.uniform(0.5, 1), 2)
    attack = random.randint(1, 4)
    health = random.randint(1, 4)

    cur = con.cursor()
    cur.execute(
        f"INSERT INTO \"Things\" (\"Name\", \"Protection\", \"Health\", \"Attack\") VALUES ('{name}', {protection} ,{health},{attack})"
    )

    con.commit()

print("Все получилось, вещи в базе")

con.close()
