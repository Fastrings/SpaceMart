import random, json

def get_starting_inventory():
    file = open('products.json', 'r')
    data = json.load(file)['products']
    sam = random.sample(data, 200)
    for product in sam:
        product['quantity'] = 5
        product['discount'] = 0
        product['remaining_days'] = random.randint(5, 25)
    file.close()
    return sam