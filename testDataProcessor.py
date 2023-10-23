import os
import unittest
from dataProcessor import read_json_file, average_age_country

class TestDataProcessor(unittest.TestCase):
	def test_read_json_file_success(self):
		current_directory = os.path.dirname(__file__)
		file_path = os.path.join(current_directory, "users.json")

		data = read_json_file(file_path)
		
		self.assertEqual(len(data), 1000)  # Ajustar o número esperado de registros
		self.assertEqual(data[0]['name'], 'Mary Yang')
		self.assertEqual(data[1]['age'], 48)
		
		obj_avg_age_country = average_age_country(file_path)
		print("objeto de média de idades por país:", format(obj_avg_age_country))
		self.assertEqual(obj_avg_age_country['BR'], 38.53900709219858)
		

	def test_read_json_file_file_not_found(self):
		with self.assertRaises(FileNotFoundError):
				read_json_file("non_existent.json")

	def test_read_json_file_invalid_json(self):
		with open("invalid.json", "w") as file:
			file.write("invalid json data")
		with self.assertRaises(ValueError):
			read_json_file("invalid.json")

if __name__ == '__main__':
	unittest.main()