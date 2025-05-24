import pymysql
from pymysql.cursors import DictCursor
from contextlib import contextmanager
from logging_setup import setup_logger

logger = setup_logger('db_helper')

@contextmanager
def get_db_cursor(commit=False):
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="root",
        database="expense_manager",
        charset='utf8mb4',
        cursorclass=DictCursor
    )
    cursor = connection.cursor()
    try:
        yield cursor
        if commit:
            connection.commit()
    finally:
        cursor.close()
        connection.close()

def fetch_expenses_for_date(expense_date):
    logger.info(f"fetch_expenses_for_date called with {expense_date}")
    with get_db_cursor() as cursor:
        cursor.execute("SELECT * FROM expenses WHERE expense_date = %s", (expense_date,))
        expenses = cursor.fetchall()
        return expenses

def delete_expenses_for_date(expense_date):
    logger.info(f"delete_expenses_for_date called with {expense_date}")
    with get_db_cursor(commit=True) as cursor:
        cursor.execute("DELETE FROM expenses WHERE expense_date = %s", (expense_date,))

def insert_expense(expense_date, amount, category, notes):
    logger.info(f"insert_expense called with date: {expense_date}, amount: {amount}, category: {category}, notes: {notes}")
    with get_db_cursor(commit=True) as cursor:
        cursor.execute(
            "INSERT INTO expenses (expense_date, amount, category, notes) VALUES (%s, %s, %s, %s)",
            (expense_date, amount, category, notes)
        )

def fetch_expense_summary(start_date, end_date):
    logger.info(f"fetch_expense_summary called with start: {start_date} end: {end_date}")
    with get_db_cursor() as cursor:
        cursor.execute(
            '''SELECT category, SUM(amount) as total
               FROM expenses WHERE expense_date
               BETWEEN %s and %s
               GROUP BY category;''',
            (start_date, end_date)
        )
        data = cursor.fetchall()
        return data

if __name__ == "__main__":
    fetched_expenses = fetch_expenses_for_date("2024-09-30")
    print(fetched_expenses)
    # delete_expenses_for_date("2024-08-2_
