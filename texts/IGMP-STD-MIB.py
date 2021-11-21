#
# PySNMP MIB module IGMP-STD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/IGMP-STD-MIB
# Produced by pysmi-1.1.3 at Sun Nov 21 00:25:48 2021
# On host fv-az39-63 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
InterfaceIndexOrZero, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero", "InterfaceIndex")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
ModuleIdentity, Counter32, MibIdentifier, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, NotificationType, Counter64, iso, Unsigned32, Integer32, experimental, TimeTicks, IpAddress, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter32", "MibIdentifier", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "NotificationType", "Counter64", "iso", "Unsigned32", "Integer32", "experimental", "TimeTicks", "IpAddress", "ObjectIdentity")
TruthValue, DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "RowStatus", "TextualConvention")
igmpStdMIB = ModuleIdentity((1, 3, 6, 1, 3, 59))
igmpStdMIB.setRevisions(('1999-09-17 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: igmpStdMIB.setRevisionsDescriptions(('Initial version, published as RFC xxxx (to be filled in by\n            RFC-Editor).',))
if mibBuilder.loadTexts: igmpStdMIB.setLastUpdated('9909171200Z')
if mibBuilder.loadTexts: igmpStdMIB.setOrganization('IETF IDMR Working Group.')
if mibBuilder.loadTexts: igmpStdMIB.setContactInfo(' Dave Thaler\n              Microsoft Corporation\n              One Microsoft Way\n              Redmond, WA  98052-6399\n              US\n\n              Phone: +1 425 703 8835\n              EMail: dthaler@dthaler.microsoft.com')
if mibBuilder.loadTexts: igmpStdMIB.setDescription('The MIB module for IGMP Management.')
igmpMIBObjects = MibIdentifier((1, 3, 6, 1, 3, 59, 1))
igmp = MibIdentifier((1, 3, 6, 1, 3, 59, 1, 1))
igmpInterfaceTable = MibTable((1, 3, 6, 1, 3, 59, 1, 1, 1), )
if mibBuilder.loadTexts: igmpInterfaceTable.setStatus('current')
if mibBuilder.loadTexts: igmpInterfaceTable.setDescription('The (conceptual) table listing the interfaces on which IGMP\n            is enabled.')
igmpInterfaceEntry = MibTableRow((1, 3, 6, 1, 3, 59, 1, 1, 1, 1), ).setIndexNames((0, "IGMP-STD-MIB", "igmpInterfaceIfIndex"))
if mibBuilder.loadTexts: igmpInterfaceEntry.setStatus('current')
if mibBuilder.loadTexts: igmpInterfaceEntry.setDescription('An entry (conceptual row) representing an interface on\n            which IGMP is enabled.')
igmpInterfaceIfIndex = MibTableColumn((1, 3, 6, 1, 3, 59, 1, 1, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: igmpInterfaceIfIndex.setStatus('current')
if mibBuilder.loadTexts: igmpInterfaceIfIndex.setDescription('The ifIndex value of the interface for which IGMP is\n            enabled.')
igmpInterfaceQueryInterval = MibTableColumn((1, 3, 6, 1, 3, 59, 1, 1, 1, 1, 2), Integer32().clone(125)).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpInterfaceQueryInterval.setStatus('current')
if mibBuilder.loadTexts: igmpInterfaceQueryInterval.setDescription('The frequency at which IGMP Host-Query packets are\n            transmitted on this interface.')
igmpInterfaceStatus = MibTableColumn((1, 3, 6, 1, 3, 59, 1, 1, 1, 1, 3), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpInterfaceStatus.setStatus('current')
if mibBuilder.loadTexts: igmpInterfaceStatus.setDescription('The activation of a row enables IGMP on the interface.  The\n            destruction of a row disables IGMP on the interface.')
igmpInterfaceVersion = MibTableColumn((1, 3, 6, 1, 3, 59, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("version1", 1), ("version2", 2))).clone('version2')).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpInterfaceVersion.setStatus('current')
if mibBuilder.loadTexts: igmpInterfaceVersion.setDescription('The version of IGMP which is running on this interface.\n            This object can be used to configure a router capable of\n            running either value.  For IGMP to function correctly, all\n            routers on a LAN must be configured to run the same version\n            of IGMP on that LAN.')
igmpInterfaceQuerier = MibTableColumn((1, 3, 6, 1, 3, 59, 1, 1, 1, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpInterfaceQuerier.setStatus('current')
if mibBuilder.loadTexts: igmpInterfaceQuerier.setDescription('The address of the IGMP Querier on the IP subnet to which\n            this interface is attached.')
igmpInterfaceQueryMaxResponseTime = MibTableColumn((1, 3, 6, 1, 3, 59, 1, 1, 1, 1, 6), Integer32().clone(100)).setUnits('tenths of seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpInterfaceQueryMaxResponseTime.setStatus('current')
if mibBuilder.loadTexts: igmpInterfaceQueryMaxResponseTime.setDescription('The maximum query response time advertised in IGMPv2\n            queries on this interface.')
igmpInterfaceVersion1QuerierTimer = MibTableColumn((1, 3, 6, 1, 3, 59, 1, 1, 1, 1, 9), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpInterfaceVersion1QuerierTimer.setStatus('current')
if mibBuilder.loadTexts: igmpInterfaceVersion1QuerierTimer.setDescription('The time remaining until the host assumes that there are no\n            IGMPv1 routers present on the interface.  While this is non-\n            zero, the host will reply to all queries with version 1\n            membership reports.')
igmpInterfaceWrongVersionQueries = MibTableColumn((1, 3, 6, 1, 3, 59, 1, 1, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpInterfaceWrongVersionQueries.setStatus('current')
if mibBuilder.loadTexts: igmpInterfaceWrongVersionQueries.setDescription('The number of queries received whose IGMP version does not\n            match igmpInterfaceVersion.   IGMP requires that all routers\n            on a LAN be configured to run the same version of IGMP.\n            Thus, if any queries are received with the wrong version,\n            this indicates a configuration error.')
igmpInterfaceJoins = MibTableColumn((1, 3, 6, 1, 3, 59, 1, 1, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpInterfaceJoins.setStatus('current')
if mibBuilder.loadTexts: igmpInterfaceJoins.setDescription('The number of times a group membership has been added on\n            this interface; that is, the number of times an entry for\n            this interface has been added to the Cache Table.  This\n            object gives an indication of the amount of IGMP activity\n            over time.')
igmpInterfaceGroups = MibTableColumn((1, 3, 6, 1, 3, 59, 1, 1, 1, 1, 13), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpInterfaceGroups.setStatus('current')
if mibBuilder.loadTexts: igmpInterfaceGroups.setDescription('The current number of entries for this interface in the\n            Cache Table.')
igmpInterfaceRobustness = MibTableColumn((1, 3, 6, 1, 3, 59, 1, 1, 1, 1, 14), Integer32().clone(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpInterfaceRobustness.setStatus('current')
if mibBuilder.loadTexts: igmpInterfaceRobustness.setDescription('The Robustness Variable allows tuning for the expected\n            packet loss on a subnet.  If a subnet is expected to be\n            lossy, the Robustness Variable may be increased.  IGMP is\n            robust to (Robustness Variable-1) packet losses.')
igmpInterfaceLastMembQueryIntvl = MibTableColumn((1, 3, 6, 1, 3, 59, 1, 1, 1, 1, 15), Integer32().clone(10)).setUnits('tenths of seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpInterfaceLastMembQueryIntvl.setStatus('current')
if mibBuilder.loadTexts: igmpInterfaceLastMembQueryIntvl.setDescription('The Last Member Query Interval is the Max Response Time\n            inserted into Group-Specific Queries sent in response to\n            Leave Group messages, and is also the amount of time between\n            Group-Specific Query messages.  This value may be tuned to\n            modify the leave latency of the network.  A reduced value\n            results in reduced time to detect the loss of the last\n            member of a group.  The value of this object is irrelevant\n            if igmpInterfaceVersion is version1.')
igmpInterfaceProxyIfIndex = MibTableColumn((1, 3, 6, 1, 3, 59, 1, 1, 1, 1, 16), InterfaceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpInterfaceProxyIfIndex.setStatus('current')
if mibBuilder.loadTexts: igmpInterfaceProxyIfIndex.setDescription('Some devices implement a form of IGMP proxying whereby\n            memberships learned on the interface represented by this\n            row, cause IGMP Host Membership Reports to be sent on the\n            interface whose ifIndex value is given by this object.  Such\n            a device would implement the igmpV2RouterMIBGroup only on\n            its router interfaces (those interfaces with non-zero\n            igmpInterfaceProxyIfIndex).  Typically, the value of this\n            object is 0, indicating that no proxying is being done.')
igmpInterfaceQuerierUpTime = MibTableColumn((1, 3, 6, 1, 3, 59, 1, 1, 1, 1, 17), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpInterfaceQuerierUpTime.setStatus('current')
if mibBuilder.loadTexts: igmpInterfaceQuerierUpTime.setDescription('The time since igmpInterfaceQuerier was last changed.')
igmpInterfaceQuerierExpiryTime = MibTableColumn((1, 3, 6, 1, 3, 59, 1, 1, 1, 1, 18), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpInterfaceQuerierExpiryTime.setStatus('current')
if mibBuilder.loadTexts: igmpInterfaceQuerierExpiryTime.setDescription('The amount of time remaining before the Other Querier\n            Present Timer expires.  If the local system is the querier,\n            the value of this object is zero.')
igmpCacheTable = MibTable((1, 3, 6, 1, 3, 59, 1, 1, 2), )
if mibBuilder.loadTexts: igmpCacheTable.setStatus('current')
if mibBuilder.loadTexts: igmpCacheTable.setDescription('The (conceptual) table listing the IP multicast groups for\n            which there are members on a particular interface.')
igmpCacheEntry = MibTableRow((1, 3, 6, 1, 3, 59, 1, 1, 2, 1), ).setIndexNames((0, "IGMP-STD-MIB", "igmpCacheAddress"), (0, "IGMP-STD-MIB", "igmpCacheIfIndex"))
if mibBuilder.loadTexts: igmpCacheEntry.setStatus('current')
if mibBuilder.loadTexts: igmpCacheEntry.setDescription('An entry (conceptual row) in the igmpCacheTable.')
igmpCacheAddress = MibTableColumn((1, 3, 6, 1, 3, 59, 1, 1, 2, 1, 1), IpAddress())
if mibBuilder.loadTexts: igmpCacheAddress.setStatus('current')
if mibBuilder.loadTexts: igmpCacheAddress.setDescription('The IP multicast group address for which this entry\n            contains information.')
igmpCacheIfIndex = MibTableColumn((1, 3, 6, 1, 3, 59, 1, 1, 2, 1, 2), InterfaceIndex())
if mibBuilder.loadTexts: igmpCacheIfIndex.setStatus('current')
if mibBuilder.loadTexts: igmpCacheIfIndex.setDescription('The interface for which this entry contains information for\n            an IP multicast group address.')
igmpCacheSelf = MibTableColumn((1, 3, 6, 1, 3, 59, 1, 1, 2, 1, 3), TruthValue().clone('true')).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpCacheSelf.setStatus('current')
if mibBuilder.loadTexts: igmpCacheSelf.setDescription('An indication of whether the local system is a member of\n            this group address on this interface.')
igmpCacheLastReporter = MibTableColumn((1, 3, 6, 1, 3, 59, 1, 1, 2, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpCacheLastReporter.setStatus('current')
if mibBuilder.loadTexts: igmpCacheLastReporter.setDescription('The IP address of the source of the last membership report\n            received for this IP Multicast group address on this\n            interface.  If no membership report has been received, this\n            object has the value 0.0.0.0.')
igmpCacheUpTime = MibTableColumn((1, 3, 6, 1, 3, 59, 1, 1, 2, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpCacheUpTime.setStatus('current')
if mibBuilder.loadTexts: igmpCacheUpTime.setDescription('The time elapsed since this entry was created.')
igmpCacheExpiryTime = MibTableColumn((1, 3, 6, 1, 3, 59, 1, 1, 2, 1, 6), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpCacheExpiryTime.setStatus('current')
if mibBuilder.loadTexts: igmpCacheExpiryTime.setDescription('The minimum amount of time remaining before this entry will\n            be aged out.  A value of 0 indicates that the entry is only\n            present because igmpCacheSelf is true and that if the router\n            left the group, this entry would be aged out immediately.\n            Note that some implementations may process membership\n            reports from the local system in the same way as reports\n            from other hosts, so a value of 0 is not required.')
igmpCacheStatus = MibTableColumn((1, 3, 6, 1, 3, 59, 1, 1, 2, 1, 7), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpCacheStatus.setStatus('current')
if mibBuilder.loadTexts: igmpCacheStatus.setDescription('The status of this entry.')
igmpCacheVersion1HostTimer = MibTableColumn((1, 3, 6, 1, 3, 59, 1, 1, 2, 1, 8), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: igmpCacheVersion1HostTimer.setStatus('current')
if mibBuilder.loadTexts: igmpCacheVersion1HostTimer.setDescription('The time remaining until the local router will assume that\n            there are no longer any IGMP version 1 members on the IP\n            subnet attached to this interface.  Upon hearing any IGMPv1\n            Membership Report, this value is reset to the group\n            membership timer.  While this time remaining is non-zero,\n            the local router ignores any IGMPv2 Leave messages for this\n            group that it receives on this interface.')
igmpMIBConformance = MibIdentifier((1, 3, 6, 1, 3, 59, 2))
igmpMIBCompliances = MibIdentifier((1, 3, 6, 1, 3, 59, 2, 1))
igmpMIBGroups = MibIdentifier((1, 3, 6, 1, 3, 59, 2, 2))
igmpV1HostMIBCompliance = ModuleCompliance((1, 3, 6, 1, 3, 59, 2, 1, 1)).setObjects(("IGMP-STD-MIB", "igmpBaseMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    igmpV1HostMIBCompliance = igmpV1HostMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: igmpV1HostMIBCompliance.setDescription('The compliance statement for hosts running IGMPv1 and\n            implementing the IGMP MIB.')
igmpV1RouterMIBCompliance = ModuleCompliance((1, 3, 6, 1, 3, 59, 2, 1, 2)).setObjects(("IGMP-STD-MIB", "igmpBaseMIBGroup"), ("IGMP-STD-MIB", "igmpRouterMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    igmpV1RouterMIBCompliance = igmpV1RouterMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: igmpV1RouterMIBCompliance.setDescription('The compliance statement for routers running IGMPv1 and\n            implementing the IGMP MIB.')
igmpV2HostMIBCompliance = ModuleCompliance((1, 3, 6, 1, 3, 59, 2, 1, 3)).setObjects(("IGMP-STD-MIB", "igmpBaseMIBGroup"), ("IGMP-STD-MIB", "igmpV2HostMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    igmpV2HostMIBCompliance = igmpV2HostMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: igmpV2HostMIBCompliance.setDescription('The compliance statement for hosts running IGMPv2 and\n            implementing the IGMP MIB.')
igmpV2RouterMIBCompliance = ModuleCompliance((1, 3, 6, 1, 3, 59, 2, 1, 4)).setObjects(("IGMP-STD-MIB", "igmpBaseMIBGroup"), ("IGMP-STD-MIB", "igmpRouterMIBGroup"), ("IGMP-STD-MIB", "igmpV2RouterMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    igmpV2RouterMIBCompliance = igmpV2RouterMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: igmpV2RouterMIBCompliance.setDescription('The compliance statement for routers running IGMPv2 and\n            implementing the IGMP MIB.')
igmpBaseMIBGroup = ObjectGroup((1, 3, 6, 1, 3, 59, 2, 2, 1)).setObjects(("IGMP-STD-MIB", "igmpCacheSelf"), ("IGMP-STD-MIB", "igmpCacheStatus"), ("IGMP-STD-MIB", "igmpInterfaceStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    igmpBaseMIBGroup = igmpBaseMIBGroup.setStatus('current')
if mibBuilder.loadTexts: igmpBaseMIBGroup.setDescription('The basic collection of objects providing management of\n            IGMP version 1 or 2.')
igmpRouterMIBGroup = ObjectGroup((1, 3, 6, 1, 3, 59, 2, 2, 2)).setObjects(("IGMP-STD-MIB", "igmpCacheUpTime"), ("IGMP-STD-MIB", "igmpCacheExpiryTime"), ("IGMP-STD-MIB", "igmpInterfaceJoins"), ("IGMP-STD-MIB", "igmpInterfaceGroups"), ("IGMP-STD-MIB", "igmpCacheLastReporter"), ("IGMP-STD-MIB", "igmpInterfaceQuerierUpTime"), ("IGMP-STD-MIB", "igmpInterfaceQuerierExpiryTime"), ("IGMP-STD-MIB", "igmpInterfaceQueryInterval"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    igmpRouterMIBGroup = igmpRouterMIBGroup.setStatus('current')
if mibBuilder.loadTexts: igmpRouterMIBGroup.setDescription('A collection of additional objects for management of IGMP\n            version 1 or 2 in routers.')
igmpV2HostMIBGroup = ObjectGroup((1, 3, 6, 1, 3, 59, 2, 2, 3)).setObjects(("IGMP-STD-MIB", "igmpInterfaceVersion1QuerierTimer"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    igmpV2HostMIBGroup = igmpV2HostMIBGroup.setStatus('current')
if mibBuilder.loadTexts: igmpV2HostMIBGroup.setDescription('A collection of additional objects for management of IGMP\n            version 2 in hosts.')
igmpHostOptMIBGroup = ObjectGroup((1, 3, 6, 1, 3, 59, 2, 2, 4)).setObjects(("IGMP-STD-MIB", "igmpCacheLastReporter"), ("IGMP-STD-MIB", "igmpInterfaceQuerier"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    igmpHostOptMIBGroup = igmpHostOptMIBGroup.setStatus('current')
if mibBuilder.loadTexts: igmpHostOptMIBGroup.setDescription('A collection of optional objects for IGMP hosts.\n            Supporting this group can be especially useful in an\n            environment with a router which does not support the IGMP\n            MIB.')
igmpV2RouterMIBGroup = ObjectGroup((1, 3, 6, 1, 3, 59, 2, 2, 5)).setObjects(("IGMP-STD-MIB", "igmpInterfaceVersion"), ("IGMP-STD-MIB", "igmpInterfaceQuerier"), ("IGMP-STD-MIB", "igmpInterfaceQueryMaxResponseTime"), ("IGMP-STD-MIB", "igmpInterfaceRobustness"), ("IGMP-STD-MIB", "igmpInterfaceWrongVersionQueries"), ("IGMP-STD-MIB", "igmpInterfaceLastMembQueryIntvl"), ("IGMP-STD-MIB", "igmpCacheVersion1HostTimer"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    igmpV2RouterMIBGroup = igmpV2RouterMIBGroup.setStatus('current')
if mibBuilder.loadTexts: igmpV2RouterMIBGroup.setDescription('A collection of additional objects for management of IGMP\n            version 2 in routers.')
igmpV2ProxyMIBGroup = ObjectGroup((1, 3, 6, 1, 3, 59, 2, 2, 6)).setObjects(("IGMP-STD-MIB", "igmpInterfaceProxyIfIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    igmpV2ProxyMIBGroup = igmpV2ProxyMIBGroup.setStatus('current')
if mibBuilder.loadTexts: igmpV2ProxyMIBGroup.setDescription('A collection of additional objects for management of IGMP\n            proxy devices.')
mibBuilder.exportSymbols("IGMP-STD-MIB", igmpInterfaceQuerierExpiryTime=igmpInterfaceQuerierExpiryTime, igmpV2HostMIBGroup=igmpV2HostMIBGroup, igmpCacheTable=igmpCacheTable, igmpBaseMIBGroup=igmpBaseMIBGroup, igmpV2RouterMIBGroup=igmpV2RouterMIBGroup, igmpCacheSelf=igmpCacheSelf, igmpCacheVersion1HostTimer=igmpCacheVersion1HostTimer, igmpInterfaceStatus=igmpInterfaceStatus, igmpInterfaceIfIndex=igmpInterfaceIfIndex, igmpCacheIfIndex=igmpCacheIfIndex, igmpStdMIB=igmpStdMIB, igmpInterfaceGroups=igmpInterfaceGroups, igmpV2HostMIBCompliance=igmpV2HostMIBCompliance, igmpV2ProxyMIBGroup=igmpV2ProxyMIBGroup, igmpInterfaceJoins=igmpInterfaceJoins, igmpCacheAddress=igmpCacheAddress, igmpInterfaceLastMembQueryIntvl=igmpInterfaceLastMembQueryIntvl, igmp=igmp, igmpInterfaceQueryInterval=igmpInterfaceQueryInterval, igmpCacheUpTime=igmpCacheUpTime, igmpHostOptMIBGroup=igmpHostOptMIBGroup, igmpV1HostMIBCompliance=igmpV1HostMIBCompliance, igmpInterfaceQueryMaxResponseTime=igmpInterfaceQueryMaxResponseTime, igmpMIBObjects=igmpMIBObjects, igmpInterfaceRobustness=igmpInterfaceRobustness, igmpInterfaceQuerierUpTime=igmpInterfaceQuerierUpTime, igmpCacheLastReporter=igmpCacheLastReporter, igmpMIBGroups=igmpMIBGroups, igmpCacheStatus=igmpCacheStatus, igmpInterfaceWrongVersionQueries=igmpInterfaceWrongVersionQueries, igmpV1RouterMIBCompliance=igmpV1RouterMIBCompliance, igmpInterfaceVersion=igmpInterfaceVersion, PYSNMP_MODULE_ID=igmpStdMIB, igmpCacheEntry=igmpCacheEntry, igmpCacheExpiryTime=igmpCacheExpiryTime, igmpInterfaceQuerier=igmpInterfaceQuerier, igmpInterfaceEntry=igmpInterfaceEntry, igmpMIBConformance=igmpMIBConformance, igmpMIBCompliances=igmpMIBCompliances, igmpV2RouterMIBCompliance=igmpV2RouterMIBCompliance, igmpInterfaceTable=igmpInterfaceTable, igmpRouterMIBGroup=igmpRouterMIBGroup, igmpInterfaceProxyIfIndex=igmpInterfaceProxyIfIndex, igmpInterfaceVersion1QuerierTimer=igmpInterfaceVersion1QuerierTimer)
