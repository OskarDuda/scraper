import os
import urllib
from datetime import datetime
from urllib import request
from bs4 import BeautifulSoup
import zipfile


def get_text_from_html(html):
    soup = BeautifulSoup(html)
    text = soup.get_text()
    return text


def get_sources_from_tags(tags):
    sources = []
    for tag in tags:
        source = 'https:' + tag['src'] if tag['src'].startswith('//') else tag['src']
        sources.append(source)
    return sources


def get_images_srcs_from_html(html):
    soup = BeautifulSoup(html)
    image_tags = soup.findAll('img')
    images_srcs = get_sources_from_tags(image_tags)
    return images_srcs


def parse_html(html):
    text = get_text_from_html(html)
    image_sources = get_images_srcs_from_html(html)
    return text, image_sources


def save_image(source, output_path):
    try:
        urllib.request.urlretrieve(source, output_path)
    except:
        pass


def clear_directory(folder):
    if not os.path.isdir(folder):
        os.makedirs(folder)
    if os.listdir(folder):
        for file in os.listdir(folder):
            file_path = os.path.join(folder, file)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
            except Exception as e:
                pass


def zip_files(folder, zipname):
    zf = zipfile.ZipFile(os.path.join(folder, zipname), 'w', zipfile.ZIP_DEFLATED)
    if not os.path.isdir(folder):
        os.makedirs(folder, )
    elif os.listdir(folder):
        for file in [el for el in os.listdir(folder) if el != zipname]:
            zf.write(os.path.join(folder, file), file)


def save_text(text, output_path):
    full_path = os.path.join(output_path, 'text.txt')
    with open(full_path, 'w+') as f:
        f.write(text)


def get_download_id():
    return datetime.now().strftime('%y_%m_%d_%H_%M_%S_%f')


def main(url, id, output_path='static/scraper/'):
    urllib.parse.unquote(url)
    with urllib.request.urlopen(url) as r:
        html = r.read()
    text, images = parse_html(html)
    output_path = os.path.join(output_path, id)
    clear_directory(output_path)
    save_text(text, output_path)
    for i, image in enumerate(images):
        save_image(image, f'{output_path}/{i}.jpeg')
    zip_files(output_path, 'data.zip')
    return id
