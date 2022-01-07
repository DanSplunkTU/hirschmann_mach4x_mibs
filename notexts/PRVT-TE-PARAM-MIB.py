#
# PySNMP MIB module PRVT-TE-PARAM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/telco-systems/binos/PRVT-TE-PARAM-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:39:22 2022
# On host fv-az36-988 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
mpls, = mibBuilder.importSymbols("PRVT-CR-LDP-MIB", "mpls")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, NotificationType, Integer32, Counter32, TimeTicks, ObjectIdentity, Gauge32, ModuleIdentity, Counter64, IpAddress, MibIdentifier, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "NotificationType", "Integer32", "Counter32", "TimeTicks", "ObjectIdentity", "Gauge32", "ModuleIdentity", "Counter64", "IpAddress", "MibIdentifier", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
prvtTeParamMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9))
prvtTeParamMib.setRevisions(('2007-12-11 00:00', '2007-10-25 00:00', '2007-08-10 00:00', '2007-06-08 00:00',))
if mibBuilder.loadTexts: prvtTeParamMib.setLastUpdated('200712110000Z')
if mibBuilder.loadTexts: prvtTeParamMib.setOrganization('BATM Advanced Communication')
prvtTeParamMibNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 0))
prvtTeParamMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 1))
prvtTeParamMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 2))
class TeLinkBandwidth(TextualConvention, OctetString):
    reference = 'IEEE Standard for Binary Floating-Point Arithmetic, Standard 754-1985'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

