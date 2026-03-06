import pandas as pd

# 讀取整個 Excel 檔案（預設第一個工作表）
df = pd.read_excel("../dataset/18 Cycles Sales.xlsx")

# 顯示前 5 列
print(df.head())