#
# PySNMP MIB module LLDP-EXT-DOT3-V2-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/iee/LLDP-EXT-DOT3-V2-MIB
# Produced by pysmi-1.1.8 at Mon Feb  7 16:06:21 2022
# On host fv-az42-619 platform Linux version 5.11.0-1028-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
ifGeneralInformationGroup, = mibBuilder.importSymbols("IF-MIB", "ifGeneralInformationGroup")
lldpV2RemTimeMark, lldpV2LocPortIfIndex, lldpV2RemLocalDestMACAddress, lldpV2RemIndex, lldpV2PortConfigEntry, lldpV2RemLocalIfIndex, lldpV2Extensions = mibBuilder.importSymbols("LLDP-V2-MIB", "lldpV2RemTimeMark", "lldpV2LocPortIfIndex", "lldpV2RemLocalDestMACAddress", "lldpV2RemIndex", "lldpV2PortConfigEntry", "lldpV2RemLocalIfIndex", "lldpV2Extensions")
LldpV2PowerPortClass, = mibBuilder.importSymbols("LLDP-V2-TC-MIB", "LldpV2PowerPortClass")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
TimeTicks, MibIdentifier, NotificationType, Unsigned32, IpAddress, Integer32, ModuleIdentity, Counter64, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Counter32, Gauge32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "MibIdentifier", "NotificationType", "Unsigned32", "IpAddress", "Integer32", "ModuleIdentity", "Counter64", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Counter32", "Gauge32", "Bits")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
lldpV2Xdot3MIB = ModuleIdentity((1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 4623))
lldpV2Xdot3MIB.setRevisions(('2013-05-24 17:53', '2009-06-08 00:00',))
if mibBuilder.loadTexts: lldpV2Xdot3MIB.setLastUpdated('201305241753Z')
if mibBuilder.loadTexts: lldpV2Xdot3MIB.setOrganization('IEEE 802.1 Working Group')
p8021lldpV2Xdot3Objects = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 4623, 1))
p8021lldpV2Xdot3Config = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 4623, 1, 1))
p8021lldpV2Xdot3LocalData = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 4623, 1, 2))
p8021lldpV2Xdot3RemoteData = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 4623, 1, 3))
p8021lldpV2Xdot3PortConfigTable = MibTable((1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 4623, 1, 1, 1), )
if mibBuilder.loadTexts: p8021lldpV2Xdot3PortConfigTable.setStatus('current')
p8021lldpV2Xdot3PortConfigEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 4623, 1, 1, 1, 1), )
lldpV2PortConfigEntry.registerAugmentions(("LLDP-EXT-DOT3-V2-MIB", "p8021lldpV2Xdot3PortConfigEntry"))
p8021lldpV2Xdot3PortConfigEntry.setIndexNames(*lldpV2PortConfigEntry.getIndexNames())
if mibBuilder.loadTexts: p8021lldpV2Xdot3PortConfigEntry.setStatus('current')
p8021lldpV2Xdot3PortConfigTLVsTxEnable = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 4623, 1, 1, 1, 1, 1), Bits().clone(namedValues=NamedValues(("macPhyConfigStatus", 0), ("powerViaMDI", 1), ("unused", 2), ("maxFrameSize", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: p8021lldpV2Xdot3PortConfigTLVsTxEnable.setStatus('current')
p8021lldpV2Xdot3LocPortTable = MibTable((1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 4623, 1, 2, 1), )
if mibBuilder.loadTexts: p8021lldpV2Xdot3LocPortTable.setStatus('current')
p8021lldpV2Xdot3LocPortEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 4623, 1, 2, 1, 1), ).setIndexNames((0, "LLDP-V2-MIB", "lldpV2LocPortIfIndex"))
if mibBuilder.loadTexts: p8021lldpV2Xdot3LocPortEntry.setStatus('current')
p8021lldpV2Xdot3LocPortAutoNegSupported = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 4623, 1, 2, 1, 1, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: p8021lldpV2Xdot3LocPortAutoNegSupported.setStatus('current')
p8021lldpV2Xdot3LocPortAutoNegEnabled = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 4623, 1, 2, 1, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: p8021lldpV2Xdot3LocPortAutoNegEnabled.setStatus('current')
p8021lldpV2Xdot3LocPortAutoNegAdvertisedCap = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 4623, 1, 2, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: p8021lldpV2Xdot3LocPortAutoNegAdvertisedCap.setStatus('current')
p8021lldpV2Xdot3LocPortOperMauType = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 4623, 1, 2, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: p8021lldpV2Xdot3LocPortOperMauType.setStatus('current')
p8021lldpV2Xdot3LocPowerTable = MibTable((1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 4623, 1, 2, 2), )
if mibBuilder.loadTexts: p8021lldpV2Xdot3LocPowerTable.setStatus('current')
p8021lldpV2Xdot3LocPowerEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 4623, 1, 2, 2, 1), ).setIndexNames((0, "LLDP-V2-MIB", "lldpV2LocPortIfIndex"))
if mibBuilder.loadTexts: p8021lldpV2Xdot3LocPowerEntry.setStatus('current')
p8021lldpV2Xdot3LocPowerPortClass = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 4623, 1, 2, 2, 1, 1), LldpV2PowerPortClass()).setMaxAccess("readonly")
if mibBuilder.loadTexts: p8021lldpV2Xdot3LocPowerPortClass.setStatus('current')
p8021lldpV2Xdot3LocPowerMDISupported = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 4623, 1, 2, 2, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: p8021lldpV2Xdot3LocPowerMDISupported.setStatus('current')
p8021lldpV2Xdot3LocPowerMDIEnabled = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 4623, 1, 2, 2, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: p8021lldpV2Xdot3LocPowerMDIEnabled.setStatus('current')
p8021lldpV2Xdot3LocPowerPairControlable = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 4623, 1, 2, 2, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: p8021lldpV2Xdot3LocPowerPairControlable.setStatus('current')
p8021lldpV2Xdot3LocPowerPairs = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 4623, 1, 2, 2, 1, 5), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(1, 1), ValueRangeConstraint(2, 2), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: p8021lldpV2Xdot3LocPowerPairs.setStatus('current')
p8021lldpV2Xdot3LocPowerClass = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 4623, 1, 2, 2, 1, 6), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(1, 1), ValueRangeConstraint(2, 2), ValueRangeConstraint(3, 3), ValueRangeConstraint(4, 4), ValueRangeConstraint(5, 5), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: p8021lldpV2Xdot3LocPowerClass.setStatus('current')
p8021lldpV2Xdot3LocMaxFrameSizeTable = MibTable((1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 4623, 1, 2, 3), )
if mibBuilder.loadTexts: p8021lldpV2Xdot3LocMaxFrameSizeTable.setStatus('current')
p8021lldpV2Xdot3LocMaxFrameSizeEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 4623, 1, 2, 3, 1), ).setIndexNames((0, "LLDP-V2-MIB", "lldpV2LocPortIfIndex"))
if mibBuilder.loadTexts: p8021lldpV2Xdot3LocMaxFrameSizeEntry.setStatus('current')
p8021lldpV2Xdot3LocMaxFrameSize = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 4623, 1, 2, 3, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: p8021lldpV2Xdot3LocMaxFrameSize.setStatus('current')
p8021lldpV2Xdot3RemPortTable = MibTable((1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 4623, 1, 3, 1), )
if mibBuilder.loadTexts: p8021lldpV2Xdot3RemPortTable.setStatus('current')
p8021lldpV2Xdot3RemPortEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 4623, 1, 3, 1, 1), ).setIndexNames((0, "LLDP-V2-MIB", "lldpV2RemTimeMark"), (0, "LLDP-V2-MIB", "lldpV2RemLocalIfIndex"), (0, "LLDP-V2-MIB", "lldpV2RemLocalDestMACAddress"), (0, "LLDP-V2-MIB", "lldpV2RemIndex"))
if mibBuilder.loadTexts: p8021lldpV2Xdot3RemPortEntry.setStatus('current')
p8021lldpV2Xdot3RemPortAutoNegSupported = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 4623, 1, 3, 1, 1, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: p8021lldpV2Xdot3RemPortAutoNegSupported.setStatus('current')
p8021lldpV2Xdot3RemPortAutoNegEnabled = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 4623, 1, 3, 1, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: p8021lldpV2Xdot3RemPortAutoNegEnabled.setStatus('current')
p8021lldpV2Xdot3RemPortAutoNegAdvertisedCap = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 4623, 1, 3, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: p8021lldpV2Xdot3RemPortAutoNegAdvertisedCap.setStatus('current')
p8021lldpV2Xdot3RemPortOperMauType = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 4623, 1, 3, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: p8021lldpV2Xdot3RemPortOperMauType.setStatus('current')
p8021lldpV2Xdot3RemPowerTable = MibTable((1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 4623, 1, 3, 2), )
if mibBuilder.loadTexts: p8021lldpV2Xdot3RemPowerTable.setStatus('current')
p8021lldpV2Xdot3RemPowerEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 4623, 1, 3, 2, 1), ).setIndexNames((0, "LLDP-V2-MIB", "lldpV2RemTimeMark"), (0, "LLDP-V2-MIB", "lldpV2RemLocalIfIndex"), (0, "LLDP-V2-MIB", "lldpV2RemLocalDestMACAddress"), (0, "LLDP-V2-MIB", "lldpV2RemIndex"))
if mibBuilder.loadTexts: p8021lldpV2Xdot3RemPowerEntry.setStatus('current')
p8021lldpV2Xdot3RemPowerPortClass = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 4623, 1, 3, 2, 1, 1), LldpV2PowerPortClass()).setMaxAccess("readonly")
if mibBuilder.loadTexts: p8021lldpV2Xdot3RemPowerPortClass.setStatus('current')
p8021lldpV2Xdot3RemPowerMDISupported = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 4623, 1, 3, 2, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: p8021lldpV2Xdot3RemPowerMDISupported.setStatus('current')
p8021lldpV2Xdot3RemPowerMDIEnabled = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 4623, 1, 3, 2, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: p8021lldpV2Xdot3RemPowerMDIEnabled.setStatus('current')
p8021lldpV2Xdot3RemPowerPairControlable = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 4623, 1, 3, 2, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: p8021lldpV2Xdot3RemPowerPairControlable.setStatus('current')
p8021lldpV2Xdot3RemPowerPairs = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 4623, 1, 3, 2, 1, 5), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(1, 1), ValueRangeConstraint(2, 2), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: p8021lldpV2Xdot3RemPowerPairs.setStatus('current')
p8021lldpV2Xdot3RemPowerClass = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 4623, 1, 3, 2, 1, 6), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(1, 1), ValueRangeConstraint(2, 2), ValueRangeConstraint(3, 3), ValueRangeConstraint(4, 4), ValueRangeConstraint(5, 5), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: p8021lldpV2Xdot3RemPowerClass.setStatus('current')
p8021lldpV2Xdot3RemMaxFrameSizeTable = MibTable((1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 4623, 1, 3, 3), )
if mibBuilder.loadTexts: p8021lldpV2Xdot3RemMaxFrameSizeTable.setStatus('current')
p8021lldpV2Xdot3RemMaxFrameSizeEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 4623, 1, 3, 3, 1), ).setIndexNames((0, "LLDP-V2-MIB", "lldpV2RemTimeMark"), (0, "LLDP-V2-MIB", "lldpV2RemLocalIfIndex"), (0, "LLDP-V2-MIB", "lldpV2RemLocalDestMACAddress"), (0, "LLDP-V2-MIB", "lldpV2RemIndex"))
if mibBuilder.loadTexts: p8021lldpV2Xdot3RemMaxFrameSizeEntry.setStatus('current')
p8021lldpV2Xdot3RemMaxFrameSize = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 4623, 1, 3, 3, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: p8021lldpV2Xdot3RemMaxFrameSize.setStatus('current')
p8021lldpV2Xdot3Conformance = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 4623, 2))
p8021lldpV2Xdot3Compliances = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 4623, 2, 1))
p8021lldpV2Xdot3Groups = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 4623, 2, 2))
p8021lldpV2Xdot3TxRxCompliance = ModuleCompliance((1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 4623, 2, 1, 1)).setObjects(("LLDP-EXT-DOT3-V2-MIB", "p8021lldpV2Xdot3ConfigGroup"), ("IF-MIB", "ifGeneralInformationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    p8021lldpV2Xdot3TxRxCompliance = p8021lldpV2Xdot3TxRxCompliance.setStatus('current')
p8021lldpV2Xdot3TxCompliance = ModuleCompliance((1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 4623, 2, 1, 2)).setObjects(("LLDP-EXT-DOT3-V2-MIB", "p8021lldpV2Xdot3LocSysGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    p8021lldpV2Xdot3TxCompliance = p8021lldpV2Xdot3TxCompliance.setStatus('current')
p8021lldpV2Xdot3RxCompliance = ModuleCompliance((1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 4623, 2, 1, 3)).setObjects(("LLDP-EXT-DOT3-V2-MIB", "p8021lldpV2Xdot3RemSysGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    p8021lldpV2Xdot3RxCompliance = p8021lldpV2Xdot3RxCompliance.setStatus('current')
p8021lldpV2Xdot3ConfigGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 4623, 2, 2, 1)).setObjects(("LLDP-EXT-DOT3-V2-MIB", "p8021lldpV2Xdot3PortConfigTLVsTxEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    p8021lldpV2Xdot3ConfigGroup = p8021lldpV2Xdot3ConfigGroup.setStatus('current')
p8021lldpV2Xdot3LocSysGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 4623, 2, 2, 2)).setObjects(("LLDP-EXT-DOT3-V2-MIB", "p8021lldpV2Xdot3LocPortAutoNegSupported"), ("LLDP-EXT-DOT3-V2-MIB", "p8021lldpV2Xdot3LocPortAutoNegEnabled"), ("LLDP-EXT-DOT3-V2-MIB", "p8021lldpV2Xdot3LocPortAutoNegAdvertisedCap"), ("LLDP-EXT-DOT3-V2-MIB", "p8021lldpV2Xdot3LocPortOperMauType"), ("LLDP-EXT-DOT3-V2-MIB", "p8021lldpV2Xdot3LocPowerPortClass"), ("LLDP-EXT-DOT3-V2-MIB", "p8021lldpV2Xdot3LocPowerMDISupported"), ("LLDP-EXT-DOT3-V2-MIB", "p8021lldpV2Xdot3LocPowerMDIEnabled"), ("LLDP-EXT-DOT3-V2-MIB", "p8021lldpV2Xdot3LocPowerPairControlable"), ("LLDP-EXT-DOT3-V2-MIB", "p8021lldpV2Xdot3LocPowerPairs"), ("LLDP-EXT-DOT3-V2-MIB", "p8021lldpV2Xdot3LocPowerClass"), ("LLDP-EXT-DOT3-V2-MIB", "p8021lldpV2Xdot3LocMaxFrameSize"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    p8021lldpV2Xdot3LocSysGroup = p8021lldpV2Xdot3LocSysGroup.setStatus('current')
p8021lldpV2Xdot3RemSysGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 4623, 2, 2, 3)).setObjects(("LLDP-EXT-DOT3-V2-MIB", "p8021lldpV2Xdot3RemPortAutoNegSupported"), ("LLDP-EXT-DOT3-V2-MIB", "p8021lldpV2Xdot3RemPortAutoNegEnabled"), ("LLDP-EXT-DOT3-V2-MIB", "p8021lldpV2Xdot3RemPortAutoNegAdvertisedCap"), ("LLDP-EXT-DOT3-V2-MIB", "p8021lldpV2Xdot3RemPortOperMauType"), ("LLDP-EXT-DOT3-V2-MIB", "p8021lldpV2Xdot3RemPowerPortClass"), ("LLDP-EXT-DOT3-V2-MIB", "p8021lldpV2Xdot3RemPowerMDISupported"), ("LLDP-EXT-DOT3-V2-MIB", "p8021lldpV2Xdot3RemPowerMDIEnabled"), ("LLDP-EXT-DOT3-V2-MIB", "p8021lldpV2Xdot3RemPowerPairControlable"), ("LLDP-EXT-DOT3-V2-MIB", "p8021lldpV2Xdot3RemPowerPairs"), ("LLDP-EXT-DOT3-V2-MIB", "p8021lldpV2Xdot3RemPowerClass"), ("LLDP-EXT-DOT3-V2-MIB", "p8021lldpV2Xdot3RemMaxFrameSize"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    p8021lldpV2Xdot3RemSysGroup = p8021lldpV2Xdot3RemSysGroup.setStatus('current')
mibBuilder.exportSymbols("LLDP-EXT-DOT3-V2-MIB", p8021lldpV2Xdot3PortConfigTable=p8021lldpV2Xdot3PortConfigTable, p8021lldpV2Xdot3LocPowerPortClass=p8021lldpV2Xdot3LocPowerPortClass, p8021lldpV2Xdot3RemPortAutoNegAdvertisedCap=p8021lldpV2Xdot3RemPortAutoNegAdvertisedCap, p8021lldpV2Xdot3RemoteData=p8021lldpV2Xdot3RemoteData, p8021lldpV2Xdot3LocPortEntry=p8021lldpV2Xdot3LocPortEntry, p8021lldpV2Xdot3RemMaxFrameSizeTable=p8021lldpV2Xdot3RemMaxFrameSizeTable, p8021lldpV2Xdot3LocPowerMDIEnabled=p8021lldpV2Xdot3LocPowerMDIEnabled, p8021lldpV2Xdot3TxCompliance=p8021lldpV2Xdot3TxCompliance, p8021lldpV2Xdot3RemMaxFrameSizeEntry=p8021lldpV2Xdot3RemMaxFrameSizeEntry, p8021lldpV2Xdot3RemPortEntry=p8021lldpV2Xdot3RemPortEntry, p8021lldpV2Xdot3RemPortOperMauType=p8021lldpV2Xdot3RemPortOperMauType, p8021lldpV2Xdot3Config=p8021lldpV2Xdot3Config, p8021lldpV2Xdot3TxRxCompliance=p8021lldpV2Xdot3TxRxCompliance, p8021lldpV2Xdot3RxCompliance=p8021lldpV2Xdot3RxCompliance, p8021lldpV2Xdot3LocPowerPairControlable=p8021lldpV2Xdot3LocPowerPairControlable, p8021lldpV2Xdot3RemPortTable=p8021lldpV2Xdot3RemPortTable, p8021lldpV2Xdot3Compliances=p8021lldpV2Xdot3Compliances, p8021lldpV2Xdot3LocPortTable=p8021lldpV2Xdot3LocPortTable, p8021lldpV2Xdot3RemPowerTable=p8021lldpV2Xdot3RemPowerTable, p8021lldpV2Xdot3Objects=p8021lldpV2Xdot3Objects, p8021lldpV2Xdot3RemPowerClass=p8021lldpV2Xdot3RemPowerClass, PYSNMP_MODULE_ID=lldpV2Xdot3MIB, p8021lldpV2Xdot3LocPortAutoNegEnabled=p8021lldpV2Xdot3LocPortAutoNegEnabled, p8021lldpV2Xdot3LocMaxFrameSizeEntry=p8021lldpV2Xdot3LocMaxFrameSizeEntry, p8021lldpV2Xdot3RemPortAutoNegSupported=p8021lldpV2Xdot3RemPortAutoNegSupported, p8021lldpV2Xdot3RemPowerEntry=p8021lldpV2Xdot3RemPowerEntry, p8021lldpV2Xdot3RemPowerPortClass=p8021lldpV2Xdot3RemPowerPortClass, p8021lldpV2Xdot3ConfigGroup=p8021lldpV2Xdot3ConfigGroup, p8021lldpV2Xdot3LocMaxFrameSizeTable=p8021lldpV2Xdot3LocMaxFrameSizeTable, p8021lldpV2Xdot3LocalData=p8021lldpV2Xdot3LocalData, p8021lldpV2Xdot3LocPortAutoNegSupported=p8021lldpV2Xdot3LocPortAutoNegSupported, p8021lldpV2Xdot3LocMaxFrameSize=p8021lldpV2Xdot3LocMaxFrameSize, p8021lldpV2Xdot3PortConfigEntry=p8021lldpV2Xdot3PortConfigEntry, p8021lldpV2Xdot3Groups=p8021lldpV2Xdot3Groups, p8021lldpV2Xdot3RemMaxFrameSize=p8021lldpV2Xdot3RemMaxFrameSize, p8021lldpV2Xdot3RemPortAutoNegEnabled=p8021lldpV2Xdot3RemPortAutoNegEnabled, p8021lldpV2Xdot3RemPowerMDIEnabled=p8021lldpV2Xdot3RemPowerMDIEnabled, p8021lldpV2Xdot3LocPowerPairs=p8021lldpV2Xdot3LocPowerPairs, p8021lldpV2Xdot3RemPowerPairControlable=p8021lldpV2Xdot3RemPowerPairControlable, p8021lldpV2Xdot3LocSysGroup=p8021lldpV2Xdot3LocSysGroup, p8021lldpV2Xdot3Conformance=p8021lldpV2Xdot3Conformance, p8021lldpV2Xdot3LocPortAutoNegAdvertisedCap=p8021lldpV2Xdot3LocPortAutoNegAdvertisedCap, p8021lldpV2Xdot3LocPowerTable=p8021lldpV2Xdot3LocPowerTable, p8021lldpV2Xdot3LocPortOperMauType=p8021lldpV2Xdot3LocPortOperMauType, p8021lldpV2Xdot3RemPowerMDISupported=p8021lldpV2Xdot3RemPowerMDISupported, p8021lldpV2Xdot3RemSysGroup=p8021lldpV2Xdot3RemSysGroup, p8021lldpV2Xdot3PortConfigTLVsTxEnable=p8021lldpV2Xdot3PortConfigTLVsTxEnable, p8021lldpV2Xdot3LocPowerClass=p8021lldpV2Xdot3LocPowerClass, p8021lldpV2Xdot3RemPowerPairs=p8021lldpV2Xdot3RemPowerPairs, p8021lldpV2Xdot3LocPowerMDISupported=p8021lldpV2Xdot3LocPowerMDISupported, p8021lldpV2Xdot3LocPowerEntry=p8021lldpV2Xdot3LocPowerEntry, lldpV2Xdot3MIB=lldpV2Xdot3MIB)
