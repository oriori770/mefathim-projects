import bs4
import requests
from bs4 import BeautifulSoup
import os
import random
import urllib.parse
import re
import urllib.request
from urllib.parse import urlparse
from bs4 import BeautifulSoup

# contents
Maximum_number_of_images_to_download = 20
Maximum_length_for_the_file_name = 20


def building_a_path_for_img(folder, img_url: str):
    end_of_name = (img_url.rsplit('/', 1)[1])
    finel_name = os.path.join('wiki', folder, end_of_name)
    return finel_name

def building_a_path_for_folder(name):
    finel_name = os.path.join('wiki', name)
    return finel_name

def downloaded_img(img_url, folder):
    respons = requests.get(img_url)
    if respons.status_code == 200:
        img_data = requests.get(img_url).content
        with open(folder, 'wb') as handler:
            handler.write(img_data)


def gets_a_page_soup(url):
    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, 'html.parser')
    return soup


def soup_to_title(soup):
    title = soup.title
    title = title.string
    return title


def soup_to_imgs(soup: BeautifulSoup):
    images = soup.find_all('img', class_='mw-file-element')
    # print(images[0].get('src'))
    images_urls = []
    for image in images:
        images_urls.append(image.get('src'))
    return images_urls


def soup_to_links(soup: BeautifulSoup, url):
    links = soup.find_all('a', href=True)
    # print(links)
    ls_link = set()
    for link in links:
        sp_url = link.get('href')
        if sp_url.startswith('/wiki') and ':' not in sp_url:
            ls_link.add(urllib.parse.urljoin(url, sp_url))
    return ls_link

def adding_a_prefix_to_the_site(urls):
    full_urls = urls
    for i in range(len(full_urls)):
        current = full_urls[i]
        if current.startswith('//'):
            full_urls[i] = 'https:' + current
        elif current.startswith('/'):
            full_urls[i] = urllib.parse.urljoin('https:/', current)
    return full_urls

def random_selection_of_images(soup, Links_already_processed):
    # imges_url = []
    # all_imgs = soup.find_all('img', class_="mw-file-element")
    # Random_pictures = random.sample(all_imgs, min(len(all_imgs), 20))
    # for i in range(len(all_imgs)):
    #
    #     src = all_imgs[i].get('src')
    #     if src.startwith('//'):
    #         src = 'http' + src
    #     elif src.startwith('/'):
    #         src = urllib.parse.urljoin(url, src)
    # return Random_pictures
    adding_a_prefix_to_the_site(soup)

def random_selection_of_Links(soup, Links_already_processed, width):
    # all_links = set()
    # for link in soup.find_all('a', href=True):
    #     reference = link.get('href')
    #     wiki_prefix = reference.startswith('/wiki')
    #     not_special_page = ':' not in reference
    #     not_yet_visited = reference not in Links_already_processed
    #     if wiki_prefix and not_yet_visited and not_special_page:
    #         all_links.add(reference)
    #     Random_links = random.sample(all_links, min(len(all_links), width))
    #     return Random_links
    adding_a_prefix_to_the_site(soup)




def crawl_wikipedia(url, folder, depth, width, links_already_processed):
    # Links_already_processed.add(url)
    soup = gets_a_page_soup(url)
    page_directory = os.path.join(folder, soup_to_title(soup))
    os.mkdir(page_directory, exist_ok=True)
    images = random_selection_of_images(soup, )
    for image_url in images:
        downloaded_img(image_url,page_directory)
    progress.update9(1)
    progress.set_description(url)
    if depth > 0:
        linkes = random_selection_of_Links(url, soup, links_already_processed, width)



# print(ghgh('https://en.wikipedia.org/wiki/Terrestrial_locomotion#Rolling'))

wiki = 'https://en.wikipedia.org/wiki/Terrestrial_locomotion#Rolling'
wiki2 = 'https://en.wikipedia.org/wiki/Evolution'
# soup_to_imgs(test_soup)
# print(adding_a_prefix_to_the_site('//upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Muybridge_race_horse_animated.gif/250px-Muybridge_race_horse_animated.gif'))
# print(adding_a_prefix_to_the_site(soup_to_imgs(test_soup)))
def main_Download_photos(link):
    soup = gets_a_page_soup(link)
    ls_imge = soup_to_imgs(soup)
    title = soup_to_title(soup)
    finel_url_img = adding_a_prefix_to_the_site(ls_imge)
    for img in finel_url_img:
        full_path = building_a_path_for_img(title, img)
        folder_path = building_a_path_for_folder(title)
        # print(full_path)
        os.makedirs(folder_path, exist_ok=True)
        downloaded_img(img, full_path)
    # link_in_page = random_selection_of_Links()


def main(link,deep):
    if deep > 0:
        main_Download_photos(link)
        soup = gets_a_page_soup(link)
        ls_link = soup_to_links(soup, link)
        print(type(ls_link))
        for i in ls_link:
            main_Download_photos(i)

        print('done')


main(wiki, 3)


# print(soup_to_links(gets_a_page_soup(wiki2), wiki2))
