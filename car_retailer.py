from car import Car
from retailer import Retailer
from order import Order
import random
import time


class CarRetailer(Retailer):
	'''
    A class used to represent a Car Retailer, inheriting from Retailer class

    Attributes
    ----------
    1. retailer_id : int
        The unique identifier for the retailer.
    2. retailer_name : str
        The name of the retailer.
    3. carretailer_address : str
        The address of the car retailer.
    4. carretailer_business_hours : tuple
        The business hours of the car retailer as a tuple (start_time, end_time).
    5. carretailer_stock : list
        A list of car codes representing the retailer's stock.

    Methods
    -------
    1. __init__(retailer_id, retailer_name, carretailer_address, carretailer_business_hours, carretailer_stock)
        Initializes a CarRetailer instance with the given attributes.
    2. __str__()
        Returns a string representation of the CarRetailer instance containing its attributes.
    3. load_current_stock(path="./data/stock.txt")
        Loads the current stock of the car retailer from a file.
    4. is_operating(cur_hour)
        Checks whether the car retailer is operating at the given hour.
    5. get_all_stock()
        Retrieves all the cars in the retailer's stock.
    6. get_postcode_distance(postcode)
        Calculates the distance between the car retailer's address postcode and the given postcode.
    7. remove_from_stock(car_code)
        Removes a car from the retailer's stock based on its car_code.
    8. add_to_stock(car)
        Adds a car to the retailer's stock.
    9. get_stock_by_car_type(car_types)
        Retrieves cars from the retailer's stock based on their car type.
    10. get_stock_by_licence_type(licence_type)
        Retrieves cars from the retailer's stock based on licence type.
    11. car_recommendation()
        Recommends a random car from the retailer's stock.
    12. create_order(car_code)
        Creates an order for a car based on its car_code.
	'''

	def __init__(self, retailer_id = 12345678, retailer_name = "fit store", carretailer_address = "Wellington Road Clayton, VIC 3800", carretailer_business_hours = (8.5, 17.5), carretailer_stock = [] ):
		super().__init__(retailer_id, retailer_name)
		self.carretailer_address = carretailer_address
		self.carretailer_business_hours = carretailer_business_hours
		self.carretailer_stock = carretailer_stock

	def __str__(self):
		return f"{self.retailer_id}, {self.retailer_name}, {self.carretailer_address}, {self.carretailer_business_hours}, {self.carretailer_stock}"
	
	def load_current_stock(self, path = "./data/stock.txt"):
		with open(path, 'r', encoding="UTF-8") as f:
			lines = f.readlines()
			for line in lines:
				data = line.strip().split(', ',6)
				if data[0] == str(self.retailer_id):
					car_datas = data[6].strip("[\' \']").split("', '")
					for raw_car_data in car_datas:
						car_data = raw_car_data.split(", ")
						self.carretailer_stock.append(car_data[0])

	def is_operating(self, cur_hour):
		open_hour, close_hour = map(float, self.carretailer_business_hours)
		return open_hour <= cur_hour <= close_hour
	
	def get_all_stock(self):
		all_stock = []
		with open("./data/stock.txt",'r', encoding="UTF-8") as f:
			lines = f.readlines()
			for line in lines:
				data = line.strip().split(', ',6)
				if data[0] == str(self.retailer_id):
					car_datas = data[6].strip("[\' \']").split("', '")
					for raw_car_data in car_datas:
						car_data = raw_car_data.split(", ")
						car_code, car_name, car_capacity, car_horsepower, car_weight, car_type = car_data
						all_stock.append(Car(car_code, car_name, int(car_capacity), int(car_horsepower), int(car_weight), car_type))
		return all_stock
	
	def get_postcode_distance(self, postcode):
		address_parts = self.carretailer_address.split(", ")
		retailer_postcode = int(address_parts[-1][-4:])
		return abs(retailer_postcode - postcode)
	
	def remove_from_stock(self, car_code):
		if car_code not in self.carretailer_stock:
			return False
	
		with open("./data/stock.txt",'r',encoding="UTF-8") as f:
			lines = f.readlines()
			new_lines = []
			for line in lines:
				data = line.strip().split(', ',6)
				if data[0] == str(self.retailer_id):
					car_datas = data[6].strip("[\' \']").split("', '")
					updated_car_data = []
					for raw_car_data in car_datas:
						car_data = raw_car_data.split(", ")
						if car_data[0] != car_code:
							updated_car_data.append(raw_car_data)
					updated_stock_str = "', '".join(updated_car_data)
					data[6] = f"[\'{updated_stock_str}\']"
					new_line = ', '.join(data)
					new_lines.append(new_line)
				else:
					new_lines.append(line.strip())
				
		with open("./data/stock.txt",'w',encoding="UTF-8") as f:
			for new_line in new_lines:
				f.write(new_line + '\n')
		return True

		
	def add_to_stock(self, car):
		if car.car_code in self.carretailer_stock:
			return False

		with open("./data/stock.txt",'r',encoding="UTF-8") as f:
			lines = f.readlines()
			new_lines = []
			for line in lines:
				data = line.strip().split(', ',6)
				if data[0] == str(self.retailer_id):
					car_datas = data[6].strip("[\' \']").split("', '")
					new_car_data = str(car)
					car_datas.append(new_car_data)
					updated_stock = "['" + "', '".join(car_datas) + "']"
					data[6] = updated_stock
					new_line = ", ".join(data)
					new_lines.append(new_line)
				else:
					new_lines.append(line.strip())

		with open("./data/stock.txt", 'w', encoding="UTF-8") as f:
			for new_line in new_lines:
				f.write(new_line + '\n')
		return True

	def get_stock_by_car_type(self, car_types):
		filtered_stock = []
		with open("./data/stock.txt",'r', encoding="UTF-8") as f:
			lines = f.readlines()
			for line in lines:
				data = line.strip().split(', ',6)
				if data[0] == str(self.retailer_id):
					car_datas = data[6].strip("[\' \']").split("', '")
					for raw_car_data in car_datas:
							car_data = raw_car_data.split(", ")
							if car_data[-1] in car_types:
								car = Car(car_data[0], car_data[1], car_data[2],car_data[3], car_data[4], car_data[5])
								filtered_stock.append(car)
		return filtered_stock

	def get_stock_by_licence_type(self, licence_type):
		allowed_stock = []
		with open("./data/stock.txt",'r', encoding="UTF-8") as f:
			lines = f.readlines()
			for line in lines:
				data = line.strip().split(', ',6)
				if data[0] == str(self.retailer_id):
					car_datas = data[6].strip("[\' \']").split("', '")
					for raw_car_data in car_datas:
						car_data = raw_car_data.split(", ")
						car = Car(car_data[0], car_data[1], int(car_data[2]),int(car_data[3]), int(car_data[4]), car_data[5])
						if licence_type == "P" and car.probationary_licence_prohibited_vehicle():
							continue
						allowed_stock.append(car)
		return allowed_stock
	
	def car_recommendation(self):
		car_objects = []
		with open("./data/stock.txt",'r', encoding="UTF-8") as f:
			lines = f.readlines()
			for line in lines:
				data = line.strip().split(', ',6)
				if data[0] == str(self.retailer_id):
					car_datas = data[6].strip("[\' \']").split("', '")
					for raw_car_data in car_datas:
						car_data = raw_car_data.split(", ")
						car = Car(car_data[0], car_data[1], int(car_data[2]),int(car_data[3]), int(car_data[4]), car_data[5])
						car_objects.append(car)
		if not car_objects:
			return None
		return random.choice(car_objects)
	
	def create_order(self, car_code):
		order_id = Order.generate_order_id(car_code)
		car_object = None
		found = False
		with open("./data/stock.txt",'r', encoding="UTF-8") as f:
			lines = f.readlines()
			for line in lines:
				data = line.strip().split(', ',6)
				if data[0] == str(self.retailer_id):
					car_datas = data[6].strip("[\' \']").split("', '")
					for raw_car_data in car_datas:
						car_data = raw_car_data.split(", ")
						temp_car = Car(car_data[0], car_data[1], int(car_data[2]), int(car_data[3]), int(car_data[4]), car_data[5])
						if temp_car.found_matching_car(car_code):
							car_object = temp_car
							found = True
							break
				if found:
					break
			if not found:
				return None		
		order = Order(order_id, car_object, self, int(time.time()))

		if self.remove_from_stock(car_code):
			with open("./data/order.txt",'a',encoding="UTF-8") as f:
				f.write(str(order) + '\n')
			return order
