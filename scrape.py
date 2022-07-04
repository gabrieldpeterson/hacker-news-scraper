import requests
from bs4 import BeautifulSoup
import pprint


def create_custom_hn(links, subtext, min_points=0):
    """Create custom dictionary that contains title, link, and points for anything above a minimum amount of points"""
    hn = []
    for index, item in enumerate(links):
        title = links[index].getText()
        href = links[index].get('href', None)
        vote = subtext[index].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points >= min_points:
                hn.append({'title': title, 'link': href, 'votes': points})
    return hn


res = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text, 'html.parser')
# print(soup.select('.titlelink')[0].text)
links = soup.find_all(attrs={'class': 'titlelink'})
subtext = soup.select('.subtext')
found_votes = links

pprint.pprint(create_custom_hn(links, subtext, 100))

