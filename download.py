import requests
import os


def get_random_wallpaper(api_key, query, ):
    base_url = "https://api.unsplash.com/photos/random"
    headers = {"Authorization": f"Client-ID {api_key}"}
    params = {
        "query": query,
        "orientation": "landscape",
        "count": 10
    }

    response = requests.get(base_url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        if data and len(data) > 0:
            for image in data:
                const_data = {
                    'url': image["urls"]["full"],
                    'name': image['slug']
                }

                image_url = const_data['url']
                image_name = f"{const_data['name']}.jpg"

                wallpaper_dir = os.path.join("D:\\Unsplash")

                if not os.path.exists(wallpaper_dir):
                    os.makedirs(wallpaper_dir)

                image_path = os.path.join(wallpaper_dir, image_name)

                download_image(image_url, image_path)
        else:
            print("No wallpapers found.")
    else:
        print(f"Failed to fetch wallpapers. Error: {response.status_code}")


def download_image(image_url, image_path):
    response = requests.get(image_url)
    if response.status_code == 200:
        image_data = response.content
        with open(image_path, "wb") as file:
            file.write(image_data)
        print("Wallpaper downloaded successfully.")
    else:
        print("Failed to download the wallpaper.")


if __name__ == "__main__":
    unsplash_api_key = 'G268OqtiBxBzIktxmF2t2Jv_vhQ2iafbqIULlAAJ-O8'
    queries = [
        "mountain desktop wallpaper",
        "sea desktop wallpaper",
        "jungle desktop wallpaper",
        "dark desktop wallpaper",
        "black desktop wallpaper",
        "road desktop wallpaper",
        "tech desktop wallpaper",
        "street desktop wallpaper",
        "italy desktop wallpaper"
        "cafe desktop wallpaper"
    ]
    
    for query in queries:
        get_random_wallpaper(unsplash_api_key, query)
