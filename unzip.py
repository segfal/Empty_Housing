import zipfile


def unzip_file(file_name):
    with zipfile.ZipFile(file_name, 'r') as zip_ref:
        zip_ref.extractall('./rent_data')



def main():
    unzip_file('zipfiles/rentalInventory_Studio.zip')
    unzip_file('zipfiles/medianAskingRent_Studio.zip')

if __name__ == "__main__":
    main()
