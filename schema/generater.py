import json
import jsonschema
from jsonschema import validate


def get_schema():
    """This function loads the given schema available"""
    with open(input("Input JSON schema: "), 'r') as file:
        schema = json.load(file)
    return schema


def validate_json(json_data):
    execute_api_schema = get_schema()

    try:
        validate(instance=json_data, schema=execute_api_schema)
    except jsonschema.exceptions.ValidationError as err:
        print(err)
        err = "Given JSON data is InValid"
        return False, err

    message = "Given JSON data is Valid"
    return True, message




# validate it
print(validate_json("json_data"))
