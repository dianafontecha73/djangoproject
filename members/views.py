from django.http import HttpResponse
from django.template import loader
from .models import Member 

# Create your views here.
def members(request):
    
    mymembers = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'mymembers': mymember,
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def testing(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('template.html')
    context = {
        #'mymembers': mymembers,
        #'firstname': 'Jana',
        # 'x' : ['Manzana', 'Banana', 'Cereza'],
        # 'y' : ['Manzana', 'Banana', 'Cereza'],
        'coches' : [{"tipo": "Toyota", "modelo": "Yaris", "año": 2012}, {"tipo": "Renault", "modelo": "Dacia", "año": 2018}],
    }
    return HttpResponse(template.render(context, request))
