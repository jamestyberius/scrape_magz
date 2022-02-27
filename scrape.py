import requests
from bs4 import BeautifulSoup

from secret_config import EMAIL, CWPW, FORM_ID, AB_KEY
  
URL = "https://www.commonwealmagazine.org"


def cw_login():

    login_url = URL + '/front?destination=front'

    payload = {
        'name':   EMAIL,
        'pass':   CWPW,
        'form_build_id': FORM_ID,
        'form_id':    'user_login_block',
        'antibot_key': AB_KEY,
        'op':	'Log+in'
    }

    r = s.post(login_url, data=payload)

def get_magz():
    # Note: This works when entire issues come in one PDF (2013 - )

    ## TODO: Individual articles are available on issues pages fdor (? - 2012)

    for x in range(7):
        page_soup = get_page(x)
        issue_list = get_issues(page_soup)
        for issue_link in issue_list:
            pdf_link = get_pdf(issue_link)
            download_pdf(pdf_link)


def get_page(x):
    # Go to each year page
    page_url = URL + '/issues?page=' + str(x)
    print(page_url)
    print('Page:' + str(x))
    r = s.get(page_url)
    soup = BeautifulSoup(r.content, 'html5lib')
    return soup

def get_issues(soup):
    # Get list of issues on each page
    table = soup.select('div.field-content a')
    issues = []
    for row in table:
        issues.append(row['href'])

    return issues

def get_pdf(issue):
    r = s.get(URL + issue)
    print('  Issue: ' + issue)
    soup = BeautifulSoup(r.content, 'html5lib')

    pdf_list =  soup.select('div.field-name-download_file a')
    pdf = pdf_list[0]['href']
    print('  ' + pdf)

    return pdf

def download_pdf(pdf_url):
    r = s.get(pdf_url)
    pdf_name = pdf_url.split('/')[-1]
    pdf = open(pdf_name, 'wb')
    pdf.write(r.content)
    pdf.close()
    print('  -Downloaded: ' + pdf_name + '\n')

if __name__ == "__main__":
    with requests.session() as s:
        cw_login()
        get_magz()