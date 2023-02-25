import json
from bs4 import BeautifulSoup

# Load the HTML file
with open("driver_training.html") as file:
    html = file.read()

# Parse the HTML with BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Find all the locations in the HTML
locations = soup.find_all("h2")

# Create an empty list to store the data
data = []

# Loop through each location
for location in locations:
    # Get the name of the location
    name = location.text.strip()

    # Find all the driving schools in the location
    schools = location.find_next_siblings("blockquote")

    # Loop through each school
    for school in schools:
        # Get the details of the school
        details = school.find_all("div")
        school_name = details[0].text.strip()
        address = details[1].text.strip()
        city = address.split()[-2]
        province = address.split()[-1]
        phone = details[4].text.strip()
        training = details[5].text.strip().split(", ")
#        certification = details[6].text.strip()

        # Create a dictionary to store the school's data
        school_data = {
            "name": school_name,
            "address": address,
            "city": city,
            "province": province,
            "phone": phone,
            "training": training
 #           "certification": certification,
        }

        # Add the school's data to the list
        data.append({"location": name, "school": school_data})

# Convert the data to JSON and write it to a file
with open("driver_training.json", "w") as file:
    json.dump(data, file, indent=4)

