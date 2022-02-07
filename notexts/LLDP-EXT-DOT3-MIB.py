#
# PySNMP MIB module LLDP-EXT-DOT3-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/iee/LLDP-EXT-DOT1-MIB
# Produced by pysmi-1.1.8 at Mon Feb  7 16:06:20 2022
# On host fv-az42-619 platform Linux version 5.11.0-1028-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
lldpLocPortNum, lldpRemTimeMark, lldpRemIndex, lldpExtensions, lldpPortConfigEntry, lldpRemLocalPortNum = mibBuilder.importSymbols("LLDP-MIB", "lldpLocPortNum", "lldpRemTimeMark", "lldpRemIndex", "lldpExtensions", "lldpPortConfigEntry", "lldpRemLocalPortNum")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
TimeTicks, MibIdentifier, NotificationType, Unsigned32, IpAddress, Integer32, ModuleIdentity, Counter64, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Counter32, Gauge32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "MibIdentifier", "NotificationType", "Unsigned32", "IpAddress", "Integer32", "ModuleIdentity", "Counter64", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Counter32", "Gauge32", "Bits")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
lldpXdot3MIB = ModuleIdentity((1, 0, 8802, 1, 1, 2, 1, 5, 4623))
lldpXdot3MIB.setRevisions(('2005-05-06 00:00',))
if mibBuilder.loadTexts: lldpXdot3MIB.setLastUpdated('200505060000Z')
if mibBuilder.loadTexts: lldpXdot3MIB.setOrganization('IEEE 802.1 Working Group')
lldpXdot3Objects = MibIdentifier((1, 0, 8802, 1, 1, 2, 1, 5, 4623, 1))
lldpXdot3Config = MibIdentifier((1, 0, 8802, 1, 1, 2, 1, 5, 4623, 1, 1))
lldpXdot3LocalData = MibIdentifier((1, 0, 8802, 1, 1, 2, 1, 5, 4623, 1, 2))
lldpXdot3RemoteData = MibIdentifier((1, 0, 8802, 1, 1, 2, 1, 5, 4623, 1, 3))
class LldpPowerPortClass(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("pClassPSE", 1), ("pClassPD", 2))

class LldpLinkAggStatusMap(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("aggCapable", 0), ("aggEnabled", 1))

