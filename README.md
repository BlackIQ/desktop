# Desktop Wallpaper Changer

As I hate default windows wallpapers, and don't have a good taste in choosing desktop wallpapers, I create a simple tiny tiny script.

## About

In ‍`README.md`, you need to **READ** something. So, **READ** these paragraphes. 😁

### Image

Images are getting randomly from **Unsplash**.

### Changing desktop

I am using **ctypes** and **subprocess** to do this.

### Storing

Here is the part I like! I wanted to store data inside the project directory for example a directory that is in `.gitignore`. But when I thougth about that user is not going to clone the repo! User will run the `desktop.exe` file!

So, I used getting username of user with `getpass.getuser()` and put images in `C:\\Users\username\Pictures\wallpapers`.

## Methods

We have 3 methods.

### `get_random_wallpaper()`

In this method we get an image from unsplash and giving it to `download_image()` method.

But, what is `download_image()` method?

### `download_image()`

Really? You don't know what is `download_image()`? It download the image and store it in C drive.

After downloadimg, we use `set_windows_wallpaper()` method.

### `set_windows_wallpaper()`

I give you 10 seconds to think about this method. What does it do?

Correct! it changes the backgroud.

> Yes, I am funny but you do not understand.

This method use `ctypes` and `subprocess` to change the background.

## Download

You can download the application from **releases**.

---

Have a good time and a good wallpaper 🤞
