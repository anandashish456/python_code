#!/usr/bin/env python

import smtplib

sender = 'ashianan@cisco.com'
receivers = ['ashianan@cisco.com']


message = """From: psu-automation@cisco.com
To: Receivers@cisco.com
Subject: CR approval Needed
MIME-Version: 1.0
Content-type: text/html

<tbody><tr style='background-color: #dddddd;'><td>For list of DB tools <b><i> <a href='https://dba.cisco.com/dbpharmacy/'>DB Pharmacy</a></i></b></td></tr>

<tr><td style='border: 1px solid #dddddd; padding: 10px;'> 
<br><br>Hi Team,<br><br> 
	<p>Please get below CR approved.

		
	<table style='width: 90%;border: 1px solid DarkBlue;border-spacing: 0px;border-collapse: collapse; font-size: 11pt;'>
		<caption style='color: white;'> Request Details</caption>
		<thead><tr>
		<th style='border: thin solid DarkBlue;background-color: SteelBlue;padding: 0.5em;color: white;'> Request#</th>
		<th style='border: thin solid DarkBlue;background-color: SteelBlue;padding: 0.5em;color: white;'> Database</th>
		<th style='border: thin solid DarkBlue;background-color: SteelBlue;padding: 0.5em;color: white;'> CR Number</th>
		<th style='border: thin solid DarkBlue;background-color: SteelBlue;padding: 0.5em;color: white;'> CR Start Date</th>
		<th style='border: thin solid DarkBlue;background-color: SteelBlue;padding: 0.5em;color: white;'> CR End Date</th>
		<th style='border: thin solid DarkBlue;background-color: SteelBlue;padding: 0.5em;color: white;'> Requester</th>
		<th style='border: thin solid DarkBlue;background-color: SteelBlue;padding: 0.5em;color: white;'> Requested On</th>
		<th style='border: thin solid DarkBlue;background-color: SteelBlue;padding: 0.5em;color: white;'> Status</th>
		</tr></thead><tbody><tr>


		<td style='text-align: center; border: thin solid DarkBlue; padding: 0.5em;'></td>
		<td style='text-align: center; border: thin solid DarkBlue; padding: 0.5em;'></td>
		<td style='text-align: center; border: thin solid DarkBlue; padding: 0.5em;'></td>
		<td style='text-align: center; border: thin solid DarkBlue; padding: 0.5em;'></td>
		<td style='text-align: center; border: thin solid DarkBlue; padding: 0.5em;'></td>
		<td style='text-align: center; border: thin solid DarkBlue; padding: 0.5em;'></td>
		<td style='text-align: center; border: thin solid DarkBlue; padding: 0.5em;'></td>
		<td style='text-align: center; border: thin solid DarkBlue; padding: 0.5em;'></td>
		</tr></tbody></table> 
		<br><br>Database services will be down during the CR window.
		<br><br><b>Note: The CR created is not submitted. Please review and submit the CR.</b>

		<br><br>Thanks, 
		<br>PSU Self Service Tool<br> 
		
</td> </tr></tbody></table>

"""
try:
    smtpObj = smtplib.SMTP('localhost', 25)
    smtpObj.sendmail(sender, receivers, message)
    print("Successfully sent email")
except:
    print("Error: unable to send email")

