import json

with open("animals_template.html", 'r', encoding='utf-8') as html_file:
    html_content = html_file.read()

def load_data(file_path):
  with open(file_path, "r") as file:
    return json.load(file)
animals_data = load_data('animals_data.json')

output = '\n'  # define an empty string
for animal in animals_data:
    # append information to each string
    output += f"Name: {animal['name']}\n"
    output += f"Diet: {animal['characteristics']['diet']}\n"
    output += f"Location: {animal['locations'][0]}\n"
    if "type" in animal['characteristics']:
        output += f"Type: {animal['characteristics']['type']}\n"
    output += "\n"

html_content = html_content.replace("__REPLACE_ANIMALS_INFO__", output)

with open("animals.html", 'w') as new_file:
    new_file.write(html_content)

