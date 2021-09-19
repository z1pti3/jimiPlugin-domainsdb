import jimi

from plugins.domainsdb.includes import domainsdb

class _domainsdbGetRegisteredDomains(jimi.action._action):
    domain = str()
    apiToken = str()

    def doAction(self,data):
        domain = jimi.helpers.evalString(self.domain,{"data" : data["flowData"], "eventData" : data["eventData"], "conductData" : data["conductData"], "persistentData" :  data["persistentData"] })
        apiToken = ""
        if self.apiToken.startswith("ENC") and self.apiToken != "":
            apiToken = jimi.auth.getPasswordFromENC(self.apiToken)

        response = domainsdb._domainsdb(apiKey=apiToken).getRegisteredDomains(domain)
        if response:
            return { "result" : True, "rc" : 200, "response" : response }
        else:
            return { "result" : False, "rc" : 404, "msg" : "Failed to get a valid response from API call" }

    def setAttribute(self,attr,value,sessionData=None):
        if attr == "apiToken" and not value.startswith("ENC "):
            self.apiToken = "ENC {0}".format(jimi.auth.getENCFromPassword(value))
            return True
        return super(_domainsdbGetRegisteredDomains, self).setAttribute(attr,value,sessionData=sessionData)

class _domainsdbGetRegisteredDomainsAdvanced(jimi.action._action):
    domain = str()
    zone = str()
    country = str()
    isDead = str()
    A = str()
    NS = str()
    CNAME = str()
    MX = str()
    TXT = str()
    apiToken = str()

    def doAction(self,data):
        domain = jimi.helpers.evalString(self.domain,{"data" : data["flowData"], "eventData" : data["eventData"], "conductData" : data["conductData"], "persistentData" :  data["persistentData"] })
        zone = jimi.helpers.evalString(self.zone,{"data" : data["flowData"], "eventData" : data["eventData"], "conductData" : data["conductData"], "persistentData" :  data["persistentData"] })
        country = jimi.helpers.evalString(self.country,{"data" : data["flowData"], "eventData" : data["eventData"], "conductData" : data["conductData"], "persistentData" :  data["persistentData"] })
        isDead = jimi.helpers.evalString(self.isDead,{"data" : data["flowData"], "eventData" : data["eventData"], "conductData" : data["conductData"], "persistentData" :  data["persistentData"] })
        A = jimi.helpers.evalString(self.A,{"data" : data["flowData"], "eventData" : data["eventData"], "conductData" : data["conductData"], "persistentData" :  data["persistentData"] })
        NS = jimi.helpers.evalString(self.NS,{"data" : data["flowData"], "eventData" : data["eventData"], "conductData" : data["conductData"], "persistentData" :  data["persistentData"] })
        CNAME = jimi.helpers.evalString(self.CNAME,{"data" : data["flowData"], "eventData" : data["eventData"], "conductData" : data["conductData"], "persistentData" :  data["persistentData"] })
        MX = jimi.helpers.evalString(self.MX,{"data" : data["flowData"], "eventData" : data["eventData"], "conductData" : data["conductData"], "persistentData" :  data["persistentData"] })
        TXT = jimi.helpers.evalString(self.TXT,{"data" : data["flowData"], "eventData" : data["eventData"], "conductData" : data["conductData"], "persistentData" :  data["persistentData"] })
        apiToken = ""
        if self.apiToken.startswith("ENC") and self.apiToken != "":
            apiToken = jimi.auth.getPasswordFromENC(self.apiToken)

        response = domainsdb._domainsdb(apiKey=apiToken).getRegisteredDomainsAdvanced(domain,zone,country,isDead,A,NS,CNAME,MX,TXT)
        if response:
            return { "result" : True, "rc" : 200, "response" : response }
        else:
            return { "result" : False, "rc" : 404, "msg" : "Failed to get a valid response from API call" }

    def setAttribute(self,attr,value,sessionData=None):
        if attr == "apiToken" and not value.startswith("ENC "):
            self.apiToken = "ENC {0}".format(jimi.auth.getENCFromPassword(value))
            return True
        return super(_domainsdbGetRegisteredDomainsAdvanced, self).setAttribute(attr,value,sessionData=sessionData)


