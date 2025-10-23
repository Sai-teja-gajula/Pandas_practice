import pandas as pd
import sqlite3
conn = sqlite3.connect("mydb.db")
sales= pd.read_csv("sales_clean.csv", parse_dates=["OrderDate"])
sales.to_sql("orders_table", conn, if_exists="replace", index=False)
output= pd.read_sql("""
select sum(Total) as total_sales, Product
from orders_table
group by Product""", conn)
conn.close()
print(output)

