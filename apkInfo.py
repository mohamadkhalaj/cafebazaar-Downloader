import urllib3, json, re

url = 'https://api.cafebazaar.ir'
app_detail_url = '/rest-v1/process/AppDetailsV2Request'

properties = {
	"androidClientInfo": {
		"adId": "",
		"adOptOut": False,
		"androidId": "488o50b88f5x228d",
		"city": "NA",
		"country": "NA",
		"cpu": "armeabi-v7a,armeabi",
		"device": "",
		"dpi": 510,
		"hardware": "",
		"height": 1920,
		"locale": "",
		"manufacturer": "huawei",
		"mcc": 432,
		"mnc": 20,
		"model": "p50-pro",
		"osBuild": "",
		"product": "p50",
		"province": "NA",
		"sdkVersion": 23,
		"width": 1080
	},
	"appThemeState": 0,
	"clientID": "DFztC8oYTRuFZSf4565xu52",
	"clientVersion": "8.11.2",
	"clientVersionCode": 801102,
	"isKidsEnabled": False,
	"language": 2
}

def app_detail(packageName, link):
	globals()
	payload = {
		"properties": properties,
		"singleRequest": {
			"appDetailsV2Request": {
				"packageName": packageName,
				"referrers": [{
						"type": 11,
						"extraJson": "{\"services\":\"vitrin\",\"slug\":\"home\"}"
					}, {
						"type": 21,
						"extraJson": "{\"services\":\"vitrin\",\"slug\":\"home\"}"
					}, {
						"type": 1,
						"extraJson": "{\"services\":\"vitrin\",\"index\":7,\"title\":\"به‌روزشده‌های برگزیده\",\"source\":\"normal\",\"is_shuffled\":false,\"referrer_identifier\":\"query_Best New Updates\"}"
					}, {
						"type": 2,
						"extraJson": "{\"services\":\"vitrin\",\"index\":1,\"referrer_identifier\":\"\"}"
					}
				]
			}
		}
	}

	http = urllib3.PoolManager()
	encoded_data = json.dumps(payload).encode('utf-8')

	r = http.request('POST', url + app_detail_url, body=encoded_data)
	response = json.loads(r.data.decode('utf-8'))

	if response['properties']['statusCode'] == 200:
		apkName = response['singleReply']['appDetailsV2Reply']['meta']['name']
		return apkName
	else:
		raise Exception('Not Found!')
