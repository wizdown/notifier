import requests
from bs4 import BeautifulSoup


def extract_data(url):
    response = requests.get(url)
    html = response.content
    soup = BeautifulSoup(html,"lxml")
    list = soup.find_all('div', attrs={'class': 'item'})
    return list

def extract_boruto_data():
    boruto_data = extract_data('https://9anime.to/search?keyword=boruto')
    for data in boruto_data:
        data = data.text[4:]
        if 'Boruto: Naruto Next Generations' in data:
            break
    # print data
    episode_no = data.split(' ')[4]
    episode_no = episode_no.split('/')[0]
    return episode_no


new_episode_no = extract_boruto_data()
file = open('../new_info.txt','a')
line='boruto:' + str(new_episode_no) + '\n'
file.write(line)
