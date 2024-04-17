import gmaps

gmaps.configure(api_key='Your api key here')

new_york_coordinates = (40.75, -74.00)
gmaps.figure(center=new_york_coordinates, zoom_level=12)

