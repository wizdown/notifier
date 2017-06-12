import requests
from bs4 import BeautifulSoup


def extract_data(url):
    response = requests.get(url)
    if response.status_code == 0:
        return -1
    # print response.text
    html = response.content
    soup = BeautifulSoup(html,"lxml")
    list = soup.find_all('div', attrs={'class': 'item'})
    return list


def extract_titans_data():
    titan_data = extract_data('https://9anime.to/search?keyword=attack+on+titan')
    if titan_data == -1:
        return 0
    if( len(titan_data) == 0):
        return 0
    for data in titan_data:
        data = data.text[4:]
        if 'Attack on Titan Season 2' in data and 'Attack on Titan Season 2 (Dub)' not in data:
            break
    # print data
    episode_no = data.split(' ')[5]
    episode_no = episode_no.split('/')[0]
    return episode_no


new_episode_no = extract_titans_data()
info = 'attack_on_titans_s02:' + str(new_episode_no)
print info
# file = open('../new_info.txt','a')
# line='attack_on_titans_s02:' + str(new_episode_no) + '\n'
# file.write(line)
