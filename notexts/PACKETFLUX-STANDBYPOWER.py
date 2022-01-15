#
# PySNMP MIB module PACKETFLUX-STANDBYPOWER (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/packetflux/PACKETFLUX-STANDBYPOWER
# Produced by pysmi-1.1.8 at Sat Jan 15 18:15:35 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
packetfluxMgmt, = mibBuilder.importSymbols("PACKETFLUX-SMI", "packetfluxMgmt")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
TimeTicks, ModuleIdentity, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Counter64, Gauge32, iso, NotificationType, Bits, MibIdentifier, IpAddress, Unsigned32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "ModuleIdentity", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Counter64", "Gauge32", "iso", "NotificationType", "Bits", "MibIdentifier", "IpAddress", "Unsigned32", "Integer32")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
standbypower = ModuleIdentity((1, 3, 6, 1, 4, 1, 32050, 2, 2))
standbypower.setRevisions(('2013-06-04 16:49',))
if mibBuilder.loadTexts: standbypower.setLastUpdated('201306041649Z')
if mibBuilder.loadTexts: standbypower.setOrganization('PacketFlux Technologies')
powercontrollerstate = MibScalar((1, 3, 6, 1, 4, 1, 32050, 2, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("onprimarypower", 1), ("startingstandby", 2), ("transferringtostandby", 3), ("onstandbypower", 4), ("transferringtoprimary", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: powercontrollerstate.setStatus('current')
transferswitchstate = MibScalar((1, 3, 6, 1, 4, 1, 32050, 2, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("primary", 1), ("transfertostandby1", 2), ("transfertostandby2", 3), ("transfertostandby3", 4), ("standby", 5), ("transfertoprimary1", 6), ("transfertoprimary2", 7), ("transfertoprimary3", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: transferswitchstate.setStatus('current')
standbypowerstate = MibScalar((1, 3, 6, 1, 4, 1, 32050, 2, 2, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26))).clone(namedValues=NamedValues(("stopped", 1), ("prepare1", 2), ("prepare2", 3), ("prepare3", 4), ("startup1", 5), ("startup2", 6), ("startup3", 7), ("checkrun", 8), ("reprepare1", 9), ("reprepare2", 10), ("reprepare3", 11), ("warmup1", 12), ("warmup2", 13), ("warmup3", 14), ("verifyrun", 15), ("running", 16), ("cooldown1", 17), ("cooldown2", 18), ("cooldown3", 19), ("shutdown1", 20), ("shutdown2", 21), ("shutdown3", 22), ("verifystopped", 23), ("postshutdown1", 24), ("postshutdown2", 25), ("postshutdown3", 26)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: standbypowerstate.setStatus('current')
ac1voltage = MibScalar((1, 3, 6, 1, 4, 1, 32050, 2, 2, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ac1voltage.setStatus('current')
ac1frequency = MibScalar((1, 3, 6, 1, 4, 1, 32050, 2, 2, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ac1frequency.setStatus('current')
ac2voltage = MibScalar((1, 3, 6, 1, 4, 1, 32050, 2, 2, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ac2voltage.setStatus('current')
ac2frequency = MibScalar((1, 3, 6, 1, 4, 1, 32050, 2, 2, 7), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ac2frequency.setStatus('current')
mtr1voltage = MibScalar((1, 3, 6, 1, 4, 1, 32050, 2, 2, 8), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mtr1voltage.setStatus('current')
mtr2voltage = MibScalar((1, 3, 6, 1, 4, 1, 32050, 2, 2, 9), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mtr2voltage.setStatus('current')
pwr1voltage = MibScalar((1, 3, 6, 1, 4, 1, 32050, 2, 2, 10), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwr1voltage.setStatus('current')
pwr2voltage = MibScalar((1, 3, 6, 1, 4, 1, 32050, 2, 2, 11), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwr2voltage.setStatus('current')
shuntvoltage = MibScalar((1, 3, 6, 1, 4, 1, 32050, 2, 2, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: shuntvoltage.setStatus('current')
temperature = MibScalar((1, 3, 6, 1, 4, 1, 32050, 2, 2, 13), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: temperature.setStatus('current')
recentunsuccessfulstarts = MibScalar((1, 3, 6, 1, 4, 1, 32050, 2, 2, 14), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: recentunsuccessfulstarts.setStatus('current')
totalunsuccessfulstarts = MibScalar((1, 3, 6, 1, 4, 1, 32050, 2, 2, 15), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: totalunsuccessfulstarts.setStatus('current')
recentstalls = MibScalar((1, 3, 6, 1, 4, 1, 32050, 2, 2, 16), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: recentstalls.setStatus('current')
totalstalls = MibScalar((1, 3, 6, 1, 4, 1, 32050, 2, 2, 17), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: totalstalls.setStatus('current')
numberofstarts = MibScalar((1, 3, 6, 1, 4, 1, 32050, 2, 2, 18), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: numberofstarts.setStatus('current')
numberoftransfers = MibScalar((1, 3, 6, 1, 4, 1, 32050, 2, 2, 19), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: numberoftransfers.setStatus('current')
currenttimeonprimary = MibScalar((1, 3, 6, 1, 4, 1, 32050, 2, 2, 20), TimeTicks()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: currenttimeonprimary.setStatus('current')
totaltimeonprimary = MibScalar((1, 3, 6, 1, 4, 1, 32050, 2, 2, 21), TimeTicks()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: totaltimeonprimary.setStatus('current')
currenttimeonstandby = MibScalar((1, 3, 6, 1, 4, 1, 32050, 2, 2, 22), TimeTicks()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: currenttimeonstandby.setStatus('current')
totaltimeonstandby = MibScalar((1, 3, 6, 1, 4, 1, 32050, 2, 2, 23), TimeTicks()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: totaltimeonstandby.setStatus('current')
currentstandbyruntime = MibScalar((1, 3, 6, 1, 4, 1, 32050, 2, 2, 24), TimeTicks()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: currentstandbyruntime.setStatus('current')
totalstandbyruntime = MibScalar((1, 3, 6, 1, 4, 1, 32050, 2, 2, 25), TimeTicks()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: totalstandbyruntime.setStatus('current')
laststandbyrun = MibScalar((1, 3, 6, 1, 4, 1, 32050, 2, 2, 26), TimeTicks()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: laststandbyrun.setStatus('current')
laststandbygracefulstop = MibScalar((1, 3, 6, 1, 4, 1, 32050, 2, 2, 27), TimeTicks()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: laststandbygracefulstop.setStatus('current')
laststandbyunsuccessfulstart = MibScalar((1, 3, 6, 1, 4, 1, 32050, 2, 2, 28), TimeTicks()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: laststandbyunsuccessfulstart.setStatus('current')
laststandbyfailure = MibScalar((1, 3, 6, 1, 4, 1, 32050, 2, 2, 29), TimeTicks()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: laststandbyfailure.setStatus('current')
switch1closed = MibScalar((1, 3, 6, 1, 4, 1, 32050, 2, 2, 30), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: switch1closed.setStatus('current')
switch2closed = MibScalar((1, 3, 6, 1, 4, 1, 32050, 2, 2, 31), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: switch2closed.setStatus('current')
switch3closed = MibScalar((1, 3, 6, 1, 4, 1, 32050, 2, 2, 32), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: switch3closed.setStatus('current')
switch4closed = MibScalar((1, 3, 6, 1, 4, 1, 32050, 2, 2, 33), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: switch4closed.setStatus('current')
switch5closed = MibScalar((1, 3, 6, 1, 4, 1, 32050, 2, 2, 34), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: switch5closed.setStatus('current')
enabled = MibScalar((1, 3, 6, 1, 4, 1, 32050, 2, 2, 35), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: enabled.setStatus('current')
relay1on = MibScalar((1, 3, 6, 1, 4, 1, 32050, 2, 2, 36), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: relay1on.setStatus('current')
relay2on = MibScalar((1, 3, 6, 1, 4, 1, 32050, 2, 2, 37), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: relay2on.setStatus('current')
relay3on = MibScalar((1, 3, 6, 1, 4, 1, 32050, 2, 2, 38), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: relay3on.setStatus('current')
relay4on = MibScalar((1, 3, 6, 1, 4, 1, 32050, 2, 2, 39), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: relay4on.setStatus('current')
relay5on = MibScalar((1, 3, 6, 1, 4, 1, 32050, 2, 2, 40), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: relay5on.setStatus('current')
relay6on = MibScalar((1, 3, 6, 1, 4, 1, 32050, 2, 2, 41), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: relay6on.setStatus('current')
relay7on = MibScalar((1, 3, 6, 1, 4, 1, 32050, 2, 2, 42), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: relay7on.setStatus('current')
ruleswitchstandby = MibScalar((1, 3, 6, 1, 4, 1, 32050, 2, 2, 43), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruleswitchstandby.setStatus('current')
rulereturnprimary = MibScalar((1, 3, 6, 1, 4, 1, 32050, 2, 2, 44), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rulereturnprimary.setStatus('current')
rulestandbygood = MibScalar((1, 3, 6, 1, 4, 1, 32050, 2, 2, 45), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rulestandbygood.setStatus('current')
rulestopstandby = MibScalar((1, 3, 6, 1, 4, 1, 32050, 2, 2, 46), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rulestopstandby.setStatus('current')
ruleexercisestandby = MibScalar((1, 3, 6, 1, 4, 1, 32050, 2, 2, 47), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruleexercisestandby.setStatus('current')
webcontrol1 = MibScalar((1, 3, 6, 1, 4, 1, 32050, 2, 2, 48), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: webcontrol1.setStatus('current')
webcontrol2 = MibScalar((1, 3, 6, 1, 4, 1, 32050, 2, 2, 49), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: webcontrol2.setStatus('current')
webcontrol3 = MibScalar((1, 3, 6, 1, 4, 1, 32050, 2, 2, 50), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: webcontrol3.setStatus('current')
webcontrol4 = MibScalar((1, 3, 6, 1, 4, 1, 32050, 2, 2, 51), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: webcontrol4.setStatus('current')
webcontrol5 = MibScalar((1, 3, 6, 1, 4, 1, 32050, 2, 2, 52), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: webcontrol5.setStatus('current')
webcontrol6 = MibScalar((1, 3, 6, 1, 4, 1, 32050, 2, 2, 53), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: webcontrol6.setStatus('current')
webcontrol7 = MibScalar((1, 3, 6, 1, 4, 1, 32050, 2, 2, 54), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: webcontrol7.setStatus('current')
webcontrol8 = MibScalar((1, 3, 6, 1, 4, 1, 32050, 2, 2, 55), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: webcontrol8.setStatus('current')
standbypowerConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 32050, 2, 2, 256))
standbypowerGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 32050, 2, 2, 256, 1))
packetfluxStandbypowerAllObjects = ObjectGroup((1, 3, 6, 1, 4, 1, 32050, 2, 2, 256, 1, 1)).setObjects(("PACKETFLUX-STANDBYPOWER", "powercontrollerstate"), ("PACKETFLUX-STANDBYPOWER", "transferswitchstate"), ("PACKETFLUX-STANDBYPOWER", "standbypowerstate"), ("PACKETFLUX-STANDBYPOWER", "ac1voltage"), ("PACKETFLUX-STANDBYPOWER", "ac1frequency"), ("PACKETFLUX-STANDBYPOWER", "ac2voltage"), ("PACKETFLUX-STANDBYPOWER", "ac2frequency"), ("PACKETFLUX-STANDBYPOWER", "mtr1voltage"), ("PACKETFLUX-STANDBYPOWER", "mtr2voltage"), ("PACKETFLUX-STANDBYPOWER", "pwr1voltage"), ("PACKETFLUX-STANDBYPOWER", "pwr2voltage"), ("PACKETFLUX-STANDBYPOWER", "shuntvoltage"), ("PACKETFLUX-STANDBYPOWER", "temperature"), ("PACKETFLUX-STANDBYPOWER", "recentunsuccessfulstarts"), ("PACKETFLUX-STANDBYPOWER", "totalunsuccessfulstarts"), ("PACKETFLUX-STANDBYPOWER", "recentstalls"), ("PACKETFLUX-STANDBYPOWER", "totalstalls"), ("PACKETFLUX-STANDBYPOWER", "numberofstarts"), ("PACKETFLUX-STANDBYPOWER", "numberoftransfers"), ("PACKETFLUX-STANDBYPOWER", "currenttimeonprimary"), ("PACKETFLUX-STANDBYPOWER", "totaltimeonprimary"), ("PACKETFLUX-STANDBYPOWER", "currenttimeonstandby"), ("PACKETFLUX-STANDBYPOWER", "totaltimeonstandby"), ("PACKETFLUX-STANDBYPOWER", "currentstandbyruntime"), ("PACKETFLUX-STANDBYPOWER", "totalstandbyruntime"), ("PACKETFLUX-STANDBYPOWER", "laststandbyrun"), ("PACKETFLUX-STANDBYPOWER", "laststandbygracefulstop"), ("PACKETFLUX-STANDBYPOWER", "laststandbyunsuccessfulstart"), ("PACKETFLUX-STANDBYPOWER", "laststandbyfailure"), ("PACKETFLUX-STANDBYPOWER", "switch1closed"), ("PACKETFLUX-STANDBYPOWER", "switch2closed"), ("PACKETFLUX-STANDBYPOWER", "switch3closed"), ("PACKETFLUX-STANDBYPOWER", "switch4closed"), ("PACKETFLUX-STANDBYPOWER", "switch5closed"), ("PACKETFLUX-STANDBYPOWER", "enabled"), ("PACKETFLUX-STANDBYPOWER", "relay1on"), ("PACKETFLUX-STANDBYPOWER", "relay2on"), ("PACKETFLUX-STANDBYPOWER", "relay3on"), ("PACKETFLUX-STANDBYPOWER", "relay4on"), ("PACKETFLUX-STANDBYPOWER", "relay5on"), ("PACKETFLUX-STANDBYPOWER", "relay6on"), ("PACKETFLUX-STANDBYPOWER", "relay7on"), ("PACKETFLUX-STANDBYPOWER", "ruleswitchstandby"), ("PACKETFLUX-STANDBYPOWER", "rulereturnprimary"), ("PACKETFLUX-STANDBYPOWER", "rulestandbygood"), ("PACKETFLUX-STANDBYPOWER", "rulestopstandby"), ("PACKETFLUX-STANDBYPOWER", "ruleexercisestandby"), ("PACKETFLUX-STANDBYPOWER", "webcontrol1"), ("PACKETFLUX-STANDBYPOWER", "webcontrol2"), ("PACKETFLUX-STANDBYPOWER", "webcontrol3"), ("PACKETFLUX-STANDBYPOWER", "webcontrol4"), ("PACKETFLUX-STANDBYPOWER", "webcontrol5"), ("PACKETFLUX-STANDBYPOWER", "webcontrol6"), ("PACKETFLUX-STANDBYPOWER", "webcontrol7"), ("PACKETFLUX-STANDBYPOWER", "webcontrol8"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    packetfluxStandbypowerAllObjects = packetfluxStandbypowerAllObjects.setStatus('current')
mibBuilder.exportSymbols("PACKETFLUX-STANDBYPOWER", rulereturnprimary=rulereturnprimary, mtr1voltage=mtr1voltage, laststandbyunsuccessfulstart=laststandbyunsuccessfulstart, switch5closed=switch5closed, ruleexercisestandby=ruleexercisestandby, recentstalls=recentstalls, webcontrol4=webcontrol4, PYSNMP_MODULE_ID=standbypower, webcontrol6=webcontrol6, ac2voltage=ac2voltage, switch4closed=switch4closed, relay4on=relay4on, mtr2voltage=mtr2voltage, relay5on=relay5on, switch3closed=switch3closed, totalunsuccessfulstarts=totalunsuccessfulstarts, currentstandbyruntime=currentstandbyruntime, powercontrollerstate=powercontrollerstate, totalstalls=totalstalls, webcontrol8=webcontrol8, rulestopstandby=rulestopstandby, ac2frequency=ac2frequency, webcontrol5=webcontrol5, standbypower=standbypower, laststandbyfailure=laststandbyfailure, shuntvoltage=shuntvoltage, numberoftransfers=numberoftransfers, packetfluxStandbypowerAllObjects=packetfluxStandbypowerAllObjects, relay1on=relay1on, recentunsuccessfulstarts=recentunsuccessfulstarts, standbypowerGroups=standbypowerGroups, ruleswitchstandby=ruleswitchstandby, temperature=temperature, currenttimeonprimary=currenttimeonprimary, standbypowerstate=standbypowerstate, switch1closed=switch1closed, totaltimeonstandby=totaltimeonstandby, laststandbygracefulstop=laststandbygracefulstop, webcontrol1=webcontrol1, totaltimeonprimary=totaltimeonprimary, ac1voltage=ac1voltage, relay3on=relay3on, pwr1voltage=pwr1voltage, enabled=enabled, laststandbyrun=laststandbyrun, webcontrol2=webcontrol2, rulestandbygood=rulestandbygood, currenttimeonstandby=currenttimeonstandby, relay7on=relay7on, webcontrol7=webcontrol7, numberofstarts=numberofstarts, relay6on=relay6on, ac1frequency=ac1frequency, standbypowerConformance=standbypowerConformance, relay2on=relay2on, pwr2voltage=pwr2voltage, webcontrol3=webcontrol3, transferswitchstate=transferswitchstate, switch2closed=switch2closed, totalstandbyruntime=totalstandbyruntime)
