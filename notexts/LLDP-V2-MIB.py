#
# PySNMP MIB module LLDP-V2-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/LLDP-V2-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:07:39 2022
# On host fv-az36-988 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
AddressFamilyNumbers, = mibBuilder.importSymbols("IANA-ADDRESS-FAMILY-NUMBERS-MIB", "AddressFamilyNumbers")
InterfaceIndex, ifGeneralInformationGroup = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "ifGeneralInformationGroup")
LldpV2PortIdSubtype, LldpV2SystemCapabilitiesMap, LldpV2DestAddressTableIndex, LldpV2ChassisId, LldpV2PortId, LldpV2ChassisIdSubtype, LldpV2ManAddrIfSubtype, LldpV2ManAddress, ieee802dot1mibs = mibBuilder.importSymbols("LLDP-V2-TC-MIB", "LldpV2PortIdSubtype", "LldpV2SystemCapabilitiesMap", "LldpV2DestAddressTableIndex", "LldpV2ChassisId", "LldpV2PortId", "LldpV2ChassisIdSubtype", "LldpV2ManAddrIfSubtype", "LldpV2ManAddress", "ieee802dot1mibs")
ZeroBasedCounter32, TimeFilter = mibBuilder.importSymbols("RMON2-MIB", "ZeroBasedCounter32", "TimeFilter")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
MibIdentifier, ObjectIdentity, ModuleIdentity, Unsigned32, iso, TimeTicks, Gauge32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, NotificationType, IpAddress, Counter64, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "ObjectIdentity", "ModuleIdentity", "Unsigned32", "iso", "TimeTicks", "Gauge32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "NotificationType", "IpAddress", "Counter64", "Counter32")
MacAddress, RowStatus, TimeStamp, DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "RowStatus", "TimeStamp", "DisplayString", "TruthValue", "TextualConvention")
lldpV2MIB = ModuleIdentity((1, 3, 111, 2, 802, 1, 1, 13))
lldpV2MIB.setRevisions(('2009-06-08 00:00',))
if mibBuilder.loadTexts: lldpV2MIB.setLastUpdated('200906080000Z')
if mibBuilder.loadTexts: lldpV2MIB.setOrganization('IEEE 802.1 Working Group')
lldpV2Notifications = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 13, 0))
lldpV2Objects = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 13, 1))
lldpV2Conformance = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 13, 2))
lldpV2Configuration = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 13, 1, 1))
lldpV2Statistics = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 13, 1, 2))
lldpV2LocalSystemData = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 13, 1, 3))
lldpV2RemoteSystemsData = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 13, 1, 4))
lldpV2Extensions = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 13, 1, 5))
lldpV2MessageTxInterval = MibScalar((1, 3, 111, 2, 802, 1, 1, 13, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(5, 32768)).clone(30)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: lldpV2MessageTxInterval.setStatus('current')
lldpV2MessageTxHoldMultiplier = MibScalar((1, 3, 111, 2, 802, 1, 1, 13, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(2, 10)).clone(4)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lldpV2MessageTxHoldMultiplier.setStatus('current')
lldpV2ReinitDelay = MibScalar((1, 3, 111, 2, 802, 1, 1, 13, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 10)).clone(2)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: lldpV2ReinitDelay.setStatus('current')
lldpV2NotificationInterval = MibScalar((1, 3, 111, 2, 802, 1, 1, 13, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(5, 3600)).clone(30)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: lldpV2NotificationInterval.setStatus('current')
lldpV2TxCreditMax = MibScalar((1, 3, 111, 2, 802, 1, 1, 13, 1, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 100)).clone(5)).setUnits('PDUs').setMaxAccess("readwrite")
if mibBuilder.loadTexts: lldpV2TxCreditMax.setStatus('current')
lldpV2MessageFastTx = MibScalar((1, 3, 111, 2, 802, 1, 1, 13, 1, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 3600)).clone(1)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: lldpV2MessageFastTx.setStatus('current')
lldpV2TxFastInit = MibScalar((1, 3, 111, 2, 802, 1, 1, 13, 1, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 8)).clone(4)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lldpV2TxFastInit.setStatus('current')
lldpV2PortConfigTable = MibTable((1, 3, 111, 2, 802, 1, 1, 13, 1, 1, 8), )
if mibBuilder.loadTexts: lldpV2PortConfigTable.setStatus('current')
lldpV2PortConfigEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 13, 1, 1, 8, 1), ).setIndexNames((0, "LLDP-V2-MIB", "lldpV2PortConfigIfIndex"), (0, "LLDP-V2-MIB", "lldpV2PortConfigDestAddressIndex"))
if mibBuilder.loadTexts: lldpV2PortConfigEntry.setStatus('current')
lldpV2PortConfigIfIndex = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 13, 1, 1, 8, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: lldpV2PortConfigIfIndex.setStatus('current')
lldpV2PortConfigDestAddressIndex = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 13, 1, 1, 8, 1, 2), LldpV2DestAddressTableIndex())
if mibBuilder.loadTexts: lldpV2PortConfigDestAddressIndex.setStatus('current')
lldpV2PortConfigAdminStatus = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 13, 1, 1, 8, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("txOnly", 1), ("rxOnly", 2), ("txAndRx", 3), ("disabled", 4))).clone('txAndRx')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lldpV2PortConfigAdminStatus.setStatus('current')
lldpV2PortConfigNotificationEnable = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 13, 1, 1, 8, 1, 4), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lldpV2PortConfigNotificationEnable.setStatus('current')
lldpV2PortConfigTLVsTxEnable = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 13, 1, 1, 8, 1, 5), Bits().clone(namedValues=NamedValues(("portDesc", 0), ("sysName", 1), ("sysDesc", 2), ("sysCap", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lldpV2PortConfigTLVsTxEnable.setStatus('current')
lldpV2DestAddressTable = MibTable((1, 3, 111, 2, 802, 1, 1, 13, 1, 1, 9), )
if mibBuilder.loadTexts: lldpV2DestAddressTable.setStatus('current')
lldpV2DestAddressTableEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 13, 1, 1, 9, 1), ).setIndexNames((0, "LLDP-V2-MIB", "lldpV2AddressTableIndex"))
if mibBuilder.loadTexts: lldpV2DestAddressTableEntry.setStatus('current')
lldpV2AddressTableIndex = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 13, 1, 1, 9, 1, 1), LldpV2DestAddressTableIndex())
if mibBuilder.loadTexts: lldpV2AddressTableIndex.setStatus('current')
lldpV2DestMacAddress = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 13, 1, 1, 9, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpV2DestMacAddress.setStatus('current')
lldpV2ManAddrConfigTxPortsTable = MibTable((1, 3, 111, 2, 802, 1, 1, 13, 1, 1, 10), )
if mibBuilder.loadTexts: lldpV2ManAddrConfigTxPortsTable.setStatus('current')
lldpV2ManAddrConfigTxPortsEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 13, 1, 1, 10, 1), ).setIndexNames((0, "LLDP-V2-MIB", "lldpV2ManAddrConfigIfIndex"), (0, "LLDP-V2-MIB", "lldpV2ManAddrConfigDestAddressIndex"), (0, "LLDP-V2-MIB", "lldpV2ManAddrConfigLocManAddrSubtype"), (0, "LLDP-V2-MIB", "lldpV2ManAddrConfigLocManAddr"))
if mibBuilder.loadTexts: lldpV2ManAddrConfigTxPortsEntry.setStatus('current')
lldpV2ManAddrConfigIfIndex = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 13, 1, 1, 10, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: lldpV2ManAddrConfigIfIndex.setStatus('current')
lldpV2ManAddrConfigDestAddressIndex = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 13, 1, 1, 10, 1, 2), LldpV2DestAddressTableIndex())
if mibBuilder.loadTexts: lldpV2ManAddrConfigDestAddressIndex.setStatus('current')
lldpV2ManAddrConfigLocManAddrSubtype = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 13, 1, 1, 10, 1, 3), AddressFamilyNumbers())
if mibBuilder.loadTexts: lldpV2ManAddrConfigLocManAddrSubtype.setStatus('current')
lldpV2ManAddrConfigLocManAddr = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 13, 1, 1, 10, 1, 4), LldpV2ManAddress())
if mibBuilder.loadTexts: lldpV2ManAddrConfigLocManAddr.setStatus('current')
lldpV2ManAddrConfigTxEnable = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 13, 1, 1, 10, 1, 5), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lldpV2ManAddrConfigTxEnable.setStatus('current')
lldpV2ManAddrConfigRowStatus = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 13, 1, 1, 10, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lldpV2ManAddrConfigRowStatus.setStatus('current')
lldpV2StatsRemTablesLastChangeTime = MibScalar((1, 3, 111, 2, 802, 1, 1, 13, 1, 2, 1), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpV2StatsRemTablesLastChangeTime.setStatus('current')
lldpV2StatsRemTablesInserts = MibScalar((1, 3, 111, 2, 802, 1, 1, 13, 1, 2, 2), ZeroBasedCounter32()).setUnits('table entries').setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpV2StatsRemTablesInserts.setStatus('current')
lldpV2StatsRemTablesDeletes = MibScalar((1, 3, 111, 2, 802, 1, 1, 13, 1, 2, 3), ZeroBasedCounter32()).setUnits('table entries').setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpV2StatsRemTablesDeletes.setStatus('current')
lldpV2StatsRemTablesDrops = MibScalar((1, 3, 111, 2, 802, 1, 1, 13, 1, 2, 4), ZeroBasedCounter32()).setUnits('table entries').setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpV2StatsRemTablesDrops.setStatus('current')
lldpV2StatsRemTablesAgeouts = MibScalar((1, 3, 111, 2, 802, 1, 1, 13, 1, 2, 5), ZeroBasedCounter32()).setUnits('table entries').setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpV2StatsRemTablesAgeouts.setStatus('current')
lldpV2StatsTxPortTable = MibTable((1, 3, 111, 2, 802, 1, 1, 13, 1, 2, 6), )
if mibBuilder.loadTexts: lldpV2StatsTxPortTable.setStatus('current')
lldpV2StatsTxPortEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 13, 1, 2, 6, 1), ).setIndexNames((0, "LLDP-V2-MIB", "lldpV2StatsTxIfIndex"), (0, "LLDP-V2-MIB", "lldpV2StatsTxDestMACAddress"))
if mibBuilder.loadTexts: lldpV2StatsTxPortEntry.setStatus('current')
lldpV2StatsTxIfIndex = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 13, 1, 2, 6, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: lldpV2StatsTxIfIndex.setStatus('current')
lldpV2StatsTxDestMACAddress = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 13, 1, 2, 6, 1, 2), LldpV2DestAddressTableIndex())
if mibBuilder.loadTexts: lldpV2StatsTxDestMACAddress.setStatus('current')
lldpV2StatsTxPortFramesTotal = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 13, 1, 2, 6, 1, 3), Counter32()).setUnits('LLDP frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpV2StatsTxPortFramesTotal.setStatus('current')
lldpV2StatsTxLLDPDULengthErrors = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 13, 1, 2, 6, 1, 4), Counter32()).setUnits('LLDP frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpV2StatsTxLLDPDULengthErrors.setStatus('current')
lldpV2StatsRxPortTable = MibTable((1, 3, 111, 2, 802, 1, 1, 13, 1, 2, 7), )
if mibBuilder.loadTexts: lldpV2StatsRxPortTable.setStatus('current')
lldpV2StatsRxPortEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 13, 1, 2, 7, 1), ).setIndexNames((0, "LLDP-V2-MIB", "lldpV2StatsRxDestIfIndex"), (0, "LLDP-V2-MIB", "lldpV2StatsRxDestMACAddress"))
if mibBuilder.loadTexts: lldpV2StatsRxPortEntry.setStatus('current')
lldpV2StatsRxDestIfIndex = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 13, 1, 2, 7, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: lldpV2StatsRxDestIfIndex.setStatus('current')
lldpV2StatsRxDestMACAddress = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 13, 1, 2, 7, 1, 2), LldpV2DestAddressTableIndex())
if mibBuilder.loadTexts: lldpV2StatsRxDestMACAddress.setStatus('current')
lldpV2StatsRxPortFramesDiscardedTotal = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 13, 1, 2, 7, 1, 3), Counter32()).setUnits('LLDP frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpV2StatsRxPortFramesDiscardedTotal.setStatus('current')
lldpV2StatsRxPortFramesErrors = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 13, 1, 2, 7, 1, 4), Counter32()).setUnits('LLDP frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpV2StatsRxPortFramesErrors.setStatus('current')
lldpV2StatsRxPortFramesTotal = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 13, 1, 2, 7, 1, 5), Counter32()).setUnits('LLDP frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpV2StatsRxPortFramesTotal.setStatus('current')
lldpV2StatsRxPortTLVsDiscardedTotal = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 13, 1, 2, 7, 1, 6), Counter32()).setUnits('TLVs').setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpV2StatsRxPortTLVsDiscardedTotal.setStatus('current')
lldpV2StatsRxPortTLVsUnrecognizedTotal = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 13, 1, 2, 7, 1, 7), Counter32()).setUnits('TLVs').setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpV2StatsRxPortTLVsUnrecognizedTotal.setStatus('current')
lldpV2StatsRxPortAgeoutsTotal = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 13, 1, 2, 7, 1, 8), ZeroBasedCounter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpV2StatsRxPortAgeoutsTotal.setStatus('current')
lldpV2LocChassisIdSubtype = MibScalar((1, 3, 111, 2, 802, 1, 1, 13, 1, 3, 1), LldpV2ChassisIdSubtype()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpV2LocChassisIdSubtype.setStatus('current')
lldpV2LocChassisId = MibScalar((1, 3, 111, 2, 802, 1, 1, 13, 1, 3, 2), LldpV2ChassisId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpV2LocChassisId.setStatus('current')
lldpV2LocSysName = MibScalar((1, 3, 111, 2, 802, 1, 1, 13, 1, 3, 3), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpV2LocSysName.setStatus('current')
lldpV2LocSysDesc = MibScalar((1, 3, 111, 2, 802, 1, 1, 13, 1, 3, 4), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpV2LocSysDesc.setStatus('current')
lldpV2LocSysCapSupported = MibScalar((1, 3, 111, 2, 802, 1, 1, 13, 1, 3, 5), LldpV2SystemCapabilitiesMap()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpV2LocSysCapSupported.setStatus('current')
lldpV2LocSysCapEnabled = MibScalar((1, 3, 111, 2, 802, 1, 1, 13, 1, 3, 6), LldpV2SystemCapabilitiesMap()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpV2LocSysCapEnabled.setStatus('current')
lldpV2LocPortTable = MibTable((1, 3, 111, 2, 802, 1, 1, 13, 1, 3, 7), )
if mibBuilder.loadTexts: lldpV2LocPortTable.setStatus('current')
lldpV2LocPortEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 13, 1, 3, 7, 1), ).setIndexNames((0, "LLDP-V2-MIB", "lldpV2LocPortIfIndex"))
if mibBuilder.loadTexts: lldpV2LocPortEntry.setStatus('current')
lldpV2LocPortIfIndex = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 13, 1, 3, 7, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: lldpV2LocPortIfIndex.setStatus('current')
lldpV2LocPortIdSubtype = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 13, 1, 3, 7, 1, 2), LldpV2PortIdSubtype()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpV2LocPortIdSubtype.setStatus('current')
lldpV2LocPortId = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 13, 1, 3, 7, 1, 3), LldpV2PortId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpV2LocPortId.setStatus('current')
lldpV2LocPortDesc = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 13, 1, 3, 7, 1, 4), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpV2LocPortDesc.setStatus('current')
lldpV2LocManAddrTable = MibTable((1, 3, 111, 2, 802, 1, 1, 13, 1, 3, 8), )
if mibBuilder.loadTexts: lldpV2LocManAddrTable.setStatus('current')
lldpV2LocManAddrEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 13, 1, 3, 8, 1), ).setIndexNames((0, "LLDP-V2-MIB", "lldpV2LocManAddrSubtype"), (0, "LLDP-V2-MIB", "lldpV2LocManAddr"))
if mibBuilder.loadTexts: lldpV2LocManAddrEntry.setStatus('current')
lldpV2LocManAddrSubtype = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 13, 1, 3, 8, 1, 1), AddressFamilyNumbers())
if mibBuilder.loadTexts: lldpV2LocManAddrSubtype.setStatus('current')
lldpV2LocManAddr = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 13, 1, 3, 8, 1, 2), LldpV2ManAddress())
if mibBuilder.loadTexts: lldpV2LocManAddr.setStatus('current')
lldpV2LocManAddrLen = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 13, 1, 3, 8, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpV2LocManAddrLen.setStatus('current')
lldpV2LocManAddrIfSubtype = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 13, 1, 3, 8, 1, 4), LldpV2ManAddrIfSubtype()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpV2LocManAddrIfSubtype.setStatus('current')
lldpV2LocManAddrIfId = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 13, 1, 3, 8, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpV2LocManAddrIfId.setStatus('current')
lldpV2LocManAddrOID = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 13, 1, 3, 8, 1, 6), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpV2LocManAddrOID.setStatus('current')
lldpV2RemTable = MibTable((1, 3, 111, 2, 802, 1, 1, 13, 1, 4, 1), )
if mibBuilder.loadTexts: lldpV2RemTable.setStatus('current')
lldpV2RemEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 13, 1, 4, 1, 1), ).setIndexNames((0, "LLDP-V2-MIB", "lldpV2RemTimeMark"), (0, "LLDP-V2-MIB", "lldpV2RemLocalIfIndex"), (0, "LLDP-V2-MIB", "lldpV2RemLocalDestMACAddress"), (0, "LLDP-V2-MIB", "lldpV2RemIndex"))
if mibBuilder.loadTexts: lldpV2RemEntry.setStatus('current')
lldpV2RemTimeMark = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 13, 1, 4, 1, 1, 1), TimeFilter())
if mibBuilder.loadTexts: lldpV2RemTimeMark.setStatus('current')
lldpV2RemLocalIfIndex = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 13, 1, 4, 1, 1, 2), InterfaceIndex())
if mibBuilder.loadTexts: lldpV2RemLocalIfIndex.setStatus('current')
lldpV2RemLocalDestMACAddress = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 13, 1, 4, 1, 1, 3), LldpV2DestAddressTableIndex())
if mibBuilder.loadTexts: lldpV2RemLocalDestMACAddress.setStatus('current')
lldpV2RemIndex = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 13, 1, 4, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: lldpV2RemIndex.setStatus('current')
lldpV2RemChassisIdSubtype = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 13, 1, 4, 1, 1, 5), LldpV2ChassisIdSubtype()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpV2RemChassisIdSubtype.setStatus('current')
lldpV2RemChassisId = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 13, 1, 4, 1, 1, 6), LldpV2ChassisId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpV2RemChassisId.setStatus('current')
lldpV2RemPortIdSubtype = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 13, 1, 4, 1, 1, 7), LldpV2PortIdSubtype()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpV2RemPortIdSubtype.setStatus('current')
lldpV2RemPortId = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 13, 1, 4, 1, 1, 8), LldpV2PortId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpV2RemPortId.setStatus('current')
lldpV2RemPortDesc = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 13, 1, 4, 1, 1, 9), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpV2RemPortDesc.setStatus('current')
lldpV2RemSysName = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 13, 1, 4, 1, 1, 10), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpV2RemSysName.setStatus('current')
lldpV2RemSysDesc = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 13, 1, 4, 1, 1, 11), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpV2RemSysDesc.setStatus('current')
lldpV2RemSysCapSupported = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 13, 1, 4, 1, 1, 12), LldpV2SystemCapabilitiesMap()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpV2RemSysCapSupported.setStatus('current')
lldpV2RemSysCapEnabled = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 13, 1, 4, 1, 1, 13), LldpV2SystemCapabilitiesMap()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpV2RemSysCapEnabled.setStatus('current')
lldpV2RemRemoteChanges = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 13, 1, 4, 1, 1, 14), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpV2RemRemoteChanges.setStatus('current')
lldpV2RemTooManyNeighbors = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 13, 1, 4, 1, 1, 15), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpV2RemTooManyNeighbors.setStatus('current')
lldpV2RemManAddrTable = MibTable((1, 3, 111, 2, 802, 1, 1, 13, 1, 4, 2), )
if mibBuilder.loadTexts: lldpV2RemManAddrTable.setStatus('current')
lldpV2RemManAddrEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 13, 1, 4, 2, 1), ).setIndexNames((0, "LLDP-V2-MIB", "lldpV2RemTimeMark"), (0, "LLDP-V2-MIB", "lldpV2RemLocalIfIndex"), (0, "LLDP-V2-MIB", "lldpV2RemLocalDestMACAddress"), (0, "LLDP-V2-MIB", "lldpV2RemIndex"), (0, "LLDP-V2-MIB", "lldpV2RemManAddrSubtype"), (0, "LLDP-V2-MIB", "lldpV2RemManAddr"))
if mibBuilder.loadTexts: lldpV2RemManAddrEntry.setStatus('current')
lldpV2RemManAddrSubtype = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 13, 1, 4, 2, 1, 1), AddressFamilyNumbers())
if mibBuilder.loadTexts: lldpV2RemManAddrSubtype.setStatus('current')
lldpV2RemManAddr = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 13, 1, 4, 2, 1, 2), LldpV2ManAddress())
if mibBuilder.loadTexts: lldpV2RemManAddr.setStatus('current')
lldpV2RemManAddrIfSubtype = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 13, 1, 4, 2, 1, 3), LldpV2ManAddrIfSubtype()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpV2RemManAddrIfSubtype.setStatus('current')
lldpV2RemManAddrIfId = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 13, 1, 4, 2, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpV2RemManAddrIfId.setStatus('current')
lldpV2RemManAddrOID = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 13, 1, 4, 2, 1, 5), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpV2RemManAddrOID.setStatus('current')
lldpV2RemUnknownTLVTable = MibTable((1, 3, 111, 2, 802, 1, 1, 13, 1, 4, 3), )
if mibBuilder.loadTexts: lldpV2RemUnknownTLVTable.setStatus('current')
lldpV2RemUnknownTLVEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 13, 1, 4, 3, 1), ).setIndexNames((0, "LLDP-V2-MIB", "lldpV2RemTimeMark"), (0, "LLDP-V2-MIB", "lldpV2RemLocalIfIndex"), (0, "LLDP-V2-MIB", "lldpV2RemLocalDestMACAddress"), (0, "LLDP-V2-MIB", "lldpV2RemIndex"), (0, "LLDP-V2-MIB", "lldpV2RemUnknownTLVType"))
if mibBuilder.loadTexts: lldpV2RemUnknownTLVEntry.setStatus('current')
lldpV2RemUnknownTLVType = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 13, 1, 4, 3, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(9, 126)))
if mibBuilder.loadTexts: lldpV2RemUnknownTLVType.setStatus('current')
lldpV2RemUnknownTLVInfo = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 13, 1, 4, 3, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 511))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpV2RemUnknownTLVInfo.setStatus('current')
lldpV2RemOrgDefInfoTable = MibTable((1, 3, 111, 2, 802, 1, 1, 13, 1, 4, 4), )
if mibBuilder.loadTexts: lldpV2RemOrgDefInfoTable.setStatus('current')
lldpV2RemOrgDefInfoEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 13, 1, 4, 4, 1), ).setIndexNames((0, "LLDP-V2-MIB", "lldpV2RemTimeMark"), (0, "LLDP-V2-MIB", "lldpV2RemLocalIfIndex"), (0, "LLDP-V2-MIB", "lldpV2RemLocalDestMACAddress"), (0, "LLDP-V2-MIB", "lldpV2RemIndex"), (0, "LLDP-V2-MIB", "lldpV2RemOrgDefInfoOUI"), (0, "LLDP-V2-MIB", "lldpV2RemOrgDefInfoSubtype"), (0, "LLDP-V2-MIB", "lldpV2RemOrgDefInfoIndex"))
if mibBuilder.loadTexts: lldpV2RemOrgDefInfoEntry.setStatus('current')
lldpV2RemOrgDefInfoOUI = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 13, 1, 4, 4, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(3, 3)).setFixedLength(3))
if mibBuilder.loadTexts: lldpV2RemOrgDefInfoOUI.setStatus('current')
lldpV2RemOrgDefInfoSubtype = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 13, 1, 4, 4, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)))
if mibBuilder.loadTexts: lldpV2RemOrgDefInfoSubtype.setStatus('current')
lldpV2RemOrgDefInfoIndex = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 13, 1, 4, 4, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: lldpV2RemOrgDefInfoIndex.setStatus('current')
lldpV2RemOrgDefInfo = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 13, 1, 4, 4, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 507))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpV2RemOrgDefInfo.setStatus('current')
lldpV2NotificationPrefix = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 13, 0, 0))
lldpV2RemTablesChange = NotificationType((1, 3, 111, 2, 802, 1, 1, 13, 0, 0, 1)).setObjects(("LLDP-V2-MIB", "lldpV2StatsRemTablesInserts"), ("LLDP-V2-MIB", "lldpV2StatsRemTablesDeletes"), ("LLDP-V2-MIB", "lldpV2StatsRemTablesDrops"), ("LLDP-V2-MIB", "lldpV2StatsRemTablesAgeouts"))
if mibBuilder.loadTexts: lldpV2RemTablesChange.setStatus('current')
lldpV2Compliances = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 13, 2, 1))
lldpV2Groups = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 13, 2, 2))
lldpV2TxRxCompliance = ModuleCompliance((1, 3, 111, 2, 802, 1, 1, 13, 2, 1, 1)).setObjects(("LLDP-V2-MIB", "lldpV2ConfigGroup"), ("LLDP-V2-MIB", "ifGeneralInformationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lldpV2TxRxCompliance = lldpV2TxRxCompliance.setStatus('current')
lldpV2TxCompliance = ModuleCompliance((1, 3, 111, 2, 802, 1, 1, 13, 2, 1, 2)).setObjects(("LLDP-V2-MIB", "lldpV2ConfigTxGroup"), ("LLDP-V2-MIB", "lldpV2StatsTxGroup"), ("LLDP-V2-MIB", "lldpV2LocSysGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lldpV2TxCompliance = lldpV2TxCompliance.setStatus('current')
lldpV2RxCompliance = ModuleCompliance((1, 3, 111, 2, 802, 1, 1, 13, 2, 1, 3)).setObjects(("LLDP-V2-MIB", "lldpV2ConfigRxGroup"), ("LLDP-V2-MIB", "lldpV2StatsRxGroup"), ("LLDP-V2-MIB", "lldpV2RemSysGroup"), ("LLDP-V2-MIB", "lldpV2NotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lldpV2RxCompliance = lldpV2RxCompliance.setStatus('current')
lldpV2ConfigGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 13, 2, 2, 1)).setObjects(("LLDP-V2-MIB", "lldpV2PortConfigAdminStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lldpV2ConfigGroup = lldpV2ConfigGroup.setStatus('current')
lldpV2ConfigRxGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 13, 2, 2, 2)).setObjects(("LLDP-V2-MIB", "lldpV2NotificationInterval"), ("LLDP-V2-MIB", "lldpV2PortConfigNotificationEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lldpV2ConfigRxGroup = lldpV2ConfigRxGroup.setStatus('current')
lldpV2ConfigTxGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 13, 2, 2, 3)).setObjects(("LLDP-V2-MIB", "lldpV2MessageTxInterval"), ("LLDP-V2-MIB", "lldpV2MessageTxHoldMultiplier"), ("LLDP-V2-MIB", "lldpV2ReinitDelay"), ("LLDP-V2-MIB", "lldpV2PortConfigTLVsTxEnable"), ("LLDP-V2-MIB", "lldpV2ManAddrConfigTxEnable"), ("LLDP-V2-MIB", "lldpV2ManAddrConfigRowStatus"), ("LLDP-V2-MIB", "lldpV2TxCreditMax"), ("LLDP-V2-MIB", "lldpV2MessageFastTx"), ("LLDP-V2-MIB", "lldpV2TxFastInit"), ("LLDP-V2-MIB", "lldpV2DestMacAddress"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lldpV2ConfigTxGroup = lldpV2ConfigTxGroup.setStatus('current')
lldpV2StatsRxGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 13, 2, 2, 4)).setObjects(("LLDP-V2-MIB", "lldpV2StatsRemTablesLastChangeTime"), ("LLDP-V2-MIB", "lldpV2StatsRemTablesInserts"), ("LLDP-V2-MIB", "lldpV2StatsRemTablesDeletes"), ("LLDP-V2-MIB", "lldpV2StatsRemTablesDrops"), ("LLDP-V2-MIB", "lldpV2StatsRemTablesAgeouts"), ("LLDP-V2-MIB", "lldpV2StatsRxPortFramesDiscardedTotal"), ("LLDP-V2-MIB", "lldpV2StatsRxPortFramesErrors"), ("LLDP-V2-MIB", "lldpV2StatsRxPortFramesTotal"), ("LLDP-V2-MIB", "lldpV2StatsRxPortTLVsDiscardedTotal"), ("LLDP-V2-MIB", "lldpV2StatsRxPortTLVsUnrecognizedTotal"), ("LLDP-V2-MIB", "lldpV2StatsRxPortAgeoutsTotal"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lldpV2StatsRxGroup = lldpV2StatsRxGroup.setStatus('current')
lldpV2StatsTxGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 13, 2, 2, 5)).setObjects(("LLDP-V2-MIB", "lldpV2StatsTxPortFramesTotal"), ("LLDP-V2-MIB", "lldpV2StatsTxLLDPDULengthErrors"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lldpV2StatsTxGroup = lldpV2StatsTxGroup.setStatus('current')
lldpV2LocSysGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 13, 2, 2, 6)).setObjects(("LLDP-V2-MIB", "lldpV2LocChassisIdSubtype"), ("LLDP-V2-MIB", "lldpV2LocChassisId"), ("LLDP-V2-MIB", "lldpV2LocPortIdSubtype"), ("LLDP-V2-MIB", "lldpV2LocPortId"), ("LLDP-V2-MIB", "lldpV2LocPortDesc"), ("LLDP-V2-MIB", "lldpV2LocSysDesc"), ("LLDP-V2-MIB", "lldpV2LocSysName"), ("LLDP-V2-MIB", "lldpV2LocSysCapSupported"), ("LLDP-V2-MIB", "lldpV2LocSysCapEnabled"), ("LLDP-V2-MIB", "lldpV2LocManAddrLen"), ("LLDP-V2-MIB", "lldpV2LocManAddrIfSubtype"), ("LLDP-V2-MIB", "lldpV2LocManAddrIfId"), ("LLDP-V2-MIB", "lldpV2LocManAddrOID"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lldpV2LocSysGroup = lldpV2LocSysGroup.setStatus('current')
lldpV2RemSysGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 13, 2, 2, 7)).setObjects(("LLDP-V2-MIB", "lldpV2RemChassisIdSubtype"), ("LLDP-V2-MIB", "lldpV2RemChassisId"), ("LLDP-V2-MIB", "lldpV2RemPortIdSubtype"), ("LLDP-V2-MIB", "lldpV2RemPortId"), ("LLDP-V2-MIB", "lldpV2RemPortDesc"), ("LLDP-V2-MIB", "lldpV2RemSysName"), ("LLDP-V2-MIB", "lldpV2RemSysDesc"), ("LLDP-V2-MIB", "lldpV2RemSysCapSupported"), ("LLDP-V2-MIB", "lldpV2RemSysCapEnabled"), ("LLDP-V2-MIB", "lldpV2RemRemoteChanges"), ("LLDP-V2-MIB", "lldpV2RemTooManyNeighbors"), ("LLDP-V2-MIB", "lldpV2RemManAddrIfSubtype"), ("LLDP-V2-MIB", "lldpV2RemManAddrIfId"), ("LLDP-V2-MIB", "lldpV2RemManAddrOID"), ("LLDP-V2-MIB", "lldpV2RemUnknownTLVInfo"), ("LLDP-V2-MIB", "lldpV2RemOrgDefInfo"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lldpV2RemSysGroup = lldpV2RemSysGroup.setStatus('current')
lldpV2NotificationsGroup = NotificationGroup((1, 3, 111, 2, 802, 1, 1, 13, 2, 2, 8)).setObjects(("LLDP-V2-MIB", "lldpV2RemTablesChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lldpV2NotificationsGroup = lldpV2NotificationsGroup.setStatus('current')
mibBuilder.exportSymbols("LLDP-V2-MIB", lldpV2StatsRemTablesDrops=lldpV2StatsRemTablesDrops, lldpV2RemChassisId=lldpV2RemChassisId, lldpV2TxRxCompliance=lldpV2TxRxCompliance, lldpV2TxCreditMax=lldpV2TxCreditMax, lldpV2StatsTxPortFramesTotal=lldpV2StatsTxPortFramesTotal, lldpV2MessageFastTx=lldpV2MessageFastTx, lldpV2StatsRemTablesLastChangeTime=lldpV2StatsRemTablesLastChangeTime, lldpV2LocSysCapEnabled=lldpV2LocSysCapEnabled, lldpV2RemoteSystemsData=lldpV2RemoteSystemsData, lldpV2Extensions=lldpV2Extensions, lldpV2RemOrgDefInfoEntry=lldpV2RemOrgDefInfoEntry, lldpV2StatsRxGroup=lldpV2StatsRxGroup, lldpV2LocPortEntry=lldpV2LocPortEntry, lldpV2RemUnknownTLVType=lldpV2RemUnknownTLVType, lldpV2PortConfigTable=lldpV2PortConfigTable, lldpV2PortConfigTLVsTxEnable=lldpV2PortConfigTLVsTxEnable, lldpV2StatsRxDestIfIndex=lldpV2StatsRxDestIfIndex, lldpV2ManAddrConfigLocManAddr=lldpV2ManAddrConfigLocManAddr, lldpV2LocManAddrIfId=lldpV2LocManAddrIfId, lldpV2PortConfigNotificationEnable=lldpV2PortConfigNotificationEnable, lldpV2NotificationPrefix=lldpV2NotificationPrefix, lldpV2RemEntry=lldpV2RemEntry, lldpV2LocSysCapSupported=lldpV2LocSysCapSupported, lldpV2RemOrgDefInfo=lldpV2RemOrgDefInfo, lldpV2LocPortIfIndex=lldpV2LocPortIfIndex, lldpV2RemManAddrEntry=lldpV2RemManAddrEntry, PYSNMP_MODULE_ID=lldpV2MIB, lldpV2RemSysCapEnabled=lldpV2RemSysCapEnabled, lldpV2PortConfigAdminStatus=lldpV2PortConfigAdminStatus, lldpV2LocChassisIdSubtype=lldpV2LocChassisIdSubtype, lldpV2RemOrgDefInfoSubtype=lldpV2RemOrgDefInfoSubtype, lldpV2Objects=lldpV2Objects, lldpV2LocSysName=lldpV2LocSysName, lldpV2TxCompliance=lldpV2TxCompliance, lldpV2ManAddrConfigTxEnable=lldpV2ManAddrConfigTxEnable, lldpV2RemSysName=lldpV2RemSysName, lldpV2RemManAddr=lldpV2RemManAddr, lldpV2RemSysGroup=lldpV2RemSysGroup, lldpV2RemManAddrTable=lldpV2RemManAddrTable, lldpV2LocalSystemData=lldpV2LocalSystemData, lldpV2NotificationInterval=lldpV2NotificationInterval, lldpV2Groups=lldpV2Groups, lldpV2ReinitDelay=lldpV2ReinitDelay, lldpV2LocPortDesc=lldpV2LocPortDesc, lldpV2LocChassisId=lldpV2LocChassisId, lldpV2RemUnknownTLVInfo=lldpV2RemUnknownTLVInfo, lldpV2RemUnknownTLVTable=lldpV2RemUnknownTLVTable, lldpV2RemTable=lldpV2RemTable, lldpV2StatsRxPortFramesTotal=lldpV2StatsRxPortFramesTotal, lldpV2StatsRxPortFramesDiscardedTotal=lldpV2StatsRxPortFramesDiscardedTotal, lldpV2RemManAddrSubtype=lldpV2RemManAddrSubtype, lldpV2StatsRxPortEntry=lldpV2StatsRxPortEntry, lldpV2LocPortIdSubtype=lldpV2LocPortIdSubtype, lldpV2DestAddressTable=lldpV2DestAddressTable, lldpV2LocSysGroup=lldpV2LocSysGroup, lldpV2MessageTxHoldMultiplier=lldpV2MessageTxHoldMultiplier, lldpV2ConfigRxGroup=lldpV2ConfigRxGroup, lldpV2TxFastInit=lldpV2TxFastInit, lldpV2ManAddrConfigTxPortsTable=lldpV2ManAddrConfigTxPortsTable, lldpV2RemManAddrIfSubtype=lldpV2RemManAddrIfSubtype, lldpV2RemLocalIfIndex=lldpV2RemLocalIfIndex, lldpV2ManAddrConfigDestAddressIndex=lldpV2ManAddrConfigDestAddressIndex, lldpV2Notifications=lldpV2Notifications, lldpV2Conformance=lldpV2Conformance, lldpV2ManAddrConfigIfIndex=lldpV2ManAddrConfigIfIndex, lldpV2ManAddrConfigLocManAddrSubtype=lldpV2ManAddrConfigLocManAddrSubtype, lldpV2StatsRxPortTLVsDiscardedTotal=lldpV2StatsRxPortTLVsDiscardedTotal, lldpV2RemTimeMark=lldpV2RemTimeMark, lldpV2RemOrgDefInfoTable=lldpV2RemOrgDefInfoTable, lldpV2StatsRxPortAgeoutsTotal=lldpV2StatsRxPortAgeoutsTotal, lldpV2LocManAddr=lldpV2LocManAddr, lldpV2LocPortTable=lldpV2LocPortTable, lldpV2StatsRemTablesAgeouts=lldpV2StatsRemTablesAgeouts, lldpV2RemIndex=lldpV2RemIndex, lldpV2StatsRxPortFramesErrors=lldpV2StatsRxPortFramesErrors, lldpV2RemManAddrIfId=lldpV2RemManAddrIfId, lldpV2LocManAddrSubtype=lldpV2LocManAddrSubtype, lldpV2RemTablesChange=lldpV2RemTablesChange, lldpV2Statistics=lldpV2Statistics, lldpV2RemChassisIdSubtype=lldpV2RemChassisIdSubtype, lldpV2StatsTxPortEntry=lldpV2StatsTxPortEntry, lldpV2RemRemoteChanges=lldpV2RemRemoteChanges, lldpV2RxCompliance=lldpV2RxCompliance, lldpV2RemSysCapSupported=lldpV2RemSysCapSupported, lldpV2StatsRxDestMACAddress=lldpV2StatsRxDestMACAddress, lldpV2RemUnknownTLVEntry=lldpV2RemUnknownTLVEntry, lldpV2RemOrgDefInfoOUI=lldpV2RemOrgDefInfoOUI, lldpV2DestMacAddress=lldpV2DestMacAddress, lldpV2LocManAddrTable=lldpV2LocManAddrTable, lldpV2RemSysDesc=lldpV2RemSysDesc, lldpV2PortConfigEntry=lldpV2PortConfigEntry, lldpV2LocManAddrIfSubtype=lldpV2LocManAddrIfSubtype, lldpV2Compliances=lldpV2Compliances, lldpV2StatsTxPortTable=lldpV2StatsTxPortTable, lldpV2ManAddrConfigRowStatus=lldpV2ManAddrConfigRowStatus, lldpV2NotificationsGroup=lldpV2NotificationsGroup, lldpV2ConfigGroup=lldpV2ConfigGroup, lldpV2LocManAddrOID=lldpV2LocManAddrOID, lldpV2ConfigTxGroup=lldpV2ConfigTxGroup, lldpV2PortConfigDestAddressIndex=lldpV2PortConfigDestAddressIndex, lldpV2LocManAddrLen=lldpV2LocManAddrLen, lldpV2LocSysDesc=lldpV2LocSysDesc, lldpV2StatsRxPortTable=lldpV2StatsRxPortTable, lldpV2StatsTxDestMACAddress=lldpV2StatsTxDestMACAddress, lldpV2RemPortId=lldpV2RemPortId, lldpV2StatsRxPortTLVsUnrecognizedTotal=lldpV2StatsRxPortTLVsUnrecognizedTotal, lldpV2ManAddrConfigTxPortsEntry=lldpV2ManAddrConfigTxPortsEntry, lldpV2RemOrgDefInfoIndex=lldpV2RemOrgDefInfoIndex, lldpV2StatsTxGroup=lldpV2StatsTxGroup, lldpV2RemLocalDestMACAddress=lldpV2RemLocalDestMACAddress, lldpV2MessageTxInterval=lldpV2MessageTxInterval, lldpV2Configuration=lldpV2Configuration, lldpV2PortConfigIfIndex=lldpV2PortConfigIfIndex, lldpV2RemManAddrOID=lldpV2RemManAddrOID, lldpV2StatsRemTablesDeletes=lldpV2StatsRemTablesDeletes, lldpV2LocManAddrEntry=lldpV2LocManAddrEntry, lldpV2DestAddressTableEntry=lldpV2DestAddressTableEntry, lldpV2StatsTxLLDPDULengthErrors=lldpV2StatsTxLLDPDULengthErrors, lldpV2LocPortId=lldpV2LocPortId, lldpV2StatsTxIfIndex=lldpV2StatsTxIfIndex, lldpV2RemPortDesc=lldpV2RemPortDesc, lldpV2AddressTableIndex=lldpV2AddressTableIndex, lldpV2StatsRemTablesInserts=lldpV2StatsRemTablesInserts, lldpV2RemPortIdSubtype=lldpV2RemPortIdSubtype, lldpV2MIB=lldpV2MIB, lldpV2RemTooManyNeighbors=lldpV2RemTooManyNeighbors)
