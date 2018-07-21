import requests

def main():
    # res = requests.get("https://api.fixer.io/latest?base=USD&symbols=EUR")
    res = requests.get("http://data.fixer.io/api/latest?access_key=3f7fc3be6fd8463aa954fd287dcf98d4&base=EUR&symbols=USD,GBP")
    if res.status_code != 200:
        raise Exception(f"ERROR: API request unsuccessful. RC={res.status_code}")
    data = res.json()
    base = data["base"]
    for key, value in data["rates"].items():
        print(f"1 {base} is equal to {key} {value}")
    # rate = data["rates"]["USD"]
    # print(f"1 {base} is equal to {rate} USD")

if __name__ == "__main__":
    main()
