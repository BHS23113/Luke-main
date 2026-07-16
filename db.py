import sqlite3

connection = sqlite3.connect("prefectconnect.db")
cursor = connection.cursor()

# USERS TABLE
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT NOT NULL UNIQUE,
    name TEXT NOT NULL,
    role TEXT NOT NULL,
    is_active BOOLEAN NOT NULL DEFAULT 1
)
""")

# LOCKER DUTY TABLE
cursor.execute("""
CREATE TABLE IF NOT EXISTS locker_duty (
    duty_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    duty_date DATE NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
)
""")

# MESSAGE POST TABLE
cursor.execute("""
CREATE TABLE IF NOT EXISTS message_post (
    post_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    content TEXT NOT NULL,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
)
""")

# NOTICE TABLE
cursor.execute("""
CREATE TABLE IF NOT EXISTS notice (
    notice_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    created_by INTEGER NOT NULL,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN NOT NULL DEFAULT 1,
    FOREIGN KEY (created_by) REFERENCES users(user_id) ON DELETE CASCADE
)
""")

# ASSEMBLY TABLE
cursor.execute("""
CREATE TABLE IF NOT EXISTS assembly (
    assembly_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    date DATE NOT NULL
)
""")

# ASSEMBLY IDEA TABLE
cursor.execute("""
CREATE TABLE IF NOT EXISTS assembly_idea (
    idea_id INTEGER PRIMARY KEY AUTOINCREMENT,
    assembly_id INTEGER NOT NULL,
    content TEXT NOT NULL,
    updated_by INTEGER NOT NULL,
    FOREIGN KEY (assembly_id) REFERENCES assembly(assembly_id) ON DELETE CASCADE,
    FOREIGN KEY (updated_by) REFERENCES users(user_id) ON DELETE CASCADE
)
""")

# RUN SHEET TABLE
cursor.execute("""
CREATE TABLE IF NOT EXISTS run_sheet (
    runsheet_id INTEGER PRIMARY KEY AUTOINCREMENT,
    assembly_id INTEGER NOT NULL,
    content TEXT NOT NULL,
    updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (assembly_id) REFERENCES assembly(assembly_id) ON DELETE CASCADE
)
""")

connection.commit()
connection.close()

print("✅ PrefectConnect database created successfully!")