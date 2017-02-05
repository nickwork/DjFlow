"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from unipath import Path

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        })

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        })

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        })

def test(request):
    """Renders the test page."""
    assert isinstance(request, HttpRequest)
    # Use Unipath to get folder names from WIP facs_data folder
    # https://github.com/mikeorr/Unipath
    wip_network_path = "\\\\UNC_SHARE\facs_data"
    wip_path = Path(wip_network_path)
    wip_folders = wip_path.listdir(pattern=None,filter=DIRS,names_only=False)
    
    return render(request,
        'app/test.html',
        {
            'title':'Test',
            'message':'Your application description page.',
            'year':datetime.now().year,
        })
