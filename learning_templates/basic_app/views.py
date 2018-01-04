from django.shortcuts import render

# Create your views here.
def index(request):
	my_dict = {"name":"haie3r","num": "7"}
	return render(request,"basic_app/index.html",my_dict)

def other(request):
	return render(request,"basic_app/other.html")

def relative(request):
	return render(request,"basic_app/relative_url_templates.html")


