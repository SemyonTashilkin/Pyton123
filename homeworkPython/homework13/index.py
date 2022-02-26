import requests
from bs4 import BeautifulSoup
import re
import csv


def get_html(url):
    r = requests.get(url)
    return r.text


def write_csv(data):
    with open('projects.csv', 'a') as f:
        writer = csv.writer(f, lineterminator="\r")
        writer.writerow((data['object'], data['name'], data['url']))


def get_data(html):
    soup = BeautifulSoup(html, "lxml")
    s = soup.find_all("div", class_="projects__item")

    for plugin in s:
        object = plugin.find("p", class_='projects__item--object').text
        name = plugin.find("p", class_="projects__item--desc").find('a').text
        url = plugin.find("p", class_="projects__item--desc").find("a").get("href")

        data = {
            'object': object,
            'name': name,
            'url': url,
        }
        write_csv(data)
    # return plugins


def main():
    url = 'https://sk-gradient.ru/nashi-proekty/'
    print(get_data(get_html(url)))


if __name__ == '__main__':
    main()
