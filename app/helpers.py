import yaml
from werkzeug.routing import BaseConverter

def read_yaml_file(yaml_file):
    with open(yaml_file, 'r', encoding='utf-8') as file:
        yaml_file_contents = yaml.safe_load(file)
    return yaml_file_contents

class RegexConverter(BaseConverter):
    def __init__(self, url_map, *items):
        super().__init__(url_map)
        self.regex = items[0]
