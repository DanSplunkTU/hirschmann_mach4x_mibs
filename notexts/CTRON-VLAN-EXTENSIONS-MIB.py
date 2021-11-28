#
# PySNMP MIB module CTRON-VLAN-EXTENSIONS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-VLAN-EXTENSIONS-MIB
# Produced by pysmi-1.1.3 at Sun Nov 28 20:25:16 2021
# On host fv-az77-612 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
ctVlanExt, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctVlanExt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Bits, ObjectIdentity, Counter32, NotificationType, Unsigned32, Integer32, iso, TimeTicks, Counter64, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Bits", "ObjectIdentity", "Counter32", "NotificationType", "Unsigned32", "Integer32", "iso", "TimeTicks", "Counter64", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ctVlanBridgeConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 1))
ctVlanVersionNumber = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctVlanVersionNumber.setStatus('mandatory')
ctVlanSupportedOperationalMode = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("static", 1), ("configurable", 2))).clone('static')).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctVlanSupportedOperationalMode.setStatus('deprecated')
ctVlanCurrentOperationalMode = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 12)).clone(12)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctVlanCurrentOperationalMode.setStatus('deprecated')
ctVlanResetDefaults = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("current", 1), ("reset", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctVlanResetDefaults.setStatus('mandatory')
ctVlanDefaultVIDStickyEgress = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctVlanDefaultVIDStickyEgress.setStatus('mandatory')
ctVlanSupportedPortTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 1, 6), )
if mibBuilder.loadTexts: ctVlanSupportedPortTable.setStatus('mandatory')
ctVlanSupportedPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 1, 6, 1), ).setIndexNames((0, "CTRON-VLAN-EXTENSIONS-MIB", "ctVlanSupportedSlotNum"))
if mibBuilder.loadTexts: ctVlanSupportedPortEntry.setStatus('mandatory')
ctVlanSupportedSlotNum = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 1, 6, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctVlanSupportedSlotNum.setStatus('mandatory')
ctVlanSupportedPortNum = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 1, 6, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctVlanSupportedPortNum.setStatus('mandatory')
ctVlanLearningMode = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ivl", 1), ("svl", 2), ("svlivl", 3))).clone('svl')).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctVlanLearningMode.setStatus('mandatory')
ctVlanTriggerPortConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 2))
ctVlanTriggerPortSetTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 2, 1), )
if mibBuilder.loadTexts: ctVlanTriggerPortSetTable.setStatus('mandatory')
ctVlanTriggerPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 2, 1, 1), ).setIndexNames((0, "CTRON-VLAN-EXTENSIONS-MIB", "ctVlanTriggerSlotNum"))
if mibBuilder.loadTexts: ctVlanTriggerPortEntry.setStatus('mandatory')
ctVlanTriggerSlotNum = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctVlanTriggerSlotNum.setStatus('mandatory')
ctVlanTriggerStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 2, 1, 1, 2), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctVlanTriggerStatus.setStatus('mandatory')
ctVlanPortConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 3))
ctVlanPortConfigTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 3, 1), )
if mibBuilder.loadTexts: ctVlanPortConfigTable.setStatus('mandatory')
ctVlanPortConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 3, 1, 1), ).setIndexNames((0, "CTRON-VLAN-EXTENSIONS-MIB", "ctVlanPortSlotNum"), (0, "CTRON-VLAN-EXTENSIONS-MIB", "ctVlanPortNum"))
if mibBuilder.loadTexts: ctVlanPortConfigEntry.setStatus('mandatory')
ctVlanPortSlotNum = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 3, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctVlanPortSlotNum.setStatus('mandatory')
ctVlanPortNum = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 3, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctVlanPortNum.setStatus('mandatory')
ctVlanPortVID = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctVlanPortVID.setStatus('mandatory')
ctVlanPortDiscardFrame = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noDiscard", 1), ("discardUntagged", 2), ("discardTagged", 3))).clone('noDiscard')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctVlanPortDiscardFrame.setStatus('mandatory')
ctVlanPortOperationalMode = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 3, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("dot1QTrunk", 1), ("hybrid", 2), ("dot1dTrunk", 3))).clone('hybrid')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctVlanPortOperationalMode.setStatus('mandatory')
ctVlanPortIngressFiltering = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 3, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctVlanPortIngressFiltering.setStatus('mandatory')
ctVlanConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 4))
ctVlanNumActiveEntries = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 4, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctVlanNumActiveEntries.setStatus('mandatory')
ctVlanNumConfiguredEntries = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 4, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctVlanNumConfiguredEntries.setStatus('mandatory')
ctVlanMaxNumEntries = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 4, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctVlanMaxNumEntries.setStatus('mandatory')
ctVlanConfigTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 4, 4), )
if mibBuilder.loadTexts: ctVlanConfigTable.setStatus('mandatory')
ctVlanConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 4, 4, 1), ).setIndexNames((0, "CTRON-VLAN-EXTENSIONS-MIB", "ctVlanVID"))
if mibBuilder.loadTexts: ctVlanConfigEntry.setStatus('mandatory')
ctVlanVID = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 4, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctVlanVID.setStatus('mandatory')
ctVlanName = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 4, 4, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctVlanName.setStatus('mandatory')
ctVlanStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 4, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctVlanStatus.setStatus('mandatory')
ctVlanEstablish = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 4, 4, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("create", 1), ("delete", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctVlanEstablish.setStatus('mandatory')
ctVlanIdToFidMapping = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 4, 4, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctVlanIdToFidMapping.setStatus('mandatory')
ctVlanType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 4, 4, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("static", 2), ("dynamicGvrp", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctVlanType.setStatus('mandatory')
ctVlanEgressPortsTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 4, 5), )
if mibBuilder.loadTexts: ctVlanEgressPortsTable.setStatus('mandatory')
ctVlanEgressPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 4, 5, 1), ).setIndexNames((0, "CTRON-VLAN-EXTENSIONS-MIB", "ctVlanEgressPortSlotNum"), (0, "CTRON-VLAN-EXTENSIONS-MIB", "ctVlanEgressVID"))
if mibBuilder.loadTexts: ctVlanEgressPortEntry.setStatus('mandatory')
ctVlanEgressPortSlotNum = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 4, 5, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctVlanEgressPortSlotNum.setStatus('mandatory')
ctVlanEgressVID = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 4, 5, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctVlanEgressVID.setStatus('mandatory')
ctVlanEgressList = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 4, 5, 1, 3), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctVlanEgressList.setStatus('mandatory')
ctVlanEgressUntaggedList = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 4, 5, 1, 4), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctVlanEgressUntaggedList.setStatus('mandatory')
ctVlanProtocolAssign = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 5))
ctVlanProtocolStatus = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 5, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctVlanProtocolStatus.setStatus('mandatory')
ctMaxNumVlanProtoEntries = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 5, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctMaxNumVlanProtoEntries.setStatus('mandatory')
ctVlanProtoAssignTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 5, 3), )
if mibBuilder.loadTexts: ctVlanProtoAssignTable.setStatus('mandatory')
ctVlanProtoAssignEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 5, 3, 1), ).setIndexNames((0, "CTRON-VLAN-EXTENSIONS-MIB", "ctVlanVID"), (0, "CTRON-VLAN-EXTENSIONS-MIB", "ctVlanProtoEtherType"))
if mibBuilder.loadTexts: ctVlanProtoAssignEntry.setStatus('mandatory')
ctVlanProtoEtherType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 5, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctVlanProtoEtherType.setStatus('mandatory')
ctVlanProtoEstablish = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 5, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("create", 1), ("delete", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctVlanProtoEstablish.setStatus('mandatory')
ctVlanProtoPortList = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 5, 3, 1, 3), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctVlanProtoPortList.setStatus('mandatory')
mibBuilder.exportSymbols("CTRON-VLAN-EXTENSIONS-MIB", ctVlanPortDiscardFrame=ctVlanPortDiscardFrame, ctVlanPortNum=ctVlanPortNum, ctVlanVersionNumber=ctVlanVersionNumber, ctVlanCurrentOperationalMode=ctVlanCurrentOperationalMode, ctVlanBridgeConfig=ctVlanBridgeConfig, ctVlanPortVID=ctVlanPortVID, ctVlanConfig=ctVlanConfig, ctVlanTriggerPortConfig=ctVlanTriggerPortConfig, ctVlanTriggerPortSetTable=ctVlanTriggerPortSetTable, ctVlanProtoAssignEntry=ctVlanProtoAssignEntry, ctVlanResetDefaults=ctVlanResetDefaults, ctVlanSupportedOperationalMode=ctVlanSupportedOperationalMode, ctVlanTriggerStatus=ctVlanTriggerStatus, ctVlanMaxNumEntries=ctVlanMaxNumEntries, ctVlanEgressVID=ctVlanEgressVID, ctVlanTriggerPortEntry=ctVlanTriggerPortEntry, ctVlanPortOperationalMode=ctVlanPortOperationalMode, ctVlanSupportedPortNum=ctVlanSupportedPortNum, ctVlanPortConfigTable=ctVlanPortConfigTable, ctVlanStatus=ctVlanStatus, ctVlanType=ctVlanType, ctVlanPortConfig=ctVlanPortConfig, ctVlanSupportedSlotNum=ctVlanSupportedSlotNum, ctVlanConfigEntry=ctVlanConfigEntry, ctVlanEgressPortEntry=ctVlanEgressPortEntry, ctVlanProtoAssignTable=ctVlanProtoAssignTable, ctVlanName=ctVlanName, ctVlanProtocolAssign=ctVlanProtocolAssign, ctVlanSupportedPortTable=ctVlanSupportedPortTable, ctVlanProtoEstablish=ctVlanProtoEstablish, ctVlanIdToFidMapping=ctVlanIdToFidMapping, ctVlanSupportedPortEntry=ctVlanSupportedPortEntry, ctVlanConfigTable=ctVlanConfigTable, ctVlanNumConfiguredEntries=ctVlanNumConfiguredEntries, ctVlanProtocolStatus=ctVlanProtocolStatus, ctVlanPortConfigEntry=ctVlanPortConfigEntry, ctVlanProtoPortList=ctVlanProtoPortList, ctVlanEgressPortsTable=ctVlanEgressPortsTable, ctMaxNumVlanProtoEntries=ctMaxNumVlanProtoEntries, ctVlanNumActiveEntries=ctVlanNumActiveEntries, ctVlanEgressList=ctVlanEgressList, ctVlanEstablish=ctVlanEstablish, ctVlanPortIngressFiltering=ctVlanPortIngressFiltering, ctVlanEgressUntaggedList=ctVlanEgressUntaggedList, ctVlanProtoEtherType=ctVlanProtoEtherType, ctVlanLearningMode=ctVlanLearningMode, ctVlanPortSlotNum=ctVlanPortSlotNum, ctVlanEgressPortSlotNum=ctVlanEgressPortSlotNum, ctVlanTriggerSlotNum=ctVlanTriggerSlotNum, ctVlanVID=ctVlanVID, ctVlanDefaultVIDStickyEgress=ctVlanDefaultVIDStickyEgress)
