import requests
from bs4 import BeautifulSoup

def extract_data(url):
    response = requests.get(url)
    if response.status_code == 0:
        return -1
    html = response.content
    soup = BeautifulSoup(html,"lxml")
    list = soup.find_all('h3', attrs={'class': 'yt-lockup-title'})
    return list


def extract_fairy_tail_data_from_youtube():
    fairy_tail_data = extract_data('https://www.youtube.com/user/Zac2Uchiha/videos')
    if fairy_tail_data == -1:
        return 0
    if( len(fairy_tail_data) == 0):
        return 0

    for entry in fairy_tail_data:
        full_title = entry.text
        if "FAIRY TAIL" in full_title:
            full_title = full_title.split('English')
            full_title=full_title[0];
            full_title = full_title[17:]
            detailed_title=full_title.split(':')
            number=detailed_title[0]
            name=detailed_title[1]
            # print full_title
            # print 'name => ' + name + ' ; ' + 'number => ' + number
            break
    return number

new_episode_no = extract_fairy_tail_data_from_youtube()
info='youtube_fairy_tail:' + str(new_episode_no)
print info

# print new_episode_no
# file = open('../new_info.txt','a')
# line='youtube_fairy_tail:' + str(new_episode_no) + '\n'
# file.write(line)
