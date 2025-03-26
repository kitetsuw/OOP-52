import sqlite3

# A4 - Бумага
connect = sqlite3.connect('users7.db')

# Рука которая держит ручку
cursor = connect.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        name VARCHAR (30) NOT NULL,
        age INTEGER NOT NULL,
        hobby TEXT
    )
''')
connect.commit()

# CRUD - Create - Read - Update - Delete


# CREATE
def add_user(name, age, hobby):
    cursor.execute(
        'INSERT INTO users(name, age, hobby) VALUES (?,?,?)',
        (name, age, hobby)
    )
    connect.commit()
    print(f"Пользователь {name} добавлен!")



# add_user('DROP DATA BASE', 23, 'Плавать')
# add_user('OLEG', 23, 'Плавать')
# add_user('VIKA', 23, 'Плавать')
# add_user('IGOR', 23, 'Плавать')

# READ
def get_all_users():
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()

    if users:
        print("Список всех пользователей")
        for i in users:
            print(f"NAME: {i[0]}, AGE: {i[1]}, HOBBY: {i[2]}")
    else:
        print('Пользователей нету!!')

get_all_users()


# UPDATE
def update_users(rowid, hobby=None, name=None, age=None):
    cursor.execute('UPDATE users SET hobby = ? WHERE rowid = ?',
                   (hobby, rowid))
    connect.commit()
    print('Пользователь обновлен!!')


update_users(rowid=2, hobby="Спать!!")

# get_all_users()

# DELETE
def delete_user(name):
    cursor.execute('DELETE FROM users WHERE name = ?',
                   (name,))
    connect.commit()
    print('Пользователь удален!!')


# delete_user("VIKA")
get_all_users()
