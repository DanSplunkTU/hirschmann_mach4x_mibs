#
# PySNMP MIB module MGMD-STD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/MGMD-STD-MIB
# Produced by pysmi-1.1.3 at Sun Nov 28 20:09:00 2021
# On host fv-az77-612 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
InterfaceIndexOrZero, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero", "InterfaceIndex")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, ObjectIdentity, iso, Counter64, Gauge32, mib_2, Counter32, MibIdentifier, Unsigned32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Integer32, NotificationType, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "ObjectIdentity", "iso", "Counter64", "Gauge32", "mib-2", "Counter32", "MibIdentifier", "Unsigned32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Integer32", "NotificationType", "IpAddress")
RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention")
mgmdStdMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 185))
mgmdStdMIB.setRevisions(('2009-03-30 00:00',))
if mibBuilder.loadTexts: mgmdStdMIB.setLastUpdated('200903300000Z')
if mibBuilder.loadTexts: mgmdStdMIB.setOrganization('INTERNET ENGINEERING TASK FORCE MULTICAST and ANYCAST GROUP MEMBERSHIP Working Group. www: http://www.ietf.org/html.charters/magma-charter.html EMail: magma@ietf.org')
mgmdMIBObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 185, 1))
mgmdHostInterfaceTable = MibTable((1, 3, 6, 1, 2, 1, 185, 1, 1), )
if mibBuilder.loadTexts: mgmdHostInterfaceTable.setStatus('current')
mgmdHostInterfaceEntry = MibTableRow((1, 3, 6, 1, 2, 1, 185, 1, 1, 1), ).setIndexNames((0, "MGMD-STD-MIB", "mgmdHostInterfaceIfIndex"), (0, "MGMD-STD-MIB", "mgmdHostInterfaceQuerierType"))
if mibBuilder.loadTexts: mgmdHostInterfaceEntry.setStatus('current')
mgmdHostInterfaceIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 185, 1, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: mgmdHostInterfaceIfIndex.setStatus('current')
mgmdHostInterfaceQuerierType = MibTableColumn((1, 3, 6, 1, 2, 1, 185, 1, 1, 1, 2), InetAddressType().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ipv4", 1), ("ipv6", 2))))
if mibBuilder.loadTexts: mgmdHostInterfaceQuerierType.setStatus('current')
mgmdHostInterfaceQuerier = MibTableColumn((1, 3, 6, 1, 2, 1, 185, 1, 1, 1, 3), InetAddress().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(4, 4), ValueSizeConstraint(16, 16), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgmdHostInterfaceQuerier.setStatus('current')
mgmdHostInterfaceStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 185, 1, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mgmdHostInterfaceStatus.setStatus('current')
mgmdHostInterfaceVersion = MibTableColumn((1, 3, 6, 1, 2, 1, 185, 1, 1, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 3)).clone(3)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mgmdHostInterfaceVersion.setStatus('current')
mgmdHostInterfaceVersion1QuerierTimer = MibTableColumn((1, 3, 6, 1, 2, 1, 185, 1, 1, 1, 6), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgmdHostInterfaceVersion1QuerierTimer.setStatus('current')
mgmdHostInterfaceVersion2QuerierTimer = MibTableColumn((1, 3, 6, 1, 2, 1, 185, 1, 1, 1, 7), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgmdHostInterfaceVersion2QuerierTimer.setStatus('current')
mgmdHostInterfaceVersion3Robustness = MibTableColumn((1, 3, 6, 1, 2, 1, 185, 1, 1, 1, 8), Unsigned32().clone(2)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mgmdHostInterfaceVersion3Robustness.setStatus('current')
mgmdRouterInterfaceTable = MibTable((1, 3, 6, 1, 2, 1, 185, 1, 2), )
if mibBuilder.loadTexts: mgmdRouterInterfaceTable.setStatus('current')
mgmdRouterInterfaceEntry = MibTableRow((1, 3, 6, 1, 2, 1, 185, 1, 2, 1), ).setIndexNames((0, "MGMD-STD-MIB", "mgmdRouterInterfaceIfIndex"), (0, "MGMD-STD-MIB", "mgmdRouterInterfaceQuerierType"))
if mibBuilder.loadTexts: mgmdRouterInterfaceEntry.setStatus('current')
mgmdRouterInterfaceIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 185, 1, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: mgmdRouterInterfaceIfIndex.setStatus('current')
mgmdRouterInterfaceQuerierType = MibTableColumn((1, 3, 6, 1, 2, 1, 185, 1, 2, 1, 2), InetAddressType().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ipv4", 1), ("ipv6", 2))))
if mibBuilder.loadTexts: mgmdRouterInterfaceQuerierType.setStatus('current')
mgmdRouterInterfaceQuerier = MibTableColumn((1, 3, 6, 1, 2, 1, 185, 1, 2, 1, 3), InetAddress().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(4, 4), ValueSizeConstraint(16, 16), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgmdRouterInterfaceQuerier.setStatus('current')
mgmdRouterInterfaceQueryInterval = MibTableColumn((1, 3, 6, 1, 2, 1, 185, 1, 2, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 31744)).clone(125)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: mgmdRouterInterfaceQueryInterval.setStatus('current')
mgmdRouterInterfaceStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 185, 1, 2, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mgmdRouterInterfaceStatus.setStatus('current')
mgmdRouterInterfaceVersion = MibTableColumn((1, 3, 6, 1, 2, 1, 185, 1, 2, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 3)).clone(3)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mgmdRouterInterfaceVersion.setStatus('current')
mgmdRouterInterfaceQueryMaxResponseTime = MibTableColumn((1, 3, 6, 1, 2, 1, 185, 1, 2, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 31744)).clone(100)).setUnits('tenths of seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: mgmdRouterInterfaceQueryMaxResponseTime.setStatus('current')
mgmdRouterInterfaceQuerierUpTime = MibTableColumn((1, 3, 6, 1, 2, 1, 185, 1, 2, 1, 8), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgmdRouterInterfaceQuerierUpTime.setStatus('current')
mgmdRouterInterfaceQuerierExpiryTime = MibTableColumn((1, 3, 6, 1, 2, 1, 185, 1, 2, 1, 9), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgmdRouterInterfaceQuerierExpiryTime.setStatus('current')
mgmdRouterInterfaceWrongVersionQueries = MibTableColumn((1, 3, 6, 1, 2, 1, 185, 1, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgmdRouterInterfaceWrongVersionQueries.setStatus('current')
mgmdRouterInterfaceJoins = MibTableColumn((1, 3, 6, 1, 2, 1, 185, 1, 2, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgmdRouterInterfaceJoins.setStatus('current')
mgmdRouterInterfaceProxyIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 185, 1, 2, 1, 12), InterfaceIndexOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mgmdRouterInterfaceProxyIfIndex.setStatus('current')
mgmdRouterInterfaceGroups = MibTableColumn((1, 3, 6, 1, 2, 1, 185, 1, 2, 1, 13), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgmdRouterInterfaceGroups.setStatus('current')
mgmdRouterInterfaceRobustness = MibTableColumn((1, 3, 6, 1, 2, 1, 185, 1, 2, 1, 14), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)).clone(2)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mgmdRouterInterfaceRobustness.setStatus('current')
mgmdRouterInterfaceLastMemberQueryInterval = MibTableColumn((1, 3, 6, 1, 2, 1, 185, 1, 2, 1, 15), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 31744)).clone(10)).setUnits('tenths of seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: mgmdRouterInterfaceLastMemberQueryInterval.setStatus('current')
mgmdRouterInterfaceLastMemberQueryCount = MibTableColumn((1, 3, 6, 1, 2, 1, 185, 1, 2, 1, 16), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgmdRouterInterfaceLastMemberQueryCount.setStatus('current')
mgmdRouterInterfaceStartupQueryCount = MibTableColumn((1, 3, 6, 1, 2, 1, 185, 1, 2, 1, 17), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgmdRouterInterfaceStartupQueryCount.setStatus('current')
mgmdRouterInterfaceStartupQueryInterval = MibTableColumn((1, 3, 6, 1, 2, 1, 185, 1, 2, 1, 18), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 31744))).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: mgmdRouterInterfaceStartupQueryInterval.setStatus('current')
mgmdHostCacheTable = MibTable((1, 3, 6, 1, 2, 1, 185, 1, 3), )
if mibBuilder.loadTexts: mgmdHostCacheTable.setStatus('current')
mgmdHostCacheEntry = MibTableRow((1, 3, 6, 1, 2, 1, 185, 1, 3, 1), ).setIndexNames((0, "MGMD-STD-MIB", "mgmdHostCacheAddressType"), (0, "MGMD-STD-MIB", "mgmdHostCacheAddress"), (0, "MGMD-STD-MIB", "mgmdHostCacheIfIndex"))
if mibBuilder.loadTexts: mgmdHostCacheEntry.setStatus('current')
mgmdHostCacheAddressType = MibTableColumn((1, 3, 6, 1, 2, 1, 185, 1, 3, 1, 1), InetAddressType().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ipv4", 1), ("ipv6", 2))))
if mibBuilder.loadTexts: mgmdHostCacheAddressType.setStatus('current')
mgmdHostCacheAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 185, 1, 3, 1, 2), InetAddress().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(4, 4), ValueSizeConstraint(16, 16), )))
if mibBuilder.loadTexts: mgmdHostCacheAddress.setStatus('current')
mgmdHostCacheIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 185, 1, 3, 1, 3), InterfaceIndex())
if mibBuilder.loadTexts: mgmdHostCacheIfIndex.setStatus('current')
mgmdHostCacheUpTime = MibTableColumn((1, 3, 6, 1, 2, 1, 185, 1, 3, 1, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgmdHostCacheUpTime.setStatus('current')
mgmdHostCacheLastReporter = MibTableColumn((1, 3, 6, 1, 2, 1, 185, 1, 3, 1, 5), InetAddress().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(4, 4), ValueSizeConstraint(16, 16), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgmdHostCacheLastReporter.setStatus('current')
mgmdHostCacheSourceFilterMode = MibTableColumn((1, 3, 6, 1, 2, 1, 185, 1, 3, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("include", 1), ("exclude", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgmdHostCacheSourceFilterMode.setStatus('current')
mgmdRouterCacheTable = MibTable((1, 3, 6, 1, 2, 1, 185, 1, 4), )
if mibBuilder.loadTexts: mgmdRouterCacheTable.setStatus('current')
mgmdRouterCacheEntry = MibTableRow((1, 3, 6, 1, 2, 1, 185, 1, 4, 1), ).setIndexNames((0, "MGMD-STD-MIB", "mgmdRouterCacheAddressType"), (0, "MGMD-STD-MIB", "mgmdRouterCacheAddress"), (0, "MGMD-STD-MIB", "mgmdRouterCacheIfIndex"))
if mibBuilder.loadTexts: mgmdRouterCacheEntry.setStatus('current')
mgmdRouterCacheAddressType = MibTableColumn((1, 3, 6, 1, 2, 1, 185, 1, 4, 1, 1), InetAddressType().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ipv4", 1), ("ipv6", 2))))
if mibBuilder.loadTexts: mgmdRouterCacheAddressType.setStatus('current')
mgmdRouterCacheAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 185, 1, 4, 1, 2), InetAddress().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(4, 4), ValueSizeConstraint(16, 16), )))
if mibBuilder.loadTexts: mgmdRouterCacheAddress.setStatus('current')
mgmdRouterCacheIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 185, 1, 4, 1, 3), InterfaceIndex())
if mibBuilder.loadTexts: mgmdRouterCacheIfIndex.setStatus('current')
mgmdRouterCacheLastReporter = MibTableColumn((1, 3, 6, 1, 2, 1, 185, 1, 4, 1, 4), InetAddress().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(4, 4), ValueSizeConstraint(16, 16), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgmdRouterCacheLastReporter.setStatus('current')
mgmdRouterCacheUpTime = MibTableColumn((1, 3, 6, 1, 2, 1, 185, 1, 4, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgmdRouterCacheUpTime.setStatus('current')
mgmdRouterCacheExpiryTime = MibTableColumn((1, 3, 6, 1, 2, 1, 185, 1, 4, 1, 6), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgmdRouterCacheExpiryTime.setStatus('current')
mgmdRouterCacheExcludeModeExpiryTimer = MibTableColumn((1, 3, 6, 1, 2, 1, 185, 1, 4, 1, 7), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgmdRouterCacheExcludeModeExpiryTimer.setStatus('current')
mgmdRouterCacheVersion1HostTimer = MibTableColumn((1, 3, 6, 1, 2, 1, 185, 1, 4, 1, 8), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgmdRouterCacheVersion1HostTimer.setStatus('current')
mgmdRouterCacheVersion2HostTimer = MibTableColumn((1, 3, 6, 1, 2, 1, 185, 1, 4, 1, 9), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgmdRouterCacheVersion2HostTimer.setStatus('current')
mgmdRouterCacheSourceFilterMode = MibTableColumn((1, 3, 6, 1, 2, 1, 185, 1, 4, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("include", 1), ("exclude", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgmdRouterCacheSourceFilterMode.setStatus('current')
mgmdInverseHostCacheTable = MibTable((1, 3, 6, 1, 2, 1, 185, 1, 5), )
if mibBuilder.loadTexts: mgmdInverseHostCacheTable.setStatus('current')
mgmdInverseHostCacheEntry = MibTableRow((1, 3, 6, 1, 2, 1, 185, 1, 5, 1), ).setIndexNames((0, "MGMD-STD-MIB", "mgmdInverseHostCacheIfIndex"), (0, "MGMD-STD-MIB", "mgmdInverseHostCacheAddressType"), (0, "MGMD-STD-MIB", "mgmdInverseHostCacheAddress"))
if mibBuilder.loadTexts: mgmdInverseHostCacheEntry.setStatus('current')
mgmdInverseHostCacheIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 185, 1, 5, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: mgmdInverseHostCacheIfIndex.setStatus('current')
mgmdInverseHostCacheAddressType = MibTableColumn((1, 3, 6, 1, 2, 1, 185, 1, 5, 1, 2), InetAddressType().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ipv4", 1), ("ipv6", 2))))
if mibBuilder.loadTexts: mgmdInverseHostCacheAddressType.setStatus('current')
mgmdInverseHostCacheAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 185, 1, 5, 1, 3), InetAddress().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(4, 4), ValueSizeConstraint(16, 16), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgmdInverseHostCacheAddress.setStatus('current')
mgmdInverseRouterCacheTable = MibTable((1, 3, 6, 1, 2, 1, 185, 1, 6), )
if mibBuilder.loadTexts: mgmdInverseRouterCacheTable.setStatus('current')
mgmdInverseRouterCacheEntry = MibTableRow((1, 3, 6, 1, 2, 1, 185, 1, 6, 1), ).setIndexNames((0, "MGMD-STD-MIB", "mgmdInverseRouterCacheIfIndex"), (0, "MGMD-STD-MIB", "mgmdInverseRouterCacheAddressType"), (0, "MGMD-STD-MIB", "mgmdInverseRouterCacheAddress"))
if mibBuilder.loadTexts: mgmdInverseRouterCacheEntry.setStatus('current')
mgmdInverseRouterCacheIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 185, 1, 6, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: mgmdInverseRouterCacheIfIndex.setStatus('current')
mgmdInverseRouterCacheAddressType = MibTableColumn((1, 3, 6, 1, 2, 1, 185, 1, 6, 1, 2), InetAddressType().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ipv4", 1), ("ipv6", 2))))
if mibBuilder.loadTexts: mgmdInverseRouterCacheAddressType.setStatus('current')
mgmdInverseRouterCacheAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 185, 1, 6, 1, 3), InetAddress().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(4, 4), ValueSizeConstraint(16, 16), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgmdInverseRouterCacheAddress.setStatus('current')
mgmdHostSrcListTable = MibTable((1, 3, 6, 1, 2, 1, 185, 1, 7), )
if mibBuilder.loadTexts: mgmdHostSrcListTable.setStatus('current')
mgmdHostSrcListEntry = MibTableRow((1, 3, 6, 1, 2, 1, 185, 1, 7, 1), ).setIndexNames((0, "MGMD-STD-MIB", "mgmdHostSrcListAddressType"), (0, "MGMD-STD-MIB", "mgmdHostSrcListAddress"), (0, "MGMD-STD-MIB", "mgmdHostSrcListIfIndex"), (0, "MGMD-STD-MIB", "mgmdHostSrcListHostAddress"))
if mibBuilder.loadTexts: mgmdHostSrcListEntry.setStatus('current')
mgmdHostSrcListAddressType = MibTableColumn((1, 3, 6, 1, 2, 1, 185, 1, 7, 1, 1), InetAddressType().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ipv4", 1), ("ipv6", 2))))
if mibBuilder.loadTexts: mgmdHostSrcListAddressType.setStatus('current')
mgmdHostSrcListAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 185, 1, 7, 1, 2), InetAddress().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(4, 4), ValueSizeConstraint(16, 16), )))
if mibBuilder.loadTexts: mgmdHostSrcListAddress.setStatus('current')
mgmdHostSrcListIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 185, 1, 7, 1, 3), InterfaceIndex())
if mibBuilder.loadTexts: mgmdHostSrcListIfIndex.setStatus('current')
mgmdHostSrcListHostAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 185, 1, 7, 1, 4), InetAddress().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(4, 4), ValueSizeConstraint(16, 16), )))
if mibBuilder.loadTexts: mgmdHostSrcListHostAddress.setStatus('current')
mgmdHostSrcListExpire = MibTableColumn((1, 3, 6, 1, 2, 1, 185, 1, 7, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgmdHostSrcListExpire.setStatus('current')
mgmdRouterSrcListTable = MibTable((1, 3, 6, 1, 2, 1, 185, 1, 8), )
if mibBuilder.loadTexts: mgmdRouterSrcListTable.setStatus('current')
mgmdRouterSrcListEntry = MibTableRow((1, 3, 6, 1, 2, 1, 185, 1, 8, 1), ).setIndexNames((0, "MGMD-STD-MIB", "mgmdRouterSrcListAddressType"), (0, "MGMD-STD-MIB", "mgmdRouterSrcListAddress"), (0, "MGMD-STD-MIB", "mgmdRouterSrcListIfIndex"), (0, "MGMD-STD-MIB", "mgmdRouterSrcListHostAddress"))
if mibBuilder.loadTexts: mgmdRouterSrcListEntry.setStatus('current')
mgmdRouterSrcListAddressType = MibTableColumn((1, 3, 6, 1, 2, 1, 185, 1, 8, 1, 1), InetAddressType().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ipv4", 1), ("ipv6", 2))))
if mibBuilder.loadTexts: mgmdRouterSrcListAddressType.setStatus('current')
mgmdRouterSrcListAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 185, 1, 8, 1, 2), InetAddress().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(4, 4), ValueSizeConstraint(16, 16), )))
if mibBuilder.loadTexts: mgmdRouterSrcListAddress.setStatus('current')
mgmdRouterSrcListIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 185, 1, 8, 1, 3), InterfaceIndex())
if mibBuilder.loadTexts: mgmdRouterSrcListIfIndex.setStatus('current')
mgmdRouterSrcListHostAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 185, 1, 8, 1, 4), InetAddress().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(4, 4), ValueSizeConstraint(16, 16), )))
if mibBuilder.loadTexts: mgmdRouterSrcListHostAddress.setStatus('current')
mgmdRouterSrcListExpire = MibTableColumn((1, 3, 6, 1, 2, 1, 185, 1, 8, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgmdRouterSrcListExpire.setStatus('current')
mgmdMIBConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 185, 2))
mgmdMIBCompliance = MibIdentifier((1, 3, 6, 1, 2, 1, 185, 2, 1))
mgmdMIBGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 185, 2, 2))
mgmdIgmpV1HostReadMIBCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 185, 2, 1, 1)).setObjects(("MGMD-STD-MIB", "mgmdHostBaseMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mgmdIgmpV1HostReadMIBCompliance = mgmdIgmpV1HostReadMIBCompliance.setStatus('current')
mgmdIgmpV1RouterReadMIBCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 185, 2, 1, 2)).setObjects(("MGMD-STD-MIB", "mgmdRouterBaseMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mgmdIgmpV1RouterReadMIBCompliance = mgmdIgmpV1RouterReadMIBCompliance.setStatus('current')
mgmdIgmpV1RouterWriteMIBCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 185, 2, 1, 3)).setObjects(("MGMD-STD-MIB", "mgmdRouterBaseMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mgmdIgmpV1RouterWriteMIBCompliance = mgmdIgmpV1RouterWriteMIBCompliance.setStatus('current')
mgmdIgmpV2MldV1HostReadMIBCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 185, 2, 1, 4)).setObjects(("MGMD-STD-MIB", "mgmdHostBaseMIBGroup"), ("MGMD-STD-MIB", "mgmdV2HostMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mgmdIgmpV2MldV1HostReadMIBCompliance = mgmdIgmpV2MldV1HostReadMIBCompliance.setStatus('current')
mgmdIgmpV2MldV1HostWriteMIBCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 185, 2, 1, 5)).setObjects(("MGMD-STD-MIB", "mgmdHostBaseMIBGroup"), ("MGMD-STD-MIB", "mgmdV2HostMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mgmdIgmpV2MldV1HostWriteMIBCompliance = mgmdIgmpV2MldV1HostWriteMIBCompliance.setStatus('current')
mgmdIgmpV2MldV1RouterReadMIBCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 185, 2, 1, 6)).setObjects(("MGMD-STD-MIB", "mgmdRouterBaseMIBGroup"), ("MGMD-STD-MIB", "mgmdV2RouterBaseMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mgmdIgmpV2MldV1RouterReadMIBCompliance = mgmdIgmpV2MldV1RouterReadMIBCompliance.setStatus('current')
mgmdIgmpV2V3MldV1V2RouterWriteMIBCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 185, 2, 1, 7)).setObjects(("MGMD-STD-MIB", "mgmdRouterBaseMIBGroup"), ("MGMD-STD-MIB", "mgmdV2RouterBaseMIBGroup"), ("MGMD-STD-MIB", "mgmdV2ProxyMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mgmdIgmpV2V3MldV1V2RouterWriteMIBCompliance = mgmdIgmpV2V3MldV1V2RouterWriteMIBCompliance.setStatus('current')
mgmdIgmpV3MldV2HostReadMIBCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 185, 2, 1, 8)).setObjects(("MGMD-STD-MIB", "mgmdHostBaseMIBGroup"), ("MGMD-STD-MIB", "mgmdV2HostMIBGroup"), ("MGMD-STD-MIB", "mgmdV3HostMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mgmdIgmpV3MldV2HostReadMIBCompliance = mgmdIgmpV3MldV2HostReadMIBCompliance.setStatus('current')
mgmdIgmpV3MldV2HostWriteMIBCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 185, 2, 1, 9)).setObjects(("MGMD-STD-MIB", "mgmdHostBaseMIBGroup"), ("MGMD-STD-MIB", "mgmdV2HostMIBGroup"), ("MGMD-STD-MIB", "mgmdV3HostMIBGroup"), ("MGMD-STD-MIB", "mgmdHostExtendedMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mgmdIgmpV3MldV2HostWriteMIBCompliance = mgmdIgmpV3MldV2HostWriteMIBCompliance.setStatus('current')
mgmdIgmpV3MldV2RouterReadMIBCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 185, 2, 1, 10)).setObjects(("MGMD-STD-MIB", "mgmdRouterBaseMIBGroup"), ("MGMD-STD-MIB", "mgmdV2RouterBaseMIBGroup"), ("MGMD-STD-MIB", "mgmdV3RouterMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mgmdIgmpV3MldV2RouterReadMIBCompliance = mgmdIgmpV3MldV2RouterReadMIBCompliance.setStatus('current')
mgmdHostBaseMIBGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 185, 2, 2, 1)).setObjects(("MGMD-STD-MIB", "mgmdHostInterfaceStatus"), ("MGMD-STD-MIB", "mgmdHostInterfaceVersion"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mgmdHostBaseMIBGroup = mgmdHostBaseMIBGroup.setStatus('current')
mgmdRouterBaseMIBGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 185, 2, 2, 2)).setObjects(("MGMD-STD-MIB", "mgmdRouterInterfaceStatus"), ("MGMD-STD-MIB", "mgmdRouterInterfaceQueryInterval"), ("MGMD-STD-MIB", "mgmdRouterCacheUpTime"), ("MGMD-STD-MIB", "mgmdRouterCacheExpiryTime"), ("MGMD-STD-MIB", "mgmdRouterInterfaceVersion"), ("MGMD-STD-MIB", "mgmdRouterInterfaceJoins"), ("MGMD-STD-MIB", "mgmdRouterInterfaceGroups"), ("MGMD-STD-MIB", "mgmdRouterCacheLastReporter"), ("MGMD-STD-MIB", "mgmdRouterInterfaceQuerierUpTime"), ("MGMD-STD-MIB", "mgmdRouterInterfaceQuerierExpiryTime"), ("MGMD-STD-MIB", "mgmdRouterInterfaceQuerier"), ("MGMD-STD-MIB", "mgmdInverseRouterCacheAddress"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mgmdRouterBaseMIBGroup = mgmdRouterBaseMIBGroup.setStatus('current')
mgmdV2HostMIBGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 185, 2, 2, 3)).setObjects(("MGMD-STD-MIB", "mgmdHostInterfaceVersion1QuerierTimer"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mgmdV2HostMIBGroup = mgmdV2HostMIBGroup.setStatus('current')
mgmdHostExtendedMIBGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 185, 2, 2, 4)).setObjects(("MGMD-STD-MIB", "mgmdHostCacheLastReporter"), ("MGMD-STD-MIB", "mgmdHostCacheUpTime"), ("MGMD-STD-MIB", "mgmdHostInterfaceQuerier"), ("MGMD-STD-MIB", "mgmdInverseHostCacheAddress"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mgmdHostExtendedMIBGroup = mgmdHostExtendedMIBGroup.setStatus('current')
mgmdV2RouterBaseMIBGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 185, 2, 2, 5)).setObjects(("MGMD-STD-MIB", "mgmdRouterInterfaceWrongVersionQueries"), ("MGMD-STD-MIB", "mgmdRouterInterfaceLastMemberQueryCount"), ("MGMD-STD-MIB", "mgmdRouterInterfaceStartupQueryCount"), ("MGMD-STD-MIB", "mgmdRouterInterfaceStartupQueryInterval"), ("MGMD-STD-MIB", "mgmdRouterCacheVersion1HostTimer"), ("MGMD-STD-MIB", "mgmdRouterInterfaceQueryMaxResponseTime"), ("MGMD-STD-MIB", "mgmdRouterInterfaceRobustness"), ("MGMD-STD-MIB", "mgmdRouterInterfaceLastMemberQueryInterval"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mgmdV2RouterBaseMIBGroup = mgmdV2RouterBaseMIBGroup.setStatus('current')
mgmdV2ProxyMIBGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 185, 2, 2, 6)).setObjects(("MGMD-STD-MIB", "mgmdRouterInterfaceProxyIfIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mgmdV2ProxyMIBGroup = mgmdV2ProxyMIBGroup.setStatus('current')
mgmdV3HostMIBGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 185, 2, 2, 7)).setObjects(("MGMD-STD-MIB", "mgmdHostInterfaceVersion2QuerierTimer"), ("MGMD-STD-MIB", "mgmdHostCacheSourceFilterMode"), ("MGMD-STD-MIB", "mgmdHostInterfaceVersion3Robustness"), ("MGMD-STD-MIB", "mgmdHostSrcListExpire"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mgmdV3HostMIBGroup = mgmdV3HostMIBGroup.setStatus('current')
mgmdV3RouterMIBGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 185, 2, 2, 8)).setObjects(("MGMD-STD-MIB", "mgmdRouterCacheSourceFilterMode"), ("MGMD-STD-MIB", "mgmdRouterCacheVersion2HostTimer"), ("MGMD-STD-MIB", "mgmdRouterCacheExcludeModeExpiryTimer"), ("MGMD-STD-MIB", "mgmdRouterSrcListExpire"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mgmdV3RouterMIBGroup = mgmdV3RouterMIBGroup.setStatus('current')
mibBuilder.exportSymbols("MGMD-STD-MIB", mgmdHostSrcListAddressType=mgmdHostSrcListAddressType, mgmdIgmpV1RouterWriteMIBCompliance=mgmdIgmpV1RouterWriteMIBCompliance, mgmdHostCacheTable=mgmdHostCacheTable, mgmdRouterCacheIfIndex=mgmdRouterCacheIfIndex, mgmdIgmpV2MldV1HostWriteMIBCompliance=mgmdIgmpV2MldV1HostWriteMIBCompliance, mgmdRouterCacheAddress=mgmdRouterCacheAddress, mgmdRouterSrcListHostAddress=mgmdRouterSrcListHostAddress, mgmdHostInterfaceVersion3Robustness=mgmdHostInterfaceVersion3Robustness, mgmdRouterInterfaceQueryInterval=mgmdRouterInterfaceQueryInterval, mgmdRouterCacheExpiryTime=mgmdRouterCacheExpiryTime, mgmdIgmpV1RouterReadMIBCompliance=mgmdIgmpV1RouterReadMIBCompliance, mgmdRouterSrcListTable=mgmdRouterSrcListTable, mgmdRouterInterfaceQuerierType=mgmdRouterInterfaceQuerierType, mgmdHostCacheIfIndex=mgmdHostCacheIfIndex, mgmdHostCacheSourceFilterMode=mgmdHostCacheSourceFilterMode, mgmdInverseRouterCacheIfIndex=mgmdInverseRouterCacheIfIndex, mgmdHostSrcListTable=mgmdHostSrcListTable, mgmdHostInterfaceVersion2QuerierTimer=mgmdHostInterfaceVersion2QuerierTimer, mgmdRouterInterfaceTable=mgmdRouterInterfaceTable, mgmdRouterInterfaceIfIndex=mgmdRouterInterfaceIfIndex, mgmdRouterInterfaceGroups=mgmdRouterInterfaceGroups, mgmdIgmpV1HostReadMIBCompliance=mgmdIgmpV1HostReadMIBCompliance, mgmdRouterCacheEntry=mgmdRouterCacheEntry, mgmdHostExtendedMIBGroup=mgmdHostExtendedMIBGroup, mgmdHostInterfaceQuerier=mgmdHostInterfaceQuerier, mgmdIgmpV2V3MldV1V2RouterWriteMIBCompliance=mgmdIgmpV2V3MldV1V2RouterWriteMIBCompliance, mgmdHostSrcListHostAddress=mgmdHostSrcListHostAddress, mgmdRouterSrcListAddress=mgmdRouterSrcListAddress, mgmdRouterInterfaceStatus=mgmdRouterInterfaceStatus, mgmdHostCacheAddress=mgmdHostCacheAddress, mgmdInverseHostCacheTable=mgmdInverseHostCacheTable, mgmdRouterSrcListAddressType=mgmdRouterSrcListAddressType, mgmdRouterInterfaceStartupQueryCount=mgmdRouterInterfaceStartupQueryCount, mgmdInverseRouterCacheTable=mgmdInverseRouterCacheTable, mgmdRouterInterfaceQuerierUpTime=mgmdRouterInterfaceQuerierUpTime, mgmdInverseHostCacheIfIndex=mgmdInverseHostCacheIfIndex, mgmdMIBObjects=mgmdMIBObjects, mgmdInverseHostCacheAddress=mgmdInverseHostCacheAddress, mgmdRouterSrcListEntry=mgmdRouterSrcListEntry, mgmdRouterSrcListIfIndex=mgmdRouterSrcListIfIndex, mgmdHostInterfaceTable=mgmdHostInterfaceTable, mgmdRouterInterfaceVersion=mgmdRouterInterfaceVersion, mgmdMIBConformance=mgmdMIBConformance, mgmdInverseHostCacheEntry=mgmdInverseHostCacheEntry, mgmdHostInterfaceVersion=mgmdHostInterfaceVersion, mgmdRouterCacheSourceFilterMode=mgmdRouterCacheSourceFilterMode, mgmdIgmpV3MldV2HostReadMIBCompliance=mgmdIgmpV3MldV2HostReadMIBCompliance, mgmdHostSrcListAddress=mgmdHostSrcListAddress, mgmdRouterCacheVersion2HostTimer=mgmdRouterCacheVersion2HostTimer, mgmdRouterCacheTable=mgmdRouterCacheTable, mgmdRouterInterfaceQueryMaxResponseTime=mgmdRouterInterfaceQueryMaxResponseTime, mgmdRouterCacheLastReporter=mgmdRouterCacheLastReporter, mgmdV2RouterBaseMIBGroup=mgmdV2RouterBaseMIBGroup, mgmdRouterInterfaceWrongVersionQueries=mgmdRouterInterfaceWrongVersionQueries, mgmdRouterInterfaceProxyIfIndex=mgmdRouterInterfaceProxyIfIndex, mgmdRouterCacheVersion1HostTimer=mgmdRouterCacheVersion1HostTimer, mgmdHostBaseMIBGroup=mgmdHostBaseMIBGroup, mgmdRouterCacheExcludeModeExpiryTimer=mgmdRouterCacheExcludeModeExpiryTimer, mgmdRouterInterfaceJoins=mgmdRouterInterfaceJoins, mgmdV2HostMIBGroup=mgmdV2HostMIBGroup, mgmdHostInterfaceVersion1QuerierTimer=mgmdHostInterfaceVersion1QuerierTimer, mgmdHostCacheLastReporter=mgmdHostCacheLastReporter, mgmdInverseRouterCacheAddress=mgmdInverseRouterCacheAddress, mgmdV3HostMIBGroup=mgmdV3HostMIBGroup, PYSNMP_MODULE_ID=mgmdStdMIB, mgmdRouterBaseMIBGroup=mgmdRouterBaseMIBGroup, mgmdStdMIB=mgmdStdMIB, mgmdHostCacheAddressType=mgmdHostCacheAddressType, mgmdIgmpV2MldV1HostReadMIBCompliance=mgmdIgmpV2MldV1HostReadMIBCompliance, mgmdRouterCacheAddressType=mgmdRouterCacheAddressType, mgmdHostInterfaceEntry=mgmdHostInterfaceEntry, mgmdRouterSrcListExpire=mgmdRouterSrcListExpire, mgmdIgmpV3MldV2HostWriteMIBCompliance=mgmdIgmpV3MldV2HostWriteMIBCompliance, mgmdRouterInterfaceLastMemberQueryCount=mgmdRouterInterfaceLastMemberQueryCount, mgmdRouterInterfaceStartupQueryInterval=mgmdRouterInterfaceStartupQueryInterval, mgmdV3RouterMIBGroup=mgmdV3RouterMIBGroup, mgmdRouterCacheUpTime=mgmdRouterCacheUpTime, mgmdRouterInterfaceLastMemberQueryInterval=mgmdRouterInterfaceLastMemberQueryInterval, mgmdInverseRouterCacheEntry=mgmdInverseRouterCacheEntry, mgmdHostSrcListIfIndex=mgmdHostSrcListIfIndex, mgmdInverseRouterCacheAddressType=mgmdInverseRouterCacheAddressType, mgmdRouterInterfaceRobustness=mgmdRouterInterfaceRobustness, mgmdIgmpV2MldV1RouterReadMIBCompliance=mgmdIgmpV2MldV1RouterReadMIBCompliance, mgmdHostSrcListEntry=mgmdHostSrcListEntry, mgmdMIBGroups=mgmdMIBGroups, mgmdHostInterfaceQuerierType=mgmdHostInterfaceQuerierType, mgmdHostSrcListExpire=mgmdHostSrcListExpire, mgmdRouterInterfaceQuerierExpiryTime=mgmdRouterInterfaceQuerierExpiryTime, mgmdRouterInterfaceQuerier=mgmdRouterInterfaceQuerier, mgmdHostCacheEntry=mgmdHostCacheEntry, mgmdHostInterfaceStatus=mgmdHostInterfaceStatus, mgmdIgmpV3MldV2RouterReadMIBCompliance=mgmdIgmpV3MldV2RouterReadMIBCompliance, mgmdHostInterfaceIfIndex=mgmdHostInterfaceIfIndex, mgmdMIBCompliance=mgmdMIBCompliance, mgmdV2ProxyMIBGroup=mgmdV2ProxyMIBGroup, mgmdHostCacheUpTime=mgmdHostCacheUpTime, mgmdRouterInterfaceEntry=mgmdRouterInterfaceEntry, mgmdInverseHostCacheAddressType=mgmdInverseHostCacheAddressType)
