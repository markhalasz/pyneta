import json
from pprint import pprint

filename = input("Give filename: ")
with open(filename) as f:
	data = json.load(f)
pprint(data)
