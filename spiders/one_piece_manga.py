import requests
from bs4 import BeautifulSoup

def extract_data(url):
    response = requests.get(url)
    html = response.content
    soup = BeautifulSoup(html,"lxml")
    list = soup.find_all('div', attrs={'class': 'col-xs-9'})
    return list

# Extracting one piece data
def extract_one_piece_manga_data():
    one_piece_manga_data = extract_data('http://www.gomymanga.com/manga/One_Piece')
    i = 0;
    data = one_piece_manga_data[1].text
    data = data[1:]
    episode_name = data[0:9]
    episode_no = data[10:13]
    # print episode_no + " : " + episode_name + '_'
    return episode_no

new_episode_no = extract_one_piece_manga_data()
file = open('../new_info.txt','a')
line='one_piece:' + str(new_episode_no) + '\n'
file.write(line)
