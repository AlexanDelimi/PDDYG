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


OXI --
			Από το: https://gecon.yale.edu/greece έχουμε το: greece_upload_xi_101509

			--greece_upload_xi_101509--
			<[53 rows x 19 columns]>
			πριν το scaling:
				Longitude min= 19.5 Longitude max= 29.5
				Latitude min= 34.5 Latitude min= 41.5

			μετά το scaling δημιουργήθηκε νέο csv με όνομα <<new_greece_upload>> όπου:
				new Longitude min= 0.0 new Longitude max= 1000.0
				new Latitude min= 0.0 new Latitude min= 1000.0

#########################################################################


OXI --
			Από το: https://gecon.yale.edu/turkey έχουμε το: turkey_upload_xi_101509

			--turkey_upload_xi_101509--
			<[115 rows x 19 columns]>
			πριν το scaling:
				Longitude min= 26.5 Longitude max= 44.5
				Latitude min= 35.5 Latitude min= 42.5

			μετά το scaling δημιουργήθηκε νέο csv με όνομα <<new_turkey_upload_xi_101509>> όπου:
				new Longitude min= 0.0 new Longitude max= 1000.0
				new Latitude min= 0.0 new Latitude min= 1000.0

#########################################################################


Από το: https://simplemaps.com/data/gr-cities έχουμε το: gr_csv

--gr_csv--
<[408 rows x 9 columns]>
πριν το scaling:
	Longitude min= 19.9214 Longitude max= 29.5917
	Latitude min= 34.8345 Latitude min= 41.5833

μετά το scaling δημιουργήθηκε νέο csv με όνομα <<new_gr_csv>> όπου:
	new Longitude min= 0.0 new Longitude max= 1000.0
	new Latitude min= 0.0 new Latitude min= 1000.0

#########################################################################


Από το: https://public.opendatasoft.com/explore/dataset/us-zip-code-latitude-and-longitude/export/?dataChart=eyJxdWVyaWVzIjpbeyJjb25maWciOnsiZGF0YXNldCI6InVzLXppcC1jb2RlLWxhdGl0dWRlLWFuZC1sb25naXR1ZGUiLCJvcHRpb25zIjp7fX0sImNoYXJ0cyI6W3siYWxpZ25Nb250aCI6dHJ1ZSwidHlwZSI6ImNvbHVtbiIsImZ1bmMiOiJBVkciLCJ5QXhpcyI6ImxhdGl0dWRlIiwic2NpZW50aWZpY0Rpc3BsYXkiOnRydWUsImNvbG9yIjoiI0ZGNTE1QSJ9XSwieEF4aXMiOiJzdGF0ZSIsIm1heHBvaW50cyI6NTAsInNvcnQiOiIifV0sInRpbWVzY2FsZSI6IiIsImRpc3BsYXlMZWdlbmQiOnRydWUsImFsaWduTW9udGgiOnRydWV9&location=2,43.25174,-69.70916&basemap=jawg.streets 
έχουμε το: us-zip-code-latitude-and-longitude

--us-zip-code-latitude-and-longitude--
<[43191 rows x 2 columns]>
πριν το scaling:
	Longitude min= -176.63675 Longitude max= -64.734694
	Latitude min= -7.209975 Latitude min= 71.299525

μετά το scaling δημιουργήθηκε νέο csv με όνομα <<new_us-zip-code-latitude-and-longitude>> όπου:
	new Longitude min= 0.0 new Longitude max= 1000.0
	new Latitude min= 0.0 new Latitude min= 1000.0

#########################################################################


--MOIAZEI ME TO us-zip-code-latitude-and-longitude
--LOGIKA OXI
			Από το: https://public.opendatasoft.com/explore/dataset/us-zip-code-latitude-and-longitude/table/?dataChart=eyJxdWVyaWVzIjpbeyJjb25maWciOnsiZGF0YXNldCI6InVzLXppcC1jb2RlLWxhdGl0dWRlLWFuZC1sb25naXR1ZGUiLCJvcHRpb25zIjp7fX0sImNoYXJ0cyI6W3siYWxpZ25Nb250aCI6dHJ1ZSwidHlwZSI6ImNvbHVtbiIsImZ1bmMiOiJBVkciLCJ5QXhpcyI6ImxhdGl0dWRlIiwic2NpZW50aWZpY0Rpc3BsYXkiOnRydWUsImNvbG9yIjoiI0ZGNTE1QSJ9XSwieEF4aXMiOiJzdGF0ZSIsIm1heHBvaW50cyI6NTAsInNvcnQiOiIifV0sInRpbWVzY2FsZSI6IiIsImRpc3BsYXlMZWdlbmQiOnRydWUsImFsaWduTW9udGgiOnRydWV9&location=2,43.25174,-69.70916&basemap=jawg.streets
			έχουμε το: uszips

			--uszips--
			<[33097 rows x 18 columns]>
			πριν το scaling:
				Longitude min= -176.63139 Longitude max= -65.29017
				Latitude min= 17.96612 Latitude min= 71.27374

			μετά το scaling δημιουργήθηκε νέο csv με όνομα <<new_uszips>> όπου:
				new Longitude min= 0.0 new Longitude max= 1000.0
				new Latitude min= 0.0 new Latitude min= 1000.0

