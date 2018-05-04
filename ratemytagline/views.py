from django.shortcuts import render
from django.http import Http404
from . models import tagLine

def index(request):
    if request.POST:
        tagLine(tagline = request.POST.get("tagline",""),username = request.POST.get("name","")).save()
    taglinesList =  #select all object from tagLine here

    context = {'taglines':''} #set taglinesList to the context so that the template engine can access it

    return render(request,'ratemytagline/index.html') # something seems to be missing !!!

def detail(request,id):
    try:
        tagline = tagLine.objects.get(pk = id)
    except:
        raise Http404("Tagline does not exist")
    if request.POST:
        tagline.numberOfVotes += 1
        #What you save , is what you get
    return render(request,'ratemytagline/details.html',{'tagline':tagline})
