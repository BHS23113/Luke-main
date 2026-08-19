import sqlite3

connection = sqlite3.connect("prefectconnect.db")
cursor = connection.cursor()


# ==============================
# USERS TABLE
# ==============================

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT NOT NULL UNIQUE,
    name TEXT NOT NULL,
    role TEXT NOT NULL,
    is_active BOOLEAN NOT NULL DEFAULT 1
)
""")


# ==============================
# LOCKER DUTY TABLE
# ==============================

cursor.execute("""
CREATE TABLE IF NOT EXISTS locker_duty (
    duty_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    week TEXT NOT NULL,
    day TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
)
""")


# ==============================
# NOTICE TABLE
# ==============================

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


# ==============================
# NOTICE READ TABLE
# ==============================

cursor.execute("""
CREATE TABLE IF NOT EXISTS notice_read (
    read_id INTEGER PRIMARY KEY AUTOINCREMENT,
    notice_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    read_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(notice_id, user_id),
    FOREIGN KEY (notice_id) REFERENCES notice(notice_id) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
)
""")


connection.commit()
connection.close()

print("✅ PrefectConnect database created successfully!")