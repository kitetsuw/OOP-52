import sqlite3

# A4 - Бумага
connect = sqlite3.connect('users_8_2.db')

# Рука которая держит ручку
cursor = connect.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR (30) NOT NULL,
        age INTEGER NOT NULL,
        hobby TEXT
    )
''')

cursor.execute("""
    CREATE TABLE IF NOT EXISTS grades (
        grade_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        subject VARCHAR (100) NOT NULL,
        grade INTEGER NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users(user_id)
    )
               """)

connect.commit()


def add_user(name, age, hobby=""):
    cursor.execute('INSERT INTO users(name, age, hobby) VALUES (?, ?, ?)', (name, age, hobby))
    connect.commit()
    print(f"Пользователь {name} добавлен")


add_user('Илья Муромец', 25, 'фехтование')
add_user('John Doe1', 25, 'плавание')
add_user('John Doe2', 27, 'шахматы')
add_user('John Doe3', 28, 'чтение')
add_user('John Doe99', 35, 'шахматы')
add_user('John Doe88', 33, 'чтение')


def add_grade(user_id, subject, grade):
    cursor.execute('INSERT INTO grades (user_id, subject, grade) VALUES (?,?,?)',
                   (user_id, subject, grade))

    connect.commit()


add_grade(5, "Алгебра", 2)
add_grade(5, "Геометрия", 3)
add_grade(5, "Физика", 5)


def delete_user_by_id(id):
    cursor.execute('DELETE FROM users WHERE user_id = ?', (id,))
    connect.commit()
    print("Пользователь удален")
delete_user_by_id(2)

def create_users_grades_view():
    cursor.execute('''
        CREATE VIEW IF NOT EXISTS users_grade AS
        SELECT 
            users.user_id, 
            users.name, 
            users.age, 
            users.hobby, 
            grades.subject, 
            grades.grade
        FROM users
        JOIN grades ON users.user_id = grades.user_id
    ''')
    connect.commit()

def get_young_users():
    cursor.execute('SELECT * FROM users_grade')
    for row in cursor.fetchall():
        print(row)

# Создание представления
create_users_grades_view()

# Проверка
get_young_users()
