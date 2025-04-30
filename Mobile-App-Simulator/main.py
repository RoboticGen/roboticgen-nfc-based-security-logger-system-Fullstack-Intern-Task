BASE_URL:str = "Your_API_Endpoint"  # Replace with your API endpoint

LOGIN_URL:str = f"{BASE_URL}/auth/login"
START_PATROL:str = f"{BASE_URL}/patrol/start"
PATROL_SCAN:str = f"{BASE_URL}/patrol/scan"
END_PATROL:str = f"{BASE_URL}/patrol/end"


# You need to implement the following functions to interact with the API with necessary parameters and responses.
# Insted of using actual NFC scanning you can use the Dummy Data provided

def login():
    pass

def start_patrol():
    pass

def scan_location():
    pass

def end_patrol():
    pass

if __name__ == "__main__":
    pass
    # Login to the system
    # Start patrol
    # Simulate scanning locations using the data given in the DummyData
    # End patrol