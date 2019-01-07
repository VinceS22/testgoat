from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase): 

    def setUp(self):
        self.browser = webdriver.Firefox()
        
    def tearDown(self):
        self.browser.quit()
        
    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')

        # We want to be able to access a to-do list on the home page
        self.assertIn('To-Do', self.browser.title)
        
        self.fail("Browser title was " + browser.title)

        # We want to be able to add a To-Do item immediately

        # A textbox exists where we can put the information for a to do item.

        # Upon adding it to the list, it should be in a format "'([0-9][:])+ ([a-z]|[A-Z]|[0-9]|\s)+'" For Example: 1. Write annoying regex

        # Make sure the textbox still exists after adding an item

        # Add another item

        # Check existence of both items now.

        # Check the textbox one more time.

        # URL must be in format that contains all to-do information

        # Verify that new link contains the previous items.

if __name__ == '__main__':
    unittest.main(warnings='ignore')