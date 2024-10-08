import sqlite3

class URLMapper:
    def __init__(self):
        self.conn = sqlite3.connect('urls.db')
        self.cursor = self.conn.cursor()

    def create_short_url(self, original_url):
        short_code = self.generate_short_code()
        self.cursor.execute("INSERT INTO urls (original_url, short_code) VALUES (?, ?)", (original_url, short_code))
        self.conn.commit()
        return short_code

    def get_original_url(self, short_code):
        self.cursor.execute("SELECT original_url FROM urls WHERE short_code=?", (short_code,))
        result = self.cursor.fetchone()
        if result:
            return result[0]
        return None

    def generate_short_code(self):

        import uuid
        return uuid.uuid4().hex[:6]

    def __del__(self):
        self.conn.close()