import requests
from bs4 import BeautifulSoup
import openpyxl

# Set the URL of the page to be scraped
url = "https://www.ccilindia.com/OMHome.aspx"

# Send a request to the URL and get the HTML response
response = requests.get(url)

# Parse the HTML response using BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Find the table on the page that contains the data to be extracted
table = soup.find("table", {"id": "grdNDSOMReg"})   # ctl00_ContentPlaceHolder1_gvOM 

# Create an Excel workbook to store the extracted data
workbook = openpyxl.Workbook()
worksheet = workbook.active

# Loop through the table rows and extract the data from each cell
row_num = 1
for row in table.find_all("tr"):
    col_num = 1
    cells = row.find_all("td")
    for cell in cells:
        worksheet.cell(row=row_num, column=col_num).value = cell.text
        col_num += 1
    row_num += 1

# Save the workbook to disk
workbook.save("data.xlsx")
