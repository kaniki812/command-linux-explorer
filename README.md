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
git clone https://github.com/kaniki812/command-linux-explorer.git
cd gtfobins-explorer
python3 -m pip install -r requirements.txt
python3 commandEXP.py -h
```
##Usage

Run the script followed by the command you want to fetch exploits for:
```
python3 commandEXP.py <command>
```

## Examples

- Fetch exploits for the cp command:
```python3 commandEXP.py cp```

##Output Example


```[+] Exploits for 'cp':

  → Type: file-write
    Description: It can be used to write arbitrary files.
    Examples:
      [1] Inline code: echo "DATA" | cp /dev/stdin "$LFILE"
      [2] Inline code: echo "DATA" | sudo cp /dev/stdin "$LFILE"

  → Type: suid
    Description: If the SUID bit is set...
    Examples:
      [1] Code block:
sudo install -m =xs $(which cp) .
./cp ...
```

