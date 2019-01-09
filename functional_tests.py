from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
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
        
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)
        
        # We want to be able to add a To-Do item immediately
        
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # A textbox exists where we can put the information for a to do item.
        
        inputbox.send_keys('Buy acme products')

        # Upon adding it to the list, it should be in a format "'([0-9][:])+ ([a-z]|[A-Z]|[0-9]|\s)+'" For Example: 1. Write annoying regex
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy acme products')
        )
        
        # Make sure the textbox still exists after adding an item
        self.fail('Finish the test!')
        # Add another item

        # Check existence of both items now.

        # Check the textbox one more time.

        # URL must be in format that contains all to-do information

        # Verify that new link contains the previous items.

if __name__ == '__main__':
    unittest.main(warnings='ignore')