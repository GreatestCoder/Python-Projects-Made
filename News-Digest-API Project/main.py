import requests
from emailsender import Emailer

topic = "Astrophysics"
API_key = "15a3855d35194c3ea2bc9ea917bc62a7"
url = f"https://newsapi.org/v2/everything?q={topic}&from=2024-07-12&sortBy=publishedAt&apiKey={API_key}&language=en"
request = requests.get(url)
content = request.json()
subject = "Subject: Today's Astrophysics News\n"
body = ""
for article in content["articles"][:20]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" + article["description"] + "\n" + article["url"] + 2*"\n"
message = subject + body
message = message.encode("utf-8")
Emailer(message)