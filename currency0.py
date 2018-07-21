import requests

def main():
    res = requests.get("http://data.fixer.io/api/latest?access_key=3f7fc3be6fd8463aa954fd287dcf98d4&base=EUR&symbols=USD")
    if res.status_code != 200:
        raise Exception(f"ERROR: API request unsuccessful. RC={res.status_code}")
    data = res.json()
    print(data)
 
if __name__ == "__main__":
    main()
