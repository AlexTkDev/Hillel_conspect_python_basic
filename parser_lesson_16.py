import csv
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Headers for sending requests to the server
header = {
    'User-Agent':
         'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:94.0) Gecko/20100101 Firefox/117.0',
    'Accept':
            'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
}

def get_data_by_selenium(url: str) -> str:
    """Function to retrieve HTML content from a URL using Selenium."""
    # Initialize the service for the Firefox driver
    service = Service(path="geckodriver")
    driver = webdriver.Firefox(service=service)
    driver.get(url)  # Navigate to the specified URL
    time.sleep(3)  # Wait for the page to load
    data = driver.page_source  # Get the HTML content of the page
    driver.quit()  # Close the browser
    return data

def parse_data(data: str) -> list:
    """Function to parse data from the HTML document."""
    rez = []
    if data:
        soup = BeautifulSoup(data, 'html.parser')
        li_list = soup.find_all('li', attrs={'class': 'catalog-grid__cell'})
        for li in li_list:
            # Find the <a> tag with the class 'goods-tile__heading'
            a = li.find('a', attrs={'class': 'goods-tile__heading'})
            # Extract the href attribute from the <a> tag
            href = a['href']
            # Extract the text containing the product name
            title = a.text
            # Find the block with the old price
            old = li.find('div', attrs={'class': 'goods-tile__price--old'})
            # Find the block with the current price
            price = li.find('div', attrs={'class': 'goods-tile__price'})
            # Handle the old price (if it exists)
            old_price = ''
            if old:
                old = old.text
                if old:
                    # Extract only digits from the old price text
                    old_price = int(''.join(c for c in old if c.isdigit()))
            # Extract only digits from the current price text
            price = int(''.join(c for c in price.text if c.isdigit()))
            # Store the results for each product as a dictionary
            rez.append({
                'title': title, 'href': href, 'price': price,
                'old_price': old_price
            })
    return rez

def save_to_csv(rows) -> None:
    """Function to save data to a CSV file."""
    csv_title = ['title', 'href', 'price', 'old_price']
    with open('videocards.csv', 'w') as f:
        writer = csv.DictWriter(f, fieldnames=csv_title, delimiter=';')
        writer.writeheader()  # Write the header row
        writer.writerows(rows)  # Write the data rows

def main() -> None:
    """Main function."""
    url = 'https://hard.rozetka.com.ua/videocards/c80087/page={}/'
    rows = []
    for i in range(1, 3):
        data = get_data_by_selenium(url.format(i))  # Retrieve data for each page
        rows += parse_data(data)  # Parse the data and add it to the list
        time.sleep(3)  # Wait before moving to the next page

    save_to_csv(rows)  # Save the data to a CSV file

if __name__ == '__main__':
    main()
