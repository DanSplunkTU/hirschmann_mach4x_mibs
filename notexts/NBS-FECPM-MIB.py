#
# PySNMP MIB module NBS-FECPM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/mrv/NBS-FECPM-MIB
# Produced by pysmi-1.1.8 at Sun Jan 16 00:41:03 2022
# On host fv-az42-839 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
ifAlias, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "ifAlias", "InterfaceIndex")
nbs, WritableU64 = mibBuilder.importSymbols("NBS-MIB", "nbs", "WritableU64")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, ModuleIdentity, Unsigned32, Counter64, TimeTicks, IpAddress, Bits, Gauge32, Counter32, iso, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "ModuleIdentity", "Unsigned32", "Counter64", "TimeTicks", "IpAddress", "Bits", "Gauge32", "Counter32", "iso", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
nbsFecpmMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 629, 223))
if mibBuilder.loadTexts: nbsFecpmMib.setLastUpdated('201610190000Z')
if mibBuilder.loadTexts: nbsFecpmMib.setOrganization('NBS')
nbsFecpmThresholdsGrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 223, 1))
if mibBuilder.loadTexts: nbsFecpmThresholdsGrp.setStatus('current')
nbsFecpmCurrentGrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 223, 2))
if mibBuilder.loadTexts: nbsFecpmCurrentGrp.setStatus('current')
nbsFecpmHistoricGrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 223, 3))
if mibBuilder.loadTexts: nbsFecpmHistoricGrp.setStatus('current')
nbsFecpmRunningGrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 223, 4))
if mibBuilder.loadTexts: nbsFecpmRunningGrp.setStatus('current')
nbsFecStatsGrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 223, 90))
if mibBuilder.loadTexts: nbsFecStatsGrp.setStatus('current')
nbsFecpmEventsGrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 223, 100))
if mibBuilder.loadTexts: nbsFecpmEventsGrp.setStatus('current')
nbsFecpmTraps = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 223, 100, 0))
if mibBuilder.loadTexts: nbsFecpmTraps.setStatus('current')
nbsFecpmThresholdsTable = MibTable((1, 3, 6, 1, 4, 1, 629, 223, 1, 1), )
if mibBuilder.loadTexts: nbsFecpmThresholdsTable.setStatus('current')
nbsFecpmThresholdsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 223, 1, 1, 1), ).setIndexNames((0, "NBS-FECPM-MIB", "nbsFecpmThresholdsIfIndex"), (0, "NBS-FECPM-MIB", "nbsFecpmThresholdsInterval"))
if mibBuilder.loadTexts: nbsFecpmThresholdsEntry.setStatus('current')
nbsFecpmThresholdsIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 223, 1, 1, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsFecpmThresholdsIfIndex.setStatus('current')
nbsFecpmThresholdsInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 223, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("quarterHour", 1), ("twentyfourHour", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsFecpmThresholdsInterval.setStatus('current')
nbsFecpmThresholdsBitErrCor = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 223, 1, 1, 1, 10), WritableU64()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsFecpmThresholdsBitErrCor.setStatus('current')
nbsFecpmThresholdsByteErrCor = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 223, 1, 1, 1, 12), WritableU64()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsFecpmThresholdsByteErrCor.setStatus('current')
nbsFecpmThresholdsCorBit0to1 = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 223, 1, 1, 1, 14), WritableU64()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsFecpmThresholdsCorBit0to1.setStatus('current')
nbsFecpmThresholdsCorBit1to0 = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 223, 1, 1, 1, 16), WritableU64()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsFecpmThresholdsCorBit1to0.setStatus('current')
nbsFecpmThresholdsUncorWords = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 223, 1, 1, 1, 18), WritableU64()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsFecpmThresholdsUncorWords.setStatus('current')
nbsFecpmCurrentSysDate = MibScalar((1, 3, 6, 1, 4, 1, 629, 223, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsFecpmCurrentSysDate.setStatus('current')
nbsFecpmCurrentSysTime = MibScalar((1, 3, 6, 1, 4, 1, 629, 223, 2, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsFecpmCurrentSysTime.setStatus('current')
nbsFecpmCurrentTable = MibTable((1, 3, 6, 1, 4, 1, 629, 223, 2, 3), )
if mibBuilder.loadTexts: nbsFecpmCurrentTable.setStatus('current')
nbsFecpmCurrentEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 223, 2, 3, 1), ).setIndexNames((0, "NBS-FECPM-MIB", "nbsFecpmCurrentIfIndex"), (0, "NBS-FECPM-MIB", "nbsFecpmCurrentInterval"))
if mibBuilder.loadTexts: nbsFecpmCurrentEntry.setStatus('current')
nbsFecpmCurrentIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 223, 2, 3, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsFecpmCurrentIfIndex.setStatus('current')
nbsFecpmCurrentInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 223, 2, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("quarterHour", 1), ("twentyfourHour", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsFecpmCurrentInterval.setStatus('current')
nbsFecpmCurrentDate = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 223, 2, 3, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsFecpmCurrentDate.setStatus('current')
nbsFecpmCurrentTime = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 223, 2, 3, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsFecpmCurrentTime.setStatus('current')
nbsFecpmCurrentBitErrCor = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 223, 2, 3, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsFecpmCurrentBitErrCor.setStatus('current')
nbsFecpmCurrentByteErrCor = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 223, 2, 3, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsFecpmCurrentByteErrCor.setStatus('current')
nbsFecpmCurrentCorBit0to1 = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 223, 2, 3, 1, 14), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsFecpmCurrentCorBit0to1.setStatus('current')
nbsFecpmCurrentCorBit1to0 = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 223, 2, 3, 1, 16), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsFecpmCurrentCorBit1to0.setStatus('current')
nbsFecpmCurrentUncorWords = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 223, 2, 3, 1, 18), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsFecpmCurrentUncorWords.setStatus('current')
nbsFecpmHistoricTable = MibTable((1, 3, 6, 1, 4, 1, 629, 223, 3, 3), )
if mibBuilder.loadTexts: nbsFecpmHistoricTable.setStatus('current')
nbsFecpmHistoricEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 223, 3, 3, 1), ).setIndexNames((0, "NBS-FECPM-MIB", "nbsFecpmHistoricIfIndex"), (0, "NBS-FECPM-MIB", "nbsFecpmHistoricInterval"), (0, "NBS-FECPM-MIB", "nbsFecpmHistoricSample"))
if mibBuilder.loadTexts: nbsFecpmHistoricEntry.setStatus('current')
nbsFecpmHistoricIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 223, 3, 3, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsFecpmHistoricIfIndex.setStatus('current')
nbsFecpmHistoricInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 223, 3, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("quarterHour", 1), ("twentyfourHour", 2))))
if mibBuilder.loadTexts: nbsFecpmHistoricInterval.setStatus('current')
nbsFecpmHistoricSample = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 223, 3, 3, 1, 4), Integer32())
if mibBuilder.loadTexts: nbsFecpmHistoricSample.setStatus('current')
nbsFecpmHistoricDate = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 223, 3, 3, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsFecpmHistoricDate.setStatus('current')
nbsFecpmHistoricTime = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 223, 3, 3, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsFecpmHistoricTime.setStatus('current')
nbsFecpmHistoricBitErrCor = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 223, 3, 3, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsFecpmHistoricBitErrCor.setStatus('current')
nbsFecpmHistoricByteErrCor = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 223, 3, 3, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsFecpmHistoricByteErrCor.setStatus('current')
nbsFecpmHistoricCorBit0to1 = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 223, 3, 3, 1, 14), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsFecpmHistoricCorBit0to1.setStatus('current')
nbsFecpmHistoricCorBit1to0 = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 223, 3, 3, 1, 16), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsFecpmHistoricCorBit1to0.setStatus('current')
nbsFecpmHistoricUncorWords = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 223, 3, 3, 1, 18), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsFecpmHistoricUncorWords.setStatus('current')
nbsFecpmRunningTable = MibTable((1, 3, 6, 1, 4, 1, 629, 223, 4, 3), )
if mibBuilder.loadTexts: nbsFecpmRunningTable.setStatus('current')
nbsFecpmRunningEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 223, 4, 3, 1), ).setIndexNames((0, "NBS-FECPM-MIB", "nbsFecpmRunningIfIndex"))
if mibBuilder.loadTexts: nbsFecpmRunningEntry.setStatus('current')
nbsFecpmRunningIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 223, 4, 3, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsFecpmRunningIfIndex.setStatus('current')
nbsFecpmRunningDate = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 223, 4, 3, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsFecpmRunningDate.setStatus('current')
nbsFecpmRunningTime = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 223, 4, 3, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsFecpmRunningTime.setStatus('current')
nbsFecpmRunningBitErrCor = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 223, 4, 3, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsFecpmRunningBitErrCor.setStatus('current')
nbsFecpmRunningByteErrCor = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 223, 4, 3, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsFecpmRunningByteErrCor.setStatus('current')
nbsFecpmRunningCorBit0to1 = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 223, 4, 3, 1, 14), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsFecpmRunningCorBit0to1.setStatus('current')
nbsFecpmRunningCorBit1to0 = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 223, 4, 3, 1, 16), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsFecpmRunningCorBit1to0.setStatus('current')
nbsFecpmRunningUncorWords = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 223, 4, 3, 1, 18), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsFecpmRunningUncorWords.setStatus('current')
nbsFecStatsTable = MibTable((1, 3, 6, 1, 4, 1, 629, 223, 90, 3), )
if mibBuilder.loadTexts: nbsFecStatsTable.setStatus('current')
nbsFecStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 223, 90, 3, 1), ).setIndexNames((0, "NBS-FECPM-MIB", "nbsFecStatsIfIndex"))
if mibBuilder.loadTexts: nbsFecStatsEntry.setStatus('current')
nbsFecStatsIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 223, 90, 3, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsFecStatsIfIndex.setStatus('current')
nbsFecStatsDate = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 223, 90, 3, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsFecStatsDate.setStatus('current')
nbsFecStatsTime = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 223, 90, 3, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsFecStatsTime.setStatus('current')
nbsFecStatsSpan = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 223, 90, 3, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsFecStatsSpan.setStatus('current')
nbsFecStatsState = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 223, 90, 3, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("notSupported", 1), ("counting", 2), ("clearing", 3), ("stopped", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsFecStatsState.setStatus('current')
nbsFecStatsBitErrCor = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 223, 90, 3, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsFecStatsBitErrCor.setStatus('current')
nbsFecStatsByteErrCor = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 223, 90, 3, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsFecStatsByteErrCor.setStatus('current')
nbsFecStatsCorBit0to1 = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 223, 90, 3, 1, 14), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsFecStatsCorBit0to1.setStatus('current')
nbsFecStatsCorBit1to0 = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 223, 90, 3, 1, 16), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsFecStatsCorBit1to0.setStatus('current')
nbsFecStatsUncorWords = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 223, 90, 3, 1, 18), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsFecStatsUncorWords.setStatus('current')
nbsFecpmTrapsBitErrCor = NotificationType((1, 3, 6, 1, 4, 1, 629, 223, 100, 0, 10)).setObjects(("NBS-FECPM-MIB", "nbsFecpmCurrentIfIndex"), ("IF-MIB", "ifAlias"), ("NBS-FECPM-MIB", "nbsFecpmCurrentInterval"), ("NBS-FECPM-MIB", "nbsFecpmCurrentBitErrCor"))
if mibBuilder.loadTexts: nbsFecpmTrapsBitErrCor.setStatus('current')
nbsFecpmTrapsByteErrCor = NotificationType((1, 3, 6, 1, 4, 1, 629, 223, 100, 0, 12)).setObjects(("NBS-FECPM-MIB", "nbsFecpmCurrentIfIndex"), ("IF-MIB", "ifAlias"), ("NBS-FECPM-MIB", "nbsFecpmCurrentInterval"), ("NBS-FECPM-MIB", "nbsFecpmCurrentByteErrCor"))
if mibBuilder.loadTexts: nbsFecpmTrapsByteErrCor.setStatus('current')
nbsFecpmTrapsCorBit0to1 = NotificationType((1, 3, 6, 1, 4, 1, 629, 223, 100, 0, 14)).setObjects(("NBS-FECPM-MIB", "nbsFecpmCurrentIfIndex"), ("IF-MIB", "ifAlias"), ("NBS-FECPM-MIB", "nbsFecpmCurrentInterval"), ("NBS-FECPM-MIB", "nbsFecpmCurrentCorBit0to1"))
if mibBuilder.loadTexts: nbsFecpmTrapsCorBit0to1.setStatus('current')
nbsFecpmTrapsCorBit1to0 = NotificationType((1, 3, 6, 1, 4, 1, 629, 223, 100, 0, 16)).setObjects(("NBS-FECPM-MIB", "nbsFecpmCurrentIfIndex"), ("IF-MIB", "ifAlias"), ("NBS-FECPM-MIB", "nbsFecpmCurrentInterval"), ("NBS-FECPM-MIB", "nbsFecpmCurrentCorBit1to0"))
if mibBuilder.loadTexts: nbsFecpmTrapsCorBit1to0.setStatus('current')
nbsFecpmTrapsUncorWords = NotificationType((1, 3, 6, 1, 4, 1, 629, 223, 100, 0, 18)).setObjects(("NBS-FECPM-MIB", "nbsFecpmCurrentIfIndex"), ("IF-MIB", "ifAlias"), ("NBS-FECPM-MIB", "nbsFecpmCurrentInterval"), ("NBS-FECPM-MIB", "nbsFecpmCurrentUncorWords"))
if mibBuilder.loadTexts: nbsFecpmTrapsUncorWords.setStatus('current')
mibBuilder.exportSymbols("NBS-FECPM-MIB", nbsFecpmRunningEntry=nbsFecpmRunningEntry, nbsFecpmRunningUncorWords=nbsFecpmRunningUncorWords, nbsFecpmMib=nbsFecpmMib, nbsFecpmRunningTable=nbsFecpmRunningTable, nbsFecpmThresholdsUncorWords=nbsFecpmThresholdsUncorWords, nbsFecpmHistoricByteErrCor=nbsFecpmHistoricByteErrCor, nbsFecpmHistoricEntry=nbsFecpmHistoricEntry, nbsFecpmCurrentEntry=nbsFecpmCurrentEntry, nbsFecpmTrapsCorBit1to0=nbsFecpmTrapsCorBit1to0, nbsFecpmRunningBitErrCor=nbsFecpmRunningBitErrCor, nbsFecpmCurrentCorBit1to0=nbsFecpmCurrentCorBit1to0, nbsFecStatsByteErrCor=nbsFecStatsByteErrCor, nbsFecStatsGrp=nbsFecStatsGrp, nbsFecpmCurrentSysDate=nbsFecpmCurrentSysDate, nbsFecpmCurrentInterval=nbsFecpmCurrentInterval, nbsFecpmRunningDate=nbsFecpmRunningDate, nbsFecStatsTable=nbsFecStatsTable, nbsFecpmCurrentDate=nbsFecpmCurrentDate, nbsFecpmHistoricCorBit0to1=nbsFecpmHistoricCorBit0to1, nbsFecpmRunningByteErrCor=nbsFecpmRunningByteErrCor, nbsFecpmCurrentByteErrCor=nbsFecpmCurrentByteErrCor, nbsFecpmHistoricGrp=nbsFecpmHistoricGrp, nbsFecpmCurrentSysTime=nbsFecpmCurrentSysTime, nbsFecpmTrapsCorBit0to1=nbsFecpmTrapsCorBit0to1, nbsFecpmRunningGrp=nbsFecpmRunningGrp, PYSNMP_MODULE_ID=nbsFecpmMib, nbsFecpmThresholdsTable=nbsFecpmThresholdsTable, nbsFecStatsCorBit1to0=nbsFecStatsCorBit1to0, nbsFecpmTrapsUncorWords=nbsFecpmTrapsUncorWords, nbsFecpmThresholdsGrp=nbsFecpmThresholdsGrp, nbsFecStatsIfIndex=nbsFecStatsIfIndex, nbsFecpmRunningTime=nbsFecpmRunningTime, nbsFecpmEventsGrp=nbsFecpmEventsGrp, nbsFecpmThresholdsEntry=nbsFecpmThresholdsEntry, nbsFecpmHistoricTable=nbsFecpmHistoricTable, nbsFecStatsCorBit0to1=nbsFecStatsCorBit0to1, nbsFecpmCurrentBitErrCor=nbsFecpmCurrentBitErrCor, nbsFecpmTrapsBitErrCor=nbsFecpmTrapsBitErrCor, nbsFecpmTrapsByteErrCor=nbsFecpmTrapsByteErrCor, nbsFecpmThresholdsCorBit1to0=nbsFecpmThresholdsCorBit1to0, nbsFecpmThresholdsByteErrCor=nbsFecpmThresholdsByteErrCor, nbsFecpmCurrentGrp=nbsFecpmCurrentGrp, nbsFecpmRunningIfIndex=nbsFecpmRunningIfIndex, nbsFecStatsEntry=nbsFecStatsEntry, nbsFecStatsDate=nbsFecStatsDate, nbsFecStatsUncorWords=nbsFecStatsUncorWords, nbsFecpmCurrentTable=nbsFecpmCurrentTable, nbsFecStatsTime=nbsFecStatsTime, nbsFecStatsBitErrCor=nbsFecStatsBitErrCor, nbsFecpmThresholdsBitErrCor=nbsFecpmThresholdsBitErrCor, nbsFecpmHistoricTime=nbsFecpmHistoricTime, nbsFecpmTraps=nbsFecpmTraps, nbsFecpmThresholdsIfIndex=nbsFecpmThresholdsIfIndex, nbsFecpmHistoricDate=nbsFecpmHistoricDate, nbsFecpmHistoricBitErrCor=nbsFecpmHistoricBitErrCor, nbsFecpmThresholdsCorBit0to1=nbsFecpmThresholdsCorBit0to1, nbsFecpmCurrentUncorWords=nbsFecpmCurrentUncorWords, nbsFecpmHistoricIfIndex=nbsFecpmHistoricIfIndex, nbsFecpmCurrentCorBit0to1=nbsFecpmCurrentCorBit0to1, nbsFecpmHistoricSample=nbsFecpmHistoricSample, nbsFecpmHistoricCorBit1to0=nbsFecpmHistoricCorBit1to0, nbsFecpmRunningCorBit1to0=nbsFecpmRunningCorBit1to0, nbsFecpmHistoricInterval=nbsFecpmHistoricInterval, nbsFecpmRunningCorBit0to1=nbsFecpmRunningCorBit0to1, nbsFecStatsSpan=nbsFecStatsSpan, nbsFecpmHistoricUncorWords=nbsFecpmHistoricUncorWords, nbsFecpmCurrentIfIndex=nbsFecpmCurrentIfIndex, nbsFecStatsState=nbsFecStatsState, nbsFecpmCurrentTime=nbsFecpmCurrentTime, nbsFecpmThresholdsInterval=nbsFecpmThresholdsInterval)
