#
# PySNMP MIB module IPV6-MLD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/IPV6-MLD-MIB
# Produced by pysmi-1.1.3 at Sun Nov 28 20:09:06 2021
# On host fv-az77-612 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
InterfaceIndex, InterfaceIndexOrZero = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "InterfaceIndexOrZero")
InetAddressIPv6, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressIPv6")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
TimeTicks, Integer32, Counter64, ModuleIdentity, mib_2, MibIdentifier, iso, ObjectIdentity, IpAddress, Unsigned32, NotificationType, Counter32, Gauge32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Integer32", "Counter64", "ModuleIdentity", "mib-2", "MibIdentifier", "iso", "ObjectIdentity", "IpAddress", "Unsigned32", "NotificationType", "Counter32", "Gauge32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TruthValue, RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "RowStatus", "TextualConvention", "DisplayString")
mldMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 91))
mldMIB.setRevisions(('2001-01-25 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: mldMIB.setRevisionsDescriptions(('Initial version, published as RFC 3019.',))
if mibBuilder.loadTexts: mldMIB.setLastUpdated('200101250000Z')
if mibBuilder.loadTexts: mldMIB.setOrganization('IETF IPNGWG Working Group.')
if mibBuilder.loadTexts: mldMIB.setContactInfo(' Brian Haberman\n                 Nortel Networks\n                 4309 Emperor Blvd.\n                 Durham, NC  27703\n                 USA\n\n                 Phone: +1 919 992 4439\n                 e-mail: haberman@nortelnetworks.com')
if mibBuilder.loadTexts: mldMIB.setDescription('The MIB module for MLD Management.')
mldMIBObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 91, 1))
mldInterfaceTable = MibTable((1, 3, 6, 1, 2, 1, 91, 1, 1), )
if mibBuilder.loadTexts: mldInterfaceTable.setStatus('current')
if mibBuilder.loadTexts: mldInterfaceTable.setDescription('The (conceptual) table listing the interfaces on which\n                MLD is enabled.')
mldInterfaceEntry = MibTableRow((1, 3, 6, 1, 2, 1, 91, 1, 1, 1), ).setIndexNames((0, "IPV6-MLD-MIB", "mldInterfaceIfIndex"))
if mibBuilder.loadTexts: mldInterfaceEntry.setStatus('current')
if mibBuilder.loadTexts: mldInterfaceEntry.setDescription('An entry (conceptual row) representing an interface on\n               which MLD is enabled.')
mldInterfaceIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 91, 1, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: mldInterfaceIfIndex.setStatus('current')
if mibBuilder.loadTexts: mldInterfaceIfIndex.setDescription('The internetwork-layer interface value of the interface\n               for which MLD is enabled.')
mldInterfaceQueryInterval = MibTableColumn((1, 3, 6, 1, 2, 1, 91, 1, 1, 1, 2), Unsigned32().clone(125)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: mldInterfaceQueryInterval.setStatus('current')
if mibBuilder.loadTexts: mldInterfaceQueryInterval.setDescription('The frequency at which MLD Host-Query packets are\n               transmitted on this interface.')
mldInterfaceStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 91, 1, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mldInterfaceStatus.setStatus('current')
if mibBuilder.loadTexts: mldInterfaceStatus.setDescription('The activation of a row enables MLD on the interface.\n                The destruction of a row disables MLD on the interface.')
mldInterfaceVersion = MibTableColumn((1, 3, 6, 1, 2, 1, 91, 1, 1, 1, 4), Unsigned32().clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mldInterfaceVersion.setStatus('current')
if mibBuilder.loadTexts: mldInterfaceVersion.setDescription('The version of MLD which is running on this interface.\n                This object is a place holder to allow for new versions\n                of MLD to be introduced.  Version 1 of MLD is defined\n                in RFC 2710.')
mldInterfaceQuerier = MibTableColumn((1, 3, 6, 1, 2, 1, 91, 1, 1, 1, 5), InetAddressIPv6().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readonly")
if mibBuilder.loadTexts: mldInterfaceQuerier.setStatus('current')
if mibBuilder.loadTexts: mldInterfaceQuerier.setDescription('The address of the MLD Querier on the IPv6 subnet to\n                which this interface is attached.')
mldInterfaceQueryMaxRespDelay = MibTableColumn((1, 3, 6, 1, 2, 1, 91, 1, 1, 1, 6), Unsigned32().clone(10)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: mldInterfaceQueryMaxRespDelay.setStatus('current')
if mibBuilder.loadTexts: mldInterfaceQueryMaxRespDelay.setDescription('The maximum query response time advertised in MLD\n               queries on this interface.')
mldInterfaceJoins = MibTableColumn((1, 3, 6, 1, 2, 1, 91, 1, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mldInterfaceJoins.setStatus('current')
if mibBuilder.loadTexts: mldInterfaceJoins.setDescription('The number of times a group membership has been added on\n               this interface; that is, the number of times an entry for\n               this interface has been added to the Cache Table.  This\n               object gives an indication of the amount of MLD activity\n               over time.')
mldInterfaceGroups = MibTableColumn((1, 3, 6, 1, 2, 1, 91, 1, 1, 1, 8), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mldInterfaceGroups.setStatus('current')
if mibBuilder.loadTexts: mldInterfaceGroups.setDescription('The current number of entries for this interface in the\n               Cache Table.')
mldInterfaceRobustness = MibTableColumn((1, 3, 6, 1, 2, 1, 91, 1, 1, 1, 9), Unsigned32().clone(2)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mldInterfaceRobustness.setStatus('current')
if mibBuilder.loadTexts: mldInterfaceRobustness.setDescription('The Robustness Variable allows tuning for the expected\n               packet loss on a subnet.  If a subnet is expected to be\n               lossy, the Robustness Variable may be increased.  MLD is\n               robust to (Robustness Variable-1) packet losses.  The\n               discussion of the Robustness Variable is in Section 7.1\n               of RFC 2710.')
mldInterfaceLastListenQueryIntvl = MibTableColumn((1, 3, 6, 1, 2, 1, 91, 1, 1, 1, 10), Unsigned32().clone(1)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: mldInterfaceLastListenQueryIntvl.setStatus('current')
if mibBuilder.loadTexts: mldInterfaceLastListenQueryIntvl.setDescription('The Last Member Query Interval is the Max Response\n                Delay inserted into Group-Specific Queries sent in\n                response to Leave Group messages, and is also the amount\n                of time between Group-Specific Query messages.  This\n                value may be tuned to modify the leave latency of the\n                network.  A reduced value results in reduced time to\n                detect the loss of the last member of a group.')
mldInterfaceProxyIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 91, 1, 1, 1, 11), InterfaceIndexOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mldInterfaceProxyIfIndex.setStatus('current')
if mibBuilder.loadTexts: mldInterfaceProxyIfIndex.setDescription('Some devices implement a form of MLD proxying whereby\n                memberships learned on the interface represented by this\n                row, cause MLD Multicast Listener Reports to be sent on\n                the internetwork-layer interface identified by this\n                object.  Such a device would implement mldRouterMIBGroup\n                only on its router interfaces (those interfaces with\n                non-zero mldInterfaceProxyIfIndex).  Typically, the\n                value of this object is 0, indicating that no proxying\n                is being done.')
mldInterfaceQuerierUpTime = MibTableColumn((1, 3, 6, 1, 2, 1, 91, 1, 1, 1, 12), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mldInterfaceQuerierUpTime.setStatus('current')
if mibBuilder.loadTexts: mldInterfaceQuerierUpTime.setDescription('The time since mldInterfaceQuerier was last changed.')
mldInterfaceQuerierExpiryTime = MibTableColumn((1, 3, 6, 1, 2, 1, 91, 1, 1, 1, 13), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mldInterfaceQuerierExpiryTime.setStatus('current')
if mibBuilder.loadTexts: mldInterfaceQuerierExpiryTime.setDescription('The time remaining before the Other Querier Present\n               Timer expires.  If the local system is the querier,\n               the value of this object is zero.')
mldCacheTable = MibTable((1, 3, 6, 1, 2, 1, 91, 1, 2), )
if mibBuilder.loadTexts: mldCacheTable.setStatus('current')
if mibBuilder.loadTexts: mldCacheTable.setDescription('The (conceptual) table listing the IPv6 multicast\n                groups for which there are members on a particular\n                interface.')
mldCacheEntry = MibTableRow((1, 3, 6, 1, 2, 1, 91, 1, 2, 1), ).setIndexNames((0, "IPV6-MLD-MIB", "mldCacheAddress"), (0, "IPV6-MLD-MIB", "mldCacheIfIndex"))
if mibBuilder.loadTexts: mldCacheEntry.setStatus('current')
if mibBuilder.loadTexts: mldCacheEntry.setDescription('An entry (conceptual row) in the mldCacheTable.')
mldCacheAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 91, 1, 2, 1, 1), InetAddressIPv6().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16))
if mibBuilder.loadTexts: mldCacheAddress.setStatus('current')
if mibBuilder.loadTexts: mldCacheAddress.setDescription('The IPv6 multicast group address for which this entry\n               contains information.')
mldCacheIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 91, 1, 2, 1, 2), InterfaceIndex())
if mibBuilder.loadTexts: mldCacheIfIndex.setStatus('current')
if mibBuilder.loadTexts: mldCacheIfIndex.setDescription('The internetwork-layer interface for which this entry\n                contains information for an IPv6 multicast group\n                address.')
mldCacheSelf = MibTableColumn((1, 3, 6, 1, 2, 1, 91, 1, 2, 1, 3), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mldCacheSelf.setStatus('current')
if mibBuilder.loadTexts: mldCacheSelf.setDescription('An indication of whether the local system is a member of\n               this group address on this interface.')
mldCacheLastReporter = MibTableColumn((1, 3, 6, 1, 2, 1, 91, 1, 2, 1, 4), InetAddressIPv6().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readonly")
if mibBuilder.loadTexts: mldCacheLastReporter.setStatus('current')
if mibBuilder.loadTexts: mldCacheLastReporter.setDescription('The IPv6 address of the source of the last membership\n                report received for this IPv6 Multicast group address on\n                this interface.  If no membership report has been\n                received, this object has the value 0::0.')
mldCacheUpTime = MibTableColumn((1, 3, 6, 1, 2, 1, 91, 1, 2, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mldCacheUpTime.setStatus('current')
if mibBuilder.loadTexts: mldCacheUpTime.setDescription('The time elapsed since this entry was created.')
mldCacheExpiryTime = MibTableColumn((1, 3, 6, 1, 2, 1, 91, 1, 2, 1, 6), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mldCacheExpiryTime.setStatus('current')
if mibBuilder.loadTexts: mldCacheExpiryTime.setDescription('The minimum amount of time remaining before this entry\n                will be aged out.  A value of 0 indicates that the entry\n                is only present because mldCacheSelf is true and that if\n                the router left the group, this entry would be aged out\n                immediately.  Note that some implementations may process\n                Membership Reports from the local system in the same way\n                as reports from other hosts, so a value of 0 is not\n                required.')
mldCacheStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 91, 1, 2, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mldCacheStatus.setStatus('current')
if mibBuilder.loadTexts: mldCacheStatus.setDescription('The status of this row, by which new entries may be\n               created, or existing entries deleted from this table.')
mldMIBConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 91, 2))
mldMIBCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 91, 2, 1))
mldMIBGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 91, 2, 2))
mldHostMIBCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 91, 2, 1, 1)).setObjects(("IPV6-MLD-MIB", "mldBaseMIBGroup"), ("IPV6-MLD-MIB", "mldHostMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mldHostMIBCompliance = mldHostMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: mldHostMIBCompliance.setDescription('The compliance statement for hosts running MLD and\n               implementing the MLD MIB.')
mldRouterMIBCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 91, 2, 1, 2)).setObjects(("IPV6-MLD-MIB", "mldBaseMIBGroup"), ("IPV6-MLD-MIB", "mldRouterMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mldRouterMIBCompliance = mldRouterMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: mldRouterMIBCompliance.setDescription('The compliance statement for routers running MLD and\n               implementing the MLD MIB.')
mldBaseMIBGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 91, 2, 2, 1)).setObjects(("IPV6-MLD-MIB", "mldCacheSelf"), ("IPV6-MLD-MIB", "mldCacheStatus"), ("IPV6-MLD-MIB", "mldInterfaceStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mldBaseMIBGroup = mldBaseMIBGroup.setStatus('current')
if mibBuilder.loadTexts: mldBaseMIBGroup.setDescription('The basic collection of objects providing management of\n               MLD.  The mldBaseMIBGroup is designed to allow for the\n               manager creation and deletion of MLD cache entries.')
mldRouterMIBGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 91, 2, 2, 2)).setObjects(("IPV6-MLD-MIB", "mldCacheUpTime"), ("IPV6-MLD-MIB", "mldCacheExpiryTime"), ("IPV6-MLD-MIB", "mldInterfaceQueryInterval"), ("IPV6-MLD-MIB", "mldInterfaceJoins"), ("IPV6-MLD-MIB", "mldInterfaceGroups"), ("IPV6-MLD-MIB", "mldCacheLastReporter"), ("IPV6-MLD-MIB", "mldInterfaceQuerierUpTime"), ("IPV6-MLD-MIB", "mldInterfaceQuerierExpiryTime"), ("IPV6-MLD-MIB", "mldInterfaceQuerier"), ("IPV6-MLD-MIB", "mldInterfaceVersion"), ("IPV6-MLD-MIB", "mldInterfaceQueryMaxRespDelay"), ("IPV6-MLD-MIB", "mldInterfaceRobustness"), ("IPV6-MLD-MIB", "mldInterfaceLastListenQueryIntvl"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mldRouterMIBGroup = mldRouterMIBGroup.setStatus('current')
if mibBuilder.loadTexts: mldRouterMIBGroup.setDescription('A collection of additional objects for management of MLD\n               in routers.')
mldHostMIBGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 91, 2, 2, 3)).setObjects(("IPV6-MLD-MIB", "mldInterfaceQuerier"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mldHostMIBGroup = mldHostMIBGroup.setStatus('current')
if mibBuilder.loadTexts: mldHostMIBGroup.setDescription('A collection of additional objects for management of MLD\n               in hosts.')
mldProxyMIBGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 91, 2, 2, 4)).setObjects(("IPV6-MLD-MIB", "mldInterfaceProxyIfIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mldProxyMIBGroup = mldProxyMIBGroup.setStatus('current')
if mibBuilder.loadTexts: mldProxyMIBGroup.setDescription('A collection of additional objects for management of MLD\n               proxy devices.')
mibBuilder.exportSymbols("IPV6-MLD-MIB", mldHostMIBGroup=mldHostMIBGroup, mldMIBCompliances=mldMIBCompliances, mldInterfaceStatus=mldInterfaceStatus, mldInterfaceVersion=mldInterfaceVersion, mldInterfaceTable=mldInterfaceTable, mldInterfaceQueryMaxRespDelay=mldInterfaceQueryMaxRespDelay, mldCacheEntry=mldCacheEntry, mldInterfaceLastListenQueryIntvl=mldInterfaceLastListenQueryIntvl, mldHostMIBCompliance=mldHostMIBCompliance, mldMIBGroups=mldMIBGroups, mldInterfaceRobustness=mldInterfaceRobustness, mldInterfaceQueryInterval=mldInterfaceQueryInterval, mldCacheLastReporter=mldCacheLastReporter, mldInterfaceGroups=mldInterfaceGroups, mldInterfaceQuerier=mldInterfaceQuerier, mldCacheTable=mldCacheTable, mldInterfaceJoins=mldInterfaceJoins, mldCacheStatus=mldCacheStatus, PYSNMP_MODULE_ID=mldMIB, mldInterfaceProxyIfIndex=mldInterfaceProxyIfIndex, mldInterfaceQuerierExpiryTime=mldInterfaceQuerierExpiryTime, mldRouterMIBGroup=mldRouterMIBGroup, mldRouterMIBCompliance=mldRouterMIBCompliance, mldMIBObjects=mldMIBObjects, mldCacheUpTime=mldCacheUpTime, mldInterfaceEntry=mldInterfaceEntry, mldCacheAddress=mldCacheAddress, mldBaseMIBGroup=mldBaseMIBGroup, mldInterfaceQuerierUpTime=mldInterfaceQuerierUpTime, mldInterfaceIfIndex=mldInterfaceIfIndex, mldMIB=mldMIB, mldCacheSelf=mldCacheSelf, mldMIBConformance=mldMIBConformance, mldProxyMIBGroup=mldProxyMIBGroup, mldCacheExpiryTime=mldCacheExpiryTime, mldCacheIfIndex=mldCacheIfIndex)
