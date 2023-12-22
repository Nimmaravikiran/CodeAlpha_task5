import requests
import geocoder
import folium
import pyttsx3
g = geocoder.ip("152.58.196.156")
my_map1 = folium.Map(location=[17.3840, 78.4564], zoom_start=12)
folium.CircleMarker(location=[17.3840, 78.4564], radius=50, popup="My_Address").add_to(my_map1)
folium.Marker([17.3840, 78.4564], popup="My_Address").add_to(my_map1)
my_map1.save("My_map.html ")


def get_geolocation(api_key):
    # Get the user's public IP address
    response = requests.get('https://api.ipify.org?format=json')
    ip_address = response.json()['ip']

    # Use the ipinfo.io API to get geolocation information based on the IP address
    url = f'https://ipinfo.io/152.58.196.156/json?token=64b2caad018d8c'
    response = requests.get(url)
    geolocation_data = response.json()

    return geolocation_data


def main():
    # Replace 'YOUR_API_KEY' with your actual ipinfo.io API key
    api_key = 'https://ipinfo.io/152.58.196.156/json?token=64b2caad018d8c'

    try:
        geolocation_data = get_geolocation(api_key)
        voice = pyttsx3.init()
        voice.say("Details fetching ")
        print("Geolocation Information:")
        print(f"IP Address: {geolocation_data.get('ip')}")
        print(f"City: {geolocation_data.get('city')}")
        print(f"Region: {geolocation_data.get('region')}")
        print(f"Country: {geolocation_data.get('country')}")
        print(f"Location: {geolocation_data.get('loc')}")
        voice.say(f"Your device is located in {geolocation_data.get('city')}. ")
        voice.runAndWait()
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()

