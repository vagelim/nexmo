#!/usr/bin/python
#Buy a phone number
import pycurl
import ast
import cStringIO


API_Key = 'YOUR API KEY'
API_Secret = 'YOUR API SECRET'

baseURL =  'https://rest.nexmo.com/number/buy/' + API_Key + '/' +  API_Secret + ' /'


def buyNumber(number, country='US'):
	url = baseURL + country + '/' + number

	#change variables into format for curl request
	country = 'country=' + country + '&'
	number = 'msisdn=' + number
 	c = pycurl.Curl()
	c.setopt(c.URL, 'url')
	c.setopt(c.POSTFIELDS, country + number)
	c.perform()
	
	#TODO:
	#Implement return code check
	#Http Status 200 if successful purchase
  #Http Status 401 if wrong credentials
  #Http Status 420 if wrong parameters
