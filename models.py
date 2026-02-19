from database import get_connection

class User:
    @staticmethod
    def create_user(username, password):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            conn.commit()
            return True
        except Exception as e:
            print(f"Error creating user: {e}")
            return False
        finally:
            conn.close()

    @staticmethod
    def login(username, password):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM users WHERE username = ? AND password = ?", (username, password))
        user = cursor.fetchone()
        conn.close()
        return user['id'] if user else None

class Expense:
    @staticmethod
    def add_expense(user_id, amount, category, date, description):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO expenses (user_id, amount, category, date, description) VALUES (?, ?, ?, ?, ?)",
            (user_id, amount, category, date, description)
        )
        conn.commit()
        conn.close()

    @staticmethod
    def get_expenses(user_id, filters=None):
        conn = get_connection()
        cursor = conn.cursor()
        query = "SELECT * FROM expenses WHERE user_id = ?"
        params = [user_id]
        
        if filters:
            if 'category' in filters:
                query += " AND category = ?"
                params.append(filters['category'])
            if 'month' in filters:
                query += " AND strftime('%Y-%m', date) = ?"
                params.append(filters['month'])
                
        cursor.execute(query, params)
        expenses = cursor.fetchall()
        conn.close()
        return expenses

    @staticmethod
    def delete_expense(expense_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
        conn.commit()
        conn.close()

class Budget:
    @staticmethod
    def set_budget(user_id, month, amount):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT OR REPLACE INTO budgets (user_id, month, amount) VALUES (?, ?, ?)",
            (user_id, month, amount)
        )
        conn.commit()
        conn.close()

    @staticmethod
    def get_budget(user_id, month):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT amount FROM budgets WHERE user_id = ? AND month = ?", (user_id, month))
        budget = cursor.fetchone()
        conn.close()
        return budget['amount'] if budget else 0.0
