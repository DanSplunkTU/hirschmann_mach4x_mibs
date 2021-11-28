#
# PySNMP MIB module FOUNDRY-SN-MAC-VLAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/foundry/FOUNDRY-SN-MAC-VLAN-MIB
# Produced by pysmi-1.1.3 at Sun Nov 28 20:21:16 2021
# On host fv-az77-612 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, iso, Integer32, NotificationType, Unsigned32, Bits, TimeTicks, ModuleIdentity, Counter32, Counter64, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "iso", "Integer32", "NotificationType", "Unsigned32", "Bits", "TimeTicks", "ModuleIdentity", "Counter32", "Counter64", "IpAddress")
MacAddress, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "TextualConvention", "DisplayString")
snMacVlan = ModuleIdentity((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 30))
snMacVlan.setRevisions(('2007-06-25 00:00',))
if mibBuilder.loadTexts: snMacVlan.setLastUpdated('200706250000Z')
if mibBuilder.loadTexts: snMacVlan.setOrganization('Foundry Networks, Inc')
snMacVlanGlobalObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 30, 1))
snMacVlanTableObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 30, 2))
snMacVlanGlobalClearOper = MibScalar((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 30, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("valid", 0), ("clear", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snMacVlanGlobalClearOper.setStatus('current')
snMacVlanGlobalDynConfigState = MibScalar((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 30, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snMacVlanGlobalDynConfigState.setStatus('current')
snMacVlanPortMemberTable = MibTable((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 30, 2, 1), )
if mibBuilder.loadTexts: snMacVlanPortMemberTable.setStatus('current')
snMacVlanPortMemberEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 30, 2, 1, 1), ).setIndexNames((0, "FOUNDRY-SN-MAC-VLAN-MIB", "snMacVlanPortMemberVLanId"), (0, "FOUNDRY-SN-MAC-VLAN-MIB", "snMacVlanPortMemberPortId"))
if mibBuilder.loadTexts: snMacVlanPortMemberEntry.setStatus('current')
snMacVlanPortMemberVLanId = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 30, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4095)))
if mibBuilder.loadTexts: snMacVlanPortMemberVLanId.setStatus('current')
snMacVlanPortMemberPortId = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 30, 2, 1, 1, 2), InterfaceIndex())
if mibBuilder.loadTexts: snMacVlanPortMemberPortId.setStatus('current')
snMacVlanPortMemberRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 30, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("valid", 2), ("delete", 3), ("create", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snMacVlanPortMemberRowStatus.setStatus('current')
snMacVlanIfTable = MibTable((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 30, 2, 2), )
if mibBuilder.loadTexts: snMacVlanIfTable.setStatus('current')
snMacVlanIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 30, 2, 2, 1), ).setIndexNames((0, "FOUNDRY-SN-MAC-VLAN-MIB", "snMacVlanIfIndex"))
if mibBuilder.loadTexts: snMacVlanIfEntry.setStatus('current')
snMacVlanIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 30, 2, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: snMacVlanIfIndex.setStatus('current')
snMacVlanIfEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 30, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snMacVlanIfEnable.setStatus('current')
snMacVlanIfMaxEntry = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 30, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(2, 32)).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snMacVlanIfMaxEntry.setStatus('current')
snMacVlanIfClearOper = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 30, 2, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("valid", 0), ("clear", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snMacVlanIfClearOper.setStatus('current')
snMacVlanIfClearConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 30, 2, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("valid", 0), ("clear", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snMacVlanIfClearConfig.setStatus('current')
snMacBasedVlanTable = MibTable((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 30, 2, 3), )
if mibBuilder.loadTexts: snMacBasedVlanTable.setStatus('current')
snMacBasedVlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 30, 2, 3, 1), ).setIndexNames((0, "FOUNDRY-SN-MAC-VLAN-MIB", "snMacVlanIfIndex"), (0, "FOUNDRY-SN-MAC-VLAN-MIB", "snMacBasedVlanId"), (0, "FOUNDRY-SN-MAC-VLAN-MIB", "snMacBasedVlanMac"))
if mibBuilder.loadTexts: snMacBasedVlanEntry.setStatus('current')
snMacBasedVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 30, 2, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4095)))
if mibBuilder.loadTexts: snMacBasedVlanId.setStatus('current')
snMacBasedVlanMac = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 30, 2, 3, 1, 2), MacAddress())
if mibBuilder.loadTexts: snMacBasedVlanMac.setStatus('current')
snMacBasedVlanPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 30, 2, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snMacBasedVlanPriority.setStatus('current')
snMacBasedVlanRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 30, 2, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("valid", 2), ("delete", 3), ("create", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snMacBasedVlanRowStatus.setStatus('current')
mibBuilder.exportSymbols("FOUNDRY-SN-MAC-VLAN-MIB", snMacBasedVlanTable=snMacBasedVlanTable, snMacBasedVlanRowStatus=snMacBasedVlanRowStatus, snMacBasedVlanEntry=snMacBasedVlanEntry, PYSNMP_MODULE_ID=snMacVlan, snMacBasedVlanPriority=snMacBasedVlanPriority, snMacVlanPortMemberPortId=snMacVlanPortMemberPortId, snMacVlan=snMacVlan, snMacBasedVlanId=snMacBasedVlanId, snMacVlanIfIndex=snMacVlanIfIndex, snMacVlanIfTable=snMacVlanIfTable, snMacVlanPortMemberEntry=snMacVlanPortMemberEntry, snMacVlanGlobalDynConfigState=snMacVlanGlobalDynConfigState, snMacVlanIfEntry=snMacVlanIfEntry, snMacVlanIfMaxEntry=snMacVlanIfMaxEntry, snMacVlanPortMemberTable=snMacVlanPortMemberTable, snMacBasedVlanMac=snMacBasedVlanMac, snMacVlanIfEnable=snMacVlanIfEnable, snMacVlanGlobalClearOper=snMacVlanGlobalClearOper, snMacVlanGlobalObjects=snMacVlanGlobalObjects, snMacVlanPortMemberRowStatus=snMacVlanPortMemberRowStatus, snMacVlanPortMemberVLanId=snMacVlanPortMemberVLanId, snMacVlanTableObjects=snMacVlanTableObjects, snMacVlanIfClearConfig=snMacVlanIfClearConfig, snMacVlanIfClearOper=snMacVlanIfClearOper)
