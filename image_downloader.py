# Import the time module (currently not used in this program)
import time

# Import asyncio to run asynchronous functions concurrently
import asyncio

# Import requests to download files from the internet
import requests

# Asynchronous function to download the first image
async def function1():

    # Print a message indicating that function1 has started
    print("func 1")

    # URL of the image to download
    URL = "https://wallpaperaccess.in/public/uploads/preview/1920x1200-desktop-background-ultra-hd-wallpaper-wiki-desktop-wallpaper-4k-.jpg"

    # Send a GET request to the URL
    response = requests.get(URL)

    # Create a new file and write the downloaded image into it
    open("instagram.ico", "wb").write(response.content)

    # Return a value to the caller
    return "Harry"

# Asynchronous function to download the second image
async def function2():

    # Print a message indicating that function2 has started
    print("func 2")

    # URL of the image to download
    URL = "https://p4.wallpaperbetter.com/wallpaper/490/433/199/nature-2560x1440-tree-snow-wallpaper-preview.jpg"

    # Send a GET request
    response = requests.get(URL)

    # Save the downloaded image
    open("instagram2.jpg", "wb").write(response.content)

# Asynchronous function to download the third image
async def function3():

    # Print a message indicating that function3 has started
    print("func 3")

    # URL of the image to download
    URL = "https://c4.wallpaperflare.com/wallpaper/622/676/943/3d-hd-wikipedia-3d-wallpaper-preview.jpg"

    # Send a GET request
    response = requests.get(URL)

    # Save the downloaded image
    open("instagram3.ico", "wb").write(response.content)

# Main asynchronous function
async def main():

    # Run all three asynchronous functions concurrently
    # asyncio.gather() waits until all of them have finished
    # and stores their return values in a list.
    L = await asyncio.gather(
        function1(),
        function2(),
        function3(),
    )

    # Print the list of returned values
    print(L)

# Start the asyncio event loop and execute the main() function
asyncio.run(main())
