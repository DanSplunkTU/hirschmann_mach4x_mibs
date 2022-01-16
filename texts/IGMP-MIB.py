#
# PySNMP MIB module IGMP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/output/asn1/IGMP-MIB
# Produced by pysmi-1.1.8 at Sun Jan 16 00:41:52 2022
# On host fv-az42-839 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter64, NotificationType, Counter32, Gauge32, ObjectIdentity, Unsigned32, IpAddress, Integer32, TimeTicks, MibIdentifier, ModuleIdentity, experimental = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter64", "NotificationType", "Counter32", "Gauge32", "ObjectIdentity", "Unsigned32", "IpAddress", "Integer32", "TimeTicks", "MibIdentifier", "ModuleIdentity", "experimental")
RowStatus, TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TruthValue", "DisplayString", "TextualConvention")
igmpMIB = ModuleIdentity((1, 3, 6, 1, 3, 59))
igmpMIB.setRevisions(('1995-08-15 00:00', '1997-01-06 00:00', '1997-12-18 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: igmpMIB.setRevisionsDescriptions(('Added more contact information.', 'Update per draft-ietf-idmr-igmp-mib-04.txt.', 'Update per draft-ietf-idmr-igmp-mib-05.txt.',))
if mibBuilder.loadTexts: igmpMIB.setLastUpdated('9712180000Z')
if mibBuilder.loadTexts: igmpMIB.setOrganization('IETF IDMR Working Group.')
if mibBuilder.loadTexts: igmpMIB.setContactInfo(' Keith McCloghrie\n\t\t  Cisco Systems, Inc.\n\t\t  170 West Tasman Drive\n\t\t  San Jose, CA  9513401706\n\t\t  US\n\n\t\t  Phone: +1 408 526 5260\n\t\t  EMail: kzm@cisco.com')
if mibBuilder.loadTexts: igmpMIB.setDescription('The MIB module for IGMP Management.')
igmpMIBObjects = MibIdentifier((1, 3, 6, 1, 3, 59, 1))
igmp = MibIdentifier((1, 3, 6, 1, 3, 59, 1, 1))
igmpInterfaceTable = MibTable((1, 3, 6, 1, 3, 59, 1, 1, 1), )
if mibBuilder.loadTexts: igmpInterfaceTable.setStatus('current')
if mibBuilder.loadTexts: igmpInterfaceTable.setDescription('The (conceptual) table listing the interfaces on\n                      which IGMP is enabled.')
igmpInterfaceEntry = MibTableRow((1, 3, 6, 1, 3, 59, 1, 1, 1, 1), ).setIndexNames((0, "IGMP-MIB", "igmpInterfaceIfIndex"))
if mibBuilder.loadTexts: igmpInterfaceEntry.setStatus('current')
if mibBuilder.loadTexts: igmpInterfaceEntry.setDescription('An entry (conceptual row) representing an\n                      interface on which IGMP is enabled.')
igmpInterfaceIfIndex = MibTableColumn((1, 3, 6, 1, 3, 59, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: igmpInterfaceIfIndex.setStatus('current')
if mibBuilder.loadTexts: igmpInterfaceIfIndex.setDescription('The interface for which IGMP is enabled.')
igmpInterfaceQueryInterval = MibTableColumn((1, 3, 6, 1, 3, 59, 1, 1, 1, 1, 2), Integer32().clone(60)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: igmpInterfaceQueryInterval.setStatus('current')
if mibBuilder.loadTexts: igmpInterfaceQueryInterval.setDescription('The frequency at which IGMP Host-Query packets\n                      are transmitted on this interface.')
igmpInterfaceStatus = MibTableColumn((1, 3, 6, 1, 3, 59, 1, 1, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: igmpInterfaceStatus.setStatus('current')
if mibBuilder.loadTexts: igmpInterfaceStatus.setDescription('The activation of a row enables IGMP on the\n                      interface.  The destruction of a row disables IGMP\n                      on the interface.')
igmpInterfaceVersion = MibTableColumn((1, 3, 6, 1, 3, 59, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("version1", 1), ("version2", 2))).clone('version2')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: igmpInterfaceVersion.setStatus('current')
if mibBuilder.loadTexts: igmpInterfaceVersion.setDescription('The version of IGMP which is running on this interface.\n                      This object can be used to configure a router capable of\n\t\t      running either value.  For IGMP to function correctly, all\n\t\t      routers on a LAN must be configured to run the same version\n\t\t      of IGMP on that LAN.')
igmpInterfaceQuerier = MibTableColumn((1, 3, 6, 1, 3, 59, 1, 1, 1, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpInterfaceQuerier.setStatus('current')
if mibBuilder.loadTexts: igmpInterfaceQuerier.setDescription('The address of the IGMP Querier on the IP subnet to which\n                      this interface is attached.')
igmpInterfaceQueryMaxResponseTime = MibTableColumn((1, 3, 6, 1, 3, 59, 1, 1, 1, 1, 6), Integer32().clone(10)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: igmpInterfaceQueryMaxResponseTime.setStatus('current')
if mibBuilder.loadTexts: igmpInterfaceQueryMaxResponseTime.setDescription('The maximum query response time advertised in IGMPv2\n                      queries on this interface.')
igmpInterfaceQuerierPresentTimeout = MibTableColumn((1, 3, 6, 1, 3, 59, 1, 1, 1, 1, 7), Integer32().clone(255)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: igmpInterfaceQuerierPresentTimeout.setStatus('deprecated')
if mibBuilder.loadTexts: igmpInterfaceQuerierPresentTimeout.setDescription('A timeout interval.  If no IGMPv2 queries are heard on this\n\t\t      interface within this timeout interval, the local router\n\t\t      will take over the Querier on the IP subnet to which this\n\t\t      interface is attached.  This object is now deprecated,\n\t\t      since its value can be derived from \n\t\t      igmpInterfaceRobustness.')
igmpInterfaceLeaveEnabled = MibTableColumn((1, 3, 6, 1, 3, 59, 1, 1, 1, 1, 8), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: igmpInterfaceLeaveEnabled.setStatus('deprecated')
if mibBuilder.loadTexts: igmpInterfaceLeaveEnabled.setDescription('An indication of whether the processing of IGMPv2 Leave\n\t\t      messages is enabled on this interface.  This object is\n\t\t      now deprecated since it must be true when\n\t\t      igmpInterfaceVersion is version2, and must be false when\n\t\t      it is version1 to comply with the IGMP specfication.')
igmpInterfaceVersion1QuerierTimer = MibTableColumn((1, 3, 6, 1, 3, 59, 1, 1, 1, 1, 9), Integer32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpInterfaceVersion1QuerierTimer.setStatus('current')
if mibBuilder.loadTexts: igmpInterfaceVersion1QuerierTimer.setDescription('The time remaining until the host assumes that there are no\n\t\t      IGMPv1 routers present on the interface.  While this is\n\t\t      non-zero, the host will reply to all queries with version 1\n\t\t      membership reports.')
igmpInterfaceWrongVersionQueries = MibTableColumn((1, 3, 6, 1, 3, 59, 1, 1, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpInterfaceWrongVersionQueries.setStatus('current')
if mibBuilder.loadTexts: igmpInterfaceWrongVersionQueries.setDescription('The number of queries received whose IGMP version does not\n\t\t      match igmpInterfaceVersion.  IGMP requires that all routers\n\t\t      on a LAN be configured to run the same version of IGMP.\n\t\t      Thus, if any queries are received with the wrong version,\n\t\t      this indicates a configuration error.')
igmpInterfaceJoins = MibTableColumn((1, 3, 6, 1, 3, 59, 1, 1, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpInterfaceJoins.setStatus('current')
if mibBuilder.loadTexts: igmpInterfaceJoins.setDescription('The number of times a group membership has been added on\n\t\t      this interface; that is, the number of times an entry for\n\t\t      this interface has been added to the Cache Table.  This\n\t\t      object gives an indication of the amount of IGMP activity\n\t\t      over time.')
igmpInterfaceLeaves = MibTableColumn((1, 3, 6, 1, 3, 59, 1, 1, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpInterfaceLeaves.setStatus('deprecated')
if mibBuilder.loadTexts: igmpInterfaceLeaves.setDescription('The number of times a group membership has been removed\n\t\t      from this interface; that is, the number of times an entry\n\t\t      for this interface has been deleted from the Cache Table.\n\t\t      This object is deprecated since its value cannot be\n\t\t      usefully compared with igmpInterfaceJoins to get the\n\t\t      number of groups joined.  Instead, igmpInterfaceGroups\n\t\t      gives the number of groups joined, which may be compared\n\t\t      with igmpInterfaceJoins to derive the number of leaves.')
igmpInterfaceGroups = MibTableColumn((1, 3, 6, 1, 3, 59, 1, 1, 1, 1, 13), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpInterfaceGroups.setStatus('current')
if mibBuilder.loadTexts: igmpInterfaceGroups.setDescription('The current number of entries for this interface in\n\t\t      the Cache Table.')
igmpInterfaceRobustness = MibTableColumn((1, 3, 6, 1, 3, 59, 1, 1, 1, 1, 14), Integer32().clone(2)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: igmpInterfaceRobustness.setStatus('current')
if mibBuilder.loadTexts: igmpInterfaceRobustness.setDescription('The Robustness Variable allows tuning for the expected\n\t\t      packet loss on a subnet.  If a subnet is expected to be\n\t\t      lossy, the Robustness Variable may be increased.  IGMP\n\t\t      is robust to (Robustness Variable-1) packet losses.')
igmpCacheTable = MibTable((1, 3, 6, 1, 3, 59, 1, 1, 2), )
if mibBuilder.loadTexts: igmpCacheTable.setStatus('current')
if mibBuilder.loadTexts: igmpCacheTable.setDescription('The (conceptual) table listing the IP multicast\n                      groups for which there are members on a particular\n                      interface.')
igmpCacheEntry = MibTableRow((1, 3, 6, 1, 3, 59, 1, 1, 2, 1), ).setIndexNames((0, "IGMP-MIB", "igmpCacheAddress"), (0, "IGMP-MIB", "igmpCacheIfIndex"))
if mibBuilder.loadTexts: igmpCacheEntry.setStatus('current')
if mibBuilder.loadTexts: igmpCacheEntry.setDescription('An entry (conceptual row) in the igmpCacheTable.')
igmpCacheAddress = MibTableColumn((1, 3, 6, 1, 3, 59, 1, 1, 2, 1, 1), IpAddress())
if mibBuilder.loadTexts: igmpCacheAddress.setStatus('current')
if mibBuilder.loadTexts: igmpCacheAddress.setDescription('The IP multicast group address for which this\n                      entry contains information.')
igmpCacheIfIndex = MibTableColumn((1, 3, 6, 1, 3, 59, 1, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: igmpCacheIfIndex.setStatus('current')
if mibBuilder.loadTexts: igmpCacheIfIndex.setDescription('The interface for which this entry contains\n                      information for an IP multicast group address.')
igmpCacheSelf = MibTableColumn((1, 3, 6, 1, 3, 59, 1, 1, 2, 1, 3), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: igmpCacheSelf.setStatus('current')
if mibBuilder.loadTexts: igmpCacheSelf.setDescription('An indication of whether the local system is a\n                      member of this group address on this interface.')
igmpCacheLastReporter = MibTableColumn((1, 3, 6, 1, 3, 59, 1, 1, 2, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpCacheLastReporter.setStatus('current')
if mibBuilder.loadTexts: igmpCacheLastReporter.setDescription('The IP address of the source of the last\n                      membership report received for this IP Multicast\n                      group address on this interface.  If no membership\n                      report has been received, this object has the\n                      value 0.0.0.0.')
igmpCacheUpTime = MibTableColumn((1, 3, 6, 1, 3, 59, 1, 1, 2, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpCacheUpTime.setStatus('current')
if mibBuilder.loadTexts: igmpCacheUpTime.setDescription('The time since the system joined this group\n                      address, or zero if the system is not currently a\n                      member.')
igmpCacheExpiryTime = MibTableColumn((1, 3, 6, 1, 3, 59, 1, 1, 2, 1, 6), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpCacheExpiryTime.setStatus('current')
if mibBuilder.loadTexts: igmpCacheExpiryTime.setDescription('The minimum amount of time remaining before this\n                      entry will be aged out.')
igmpCacheStatus = MibTableColumn((1, 3, 6, 1, 3, 59, 1, 1, 2, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: igmpCacheStatus.setStatus('current')
if mibBuilder.loadTexts: igmpCacheStatus.setDescription('The status of this entry.')
igmpCacheVersion1HostTimer = MibTableColumn((1, 3, 6, 1, 3, 59, 1, 1, 2, 1, 8), Integer32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpCacheVersion1HostTimer.setStatus('current')
if mibBuilder.loadTexts: igmpCacheVersion1HostTimer.setDescription('The time remaining until the local router will assume that\n\t\t      there are no longer any IGMP version 1 members on the IP\n\t\t      subnet attached to this interface.  Upon hearing any IGMPv1\n\t\t      Membership Report, this value is reset to the group\n\t\t      membership timer.  While this time remaining is non-zero,\n\t\t      the local router ignores any IGMPv2 Leave messages for this\n\t\t      group that it receives on this interface.')
igmpMIBConformance = MibIdentifier((1, 3, 6, 1, 3, 59, 2))
igmpMIBCompliances = MibIdentifier((1, 3, 6, 1, 3, 59, 2, 1))
igmpMIBGroups = MibIdentifier((1, 3, 6, 1, 3, 59, 2, 2))
igmpV1HostMIBCompliance = ModuleCompliance((1, 3, 6, 1, 3, 59, 2, 1, 1)).setObjects(("IGMP-MIB", "igmpBaseMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    igmpV1HostMIBCompliance = igmpV1HostMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: igmpV1HostMIBCompliance.setDescription('The compliance statement for hosts running IGMPv1 and\n                      implementing the IGMP MIB.')
igmpV1RouterMIBCompliance = ModuleCompliance((1, 3, 6, 1, 3, 59, 2, 1, 2)).setObjects(("IGMP-MIB", "igmpBaseMIBGroup"), ("IGMP-MIB", "igmpRouterMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    igmpV1RouterMIBCompliance = igmpV1RouterMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: igmpV1RouterMIBCompliance.setDescription('The compliance statement for routers running IGMPv1 and\n\t\t      implementing the IGMP MIB.')
igmpV2HostMIBCompliance = ModuleCompliance((1, 3, 6, 1, 3, 59, 2, 1, 3)).setObjects(("IGMP-MIB", "igmpBaseMIBGroup"), ("IGMP-MIB", "igmpV2HostMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    igmpV2HostMIBCompliance = igmpV2HostMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: igmpV2HostMIBCompliance.setDescription('The compliance statement for hosts running IGMPv2 and\n\t\t      implementing the IGMP MIB.')
igmpV2RouterMIBCompliance = ModuleCompliance((1, 3, 6, 1, 3, 59, 2, 1, 4)).setObjects(("IGMP-MIB", "igmpBaseMIBGroup"), ("IGMP-MIB", "igmpRouterMIBGroup"), ("IGMP-MIB", "igmpV2RouterMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    igmpV2RouterMIBCompliance = igmpV2RouterMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: igmpV2RouterMIBCompliance.setDescription('The compliance statement for routers running IGMPv2 and\n\t\t      implementing the IGMP MIB.')
igmpBaseMIBGroup = ObjectGroup((1, 3, 6, 1, 3, 59, 2, 2, 1)).setObjects(("IGMP-MIB", "igmpCacheSelf"), ("IGMP-MIB", "igmpCacheLastReporter"), ("IGMP-MIB", "igmpCacheStatus"), ("IGMP-MIB", "igmpInterfaceStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    igmpBaseMIBGroup = igmpBaseMIBGroup.setStatus('current')
if mibBuilder.loadTexts: igmpBaseMIBGroup.setDescription('The basic collection of objects providing\n                      management of IGMP version 1 or 2.')
igmpRouterMIBGroup = ObjectGroup((1, 3, 6, 1, 3, 59, 2, 2, 2)).setObjects(("IGMP-MIB", "igmpCacheUpTime"), ("IGMP-MIB", "igmpCacheExpiryTime"), ("IGMP-MIB", "igmpInterfaceQueryInterval"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    igmpRouterMIBGroup = igmpRouterMIBGroup.setStatus('current')
if mibBuilder.loadTexts: igmpRouterMIBGroup.setDescription('A collection of additional objects for management\n                      of IGMP version 1 or 2 in routers.')
igmpV2HostMIBGroup = ObjectGroup((1, 3, 6, 1, 3, 59, 2, 2, 3)).setObjects(("IGMP-MIB", "igmpInterfaceQuerier"), ("IGMP-MIB", "igmpInterfaceVersion1QuerierTimer"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    igmpV2HostMIBGroup = igmpV2HostMIBGroup.setStatus('current')
if mibBuilder.loadTexts: igmpV2HostMIBGroup.setDescription('A collection of additional objects for management of\n\t\t      IGMP version 2 in hosts.')
igmpRouterVersion2MIBGroup = ObjectGroup((1, 3, 6, 1, 3, 59, 2, 2, 4)).setObjects(("IGMP-MIB", "igmpInterfaceVersion"), ("IGMP-MIB", "igmpInterfaceQueryMaxResponseTime"), ("IGMP-MIB", "igmpInterfaceQuerierPresentTimeout"), ("IGMP-MIB", "igmpInterfaceLeaveEnabled"), ("IGMP-MIB", "igmpInterfaceWrongVersionQueries"), ("IGMP-MIB", "igmpInterfaceJoins"), ("IGMP-MIB", "igmpInterfaceLeaves"), ("IGMP-MIB", "igmpCacheVersion1HostTimer"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    igmpRouterVersion2MIBGroup = igmpRouterVersion2MIBGroup.setStatus('deprecated')
if mibBuilder.loadTexts: igmpRouterVersion2MIBGroup.setDescription('A collection of additional objects for management\n\t\t      of IGMP version 2 in routers.  This group has been\n\t\t      obsoleted by igmpV2RouterMIBGroup.')
igmpV2RouterMIBGroup = ObjectGroup((1, 3, 6, 1, 3, 59, 2, 2, 5)).setObjects(("IGMP-MIB", "igmpInterfaceVersion"), ("IGMP-MIB", "igmpInterfaceQuerier"), ("IGMP-MIB", "igmpInterfaceQueryMaxResponseTime"), ("IGMP-MIB", "igmpInterfaceRobustness"), ("IGMP-MIB", "igmpInterfaceWrongVersionQueries"), ("IGMP-MIB", "igmpInterfaceJoins"), ("IGMP-MIB", "igmpInterfaceGroups"), ("IGMP-MIB", "igmpCacheVersion1HostTimer"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    igmpV2RouterMIBGroup = igmpV2RouterMIBGroup.setStatus('current')
if mibBuilder.loadTexts: igmpV2RouterMIBGroup.setDescription('A collection of additional objects for management\n\t\t      of IGMP version 2 in routers.')
mibBuilder.exportSymbols("IGMP-MIB", igmpInterfaceGroups=igmpInterfaceGroups, igmpMIBGroups=igmpMIBGroups, igmpRouterMIBGroup=igmpRouterMIBGroup, igmpInterfaceLeaveEnabled=igmpInterfaceLeaveEnabled, igmpV1RouterMIBCompliance=igmpV1RouterMIBCompliance, igmpV2RouterMIBCompliance=igmpV2RouterMIBCompliance, igmpCacheLastReporter=igmpCacheLastReporter, igmpInterfaceJoins=igmpInterfaceJoins, igmpV2RouterMIBGroup=igmpV2RouterMIBGroup, igmpCacheEntry=igmpCacheEntry, igmpInterfaceLeaves=igmpInterfaceLeaves, igmpRouterVersion2MIBGroup=igmpRouterVersion2MIBGroup, igmpCacheUpTime=igmpCacheUpTime, igmpBaseMIBGroup=igmpBaseMIBGroup, igmpInterfaceQuerierPresentTimeout=igmpInterfaceQuerierPresentTimeout, igmpInterfaceEntry=igmpInterfaceEntry, igmpMIBObjects=igmpMIBObjects, igmpInterfaceVersion1QuerierTimer=igmpInterfaceVersion1QuerierTimer, igmp=igmp, igmpCacheIfIndex=igmpCacheIfIndex, igmpCacheVersion1HostTimer=igmpCacheVersion1HostTimer, igmpV1HostMIBCompliance=igmpV1HostMIBCompliance, igmpCacheSelf=igmpCacheSelf, igmpInterfaceQueryMaxResponseTime=igmpInterfaceQueryMaxResponseTime, igmpInterfaceVersion=igmpInterfaceVersion, igmpInterfaceStatus=igmpInterfaceStatus, igmpInterfaceRobustness=igmpInterfaceRobustness, igmpInterfaceQuerier=igmpInterfaceQuerier, igmpCacheAddress=igmpCacheAddress, igmpMIBConformance=igmpMIBConformance, igmpInterfaceWrongVersionQueries=igmpInterfaceWrongVersionQueries, PYSNMP_MODULE_ID=igmpMIB, igmpV2HostMIBCompliance=igmpV2HostMIBCompliance, igmpCacheTable=igmpCacheTable, igmpCacheStatus=igmpCacheStatus, igmpMIB=igmpMIB, igmpMIBCompliances=igmpMIBCompliances, igmpCacheExpiryTime=igmpCacheExpiryTime, igmpInterfaceTable=igmpInterfaceTable, igmpInterfaceIfIndex=igmpInterfaceIfIndex, igmpV2HostMIBGroup=igmpV2HostMIBGroup, igmpInterfaceQueryInterval=igmpInterfaceQueryInterval)
