#
# PySNMP MIB module IGMP-STD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/IGMP-STD-MIB
# Produced by pysmi-1.1.3 at Sun Nov 21 00:25:42 2021
# On host fv-az39-63 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
InterfaceIndex, InterfaceIndexOrZero = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "InterfaceIndexOrZero")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
experimental, TimeTicks, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, ModuleIdentity, Gauge32, IpAddress, Bits, ObjectIdentity, Unsigned32, MibIdentifier, NotificationType, Integer32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "experimental", "TimeTicks", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "ModuleIdentity", "Gauge32", "IpAddress", "Bits", "ObjectIdentity", "Unsigned32", "MibIdentifier", "NotificationType", "Integer32", "Counter64")
DisplayString, TruthValue, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "RowStatus", "TextualConvention")
igmpStdMIB = ModuleIdentity((1, 3, 6, 1, 3, 59))
igmpStdMIB.setRevisions(('1999-09-17 12:00',))
if mibBuilder.loadTexts: igmpStdMIB.setLastUpdated('9909171200Z')
if mibBuilder.loadTexts: igmpStdMIB.setOrganization('IETF IDMR Working Group.')
igmpMIBObjects = MibIdentifier((1, 3, 6, 1, 3, 59, 1))
igmp = MibIdentifier((1, 3, 6, 1, 3, 59, 1, 1))
igmpInterfaceTable = MibTable((1, 3, 6, 1, 3, 59, 1, 1, 1), )
if mibBuilder.loadTexts: igmpInterfaceTable.setStatus('current')
igmpInterfaceEntry = MibTableRow((1, 3, 6, 1, 3, 59, 1, 1, 1, 1), ).setIndexNames((0, "IGMP-STD-MIB", "igmpInterfaceIfIndex"))
if mibBuilder.loadTexts: igmpInterfaceEntry.setStatus('current')
igmpInterfaceIfIndex = MibTableColumn((1, 3, 6, 1, 3, 59, 1, 1, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: igmpInterfaceIfIndex.setStatus('current')
igmpInterfaceQueryInterval = MibTableColumn((1, 3, 6, 1, 3, 59, 1, 1, 1, 1, 2), Integer32().clone(125)).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpInterfaceQueryInterval.setStatus('current')
igmpInterfaceStatus = MibTableColumn((1, 3, 6, 1, 3, 59, 1, 1, 1, 1, 3), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpInterfaceStatus.setStatus('current')
igmpInterfaceVersion = MibTableColumn((1, 3, 6, 1, 3, 59, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("version1", 1), ("version2", 2))).clone('version2')).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpInterfaceVersion.setStatus('current')
igmpInterfaceQuerier = MibTableColumn((1, 3, 6, 1, 3, 59, 1, 1, 1, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpInterfaceQuerier.setStatus('current')
igmpInterfaceQueryMaxResponseTime = MibTableColumn((1, 3, 6, 1, 3, 59, 1, 1, 1, 1, 6), Integer32().clone(100)).setUnits('tenths of seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpInterfaceQueryMaxResponseTime.setStatus('current')
igmpInterfaceVersion1QuerierTimer = MibTableColumn((1, 3, 6, 1, 3, 59, 1, 1, 1, 1, 9), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpInterfaceVersion1QuerierTimer.setStatus('current')
igmpInterfaceWrongVersionQueries = MibTableColumn((1, 3, 6, 1, 3, 59, 1, 1, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpInterfaceWrongVersionQueries.setStatus('current')
igmpInterfaceJoins = MibTableColumn((1, 3, 6, 1, 3, 59, 1, 1, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpInterfaceJoins.setStatus('current')
igmpInterfaceGroups = MibTableColumn((1, 3, 6, 1, 3, 59, 1, 1, 1, 1, 13), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpInterfaceGroups.setStatus('current')
igmpInterfaceRobustness = MibTableColumn((1, 3, 6, 1, 3, 59, 1, 1, 1, 1, 14), Integer32().clone(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpInterfaceRobustness.setStatus('current')
igmpInterfaceLastMembQueryIntvl = MibTableColumn((1, 3, 6, 1, 3, 59, 1, 1, 1, 1, 15), Integer32().clone(10)).setUnits('tenths of seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpInterfaceLastMembQueryIntvl.setStatus('current')
igmpInterfaceProxyIfIndex = MibTableColumn((1, 3, 6, 1, 3, 59, 1, 1, 1, 1, 16), InterfaceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpInterfaceProxyIfIndex.setStatus('current')
igmpInterfaceQuerierUpTime = MibTableColumn((1, 3, 6, 1, 3, 59, 1, 1, 1, 1, 17), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpInterfaceQuerierUpTime.setStatus('current')
igmpInterfaceQuerierExpiryTime = MibTableColumn((1, 3, 6, 1, 3, 59, 1, 1, 1, 1, 18), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpInterfaceQuerierExpiryTime.setStatus('current')
igmpCacheTable = MibTable((1, 3, 6, 1, 3, 59, 1, 1, 2), )
if mibBuilder.loadTexts: igmpCacheTable.setStatus('current')
igmpCacheEntry = MibTableRow((1, 3, 6, 1, 3, 59, 1, 1, 2, 1), ).setIndexNames((0, "IGMP-STD-MIB", "igmpCacheAddress"), (0, "IGMP-STD-MIB", "igmpCacheIfIndex"))
if mibBuilder.loadTexts: igmpCacheEntry.setStatus('current')
igmpCacheAddress = MibTableColumn((1, 3, 6, 1, 3, 59, 1, 1, 2, 1, 1), IpAddress())
if mibBuilder.loadTexts: igmpCacheAddress.setStatus('current')
igmpCacheIfIndex = MibTableColumn((1, 3, 6, 1, 3, 59, 1, 1, 2, 1, 2), InterfaceIndex())
if mibBuilder.loadTexts: igmpCacheIfIndex.setStatus('current')
igmpCacheSelf = MibTableColumn((1, 3, 6, 1, 3, 59, 1, 1, 2, 1, 3), TruthValue().clone('true')).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpCacheSelf.setStatus('current')
igmpCacheLastReporter = MibTableColumn((1, 3, 6, 1, 3, 59, 1, 1, 2, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpCacheLastReporter.setStatus('current')
igmpCacheUpTime = MibTableColumn((1, 3, 6, 1, 3, 59, 1, 1, 2, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpCacheUpTime.setStatus('current')
igmpCacheExpiryTime = MibTableColumn((1, 3, 6, 1, 3, 59, 1, 1, 2, 1, 6), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpCacheExpiryTime.setStatus('current')
igmpCacheStatus = MibTableColumn((1, 3, 6, 1, 3, 59, 1, 1, 2, 1, 7), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpCacheStatus.setStatus('current')
igmpCacheVersion1HostTimer = MibTableColumn((1, 3, 6, 1, 3, 59, 1, 1, 2, 1, 8), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpCacheVersion1HostTimer.setStatus('current')
igmpMIBConformance = MibIdentifier((1, 3, 6, 1, 3, 59, 2))
igmpMIBCompliances = MibIdentifier((1, 3, 6, 1, 3, 59, 2, 1))
igmpMIBGroups = MibIdentifier((1, 3, 6, 1, 3, 59, 2, 2))
igmpV1HostMIBCompliance = ModuleCompliance((1, 3, 6, 1, 3, 59, 2, 1, 1)).setObjects(("IGMP-STD-MIB", "igmpBaseMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    igmpV1HostMIBCompliance = igmpV1HostMIBCompliance.setStatus('current')
igmpV1RouterMIBCompliance = ModuleCompliance((1, 3, 6, 1, 3, 59, 2, 1, 2)).setObjects(("IGMP-STD-MIB", "igmpBaseMIBGroup"), ("IGMP-STD-MIB", "igmpRouterMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    igmpV1RouterMIBCompliance = igmpV1RouterMIBCompliance.setStatus('current')
igmpV2HostMIBCompliance = ModuleCompliance((1, 3, 6, 1, 3, 59, 2, 1, 3)).setObjects(("IGMP-STD-MIB", "igmpBaseMIBGroup"), ("IGMP-STD-MIB", "igmpV2HostMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    igmpV2HostMIBCompliance = igmpV2HostMIBCompliance.setStatus('current')
igmpV2RouterMIBCompliance = ModuleCompliance((1, 3, 6, 1, 3, 59, 2, 1, 4)).setObjects(("IGMP-STD-MIB", "igmpBaseMIBGroup"), ("IGMP-STD-MIB", "igmpRouterMIBGroup"), ("IGMP-STD-MIB", "igmpV2RouterMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    igmpV2RouterMIBCompliance = igmpV2RouterMIBCompliance.setStatus('current')
igmpBaseMIBGroup = ObjectGroup((1, 3, 6, 1, 3, 59, 2, 2, 1)).setObjects(("IGMP-STD-MIB", "igmpCacheSelf"), ("IGMP-STD-MIB", "igmpCacheStatus"), ("IGMP-STD-MIB", "igmpInterfaceStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    igmpBaseMIBGroup = igmpBaseMIBGroup.setStatus('current')
igmpRouterMIBGroup = ObjectGroup((1, 3, 6, 1, 3, 59, 2, 2, 2)).setObjects(("IGMP-STD-MIB", "igmpCacheUpTime"), ("IGMP-STD-MIB", "igmpCacheExpiryTime"), ("IGMP-STD-MIB", "igmpInterfaceJoins"), ("IGMP-STD-MIB", "igmpInterfaceGroups"), ("IGMP-STD-MIB", "igmpCacheLastReporter"), ("IGMP-STD-MIB", "igmpInterfaceQuerierUpTime"), ("IGMP-STD-MIB", "igmpInterfaceQuerierExpiryTime"), ("IGMP-STD-MIB", "igmpInterfaceQueryInterval"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    igmpRouterMIBGroup = igmpRouterMIBGroup.setStatus('current')
igmpV2HostMIBGroup = ObjectGroup((1, 3, 6, 1, 3, 59, 2, 2, 3)).setObjects(("IGMP-STD-MIB", "igmpInterfaceVersion1QuerierTimer"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    igmpV2HostMIBGroup = igmpV2HostMIBGroup.setStatus('current')
igmpHostOptMIBGroup = ObjectGroup((1, 3, 6, 1, 3, 59, 2, 2, 4)).setObjects(("IGMP-STD-MIB", "igmpCacheLastReporter"), ("IGMP-STD-MIB", "igmpInterfaceQuerier"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    igmpHostOptMIBGroup = igmpHostOptMIBGroup.setStatus('current')
igmpV2RouterMIBGroup = ObjectGroup((1, 3, 6, 1, 3, 59, 2, 2, 5)).setObjects(("IGMP-STD-MIB", "igmpInterfaceVersion"), ("IGMP-STD-MIB", "igmpInterfaceQuerier"), ("IGMP-STD-MIB", "igmpInterfaceQueryMaxResponseTime"), ("IGMP-STD-MIB", "igmpInterfaceRobustness"), ("IGMP-STD-MIB", "igmpInterfaceWrongVersionQueries"), ("IGMP-STD-MIB", "igmpInterfaceLastMembQueryIntvl"), ("IGMP-STD-MIB", "igmpCacheVersion1HostTimer"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    igmpV2RouterMIBGroup = igmpV2RouterMIBGroup.setStatus('current')
igmpV2ProxyMIBGroup = ObjectGroup((1, 3, 6, 1, 3, 59, 2, 2, 6)).setObjects(("IGMP-STD-MIB", "igmpInterfaceProxyIfIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    igmpV2ProxyMIBGroup = igmpV2ProxyMIBGroup.setStatus('current')
mibBuilder.exportSymbols("IGMP-STD-MIB", igmpMIBGroups=igmpMIBGroups, igmpInterfaceVersion1QuerierTimer=igmpInterfaceVersion1QuerierTimer, igmpInterfaceQuerierUpTime=igmpInterfaceQuerierUpTime, igmpInterfaceJoins=igmpInterfaceJoins, igmpMIBCompliances=igmpMIBCompliances, igmpBaseMIBGroup=igmpBaseMIBGroup, igmpV2ProxyMIBGroup=igmpV2ProxyMIBGroup, igmpV2HostMIBCompliance=igmpV2HostMIBCompliance, igmp=igmp, igmpV1HostMIBCompliance=igmpV1HostMIBCompliance, igmpV1RouterMIBCompliance=igmpV1RouterMIBCompliance, igmpCacheTable=igmpCacheTable, igmpV2RouterMIBCompliance=igmpV2RouterMIBCompliance, igmpInterfaceRobustness=igmpInterfaceRobustness, igmpCacheLastReporter=igmpCacheLastReporter, igmpCacheStatus=igmpCacheStatus, igmpInterfaceLastMembQueryIntvl=igmpInterfaceLastMembQueryIntvl, igmpV2RouterMIBGroup=igmpV2RouterMIBGroup, igmpCacheIfIndex=igmpCacheIfIndex, igmpCacheUpTime=igmpCacheUpTime, igmpCacheVersion1HostTimer=igmpCacheVersion1HostTimer, igmpCacheSelf=igmpCacheSelf, igmpInterfaceStatus=igmpInterfaceStatus, igmpInterfaceQuerierExpiryTime=igmpInterfaceQuerierExpiryTime, igmpInterfaceGroups=igmpInterfaceGroups, igmpStdMIB=igmpStdMIB, PYSNMP_MODULE_ID=igmpStdMIB, igmpInterfaceProxyIfIndex=igmpInterfaceProxyIfIndex, igmpMIBObjects=igmpMIBObjects, igmpInterfaceTable=igmpInterfaceTable, igmpInterfaceIfIndex=igmpInterfaceIfIndex, igmpInterfaceQuerier=igmpInterfaceQuerier, igmpRouterMIBGroup=igmpRouterMIBGroup, igmpInterfaceQueryInterval=igmpInterfaceQueryInterval, igmpInterfaceVersion=igmpInterfaceVersion, igmpV2HostMIBGroup=igmpV2HostMIBGroup, igmpMIBConformance=igmpMIBConformance, igmpInterfaceEntry=igmpInterfaceEntry, igmpInterfaceQueryMaxResponseTime=igmpInterfaceQueryMaxResponseTime, igmpInterfaceWrongVersionQueries=igmpInterfaceWrongVersionQueries, igmpCacheAddress=igmpCacheAddress, igmpHostOptMIBGroup=igmpHostOptMIBGroup, igmpCacheEntry=igmpCacheEntry, igmpCacheExpiryTime=igmpCacheExpiryTime)
