import requests
from bs4 import BeautifulSoup

def extract_data(url):
    response = requests.get(url)
    html = response.content
    soup = BeautifulSoup(html,"lxml")
    list = soup.find_all('h1', attrs={'class': 'entry-title'})
    return list

def extract_fairy_tail_data_from_dailyanimeart():
    fairy_tail_data = extract_data('https://dailyanimeart.com/category/daily-anime-manga/')
    for entry in fairy_tail_data:
        title = entry.text
        if "Fairy Tail" in title:
            title = title.strip('\n')
            title_info = title.split('Fairy Tail')
            chapter_number = title_info[1]
            chapter_number = chapter_number[1:]

            chapter_name = title_info[0]
            chapter_name = chapter_name[:-2]
            new_title = chapter_number + ' ' + chapter_name
            # print new_title
            break
    return chapter_number

new_episode_no = extract_fairy_tail_data_from_dailyanimeart()
file = open('../new_info.txt','a')
line='dailyanimeart_fairy_tail:' + str(new_episode_no) + '\n'
file.write(line)
