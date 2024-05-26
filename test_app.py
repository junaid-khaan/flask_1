import unittest
from app import app

class BasicTests(unittest.TestCase):

    # Set up the test client before each test
    def setUp(self):
        # Create a test client using the Flask application configured for testing
        app.config['TESTING'] = True
        self.app = app.test_client()

    # Clean up after each test
    def tearDown(self):
        pass

    # Test the root URL
    def test_home(self):
        # Send a GET request to the root URL
        response = self.app.get('/')
        # Check that the status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        # Check that the response data matches 'Hello, World!'
        self.assertEqual(response.data.decode('utf-8'), 'Hello, World!')

if __name__ == '__main__':
    unittest.main()
