import sys
import requests
from bs4 import BeautifulSoup
from colorama import init, Fore, Style
import argparse

init(autoreset=True)  # Auto reset colors after print

BASE_URL = "https://gtfobins.github.io/gtfobins/"

def format_command_url(command):
    return f"{BASE_URL}{command}/"

def fetch_gtfobin_page(command):
    url = format_command_url(command)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.RequestException as e:
        print(f"{Fore.RED}[!] Request failed: {e}")
        return None

def parse_exploits(html):
    soup = BeautifulSoup(html, "html.parser")
    exploits = {}

    for h2 in soup.find_all("h2"):
        exploit_type = h2.get("id")
        if not exploit_type:
            continue

        p = h2.find_next_sibling("p")
        description = p.get_text(strip=True) if p else "No description found"

        examples = []
        ul = p.find_next_sibling("ul", class_="examples") if p else None
        if ul:
            for li in ul.find_all("li"):
                example_obj = {}

                # Inline code inside <p><code>
                p_tag = li.find("p")
                if p_tag:
                    code_tag = p_tag.find("code")
                    if code_tag:
                        example_obj['inline'] = code_tag.get_text(strip=True)

                # Code block inside <pre><code>
                pre_tag = li.find("pre")
                if pre_tag:
                    code_block = pre_tag.find("code")
                    if code_block:
                        example_obj['code_block'] = code_block.get_text()

                # If no code found, fallback to li text
                if not example_obj:
                    example_obj['text'] = li.get_text(strip=True)

                examples.append(example_obj)
        else:
            examples.append({"text": "No example found"})

        exploits[exploit_type] = {
            "description": description,
            "examples": examples
        }

    return exploits

def display_exploits(command, exploits):
    print(f"\n{Fore.GREEN}[+] Exploits for '{Fore.YELLOW}{command}{Fore.GREEN}':\n")

    for exploit_type, details in exploits.items():
        print(f"  {Fore.CYAN}→ Type: {Fore.MAGENTA}{exploit_type}")
        print(f"    {Fore.CYAN}Description: {Style.RESET_ALL}{details['description']}")
        print(f"    {Fore.CYAN}Examples:")

        for i, ex in enumerate(details['examples'], 1):
            if 'inline' in ex:
                print(f"      [{i}] Inline code: {Fore.YELLOW}{ex['inline']}{Style.RESET_ALL}")
            if 'code_block' in ex:
                print(f"      [{i}] Code block:\n{Fore.YELLOW}{ex['code_block']}{Style.RESET_ALL}")
            if 'text' in ex:
                print(f"      [{i}] {ex['text']}")

        print()  # Blank line after each exploit type

def main():
    parser = argparse.ArgumentParser(
        description="Fetch and display GTFOBins exploits for a given command.",
        usage="python3 commandEXP.py <command>"
    )
    parser.add_argument('command', nargs='?', help='The binary/command to look up in GTFOBins')
    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    command = args.command
    html = fetch_gtfobin_page(command)

    if not html:
        print(f"{Fore.RED}No exploit found for '{command}'.")
        sys.exit(1)

    exploits = parse_exploits(html)
    if not exploits:
        print(f"{Fore.RED}No exploits parsed for '{command}'.")
        sys.exit(1)

    display_exploits(command, exploits)

if __name__ == "__main__":
    main()
