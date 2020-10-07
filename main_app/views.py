from django.shortcuts import render, redirect
import requests
import json

# Toy Data for Testing UI

# locations = {'pollingLocations': [
#     {
#       'id': 'string',
#       "address": {
#         "locationName": 'High School',
#         "line1": '123 Main St',
#         "line2": 'string',
#         "line3": 'string',
#         "city": 'Town',
#         "state": 'State',
#         "zip": '123456'
#       },
#       "notes": 'string',
#       "pollingHours": '3-4pm',
#       "name": 'string',
#       "voterServices": 'We help',
#       "startDate": 'Today',
#       "endDate": 'Tomorrow',
#       "latitude": 'double',
#       "longitude": 'double',
#       "sources": [
#         {
#           "name": 'string',
#           "official": 'boolean'
#         }
#       ]
#     }
#   ],
#   'earlyVoteSites': [
#     {
#       "id": 'string',
#       "address": {
#         "locationName": 'Someplace',
#         "line1": '456 Old Main St.',
#         "line2": 'string',
#         "line3": 'string',
#         "city": 'Another Town',
#         "state": 'Another State',
#         "zip": '654321'
#       },
#       "notes": 'string',
#       "pollingHours": '4-5pm',
#       "name": 'string',
#       "voterServices": 'I guess',
#       "startDate": 'Yesterday',
#       "endDate": 'Never',
#       "latitude": 'double',
#       "longitude": 'double',
#       "sources": [
#         {
#           "name": 'string',
#           "official": 'boolean'
#         }
#       ]
#     }
#   ],
#   "dropOffLocations": [
#     {
#       "id": 'string',
#       "address": {
#         "locationName": 'Home',
#         "line1": '789 Road',
#         "line2": 'string',
#         "line3": 'string',
#         "city": 'CityTown',
#         "state": 'StatePlace',
#         "zip": '13579'
#       },
#       "notes": 'string',
#       "pollingHours": '5-6pm',
#       "name": 'string',
#       "voterServices": 'Occasionally',
#       "startDate": '2312 A.D.',
#       "endDate": 'The Big Crunch',
#       "latitude": 'double',
#       "longitude": 'double',
#       "sources": [
#         {
#           "name": 'string',
#           "official": 'boolean'
#         }
#       ]
#     }
#   ]
# }


# Create your views here.

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def get_data(request):
    address = request.POST['address']
    print(request.POST)
    if request.method == 'POST' and 'representatives' in request.POST:
        url = f"https://civicinfo.googleapis.com/civicinfo/v2/representatives?address={address}&includeOffices=true&key=AIzaSyD5XEFhbr4Shpzlq44v6gPSljNyauVnSvs"
        response = requests.get(url)
        representatives = response.json()
        json_reps = json.loads(response.text)
        offices = json_reps['offices']
        officials = json_reps['officials']
        names = []
        indices = []
        heldOffice = {}
        realOffice = {}
        electedOffice = {}
        test_representatives = {}
        print(type(officials))
        for office in offices:
            names.append(office['name'])
            indices.append(office['officialIndices'])
            idxs = tuple(office['officialIndices'])
            heldOffice[office['name']] = office['officialIndices']
            realOffice[idxs] = office['name']
            for key, value in realOffice.items():
                print(key, value)
        
        for official_idx, official in enumerate(officials):
            test_representatives[official_idx] = official
            for office_idx, office in enumerate(offices):
                if official_idx in office['officialIndices']:
                    test_representatives[official_idx]['office'] = office
        
        print(test_representatives)
        
        # for official in officials:
        #     idx = officials.index[official]
        #     print(idx)
        #     electedOffice[official['name']] = offices['officialIndices'[idx]]
        

        
            # print(realOffice)
        #     for idx in idxs:
        #         realOffice[idx] = office['name']
        #     return realOffice
        # print(realOffice)
        #     for index in indices:
        #         if len(index) == 1:
        #             index = index.join()
        #             realOffice[index] = office['name']
        #         else:
        #             for idx in index:
        #                 realOffice[idx] = office['name']
        #         return realOffice
        # print(realOffice)
        officeIndices = heldOffice.values()
        # print(realOffice[(4,)])
        # print(len(offices))
        # print(len(officials))
        # print(electedOffice)
        # print(names)
        # print(indices)
        # print(heldOffice)
        # print(officeIndices)
        return render(request, "data.html", {"address": address, "representatives": representatives, "names": names, "indices": indices, "heldOffice": heldOffice, 'officeIndices': officeIndices, 'realOffice': realOffice, 'test_representatives': test_representatives})
    elif request.method == 'POST' and 'elections' in request.POST:
        url = f"https://civicinfo.googleapis.com/civicinfo/v2/voterinfo?address={address}&electionId=7000&key=AIzaSyD5XEFhbr4Shpzlq44v6gPSljNyauVnSvs"
        response = requests.get(url)
        elections = response.json()
        print(elections)
        return render(request, "data.html", {"elections": elections, "address": address})
    else:
        url = f"https://civicinfo.googleapis.com/civicinfo/v2/voterinfo?address={address}&electionId=7000&key=AIzaSyD5XEFhbr4Shpzlq44v6gPSljNyauVnSvs"
        response = requests.get(url)
        locations = response.json()
        return render(request, "data.html", {"locations": locations, "address": address})

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
