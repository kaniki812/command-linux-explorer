# command-linux-explorer


A simple Python script to fetch and display GTFOBins exploits for any given Linux command.  
The script scrapes https://gtfobins.github.io to retrieve exploit types, descriptions, and examples,  
displaying them in a clean, colorized terminal output.

---

## Features

- Fetches live exploit data for any command available on GTFOBins  
- Displays multiple exploit examples per exploit type  
- Colorful and easy-to-read terminal output  
- Supports help (`-h`) and usage instructions

---

## Requirements

- Python 3.6 or higher  
- [requests](https://pypi.org/project/requests/)  
- [beautifulsoup4](https://pypi.org/project/beautifulsoup4/)  
- [colorama](https://pypi.org/project/colorama/)  

---

## Installation

1. **Clone or download this repository:**

```bash
git clone https://github.com/your-username/gtfobins-explorer.git
cd gtfobins-explorer
python3 -m pip install -r requirements.txt
python3 commandEXP.py -h

##Usage

