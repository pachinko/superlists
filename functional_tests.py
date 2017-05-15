from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()
        
    def test_can_start_a_list_and_retrive_it_later(self):
        self.browser.get('http://localhost:8000')
        # assert 'To-Do' in self.browser.title, "瀏覽器標題是： " + self.browser.title
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

    # She is invited to enter a to-do item,

    # She typed "buy peacock feathers" into a textbox.

    # When she typed enter, the page updated, now the page lists a item "1: buy peacock feathers".

    # There is still a textbox inviting her to add another item. She enters "use peacock feathers to make a fly"(?)


    # The page updates again, now there are 2 items on her list.


    ## Edith wonders whether the site will remember her list. Then she sees
    # that the site has generated a unique URL for her -- there is some
    # explanatory text to that effect.


    # She visits that URL - her to-do list is still there.

    # Satisfied, she goes back to sleep

if __name__ == '__main__':
    unittest.main(warnings='ignore')
    
    


