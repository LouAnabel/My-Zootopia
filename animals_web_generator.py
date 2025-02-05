import json

with open("animals_template.html", 'r', encoding='utf-8') as html_file:
    html_content = html_file.read()

def load_data(file_path):
  with open(file_path, "r") as file:
    return json.load(file)
animals_data = load_data('animals_data.json')

output = ' '  # define an empty string
for animal in animals_data:
    # append information to each string
    output += '<li class="cards__item">'
    output += f"Name: {animal['name']}<br/>\n"
    output += f"Diet: {animal['characteristics']['diet']}<br/>\n"
    output += f"Location: {animal['locations'][0]}<br/>\n"
    if "type" in animal['characteristics']:
        output += f"Type: {animal['characteristics']['type']}<br/>\n"
    output += '</li>'

print(output)
html_content = html_content.replace("__REPLACE_ANIMALS_INFO__", output)

with open("animals.html", 'w') as new_file:
    new_file.write(html_content)



