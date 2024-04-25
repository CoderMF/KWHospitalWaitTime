import requests
from bs4 import BeautifulSoup

# URL of the JSON file
GRH_json_url = 'https://www.grhosp.on.ca/assets/documents/current-emergency-waits.json'
SMH_url = 'https://www.smgh.ca/patients-visitors/emergency-department-wait-times'

def json_scraper(url,arrival,patients,date):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse JSON data
        data = response.json()

        # Extracting specific fields
        arrival_to_md = data[arrival]
        patients_waiting = data[patients]
        date_created = data[date]
        texts(arrival,patients,date)
        
    else:
        print("Failed to retrieve data")
        
def scraper (url,arrival,patients,date):
    response = requests.get(url)
    if response.status_code == 200:
    # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find the element containing the wait time using the ID
        wait_time = soup.find('div', class_=patients)
    
        if wait_time:
            print("Current Wait Time:", wait_time.text.strip())
        else:
            print("Element not found.")
    else:
        print("Failed to retrieve the webpage")
        
def texts(arrival,patients,date):
        print("Arrival to MD Time:", arrival)
        print("Patients Waiting:", patients)
        print("Data Last Updated On:", date)

#scraper (GRH_json_url,'arrival-to-md','patients-waiting','date-created')
scraper (SMH_url,'absoluteHorCenter stdStopwatchMiddleText','stdPatientsWaitingText','absoluteHorCenter stdStopwatchBottomText')