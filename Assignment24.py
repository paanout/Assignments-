import datetime

class Person(object):
    """Abstract Data Type representing a person with name and birthday information.
    
    The implementation details of how names are stored and age is calculated 
    are hidden from users of this class.
    """
    
    def __init__(self, name):
        """Initialize a Person with a name.
        
        Args:
            name: A string representing the full name. Last name is extracted 
                 automatically (everything after last space).
        
        Abstraction: Users don't need to know how we store or parse the name.
        """
        self._name = name  # Internal storage marked with underscore
        try:
            last_blank = name.rindex(' ')
            self._last_name = name[last_blank+1:]
        except ValueError:
            self._last_name = name
        self._birthday = None  # None represents unknown birthday

    def get_name(self):
        """Return the person's full name.
        
        Abstraction: Provides controlled access to the name without exposing 
        implementation details.
        """
        return self._name

    def get_last_name(self):
        """Return the person's last name.
        
        Abstraction: Hides how last names are extracted/stored.
        """
        return self._last_name

    def set_birthday(self, birthdate):
        """Set the person's birthday.
        
        Args:
            birthdate: datetime.date object
            
        Abstraction: Validates input is a date object without exposing storage.
        """
        if not isinstance(birthdate, datetime.date):
            raise TypeError("birthdate must be a datetime.date object")
        self._birthday = birthdate

    def get_age(self):
        """Return the person's age in days.
        
        Returns:
            int: Age in days
            
        Raises:
            ValueError: If birthday hasn't been set
            
        Abstraction: Complex date calculation is hidden behind simple method.
        """
        if self._birthday is None:
            raise ValueError("Birthday not set")
        return (datetime.date.today() - self._birthday).days

    def __lt__(self, other):
        """Compare two people by last name, then full name if last names match.
        
        Abstraction: Comparison logic is encapsulated - users just use < operator.
        """
        if not isinstance(other, Person):
            raise TypeError("Can only compare with other Person objects")
            
        if self._last_name == other._last_name:
            return self._name < other._name
        return self._last_name < other._last_name

    def __str__(self):
        """Return string representation of the person (their full name).
        
        Abstraction: Provides a standard way to convert Person to string.
        """
        return self._name
