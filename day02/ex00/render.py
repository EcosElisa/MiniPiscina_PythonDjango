import sys
import re
import os

def create_html(template):
    validate(template[0])
    template_content = read_template(template[0])
    dict_values = load_settings()
    new_contet = update_content(template_content, dict_values)
    create_file(new_contet)

def load_settings():
    settings = {}
    with open("settings.py") as f:
        exec(f.read(), settings)
    return settings

def validate(template):
    if (not (template.endswith(".template"))):
        print("Invalid extension: must be a '.template' file.")
        sys.exit()

def read_template(template):
    try:
        file = open(template, "r")
        content = file.read()
        return content
    except FileNotFoundError:
        print("Error: File cannot be read")

def get_values_settings(settings):
    file = open (settings, "r")
    content = file.read()
    dict = {}

    lines = content.splitlines()

    for line in lines:
        value = line.replace('"', '').split(" = ")
        dict[value[0]] = value[1]

    file.close()
    return dict

def update_content(template_content, dict_values):
    for value in dict_values:
        template_content = re.sub(f'{{{value}}}', f'{dict_values[value]}', template_content)

    template_content = template_content.replace("{", "").replace("}", "")

    return template_content

def create_file(new_content):
    try:
        file = open("result.html", "x")
        file.write(new_content)
        file.close()

    except FileExistsError:
        print("File result.html already exists.")

if __name__ == '__main__':
   
    try:
        if len(sys.argv) != 2:
            print("Usage: python3 render.py <template_file>")
            sys.exit(1)

        template_file = sys.argv[1]
        if not template_file.endswith(".template"):
            print("Error: Invalid file extension. The template file must have the .template extension.")
            sys.exit(1)

        if not os.path.exists(template_file):
            print("Error: The specified template file does not exist.")
            sys.exit(1)

        create_html(sys.argv[1:])

    except Exception as e:
        print(e)