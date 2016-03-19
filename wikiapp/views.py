# Date 28th May
# Group: Charne, Cleo, Doug, Jess

from django.shortcuts import render, render_to_response
from django.contrib.auth.models import User
from django.contrib.auth.models import AnonymousUser
from django.contrib import auth
from django.http import HttpResponseRedirect
from models import Article, Content
from datetime import datetime
import markdown
from django.contrib.sessions.models import Session

# Retreiving and appending continent objects containing corresponding 
# country articles to a list to display in continent drop down boxes
def dropdown():
	continent_list = list()

	continent_list.append(Article.objects.filter(article_continent='Africa'))
	continent_list.append(Article.objects.filter(article_continent='Asia'))
	continent_list.append(Article.objects.filter(article_continent='Australia'))
	continent_list.append(Article.objects.filter(article_continent='Europe'))
	continent_list.append(Article.objects.filter(article_continent='North America'))
	continent_list.append(Article.objects.filter(article_continent='South America'))

	return continent_list

# Checks if current user session is authenticated
# in order to determine if the user is a non-user, logged in user or an anonymous user
def check_authentication(request):
	hide_button = 0

	if request.user.is_authenticated():
		hide_button = 1
		if request.user.first_name == 'guest':
			hide_button = 2

	return hide_button

# retreives ip of current client machine to be used when creating anonymous users
def get_client_ip(request):
	x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
	if x_forwarded_for:
		ip=x_forwarded_for.split(',')[0]
	else:
		ip=request.META.get('REMOTE_ADDR')
	return ip

# Displays the join page
def join_page(request):
	hide = check_authentication(request)
	continent_list = dropdown()
	return render(request, "signup.html", {"africa":  continent_list[0], 
										   "asia": continent_list[1],
	 									   "australia": continent_list[2],
	 									   "europe": continent_list[3], 
	 									   "north": continent_list[4], 
	 									   "south": continent_list[5], 
	 									   "hide": hide})

# Displays the user profile page
def user_profile(request):
	hide = check_authentication(request)
	continent_list = dropdown()
	return render(request, "Profile.html", {"africa":  continent_list[0], 
											"asia": continent_list[1],
	 										"australia": continent_list[2], 
	 										"europe": continent_list[3], 
	 										"north": continent_list[4], 
	 										"south": continent_list[5], 
	 										"hide": hide})

# Displays the All country page
def country_page(request):
	hide = check_authentication(request)
	continent_list = dropdown()
	return render(request, "country.html", {"africa":  continent_list[0], 
											"asia": continent_list[1],
	 										"australia": continent_list[2], 
	 										"europe": continent_list[3], 
	 										"north": continent_list[4], 
	 										"south": continent_list[5], 
	 										"hide": hide})

# Displays the log in page
def log_in_page(request):
	hide = check_authentication(request)
	continent_list = dropdown()
	return render(request, "login.html", {"africa":  continent_list[0], 
										  "asia": continent_list[1],
	 									  "australia": continent_list[2], 
	 									  "europe": continent_list[3], 
	 									  "north": continent_list[4], 
	 									  "south": continent_list[5], 

	 									  "hide":hide})

# Displays the help manual
def help_page(request):
	hide = check_authentication(request)
	continent_list = dropdown()
	return render(request, "help.html", {"africa":  continent_list[0], 
										 "asia": continent_list[1],
	 									 "australia": continent_list[2], 
	 									 "europe": continent_list[3], 
	 									 "north": continent_list[4], 
	 									 "south": continent_list[5], 
	 									 "hide":hide})

# Checks the authentication of the current user
# Checks the user input password
def login(request):
	hide = check_authentication(request)
	password_correct= False
	continent_list = dropdown()
	email_content = request.POST['inputEmail']
	password_content = request.POST['inputPassword']
	
	user = auth.authenticate(username=email_content, 
							 password=password_content)
	
	if user is not None and user.is_active:
		auth.login(request, user)

		return HttpResponseRedirect("/wikijourney")

	else:
		return render(request, "login.html", {"africa":  continent_list[0], 
											  "asia": continent_list[1],
											  "australia": continent_list[2], 
											  "europe": continent_list[3], 
											  "north": continent_list[4], 
											  "south": continent_list[5], 
											  "password_incorrect": password_correct, 
											  "hide":hide})

