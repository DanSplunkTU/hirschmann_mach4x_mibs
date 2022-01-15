#
# PySNMP MIB module NBS-ODSYS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/mrv/NBS-ODSYS-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 18:13:00 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
NbsTcStatusLevel, NbsTcPartIndex, NbsTcMilliAmp, NbsTcStatusSimple, nbs, NbsTcTemperature, NbsTcMilliVolt = mibBuilder.importSymbols("NBS-MIB", "NbsTcStatusLevel", "NbsTcPartIndex", "NbsTcMilliAmp", "NbsTcStatusSimple", "nbs", "NbsTcTemperature", "NbsTcMilliVolt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, iso, IpAddress, ObjectIdentity, TimeTicks, Counter32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Counter64, MibIdentifier, Gauge32, Bits, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "iso", "IpAddress", "ObjectIdentity", "TimeTicks", "Counter32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Counter64", "MibIdentifier", "Gauge32", "Bits", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
nbsOdsysMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 629, 228))
if mibBuilder.loadTexts: nbsOdsysMib.setLastUpdated('201308200000Z')
if mibBuilder.loadTexts: nbsOdsysMib.setOrganization('NBS')
nbsOdsysChasGrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 228, 2))
if mibBuilder.loadTexts: nbsOdsysChasGrp.setStatus('current')
nbsOdsysCcGrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 228, 3))
if mibBuilder.loadTexts: nbsOdsysCcGrp.setStatus('current')
nbsOdsysFtGrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 228, 4))
if mibBuilder.loadTexts: nbsOdsysFtGrp.setStatus('current')
nbsOdsysPsGrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 228, 5))
if mibBuilder.loadTexts: nbsOdsysPsGrp.setStatus('current')
nbsOdsysEventsGrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 228, 100))
if mibBuilder.loadTexts: nbsOdsysEventsGrp.setStatus('current')
nbsOdsysEvents = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 228, 100, 0))
if mibBuilder.loadTexts: nbsOdsysEvents.setStatus('current')
nbsOdsysChasTable = MibTable((1, 3, 6, 1, 4, 1, 629, 228, 2, 1), )
if mibBuilder.loadTexts: nbsOdsysChasTable.setStatus('current')
nbsOdsysChasEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 228, 2, 1, 1), ).setIndexNames((0, "NBS-ODSYS-MIB", "nbsOdsysChasIndex"))
if mibBuilder.loadTexts: nbsOdsysChasEntry.setStatus('current')
nbsOdsysChasIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 228, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsOdsysChasIndex.setStatus('current')
nbsOdsysChasCcMaxCount = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 228, 2, 1, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsOdsysChasCcMaxCount.setStatus('current')
nbsOdsysChasPsMaxCount = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 228, 2, 1, 1, 20), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsOdsysChasPsMaxCount.setStatus('current')
nbsOdsysChasFtMaxCount = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 228, 2, 1, 1, 30), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsOdsysChasFtMaxCount.setStatus('current')
nbsOdsysCcTable = MibTable((1, 3, 6, 1, 4, 1, 629, 228, 3, 1), )
if mibBuilder.loadTexts: nbsOdsysCcTable.setStatus('current')
nbsOdsysCcEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 228, 3, 1, 1), ).setIndexNames((0, "NBS-ODSYS-MIB", "nbsOdsysCcChasIndex"), (0, "NBS-ODSYS-MIB", "nbsOdsysCcBayIndex"))
if mibBuilder.loadTexts: nbsOdsysCcEntry.setStatus('current')
nbsOdsysCcChasIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 228, 3, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsOdsysCcChasIndex.setStatus('current')
nbsOdsysCcBayIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 228, 3, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsOdsysCcBayIndex.setStatus('current')
nbsOdsysCcChIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 228, 3, 1, 1, 10), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsOdsysCcChIfIndex.setStatus('current')
nbsOdsysCcPartIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 228, 3, 1, 1, 11), NbsTcPartIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsOdsysCcPartIndex.setStatus('current')
nbsOdsysCcThermActual = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 228, 3, 1, 1, 30), NbsTcTemperature()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsOdsysCcThermActual.setStatus('current')
nbsOdsysCcThermLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 228, 3, 1, 1, 40), NbsTcStatusLevel()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsOdsysCcThermLevel.setStatus('current')
nbsOdsysCcThermThreshLoErr = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 228, 3, 1, 1, 41), NbsTcTemperature()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsOdsysCcThermThreshLoErr.setStatus('current')
nbsOdsysCcThermThreshLoWarn = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 228, 3, 1, 1, 42), NbsTcTemperature()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsOdsysCcThermThreshLoWarn.setStatus('current')
nbsOdsysCcThermThreshHiWarn = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 228, 3, 1, 1, 43), NbsTcTemperature()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsOdsysCcThermThreshHiWarn.setStatus('current')
nbsOdsysCcThermThreshHiErr = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 228, 3, 1, 1, 44), NbsTcTemperature()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsOdsysCcThermThreshHiErr.setStatus('current')
nbsOdsysCcOperationalStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 228, 3, 1, 1, 50), NbsTcStatusSimple()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsOdsysCcOperationalStatus.setStatus('current')
nbsOdsysFtTable = MibTable((1, 3, 6, 1, 4, 1, 629, 228, 4, 1), )
if mibBuilder.loadTexts: nbsOdsysFtTable.setStatus('current')
nbsOdsysFtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 228, 4, 1, 1), ).setIndexNames((0, "NBS-ODSYS-MIB", "nbsOdsysFtChasIndex"), (0, "NBS-ODSYS-MIB", "nbsOdsysFtBayIndex"))
if mibBuilder.loadTexts: nbsOdsysFtEntry.setStatus('current')
nbsOdsysFtChasIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 228, 4, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsOdsysFtChasIndex.setStatus('current')
nbsOdsysFtBayIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 228, 4, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsOdsysFtBayIndex.setStatus('current')
nbsOdsysFtOperationalStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 228, 4, 1, 1, 3), NbsTcStatusSimple()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsOdsysFtOperationalStatus.setStatus('current')
nbsOdsysFtChIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 228, 4, 1, 1, 10), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsOdsysFtChIfIndex.setStatus('current')
nbsOdsysFtPartIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 228, 4, 1, 1, 11), NbsTcPartIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsOdsysFtPartIndex.setStatus('current')
nbsOdsysFtFanCount = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 228, 4, 1, 1, 20), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsOdsysFtFanCount.setStatus('current')
nbsOdsysFtThermActual = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 228, 4, 1, 1, 30), NbsTcTemperature()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsOdsysFtThermActual.setStatus('current')
nbsOdsysFtThermLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 228, 4, 1, 1, 40), NbsTcStatusLevel()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsOdsysFtThermLevel.setStatus('current')
nbsOdsysFtThermThreshLoErr = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 228, 4, 1, 1, 41), NbsTcTemperature()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsOdsysFtThermThreshLoErr.setStatus('current')
nbsOdsysFtThermThreshLoWarn = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 228, 4, 1, 1, 42), NbsTcTemperature()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsOdsysFtThermThreshLoWarn.setStatus('current')
nbsOdsysFtThermThreshHiWarn = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 228, 4, 1, 1, 43), NbsTcTemperature()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsOdsysFtThermThreshHiWarn.setStatus('current')
nbsOdsysFtThermThreshHiErr = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 228, 4, 1, 1, 44), NbsTcTemperature()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsOdsysFtThermThreshHiErr.setStatus('current')
nbsOdsysPsTable = MibTable((1, 3, 6, 1, 4, 1, 629, 228, 5, 2), )
if mibBuilder.loadTexts: nbsOdsysPsTable.setStatus('current')
nbsOdsysPsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 228, 5, 2, 1), ).setIndexNames((0, "NBS-ODSYS-MIB", "nbsOdsysPsChasIndex"), (0, "NBS-ODSYS-MIB", "nbsOdsysPsBayIndex"))
if mibBuilder.loadTexts: nbsOdsysPsEntry.setStatus('current')
nbsOdsysPsChasIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 228, 5, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsOdsysPsChasIndex.setStatus('current')
nbsOdsysPsBayIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 228, 5, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsOdsysPsBayIndex.setStatus('current')
nbsOdsysPsOperationalStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 228, 5, 2, 1, 3), NbsTcStatusSimple()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsOdsysPsOperationalStatus.setStatus('current')
nbsOdsysPsChIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 228, 5, 2, 1, 10), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsOdsysPsChIfIndex.setStatus('current')
nbsOdsysPsPartIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 228, 5, 2, 1, 11), NbsTcPartIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsOdsysPsPartIndex.setStatus('current')
nbsOdsysPsFanCount = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 228, 5, 2, 1, 30), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsOdsysPsFanCount.setStatus('current')
nbsOdsysPsThermActual = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 228, 5, 2, 1, 40), NbsTcTemperature()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsOdsysPsThermActual.setStatus('current')
nbsOdsysPsThermLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 228, 5, 2, 1, 41), NbsTcStatusLevel()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsOdsysPsThermLevel.setStatus('current')
nbsOdsysPsThermThreshLoErr = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 228, 5, 2, 1, 42), NbsTcTemperature()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsOdsysPsThermThreshLoErr.setStatus('current')
nbsOdsysPsThermThreshLoWarn = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 228, 5, 2, 1, 43), NbsTcTemperature()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsOdsysPsThermThreshLoWarn.setStatus('current')
nbsOdsysPsThermThreshHiWarn = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 228, 5, 2, 1, 44), NbsTcTemperature()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsOdsysPsThermThreshHiWarn.setStatus('current')
nbsOdsysPsThermThreshHiErr = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 228, 5, 2, 1, 45), NbsTcTemperature()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsOdsysPsThermThreshHiErr.setStatus('current')
nbsOdsysPsVInActual = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 228, 5, 2, 1, 50), NbsTcMilliVolt()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsOdsysPsVInActual.setStatus('current')
nbsOdsysPsVInLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 228, 5, 2, 1, 51), NbsTcStatusLevel()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsOdsysPsVInLevel.setStatus('current')
nbsOdsysPsVInThreshLoErr = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 228, 5, 2, 1, 52), NbsTcMilliVolt()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsOdsysPsVInThreshLoErr.setStatus('current')
nbsOdsysPsVInThreshLoWarn = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 228, 5, 2, 1, 53), NbsTcMilliVolt()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsOdsysPsVInThreshLoWarn.setStatus('current')
nbsOdsysPsVInThreshHiWarn = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 228, 5, 2, 1, 54), NbsTcMilliVolt()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsOdsysPsVInThreshHiWarn.setStatus('current')
nbsOdsysPsVInThreshHiErr = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 228, 5, 2, 1, 55), NbsTcMilliVolt()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsOdsysPsVInThreshHiErr.setStatus('current')
nbsOdsysPsVOutActual = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 228, 5, 2, 1, 60), NbsTcMilliVolt()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsOdsysPsVOutActual.setStatus('current')
nbsOdsysPsVOutLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 228, 5, 2, 1, 61), NbsTcStatusLevel()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsOdsysPsVOutLevel.setStatus('current')
nbsOdsysPsVOutThreshLoErr = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 228, 5, 2, 1, 62), NbsTcMilliVolt()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsOdsysPsVOutThreshLoErr.setStatus('current')
nbsOdsysPsVOutThreshLoWarn = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 228, 5, 2, 1, 63), NbsTcMilliVolt()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsOdsysPsVOutThreshLoWarn.setStatus('current')
nbsOdsysPsVOutThreshHiWarn = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 228, 5, 2, 1, 64), NbsTcMilliVolt()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsOdsysPsVOutThreshHiWarn.setStatus('current')
nbsOdsysPsVOutThreshHiErr = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 228, 5, 2, 1, 65), NbsTcMilliVolt()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsOdsysPsVOutThreshHiErr.setStatus('current')
nbsOdsysPsIInActual = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 228, 5, 2, 1, 70), NbsTcMilliAmp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsOdsysPsIInActual.setStatus('current')
nbsOdsysPsIInLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 228, 5, 2, 1, 71), NbsTcStatusLevel()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsOdsysPsIInLevel.setStatus('current')
nbsOdsysPsIInThreshLoErr = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 228, 5, 2, 1, 72), NbsTcMilliAmp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsOdsysPsIInThreshLoErr.setStatus('current')
nbsOdsysPsIInThreshLoWarn = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 228, 5, 2, 1, 73), NbsTcMilliAmp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsOdsysPsIInThreshLoWarn.setStatus('current')
nbsOdsysPsIInThreshHiWarn = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 228, 5, 2, 1, 74), NbsTcMilliAmp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsOdsysPsIInThreshHiWarn.setStatus('current')
nbsOdsysPsIInThreshHiErr = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 228, 5, 2, 1, 75), NbsTcMilliAmp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsOdsysPsIInThreshHiErr.setStatus('current')
nbsOdsysPsIOutActual = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 228, 5, 2, 1, 80), NbsTcMilliAmp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsOdsysPsIOutActual.setStatus('current')
nbsOdsysPsIOutLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 228, 5, 2, 1, 81), NbsTcStatusLevel()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsOdsysPsIOutLevel.setStatus('current')
nbsOdsysPsIOutThreshLoErr = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 228, 5, 2, 1, 82), NbsTcMilliAmp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsOdsysPsIOutThreshLoErr.setStatus('current')
nbsOdsysPsIOutThreshLoWarn = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 228, 5, 2, 1, 83), NbsTcMilliAmp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsOdsysPsIOutThreshLoWarn.setStatus('current')
nbsOdsysPsIOutThreshHiWarn = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 228, 5, 2, 1, 84), NbsTcMilliAmp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsOdsysPsIOutThreshHiWarn.setStatus('current')
nbsOdsysPsIOutThreshHiErr = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 228, 5, 2, 1, 85), NbsTcMilliAmp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsOdsysPsIOutThreshHiErr.setStatus('current')
nbsOdsysTrapCcThermLevelBad = NotificationType((1, 3, 6, 1, 4, 1, 629, 228, 100, 0, 30)).setObjects(("NBS-ODSYS-MIB", "nbsOdsysCcChasIndex"), ("NBS-ODSYS-MIB", "nbsOdsysCcBayIndex"), ("NBS-ODSYS-MIB", "nbsOdsysCcThermActual"), ("NBS-ODSYS-MIB", "nbsOdsysCcThermLevel"))
if mibBuilder.loadTexts: nbsOdsysTrapCcThermLevelBad.setStatus('current')
nbsOdsysTrapCcThermLevelOk = NotificationType((1, 3, 6, 1, 4, 1, 629, 228, 100, 0, 31)).setObjects(("NBS-ODSYS-MIB", "nbsOdsysCcChasIndex"), ("NBS-ODSYS-MIB", "nbsOdsysCcBayIndex"), ("NBS-ODSYS-MIB", "nbsOdsysCcThermActual"), ("NBS-ODSYS-MIB", "nbsOdsysCcThermLevel"))
if mibBuilder.loadTexts: nbsOdsysTrapCcThermLevelOk.setStatus('current')
nbsOdsysTrapFtThermLevelBad = NotificationType((1, 3, 6, 1, 4, 1, 629, 228, 100, 0, 40)).setObjects(("NBS-ODSYS-MIB", "nbsOdsysFtChasIndex"), ("NBS-ODSYS-MIB", "nbsOdsysFtBayIndex"), ("NBS-ODSYS-MIB", "nbsOdsysFtThermActual"), ("NBS-ODSYS-MIB", "nbsOdsysFtThermLevel"))
if mibBuilder.loadTexts: nbsOdsysTrapFtThermLevelBad.setStatus('current')
nbsOdsysTrapFtThermLevelOk = NotificationType((1, 3, 6, 1, 4, 1, 629, 228, 100, 0, 41)).setObjects(("NBS-ODSYS-MIB", "nbsOdsysFtChasIndex"), ("NBS-ODSYS-MIB", "nbsOdsysFtBayIndex"), ("NBS-ODSYS-MIB", "nbsOdsysFtThermActual"), ("NBS-ODSYS-MIB", "nbsOdsysFtThermLevel"))
if mibBuilder.loadTexts: nbsOdsysTrapFtThermLevelOk.setStatus('current')
nbsOdsysTrapPsThermLevelBad = NotificationType((1, 3, 6, 1, 4, 1, 629, 228, 100, 0, 50)).setObjects(("NBS-ODSYS-MIB", "nbsOdsysPsChasIndex"), ("NBS-ODSYS-MIB", "nbsOdsysPsBayIndex"), ("NBS-ODSYS-MIB", "nbsOdsysPsThermActual"), ("NBS-ODSYS-MIB", "nbsOdsysPsThermLevel"))
if mibBuilder.loadTexts: nbsOdsysTrapPsThermLevelBad.setStatus('current')
nbsOdsysTrapPsThermLevelOk = NotificationType((1, 3, 6, 1, 4, 1, 629, 228, 100, 0, 51)).setObjects(("NBS-ODSYS-MIB", "nbsOdsysPsChasIndex"), ("NBS-ODSYS-MIB", "nbsOdsysPsBayIndex"), ("NBS-ODSYS-MIB", "nbsOdsysPsThermActual"), ("NBS-ODSYS-MIB", "nbsOdsysPsThermLevel"))
if mibBuilder.loadTexts: nbsOdsysTrapPsThermLevelOk.setStatus('current')
nbsOdsysTrapPsVInLevelBad = NotificationType((1, 3, 6, 1, 4, 1, 629, 228, 100, 0, 60)).setObjects(("NBS-ODSYS-MIB", "nbsOdsysPsChasIndex"), ("NBS-ODSYS-MIB", "nbsOdsysPsBayIndex"), ("NBS-ODSYS-MIB", "nbsOdsysPsVInActual"), ("NBS-ODSYS-MIB", "nbsOdsysPsVInLevel"))
if mibBuilder.loadTexts: nbsOdsysTrapPsVInLevelBad.setStatus('current')
nbsOdsysTrapPsVInLevelOk = NotificationType((1, 3, 6, 1, 4, 1, 629, 228, 100, 0, 61)).setObjects(("NBS-ODSYS-MIB", "nbsOdsysPsChasIndex"), ("NBS-ODSYS-MIB", "nbsOdsysPsBayIndex"), ("NBS-ODSYS-MIB", "nbsOdsysPsVInActual"), ("NBS-ODSYS-MIB", "nbsOdsysPsVInLevel"))
if mibBuilder.loadTexts: nbsOdsysTrapPsVInLevelOk.setStatus('current')
nbsOdsysTrapPsVOutLevelBad = NotificationType((1, 3, 6, 1, 4, 1, 629, 228, 100, 0, 70)).setObjects(("NBS-ODSYS-MIB", "nbsOdsysPsChasIndex"), ("NBS-ODSYS-MIB", "nbsOdsysPsBayIndex"), ("NBS-ODSYS-MIB", "nbsOdsysPsVOutActual"), ("NBS-ODSYS-MIB", "nbsOdsysPsVOutLevel"))
if mibBuilder.loadTexts: nbsOdsysTrapPsVOutLevelBad.setStatus('current')
nbsOdsysTrapPsVOutLevelOk = NotificationType((1, 3, 6, 1, 4, 1, 629, 228, 100, 0, 71)).setObjects(("NBS-ODSYS-MIB", "nbsOdsysPsChasIndex"), ("NBS-ODSYS-MIB", "nbsOdsysPsBayIndex"), ("NBS-ODSYS-MIB", "nbsOdsysPsVOutActual"), ("NBS-ODSYS-MIB", "nbsOdsysPsVOutLevel"))
if mibBuilder.loadTexts: nbsOdsysTrapPsVOutLevelOk.setStatus('current')
nbsOdsysTrapPsIInLevelBad = NotificationType((1, 3, 6, 1, 4, 1, 629, 228, 100, 0, 80)).setObjects(("NBS-ODSYS-MIB", "nbsOdsysPsChasIndex"), ("NBS-ODSYS-MIB", "nbsOdsysPsBayIndex"), ("NBS-ODSYS-MIB", "nbsOdsysPsIInActual"), ("NBS-ODSYS-MIB", "nbsOdsysPsIInLevel"))
if mibBuilder.loadTexts: nbsOdsysTrapPsIInLevelBad.setStatus('current')
nbsOdsysTrapPsIInLevelOk = NotificationType((1, 3, 6, 1, 4, 1, 629, 228, 100, 0, 81)).setObjects(("NBS-ODSYS-MIB", "nbsOdsysPsChasIndex"), ("NBS-ODSYS-MIB", "nbsOdsysPsBayIndex"), ("NBS-ODSYS-MIB", "nbsOdsysPsIInActual"), ("NBS-ODSYS-MIB", "nbsOdsysPsIInLevel"))
if mibBuilder.loadTexts: nbsOdsysTrapPsIInLevelOk.setStatus('current')
nbsOdsysTrapPsIOutLevelBad = NotificationType((1, 3, 6, 1, 4, 1, 629, 228, 100, 0, 90)).setObjects(("NBS-ODSYS-MIB", "nbsOdsysPsChasIndex"), ("NBS-ODSYS-MIB", "nbsOdsysPsBayIndex"), ("NBS-ODSYS-MIB", "nbsOdsysPsIOutActual"), ("NBS-ODSYS-MIB", "nbsOdsysPsIOutLevel"))
if mibBuilder.loadTexts: nbsOdsysTrapPsIOutLevelBad.setStatus('current')
nbsOdsysTrapPsIOutLevelOk = NotificationType((1, 3, 6, 1, 4, 1, 629, 228, 100, 0, 91)).setObjects(("NBS-ODSYS-MIB", "nbsOdsysPsChasIndex"), ("NBS-ODSYS-MIB", "nbsOdsysPsBayIndex"), ("NBS-ODSYS-MIB", "nbsOdsysPsIOutActual"), ("NBS-ODSYS-MIB", "nbsOdsysPsIOutLevel"))
if mibBuilder.loadTexts: nbsOdsysTrapPsIOutLevelOk.setStatus('current')
nbsOdsysTrapCcFailed = NotificationType((1, 3, 6, 1, 4, 1, 629, 228, 100, 0, 131)).setObjects(("NBS-ODSYS-MIB", "nbsOdsysCcChasIndex"), ("NBS-ODSYS-MIB", "nbsOdsysCcBayIndex"))
if mibBuilder.loadTexts: nbsOdsysTrapCcFailed.setStatus('current')
nbsOdsysTrapCcRestored = NotificationType((1, 3, 6, 1, 4, 1, 629, 228, 100, 0, 132)).setObjects(("NBS-ODSYS-MIB", "nbsOdsysCcChasIndex"), ("NBS-ODSYS-MIB", "nbsOdsysCcBayIndex"))
if mibBuilder.loadTexts: nbsOdsysTrapCcRestored.setStatus('current')
nbsOdsysTrapCcRemoved = NotificationType((1, 3, 6, 1, 4, 1, 629, 228, 100, 0, 133)).setObjects(("NBS-ODSYS-MIB", "nbsOdsysCcChasIndex"), ("NBS-ODSYS-MIB", "nbsOdsysCcBayIndex"))
if mibBuilder.loadTexts: nbsOdsysTrapCcRemoved.setStatus('current')
nbsOdsysTrapCcInserted = NotificationType((1, 3, 6, 1, 4, 1, 629, 228, 100, 0, 134)).setObjects(("NBS-ODSYS-MIB", "nbsOdsysCcChasIndex"), ("NBS-ODSYS-MIB", "nbsOdsysCcBayIndex"))
if mibBuilder.loadTexts: nbsOdsysTrapCcInserted.setStatus('current')
mibBuilder.exportSymbols("NBS-ODSYS-MIB", nbsOdsysTrapPsVInLevelBad=nbsOdsysTrapPsVInLevelBad, nbsOdsysPsEntry=nbsOdsysPsEntry, nbsOdsysTrapPsVOutLevelBad=nbsOdsysTrapPsVOutLevelBad, nbsOdsysFtOperationalStatus=nbsOdsysFtOperationalStatus, nbsOdsysPsIInLevel=nbsOdsysPsIInLevel, nbsOdsysEvents=nbsOdsysEvents, nbsOdsysTrapCcThermLevelBad=nbsOdsysTrapCcThermLevelBad, nbsOdsysTrapCcRestored=nbsOdsysTrapCcRestored, nbsOdsysCcPartIndex=nbsOdsysCcPartIndex, nbsOdsysPsVInActual=nbsOdsysPsVInActual, nbsOdsysFtThermActual=nbsOdsysFtThermActual, nbsOdsysPsVInThreshLoErr=nbsOdsysPsVInThreshLoErr, nbsOdsysChasFtMaxCount=nbsOdsysChasFtMaxCount, nbsOdsysChasCcMaxCount=nbsOdsysChasCcMaxCount, nbsOdsysPsOperationalStatus=nbsOdsysPsOperationalStatus, nbsOdsysPsVOutThreshLoErr=nbsOdsysPsVOutThreshLoErr, nbsOdsysPsThermThreshHiErr=nbsOdsysPsThermThreshHiErr, nbsOdsysPsIOutThreshLoWarn=nbsOdsysPsIOutThreshLoWarn, nbsOdsysCcChasIndex=nbsOdsysCcChasIndex, nbsOdsysChasTable=nbsOdsysChasTable, nbsOdsysTrapPsVOutLevelOk=nbsOdsysTrapPsVOutLevelOk, nbsOdsysFtThermThreshLoErr=nbsOdsysFtThermThreshLoErr, nbsOdsysPsVInThreshHiWarn=nbsOdsysPsVInThreshHiWarn, nbsOdsysFtThermLevel=nbsOdsysFtThermLevel, nbsOdsysChasPsMaxCount=nbsOdsysChasPsMaxCount, nbsOdsysFtGrp=nbsOdsysFtGrp, nbsOdsysChasEntry=nbsOdsysChasEntry, nbsOdsysFtThermThreshLoWarn=nbsOdsysFtThermThreshLoWarn, nbsOdsysTrapPsIOutLevelOk=nbsOdsysTrapPsIOutLevelOk, nbsOdsysCcTable=nbsOdsysCcTable, nbsOdsysPsChIfIndex=nbsOdsysPsChIfIndex, PYSNMP_MODULE_ID=nbsOdsysMib, nbsOdsysPsIInThreshHiErr=nbsOdsysPsIInThreshHiErr, nbsOdsysTrapFtThermLevelBad=nbsOdsysTrapFtThermLevelBad, nbsOdsysTrapPsThermLevelBad=nbsOdsysTrapPsThermLevelBad, nbsOdsysTrapCcInserted=nbsOdsysTrapCcInserted, nbsOdsysPsPartIndex=nbsOdsysPsPartIndex, nbsOdsysPsVOutLevel=nbsOdsysPsVOutLevel, nbsOdsysCcGrp=nbsOdsysCcGrp, nbsOdsysTrapCcThermLevelOk=nbsOdsysTrapCcThermLevelOk, nbsOdsysFtBayIndex=nbsOdsysFtBayIndex, nbsOdsysPsIInThreshHiWarn=nbsOdsysPsIInThreshHiWarn, nbsOdsysPsIOutThreshHiWarn=nbsOdsysPsIOutThreshHiWarn, nbsOdsysPsVOutActual=nbsOdsysPsVOutActual, nbsOdsysPsBayIndex=nbsOdsysPsBayIndex, nbsOdsysPsGrp=nbsOdsysPsGrp, nbsOdsysCcEntry=nbsOdsysCcEntry, nbsOdsysPsThermThreshHiWarn=nbsOdsysPsThermThreshHiWarn, nbsOdsysPsIInThreshLoErr=nbsOdsysPsIInThreshLoErr, nbsOdsysTrapCcRemoved=nbsOdsysTrapCcRemoved, nbsOdsysPsIInThreshLoWarn=nbsOdsysPsIInThreshLoWarn, nbsOdsysFtFanCount=nbsOdsysFtFanCount, nbsOdsysPsThermThreshLoWarn=nbsOdsysPsThermThreshLoWarn, nbsOdsysTrapPsIOutLevelBad=nbsOdsysTrapPsIOutLevelBad, nbsOdsysTrapPsIInLevelOk=nbsOdsysTrapPsIInLevelOk, nbsOdsysPsThermThreshLoErr=nbsOdsysPsThermThreshLoErr, nbsOdsysPsVInThreshHiErr=nbsOdsysPsVInThreshHiErr, nbsOdsysTrapPsVInLevelOk=nbsOdsysTrapPsVInLevelOk, nbsOdsysFtEntry=nbsOdsysFtEntry, nbsOdsysPsThermActual=nbsOdsysPsThermActual, nbsOdsysFtPartIndex=nbsOdsysFtPartIndex, nbsOdsysPsIOutThreshHiErr=nbsOdsysPsIOutThreshHiErr, nbsOdsysPsThermLevel=nbsOdsysPsThermLevel, nbsOdsysChasIndex=nbsOdsysChasIndex, nbsOdsysTrapFtThermLevelOk=nbsOdsysTrapFtThermLevelOk, nbsOdsysFtChasIndex=nbsOdsysFtChasIndex, nbsOdsysEventsGrp=nbsOdsysEventsGrp, nbsOdsysTrapCcFailed=nbsOdsysTrapCcFailed, nbsOdsysPsVOutThreshHiWarn=nbsOdsysPsVOutThreshHiWarn, nbsOdsysPsVInLevel=nbsOdsysPsVInLevel, nbsOdsysPsIOutLevel=nbsOdsysPsIOutLevel, nbsOdsysCcOperationalStatus=nbsOdsysCcOperationalStatus, nbsOdsysPsIOutThreshLoErr=nbsOdsysPsIOutThreshLoErr, nbsOdsysTrapPsIInLevelBad=nbsOdsysTrapPsIInLevelBad, nbsOdsysCcThermThreshLoWarn=nbsOdsysCcThermThreshLoWarn, nbsOdsysChasGrp=nbsOdsysChasGrp, nbsOdsysFtChIfIndex=nbsOdsysFtChIfIndex, nbsOdsysCcThermLevel=nbsOdsysCcThermLevel, nbsOdsysCcBayIndex=nbsOdsysCcBayIndex, nbsOdsysPsFanCount=nbsOdsysPsFanCount, nbsOdsysMib=nbsOdsysMib, nbsOdsysCcThermActual=nbsOdsysCcThermActual, nbsOdsysPsChasIndex=nbsOdsysPsChasIndex, nbsOdsysCcThermThreshLoErr=nbsOdsysCcThermThreshLoErr, nbsOdsysFtThermThreshHiWarn=nbsOdsysFtThermThreshHiWarn, nbsOdsysCcThermThreshHiErr=nbsOdsysCcThermThreshHiErr, nbsOdsysFtTable=nbsOdsysFtTable, nbsOdsysPsVOutThreshHiErr=nbsOdsysPsVOutThreshHiErr, nbsOdsysPsIInActual=nbsOdsysPsIInActual, nbsOdsysTrapPsThermLevelOk=nbsOdsysTrapPsThermLevelOk, nbsOdsysPsVOutThreshLoWarn=nbsOdsysPsVOutThreshLoWarn, nbsOdsysPsIOutActual=nbsOdsysPsIOutActual, nbsOdsysPsVInThreshLoWarn=nbsOdsysPsVInThreshLoWarn, nbsOdsysCcChIfIndex=nbsOdsysCcChIfIndex, nbsOdsysPsTable=nbsOdsysPsTable, nbsOdsysCcThermThreshHiWarn=nbsOdsysCcThermThreshHiWarn, nbsOdsysFtThermThreshHiErr=nbsOdsysFtThermThreshHiErr)
