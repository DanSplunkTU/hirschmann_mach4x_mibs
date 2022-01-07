#
# PySNMP MIB module RFC1389-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/RFC1389-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 15:51:05 2022
# On host fv-az135-792 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, NotificationType, Gauge32, ObjectIdentity, Unsigned32, Counter32, MibIdentifier, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, mib_2, IpAddress, Bits, ModuleIdentity, iso, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "NotificationType", "Gauge32", "ObjectIdentity", "Unsigned32", "Counter32", "MibIdentifier", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "mib-2", "IpAddress", "Bits", "ModuleIdentity", "iso", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
rip2 = MibIdentifier((1, 3, 6, 1, 2, 1, 23))
class RouteTag(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(2, 2)
    fixedLength = 2

class Validation(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("valid", 1), ("invalid", 2))

rip2GlobalGroup = MibIdentifier((1, 3, 6, 1, 2, 1, 23, 1))
rip2GlobalRouteChanges = MibScalar((1, 3, 6, 1, 2, 1, 23, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rip2GlobalRouteChanges.setStatus('mandatory')
rip2GlobalQueries = MibScalar((1, 3, 6, 1, 2, 1, 23, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rip2GlobalQueries.setStatus('mandatory')
rip2IfStatTable = MibTable((1, 3, 6, 1, 2, 1, 23, 2), )
if mibBuilder.loadTexts: rip2IfStatTable.setStatus('mandatory')
rip2IfStatEntry = MibTableRow((1, 3, 6, 1, 2, 1, 23, 2, 1), ).setIndexNames((0, "RFC1389-MIB", "rip2IfStatAddress"))
if mibBuilder.loadTexts: rip2IfStatEntry.setStatus('mandatory')
rip2IfStatAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 23, 2, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rip2IfStatAddress.setStatus('mandatory')
rip2IfStatRcvBadPackets = MibTableColumn((1, 3, 6, 1, 2, 1, 23, 2, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rip2IfStatRcvBadPackets.setStatus('mandatory')
rip2IfStatRcvBadRoutes = MibTableColumn((1, 3, 6, 1, 2, 1, 23, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rip2IfStatRcvBadRoutes.setStatus('mandatory')
rip2IfStatSentUpdates = MibTableColumn((1, 3, 6, 1, 2, 1, 23, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rip2IfStatSentUpdates.setStatus('mandatory')
rip2IfStatStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 23, 2, 1, 5), Validation().clone('valid')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rip2IfStatStatus.setStatus('mandatory')
rip2IfConfTable = MibTable((1, 3, 6, 1, 2, 1, 23, 3), )
if mibBuilder.loadTexts: rip2IfConfTable.setStatus('mandatory')
rip2IfConfEntry = MibTableRow((1, 3, 6, 1, 2, 1, 23, 3, 1), ).setIndexNames((0, "RFC1389-MIB", "rip2IfConfAddress"))
if mibBuilder.loadTexts: rip2IfConfEntry.setStatus('mandatory')
rip2IfConfAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 23, 3, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rip2IfConfAddress.setStatus('mandatory')
rip2IfConfDomain = MibTableColumn((1, 3, 6, 1, 2, 1, 23, 3, 1, 2), RouteTag().clone(hexValue="0000")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rip2IfConfDomain.setStatus('mandatory')
rip2IfConfAuthType = MibTableColumn((1, 3, 6, 1, 2, 1, 23, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noAuthentication", 1), ("simplePassword", 2))).clone('noAuthentication')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rip2IfConfAuthType.setStatus('mandatory')
rip2IfConfAuthKey = MibTableColumn((1, 3, 6, 1, 2, 1, 23, 3, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 16)).clone(hexValue="")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rip2IfConfAuthKey.setStatus('mandatory')
rip2IfConfSend = MibTableColumn((1, 3, 6, 1, 2, 1, 23, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("doNotSend", 1), ("ripVersion1", 2), ("rip1Compatible", 3), ("ripVersion2", 4))).clone('rip1Compatible')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rip2IfConfSend.setStatus('mandatory')
rip2IfConfReceive = MibTableColumn((1, 3, 6, 1, 2, 1, 23, 3, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("rip1", 1), ("rip2", 2), ("rip1OrRip2", 3))).clone('rip1OrRip2')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rip2IfConfReceive.setStatus('mandatory')
rip2IfConfDefaultMetric = MibTableColumn((1, 3, 6, 1, 2, 1, 23, 3, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rip2IfConfDefaultMetric.setStatus('mandatory')
rip2IfConfStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 23, 3, 1, 8), Validation().clone('valid')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rip2IfConfStatus.setStatus('mandatory')
rip2PeerTable = MibTable((1, 3, 6, 1, 2, 1, 23, 4), )
if mibBuilder.loadTexts: rip2PeerTable.setStatus('mandatory')
rip2PeerEntry = MibTableRow((1, 3, 6, 1, 2, 1, 23, 4, 1), ).setIndexNames((0, "RFC1389-MIB", "rip2PeerAddress"), (0, "RFC1389-MIB", "rip2PeerDomain"))
if mibBuilder.loadTexts: rip2PeerEntry.setStatus('mandatory')
rip2PeerAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 23, 4, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rip2PeerAddress.setStatus('mandatory')
rip2PeerDomain = MibTableColumn((1, 3, 6, 1, 2, 1, 23, 4, 1, 2), RouteTag()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rip2PeerDomain.setStatus('mandatory')
rip2PeerLastUpdate = MibTableColumn((1, 3, 6, 1, 2, 1, 23, 4, 1, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rip2PeerLastUpdate.setStatus('mandatory')
rip2PeerVersion = MibTableColumn((1, 3, 6, 1, 2, 1, 23, 4, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rip2PeerVersion.setStatus('mandatory')
rip2PeerRcvBadPackets = MibTableColumn((1, 3, 6, 1, 2, 1, 23, 4, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rip2PeerRcvBadPackets.setStatus('mandatory')
rip2PeerRcvBadRoutes = MibTableColumn((1, 3, 6, 1, 2, 1, 23, 4, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rip2PeerRcvBadRoutes.setStatus('mandatory')
mibBuilder.exportSymbols("RFC1389-MIB", rip2IfConfDefaultMetric=rip2IfConfDefaultMetric, rip2IfStatStatus=rip2IfStatStatus, rip2IfStatTable=rip2IfStatTable, rip2IfStatSentUpdates=rip2IfStatSentUpdates, rip2IfStatRcvBadPackets=rip2IfStatRcvBadPackets, rip2PeerEntry=rip2PeerEntry, rip2IfStatAddress=rip2IfStatAddress, rip2IfStatRcvBadRoutes=rip2IfStatRcvBadRoutes, rip2=rip2, rip2GlobalRouteChanges=rip2GlobalRouteChanges, rip2IfConfAddress=rip2IfConfAddress, rip2IfConfReceive=rip2IfConfReceive, rip2PeerTable=rip2PeerTable, rip2GlobalGroup=rip2GlobalGroup, rip2IfConfSend=rip2IfConfSend, rip2GlobalQueries=rip2GlobalQueries, rip2PeerDomain=rip2PeerDomain, rip2IfConfAuthType=rip2IfConfAuthType, rip2PeerAddress=rip2PeerAddress, RouteTag=RouteTag, rip2IfConfDomain=rip2IfConfDomain, rip2IfConfStatus=rip2IfConfStatus, Validation=Validation, rip2PeerLastUpdate=rip2PeerLastUpdate, rip2IfStatEntry=rip2IfStatEntry, rip2PeerVersion=rip2PeerVersion, rip2IfConfTable=rip2IfConfTable, rip2IfConfEntry=rip2IfConfEntry, rip2PeerRcvBadPackets=rip2PeerRcvBadPackets, rip2IfConfAuthKey=rip2IfConfAuthKey, rip2PeerRcvBadRoutes=rip2PeerRcvBadRoutes)
