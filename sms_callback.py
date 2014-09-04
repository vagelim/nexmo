#!/usr/bin/env python
# __author__ = 'vageli'

import cgi, cgitb
import sys
from sendEmail import sendEmail

form = cgi.FieldStorage() 
msisdn = form.getvalue('msisdn')
to  = form.getvalue('to')
messageId = form.getvalue('messageId')
text  = form.getvalue('text')
message_timestamp = form.getvalue('message-timestamp')
type  = form.getvalue('type')
msisdn = str(msisdn)
msisdn = msisdn.translate(None, "'")
to = str(to)
to = to.translate(None, "'")
messageId = str(messageId)
messageId = messageId.translate(None, "'")
text = str(text)
text = text.translate(None, "'")
message_timestamp = str(message_timestamp)
message_timestamp = message_timestamp.translate(None, "'")
type = str(type)
type = type.translate(None, "'")

sys.stdout.write("Content-type:text/html\r\n\r\n")
sys.stdout.write( 'HTTP/1.1 200 OK\r\n\r\n')
print "<html>"
print "<head>"
print "<title>Test Callback</title>"
print "</head>"
print "<body>"
print "<h2>Hello %s %s %s %s %s %s</h2>" % (msisdn, to, messageId,text,message_timestamp,type)
print "</body>"
print "</html>"

from gv import sendTxt

message = 'MSISDN: ' + msisdn + '\nTo: ' + to + '\nmessageId: ' + messageId + '\nTEXT:' + text + '\n\nTimestamp: ' + message_timestamp

number = '1234567890'
sendTxt(number,message)
