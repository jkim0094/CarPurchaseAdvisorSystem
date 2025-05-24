
import random
import time
import string

class Order:
	'''
    A class used to represent an Order

    Attributes
    ----------
    1. order_id : str
        A unique identifier for the order.
    2. order_car : Car
        The car associated with the order.
    3. order_retailer : CarRetailer
        The car retailer associated with the order.
    4. order_creation_time : int
        The timestamp when the order was created.

    Methods
    -------
    1. __init__(order_id, order_car, order_retailer, order_creation_time)
        Initializes an Order instance with the given attributes.
    2. __str__()
        Returns a string representation of the Order instance.
    3. generate_order_id(car_code)
        Generates a unique order ID based on the provided car code.
    '''
	def __init__(self, order_id="", order_car = None, order_retailer = None, order_creation_time = None):
		if order_creation_time is None:
			order_creation_time = int(time.time())

		if not order_id and order_car:
			order_id = self.generate_order_id(order_car.car_code)

		self.order_id = order_id
		self.order_car = order_car
		self.order_retailer = order_retailer
		self.order_creation_time = order_creation_time

	def __str__(self):
		return f"{self.order_id}, {self.order_car.car_code}, {self.order_retailer.retailer_id},{self.order_creation_time}"
	
	@classmethod
	def generate_order_id(cls, car_code):
		str_1 = "~!@#$%^&*f"
		random_str = ''.join(random.choice(string.ascii_lowercase) for i in range(6))
		even_upper_str = ''.join([char.upper() if index % 2 else char for index, char in enumerate(random_str)])
		numbers = [(ord(char)**2) % len(str_1) for char in even_upper_str]
		chars_from_str1 = [str_1[i] for i in numbers]
		updated_str = ''.join([even_upper_str[i] + char * i for i, char in enumerate(chars_from_str1)])
		current_time = int(time.time())
		final_str = updated_str + car_code + str(current_time)
		return final_str