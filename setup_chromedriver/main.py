import os
import subprocess
import requests
import zipfile
import shutil

# ChromeDriver management functions
def get_chrome_version():
    """Get the version of the installed Chrome browser using the Windows registry."""
    try:
        # Query the Windows registry to get the installed Chrome version
        command = r'reg query "HKEY_CURRENT_USER\Software\Google\Chrome\BLBeacon" /v version'
        version_output = subprocess.check_output(command, shell=True).decode()
        
        # Extract the version number from the command output
        version_line = version_output.strip().split('\n')[-1]
        chrome_version = version_line.split()[-1]
        return chrome_version
    except Exception as e:
        print(f"Error getting Chrome version: {e}")
        return None

def get_chromedriver_version():
    """Get the version of the installed Chromedriver."""
    try:
        chromedriver_path = os.path.join(os.getcwd(), "Chromedriver", "chromedriver.exe")
        if not os.path.exists(chromedriver_path):
            raise FileNotFoundError("Chromedriver executable not found in the expected directory.")
        
        # Execute chromedriver.exe to get its version
        output = subprocess.check_output([chromedriver_path, '--version']).decode().strip()
        return output.split()[1]
    except Exception as e:
        print(f"Error getting Chromedriver version: {e}")
        return None

def download_chromedriver(chrome_version):
    """Download the compatible Chromedriver for the given Chrome version using the specified URL format."""
    if not chrome_version:
        print("Cannot determine Chrome version. Please ensure Chrome is installed correctly.")
        return

    # Construct the download URL using the Chrome version
    download_url = f"https://storage.googleapis.com/chrome-for-testing-public/{chrome_version}/win64/chromedriver-win64.zip"
    
    try:
        # Downloading the zip file
        print(f"Downloading Chromedriver from: {download_url}")
        r = requests.get(download_url, stream=True)
        
        if r.status_code == 200:
            zip_path = os.path.join(os.getcwd(), "chromedriver.zip")
            with open(zip_path, 'wb') as file:
                file.write(r.content)
            
            # Extracting the zip file contents
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall("Chromedriver")
            
            # Move files from 'chromedriver-win64' to 'Chromedriver' folder
            extracted_folder = os.path.join("Chromedriver", "chromedriver-win64")
            if os.path.exists(extracted_folder):
                for file_name in os.listdir(extracted_folder):
                    shutil.move(os.path.join(extracted_folder, file_name), "Chromedriver")
                os.rmdir(extracted_folder)  # Remove the empty folder
            
            # Clean up zip file
            os.remove(zip_path)
            print(f"Downloaded and extracted Chromedriver version: {chrome_version}")
        else:
            print("Failed to download Chromedriver. Please check the URL and Chrome version.")
    
    except Exception as e:
        print(f"Error during Chromedriver download: {e}")

def setup_chromedriver():
    """Ensure Chromedriver is set up correctly with matching Chrome version."""
    if not os.path.exists("Chromedriver"):
        os.makedirs("Chromedriver")
    
    chrome_version = get_chrome_version()
    driver_version = get_chromedriver_version()

    if chrome_version and driver_version and chrome_version.startswith(driver_version.split('.')[0]):
        print("ChromeDriver and Chrome versions are compatible.")
    else:
        print("Updating ChromeDriver to match the Chrome version.")
        download_chromedriver(chrome_version)

# Set up ChromeDriver at application start
setup_chromedriver()

# Set up Chrome driver
# def setup_chrome_driver():
#     chrome_options = Options()
#     # chrome_options.add_argument('--headless')  # Run Chrome in headless mode
#     chrome_options.add_argument('--no-sandbox')  # Disable sandbox
#     chrome_options.add_argument('--disable-dev-shm-usage')  # Overcome limited resources
#     chrome_options.add_argument('--disable-gpu')
#     chrome_service = Service(executable_path='Chromedriver/chromedriver.exe')  # Adjust path if needed
#     return webdriver.Chrome(service=chrome_service, options=chrome_options)