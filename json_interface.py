import random, json

def get_starting_inventory():
    file = open('products.json', 'r')
    data = json.load(file)['products']
    sam = random.sample(data, 200)
    return sam