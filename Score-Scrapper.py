from playwright.sync_api import sync_playwright
import time
from bs4 import BeautifulSoup

# Launch the browser
with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    
    # Login to the website
    page.goto('https://app.ktu.edu.in/login.htm')
    # credentials to login
    page.fill('input#login-username', 'yourusername')
    page.fill('input#login-password', 'yourpassword')
    page.click('input#btn-login')
    
    # Navigate to the target page
    page.goto('https://app.ktu.edu.in/eu/stu/studentDetailsView.htm') # to avoid the unauthenticated page redirect
    page.goto('https://app.ktu.edu.in/eu/res/semesterGradeCardListing.htm') 
    
    # Select a specific semester
    page.select_option('select#semesterGradeCardListingSearchForm_semesterId', value="1")
    page.click('button#semesterGradeCardListingSearchForm_search')
    
    # Extract the HTML content of the table section
    html = page.inner_html('.step')
    soup = BeautifulSoup(html, 'html.parser')

    # Find the table element
    table = soup.find('table')
    
    # Extract table headers
    headers = [header.get_text(strip=True) for header in table.select('thead tr td')]
    
    # Extract table rows
    data_list = []
    for row in table.select('tbody tr'):
        row_data = {}
        cells = row.find_all('td')
        for idx, cell in enumerate(cells):
            row_data[headers[idx]] = cell.get_text(strip=True)
        data_list.append(row_data)
    
    # Print the extracted data as a list of dictionaries
    print(data_list)
