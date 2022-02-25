import requests
from bs4 import BeautifulSoup

from secret_config import EMAIL, CWPW, FORM_ID, AB_KEY
  
URL = "https://www.commonwealmagazine.org"

issues_urls = []


def cw_login(session):

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
    soup = BeautifulSoup(r.content, 'html5lib')
    print(soup.prettify())


if __name__ == "__main__":
    with requests.session() as s:
        cw_login(s)

        for x in range(7):
            issues_urls.append(URL + '/issues?page=' + str(x))

        
        # Go to each issues page
        i = 0
        for x in issues_urls:

            # For Testing
            if i >= 1:
                break

            print('Page:' + str(i))
            r2 = s.get(x)
            soup = BeautifulSoup(r2.content, 'html5lib')

            # Get list of issues on each page
            table = soup.select('div.field-content a')
            issue_links = []
            for row in table:
                issue = row['href']
                issue_links.append(issue)
                print(issue)

                # For Testing
                if len(issue_links) >= 1:
                    break

            i += 1

            # Go to each issue page and download PDF
            for x in issue_links:
                print(URL + x)
                r3 = s.get(URL + x)
                soup2 = BeautifulSoup(r3.content, 'html5lib')

                pdf_list =  soup2.select('div.field-name-download_file a')
                for x in pdf_list:
                    pdf_link = (x['href'])
                    print(pdf_link)
                    
                    # Turn off actual download while testing
                    '''
                    # Get response object for link
                    response = s.get(pdf_link)
            
                    # Write content in pdf file
                    pdf = open('test.pdf', 'wb')
                    pdf.write(response.content)
                    pdf.close()
                    print("File downloaded")
                    '''
