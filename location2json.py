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

#strings = ["SEABIRD ISLAND DRIVING SCHOOL", "COLLEGE OF THE ROCKIES", "ALL CANADIAN DRIVING SCHOOL 2007", "NORTH ISLAND DRIVING SCHOOL SOCIETY", "BROADWAY DRIVING SCHOOL LIMITED"]

# Loop through each location
for location in locations:
    # Get the name of the location
    name = location.text.strip()

    # Find all the driving schools in the location
    #schools = location.find_next_siblings("blockquote")

    next_sibling = location.find_next_sibling()
    while next_sibling and next_sibling.name != 'h2' and next_sibling.name == "blockquote":
        # Loop through each school
        #for school in schools:
        # Get the details of the school
        details = next_sibling.find_all("div")
        school_name = details[0].text.strip()

        completeAddress = next_sibling.find_all("a")[0].get('href').replace("https://www.google.com/maps/search/?api=1&query=", "")
        #print(completeAddress)    
        #address1 = details[1].text.strip()
        #address2 = details[2].text.strip()
        #print("ffff " + school_name + " ffff " + address1 + " fff " + address2 + " fff " + name)
        
        city = name

        pincode = ""
        for i in range(len(details)):
            if "BC  " in details[i].text.strip():
                tokens = details[i].text.strip().split(" ")
                pincode = tokens[len(tokens)-2] + tokens[len(tokens)-1] 
                break

        #pincode = address2split[3] 
        phone = details[4].text.strip()
        training = details[5].text.strip().split(", ")
    #        certification = details[6].text.strip()

        # Create a dictionary to store the school's data
        school_data = {
            "name": school_name,
            "address": completeAddress,
            "city": city,
            "pincode": pincode,
            "phone": phone,
            "training": training
    #           "certification": certification,
        }

        # Add the school's data to the list
        data.append({"location": name, "school": school_data})
        next_sibling = next_sibling.find_next_sibling()
    

# Convert the data to JSON and write it to a file
with open("driver_training.json", "w") as file:
    json.dump(data, file, indent=4)

