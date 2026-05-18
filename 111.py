import csv
import urllib.request
import sys

def fetch_and_query_data():
    # 政府開放資料 URL：樂齡學習中心活動參與人次
    url = 'https://quality.data.gov.tw/dq_download_csv.php?nid=127117&md5_url=6d6a61b0b5853713ca571c690355a5a0'

    print("正在從網路獲取最新資料 ，請稍候...")

    try:
        # 使用 with 確保連線資源會被正確關閉
        with urllib.request.urlopen(url, timeout=10) as response:
            # 讀取並解碼資料
            content = response.read().decode('utf-8')
            lines = content.splitlines()

            # 使用 csv.reader 讀取資料
            reader = csv.reader(lines)

            # 取得標題列（第一列）
            header = next(reader)
            # 將剩餘資料轉為清單，方便重複查詢
            data_list = list(reader)

            print("\n資料下載完成！")
            print("提示：資料年份格式為 '2013年'，您可以輸入 '2013' 或 '2013年'")
            print("輸入 'q' 或直接按 Enter 鍵可結束程式。")

            # --- 新增：使用 while 迴圈達成連續查詢功能 ---
            while True:
                query_year = input("\n請輸入查詢年別：").strip()

                # 如果輸入 'q'、'Q' 或空白，則跳出迴圈結束程式
                if not query_year or query_year.lower() == 'q':
                    print("程式結束，謝謝使用！")
                    break

                # 格式化輸出結果
                print(f"\n{'='*70}")
                print(f"{'序號':<6} | {'年份':<10} | {'女性參與人次':<15} | {'男性參與人次':<15}")
                print(f"{'-'*70}")

                found = False
                for row in data_list:
                    # 檢查年份欄位 (row[1])
                    if query_year in row[1]:
                        found = True
                        # 使用 f-string 進行對齊輸出
                        print(f"{row[0]:<8} | {row[1]:<12} | {row[2]:>12} | {row[3]:>12}")

                if not found:
                    print(f"找不到關於 '{query_year}' 的資料。")
                print(f"{'='*70}")

    except urllib.error.URLError as e:
        print(f"網路連線錯誤: {e.reason}")
    except Exception as e:
        print(f"發生非預期錯誤: {e}")

if __name__ == "__main__":
    fetch_and_query_data()
