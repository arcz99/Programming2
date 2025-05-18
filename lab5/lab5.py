import sqlite3

conn = sqlite3.connect("sales.db")
cursor = conn.cursor()
cursor.execute("SELECT date, SUM(quantity) AS total_quantity FROM sales GROUP BY date ORDER BY total_quantity DESC LIMIT 1")
#"SELECT * FROM salesWHERE product = 'Laptop'"
#"SELECT * FROM sales WHERE date = '2025-05-07' OR date = '2025-05-08'"
#"SELECT * FROM sales WHERE price > 200.0"
#"SELECT product, SUM(quantity*price) AS total_sales FROM sales GROUP BY product"
#"SELECT date, SUM(quantity) AS total_quantity FROM sales GROUP BY date ORDER BY total_quantity DESC LIMIT 1"

rows = cursor.fetchall()
for row in rows:
    print(row)

conn.close()