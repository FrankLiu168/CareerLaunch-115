def castYearMonthToInt(yearMonth : str) -> int:
    yearMonth = yearMonth.split("年")
    year = int(yearMonth[0])
    month = int(yearMonth[1].replace("月", ""))
    return year * 100 + month

def createYearMonthData(minYear,maxYear):
    data = []
    for year in range(minYear, maxYear + 1):
        for month in range(1, 13):
            data.append((year * 100 + month, year, month))
    return data

def getDistinctOrgan(db_path):
    import sqlite3
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT 分局 FROM 原始_交通事故_肇事者")
    organs = [row[0] for row in cursor.fetchall()]
    conn.close()
    return organs

def initYearMonthTable(db_path, minYear, maxYear):
    import sqlite3
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    data = createYearMonthData(minYear, maxYear)
    cursor.executemany("INSERT INTO 時間 (年月, 年, 月) VALUES (?, ?, ?)", data)
    conn.commit()
    conn.close()

def initOrganTable(db_path):
    import sqlite3
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    organs = getDistinctOrgan(db_path)
    cursor.executemany("INSERT INTO 分局 (分局名稱) VALUES (?)", [(organ,) for organ in organs])
    conn.commit()
    conn.close()

def init肇事者Table(db_path):
    import sqlite3
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT 年月, 分局, 肇事者_第一當事人_男, 肇事者_第一當事人_女, 肇事者_第一當事人_不詳, 死亡人數_男, 死亡人數_女, 受傷人數_男, 受傷人數_女 FROM 原始_交通事故_肇事者")
    datas = cursor.fetchall()
    for data in datas:
        data = list(data)
        data[0] = castYearMonthToInt(data[0])  # 將年月轉換為整數
        cursor.executemany("""
        INSERT INTO 交通事故_肇事者 (
        年月, 
        分局, 
        肇事者_第一當事人_男, 
        肇事者_第一當事人_女, 
        肇事者_第一當事人_不詳, 
        死亡人數_男, 
        死亡人數_女, 
        受傷人數_男, 
        受傷人數_女
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);""")
    conn.commit()
    conn.close()
def init原因及傷亡Table(db_path):
    pass


initYearMonthTable('./db/local.db', 103, 115)
initOrganTable('./db/local.db')