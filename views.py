from django.http import HttpResponse
from . import scrape_lib

def index(request):
    return HttpResponse("Please specify URL to parse")


def scrape(request, url):
    id = scrape_lib.get_download_id()
    scrape_lib.main(url, id)
    return HttpResponse(f"""
    <h1>ID: {id}</h1>""")


def download(request, id):
    filename = 'data.zip'
    with open(f'static/scraper/{id}/{filename}', 'rb') as zip_file:
        response = HttpResponse(zip_file, content_type='application/force-download')
        response['Content-Disposition'] = 'attachment; filename="%s"' % filename
        return response