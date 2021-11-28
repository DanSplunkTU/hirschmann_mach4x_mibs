#
# PySNMP MIB module SFA-INFO (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/ddn/SFA-INFO
# Produced by pysmi-1.1.3 at Sun Nov 28 20:25:44 2021
# On host fv-az77-612 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, Unsigned32, Counter64, iso, Counter32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, enterprises, Gauge32, TimeTicks, IpAddress, NotificationType, MibIdentifier, Integer32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Unsigned32", "Counter64", "iso", "Counter32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "enterprises", "Gauge32", "TimeTicks", "IpAddress", "NotificationType", "MibIdentifier", "Integer32", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
datadirect = MibIdentifier((1, 3, 6, 1, 4, 1, 6894))
unit = MibIdentifier((1, 3, 6, 1, 4, 1, 6894, 2))
eventLog = MibIdentifier((1, 3, 6, 1, 4, 1, 6894, 2, 10))
class DisplayString(OctetString):
    pass

tempNumber = MibScalar((1, 3, 6, 1, 4, 1, 6894, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tempNumber.setStatus('mandatory')
tempTable = MibTable((1, 3, 6, 1, 4, 1, 6894, 2, 2), )
if mibBuilder.loadTexts: tempTable.setStatus('mandatory')
tempEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6894, 2, 2, 1), ).setIndexNames((0, "SFA-INFO", "tempIndex"))
if mibBuilder.loadTexts: tempEntry.setStatus('mandatory')
tempIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6894, 2, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tempIndex.setStatus('mandatory')
tempEncId = MibTableColumn((1, 3, 6, 1, 4, 1, 6894, 2, 2, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tempEncId.setStatus('mandatory')
tempEncPos = MibTableColumn((1, 3, 6, 1, 4, 1, 6894, 2, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tempEncPos.setStatus('mandatory')
tempStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6894, 2, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("normal", 1), ("warning", 2), ("critical", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tempStatus.setStatus('mandatory')
fanNumber = MibScalar((1, 3, 6, 1, 4, 1, 6894, 2, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fanNumber.setStatus('mandatory')
fanTable = MibTable((1, 3, 6, 1, 4, 1, 6894, 2, 4), )
if mibBuilder.loadTexts: fanTable.setStatus('mandatory')
fanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6894, 2, 4, 1), ).setIndexNames((0, "SFA-INFO", "fanIndex"))
if mibBuilder.loadTexts: fanEntry.setStatus('mandatory')
fanIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6894, 2, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fanIndex.setStatus('mandatory')
fanEncId = MibTableColumn((1, 3, 6, 1, 4, 1, 6894, 2, 4, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fanEncId.setStatus('mandatory')
fanEncPos = MibTableColumn((1, 3, 6, 1, 4, 1, 6894, 2, 4, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fanEncPos.setStatus('mandatory')
fanStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6894, 2, 4, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("healthy", 1), ("failure", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fanStatus.setStatus('mandatory')
powerNumber = MibScalar((1, 3, 6, 1, 4, 1, 6894, 2, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: powerNumber.setStatus('mandatory')
powerTable = MibTable((1, 3, 6, 1, 4, 1, 6894, 2, 6), )
if mibBuilder.loadTexts: powerTable.setStatus('mandatory')
powerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6894, 2, 6, 1), ).setIndexNames((0, "SFA-INFO", "powerIndex"))
if mibBuilder.loadTexts: powerEntry.setStatus('mandatory')
powerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6894, 2, 6, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: powerIndex.setStatus('mandatory')
powerEncId = MibTableColumn((1, 3, 6, 1, 4, 1, 6894, 2, 6, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: powerEncId.setStatus('mandatory')
powerEncPos = MibTableColumn((1, 3, 6, 1, 4, 1, 6894, 2, 6, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: powerEncPos.setStatus('mandatory')
powerStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6894, 2, 6, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("healthy", 1), ("failure", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: powerStatus.setStatus('mandatory')
poolNumber = MibScalar((1, 3, 6, 1, 4, 1, 6894, 2, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: poolNumber.setStatus('mandatory')
poolTable = MibTable((1, 3, 6, 1, 4, 1, 6894, 2, 8), )
if mibBuilder.loadTexts: poolTable.setStatus('mandatory')
poolEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6894, 2, 8, 1), ).setIndexNames((0, "SFA-INFO", "poolIndex"))
if mibBuilder.loadTexts: poolEntry.setStatus('mandatory')
poolIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6894, 2, 8, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: poolIndex.setStatus('mandatory')
poolId = MibTableColumn((1, 3, 6, 1, 4, 1, 6894, 2, 8, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: poolId.setStatus('mandatory')
poolType = MibTableColumn((1, 3, 6, 1, 4, 1, 6894, 2, 8, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("storage", 1), ("spare", 2), ("unassigned", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: poolType.setStatus('mandatory')
poolNumDisks = MibTableColumn((1, 3, 6, 1, 4, 1, 6894, 2, 8, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: poolNumDisks.setStatus('mandatory')
physicalDiskTable = MibTable((1, 3, 6, 1, 4, 1, 6894, 2, 9), )
if mibBuilder.loadTexts: physicalDiskTable.setStatus('mandatory')
physicalDiskEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6894, 2, 9, 1), ).setIndexNames((0, "SFA-INFO", "physDiskIndex"))
if mibBuilder.loadTexts: physicalDiskEntry.setStatus('mandatory')
physDiskIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6894, 2, 9, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: physDiskIndex.setStatus('mandatory')
physDiskPoolId = MibTableColumn((1, 3, 6, 1, 4, 1, 6894, 2, 9, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: physDiskPoolId.setStatus('mandatory')
physDiskId = MibTableColumn((1, 3, 6, 1, 4, 1, 6894, 2, 9, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: physDiskId.setStatus('mandatory')
physDiskWWN = MibTableColumn((1, 3, 6, 1, 4, 1, 6894, 2, 9, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: physDiskWWN.setStatus('mandatory')
physDiskEnc = MibTableColumn((1, 3, 6, 1, 4, 1, 6894, 2, 9, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: physDiskEnc.setStatus('mandatory')
physDiskSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 6894, 2, 9, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: physDiskSlot.setStatus('mandatory')
physDiskState = MibTableColumn((1, 3, 6, 1, 4, 1, 6894, 2, 9, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("normal", 1), ("failed", 2), ("predictedfailure", 3), ("unknown", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: physDiskState.setStatus('mandatory')
systemName = MibScalar((1, 3, 6, 1, 4, 1, 6894, 2, 30), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemName.setStatus('mandatory')
eventLogTrapLevel = MibScalar((1, 3, 6, 1, 4, 1, 6894, 2, 10, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("none", 0), ("emergency", 1), ("alert", 2), ("critical", 3), ("error", 4), ("warning", 5), ("notice", 6), ("informational", 7), ("debug", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventLogTrapLevel.setStatus('mandatory')
eventLogNumEntries = MibScalar((1, 3, 6, 1, 4, 1, 6894, 2, 10, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 30))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventLogNumEntries.setStatus('mandatory')
eventLogTable = MibTable((1, 3, 6, 1, 4, 1, 6894, 2, 10, 3), )
if mibBuilder.loadTexts: eventLogTable.setStatus('mandatory')
eventLogEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6894, 2, 10, 3, 1), ).setIndexNames((0, "SFA-INFO", "eventLogIndex"))
if mibBuilder.loadTexts: eventLogEntry.setStatus('mandatory')
eventLogIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6894, 2, 10, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 30))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventLogIndex.setStatus('mandatory')
eventLogLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 6894, 2, 10, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("none", 0), ("emergency", 1), ("alert", 2), ("critical", 3), ("error", 4), ("warning", 5), ("notice", 6), ("informational", 7), ("debug", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventLogLevel.setStatus('mandatory')
eventLogDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 6894, 2, 10, 3, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventLogDescr.setStatus('mandatory')
mibBuilder.exportSymbols("SFA-INFO", datadirect=datadirect, eventLogNumEntries=eventLogNumEntries, eventLogDescr=eventLogDescr, poolNumDisks=poolNumDisks, eventLogTrapLevel=eventLogTrapLevel, tempEntry=tempEntry, tempEncPos=tempEncPos, poolNumber=poolNumber, powerEncPos=powerEncPos, physicalDiskTable=physicalDiskTable, poolIndex=poolIndex, eventLog=eventLog, poolId=poolId, fanNumber=fanNumber, fanEncPos=fanEncPos, tempNumber=tempNumber, systemName=systemName, tempEncId=tempEncId, physDiskId=physDiskId, fanEntry=fanEntry, powerEntry=powerEntry, fanEncId=fanEncId, physDiskEnc=physDiskEnc, powerIndex=powerIndex, poolTable=poolTable, powerTable=powerTable, powerNumber=powerNumber, physDiskPoolId=physDiskPoolId, poolType=poolType, fanTable=fanTable, fanStatus=fanStatus, tempTable=tempTable, poolEntry=poolEntry, eventLogEntry=eventLogEntry, powerStatus=powerStatus, physDiskSlot=physDiskSlot, physDiskIndex=physDiskIndex, eventLogIndex=eventLogIndex, unit=unit, tempStatus=tempStatus, physDiskWWN=physDiskWWN, fanIndex=fanIndex, physDiskState=physDiskState, DisplayString=DisplayString, powerEncId=powerEncId, eventLogTable=eventLogTable, eventLogLevel=eventLogLevel, tempIndex=tempIndex, physicalDiskEntry=physicalDiskEntry)
