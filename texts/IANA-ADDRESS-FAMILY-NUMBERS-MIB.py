#
# PySNMP MIB module IANA-ADDRESS-FAMILY-NUMBERS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/IANA-ADDRESS-FAMILY-NUMBERS-MIB
# Produced by pysmi-1.1.3 at Sun Nov 21 00:25:48 2021
# On host fv-az39-63 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
mib_2, ModuleIdentity, Counter32, MibIdentifier, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, NotificationType, Counter64, iso, Unsigned32, Integer32, TimeTicks, IpAddress, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "mib-2", "ModuleIdentity", "Counter32", "MibIdentifier", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "NotificationType", "Counter64", "iso", "Unsigned32", "Integer32", "TimeTicks", "IpAddress", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ianaAddressFamilyNumbers = ModuleIdentity((1, 3, 6, 1, 2, 1, 72))
ianaAddressFamilyNumbers.setRevisions(('2019-11-04 00:00', '2014-09-02 00:00', '2013-09-25 00:00', '2013-07-16 00:00', '2013-06-26 00:00', '2013-06-18 00:00', '2002-03-14 00:00', '2000-09-08 00:00', '2000-03-01 00:00', '2000-02-04 00:00', '1999-08-26 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ianaAddressFamilyNumbers.setRevisionsDescriptions(('Assigned value 16397.', 'Assigned value 16396.', 'Assigned values 16391-16395.', 'Fixed labels for 16389-16390.', 'Added assignments 26-28.', 'Added assignments 16384-16390. Assignment\n                  25 added in 2007 revision.', 'AddressFamilyNumbers assignment 22 to\n                 fibreChannelWWPN. AddressFamilyNumbers\n                 assignment 23 to fibreChannelWWNN.\n                 AddressFamilyNumers assignment 24 to gwid.', 'AddressFamilyNumbers assignment 19 to xtpOverIpv4.\n                 AddressFamilyNumbers assignment 20 to xtpOverIpv6.\n                 AddressFamilyNumbers assignment 21 to xtpNativeModeXTP.', 'AddressFamilyNumbers assignment 17 to distinguishedName.\n                 AddressFamilyNumbers assignment 18 to asNumber.', 'AddressFamilyNumbers assignment 16 to dns.', 'Initial version, published as RFC 2677.',))
if mibBuilder.loadTexts: ianaAddressFamilyNumbers.setLastUpdated('201911040000Z')
if mibBuilder.loadTexts: ianaAddressFamilyNumbers.setOrganization('IANA')
if mibBuilder.loadTexts: ianaAddressFamilyNumbers.setContactInfo('Postal:    Internet Assigned Numbers Authority\n                    Internet Corporation for Assigned Names and Numbers\n                    12025 Waterfront Drive, Suite 300\n                    Los Angeles, CA 90094-2536\n                    USA\n\n        Tel:    +1  310-301-5800\n        E-Mail: iana&iana.org')
if mibBuilder.loadTexts: ianaAddressFamilyNumbers.setDescription('The MIB module defines the AddressFamilyNumbers\n        textual convention.')
class AddressFamilyNumbers(TextualConvention, Integer32):
    description = "The definition of this textual convention with the\n        addition of newly assigned values is published\n        periodically by the IANA, in either the Assigned\n        Numbers RFC, or some derivative of it specific to\n        Internet Network Management number assignments.\n        (The latest arrangements can be obtained by\n        contacting the IANA.)\n\n        The enumerations are described as:\n\n        other(0),    -- none of the following\n        ipV4(1),     -- IP Version 4\n        ipV6(2),     -- IP Version 6\n        nsap(3),     -- NSAP\n        hdlc(4),     -- (8-bit multidrop)\n        bbn1822(5),\n        all802(6),   -- (includes all 802 media\n                     --   plus Ethernet 'canonical format')\n        e163(7),\n        e164(8),     -- (SMDS, Frame Relay, ATM)\n        f69(9),      -- (Telex)\n        x121(10),    -- (X.25, Frame Relay)\n        ipx(11),     -- IPX (Internet Protocol Exchange)\n        appleTalk(12),  -- Apple Talk\n        decnetIV(13),   -- DEC Net Phase IV\n        banyanVines(14),  -- Banyan Vines\n        e164withNsap(15),\n                     -- (E.164 with NSAP format subaddress)\n        dns(16),     -- (Domain Name System)\n        distinguishedName(17), -- (Distinguished Name, per X.500)\n        asNumber(18), -- (16-bit quantity, per the AS number space)\n        xtpOverIpv4(19),  -- XTP over IP version 4\n        xtpOverIpv6(20),  -- XTP over IP version 6\n        xtpNativeModeXTP(21),  -- XTP native mode XTP\n        fibreChannelWWPN(22),  -- Fibre Channel World-Wide Port Name\n        fibreChannelWWNN(23),  -- Fibre Channel World-Wide Node Name\n        gwid(24),    -- Gateway Identifier\n        afi(25),  -- AFI for L2VPN information\n        mplsTpSectionEndpointIdentifier(26),  -- MPLS-TP Section Endpoint Identifier\n        mplsTpLspEndpointIdentifier(27),  -- MPLS-TP LSP Endpoint Identifier\n        mplsTpPseudowireEndpointIdentifier(28),  -- MPLS-TP Pseudowire Endpoint Identifier\n        eigrpCommonServiceFamily(16384),  -- EIGRP Common Service Family\n        eigrpIpv4ServiceFamily(16385),  -- EIGRP IPv4 Service Family\n        eigrpIpv6ServiceFamily(16386),  -- EIGRP IPv6 Service Family\n        lispCanonicalAddressFormat(16387),  -- LISP Canonical Address Format (LCAF)\n        bgpLs(16388),  -- BGP-LS\n        fortyeightBitMacBitMac(16389),  -- 48-bit MAC\n        sixtyfourBitMac(16390),  -- 64-bit MAC\n        oui(16391),  -- OUI\n        mac24(16392),  -- MAC/24\n        mac40(16393),  -- MAC/40\n        ipv664(16394),  -- IPv6/64\n        rBridgePortID(16395),  -- RBridge Port ID\n        trillNickname(16396),  -- TRILL Nickname\n        universallyUniqueIdentifier(16397),  -- Universally Unique Identifier (UUID)\n        reserved(65535)\n\n        Requests for new values should be made to IANA via\n        email (iana&iana.org)."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 16384, 16385, 16386, 16387, 16388, 16389, 16390, 16391, 16392, 16393, 16394, 16395, 16396, 16397, 65535))
    namedValues = NamedValues(("other", 0), ("ipV4", 1), ("ipV6", 2), ("nsap", 3), ("hdlc", 4), ("bbn1822", 5), ("all802", 6), ("e163", 7), ("e164", 8), ("f69", 9), ("x121", 10), ("ipx", 11), ("appleTalk", 12), ("decnetIV", 13), ("banyanVines", 14), ("e164withNsap", 15), ("dns", 16), ("distinguishedName", 17), ("asNumber", 18), ("xtpOverIpv4", 19), ("xtpOverIpv6", 20), ("xtpNativeModeXTP", 21), ("fibreChannelWWPN", 22), ("fibreChannelWWNN", 23), ("gwid", 24), ("afi", 25), ("mplsTpSectionEndpointIdentifier", 26), ("mplsTpLspEndpointIdentifier", 27), ("mplsTpPseudowireEndpointIdentifier", 28), ("eigrpCommonServiceFamily", 16384), ("eigrpIpv4ServiceFamily", 16385), ("eigrpIpv6ServiceFamily", 16386), ("lispCanonicalAddressFormat", 16387), ("bgpLs", 16388), ("fortyeightBitMac", 16389), ("sixtyfourBitMac", 16390), ("oui", 16391), ("mac24", 16392), ("mac40", 16393), ("ipv664", 16394), ("rBridgePortID", 16395), ("trillNickname", 16396), ("universallyUniqueIdentifier", 16397), ("reserved", 65535))

mibBuilder.exportSymbols("IANA-ADDRESS-FAMILY-NUMBERS-MIB", AddressFamilyNumbers=AddressFamilyNumbers, PYSNMP_MODULE_ID=ianaAddressFamilyNumbers, ianaAddressFamilyNumbers=ianaAddressFamilyNumbers)
