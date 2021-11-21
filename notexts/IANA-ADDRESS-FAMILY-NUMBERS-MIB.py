#
# PySNMP MIB module IANA-ADDRESS-FAMILY-NUMBERS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/output/asn1/IANA-ADDRESS-FAMILY-NUMBERS-MIB
# Produced by pysmi-1.1.3 at Sun Nov 21 00:27:18 2021
# On host fv-az39-63 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, Counter32, ObjectIdentity, NotificationType, ModuleIdentity, MibIdentifier, Integer32, TimeTicks, IpAddress, Gauge32, mib_2, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "ObjectIdentity", "NotificationType", "ModuleIdentity", "MibIdentifier", "Integer32", "TimeTicks", "IpAddress", "Gauge32", "mib-2", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ianaAddressFamilyNumbers = ModuleIdentity((1, 3, 6, 1, 2, 1, 72))
ianaAddressFamilyNumbers.setRevisions(('2019-11-04 00:00', '2014-09-02 00:00', '2013-09-25 00:00', '2013-07-16 00:00', '2013-06-26 00:00', '2013-06-18 00:00', '2002-03-14 00:00', '2000-09-08 00:00', '2000-03-01 00:00', '2000-02-04 00:00', '1999-08-26 00:00',))
if mibBuilder.loadTexts: ianaAddressFamilyNumbers.setLastUpdated('201911040000Z')
if mibBuilder.loadTexts: ianaAddressFamilyNumbers.setOrganization('IANA')
class AddressFamilyNumbers(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 16384, 16385, 16386, 16387, 16388, 16389, 16390, 16391, 16392, 16393, 16394, 16395, 16396, 16397, 65535))
    namedValues = NamedValues(("other", 0), ("ipV4", 1), ("ipV6", 2), ("nsap", 3), ("hdlc", 4), ("bbn1822", 5), ("all802", 6), ("e163", 7), ("e164", 8), ("f69", 9), ("x121", 10), ("ipx", 11), ("appleTalk", 12), ("decnetIV", 13), ("banyanVines", 14), ("e164withNsap", 15), ("dns", 16), ("distinguishedName", 17), ("asNumber", 18), ("xtpOverIpv4", 19), ("xtpOverIpv6", 20), ("xtpNativeModeXTP", 21), ("fibreChannelWWPN", 22), ("fibreChannelWWNN", 23), ("gwid", 24), ("afi", 25), ("mplsTpSectionEndpointIdentifier", 26), ("mplsTpLspEndpointIdentifier", 27), ("mplsTpPseudowireEndpointIdentifier", 28), ("eigrpCommonServiceFamily", 16384), ("eigrpIpv4ServiceFamily", 16385), ("eigrpIpv6ServiceFamily", 16386), ("lispCanonicalAddressFormat", 16387), ("bgpLs", 16388), ("fortyeightBitMac", 16389), ("sixtyfourBitMac", 16390), ("oui", 16391), ("mac24", 16392), ("mac40", 16393), ("ipv664", 16394), ("rBridgePortID", 16395), ("trillNickname", 16396), ("universallyUniqueIdentifier", 16397), ("reserved", 65535))

mibBuilder.exportSymbols("IANA-ADDRESS-FAMILY-NUMBERS-MIB", PYSNMP_MODULE_ID=ianaAddressFamilyNumbers, AddressFamilyNumbers=AddressFamilyNumbers, ianaAddressFamilyNumbers=ianaAddressFamilyNumbers)
