from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext

from django.conf import settings

from models import *
from forms import *

import facebook
import uuid

def index(request):
    user = facebook.get_user_from_cookie(request.COOKIES, settings.FB_APP_ID, settings.FB_APP_KEY)
    if user:
        graph = facebook.GraphAPI(user["access_token"])
        profile = graph.get_object("me")
        friends = graph.get_connections("me", "friends")        
        print profile.keys()
        print user.keys()
        print user["uid"]
        print profile["id"], profile["name"]
    
    return render_to_response('fbdiscuss/index.html',{'settings':settings}, context_instance=RequestContext(request))

def list(request):
    return render_to_response('fbdiscuss/list.html',{'settings':settings, 'dicussions': Discussion.objects.all()}, context_instance=RequestContext(request))
    
def create(request):
    user = facebook.get_user_from_cookie(request.COOKIES, settings.FB_APP_ID, settings.FB_APP_KEY)
    if request.method == 'POST': # If the form has been submitted...
        form = DiscussionForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            new_discussion = form.save(commit=False);
            new_discussion.guid = str(uuid.uuid1());
            new_discussion.owner = str(user["uid"])
            new_discussion.access_token = str(user["access_token"])
            new_discussion.session_key = str(user["session_key"])
            new_discussion.save()
            return HttpResponseRedirect(reverse('fbdiscuss.discuss', kwargs={'settings':settings, 'guid':new_discussion.guid})) # Redirect after POST
    else:
        form = DiscussionForm() # An unbound form
    
    return render_to_response('fbdiscuss/create.html',{'settings':settings, 'user' : user, 'form' : form }, context_instance=RequestContext(request))
    
def discuss(request, guid):
    discussion = get_object_or_404(Discussion, guid=guid)
    return render_to_response('fbdiscuss/discuss.html',{'settings':settings, "discussion":discussion}, context_instance=RequestContext(request))