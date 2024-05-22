import os
import requests
import time

# Function to fetch observations for a specific species
def fetch_observations_for_species(species_name, page):
    url = f"https://mushroomobserver.org/api2/observations?name={species_name}&page={page}&detail=high&format=json"
    response = requests.get(url)
    if response.status_code == 200:
        try:
            return response.json()
        except ValueError:
            print("Error decoding JSON response")
            return None
    else:
        print(f"Error fetching observations for {species_name}: HTTP {response.status_code}")
        return None

# Function to download an image
def download_image(image_url, folder_name, image_id):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    image_path = os.path.join(folder_name, f"{image_id}.jpg")
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(image_url, headers=headers)
    if response.status_code == 200:
        with open(image_path, 'wb') as file:
            file.write(response.content)
        print(f"{image_id}.jpg downloaded to {folder_name}.")
    else:
        print(f"Failed to download image: {image_url} - HTTP {response.status_code}")

# Main function to fetch and download images for a species
def main(species_name):
    page = 1
    while True:
        data = fetch_observations_for_species(species_name, page)
        if not data or 'results' not in data:
            print("No more data available or error fetching data.")
            break

        for observation in data['results']:
            if isinstance(observation, dict):
                observation_id = observation.get('id')
                if observation_id:
                    primary_image = observation.get('primary_image')
                    if primary_image and 'original_url' in primary_image:
                        image_url = primary_image['original_url']
                        download_image(image_url, species_name, observation_id)
                    else:
                        print(f"No image found for observation {observation_id}.")
                    time.sleep(1)  # To prevent overwhelming the server
            else:
                print(f"Unexpected data type: {type(observation)} - Data: {observation}")

        if page >= data.get('number_of_pages', 1):
            break
        page += 1
        print(f"Page {page} processed.")

    print("All pages processed.")

if __name__ == "__main__":
    species_name = "Amanita muscaria"   # ======>  Please type here the specie of mushroom you want before running the code.
    main(species_name)
