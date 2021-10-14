import requests
from bs4 import BeautifulSoup
strYear = "2020"
strFile = 'WuhanWeather' + strYear +'.csv'
f = open(strFile, "w")
bigmonth = ['01', '03', '05', '07', '08', '10', '12']
smallmonth = ['04', '06', '09', '11']
runmonth = ['02']
for month in range(1, 13):
    if month < 10:
        strMonth = '0' + str(month)
    else:
        strMonth = str(month)
    strYearMonth = strYear + strMonth
    print('\nGetting data for month' + strYearMonth + '...', end="")

    url = "https://lishi.tianqi.com/wuhan/" + strYearMonth + ".html"
    page = requests.get(url)
    html = page.text

    soup = BeautifulSoup(html, 'html.parser')
    data = soup.find(attrs={"class":"thrui"})
    qiepian = data.text.split()
    if strMonth in smallmonth:
        Monthday = 30
    elif strMonth in bigmonth:
        Monthday = 31
    else:
        Monthday = 29
    for day in range(0,Monthday):
        strDate = qiepian[0+7*day]
        highWeather = qiepian[2+7*day]
        lowWeather = qiepian[3+7*day]
        f.write(strDate + ',' + lowWeather + ',' + highWeather + '\n')
        print("done", end=' ')

f.close()
print("\nover")


