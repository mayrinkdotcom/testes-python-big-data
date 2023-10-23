import json

def read_json_file(file_path):

  try:
    with open(file_path, 'r') as file:
      data = json.load(file)
      return data
  except FileNotFoundError:
    raise FileNotFoundError(f"File not found: {file_path}")
  except json.JSONDecodeError:
    raise ValueError(f"Invalid JSON format in file: {file_path}")
  
def average_age_count(file_path):
  try:
    data = read_json_file(file_path)
    total_age = sum([person['Age'] for person in data])
    count = len(data)
    avg_age = total_age / count if count != 0 else None
    return {"average": avg_age}
  except FileNotFoundError:
    print("O arquivo não foi encontrado")
  except json.JSONDecodeError:
    print("Formato de JSON inválido no arquivo")
  except Exception as e:
    print("An error occurred while calculating the average age and count.")
    print(e)

