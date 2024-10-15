import googlemaps
from datetime import datetime

# Replace 'YOUR_API_KEY' with your actual Google Maps API Key
API_KEY = "AlzaSyxyC5xNCHsh6LqqjyGDyRoCGVd9_HnXpGz"
gmaps = googlemaps.Client(key=API_KEY)

def geocode_location(address):
    """
    Geocodes an address and returns latitude and longitude.
    """
    geocode_result = gmaps.geocode(address)
    if geocode_result:
        location = geocode_result[0]['geometry']['location']
        print(f"Address: {address}\nLatitude: {location['lat']}, Longitude: {location['lng']}")
        return location
    else:
        print("Geocode failed.")
        return None

def get_directions(origin, destination):
    """
    Gets driving directions between the origin and destination.
    """
    directions_result = gmaps.directions(origin, destination, mode="driving", departure_time=datetime.now())
    
    if directions_result:
        print("\nDriving Directions:")
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

def find_nearby_places(location, place_type, radius=1000):
    """
    Finds nearby places like restaurants, cafes, or gas stations near the specified location.
    """
    places_result = gmaps.places_nearby(location=location, radius=radius, type=place_type)
    
    print(f"\nNearby {place_type}s:")
    if places_result['results']:
        for place in places_result['results'][:5]:  # Show top 5 results
            print(f"- {place['name']}, Rating: {place.get('rating', 'N/A')}, Address: {place.get('vicinity', 'N/A')}")
    else:
        print(f"No nearby {place_type}s found.")

if __name__ == "__main__":
    # Input locations
    origin_address = "VNIT Nagpur"
    destination_address = "Gateway of India, Mumbai"

    # Geocode the locations
    origin_location = geocode_location(origin_address)
    destination_location = geocode_location(destination_address)

    if origin_location and destination_location:
        # Get directions between the two locations
        get_directions(origin_address, destination_address)

        # Calculate distance and time between the two locations
        calculate_distance(origin_address, destination_address)

        # Find nearby restaurants at the destination
        find_nearby_places(destination_location, "restaurant")
        
        # Find nearby gas stations at the origin
        find_nearby_places(origin_location, "gas_station")
