import requests
from bs4 import BeautifulSoup
import pprint


def sort_by_votes(hnlist):
    return sorted(hnlist, key=lambda x: x['votes'], reverse=True)


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
    return sort_by_votes(hn)


res = requests.get('https://news.ycombinator.com/news')
res2 = requests.get('https://news.ycombinator.com/news?p=2')
soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')
# print(soup.select('.titlelink')[0].text)
links1 = soup.find_all(attrs={'class': 'titlelink'})
links2 = soup2.find_all(attrs={'class': 'titlelink'})
links = links1 + links2
subtext1 = soup.select('.subtext')
subtext2 = soup.select('.subtext')
subtext = subtext1 + subtext2
found_votes = links

pprint.pprint(create_custom_hn(links, subtext, 100))

