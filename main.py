import subprocess
import requests
import getpass
import random
import ctypes
import os


def get_random_wallpaper(api_key):
    base_url = "https://api.unsplash.com/photos/random"
    headers = {"Authorization": f"Client-ID {api_key}"}
    params = {
        "query": "desktop wallpaper",
        "orientation": "landscape",
        "count": 1
    }

    response = requests.get(base_url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        if data and len(data) > 0:
            image_url = data[0]["urls"]["full"]
            image_name = f"desktop-wallpaper-random-{random.randint(1, 100)}.jpg"

            username = getpass.getuser()

            wallpaper_dir = os.path.join(
                "C:\\Users", username, "Pictures", "wallpapers")
            if not os.path.exists(wallpaper_dir):
                os.makedirs(wallpaper_dir)

            # Construct the full image path
            image_path = os.path.join(wallpaper_dir, image_name)

            download_image(image_url, image_path)
            set_windows_wallpaper(image_path)
        else:
            print("No wallpapers found.")
    else:
        print("Failed to fetch wallpapers.")


def download_image(image_url, image_path):
    response = requests.get(image_url)
    if response.status_code == 200:
        image_data = response.content
        with open(image_path, "wb") as file:
            file.write(image_data)
        print("Wallpaper downloaded successfully.")
    else:
        print("Failed to download the wallpaper.")


def set_windows_wallpaper(image_path):
    reg_command = 'REG ADD "HKEY_CURRENT_USER\\Control Panel\\Desktop" /v Wallpaper /t REG_SZ /d "{}" /f'.format(
        image_path)
    subprocess.run(reg_command, shell=True)

    ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)

    print("Windows wallpaper set successfully.")


if __name__ == "__main__":
    unsplash_api_key = 'G268OqtiBxBzIktxmF2t2Jv_vhQ2iafbqIULlAAJ-O8'
    get_random_wallpaper(unsplash_api_key)
