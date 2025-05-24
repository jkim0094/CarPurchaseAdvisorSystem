class Car:
    '''
    A class used to represent a Car


    Attributes
    ----------
    1. car_code : str
       two uppercase letters plus 6 digits, e.g., MB123456
    2.  car_name : str
    3. car_capacity : int
        a string to store the video Id to be played.
    4. car_horsepower : int
    5. car_weight : int
    6. car_type : str
        values should be one of “FWD”, “RWD” or “AWD”
    
        
    Methods
    -------
    1. __init__(car_code, car_name, car_capacity, car_horsepower, car_weight , car_type)
    2. __str__()
        : same as value of Car instance attributes
        : Return -> str "car_code, car_name, car_capacity, car_horsepower, car_type"
    3. probationary_licence_prohibited_vehicle()
        : whether the vehicle is a prohibited vehicle for probationary licence drivers
        : Return -> Bool
    4. found_matching_car(car_code)
        : whether the current vehicle is the one to be found based on a car_code.
        : Return -> Bool
    5. get_car_type()
        : car_type of the current car
        : Return -> str "car_type"

    '''

    def __init__(self, car_code="AB123456", car_name = "happycar", car_capacity = 4, car_horsepower = 200, car_weight = 2000, car_type = "FWD"):
        """
        Parameters
        ----------
        1. car_code : str
        2. car_name : str
        3. car_capacity : int
        4. car_horsepower : int
        5. car_weight : int
        6. car_type : str
        """
        self.car_code = car_code
        self.car_name = car_name
        self.car_capacity = car_capacity
        self.car_horsepower = car_horsepower
        self.car_weight = car_weight
        self.car_type = car_type

    def __str__(self):
        return f"{self.car_code}, {self.car_name}, {self.car_capacity}, {self.car_horsepower}, {self.car_weight}, {self.car_type}"
    
    def probationary_licence_prohibited_vehicle(self):
        power_to_mass_ratio = round((self.car_horsepower/self.car_weight),3)*1000
        return power_to_mass_ratio > 130
    
    def found_matching_car(self, car_code):
        """
        Parameters
        ----------
        1. car_code : str
        """
        return self.car_code == car_code
   
    def get_car_type(self):
        return self.car_type