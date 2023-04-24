from django.shortcuts import render
import requests
# Create your views here.
def tempapp(request):
    #desham = request.GET.get("country")
    url =f"https://restcountries.com/v3.1/all"
    #url =f"https://restcountries.com/v3.1/name/{desham}?fullText=true"
    res = requests.get(url)
    response = res.json() 
    
    # payload={ 
    #     "country" : response[1]["name"]["common"],
    #     "capital" : response[1]["capital"][0],
    #     "population" : (int(response[1]["population"])),
    #     "flag" : response[1]["flags"]["png"],
        
    # }

    context = {"response" : response}


    return render(request, 'index.html',context) 