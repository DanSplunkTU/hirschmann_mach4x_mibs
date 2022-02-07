#
# PySNMP MIB module CTRON-FDDI-STAT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-FDDI-STAT-MIB
# Produced by pysmi-1.1.8 at Mon Feb  7 16:12:01 2022
# On host fv-az42-619 platform Linux version 5.11.0-1028-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
ctFDDIStats, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctFDDIStats")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, Bits, ObjectIdentity, ModuleIdentity, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, MibIdentifier, Counter64, Gauge32, Counter32, IpAddress, TimeTicks, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Bits", "ObjectIdentity", "ModuleIdentity", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "MibIdentifier", "Counter64", "Gauge32", "Counter32", "IpAddress", "TimeTicks", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ctFDDIStatsUtil = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 2, 1))
ctFDDIStatsCtlTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 2, 1, 1), )
if mibBuilder.loadTexts: ctFDDIStatsCtlTable.setStatus('mandatory')
ctFDDIStatsCtlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 2, 1, 1, 1), ).setIndexNames((0, "CTRON-FDDI-STAT-MIB", "ctFDDISlot"), (0, "CTRON-FDDI-STAT-MIB", "ctFDDISMT"), (0, "CTRON-FDDI-STAT-MIB", "ctFDDIPath"))
if mibBuilder.loadTexts: ctFDDIStatsCtlEntry.setStatus('mandatory')
ctFDDISlot = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 2, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFDDISlot.setStatus('mandatory')
ctFDDISMT = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 2, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFDDISMT.setStatus('mandatory')
ctFDDIPath = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 2, 1, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFDDIPath.setStatus('mandatory')
ctFDDINextEntry = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 2, 1, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFDDINextEntry.setStatus('mandatory')
ctFDDIResetPeak = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 2, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("normal", 1), ("reset", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctFDDIResetPeak.setStatus('mandatory')
ctFDDIStatsHistoryTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 2, 1, 2), )
if mibBuilder.loadTexts: ctFDDIStatsHistoryTable.setStatus('mandatory')
ctFDDIStatsHistoryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 2, 1, 2, 1), ).setIndexNames((0, "CTRON-FDDI-STAT-MIB", "ctFDDISlot"), (0, "CTRON-FDDI-STAT-MIB", "ctFDDIStatsIndex"))
if mibBuilder.loadTexts: ctFDDIStatsHistoryEntry.setStatus('mandatory')
ctFDDIStatsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 2, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFDDIStatsIndex.setStatus('mandatory')
ctFDDIStatsTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 2, 1, 2, 1, 2), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFDDIStatsTimeStamp.setStatus('mandatory')
ctFDDIFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 2, 1, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFDDIFrames.setStatus('mandatory')
ctFDDIBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 2, 1, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFDDIBytes.setStatus('mandatory')
ctFDDIPeakBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 2, 1, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFDDIPeakBytes.setStatus('mandatory')
ctFDDIPeakTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 2, 1, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFDDIPeakTime.setStatus('mandatory')
ctFDDIStatsSMT = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 2, 1, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFDDIStatsSMT.setStatus('mandatory')
ctFDDIStatsPath = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 2, 1, 2, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFDDIStatsPath.setStatus('mandatory')
mibBuilder.exportSymbols("CTRON-FDDI-STAT-MIB", ctFDDIPeakBytes=ctFDDIPeakBytes, ctFDDIStatsHistoryEntry=ctFDDIStatsHistoryEntry, ctFDDIStatsTimeStamp=ctFDDIStatsTimeStamp, ctFDDIStatsCtlTable=ctFDDIStatsCtlTable, ctFDDIStatsSMT=ctFDDIStatsSMT, ctFDDIStatsIndex=ctFDDIStatsIndex, ctFDDISMT=ctFDDISMT, ctFDDIFrames=ctFDDIFrames, ctFDDIBytes=ctFDDIBytes, ctFDDIResetPeak=ctFDDIResetPeak, ctFDDIStatsPath=ctFDDIStatsPath, ctFDDIPeakTime=ctFDDIPeakTime, ctFDDIStatsUtil=ctFDDIStatsUtil, ctFDDIStatsCtlEntry=ctFDDIStatsCtlEntry, ctFDDINextEntry=ctFDDINextEntry, ctFDDIStatsHistoryTable=ctFDDIStatsHistoryTable, ctFDDISlot=ctFDDISlot, ctFDDIPath=ctFDDIPath)
