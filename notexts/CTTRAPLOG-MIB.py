#
# PySNMP MIB module CTTRAPLOG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTTRAPLOG-MIB
# Produced by pysmi-1.1.3 at Sun Nov 21 00:45:06 2021
# On host fv-az39-63 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ctTrapLog, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctTrapLog")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, NotificationType, ObjectIdentity, TimeTicks, MibIdentifier, Bits, Integer32, Gauge32, ModuleIdentity, Counter32, Unsigned32, IpAddress, iso = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "NotificationType", "ObjectIdentity", "TimeTicks", "MibIdentifier", "Bits", "Integer32", "Gauge32", "ModuleIdentity", "Counter32", "Unsigned32", "IpAddress", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
totalNumberOfEntries = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 44, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: totalNumberOfEntries.setStatus('mandatory')
configTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 44, 2), )
if mibBuilder.loadTexts: configTable.setStatus('mandatory')
configTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 44, 2, 1), ).setIndexNames((0, "CTTRAPLOG-MIB", "slotInChassis"))
if mibBuilder.loadTexts: configTableEntry.setStatus('mandatory')
slotInChassis = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 44, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slotInChassis.setStatus('mandatory')
numEntriesLoggeds = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 44, 2, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: numEntriesLoggeds.setStatus('mandatory')
numEntriesRequested = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 44, 2, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: numEntriesRequested.setStatus('mandatory')
numEntriesAllocated = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 44, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: numEntriesAllocated.setStatus('mandatory')
lastLoggedEntryLogId = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 44, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lastLoggedEntryLogId.setStatus('mandatory')
logCommand = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 44, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("clearLog", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: logCommand.setStatus('mandatory')
wrap = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 44, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wrap.setStatus('mandatory')
trapLogTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 44, 3), )
if mibBuilder.loadTexts: trapLogTable.setStatus('mandatory')
trapLogEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 44, 3, 1), ).setIndexNames((0, "CTTRAPLOG-MIB", "slotChassis"), (0, "CTTRAPLOG-MIB", "logId"))
if mibBuilder.loadTexts: trapLogEntry.setStatus('mandatory')
logId = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 44, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: logId.setStatus('mandatory')
nvmpId = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 44, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nvmpId.setStatus('mandatory')
trapLogAcknowledged = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 44, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapLogAcknowledged.setStatus('mandatory')
trapLogVarBind = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 44, 3, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 1500))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapLogVarBind.setStatus('mandatory')
trapLogDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 44, 3, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapLogDescription.setStatus('mandatory')
timeLogged = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 44, 3, 1, 6), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: timeLogged.setStatus('mandatory')
filterId = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 44, 3, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("informational", 1), ("warning", 2), ("severe", 3), ("fatal", 4), ("existing", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: filterId.setStatus('mandatory')
slotChassis = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 44, 3, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slotChassis.setStatus('mandatory')
trapOID = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 44, 3, 1, 9), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapOID.setStatus('mandatory')
z80Time = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 44, 3, 1, 10), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: z80Time.setStatus('mandatory')
filterTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 44, 4), )
if mibBuilder.loadTexts: filterTable.setStatus('mandatory')
filterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 44, 4, 1), ).setIndexNames((0, "CTTRAPLOG-MIB", "filterSlotInChassis"), (0, "CTTRAPLOG-MIB", "filterFilterId"), (0, "CTTRAPLOG-MIB", "filterLogId"))
if mibBuilder.loadTexts: filterEntry.setStatus('mandatory')
filterLogId = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 44, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: filterLogId.setStatus('mandatory')
filterNvmpId = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 44, 4, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: filterNvmpId.setStatus('mandatory')
filterTrapLogAcknowledged = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 44, 4, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: filterTrapLogAcknowledged.setStatus('mandatory')
filterTrapLogVarBind = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 44, 4, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 1500))).setMaxAccess("readonly")
if mibBuilder.loadTexts: filterTrapLogVarBind.setStatus('mandatory')
filterTrapLogDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 44, 4, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: filterTrapLogDescription.setStatus('mandatory')
filterTimeLogged = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 44, 4, 1, 6), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: filterTimeLogged.setStatus('mandatory')
filterFilterId = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 44, 4, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("informational", 1), ("warning", 2), ("severe", 3), ("fatal", 4), ("existing", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: filterFilterId.setStatus('mandatory')
filterSlotInChassis = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 44, 4, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: filterSlotInChassis.setStatus('mandatory')
filterTrapOID = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 44, 4, 1, 9), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: filterTrapOID.setStatus('mandatory')
filterZ80Time = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 44, 4, 1, 10), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: filterZ80Time.setStatus('mandatory')
trapLoggerAgent = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 44, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2), ("standby", 3), ("elected", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trapLoggerAgent.setStatus('mandatory')
mibBuilder.exportSymbols("CTTRAPLOG-MIB", logId=logId, trapOID=trapOID, trapLogEntry=trapLogEntry, wrap=wrap, trapLogDescription=trapLogDescription, trapLogTable=trapLogTable, filterTrapLogVarBind=filterTrapLogVarBind, trapLoggerAgent=trapLoggerAgent, trapLogAcknowledged=trapLogAcknowledged, filterZ80Time=filterZ80Time, slotInChassis=slotInChassis, filterTrapLogAcknowledged=filterTrapLogAcknowledged, filterSlotInChassis=filterSlotInChassis, filterTrapOID=filterTrapOID, configTableEntry=configTableEntry, filterTable=filterTable, filterTimeLogged=filterTimeLogged, configTable=configTable, filterFilterId=filterFilterId, filterLogId=filterLogId, numEntriesRequested=numEntriesRequested, slotChassis=slotChassis, filterNvmpId=filterNvmpId, filterTrapLogDescription=filterTrapLogDescription, filterId=filterId, totalNumberOfEntries=totalNumberOfEntries, z80Time=z80Time, nvmpId=nvmpId, timeLogged=timeLogged, lastLoggedEntryLogId=lastLoggedEntryLogId, trapLogVarBind=trapLogVarBind, filterEntry=filterEntry, logCommand=logCommand, numEntriesLoggeds=numEntriesLoggeds, numEntriesAllocated=numEntriesAllocated)
