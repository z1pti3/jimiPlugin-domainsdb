import jimi

class _domainsdb(jimi.plugin._plugin):
    version = 0.1

    def install(self):
        # Register models
        jimi.model.registerModel("domainsdbGetRegisteredDomains","_domainsdbGetRegisteredDomains","_action","plugins.domainsdb.models.action")
        jimi.model.registerModel("domainsdbGetRegisteredDomainsAdvanced","_domainsdbGetRegisteredDomainsAdvanced","_action","plugins.domainsdb.models.action")
        jimi.model.registerModel("domainsdbGetTLD","_domainsdbGetTLD","_action","plugins.domainsdb.models.action")
        jimi.model.registerModel("domainsdbGetLatestAddedDomains","_domainsdbGetLatestAddedDomains","_action","plugins.domainsdb.models.action")
        jimi.model.registerModel("domainsdbGetLatestDeletedDomains","_domainsdbGetLatestDeletedDomains","_action","plugins.domainsdb.models.action")
        jimi.model.registerModel("domainsdbGetTLD","_domainsdbGetTLD","_action","plugins.domainsdb.models.action")
        jimi.model.registerModel("domainsdbGetStat","_domainsdbGetStat","_action","plugins.domainsdb.models.action")
        return True

    def uninstall(self):
        # deregister models
        jimi.model.deregisterModel("domainsdbGetRegisteredDomains","_domainsdbGetRegisteredDomains","_action","plugins.domainsdb.models.action")
        jimi.model.deregisterModel("domainsdbGetRegisteredDomainsAdvanced","_domainsdbGetRegisteredDomainsAdvanced","_action","plugins.domainsdb.models.action")
        jimi.model.deregisterModel("domainsdbGetTLD","_domainsdbGetTLD","_action","plugins.domainsdb.models.action")
        jimi.model.deregisterModel("domainsdbGetLatestAddedDomains","_domainsdbGetLatestAddedDomains","_action","plugins.domainsdb.models.action")
        jimi.model.deregisterModel("domainsdbGetLatestDeletedDomains","_domainsdbGetLatestDeletedDomains","_action","plugins.domainsdb.models.action")
        jimi.model.deregisterModel("domainsdbGetTLD","_domainsdbGetTLD","_action","plugins.domainsdb.models.action")
        jimi.model.deregisterModel("domainsdbGetStat","_domainsdbGetStat","_action","plugins.domainsdb.models.action")
        return True

    def upgrade(self,LatestPluginVersion):
        #if self.version < 0.2:
        return True
