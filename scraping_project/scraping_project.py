import requests
from bs4 import BeautifulSoup
from csv import writer

base_url = "http://quotes.toscrape.com"
url = "/page/1/"
quote_list = []

while url:
    response = requests.get(f"{base_url}{url}")
    soup = BeautifulSoup(response.text, "html.parser")
    quotes = soup.find_all("div", class_="quote")

    # with open("quotes_data.csv", "w") as csv_file:
    #     csv_writer = writer(csv_file)
    #     csv_writer.writerow(["quote", "author", "link"])

    for q in quotes:
        quote_list.append({
            "quote": q.find("span", class_="text").get_text(),
            "author": q.find("small", class_="author").get_text(),
            "link": q.find("a")["href"]
        })
    next_btn = soup.find(class_="next")
    url = next_btn.find("a")["href"] if next_btn else None

# csv_writer.writerow([quote, author, link])

print(quote_list)
