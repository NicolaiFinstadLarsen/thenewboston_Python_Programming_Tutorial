from urllib import request

qfree_url = "https://query1.finance.yahoo.com/v7/finance/download/QFR.OL?period1=1554843189&period2=1586465589&interval=1d&events=history"


def download_qfree(csv_qfree):
    response = request.urlopen(csv_qfree)
    csv = response.read()
    csv_str = str(csv)
    lines = csv_str.split("\\n")
    dest_url = r"qfree_prices"
    
    aksje_text = open(dest_url, "w")
    for line in lines:
        aksje_text.write(line + "\n")
    aksje_text.close()
download_qfree(qfree_url)    

    
