# Unstructured data to be parsed
unstructured_data = """
Center/Daycare
825 23rd Street South
Arlington, VA 22202
703-979-BABY (2229)
22.
Maria Teresa Desaba, Owner/Director; Tony Saba, Org. Director.
Web site: www.mariateresasbabies.com
Serving children 6 wks to 5yrs full-time.

National Science Foundation Child Development Center
23.
4201 Wilson Blvd., Suite 180 22203
703-292-4794
Web site: www.brighthorizons.com 112 children, ages 6 wks–5 yrs.
7:00 a.m. – 6:00 p.m. Summer Camp for children 5–9 years.
"""

# Split the data into individual centers using double newlines as the delimiter
data = unstructured_data.strip().split("\n\n")

# Iterate over each center's data block
for d in data:
    lines = d.split("\n")  # Split the center data into individual lines
    name = lines[0]  # The first line is the name of the center
    address = lines[1] + ", " + lines[2]  # The second and third lines form the address
    phone = lines[3]  # The fourth line is the phone number
    directors = lines[5]  # The sixth line contains the directors' information
    
    # Extract website
    website = ""
    for line in lines:
        if "Web site:" in line:
            website = line.split("Web site: ")[1]
            break

    # Extract services
    services = ""
    for line in lines:
        if "Serving" in line:
            services = line.split("Serving ")[1]
            break
    
    # Extract hours
    hours = ""
    for line in lines:
        if "a.m." in line and "p.m." in line:
            hours = line.strip()
        break

    # Print the extracted information in a formatted manner
    print("==================================================================")
    print(f"Name: {name}")
    print(f"Address: {address}")
    print(f"Phone: {phone}")
    print(f"Directors: {directors}")
    print(f"Website: {website}")
    if services:
        print(f"Services: {services}")
    if hours:
        print(f"Hours: {hours}")
    print("==================================================================")
    print("\n")  # Print a newline for readability between different data
