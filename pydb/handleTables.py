import sqlite3
def create_tables(db_path):
    sqls = ["./sql/original/原因及傷亡.sql",
            "./sql/original/肇事者.sql",
            "./sql/tables/分局.sql",
            "./sql/tables/時間.sql",
            "./sql/tables/肇事者.sql",
            "./sql/tables/原因及傷亡.sql"] 
    
    # Create a new SQLite database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Create a dataset table with three VARCHAR columns
    for sql in sqls:
        with open(sql, 'r', encoding='utf-8') as file:
            sql_script = file.read()
            cursor.executescript(sql_script)

    # Commit changes and close the connection
    conn.commit()
    conn.close()

import sqlite3

def drop_all_tables(db_path):
    """
    刪除指定 SQLite 資料庫中的所有使用者表格（不含 sqlite_ 開頭的系統表）
    
    :param db_path: SQLite 資料庫檔案路徑（例如 'data.db'）
    """
    # 連接到資料庫
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # 查詢所有非系統表格的名稱
    cursor.execute("""
        SELECT name 
        FROM sqlite_master 
        WHERE type = 'table' 
          AND name NOT LIKE 'sqlite_%';
    """)
    tables = cursor.fetchall()

    # 逐一刪除每個表格
    for table_name, in tables:
        print(f"Dropping table: {table_name}")
        cursor.execute(f'DROP TABLE IF EXISTS "{table_name}";')

    # 提交變更並關閉連線
    conn.commit()
    conn.close()
    print("所有使用者表格已成功刪除。")


drop_all_tables('./db/local.db')  # 替換成你的 .db 檔案路徑
create_tables('./db/local.db')