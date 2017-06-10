import requests
from bs4 import BeautifulSoup


def extract_data(url):
    response = requests.get(url)
    html = response.content
    soup = BeautifulSoup(html,"lxml")
    list = soup.find_all('figure')
    return list

def extract_new_data(url):
    response = requests.get(url)
    html = response.content
    soup = BeautifulSoup(html,"lxml")
    list = soup.find_all('span', attrs={'class': 'name'})
    return list


def extract_originals_data():
    base_url = 'http://fmovie.io'
    originals_data = extract_data('http://fmovie.io/search.html?keyword=originals')
    if( len(originals_data) == 0):
        return 0
    data = originals_data[4]
    data = data.find('a')
    data = data['href']
    new_url = base_url + data
    # print new_url
    new_originals_data = extract_new_data(new_url)
    if( len(new_originals_data) == 0):
        return 0
    new_originals_data = new_originals_data[0]
    data = new_originals_data.text
    index = data.find('Episode')
    index = index + 8
    episode_no = data[index:index+2]
    return episode_no

new_episode_no = extract_originals_data()
info = 'originals_s04:' + str(new_episode_no)
print info
