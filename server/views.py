# Create your views here.
from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.utils import simplejson
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import list_detail, create_update
from server.models import Post, KML




def KML_detail(request, title):
    print "in KML_detail with title: %s" % title
    kml = KML.objects.get(name=title)
    
    return list_detail.object_list(
                    request,
                    queryset=KML.objects.filter(name=title),
                    template_name='server/kml_list.html',
                    template_object_name="KML"
                    )
@csrf_exempt
def KML_form(request):
    if request.POST:
        
        pass
    print 'in kml form'
    return create_update.create_object(
                    request,
                    model=KML,
                    post_save_redirect='/KML')
    

def post_list(request):
    print 'in post_list'
    return list_detail.object_list(
                    request,
                    queryset=Post.objects.all(),
                    template_object_name='post')

@csrf_exempt
def ep_post(request):
    print 'in ep_post'
    if request.POST:
        print 'POST detected'
        print request.POST
        print 'starting parse'
    return HttpResponse('1')

@csrf_exempt
def post_create_ajax(request):
    print 'in ajax view'
    print request.POST
    text = request.POST['data']
    #print request.POST
    response = {'status' : 'E'}
    try:
        print 'got text %s' % text
        post = Post(data=text)
        post.save()
        print 'got here'
        response['status'] = 'S'
        print 'and here'
    except:
        pass
    json = simplejson.dumps(response)
    return HttpResponse(json, mimetype='application/json')

@csrf_exempt
def post_form(request):
    print 'in post_form'
    if request.is_ajax():
        print 'in post_form ajax'
        text = request.POST['data']
        response = {'status' : 'E'}
        try:
            print 'got text %s' % text
            post = Post(data=text)
            post.save()
            print 'got here'
            response['status'] = 'S'
            print 'and here'
        except:
            pass
        json = simplejson.dumps(response)
        return HttpResponse(json, mimetype='application/json')
        pass
    
    print 'in post_form'
    return create_update.create_object(
                    request,
                    model=Post,
                    post_save_redirect='/posts')
    