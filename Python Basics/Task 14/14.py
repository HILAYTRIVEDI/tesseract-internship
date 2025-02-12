import sqlite3
import csv

# Connect to SQLite database file example.db
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    age INTEGER NOT NULL)''')

# Insert records
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('Alice', 30))
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('Bob', 25))
conn.commit()

# Retrieve and display all records
cursor.execute("SELECT * FROM users")
print("All Records:", cursor.fetchall())

# Update a specific record
cursor.execute("UPDATE users SET age = ? WHERE name = ?", (35, 'Alice'))
conn.commit()

# Display after update
cursor.execute("SELECT * FROM users")
print("After Update:", cursor.fetchall())

# Delete a record
cursor.execute("DELETE FROM users WHERE name = ?", ('Bob',))
conn.commit()

# Display after deletion
cursor.execute("SELECT * FROM users")
print("After Deletion:", cursor.fetchall())

# Search for a record based on user input
def search_user(name):
    cursor.execute("SELECT * FROM users WHERE name = ?", (name,))
    result = cursor.fetchall()
    if result:
        print(f"Search Results for {name}:", result)
    else:
        print(f"No records found for {name}")

search_user('Alice')
search_user('Charlie')

# Read data from CSV and insert into database
with open('users.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['name', 'age'])
    writer.writerow(['Charlie', 28])
    writer.writerow(['Diana', 32])

with open('users.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (row['name'], row['age']))
conn.commit()

# Display after CSV insert
cursor.execute("SELECT * FROM users")
print("After CSV Insert:", cursor.fetchall())

# Demonstrate transactions with commit and rollback
try:
    cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('Eve', 40))
    conn.commit()
    raise Exception("Simulated error!")
except Exception as e:
    print("Error occurred, rolling back transaction.")
    conn.rollback()

# Display after rollback
cursor.execute("SELECT * FROM users")
print("After Rollback:", cursor.fetchall())

# Execute SQL query dynamically based on user input
def dynamic_query(sql_query):
    try:
        cursor.execute(sql_query)
        result = cursor.fetchall()
        print("Dynamic Query Result:", result)
    except sqlite3.Error as e:
        print("Error executing query:", e)

dynamic_query("SELECT * FROM users WHERE age > 30")

# Close SQLite connection
conn.close()
