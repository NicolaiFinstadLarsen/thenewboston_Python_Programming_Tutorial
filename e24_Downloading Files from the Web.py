from urllib import request

akso_url = "https://query1.finance.yahoo.com/v7/finance/download/AKSO.OL?period1=1554838624&period2=1586461024&interval=1d&events=history"

def download_aker_sol(csv_akso):
    response = request.urlopen(csv_akso)
    csv = response.read()
    csv_str = str(csv)    
    lines = csv_str.split(\\n") #vi bruker \\n fordi stringen vi har fra før inneholder \n der de nye linjene skal begynne. 
    #Vi splitter derfor ved \n men må bruke en escape \ for å få med \n i stringen.
    dest_url = r"akso_prices"
    
    aksje_text = open(dest_url, "w")
    for line in lines:
        aksje_text.write(line + "\n")
    aksje_text.close
download_aker_sol(akso_url)




    
    