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
    output += "<li class='cards__item'><br/>\n"
    output += f"<div class='card__title'>{animal['name']}</div><br/>\n"
    output += "<p class='card__text'><br/>\n"
    output += f"<strong>Diet:</strong> {animal['characteristics']['diet']}<br/>\n"
    output += f"<strong>Location:</strong> {' and '.join(animal['locations'])}<br/>\n"
    if "type" in animal['characteristics']:
        output += f"<strong>Type:</strong> {animal['characteristics']['type']}<br/>\n"
    output += "</p>"
    output += "</li>"

html_content = html_content.replace("__REPLACE_ANIMALS_INFO__", output)

with open("animals.html", 'w') as new_file:
    new_file.write(html_content)


