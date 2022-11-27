from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader


# def home(request):
#    #return HttpResponse("Hello, world. You're at the introduction index.")
#    template = loader.get_template('home.html')
#    return HttpResponse(template.render())
#
def about(request):
    """View function for home page of site."""

    member1 = "Soujanya Nayak"
    member2 = 'Andy Cho'
    member3 = 'Margaret De La Torre'
    member4 = 'Martin Salvatierra'
    member5 = 'Qin Geng'
    member6 = 'William Plachno'
    member7 = 'Victor Callejas'

    context = {
        # "indexes" : [1,2,3,4,5,6,7],
        # "members" : [member1,member2,member3,member4,member5,member6,member7],
        # "pages" : ['soujanya', 'andy', 'margaret', 'martin', 'qin', 'william', 'victor'],
        "member1": member1,
        "member2": member2,
        "member3": member3,
        "member4": member4,
        "member5": member5,
        "member6": member6,
        "member7": member7,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'about.html', context=context)


def soujanya(request):
    return render(request, 'soujanya.html')


def andy(request):
    return render(request, 'andy.html')


def margaret(request):
    return render(request, 'margaret.html')


def martin(request):
    return render(request, 'martin.html')


def qin(request):
    return render(request, 'qin.html')


def william(request):
    return render(request, 'william.html')


def victor(request):
    return render(request, 'victor.html')

def HelenLee(request):
    return render(request, 'HelenLee.html')

# def soujanya(request):
#     #return HttpResponse("Hello, world. You're at the introduction index.")
#     template = loader.get_template('soujanya.html')
#     return HttpResponse(template.render())

# def qin(request):
#     #return HttpResponse("Hello, world. You're at the introduction index.")
#     template = loader.get_template('qin.html')
#     return HttpResponse(template.render())

# def about(request):
#     #return HttpResponse("Hello, world. You're at the introduction index.")
#     template = loader.get_template('about.html')
#     return HttpResponse(template.render())
