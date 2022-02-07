#
# PySNMP MIB module ATM-FORUM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/atmforum/ATM-FORUM-MIB
# Produced by pysmi-1.1.8 at Mon Feb  7 16:06:15 2022
# On host fv-az42-619 platform Linux version 5.11.0-1028-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, MibIdentifier, iso, enterprises, ObjectIdentity, Bits, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, IpAddress, ModuleIdentity, Counter64, Gauge32, NotificationType, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "MibIdentifier", "iso", "enterprises", "ObjectIdentity", "Bits", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "IpAddress", "ModuleIdentity", "Counter64", "Gauge32", "NotificationType", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
atmForum = MibIdentifier((1, 3, 6, 1, 4, 1, 353))
atmForumAdmin = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 1))
atmForumUni = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 2))
class AtmAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class AtmAddress2(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(8, 8), ValueSizeConstraint(20, 20), )
class NetPrefix(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(8, 8), ValueSizeConstraint(13, 13), )
atmfTransmissionTypes = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 1, 2))
atmfUnknownType = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 1, 2, 1))
atmfSonetSTS3c = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 1, 2, 2))
atmfDs3 = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 1, 2, 3))
atmf4B5B = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 1, 2, 4))
atmf8B10B = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 1, 2, 5))
atmfMediaTypes = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 1, 3))
atmfMediaUnknownType = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 1, 3, 1))
atmfMediaCoaxCable = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 1, 3, 2))
atmfMediaSingleMode = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 1, 3, 3))
atmfMediaMultiMode = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 1, 3, 4))
atmfMediaStp = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 1, 3, 5))
atmfMediaUtp = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 1, 3, 6))
atmfTrafficDescrTypes = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 1, 4))
atmfNoDescriptor = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 1, 4, 1))
atmfPeakRate = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 1, 4, 2))
atmfNoClpNoScr = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 1, 4, 3))
atmfClpNoTaggingNoScr = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 1, 4, 4))
atmfClpTaggingNoScr = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 1, 4, 5))
atmfNoClpScr = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 1, 4, 6))
atmfClpNoTaggingScr = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 1, 4, 7))
atmfClpTaggingScr = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 1, 4, 8))
atmfPhysicalGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 2, 1))
atmfAtmLayerGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 2, 2))
atmfAtmStatsGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 2, 3))
atmfVpcGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 2, 4))
atmfVccGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 2, 5))
atmfAddressGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 2, 6))
atmfNetPrefixGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 2, 7))
atmfPortTable = MibTable((1, 3, 6, 1, 4, 1, 353, 2, 1, 1), )
if mibBuilder.loadTexts: atmfPortTable.setStatus('mandatory')
atmfPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 353, 2, 1, 1, 1), ).setIndexNames((0, "ATM-FORUM-MIB", "atmfPortIndex"))
if mibBuilder.loadTexts: atmfPortEntry.setStatus('mandatory')
atmfPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 2, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfPortIndex.setStatus('mandatory')
atmfPortAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 2, 1, 1, 1, 2), AtmAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfPortAddress.setStatus('deprecated')
atmfPortTransmissionType = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 2, 1, 1, 1, 3), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfPortTransmissionType.setStatus('mandatory')
atmfPortMediaType = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 2, 1, 1, 1, 4), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfPortMediaType.setStatus('mandatory')
atmfPortOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 2, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("inService", 2), ("outOfService", 3), ("loopBack", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfPortOperStatus.setStatus('mandatory')
atmfPortSpecific = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 2, 1, 1, 1, 6), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfPortSpecific.setStatus('mandatory')
atmfPortMyIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 2, 1, 1, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfPortMyIfName.setStatus('mandatory')
atmfMyIpNmAddress = MibScalar((1, 3, 6, 1, 4, 1, 353, 2, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfMyIpNmAddress.setStatus('mandatory')
atmfAtmLayerTable = MibTable((1, 3, 6, 1, 4, 1, 353, 2, 2, 1), )
if mibBuilder.loadTexts: atmfAtmLayerTable.setStatus('mandatory')
atmfAtmLayerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 353, 2, 2, 1, 1), ).setIndexNames((0, "ATM-FORUM-MIB", "atmfAtmLayerIndex"))
if mibBuilder.loadTexts: atmfAtmLayerEntry.setStatus('mandatory')
atmfAtmLayerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 2, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfAtmLayerIndex.setStatus('mandatory')
atmfAtmLayerMaxVPCs = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 2, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfAtmLayerMaxVPCs.setStatus('mandatory')
atmfAtmLayerMaxVCCs = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 2, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 16777215))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfAtmLayerMaxVCCs.setStatus('mandatory')
atmfAtmLayerConfiguredVPCs = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 2, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfAtmLayerConfiguredVPCs.setStatus('mandatory')
atmfAtmLayerConfiguredVCCs = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 2, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 16777215))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfAtmLayerConfiguredVCCs.setStatus('mandatory')
atmfAtmLayerMaxVpiBits = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 2, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfAtmLayerMaxVpiBits.setStatus('mandatory')
atmfAtmLayerMaxVciBits = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 2, 2, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfAtmLayerMaxVciBits.setStatus('mandatory')
atmfAtmLayerUniType = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 2, 2, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("public", 1), ("private", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfAtmLayerUniType.setStatus('mandatory')
atmfAtmLayerUniVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 2, 2, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("version2point0", 1), ("version3point0", 2), ("version3point1", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfAtmLayerUniVersion.setStatus('mandatory')
atmfAtmStatsTable = MibTable((1, 3, 6, 1, 4, 1, 353, 2, 3, 1), )
if mibBuilder.loadTexts: atmfAtmStatsTable.setStatus('mandatory')
atmfAtmStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 353, 2, 3, 1, 1), ).setIndexNames((0, "ATM-FORUM-MIB", "atmfAtmStatsIndex"))
if mibBuilder.loadTexts: atmfAtmStatsEntry.setStatus('mandatory')
atmfAtmStatsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 2, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfAtmStatsIndex.setStatus('mandatory')
atmfAtmStatsReceivedCells = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 2, 3, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfAtmStatsReceivedCells.setStatus('mandatory')
atmfAtmStatsDroppedReceivedCells = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 2, 3, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfAtmStatsDroppedReceivedCells.setStatus('mandatory')
atmfAtmStatsTransmittedCells = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 2, 3, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfAtmStatsTransmittedCells.setStatus('mandatory')
atmfVpcTable = MibTable((1, 3, 6, 1, 4, 1, 353, 2, 4, 1), )
if mibBuilder.loadTexts: atmfVpcTable.setStatus('mandatory')
atmfVpcEntry = MibTableRow((1, 3, 6, 1, 4, 1, 353, 2, 4, 1, 1), ).setIndexNames((0, "ATM-FORUM-MIB", "atmfVpcPortIndex"), (0, "ATM-FORUM-MIB", "atmfVpcVpi"))
if mibBuilder.loadTexts: atmfVpcEntry.setStatus('mandatory')
atmfVpcPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 2, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfVpcPortIndex.setStatus('mandatory')
atmfVpcVpi = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 2, 4, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfVpcVpi.setStatus('mandatory')
atmfVpcOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 2, 4, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("unknown", 1), ("end2endUp", 2), ("end2endDown", 3), ("localUpEnd2endUnknown", 4), ("localDown", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfVpcOperStatus.setStatus('mandatory')
atmfVpcTransmitTrafficDescriptorType = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 2, 4, 1, 1, 4), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfVpcTransmitTrafficDescriptorType.setStatus('mandatory')
atmfVpcTransmitTrafficDescriptorParam1 = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 2, 4, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfVpcTransmitTrafficDescriptorParam1.setStatus('mandatory')
atmfVpcTransmitTrafficDescriptorParam2 = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 2, 4, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfVpcTransmitTrafficDescriptorParam2.setStatus('mandatory')
atmfVpcTransmitTrafficDescriptorParam3 = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 2, 4, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfVpcTransmitTrafficDescriptorParam3.setStatus('mandatory')
atmfVpcTransmitTrafficDescriptorParam4 = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 2, 4, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfVpcTransmitTrafficDescriptorParam4.setStatus('mandatory')
atmfVpcTransmitTrafficDescriptorParam5 = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 2, 4, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfVpcTransmitTrafficDescriptorParam5.setStatus('mandatory')
atmfVpcReceiveTrafficDescriptorType = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 2, 4, 1, 1, 10), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfVpcReceiveTrafficDescriptorType.setStatus('mandatory')
atmfVpcReceiveTrafficDescriptorParam1 = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 2, 4, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfVpcReceiveTrafficDescriptorParam1.setStatus('mandatory')
atmfVpcReceiveTrafficDescriptorParam2 = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 2, 4, 1, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfVpcReceiveTrafficDescriptorParam2.setStatus('mandatory')
atmfVpcReceiveTrafficDescriptorParam3 = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 2, 4, 1, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfVpcReceiveTrafficDescriptorParam3.setStatus('mandatory')
atmfVpcReceiveTrafficDescriptorParam4 = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 2, 4, 1, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfVpcReceiveTrafficDescriptorParam4.setStatus('mandatory')
atmfVpcReceiveTrafficDescriptorParam5 = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 2, 4, 1, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfVpcReceiveTrafficDescriptorParam5.setStatus('mandatory')
atmfVpcQoSCategory = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 2, 4, 1, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("deterministic", 2), ("statistical", 3), ("unspecified", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfVpcQoSCategory.setStatus('deprecated')
atmfVpcTransmitQoSClass = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 2, 4, 1, 1, 17), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfVpcTransmitQoSClass.setStatus('mandatory')
atmfVpcReceiveQoSClass = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 2, 4, 1, 1, 18), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfVpcReceiveQoSClass.setStatus('mandatory')
atmfVccTable = MibTable((1, 3, 6, 1, 4, 1, 353, 2, 5, 1), )
if mibBuilder.loadTexts: atmfVccTable.setStatus('mandatory')
atmfVccEntry = MibTableRow((1, 3, 6, 1, 4, 1, 353, 2, 5, 1, 1), ).setIndexNames((0, "ATM-FORUM-MIB", "atmfVccPortIndex"), (0, "ATM-FORUM-MIB", "atmfVccVpi"), (0, "ATM-FORUM-MIB", "atmfVccVci"))
if mibBuilder.loadTexts: atmfVccEntry.setStatus('mandatory')
atmfVccPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 2, 5, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfVccPortIndex.setStatus('mandatory')
atmfVccVpi = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 2, 5, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfVccVpi.setStatus('mandatory')
atmfVccVci = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 2, 5, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfVccVci.setStatus('mandatory')
atmfVccOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 2, 5, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("unknown", 1), ("end2endUp", 2), ("end2endDown", 3), ("localUpEnd2endUnknown", 4), ("localDown", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfVccOperStatus.setStatus('mandatory')
atmfVccTransmitTrafficDescriptorType = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 2, 5, 1, 1, 5), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfVccTransmitTrafficDescriptorType.setStatus('mandatory')
atmfVccTransmitTrafficDescriptorParam1 = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 2, 5, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfVccTransmitTrafficDescriptorParam1.setStatus('mandatory')
atmfVccTransmitTrafficDescriptorParam2 = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 2, 5, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfVccTransmitTrafficDescriptorParam2.setStatus('mandatory')
atmfVccTransmitTrafficDescriptorParam3 = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 2, 5, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfVccTransmitTrafficDescriptorParam3.setStatus('mandatory')
atmfVccTransmitTrafficDescriptorParam4 = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 2, 5, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfVccTransmitTrafficDescriptorParam4.setStatus('mandatory')
atmfVccTransmitTrafficDescriptorParam5 = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 2, 5, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfVccTransmitTrafficDescriptorParam5.setStatus('mandatory')
atmfVccReceiveTrafficDescriptorType = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 2, 5, 1, 1, 11), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfVccReceiveTrafficDescriptorType.setStatus('mandatory')
atmfVccReceiveTrafficDescriptorParam1 = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 2, 5, 1, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfVccReceiveTrafficDescriptorParam1.setStatus('mandatory')
atmfVccReceiveTrafficDescriptorParam2 = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 2, 5, 1, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfVccReceiveTrafficDescriptorParam2.setStatus('mandatory')
atmfVccReceiveTrafficDescriptorParam3 = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 2, 5, 1, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfVccReceiveTrafficDescriptorParam3.setStatus('mandatory')
atmfVccReceiveTrafficDescriptorParam4 = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 2, 5, 1, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfVccReceiveTrafficDescriptorParam4.setStatus('mandatory')
atmfVccReceiveTrafficDescriptorParam5 = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 2, 5, 1, 1, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfVccReceiveTrafficDescriptorParam5.setStatus('mandatory')
atmfVccQoSCategory = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 2, 5, 1, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("deterministic", 2), ("statistical", 3), ("unspecified", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfVccQoSCategory.setStatus('deprecated')
atmfVccTransmitQoSClass = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 2, 5, 1, 1, 18), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfVccTransmitQoSClass.setStatus('mandatory')
atmfVccReceiveQoSClass = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 2, 5, 1, 1, 19), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfVccReceiveQoSClass.setStatus('mandatory')
atmfNetPrefixTable = MibTable((1, 3, 6, 1, 4, 1, 353, 2, 7, 1), )
if mibBuilder.loadTexts: atmfNetPrefixTable.setStatus('mandatory')
atmfNetPrefixEntry = MibTableRow((1, 3, 6, 1, 4, 1, 353, 2, 7, 1, 1), ).setIndexNames((0, "ATM-FORUM-MIB", "atmfNetPrefixPort"), (0, "ATM-FORUM-MIB", "atmfNetPrefixPrefix"))
if mibBuilder.loadTexts: atmfNetPrefixEntry.setStatus('mandatory')
atmfNetPrefixPort = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 2, 7, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: atmfNetPrefixPort.setStatus('mandatory')
atmfNetPrefixPrefix = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 2, 7, 1, 1, 2), NetPrefix())
if mibBuilder.loadTexts: atmfNetPrefixPrefix.setStatus('mandatory')
atmfNetPrefixStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 2, 7, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("valid", 1), ("invalid", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmfNetPrefixStatus.setStatus('mandatory')
atmfAddressTable = MibTable((1, 3, 6, 1, 4, 1, 353, 2, 6, 1), )
if mibBuilder.loadTexts: atmfAddressTable.setStatus('mandatory')
atmfAddressEntry = MibTableRow((1, 3, 6, 1, 4, 1, 353, 2, 6, 1, 1), ).setIndexNames((0, "ATM-FORUM-MIB", "atmfAddressPort"), (0, "ATM-FORUM-MIB", "atmfAddressAtmAddress"))
if mibBuilder.loadTexts: atmfAddressEntry.setStatus('mandatory')
atmfAddressPort = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 2, 6, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: atmfAddressPort.setStatus('mandatory')
atmfAddressAtmAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 2, 6, 1, 1, 2), AtmAddress2())
if mibBuilder.loadTexts: atmfAddressAtmAddress.setStatus('mandatory')
atmfAddressStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 2, 6, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("valid", 1), ("invalid", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmfAddressStatus.setStatus('mandatory')
mibBuilder.exportSymbols("ATM-FORUM-MIB", AtmAddress=AtmAddress, atmfVccOperStatus=atmfVccOperStatus, atmfVpcTable=atmfVpcTable, atmfVpcTransmitTrafficDescriptorParam4=atmfVpcTransmitTrafficDescriptorParam4, atmfVccTransmitTrafficDescriptorParam4=atmfVccTransmitTrafficDescriptorParam4, atmfVccReceiveTrafficDescriptorParam2=atmfVccReceiveTrafficDescriptorParam2, atmfAtmLayerEntry=atmfAtmLayerEntry, atmfVccVpi=atmfVccVpi, atmfVpcReceiveTrafficDescriptorParam4=atmfVpcReceiveTrafficDescriptorParam4, atmfVpcGroup=atmfVpcGroup, atmfAtmLayerMaxVpiBits=atmfAtmLayerMaxVpiBits, atmfNetPrefixTable=atmfNetPrefixTable, atmfAddressStatus=atmfAddressStatus, atmfTransmissionTypes=atmfTransmissionTypes, atmfAddressEntry=atmfAddressEntry, atmfVccTransmitTrafficDescriptorType=atmfVccTransmitTrafficDescriptorType, atmfVccReceiveQoSClass=atmfVccReceiveQoSClass, atmfNetPrefixStatus=atmfNetPrefixStatus, atmfAddressGroup=atmfAddressGroup, atmfDs3=atmfDs3, atmfAtmStatsDroppedReceivedCells=atmfAtmStatsDroppedReceivedCells, atmfNetPrefixGroup=atmfNetPrefixGroup, atmfVccVci=atmfVccVci, atmfVccReceiveTrafficDescriptorParam5=atmfVccReceiveTrafficDescriptorParam5, atmfAtmStatsTransmittedCells=atmfAtmStatsTransmittedCells, atmfPortEntry=atmfPortEntry, atmfAtmStatsGroup=atmfAtmStatsGroup, atmfMediaUtp=atmfMediaUtp, atmfPortSpecific=atmfPortSpecific, atmfAtmLayerUniType=atmfAtmLayerUniType, atmfVpcEntry=atmfVpcEntry, atmfVccGroup=atmfVccGroup, atmfVpcReceiveTrafficDescriptorParam5=atmfVpcReceiveTrafficDescriptorParam5, atmfVccTransmitTrafficDescriptorParam1=atmfVccTransmitTrafficDescriptorParam1, atmfVccReceiveTrafficDescriptorParam4=atmfVccReceiveTrafficDescriptorParam4, atmfVpcTransmitTrafficDescriptorParam5=atmfVpcTransmitTrafficDescriptorParam5, atmfPortTransmissionType=atmfPortTransmissionType, atmfVpcReceiveTrafficDescriptorParam3=atmfVpcReceiveTrafficDescriptorParam3, atmf4B5B=atmf4B5B, atmfVccQoSCategory=atmfVccQoSCategory, atmfAtmLayerMaxVPCs=atmfAtmLayerMaxVPCs, atmfNetPrefixEntry=atmfNetPrefixEntry, atmfVpcTransmitTrafficDescriptorParam3=atmfVpcTransmitTrafficDescriptorParam3, atmfPortMyIfName=atmfPortMyIfName, atmfVpcVpi=atmfVpcVpi, atmfAddressPort=atmfAddressPort, atmfVpcReceiveTrafficDescriptorType=atmfVpcReceiveTrafficDescriptorType, atmfAtmStatsTable=atmfAtmStatsTable, atmfVccReceiveTrafficDescriptorParam1=atmfVccReceiveTrafficDescriptorParam1, atmfNoClpNoScr=atmfNoClpNoScr, atmfVccTransmitTrafficDescriptorParam2=atmfVccTransmitTrafficDescriptorParam2, atmfPeakRate=atmfPeakRate, atmfAddressTable=atmfAddressTable, atmForum=atmForum, atmfPortTable=atmfPortTable, atmfSonetSTS3c=atmfSonetSTS3c, atmfVccReceiveTrafficDescriptorParam3=atmfVccReceiveTrafficDescriptorParam3, atmfMediaMultiMode=atmfMediaMultiMode, atmfAtmStatsReceivedCells=atmfAtmStatsReceivedCells, AtmAddress2=AtmAddress2, atmfPortAddress=atmfPortAddress, atmfVccPortIndex=atmfVccPortIndex, atmfVpcQoSCategory=atmfVpcQoSCategory, atmfPortMediaType=atmfPortMediaType, atmfPortOperStatus=atmfPortOperStatus, atmfNetPrefixPort=atmfNetPrefixPort, atmfVccTransmitTrafficDescriptorParam3=atmfVccTransmitTrafficDescriptorParam3, atmf8B10B=atmf8B10B, atmfVpcPortIndex=atmfVpcPortIndex, atmfMediaStp=atmfMediaStp, atmfPortIndex=atmfPortIndex, atmfVpcReceiveTrafficDescriptorParam1=atmfVpcReceiveTrafficDescriptorParam1, atmfVpcTransmitTrafficDescriptorParam2=atmfVpcTransmitTrafficDescriptorParam2, atmfMediaSingleMode=atmfMediaSingleMode, atmfAtmLayerUniVersion=atmfAtmLayerUniVersion, atmfVccTable=atmfVccTable, atmfAtmLayerConfiguredVCCs=atmfAtmLayerConfiguredVCCs, atmfAddressAtmAddress=atmfAddressAtmAddress, atmForumUni=atmForumUni, atmfVccEntry=atmfVccEntry, atmfMediaUnknownType=atmfMediaUnknownType, atmfNoClpScr=atmfNoClpScr, atmfClpNoTaggingScr=atmfClpNoTaggingScr, atmfClpNoTaggingNoScr=atmfClpNoTaggingNoScr, atmfUnknownType=atmfUnknownType, atmfClpTaggingNoScr=atmfClpTaggingNoScr, atmfTrafficDescrTypes=atmfTrafficDescrTypes, atmfPhysicalGroup=atmfPhysicalGroup, atmfVpcTransmitTrafficDescriptorType=atmfVpcTransmitTrafficDescriptorType, atmForumAdmin=atmForumAdmin, atmfVpcReceiveTrafficDescriptorParam2=atmfVpcReceiveTrafficDescriptorParam2, atmfNetPrefixPrefix=atmfNetPrefixPrefix, atmfClpTaggingScr=atmfClpTaggingScr, atmfAtmStatsEntry=atmfAtmStatsEntry, atmfVpcReceiveQoSClass=atmfVpcReceiveQoSClass, atmfVpcTransmitTrafficDescriptorParam1=atmfVpcTransmitTrafficDescriptorParam1, atmfVccTransmitQoSClass=atmfVccTransmitQoSClass, atmfMediaTypes=atmfMediaTypes, atmfNoDescriptor=atmfNoDescriptor, atmfMyIpNmAddress=atmfMyIpNmAddress, atmfAtmStatsIndex=atmfAtmStatsIndex, atmfAtmLayerIndex=atmfAtmLayerIndex, atmfVpcOperStatus=atmfVpcOperStatus, atmfVccReceiveTrafficDescriptorType=atmfVccReceiveTrafficDescriptorType, NetPrefix=NetPrefix, atmfAtmLayerMaxVCCs=atmfAtmLayerMaxVCCs, atmfMediaCoaxCable=atmfMediaCoaxCable, atmfAtmLayerGroup=atmfAtmLayerGroup, atmfAtmLayerMaxVciBits=atmfAtmLayerMaxVciBits, atmfVpcTransmitQoSClass=atmfVpcTransmitQoSClass, atmfAtmLayerConfiguredVPCs=atmfAtmLayerConfiguredVPCs, atmfVccTransmitTrafficDescriptorParam5=atmfVccTransmitTrafficDescriptorParam5, atmfAtmLayerTable=atmfAtmLayerTable)
