#
# PySNMP MIB module IANA-RTPROTO-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/IANA-RTPROTO-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 15:51:16 2022
# On host fv-az135-792 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, Counter64, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, mib_2, Unsigned32, iso, TimeTicks, Counter32, Bits, ModuleIdentity, MibIdentifier, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Counter64", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "mib-2", "Unsigned32", "iso", "TimeTicks", "Counter32", "Bits", "ModuleIdentity", "MibIdentifier", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ianaRtProtoMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 84))
ianaRtProtoMIB.setRevisions(('2016-04-25 00:00', '2016-04-06 00:00', '2012-08-30 00:00', '2011-07-22 00:00', '2000-09-26 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ianaRtProtoMIB.setRevisionsDescriptions(('Corrected typographical error in revision date.', 'Added ttdp(20).', 'Added dhcp(19).', 'Added rpl(18) .', 'Original version, published in coordination\n                 with RFC 2932.',))
if mibBuilder.loadTexts: ianaRtProtoMIB.setLastUpdated('201604250000Z')
if mibBuilder.loadTexts: ianaRtProtoMIB.setOrganization('IANA')
if mibBuilder.loadTexts: ianaRtProtoMIB.setContactInfo(' Internet Assigned Numbers Authority\n              Internet Corporation for Assigned Names and Numbers\n              12025 Waterfront Drive, Suite 300\n              Los Angeles, CA 90094-2536\n\n              Phone: +1 310 301 5800\n              EMail: iana&iana.org')
if mibBuilder.loadTexts: ianaRtProtoMIB.setDescription('This MIB module defines the IANAipRouteProtocol and\n            IANAipMRouteProtocol textual conventions for use in MIBs\n            which need to identify unicast or multicast routing\n            mechanisms.\n\n            Any additions or changes to the contents of this MIB module\n            require either publication of an RFC, or Designated Expert\n            Review as defined in RFC 2434, Guidelines for Writing an\n            IANA Considerations Section in RFCs.  The Designated Expert\n            will be selected by the IESG Area Director(s) of the Routing\n            Area.')
class IANAipRouteProtocol(TextualConvention, Integer32):
    description = 'A mechanism for learning routes.  Inclusion of values for\n            routing protocols is not intended to imply that those\n            protocols need be supported.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20))
    namedValues = NamedValues(("other", 1), ("local", 2), ("netmgmt", 3), ("icmp", 4), ("egp", 5), ("ggp", 6), ("hello", 7), ("rip", 8), ("isIs", 9), ("esIs", 10), ("ciscoIgrp", 11), ("bbnSpfIgp", 12), ("ospf", 13), ("bgp", 14), ("idpr", 15), ("ciscoEigrp", 16), ("dvmrp", 17), ("rpl", 18), ("dhcp", 19), ("ttdp", 20))

class IANAipMRouteProtocol(TextualConvention, Integer32):
    description = 'The multicast routing protocol.  Inclusion of values for\n            multicast routing protocols is not intended to imply that\n            those protocols need be supported.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    namedValues = NamedValues(("other", 1), ("local", 2), ("netmgmt", 3), ("dvmrp", 4), ("mospf", 5), ("pimSparseDense", 6), ("cbt", 7), ("pimSparseMode", 8), ("pimDenseMode", 9), ("igmpOnly", 10), ("bgmp", 11), ("msdp", 12))

mibBuilder.exportSymbols("IANA-RTPROTO-MIB", IANAipRouteProtocol=IANAipRouteProtocol, IANAipMRouteProtocol=IANAipMRouteProtocol, PYSNMP_MODULE_ID=ianaRtProtoMIB, ianaRtProtoMIB=ianaRtProtoMIB)
