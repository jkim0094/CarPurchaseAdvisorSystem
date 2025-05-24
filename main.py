import datetime
import string
import random
from car import Car
from car_retailer import CarRetailer


# Display the main menu
def main_menu():
	print("======== Car Purchase Advisor System ========")
	print("a) Look for the nearest car retailer")
	print("b) Get car purchase advice")
	print("c) Place a car order")
	print("d) Exit")

# Generates test data for car retailers and cars
def generate_test_data():
	test_data_carretailer = []
	test_data_cars = []
	# Predefined retailer address list
	carretailer_address_list = ["Wellington Rd Clayton, VIC3168", "Clayton Rd Mount Waverley, VIC3170", "Princes Rd Springvale, VIC3171"]
	# Create random retailer data
	for i in range(3):
		new_carretailer = CarRetailer()
		new_carretailer.generate_retailer_id(test_data_carretailer)

		retailer_name = ''.join(random.choice(string.ascii_letters) for i in range(10))

		carretailer_address = carretailer_address_list[i]

		start_time = round(random.uniform(6.0, 10.0), 1)
		end_time = round(random.uniform(start_time, 23.0), 1)
		carretailer_business_hours = (start_time, end_time)
		new_carretailer.retailer_name = retailer_name
		new_carretailer.carretailer_address = carretailer_address
		new_carretailer.carretailer_business_hours = carretailer_business_hours
		test_data_carretailer.append(new_carretailer)
		with open("./data/stock.txt", "a", encoding="UTF-8") as f:
			f.write(str(new_carretailer)+"\n")

		# Generate random car data for the retailer
		types = ["FWD", "RWD", "AWD"]
		for i in range(4):
			car_code = ''.join(random.choice(string.ascii_letters.upper()) for _ in range(2)) + ''.join(random.choice(string.digits) for _ in range(6))
			while any(car_code in retailer.carretailer_stock for retailer in test_data_carretailer):
				car_code = ''.join(random.choice(string.ascii_letters.upper()) for _ in range(2)) + ''.join(random.choice(string.digits) for _ in range(6))


			length_car_name = random.randint(5, 10)
			car_name = ''.join(random.choice(string.ascii_letters) for i in range(length_car_name))
			car_capacity = random.randint(2, 6)
			car_horsepower = random.randint(100, 400)
			car_weight = random.randint(2000, 4000)
			car_type = random.choice(types)

			new_car = Car(car_code, car_name, car_capacity, car_horsepower, car_weight, car_type)
			test_data_cars.append(new_car)
			new_carretailer.add_to_stock(new_car)
	# Clean and save the stock data
	with open('./data/stock.txt', 'r', encoding='utf-8') as f:
		lines = f.readlines()
	cleaned_lines = []
	for line in lines:
		if "[', " in line:
			line = line.replace("[', ", "[", 1)
			cleaned_lines.append(line)
	with open('./data/stock.txt', 'w', encoding='utf-8') as f:
		f.writelines(cleaned_lines)

