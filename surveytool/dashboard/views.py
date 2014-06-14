from django.http import HttpResponse
from django.shortcuts import render
from dashboard.models import Farmer
import random, json, requests
from collections import namedtuple


def getLatestSMS():
    r = requests.get('https://api.twilio.com/2010-04-01/Accounts/AC2538516e85acddb63169a9c56019a68a/Messages.json', auth=('AC2538516e85acddb63169a9c56019a68a', '170945ab2aed0d2ec992a22e9fa41ca4'))
    all_messages = []
    for item in r.json()['messages']:
        all_messages.append(SMS(
        phone = item['from'],
        body = item['body'],
        direction = item['direction'], #inbound or outbound
        date_created = item['date_created'],
        sid = item['sid']
        ))
    if all_messages[0].sid != "":
        last_SMS_id = all_messages[0].sid
        farmer = matchPhoneToFarmer(all_messages[0].phone[1:])
        return farmer
    return "BAD"

def matchPhoneToFarmer(phone):
    print "PHONE: ", phone
    for farmer in sample_farmers:
        if phone==farmer.phone:
            return farmer
    return None


def generateSampleData():
    sample_names = ("Bob", "Dan", "Chloe", "Lyra", "Dev", "Eric")
    sample_land_area = (100, 140, 120, 30, 10, 1500)
    sample_phone = ("17792329691","17792329696","17792329691","17792329691","17792329691","17792329691")
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

    for i in range(6):
        name=sample_names[i]
        land_area=sample_land_area[i],
        phone = sample_phone[i]
        latitude=sample_lat[i], 
        longitude=sample_long[i],
        is_diseased=sample_diseased[i]
        sample_farmers.append(Farmer(name=name, land_area=land_area, phone=phone,
                                     latitude=latitude, longitude=longitude,
                                     is_diseased=is_diseased))

def returnFarmerDataJSON(request):
    data = {'all_farmers':[]}
    for item in sample_farmers:
        data['all_farmers'].append(str(item))
    response = json.dumps(data)
    return HttpResponse(response, mimetype='application/json')

def dashboard(request):
    context = {}
    return render(request, 'dashboard/dashboard.html', context)

sample_farmers = []
generateSampleData()
SMS = namedtuple('SMS', ['phone', 'body', 'direction', 'date_created', 'sid'])
last_SMS_id = ""

