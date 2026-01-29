import sqlite3
import pandas as pd

# ------------------ DATABASE SETUP ------------------
conn = sqlite3.connect("sales.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    order_id INTEGER,
    product TEXT,
    region TEXT,
    amount INTEGER,
    order_date TEXT
)
""")

cursor.execute("DELETE FROM sales")

data = [
    (1, 'Laptop', 'South', 60000, '2024-01-05'),
    (2, 'Phone', 'North', 30000, '2024-01-10'),
    (3, 'Tablet', 'East', 20000, '2024-02-12'),
    (4, 'Laptop', 'West', 65000, '2024-02-15'),
    (5, 'Phone', 'South', 28000, '2024-03-01'),
    (6, 'Tablet', 'North', 22000, '2024-03-10'),
    (7, 'Laptop', 'East', 70000, '2024-03-15'),
    (8, 'Phone', 'West', 32000, '2024-04-01')
]

cursor.executemany("INSERT INTO sales VALUES (?,?,?,?,?)", data)
conn.commit()

# ------------------ QUERIES ------------------
expected_queries = {
    "Q1": "SELECT SUM(amount) FROM sales",
    "Q2": "SELECT region, SUM(amount) FROM sales GROUP BY region",
    "Q3": "SELECT product, SUM(amount) FROM sales GROUP BY product ORDER BY SUM(amount) DESC LIMIT 1",
    "Q4": "SELECT * FROM sales WHERE order_date > '2024-02-01'",
    "Q5": "SELECT AVG(amount) FROM sales"
}

generated_queries = {
    "Q1": "SELECT amount FROM sales",   # wrong
    "Q2": "SELECT region, SUM(amount) FROM sales GROUP BY region",  # correct
    "Q3": "SELECT product FROM sales",  # wrong
    "Q4": "SELECT * FROM sales WHERE order_date > '2024-02-01'",    # correct
    "Q5": "SELECT AVG(amount) FROM sales"  # correct
}

# ------------------ EVALUATION FUNCTIONS ------------------
def execute_query(query):
    try:
        df = pd.read_sql_query(query, conn)
        return df, "Valid"
    except Exception:
        return None, "Syntax Error"

def evaluate_query(expected_sql, generated_sql):
    exp_df, _ = execute_query(expected_sql)
    gen_df, status = execute_query(generated_sql)

    if status != "Valid":
        return "Syntax Error"
    if exp_df.equals(gen_df):
        return "Correct"
    return "Logical Error"

# ------------------ RUN EVALUATION ------------------
print("\nEvaluation Results:\n")

for q in expected_queries:
    result = evaluate_query(expected_queries[q], generated_queries[q])
    print(f"{q} -> {result}")

conn.close()
