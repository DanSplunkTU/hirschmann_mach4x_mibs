#
# PySNMP MIB module IPMROUTE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/IPMROUTE-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 17:49:36 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
InterfaceIndex, InterfaceIndexOrZero = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "InterfaceIndexOrZero")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
TimeTicks, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, iso, ObjectIdentity, IpAddress, Counter64, Bits, Counter32, experimental, NotificationType, Unsigned32, Gauge32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "iso", "ObjectIdentity", "IpAddress", "Counter64", "Bits", "Counter32", "experimental", "NotificationType", "Unsigned32", "Gauge32", "MibIdentifier")
TruthValue, DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "RowStatus", "TextualConvention")
ipMRoute1MIB = ModuleIdentity((1, 3, 6, 1, 3, 60))
ipMRoute1MIB.setRevisions(('1999-07-22 12:00',))
if mibBuilder.loadTexts: ipMRoute1MIB.setLastUpdated('9907221200Z')
if mibBuilder.loadTexts: ipMRoute1MIB.setOrganization('IETF IDMR Working Group')
class IpMRoute1Protocol(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    namedValues = NamedValues(("other", 1), ("local", 2), ("netmgmt", 3), ("dvmrp", 4), ("mospf", 5), ("pimSparseDense", 6), ("cbt", 7), ("pimSparseMode", 8), ("pimDenseMode", 9), ("igmpOnly", 10), ("bgmp", 11), ("msdp", 12))

ipMRoute1MIBObjects = MibIdentifier((1, 3, 6, 1, 3, 60, 1))
ipMRoute1 = MibIdentifier((1, 3, 6, 1, 3, 60, 1, 1))
ipMRoute1Enable = MibScalar((1, 3, 6, 1, 3, 60, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipMRoute1Enable.setStatus('current')
ipMRoute1EntryCount = MibScalar((1, 3, 6, 1, 3, 60, 1, 1, 7), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipMRoute1EntryCount.setStatus('current')
ipMRoute1Table = MibTable((1, 3, 6, 1, 3, 60, 1, 1, 2), )
if mibBuilder.loadTexts: ipMRoute1Table.setStatus('current')
ipMRoute1Entry = MibTableRow((1, 3, 6, 1, 3, 60, 1, 1, 2, 1), ).setIndexNames((0, "IPMROUTE-MIB", "ipMRoute1Group"), (0, "IPMROUTE-MIB", "ipMRoute1Source"), (0, "IPMROUTE-MIB", "ipMRoute1SourceMask"))
if mibBuilder.loadTexts: ipMRoute1Entry.setStatus('current')
ipMRoute1Group = MibTableColumn((1, 3, 6, 1, 3, 60, 1, 1, 2, 1, 1), IpAddress())
if mibBuilder.loadTexts: ipMRoute1Group.setStatus('current')
ipMRoute1Source = MibTableColumn((1, 3, 6, 1, 3, 60, 1, 1, 2, 1, 2), IpAddress())
if mibBuilder.loadTexts: ipMRoute1Source.setStatus('current')
ipMRoute1SourceMask = MibTableColumn((1, 3, 6, 1, 3, 60, 1, 1, 2, 1, 3), IpAddress())
if mibBuilder.loadTexts: ipMRoute1SourceMask.setStatus('current')
ipMRoute1UpstreamNeighbor = MibTableColumn((1, 3, 6, 1, 3, 60, 1, 1, 2, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipMRoute1UpstreamNeighbor.setStatus('current')
ipMRoute1InIfIndex = MibTableColumn((1, 3, 6, 1, 3, 60, 1, 1, 2, 1, 5), InterfaceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipMRoute1InIfIndex.setStatus('current')
ipMRoute1UpTime = MibTableColumn((1, 3, 6, 1, 3, 60, 1, 1, 2, 1, 6), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipMRoute1UpTime.setStatus('current')
ipMRoute1ExpiryTime = MibTableColumn((1, 3, 6, 1, 3, 60, 1, 1, 2, 1, 7), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipMRoute1ExpiryTime.setStatus('current')
ipMRoute1Pkts = MibTableColumn((1, 3, 6, 1, 3, 60, 1, 1, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipMRoute1Pkts.setStatus('current')
ipMRoute1DifferentInIfPackets = MibTableColumn((1, 3, 6, 1, 3, 60, 1, 1, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipMRoute1DifferentInIfPackets.setStatus('current')
ipMRoute1Octets = MibTableColumn((1, 3, 6, 1, 3, 60, 1, 1, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipMRoute1Octets.setStatus('current')
ipMRoute1Protocol = MibTableColumn((1, 3, 6, 1, 3, 60, 1, 1, 2, 1, 11), IpMRoute1Protocol()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipMRoute1Protocol.setStatus('current')
ipMRoute1RtProto = MibTableColumn((1, 3, 6, 1, 3, 60, 1, 1, 2, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17))).clone(namedValues=NamedValues(("other", 1), ("local", 2), ("netmgmt", 3), ("icmp", 4), ("egp", 5), ("ggp", 6), ("hello", 7), ("rip", 8), ("isIs", 9), ("esIs", 10), ("ciscoIgrp", 11), ("bbnSpfIgp", 12), ("ospf", 13), ("bgp", 14), ("idpr", 15), ("ciscoEigrp", 16), ("dvmrp", 17)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipMRoute1RtProto.setStatus('current')
ipMRoute1RtAddress = MibTableColumn((1, 3, 6, 1, 3, 60, 1, 1, 2, 1, 13), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipMRoute1RtAddress.setStatus('current')
ipMRoute1RtMask = MibTableColumn((1, 3, 6, 1, 3, 60, 1, 1, 2, 1, 14), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipMRoute1RtMask.setStatus('current')
ipMRoute1RtType = MibTableColumn((1, 3, 6, 1, 3, 60, 1, 1, 2, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("unicast", 1), ("multicast", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipMRoute1RtType.setStatus('current')
ipMRoute1HCOctets = MibTableColumn((1, 3, 6, 1, 3, 60, 1, 1, 2, 1, 16), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipMRoute1HCOctets.setStatus('current')
ipMRoute1NextHopTable = MibTable((1, 3, 6, 1, 3, 60, 1, 1, 3), )
if mibBuilder.loadTexts: ipMRoute1NextHopTable.setStatus('current')
ipMRoute1NextHopEntry = MibTableRow((1, 3, 6, 1, 3, 60, 1, 1, 3, 1), ).setIndexNames((0, "IPMROUTE-MIB", "ipMRoute1NextHopGroup"), (0, "IPMROUTE-MIB", "ipMRoute1NextHopSource"), (0, "IPMROUTE-MIB", "ipMRoute1NextHopSourceMask"), (0, "IPMROUTE-MIB", "ipMRoute1NextHopIfIndex"), (0, "IPMROUTE-MIB", "ipMRoute1NextHopAddress"))
if mibBuilder.loadTexts: ipMRoute1NextHopEntry.setStatus('current')
ipMRoute1NextHopGroup = MibTableColumn((1, 3, 6, 1, 3, 60, 1, 1, 3, 1, 1), IpAddress())
if mibBuilder.loadTexts: ipMRoute1NextHopGroup.setStatus('current')
ipMRoute1NextHopSource = MibTableColumn((1, 3, 6, 1, 3, 60, 1, 1, 3, 1, 2), IpAddress())
if mibBuilder.loadTexts: ipMRoute1NextHopSource.setStatus('current')
ipMRoute1NextHopSourceMask = MibTableColumn((1, 3, 6, 1, 3, 60, 1, 1, 3, 1, 3), IpAddress())
if mibBuilder.loadTexts: ipMRoute1NextHopSourceMask.setStatus('current')
ipMRoute1NextHopIfIndex = MibTableColumn((1, 3, 6, 1, 3, 60, 1, 1, 3, 1, 4), InterfaceIndex())
if mibBuilder.loadTexts: ipMRoute1NextHopIfIndex.setStatus('current')
ipMRoute1NextHopAddress = MibTableColumn((1, 3, 6, 1, 3, 60, 1, 1, 3, 1, 5), IpAddress())
if mibBuilder.loadTexts: ipMRoute1NextHopAddress.setStatus('current')
ipMRoute1NextHopState = MibTableColumn((1, 3, 6, 1, 3, 60, 1, 1, 3, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("pruned", 1), ("forwarding", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipMRoute1NextHopState.setStatus('current')
ipMRoute1NextHopUpTime = MibTableColumn((1, 3, 6, 1, 3, 60, 1, 1, 3, 1, 7), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipMRoute1NextHopUpTime.setStatus('current')
ipMRoute1NextHopExpiryTime = MibTableColumn((1, 3, 6, 1, 3, 60, 1, 1, 3, 1, 8), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipMRoute1NextHopExpiryTime.setStatus('current')
ipMRoute1NextHopClosestMemberHops = MibTableColumn((1, 3, 6, 1, 3, 60, 1, 1, 3, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipMRoute1NextHopClosestMemberHops.setStatus('current')
ipMRoute1NextHopProtocol = MibTableColumn((1, 3, 6, 1, 3, 60, 1, 1, 3, 1, 10), IpMRoute1Protocol()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipMRoute1NextHopProtocol.setStatus('current')
ipMRoute1NextHopPkts = MibTableColumn((1, 3, 6, 1, 3, 60, 1, 1, 3, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipMRoute1NextHopPkts.setStatus('current')
ipMRoute1InterfaceTable = MibTable((1, 3, 6, 1, 3, 60, 1, 1, 4), )
if mibBuilder.loadTexts: ipMRoute1InterfaceTable.setStatus('current')
ipMRoute1InterfaceEntry = MibTableRow((1, 3, 6, 1, 3, 60, 1, 1, 4, 1), ).setIndexNames((0, "IPMROUTE-MIB", "ipMRoute1InterfaceIfIndex"))
if mibBuilder.loadTexts: ipMRoute1InterfaceEntry.setStatus('current')
ipMRoute1InterfaceIfIndex = MibTableColumn((1, 3, 6, 1, 3, 60, 1, 1, 4, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: ipMRoute1InterfaceIfIndex.setStatus('current')
ipMRoute1InterfaceTtl = MibTableColumn((1, 3, 6, 1, 3, 60, 1, 1, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipMRoute1InterfaceTtl.setStatus('current')
ipMRoute1InterfaceProtocol = MibTableColumn((1, 3, 6, 1, 3, 60, 1, 1, 4, 1, 3), IpMRoute1Protocol()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipMRoute1InterfaceProtocol.setStatus('current')
ipMRoute1InterfaceRateLimit = MibTableColumn((1, 3, 6, 1, 3, 60, 1, 1, 4, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipMRoute1InterfaceRateLimit.setStatus('current')
ipMRoute1InterfaceInMcastOctets = MibTableColumn((1, 3, 6, 1, 3, 60, 1, 1, 4, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipMRoute1InterfaceInMcastOctets.setStatus('current')
ipMRoute1InterfaceOutMcastOctets = MibTableColumn((1, 3, 6, 1, 3, 60, 1, 1, 4, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipMRoute1InterfaceOutMcastOctets.setStatus('current')
ipMRoute1InterfaceHCInMcastOctets = MibTableColumn((1, 3, 6, 1, 3, 60, 1, 1, 4, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipMRoute1InterfaceHCInMcastOctets.setStatus('current')
ipMRoute1InterfaceHCOutMcastOctets = MibTableColumn((1, 3, 6, 1, 3, 60, 1, 1, 4, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipMRoute1InterfaceHCOutMcastOctets.setStatus('current')
ipMRoute1BoundaryTable = MibTable((1, 3, 6, 1, 3, 60, 1, 1, 5), )
if mibBuilder.loadTexts: ipMRoute1BoundaryTable.setStatus('current')
ipMRoute1BoundaryEntry = MibTableRow((1, 3, 6, 1, 3, 60, 1, 1, 5, 1), ).setIndexNames((0, "IPMROUTE-MIB", "ipMRoute1BoundaryIfIndex"), (0, "IPMROUTE-MIB", "ipMRoute1BoundaryAddress"), (0, "IPMROUTE-MIB", "ipMRoute1BoundaryAddressMask"))
if mibBuilder.loadTexts: ipMRoute1BoundaryEntry.setStatus('current')
ipMRoute1BoundaryIfIndex = MibTableColumn((1, 3, 6, 1, 3, 60, 1, 1, 5, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: ipMRoute1BoundaryIfIndex.setStatus('current')
ipMRoute1BoundaryAddress = MibTableColumn((1, 3, 6, 1, 3, 60, 1, 1, 5, 1, 2), IpAddress())
if mibBuilder.loadTexts: ipMRoute1BoundaryAddress.setStatus('current')
ipMRoute1BoundaryAddressMask = MibTableColumn((1, 3, 6, 1, 3, 60, 1, 1, 5, 1, 3), IpAddress())
if mibBuilder.loadTexts: ipMRoute1BoundaryAddressMask.setStatus('current')
ipMRoute1BoundaryStatus = MibTableColumn((1, 3, 6, 1, 3, 60, 1, 1, 5, 1, 4), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipMRoute1BoundaryStatus.setStatus('current')
ipMRoute1ScopeNameTable = MibTable((1, 3, 6, 1, 3, 60, 1, 1, 6), )
if mibBuilder.loadTexts: ipMRoute1ScopeNameTable.setStatus('current')
ipMRoute1ScopeNameEntry = MibTableRow((1, 3, 6, 1, 3, 60, 1, 1, 6, 1), ).setIndexNames((0, "IPMROUTE-MIB", "ipMRoute1ScopeNameAddress"), (0, "IPMROUTE-MIB", "ipMRoute1ScopeNameAddressMask"), (1, "IPMROUTE-MIB", "ipMRoute1ScopeNameLanguage"))
if mibBuilder.loadTexts: ipMRoute1ScopeNameEntry.setStatus('current')
ipMRoute1ScopeNameAddress = MibTableColumn((1, 3, 6, 1, 3, 60, 1, 1, 6, 1, 1), IpAddress())
if mibBuilder.loadTexts: ipMRoute1ScopeNameAddress.setStatus('current')
ipMRoute1ScopeNameAddressMask = MibTableColumn((1, 3, 6, 1, 3, 60, 1, 1, 6, 1, 2), IpAddress())
if mibBuilder.loadTexts: ipMRoute1ScopeNameAddressMask.setStatus('current')
ipMRoute1ScopeNameLanguage = MibTableColumn((1, 3, 6, 1, 3, 60, 1, 1, 6, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 8)))
if mibBuilder.loadTexts: ipMRoute1ScopeNameLanguage.setStatus('current')
ipMRoute1ScopeNameString = MibTableColumn((1, 3, 6, 1, 3, 60, 1, 1, 6, 1, 4), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipMRoute1ScopeNameString.setStatus('current')
ipMRoute1ScopeNameDefault = MibTableColumn((1, 3, 6, 1, 3, 60, 1, 1, 6, 1, 5), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipMRoute1ScopeNameDefault.setStatus('current')
ipMRoute1ScopeNameStatus = MibTableColumn((1, 3, 6, 1, 3, 60, 1, 1, 6, 1, 6), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipMRoute1ScopeNameStatus.setStatus('current')
ipMRoute1MIBConformance = MibIdentifier((1, 3, 6, 1, 3, 60, 2))
ipMRoute1MIBCompliances = MibIdentifier((1, 3, 6, 1, 3, 60, 2, 1))
ipMRoute1MIBGroups = MibIdentifier((1, 3, 6, 1, 3, 60, 2, 2))
ipMRoute1MIBCompliance = ModuleCompliance((1, 3, 6, 1, 3, 60, 2, 1, 1)).setObjects(("IPMROUTE-MIB", "ipMRoute1MIBBasicGroup"), ("IPMROUTE-MIB", "ipMRoute1MIBRouteGroup"), ("IPMROUTE-MIB", "ipMRoute1MIBBoundaryGroup"), ("IPMROUTE-MIB", "ipMRoute1MIBHCInterfaceGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ipMRoute1MIBCompliance = ipMRoute1MIBCompliance.setStatus('current')
ipMRoute1MIBBasicGroup = ObjectGroup((1, 3, 6, 1, 3, 60, 2, 2, 1)).setObjects(("IPMROUTE-MIB", "ipMRoute1Enable"), ("IPMROUTE-MIB", "ipMRoute1EntryCount"), ("IPMROUTE-MIB", "ipMRoute1UpstreamNeighbor"), ("IPMROUTE-MIB", "ipMRoute1InIfIndex"), ("IPMROUTE-MIB", "ipMRoute1UpTime"), ("IPMROUTE-MIB", "ipMRoute1ExpiryTime"), ("IPMROUTE-MIB", "ipMRoute1NextHopState"), ("IPMROUTE-MIB", "ipMRoute1NextHopUpTime"), ("IPMROUTE-MIB", "ipMRoute1NextHopExpiryTime"), ("IPMROUTE-MIB", "ipMRoute1NextHopProtocol"), ("IPMROUTE-MIB", "ipMRoute1NextHopPkts"), ("IPMROUTE-MIB", "ipMRoute1InterfaceTtl"), ("IPMROUTE-MIB", "ipMRoute1InterfaceProtocol"), ("IPMROUTE-MIB", "ipMRoute1InterfaceRateLimit"), ("IPMROUTE-MIB", "ipMRoute1InterfaceInMcastOctets"), ("IPMROUTE-MIB", "ipMRoute1InterfaceOutMcastOctets"), ("IPMROUTE-MIB", "ipMRoute1Protocol"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ipMRoute1MIBBasicGroup = ipMRoute1MIBBasicGroup.setStatus('current')
ipMRoute1MIBHopCountGroup = ObjectGroup((1, 3, 6, 1, 3, 60, 2, 2, 2)).setObjects(("IPMROUTE-MIB", "ipMRoute1NextHopClosestMemberHops"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ipMRoute1MIBHopCountGroup = ipMRoute1MIBHopCountGroup.setStatus('current')
ipMRoute1MIBBoundaryGroup = ObjectGroup((1, 3, 6, 1, 3, 60, 2, 2, 3)).setObjects(("IPMROUTE-MIB", "ipMRoute1BoundaryStatus"), ("IPMROUTE-MIB", "ipMRoute1ScopeNameString"), ("IPMROUTE-MIB", "ipMRoute1ScopeNameDefault"), ("IPMROUTE-MIB", "ipMRoute1ScopeNameStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ipMRoute1MIBBoundaryGroup = ipMRoute1MIBBoundaryGroup.setStatus('current')
ipMRoute1MIBPktsOutGroup = ObjectGroup((1, 3, 6, 1, 3, 60, 2, 2, 4)).setObjects(("IPMROUTE-MIB", "ipMRoute1NextHopPkts"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ipMRoute1MIBPktsOutGroup = ipMRoute1MIBPktsOutGroup.setStatus('current')
ipMRoute1MIBHCInterfaceGroup = ObjectGroup((1, 3, 6, 1, 3, 60, 2, 2, 5)).setObjects(("IPMROUTE-MIB", "ipMRoute1InterfaceHCInMcastOctets"), ("IPMROUTE-MIB", "ipMRoute1InterfaceHCOutMcastOctets"), ("IPMROUTE-MIB", "ipMRoute1HCOctets"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ipMRoute1MIBHCInterfaceGroup = ipMRoute1MIBHCInterfaceGroup.setStatus('current')
ipMRoute1MIBRouteGroup = ObjectGroup((1, 3, 6, 1, 3, 60, 2, 2, 6)).setObjects(("IPMROUTE-MIB", "ipMRoute1RtProto"), ("IPMROUTE-MIB", "ipMRoute1RtAddress"), ("IPMROUTE-MIB", "ipMRoute1RtMask"), ("IPMROUTE-MIB", "ipMRoute1RtType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ipMRoute1MIBRouteGroup = ipMRoute1MIBRouteGroup.setStatus('current')
ipMRoute1MIBPktsGroup = ObjectGroup((1, 3, 6, 1, 3, 60, 2, 2, 7)).setObjects(("IPMROUTE-MIB", "ipMRoute1Pkts"), ("IPMROUTE-MIB", "ipMRoute1DifferentInIfPackets"), ("IPMROUTE-MIB", "ipMRoute1Octets"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ipMRoute1MIBPktsGroup = ipMRoute1MIBPktsGroup.setStatus('current')
mibBuilder.exportSymbols("IPMROUTE-MIB", ipMRoute1InterfaceOutMcastOctets=ipMRoute1InterfaceOutMcastOctets, ipMRoute1UpstreamNeighbor=ipMRoute1UpstreamNeighbor, PYSNMP_MODULE_ID=ipMRoute1MIB, ipMRoute1Source=ipMRoute1Source, ipMRoute1Pkts=ipMRoute1Pkts, ipMRoute1InterfaceTable=ipMRoute1InterfaceTable, ipMRoute1BoundaryStatus=ipMRoute1BoundaryStatus, IpMRoute1Protocol=IpMRoute1Protocol, ipMRoute1InterfaceEntry=ipMRoute1InterfaceEntry, ipMRoute1InterfaceHCOutMcastOctets=ipMRoute1InterfaceHCOutMcastOctets, ipMRoute1BoundaryEntry=ipMRoute1BoundaryEntry, ipMRoute1RtAddress=ipMRoute1RtAddress, ipMRoute1InIfIndex=ipMRoute1InIfIndex, ipMRoute1InterfaceProtocol=ipMRoute1InterfaceProtocol, ipMRoute1MIBRouteGroup=ipMRoute1MIBRouteGroup, ipMRoute1DifferentInIfPackets=ipMRoute1DifferentInIfPackets, ipMRoute1HCOctets=ipMRoute1HCOctets, ipMRoute1Protocol=ipMRoute1Protocol, ipMRoute1RtProto=ipMRoute1RtProto, ipMRoute1EntryCount=ipMRoute1EntryCount, ipMRoute1NextHopProtocol=ipMRoute1NextHopProtocol, ipMRoute1MIBConformance=ipMRoute1MIBConformance, ipMRoute1NextHopGroup=ipMRoute1NextHopGroup, ipMRoute1ScopeNameAddress=ipMRoute1ScopeNameAddress, ipMRoute1Entry=ipMRoute1Entry, ipMRoute1BoundaryAddressMask=ipMRoute1BoundaryAddressMask, ipMRoute1ScopeNameString=ipMRoute1ScopeNameString, ipMRoute1MIBPktsGroup=ipMRoute1MIBPktsGroup, ipMRoute1UpTime=ipMRoute1UpTime, ipMRoute1NextHopSource=ipMRoute1NextHopSource, ipMRoute1BoundaryTable=ipMRoute1BoundaryTable, ipMRoute1RtType=ipMRoute1RtType, ipMRoute1NextHopSourceMask=ipMRoute1NextHopSourceMask, ipMRoute1BoundaryIfIndex=ipMRoute1BoundaryIfIndex, ipMRoute1MIBGroups=ipMRoute1MIBGroups, ipMRoute1NextHopState=ipMRoute1NextHopState, ipMRoute1InterfaceTtl=ipMRoute1InterfaceTtl, ipMRoute1NextHopIfIndex=ipMRoute1NextHopIfIndex, ipMRoute1NextHopExpiryTime=ipMRoute1NextHopExpiryTime, ipMRoute1NextHopClosestMemberHops=ipMRoute1NextHopClosestMemberHops, ipMRoute1BoundaryAddress=ipMRoute1BoundaryAddress, ipMRoute1MIBBasicGroup=ipMRoute1MIBBasicGroup, ipMRoute1ScopeNameAddressMask=ipMRoute1ScopeNameAddressMask, ipMRoute1ScopeNameDefault=ipMRoute1ScopeNameDefault, ipMRoute1MIBCompliance=ipMRoute1MIBCompliance, ipMRoute1NextHopPkts=ipMRoute1NextHopPkts, ipMRoute1NextHopTable=ipMRoute1NextHopTable, ipMRoute1InterfaceInMcastOctets=ipMRoute1InterfaceInMcastOctets, ipMRoute1ScopeNameEntry=ipMRoute1ScopeNameEntry, ipMRoute1=ipMRoute1, ipMRoute1ScopeNameLanguage=ipMRoute1ScopeNameLanguage, ipMRoute1ScopeNameStatus=ipMRoute1ScopeNameStatus, ipMRoute1MIBHCInterfaceGroup=ipMRoute1MIBHCInterfaceGroup, ipMRoute1NextHopEntry=ipMRoute1NextHopEntry, ipMRoute1MIBCompliances=ipMRoute1MIBCompliances, ipMRoute1MIBHopCountGroup=ipMRoute1MIBHopCountGroup, ipMRoute1RtMask=ipMRoute1RtMask, ipMRoute1MIBObjects=ipMRoute1MIBObjects, ipMRoute1Enable=ipMRoute1Enable, ipMRoute1InterfaceRateLimit=ipMRoute1InterfaceRateLimit, ipMRoute1MIB=ipMRoute1MIB, ipMRoute1MIBPktsOutGroup=ipMRoute1MIBPktsOutGroup, ipMRoute1ScopeNameTable=ipMRoute1ScopeNameTable, ipMRoute1Table=ipMRoute1Table, ipMRoute1NextHopAddress=ipMRoute1NextHopAddress, ipMRoute1Group=ipMRoute1Group, ipMRoute1SourceMask=ipMRoute1SourceMask, ipMRoute1ExpiryTime=ipMRoute1ExpiryTime, ipMRoute1Octets=ipMRoute1Octets, ipMRoute1InterfaceIfIndex=ipMRoute1InterfaceIfIndex, ipMRoute1MIBBoundaryGroup=ipMRoute1MIBBoundaryGroup, ipMRoute1NextHopUpTime=ipMRoute1NextHopUpTime, ipMRoute1InterfaceHCInMcastOctets=ipMRoute1InterfaceHCInMcastOctets)
