#
# PySNMP MIB module B100-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/kemp/B100-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 18:11:34 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
InetAddressType, InetAddress, InetPortNumber = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress", "InetPortNumber")
one4net, = mibBuilder.importSymbols("ONE4NET-MIB", "one4net")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, ModuleIdentity, iso, Counter64, MibIdentifier, TimeTicks, IpAddress, Gauge32, NotificationType, Counter32, Bits, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "ModuleIdentity", "iso", "Counter64", "MibIdentifier", "TimeTicks", "IpAddress", "Gauge32", "NotificationType", "Counter32", "Bits", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32")
TextualConvention, TimeInterval, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TimeInterval", "DisplayString")
b100 = ModuleIdentity((1, 3, 6, 1, 4, 1, 12196, 13))
b100.setRevisions(('2011-12-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: b100.setRevisionsDescriptions(('version V6.0',))
if mibBuilder.loadTexts: b100.setLastUpdated('201112010000Z')
if mibBuilder.loadTexts: b100.setOrganization('KEMP Technologies')
if mibBuilder.loadTexts: b100.setContactInfo('email:      support@kemptechnologies.com')
if mibBuilder.loadTexts: b100.setDescription('Load Master configuration.')
b100VSTable = MibTable((1, 3, 6, 1, 4, 1, 12196, 13, 1), )
if mibBuilder.loadTexts: b100VSTable.setStatus('current')
if mibBuilder.loadTexts: b100VSTable.setDescription('A table containing ipvs Virtual Service (VS) specific information.')
b100RSTable = MibTable((1, 3, 6, 1, 4, 1, 12196, 13, 2), )
if mibBuilder.loadTexts: b100RSTable.setStatus('current')
if mibBuilder.loadTexts: b100RSTable.setDescription('A table containing ipvs Virtual Service (VS) specific information.')
b100NotificationsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 12196, 13, 3))
version = MibScalar((1, 3, 6, 1, 4, 1, 12196, 13, 0, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: version.setStatus('current')
if mibBuilder.loadTexts: version.setDescription('Version of the IPVS netfilter modules')
numServices = MibScalar((1, 3, 6, 1, 4, 1, 12196, 13, 0, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: numServices.setStatus('current')
if mibBuilder.loadTexts: numServices.setDescription('current number of virtual services')
hashTableSize = MibScalar((1, 3, 6, 1, 4, 1, 12196, 13, 0, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hashTableSize.setStatus('current')
if mibBuilder.loadTexts: hashTableSize.setDescription('size of hash table for L4 connection contexts')
tcpTimeOut = MibScalar((1, 3, 6, 1, 4, 1, 12196, 13, 0, 4), TimeInterval()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tcpTimeOut.setStatus('current')
if mibBuilder.loadTexts: tcpTimeOut.setDescription('L4 TCP Timeout [s] for established connections')
tcpFinTimeOut = MibScalar((1, 3, 6, 1, 4, 1, 12196, 13, 0, 5), TimeInterval()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tcpFinTimeOut.setStatus('current')
if mibBuilder.loadTexts: tcpFinTimeOut.setDescription('L4 TCP Timeout [s] for connections in FIN wait state')
udpTimeOut = MibScalar((1, 3, 6, 1, 4, 1, 12196, 13, 0, 6), TimeInterval()).setMaxAccess("readonly")
if mibBuilder.loadTexts: udpTimeOut.setStatus('current')
if mibBuilder.loadTexts: udpTimeOut.setDescription('L4 UDP Timeout [s]')
daemonState = MibScalar((1, 3, 6, 1, 4, 1, 12196, 13, 0, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("none", 0), ("master", 1), ("backup", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: daemonState.setStatus('current')
if mibBuilder.loadTexts: daemonState.setDescription('state of daemon for synchronisation of l4 connection contexts')
mcastInterface = MibScalar((1, 3, 6, 1, 4, 1, 12196, 13, 0, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcastInterface.setStatus('current')
if mibBuilder.loadTexts: mcastInterface.setDescription('multicast interface used by l4 inter machine update daemon')
hAstate = MibScalar((1, 3, 6, 1, 4, 1, 12196, 13, 0, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("none", 0), ("master", 1), ("standby", 2), ("passive", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hAstate.setStatus('current')
if mibBuilder.loadTexts: hAstate.setDescription('Current state of HA on current machine')
patchVersion = MibScalar((1, 3, 6, 1, 4, 1, 12196, 13, 0, 10), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: patchVersion.setStatus('current')
if mibBuilder.loadTexts: patchVersion.setDescription('Currently installed Software Patch version')
totalTps = MibScalar((1, 3, 6, 1, 4, 1, 12196, 13, 0, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: totalTps.setStatus('current')
if mibBuilder.loadTexts: totalTps.setDescription('Total Current TPS')
sslTps = MibScalar((1, 3, 6, 1, 4, 1, 12196, 13, 0, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sslTps.setStatus('current')
if mibBuilder.loadTexts: sslTps.setDescription('Current SSL TPS')
vsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12196, 13, 1, 1), ).setIndexNames((0, "B100-MIB", "vSidx"))
if mibBuilder.loadTexts: vsEntry.setStatus('current')
if mibBuilder.loadTexts: vsEntry.setDescription('information about a VS')
vSidx = MibTableColumn((1, 3, 6, 1, 4, 1, 12196, 13, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vSidx.setStatus('current')
if mibBuilder.loadTexts: vSidx.setDescription('Unique VS Id')
vSip = MibTableColumn((1, 3, 6, 1, 4, 1, 12196, 13, 1, 1, 2), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vSip.setStatus('current')
if mibBuilder.loadTexts: vSip.setDescription('IP address of VS Differented by AddressType')
vSport = MibTableColumn((1, 3, 6, 1, 4, 1, 12196, 13, 1, 1, 3), InetPortNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vSport.setStatus('current')
if mibBuilder.loadTexts: vSport.setDescription('VS port number')
vSaddrtype = MibTableColumn((1, 3, 6, 1, 4, 1, 12196, 13, 1, 1, 4), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vSaddrtype.setStatus('current')
if mibBuilder.loadTexts: vSaddrtype.setDescription('VS address type')
vSprotocol = MibTableColumn((1, 3, 6, 1, 4, 1, 12196, 13, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(6, 17))).clone(namedValues=NamedValues(("tcp", 6), ("udp", 17)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vSprotocol.setStatus('current')
if mibBuilder.loadTexts: vSprotocol.setDescription('VS protocol TCP/UDP')
vSschedulingMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 12196, 13, 1, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vSschedulingMethod.setStatus('current')
if mibBuilder.loadTexts: vSschedulingMethod.setDescription('scheduling method')
vSpersistenceTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 12196, 13, 1, 1, 7), TimeInterval()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vSpersistenceTimeout.setStatus('current')
if mibBuilder.loadTexts: vSpersistenceTimeout.setDescription('timeout [s] for persistent connections')
vScheckerType = MibTableColumn((1, 3, 6, 1, 4, 1, 12196, 13, 1, 1, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vScheckerType.setStatus('current')
if mibBuilder.loadTexts: vScheckerType.setDescription('Type of checker associated with VS')
vSadaptiveMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 12196, 13, 1, 1, 9), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vSadaptiveMethod.setStatus('current')
if mibBuilder.loadTexts: vSadaptiveMethod.setDescription('Type of adaptiv method used with VS')
vSnumDests = MibTableColumn((1, 3, 6, 1, 4, 1, 12196, 13, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vSnumDests.setStatus('current')
if mibBuilder.loadTexts: vSnumDests.setDescription('Number of destinations (RS) for this VS')
vSl7persist = MibTableColumn((1, 3, 6, 1, 4, 1, 12196, 13, 1, 1, 11), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vSl7persist.setStatus('current')
if mibBuilder.loadTexts: vSl7persist.setDescription('Type of persistence used with VS')
vSl7cookieId = MibTableColumn((1, 3, 6, 1, 4, 1, 12196, 13, 1, 1, 12), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vSl7cookieId.setStatus('current')
if mibBuilder.loadTexts: vSl7cookieId.setDescription('Name of the cookie associated with the VS')
vSname = MibTableColumn((1, 3, 6, 1, 4, 1, 12196, 13, 1, 1, 13), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vSname.setStatus('current')
if mibBuilder.loadTexts: vSname.setDescription('Name of the VS')
vSstate = MibTableColumn((1, 3, 6, 1, 4, 1, 12196, 13, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 4, 5, 6, 7))).clone(namedValues=NamedValues(("inService", 1), ("outOfService", 2), ("disabled", 4), ("sorry", 5), ("redirect", 6), ("errormsg", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vSstate.setStatus('current')
if mibBuilder.loadTexts: vSstate.setDescription('state of VS')
vSfollow = MibTableColumn((1, 3, 6, 1, 4, 1, 12196, 13, 1, 1, 15), InetPortNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vSfollow.setStatus('current')
if mibBuilder.loadTexts: vSfollow.setDescription('VS follow port number')
vSConns = MibTableColumn((1, 3, 6, 1, 4, 1, 12196, 13, 1, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vSConns.setStatus('current')
if mibBuilder.loadTexts: vSConns.setDescription('the total number of connections for this VS')
vSInPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 12196, 13, 1, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vSInPkts.setStatus('current')
if mibBuilder.loadTexts: vSInPkts.setDescription('the total number of incomming pakets to this VS')
vSOutPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 12196, 13, 1, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vSOutPkts.setStatus('current')
if mibBuilder.loadTexts: vSOutPkts.setDescription('the total number of outgoing pakets from this VS')
vSInBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 12196, 13, 1, 1, 19), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vSInBytes.setStatus('current')
if mibBuilder.loadTexts: vSInBytes.setDescription('the total number of incomming bytes to this VS')
vSOutBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 12196, 13, 1, 1, 20), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vSOutBytes.setStatus('current')
if mibBuilder.loadTexts: vSOutBytes.setDescription('the number of outgoing bytes from this VS')
vSActivConns = MibTableColumn((1, 3, 6, 1, 4, 1, 12196, 13, 1, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vSActivConns.setStatus('current')
if mibBuilder.loadTexts: vSActivConns.setDescription('the current number of connections for this VS')
rsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12196, 13, 2, 1), ).setIndexNames((0, "B100-MIB", "rSidx"))
if mibBuilder.loadTexts: rsEntry.setStatus('current')
if mibBuilder.loadTexts: rsEntry.setDescription('information about an RS on a VS')
rSvsidx = MibTableColumn((1, 3, 6, 1, 4, 1, 12196, 13, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rSvsidx.setStatus('current')
if mibBuilder.loadTexts: rSvsidx.setDescription('Id of associated VS')
rSip = MibTableColumn((1, 3, 6, 1, 4, 1, 12196, 13, 2, 1, 2), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rSip.setStatus('current')
if mibBuilder.loadTexts: rSip.setDescription('IP address of RS')
rSport = MibTableColumn((1, 3, 6, 1, 4, 1, 12196, 13, 2, 1, 3), InetPortNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rSport.setStatus('current')
if mibBuilder.loadTexts: rSport.setDescription('RS port number')
rSaddrtype = MibTableColumn((1, 3, 6, 1, 4, 1, 12196, 13, 2, 1, 4), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rSaddrtype.setStatus('current')
if mibBuilder.loadTexts: rSaddrtype.setDescription('RS address type')
rSidx = MibTableColumn((1, 3, 6, 1, 4, 1, 12196, 13, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rSidx.setStatus('current')
if mibBuilder.loadTexts: rSidx.setDescription('Unique Id of RS')
rSforwardingMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 12196, 13, 2, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rSforwardingMethod.setStatus('current')
if mibBuilder.loadTexts: rSforwardingMethod.setDescription('forwarding method used for RS')
rSweight = MibTableColumn((1, 3, 6, 1, 4, 1, 12196, 13, 2, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rSweight.setStatus('current')
if mibBuilder.loadTexts: rSweight.setDescription('configured weight of RS')
rSstate = MibTableColumn((1, 3, 6, 1, 4, 1, 12196, 13, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 4))).clone(namedValues=NamedValues(("inService", 1), ("outOfService", 2), ("disabled", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rSstate.setStatus('current')
if mibBuilder.loadTexts: rSstate.setDescription('current state of RS')
rSConns = MibTableColumn((1, 3, 6, 1, 4, 1, 12196, 13, 2, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rSConns.setStatus('current')
if mibBuilder.loadTexts: rSConns.setDescription('the total number of connections for this RS')
rSInPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 12196, 13, 2, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rSInPkts.setStatus('current')
if mibBuilder.loadTexts: rSInPkts.setDescription('the total number of incoming pakets to this RS')
rSOutPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 12196, 13, 2, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rSOutPkts.setStatus('current')
if mibBuilder.loadTexts: rSOutPkts.setDescription('the total number of outgoing pakets from this RS')
rSInBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 12196, 13, 2, 1, 15), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rSInBytes.setStatus('current')
if mibBuilder.loadTexts: rSInBytes.setDescription('the total number of incoming bytes from this RS')
rSOutBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 12196, 13, 2, 1, 16), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rSOutBytes.setStatus('current')
if mibBuilder.loadTexts: rSOutBytes.setDescription('the total number of outgoing bytes from this RS')
rSActiveConns = MibTableColumn((1, 3, 6, 1, 4, 1, 12196, 13, 2, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rSActiveConns.setStatus('current')
if mibBuilder.loadTexts: rSActiveConns.setDescription('the number of active connection for this RS')
rSInactiveConns = MibTableColumn((1, 3, 6, 1, 4, 1, 12196, 13, 2, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rSInactiveConns.setStatus('current')
if mibBuilder.loadTexts: rSInactiveConns.setDescription('the number of inactive connection for this RS')
adaptivInterval = MibScalar((1, 3, 6, 1, 4, 1, 12196, 13, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adaptivInterval.setStatus('current')
if mibBuilder.loadTexts: adaptivInterval.setDescription('Adaptiv scheduling: interval [s]')
adaptivUrl = MibScalar((1, 3, 6, 1, 4, 1, 12196, 13, 14), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 1023))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adaptivUrl.setStatus('current')
if mibBuilder.loadTexts: adaptivUrl.setDescription('Adaptiv scheduling: URL with RS load')
adaptivCtrlMinP = MibScalar((1, 3, 6, 1, 4, 1, 12196, 13, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adaptivCtrlMinP.setStatus('current')
if mibBuilder.loadTexts: adaptivCtrlMinP.setDescription('Adaptiv scheduling: minimum (%) of ctrl variable')
adaptivMinWeight = MibScalar((1, 3, 6, 1, 4, 1, 12196, 13, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adaptivMinWeight.setStatus('current')
if mibBuilder.loadTexts: adaptivMinWeight.setDescription('Adaptiv scheduling: min bound (>0) for adaptiv weight')
b100Notifications = MibIdentifier((1, 3, 6, 1, 4, 1, 12196, 13, 3, 1))
vSstateChange = NotificationType((1, 3, 6, 1, 4, 1, 12196, 13, 3, 1, 1)).setObjects(("B100-MIB", "vSstate"), ("B100-MIB", "vSip"), ("B100-MIB", "vSport"), ("B100-MIB", "vSaddrtype"), ("B100-MIB", "vSname"), ("B100-MIB", "vSidx"))
if mibBuilder.loadTexts: vSstateChange.setStatus('current')
if mibBuilder.loadTexts: vSstateChange.setDescription('Notification sent when a Virtual Service changes state.')
rSstateChange = NotificationType((1, 3, 6, 1, 4, 1, 12196, 13, 3, 1, 2)).setObjects(("B100-MIB", "rSstate"), ("B100-MIB", "rSip"), ("B100-MIB", "rSport"), ("B100-MIB", "rSaddrtype"), ("B100-MIB", "rSidx"), ("B100-MIB", "vSip"), ("B100-MIB", "vSport"), ("B100-MIB", "vSaddrtype"), ("B100-MIB", "vSname"), ("B100-MIB", "vSidx"))
if mibBuilder.loadTexts: rSstateChange.setStatus('current')
if mibBuilder.loadTexts: rSstateChange.setDescription('Notification sent when a Real Server changes state.')
hAstateChange = NotificationType((1, 3, 6, 1, 4, 1, 12196, 13, 3, 1, 3)).setObjects(("B100-MIB", "hAstate"))
if mibBuilder.loadTexts: hAstateChange.setStatus('current')
if mibBuilder.loadTexts: hAstateChange.setDescription('Notification sent when a failover occurs.')
licenseExceeded = NotificationType((1, 3, 6, 1, 4, 1, 12196, 13, 3, 1, 4))
if mibBuilder.loadTexts: licenseExceeded.setStatus('current')
if mibBuilder.loadTexts: licenseExceeded.setDescription('Notification when a timed License has expired.')
mibBuilder.exportSymbols("B100-MIB", b100RSTable=b100RSTable, vSschedulingMethod=vSschedulingMethod, vSConns=vSConns, b100VSTable=b100VSTable, rSOutPkts=rSOutPkts, daemonState=daemonState, rSweight=rSweight, patchVersion=patchVersion, vSport=vSport, vScheckerType=vScheckerType, b100Notifications=b100Notifications, rSidx=rSidx, vSname=vSname, hAstateChange=hAstateChange, udpTimeOut=udpTimeOut, vSl7persist=vSl7persist, vSpersistenceTimeout=vSpersistenceTimeout, vSadaptiveMethod=vSadaptiveMethod, vSip=vSip, tcpFinTimeOut=tcpFinTimeOut, vSstateChange=vSstateChange, rSvsidx=rSvsidx, vSfollow=vSfollow, vSActivConns=vSActivConns, vSprotocol=vSprotocol, b100NotificationsPrefix=b100NotificationsPrefix, vSl7cookieId=vSl7cookieId, rSstate=rSstate, rSInBytes=rSInBytes, vSstate=vSstate, rSaddrtype=rSaddrtype, mcastInterface=mcastInterface, licenseExceeded=licenseExceeded, vSInBytes=vSInBytes, rsEntry=rsEntry, rSInPkts=rSInPkts, vSidx=vSidx, tcpTimeOut=tcpTimeOut, version=version, vSOutPkts=vSOutPkts, vSOutBytes=vSOutBytes, rSstateChange=rSstateChange, rSConns=rSConns, rSOutBytes=rSOutBytes, sslTps=sslTps, PYSNMP_MODULE_ID=b100, vSnumDests=vSnumDests, vsEntry=vsEntry, vSaddrtype=vSaddrtype, rSActiveConns=rSActiveConns, hAstate=hAstate, adaptivCtrlMinP=adaptivCtrlMinP, numServices=numServices, adaptivInterval=adaptivInterval, vSInPkts=vSInPkts, rSport=rSport, rSip=rSip, adaptivMinWeight=adaptivMinWeight, rSforwardingMethod=rSforwardingMethod, adaptivUrl=adaptivUrl, totalTps=totalTps, rSInactiveConns=rSInactiveConns, hashTableSize=hashTableSize, b100=b100)
