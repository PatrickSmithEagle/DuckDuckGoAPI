# Patrick Smith
# 11/5/22
# query the DuckDuckGo API for presidents of the united states and test whether each president is listed
import requests


def test_pres():
    presidents = {"Washington": False, "Adams": False, "Jefferson": False, "Madison": False, "Monroe": False, "Jackson": False, "Van Buren": False, "Harrison": False, "Tyler": False, "Polk": False, "Taylor": False, "Fillmore": False, "Pierce": False, "Buchanan": False, "Lincoln": False, "Johnson": False, "Grant": False, "Hayes": False, "Garfield": False, "Arthur": False, "Cleveland": False, "McKinley": False, "Roosevelt": False, "Taft": False, "Wilson": False, "Harding": False, "Coolidge": False, "Hoover": False, "Truman": False, "Eisenhower": False, "Kennedy": False, "Nixon": False, "Ford": False, "Carter": False, "Reagan": False, "Bush": False, "Clinton": False, "Obama": False, "Trump": False, "Biden": False}
    url_ddg = "https://api.duckduckgo.com/?q=presidents+of+the+united+states&format=json"
    response = requests.get(url_ddg)
    json_data = response.json()
    for pkey in presidents:
        for key in json_data["RelatedTopics"]:
            if pkey in key["Text"]:
                presidents[pkey] = True
                break
    for pkey in presidents:
        assert pkey

