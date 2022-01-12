import requests
import datetime 
from twilio.rest import Client 

URL = "https://www.alphavantage.co/query"
STOCK = "TSLA"
API_KEY = "*************"

URL_NEWS = "https://newsapi.org/v2/everything"
API_NEWS = "*******************************"
COMPANY_NAME = "tesla"

ACCOUNT_SID = "******************************"
AUTH_TOKEN = "******************************"

now = datetime.datetime.now()
today = now.date()
yesterday = today - datetime.timedelta(days=1)
day_before_yestarday = today - datetime.timedelta(days=2)

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 

def send_sms(title, body):
    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    message = client.messages \
                    .create(
                        body=f"{title}\n{body}",
                        from_= '+************',
                        to= '+************'
                    )
    print(message.status)

## STEP 2: Use https://newsapi.org
def get_news():
    response = requests.get(f'{URL_NEWS}?qInTitle={COMPANY_NAME}&sortBy=publishedAt&language=en&apiKey={API_NEWS}')
    response.raise_for_status()
    tesla_data = response.json()['articles']
    # three_articles = tesla_data[:3]
    for n in range(0,3):
        title = tesla_data[n]["title"]
        body = tesla_data[n]["description"]
        send_sms(title, body)


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=demo
response = requests.get(f'{URL}?function=TIME_SERIES_DAILY&symbol={STOCK}&apikey={API_KEY}')
response.raise_for_status()
tesla_data = response.json()

y_close = tesla_data["Time Series (Daily)"][f"{yesterday}"]['4. close']
dby_close = tesla_data["Time Series (Daily)"][f"{day_before_yestarday}"]['4. close']

diffrence = abs(float(y_close) - float(dby_close))

percentage = (diffrence / float(dby_close)) * 100

if percentage > 5:
    get_news()





