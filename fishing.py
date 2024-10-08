import requests
from bs4 import BeautifulSoup

VIVIAN_COUNT = 14
PROVO_COUNT = 4
HOBBLE_COUNT = 0

url = "https://dwrapps.utah.gov/fishstocking/Fish?y=2024"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

print()
print("Running web crawler to check for UDWR fishing updates...")

try:
  response = requests.get(url, headers=headers, timeout=5)
  response.raise_for_status()
except (requests.RequestException, requests.exceptions.Timeout) as e:
  print("ERROR: Could not connect to the internet. Skipping update check.")
else:
  soup = BeautifulSoup(response.text, "lxml")

  if str(soup).count("VIVIAN PARK P") > VIVIAN_COUNT:
      print()
      print("Vivian Park Pond has been stocked! (new stock count: " + str(str(soup).count("VIVIAN PARK P")) + ")")
      print("https://dwrapps.utah.gov/fishstocking/Fish?y=2024")

  if str(soup).count("PROVO R") > PROVO_COUNT:
      print()
      print("The Provo River has been stocked! (new stock count: " + str(str(soup).count("PROVO R")) + ")")
      print("https://dwrapps.utah.gov/fishstocking/Fish?y=2024")

  if str(soup).count("HOBBLE CR") > HOBBLE_COUNT:
      print()
      print("Hobble Creek has been stocked! (new stock count: " + str(str(soup).count("HOBBLE CR")) + ")")
      print("https://dwrapps.utah.gov/fishstocking/Fish?y=2024")

print()
