import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as file:
    return json.load(file)

animals_data = load_data('animals_data.json')
# print(animals_data)
# Write a simple Python script that reads the content of animals_data.json, iterates through the animals, and for each one prints:
# Name
# Diet
# The first location from the locations list
# Type

def print_animal_data(animals_data):
    print(" ")
    for animal in animals_data:
        print(f"Name: {animal['name']}")
        print(f"Diet: {animal['characteristics']['diet']}")
        #print(f"Location: {', '.join(animal['locations'])}")
        print(f"Location: {animal['locations'][0]}")
        if "type" in animal['characteristics']:
            print(f"Type: {animal['characteristics']['type']}")
        print(" ")

print_animal_data(animals_data)
