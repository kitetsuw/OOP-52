import sqlite3

connect = sqlite3.connect('users.db')
cursor = connect.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR (30) NOT NULL,
        age INTEGER NOT NULL,
        hobby TEXT
    )
''')
connect.commit()

# Create
def add_user(name, age, hobby):
    cursor.execute(
        'INSERT INTO users(name, age, hobby) VALUES (?, ?, ?)',
        (name, age, hobby)
    )
    connect.commit()
    print(f"Пользователь {name} добавлен!")

add_user('Danil', 23, 'Плавать')
add_user('OLEG', 24, 'Плавать')
add_user('Vika', 25, 'Плавать')
add_user('IGOR', 24, 'Плавать')

# Read
def get_all_users():
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()

    if users:
        print("Список всех пользователей:")
        for i in users:
            print(f"ID: {i[0]}, NAME: {i[1]}, AGE: {i[2]}, HOBBY: {i[3]}")
    else:
        print('Пользователей нет!')

get_all_users()
print("Пользователь с айди №3")
# update
def update_user(conn, user_id, name=None, age=None, hobby=None):
    """Обновляет данные пользователя по id"""
    query = 'UPDATE users SET '
    params = []
    
    if name:
        query += 'name = ?, '
        params.append(name)
    if age:
        query += 'age = ?, '
        params.append(age)
    if hobby:
        query += 'hobby = ?, '
        params.append(hobby)
    
    query = query.rstrip(', ') + ' WHERE id = ?;'
    params.append(user_id)
    
    cursor.execute(query, params)
    conn.commit()
    print("Данные пользователя обновлены")


def get_user_by_id(conn, user_id):
    query = 'SELECT id, name, age, hobby FROM users WHERE id = ?;'
    cursor.execute(query, (user_id,))
    user = cursor.fetchone()
    if user:
        print(f"ID: {user[0]}, NAME: {user[1]}, AGE: {user[2]}, HOBBY: {user[3]}")
    else:
        print("Пользователь не найден")


get_user_by_id(connect, 3)
update_user(connect, 3, name="SIMON")
get_all_users()
