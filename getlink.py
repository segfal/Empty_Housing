import requests
import zipfile
import io


def main():
    url = "https://cdn-charts.streeteasy.com/rentals/Studio.zip"

    rent_data = requests.get(url)
    print(rent_data)
    unzipped = zipfile.ZipFile(io.BytesIO(rent_data.content))
    unzipped.extractall("./zipfiles")


if __name__ == "__main__":
    main()