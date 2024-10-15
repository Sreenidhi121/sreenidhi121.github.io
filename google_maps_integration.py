import googlemaps
from datetime import datetime


API_KEY = "AlzaSyxyC5xNCHsh6LqqjyGDyRoCGVd9_HnXpGz"
gmaps = googlemaps.Client(key="AlzaSyxyC5xNCHsh6LqqjyGDyRoCGVd9_HnXpGz")

def geocode_address(address):
    """
    Converts an address into geographic coordinates (latitude and longitude).
    """
    geocode_result = gmaps.geocode(address)
    if geocode_result:
        location = geocode_result[0]['geometry']['location']
        print(f"Geocoded Address: {address}")
        print(f"Latitude: {location['lat']}, Longitude: {location['lng']}")
        return location
    else:
        print("Geocoding failed.")
        return None

def get_directions(origin, destination):
    """
    Gets driving directions between the origin and destination.
    """
    directions_result = gmaps.directions(origin, destination, mode="driving", departure_time=datetime.now())
    
    if directions_result:
        print(f"\nDirections from {origin} to {destination}:")
        for step in directions_result[0]['legs'][0]['steps']:
            print(step['html_instructions'].replace('<b>', '').replace('</b>', ''))
    else:
        print("No directions found.")

def calculate_distance(origin, destination):
    """
    Calculates distance and duration between two locations.
    """
    distance_result = gmaps.distance_matrix(origins=origin, destinations=destination, mode="driving")
    
    if distance_result['rows'][0]['elements'][0]['status'] == 'OK':
        distance = distance_result['rows'][0]['elements'][0]['distance']['text']
        duration = distance_result['rows'][0]['elements'][0]['duration']['text']
        print(f"\nDistance from {origin} to {destination}: {distance}")
        print(f"Estimated travel time: {duration}")
    else:
        print("Distance calculation failed.")

def get_time_zone(location):
    """
    Gets the time zone for the given location (latitude, longitude).
    """
    lat, lng = location['lat'], location['lng']
    time_zone_result = gmaps.timezone((lat, lng), timestamp=datetime.now())
    if time_zone_result:
        time_zone_id = time_zone_result['timeZoneId']
        time_zone_name = time_zone_result['timeZoneName']
        print(f"\nTime Zone for ({lat}, {lng}): {time_zone_name} (ID: {time_zone_id})")
    else:
        print("Time zone request failed.")

if __name__ == "__main__":
    # Input addresses for testing
    origin_address = "Vnit Nagpur"
    destination_address = "Mumbai"

    # Step 1: Geocode the origin and destination addresses
    origin_location = geocode_address(origin_address)
    destination_location = geocode_address(destination_address)

    if origin_location and destination_location:
        # Step 2: Get directions between the origin and destination
        get_directions(origin_address, destination_address)

        # Step 3: Calculate the distance and time between the origin and destination
        calculate_distance(origin_address, destination_address)

        # Step 4: Get the time zone of the origin location
        get_time_zone(origin_location)
