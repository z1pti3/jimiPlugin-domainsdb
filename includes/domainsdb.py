import requests
import json
from pathlib import Path

class _domainsdb():
    apiAddress = "https://api.domainsdb.info/v1"

    def __init__(self, apiKey=None, ca=None, requestTimeout=15, pages=False):
        self.apiKey = apiKey
        self.pages = pages
        self.requestTimeout = requestTimeout
        if ca != None:
            if type(ca) is str:
                self.ca = str(Path(ca))
            elif type(ca) is bool:
                self.ca = ca
        else:
            self.ca = None

    def apiCall(self,endpoint,methord="GET",data=None):
        kwargs={}
        kwargs["timeout"] = self.requestTimeout
        if self.ca != None:
            kwargs["verify"] = self.ca
        if self.apiKey:
            if "?" in endpoint:
                endpoint+="&api_key={0}".format(self.apiKey)
            else:
                endpoint+="?api_key={0}".format(self.apiKey)
        try:
            limit = 50
            url = "{0}/{1}".format(self.apiAddress,endpoint)
            if "?" in url:
                url+="&page={0}&limit={1}".format(0,limit)
            else:
                url+="?page={0}&limit={1}".format(0,limit)
            response = requests.get(url, **kwargs)
            data = json.loads(response.text)
            if self.pages:
                if "total" in data:
                    pages = int(data["total"]/limit)
                    pages -= 1
                    if pages > 0:
                        responseData = {}
                        listKey = ""
                        for key, value in data.items():
                            if type(value) is list and len(value) == limit:
                                listKey = key
                                break
                        if not listKey:
                            return 0, "Unable to find the page list key from response."
                        responseData[listKey] = data[listKey]
                        for x in range(1,pages):
                            url = "{0}/{1}".format(self.apiAddress,endpoint)
                            if "?" in url:
                                url+="&page={0}&limit={1}".format(x,limit)
                            else:
                                url+="?page={0}&limit={1}".format(x,limit)
                            print(url)
                            response = requests.get(url, **kwargs)
                            data = json.loads(response.text)
                            print(data)
                            if listKey in data:
                                responseData[listKey] += data[listKey]
                            else:
                                return 0, "Unexpected response from API. - {0}".format(data)
                    else:
                        return response.status_code, data
                    return 200, responseData
            else:
                return response.status_code, data
        except (requests.exceptions.Timeout, requests.exceptions.ConnectionError) as e:
            return 0, "Connection Timeout - {0}".format(e)
        return 0, "Unknown Error Occurred."

    def getRegisteredDomains(self,domain):
        statusCode, response = self.apiCall("domains/search?domain={0}".format(domain))
        return response

    def getRegisteredDomainsAdvanced(self,domain,zone="",country="",isDead=None,A="",NS="",CNAME="",MX="",TXT=""):
        arg = "domain={0}".format(domain)
        if zone:
            arg+="&zone={0}".format(zone)
        if country:
            arg+="&country={0}".format(country)
        if isDead:
            arg+="&isDead={0}".format(isDead)
        if A:
            arg+="&A={0}".format(A)
        if NS:
            arg+="&NS={0}".format(NS)
        if CNAME:
            arg+="&CNAME={0}".format(CNAME)
        if MX:
            arg+="&MX={0}".format(MX)
        if TXT:
            arg+="&TXT={0}".format(TXT)
        statusCode, response = self.apiCall("domains/search?{0}".format(arg))
        return response

    def getTLD(self,zone_id,domain="",country="",isDead=None,A="",NS="",CNAME="",MX="",TXT=""):
        arg = "{0}?".format(zone_id)
        if domain:
            arg+="&domain={0}".format(domain)
        if country:
            arg+="&country={0}".format(country)
        if isDead:
            arg+="&isDead={0}".format(isDead)
        if A:
            arg+="&A={0}".format(A)
        if NS:
            arg+="&NS={0}".format(NS)
        if CNAME:
            arg+="&CNAME={0}".format(CNAME)
        if MX:
            arg+="&MX={0}".format(MX)
        if TXT:
            arg+="&TXT={0}".format(TXT)
        statusCode, response = self.apiCall("domains/tld/{0}".format(arg))
        return response

    def getLatestAddedDomains(self,date=""):
        arg = ""
        if date:
            arg+="&date={0}".format(date)
        statusCode, response = self.apiCall("domains/updates/added?{0}".format(arg))
        return response

    def getLatestDeletedDomains(self,date=""):
        arg = ""
        if date:
            arg+="&date={0}".format(date)
        statusCode, response = self.apiCall("domains/updates/deleted?{0}".format(arg))
        return response

    def getDomainUpdatesList(self):
        statusCode, response = self.apiCall("domains/updates/list")
        return response

    def getTLD(self):
        statusCode, response = self.apiCall("info/tld/")
        return response
    
    def getStat(self):
        statusCode, response = self.apiCall("info/stat/")
        return response
