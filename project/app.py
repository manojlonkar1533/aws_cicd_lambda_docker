import requests

def main():
    print("Hello from Docker container!")
    r = requests.get("https://api.github.com")
    print("Status:", r.status_code)

if __name__ == "__main__":
    main()