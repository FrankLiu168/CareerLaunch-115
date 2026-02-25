

import requests
from bs4 import BeautifulSoup

def get_google_finance_price(ticker):
    url = f"https://www.google.com/finance/quote/{ticker}:TPE"
    
    # 模擬瀏覽器 Header，避免被阻擋
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    

    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Google Finance 的價格通常放在 class 為 "fxKbKc" 的 div 中 (這類 class 名稱可能隨時改變)
        price = soup.find("div", {"class": "fxKbKc"}).text
        name = soup.find("div", {"class": "zzDege"}).text
        
        print(f"股票爬蟲 3.0版")
        print(f"股票名稱: {name}")
        print(f"即時股價: {price}")
    else:
        print("無法取得網頁內容")

get_google_finance_price("2330")