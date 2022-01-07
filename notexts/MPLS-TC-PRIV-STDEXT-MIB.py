#
# PySNMP MIB module MPLS-TC-PRIV-STDEXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/telco-systems/binos/MPLS-TC-PRIV-STDEXT-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:39:22 2022
# On host fv-az36-988 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, NotificationType, Integer32, Counter32, TimeTicks, ObjectIdentity, Gauge32, ModuleIdentity, Counter64, IpAddress, iso, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, transmission = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "NotificationType", "Integer32", "Counter32", "TimeTicks", "ObjectIdentity", "Gauge32", "ModuleIdentity", "Counter64", "IpAddress", "iso", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "transmission")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
mplsTCPrivStdExtMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 10, 166, 1))
mplsTCPrivStdExtMIB.setRevisions(('2007-12-06 00:00', '2004-06-03 00:00',))
if mibBuilder.loadTexts: mplsTCPrivStdExtMIB.setLastUpdated('200712060000Z')
if mibBuilder.loadTexts: mplsTCPrivStdExtMIB.setOrganization('BATM Advanced Communication')
mplsStdMIB = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166))
class MplsAtmVcIdentifier(TextualConvention, Integer32):
    reference = 'MPLS using LDP and ATM VC Switching, RFC3035.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(32, 65535)

class MplsBitRate(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 4294967295), )
class MplsBurstSize(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class MplsExtendedTunnelId(TextualConvention, Unsigned32):
    reference = 'RSVP-TE: Extensions to RSVP for LSP Tunnels, [RFC3209]. Constraint-Based LSP Setup using LDP, [RFC3212].'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class MplsLabel(TextualConvention, Unsigned32):
    reference = 'Multiprotocol Label Switching Architecture, RFC3031. MPLS Label Stack Encoding, [RFC3032]. Use of Label Switching on Frame Relay Networks, RFC3034. MPLS using LDP and ATM VC Switching, RFC3035. Generalized Multiprotocol Label Switching (GMPLS) Architecture, [RFC3471].'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class MplsLabelDistributionMethod(TextualConvention, Integer32):
    reference = 'Multiprotocol Label Switching Architecture, RFC3031. LDP Specification, RFC3036, Section 2.6.3.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("downstreamOnDemand", 1), ("downstreamUnsolicited", 2))

class MplsLdpIdentifier(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1d.1d.1d.1d:2d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

class MplsLsrIdentifier(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class MplsLdpLabelType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("generic", 1), ("atm", 2), ("frameRelay", 3))

class MplsLSPID(TextualConvention, OctetString):
    reference = 'RSVP-TE: Extensions to RSVP for LSP Tunnels, [RFC3209]. Constraint-Based LSP Setup using LDP, [RFC3212].'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(2, 2), ValueSizeConstraint(6, 6), )
class MplsLspType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("unknown", 1), ("terminatingLsp", 2), ("originatingLsp", 3), ("crossConnectingLsp", 4))

class MplsOwner(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    namedValues = NamedValues(("unknown", 1), ("other", 2), ("snmp", 3), ("ldp", 4), ("crldp", 5), ("rsvpTe", 6), ("policyAgent", 7), ("mplsVpn", 8), ("cli", 9), ("dynamic", 10))

class MplsPathIndexOrZero(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class MplsPathIndex(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class MplsRetentionMode(TextualConvention, Integer32):
    reference = 'Multiprotocol Label Switching Architecture, RFC3031. LDP Specification, RFC3036, Section 2.6.2.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("conservative", 1), ("liberal", 2))

class MplsTunnelAffinity(TextualConvention, Unsigned32):
    reference = 'RSVP-TE: Extensions to RSVP for LSP Tunnels, RFC3209, Section 4.7.4.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class MplsTunnelIndex(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 65535)

class MplsTunnelInstanceIndex(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 65535), ValueRangeConstraint(65536, 4294967295), )
class TeHopAddressType(TextualConvention, Integer32):
    reference = 'TEXTUAL-CONVENTIONs for Internet Network Addresses, RFC3291. Constraint-Based LSP Setup using LDP, [RFC3212]'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("unknown", 0), ("ipv4", 1), ("ipv6", 2), ("asnumber", 3), ("unnum", 4), ("lspid", 5), ("unnumv6", 6))

class TeHopAddress(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class TeHopAddressAS(TextualConvention, Unsigned32):
    reference = 'Textual Conventions for Internet Network Addresses, [RFC3291].'
    status = 'current'

class TeHopAddressUnnum(TextualConvention, Unsigned32):
    status = 'current'

mibBuilder.exportSymbols("MPLS-TC-PRIV-STDEXT-MIB", MplsAtmVcIdentifier=MplsAtmVcIdentifier, MplsLdpIdentifier=MplsLdpIdentifier, MplsOwner=MplsOwner, mplsStdMIB=mplsStdMIB, MplsPathIndex=MplsPathIndex, MplsLSPID=MplsLSPID, MplsBitRate=MplsBitRate, TeHopAddressAS=TeHopAddressAS, MplsLabelDistributionMethod=MplsLabelDistributionMethod, MplsLdpLabelType=MplsLdpLabelType, MplsRetentionMode=MplsRetentionMode, MplsTunnelInstanceIndex=MplsTunnelInstanceIndex, MplsLspType=MplsLspType, MplsExtendedTunnelId=MplsExtendedTunnelId, PYSNMP_MODULE_ID=mplsTCPrivStdExtMIB, MplsTunnelAffinity=MplsTunnelAffinity, MplsPathIndexOrZero=MplsPathIndexOrZero, TeHopAddressType=TeHopAddressType, MplsLsrIdentifier=MplsLsrIdentifier, TeHopAddress=TeHopAddress, MplsTunnelIndex=MplsTunnelIndex, MplsBurstSize=MplsBurstSize, TeHopAddressUnnum=TeHopAddressUnnum, mplsTCPrivStdExtMIB=mplsTCPrivStdExtMIB, MplsLabel=MplsLabel)
