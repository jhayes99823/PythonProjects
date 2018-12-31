import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])
location = list(data["LOCATION"])

html = """<h4>Volcano Information:</h4>
Name: %s
Location: %s
Height: %s m
"""

def get_color(elev):
    if (elev <= 1500.0):
        return 'green'
    elif (elev > 1500.0 and elev <= 2800.0):
        return 'orange'
    else:
        return 'red'

map = folium.Map(location=[39, -94], zoom_start=3, tiles="Mapbox Bright")

# add elements to the map like markers
# map.add_child(folium.Marker(location=[38.2, -99.1], popup="Hi I am a marker", icon=folium.Icon(color='green')))

# other way to add children
fg_volacanoes = folium.FeatureGroup(name="Volcanoes") # feature group
# fg.add_child(folium.Marker(location=[38.2, -99.1], popup="Hi I am a marker", icon=folium.Icon(color='green')))

# adding multiple markers
for lt, ln, el, nm, loc in zip(lat, lon, elev, name, location):
    iframe = folium.IFrame(html=html % (nm, loc, str(el)), width=200, height=100)
    # fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon=folium.Icon(color=get_color(el))))
    # change to CircleMarker
    fg_volacanoes.add_child(folium.CircleMarker(location=[lt, ln], radius=5, popup=folium.Popup(iframe), fill=True, fill_color=get_color(el), color='grey', fill_opacity=0.8))

fg_population = folium.FeatureGroup(name="Population") # feature group

fg_population.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(), style_function=lambda x: {
    'fillColor' : 'green' if x['properties']['POP2005'] < 10000000
    else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000
    else 'red'
}))

map.add_child(fg_volacanoes)
map.add_child(fg_population)
map.add_child(folium.LayerControl())

map.save("Map1.html")

