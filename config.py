from configparser import ConfigParser

# Function which gets the required data fields from the database.ini file by using the configparser library to return a dictionary of the data
def getFields():
    parser = ConfigParser()
    parser.read("database.ini")
    data = {}

    # checking if the database.ini file has the intended "postgresql header" to look for the data under
    if parser.has_section("postgresql"):
        fields = parser.items("postgresql")
        # iterating through the fields and assigning values to the dictionary
        for entry in fields:
            data[entry[0]] = entry[1]
    
    else:
        raise Exception("Invalid database.ini file")

    return data 

def parseCursorFetch(curs):
    for item in curs.fetchall():
        a, b = item  # Unpack the tuple
        print("First element:", a)
        print("Second element:", b)
        print()  # Add a blank line between items