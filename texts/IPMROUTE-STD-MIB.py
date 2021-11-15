#
# PySNMP MIB module IPMROUTE-STD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/IPMROUTE-STD-MIB
# Produced by pysmi-1.1.0 at Mon Nov 15 18:46:27 2021
# On host fv-az77-248 platform Linux version 5.11.0-1020-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
IANAipRouteProtocol, IANAipMRouteProtocol = mibBuilder.importSymbols("IANA-RTPROTO-MIB", "IANAipRouteProtocol", "IANAipMRouteProtocol")
InterfaceIndex, InterfaceIndexOrZero = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "InterfaceIndexOrZero")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
TimeTicks, NotificationType, Unsigned32, mib_2, IpAddress, Integer32, iso, Counter32, ModuleIdentity, ObjectIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "NotificationType", "Unsigned32", "mib-2", "IpAddress", "Integer32", "iso", "Counter32", "ModuleIdentity", "ObjectIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter64", "Gauge32")
TruthValue, DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention", "RowStatus")
ipMRouteStdMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 83))
ipMRouteStdMIB.setRevisions(('2000-09-22 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ipMRouteStdMIB.setRevisionsDescriptions(('Initial version, published as RFC 2932.',))
if mibBuilder.loadTexts: ipMRouteStdMIB.setLastUpdated('200009220000Z')
if mibBuilder.loadTexts: ipMRouteStdMIB.setOrganization('IETF IDMR Working Group')
if mibBuilder.loadTexts: ipMRouteStdMIB.setContactInfo(' Dave Thaler\n              Microsoft Corporation\n              One Microsoft Way\n              Redmond, WA  98052-6399\n              US\n\n              Phone: +1 425 703 8835\n              EMail: dthaler@microsoft.com')
if mibBuilder.loadTexts: ipMRouteStdMIB.setDescription('The MIB module for management of IP Multicast routing, but\n            independent of the specific multicast routing protocol in\n            use.')
class LanguageTag(TextualConvention, OctetString):
    description = 'An RFC 1766-style language tag, with all alphabetic\n            characters converted to lowercase.  This restriction is\n            intended to make the lexical ordering imposed by SNMP useful\n            when applied to language tags.  Note that it is\n            theoretically possible for a valid language tag to exceed\n            the allowed length of this syntax, and thus be impossible to\n            represent with this syntax.  Sampling of language tags in\n            current use on the Internet suggests that this limit does\n            not pose a serious problem in practice.'
    status = 'current'
    displayHint = '100a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 100)

ipMRouteMIBObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 83, 1))
ipMRoute = MibIdentifier((1, 3, 6, 1, 2, 1, 83, 1, 1))
ipMRouteEnable = MibScalar((1, 3, 6, 1, 2, 1, 83, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipMRouteEnable.setStatus('current')
if mibBuilder.loadTexts: ipMRouteEnable.setDescription('The enabled status of IP Multicast routing on this router.')
ipMRouteEntryCount = MibScalar((1, 3, 6, 1, 2, 1, 83, 1, 1, 7), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipMRouteEntryCount.setStatus('current')
if mibBuilder.loadTexts: ipMRouteEntryCount.setDescription('The number of rows in the ipMRouteTable.  This can be used\n            to monitor the multicast routing table size.')
ipMRouteTable = MibTable((1, 3, 6, 1, 2, 1, 83, 1, 1, 2), )
if mibBuilder.loadTexts: ipMRouteTable.setStatus('current')
if mibBuilder.loadTexts: ipMRouteTable.setDescription('The (conceptual) table containing multicast routing\n            information for IP datagrams sent by particular sources to\n            the IP multicast groups known to this router.')
ipMRouteEntry = MibTableRow((1, 3, 6, 1, 2, 1, 83, 1, 1, 2, 1), ).setIndexNames((0, "IPMROUTE-STD-MIB", "ipMRouteGroup"), (0, "IPMROUTE-STD-MIB", "ipMRouteSource"), (0, "IPMROUTE-STD-MIB", "ipMRouteSourceMask"))
if mibBuilder.loadTexts: ipMRouteEntry.setStatus('current')
if mibBuilder.loadTexts: ipMRouteEntry.setDescription('An entry (conceptual row) containing the multicast routing\n            information for IP datagrams from a particular source and\n            addressed to a particular IP multicast group address.\n            Discontinuities in counters in this entry can be detected by\n            observing the value of ipMRouteUpTime.')
ipMRouteGroup = MibTableColumn((1, 3, 6, 1, 2, 1, 83, 1, 1, 2, 1, 1), IpAddress())
if mibBuilder.loadTexts: ipMRouteGroup.setStatus('current')
if mibBuilder.loadTexts: ipMRouteGroup.setDescription('The IP multicast group address for which this entry\n            contains multicast routing information.')
ipMRouteSource = MibTableColumn((1, 3, 6, 1, 2, 1, 83, 1, 1, 2, 1, 2), IpAddress())
if mibBuilder.loadTexts: ipMRouteSource.setStatus('current')
if mibBuilder.loadTexts: ipMRouteSource.setDescription('The network address which when combined with the\n            corresponding value of ipMRouteSourceMask identifies the\n            sources for which this entry contains multicast routing\n            information.')
ipMRouteSourceMask = MibTableColumn((1, 3, 6, 1, 2, 1, 83, 1, 1, 2, 1, 3), IpAddress())
if mibBuilder.loadTexts: ipMRouteSourceMask.setStatus('current')
if mibBuilder.loadTexts: ipMRouteSourceMask.setDescription('The network mask which when combined with the corresponding\n            value of ipMRouteSource identifies the sources for which\n            this entry contains multicast routing information.')
ipMRouteUpstreamNeighbor = MibTableColumn((1, 3, 6, 1, 2, 1, 83, 1, 1, 2, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipMRouteUpstreamNeighbor.setStatus('current')
if mibBuilder.loadTexts: ipMRouteUpstreamNeighbor.setDescription('The address of the upstream neighbor (e.g., RPF neighbor)\n            from which IP datagrams from these sources to this multicast\n            address are received, or 0.0.0.0 if the upstream neighbor is\n            unknown (e.g., in CBT).')
ipMRouteInIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 83, 1, 1, 2, 1, 5), InterfaceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipMRouteInIfIndex.setStatus('current')
if mibBuilder.loadTexts: ipMRouteInIfIndex.setDescription('The value of ifIndex for the interface on which IP\n            datagrams sent by these sources to this multicast address\n            are received.  A value of 0 indicates that datagrams are not\n            subject to an incoming interface check, but may be accepted\n            on multiple interfaces (e.g., in CBT).')
ipMRouteUpTime = MibTableColumn((1, 3, 6, 1, 2, 1, 83, 1, 1, 2, 1, 6), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipMRouteUpTime.setStatus('current')
if mibBuilder.loadTexts: ipMRouteUpTime.setDescription('The time since the multicast routing information\n            represented by this entry was learned by the router.')
ipMRouteExpiryTime = MibTableColumn((1, 3, 6, 1, 2, 1, 83, 1, 1, 2, 1, 7), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipMRouteExpiryTime.setStatus('current')
if mibBuilder.loadTexts: ipMRouteExpiryTime.setDescription('The minimum amount of time remaining before this entry will\n            be aged out.  The value 0 indicates that the entry is not\n            subject to aging.')
ipMRoutePkts = MibTableColumn((1, 3, 6, 1, 2, 1, 83, 1, 1, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipMRoutePkts.setStatus('current')
if mibBuilder.loadTexts: ipMRoutePkts.setDescription('The number of packets which this router has received from\n            these sources and addressed to this multicast group\n            address.')
ipMRouteDifferentInIfPackets = MibTableColumn((1, 3, 6, 1, 2, 1, 83, 1, 1, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipMRouteDifferentInIfPackets.setStatus('current')
if mibBuilder.loadTexts: ipMRouteDifferentInIfPackets.setDescription('The number of packets which this router has received from\n            these sources and addressed to this multicast group address,\n            which were dropped because they were not received on the\n            interface indicated by ipMRouteInIfIndex.  Packets which are\n            not subject to an incoming interface check (e.g., using CBT)\n            are not counted.')
ipMRouteOctets = MibTableColumn((1, 3, 6, 1, 2, 1, 83, 1, 1, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipMRouteOctets.setStatus('current')
if mibBuilder.loadTexts: ipMRouteOctets.setDescription('The number of octets contained in IP datagrams which were\n            received from these sources and addressed to this multicast\n            group address, and which were forwarded by this router.')
ipMRouteProtocol = MibTableColumn((1, 3, 6, 1, 2, 1, 83, 1, 1, 2, 1, 11), IANAipMRouteProtocol()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipMRouteProtocol.setStatus('current')
if mibBuilder.loadTexts: ipMRouteProtocol.setDescription('The multicast routing protocol via which this multicast\n            forwarding entry was learned.')
ipMRouteRtProto = MibTableColumn((1, 3, 6, 1, 2, 1, 83, 1, 1, 2, 1, 12), IANAipRouteProtocol()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipMRouteRtProto.setStatus('current')
if mibBuilder.loadTexts: ipMRouteRtProto.setDescription('The routing mechanism via which the route used to find the\n           upstream or parent interface for this multicast forwarding\n           entry was learned.  Inclusion of values for routing\n           protocols is not intended to imply that those protocols need\n           be supported.')
ipMRouteRtAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 83, 1, 1, 2, 1, 13), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipMRouteRtAddress.setStatus('current')
if mibBuilder.loadTexts: ipMRouteRtAddress.setDescription('The address portion of the route used to find the upstream\n            or parent interface for this multicast forwarding entry.')
ipMRouteRtMask = MibTableColumn((1, 3, 6, 1, 2, 1, 83, 1, 1, 2, 1, 14), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipMRouteRtMask.setStatus('current')
if mibBuilder.loadTexts: ipMRouteRtMask.setDescription('The mask associated with the route used to find the upstream\n            or parent interface for this multicast forwarding entry.')
ipMRouteRtType = MibTableColumn((1, 3, 6, 1, 2, 1, 83, 1, 1, 2, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("unicast", 1), ("multicast", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipMRouteRtType.setStatus('current')
if mibBuilder.loadTexts: ipMRouteRtType.setDescription('The reason the given route was placed in the (logical)\n            multicast Routing Information Base (RIB).  A value of\n            unicast means that the route would normally be placed only\n            in the unicast RIB, but was placed in the multicast RIB\n            (instead or in addition) due to local configuration, such as\n            when running PIM over RIP.  A value of multicast means that\n            the route was explicitly added to the multicast RIB by the\n            routing protocol, such as DVMRP or Multiprotocol BGP.')
ipMRouteHCOctets = MibTableColumn((1, 3, 6, 1, 2, 1, 83, 1, 1, 2, 1, 16), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipMRouteHCOctets.setStatus('current')
if mibBuilder.loadTexts: ipMRouteHCOctets.setDescription('The number of octets contained in IP datagrams which were\n            received from these sources and addressed to this multicast\n            group address, and which were forwarded by this router.\n            This object is a 64-bit version of ipMRouteOctets.')
ipMRouteNextHopTable = MibTable((1, 3, 6, 1, 2, 1, 83, 1, 1, 3), )
if mibBuilder.loadTexts: ipMRouteNextHopTable.setStatus('current')
if mibBuilder.loadTexts: ipMRouteNextHopTable.setDescription('The (conceptual) table containing information on the next-\n            hops on outgoing interfaces for routing IP multicast\n\n            datagrams.  Each entry is one of a list of next-hops on\n            outgoing interfaces for particular sources sending to a\n            particular multicast group address.')
ipMRouteNextHopEntry = MibTableRow((1, 3, 6, 1, 2, 1, 83, 1, 1, 3, 1), ).setIndexNames((0, "IPMROUTE-STD-MIB", "ipMRouteNextHopGroup"), (0, "IPMROUTE-STD-MIB", "ipMRouteNextHopSource"), (0, "IPMROUTE-STD-MIB", "ipMRouteNextHopSourceMask"), (0, "IPMROUTE-STD-MIB", "ipMRouteNextHopIfIndex"), (0, "IPMROUTE-STD-MIB", "ipMRouteNextHopAddress"))
if mibBuilder.loadTexts: ipMRouteNextHopEntry.setStatus('current')
if mibBuilder.loadTexts: ipMRouteNextHopEntry.setDescription('An entry (conceptual row) in the list of next-hops on\n            outgoing interfaces to which IP multicast datagrams from\n            particular sources to a IP multicast group address are\n            routed.  Discontinuities in counters in this entry can be\n            detected by observing the value of ipMRouteUpTime.')
ipMRouteNextHopGroup = MibTableColumn((1, 3, 6, 1, 2, 1, 83, 1, 1, 3, 1, 1), IpAddress())
if mibBuilder.loadTexts: ipMRouteNextHopGroup.setStatus('current')
if mibBuilder.loadTexts: ipMRouteNextHopGroup.setDescription('The IP multicast group for which this entry specifies a\n            next-hop on an outgoing interface.')
ipMRouteNextHopSource = MibTableColumn((1, 3, 6, 1, 2, 1, 83, 1, 1, 3, 1, 2), IpAddress())
if mibBuilder.loadTexts: ipMRouteNextHopSource.setStatus('current')
if mibBuilder.loadTexts: ipMRouteNextHopSource.setDescription('The network address which when combined with the\n            corresponding value of ipMRouteNextHopSourceMask identifies\n            the sources for which this entry specifies a next-hop on an\n            outgoing interface.')
ipMRouteNextHopSourceMask = MibTableColumn((1, 3, 6, 1, 2, 1, 83, 1, 1, 3, 1, 3), IpAddress())
if mibBuilder.loadTexts: ipMRouteNextHopSourceMask.setStatus('current')
if mibBuilder.loadTexts: ipMRouteNextHopSourceMask.setDescription('The network mask which when combined with the corresponding\n            value of ipMRouteNextHopSource identifies the sources for\n            which this entry specifies a next-hop on an outgoing\n            interface.')
ipMRouteNextHopIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 83, 1, 1, 3, 1, 4), InterfaceIndex())
if mibBuilder.loadTexts: ipMRouteNextHopIfIndex.setStatus('current')
if mibBuilder.loadTexts: ipMRouteNextHopIfIndex.setDescription('The ifIndex value of the interface for the outgoing\n            interface for this next-hop.')
ipMRouteNextHopAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 83, 1, 1, 3, 1, 5), IpAddress())
if mibBuilder.loadTexts: ipMRouteNextHopAddress.setStatus('current')
if mibBuilder.loadTexts: ipMRouteNextHopAddress.setDescription('The address of the next-hop specific to this entry.  For\n            most interfaces, this is identical to ipMRouteNextHopGroup.\n            NBMA interfaces, however, may have multiple next-hop\n            addresses out a single outgoing interface.')
ipMRouteNextHopState = MibTableColumn((1, 3, 6, 1, 2, 1, 83, 1, 1, 3, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("pruned", 1), ("forwarding", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipMRouteNextHopState.setStatus('current')
if mibBuilder.loadTexts: ipMRouteNextHopState.setDescription("An indication of whether the outgoing interface and next-\n            hop represented by this entry is currently being used to\n            forward IP datagrams.  The value 'forwarding' indicates it\n            is currently being used; the value 'pruned' indicates it is\n            not.")
ipMRouteNextHopUpTime = MibTableColumn((1, 3, 6, 1, 2, 1, 83, 1, 1, 3, 1, 7), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipMRouteNextHopUpTime.setStatus('current')
if mibBuilder.loadTexts: ipMRouteNextHopUpTime.setDescription('The time since the multicast routing information\n            represented by this entry was learned by the router.')
ipMRouteNextHopExpiryTime = MibTableColumn((1, 3, 6, 1, 2, 1, 83, 1, 1, 3, 1, 8), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipMRouteNextHopExpiryTime.setStatus('current')
if mibBuilder.loadTexts: ipMRouteNextHopExpiryTime.setDescription('The minimum amount of time remaining before this entry will\n            be aged out.  If ipMRouteNextHopState is pruned(1), the\n            remaining time until the prune expires and the state reverts\n            to forwarding(2).  Otherwise, the remaining time until this\n            entry is removed from the table.  The time remaining may be\n            copied from ipMRouteExpiryTime if the protocol in use for\n            this entry does not specify next-hop timers.  The value 0\n            indicates that the entry is not subject to aging.')
ipMRouteNextHopClosestMemberHops = MibTableColumn((1, 3, 6, 1, 2, 1, 83, 1, 1, 3, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipMRouteNextHopClosestMemberHops.setStatus('current')
if mibBuilder.loadTexts: ipMRouteNextHopClosestMemberHops.setDescription('The minimum number of hops between this router and any\n            member of this IP multicast group reached via this next-hop\n            on this outgoing interface.  Any IP multicast datagrams for\n            the group which have a TTL less than this number of hops\n            will not be forwarded to this next-hop.')
ipMRouteNextHopProtocol = MibTableColumn((1, 3, 6, 1, 2, 1, 83, 1, 1, 3, 1, 10), IANAipMRouteProtocol()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipMRouteNextHopProtocol.setStatus('current')
if mibBuilder.loadTexts: ipMRouteNextHopProtocol.setDescription('The routing mechanism via which this next-hop was learned.')
ipMRouteNextHopPkts = MibTableColumn((1, 3, 6, 1, 2, 1, 83, 1, 1, 3, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipMRouteNextHopPkts.setStatus('current')
if mibBuilder.loadTexts: ipMRouteNextHopPkts.setDescription('The number of packets which have been forwarded using this\n            route.')
ipMRouteInterfaceTable = MibTable((1, 3, 6, 1, 2, 1, 83, 1, 1, 4), )
if mibBuilder.loadTexts: ipMRouteInterfaceTable.setStatus('current')
if mibBuilder.loadTexts: ipMRouteInterfaceTable.setDescription('The (conceptual) table containing multicast routing\n            information specific to interfaces.')
ipMRouteInterfaceEntry = MibTableRow((1, 3, 6, 1, 2, 1, 83, 1, 1, 4, 1), ).setIndexNames((0, "IPMROUTE-STD-MIB", "ipMRouteInterfaceIfIndex"))
if mibBuilder.loadTexts: ipMRouteInterfaceEntry.setStatus('current')
if mibBuilder.loadTexts: ipMRouteInterfaceEntry.setDescription('An entry (conceptual row) containing the multicast routing\n            information for a particular interface.')
ipMRouteInterfaceIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 83, 1, 1, 4, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: ipMRouteInterfaceIfIndex.setStatus('current')
if mibBuilder.loadTexts: ipMRouteInterfaceIfIndex.setDescription('The ifIndex value of the interface for which this entry\n            contains information.')
ipMRouteInterfaceTtl = MibTableColumn((1, 3, 6, 1, 2, 1, 83, 1, 1, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipMRouteInterfaceTtl.setStatus('current')
if mibBuilder.loadTexts: ipMRouteInterfaceTtl.setDescription('The datagram TTL threshold for the interface. Any IP\n            multicast datagrams with a TTL less than this threshold will\n            not be forwarded out the interface. The default value of 0\n            means all multicast packets are forwarded out the\n            interface.')
ipMRouteInterfaceProtocol = MibTableColumn((1, 3, 6, 1, 2, 1, 83, 1, 1, 4, 1, 3), IANAipMRouteProtocol()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipMRouteInterfaceProtocol.setStatus('current')
if mibBuilder.loadTexts: ipMRouteInterfaceProtocol.setDescription('The routing protocol running on this interface.')
ipMRouteInterfaceRateLimit = MibTableColumn((1, 3, 6, 1, 2, 1, 83, 1, 1, 4, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipMRouteInterfaceRateLimit.setStatus('current')
if mibBuilder.loadTexts: ipMRouteInterfaceRateLimit.setDescription('The rate-limit, in kilobits per second, of forwarded\n            multicast traffic on the interface.  A rate-limit of 0\n            indicates that no rate limiting is done.')
ipMRouteInterfaceInMcastOctets = MibTableColumn((1, 3, 6, 1, 2, 1, 83, 1, 1, 4, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipMRouteInterfaceInMcastOctets.setStatus('current')
if mibBuilder.loadTexts: ipMRouteInterfaceInMcastOctets.setDescription('The number of octets of multicast packets that have arrived\n            on the interface, including framing characters.  This object\n            is similar to ifInOctets in the Interfaces MIB, except that\n            only multicast packets are counted.')
ipMRouteInterfaceOutMcastOctets = MibTableColumn((1, 3, 6, 1, 2, 1, 83, 1, 1, 4, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipMRouteInterfaceOutMcastOctets.setStatus('current')
if mibBuilder.loadTexts: ipMRouteInterfaceOutMcastOctets.setDescription('The number of octets of multicast packets that have been\n            sent on the interface.')
ipMRouteInterfaceHCInMcastOctets = MibTableColumn((1, 3, 6, 1, 2, 1, 83, 1, 1, 4, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipMRouteInterfaceHCInMcastOctets.setStatus('current')
if mibBuilder.loadTexts: ipMRouteInterfaceHCInMcastOctets.setDescription('The number of octets of multicast packets that have arrived\n            on the interface, including framing characters.  This object\n            is a 64-bit version of ipMRouteInterfaceInMcastOctets.  It\n            is similar to ifHCInOctets in the Interfaces MIB, except\n            that only multicast packets are counted.')
ipMRouteInterfaceHCOutMcastOctets = MibTableColumn((1, 3, 6, 1, 2, 1, 83, 1, 1, 4, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipMRouteInterfaceHCOutMcastOctets.setStatus('current')
if mibBuilder.loadTexts: ipMRouteInterfaceHCOutMcastOctets.setDescription('The number of octets of multicast packets that have been\n            sent on the interface.  This object is a 64-bit version of\n            ipMRouteInterfaceOutMcastOctets.')
ipMRouteBoundaryTable = MibTable((1, 3, 6, 1, 2, 1, 83, 1, 1, 5), )
if mibBuilder.loadTexts: ipMRouteBoundaryTable.setStatus('current')
if mibBuilder.loadTexts: ipMRouteBoundaryTable.setDescription("The (conceptual) table listing the router's scoped\n            multicast address boundaries.")
ipMRouteBoundaryEntry = MibTableRow((1, 3, 6, 1, 2, 1, 83, 1, 1, 5, 1), ).setIndexNames((0, "IPMROUTE-STD-MIB", "ipMRouteBoundaryIfIndex"), (0, "IPMROUTE-STD-MIB", "ipMRouteBoundaryAddress"), (0, "IPMROUTE-STD-MIB", "ipMRouteBoundaryAddressMask"))
if mibBuilder.loadTexts: ipMRouteBoundaryEntry.setStatus('current')
if mibBuilder.loadTexts: ipMRouteBoundaryEntry.setDescription('An entry (conceptual row) in the ipMRouteBoundaryTable\n            representing a scoped boundary.')
ipMRouteBoundaryIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 83, 1, 1, 5, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: ipMRouteBoundaryIfIndex.setStatus('current')
if mibBuilder.loadTexts: ipMRouteBoundaryIfIndex.setDescription('The IfIndex value for the interface to which this boundary\n            applies.  Packets with a destination address in the\n            associated address/mask range will not be forwarded out this\n            interface.')
ipMRouteBoundaryAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 83, 1, 1, 5, 1, 2), IpAddress())
if mibBuilder.loadTexts: ipMRouteBoundaryAddress.setStatus('current')
if mibBuilder.loadTexts: ipMRouteBoundaryAddress.setDescription('The group address which when combined with the\n            corresponding value of ipMRouteBoundaryAddressMask\n            identifies the group range for which the scoped boundary\n            exists.  Scoped addresses must come from the range 239.x.x.x\n            as specified in RFC 2365.')
ipMRouteBoundaryAddressMask = MibTableColumn((1, 3, 6, 1, 2, 1, 83, 1, 1, 5, 1, 3), IpAddress())
if mibBuilder.loadTexts: ipMRouteBoundaryAddressMask.setStatus('current')
if mibBuilder.loadTexts: ipMRouteBoundaryAddressMask.setDescription('The group address mask which when combined with the\n            corresponding value of ipMRouteBoundaryAddress identifies\n            the group range for which the scoped boundary exists.')
ipMRouteBoundaryStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 83, 1, 1, 5, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipMRouteBoundaryStatus.setStatus('current')
if mibBuilder.loadTexts: ipMRouteBoundaryStatus.setDescription('The status of this row, by which new entries may be\n            created, or old entries deleted from this table.')
ipMRouteScopeNameTable = MibTable((1, 3, 6, 1, 2, 1, 83, 1, 1, 6), )
if mibBuilder.loadTexts: ipMRouteScopeNameTable.setStatus('current')
if mibBuilder.loadTexts: ipMRouteScopeNameTable.setDescription('The (conceptual) table listing the multicast scope names.')
ipMRouteScopeNameEntry = MibTableRow((1, 3, 6, 1, 2, 1, 83, 1, 1, 6, 1), ).setIndexNames((0, "IPMROUTE-STD-MIB", "ipMRouteScopeNameAddress"), (0, "IPMROUTE-STD-MIB", "ipMRouteScopeNameAddressMask"), (1, "IPMROUTE-STD-MIB", "ipMRouteScopeNameLanguage"))
if mibBuilder.loadTexts: ipMRouteScopeNameEntry.setStatus('current')
if mibBuilder.loadTexts: ipMRouteScopeNameEntry.setDescription('An entry (conceptual row) in the ipMRouteScopeNameTable\n            representing a multicast scope name.')
ipMRouteScopeNameAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 83, 1, 1, 6, 1, 1), IpAddress())
if mibBuilder.loadTexts: ipMRouteScopeNameAddress.setStatus('current')
if mibBuilder.loadTexts: ipMRouteScopeNameAddress.setDescription('The group address which when combined with the\n            corresponding value of ipMRouteScopeNameAddressMask\n            identifies the group range associated with the multicast\n            scope.  Scoped addresses must come from the range\n            239.x.x.x.')
ipMRouteScopeNameAddressMask = MibTableColumn((1, 3, 6, 1, 2, 1, 83, 1, 1, 6, 1, 2), IpAddress())
if mibBuilder.loadTexts: ipMRouteScopeNameAddressMask.setStatus('current')
if mibBuilder.loadTexts: ipMRouteScopeNameAddressMask.setDescription('The group address mask which when combined with the\n            corresponding value of ipMRouteScopeNameAddress identifies\n            the group range associated with the multicast scope.')
ipMRouteScopeNameLanguage = MibTableColumn((1, 3, 6, 1, 2, 1, 83, 1, 1, 6, 1, 3), LanguageTag())
if mibBuilder.loadTexts: ipMRouteScopeNameLanguage.setStatus('current')
if mibBuilder.loadTexts: ipMRouteScopeNameLanguage.setDescription('The RFC 1766-style language tag associated with the scope\n            name.')
ipMRouteScopeNameString = MibTableColumn((1, 3, 6, 1, 2, 1, 83, 1, 1, 6, 1, 4), SnmpAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipMRouteScopeNameString.setStatus('current')
if mibBuilder.loadTexts: ipMRouteScopeNameString.setDescription('The textual name associated with the multicast scope.  The\n            value of this object should be suitable for displaying to\n            end-users, such as when allocating a multicast address in\n            this scope.  When no name is specified, the default value of\n            this object should be the string 239.x.x.x/y with x and y\n            replaced appropriately to describe the address and mask\n            length associated with the scope.')
ipMRouteScopeNameDefault = MibTableColumn((1, 3, 6, 1, 2, 1, 83, 1, 1, 6, 1, 5), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipMRouteScopeNameDefault.setStatus('current')
if mibBuilder.loadTexts: ipMRouteScopeNameDefault.setDescription('If true, indicates a preference that the name in the\n            following language should be used by applications if no name\n            is available in a desired language.')
ipMRouteScopeNameStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 83, 1, 1, 6, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipMRouteScopeNameStatus.setStatus('current')
if mibBuilder.loadTexts: ipMRouteScopeNameStatus.setDescription('The status of this row, by which new entries may be\n            created, or old entries deleted from this table.')
ipMRouteMIBConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 83, 2))
ipMRouteMIBCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 83, 2, 1))
ipMRouteMIBGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 83, 2, 2))
ipMRouteMIBCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 83, 2, 1, 1)).setObjects(("IPMROUTE-STD-MIB", "ipMRouteMIBBasicGroup"), ("IPMROUTE-STD-MIB", "ipMRouteMIBRouteGroup"), ("IPMROUTE-STD-MIB", "ipMRouteMIBBoundaryGroup"), ("IPMROUTE-STD-MIB", "ipMRouteMIBHCInterfaceGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ipMRouteMIBCompliance = ipMRouteMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: ipMRouteMIBCompliance.setDescription('The compliance statement for the IP Multicast MIB.')
ipMRouteMIBBasicGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 83, 2, 2, 1)).setObjects(("IPMROUTE-STD-MIB", "ipMRouteEnable"), ("IPMROUTE-STD-MIB", "ipMRouteEntryCount"), ("IPMROUTE-STD-MIB", "ipMRouteUpstreamNeighbor"), ("IPMROUTE-STD-MIB", "ipMRouteInIfIndex"), ("IPMROUTE-STD-MIB", "ipMRouteUpTime"), ("IPMROUTE-STD-MIB", "ipMRouteExpiryTime"), ("IPMROUTE-STD-MIB", "ipMRouteNextHopState"), ("IPMROUTE-STD-MIB", "ipMRouteNextHopUpTime"), ("IPMROUTE-STD-MIB", "ipMRouteNextHopExpiryTime"), ("IPMROUTE-STD-MIB", "ipMRouteNextHopProtocol"), ("IPMROUTE-STD-MIB", "ipMRouteNextHopPkts"), ("IPMROUTE-STD-MIB", "ipMRouteInterfaceTtl"), ("IPMROUTE-STD-MIB", "ipMRouteInterfaceProtocol"), ("IPMROUTE-STD-MIB", "ipMRouteInterfaceRateLimit"), ("IPMROUTE-STD-MIB", "ipMRouteInterfaceInMcastOctets"), ("IPMROUTE-STD-MIB", "ipMRouteInterfaceOutMcastOctets"), ("IPMROUTE-STD-MIB", "ipMRouteProtocol"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ipMRouteMIBBasicGroup = ipMRouteMIBBasicGroup.setStatus('current')
if mibBuilder.loadTexts: ipMRouteMIBBasicGroup.setDescription('A collection of objects to support basic management of IP\n            Multicast routing.')
ipMRouteMIBHopCountGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 83, 2, 2, 2)).setObjects(("IPMROUTE-STD-MIB", "ipMRouteNextHopClosestMemberHops"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ipMRouteMIBHopCountGroup = ipMRouteMIBHopCountGroup.setStatus('current')
if mibBuilder.loadTexts: ipMRouteMIBHopCountGroup.setDescription('A collection of objects to support management of the use of\n            hop counts in IP Multicast routing.')
ipMRouteMIBBoundaryGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 83, 2, 2, 3)).setObjects(("IPMROUTE-STD-MIB", "ipMRouteBoundaryStatus"), ("IPMROUTE-STD-MIB", "ipMRouteScopeNameString"), ("IPMROUTE-STD-MIB", "ipMRouteScopeNameDefault"), ("IPMROUTE-STD-MIB", "ipMRouteScopeNameStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ipMRouteMIBBoundaryGroup = ipMRouteMIBBoundaryGroup.setStatus('current')
if mibBuilder.loadTexts: ipMRouteMIBBoundaryGroup.setDescription('A collection of objects to support management of scoped\n            multicast address boundaries.')
ipMRouteMIBPktsOutGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 83, 2, 2, 4)).setObjects(("IPMROUTE-STD-MIB", "ipMRouteNextHopPkts"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ipMRouteMIBPktsOutGroup = ipMRouteMIBPktsOutGroup.setStatus('current')
if mibBuilder.loadTexts: ipMRouteMIBPktsOutGroup.setDescription('A collection of objects to support management of packet\n            counters for each outgoing interface entry of a route.')
ipMRouteMIBHCInterfaceGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 83, 2, 2, 5)).setObjects(("IPMROUTE-STD-MIB", "ipMRouteInterfaceHCInMcastOctets"), ("IPMROUTE-STD-MIB", "ipMRouteInterfaceHCOutMcastOctets"), ("IPMROUTE-STD-MIB", "ipMRouteHCOctets"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ipMRouteMIBHCInterfaceGroup = ipMRouteMIBHCInterfaceGroup.setStatus('current')
if mibBuilder.loadTexts: ipMRouteMIBHCInterfaceGroup.setDescription('A collection of objects providing information specific to\n            high speed (greater than 20,000,000 bits/second) network\n            interfaces.')
ipMRouteMIBRouteGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 83, 2, 2, 6)).setObjects(("IPMROUTE-STD-MIB", "ipMRouteRtProto"), ("IPMROUTE-STD-MIB", "ipMRouteRtAddress"), ("IPMROUTE-STD-MIB", "ipMRouteRtMask"), ("IPMROUTE-STD-MIB", "ipMRouteRtType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ipMRouteMIBRouteGroup = ipMRouteMIBRouteGroup.setStatus('current')
if mibBuilder.loadTexts: ipMRouteMIBRouteGroup.setDescription('A collection of objects providing information on the\n            relationship between multicast routing information, and the\n            IP Forwarding Table.')
ipMRouteMIBPktsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 83, 2, 2, 7)).setObjects(("IPMROUTE-STD-MIB", "ipMRoutePkts"), ("IPMROUTE-STD-MIB", "ipMRouteDifferentInIfPackets"), ("IPMROUTE-STD-MIB", "ipMRouteOctets"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ipMRouteMIBPktsGroup = ipMRouteMIBPktsGroup.setStatus('current')
if mibBuilder.loadTexts: ipMRouteMIBPktsGroup.setDescription('A collection of objects to support management of packet\n            counters for each forwarding entry.')
mibBuilder.exportSymbols("IPMROUTE-STD-MIB", ipMRouteNextHopAddress=ipMRouteNextHopAddress, ipMRouteMIBRouteGroup=ipMRouteMIBRouteGroup, ipMRouteSource=ipMRouteSource, ipMRouteUpstreamNeighbor=ipMRouteUpstreamNeighbor, ipMRouteRtAddress=ipMRouteRtAddress, ipMRouteNextHopUpTime=ipMRouteNextHopUpTime, ipMRouteScopeNameAddress=ipMRouteScopeNameAddress, ipMRouteBoundaryAddressMask=ipMRouteBoundaryAddressMask, ipMRouteInterfaceIfIndex=ipMRouteInterfaceIfIndex, ipMRouteScopeNameLanguage=ipMRouteScopeNameLanguage, ipMRouteMIBConformance=ipMRouteMIBConformance, ipMRouteHCOctets=ipMRouteHCOctets, ipMRouteNextHopSource=ipMRouteNextHopSource, ipMRouteBoundaryTable=ipMRouteBoundaryTable, ipMRouteNextHopClosestMemberHops=ipMRouteNextHopClosestMemberHops, ipMRouteMIBPktsOutGroup=ipMRouteMIBPktsOutGroup, ipMRouteInterfaceTable=ipMRouteInterfaceTable, ipMRouteInterfaceProtocol=ipMRouteInterfaceProtocol, ipMRouteRtProto=ipMRouteRtProto, ipMRouteEntry=ipMRouteEntry, ipMRouteBoundaryIfIndex=ipMRouteBoundaryIfIndex, ipMRouteRtType=ipMRouteRtType, ipMRouteEnable=ipMRouteEnable, ipMRouteNextHopEntry=ipMRouteNextHopEntry, ipMRouteScopeNameStatus=ipMRouteScopeNameStatus, ipMRouteBoundaryEntry=ipMRouteBoundaryEntry, ipMRouteBoundaryAddress=ipMRouteBoundaryAddress, ipMRoutePkts=ipMRoutePkts, ipMRouteRtMask=ipMRouteRtMask, ipMRouteNextHopState=ipMRouteNextHopState, ipMRouteInterfaceOutMcastOctets=ipMRouteInterfaceOutMcastOctets, ipMRouteSourceMask=ipMRouteSourceMask, ipMRouteInterfaceInMcastOctets=ipMRouteInterfaceInMcastOctets, ipMRouteInterfaceHCOutMcastOctets=ipMRouteInterfaceHCOutMcastOctets, ipMRouteMIBGroups=ipMRouteMIBGroups, ipMRouteExpiryTime=ipMRouteExpiryTime, ipMRouteUpTime=ipMRouteUpTime, ipMRouteOctets=ipMRouteOctets, ipMRouteInterfaceHCInMcastOctets=ipMRouteInterfaceHCInMcastOctets, ipMRouteNextHopExpiryTime=ipMRouteNextHopExpiryTime, ipMRouteScopeNameAddressMask=ipMRouteScopeNameAddressMask, ipMRouteInterfaceTtl=ipMRouteInterfaceTtl, ipMRouteEntryCount=ipMRouteEntryCount, ipMRouteNextHopProtocol=ipMRouteNextHopProtocol, ipMRouteScopeNameDefault=ipMRouteScopeNameDefault, PYSNMP_MODULE_ID=ipMRouteStdMIB, ipMRouteScopeNameEntry=ipMRouteScopeNameEntry, ipMRouteMIBCompliances=ipMRouteMIBCompliances, ipMRouteMIBBoundaryGroup=ipMRouteMIBBoundaryGroup, ipMRouteMIBHCInterfaceGroup=ipMRouteMIBHCInterfaceGroup, ipMRouteNextHopTable=ipMRouteNextHopTable, ipMRouteNextHopPkts=ipMRouteNextHopPkts, ipMRouteInterfaceEntry=ipMRouteInterfaceEntry, ipMRouteInterfaceRateLimit=ipMRouteInterfaceRateLimit, LanguageTag=LanguageTag, ipMRouteScopeNameString=ipMRouteScopeNameString, ipMRouteInIfIndex=ipMRouteInIfIndex, ipMRouteStdMIB=ipMRouteStdMIB, ipMRouteDifferentInIfPackets=ipMRouteDifferentInIfPackets, ipMRouteBoundaryStatus=ipMRouteBoundaryStatus, ipMRouteScopeNameTable=ipMRouteScopeNameTable, ipMRouteMIBHopCountGroup=ipMRouteMIBHopCountGroup, ipMRouteGroup=ipMRouteGroup, ipMRouteMIBCompliance=ipMRouteMIBCompliance, ipMRouteMIBObjects=ipMRouteMIBObjects, ipMRouteMIBPktsGroup=ipMRouteMIBPktsGroup, ipMRouteNextHopSourceMask=ipMRouteNextHopSourceMask, ipMRouteTable=ipMRouteTable, ipMRouteMIBBasicGroup=ipMRouteMIBBasicGroup, ipMRouteNextHopIfIndex=ipMRouteNextHopIfIndex, ipMRouteNextHopGroup=ipMRouteNextHopGroup, ipMRoute=ipMRoute, ipMRouteProtocol=ipMRouteProtocol)
