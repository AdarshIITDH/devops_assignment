import requests
import time
from tabulate import tabulate

def check_subdomain(subdomain):
    url = f"https://{subdomain}.github.com"
    try:
        response = requests.get(url, timeout=5)
        status = "Up" if response.status_code == 200 else "Down"
    except requests.RequestException:
        status = "Down"
    return subdomain, status

def print_table(subdomain_statuses):
    headers = ["Subdomain", "Status"]
    print(tabulate(subdomain_statuses, headers=headers, tablefmt="grid"))

def main():
    subdomains = [
        "gist",
        "help",
        "education",
        "enterprise",
        "developer",
        "status"
    ]
    
    while True:
        subdomain_statuses = [check_subdomain(subdomain) for subdomain in subdomains]
        print_table(subdomain_statuses)
        time.sleep(60)

if __name__ == "__main__":
    main()
