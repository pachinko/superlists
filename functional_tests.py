from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()
        
    def test_can_start_a_list_and_retrive_it_later(self):
        # to check out its homepage.
        self.browser.get('http://localhost:8000')
        # assert 'To-Do' in self.browser.title, "瀏覽器標題是： " + self.browser.title
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do'), header_text

#        self.assertIn('To-Do', self.browser.title)

        # She is invited to enter a to-do item,
        inputbox =self.browser.find_element_by_id('id_new_item')
        self.AssertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a To-do item'
            )
        # She typed "buy peacock feathers" into a textbox.
        inputbox.send_keys('Buy peacock feathers')
        # When she typed enter, the page updated, now the page lists a item "1: buy peacock feathers".
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_element_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows)
        )
        # There is still a textbox inviting her to add another item. She enters "use peacock feathers to make a fly"(?)
        self.fail('Finish the test!')


    # The page updates again, now there are 2 items on her list.


    ## Edith wonders whether the site will remember her list. Then she sees
    # that the site has generated a unique URL for her -- there is some
    # explanatory text to that effect.


    # She visits that URL - her to-do list is still there.

    # Satisfied, she goes back to sleep

if __name__ == '__main__':
    unittest.main(warnings='ignore')
    
    


