import pandas as pd
import sqlite3

def importCsvToSqlite(csv_file, db_path, table_name,columns):    
    # 讀取 CSV：跳過第一行，且不將任何行視為欄位名
    df = pd.read_csv(csv_file, header=None, skiprows=1)
    df.columns = columns# 設定欄位名稱為空字串，或你可以自訂欄位名稱
    # 建立 SQLite 連線
    conn = sqlite3.connect(db_path)    
    # 寫入 SQLite（若無自訂欄位名，則用 0,1,2... 當欄位名）
    df.to_sql(table_name, conn, if_exists='replace', index=False)    
    conn.close()

importCsvToSqlite('./dataset/每月新北市A1類道路交通事故－原因及傷亡.csv', 
                  './db/local.db', 
                  '原始_交通事故_原因及傷亡',
                  ["年月", "分局", "駕駛人過失_超速失控_含未減速", "駕駛人過失_酒後駕車", "駕駛人過失_未注意車前狀況", "駕駛人過失_肇事逃逸", "駕駛人過失_未保持行車安全間距", "駕駛人過失_未依規定讓車", "駕駛人過失_行駛疏忽", "駕駛人過失_違反號誌管制", "駕駛人過失_違反標誌標線", "駕駛人過失_逆向行駛", "駕駛人過失_轉彎不當", "駕駛人過失_搶越行人穿越道", "駕駛人過失_其他", "機件故障", "行人過失", "交通管制設施缺陷", "其他"] )
importCsvToSqlite('./dataset/每月新北市A1類道路交通事故－肇事者.csv', 
                  './db/local.db', 
                  '原始_交通事故_肇事者',
                  ["年月", "分局", "肇事者_第一當事人_男", "肇事者_第一當事人_女", "肇事者_第一當事人_不詳", "死亡人數_男", "死亡人數_女", "受傷人數_男", "受傷人數_女"])