class _domainsdbGetTLD(jimi.action._action):
    zone = str()
    domain = str()
    country = str()
    isDead = str()
    A = str()
    NS = str()
    CNAME = str()
    MX = str()
    TXT = str()
    apiToken = str()

    def doAction(self,data):
        zone = jimi.helpers.evalString(self.zone,{"data" : data["flowData"], "eventData" : data["eventData"], "conductData" : data["conductData"], "persistentData" :  data["persistentData"] })
        domain = jimi.helpers.evalString(self.domain,{"data" : data["flowData"], "eventData" : data["eventData"], "conductData" : data["conductData"], "persistentData" :  data["persistentData"] })
        country = jimi.helpers.evalString(self.country,{"data" : data["flowData"], "eventData" : data["eventData"], "conductData" : data["conductData"], "persistentData" :  data["persistentData"] })
        isDead = jimi.helpers.evalString(self.isDead,{"data" : data["flowData"], "eventData" : data["eventData"], "conductData" : data["conductData"], "persistentData" :  data["persistentData"] })
        A = jimi.helpers.evalString(self.A,{"data" : data["flowData"], "eventData" : data["eventData"], "conductData" : data["conductData"], "persistentData" :  data["persistentData"] })
        NS = jimi.helpers.evalString(self.NS,{"data" : data["flowData"], "eventData" : data["eventData"], "conductData" : data["conductData"], "persistentData" :  data["persistentData"] })
        CNAME = jimi.helpers.evalString(self.CNAME,{"data" : data["flowData"], "eventData" : data["eventData"], "conductData" : data["conductData"], "persistentData" :  data["persistentData"] })
        MX = jimi.helpers.evalString(self.MX,{"data" : data["flowData"], "eventData" : data["eventData"], "conductData" : data["conductData"], "persistentData" :  data["persistentData"] })
        TXT = jimi.helpers.evalString(self.TXT,{"data" : data["flowData"], "eventData" : data["eventData"], "conductData" : data["conductData"], "persistentData" :  data["persistentData"] })
        apiToken = ""
        if self.apiToken.startswith("ENC") and self.apiToken != "":
            apiToken = jimi.auth.getPasswordFromENC(self.apiToken)

        response = domainsdb._domainsdb(apiKey=apiToken).getRegisteredDomainsAdvanced(zone,domain,country,isDead,A,NS,CNAME,MX,TXT)
        if response:
            return { "result" : True, "rc" : 200, "response" : response }
        else:
            return { "result" : False, "rc" : 404, "msg" : "Failed to get a valid response from API call" }

    def setAttribute(self,attr,value,sessionData=None):
        if attr == "apiToken" and not value.startswith("ENC "):
            self.apiToken = "ENC {0}".format(jimi.auth.getENCFromPassword(value))
            return True
        return super(_domainsdbGetTLD, self).setAttribute(attr,value,sessionData=sessionData)


class _domainsdbGetLatestAddedDomains(jimi.action._action):
    date = str()
    apiToken = str()

    def doAction(self,data):
        date = jimi.helpers.evalString(self.date,{"data" : data["flowData"], "eventData" : data["eventData"], "conductData" : data["conductData"], "persistentData" :  data["persistentData"] })
        apiToken = ""
        if self.apiToken.startswith("ENC") and self.apiToken != "":
            apiToken = jimi.auth.getPasswordFromENC(self.apiToken)

        response = domainsdb._domainsdb(apiKey=apiToken).getLatestAddedDomains(date)
        if response:
            return { "result" : True, "rc" : 200, "response" : response }
        else:
            return { "result" : False, "rc" : 404, "msg" : "Failed to get a valid response from API call" }

    def setAttribute(self,attr,value,sessionData=None):
        if attr == "apiToken" and not value.startswith("ENC "):
            self.apiToken = "ENC {0}".format(jimi.auth.getENCFromPassword(value))
            return True
        return super(_domainsdbGetLatestAddedDomains, self).setAttribute(attr,value,sessionData=sessionData)

class _domainsdbGetLatestDeletedDomains(jimi.action._action):
    date = str()
    apiToken = str()

    def doAction(self,data):
        date = jimi.helpers.evalString(self.date,{"data" : data["flowData"], "eventData" : data["eventData"], "conductData" : data["conductData"], "persistentData" :  data["persistentData"] })
        apiToken = ""
        if self.apiToken.startswith("ENC") and self.apiToken != "":
            apiToken = jimi.auth.getPasswordFromENC(self.apiToken)

        response = domainsdb._domainsdb(apiKey=apiToken).getLatestDeletedDomains(date)
        if response:
            return { "result" : True, "rc" : 200, "response" : response }
        else:
            return { "result" : False, "rc" : 404, "msg" : "Failed to get a valid response from API call" }

    def setAttribute(self,attr,value,sessionData=None):
        if attr == "apiToken" and not value.startswith("ENC "):
            self.apiToken = "ENC {0}".format(jimi.auth.getENCFromPassword(value))
            return True
        return super(_domainsdbGetLatestDeletedDomains, self).setAttribute(attr,value,sessionData=sessionData)

class _domainsdbGetTLD(jimi.action._action):

    def doAction(self,data):
        response = domainsdb._domainsdb().getTLD()
        if response:
            return { "result" : True, "rc" : 200, "response" : response }
        else:
            return { "result" : False, "rc" : 404, "msg" : "Failed to get a valid response from API call" }

class _domainsdbGetStat(jimi.action._action):

    def doAction(self,data):
        response = domainsdb._domainsdb().getStat()
        if response:
            return { "result" : True, "rc" : 200, "response" : response }
        else:
            return { "result" : False, "rc" : 404, "msg" : "Failed to get a valid response from API call" }

