from django.http import HttpResponse
from django.shortcuts import render
from dashboard.models import Farmer
import random, json



def generateSampleData():
    sample_names = ("Bob", "Dan", "Chloe", "Lyra", "Dev", "Eric")
    sample_land_area = (100, 140, 120, 30, 10, 1500)
    sample_lat = (20.762765 + random.random()/1000,
                    20.762765 + random.random()/1000,
                    20.762765 + random.random()/1000,
                    20.762765 + random.random()/1000,
                    20.762765 + random.random()/1000,
                    20.762765 + random.random()/1000)
    sample_long = (72.978160 + random.random()/1000,
                    72.978160 + random.random()/1000,
                    72.978160 + random.random()/1000,
                    72.978160 + random.random()/1000,
                    72.978160 + random.random()/1000,
                    72.978160)
    sample_diseased = (True, False, False, False, True, True)
    sample_farmers = []

    for i in range(6):
        name=sample_names[i]
        land_area=sample_land_area[i],
        latitude=sample_lat[i], 
        longitude=sample_long[i],
        is_diseased=sample_diseased[i]
        sample_farmers.append(Farmer(name=name, land_area=land_area,
                                     latitude=latitude, longitude=longitude,
                                     is_diseased=is_diseased))
    return sample_farmers

def returnSampleFarmerData(request):
    farmers = generateSampleData()
    data = {'all_farmers':[]}
    for item in farmers:
        data['all_farmers'].append(str(item))
    response = json.dumps(data)
    # print json.loads(response)
    # print json.loads(response)['all_farmers']
    #print json.loads(response)['all_farmers'][0]
    #return json.dumps(data)
    return HttpResponse(response, mimetype='application/json') 

def dashboard(request):
    context = {}
    return render(request, 'dashboard/dashboard.html', context)

