import requests
import argparse
import time
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

# Function to print animated text
def animated_print(text, color=Fore.WHITE, delay=0.005):
    for char in text:
        print(color + char, end='', flush=True)
        time.sleep(delay)
    print(Style.RESET_ALL)

# Banner display with animation
def print_banner():
    banner_lines = [
        "██╗██████╗░██╗░░░░░░█████╗░░█████╗░██╗░░██╗██╗░░░██╗██████╗░",
        "██║██╔══██╗██║░░░░░██╔══██╗██╔══██╗██║░██╔╝██║░░░██║██╔══██╗",
        "██║██████╔╝██║░░░░░██║░░██║██║░░██║█████═╝░██║░░░██║██████╔╝",
        "██║██╔═══╝░██║░░░░░██║░░██║██║░░██║██╔═██╗░██║░░░██║██╔═══╝░",
        "██║██║░░░░░███████╗╚█████╔╝╚█████╔╝██║░╚██╗╚██████╔╝██║░░░░░",
        "╚═╝╚═╝░░░░░╚══════╝░╚════╝░░╚════╝░╚═╝░░╚═╝░╚═════╝░╚═╝░░░░░"
    ]

    # Animate banner lines
    for line in banner_lines:
        animated_print(line, color=Fore.CYAN, delay=0.002)

    print()
    animated_print("🎤IP Address Info Lookup CLI Tool", color=Fore.RED, delay=0.01)
    animated_print("                                                          🛠  Made by: Md.Sojan", color=Fore.RED, delay=0.01)
    print()

# Function to fetch and display IP info
def get_ip_info(ip=None):
    url = f"https://ipwhois.app/json/{ip}" if ip else "https://ipwhois.app/json/"
    try:
        response = requests.get(url)
        data = response.json()

        if not data.get("success", True):
            print(Fore.RED + f"[!] Error: {data.get('message')}")
            return

        print(Fore.GREEN + "\n📡 IP Address Information:")
        print(Fore.YELLOW + "="*40 + Style.RESET_ALL)

        def colored_line(key, value):
            print(Fore.YELLOW + f"{key:<15}:" + Fore.GREEN + f" {value}")

        colored_line("IP Address", data.get('ip'))
        colored_line("Type", data.get('type'))
        colored_line("Continent", data.get('continent'))
        colored_line("Country", f"{data.get('country')} ({data.get('country_code')})")
        colored_line("Region", data.get('region'))
        colored_line("City", data.get('city'))
        colored_line("Latitude", data.get('latitude'))
        colored_line("Longitude", data.get('longitude'))
        colored_line("ISP", data.get('isp'))
        colored_line("Organization", data.get('org'))
        colored_line("ASN", data.get('asn'))
        colored_line("Timezone", data.get('timezone'))
        colored_line("Currency", data.get('currency'))

        print(Fore.YELLOW + "="*40 + Style.RESET_ALL)

    except Exception as e:
        print(Fore.RED + f"[!] Failed to fetch data: {e}")

# CLI entry
def main():
    parser = argparse.ArgumentParser(description="🔍 IP Address Info Lookup (CLI Tool)")
    parser.add_argument("-i", "--ip", help="IP address to lookup (leave blank for your own IP)")
    args = parser.parse_args()
    get_ip_info(args.ip)

# Start
if __name__ == "__main__":
    print_banner()
    main()

print("Thnak you for using iplookup")
print("Hope this information helps you a lots ❤️")
print("Part of Dark Horse")
