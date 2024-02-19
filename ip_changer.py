import time
import os
import subprocess
import requests
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def install_package(package_name):
    try:
        subprocess.run(['dpkg', '-s', package_name], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        logger.info(f'{package_name} is already installed')
    except subprocess.CalledProcessError:
        logger.info(f'{package_name} not installed, attempting installation...')
        subprocess.run(['sudo', 'apt', 'update'])
        subprocess.run(['sudo', 'apt', 'install', package_name, '-y'])
        logger.info(f'{package_name} installed successfully')

def get_external_ip():
    url = 'https://www.myexternalip.com/raw'
    try:
        response = requests.get(url, proxies=dict(http='socks5://127.0.0.1:9050', https='socks5://127.0.0.1:9050'))
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        logger.error(f'Failed to get external IP: {e}')
        return None

def change_ip():
    try:
        os.system("service tor reload")
        time.sleep(5)  # Wait for Tor to establish connection
        logger.info('Tor service reloaded')
        external_ip = get_external_ip()
        if external_ip:
            logger.info(f'Your IP has been changed to: {external_ip}')
        else:
            logger.warning('Failed to retrieve external IP')
    except Exception as e:
        logger.error(f'Error while changing IP: {e}')

if __name__ == "__main__":
    try:
        install_package('python3-pip')
        install_package('tor')
        install_package('requests')
        install_package('torsocks')
    except Exception as e:
        logger.error(f'An error occurred during installation: {e}')

    os.system("clear")
    logger.info('Starting Tor service...')
    os.system("service tor start")

    x = input("[+] Time to change IP in seconds [type=60] >> ")
    lin = input("[+] How many times do you want to change your IP [type=1000], for infinite IP change type [0] >> ")

    if int(lin) == 0:
        try:
            while True:
                time.sleep(int(x))
                change_ip()
        except KeyboardInterrupt:
            print('\nip_changer is closed')
