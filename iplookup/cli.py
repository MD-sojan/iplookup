import requests
import argparse

def print_banner():
    ascii_art = r"""
 
██╗██████╗░██╗░░░░░░█████╗░░█████╗░██╗░░██╗██╗░░░██╗██████╗░
██║██╔══██╗██║░░░░░██╔══██╗██╔══██╗██║░██╔╝██║░░░██║██╔══██╗
██║██████╔╝██║░░░░░██║░░██║██║░░██║█████═╝░██║░░░██║██████╔╝
██║██╔═══╝░██║░░░░░██║░░██║██║░░██║██╔═██╗░██║░░░██║██╔═══╝░
██║██║░░░░░███████╗╚█████╔╝╚█████╔╝██║░╚██╗╚██████╔╝██║░░░░░
╚═╝╚═╝░░░░░╚══════╝░╚════╝░░╚════╝░╚═╝░░╚═╝░╚═════╝░╚═╝░░░░░ 
  
    🔍 IP Address Info Lookup CLI Tool
    🛠️  Made by: Md.Sojan
    """
    print(ascii_art)

def get_ip_info(ip=None):
    url = f"https://ipwhois.app/json/{ip}" if ip else "https://ipwhois.app/json/"
    try:
        response = requests.get(url)
        data = response.json()

        if not data.get("success", True):
            print(f"[!] Error: {data.get('message')}")
            return

        print("\n📡 IP Address Information:")
        print("="*40)
        print(f"IP Address     : {data.get('ip')}")
        print(f"Type           : {data.get('type')}")
        print(f"Continent      : {data.get('continent')}")
        print(f"Country        : {data.get('country')} ({data.get('country_code')})")
        print(f"Region         : {data.get('region')}")
        print(f"City           : {data.get('city')}")
        print(f"Latitude       : {data.get('latitude')}")
        print(f"Longitude      : {data.get('longitude')}")
        print(f"ISP            : {data.get('isp')}")
        print(f"Organization   : {data.get('org')}")
        print(f"ASN            : {data.get('asn')}")
        print(f"Timezone       : {data.get('timezone')}")
        print(f"Currency       : {data.get('currency')}")
        print("="*40)

    except Exception as e:
        print(f"[!] Failed to fetch data: {e}")
        


def main():
    parser = argparse.ArgumentParser(description="🔍 IP Address Info Lookup (CLI Tool)")
    parser.add_argument("-i", "--ip", help="IP address to lookup (leave blank for your own IP)")
    args = parser.parse_args()
    get_ip_info(args.ip)

if __name__ == "__main__":
    print_banner()
    main()
