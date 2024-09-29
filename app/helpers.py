import yaml

def read_yaml_file(yaml_file):
    with open(yaml_file, 'r', encoding='utf-8') as file:
        yaml_file_contents = yaml.safe_load(file)
    return yaml_file_contents
