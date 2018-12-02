import vk_api
import requests
import os

lat_t = 36.021225 
long_t = 129.337693
radius_t = 5000
count_t = 1000
folder = "/folder/photo_save/"

vk_session = vk_api.VkApi( 'YOULOGIN', 'PASS' )
vk_session.auth()
vk = vk_session.get_api()

for i in vk.photos.search(lat=lat_t, long=long_t, radius=radius_t, count=count_t)['items']:
    for sz in i['sizes']:
        if sz['type'] == 'y':
            url = (sz["url"])
            img_data = requests.get(url).content
            tail = os.path.split(url)[1]
            with open(folder + tail, 'wb' ) as handler:
                handler.write( img_data )
                print("Файл скачан %s" % tail)