# Flushes the session and logs out
# redirects to the homepage
def logout(request):
	request.session.flush()
	request.session.clear()
	auth.logout(request)
	return HttpResponseRedirect("/wikijourney")

# Displays the home page
def home_page(request):
	hide = check_authentication(request)
	continent_list = dropdown()
	return render(request, "home.html", {"africa":  continent_list[0], 
										 "asia": continent_list[1],
	 									 "australia": continent_list[2], 
	 									 "europe": continent_list[3], 
	 									 "north": continent_list[4], 
	 									 "south": continent_list[5], 
	 									 "hide": hide})

# Checks if entered email address matches any current users addresses
# Promts log in if already exists
# If it does not exist it reads in information and creates new profile
# Then logs in
def create_profile(request):
	hide = check_authentication(request)
	continent_list = dropdown()
	password_correct = False
	email_content = request.POST['inputEmail']
	password_content = request.POST['inputPassword']
	re_password_content = request.POST['inputRePassword']

	try:
		user = User.objects.get(username=email_content)
		exists = True
		if password_content == re_password_content:
			password_correct = True
			
		return render(request, "signup.html", {"africa":  continent_list[0], 
												   "asia": continent_list[1], 
												   "australia": continent_list[2], 
												   "europe": continent_list[3], 
												   "north": continent_list[4], 
												   "south": continent_list[5], 
												   "password_incorrect": password_correct, 
												   "hide": hide, "exists": exists})

	except User.DoesNotExist:
		if password_content == re_password_content:
			password_correct = True
			user = User.objects.create_user(username = email_content, 
										    email=email_content, 
											password=password_content)
			user.save()

			user = auth.authenticate(username=email_content, 
								 password=password_content)

			if user is not None and user.is_active:
				auth.login(request, user)

			return HttpResponseRedirect("/wikijourney/profile")
		else:
			return render(request, "signup.html", {"africa":  continent_list[0], 
												   "asia": continent_list[1], 
												   "australia": continent_list[2], 
												   "europe": continent_list[3], 
												   "north": continent_list[4], 
												   "south": continent_list[5], 
												   "password_incorrect": password_correct, 
												   "hide": hide})

# Obtains the current clients ip address
# Matches to a current guest user
# logs in if match is found
# if not creates the new guest account
def guest(request):
	ip = get_client_ip(request)
	try:
		user = User.objects.get(username=ip)

		user = auth.authenticate(username=ip,
	 						 password='guest')

	 	if user is not None and user.is_active:
	 		auth.login(request, user)

	 	return HttpResponseRedirect("/wikijourney")

	except User.DoesNotExist:

		user = User.objects.create_user(username=ip, 
										first_name='guest', 
										password='guest')
		user.save()

		user = auth.authenticate(username=ip,
								 password='guest')

		if user is not None and user.is_active:
				auth.login(request, user)

		return HttpResponseRedirect("/wikijourney")

