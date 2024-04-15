def test_function():
    print("This is  a test function")



class DBConnection:
    """
    This  is a simple database connection manager. It provides methods to connect, disconnect and get the current connectionA database connection object."""
    
    def __init__(self):
        pass

    def connect(self):
        """
        This  method is used to establish a connection with the database
        """
        print("Connect to data base")