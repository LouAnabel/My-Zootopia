import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as file:
    return json.load(file)

animals_data = load_data('animals_data.json')

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
