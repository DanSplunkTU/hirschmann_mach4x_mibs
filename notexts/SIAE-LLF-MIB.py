#
# PySNMP MIB module SIAE-LLF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/siae/SIAE-LLF-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 18:19:21 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
AlarmSeverityCode, AlarmStatus = mibBuilder.importSymbols("SIAE-ALARM-MIB", "AlarmSeverityCode", "AlarmStatus")
siaeMib, = mibBuilder.importSymbols("SIAE-TREE-MIB", "siaeMib")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, NotificationType, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, iso, Bits, TimeTicks, IpAddress, MibIdentifier, ObjectIdentity, Counter32, Gauge32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "NotificationType", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "iso", "Bits", "TimeTicks", "IpAddress", "MibIdentifier", "ObjectIdentity", "Counter32", "Gauge32", "Counter64")
TruthValue, RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "RowStatus", "TextualConvention", "DisplayString")
llf = ModuleIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 85))
if mibBuilder.loadTexts: llf.setLastUpdated('201409020000Z')
if mibBuilder.loadTexts: llf.setOrganization('SIAE MICROELETTRONICA spa')
llfMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 85, 1), Integer32().clone(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: llfMibVersion.setStatus('current')
llfTable = MibTable((1, 3, 6, 1, 4, 1, 3373, 1103, 85, 2), )
if mibBuilder.loadTexts: llfTable.setStatus('current')
llfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3373, 1103, 85, 2, 1), ).setIndexNames((0, "SIAE-LLF-MIB", "llfIndex"))
if mibBuilder.loadTexts: llfEntry.setStatus('current')
llfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 85, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: llfIndex.setStatus('current')
llfEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 85, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2))).clone('disable')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: llfEnable.setStatus('current')
llfUnidirectionalFault = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 85, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2))).clone('disable')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: llfUnidirectionalFault.setStatus('current')
llfDelayTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 85, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 10))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: llfDelayTime.setStatus('current')
llfProtectionMode = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 85, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2))).clone('disable')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: llfProtectionMode.setStatus('current')
llfAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 85, 2, 1, 6), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: llfAlarm.setStatus('current')
llfRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 85, 2, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: llfRowStatus.setStatus('current')
llfMapTable = MibTable((1, 3, 6, 1, 4, 1, 3373, 1103, 85, 3), )
if mibBuilder.loadTexts: llfMapTable.setStatus('current')
llfMapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3373, 1103, 85, 3, 1), ).setIndexNames((0, "SIAE-LLF-MIB", "llfIndex"), (0, "SIAE-LLF-MIB", "llfMapLinkIndex"), (0, "SIAE-LLF-MIB", "llfMapPolIndex"), (0, "SIAE-LLF-MIB", "llfMapCircuitIndex"))
if mibBuilder.loadTexts: llfMapEntry.setStatus('current')
llfMapLinkIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 85, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: llfMapLinkIndex.setStatus('current')
llfMapPolIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 85, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: llfMapPolIndex.setStatus('current')
llfMapCircuitIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 85, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: llfMapCircuitIndex.setStatus('current')
llfMapLosInsertion = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 85, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2))).clone('enable')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: llfMapLosInsertion.setStatus('current')
llfMapInsertionMode = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 85, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("single", 1), ("group", 2))).clone('single')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: llfMapInsertionMode.setStatus('current')
llfMapSignalFail = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 85, 3, 1, 6), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: llfMapSignalFail.setStatus('current')
llfMapRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 85, 3, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: llfMapRowStatus.setStatus('current')
llfCircuitTable = MibTable((1, 3, 6, 1, 4, 1, 3373, 1103, 85, 4), )
if mibBuilder.loadTexts: llfCircuitTable.setStatus('current')
llfCircuitEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3373, 1103, 85, 4, 1), ).setIndexNames((0, "SIAE-LLF-MIB", "llfCircuitLinkIndex"), (0, "SIAE-LLF-MIB", "llfCircuitPolIndex"), (0, "SIAE-LLF-MIB", "llfCircuitIndex"))
if mibBuilder.loadTexts: llfCircuitEntry.setStatus('current')
llfCircuitLinkIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 85, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: llfCircuitLinkIndex.setStatus('current')
llfCircuitPolIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 85, 4, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: llfCircuitPolIndex.setStatus('current')
llfCircuitIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 85, 4, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: llfCircuitIndex.setStatus('current')
llfCircuitLinkLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 85, 4, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: llfCircuitLinkLabel.setStatus('current')
llfCircuitRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 85, 4, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: llfCircuitRowStatus.setStatus('current')
llfAlarmSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 85, 5), AlarmSeverityCode().clone('majorTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: llfAlarmSeverityCode.setStatus('current')
mibBuilder.exportSymbols("SIAE-LLF-MIB", llf=llf, llfRowStatus=llfRowStatus, PYSNMP_MODULE_ID=llf, llfProtectionMode=llfProtectionMode, llfMapInsertionMode=llfMapInsertionMode, llfMapLosInsertion=llfMapLosInsertion, llfCircuitTable=llfCircuitTable, llfMapCircuitIndex=llfMapCircuitIndex, llfAlarm=llfAlarm, llfCircuitRowStatus=llfCircuitRowStatus, llfCircuitLinkLabel=llfCircuitLinkLabel, llfMapRowStatus=llfMapRowStatus, llfMapTable=llfMapTable, llfCircuitLinkIndex=llfCircuitLinkIndex, llfUnidirectionalFault=llfUnidirectionalFault, llfCircuitEntry=llfCircuitEntry, llfAlarmSeverityCode=llfAlarmSeverityCode, llfEnable=llfEnable, llfDelayTime=llfDelayTime, llfEntry=llfEntry, llfMapEntry=llfMapEntry, llfMibVersion=llfMibVersion, llfMapPolIndex=llfMapPolIndex, llfTable=llfTable, llfMapLinkIndex=llfMapLinkIndex, llfCircuitPolIndex=llfCircuitPolIndex, llfIndex=llfIndex, llfCircuitIndex=llfCircuitIndex, llfMapSignalFail=llfMapSignalFail)
