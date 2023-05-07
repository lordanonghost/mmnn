import argparse
import whois
import requests
import socket
import urllib.robotparser


def get_whois_info(domain):
    w = whois.whois(domain)
    return w


def get_robots_txt(url):
    domain = url.split("//")[-1].split("/")[0]
    robots_txt_url = f"{url}/robots.txt"
    response = requests.get(robots_txt_url)
    if response.status_code == 200:
        return response.text
    else:
        return f"No robots.txt file found for {domain}"


def get_ip_address(domain):
    ip = socket.gethostbyname(domain)
    return ip


def get_index_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return f"Failed to retrieve index.html for {url}"

#more function
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Website Scanner")

    parser.add_argument("url", type=str, help="URL of the website to scan")
    parser.add_argument("--whois", action="store_true", help="Get WHOIS information")
    parser.add_argument("--robots", action="store_true", help="Get robots.txt content")
    parser.add_argument("--ip", action="store_true", help="Get IP address information")
    parser.add_argument("--index", action="store_true", help="Get index.html content")

    args = parser.parse_args()

    website_url = args.url
    domain = website_url.split("//")[-1].split("/")[0]

    if args.whois:
        whois_info = get_whois_info(domain)
        print("WHOIS Information:")
        print(whois_info)

    if args.robots:
        robots_txt = get_robots_txt(website_url)
        print("\nrobots.txt Content:")
        print(robots_txt)

    if args.ip:
        ip_address = get_ip_address(domain)
        print("\nIP Address:")
        print(ip_address)

    if args.index:
        index_html = get_index_html(website_url)
        print("\nindex.html Content:")
        print(index_html)