#
# PySNMP MIB module DVMRP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/DVMRP-MIB
# Produced by pysmi-1.1.3 at Sun Nov 28 20:09:06 2021
# On host fv-az77-612 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
TimeTicks, Integer32, Counter64, ModuleIdentity, MibIdentifier, iso, ObjectIdentity, Unsigned32, NotificationType, experimental, Bits, Counter32, Gauge32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Integer32", "Counter64", "ModuleIdentity", "MibIdentifier", "iso", "ObjectIdentity", "Unsigned32", "NotificationType", "experimental", "Bits", "Counter32", "Gauge32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
dvmrpMIB = ModuleIdentity((1, 3, 6, 1, 3, 62))
if mibBuilder.loadTexts: dvmrpMIB.setLastUpdated('9804221900Z')
if mibBuilder.loadTexts: dvmrpMIB.setOrganization('IETF IDMR Working Group.')
if mibBuilder.loadTexts: dvmrpMIB.setContactInfo(' Dave Thaler\n              Microsoft\n              One Microsoft Way\n              Redmond, WA 98052-6399\n              EMail: dthalerd@microsoft.com')
if mibBuilder.loadTexts: dvmrpMIB.setDescription('The MIB module for management of DVMRP routers.')
dvmrpMIBObjects = MibIdentifier((1, 3, 6, 1, 3, 62, 1))
dvmrp = MibIdentifier((1, 3, 6, 1, 3, 62, 1, 1))
dvmrpVersionString = MibScalar((1, 3, 6, 1, 3, 62, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpVersionString.setStatus('current')
if mibBuilder.loadTexts: dvmrpVersionString.setDescription("The router's DVMRP version information.")
dvmrpGenerationId = MibScalar((1, 3, 6, 1, 3, 62, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpGenerationId.setStatus('current')
if mibBuilder.loadTexts: dvmrpGenerationId.setDescription('The generation identifier for the routing process.  This is\n            used by neighboring routers to detect whether the DVMRP\n            routing table should be resent.')
dvmrpNumRoutes = MibScalar((1, 3, 6, 1, 3, 62, 1, 1, 9), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpNumRoutes.setStatus('current')
if mibBuilder.loadTexts: dvmrpNumRoutes.setDescription('The number of entries in the routing table.  This can be\n            used to monitor the routing table size to detect illegal\n            advertisements of unicast routes.')
dvmrpReachableRoutes = MibScalar((1, 3, 6, 1, 3, 62, 1, 1, 10), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpReachableRoutes.setStatus('current')
if mibBuilder.loadTexts: dvmrpReachableRoutes.setDescription('The number of entries in the routing table with non\n            infinite metrics.  This can be used to detect network\n            partitions by observing the ratio of reachable routes to\n            total routes.')
dvmrpInterfaceTable = MibTable((1, 3, 6, 1, 3, 62, 1, 1, 3), )
if mibBuilder.loadTexts: dvmrpInterfaceTable.setStatus('current')
if mibBuilder.loadTexts: dvmrpInterfaceTable.setDescription("The (conceptual) table listing the router's multicast-\n            capable interfaces.")
dvmrpInterfaceEntry = MibTableRow((1, 3, 6, 1, 3, 62, 1, 1, 3, 1), ).setIndexNames((0, "DVMRP-MIB", "dvmrpInterfaceIfIndex"))
if mibBuilder.loadTexts: dvmrpInterfaceEntry.setStatus('current')
if mibBuilder.loadTexts: dvmrpInterfaceEntry.setDescription('An entry (conceptual row) in the dvmrpInterfaceTable.  This\n            row augments ipMRouteInterfaceEntry in the IP Multicast MIB,\n            where the threshold object resides.')
dvmrpInterfaceIfIndex = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 3, 1, 1), Integer32())
if mibBuilder.loadTexts: dvmrpInterfaceIfIndex.setStatus('current')
if mibBuilder.loadTexts: dvmrpInterfaceIfIndex.setDescription('The ifIndex value of the interface for which DVMRP is\n            enabled.')
dvmrpInterfaceType = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("tunnel", 1), ("srcrt", 2), ("querier", 3), ("subnet", 4))).clone('tunnel')).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpInterfaceType.setStatus('deprecated')
if mibBuilder.loadTexts: dvmrpInterfaceType.setDescription('The type of this DVMRP interface, whether it uses a tunnel,\n            source routing, a physical interface for which we are a\n            querier, or a physical interface for which we are not a\n            querier.  This object is deprecated in favor of ifType.')
dvmrpInterfaceOperState = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpInterfaceOperState.setStatus('deprecated')
if mibBuilder.loadTexts: dvmrpInterfaceOperState.setDescription('The current operational state of this DVMRP interface. This\n            object is deprecated in favor of ifOperStatus.')
dvmrpInterfaceLocalAddress = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 3, 1, 4), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dvmrpInterfaceLocalAddress.setStatus('current')
if mibBuilder.loadTexts: dvmrpInterfaceLocalAddress.setDescription('The IP address this system will use as a source address on\n            this interface.  On unnumbered interfaces, it must be the\n            same value as dvmrpInterfaceLocalAddress for some interface\n            on the system.')
dvmrpInterfaceRemoteAddress = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 3, 1, 5), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dvmrpInterfaceRemoteAddress.setStatus('deprecated')
if mibBuilder.loadTexts: dvmrpInterfaceRemoteAddress.setDescription('The IP address of the remote end of this DVMRP virtual\n            interface.  For a tunnel (including source routed), this is\n            the IP address of the neighboring router.  For a subnet,\n            this is the subnet address.  This object is deprecated in\n            favor of address information associated with the underlying\n            ifEntry.')
dvmrpInterfaceRemoteSubnetMask = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 3, 1, 6), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpInterfaceRemoteSubnetMask.setStatus('deprecated')
if mibBuilder.loadTexts: dvmrpInterfaceRemoteSubnetMask.setDescription('The subnet mask for a directly connected subnet.  For a\n            tunnel, this should be 0.0.0.0.  This object is deprecated\n            in favor of address information associated with the\n            underlying ifEntry.')
dvmrpInterfaceMetric = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 3, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 31)).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dvmrpInterfaceMetric.setStatus('current')
if mibBuilder.loadTexts: dvmrpInterfaceMetric.setDescription('The distance metric for this interface which is used to\n            calculate distance vectors.')
dvmrpInterfaceRateLimit = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 3, 1, 8), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dvmrpInterfaceRateLimit.setStatus('deprecated')
if mibBuilder.loadTexts: dvmrpInterfaceRateLimit.setDescription('The rate-limit, in kilobits per second, of forwarded\n            multicast traffic on the interface.  A rate-limit of 0\n            indicates that no rate limiting is done.  This object has\n            been moved to the IP Multicast MIB.')
dvmrpInterfaceInPkts = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 3, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpInterfaceInPkts.setStatus('deprecated')
if mibBuilder.loadTexts: dvmrpInterfaceInPkts.setDescription('The number of multicast packets that have arrived on the\n            interface.  This object is deprecated in favor of\n            ifInMulticastPkts in the Interfaces MIB [8].')
dvmrpInterfaceOutPkts = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 3, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpInterfaceOutPkts.setStatus('deprecated')
if mibBuilder.loadTexts: dvmrpInterfaceOutPkts.setDescription('The number of multicast packets that have been sent on the\n            interface.  This object is deprecated in favor of\n            ifOutMulticastPkts in the Interfaces MIB [8].')
dvmrpInterfaceInOctets = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 3, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpInterfaceInOctets.setStatus('deprecated')
if mibBuilder.loadTexts: dvmrpInterfaceInOctets.setDescription('The number of octets in multicast packets that have arrived\n            on the interface.  This object has been moved to the IP\n            Multicast MIB.')
dvmrpInterfaceOutOctets = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 3, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpInterfaceOutOctets.setStatus('deprecated')
if mibBuilder.loadTexts: dvmrpInterfaceOutOctets.setDescription('The number of octets in multicast packets that have been\n            sent on the interface.  This object has been moved to the IP\n            Multicast MIB.')
dvmrpInterfaceStatus = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 3, 1, 13), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dvmrpInterfaceStatus.setStatus('current')
if mibBuilder.loadTexts: dvmrpInterfaceStatus.setDescription('The status of this entry.  Creating the entry enables DVMRP\n            on the virtual interface; destroying the entry or setting it\n            to notInService disables DVMRP on the virtual interface.')
dvmrpInterfaceRcvBadPkts = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 3, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpInterfaceRcvBadPkts.setStatus('current')
if mibBuilder.loadTexts: dvmrpInterfaceRcvBadPkts.setDescription('The number of DVMRP packets received on the interface by\n            the DVMRP process which were subsequently discarded as\n            invalid (e.g. invalid packet format, or a route report from\n            an unknown neighbor).')
dvmrpInterfaceRcvBadRoutes = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 3, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpInterfaceRcvBadRoutes.setStatus('current')
if mibBuilder.loadTexts: dvmrpInterfaceRcvBadRoutes.setDescription('The number of routes, in valid DVMRP packets, which were\n            ignored because the entry was invalid.')
dvmrpInterfaceSentRoutes = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 3, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpInterfaceSentRoutes.setStatus('current')
if mibBuilder.loadTexts: dvmrpInterfaceSentRoutes.setDescription('The number of routes, in DVMRP Report packets, which have\n            been sent on this interface.  Together with\n            dvmrpNeighborRcvRoutes at a peer, this object is useful for\n            detecting routes being lost.')
dvmrpInterfaceMasterKey = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 3, 1, 17), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dvmrpInterfaceMasterKey.setStatus('current')
if mibBuilder.loadTexts: dvmrpInterfaceMasterKey.setDescription('The master (shared) key for authenticating neighbors on\n            this interface.  This object is intended solely for the\n            purpose of setting the master key, and MUST be accessible\n            only via requests using both authentication and privacy.\n            The agent MAY report an empty string in response to get,\n            get-next, get-bulk requests.')
dvmrpInterfaceMasterKeyVersion = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 3, 1, 18), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dvmrpInterfaceMasterKeyVersion.setStatus('current')
if mibBuilder.loadTexts: dvmrpInterfaceMasterKeyVersion.setDescription('The highest version number of all known master keys used\n            for authenticating neighbors on this interface.')
dvmrpNeighborTable = MibTable((1, 3, 6, 1, 3, 62, 1, 1, 4), )
if mibBuilder.loadTexts: dvmrpNeighborTable.setStatus('current')
if mibBuilder.loadTexts: dvmrpNeighborTable.setDescription("The (conceptual) table listing the router's DVMRP\n            neighbors, as discovered by receiving DVMRP messages.")
dvmrpNeighborEntry = MibTableRow((1, 3, 6, 1, 3, 62, 1, 1, 4, 1), ).setIndexNames((0, "DVMRP-MIB", "dvmrpNeighborIfIndex"), (0, "DVMRP-MIB", "dvmrpNeighborAddress"))
if mibBuilder.loadTexts: dvmrpNeighborEntry.setStatus('current')
if mibBuilder.loadTexts: dvmrpNeighborEntry.setDescription('An entry (conceptual row) in the dvmrpNeighborTable.')
dvmrpNeighborIfIndex = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpNeighborIfIndex.setStatus('current')
if mibBuilder.loadTexts: dvmrpNeighborIfIndex.setDescription('The value of ifIndex for the virtual interface used to\n            reach this DVMRP neighbor.')
dvmrpNeighborAddress = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 4, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpNeighborAddress.setStatus('current')
if mibBuilder.loadTexts: dvmrpNeighborAddress.setDescription('The IP address of the DVMRP neighbor for which this entry\n            contains information.')
dvmrpNeighborUpTime = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 4, 1, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpNeighborUpTime.setStatus('current')
if mibBuilder.loadTexts: dvmrpNeighborUpTime.setDescription('The time since this DVMRP neighbor (last) became a neighbor\n            of the local router.')
dvmrpNeighborExpiryTime = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 4, 1, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpNeighborExpiryTime.setStatus('current')
if mibBuilder.loadTexts: dvmrpNeighborExpiryTime.setDescription('The minimum time remaining before this DVMRP neighbor will\n            be aged out.')
dvmrpNeighborGenerationId = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 4, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpNeighborGenerationId.setStatus('current')
if mibBuilder.loadTexts: dvmrpNeighborGenerationId.setDescription("The neighboring router's generation identifier.")
dvmrpNeighborMajorVersion = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 4, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpNeighborMajorVersion.setStatus('current')
if mibBuilder.loadTexts: dvmrpNeighborMajorVersion.setDescription("The neighboring router's major DVMRP version number.")
dvmrpNeighborMinorVersion = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 4, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpNeighborMinorVersion.setStatus('current')
if mibBuilder.loadTexts: dvmrpNeighborMinorVersion.setDescription("The neighboring router's minor DVMRP version number.")
dvmrpNeighborCapabilities = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 4, 1, 9), Bits().clone(namedValues=NamedValues(("leaf", 0), ("prune", 1), ("generationID", 2), ("mtrace", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpNeighborCapabilities.setStatus('current')
if mibBuilder.loadTexts: dvmrpNeighborCapabilities.setDescription("This object describes the neighboring router's\n            capabilities.  The leaf bit indicates that the neighbor has\n            only one interface with neighbors.  The prune bit indicates\n            that the neighbor supports pruning.  The generationID bit\n            indicates that the neighbor sends its generationID in Probe\n            messages.  The mtrace bit indicates that the neighbor can\n            handle mtrace requests.")
dvmrpNeighborRcvRoutes = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 4, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpNeighborRcvRoutes.setStatus('current')
if mibBuilder.loadTexts: dvmrpNeighborRcvRoutes.setDescription('The total number of routes received in valid DVMRP packets\n            received from this neighbor.  This can be used to diagnose\n            problems such as unicast route injection, as well as giving\n            an indication of the level of DVMRP route exchange\n            activity.')
dvmrpNeighborRcvBadPkts = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 4, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpNeighborRcvBadPkts.setStatus('current')
if mibBuilder.loadTexts: dvmrpNeighborRcvBadPkts.setDescription('The number of packet received from this neighbor which were\n            discarded as invalid.')
dvmrpNeighborRcvBadRoutes = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 4, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpNeighborRcvBadRoutes.setStatus('current')
if mibBuilder.loadTexts: dvmrpNeighborRcvBadRoutes.setDescription('The number of routes, in valid DVMRP packets received from\n            this neighbor, which were ignored because the entry was\n            invalid.')
dvmrpNeighborState = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 4, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("oneway", 1), ("active", 2), ("ignoring", 3), ("down", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpNeighborState.setStatus('current')
if mibBuilder.loadTexts: dvmrpNeighborState.setDescription('State of the neighbor adjacency.')
dvmrpRouteTable = MibTable((1, 3, 6, 1, 3, 62, 1, 1, 5), )
if mibBuilder.loadTexts: dvmrpRouteTable.setStatus('current')
if mibBuilder.loadTexts: dvmrpRouteTable.setDescription('The table of routes learned through DVMRP route exchange.')
dvmrpRouteEntry = MibTableRow((1, 3, 6, 1, 3, 62, 1, 1, 5, 1), ).setIndexNames((0, "DVMRP-MIB", "dvmrpRouteSource"), (0, "DVMRP-MIB", "dvmrpRouteSourceMask"))
if mibBuilder.loadTexts: dvmrpRouteEntry.setStatus('current')
if mibBuilder.loadTexts: dvmrpRouteEntry.setDescription('An entry (conceptual row) containing the multicast routing\n            information used by DVMRP in place of the unicast routing\n            information.')
dvmrpRouteSource = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 5, 1, 1), IpAddress())
if mibBuilder.loadTexts: dvmrpRouteSource.setStatus('current')
if mibBuilder.loadTexts: dvmrpRouteSource.setDescription('The network address which when combined with the\n            corresponding value of dvmrpRouteSourceMask identifies the\n            sources for which this entry contains multicast routing\n            information.')
dvmrpRouteSourceMask = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 5, 1, 2), IpAddress())
if mibBuilder.loadTexts: dvmrpRouteSourceMask.setStatus('current')
if mibBuilder.loadTexts: dvmrpRouteSourceMask.setDescription('The network mask which when combined with the corresponding\n            value of dvmrpRouteSource identifies the sources for which\n            this entry contains multicast routing information.')
dvmrpRouteUpstreamNeighbor = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 5, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpRouteUpstreamNeighbor.setStatus('current')
if mibBuilder.loadTexts: dvmrpRouteUpstreamNeighbor.setDescription('The address of the upstream neighbor (e.g., RPF neighbor)\n            from which IP datagrams from these sources are received.')
dvmrpRouteIfIndex = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 5, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpRouteIfIndex.setStatus('current')
if mibBuilder.loadTexts: dvmrpRouteIfIndex.setDescription('The value of ifIndex for the interface on which IP\n            datagrams sent by these sources are received.')
dvmrpRouteMetric = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 5, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpRouteMetric.setStatus('current')
if mibBuilder.loadTexts: dvmrpRouteMetric.setDescription('The distance in hops to the source subnet.')
dvmrpRouteExpiryTime = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 5, 1, 6), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpRouteExpiryTime.setStatus('current')
if mibBuilder.loadTexts: dvmrpRouteExpiryTime.setDescription('The minimum amount of time remaining before this entry will\n            be aged out.')
dvmrpRouteUpTime = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 5, 1, 7), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpRouteUpTime.setStatus('current')
if mibBuilder.loadTexts: dvmrpRouteUpTime.setDescription('The time since the route represented by this entry was\n            learned by the router.')
dvmrpRouteNextHopTable = MibTable((1, 3, 6, 1, 3, 62, 1, 1, 6), )
if mibBuilder.loadTexts: dvmrpRouteNextHopTable.setStatus('current')
if mibBuilder.loadTexts: dvmrpRouteNextHopTable.setDescription('The (conceptual) table containing information on the next\n            hops on outgoing interfaces for routing IP multicast\n            datagrams.')
dvmrpRouteNextHopEntry = MibTableRow((1, 3, 6, 1, 3, 62, 1, 1, 6, 1), ).setIndexNames((0, "DVMRP-MIB", "dvmrpRouteNextHopSource"), (0, "DVMRP-MIB", "dvmrpRouteNextHopSourceMask"), (0, "DVMRP-MIB", "dvmrpRouteNextHopIfIndex"))
if mibBuilder.loadTexts: dvmrpRouteNextHopEntry.setStatus('current')
if mibBuilder.loadTexts: dvmrpRouteNextHopEntry.setDescription('An entry (conceptual row) in the list of next hops on\n            outgoing interfaces to which IP multicast datagrams from\n            particular sources are routed.')
dvmrpRouteNextHopSource = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 6, 1, 1), IpAddress())
if mibBuilder.loadTexts: dvmrpRouteNextHopSource.setStatus('current')
if mibBuilder.loadTexts: dvmrpRouteNextHopSource.setDescription('The network address which when combined with the\n            corresponding value of dvmrpRouteNextHopSourceMask\n            identifies the sources for which this entry specifies a next\n            hop on an outgoing interface.')
dvmrpRouteNextHopSourceMask = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 6, 1, 2), IpAddress())
if mibBuilder.loadTexts: dvmrpRouteNextHopSourceMask.setStatus('current')
if mibBuilder.loadTexts: dvmrpRouteNextHopSourceMask.setDescription('The network mask which when combined with the corresponding\n            value of dvmrpRouteNextHopSource identifies the sources for\n            which this entry specifies a next hop on an outgoing\n            interface.')
dvmrpRouteNextHopIfIndex = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 6, 1, 3), Integer32())
if mibBuilder.loadTexts: dvmrpRouteNextHopIfIndex.setStatus('current')
if mibBuilder.loadTexts: dvmrpRouteNextHopIfIndex.setDescription('The ifIndex value of the interface for the outgoing\n            interface for this next hop.')
dvmrpRouteNextHopType = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 6, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("leaf", 1), ("branch", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpRouteNextHopType.setStatus('current')
if mibBuilder.loadTexts: dvmrpRouteNextHopType.setDescription('Type is leaf if no downstream dependent neighbors exist on\n            the outgoing virtual interface.  Otherwise, type is branch.')
dvmrpAltNetTable = MibTable((1, 3, 6, 1, 3, 62, 1, 1, 8), )
if mibBuilder.loadTexts: dvmrpAltNetTable.setStatus('deprecated')
if mibBuilder.loadTexts: dvmrpAltNetTable.setDescription("The (conceptual) table listing the router's alternate\n            subnets on physical interfaces for use in constructing the\n            routing tables.")
dvmrpAltNetEntry = MibTableRow((1, 3, 6, 1, 3, 62, 1, 1, 8, 1), ).setIndexNames((0, "DVMRP-MIB", "dvmrpAltNetIfIndex"), (0, "DVMRP-MIB", "dvmrpAltNetAddress"), (0, "DVMRP-MIB", "dvmrpAltNetMask"))
if mibBuilder.loadTexts: dvmrpAltNetEntry.setStatus('deprecated')
if mibBuilder.loadTexts: dvmrpAltNetEntry.setDescription('An entry (conceptual row) in the dvmrpAltNetTable.')
dvmrpAltNetIfIndex = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 8, 1, 1), Integer32())
if mibBuilder.loadTexts: dvmrpAltNetIfIndex.setStatus('deprecated')
if mibBuilder.loadTexts: dvmrpAltNetIfIndex.setDescription('The ifIndex value of the interface to which this alternate\n            subnet applies.')
dvmrpAltNetAddress = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 8, 1, 2), IpAddress())
if mibBuilder.loadTexts: dvmrpAltNetAddress.setStatus('deprecated')
if mibBuilder.loadTexts: dvmrpAltNetAddress.setDescription('The subnet address of the alternate subnet.')
dvmrpAltNetMask = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 8, 1, 3), IpAddress())
if mibBuilder.loadTexts: dvmrpAltNetMask.setStatus('deprecated')
if mibBuilder.loadTexts: dvmrpAltNetMask.setDescription('The subnet mask of the alternate subnet.')
dvmrpAltNetStatus = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 8, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dvmrpAltNetStatus.setStatus('deprecated')
if mibBuilder.loadTexts: dvmrpAltNetStatus.setDescription('The status of this row, by which new entries may be\n            created, or old entries deleted from this table.')
dvmrpTraps = MibIdentifier((1, 3, 6, 1, 3, 62, 1, 1, 11))
dvmrpNeighborLoss = NotificationType((1, 3, 6, 1, 3, 62, 1, 1, 11, 1)).setObjects(("DVMRP-MIB", "dvmrpInterfaceLocalAddress"), ("DVMRP-MIB", "dvmrpNeighborIfIndex"), ("DVMRP-MIB", "dvmrpNeighborAddress"), ("DVMRP-MIB", "dvmrpNeighborState"))
if mibBuilder.loadTexts: dvmrpNeighborLoss.setStatus('current')
if mibBuilder.loadTexts: dvmrpNeighborLoss.setDescription('A dvmrpNeighborLoss trap signifies the loss of a 2-way\n            adjacency with a neighbor.  This trap should be generated\n            when the neighbor state changes from active to one-way,\n            ignoring, or down.  The trap should be generated only if the\n            router has no other neighbors on the same interface with a\n            lower IP address than itself.')
dvmrpNeighborNotPruning = NotificationType((1, 3, 6, 1, 3, 62, 1, 1, 11, 2)).setObjects(("DVMRP-MIB", "dvmrpInterfaceLocalAddress"), ("DVMRP-MIB", "dvmrpNeighborIfIndex"), ("DVMRP-MIB", "dvmrpNeighborAddress"))
if mibBuilder.loadTexts: dvmrpNeighborNotPruning.setStatus('current')
if mibBuilder.loadTexts: dvmrpNeighborNotPruning.setDescription('A dvmrpNeighborNotPruning trap signifies that a non-pruning\n            neighbor has been detected.  This trap should be generated\n            at most once per generation ID of the neighbor.  For\n            example, it may be generated at the time a neighbor is first\n            heard from if the prune bit is not set in its capabilities.\n            The trap should be generated only if the router has no other\n            neighbors on the same interface with a lower IP address than\n            itself.')
dvmrpMIBConformance = MibIdentifier((1, 3, 6, 1, 3, 62, 2))
dvmrpMIBCompliances = MibIdentifier((1, 3, 6, 1, 3, 62, 2, 1))
dvmrpMIBGroups = MibIdentifier((1, 3, 6, 1, 3, 62, 2, 2))
dvmrpMIBCompliance = ModuleCompliance((1, 3, 6, 1, 3, 62, 2, 1, 1)).setObjects(("DVMRP-MIB", "dvmrpGeneralGroup"), ("DVMRP-MIB", "dvmrpInterfaceGroup"), ("DVMRP-MIB", "dvmrpNeighborGroup"), ("DVMRP-MIB", "dvmrpRoutingGroup"), ("DVMRP-MIB", "dvmrpSecurityGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dvmrpMIBCompliance = dvmrpMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: dvmrpMIBCompliance.setDescription('The compliance statement for the DVMRP MIB.')
dvmrpMIBGroup = ObjectGroup((1, 3, 6, 1, 3, 62, 2, 2, 1)).setObjects(("DVMRP-MIB", "dvmrpVersionString"), ("DVMRP-MIB", "dvmrpGenerationId"), ("DVMRP-MIB", "dvmrpNumRoutes"), ("DVMRP-MIB", "dvmrpReachableRoutes"), ("DVMRP-MIB", "dvmrpInterfaceType"), ("DVMRP-MIB", "dvmrpInterfaceOperState"), ("DVMRP-MIB", "dvmrpInterfaceLocalAddress"), ("DVMRP-MIB", "dvmrpInterfaceRemoteAddress"), ("DVMRP-MIB", "dvmrpInterfaceRemoteSubnetMask"), ("DVMRP-MIB", "dvmrpInterfaceMetric"), ("DVMRP-MIB", "dvmrpInterfaceRateLimit"), ("DVMRP-MIB", "dvmrpInterfaceInPkts"), ("DVMRP-MIB", "dvmrpInterfaceOutPkts"), ("DVMRP-MIB", "dvmrpInterfaceInOctets"), ("DVMRP-MIB", "dvmrpInterfaceOutOctets"), ("DVMRP-MIB", "dvmrpInterfaceStatus"), ("DVMRP-MIB", "dvmrpNeighborUpTime"), ("DVMRP-MIB", "dvmrpNeighborExpiryTime"), ("DVMRP-MIB", "dvmrpNeighborGenerationId"), ("DVMRP-MIB", "dvmrpNeighborMajorVersion"), ("DVMRP-MIB", "dvmrpNeighborMinorVersion"), ("DVMRP-MIB", "dvmrpNeighborCapabilities"), ("DVMRP-MIB", "dvmrpRouteUpstreamNeighbor"), ("DVMRP-MIB", "dvmrpRouteIfIndex"), ("DVMRP-MIB", "dvmrpRouteMetric"), ("DVMRP-MIB", "dvmrpRouteExpiryTime"), ("DVMRP-MIB", "dvmrpRouteNextHopType"), ("DVMRP-MIB", "dvmrpAltNetStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dvmrpMIBGroup = dvmrpMIBGroup.setStatus('deprecated')
if mibBuilder.loadTexts: dvmrpMIBGroup.setDescription('A collection of objects to support management of DVMRP\n            routers.')
dvmrpGeneralGroup = ObjectGroup((1, 3, 6, 1, 3, 62, 2, 2, 2)).setObjects(("DVMRP-MIB", "dvmrpVersionString"), ("DVMRP-MIB", "dvmrpGenerationId"), ("DVMRP-MIB", "dvmrpNumRoutes"), ("DVMRP-MIB", "dvmrpReachableRoutes"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dvmrpGeneralGroup = dvmrpGeneralGroup.setStatus('current')
if mibBuilder.loadTexts: dvmrpGeneralGroup.setDescription('A collection of objects used to describe general DVMRP\n            configuration information.')
dvmrpInterfaceGroup = ObjectGroup((1, 3, 6, 1, 3, 62, 2, 2, 3)).setObjects(("DVMRP-MIB", "dvmrpInterfaceLocalAddress"), ("DVMRP-MIB", "dvmrpInterfaceMetric"), ("DVMRP-MIB", "dvmrpInterfaceStatus"), ("DVMRP-MIB", "dvmrpInterfaceRcvBadPkts"), ("DVMRP-MIB", "dvmrpInterfaceRcvBadRoutes"), ("DVMRP-MIB", "dvmrpInterfaceSentRoutes"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dvmrpInterfaceGroup = dvmrpInterfaceGroup.setStatus('current')
if mibBuilder.loadTexts: dvmrpInterfaceGroup.setDescription('A collection of objects used to describe DVMRP interface\n            configuration and statistics.')
dvmrpNeighborGroup = ObjectGroup((1, 3, 6, 1, 3, 62, 2, 2, 4)).setObjects(("DVMRP-MIB", "dvmrpNeighborUpTime"), ("DVMRP-MIB", "dvmrpNeighborExpiryTime"), ("DVMRP-MIB", "dvmrpNeighborGenerationId"), ("DVMRP-MIB", "dvmrpNeighborMajorVersion"), ("DVMRP-MIB", "dvmrpNeighborMinorVersion"), ("DVMRP-MIB", "dvmrpNeighborCapabilities"), ("DVMRP-MIB", "dvmrpNeighborRcvRoutes"), ("DVMRP-MIB", "dvmrpNeighborRcvBadPkts"), ("DVMRP-MIB", "dvmrpNeighborRcvBadRoutes"), ("DVMRP-MIB", "dvmrpNeighborState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dvmrpNeighborGroup = dvmrpNeighborGroup.setStatus('current')
if mibBuilder.loadTexts: dvmrpNeighborGroup.setDescription('A collection of objects used to describe DVMRP peer\n            configuration and statistics.')
dvmrpRoutingGroup = ObjectGroup((1, 3, 6, 1, 3, 62, 2, 2, 5)).setObjects(("DVMRP-MIB", "dvmrpRouteUpstreamNeighbor"), ("DVMRP-MIB", "dvmrpRouteIfIndex"), ("DVMRP-MIB", "dvmrpRouteMetric"), ("DVMRP-MIB", "dvmrpRouteExpiryTime"), ("DVMRP-MIB", "dvmrpRouteUpTime"), ("DVMRP-MIB", "dvmrpRouteNextHopType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dvmrpRoutingGroup = dvmrpRoutingGroup.setStatus('current')
if mibBuilder.loadTexts: dvmrpRoutingGroup.setDescription('A collection of objects used to store the DVMRP routing\n            table.')
dvmrpSecurityGroup = ObjectGroup((1, 3, 6, 1, 3, 62, 2, 2, 6)).setObjects(("DVMRP-MIB", "dvmrpInterfaceMasterKey"), ("DVMRP-MIB", "dvmrpInterfaceMasterKeyVersion"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dvmrpSecurityGroup = dvmrpSecurityGroup.setStatus('current')
if mibBuilder.loadTexts: dvmrpSecurityGroup.setDescription('A collection of objects used to store information related\n            to DVMRP security.')
mibBuilder.exportSymbols("DVMRP-MIB", PYSNMP_MODULE_ID=dvmrpMIB, dvmrpRouteIfIndex=dvmrpRouteIfIndex, dvmrpMIB=dvmrpMIB, dvmrpInterfaceType=dvmrpInterfaceType, dvmrpInterfaceRcvBadPkts=dvmrpInterfaceRcvBadPkts, dvmrpInterfaceInPkts=dvmrpInterfaceInPkts, dvmrpNeighborTable=dvmrpNeighborTable, dvmrpInterfaceMasterKey=dvmrpInterfaceMasterKey, dvmrpNeighborGenerationId=dvmrpNeighborGenerationId, dvmrpRouteMetric=dvmrpRouteMetric, dvmrpAltNetIfIndex=dvmrpAltNetIfIndex, dvmrpRoutingGroup=dvmrpRoutingGroup, dvmrpNeighborNotPruning=dvmrpNeighborNotPruning, dvmrpNeighborCapabilities=dvmrpNeighborCapabilities, dvmrpNeighborEntry=dvmrpNeighborEntry, dvmrpMIBGroup=dvmrpMIBGroup, dvmrpRouteExpiryTime=dvmrpRouteExpiryTime, dvmrpAltNetAddress=dvmrpAltNetAddress, dvmrpInterfaceOperState=dvmrpInterfaceOperState, dvmrpMIBCompliance=dvmrpMIBCompliance, dvmrpRouteSource=dvmrpRouteSource, dvmrpMIBConformance=dvmrpMIBConformance, dvmrpInterfaceOutOctets=dvmrpInterfaceOutOctets, dvmrpMIBCompliances=dvmrpMIBCompliances, dvmrpInterfaceEntry=dvmrpInterfaceEntry, dvmrpInterfaceOutPkts=dvmrpInterfaceOutPkts, dvmrpNeighborUpTime=dvmrpNeighborUpTime, dvmrpAltNetTable=dvmrpAltNetTable, dvmrpInterfaceLocalAddress=dvmrpInterfaceLocalAddress, dvmrpNeighborState=dvmrpNeighborState, dvmrpInterfaceRateLimit=dvmrpInterfaceRateLimit, dvmrpInterfaceMasterKeyVersion=dvmrpInterfaceMasterKeyVersion, dvmrpInterfaceRemoteAddress=dvmrpInterfaceRemoteAddress, dvmrpInterfaceMetric=dvmrpInterfaceMetric, dvmrpNeighborIfIndex=dvmrpNeighborIfIndex, dvmrpRouteNextHopEntry=dvmrpRouteNextHopEntry, dvmrpAltNetEntry=dvmrpAltNetEntry, dvmrpMIBGroups=dvmrpMIBGroups, dvmrpNeighborGroup=dvmrpNeighborGroup, dvmrpRouteSourceMask=dvmrpRouteSourceMask, dvmrpMIBObjects=dvmrpMIBObjects, dvmrp=dvmrp, dvmrpNeighborMinorVersion=dvmrpNeighborMinorVersion, dvmrpNumRoutes=dvmrpNumRoutes, dvmrpRouteNextHopIfIndex=dvmrpRouteNextHopIfIndex, dvmrpGeneralGroup=dvmrpGeneralGroup, dvmrpRouteNextHopSourceMask=dvmrpRouteNextHopSourceMask, dvmrpAltNetMask=dvmrpAltNetMask, dvmrpInterfaceGroup=dvmrpInterfaceGroup, dvmrpNeighborRcvBadRoutes=dvmrpNeighborRcvBadRoutes, dvmrpAltNetStatus=dvmrpAltNetStatus, dvmrpNeighborMajorVersion=dvmrpNeighborMajorVersion, dvmrpRouteUpTime=dvmrpRouteUpTime, dvmrpInterfaceStatus=dvmrpInterfaceStatus, dvmrpInterfaceRcvBadRoutes=dvmrpInterfaceRcvBadRoutes, dvmrpTraps=dvmrpTraps, dvmrpNeighborRcvBadPkts=dvmrpNeighborRcvBadPkts, dvmrpRouteNextHopType=dvmrpRouteNextHopType, dvmrpInterfaceTable=dvmrpInterfaceTable, dvmrpRouteTable=dvmrpRouteTable, dvmrpRouteUpstreamNeighbor=dvmrpRouteUpstreamNeighbor, dvmrpReachableRoutes=dvmrpReachableRoutes, dvmrpInterfaceIfIndex=dvmrpInterfaceIfIndex, dvmrpSecurityGroup=dvmrpSecurityGroup, dvmrpInterfaceRemoteSubnetMask=dvmrpInterfaceRemoteSubnetMask, dvmrpNeighborLoss=dvmrpNeighborLoss, dvmrpRouteNextHopTable=dvmrpRouteNextHopTable, dvmrpGenerationId=dvmrpGenerationId, dvmrpNeighborAddress=dvmrpNeighborAddress, dvmrpRouteNextHopSource=dvmrpRouteNextHopSource, dvmrpVersionString=dvmrpVersionString, dvmrpNeighborRcvRoutes=dvmrpNeighborRcvRoutes, dvmrpInterfaceSentRoutes=dvmrpInterfaceSentRoutes, dvmrpRouteEntry=dvmrpRouteEntry, dvmrpInterfaceInOctets=dvmrpInterfaceInOctets, dvmrpNeighborExpiryTime=dvmrpNeighborExpiryTime)
