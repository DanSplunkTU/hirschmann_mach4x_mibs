#
# PySNMP MIB module MPLS-TE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/MPLS-TE-MIB
# Produced by pysmi-1.1.0 at Mon Nov 15 18:46:22 2021
# On host fv-az77-248 platform Linux version 5.11.0-1020-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
InetAddressIPv6, InetAddressIPv4 = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressIPv6", "InetAddressIPv4")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
experimental, ModuleIdentity, Unsigned32, Bits, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, iso, Integer32, Counter32, Counter64, TimeTicks, ObjectIdentity, NotificationType, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "experimental", "ModuleIdentity", "Unsigned32", "Bits", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "iso", "Integer32", "Counter32", "Counter64", "TimeTicks", "ObjectIdentity", "NotificationType", "Gauge32")
RowPointer, StorageType, TruthValue, DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "RowPointer", "StorageType", "TruthValue", "DisplayString", "TextualConvention", "RowStatus")
mplsTeMIB = ModuleIdentity((1, 3, 6, 1, 3, 95))
mplsTeMIB.setRevisions(('2000-07-14 12:00', '2000-05-26 12:00', '2000-03-03 12:00', '1999-07-16 12:00',))
if mibBuilder.loadTexts: mplsTeMIB.setLastUpdated('200007141200Z')
if mibBuilder.loadTexts: mplsTeMIB.setOrganization('Multiprotocol Label Switching (MPLS) Working Group')
class MplsLSPID(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 31)

