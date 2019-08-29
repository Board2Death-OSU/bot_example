
import json
secret_input = open('data/secret.json')
keys = json.load(secret_input)
secret_input.close()

print(keys)