# Main function to drive the program
def main():

	retailers = []
	all_cars_list = []

	generate_test_data()
	# Load the car and retailer data from file
	with open('./data/stock.txt', 'r', encoding="UTF-8") as f:
		lines = f.readlines()
		# Parse the retailer and car data
		for line in lines:
			data = line.strip().split(', ',6)
			retailer_id = int(data[0])
			retailer_name = data[1]
			carretailer_address = ", ".join(data[2:4])
			carretailer_business_hours = data[4].strip('('), data[5].strip(')')
			car_strings = data[6][2:-2].split("', '")
			
			cars = []
			carretailer_stock = []
			# Extract car details and create car instances
			for car_string in car_strings:
				car_attributes = car_string.split(", ")
				car_code = car_attributes[0].strip("'")
				car_name = car_attributes[1].strip("'")
				car_capcity = int(car_attributes[2])
				car_horsepower = int(car_attributes[3])
				car_weight = int(car_attributes[4])
				car_type = car_attributes[5].strip("'")
				new_car = Car(car_code, car_name, car_capcity, car_horsepower,car_weight, car_type)
				cars.append(new_car)
				all_cars_list.append(new_car)
				carretailer_stock.append(car_code)

			retailer = CarRetailer(retailer_id, retailer_name, carretailer_address, carretailer_business_hours, carretailer_stock)
			retailers.append(retailer)	

	
	while True:
 	# Display the main menu to the user
		main_menu()

		choice = input("Enter your choice(a ~ d):").strip().lower()

		if choice == 'a':
			try:
				postcode = int(input("Enter your post code:"))
				if 999< postcode < 10000:

					differences = [retailer.get_postcode_distance(postcode) for retailer in retailers]
					min_index = differences.index(min(differences))
					closest_retailer = retailers[min_index]

					if closest_retailer:
						print("Nearest Car Retailer based on postcode you enter is:")
						print(f"Retailer ID : {closest_retailer.retailer_id}")
						print(f"Name : {closest_retailer.retailer_name}")
						print(f"Address : {closest_retailer.carretailer_address}")
						print(f"Business Hours : {closest_retailer.carretailer_business_hours[0]} to {closest_retailer.carretailer_business_hours[1]}")
					else:
						print("No retailers found.")
				else:
					print("Please enter a valid 4-digit postcode.")
			except ValueError:
				print("Please enter a valid 4-digit postcode.")

		elif choice == 'b':
			for index, retailer in enumerate(retailers, 1):
				print(f"{index}, Retailer ID : {retailer.retailer_id}, Name : {retailer.retailer_name}, Address : {retailer.carretailer_address}, Business Hours : {retailer.carretailer_business_hours[0]} to {retailer.carretailer_business_hours[1]}")
			select = None
			while True:
				try:
					select = int(input("\nPlease select a car retailer from the list above: "))
					if 1<= select <= len(retailers):
						selected_retailer = retailers[select - 1]
						break
					else:
						print("Invaild selection. Please select a number from the list.")
				except ValueError:
						print("Please Enter a vaild number.")

			print("\n======== Options ========")
			print("1) Recommend a car")
			print("2) Get all cars in stock")
			print("3) Get cars in stock by car types[AWD, RWD, FWD]")
			print("4) Get probationary licence permitted cars in stock")

			option_choice = None
			while True:
				try:
					option_choice = int(input("\nPlease select an option: "))
					if 1 <= option_choice <= 4:
						break
					else:
						print("invalid selection. Please select a number ( 1 ~ 4 )")
				except ValueError:
					print("Please enter a valid number.")
			
			if option_choice == 1:
				recommended_car = selected_retailer.car_recommendation()
				if recommended_car:
					print("\nWe recommend the following car for you:")
					print("-" * 40)
					print(f"Car Code: {recommended_car.car_code}")
					print(f"Car Name: {recommended_car.car_name}")
					print(f"Capacity: {recommended_car.car_capacity} persons")
					print(f"Horsepower: {recommended_car.car_horsepower} kilowatts")
					print(f"Weight: {recommended_car.car_weight} kg")
					print(f"Drive Type: {recommended_car.car_type}")
					print("-" * 40)
				else:
					print("No cars avialable for recommendation.")

			elif option_choice == 2:
				all_cars = selected_retailer.get_all_stock()
				print(f"\nRetailer ID: {selected_retailer.retailer_id}, Name: {selected_retailer.retailer_name}")
				for car in all_cars:
					print("-" * 40)
					print(f"Car Code: {car.car_code}")
					print(f"Car Name: {car.car_name}")
					print(f"Capacity: {car.car_capacity} persons")
					print(f"Horsepower: {car.car_horsepower} HP")
					print(f"Weight: {car.car_weight} kg")
					print(f"Drive Type: {car.car_type}")
				print("-" * 40)

			elif option_choice == 3:
				car_type_input = input("Please enter car types separated by commas (e.g., AWD, RWD, FWD): ").strip().upper()
				car_types = [car_type.strip() for car_type in car_type_input.split(',')]
				valid_types = {"AWD", "RWD", "FWD"}
				if not all(car_type in valid_types for car_type in car_types):
					print("Invalid type. Please enter car types separated by commas (e.g., AWD, RWD, FWD)")
					continue
				cars_by_types = selected_retailer.get_stock_by_car_type(car_types)
				print(f"\nRetailer ID: {selected_retailer.retailer_id}, Name: {selected_retailer.retailer_name}")
				for car in cars_by_types:
					print("-" * 40)
					print(f"Car Code: {car.car_code}")
					print(f"Car Name: {car.car_name}")
					print(f"Capacity: {car.car_capacity} persons")
					print(f"Horsepower: {car.car_horsepower} kilowatts")
					print(f"Weight: {car.car_weight} kg")
					print(f"Drive Type: {car.car_type}")
				print("-" * 40)

			elif option_choice == 4:
				licence_type = input('\nPlease enter your license type [“L” (Learner Licence), “P” (Probationary Licence), or “Full” (Full Licence)] : ').strip().upper()

				while licence_type not in["L","P","FULL"]:
					print("Invalid licence type. Please enter agia.")
					licence_type = input('\nPlease enter your license type [“L” (Learner Licence), “P” (Probationary Licence), or “Full” (Full Licence)] : ').strip().upper()

				if licence_type == "P":
					permitted_cars = selected_retailer.get_probationary_permitted_cars()
				else:
					permitted_cars = selected_retailer.get_all_stock()

				print(f"\nRetailer ID: {selected_retailer.retailer_id}, Name: {selected_retailer.retailer_name}")
				for car in permitted_cars:
					print("-" * 40)
					print(f"Car Code: {car.car_code}")
					print(f"Car Name: {car.car_name}")
					print(f"Capacity: {car.car_capacity} persons")
					print(f"Horsepower: {car.car_horsepower} kilowatts")
					print(f"Weight: {car.car_weight} kg")
					print(f"Drive Type: {car.car_type}")
				print("-" * 40)

		elif choice == 'c':
			while True:
				try:
					user_inputs = input("Enter the retaielr ID and car ID separated by a space: ").split()
					if len(user_inputs) != 2:
						print("Invalid. Enter the retaielr ID and car ID separated by a space")
						continue

					retailer_id = int(user_inputs[0])
					car_code = user_inputs[1]

					order_retailer = None
					for retailer in retailers:
						if retailer.retailer_id == retailer_id:
							order_retailer = retailer
							break

					if order_retailer is None:
						print("Retailer ID not found. Please try again.")
						continue

					order_car = None
					for car in all_cars_list:
					#for car in order_retailer.carretailer_stock:
						if car.found_matching_car(car_code):
							order_car = car
							break
					
					if order_car is None:
						print("Car ID not found. Please try again.")
						continue
					
					current_hour = datetime.datetime.now().hour + datetime.datetime.now().minute/60.0

					if not order_retailer.is_operating(current_hour):
						print("Sorry! \nWe are unable to take orders as the current time is not the buisness hours")
						break

					new_order = order_retailer.create_order(car_code)
					if new_order:
						print("Order placed successfully!")
						print(f"Order ID: {new_order.order_id}")
						print(f"Car Code: {new_order.order_car.car_code}")
						print(f"Retailer ID: {new_order.order_retailer.retailer_id}")
						print(f"Order Creation Time: {datetime.datetime.fromtimestamp(new_order.order_creation_time).strftime('%Y-%m-%d %H:%M:%S')}")
						break
					else:
						print("Failed to create order. Please try again.")
						continue
				except ValueError:
						print("Invalid input. Please enter the retailer ID and car ID separated by a space.")
		elif choice == 'd':
			print("Existing")
			break

if __name__ == "__main__":
	main()