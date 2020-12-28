import requests
from bs4 import BeautifulSoup
import string

KEYWORDS = ['дизайн', 'фото', 'web', 'python', 'программ']
translator = str.maketrans('', '', string.punctuation)


def scanning_page(post):
    hubs = post.find_all('a', class_='hub-link')
    preview = post.find_all('div', class_='post__text')
    post_date = post.find('span', class_='post__time')
    heading = post.find('a', class_='post__title_link')
    link = heading.attrs.get('href')
    heading_text = heading.text.lower().translate(translator).split()
    for word in KEYWORDS:
        if any(word in x for x in heading_text):
            return print(post_date.text, heading.text, link)

    for hub in hubs:
        hub_lower = hub.text.lower()
        if any([hub_lower in desired for desired in KEYWORDS]):
            return print(post_date.text, heading.text, link)

    for preview_text in preview:
        text = preview_text.text.lower().translate(translator).split()
        for word in KEYWORDS:
            if any(word in x for x in text):
                return print(post_date.text, heading.text, link)



response = requests.get('https://habr.com/ru/all/')
soup = BeautifulSoup(response.text, 'html.parser')
posts = soup.find_all('article', class_='post')
for post in posts:
    scanning_page(post)