lldpXdot3PortConfigTable = MibTable((1, 0, 8802, 1, 1, 2, 1, 5, 4623, 1, 1, 1), )
if mibBuilder.loadTexts: lldpXdot3PortConfigTable.setStatus('current')
lldpXdot3PortConfigEntry = MibTableRow((1, 0, 8802, 1, 1, 2, 1, 5, 4623, 1, 1, 1, 1), )
lldpPortConfigEntry.registerAugmentions(("LLDP-EXT-DOT3-MIB", "lldpXdot3PortConfigEntry"))
lldpXdot3PortConfigEntry.setIndexNames(*lldpPortConfigEntry.getIndexNames())
if mibBuilder.loadTexts: lldpXdot3PortConfigEntry.setStatus('current')
lldpXdot3PortConfigTLVsTxEnable = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 4623, 1, 1, 1, 1, 1), Bits().clone(namedValues=NamedValues(("macPhyConfigStatus", 0), ("powerViaMDI", 1), ("linkAggregation", 2), ("maxFrameSize", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lldpXdot3PortConfigTLVsTxEnable.setStatus('current')
lldpXdot3LocPortTable = MibTable((1, 0, 8802, 1, 1, 2, 1, 5, 4623, 1, 2, 1), )
if mibBuilder.loadTexts: lldpXdot3LocPortTable.setStatus('current')
lldpXdot3LocPortEntry = MibTableRow((1, 0, 8802, 1, 1, 2, 1, 5, 4623, 1, 2, 1, 1), ).setIndexNames((0, "LLDP-MIB", "lldpLocPortNum"))
if mibBuilder.loadTexts: lldpXdot3LocPortEntry.setStatus('current')
lldpXdot3LocPortAutoNegSupported = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 4623, 1, 2, 1, 1, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXdot3LocPortAutoNegSupported.setStatus('current')
lldpXdot3LocPortAutoNegEnabled = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 4623, 1, 2, 1, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXdot3LocPortAutoNegEnabled.setStatus('current')
lldpXdot3LocPortAutoNegAdvertisedCap = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 4623, 1, 2, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXdot3LocPortAutoNegAdvertisedCap.setStatus('current')
lldpXdot3LocPortOperMauType = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 4623, 1, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXdot3LocPortOperMauType.setStatus('current')
lldpXdot3LocPowerTable = MibTable((1, 0, 8802, 1, 1, 2, 1, 5, 4623, 1, 2, 2), )
if mibBuilder.loadTexts: lldpXdot3LocPowerTable.setStatus('current')
lldpXdot3LocPowerEntry = MibTableRow((1, 0, 8802, 1, 1, 2, 1, 5, 4623, 1, 2, 2, 1), ).setIndexNames((0, "LLDP-MIB", "lldpLocPortNum"))
if mibBuilder.loadTexts: lldpXdot3LocPowerEntry.setStatus('current')
lldpXdot3LocPowerPortClass = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 4623, 1, 2, 2, 1, 1), LldpPowerPortClass()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXdot3LocPowerPortClass.setStatus('current')
lldpXdot3LocPowerMDISupported = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 4623, 1, 2, 2, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXdot3LocPowerMDISupported.setStatus('current')
lldpXdot3LocPowerMDIEnabled = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 4623, 1, 2, 2, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXdot3LocPowerMDIEnabled.setStatus('current')
lldpXdot3LocPowerPairControlable = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 4623, 1, 2, 2, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXdot3LocPowerPairControlable.setStatus('current')
lldpXdot3LocPowerPairs = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 4623, 1, 2, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(1, 1), ValueRangeConstraint(2, 2), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXdot3LocPowerPairs.setStatus('current')
lldpXdot3LocPowerClass = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 4623, 1, 2, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(1, 1), ValueRangeConstraint(2, 2), ValueRangeConstraint(3, 3), ValueRangeConstraint(4, 4), ValueRangeConstraint(5, 5), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXdot3LocPowerClass.setStatus('current')
lldpXdot3LocLinkAggTable = MibTable((1, 0, 8802, 1, 1, 2, 1, 5, 4623, 1, 2, 3), )
if mibBuilder.loadTexts: lldpXdot3LocLinkAggTable.setStatus('current')
lldpXdot3LocLinkAggEntry = MibTableRow((1, 0, 8802, 1, 1, 2, 1, 5, 4623, 1, 2, 3, 1), ).setIndexNames((0, "LLDP-MIB", "lldpLocPortNum"))
if mibBuilder.loadTexts: lldpXdot3LocLinkAggEntry.setStatus('current')
lldpXdot3LocLinkAggStatus = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 4623, 1, 2, 3, 1, 1), LldpLinkAggStatusMap()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXdot3LocLinkAggStatus.setStatus('current')
lldpXdot3LocLinkAggPortId = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 4623, 1, 2, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 2147483647), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXdot3LocLinkAggPortId.setStatus('current')
lldpXdot3LocMaxFrameSizeTable = MibTable((1, 0, 8802, 1, 1, 2, 1, 5, 4623, 1, 2, 4), )
if mibBuilder.loadTexts: lldpXdot3LocMaxFrameSizeTable.setStatus('current')
lldpXdot3LocMaxFrameSizeEntry = MibTableRow((1, 0, 8802, 1, 1, 2, 1, 5, 4623, 1, 2, 4, 1), ).setIndexNames((0, "LLDP-MIB", "lldpLocPortNum"))
if mibBuilder.loadTexts: lldpXdot3LocMaxFrameSizeEntry.setStatus('current')
lldpXdot3LocMaxFrameSize = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 4623, 1, 2, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXdot3LocMaxFrameSize.setStatus('current')
lldpXdot3RemPortTable = MibTable((1, 0, 8802, 1, 1, 2, 1, 5, 4623, 1, 3, 1), )
if mibBuilder.loadTexts: lldpXdot3RemPortTable.setStatus('current')
lldpXdot3RemPortEntry = MibTableRow((1, 0, 8802, 1, 1, 2, 1, 5, 4623, 1, 3, 1, 1), ).setIndexNames((0, "LLDP-MIB", "lldpRemTimeMark"), (0, "LLDP-MIB", "lldpRemLocalPortNum"), (0, "LLDP-MIB", "lldpRemIndex"))
if mibBuilder.loadTexts: lldpXdot3RemPortEntry.setStatus('current')
lldpXdot3RemPortAutoNegSupported = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 4623, 1, 3, 1, 1, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXdot3RemPortAutoNegSupported.setStatus('current')
lldpXdot3RemPortAutoNegEnabled = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 4623, 1, 3, 1, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXdot3RemPortAutoNegEnabled.setStatus('current')
lldpXdot3RemPortAutoNegAdvertisedCap = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 4623, 1, 3, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXdot3RemPortAutoNegAdvertisedCap.setStatus('current')
lldpXdot3RemPortOperMauType = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 4623, 1, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXdot3RemPortOperMauType.setStatus('current')
lldpXdot3RemPowerTable = MibTable((1, 0, 8802, 1, 1, 2, 1, 5, 4623, 1, 3, 2), )
if mibBuilder.loadTexts: lldpXdot3RemPowerTable.setStatus('current')
lldpXdot3RemPowerEntry = MibTableRow((1, 0, 8802, 1, 1, 2, 1, 5, 4623, 1, 3, 2, 1), ).setIndexNames((0, "LLDP-MIB", "lldpRemTimeMark"), (0, "LLDP-MIB", "lldpRemLocalPortNum"), (0, "LLDP-MIB", "lldpRemIndex"))
if mibBuilder.loadTexts: lldpXdot3RemPowerEntry.setStatus('current')
lldpXdot3RemPowerPortClass = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 4623, 1, 3, 2, 1, 1), LldpPowerPortClass()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXdot3RemPowerPortClass.setStatus('current')
lldpXdot3RemPowerMDISupported = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 4623, 1, 3, 2, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXdot3RemPowerMDISupported.setStatus('current')
lldpXdot3RemPowerMDIEnabled = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 4623, 1, 3, 2, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXdot3RemPowerMDIEnabled.setStatus('current')
lldpXdot3RemPowerPairControlable = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 4623, 1, 3, 2, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXdot3RemPowerPairControlable.setStatus('current')
lldpXdot3RemPowerPairs = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 4623, 1, 3, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(1, 1), ValueRangeConstraint(2, 2), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXdot3RemPowerPairs.setStatus('current')
lldpXdot3RemPowerClass = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 4623, 1, 3, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(1, 1), ValueRangeConstraint(2, 2), ValueRangeConstraint(3, 3), ValueRangeConstraint(4, 4), ValueRangeConstraint(5, 5), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXdot3RemPowerClass.setStatus('current')
lldpXdot3RemLinkAggTable = MibTable((1, 0, 8802, 1, 1, 2, 1, 5, 4623, 1, 3, 3), )
if mibBuilder.loadTexts: lldpXdot3RemLinkAggTable.setStatus('current')
lldpXdot3RemLinkAggEntry = MibTableRow((1, 0, 8802, 1, 1, 2, 1, 5, 4623, 1, 3, 3, 1), ).setIndexNames((0, "LLDP-MIB", "lldpRemTimeMark"), (0, "LLDP-MIB", "lldpRemLocalPortNum"), (0, "LLDP-MIB", "lldpRemIndex"))
if mibBuilder.loadTexts: lldpXdot3RemLinkAggEntry.setStatus('current')
lldpXdot3RemLinkAggStatus = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 4623, 1, 3, 3, 1, 1), LldpLinkAggStatusMap()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXdot3RemLinkAggStatus.setStatus('current')
lldpXdot3RemLinkAggPortId = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 4623, 1, 3, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 2147483647), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXdot3RemLinkAggPortId.setStatus('current')
lldpXdot3RemMaxFrameSizeTable = MibTable((1, 0, 8802, 1, 1, 2, 1, 5, 4623, 1, 3, 4), )
if mibBuilder.loadTexts: lldpXdot3RemMaxFrameSizeTable.setStatus('current')
lldpXdot3RemMaxFrameSizeEntry = MibTableRow((1, 0, 8802, 1, 1, 2, 1, 5, 4623, 1, 3, 4, 1), ).setIndexNames((0, "LLDP-MIB", "lldpRemTimeMark"), (0, "LLDP-MIB", "lldpRemLocalPortNum"), (0, "LLDP-MIB", "lldpRemIndex"))
if mibBuilder.loadTexts: lldpXdot3RemMaxFrameSizeEntry.setStatus('current')
lldpXdot3RemMaxFrameSize = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 4623, 1, 3, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXdot3RemMaxFrameSize.setStatus('current')
lldpXdot3Conformance = MibIdentifier((1, 0, 8802, 1, 1, 2, 1, 5, 4623, 2))
lldpXdot3Compliances = MibIdentifier((1, 0, 8802, 1, 1, 2, 1, 5, 4623, 2, 1))
lldpXdot3Groups = MibIdentifier((1, 0, 8802, 1, 1, 2, 1, 5, 4623, 2, 2))
lldpXdot3Compliance = ModuleCompliance((1, 0, 8802, 1, 1, 2, 1, 5, 4623, 2, 1, 1)).setObjects(("LLDP-EXT-DOT3-MIB", "lldpXdot3ConfigGroup"), ("LLDP-EXT-DOT3-MIB", "lldpXdot3LocSysGroup"), ("LLDP-EXT-DOT3-MIB", "lldpXdot3RemSysGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lldpXdot3Compliance = lldpXdot3Compliance.setStatus('current')
lldpXdot3ConfigGroup = ObjectGroup((1, 0, 8802, 1, 1, 2, 1, 5, 4623, 2, 2, 1)).setObjects(("LLDP-EXT-DOT3-MIB", "lldpXdot3PortConfigTLVsTxEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lldpXdot3ConfigGroup = lldpXdot3ConfigGroup.setStatus('current')
lldpXdot3LocSysGroup = ObjectGroup((1, 0, 8802, 1, 1, 2, 1, 5, 4623, 2, 2, 2)).setObjects(("LLDP-EXT-DOT3-MIB", "lldpXdot3LocPortAutoNegSupported"), ("LLDP-EXT-DOT3-MIB", "lldpXdot3LocPortAutoNegEnabled"), ("LLDP-EXT-DOT3-MIB", "lldpXdot3LocPortAutoNegAdvertisedCap"), ("LLDP-EXT-DOT3-MIB", "lldpXdot3LocPortOperMauType"), ("LLDP-EXT-DOT3-MIB", "lldpXdot3LocPowerPortClass"), ("LLDP-EXT-DOT3-MIB", "lldpXdot3LocPowerMDISupported"), ("LLDP-EXT-DOT3-MIB", "lldpXdot3LocPowerMDIEnabled"), ("LLDP-EXT-DOT3-MIB", "lldpXdot3LocPowerPairControlable"), ("LLDP-EXT-DOT3-MIB", "lldpXdot3LocPowerPairs"), ("LLDP-EXT-DOT3-MIB", "lldpXdot3LocPowerClass"), ("LLDP-EXT-DOT3-MIB", "lldpXdot3LocLinkAggStatus"), ("LLDP-EXT-DOT3-MIB", "lldpXdot3LocLinkAggPortId"), ("LLDP-EXT-DOT3-MIB", "lldpXdot3LocMaxFrameSize"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lldpXdot3LocSysGroup = lldpXdot3LocSysGroup.setStatus('current')
lldpXdot3RemSysGroup = ObjectGroup((1, 0, 8802, 1, 1, 2, 1, 5, 4623, 2, 2, 3)).setObjects(("LLDP-EXT-DOT3-MIB", "lldpXdot3RemPortAutoNegSupported"), ("LLDP-EXT-DOT3-MIB", "lldpXdot3RemPortAutoNegEnabled"), ("LLDP-EXT-DOT3-MIB", "lldpXdot3RemPortAutoNegAdvertisedCap"), ("LLDP-EXT-DOT3-MIB", "lldpXdot3RemPortOperMauType"), ("LLDP-EXT-DOT3-MIB", "lldpXdot3RemPowerPortClass"), ("LLDP-EXT-DOT3-MIB", "lldpXdot3RemPowerMDISupported"), ("LLDP-EXT-DOT3-MIB", "lldpXdot3RemPowerMDIEnabled"), ("LLDP-EXT-DOT3-MIB", "lldpXdot3RemPowerPairControlable"), ("LLDP-EXT-DOT3-MIB", "lldpXdot3RemPowerPairs"), ("LLDP-EXT-DOT3-MIB", "lldpXdot3RemPowerClass"), ("LLDP-EXT-DOT3-MIB", "lldpXdot3RemLinkAggStatus"), ("LLDP-EXT-DOT3-MIB", "lldpXdot3RemLinkAggPortId"), ("LLDP-EXT-DOT3-MIB", "lldpXdot3RemMaxFrameSize"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lldpXdot3RemSysGroup = lldpXdot3RemSysGroup.setStatus('current')
mibBuilder.exportSymbols("LLDP-EXT-DOT3-MIB", lldpXdot3Config=lldpXdot3Config, lldpXdot3RemPowerPairs=lldpXdot3RemPowerPairs, lldpXdot3Compliances=lldpXdot3Compliances, lldpXdot3RemPortEntry=lldpXdot3RemPortEntry, lldpXdot3LocPowerEntry=lldpXdot3LocPowerEntry, lldpXdot3LocSysGroup=lldpXdot3LocSysGroup, lldpXdot3RemLinkAggPortId=lldpXdot3RemLinkAggPortId, lldpXdot3LocPortAutoNegAdvertisedCap=lldpXdot3LocPortAutoNegAdvertisedCap, lldpXdot3Objects=lldpXdot3Objects, lldpXdot3LocPowerMDISupported=lldpXdot3LocPowerMDISupported, lldpXdot3PortConfigEntry=lldpXdot3PortConfigEntry, lldpXdot3RemSysGroup=lldpXdot3RemSysGroup, lldpXdot3LocLinkAggStatus=lldpXdot3LocLinkAggStatus, lldpXdot3LocalData=lldpXdot3LocalData, lldpXdot3MIB=lldpXdot3MIB, lldpXdot3Groups=lldpXdot3Groups, lldpXdot3LocPortOperMauType=lldpXdot3LocPortOperMauType, lldpXdot3RemPowerMDIEnabled=lldpXdot3RemPowerMDIEnabled, lldpXdot3RemPowerClass=lldpXdot3RemPowerClass, lldpXdot3LocPowerMDIEnabled=lldpXdot3LocPowerMDIEnabled, lldpXdot3LocPowerPairs=lldpXdot3LocPowerPairs, lldpXdot3LocPortAutoNegSupported=lldpXdot3LocPortAutoNegSupported, lldpXdot3LocLinkAggPortId=lldpXdot3LocLinkAggPortId, lldpXdot3LocPortTable=lldpXdot3LocPortTable, lldpXdot3RemPowerTable=lldpXdot3RemPowerTable, lldpXdot3RemMaxFrameSizeTable=lldpXdot3RemMaxFrameSizeTable, lldpXdot3LocPowerTable=lldpXdot3LocPowerTable, lldpXdot3LocPowerClass=lldpXdot3LocPowerClass, lldpXdot3PortConfigTLVsTxEnable=lldpXdot3PortConfigTLVsTxEnable, lldpXdot3RemPortOperMauType=lldpXdot3RemPortOperMauType, lldpXdot3RemoteData=lldpXdot3RemoteData, lldpXdot3LocMaxFrameSize=lldpXdot3LocMaxFrameSize, lldpXdot3RemPowerMDISupported=lldpXdot3RemPowerMDISupported, lldpXdot3Compliance=lldpXdot3Compliance, lldpXdot3ConfigGroup=lldpXdot3ConfigGroup, lldpXdot3LocLinkAggTable=lldpXdot3LocLinkAggTable, lldpXdot3RemPowerEntry=lldpXdot3RemPowerEntry, LldpPowerPortClass=LldpPowerPortClass, lldpXdot3LocMaxFrameSizeTable=lldpXdot3LocMaxFrameSizeTable, lldpXdot3RemMaxFrameSize=lldpXdot3RemMaxFrameSize, lldpXdot3Conformance=lldpXdot3Conformance, lldpXdot3RemPortTable=lldpXdot3RemPortTable, lldpXdot3LocPortEntry=lldpXdot3LocPortEntry, lldpXdot3PortConfigTable=lldpXdot3PortConfigTable, lldpXdot3RemPortAutoNegAdvertisedCap=lldpXdot3RemPortAutoNegAdvertisedCap, lldpXdot3RemLinkAggTable=lldpXdot3RemLinkAggTable, lldpXdot3RemLinkAggStatus=lldpXdot3RemLinkAggStatus, lldpXdot3LocLinkAggEntry=lldpXdot3LocLinkAggEntry, lldpXdot3LocPortAutoNegEnabled=lldpXdot3LocPortAutoNegEnabled, lldpXdot3LocMaxFrameSizeEntry=lldpXdot3LocMaxFrameSizeEntry, lldpXdot3RemPowerPortClass=lldpXdot3RemPowerPortClass, LldpLinkAggStatusMap=LldpLinkAggStatusMap, lldpXdot3LocPowerPortClass=lldpXdot3LocPowerPortClass, lldpXdot3RemPowerPairControlable=lldpXdot3RemPowerPairControlable, PYSNMP_MODULE_ID=lldpXdot3MIB, lldpXdot3RemPortAutoNegSupported=lldpXdot3RemPortAutoNegSupported, lldpXdot3RemPortAutoNegEnabled=lldpXdot3RemPortAutoNegEnabled, lldpXdot3RemLinkAggEntry=lldpXdot3RemLinkAggEntry, lldpXdot3LocPowerPairControlable=lldpXdot3LocPowerPairControlable, lldpXdot3RemMaxFrameSizeEntry=lldpXdot3RemMaxFrameSizeEntry)
