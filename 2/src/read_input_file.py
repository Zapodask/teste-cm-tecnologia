import json

def read_input_file() -> list[list]:
  try:
    with open('./input.json') as json_file:
      data = json.load(json_file)

    return data
  except:
    raise Exception('Error reading input file')
