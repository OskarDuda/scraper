# Scraping tool
This tool allows for easy scraping of text and images on a given website

## Installation
If you already have an existing Django project skip the below step, otherwise execute:
```bash
django-admin startproject my_project
cd my_project
```
once inside your project:
```bash
git clone 
cd scraper
pip install -r requirements.txt
```
then add the 'scraper' app to your apps in '/my_project/settings.py' under list named 'INSTALLED_APPS'

## How to use
To run the application type the below in your console:
```bash
source venv/bin/activate
cd assessment_project
python manage.py runserver
```
once the server is running the app is ready to use. 

Select a URL to a website you need to scrape and paste below to your browser address field (replacing <url> with the URL of your choice):
```
http://127.0.0.1:8000/scraper/scrape/<url>
```  
after a while an ID will be printed. 

To download the result type below in your browser address field (replacing <id> with ID that was printed in previous step):
```
http://127.0.0.1:8000/scraper/download/<id>
```