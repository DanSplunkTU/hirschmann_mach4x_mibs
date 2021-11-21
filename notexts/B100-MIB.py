#
# PySNMP MIB module B100-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/kemp/B100-MIB
# Produced by pysmi-1.1.3 at Sun Nov 21 00:46:22 2021
# On host fv-az39-63 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
InetAddressType, InetAddress, InetPortNumber = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress", "InetPortNumber")
one4net, = mibBuilder.importSymbols("ONE4NET-MIB", "one4net")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Unsigned32, IpAddress, Gauge32, Counter32, Counter64, TimeTicks, Integer32, MibIdentifier, iso, ObjectIdentity, ModuleIdentity, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Unsigned32", "IpAddress", "Gauge32", "Counter32", "Counter64", "TimeTicks", "Integer32", "MibIdentifier", "iso", "ObjectIdentity", "ModuleIdentity", "NotificationType")
TimeInterval, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TimeInterval", "TextualConvention", "DisplayString")
b100 = ModuleIdentity((1, 3, 6, 1, 4, 1, 12196, 13))
b100.setRevisions(('2011-12-01 00:00',))
if mibBuilder.loadTexts: b100.setLastUpdated('201112010000Z')
if mibBuilder.loadTexts: b100.setOrganization('KEMP Technologies')
b100VSTable = MibTable((1, 3, 6, 1, 4, 1, 12196, 13, 1), )
if mibBuilder.loadTexts: b100VSTable.setStatus('current')
b100RSTable = MibTable((1, 3, 6, 1, 4, 1, 12196, 13, 2), )
if mibBuilder.loadTexts: b100RSTable.setStatus('current')
b100NotificationsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 12196, 13, 3))
version = MibScalar((1, 3, 6, 1, 4, 1, 12196, 13, 0, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: version.setStatus('current')
numServices = MibScalar((1, 3, 6, 1, 4, 1, 12196, 13, 0, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: numServices.setStatus('current')
hashTableSize = MibScalar((1, 3, 6, 1, 4, 1, 12196, 13, 0, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hashTableSize.setStatus('current')
tcpTimeOut = MibScalar((1, 3, 6, 1, 4, 1, 12196, 13, 0, 4), TimeInterval()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tcpTimeOut.setStatus('current')
tcpFinTimeOut = MibScalar((1, 3, 6, 1, 4, 1, 12196, 13, 0, 5), TimeInterval()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tcpFinTimeOut.setStatus('current')
udpTimeOut = MibScalar((1, 3, 6, 1, 4, 1, 12196, 13, 0, 6), TimeInterval()).setMaxAccess("readonly")
if mibBuilder.loadTexts: udpTimeOut.setStatus('current')
daemonState = MibScalar((1, 3, 6, 1, 4, 1, 12196, 13, 0, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("none", 0), ("master", 1), ("backup", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: daemonState.setStatus('current')
mcastInterface = MibScalar((1, 3, 6, 1, 4, 1, 12196, 13, 0, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcastInterface.setStatus('current')
hAstate = MibScalar((1, 3, 6, 1, 4, 1, 12196, 13, 0, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("none", 0), ("master", 1), ("standby", 2), ("passive", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hAstate.setStatus('current')
patchVersion = MibScalar((1, 3, 6, 1, 4, 1, 12196, 13, 0, 10), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: patchVersion.setStatus('current')
totalTps = MibScalar((1, 3, 6, 1, 4, 1, 12196, 13, 0, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: totalTps.setStatus('current')
sslTps = MibScalar((1, 3, 6, 1, 4, 1, 12196, 13, 0, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sslTps.setStatus('current')
vsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12196, 13, 1, 1), ).setIndexNames((0, "B100-MIB", "vSidx"))
if mibBuilder.loadTexts: vsEntry.setStatus('current')
vSidx = MibTableColumn((1, 3, 6, 1, 4, 1, 12196, 13, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vSidx.setStatus('current')
vSip = MibTableColumn((1, 3, 6, 1, 4, 1, 12196, 13, 1, 1, 2), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vSip.setStatus('current')
vSport = MibTableColumn((1, 3, 6, 1, 4, 1, 12196, 13, 1, 1, 3), InetPortNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vSport.setStatus('current')
vSaddrtype = MibTableColumn((1, 3, 6, 1, 4, 1, 12196, 13, 1, 1, 4), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vSaddrtype.setStatus('current')
vSprotocol = MibTableColumn((1, 3, 6, 1, 4, 1, 12196, 13, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(6, 17))).clone(namedValues=NamedValues(("tcp", 6), ("udp", 17)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vSprotocol.setStatus('current')
vSschedulingMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 12196, 13, 1, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vSschedulingMethod.setStatus('current')
vSpersistenceTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 12196, 13, 1, 1, 7), TimeInterval()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vSpersistenceTimeout.setStatus('current')
vScheckerType = MibTableColumn((1, 3, 6, 1, 4, 1, 12196, 13, 1, 1, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vScheckerType.setStatus('current')
vSadaptiveMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 12196, 13, 1, 1, 9), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vSadaptiveMethod.setStatus('current')
vSnumDests = MibTableColumn((1, 3, 6, 1, 4, 1, 12196, 13, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vSnumDests.setStatus('current')
vSl7persist = MibTableColumn((1, 3, 6, 1, 4, 1, 12196, 13, 1, 1, 11), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vSl7persist.setStatus('current')
vSl7cookieId = MibTableColumn((1, 3, 6, 1, 4, 1, 12196, 13, 1, 1, 12), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vSl7cookieId.setStatus('current')
vSname = MibTableColumn((1, 3, 6, 1, 4, 1, 12196, 13, 1, 1, 13), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vSname.setStatus('current')
vSstate = MibTableColumn((1, 3, 6, 1, 4, 1, 12196, 13, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 4, 5, 6, 7))).clone(namedValues=NamedValues(("inService", 1), ("outOfService", 2), ("disabled", 4), ("sorry", 5), ("redirect", 6), ("errormsg", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vSstate.setStatus('current')
vSfollow = MibTableColumn((1, 3, 6, 1, 4, 1, 12196, 13, 1, 1, 15), InetPortNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vSfollow.setStatus('current')
vSConns = MibTableColumn((1, 3, 6, 1, 4, 1, 12196, 13, 1, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vSConns.setStatus('current')
vSInPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 12196, 13, 1, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vSInPkts.setStatus('current')
vSOutPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 12196, 13, 1, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vSOutPkts.setStatus('current')
vSInBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 12196, 13, 1, 1, 19), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vSInBytes.setStatus('current')
vSOutBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 12196, 13, 1, 1, 20), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vSOutBytes.setStatus('current')
vSActivConns = MibTableColumn((1, 3, 6, 1, 4, 1, 12196, 13, 1, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vSActivConns.setStatus('current')
rsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12196, 13, 2, 1), ).setIndexNames((0, "B100-MIB", "rSidx"))
if mibBuilder.loadTexts: rsEntry.setStatus('current')
rSvsidx = MibTableColumn((1, 3, 6, 1, 4, 1, 12196, 13, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rSvsidx.setStatus('current')
rSip = MibTableColumn((1, 3, 6, 1, 4, 1, 12196, 13, 2, 1, 2), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rSip.setStatus('current')
rSport = MibTableColumn((1, 3, 6, 1, 4, 1, 12196, 13, 2, 1, 3), InetPortNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rSport.setStatus('current')
rSaddrtype = MibTableColumn((1, 3, 6, 1, 4, 1, 12196, 13, 2, 1, 4), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rSaddrtype.setStatus('current')
rSidx = MibTableColumn((1, 3, 6, 1, 4, 1, 12196, 13, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rSidx.setStatus('current')
rSforwardingMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 12196, 13, 2, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rSforwardingMethod.setStatus('current')
rSweight = MibTableColumn((1, 3, 6, 1, 4, 1, 12196, 13, 2, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rSweight.setStatus('current')
rSstate = MibTableColumn((1, 3, 6, 1, 4, 1, 12196, 13, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 4))).clone(namedValues=NamedValues(("inService", 1), ("outOfService", 2), ("disabled", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rSstate.setStatus('current')
rSConns = MibTableColumn((1, 3, 6, 1, 4, 1, 12196, 13, 2, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rSConns.setStatus('current')
rSInPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 12196, 13, 2, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rSInPkts.setStatus('current')
rSOutPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 12196, 13, 2, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rSOutPkts.setStatus('current')
rSInBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 12196, 13, 2, 1, 15), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rSInBytes.setStatus('current')
rSOutBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 12196, 13, 2, 1, 16), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rSOutBytes.setStatus('current')
rSActiveConns = MibTableColumn((1, 3, 6, 1, 4, 1, 12196, 13, 2, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rSActiveConns.setStatus('current')
rSInactiveConns = MibTableColumn((1, 3, 6, 1, 4, 1, 12196, 13, 2, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rSInactiveConns.setStatus('current')
adaptivInterval = MibScalar((1, 3, 6, 1, 4, 1, 12196, 13, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adaptivInterval.setStatus('current')
adaptivUrl = MibScalar((1, 3, 6, 1, 4, 1, 12196, 13, 14), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 1023))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adaptivUrl.setStatus('current')
adaptivCtrlMinP = MibScalar((1, 3, 6, 1, 4, 1, 12196, 13, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adaptivCtrlMinP.setStatus('current')
adaptivMinWeight = MibScalar((1, 3, 6, 1, 4, 1, 12196, 13, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adaptivMinWeight.setStatus('current')
b100Notifications = MibIdentifier((1, 3, 6, 1, 4, 1, 12196, 13, 3, 1))
vSstateChange = NotificationType((1, 3, 6, 1, 4, 1, 12196, 13, 3, 1, 1)).setObjects(("B100-MIB", "vSstate"), ("B100-MIB", "vSip"), ("B100-MIB", "vSport"), ("B100-MIB", "vSaddrtype"), ("B100-MIB", "vSname"), ("B100-MIB", "vSidx"))
if mibBuilder.loadTexts: vSstateChange.setStatus('current')
rSstateChange = NotificationType((1, 3, 6, 1, 4, 1, 12196, 13, 3, 1, 2)).setObjects(("B100-MIB", "rSstate"), ("B100-MIB", "rSip"), ("B100-MIB", "rSport"), ("B100-MIB", "rSaddrtype"), ("B100-MIB", "rSidx"), ("B100-MIB", "vSip"), ("B100-MIB", "vSport"), ("B100-MIB", "vSaddrtype"), ("B100-MIB", "vSname"), ("B100-MIB", "vSidx"))
if mibBuilder.loadTexts: rSstateChange.setStatus('current')
hAstateChange = NotificationType((1, 3, 6, 1, 4, 1, 12196, 13, 3, 1, 3)).setObjects(("B100-MIB", "hAstate"))
if mibBuilder.loadTexts: hAstateChange.setStatus('current')
licenseExceeded = NotificationType((1, 3, 6, 1, 4, 1, 12196, 13, 3, 1, 4))
if mibBuilder.loadTexts: licenseExceeded.setStatus('current')
mibBuilder.exportSymbols("B100-MIB", vSInBytes=vSInBytes, vSname=vSname, b100RSTable=b100RSTable, rSInPkts=rSInPkts, b100VSTable=b100VSTable, rSOutPkts=rSOutPkts, tcpTimeOut=tcpTimeOut, sslTps=sslTps, vSprotocol=vSprotocol, vSstate=vSstate, rSvsidx=rSvsidx, rSaddrtype=rSaddrtype, hashTableSize=hashTableSize, vSConns=vSConns, vSActivConns=vSActivConns, rSweight=rSweight, version=version, vSstateChange=vSstateChange, vSschedulingMethod=vSschedulingMethod, b100NotificationsPrefix=b100NotificationsPrefix, daemonState=daemonState, vSip=vSip, vSl7persist=vSl7persist, hAstate=hAstate, vSadaptiveMethod=vSadaptiveMethod, rSforwardingMethod=rSforwardingMethod, rSstate=rSstate, rSidx=rSidx, rsEntry=rsEntry, vSpersistenceTimeout=vSpersistenceTimeout, vSidx=vSidx, tcpFinTimeOut=tcpFinTimeOut, mcastInterface=mcastInterface, adaptivUrl=adaptivUrl, rSOutBytes=rSOutBytes, vSInPkts=vSInPkts, PYSNMP_MODULE_ID=b100, vsEntry=vsEntry, vSOutBytes=vSOutBytes, adaptivMinWeight=adaptivMinWeight, totalTps=totalTps, rSConns=rSConns, rSInactiveConns=rSInactiveConns, vSnumDests=vSnumDests, hAstateChange=hAstateChange, numServices=numServices, patchVersion=patchVersion, vScheckerType=vScheckerType, udpTimeOut=udpTimeOut, rSport=rSport, b100Notifications=b100Notifications, adaptivCtrlMinP=adaptivCtrlMinP, licenseExceeded=licenseExceeded, b100=b100, adaptivInterval=adaptivInterval, vSfollow=vSfollow, rSInBytes=rSInBytes, rSstateChange=rSstateChange, vSport=vSport, vSOutPkts=vSOutPkts, rSActiveConns=rSActiveConns, vSaddrtype=vSaddrtype, rSip=rSip, vSl7cookieId=vSl7cookieId)
