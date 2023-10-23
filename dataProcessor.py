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
  
def average_age_country(file_path):
  try:
    # Dicionário para rastrear as idades por país
    age_by_country = {}

    data = read_json_file(file_path)

    for person in data:
      age = person['age']
      country = person['country']

      # Adiciona a idade à lista de idades do país
      if country in age_by_country:
        age_by_country[country].append(age)
      else:
        age_by_country[country] = [age]

    # Calcula a média de idade por país
    average_ages = {}
    for country, ages in age_by_country.items():
      average_age = sum(ages) / len(ages)
      average_ages[country] = average_age

    return average_ages
  except FileNotFoundError:
    print("O arquivo não foi encontrado")
  except json.JSONDecodeError:
    print("Formato de JSON inválido no arquivo")
  except ZeroDivisionError:
    print("Erro: Valores de idade ausentes ou nulos em todos os registros")
  except Exception as e:
    print("An error occurred while calculating the average age and count.")
    print(e)
