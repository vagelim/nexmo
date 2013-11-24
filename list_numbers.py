#!/usr/bin/python
#Get a list of currently available numbers for a given country
import pycurl
import ast
import cStringIO
 
API_Key = 'YOUR API KEY'
API_Secret = 'YOUR API SECRET'

URL1 = 'https://rest.nexmo.com/number/search/' + API_Key + '/' +  API_Secret + ' /'
URL2 = '?&index=2&size=25'

def list_numbers(COUNTRY='US'):
	buf = cStringIO.StringIO()
 
	c = pycurl.Curl()
	c.setopt(c.URL, URL1+COUNTRY+URL2)
	c.setopt(c.WRITEFUNCTION, buf.write)
	c.perform()
 
	#Transform string into dictionary
	#Has two keys:
	#	"count" -> How many numbers returned
	#	"numbers" -> List containing json of number, country, cost, and type

	numbers = ast.literal_eval(buf.getvalue())

	buf.close()

	numbers = numbers['numbers']
	return numbers


if __name__ == "__main__":
	list_numbers(COUNTRY='US')
