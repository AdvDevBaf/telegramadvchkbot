from mysql import connector as mysql
from mysql.connector import errors as con_error
from Settings import auth
import os

class DataBase(object):
    def __init__(self):
        print(os.environ['DATABASE_URL'])
        self.db = mysql.connect(
            host = auth['host'],
            user = auth['user'],
            passwd = auth['password']
        )
        self.cursor = self.db.cursor(buffered=True)

    def create_data(self):
        try:
            self.cursor.execute('USE heroku_65824eb363ca8cf')
        except con_error.ProgrammingError:
            self.cursor.execute('CREATE DATABASE IF NOT EXISTS heroku_65824eb363ca8cf')
            self.cursor.execute("CREATE TABLE IF NOT EXISTS users(campaign VARCHAR(255), links VARCHAR(255))")
        return self.db.commit()

    def insert_data(self, message):
        self.create_data()
        val = (str(message)[:str(message).find(':')].lower(), str(message)[str(message).find(':') + 1:])
        sql = "INSERT INTO users (campaign, links) VALUES (%s,%s)"
        self.cursor.execute(sql, val)
        return self.db.commit()

    def select_data(self):
        self.create_data()
        self.cursor.execute("SELECT * FROM users")
        self.db.commit()
        data = {}
        for elem in self.cursor:
            data[elem[0]] = elem[1]
        return data

    def delete_data(self, message):
        self.create_data()
        val = (str(message.text).lower(),)
        data = self.select_data()
        for elem in data:
            if elem == val[0]:
                sql = "DELETE FROM heroku_65824eb363ca8cf.users WHERE campaign=%s"
                self.cursor.execute(sql, val)
                self.db.commit()
                status = 'Кампания удалена'
            else:
                status = "Doesn't found campaign"
                return status
        return status
