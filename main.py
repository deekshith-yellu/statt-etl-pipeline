# main.py
# This script scrapes proposed regulations from the California OAL website
# and saves them as a JSON file. Note that the date of first proposal is
# not available in the source data, so it's excluded to avoid confusion.

import requests
from bs4 import BeautifulSoup
import json
import logging
from datetime import datetime

# Set up basic logging to track what the script is doing
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def scrape_regulations_list(url):
    """Fetch the list of proposed regulations from the given URL."""
    logging.info(f"Starting to scrape regulations from {url}")
    try:
        # Use a User-Agent to avoid being blocked, mimicking a browser
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.90 Safari/537.36'}
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Check if the request was successful
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find the table with the regulations (based on inspected class)
        table = soup.find('table', class_='tablepress-id-9')
        if not table:
            logging.error("Couldn't find the regulations table")
            return []
        
        # Get all rows except the header
        rows = table.find_all('tr')[1:]
        regulations = []
        for row in rows:
            try:
                cells = row.find_all('td')
                # Extract data: OAL File Number, Agency, Subject, File Type
                identifier = cells[0].text.strip()  # Unique ID from the source
                agency = cells[1].text.strip() if len(cells) > 1 else "Unknown"
                title = cells[2].text.strip() if len(cells) > 2 else "Unknown"
                file_type = cells[3].text.strip() if len(cells) > 3 else "Unknown"
                
                # No proposal date available in the source, so skipping it
                regulations.append({
                    'title': title,
                    'identifier': identifier,
                    'full_text': "",  # No text available in source
                    'agency': agency,  # Extra info for bonus
                    'file_type': file_type  # Extra info for bonus
                })
            except Exception as e:
                logging.warning(f"Skipped a row because of an error: {e}")
        return regulations
    except Exception as e:
        logging.error(f"Failed to scrape the list: {e}")
        return []

def transform_data(regulations):
    """Turn the scraped data into the final format with some extra details."""
    logging.info("Processing the scraped data")
    result = []
    for reg in regulations:
        result.append({
            'title': reg['title'],
            'identifier': reg['identifier'],
            'full_text': reg['full_text'],  # Empty due to source limitation
            'agency': reg['agency'],  # Bonus field
            'file_type': reg['file_type'],  # Bonus field
            'source': 'California OAL',  # Extra context
            'scraped_at': datetime.now().isoformat()  # When we grabbed it
        })
    return result

def save_to_json(data, filename='proposed_regulations.json'):
    """Save the data to a JSON file for output."""
    logging.info(f"Saving data to {filename}")
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
    except Exception as e:
        logging.error(f"Couldn’t save the JSON file: {e}")

def main():
    """Run the whole ETL process."""
    url = 'https://oal.ca.gov/proposed-regulations/'
    regulations = scrape_regulations_list(url)
    if not regulations:
        logging.error("No regulations were scraped, so we’re stopping.")
        return
    data = transform_data(regulations)
    save_to_json(data)
    logging.info("ETL process finished successfully!")

if __name__ == '__main__':
    main()