import json

"""creates the string of all the info for each 
animal that will be added to the json and displayed on the website"""
def serialize_animal(animal):
    output = ' '
    output += "<li class='cards__item'>\n"

    try:
        output += f"<div class='card__title'>{animal['name']}</div><br/>\n"
    except KeyError:
        output += "<div class='card__title'>Unknown</div><br/>\n"
    output += "<div class='card__text'>\n"
    output += "<ul class='info_block'>\n"

    try:
        output += f"<li class='diet'><strong>Diet:</strong> {animal['characteristics']['diet']}<br/>\n"
    except KeyError:
        output += "<li class='diet'><strong>Diet:</strong> Unknown<br/>\n"
    try:
        location_text = ' and '.join(animal['locations'])
    except KeyError:
        location_text = "Unknown"
    except TypeError:
        location_text = "Unknown"
    output += f"<li class='location'><strong>Location:</strong> {location_text}<br/>\n"
    try:
        output += f"<li class='type'><strong>Type:</strong> {animal['characteristics']['type']}\n"
    except KeyError:
        pass
    output += "</ul>\n"
    output += "</div>\n"
    output += "</li>\n"

    return output

def main():
    with open("animals_template.html", 'r', encoding='utf-8') as html_file:
        html_content = html_file.read()

    def load_data(file_path):
        with open(file_path, "r") as file:
            return json.load(file)

    animals_data = load_data('animals_data.json')

    output = ''
    for animal in animals_data:
        output += serialize_animal(animal)

    html_content = html_content.replace("__REPLACE_ANIMALS_INFO__", output)

    with open("animals.html", 'w') as new_file:
        new_file.write(html_content)

if __name__ == "__main__":
    main()
