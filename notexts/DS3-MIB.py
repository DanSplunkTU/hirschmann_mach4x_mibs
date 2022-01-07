#
# PySNMP MIB module DS3-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/DS3-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:07:39 2022
# On host fv-az36-988 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
PerfCurrentCount, PerfIntervalCount, PerfTotalCount = mibBuilder.importSymbols("PerfHist-TC-MIB", "PerfCurrentCount", "PerfIntervalCount", "PerfTotalCount")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
MibIdentifier, ObjectIdentity, ModuleIdentity, iso, Unsigned32, TimeTicks, Gauge32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, transmission, Bits, NotificationType, IpAddress, Counter64, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "ObjectIdentity", "ModuleIdentity", "iso", "Unsigned32", "TimeTicks", "Gauge32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "transmission", "Bits", "NotificationType", "IpAddress", "Counter64", "Counter32")
TruthValue, TimeStamp, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TimeStamp", "TextualConvention", "DisplayString")
ds3 = ModuleIdentity((1, 3, 6, 1, 2, 1, 10, 30))
ds3.setRevisions(('2004-09-08 00:00', '1998-08-01 21:30', '1993-01-25 20:28',))
if mibBuilder.loadTexts: ds3.setLastUpdated('200409080000Z')
if mibBuilder.loadTexts: ds3.setOrganization('IETF AToM MIB Working Group')
dsx3ConfigTable = MibTable((1, 3, 6, 1, 2, 1, 10, 30, 5), )
if mibBuilder.loadTexts: dsx3ConfigTable.setStatus('current')
dsx3ConfigEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 30, 5, 1), ).setIndexNames((0, "DS3-MIB", "dsx3LineIndex"))
if mibBuilder.loadTexts: dsx3ConfigEntry.setStatus('current')
dsx3LineIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 5, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx3LineIndex.setStatus('current')
dsx3IfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 5, 1, 2), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx3IfIndex.setStatus('deprecated')
dsx3TimeElapsed = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 5, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 899))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx3TimeElapsed.setStatus('current')
dsx3ValidIntervals = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 5, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 96))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx3ValidIntervals.setStatus('current')
dsx3LineType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 5, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("dsx3other", 1), ("dsx3M23", 2), ("dsx3SYNTRAN", 3), ("dsx3CbitParity", 4), ("dsx3ClearChannel", 5), ("e3other", 6), ("e3Framed", 7), ("e3Plcp", 8), ("dsx3M13", 9)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsx3LineType.setStatus('current')
dsx3LineCoding = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 5, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("dsx3Other", 1), ("dsx3B3ZS", 2), ("e3HDB3", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsx3LineCoding.setStatus('current')
dsx3SendCode = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 5, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("dsx3SendNoCode", 1), ("dsx3SendLineCode", 2), ("dsx3SendPayloadCode", 3), ("dsx3SendResetCode", 4), ("dsx3SendDS1LoopCode", 5), ("dsx3SendTestPattern", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsx3SendCode.setStatus('current')
dsx3CircuitIdentifier = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 5, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsx3CircuitIdentifier.setStatus('current')
dsx3LoopbackConfig = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 5, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("dsx3NoLoop", 1), ("dsx3PayloadLoop", 2), ("dsx3LineLoop", 3), ("dsx3OtherLoop", 4), ("dsx3InwardLoop", 5), ("dsx3DualLoop", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsx3LoopbackConfig.setStatus('current')
dsx3LineStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 5, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4095))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx3LineStatus.setStatus('current')
dsx3TransmitClockSource = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 5, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("loopTiming", 1), ("localTiming", 2), ("throughTiming", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsx3TransmitClockSource.setStatus('current')
dsx3InvalidIntervals = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 5, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 96))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx3InvalidIntervals.setStatus('current')
dsx3LineLength = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 5, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 64000))).setUnits('meters').setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsx3LineLength.setStatus('current')
dsx3LineStatusLastChange = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 5, 1, 14), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx3LineStatusLastChange.setStatus('current')
dsx3LineStatusChangeTrapEnable = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 5, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsx3LineStatusChangeTrapEnable.setStatus('current')
dsx3LoopbackStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 5, 1, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 127))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx3LoopbackStatus.setStatus('current')
dsx3Channelization = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 5, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("disabled", 1), ("enabledDs1", 2), ("enabledDs2", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsx3Channelization.setStatus('current')
dsx3Ds1ForRemoteLoop = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 5, 1, 18), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 29))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsx3Ds1ForRemoteLoop.setStatus('current')
dsx3CurrentTable = MibTable((1, 3, 6, 1, 2, 1, 10, 30, 6), )
if mibBuilder.loadTexts: dsx3CurrentTable.setStatus('current')
dsx3CurrentEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 30, 6, 1), ).setIndexNames((0, "DS3-MIB", "dsx3CurrentIndex"))
if mibBuilder.loadTexts: dsx3CurrentEntry.setStatus('current')
dsx3CurrentIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 6, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx3CurrentIndex.setStatus('current')
dsx3CurrentPESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 6, 1, 2), PerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx3CurrentPESs.setStatus('current')
dsx3CurrentPSESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 6, 1, 3), PerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx3CurrentPSESs.setStatus('current')
dsx3CurrentSEFSs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 6, 1, 4), PerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx3CurrentSEFSs.setStatus('current')
dsx3CurrentUASs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 6, 1, 5), PerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx3CurrentUASs.setStatus('current')
dsx3CurrentLCVs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 6, 1, 6), PerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx3CurrentLCVs.setStatus('current')
dsx3CurrentPCVs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 6, 1, 7), PerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx3CurrentPCVs.setStatus('current')
dsx3CurrentLESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 6, 1, 8), PerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx3CurrentLESs.setStatus('current')
dsx3CurrentCCVs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 6, 1, 9), PerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx3CurrentCCVs.setStatus('current')
dsx3CurrentCESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 6, 1, 10), PerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx3CurrentCESs.setStatus('current')
dsx3CurrentCSESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 6, 1, 11), PerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx3CurrentCSESs.setStatus('current')
dsx3IntervalTable = MibTable((1, 3, 6, 1, 2, 1, 10, 30, 7), )
if mibBuilder.loadTexts: dsx3IntervalTable.setStatus('current')
dsx3IntervalEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 30, 7, 1), ).setIndexNames((0, "DS3-MIB", "dsx3IntervalIndex"), (0, "DS3-MIB", "dsx3IntervalNumber"))
if mibBuilder.loadTexts: dsx3IntervalEntry.setStatus('current')
dsx3IntervalIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 7, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx3IntervalIndex.setStatus('current')
dsx3IntervalNumber = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 7, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 96))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx3IntervalNumber.setStatus('current')
dsx3IntervalPESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 7, 1, 3), PerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx3IntervalPESs.setStatus('current')
dsx3IntervalPSESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 7, 1, 4), PerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx3IntervalPSESs.setStatus('current')
dsx3IntervalSEFSs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 7, 1, 5), PerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx3IntervalSEFSs.setStatus('current')
dsx3IntervalUASs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 7, 1, 6), PerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx3IntervalUASs.setStatus('current')
dsx3IntervalLCVs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 7, 1, 7), PerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx3IntervalLCVs.setStatus('current')
dsx3IntervalPCVs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 7, 1, 8), PerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx3IntervalPCVs.setStatus('current')
dsx3IntervalLESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 7, 1, 9), PerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx3IntervalLESs.setStatus('current')
dsx3IntervalCCVs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 7, 1, 10), PerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx3IntervalCCVs.setStatus('current')
dsx3IntervalCESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 7, 1, 11), PerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx3IntervalCESs.setStatus('current')
dsx3IntervalCSESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 7, 1, 12), PerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx3IntervalCSESs.setStatus('current')
dsx3IntervalValidData = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 7, 1, 13), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx3IntervalValidData.setStatus('current')
dsx3TotalTable = MibTable((1, 3, 6, 1, 2, 1, 10, 30, 8), )
if mibBuilder.loadTexts: dsx3TotalTable.setStatus('current')
dsx3TotalEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 30, 8, 1), ).setIndexNames((0, "DS3-MIB", "dsx3TotalIndex"))
if mibBuilder.loadTexts: dsx3TotalEntry.setStatus('current')
dsx3TotalIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 8, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx3TotalIndex.setStatus('current')
dsx3TotalPESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 8, 1, 2), PerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx3TotalPESs.setStatus('current')
dsx3TotalPSESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 8, 1, 3), PerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx3TotalPSESs.setStatus('current')
dsx3TotalSEFSs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 8, 1, 4), PerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx3TotalSEFSs.setStatus('current')
dsx3TotalUASs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 8, 1, 5), PerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx3TotalUASs.setStatus('current')
dsx3TotalLCVs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 8, 1, 6), PerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx3TotalLCVs.setStatus('current')
dsx3TotalPCVs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 8, 1, 7), PerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx3TotalPCVs.setStatus('current')
dsx3TotalLESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 8, 1, 8), PerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx3TotalLESs.setStatus('current')
dsx3TotalCCVs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 8, 1, 9), PerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx3TotalCCVs.setStatus('current')
dsx3TotalCESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 8, 1, 10), PerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx3TotalCESs.setStatus('current')
dsx3TotalCSESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 8, 1, 11), PerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx3TotalCSESs.setStatus('current')
dsx3FarEndConfigTable = MibTable((1, 3, 6, 1, 2, 1, 10, 30, 9), )
if mibBuilder.loadTexts: dsx3FarEndConfigTable.setStatus('current')
dsx3FarEndConfigEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 30, 9, 1), ).setIndexNames((0, "DS3-MIB", "dsx3FarEndLineIndex"))
if mibBuilder.loadTexts: dsx3FarEndConfigEntry.setStatus('current')
dsx3FarEndLineIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 9, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx3FarEndLineIndex.setStatus('current')
dsx3FarEndEquipCode = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 9, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 10))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsx3FarEndEquipCode.setStatus('current')
dsx3FarEndLocationIDCode = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 9, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 11))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsx3FarEndLocationIDCode.setStatus('current')
dsx3FarEndFrameIDCode = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 9, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 10))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsx3FarEndFrameIDCode.setStatus('current')
dsx3FarEndUnitCode = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 9, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 6))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsx3FarEndUnitCode.setStatus('current')
dsx3FarEndFacilityIDCode = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 9, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 38))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsx3FarEndFacilityIDCode.setStatus('current')
dsx3FarEndCurrentTable = MibTable((1, 3, 6, 1, 2, 1, 10, 30, 10), )
if mibBuilder.loadTexts: dsx3FarEndCurrentTable.setStatus('current')
dsx3FarEndCurrentEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 30, 10, 1), ).setIndexNames((0, "DS3-MIB", "dsx3FarEndCurrentIndex"))
if mibBuilder.loadTexts: dsx3FarEndCurrentEntry.setStatus('current')
dsx3FarEndCurrentIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 10, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx3FarEndCurrentIndex.setStatus('current')
dsx3FarEndTimeElapsed = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 10, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 899))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx3FarEndTimeElapsed.setStatus('current')
dsx3FarEndValidIntervals = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 10, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 96))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx3FarEndValidIntervals.setStatus('current')
dsx3FarEndCurrentCESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 10, 1, 4), PerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx3FarEndCurrentCESs.setStatus('current')
dsx3FarEndCurrentCSESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 10, 1, 5), PerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx3FarEndCurrentCSESs.setStatus('current')
dsx3FarEndCurrentCCVs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 10, 1, 6), PerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx3FarEndCurrentCCVs.setStatus('current')
dsx3FarEndCurrentUASs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 10, 1, 7), PerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx3FarEndCurrentUASs.setStatus('current')
dsx3FarEndInvalidIntervals = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 10, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 96))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx3FarEndInvalidIntervals.setStatus('current')
dsx3FarEndIntervalTable = MibTable((1, 3, 6, 1, 2, 1, 10, 30, 11), )
if mibBuilder.loadTexts: dsx3FarEndIntervalTable.setStatus('current')
dsx3FarEndIntervalEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 30, 11, 1), ).setIndexNames((0, "DS3-MIB", "dsx3FarEndIntervalIndex"), (0, "DS3-MIB", "dsx3FarEndIntervalNumber"))
if mibBuilder.loadTexts: dsx3FarEndIntervalEntry.setStatus('current')
dsx3FarEndIntervalIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 11, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx3FarEndIntervalIndex.setStatus('current')
dsx3FarEndIntervalNumber = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 11, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 96))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx3FarEndIntervalNumber.setStatus('current')
dsx3FarEndIntervalCESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 11, 1, 3), PerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx3FarEndIntervalCESs.setStatus('current')
dsx3FarEndIntervalCSESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 11, 1, 4), PerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx3FarEndIntervalCSESs.setStatus('current')
dsx3FarEndIntervalCCVs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 11, 1, 5), PerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx3FarEndIntervalCCVs.setStatus('current')
dsx3FarEndIntervalUASs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 11, 1, 6), PerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx3FarEndIntervalUASs.setStatus('current')
dsx3FarEndIntervalValidData = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 11, 1, 7), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx3FarEndIntervalValidData.setStatus('current')
dsx3FarEndTotalTable = MibTable((1, 3, 6, 1, 2, 1, 10, 30, 12), )
if mibBuilder.loadTexts: dsx3FarEndTotalTable.setStatus('current')
dsx3FarEndTotalEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 30, 12, 1), ).setIndexNames((0, "DS3-MIB", "dsx3FarEndTotalIndex"))
if mibBuilder.loadTexts: dsx3FarEndTotalEntry.setStatus('current')
dsx3FarEndTotalIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 12, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx3FarEndTotalIndex.setStatus('current')
dsx3FarEndTotalCESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 12, 1, 2), PerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx3FarEndTotalCESs.setStatus('current')
dsx3FarEndTotalCSESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 12, 1, 3), PerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx3FarEndTotalCSESs.setStatus('current')
dsx3FarEndTotalCCVs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 12, 1, 4), PerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx3FarEndTotalCCVs.setStatus('current')
dsx3FarEndTotalUASs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 12, 1, 5), PerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx3FarEndTotalUASs.setStatus('current')
dsx3FracTable = MibTable((1, 3, 6, 1, 2, 1, 10, 30, 13), )
if mibBuilder.loadTexts: dsx3FracTable.setStatus('deprecated')
dsx3FracEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 30, 13, 1), ).setIndexNames((0, "DS3-MIB", "dsx3FracIndex"), (0, "DS3-MIB", "dsx3FracNumber"))
if mibBuilder.loadTexts: dsx3FracEntry.setStatus('deprecated')
dsx3FracIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 13, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx3FracIndex.setStatus('deprecated')
dsx3FracNumber = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 13, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx3FracNumber.setStatus('deprecated')
dsx3FracIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 30, 13, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsx3FracIfIndex.setStatus('deprecated')
ds3Traps = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 30, 15))
dsx3LineStatusChange = NotificationType((1, 3, 6, 1, 2, 1, 10, 30, 15, 0, 1)).setObjects(("DS3-MIB", "dsx3LineStatus"), ("DS3-MIB", "dsx3LineStatusLastChange"))
if mibBuilder.loadTexts: dsx3LineStatusChange.setStatus('current')
ds3Conformance = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 30, 14))
ds3Groups = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 30, 14, 1))
ds3Compliances = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 30, 14, 2))
ds3Compliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 10, 30, 14, 2, 1)).setObjects(("DS3-MIB", "ds3NearEndConfigGroup"), ("DS3-MIB", "ds3NearEndStatisticsGroup"), ("DS3-MIB", "ds3FarEndGroup"), ("DS3-MIB", "ds3NearEndOptionalTrapGroup"), ("DS3-MIB", "ds3NearEndOptionalConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ds3Compliance = ds3Compliance.setStatus('current')
ds3NearEndConfigGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 30, 14, 1, 1)).setObjects(("DS3-MIB", "dsx3LineIndex"), ("DS3-MIB", "dsx3TimeElapsed"), ("DS3-MIB", "dsx3ValidIntervals"), ("DS3-MIB", "dsx3LineType"), ("DS3-MIB", "dsx3LineCoding"), ("DS3-MIB", "dsx3SendCode"), ("DS3-MIB", "dsx3CircuitIdentifier"), ("DS3-MIB", "dsx3LoopbackConfig"), ("DS3-MIB", "dsx3LineStatus"), ("DS3-MIB", "dsx3TransmitClockSource"), ("DS3-MIB", "dsx3InvalidIntervals"), ("DS3-MIB", "dsx3LineLength"), ("DS3-MIB", "dsx3LoopbackStatus"), ("DS3-MIB", "dsx3Channelization"), ("DS3-MIB", "dsx3Ds1ForRemoteLoop"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ds3NearEndConfigGroup = ds3NearEndConfigGroup.setStatus('current')
ds3NearEndStatisticsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 30, 14, 1, 2)).setObjects(("DS3-MIB", "dsx3CurrentIndex"), ("DS3-MIB", "dsx3CurrentPESs"), ("DS3-MIB", "dsx3CurrentPSESs"), ("DS3-MIB", "dsx3CurrentSEFSs"), ("DS3-MIB", "dsx3CurrentUASs"), ("DS3-MIB", "dsx3CurrentLCVs"), ("DS3-MIB", "dsx3CurrentPCVs"), ("DS3-MIB", "dsx3CurrentLESs"), ("DS3-MIB", "dsx3CurrentCCVs"), ("DS3-MIB", "dsx3CurrentCESs"), ("DS3-MIB", "dsx3CurrentCSESs"), ("DS3-MIB", "dsx3IntervalIndex"), ("DS3-MIB", "dsx3IntervalNumber"), ("DS3-MIB", "dsx3IntervalPESs"), ("DS3-MIB", "dsx3IntervalPSESs"), ("DS3-MIB", "dsx3IntervalSEFSs"), ("DS3-MIB", "dsx3IntervalUASs"), ("DS3-MIB", "dsx3IntervalLCVs"), ("DS3-MIB", "dsx3IntervalPCVs"), ("DS3-MIB", "dsx3IntervalLESs"), ("DS3-MIB", "dsx3IntervalCCVs"), ("DS3-MIB", "dsx3IntervalCESs"), ("DS3-MIB", "dsx3IntervalCSESs"), ("DS3-MIB", "dsx3IntervalValidData"), ("DS3-MIB", "dsx3TotalIndex"), ("DS3-MIB", "dsx3TotalPESs"), ("DS3-MIB", "dsx3TotalPSESs"), ("DS3-MIB", "dsx3TotalSEFSs"), ("DS3-MIB", "dsx3TotalUASs"), ("DS3-MIB", "dsx3TotalLCVs"), ("DS3-MIB", "dsx3TotalPCVs"), ("DS3-MIB", "dsx3TotalLESs"), ("DS3-MIB", "dsx3TotalCCVs"), ("DS3-MIB", "dsx3TotalCESs"), ("DS3-MIB", "dsx3TotalCSESs"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ds3NearEndStatisticsGroup = ds3NearEndStatisticsGroup.setStatus('current')
ds3FarEndGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 30, 14, 1, 3)).setObjects(("DS3-MIB", "dsx3FarEndLineIndex"), ("DS3-MIB", "dsx3FarEndEquipCode"), ("DS3-MIB", "dsx3FarEndLocationIDCode"), ("DS3-MIB", "dsx3FarEndFrameIDCode"), ("DS3-MIB", "dsx3FarEndUnitCode"), ("DS3-MIB", "dsx3FarEndFacilityIDCode"), ("DS3-MIB", "dsx3FarEndCurrentIndex"), ("DS3-MIB", "dsx3FarEndTimeElapsed"), ("DS3-MIB", "dsx3FarEndValidIntervals"), ("DS3-MIB", "dsx3FarEndCurrentCESs"), ("DS3-MIB", "dsx3FarEndCurrentCSESs"), ("DS3-MIB", "dsx3FarEndCurrentCCVs"), ("DS3-MIB", "dsx3FarEndCurrentUASs"), ("DS3-MIB", "dsx3FarEndInvalidIntervals"), ("DS3-MIB", "dsx3FarEndIntervalIndex"), ("DS3-MIB", "dsx3FarEndIntervalNumber"), ("DS3-MIB", "dsx3FarEndIntervalCESs"), ("DS3-MIB", "dsx3FarEndIntervalCSESs"), ("DS3-MIB", "dsx3FarEndIntervalCCVs"), ("DS3-MIB", "dsx3FarEndIntervalUASs"), ("DS3-MIB", "dsx3FarEndIntervalValidData"), ("DS3-MIB", "dsx3FarEndTotalIndex"), ("DS3-MIB", "dsx3FarEndTotalCESs"), ("DS3-MIB", "dsx3FarEndTotalCSESs"), ("DS3-MIB", "dsx3FarEndTotalCCVs"), ("DS3-MIB", "dsx3FarEndTotalUASs"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ds3FarEndGroup = ds3FarEndGroup.setStatus('current')
ds3DeprecatedGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 30, 14, 1, 4)).setObjects(("DS3-MIB", "dsx3IfIndex"), ("DS3-MIB", "dsx3FracIndex"), ("DS3-MIB", "dsx3FracNumber"), ("DS3-MIB", "dsx3FracIfIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ds3DeprecatedGroup = ds3DeprecatedGroup.setStatus('deprecated')
ds3NearEndOptionalConfigGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 30, 14, 1, 5)).setObjects(("DS3-MIB", "dsx3LineStatusLastChange"), ("DS3-MIB", "dsx3LineStatusChangeTrapEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ds3NearEndOptionalConfigGroup = ds3NearEndOptionalConfigGroup.setStatus('current')
ds3NearEndOptionalTrapGroup = NotificationGroup((1, 3, 6, 1, 2, 1, 10, 30, 14, 1, 6)).setObjects(("DS3-MIB", "dsx3LineStatusChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ds3NearEndOptionalTrapGroup = ds3NearEndOptionalTrapGroup.setStatus('current')
mibBuilder.exportSymbols("DS3-MIB", ds3Compliances=ds3Compliances, dsx3FarEndFacilityIDCode=dsx3FarEndFacilityIDCode, dsx3CurrentPSESs=dsx3CurrentPSESs, dsx3FarEndIntervalCSESs=dsx3FarEndIntervalCSESs, dsx3TotalCESs=dsx3TotalCESs, dsx3IfIndex=dsx3IfIndex, ds3Groups=ds3Groups, dsx3FarEndTotalUASs=dsx3FarEndTotalUASs, dsx3FracIndex=dsx3FracIndex, ds3NearEndOptionalTrapGroup=ds3NearEndOptionalTrapGroup, dsx3TotalPSESs=dsx3TotalPSESs, dsx3FracTable=dsx3FracTable, dsx3CurrentSEFSs=dsx3CurrentSEFSs, dsx3IntervalCCVs=dsx3IntervalCCVs, dsx3TotalLCVs=dsx3TotalLCVs, dsx3FarEndIntervalTable=dsx3FarEndIntervalTable, dsx3IntervalEntry=dsx3IntervalEntry, dsx3IntervalSEFSs=dsx3IntervalSEFSs, dsx3TotalSEFSs=dsx3TotalSEFSs, dsx3FarEndCurrentCESs=dsx3FarEndCurrentCESs, dsx3LineStatus=dsx3LineStatus, dsx3TransmitClockSource=dsx3TransmitClockSource, dsx3TimeElapsed=dsx3TimeElapsed, ds3DeprecatedGroup=ds3DeprecatedGroup, dsx3IntervalValidData=dsx3IntervalValidData, ds3FarEndGroup=ds3FarEndGroup, dsx3TotalCSESs=dsx3TotalCSESs, dsx3FarEndLineIndex=dsx3FarEndLineIndex, dsx3IntervalUASs=dsx3IntervalUASs, dsx3FarEndConfigEntry=dsx3FarEndConfigEntry, dsx3LineIndex=dsx3LineIndex, dsx3FarEndCurrentIndex=dsx3FarEndCurrentIndex, dsx3IntervalCSESs=dsx3IntervalCSESs, dsx3FarEndInvalidIntervals=dsx3FarEndInvalidIntervals, dsx3FarEndConfigTable=dsx3FarEndConfigTable, dsx3LineLength=dsx3LineLength, dsx3FracNumber=dsx3FracNumber, dsx3FarEndCurrentCCVs=dsx3FarEndCurrentCCVs, dsx3FarEndTotalIndex=dsx3FarEndTotalIndex, dsx3IntervalPESs=dsx3IntervalPESs, dsx3TotalPCVs=dsx3TotalPCVs, dsx3FarEndIntervalEntry=dsx3FarEndIntervalEntry, dsx3FarEndIntervalCESs=dsx3FarEndIntervalCESs, dsx3FarEndIntervalNumber=dsx3FarEndIntervalNumber, dsx3IntervalIndex=dsx3IntervalIndex, dsx3TotalCCVs=dsx3TotalCCVs, dsx3FarEndTotalCESs=dsx3FarEndTotalCESs, dsx3LineStatusLastChange=dsx3LineStatusLastChange, dsx3IntervalPCVs=dsx3IntervalPCVs, dsx3TotalIndex=dsx3TotalIndex, dsx3FarEndCurrentTable=dsx3FarEndCurrentTable, dsx3TotalLESs=dsx3TotalLESs, dsx3FarEndLocationIDCode=dsx3FarEndLocationIDCode, dsx3CurrentCCVs=dsx3CurrentCCVs, dsx3FarEndIntervalCCVs=dsx3FarEndIntervalCCVs, dsx3FracEntry=dsx3FracEntry, ds3Traps=ds3Traps, dsx3FarEndCurrentEntry=dsx3FarEndCurrentEntry, ds3NearEndStatisticsGroup=ds3NearEndStatisticsGroup, dsx3CurrentIndex=dsx3CurrentIndex, dsx3IntervalLCVs=dsx3IntervalLCVs, dsx3CurrentPCVs=dsx3CurrentPCVs, dsx3SendCode=dsx3SendCode, dsx3LineType=dsx3LineType, dsx3FarEndCurrentUASs=dsx3FarEndCurrentUASs, dsx3Channelization=dsx3Channelization, dsx3TotalEntry=dsx3TotalEntry, ds3NearEndOptionalConfigGroup=ds3NearEndOptionalConfigGroup, dsx3LoopbackStatus=dsx3LoopbackStatus, dsx3FarEndIntervalUASs=dsx3FarEndIntervalUASs, ds3NearEndConfigGroup=ds3NearEndConfigGroup, PYSNMP_MODULE_ID=ds3, dsx3ConfigEntry=dsx3ConfigEntry, dsx3FarEndIntervalValidData=dsx3FarEndIntervalValidData, dsx3IntervalPSESs=dsx3IntervalPSESs, dsx3FarEndTotalCSESs=dsx3FarEndTotalCSESs, dsx3CurrentTable=dsx3CurrentTable, dsx3FarEndTotalTable=dsx3FarEndTotalTable, dsx3TotalUASs=dsx3TotalUASs, dsx3FarEndEquipCode=dsx3FarEndEquipCode, dsx3CurrentLESs=dsx3CurrentLESs, dsx3FarEndIntervalIndex=dsx3FarEndIntervalIndex, dsx3FracIfIndex=dsx3FracIfIndex, dsx3FarEndTotalEntry=dsx3FarEndTotalEntry, dsx3CircuitIdentifier=dsx3CircuitIdentifier, dsx3ValidIntervals=dsx3ValidIntervals, dsx3TotalTable=dsx3TotalTable, ds3Conformance=ds3Conformance, dsx3FarEndUnitCode=dsx3FarEndUnitCode, dsx3FarEndValidIntervals=dsx3FarEndValidIntervals, dsx3FarEndTimeElapsed=dsx3FarEndTimeElapsed, dsx3LineStatusChangeTrapEnable=dsx3LineStatusChangeTrapEnable, dsx3Ds1ForRemoteLoop=dsx3Ds1ForRemoteLoop, dsx3LoopbackConfig=dsx3LoopbackConfig, dsx3LineCoding=dsx3LineCoding, ds3=ds3, dsx3CurrentCESs=dsx3CurrentCESs, dsx3FarEndFrameIDCode=dsx3FarEndFrameIDCode, dsx3InvalidIntervals=dsx3InvalidIntervals, dsx3IntervalNumber=dsx3IntervalNumber, dsx3FarEndCurrentCSESs=dsx3FarEndCurrentCSESs, dsx3ConfigTable=dsx3ConfigTable, ds3Compliance=ds3Compliance, dsx3LineStatusChange=dsx3LineStatusChange, dsx3FarEndTotalCCVs=dsx3FarEndTotalCCVs, dsx3TotalPESs=dsx3TotalPESs, dsx3CurrentPESs=dsx3CurrentPESs, dsx3CurrentEntry=dsx3CurrentEntry, dsx3CurrentUASs=dsx3CurrentUASs, dsx3CurrentCSESs=dsx3CurrentCSESs, dsx3IntervalLESs=dsx3IntervalLESs, dsx3CurrentLCVs=dsx3CurrentLCVs, dsx3IntervalCESs=dsx3IntervalCESs, dsx3IntervalTable=dsx3IntervalTable)