# Displays the articles page
# Checks user authentication
# Attempts to get the article from the url name and populate with the content
# if it does not exists it displays the option to create the article
def view_article(request, page_name):
	hide_button = check_authentication(request)
	if not request.user.is_authenticated():
		continent_list = dropdown()
		try:
			article = Article.objects.get(article_title = page_name)
			most_recent_content = article.article_last_revision
			author = article.article_author
			content_list = Content.objects.filter(content_article = article)
		except Article.DoesNotExist:
			return render_to_response("create.html", {"article_name": page_name, 
													  "hide": hide_button, 
													  "africa":  continent_list[0],
													  "asia": continent_list[1],
													  "australia": continent_list[2],
													  "europe": continent_list[3],
													  "north": continent_list[4],
													  "south": continent_list[5]})

		page_content = most_recent_content.content_content
		page_continent = article.article_continent 	
		return render(request, "View Page.html", {"article_name": page_name,
												  "content": markdown.markdown(page_content),
												  "continent": page_continent,
												  "africa":  continent_list[0],
												  "asia": continent_list[1], 
												  "australia": continent_list[2],
												  "europe": continent_list[3], 
												  "north": continent_list[4],
												  "south": continent_list[5],
												  "hide": hide_button,
											      "author": author,
											      "editors": content_list})
	else:
		hide_button = check_authentication(request)
		continent_list = dropdown()
		try:
			article = Article.objects.get(article_title=page_name)
			
			most_recent_content = article.article_last_revision
			author = article.article_author
			content_list = Content.objects.filter(content_article = article)
		except Article.DoesNotExist:
			return render_to_response("create.html", {"article_name": page_name,
													  "africa":  continent_list[0],
													  "asia": continent_list[1], 
													  "australia": continent_list[2], 
													  "europe": continent_list[3],
													  "north": continent_list[4],
													  "south": continent_list[5],
													  "hide": hide_button})

		page_content = most_recent_content.content_content
		page_continent = article.article_continent 	
		return render(request, "View Page.html", {"article_name": page_name,
												  "content": markdown.markdown(page_content),
												  "continent": page_continent,
												  "africa":  continent_list[0],
												  "asia": continent_list[1],
												  "australia": continent_list[2],
												  "europe": continent_list[3], 
												  "north": continent_list[4],
												  "south": continent_list[5],
												  "hide": hide_button,
												  "author": author,
												  "editors": content_list})

# Display the edit interface
# populating it with the latest revised content, calling that by the id saved in the content model
# displays the list of all the selectable revisions which call their object containing content
def edit_article(request, page_name):
	hide = check_authentication(request)
	continent_list = dropdown()
	try:
		article = Article.objects.get(article_title=page_name)
		content_list = Content.objects.filter(content_article = article)
		most_recent_content = article.article_last_revision
		page_content = most_recent_content.content_content
		page_continent = article.article_continent	
		author = article.article_author
	except Article.DoesNotExist:
		content_list = list()

		page_content = ""
		page_continent=""
	return render(request, "Edit Page.html", {"article_name": page_name, 
											  "content": page_content,
											  "list": content_list,
											  "continent": page_continent, 
											  "africa":  continent_list[0],
		 									  "asia": continent_list[1], 
		 									  "australia": continent_list[2], 
		 									  "europe": continent_list[3], 
											  "north": continent_list[4], 
											  "south": continent_list[5], 
											  "hide": hide})

# receives the content from a form
# checks if article already exists
# If it does it updates with new content and editor
# if it does not exist it constructs a new article object as well as a new content object
# assigning the objects the new content
def save_article(request, page_name):
	continent_list = dropdown()

	page_content = request.POST['Content']
	continent_content = request.POST['continent_rad']

	try:
		article = Article.objects.get(article_title=page_name)

	except Article.DoesNotExist:
		author = request.user
		authorname = author.username
		article = Article(article_title = page_name, 
						  article_continent = continent_content, 
						  article_author= authorname)
		article.save()
	content_author = request.user
	content_author_name=content_author.username
	content = Content(content_content= page_content, 
					  content_article= article,
					  content_change_date= datetime.now(), 
					  content_author=content_author_name)
	content.save()

	article.article_last_revision = content
	article.save()

	return HttpResponseRedirect("/wikijourney/" + page_name + "/")

# receives the url to gain access to the id of the article
# uses the id to display article content in a reverted manner
# Reverted artciles can then be saved
def revert(request,page_name):
	url = request.build_absolute_uri()
	splits = url.split('/')
	revertID = splits[7]

	reversion_content = Content.objects.get(content_contentID=revertID)
	article = Article.objects.get(article_title=page_name)
	article.article_last_revision = reversion_content
	article.save()

	return HttpResponseRedirect("/wikijourney/" + page_name + "/")

