import requests
from bs4 import BeautifulSoup

print("BeautifulSoup is installed successfully!")

# URL of the page to scrape
url = 'https://www.grhosp.on.ca/care/services-departments/emergency/current-emergency-wait'

# Send a GET request to the URL
response = requests.get(url)

# Print the HTTP status code and the first 500 characters of the response
# print("Status Code:", response.status_code)
# print("Content Preview:", response.text[:500])

# Continue if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find the element containing the wait time using the ID
    wait_time = soup.find('div', id='arrival-to-md')
    
    if wait_time:
        print("Current Wait Time:", wait_time.text.strip())
    else:
        print("Wait time element not found.")
else:
    print("Failed to retrieve the webpage")




