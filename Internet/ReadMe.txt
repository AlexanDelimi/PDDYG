Χρησιμοποιούμε τα csv με new_

Από το: https://mrdata.usgs.gov/mrds/ έχουμε το: mrds-csv 

--mrds-csv--
<[304632 rows x 45 columns]>
πριν το scaling:
	Longitude min= -178.8205 Longitude max= 179.1318
	Latitude min= -72.99718 Latitude min= 80.00095999999999

μετά το scaling δημιουργήθηκε νέο csv με όνομα <<new_mrds>> όπου:
	new Longitude min= 0.0 new Longitude max= 1000.0
	new Latitude min= 0.0 new Latitude min= 1000.0


Το <<new_mrds>> έχει δύο στήλες -> longitude,latitude

#########################################################################


Από το: https://gecon.yale.edu/greece έχουμε το: greece_upload_xi_101509

--greece_upload_xi_101509--
<[53 rows x 19 columns]>
πριν το scaling:
	Longitude min= 19.5 Longitude max= 29.5
	Latitude min= 34.5 Latitude min= 41.5

Δεν χρειάζεται scaling δημιουργήθηκε νέο csv με όνομα <<new_greece_upload>> που έχει δύο στήλες -> longitude,latitude

#########################################################################


Από το: https://gecon.yale.edu/turkey έχουμε το: turkey_upload_xi_101509

--turkey_upload_xi_101509--
<[115 rows x 19 columns]>
πριν το scaling:
	Longitude min= 26.5 Longitude max= 44.5
	Latitude min= 35.5 Latitude min= 42.5

Δεν χρειάζεται scaling δημιουργήθηκε νέο csv με όνομα <<new_turkey_upload_xi_101509>> που έχει δύο στήλες -> longitude,latitude

#########################################################################


Από το: https://simplemaps.com/data/gr-cities έχουμε το: gr_csv

--gr_csv--
<[408 rows x 9 columns]>
πριν το scaling:
	Longitude min= 19.9214 Longitude max= 29.5917
	Latitude min= 34.8345 Latitude min= 41.5833

Δεν χρειάζεται scaling δημιουργήθηκε νέο csv με όνομα <<new_gr_csv>> που έχει δύο στήλες -> longitude,latitude


#CODE FOR SCALING#
# a, b = 0, 1000
# x, y = data.COLUMN_NAME.min(), data.COLUMN_NAME.max()
# data['COLUMN_NAME'] = (data.COLUMN_NAME - x) / (y - x) * (b - a) + a
# # print(data.COLUMN_NAME.min())
# # print(data.COLUMN_NAME.max())
