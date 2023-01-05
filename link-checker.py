import csv
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

def check_link(url):
  # Send a GET request to the URL
  response = requests.get(url)

  # Check the status code of the response
  if response.status_code == 200:
    print(f'{url} is active')
  else:
    print(f'{url} was not found')

def main():
  # Open the CSV file of links
  with open('links.csv', 'r') as file:
    reader = csv.reader(file)

    # Iterate through each row in the CSV
    for row in reader:
      url = row[0]

      # Check the link
      check_link(url)

if __name__ == '__main__':
  main()