class MplsBitRate(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class MplsBurstSize(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class MplsTunnelIndex(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 65535)

mplsTeObjects = MibIdentifier((1, 3, 6, 1, 3, 95, 1))
mplsTeNotifications = MibIdentifier((1, 3, 6, 1, 3, 95, 2))
mplsTeNotifyPrefix = MibIdentifier((1, 3, 6, 1, 3, 95, 2, 0))
mplsTeConformance = MibIdentifier((1, 3, 6, 1, 3, 95, 3))
mplsTunnelIndexNext = MibScalar((1, 3, 6, 1, 3, 95, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsTunnelIndexNext.setStatus('current')
mplsTunnelTable = MibTable((1, 3, 6, 1, 3, 95, 1, 2), )
if mibBuilder.loadTexts: mplsTunnelTable.setStatus('current')
mplsTunnelEntry = MibTableRow((1, 3, 6, 1, 3, 95, 1, 2, 1), ).setIndexNames((0, "MPLS-TE-MIB", "mplsTunnelIndex"), (0, "MPLS-TE-MIB", "mplsTunnelInstance"), (0, "MPLS-TE-MIB", "mplsTunnelIngressLSRId"))
if mibBuilder.loadTexts: mplsTunnelEntry.setStatus('current')
mplsTunnelIndex = MibTableColumn((1, 3, 6, 1, 3, 95, 1, 2, 1, 1), MplsTunnelIndex()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: mplsTunnelIndex.setStatus('current')
mplsTunnelInstance = MibTableColumn((1, 3, 6, 1, 3, 95, 1, 2, 1, 2), MplsTunnelIndex()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: mplsTunnelInstance.setStatus('current')
mplsTunnelIngressLSRId = MibTableColumn((1, 3, 6, 1, 3, 95, 1, 2, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: mplsTunnelIngressLSRId.setStatus('current')
mplsTunnelName = MibTableColumn((1, 3, 6, 1, 3, 95, 1, 2, 1, 4), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsTunnelName.setStatus('current')
mplsTunnelDescr = MibTableColumn((1, 3, 6, 1, 3, 95, 1, 2, 1, 5), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsTunnelDescr.setStatus('current')
mplsTunnelIsIf = MibTableColumn((1, 3, 6, 1, 3, 95, 1, 2, 1, 6), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsTunnelIsIf.setStatus('current')
mplsTunnelIfIndex = MibTableColumn((1, 3, 6, 1, 3, 95, 1, 2, 1, 7), InterfaceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsTunnelIfIndex.setStatus('current')
mplsTunnelXCPointer = MibTableColumn((1, 3, 6, 1, 3, 95, 1, 2, 1, 8), RowPointer()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsTunnelXCPointer.setStatus('current')
mplsTunnelSignallingProto = MibTableColumn((1, 3, 6, 1, 3, 95, 1, 2, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("rsvp", 2), ("crldp", 3), ("other", 4))).clone('none')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsTunnelSignallingProto.setStatus('current')
mplsTunnelSetupPrio = MibTableColumn((1, 3, 6, 1, 3, 95, 1, 2, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsTunnelSetupPrio.setStatus('current')
mplsTunnelHoldingPrio = MibTableColumn((1, 3, 6, 1, 3, 95, 1, 2, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsTunnelHoldingPrio.setStatus('current')
mplsTunnelSessionAttributes = MibTableColumn((1, 3, 6, 1, 3, 95, 1, 2, 1, 12), Bits().clone(namedValues=NamedValues(("fastReroute", 0), ("mergingPermitted", 1), ("isPersistent", 2), ("localProtectionAvailable", 3), ("isPinned", 4)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsTunnelSessionAttributes.setStatus('current')
mplsTunnelOwner = MibTableColumn((1, 3, 6, 1, 3, 95, 1, 2, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("admin", 1), ("rsvp", 2), ("crldp", 3), ("policyAgent", 4), ("other", 5)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsTunnelOwner.setStatus('current')
mplsTunnelLocalProtectInUse = MibTableColumn((1, 3, 6, 1, 3, 95, 1, 2, 1, 14), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsTunnelLocalProtectInUse.setStatus('current')
mplsTunnelResourcePointer = MibTableColumn((1, 3, 6, 1, 3, 95, 1, 2, 1, 15), RowPointer()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsTunnelResourcePointer.setStatus('current')
mplsTunnelInstancePriority = MibTableColumn((1, 3, 6, 1, 3, 95, 1, 2, 1, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsTunnelInstancePriority.setStatus('current')
mplsTunnelHopTableIndex = MibTableColumn((1, 3, 6, 1, 3, 95, 1, 2, 1, 17), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsTunnelHopTableIndex.setStatus('current')
mplsTunnelARHopTableIndex = MibTableColumn((1, 3, 6, 1, 3, 95, 1, 2, 1, 18), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsTunnelARHopTableIndex.setStatus('current')
mplsTunnelAdminStatus = MibTableColumn((1, 3, 6, 1, 3, 95, 1, 2, 1, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("testing", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsTunnelAdminStatus.setStatus('current')
mplsTunnelOperStatus = MibTableColumn((1, 3, 6, 1, 3, 95, 1, 2, 1, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("testing", 3), ("unknown", 4), ("dormant", 5), ("notPresent", 6), ("lowerLayerDown", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsTunnelOperStatus.setStatus('current')
mplsTunnelRowStatus = MibTableColumn((1, 3, 6, 1, 3, 95, 1, 2, 1, 21), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsTunnelRowStatus.setStatus('current')
mplsTunnelStorageType = MibTableColumn((1, 3, 6, 1, 3, 95, 1, 2, 1, 22), StorageType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsTunnelStorageType.setStatus('current')
mplsTunnelMaxHops = MibScalar((1, 3, 6, 1, 3, 95, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsTunnelMaxHops.setStatus('current')
mplsTunnelHopIndexNext = MibScalar((1, 3, 6, 1, 3, 95, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsTunnelHopIndexNext.setStatus('current')
mplsTunnelHopTable = MibTable((1, 3, 6, 1, 3, 95, 1, 5), )
if mibBuilder.loadTexts: mplsTunnelHopTable.setStatus('current')
mplsTunnelHopEntry = MibTableRow((1, 3, 6, 1, 3, 95, 1, 5, 1), ).setIndexNames((0, "MPLS-TE-MIB", "mplsTunnelHopListIndex"), (0, "MPLS-TE-MIB", "mplsTunnelHopIndex"))
if mibBuilder.loadTexts: mplsTunnelHopEntry.setStatus('current')
mplsTunnelHopListIndex = MibTableColumn((1, 3, 6, 1, 3, 95, 1, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: mplsTunnelHopListIndex.setStatus('current')
mplsTunnelHopIndex = MibTableColumn((1, 3, 6, 1, 3, 95, 1, 5, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: mplsTunnelHopIndex.setStatus('current')
mplsTunnelHopAddrType = MibTableColumn((1, 3, 6, 1, 3, 95, 1, 5, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("ipV4", 1), ("ipV6", 2), ("asNumber", 3), ("lspid", 4))).clone('ipV4')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsTunnelHopAddrType.setStatus('current')
mplsTunnelHopIpv4Addr = MibTableColumn((1, 3, 6, 1, 3, 95, 1, 5, 1, 4), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsTunnelHopIpv4Addr.setStatus('current')
mplsTunnelHopIpv4PrefixLen = MibTableColumn((1, 3, 6, 1, 3, 95, 1, 5, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsTunnelHopIpv4PrefixLen.setStatus('current')
mplsTunnelHopIpv6Addr = MibTableColumn((1, 3, 6, 1, 3, 95, 1, 5, 1, 6), InetAddressIPv6()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsTunnelHopIpv6Addr.setStatus('current')
mplsTunnelHopIpv6PrefixLen = MibTableColumn((1, 3, 6, 1, 3, 95, 1, 5, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 128))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsTunnelHopIpv6PrefixLen.setStatus('current')
mplsTunnelHopAsNumber = MibTableColumn((1, 3, 6, 1, 3, 95, 1, 5, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsTunnelHopAsNumber.setStatus('current')
mplsTunnelHopLspId = MibTableColumn((1, 3, 6, 1, 3, 95, 1, 5, 1, 9), MplsLSPID()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsTunnelHopLspId.setStatus('current')
mplsTunnelHopStrictOrLoose = MibTableColumn((1, 3, 6, 1, 3, 95, 1, 5, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("strict", 1), ("loose", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsTunnelHopStrictOrLoose.setStatus('current')
mplsTunnelHopRowStatus = MibTableColumn((1, 3, 6, 1, 3, 95, 1, 5, 1, 11), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsTunnelHopRowStatus.setStatus('current')
mplsTunnelHopStorageType = MibTableColumn((1, 3, 6, 1, 3, 95, 1, 5, 1, 12), StorageType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsTunnelHopStorageType.setStatus('current')
mplsTunnelResourceIndexNext = MibScalar((1, 3, 6, 1, 3, 95, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsTunnelResourceIndexNext.setStatus('current')
mplsTunnelResourceTable = MibTable((1, 3, 6, 1, 3, 95, 1, 7), )
if mibBuilder.loadTexts: mplsTunnelResourceTable.setStatus('current')
mplsTunnelResourceEntry = MibTableRow((1, 3, 6, 1, 3, 95, 1, 7, 1), ).setIndexNames((0, "MPLS-TE-MIB", "mplsTunnelResourceIndex"))
if mibBuilder.loadTexts: mplsTunnelResourceEntry.setStatus('current')
mplsTunnelResourceIndex = MibTableColumn((1, 3, 6, 1, 3, 95, 1, 7, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: mplsTunnelResourceIndex.setStatus('current')
mplsTunnelResourceMaxRate = MibTableColumn((1, 3, 6, 1, 3, 95, 1, 7, 1, 2), MplsBitRate()).setUnits('bits per second').setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsTunnelResourceMaxRate.setStatus('current')
mplsTunnelResourceMeanRate = MibTableColumn((1, 3, 6, 1, 3, 95, 1, 7, 1, 3), MplsBitRate()).setUnits('bits per second').setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsTunnelResourceMeanRate.setStatus('current')
mplsTunnelResourceMaxBurstSize = MibTableColumn((1, 3, 6, 1, 3, 95, 1, 7, 1, 4), MplsBurstSize()).setUnits('bytes').setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsTunnelResourceMaxBurstSize.setStatus('current')
mplsTunnelResourceRowStatus = MibTableColumn((1, 3, 6, 1, 3, 95, 1, 7, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsTunnelResourceRowStatus.setStatus('current')
mplsTunnelResourceStorageType = MibTableColumn((1, 3, 6, 1, 3, 95, 1, 7, 1, 6), StorageType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsTunnelResourceStorageType.setStatus('current')
mplsTunnelARHopTable = MibTable((1, 3, 6, 1, 3, 95, 1, 8), )
if mibBuilder.loadTexts: mplsTunnelARHopTable.setStatus('current')
mplsTunnelARHopEntry = MibTableRow((1, 3, 6, 1, 3, 95, 1, 8, 1), ).setIndexNames((0, "MPLS-TE-MIB", "mplsTunnelARHopListIndex"), (0, "MPLS-TE-MIB", "mplsTunnelARHopIndex"))
if mibBuilder.loadTexts: mplsTunnelARHopEntry.setStatus('current')
mplsTunnelARHopListIndex = MibTableColumn((1, 3, 6, 1, 3, 95, 1, 8, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: mplsTunnelARHopListIndex.setStatus('current')
mplsTunnelARHopIndex = MibTableColumn((1, 3, 6, 1, 3, 95, 1, 8, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: mplsTunnelARHopIndex.setStatus('current')
mplsTunnelARHopAddrType = MibTableColumn((1, 3, 6, 1, 3, 95, 1, 8, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ipV4", 1), ("ipV6", 2), ("asNumber", 3))).clone('ipV4')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsTunnelARHopAddrType.setStatus('current')
mplsTunnelARHopIpv4Addr = MibTableColumn((1, 3, 6, 1, 3, 95, 1, 8, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsTunnelARHopIpv4Addr.setStatus('current')
mplsTunnelARHopIpv4PrefixLen = MibTableColumn((1, 3, 6, 1, 3, 95, 1, 8, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsTunnelARHopIpv4PrefixLen.setStatus('current')
mplsTunnelARHopIpv6Addr = MibTableColumn((1, 3, 6, 1, 3, 95, 1, 8, 1, 6), InetAddressIPv6()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsTunnelARHopIpv6Addr.setStatus('current')
mplsTunnelARHopIpv6PrefixLen = MibTableColumn((1, 3, 6, 1, 3, 95, 1, 8, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsTunnelARHopIpv6PrefixLen.setStatus('current')
mplsTunnelARHopAsNumber = MibTableColumn((1, 3, 6, 1, 3, 95, 1, 8, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsTunnelARHopAsNumber.setStatus('current')
mplsTunnelARHopStrictOrLoose = MibTableColumn((1, 3, 6, 1, 3, 95, 1, 8, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("strict", 1), ("loose", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsTunnelARHopStrictOrLoose.setStatus('current')
mplsTunnelTrapEnable = MibScalar((1, 3, 6, 1, 3, 95, 1, 9), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mplsTunnelTrapEnable.setStatus('current')
mplsTunnelUp = NotificationType((1, 3, 6, 1, 3, 95, 2, 0, 1)).setObjects(("MPLS-TE-MIB", "mplsTunnelIndex"), ("MPLS-TE-MIB", "mplsTunnelInstance"), ("MPLS-TE-MIB", "mplsTunnelAdminStatus"), ("MPLS-TE-MIB", "mplsTunnelOperStatus"))
if mibBuilder.loadTexts: mplsTunnelUp.setStatus('current')
mplsTunnelDown = NotificationType((1, 3, 6, 1, 3, 95, 2, 0, 2)).setObjects(("MPLS-TE-MIB", "mplsTunnelIndex"), ("MPLS-TE-MIB", "mplsTunnelInstance"), ("MPLS-TE-MIB", "mplsTunnelAdminStatus"), ("MPLS-TE-MIB", "mplsTunnelOperStatus"))
if mibBuilder.loadTexts: mplsTunnelDown.setStatus('current')
mplsTunnelRerouted = NotificationType((1, 3, 6, 1, 3, 95, 2, 0, 3)).setObjects(("MPLS-TE-MIB", "mplsTunnelIndex"), ("MPLS-TE-MIB", "mplsTunnelInstance"), ("MPLS-TE-MIB", "mplsTunnelAdminStatus"), ("MPLS-TE-MIB", "mplsTunnelOperStatus"))
if mibBuilder.loadTexts: mplsTunnelRerouted.setStatus('current')
mplsTunnelReoptimized = NotificationType((1, 3, 6, 1, 3, 95, 2, 0, 4)).setObjects(("MPLS-TE-MIB", "mplsTunnelIndex"), ("MPLS-TE-MIB", "mplsTunnelInstance"), ("MPLS-TE-MIB", "mplsTunnelIngressLSRId"), ("MPLS-TE-MIB", "mplsTunnelAdminStatus"), ("MPLS-TE-MIB", "mplsTunnelOperStatus"))
if mibBuilder.loadTexts: mplsTunnelReoptimized.setStatus('current')
mplsTeGroups = MibIdentifier((1, 3, 6, 1, 3, 95, 3, 1))
mplsTeCompliances = MibIdentifier((1, 3, 6, 1, 3, 95, 3, 2))
mplsTeModuleCompliance = ModuleCompliance((1, 3, 6, 1, 3, 95, 3, 2, 1)).setObjects(("MPLS-TE-MIB", "mplsTunnelGroup"), ("MPLS-TE-MIB", "mplsTunnelManualGroup"), ("MPLS-TE-MIB", "mplsTunnelSignaledGroup"), ("MPLS-TE-MIB", "mplsTunnelIsNotIntfcGroup"), ("MPLS-TE-MIB", "mplsTunnelIsIntfcGroup"), ("MPLS-TE-MIB", "mplsTunnelOptionalGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mplsTeModuleCompliance = mplsTeModuleCompliance.setStatus('current')
mplsTunnelGroup = ObjectGroup((1, 3, 6, 1, 3, 95, 3, 1, 1)).setObjects(("MPLS-TE-MIB", "mplsTunnelIndexNext"), ("MPLS-TE-MIB", "mplsTunnelName"), ("MPLS-TE-MIB", "mplsTunnelDescr"), ("MPLS-TE-MIB", "mplsTunnelOwner"), ("MPLS-TE-MIB", "mplsTunnelXCPointer"), ("MPLS-TE-MIB", "mplsTunnelIfIndex"), ("MPLS-TE-MIB", "mplsTunnelHopTableIndex"), ("MPLS-TE-MIB", "mplsTunnelARHopTableIndex"), ("MPLS-TE-MIB", "mplsTunnelAdminStatus"), ("MPLS-TE-MIB", "mplsTunnelOperStatus"), ("MPLS-TE-MIB", "mplsTunnelRowStatus"), ("MPLS-TE-MIB", "mplsTunnelTrapEnable"), ("MPLS-TE-MIB", "mplsTunnelStorageType"), ("MPLS-TE-MIB", "mplsTunnelMaxHops"), ("MPLS-TE-MIB", "mplsTunnelResourcePointer"), ("MPLS-TE-MIB", "mplsTunnelInstancePriority"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mplsTunnelGroup = mplsTunnelGroup.setStatus('current')
mplsTunnelManualGroup = ObjectGroup((1, 3, 6, 1, 3, 95, 3, 1, 2)).setObjects(("MPLS-TE-MIB", "mplsTunnelSignallingProto"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mplsTunnelManualGroup = mplsTunnelManualGroup.setStatus('current')
mplsTunnelSignaledGroup = ObjectGroup((1, 3, 6, 1, 3, 95, 3, 1, 3)).setObjects(("MPLS-TE-MIB", "mplsTunnelSetupPrio"), ("MPLS-TE-MIB", "mplsTunnelHoldingPrio"), ("MPLS-TE-MIB", "mplsTunnelSignallingProto"), ("MPLS-TE-MIB", "mplsTunnelLocalProtectInUse"), ("MPLS-TE-MIB", "mplsTunnelSessionAttributes"), ("MPLS-TE-MIB", "mplsTunnelHopIndexNext"), ("MPLS-TE-MIB", "mplsTunnelHopAddrType"), ("MPLS-TE-MIB", "mplsTunnelHopIpv4Addr"), ("MPLS-TE-MIB", "mplsTunnelHopIpv4PrefixLen"), ("MPLS-TE-MIB", "mplsTunnelHopIpv6Addr"), ("MPLS-TE-MIB", "mplsTunnelHopIpv6PrefixLen"), ("MPLS-TE-MIB", "mplsTunnelHopAsNumber"), ("MPLS-TE-MIB", "mplsTunnelHopLspId"), ("MPLS-TE-MIB", "mplsTunnelHopStrictOrLoose"), ("MPLS-TE-MIB", "mplsTunnelHopRowStatus"), ("MPLS-TE-MIB", "mplsTunnelHopStorageType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mplsTunnelSignaledGroup = mplsTunnelSignaledGroup.setStatus('current')
mplsTunnelIsIntfcGroup = ObjectGroup((1, 3, 6, 1, 3, 95, 3, 1, 4)).setObjects(("MPLS-TE-MIB", "mplsTunnelIsIf"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mplsTunnelIsIntfcGroup = mplsTunnelIsIntfcGroup.setStatus('current')
mplsTunnelIsNotIntfcGroup = ObjectGroup((1, 3, 6, 1, 3, 95, 3, 1, 5)).setObjects(("MPLS-TE-MIB", "mplsTunnelIsIf"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mplsTunnelIsNotIntfcGroup = mplsTunnelIsNotIntfcGroup.setStatus('current')
mplsTunnelOptionalGroup = ObjectGroup((1, 3, 6, 1, 3, 95, 3, 1, 6)).setObjects(("MPLS-TE-MIB", "mplsTunnelResourceIndexNext"), ("MPLS-TE-MIB", "mplsTunnelResourceMaxRate"), ("MPLS-TE-MIB", "mplsTunnelResourceMeanRate"), ("MPLS-TE-MIB", "mplsTunnelResourceMaxBurstSize"), ("MPLS-TE-MIB", "mplsTunnelResourceRowStatus"), ("MPLS-TE-MIB", "mplsTunnelResourceStorageType"), ("MPLS-TE-MIB", "mplsTunnelARHopAddrType"), ("MPLS-TE-MIB", "mplsTunnelARHopIpv4Addr"), ("MPLS-TE-MIB", "mplsTunnelARHopIpv4PrefixLen"), ("MPLS-TE-MIB", "mplsTunnelARHopIpv6Addr"), ("MPLS-TE-MIB", "mplsTunnelARHopIpv6PrefixLen"), ("MPLS-TE-MIB", "mplsTunnelARHopAsNumber"), ("MPLS-TE-MIB", "mplsTunnelARHopStrictOrLoose"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mplsTunnelOptionalGroup = mplsTunnelOptionalGroup.setStatus('current')
mplsTeNotificationGroup = NotificationGroup((1, 3, 6, 1, 3, 95, 3, 1, 7)).setObjects(("MPLS-TE-MIB", "mplsTunnelUp"), ("MPLS-TE-MIB", "mplsTunnelDown"), ("MPLS-TE-MIB", "mplsTunnelRerouted"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mplsTeNotificationGroup = mplsTeNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("MPLS-TE-MIB", mplsTunnelHopAsNumber=mplsTunnelHopAsNumber, mplsTunnelResourcePointer=mplsTunnelResourcePointer, mplsTunnelHopIndex=mplsTunnelHopIndex, mplsTunnelStorageType=mplsTunnelStorageType, mplsTunnelUp=mplsTunnelUp, MplsLSPID=MplsLSPID, mplsTunnelResourceIndexNext=mplsTunnelResourceIndexNext, mplsTunnelHopStrictOrLoose=mplsTunnelHopStrictOrLoose, mplsTunnelIsIntfcGroup=mplsTunnelIsIntfcGroup, MplsBitRate=MplsBitRate, mplsTunnelIsIf=mplsTunnelIsIf, mplsTunnelIfIndex=mplsTunnelIfIndex, mplsTunnelInstance=mplsTunnelInstance, mplsTunnelName=mplsTunnelName, mplsTeNotifyPrefix=mplsTeNotifyPrefix, mplsTeMIB=mplsTeMIB, mplsTunnelInstancePriority=mplsTunnelInstancePriority, mplsTeGroups=mplsTeGroups, mplsTunnelARHopStrictOrLoose=mplsTunnelARHopStrictOrLoose, mplsTunnelARHopAsNumber=mplsTunnelARHopAsNumber, mplsTunnelOperStatus=mplsTunnelOperStatus, mplsTunnelARHopIndex=mplsTunnelARHopIndex, MplsBurstSize=MplsBurstSize, mplsTunnelHopTableIndex=mplsTunnelHopTableIndex, mplsTunnelTable=mplsTunnelTable, mplsTunnelHopTable=mplsTunnelHopTable, mplsTunnelResourceMeanRate=mplsTunnelResourceMeanRate, mplsTunnelHopIpv4Addr=mplsTunnelHopIpv4Addr, mplsTunnelLocalProtectInUse=mplsTunnelLocalProtectInUse, PYSNMP_MODULE_ID=mplsTeMIB, mplsTunnelHoldingPrio=mplsTunnelHoldingPrio, mplsTunnelHopIndexNext=mplsTunnelHopIndexNext, mplsTunnelResourceIndex=mplsTunnelResourceIndex, mplsTunnelARHopIpv6Addr=mplsTunnelARHopIpv6Addr, mplsTunnelIsNotIntfcGroup=mplsTunnelIsNotIntfcGroup, mplsTunnelHopIpv6PrefixLen=mplsTunnelHopIpv6PrefixLen, mplsTunnelResourceStorageType=mplsTunnelResourceStorageType, mplsTunnelResourceEntry=mplsTunnelResourceEntry, mplsTunnelHopIpv6Addr=mplsTunnelHopIpv6Addr, mplsTunnelSignaledGroup=mplsTunnelSignaledGroup, mplsTunnelManualGroup=mplsTunnelManualGroup, mplsTunnelOptionalGroup=mplsTunnelOptionalGroup, mplsTunnelTrapEnable=mplsTunnelTrapEnable, mplsTunnelSessionAttributes=mplsTunnelSessionAttributes, mplsTunnelARHopIpv4PrefixLen=mplsTunnelARHopIpv4PrefixLen, mplsTunnelReoptimized=mplsTunnelReoptimized, mplsTunnelOwner=mplsTunnelOwner, mplsTunnelEntry=mplsTunnelEntry, mplsTunnelARHopAddrType=mplsTunnelARHopAddrType, mplsTunnelGroup=mplsTunnelGroup, mplsTunnelHopListIndex=mplsTunnelHopListIndex, mplsTunnelHopEntry=mplsTunnelHopEntry, mplsTunnelMaxHops=mplsTunnelMaxHops, mplsTeNotifications=mplsTeNotifications, mplsTunnelResourceMaxRate=mplsTunnelResourceMaxRate, mplsTunnelARHopTable=mplsTunnelARHopTable, MplsTunnelIndex=MplsTunnelIndex, mplsTunnelHopLspId=mplsTunnelHopLspId, mplsTeConformance=mplsTeConformance, mplsTunnelResourceRowStatus=mplsTunnelResourceRowStatus, mplsTunnelRowStatus=mplsTunnelRowStatus, mplsTeCompliances=mplsTeCompliances, mplsTunnelHopRowStatus=mplsTunnelHopRowStatus, mplsTunnelResourceTable=mplsTunnelResourceTable, mplsTeObjects=mplsTeObjects, mplsTunnelARHopTableIndex=mplsTunnelARHopTableIndex, mplsTunnelSetupPrio=mplsTunnelSetupPrio, mplsTunnelHopIpv4PrefixLen=mplsTunnelHopIpv4PrefixLen, mplsTeNotificationGroup=mplsTeNotificationGroup, mplsTeModuleCompliance=mplsTeModuleCompliance, mplsTunnelHopAddrType=mplsTunnelHopAddrType, mplsTunnelIndex=mplsTunnelIndex, mplsTunnelRerouted=mplsTunnelRerouted, mplsTunnelResourceMaxBurstSize=mplsTunnelResourceMaxBurstSize, mplsTunnelARHopIpv6PrefixLen=mplsTunnelARHopIpv6PrefixLen, mplsTunnelSignallingProto=mplsTunnelSignallingProto, mplsTunnelDescr=mplsTunnelDescr, mplsTunnelXCPointer=mplsTunnelXCPointer, mplsTunnelARHopIpv4Addr=mplsTunnelARHopIpv4Addr, mplsTunnelAdminStatus=mplsTunnelAdminStatus, mplsTunnelARHopEntry=mplsTunnelARHopEntry, mplsTunnelIndexNext=mplsTunnelIndexNext, mplsTunnelARHopListIndex=mplsTunnelARHopListIndex, mplsTunnelHopStorageType=mplsTunnelHopStorageType, mplsTunnelIngressLSRId=mplsTunnelIngressLSRId, mplsTunnelDown=mplsTunnelDown)
