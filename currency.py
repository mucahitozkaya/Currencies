import pandas as pd

base="USD"
out_curr=()
start_date="2021-01-01"
end_date="2021-01-10"

url = 'https://api.exchangerate.host/timeseries?base={0}&start_date={1}&end_date={2}&symbols={3}'.format(base,start_date,end_date,out_curr)

response = requests.get(url)
data = response.json()

rates=[]
for id, info in data["rates"].items():
    for key in info:
        rates.append([ id , key , info[key]])

df = pd.DataFrame(rates)
df.columns=["Date","Name","Value"]
df.to_csv('currency.csv', index=False)