#########################################################################


Από το: https://archive.ics.uci.edu/ml/datasets/Restaurant+%26+consumer+data# έχουμε το: geoplaces2

--geoplaces2--
<[130 rows x 21 columns]>
πριν το scaling:
	Longitude min= -101.0286 Longitude max= -99.1265059
	Latitude min= 18.859803 Latitude min= 23.7602683

μετά το scaling δημιουργήθηκε νέο csv με όνομα <<new_geoplaces2>> όπου:
	new Longitude min= 0.0 new Longitude max= 1000.0
	new Latitude min= 0.0 new Latitude min= 1000.0

#########################################################################


Από το: https://catalog.data.gov/dataset/geocoders έχουμε το: parcelcoords

--parcelcoords--
<[579473 rows x 3 columns]>
πριν το scaling:
	Longitude min= -80.36003018 Longitude max= -79.69250413
	Latitude min= 40.19588887 Latitude min= 40.67449868

μετά το scaling δημιουργήθηκε νέο csv με όνομα <<new_geoplaces2>> όπου:
	new Longitude min= 0.0 new Longitude max= 1000.0
	new Latitude min= 0.0 new Latitude min= 1000.0

#########################################################################


Από το: https://catalog.data.gov/dataset/loudoun-wells έχουμε το: Loudoun_Wells

--Loudoun_Wells--
<[22174 rows x 18 columns]>
πριν το scaling:
	Longitude min= -77.9532609 Longitude max= -77.33810806
	Latitude min= 38.85012684 Latitude min= 39.32033552

μετά το scaling δημιουργήθηκε νέο csv με όνομα <<new_Loudoun_Wells>> όπου:
	new Longitude min= 0.0 new Longitude max= 1000.0
	new Latitude min= 0.0 new Latitude min= 1000.0

#########################################################################


Από το: https://catalog.data.gov/dataset/allegheny-county-dam-locations-426e6 έχουμε το: Allegheny_County_Dam_Locations

--Allegheny_County_Dam_Locations--
<[46 rows x 25 columns]>
πριν το scaling:
	Longitude min= -80.31506445 Longitude max= -79.71476727
	Latitude min= 40.26507524 Latitude min= 40.66979796

μετά το scaling δημιουργήθηκε νέο csv με όνομα <<new_Allegheny_County_Dam_Locations>> όπου:
	new Longitude min= 0.0 new Longitude max= 1000.0
	new Latitude min= 0.0 new Latitude min= 1000.0

#########################################################################


Από το: https://simplemaps.com/data/au-cities έχουμε το au: 

--au--
<[1035 rows x 9 columns]>
πριν το scaling:	
	Longitude min= -43.1667 Longitude max= -10.5789
	Latitude min= 113.6611 Latitude min= 153.6178
	
μετά το scaling δημιουργήθηκε νέο csv με όνομα <<new_au>> όπου:
	new Longitude min= 0.0 new Longitude max= 1000.0
	new Latitude min= 0.0 new Latitude min= 1000.0

#########################################################################


Από το:https://simplemaps.com/data/cy-cities έχουμε το cy: 

--cy--
<[100 rows x 9 columns]>
πριν το scaling:	
	Longitude min= 34.6576 Longitude max= 35.343
	Latitude min= 32.4019 Latitude min= 33.9977

μετά το scaling δημιουργήθηκε νέο csv με όνομα <<new_cy>> όπου:
	new Longitude min= 0.0 new Longitude max= 1000.0
	new Latitude min= 0.0 new Latitude min= 1000.0

#########################################################################



#CODE FOR SCALING#
# a, b = 0, 1000
# x, y = data.COLUMN_NAME.min(), data.COLUMN_NAME.max()
# data['COLUMN_NAME'] = (data.COLUMN_NAME - x) / (y - x) * (b - a) + a
# # print(data.COLUMN_NAME.min())
# # print(data.COLUMN_NAME.max())
