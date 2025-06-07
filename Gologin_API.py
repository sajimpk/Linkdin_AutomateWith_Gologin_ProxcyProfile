from gologin import GoLogin
import time
from webdriver_manager.chrome import ChromeDriverManager
from config import GLOGIN_API_TOKEN,PROFILE_NAME,proxcy_url
import requests

gl = GoLogin({
	"token": GLOGIN_API_TOKEN,
	})
def create_profileQ():
    profile = gl.createProfileRandomFingerprint({"os": "lin", "name": PROFILE_NAME})
    profile_id = profile["id"]
    gl.addGologinProxyToProfile(profile_id,"us")
    return profile_id

def Proxcy_setup(profile_id):
    url = proxcy_url
    res = requests.get(url)
    data = res.json()
    if data["data"]:
        proxy = data["data"][0]
        print(f"🧩 Using Proxy: {proxy['ip']}:{proxy['port']} {proxy['protocols']}")
        gl.changeProfileProxy(profile_id, {
        "mode": proxy['protocols'],
        "host": proxy['ip'],
        "port": proxy['port'],
        "username": "",
        "password": "",
        "changeIpUrl": "https://some-proxy-provider.com/change-ip",
        "customName": "My Proxy",
        "notes": "string"
        })
    return profile_id

def start_profileQ(profile_id):
    gl.setProfileId(profile_id)
    start_response = gl.start()
    print("Started profile:", start_response)
    return start_response

def stop_profileQ(profile_id):
    gl.setProfileId(profile_id)
    print("Stoping ..")
    time.sleep(5)
    gl.stop()
    print("deleteing profile..")
    gl.delete(profile_id)
    return