prvtTeParamTable = MibTable((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 1, 4), )
if mibBuilder.loadTexts: prvtTeParamTable.setStatus('current')
prvtTeParamEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 1, 4, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: prvtTeParamEntry.setStatus('current')
prvtTeParamAdminGroupTable = MibTable((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 1, 5), )
if mibBuilder.loadTexts: prvtTeParamAdminGroupTable.setStatus('current')
prvtTeParamAdminGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 1, 5, 1), ).setIndexNames((0, "PRVT-TE-PARAM-MIB", "prvtTeParamAdminGroupId"))
if mibBuilder.loadTexts: prvtTeParamAdminGroupEntry.setStatus('current')
ospfOpaqueEngSupport = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ospfOpaqueEngSupport.setStatus('current')
ospfTeRouterId = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ospfTeRouterId.setStatus('current')
ospfTrafficEngSupport = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ospfTrafficEngSupport.setStatus('current')
prvtTeParamLinkAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 1, 4, 1, 1), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtTeParamLinkAddressType.setStatus('current')
prvtTeParamMetric = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 1, 4, 1, 2), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtTeParamMetric.setStatus('current')
prvtTeParamLinkType = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 1, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("multiAccess", 1), ("pointToPoint", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtTeParamLinkType.setStatus('current')
prvtTeParamPhysicalBandwidth = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 1, 4, 1, 4), TeLinkBandwidth()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtTeParamPhysicalBandwidth.setStatus('current')
prvtTeParamMaximumReservableBandwidth = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 1, 4, 1, 5), TeLinkBandwidth()).setUnits('bps').setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtTeParamMaximumReservableBandwidth.setStatus('current')
prvtTeParamMaxReservableBandwidthPrio0 = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 1, 4, 1, 6), TeLinkBandwidth()).setUnits('bps').setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtTeParamMaxReservableBandwidthPrio0.setStatus('current')
prvtTeParamMaxReservableBandwidthPrio1 = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 1, 4, 1, 7), TeLinkBandwidth()).setUnits('bps').setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtTeParamMaxReservableBandwidthPrio1.setStatus('current')
prvtTeParamMaxReservableBandwidthPrio2 = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 1, 4, 1, 8), TeLinkBandwidth()).setUnits('bps').setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtTeParamMaxReservableBandwidthPrio2.setStatus('current')
prvtTeParamMaxReservableBandwidthPrio3 = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 1, 4, 1, 9), TeLinkBandwidth()).setUnits('bps').setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtTeParamMaxReservableBandwidthPrio3.setStatus('current')
prvtTeParamMaxReservableBandwidthPrio4 = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 1, 4, 1, 10), TeLinkBandwidth()).setUnits('bps').setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtTeParamMaxReservableBandwidthPrio4.setStatus('current')
prvtTeParamMaxReservableBandwidthPrio5 = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 1, 4, 1, 11), TeLinkBandwidth()).setUnits('bps').setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtTeParamMaxReservableBandwidthPrio5.setStatus('current')
prvtTeParamMaxReservableBandwidthPrio6 = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 1, 4, 1, 12), TeLinkBandwidth()).setUnits('bps').setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtTeParamMaxReservableBandwidthPrio6.setStatus('current')
prvtTeParamMaxReservableBandwidthPrio7 = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 1, 4, 1, 13), TeLinkBandwidth()).setUnits('bps').setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtTeParamMaxReservableBandwidthPrio7.setStatus('current')
prvtTeParamReservedBandwidthPrio0 = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 1, 4, 1, 14), TeLinkBandwidth()).setUnits('bps').setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtTeParamReservedBandwidthPrio0.setStatus('current')
prvtTeParamReservedBandwidthPrio1 = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 1, 4, 1, 15), TeLinkBandwidth()).setUnits('bps').setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtTeParamReservedBandwidthPrio1.setStatus('current')
prvtTeParamReservedBandwidthPrio2 = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 1, 4, 1, 16), TeLinkBandwidth()).setUnits('bps').setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtTeParamReservedBandwidthPrio2.setStatus('current')
prvtTeParamReservedBandwidthPrio3 = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 1, 4, 1, 17), TeLinkBandwidth()).setUnits('bps').setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtTeParamReservedBandwidthPrio3.setStatus('current')
prvtTeParamReservedBandwidthPrio4 = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 1, 4, 1, 18), TeLinkBandwidth()).setUnits('bps').setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtTeParamReservedBandwidthPrio4.setStatus('current')
prvtTeParamReservedBandwidthPrio5 = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 1, 4, 1, 19), TeLinkBandwidth()).setUnits('bps').setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtTeParamReservedBandwidthPrio5.setStatus('current')
prvtTeParamReservedBandwidthPrio6 = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 1, 4, 1, 20), TeLinkBandwidth()).setUnits('bps').setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtTeParamReservedBandwidthPrio6.setStatus('current')
prvtTeParamReservedBandwidthPrio7 = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 1, 4, 1, 21), TeLinkBandwidth()).setUnits('bps').setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtTeParamReservedBandwidthPrio7.setStatus('current')
prvtTeParamUnreservedBandwidthPrio0 = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 1, 4, 1, 22), TeLinkBandwidth()).setUnits('bps').setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtTeParamUnreservedBandwidthPrio0.setStatus('current')
prvtTeParamUnreservedBandwidthPrio1 = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 1, 4, 1, 23), TeLinkBandwidth()).setUnits('bps').setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtTeParamUnreservedBandwidthPrio1.setStatus('current')
prvtTeParamUnreservedBandwidthPrio2 = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 1, 4, 1, 24), TeLinkBandwidth()).setUnits('bps').setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtTeParamUnreservedBandwidthPrio2.setStatus('current')
prvtTeParamUnreservedBandwidthPrio3 = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 1, 4, 1, 25), TeLinkBandwidth()).setUnits('bps').setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtTeParamUnreservedBandwidthPrio3.setStatus('current')
prvtTeParamUnreservedBandwidthPrio4 = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 1, 4, 1, 26), TeLinkBandwidth()).setUnits('bps').setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtTeParamUnreservedBandwidthPrio4.setStatus('current')
prvtTeParamUnreservedBandwidthPrio5 = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 1, 4, 1, 27), TeLinkBandwidth()).setUnits('bps').setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtTeParamUnreservedBandwidthPrio5.setStatus('current')
prvtTeParamUnreservedBandwidthPrio6 = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 1, 4, 1, 28), TeLinkBandwidth()).setUnits('bps').setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtTeParamUnreservedBandwidthPrio6.setStatus('current')
prvtTeParamUnreservedBandwidthPrio7 = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 1, 4, 1, 29), TeLinkBandwidth()).setUnits('bps').setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtTeParamUnreservedBandwidthPrio7.setStatus('current')
prvtTeParamResourceClass = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 1, 4, 1, 30), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtTeParamResourceClass.setStatus('current')
prvtTeParamAdminGroupId = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 1, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtTeParamAdminGroupId.setStatus('current')
prvtTeParamAdminGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 1, 5, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtTeParamAdminGroupName.setStatus('current')
prvtCspfStatisticsTable = MibTable((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 1, 6), )
if mibBuilder.loadTexts: prvtCspfStatisticsTable.setStatus('current')
prvtCspfStatisticsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 1, 6, 1), ).setIndexNames((0, "PRVT-TE-PARAM-MIB", "prvtCspfEntIndex"))
if mibBuilder.loadTexts: prvtCspfStatisticsEntry.setStatus('current')
prvtCspfEntIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 1, 6, 1, 1), Unsigned32())
if mibBuilder.loadTexts: prvtCspfEntIndex.setStatus('current')
prvtCspfStatNumRtQueries = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 1, 6, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCspfStatNumRtQueries.setStatus('current')
prvtCspfStatNumRtsClcd = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 1, 6, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCspfStatNumRtsClcd.setStatus('current')
prvtCspfStatNumRtsInCache = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 1, 6, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCspfStatNumRtsInCache.setStatus('current')
prvtCspfStatNumUpdatesRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 1, 6, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCspfStatNumUpdatesRcvd.setStatus('current')
prvtCspfStatNumEntriesDeleted = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 1, 6, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCspfStatNumEntriesDeleted.setStatus('current')
prvtCspfStatNumLinkEntries = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 1, 6, 1, 7), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCspfStatNumLinkEntries.setStatus('current')
prvtCspfStatNumNetworkEntries = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 1, 6, 1, 8), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCspfStatNumNetworkEntries.setStatus('current')
prvtCspfStatNumReturnedCaches = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 1, 6, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCspfStatNumReturnedCaches.setStatus('current')
prvtCspfStatNumBkupQueries = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 1, 6, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCspfStatNumBkupQueries.setStatus('current')
prvtCspfStatNumBkupPathsFound = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 1, 6, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCspfStatNumBkupPathsFound.setStatus('current')
prvtCspfStatNumRouteUpdates = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 1, 6, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCspfStatNumRouteUpdates.setStatus('current')
prvtCspfStatNumDiscardedRoutes = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 1, 6, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCspfStatNumDiscardedRoutes.setStatus('current')
mibBuilder.exportSymbols("PRVT-TE-PARAM-MIB", prvtTeParamTable=prvtTeParamTable, prvtTeParamLinkType=prvtTeParamLinkType, prvtTeParamMaxReservableBandwidthPrio1=prvtTeParamMaxReservableBandwidthPrio1, prvtTeParamReservedBandwidthPrio6=prvtTeParamReservedBandwidthPrio6, prvtCspfStatNumUpdatesRcvd=prvtCspfStatNumUpdatesRcvd, prvtTeParamMaxReservableBandwidthPrio2=prvtTeParamMaxReservableBandwidthPrio2, prvtTeParamMib=prvtTeParamMib, prvtTeParamReservedBandwidthPrio7=prvtTeParamReservedBandwidthPrio7, prvtTeParamMaxReservableBandwidthPrio0=prvtTeParamMaxReservableBandwidthPrio0, prvtTeParamAdminGroupName=prvtTeParamAdminGroupName, prvtTeParamMaximumReservableBandwidth=prvtTeParamMaximumReservableBandwidth, prvtTeParamAdminGroupTable=prvtTeParamAdminGroupTable, prvtTeParamReservedBandwidthPrio4=prvtTeParamReservedBandwidthPrio4, prvtTeParamUnreservedBandwidthPrio5=prvtTeParamUnreservedBandwidthPrio5, prvtTeParamResourceClass=prvtTeParamResourceClass, prvtCspfStatNumNetworkEntries=prvtCspfStatNumNetworkEntries, prvtCspfStatNumDiscardedRoutes=prvtCspfStatNumDiscardedRoutes, prvtCspfEntIndex=prvtCspfEntIndex, prvtTeParamMibObjects=prvtTeParamMibObjects, prvtTeParamUnreservedBandwidthPrio2=prvtTeParamUnreservedBandwidthPrio2, prvtTeParamMaxReservableBandwidthPrio3=prvtTeParamMaxReservableBandwidthPrio3, prvtTeParamUnreservedBandwidthPrio1=prvtTeParamUnreservedBandwidthPrio1, prvtTeParamMibConformance=prvtTeParamMibConformance, prvtTeParamMetric=prvtTeParamMetric, prvtTeParamUnreservedBandwidthPrio6=prvtTeParamUnreservedBandwidthPrio6, prvtTeParamMaxReservableBandwidthPrio7=prvtTeParamMaxReservableBandwidthPrio7, prvtTeParamMaxReservableBandwidthPrio5=prvtTeParamMaxReservableBandwidthPrio5, prvtTeParamUnreservedBandwidthPrio7=prvtTeParamUnreservedBandwidthPrio7, prvtCspfStatNumRouteUpdates=prvtCspfStatNumRouteUpdates, prvtTeParamUnreservedBandwidthPrio4=prvtTeParamUnreservedBandwidthPrio4, prvtTeParamAdminGroupEntry=prvtTeParamAdminGroupEntry, ospfTrafficEngSupport=ospfTrafficEngSupport, prvtTeParamReservedBandwidthPrio3=prvtTeParamReservedBandwidthPrio3, prvtTeParamMibNotifications=prvtTeParamMibNotifications, prvtTeParamReservedBandwidthPrio5=prvtTeParamReservedBandwidthPrio5, prvtCspfStatNumBkupPathsFound=prvtCspfStatNumBkupPathsFound, ospfTeRouterId=ospfTeRouterId, TeLinkBandwidth=TeLinkBandwidth, prvtCspfStatNumRtsClcd=prvtCspfStatNumRtsClcd, PYSNMP_MODULE_ID=prvtTeParamMib, prvtCspfStatisticsTable=prvtCspfStatisticsTable, prvtTeParamEntry=prvtTeParamEntry, prvtTeParamUnreservedBandwidthPrio3=prvtTeParamUnreservedBandwidthPrio3, prvtCspfStatNumRtsInCache=prvtCspfStatNumRtsInCache, prvtCspfStatNumBkupQueries=prvtCspfStatNumBkupQueries, prvtTeParamPhysicalBandwidth=prvtTeParamPhysicalBandwidth, prvtTeParamMaxReservableBandwidthPrio6=prvtTeParamMaxReservableBandwidthPrio6, prvtCspfStatNumLinkEntries=prvtCspfStatNumLinkEntries, prvtTeParamUnreservedBandwidthPrio0=prvtTeParamUnreservedBandwidthPrio0, ospfOpaqueEngSupport=ospfOpaqueEngSupport, prvtTeParamReservedBandwidthPrio2=prvtTeParamReservedBandwidthPrio2, prvtTeParamAdminGroupId=prvtTeParamAdminGroupId, prvtTeParamMaxReservableBandwidthPrio4=prvtTeParamMaxReservableBandwidthPrio4, prvtCspfStatNumRtQueries=prvtCspfStatNumRtQueries, prvtCspfStatisticsEntry=prvtCspfStatisticsEntry, prvtCspfStatNumEntriesDeleted=prvtCspfStatNumEntriesDeleted, prvtTeParamLinkAddressType=prvtTeParamLinkAddressType, prvtCspfStatNumReturnedCaches=prvtCspfStatNumReturnedCaches, prvtTeParamReservedBandwidthPrio0=prvtTeParamReservedBandwidthPrio0, prvtTeParamReservedBandwidthPrio1=prvtTeParamReservedBandwidthPrio1)
