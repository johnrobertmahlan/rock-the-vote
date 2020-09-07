from django.shortcuts import render, redirect
import requests

# Create your views here.

def home(request):
    # response = requests.get('https://www.googleapis.com/civicinfo/v2/elections?key=AIzaSyD5XEFhbr4Shpzlq44v6gPSljNyauVnSvs')
    # data = response.json()
    # print(data)
    return render(request, "home.html")

def get_data(request):
    address = request.POST['address']
    print(request.POST)
    if request.method == 'POST' and 'representatives' in request.POST:
        url = f"https://civicinfo.googleapis.com/civicinfo/v2/representatives?address={address}&includeOffices=true&key=AIzaSyD5XEFhbr4Shpzlq44v6gPSljNyauVnSvs"
        response = requests.get(url)
        representatives = response.json()
        print(representatives)
        return render(request, "data.html", {"representatives": representatives})
    else:
        url = f"https://civicinfo.googleapis.com/civicinfo/v2/voterinfo?address={address}&electionId=2000&key=AIzaSyD5XEFhbr4Shpzlq44v6gPSljNyauVnSvs"
        response = requests.get(url)
        elections = response.json()
        print(elections)
        return render(request, "data.html", {"elections": elections})

# def representatives(request):
#     address = request.POST['address']
#     url = f"https://civicinfo.googleapis.com/civicinfo/v2/representatives?address={address}&includeOffices=true&key=AIzaSyD5XEFhbr4Shpzlq44v6gPSljNyauVnSvs"
#     response = requests.get(url)
#     representatives = response.json()
#     print(representatives)
#     return render(request, "data.html", {"representatives": representatives})

# def elections(request):
#     address = request.POST['address']
#     response = requests.get(f"https://civicinfo.googleapis.com/civicinfo/v2/voterinfo?address={address}&electionId=2000&key=AIzaSyD5XEFhbr4Shpzlq44v6gPSljNyauVnSvs")
#     elections = response.json()
#     print(elections)
#     return render(request, "data.html", {"elections": elections})
