from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import json
from django.contrib.auth import logout as log_out
from django.conf import settings
from django.http import HttpResponseRedirect
from urllib.parse import urlencode

from groups.models import Topics

from .forms import TopicForm

def index(request):
	user = request.user
	if user.is_authenticated:
		return redirect(dashboard)
	else:
		if request.method == 'POST':
			if 'search_topics' in request.POST:
				if request.POST['name']:
					print(request.POST['name'])
					name = request.POST['name']
					found_topics=Topics.objects.filter(name__contains=name)
					topics_list=list(found_topics)
					print(topics_list[0].name)
					return render(request, 'search_results.html',{
						'topics_list' : topics_list,
						})

		return render(request, 'index.html')

@login_required
def dashboard(request):
	user = request.user
	auth0user = user.social_auth.get(provider='auth0')
	userdata = {
		'user_id': auth0user.uid,
		'name': user.first_name,
		'picture': auth0user.extra_data['picture'],
		'email': auth0user.extra_data['email'],
	}

	return render(request, 'dashboard.html', {
		'auth0User': auth0user,
		'userdata': json.dumps(userdata, indent=4)
	})

def logout(request):
	log_out(request)
	return_to = urlencode({'returnTo': request.build_absolute_uri('/')})
	logout_url = 'https://%s/v2/logout?client_id=%s&%s' % \
	(settings.SOCIAL_AUTH_AUTH0_DOMAIN, settings.SOCIAL_AUTH_AUTH0_KEY, return_to)
	return HttpResponseRedirect(logout_url)

def groups(request):
	return render(request, 'groups.html')