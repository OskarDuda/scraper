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

## Summary
The web scraping and downloading parts are separate processes which enables the user to fire and forget the scraping and return to the process once it's done, as long as they have their process ID. 

Currently the download ID is shown to the user after scraping is done, but it is created before scraping is even started, so changing how this is presented to the user should be a minor tweak to the application.

The user interface is non existent right now.

Every time scraping is fired it creates a new folder with new data, which might be a security issue. It's prone to DOS attacks.

The download ID is a folder name, where the scraping output is kept. Although there is no interface for the user to get this ID if he forgets it right, the ID is retrievable, so ID retrieval functionality might be considered in the future. 

App lacks tests right now.