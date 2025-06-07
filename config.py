# config.py
import random


GLOGIN_API_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2ODNiYTJmMmMzOGUzOTQ0YWQ3MWQ5YzkiLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2ODNiYjA1N2FiMWIwY2QzYjk4NWU2NjQifQ.mv4mKaahBcL32gpBtXdmg_uq_JMayi_cclKvSg70wCk"
LINKEDIN_EMAIL = "linkdin@gmail.com"
LINKEDIN_PASSWORD = "this is a password"

proxcy_url = "https://proxylist.geonode.com/api/proxy-list?limit=1&page=1&sort_by=lastChecked&sort_type=desc&protocols=socks5"

PROXY = {
    "mode": "socks5",
    "host": "proxy_ip_here",
    "port": 12345,
    "username": "proxy_user",
    "password": "proxy_pass"
}


PROFILE_NAME_LIST = ["test 20","test 21","test 23","test 24","test 25","test 26"]

PROFILE_NAME = random.choice(PROFILE_NAME_LIST)


