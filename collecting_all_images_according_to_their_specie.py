import os
import requests
import time

# Function to get observation details from API
def fetch_observation_details(observation_id):
    url = f"https://mushroomobserver.org/api2/observations/{observation_id}?detail=high&format=json"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Function to retrieve observations from API
def fetch_observations(page):
    url = f"https://mushroomobserver.org/api2/observations?page={page}&format=json"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Function to download the image and save it in the specified folder
def download_image(image_url, folder_name, image_id):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    image_path = os.path.join(folder_name, f"{image_id}.jpg")
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    response = requests.get(image_url, headers=headers)
    if response.status_code == 200:
        with open(image_path, 'wb') as file:
            file.write(response.content)
        print(f"{image_id}.jpg image downloaded to  {folder_name} folder.")
    else:
        print(f"Image failed to download: {image_url} - HTTP Status Code: {response.status_code}")

page = 1
total_pages = 1

while page <= total_pages:
    data = fetch_observations(page)
    if not data or 'results' not in data:
        print(f"Failed to retrieve data or no data found for page : {page}.")
        break

    observation_ids = data['results']
    for observation_id in observation_ids:
        observation = fetch_observation_details(observation_id)
        if observation:
            if 'consensus' in observation['results'][0] and 'name' in observation['results'][0]['consensus']:
                consensus_name = observation['results'][0]['consensus']['name']
                image_data = observation['results'][0].get('primary_image')
                if image_data and 'original_url' in image_data:
                    image_url = image_data['original_url']
                    download_image(image_url, consensus_name, observation_id)
                else:
                    print(f"No image found for observation {observation_id}.")
            else:
                print(f"Observation  {observation_id} is skipped because the consensus name is missing.")
        else:
            print(f"Observation  {observation_id} data could not be retrieved.")
        time.sleep(5)
    
    if 'number_of_pages' in data:
        total_pages = data['number_of_pages']
    
    print(f"Page {page} is completed.")
    page += 1

print("All pages have been processed.")
