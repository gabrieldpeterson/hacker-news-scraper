import requests
from bs4 import BeautifulSoup


def create_custom_hn(links, votes):
    hn = []
    return hn


res = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text, 'html.parser')
# print(soup.select('.titlelink')[0].text)
links = soup.find_all(attrs={'class': 'titlelink'})
votes = soup.select('.score')
found_votes = links

print(len(links), len(votes))

for link in links:
    print(link.getText)

