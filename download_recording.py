import requests


def main():
    # get audio file from url
    url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-GPXX04C6EN/Testing%20speech%20to%20text.mp3"
    response = requests.get(url)

    if response.status_code == 200:
        with open("downloaded_audio.mp3", "wb") as file:
            file.write(response.content)


if __name__ == "__main__":
    main()
