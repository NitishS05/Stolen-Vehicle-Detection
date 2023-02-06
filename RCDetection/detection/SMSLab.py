import requests

def sendsms(mobile):
	url = "https://www.fast2sms.com/dev/bulk"
	payload = "sender_id=FSTSMS&message=Your vehicle has been detected.\nPlease contact the police for further details. &language=english&route=p&numbers="+str(mobile)
	headers = {
	'authorization': "6CQEkOoTbRpLvy5AuJ8KaH4c0l79YgdntNUXj1ziMWVZfsSx2mOadKc2Y3qeQSbBV95yCrEvt7xfMRIg",
	'Content-Type': "application/x-www-form-urlencoded",
	'Cache-Control': "no-cache",
	}
	response = requests.request("POST", url, data=payload, headers=headers)
	print(response.text)

	return
