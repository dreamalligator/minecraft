from optimizeimages import optipng
def signFilter(poi):
        if poi['id']=='Sign':		
		texts=[poi['Text1'],poi['Text2'],poi['Text3'],poi['Text4']]
		texts="\n".join(texts)
                s=texts.replace('"','')
                s=s.lower()		
		#Harbor
		h=['harbor','ship','port','cove','bay']
		if any(x in s for x in h):
			poi['icon']='icons/marker_ship.png'
		#Tower
		t=['tower']
		if any(x in s for x in t):
			poi['icon']='icons/marker_tower.png'
		#Castle
                c=['citadel','fortress','castle']
                if any(x in s for x in c):
                        poi['icon']='icons/dled/marker_city_blue.png'
		#Kingdom
		k=['kingdom','domain','realm']
		if any(x in s for x in k):
			poi['icon']='icons/dled/marker_kingdom_blue.png'
		#Farm
		f=['farm','grove','homestead','collective','orchard','garden']
		if any(x in s for  x in f):
			poi['icon']='icons/marker_hoe.png'
		#Forest
		fo=['forest','marsh']
		if any(x in s for x in fo):
			poi['icon']='icons/dled/marker_tree_green.png'
		#Water
		w=['well','stream','river','falls','island','isle','lake','lagoon','sea']
		if any(x in s for x in w):
			poi['icon']='icons/dled/marker_water_green.png'
		#Mountain
                mo=['mountain','peak','floatingisle']
                if any(x in s for x in mo):
                        poi['icon']='icons/dled/marker_mountain_green.png'
		#Mine
		m=['mine','cave']
		if any(x in s for x in m):
			poi['icon']='icons/marker_mine.png'
		#Village
		v=['village','town','city']
		if any(x in s for x in v):
			poi['icon']='icons/marker_town.png'
		#Minecart
		mi=['track','rail','cart']
		if any(x in s for x in mi):
			poi['icon']='icons/marker_minecart_blue.png'
		#Blacksmith
		b=['smith','forge']
		if any(x in s for x in b):
			poi['icon']='icons/marker_anvil.png'
		#Factory
		y=['factory','refinery','mill']
		if any(x in s for x in y):
			poi['icon']='icons/marker_factory.png'
		#Anomaly
		a=['?','Q:']
		if any(x in s for x in a):
			poi['icon']='icons/dled/marker_anomaly_grey.png'
		#Star
		st=['capital','star','larry','temple','outpost']
		if any(x in s for x in st):
			poi['icon']='icons/dled/marker_star_green.png'
		return s
def playerIcons(poi):
        if poi['id']=='Player':
                poi['icon']="http://overviewer.org/avatar/%s" % poi['EntityId']
                return "Last known location for %s" % poi['EntityId']
def playerSpawns(poi):
        if poi['id']=='PlayerSpawn':
                poi['icon']="bed.png"
		return "Spawn for %s" % poi['EntityId']
#Houses
#Towns
#Cities
#Inns
#Landmarks
#Bridges
#Mines
#Temples
#Beacon Towers
#Nether Portals
#Strongholds
def screenshotFilter(poi):
	'''This looks for signs that have their first line in the 'Image:<id>' format, where <id> is an
	id from an Imgur.com image.'''
	if poi['id'] == 'Sign':
		if poi['Text1'].startswith('Image:'):
			poi['icon'] = "painting_icon.png"
			image_html = "<style>.infoWindow img[src='{icon}'] {{display: none}}</style><a href='http://imgur.com/{id}'><img src='http://imgur.com/{id}s.jpg' /></a>".format(icon=poi['icon'], id=poi['Text1'][6:])
			return "\n".join([image_html, poi['Text2'], poi['Text3'], poi['Text4']])
#Harbors
def harborFilter(poi):
	if poi['id']=='Harbor':
		poi['icon']='icons/marker_ship.png'
		return poi['name']
#Retrieved POIs
def retrievePOIs(poi):
	pass
worlds["Kingdom Plantar"]="~/minecraft/kingdomplantar"
renders["normalrender0"]={
	"world":"Kingdom Plantar",
	"title":"SW view of the kingdom",
	"northdirection":"upper-left",
	'manualpois':[
		{'id':'Harbor',
		'x':275,
		'y':64,
		'z':440,
		'name':'Dark Harbor'},
	],
	'markers':[
                dict(name='sines',filterFunction=signFilter,checked=True),
                dict(name='players',filterFunction=playerIcons,checked=True),
                dict(name='spawns',filterFunction=playerSpawns),
		#dict(name='harbors',filterFunction=harborFilter),
        ],
	'optimizeimg':[optipng(olevel=3)],
}
renders["normalrender1"]={
	"world":"Kingdom Plantar",
	"title":"NE view of the kingdom",
	"northdirection":"lower-right",
	"markers":[
                dict(name='sines',filterFunction=signFilter,checked=True),
                dict(name='players',filterFunction=playerIcons,checked=True),
                dict(name='spawns',filterFunction=playerSpawns),
        ],
	"optimizeimg":[optipng(olevel=3)],
}
outputdir="~/digitalvapor/kingdomplantar"
texturepath="~/minecraft/kingdomplantar"

