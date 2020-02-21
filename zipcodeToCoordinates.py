import pandas as pd

from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="EP_coordinates")

#Read the xlsx file
path_file="data.xlsx"
col_types = {"COUNTRY":str,"POSTALCODE":str}
hoja = "Hoja1"
df = pd.read_excel(path_file,sheet_name=hoja,dtype=col_types)

#List of colums
col1 = []
col2 = []
col3 = []
col4 = []
col5 = []

#Loop to the data adding in the list our Result
for i in range(len(df)):
	location = geolocator.geocode(str(df['POSTALCODE'][i]) + ' ' + df['COUNTRY'][i])
	col1.append(df['COUNTRY'][i])
	col2.append(df['POSTALCODE'][i])
	col3.append(location.latitude)
	col4.append(location.longitude)
	col5.append(location.address)

data1 = [col1,col2,col3,col4,col5]
index = ["COUNTRY","POSTALCODE","latitude","longitude","Street"]
r1 = pd.DataFrame(data=data1, index=index).transpose()
print('\n'*2)
print(r1)
print('\n'*2)

#Write outfile xlsx
outfile = "Resultados1.xlsx"
writer = pd.ExcelWriter(outfile, engine ='xlsxwriter')
r1.to_excel(writer, sheet_name ='Sheet1')
writer.save()
