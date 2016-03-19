# FUNCTIONAL TESTS:

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#to run this file: $ python manage.py  test functional_tests

class HomePageTests(StaticLiveServerTestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	# The following tests assert that the homepage loads correctly	
	def test_home_page_loads_correctly(self):
		self.browser.get(self.live_server_url)
		self.assertIn('wikijourney - Home', self.browser.title)

		#test to ensure that the footer element loads correctly and contains the correct text
		footer_element = self.browser.find_element_by_id("left-side")
		self.assertTrue(footer_element.text, 'WikiJourney')

class JoinPageTests(StaticLiveServerTestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	# The following tests assert that the homepage loads correctly	
	def test_signup_page_loads_correctly(self):
		self.browser.get(self.live_server_url)
		self.assertIn(b'<h1 id="join_id">Sign up</h1>', response.content)

		#test to ensure that the footer element loads correctly and contains the correct text
		footer_element = self.browser.find_element_by_id("footer")
		self.assertTrue(footer_element.text, 'WikiJourney')

	# The following tests assert that the input placeholder values are correct
	def test_email_placeholders(self):
		self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element_by_id('inputEmail')
        self.assertEqual(
                inputbox.get_attribute('placeholder'),
                'mysupermail@mail.com'

    def test_password_placeholders(self):
		self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element_by_id('inputPassword')
        self.assertEqual(
                inputbox.get_attribute('placeholder'),
                'Password'

    def test_reenter_password_placeholders(self):
		self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element_by_id('inputPasswords')
        self.assertEqual(
                inputbox.get_attribute('placeholder'),
                'eg. X8df!90EO'

    #the following tests assert that the link works correctly 
	# and that the profile page loads correctly	
	def test_profile_page_loads_correctly(self):
		self.browser.get(self.live_server_url)
		self.browser.find_element_by_link_text('Sign up').click()
		page_header = self.browser.find_element_by_id('editjumbo').text
		self.assertIn('Welcome to your profile', page_header)

	def test_login_page_loads_correctly(self):
		self.browser.get(self.live_server_url)
		self.browser.find_element_by_link_text('Log in here').click()
		page_header = self.browser.find_element_by_id('log_id').text
		self.assertIn('Please Log In', page_header)

class LoginPageTests(StaticLiveServerTestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	# The following tests assert that the homepage loads correctly	
	def test_login_page_loads_correctly(self):
		self.browser.get(self.live_server_url)
		self.assertIn(b'<h1 id="log_id">Please Log In</h1>', response.content)

		#test to ensure that the footer element loads correctly and contains the correct text
		footer_element = self.browser.find_element_by_id("footer")
		self.assertTrue(footer_element.text, 'WikiJourney')

	# The following tests assert that the input placeholder values are correct
	def test_email_placeholders(self):
		self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element_by_id('inputEmail')
        self.assertEqual(
                inputbox.get_attribute('placeholder'),
                'Email address'

    def test_password_placeholders(self):
		self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element_by_id('inputPassword')
        self.assertEqual(
                inputbox.get_attribute('placeholder'),
                'Password'

    #the following tests assert that the link works correctly 
	# and that the profile page loads correctly	
	def test_profile_page_loads_correctly(self):
		self.browser.get(self.live_server_url)
		self.browser.find_element_by_link_text('Login').click()
		page_header = self.browser.find_element_by_id('editjumbo').text
		self.assertIn('Welcome to your profile', page_header)

	def test_guest_login_page_loads_correctly(self):
		self.browser.get(self.live_server_url)
		self.browser.find_element_by_link_text('Proceed as guest').click()
		page_header = self.browser.find_element_by_id('editjumbo').text
		self.assertIn('Welcome to your profile', page_header)

class HelpPageTests(StaticLiveServerTestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	# The following tests assert that the homepage loads correctly	
	def test_help_page_loads_correctly(self):
		self.browser.get(self.live_server_url)
		self.assertIn(b'<h1 id="PageHeader">Using the Site</h1>', response.content)

		#test to ensure that the footer element loads correctly and contains the correct text
		footer_element = self.browser.find_element_by_id("footer")
		self.assertTrue(footer_element.text, 'WikiJourney')

class ViewPageTests(StaticLiveServerTestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	# The following tests assert that the homepage loads correctly	
	def test_view_page_loads_correctly(self):
		self.browser.get(self.live_server_url)
		self.assertIn(b'<h1 id="editjumbo">Create a page</h1>', response.content)

		#test to ensure that the footer element loads correctly and contains the correct text
		footer_element = self.browser.find_element_by_id("footer")
		self.assertTrue(footer_element.text, 'WikiJourney')

class EditPageTests(StaticLiveServerTestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	# The following tests assert that the homepage loads correctly	
	def test_edit_page_loads_correctly(self):
		self.browser.get(self.live_server_url)
		self.assertIn(b'<h1 id="PageHeader">Edit</h1>', response.content)

		#test to ensure that the footer element loads correctly and contains the correct text
		footer_element = self.browser.find_element_by_id("footer")
		self.assertTrue(footer_element.text, 'WikiJourney')

class CountryPageTests(StaticLiveServerTestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	# The following tests assert that the link works correctly from the home page
	# and that the categories page loads correctly 
	def test_country_page_loads_correctly(self):
		self.browser.get(self.live_server_url)
	#ensure that all collapsed continent lists are visable by running a loop
	for i in range(1, 7):
		self.assertIn(b'id=\"hide ' + i + ' "', response.content) 

class ProfilePageTests(StaticLiveServerTestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	# the following tests assert that the link works correctly 
	# and that the contact page loads correctly	
	def test_profile_page_loads_correctly(self):
		self.browser.get(self.live_server_url)
		page_header = self.browser.find_element_by_id('page header').text
		self.assertIn(b'<h2 id="bioID">Sign up</h2>', response.content)

