#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib.request
import json

def SportDemo():
    # Set url parameter
    url = "http://api.isportsapi.com/sport/basketball/livescores?api_key=VNhjOMjbs2kQmk9Z"

    # Call iSport Api to get data in json format
    f = urllib.request.urlopen(url)
    content = f.read()

    decoded = content.decode('utf-8')
    jsoned = json.loads(decoded)

    for k in jsoned['data']:
        if k['leagueName'] == 'NBA':
            remainingQuarterTime = k['quarterRemainTime']
            homeTeam = k['homeName']
            awayTeam = k['awayName']
            homeScore = k['homeScore']
            awayScore = k['awayScore']
            print("{} (home) vs {} (away)".format(homeTeam, awayTeam))
            print("Current score: {} - {}".format(homeScore, awayScore))
            print("Time remaining in quarter: {}".format(remainingQuarterTime))


        
            ##print(homeTeam)

            #print(awayTeam)
        #print(k['leagueName'])





        #print(k.items())
        #for data in k.items():
           #print(data)
        #print(type(k.items()))
        #print("League: {}".format(k.items()[2][1]))
        #print("END")
            #print("{} : {}".format(data, value))
            #leagueName = data['leagueName']
            #print(leagueName)
        
    


SportDemo()
