Tor IP Changer
This Python script allows you to change your IP address using Tor's SOCKS proxy. It automates the process of reloading the Tor service and fetching the external IP address.

Features
Change your IP address using Tor
Specify the time interval between IP changes
Option to change the IP address indefinitely
Logs important events and errors for easy debugging
Prerequisites
Python 3.x
Tor service installed and configured
Python requests library
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/Zierax/ip-changer.git
install required Python packages:

bash
Copy code
pip3 install -r requirements.txt
Start the Tor service:

bash
Copy code
service tor start
Usage
Run the script:

bash
Copy code
python3 tor_ip_changer.py
Follow the prompts to specify the time interval and number of IP changes.

Update your SOCKS proxy settings to 127.0.0.1:9050 to route traffic through Tor.

Contributing
Contributions are welcome! Feel free to open issues and pull requests.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
Thanks to the creators of Tor for providing a secure and anonymous way to access the internet.