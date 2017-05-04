from django import template

register = template.Library()

@register.filter
def bldIndex(List, strIndex):
	dctBuild = {'ATRIUMCAFE':0, 'BUTLERCOLLEGE':1, 'CAFEVIVIAN':2, 'CENTERFORJEWISHLIFE':3, 'CHANCELLORGREEN':4, 'CHEMISTRYCAFE':5, 'CONCESSIONS_12':6, 'FORBESCOLLEGE':7, 'FRISTCSTORE':8, 'FRISTGALLERY1':9, 'FRISTGALLERY2':10, 'FRISTGALLERY3':11, 'FRISTGALLERY4':12, 'FRISTWITHERSPOONS':13, 'GRADUATECOLLEGE':14, 'LIBRARY_CART':15, 'MATHEYCOLLEGE':16, 'ROCKEFELLERCOLLEGE':17, 'STUDIO34BUTLEREMPORIUM':18, 'WHITMANCOLLEGE':19, 'WILSONCOLLEGE':20, 'WOODROWWILSONCAFE':21, 'FIRESTONELIBRARY':22}
	i = int(dctBuild.get(strIndex))
	return List[i]

@register.filter
def dayIndex(List, strIndex):
	#dctDay = {'SUNDAY':0, 'MONDAY':1, 'TUESDAY':2, 'WEDNESDAY':3, 'THURSDAY':4, 'FRIDAY':5, 'SATURDAY':6}
	#i = int(dctDay.get(strIndex))
	#return List[i]
	return List[int(strIndex)]

@register.filter
def timeIndex(List, strIndex):
	dctTime = { "T0000":0, "T0030":1, "T0100":2, "T0130":3, "T0200":4, "T0230":5, "T0300":6, "T0330":7, "T0400":8, "T0430":9, "T0500":10, "T0530":11, "T0600":12, "T0630":13, "T0700":14, "T0730":15, "T0800":16, "T0830":17, "T0900":18, "T0930":19, "T1000":20, "T1030":21, "T1100":22, "T1130":23, "T1200":24, "T1230":25, "T1300":26, "T1330":27, "T1400":28, "T1430":29, "T1500":30, "T1530":31, "T1600":32, "T1630":33, "T1700":34, "T1730":35, "T1800":36, "T1830":37, "T1900":38, "T1930":39, "T2000":40, "T2030":41, "T2100":42, "T2130":43, "T2200":44, "T2230":45, "T2300":46, "T2330":47}
	i = int(dctTime.get(strIndex))
	return List[i]