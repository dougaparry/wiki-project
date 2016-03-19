# TESTS:

from django.core.urlresolvers import resolve 
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from wikiapp.views import home_page, join_page, user_profile, country_page, log_in_page, help_page, view_article, edit_article
from wikiapp.models import Content, Article

# To run this file: python manage.py test store

# These tests are run on the homepage and detect 
# whether it runs correctly and contains the correct tags

class HomePageTest(TestCase):
	def test_root_url_resolves_to_home_page_view(self):
		found = resolve('/')
		self.assertEqual(found.func, home_page)

	def test_home_page_returns_correct_html(self):
		request = HttpRequest()
		response = home_page(request)

		self.assertIn(b'<title>wikijourney - Home</title>', response.content)
		self.assertIn(b'<img', response.content)
			self.assertIn(b'src=\"/static/Vietnam/lake.jpg\"', response.content)
			self.assertIn(b'src=\"/static/Zimbabwe/children.jpg\"', response.content)
			self.assertIn(b'src=\"/static/Australia/gbr.jpg\"', response.content)
            
# tests that the join page runs correctly

class JoinPageTest(TestCase):
	def test_join_page_returns_correct_html(self):
		request = HttpRequest()
		response = join_page(request)

		self.assertIn(b'<h1 id="join_id">Sign up</h1>', response.content)

	# This test asserts that the correct images are displayed on the page by checking the src path is correct.

	def test_categories_images_appear_correctly(self):
		request = HttpRequest()
		response = categories_page(request)

		self.assertIn(b'<img', response.content)
			self.assertIn(b'src=\"/static/People/view1.jpg\"', response.content)
            self.assertIn(b'src=\"/static/People/travel.jpg\"', response.content)
            self.assertIn(b'src=\"/static/People/view.jpg\"', response.content)
# These tests assert that the user profile page loads correctly

class ProfilePageTest(TestCase):
	def test_user_profile_returns_correct_html(self):
		request = HttpRequest()
		response = user_profile(request)

		self.assertIn(b'<h1 id="editjumbo">Welcome to your profile</h1>', response.content)

	# This test asserts that the correct images are displayed on the page	

	def test_user_profile_images_appear_correctly(self):
		request = HttpRequest()
		response = user_profile(request)

		self.assertIn(b'<img', response.content)
			self.assertIn(b'src=\"/static/People/avatar.jpg\"', response.content)

# These tests assert that the correct HTML and content loads on the page			

class ContactPageTest(TestCase):
	def test_contact_page_returns_correct_html(self):
		request = HttpRequest()
		response = contact_page(request)

		self.assertIn(b'<h1 id="page header">Contact Douglas & sons</h1>', response.content)

	def test_contact_page_images_appear_correctly(self):
		request = HttpRequest()
		response = contact_page(request)

		self.assertIn(b'<img', response.content)
		self.assertIn(b'src=\"/static/contact1.jpg\"', response.content)




