import requests
import shutil
import os


def get_random_wallpaper(api_key, smb_target_path):
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
            image = data[0]

            const_data = {
                'url': image["urls"]["full"],
                'name': image['slug']
            }

            image_url = const_data['url']
            image_name = f"{const_data['name']}.jpg"

            wallpaper_dir = os.path.join(smb_target_path, "Unsplash")

            if not os.path.exists(wallpaper_dir):
                os.makedirs(wallpaper_dir)

            image_path = os.path.join(wallpaper_dir, image_name)

            download_image(image_url, image_path)

            smb_destination_path = "//192.168.0.245/wallpapers/test"
            copy_to_smb(image_path, smb_destination_path, "sbbiran.com/a.mohammadi", "123456")
        else:
            print("No wallpapers found.")
    else:
        print("Failed to fetch wallpapers.")


def copy_to_smb(local_path, smb_path, smb_user, smb_password):
    smb_command = f"smbclient {smb_path} -U {smb_user} --password {smb_password} -c 'put {local_path}'"

    os.system(smb_command)
    print("File copied to SMB successfully.")


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
    smb_target_path = "//192.168.0.245/wallpapers"
    get_random_wallpaper(unsplash_api_key, smb_target_path)
