import requests, json, time, polyline

# make a call to the route-planning function
# doc'ed at http://dev.opentripplanner.org/apidoc/1.0.0/resource_PlannerResource.html

# There are more options available. These are just some.
options = {
	'fromPlace':'49.89529789184489,-97.16742038726807',
	'toPlace':'49.895629636479185,-97.11733818054198',
	'time':'1:02pm',
	'date':'05-20-2016',
	'mode':'TRANSIT,WALK',
	'maxWalkDistance':8152,
	'clampInitialWait':0,
	'wheelchair':False
}
response = requests.get(
	"http://localhost:8080/otp/routers/default/plan",
	params = options
)

# parse from JSON to python dictionary
# print response.content

response = json.loads(response.content)

legs = (response["plan"]["itineraries"][0]["legs"])

for l in legs:
	print l['legGeometry']

