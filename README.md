# zipcodeToCoordinates
Transform the ZipCode and Country Code taken from a excel file (xlsx) to the coordinates (Longitude and Latitude). It also gives the Address.

**How does it work?** the script takes the values of the columns "COUNTRY" and "POSTALCODE" using pandas' library and the geolocation's libraries to calculate the exact position. It generates another excel called "result.xlsx" (pandas).

## Libraries used:  
Geolocation: **Geocoder** and **Geopy - Nominatim**.  
Excel: **pandas**.  

### Notes: 
-The entry of the datasheet file has to have the colums: **COUNTRY** and **POSTALCODE**  
-The data of the datasheet should be in text format
