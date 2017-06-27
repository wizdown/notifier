import requests
from bs4 import BeautifulSoup


def extract_data(url):
    response = requests.get(url)
    if response.status_code == 0:
        return -1
    html = response.content
    soup = BeautifulSoup(html,"lxml")
    list = soup.find_all('figure')
    return list

def extract_new_data(url):
    response = requests.get(url)
    if response.status_code == 0:
        return -1
    html = response.content
    soup = BeautifulSoup(html,"lxml")
    list = soup.find_all('span', attrs={'class': 'name'})
    return list


def extract_silicon_valley_data():
    base_url = 'http://fmovie.io'
    silicon_valley_data = extract_data('http://fmovie.io/search.html?keyword=silicon+valley')
    if silicon_valley_data == -1:
        return 0
    if( len(silicon_valley_data) == 0):
        return 0
    data =silicon_valley_data[4]
    data = data.find('a')
    data = data['href']
    new_url = base_url + data
    # print new_url
    new_silicon_valley_data = extract_new_data(new_url)
    if new_silicon_valley_data == -1:
        return 0
    if( len(new_silicon_valley_data) == 0):
        return 0
    new_silicon_valley_data = new_silicon_valley_data[0]
    data = new_silicon_valley_data.text
    index = data.find('Episode')
    index = index + 8
    episode_no = data[index:index+2]
    return episode_no

new_episode_no = extract_silicon_valley_data()
info = 'silicon_valley_s04:' + str(new_episode_no)
print info
