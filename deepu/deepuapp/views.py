from django.shortcuts import render
import requests
import json

url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-key': "ebe661824cmsh284f09d69f174a0p1b3232jsnd0c177b11c53",
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers).json()


# Create your views here.
def Deepuview(request):
	text="Every One"
	noofresults=int(response['results'])
	mylist=[]
	for x in range(0,noofresults):
		mylist.append(response['response'][x]['country'])
	if request.method=='POST':
		selectedcountry = request.POST['selectedcountry']
		noofresults=int(response['results'])
		for x in range(0,noofresults):
			if selectedcountry==response['response'][x]['country'] :
				country = response['response'][x]['country']
				new = response['response'][x]['cases']['new']
				active = response['response'][x]['cases']['active']
				critical = response['response'][x]['cases']['critical']
				recovered = response['response'][x]['cases']['recovered']
				pop = response['response'][x]['cases']['1M_pop']
				total = response['response'][x]['cases']['total']
				
		context = {'mylist':mylist,'country':country,'new':new,'active':active,'critical':critical,
		'recovered':recovered,'pop':pop,'total':total}
		return render(request,'Deepu.html',context)
	context={'text':text,'mylist':mylist}
	return render (request,'Deepu.html',context)