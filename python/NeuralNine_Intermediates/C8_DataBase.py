import sqlite3

connection = sqlite3.connect(database="mydata.db")
cursor = connection.cursor()

# 创建表
cursor.execute("""
CREATE TABLE IF NOT EXISTS persons(
    first_name TEXT,
    last_name TEXT,
    age INTEAGE
)
""")
#增加条目
cursor.execute("""
INSERT INTO persons VALUES
('Paul','Smith',24),
('Mark','Smith',24),
('Anna','Smith',24)
"""
)
#查找
cursor.execute("""
SELECT * FROM persons
WHERE first_name = 'Paul'
""")

rows = cursor.fetchall()
print(rows)

connection.commit()
connection.close()