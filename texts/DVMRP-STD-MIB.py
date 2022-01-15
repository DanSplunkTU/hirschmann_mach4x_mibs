#
# PySNMP MIB module DVMRP-STD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/DVMRP-STD-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 17:49:46 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
InterfaceIndex, InterfaceIndexOrZero = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "InterfaceIndexOrZero")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
iso, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ObjectIdentity, Integer32, experimental, Gauge32, IpAddress, Bits, Unsigned32, Counter32, MibIdentifier, ModuleIdentity, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ObjectIdentity", "Integer32", "experimental", "Gauge32", "IpAddress", "Bits", "Unsigned32", "Counter32", "MibIdentifier", "ModuleIdentity", "NotificationType")
TextualConvention, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "RowStatus")
dvmrpStdMIB = ModuleIdentity((1, 3, 6, 1, 3, 62))
dvmrpStdMIB.setRevisions(('2001-11-21 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: dvmrpStdMIB.setRevisionsDescriptions(('Initial version, published as RFC xxxx (to be filled in by\n            RFC-Editor).',))
if mibBuilder.loadTexts: dvmrpStdMIB.setLastUpdated('200111211200Z')
if mibBuilder.loadTexts: dvmrpStdMIB.setOrganization('IETF IDMR Working Group.')
if mibBuilder.loadTexts: dvmrpStdMIB.setContactInfo(' Dave Thaler\n              Microsoft\n              One Microsoft Way\n              Redmond, WA 98052-6399\n              EMail: dthaler@microsoft.com')
if mibBuilder.loadTexts: dvmrpStdMIB.setDescription('The MIB module for management of DVMRP routers.')
dvmrpMIBObjects = MibIdentifier((1, 3, 6, 1, 3, 62, 1))
dvmrp = MibIdentifier((1, 3, 6, 1, 3, 62, 1, 1))
dvmrpScalar = MibIdentifier((1, 3, 6, 1, 3, 62, 1, 1, 1))
dvmrpVersionString = MibScalar((1, 3, 6, 1, 3, 62, 1, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpVersionString.setStatus('current')
if mibBuilder.loadTexts: dvmrpVersionString.setDescription("The router's DVMRP version information.  Similar to\n            sysDescr in MIB-II, this is a free-form field which can be\n            used to display vendor-specific information.")
dvmrpNumRoutes = MibScalar((1, 3, 6, 1, 3, 62, 1, 1, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpNumRoutes.setStatus('current')
if mibBuilder.loadTexts: dvmrpNumRoutes.setDescription('The number of entries in the routing table.  This can be\n            used to monitor the routing table size.')
dvmrpReachableRoutes = MibScalar((1, 3, 6, 1, 3, 62, 1, 1, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpReachableRoutes.setStatus('current')
if mibBuilder.loadTexts: dvmrpReachableRoutes.setDescription('The number of entries in the routing table with non\n            infinite metrics.  This can be used to detect network\n            partitions by observing the ratio of reachable routes to\n            total routes.')
dvmrpInterfaceTable = MibTable((1, 3, 6, 1, 3, 62, 1, 1, 2), )
if mibBuilder.loadTexts: dvmrpInterfaceTable.setStatus('current')
if mibBuilder.loadTexts: dvmrpInterfaceTable.setDescription("The (conceptual) table listing the router's multicast-\n            capable interfaces.")
dvmrpInterfaceEntry = MibTableRow((1, 3, 6, 1, 3, 62, 1, 1, 2, 1), ).setIndexNames((0, "DVMRP-STD-MIB", "dvmrpInterfaceIndex"))
if mibBuilder.loadTexts: dvmrpInterfaceEntry.setStatus('current')
if mibBuilder.loadTexts: dvmrpInterfaceEntry.setDescription('An entry (conceptual row) in the dvmrpInterfaceTable.  This\n            row augments ipMRouteInterfaceEntry in the IP Multicast MIB,\n            where the threshold object resides.')
dvmrpInterfaceIndex = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: dvmrpInterfaceIndex.setStatus('current')
if mibBuilder.loadTexts: dvmrpInterfaceIndex.setDescription('The ifIndex value of the interface for which DVMRP is\n            enabled.')
dvmrpInterfaceLocalAddress = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 2, 1, 2), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dvmrpInterfaceLocalAddress.setStatus('current')
if mibBuilder.loadTexts: dvmrpInterfaceLocalAddress.setDescription('The IP address this system will use as a source address on\n            this interface.  On unnumbered interfaces, it must be the\n            same value as dvmrpInterfaceLocalAddress for some interface\n            on the system.')
dvmrpInterfaceMetric = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 31)).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dvmrpInterfaceMetric.setStatus('current')
if mibBuilder.loadTexts: dvmrpInterfaceMetric.setDescription('The distance metric for this interface which is used to\n            calculate distance vectors.')
dvmrpInterfaceStatus = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 2, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dvmrpInterfaceStatus.setStatus('current')
if mibBuilder.loadTexts: dvmrpInterfaceStatus.setDescription('The status of this entry.  Creating the entry enables DVMRP\n            on the virtual interface; destroying the entry or setting it\n            to notInService disables DVMRP on the virtual interface.')
dvmrpInterfaceRcvBadPkts = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpInterfaceRcvBadPkts.setStatus('current')
if mibBuilder.loadTexts: dvmrpInterfaceRcvBadPkts.setDescription('The number of DVMRP messages received on the interface by\n            the DVMRP process which were subsequently discarded as\n            invalid (e.g. invalid packet format, or a route report from\n            an unknown neighbor).')
dvmrpInterfaceRcvBadRoutes = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpInterfaceRcvBadRoutes.setStatus('current')
if mibBuilder.loadTexts: dvmrpInterfaceRcvBadRoutes.setDescription('The number of routes, in valid DVMRP packets, which were\n            ignored because the entry was invalid.')
dvmrpInterfaceSentRoutes = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpInterfaceSentRoutes.setStatus('current')
if mibBuilder.loadTexts: dvmrpInterfaceSentRoutes.setDescription('The number of routes, in DVMRP Report packets, which have\n            been sent on this interface.  Together with\n            dvmrpNeighborRcvRoutes at a peer, this object is useful for\n            detecting routes being lost.')
dvmrpInterfaceKey = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 2, 1, 8), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dvmrpInterfaceKey.setStatus('current')
if mibBuilder.loadTexts: dvmrpInterfaceKey.setDescription('The (shared) key for authenticating neighbors on this\n            interface.  This object is intended solely for the purpose\n            of setting the interface key, and MUST be accessible only\n            via requests using both authentication and privacy.  The\n            agent MAY report an empty string in response to get, get-\n            next, get-bulk requests.')
dvmrpInterfaceKeyVersion = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 2, 1, 9), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dvmrpInterfaceKeyVersion.setStatus('current')
if mibBuilder.loadTexts: dvmrpInterfaceKeyVersion.setDescription('The highest version number of all known interface keys for\n            this interface used for authenticating neighbors.')
dvmrpInterfaceGenerationId = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 2, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpInterfaceGenerationId.setStatus('current')
if mibBuilder.loadTexts: dvmrpInterfaceGenerationId.setDescription('The generation identifier for the interface.  This is used\n            by neighboring routers to detect whether the DVMRP routing\n            table should be resent.')
dvmrpNeighborTable = MibTable((1, 3, 6, 1, 3, 62, 1, 1, 3), )
if mibBuilder.loadTexts: dvmrpNeighborTable.setStatus('current')
if mibBuilder.loadTexts: dvmrpNeighborTable.setDescription("The (conceptual) table listing the router's DVMRP\n            neighbors, as discovered by receiving DVMRP messages.")
dvmrpNeighborEntry = MibTableRow((1, 3, 6, 1, 3, 62, 1, 1, 3, 1), ).setIndexNames((0, "DVMRP-STD-MIB", "dvmrpNeighborIfIndex"), (0, "DVMRP-STD-MIB", "dvmrpNeighborAddress"))
if mibBuilder.loadTexts: dvmrpNeighborEntry.setStatus('current')
if mibBuilder.loadTexts: dvmrpNeighborEntry.setDescription('An entry (conceptual row) in the dvmrpNeighborTable.')
dvmrpNeighborIfIndex = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 3, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: dvmrpNeighborIfIndex.setStatus('current')
if mibBuilder.loadTexts: dvmrpNeighborIfIndex.setDescription('The value of ifIndex for the virtual interface used to\n            reach this DVMRP neighbor.')
dvmrpNeighborAddress = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 3, 1, 2), IpAddress())
if mibBuilder.loadTexts: dvmrpNeighborAddress.setStatus('current')
if mibBuilder.loadTexts: dvmrpNeighborAddress.setDescription('The IP address of the DVMRP neighbor for which this entry\n            contains information.')
dvmrpNeighborUpTime = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 3, 1, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpNeighborUpTime.setStatus('current')
if mibBuilder.loadTexts: dvmrpNeighborUpTime.setDescription('The time since this DVMRP neighbor (last) became a neighbor\n            of the local router.')
dvmrpNeighborExpiryTime = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 3, 1, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpNeighborExpiryTime.setStatus('current')
if mibBuilder.loadTexts: dvmrpNeighborExpiryTime.setDescription('The minimum time remaining before this DVMRP neighbor will\n            be aged out.')
dvmrpNeighborGenerationId = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 3, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpNeighborGenerationId.setStatus('current')
if mibBuilder.loadTexts: dvmrpNeighborGenerationId.setDescription("The neighboring router's generation identifier.")
dvmrpNeighborMajorVersion = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 3, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpNeighborMajorVersion.setStatus('current')
if mibBuilder.loadTexts: dvmrpNeighborMajorVersion.setDescription("The neighboring router's major DVMRP version number.")
dvmrpNeighborMinorVersion = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 3, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpNeighborMinorVersion.setStatus('current')
if mibBuilder.loadTexts: dvmrpNeighborMinorVersion.setDescription("The neighboring router's minor DVMRP version number.")
dvmrpNeighborCapabilities = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 3, 1, 8), Bits().clone(namedValues=NamedValues(("leaf", 0), ("prune", 1), ("generationID", 2), ("mtrace", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpNeighborCapabilities.setStatus('current')
if mibBuilder.loadTexts: dvmrpNeighborCapabilities.setDescription("This object describes the neighboring router's\n            capabilities.  The leaf bit indicates that the neighbor has\n            only one interface with neighbors.  The prune bit indicates\n            that the neighbor supports pruning.  The generationID bit\n            indicates that the neighbor sends its generationID in Probe\n            messages.  The mtrace bit indicates that the neighbor can\n            handle mtrace requests.")
dvmrpNeighborRcvRoutes = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 3, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpNeighborRcvRoutes.setStatus('current')
if mibBuilder.loadTexts: dvmrpNeighborRcvRoutes.setDescription('The total number of routes received in valid DVMRP packets\n            received from this neighbor.  This can be used to diagnose\n            problems such as unicast route injection, as well as giving\n            an indication of the level of DVMRP route exchange\n            activity.')
dvmrpNeighborRcvBadPkts = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 3, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpNeighborRcvBadPkts.setStatus('current')
if mibBuilder.loadTexts: dvmrpNeighborRcvBadPkts.setDescription('The number of packet received from this neighbor which were\n            discarded as invalid.')
dvmrpNeighborRcvBadRoutes = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 3, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpNeighborRcvBadRoutes.setStatus('current')
if mibBuilder.loadTexts: dvmrpNeighborRcvBadRoutes.setDescription('The number of routes, in valid DVMRP packets received from\n            this neighbor, which were ignored because the entry was\n            invalid.')
dvmrpNeighborState = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 3, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("oneway", 1), ("active", 2), ("ignoring", 3), ("down", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpNeighborState.setStatus('current')
if mibBuilder.loadTexts: dvmrpNeighborState.setDescription('State of the neighbor adjacency.')
dvmrpRouteTable = MibTable((1, 3, 6, 1, 3, 62, 1, 1, 4), )
if mibBuilder.loadTexts: dvmrpRouteTable.setStatus('current')
if mibBuilder.loadTexts: dvmrpRouteTable.setDescription('The table of routes learned through DVMRP route exchange.')
dvmrpRouteEntry = MibTableRow((1, 3, 6, 1, 3, 62, 1, 1, 4, 1), ).setIndexNames((0, "DVMRP-STD-MIB", "dvmrpRouteSource"), (0, "DVMRP-STD-MIB", "dvmrpRouteSourceMask"))
if mibBuilder.loadTexts: dvmrpRouteEntry.setStatus('current')
if mibBuilder.loadTexts: dvmrpRouteEntry.setDescription('An entry (conceptual row) containing the multicast routing\n            information used by DVMRP in place of the unicast routing\n            information.')
dvmrpRouteSource = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 4, 1, 1), IpAddress())
if mibBuilder.loadTexts: dvmrpRouteSource.setStatus('current')
if mibBuilder.loadTexts: dvmrpRouteSource.setDescription('The network address which when combined with the\n            corresponding value of dvmrpRouteSourceMask identifies the\n            sources for which this entry contains multicast routing\n            information.')
dvmrpRouteSourceMask = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 4, 1, 2), IpAddress())
if mibBuilder.loadTexts: dvmrpRouteSourceMask.setStatus('current')
if mibBuilder.loadTexts: dvmrpRouteSourceMask.setDescription('The network mask which when combined with the corresponding\n            value of dvmrpRouteSource identifies the sources for which\n            this entry contains multicast routing information.')
dvmrpRouteUpstreamNeighbor = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 4, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpRouteUpstreamNeighbor.setStatus('current')
if mibBuilder.loadTexts: dvmrpRouteUpstreamNeighbor.setDescription('The address of the upstream neighbor (e.g., RPF neighbor)\n            from which IP datagrams from these sources are received.')
dvmrpRouteIfIndex = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 4, 1, 4), InterfaceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpRouteIfIndex.setStatus('current')
if mibBuilder.loadTexts: dvmrpRouteIfIndex.setDescription('The value of ifIndex for the interface on which IP\n            datagrams sent by these sources are received.  A value of 0\n            typically means the route is an aggregate for which no next-\n            hop interface exists.')
dvmrpRouteMetric = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 4, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpRouteMetric.setStatus('current')
if mibBuilder.loadTexts: dvmrpRouteMetric.setDescription('The distance in hops to the source subnet.')
dvmrpRouteExpiryTime = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 4, 1, 6), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpRouteExpiryTime.setStatus('current')
if mibBuilder.loadTexts: dvmrpRouteExpiryTime.setDescription('The minimum amount of time remaining before this entry will\n            be aged out.')
dvmrpRouteUpTime = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 4, 1, 7), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpRouteUpTime.setStatus('current')
if mibBuilder.loadTexts: dvmrpRouteUpTime.setDescription('The time since the route represented by this entry was\n            learned by the router.')
dvmrpRouteNextHopTable = MibTable((1, 3, 6, 1, 3, 62, 1, 1, 5), )
if mibBuilder.loadTexts: dvmrpRouteNextHopTable.setStatus('current')
if mibBuilder.loadTexts: dvmrpRouteNextHopTable.setDescription('The (conceptual) table containing information on the next\n            hops on outgoing interfaces for routing IP multicast\n            datagrams.')
dvmrpRouteNextHopEntry = MibTableRow((1, 3, 6, 1, 3, 62, 1, 1, 5, 1), ).setIndexNames((0, "DVMRP-STD-MIB", "dvmrpRouteNextHopSource"), (0, "DVMRP-STD-MIB", "dvmrpRouteNextHopSourceMask"), (0, "DVMRP-STD-MIB", "dvmrpRouteNextHopIfIndex"))
if mibBuilder.loadTexts: dvmrpRouteNextHopEntry.setStatus('current')
if mibBuilder.loadTexts: dvmrpRouteNextHopEntry.setDescription('An entry (conceptual row) in the list of next hops on\n            outgoing interfaces to which IP multicast datagrams from\n            particular sources are routed.')
dvmrpRouteNextHopSource = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 5, 1, 1), IpAddress())
if mibBuilder.loadTexts: dvmrpRouteNextHopSource.setStatus('current')
if mibBuilder.loadTexts: dvmrpRouteNextHopSource.setDescription('The network address which when combined with the\n            corresponding value of dvmrpRouteNextHopSourceMask\n            identifies the sources for which this entry specifies a next\n            hop on an outgoing interface.')
dvmrpRouteNextHopSourceMask = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 5, 1, 2), IpAddress())
if mibBuilder.loadTexts: dvmrpRouteNextHopSourceMask.setStatus('current')
if mibBuilder.loadTexts: dvmrpRouteNextHopSourceMask.setDescription('The network mask which when combined with the corresponding\n            value of dvmrpRouteNextHopSource identifies the sources for\n            which this entry specifies a next hop on an outgoing\n            interface.')
dvmrpRouteNextHopIfIndex = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 5, 1, 3), InterfaceIndex())
if mibBuilder.loadTexts: dvmrpRouteNextHopIfIndex.setStatus('current')
if mibBuilder.loadTexts: dvmrpRouteNextHopIfIndex.setDescription('The ifIndex value of the interface for the outgoing\n            interface for this next hop.')
dvmrpRouteNextHopType = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 5, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("leaf", 1), ("branch", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpRouteNextHopType.setStatus('current')
if mibBuilder.loadTexts: dvmrpRouteNextHopType.setDescription('Type is leaf if no downstream dependent neighbors exist on\n            the outgoing virtual interface.  Otherwise, type is branch.')
dvmrpPruneTable = MibTable((1, 3, 6, 1, 3, 62, 1, 1, 6), )
if mibBuilder.loadTexts: dvmrpPruneTable.setStatus('current')
if mibBuilder.loadTexts: dvmrpPruneTable.setDescription("The (conceptual) table listing the router's upstream prune\n            state.")
dvmrpPruneEntry = MibTableRow((1, 3, 6, 1, 3, 62, 1, 1, 6, 1), ).setIndexNames((0, "DVMRP-STD-MIB", "dvmrpPruneGroup"), (0, "DVMRP-STD-MIB", "dvmrpPruneSource"), (0, "DVMRP-STD-MIB", "dvmrpPruneSourceMask"))
if mibBuilder.loadTexts: dvmrpPruneEntry.setStatus('current')
if mibBuilder.loadTexts: dvmrpPruneEntry.setDescription('An entry (conceptual row) in the dvmrpPruneTable.')
dvmrpPruneGroup = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 6, 1, 1), IpAddress())
if mibBuilder.loadTexts: dvmrpPruneGroup.setStatus('current')
if mibBuilder.loadTexts: dvmrpPruneGroup.setDescription('The group address which has been pruned.')
dvmrpPruneSource = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 6, 1, 2), IpAddress())
if mibBuilder.loadTexts: dvmrpPruneSource.setStatus('current')
if mibBuilder.loadTexts: dvmrpPruneSource.setDescription('The address of the source or source network which has been\n            pruned.')
dvmrpPruneSourceMask = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 6, 1, 3), IpAddress())
if mibBuilder.loadTexts: dvmrpPruneSourceMask.setStatus('current')
if mibBuilder.loadTexts: dvmrpPruneSourceMask.setDescription("The address of the source or source network which has been\n            pruned.  The mask must either be all 1's, or else\n            dvmrpPruneSource and dvmrpPruneSourceMask must match\n            dvmrpRouteSource and dvmrpRouteSourceMask for some entry in\n            the dvmrpRouteTable.")
dvmrpPruneExpiryTime = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 6, 1, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpPruneExpiryTime.setStatus('current')
if mibBuilder.loadTexts: dvmrpPruneExpiryTime.setDescription("The amount of time remaining before this prune should\n            expire at the upstream neighbor.  This value should be the\n            minimum of the default prune lifetime and the remaining\n            prune lifetimes of the local router's downstream neighbors,\n            if any.")
dvmrpTraps = MibIdentifier((1, 3, 6, 1, 3, 62, 1, 1, 7))
dvmrpNeighborLoss = NotificationType((1, 3, 6, 1, 3, 62, 1, 1, 7, 1)).setObjects(("DVMRP-STD-MIB", "dvmrpInterfaceLocalAddress"), ("DVMRP-STD-MIB", "dvmrpNeighborState"))
if mibBuilder.loadTexts: dvmrpNeighborLoss.setStatus('current')
if mibBuilder.loadTexts: dvmrpNeighborLoss.setDescription('A dvmrpNeighborLoss trap signifies the loss of a 2-way\n            adjacency with a neighbor.  This trap should be generated\n            when the neighbor state changes from active to one-way,\n            ignoring, or down.  The trap should be generated only if the\n            router has no other neighbors on the same interface with a\n            lower IP address than itself.')
dvmrpNeighborNotPruning = NotificationType((1, 3, 6, 1, 3, 62, 1, 1, 7, 2)).setObjects(("DVMRP-STD-MIB", "dvmrpInterfaceLocalAddress"), ("DVMRP-STD-MIB", "dvmrpNeighborCapabilities"))
if mibBuilder.loadTexts: dvmrpNeighborNotPruning.setStatus('current')
if mibBuilder.loadTexts: dvmrpNeighborNotPruning.setDescription('A dvmrpNeighborNotPruning trap signifies that a non-pruning\n            neighbor has been detected (in an implementation-dependent\n            manner).  This trap should be generated at most once per\n            generation ID of the neighbor.  For example, it should be\n            generated at the time a neighbor is first heard from if the\n            prune bit is not set in its capabilities.  It should also be\n            generated if the local system has the ability to tell that a\n            neighbor which sets the the prune bit in its capabilities is\n            not pruning any branches over an extended period of time.\n            The trap should be generated only if the router has no other\n            neighbors on the same interface with a lower IP address than\n            itself.')
dvmrpMIBConformance = MibIdentifier((1, 3, 6, 1, 3, 62, 2))
dvmrpMIBCompliances = MibIdentifier((1, 3, 6, 1, 3, 62, 2, 1))
dvmrpMIBGroups = MibIdentifier((1, 3, 6, 1, 3, 62, 2, 2))
dvmrpMIBCompliance = ModuleCompliance((1, 3, 6, 1, 3, 62, 2, 1, 1)).setObjects(("DVMRP-STD-MIB", "dvmrpGeneralGroup"), ("DVMRP-STD-MIB", "dvmrpInterfaceGroup"), ("DVMRP-STD-MIB", "dvmrpNeighborGroup"), ("DVMRP-STD-MIB", "dvmrpRoutingGroup"), ("DVMRP-STD-MIB", "dvmrpTreeGroup"), ("DVMRP-STD-MIB", "dvmrpSecurityGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dvmrpMIBCompliance = dvmrpMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: dvmrpMIBCompliance.setDescription('The compliance statement for the DVMRP MIB.')
dvmrpGeneralGroup = ObjectGroup((1, 3, 6, 1, 3, 62, 2, 2, 2)).setObjects(("DVMRP-STD-MIB", "dvmrpVersionString"), ("DVMRP-STD-MIB", "dvmrpNumRoutes"), ("DVMRP-STD-MIB", "dvmrpReachableRoutes"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dvmrpGeneralGroup = dvmrpGeneralGroup.setStatus('current')
if mibBuilder.loadTexts: dvmrpGeneralGroup.setDescription('A collection of objects used to describe general DVMRP\n            configuration information.')
dvmrpInterfaceGroup = ObjectGroup((1, 3, 6, 1, 3, 62, 2, 2, 3)).setObjects(("DVMRP-STD-MIB", "dvmrpInterfaceLocalAddress"), ("DVMRP-STD-MIB", "dvmrpInterfaceMetric"), ("DVMRP-STD-MIB", "dvmrpInterfaceStatus"), ("DVMRP-STD-MIB", "dvmrpInterfaceGenerationId"), ("DVMRP-STD-MIB", "dvmrpInterfaceRcvBadPkts"), ("DVMRP-STD-MIB", "dvmrpInterfaceRcvBadRoutes"), ("DVMRP-STD-MIB", "dvmrpInterfaceSentRoutes"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dvmrpInterfaceGroup = dvmrpInterfaceGroup.setStatus('current')
if mibBuilder.loadTexts: dvmrpInterfaceGroup.setDescription('A collection of objects used to describe DVMRP interface\n            configuration and statistics.')
dvmrpNeighborGroup = ObjectGroup((1, 3, 6, 1, 3, 62, 2, 2, 4)).setObjects(("DVMRP-STD-MIB", "dvmrpNeighborUpTime"), ("DVMRP-STD-MIB", "dvmrpNeighborExpiryTime"), ("DVMRP-STD-MIB", "dvmrpNeighborGenerationId"), ("DVMRP-STD-MIB", "dvmrpNeighborMajorVersion"), ("DVMRP-STD-MIB", "dvmrpNeighborMinorVersion"), ("DVMRP-STD-MIB", "dvmrpNeighborCapabilities"), ("DVMRP-STD-MIB", "dvmrpNeighborRcvRoutes"), ("DVMRP-STD-MIB", "dvmrpNeighborRcvBadPkts"), ("DVMRP-STD-MIB", "dvmrpNeighborRcvBadRoutes"), ("DVMRP-STD-MIB", "dvmrpNeighborState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dvmrpNeighborGroup = dvmrpNeighborGroup.setStatus('current')
if mibBuilder.loadTexts: dvmrpNeighborGroup.setDescription('A collection of objects used to describe DVMRP peer\n            configuration and statistics.')
dvmrpRoutingGroup = ObjectGroup((1, 3, 6, 1, 3, 62, 2, 2, 5)).setObjects(("DVMRP-STD-MIB", "dvmrpRouteUpstreamNeighbor"), ("DVMRP-STD-MIB", "dvmrpRouteIfIndex"), ("DVMRP-STD-MIB", "dvmrpRouteMetric"), ("DVMRP-STD-MIB", "dvmrpRouteExpiryTime"), ("DVMRP-STD-MIB", "dvmrpRouteUpTime"), ("DVMRP-STD-MIB", "dvmrpRouteNextHopType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dvmrpRoutingGroup = dvmrpRoutingGroup.setStatus('current')
if mibBuilder.loadTexts: dvmrpRoutingGroup.setDescription('A collection of objects used to store the DVMRP routing\n            table.')
dvmrpSecurityGroup = ObjectGroup((1, 3, 6, 1, 3, 62, 2, 2, 6)).setObjects(("DVMRP-STD-MIB", "dvmrpInterfaceKey"), ("DVMRP-STD-MIB", "dvmrpInterfaceKeyVersion"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dvmrpSecurityGroup = dvmrpSecurityGroup.setStatus('current')
if mibBuilder.loadTexts: dvmrpSecurityGroup.setDescription('A collection of objects used to store information related\n            to DVMRP security.')
dvmrpTreeGroup = ObjectGroup((1, 3, 6, 1, 3, 62, 2, 2, 7)).setObjects(("DVMRP-STD-MIB", "dvmrpPruneExpiryTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dvmrpTreeGroup = dvmrpTreeGroup.setStatus('current')
if mibBuilder.loadTexts: dvmrpTreeGroup.setDescription('A collection of objects used to store information related\n            to DVMRP prune state.')
dvmrpNotificationGroup = NotificationGroup((1, 3, 6, 1, 3, 62, 2, 2, 8)).setObjects(("DVMRP-STD-MIB", "dvmrpNeighborLoss"), ("DVMRP-STD-MIB", "dvmrpNeighborNotPruning"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dvmrpNotificationGroup = dvmrpNotificationGroup.setStatus('current')
if mibBuilder.loadTexts: dvmrpNotificationGroup.setDescription('A collection of notifications for signaling important DVMRP\n            events.')
mibBuilder.exportSymbols("DVMRP-STD-MIB", dvmrpInterfaceKey=dvmrpInterfaceKey, dvmrpRouteUpTime=dvmrpRouteUpTime, dvmrpInterfaceIndex=dvmrpInterfaceIndex, dvmrpRoutingGroup=dvmrpRoutingGroup, dvmrpTraps=dvmrpTraps, dvmrpNeighborGroup=dvmrpNeighborGroup, dvmrpInterfaceMetric=dvmrpInterfaceMetric, dvmrpNeighborLoss=dvmrpNeighborLoss, dvmrpNotificationGroup=dvmrpNotificationGroup, dvmrpRouteNextHopIfIndex=dvmrpRouteNextHopIfIndex, dvmrpNeighborNotPruning=dvmrpNeighborNotPruning, dvmrpNeighborState=dvmrpNeighborState, dvmrpInterfaceGenerationId=dvmrpInterfaceGenerationId, dvmrpInterfaceGroup=dvmrpInterfaceGroup, dvmrpScalar=dvmrpScalar, dvmrpNeighborTable=dvmrpNeighborTable, dvmrpInterfaceLocalAddress=dvmrpInterfaceLocalAddress, dvmrpInterfaceSentRoutes=dvmrpInterfaceSentRoutes, dvmrpRouteMetric=dvmrpRouteMetric, dvmrpNeighborEntry=dvmrpNeighborEntry, dvmrpInterfaceTable=dvmrpInterfaceTable, dvmrpMIBObjects=dvmrpMIBObjects, dvmrpPruneTable=dvmrpPruneTable, dvmrpRouteSourceMask=dvmrpRouteSourceMask, dvmrpNeighborAddress=dvmrpNeighborAddress, dvmrpRouteIfIndex=dvmrpRouteIfIndex, dvmrpRouteNextHopSource=dvmrpRouteNextHopSource, dvmrpSecurityGroup=dvmrpSecurityGroup, dvmrpNeighborUpTime=dvmrpNeighborUpTime, dvmrpPruneExpiryTime=dvmrpPruneExpiryTime, dvmrpRouteNextHopSourceMask=dvmrpRouteNextHopSourceMask, dvmrpNeighborRcvRoutes=dvmrpNeighborRcvRoutes, dvmrpStdMIB=dvmrpStdMIB, dvmrpNeighborIfIndex=dvmrpNeighborIfIndex, dvmrpRouteEntry=dvmrpRouteEntry, dvmrpPruneSourceMask=dvmrpPruneSourceMask, dvmrpMIBCompliances=dvmrpMIBCompliances, dvmrpVersionString=dvmrpVersionString, dvmrpReachableRoutes=dvmrpReachableRoutes, dvmrpInterfaceRcvBadRoutes=dvmrpInterfaceRcvBadRoutes, dvmrpMIBGroups=dvmrpMIBGroups, dvmrpNeighborCapabilities=dvmrpNeighborCapabilities, dvmrpInterfaceStatus=dvmrpInterfaceStatus, dvmrpMIBConformance=dvmrpMIBConformance, dvmrpPruneGroup=dvmrpPruneGroup, dvmrpPruneEntry=dvmrpPruneEntry, dvmrpRouteNextHopType=dvmrpRouteNextHopType, dvmrpNeighborRcvBadPkts=dvmrpNeighborRcvBadPkts, dvmrpPruneSource=dvmrpPruneSource, dvmrp=dvmrp, dvmrpInterfaceRcvBadPkts=dvmrpInterfaceRcvBadPkts, dvmrpNeighborMajorVersion=dvmrpNeighborMajorVersion, dvmrpRouteNextHopEntry=dvmrpRouteNextHopEntry, dvmrpInterfaceKeyVersion=dvmrpInterfaceKeyVersion, dvmrpRouteSource=dvmrpRouteSource, PYSNMP_MODULE_ID=dvmrpStdMIB, dvmrpNeighborRcvBadRoutes=dvmrpNeighborRcvBadRoutes, dvmrpNumRoutes=dvmrpNumRoutes, dvmrpInterfaceEntry=dvmrpInterfaceEntry, dvmrpNeighborExpiryTime=dvmrpNeighborExpiryTime, dvmrpGeneralGroup=dvmrpGeneralGroup, dvmrpRouteTable=dvmrpRouteTable, dvmrpTreeGroup=dvmrpTreeGroup, dvmrpNeighborGenerationId=dvmrpNeighborGenerationId, dvmrpRouteNextHopTable=dvmrpRouteNextHopTable, dvmrpRouteUpstreamNeighbor=dvmrpRouteUpstreamNeighbor, dvmrpRouteExpiryTime=dvmrpRouteExpiryTime, dvmrpNeighborMinorVersion=dvmrpNeighborMinorVersion, dvmrpMIBCompliance=dvmrpMIBCompliance)
