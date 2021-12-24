import sqlite3

db_path = "ContactBook.db"
table_name = "contact_book"


class DBHandler:
    def __init__(self):
        self.con = sqlite3.connect(db_path)
        self.cur = self.con.cursor()

    def query(self, query_text):
        query_command = f"SELECT * from {table_name} \
            WHERE first_name LIKE '%{query_text}%' \
            OR last_name LIKE '%{query_text}%' \
            OR email LIKE '%{query_text}%' \
            OR phone_number IS '{query_text}'"

        self.cur.execute(query_command)
        return self.cur.fetchall()

    def insert(self, first_name, last_name, phone_number, email):
        query_command = f"INSERT INTO {table_name} (first_name, last_name, phone_number, email) \
            VALUES ('{first_name}', '{last_name}', '{phone_number}', '{email}')"

        self.cur.execute(query_command)
        self.con.commit()

        return self.cur.lastrowid

    def delete(self, id):
        query_command = f"DELETE from {table_name} WHERE {table_name}.id = {id}"
        self.cur.execute(query_command)
        self.con.commit()

        return self.cur.lastrowid