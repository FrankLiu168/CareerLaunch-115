import sqlite3
import pandas as pd

# 修改為你的 SQLite 檔案路徑
db_path = R"C:\data\your_database.db"

# 建立連線
conn = sqlite3.connect(db_path)

# 執行查詢（替換 your_table 為實際表格名）
df = pd.read_sql_query("SELECT * FROM your_table", conn)

# 關閉連線
conn.close()