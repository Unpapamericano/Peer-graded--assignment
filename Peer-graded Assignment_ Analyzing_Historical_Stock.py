get_ipython().system('pip install yfinance')
get_ipython().system('pip install pandas')



get_ipython().system('pip install yfinance')
get_ipython().system('pip install pandas')
get_ipython().system('pip install requests')
get_ipython().system('pip install bs4')
get_ipython().system('pip install plotly')



import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup
import plotly.graph_objects as go
from plotly.subplots import make_subplots




tesla=yf.Ticker("TSLA")



tesla_data=tesla.history(period="max")



tesla_data.reset_index(inplace=True)
tesla_data.head(5)



get_ipython().system('pip3 install requests')
import requests

# The URL you want to fetch
url = "https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue"
# Check if the request was successful
if response.status_code == 200:
    html_data = response.text
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
    
soup_tesla = BeautifulSoup(html_data, 'html.parser')




url_tesla = "https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
response_tesla = requests.get(url_tesla, headers=headers)
html_data_tesla = response_tesla.text

soup_tesla = BeautifulSoup(html_data_tesla, 'html.parser')

data_tesla = []
for table in soup_tesla.find_all("table"):
    
    if any(["Tesla Quarterly Revenue".lower() in th.text.lower() for th in table.find_all("th")]):
        for row in table.find("tbody").find_all("tr"):
            date_col, rev_col = [col.text for col in row.find_all("td")]
            data_tesla.append({
                "Date": date_col,
                "Revenue": rev_col.replace("$", "").replace(",", "")
            })

tesla_revenue = pd.DataFrame(data_tesla)

tesla_revenue.tail()








# In[159]:


gme = yf.Ticker("GME")



gme_data = gme.history(period="max")


gme_data.reset_index(inplace=True)
gme_data.head()


get_ipython().system('pip3 install requests')
import requests

url = "https://www.macrotrends.net/stocks/charts/GME/gamestop/revenue?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkPY0220ENSkillsNetwork23455606-2021-01-01"
html_data = requests.get(url).text


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
response = requests.get(url, headers=headers)
html_data = response.text

soup = BeautifulSoup(html_data)


data = []
for table in soup.find_all("table"):
    
    if any(["GameStop Quarterly Revenue".lower() in th.text.lower() for th in table.find_all("th")]):
        for row in table.find("tbody").find_all("tr"):
            date_col, rev_col = [col for col in row.find_all("td")]
            data.append({
                "Date": date_col.text,
                "Revenue": rev_col.text.replace("$", "").replace(",", "")
            })

gme_revenue = pd.DataFrame(data)

gme_revenue.tail()


print(tesla_data.columns)


print(tesla_data.columns)


print(tesla_data.index.name)
