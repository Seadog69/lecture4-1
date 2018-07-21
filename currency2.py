import requests

def main():
    base = input("First Currency: ")
    other = input("Second Currency: ")
    # res = requests.get("https://api.fixer.io/latest",
    res = requests.get("http://data.fixer.io/api/latest?access_key=3f7fc3be6fd8463aa954fd287dcf98d4",
                       params={"base": base, "symbols": other})
    if res.status_code != 200:
        raise Exception(f"ERROR: API request unsuccessful. RC={res.status_code}")
    data = res.json()
    rate = data["rates"][other]
    print(f"1 {base} is equal to {rate} {other}")

if __name__ == "__main__":
    main()
