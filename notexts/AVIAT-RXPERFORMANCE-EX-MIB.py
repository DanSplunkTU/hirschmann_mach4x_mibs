#
# PySNMP MIB module AVIAT-RXPERFORMANCE-EX-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/aviat-wtm/AVIAT-RXPERFORMANCE-EX-MIB
# Produced by pysmi-1.1.3 at Sun Nov 28 20:33:43 2021
# On host fv-az77-612 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
aviatRxPerformQHourPeriod, aviatRxPerformDayIndex, aviatRxPerformQHourIndex, aviatRxPerformDayPeriod = mibBuilder.importSymbols("AVIAT-RXPERFORMANCE-MIB", "aviatRxPerformQHourPeriod", "aviatRxPerformDayIndex", "aviatRxPerformQHourIndex", "aviatRxPerformDayPeriod")
AviatPowerLevel, = mibBuilder.importSymbols("AVIAT-TEXTCONVENTION-MIB", "AviatPowerLevel")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
TimeTicks, iso, Integer32, ModuleIdentity, ObjectIdentity, Bits, NotificationType, Counter64, Unsigned32, Counter32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "iso", "Integer32", "ModuleIdentity", "ObjectIdentity", "Bits", "NotificationType", "Counter64", "Unsigned32", "Counter32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
aviatModules, = mibBuilder.importSymbols("STXN-GLOBALREGISTER-MIB", "aviatModules")
aviatRxPerformanceExModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 2509, 9, 33))
aviatRxPerformanceExModule.setRevisions(('2014-01-21 01:57',))
if mibBuilder.loadTexts: aviatRxPerformanceExModule.setLastUpdated('201401210157Z')
if mibBuilder.loadTexts: aviatRxPerformanceExModule.setOrganization('Aviat Networks')
aviatRxPerformanceExConf = MibIdentifier((1, 3, 6, 1, 4, 1, 2509, 9, 33, 1))
aviatRxPerformanceExGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2509, 9, 33, 1, 1))
aviatRxPerformanceExCompl = MibIdentifier((1, 3, 6, 1, 4, 1, 2509, 9, 33, 1, 2))
aviatRxPerformanceExMIBObjs = MibIdentifier((1, 3, 6, 1, 4, 1, 2509, 9, 33, 2))
aviatRxPerformExTable = MibTable((1, 3, 6, 1, 4, 1, 2509, 9, 33, 2, 2), )
if mibBuilder.loadTexts: aviatRxPerformExTable.setStatus('current')
aviatRxPerformExEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2509, 9, 33, 2, 2, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: aviatRxPerformExEntry.setStatus('current')
aviatRxPerformCinrReadingMean = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 33, 2, 2, 1, 2), AviatPowerLevel()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatRxPerformCinrReadingMean.setStatus('current')
aviatRxPerformCinrReadingCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 33, 2, 2, 1, 3), AviatPowerLevel()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatRxPerformCinrReadingCurrent.setStatus('current')
aviatRxPerformCinrReadingMax = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 33, 2, 2, 1, 4), AviatPowerLevel()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatRxPerformCinrReadingMax.setStatus('current')
aviatRxPerformCinrReadingMin = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 33, 2, 2, 1, 5), AviatPowerLevel()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatRxPerformCinrReadingMin.setStatus('current')
aviatRxPerformTxpowReadingMean = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 33, 2, 2, 1, 6), AviatPowerLevel()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatRxPerformTxpowReadingMean.setStatus('current')
aviatRxPerformTxpowReadingCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 33, 2, 2, 1, 7), AviatPowerLevel()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatRxPerformTxpowReadingCurrent.setStatus('current')
aviatRxPerformTxpowReadingMax = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 33, 2, 2, 1, 8), AviatPowerLevel()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatRxPerformTxpowReadingMax.setStatus('current')
aviatRxPerformTxpowReadingMin = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 33, 2, 2, 1, 9), AviatPowerLevel()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatRxPerformTxpowReadingMin.setStatus('current')
aviatRxPerformQuarterHourExTable = MibTable((1, 3, 6, 1, 4, 1, 2509, 9, 33, 2, 3), )
if mibBuilder.loadTexts: aviatRxPerformQuarterHourExTable.setStatus('current')
aviatRxPerformQuarterHourExEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2509, 9, 33, 2, 3, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "AVIAT-RXPERFORMANCE-MIB", "aviatRxPerformQHourIndex"), (0, "AVIAT-RXPERFORMANCE-MIB", "aviatRxPerformQHourPeriod"))
if mibBuilder.loadTexts: aviatRxPerformQuarterHourExEntry.setStatus('current')
aviatRxPerformQHourCinrReadingMean = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 33, 2, 3, 1, 4), AviatPowerLevel()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatRxPerformQHourCinrReadingMean.setStatus('current')
aviatRxPerformQHourCinrReadingMax = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 33, 2, 3, 1, 5), AviatPowerLevel()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatRxPerformQHourCinrReadingMax.setStatus('current')
aviatRxPerformQHourCinrReadingMin = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 33, 2, 3, 1, 6), AviatPowerLevel()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatRxPerformQHourCinrReadingMin.setStatus('current')
aviatRxPerformQHourTxpowReadingMean = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 33, 2, 3, 1, 7), AviatPowerLevel()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatRxPerformQHourTxpowReadingMean.setStatus('current')
aviatRxPerformQHourTxpowReadingMax = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 33, 2, 3, 1, 8), AviatPowerLevel()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatRxPerformQHourTxpowReadingMax.setStatus('current')
aviatRxPerformQHourTxpowReadingMin = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 33, 2, 3, 1, 9), AviatPowerLevel()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatRxPerformQHourTxpowReadingMin.setStatus('current')
aviatRxPerformDayExTable = MibTable((1, 3, 6, 1, 4, 1, 2509, 9, 33, 2, 4), )
if mibBuilder.loadTexts: aviatRxPerformDayExTable.setStatus('current')
aviatRxPerformDayExEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2509, 9, 33, 2, 4, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "AVIAT-RXPERFORMANCE-MIB", "aviatRxPerformDayIndex"), (0, "AVIAT-RXPERFORMANCE-MIB", "aviatRxPerformDayPeriod"))
if mibBuilder.loadTexts: aviatRxPerformDayExEntry.setStatus('current')
aviatRxPerformDayCinrReadingMean = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 33, 2, 4, 1, 4), AviatPowerLevel()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatRxPerformDayCinrReadingMean.setStatus('current')
aviatRxPerformDayCinrReadingMax = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 33, 2, 4, 1, 5), AviatPowerLevel()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatRxPerformDayCinrReadingMax.setStatus('current')
aviatRxPerformDayCinrReadingMin = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 33, 2, 4, 1, 6), AviatPowerLevel()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatRxPerformDayCinrReadingMin.setStatus('current')
aviatRxPerformDayTxpowReadingMean = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 33, 2, 4, 1, 7), AviatPowerLevel()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatRxPerformDayTxpowReadingMean.setStatus('current')
aviatRxPerformDayTxpowReadingMax = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 33, 2, 4, 1, 8), AviatPowerLevel()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatRxPerformDayTxpowReadingMax.setStatus('current')
aviatRxPerformDayTxpowReadingMin = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 33, 2, 4, 1, 9), AviatPowerLevel()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatRxPerformDayTxpowReadingMin.setStatus('current')
aviatRxPerformExObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2509, 9, 33, 1, 1, 1)).setObjects(("AVIAT-RXPERFORMANCE-EX-MIB", "aviatRxPerformCinrReadingMean"), ("AVIAT-RXPERFORMANCE-EX-MIB", "aviatRxPerformCinrReadingCurrent"), ("AVIAT-RXPERFORMANCE-EX-MIB", "aviatRxPerformCinrReadingMax"), ("AVIAT-RXPERFORMANCE-EX-MIB", "aviatRxPerformCinrReadingMin"), ("AVIAT-RXPERFORMANCE-EX-MIB", "aviatRxPerformTxpowReadingMean"), ("AVIAT-RXPERFORMANCE-EX-MIB", "aviatRxPerformTxpowReadingCurrent"), ("AVIAT-RXPERFORMANCE-EX-MIB", "aviatRxPerformTxpowReadingMax"), ("AVIAT-RXPERFORMANCE-EX-MIB", "aviatRxPerformTxpowReadingMin"), ("AVIAT-RXPERFORMANCE-EX-MIB", "aviatRxPerformQHourCinrReadingMean"), ("AVIAT-RXPERFORMANCE-EX-MIB", "aviatRxPerformQHourCinrReadingMax"), ("AVIAT-RXPERFORMANCE-EX-MIB", "aviatRxPerformQHourCinrReadingMin"), ("AVIAT-RXPERFORMANCE-EX-MIB", "aviatRxPerformQHourTxpowReadingMean"), ("AVIAT-RXPERFORMANCE-EX-MIB", "aviatRxPerformQHourTxpowReadingMax"), ("AVIAT-RXPERFORMANCE-EX-MIB", "aviatRxPerformQHourTxpowReadingMin"), ("AVIAT-RXPERFORMANCE-EX-MIB", "aviatRxPerformDayCinrReadingMean"), ("AVIAT-RXPERFORMANCE-EX-MIB", "aviatRxPerformDayCinrReadingMax"), ("AVIAT-RXPERFORMANCE-EX-MIB", "aviatRxPerformDayCinrReadingMin"), ("AVIAT-RXPERFORMANCE-EX-MIB", "aviatRxPerformDayTxpowReadingMean"), ("AVIAT-RXPERFORMANCE-EX-MIB", "aviatRxPerformDayTxpowReadingMax"), ("AVIAT-RXPERFORMANCE-EX-MIB", "aviatRxPerformDayTxpowReadingMin"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aviatRxPerformExObjectGroup = aviatRxPerformExObjectGroup.setStatus('current')
aviatRxPerformanceExComplV1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 2509, 9, 33, 1, 2, 1)).setObjects(("AVIAT-RXPERFORMANCE-EX-MIB", "aviatRxPerformExObjectGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aviatRxPerformanceExComplV1 = aviatRxPerformanceExComplV1.setStatus('current')
mibBuilder.exportSymbols("AVIAT-RXPERFORMANCE-EX-MIB", aviatRxPerformanceExModule=aviatRxPerformanceExModule, aviatRxPerformQHourCinrReadingMax=aviatRxPerformQHourCinrReadingMax, aviatRxPerformDayExTable=aviatRxPerformDayExTable, aviatRxPerformExEntry=aviatRxPerformExEntry, aviatRxPerformDayCinrReadingMax=aviatRxPerformDayCinrReadingMax, aviatRxPerformanceExMIBObjs=aviatRxPerformanceExMIBObjs, aviatRxPerformDayTxpowReadingMin=aviatRxPerformDayTxpowReadingMin, aviatRxPerformQHourCinrReadingMean=aviatRxPerformQHourCinrReadingMean, aviatRxPerformExObjectGroup=aviatRxPerformExObjectGroup, aviatRxPerformCinrReadingMax=aviatRxPerformCinrReadingMax, aviatRxPerformQHourCinrReadingMin=aviatRxPerformQHourCinrReadingMin, aviatRxPerformQHourTxpowReadingMax=aviatRxPerformQHourTxpowReadingMax, aviatRxPerformExTable=aviatRxPerformExTable, aviatRxPerformDayTxpowReadingMean=aviatRxPerformDayTxpowReadingMean, aviatRxPerformanceExCompl=aviatRxPerformanceExCompl, aviatRxPerformTxpowReadingMin=aviatRxPerformTxpowReadingMin, aviatRxPerformDayCinrReadingMean=aviatRxPerformDayCinrReadingMean, aviatRxPerformQuarterHourExTable=aviatRxPerformQuarterHourExTable, aviatRxPerformQHourTxpowReadingMin=aviatRxPerformQHourTxpowReadingMin, aviatRxPerformTxpowReadingCurrent=aviatRxPerformTxpowReadingCurrent, aviatRxPerformCinrReadingMin=aviatRxPerformCinrReadingMin, PYSNMP_MODULE_ID=aviatRxPerformanceExModule, aviatRxPerformDayCinrReadingMin=aviatRxPerformDayCinrReadingMin, aviatRxPerformCinrReadingCurrent=aviatRxPerformCinrReadingCurrent, aviatRxPerformanceExGroups=aviatRxPerformanceExGroups, aviatRxPerformDayTxpowReadingMax=aviatRxPerformDayTxpowReadingMax, aviatRxPerformCinrReadingMean=aviatRxPerformCinrReadingMean, aviatRxPerformTxpowReadingMax=aviatRxPerformTxpowReadingMax, aviatRxPerformQuarterHourExEntry=aviatRxPerformQuarterHourExEntry, aviatRxPerformQHourTxpowReadingMean=aviatRxPerformQHourTxpowReadingMean, aviatRxPerformanceExComplV1=aviatRxPerformanceExComplV1, aviatRxPerformanceExConf=aviatRxPerformanceExConf, aviatRxPerformDayExEntry=aviatRxPerformDayExEntry, aviatRxPerformTxpowReadingMean=aviatRxPerformTxpowReadingMean)
