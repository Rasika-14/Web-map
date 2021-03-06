import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list (data["LAT"])
lon = list (data["LON"])
elev = list(data["ELEV"])

def color_producer(elevation):
     if elevation < 1000:
         return 'green'
     elif 1000 <= elevation < 3000:
          return 'orange'
     else:
      return 'red' 
map = folium.Map(location=[38.58, -99.89], zoom_start=6)

#fgv = folium.FeatureGroup(name="Volcanoes")
fg = folium.FeatureGroup(name="My map")

for lt, In, el in zip(lat, lon, elev):
    fg.add_child(folium.CircleMarker(location=[lt, In], radius = 6, popup = str(el)+" m", 
    fill_color=color_producer(el), color= 'grey', fill_opacity=0.7))

#fgp = folium.FeatureGroup(name="Population")

#fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding="utf-8-sig"), read())))
fg.add_child(folium.GeoJson(data=open('world.json', 'r', encoding="utf-8-sig").read()))


#map.add_child(fgv)
#map.add_child(fgp)
map.add_child(fg)
#map.add_child(folium.LayerControl())

map.save("simplemap.html")
