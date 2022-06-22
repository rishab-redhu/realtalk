"""
To render HTML Web Pages
"""

from django.http import HttpResponse
from articles.models import Article
from django.template.loader import render_to_string



def home(request,  *args, **kwargs): #to catch extra objects
    """
    Take in an request and return HTML as a response
    """
    #from the database
    article_querylist=Article.objects.all()

    context= {
        'object_list': article_querylist,
    }
    #Django Template 
    
    HTML_STRING= render_to_string('home.html', context= context)  #converting template (HTML) to string
    
    # H1_STRING= """
    # """.format(**context)
    
    return HttpResponse(HTML_STRING)

