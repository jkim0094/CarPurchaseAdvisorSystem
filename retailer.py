import random
class Retailer:
	'''
    A class used to represent a Retailer


    Attributes
    ----------
    1. retailer_id : int
       unique integer of 8 digits
    2. retailer_name : str
		letters and the whitespace character
        
    Methods
    -------
    1. __init__(retailer_id, retailer_name)
    2. __str__()
        : same as value of Retailer instance attributes
        : Return -> str "retailer_id, retailer_name"
    3. generate_retailer_id(list_retailer)
		: Generate a randomly generated unique retailer ID that is different from the existing retailer IDs and set it as the retailer_id
        : list_retailer (A list of all existing retailers)


    '''
	def __init__(self, retailer_id = 12345678, retailer_name = "lucky retailer"):
		self.retailer_id = retailer_id
		#if not re.match("^[A-Za-z\s]+$", retailer_name):
			#raise ValueError("retailer_name can only consist of letters and the whitespace charater.")
		self.retailer_name = retailer_name

	def __str__(self):
		return f"{self.retailer_id}, {self.retailer_name}"
	
	def generate_retailer_id(self, list_retailer):
		while True:
			random_id = random.randint(10000000, 99999999)
			if all(r.retailer_id != random_id for r in list_retailer):
				self.retailer_id = random_id
				break