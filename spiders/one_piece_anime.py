import requests
from bs4 import BeautifulSoup

def extract_data(url):
    response = requests.get(url)
    html = response.content
    soup = BeautifulSoup(html,"lxml")
    list = soup.find_all('div', attrs={'class': 'item'})
    return list

# Extracting one piece data
def extract_one_piece_anime_data():
    one_piece_anime_data = extract_data('https://9anime.to/search?keyword=one+piece')
    for data in one_piece_anime_data:
        data = data.text[4:]
        if 'ONE PIECE' in data:
                break
    # print data
    episode_no = data.split(' ')[2]
    episode_no = episode_no.split('/')[0]
    return episode_no

new_episode_no = extract_one_piece_anime_data()
file = open('../new_info.txt','a')
line='one_piece_anime:' + str(new_episode_no) + '\n'
file.write(line)
