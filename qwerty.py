import urllib2
import json

API_ID_long = 'AIzaSyAAwUUvHzP9K05XgvlMRFwTo7dSL3G89KM'

API_ID_PLACES = 'AIzaSyB3z4FwBseed2D7nGkOO0yCICt8ybxt4Dg'

def places(lati, longi):
	radius = raw_input("Enter radius till where you want ot search ")
	typ = raw_input("Type of places you want to know about ")
	name = ''

	appid_places = API_ID_PLACES
	url_places = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location='+lati+','+longi+'&radius='+radius+'&types='+typ+'&name='+name+'&key='+appid_places
	json_obj_places = urllib2.urlopen(url_places)
	places = json.load(json_obj_places)

	# print places["results"][0]["geometry"]
	# for i in places:
	print len(places)
	print places
	for i in range(len(places)):
		print places["results"][i]["name"]



def location(address):
	appid_long = API_ID_long
	address = address.replace(' ', '+')
	url_loc = 'https://maps.googleapis.com/maps/api/geocode/json?address='+address+'&key='+appid_long
	json_obj_loc = urllib2.urlopen(url_loc)
	data = json.load(json_obj_loc)
	
	lati = str(data["results"][0]["geometry"]["location"]["lat"])
	longi = str(data["results"][0]["geometry"]["location"]["lng"])
	print lati
	print longi
	
	places(lati, longi)

address = raw_input("ENTER THE NAME OF THE CITY:  ")
location(address)


# API_ID_PLACES = 'AIzaSyB3z4FwBseed2D7nGkOO0yCICt8ybxt4Dg'

# def places(lati, longi):
# 	radius = raw_input("Enter radius till where you want ot search ")
# 	typ = raw_input("Type of places you want to know about ")
# 	name = ''

# 	appid_places = API_ID_PLACES
# 	url_places = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location='+lati+','+longi+'&radius='+radius+'&types='+typ+'&name='+name+'&key='+appid_places
# 	json_obj_places = urllib2.urlopen(url_places)
# 	places = json.load(json_obj_places)

