#
# PySNMP MIB module ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/adtran/ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 17:50:19 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
adGenAOSMef, adGenAOSConformance = mibBuilder.importSymbols("ADTRAN-AOS", "adGenAOSMef", "adGenAOSConformance")
adIdentity, = mibBuilder.importSymbols("ADTRAN-MIB", "adIdentity")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
HCPerfTimeElapsed, HCPerfTotalCount, HCPerfInvalidIntervals, HCPerfValidIntervals, HCPerfIntervalCount, HCPerfCurrentCount = mibBuilder.importSymbols("HC-PerfHist-TC-MIB", "HCPerfTimeElapsed", "HCPerfTotalCount", "HCPerfInvalidIntervals", "HCPerfValidIntervals", "HCPerfIntervalCount", "HCPerfCurrentCount")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, MibIdentifier, Counter64, IpAddress, Counter32, ModuleIdentity, TimeTicks, Bits, ObjectIdentity, NotificationType, iso, Integer32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "MibIdentifier", "Counter64", "IpAddress", "Counter32", "ModuleIdentity", "TimeTicks", "Bits", "ObjectIdentity", "NotificationType", "iso", "Integer32", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
adGenAosMefPerCosPerUniPerfHistoryMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 664, 6, 10000, 53, 9, 2))
adGenAosMefPerCosPerUniPerfHistoryMib.setRevisions(('2014-09-10 00:00',))
if mibBuilder.loadTexts: adGenAosMefPerCosPerUniPerfHistoryMib.setLastUpdated('201409100000Z')
if mibBuilder.loadTexts: adGenAosMefPerCosPerUniPerfHistoryMib.setOrganization('ADTRAN Inc.')
adGenAosMefPerCosPerUniPerfHistory = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2))
adMefPerCosPerUniPhCurTable = MibTable((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 1), )
if mibBuilder.loadTexts: adMefPerCosPerUniPhCurTable.setStatus('current')
adMefPerCosPerUniPhCurEntry = MibTableRow((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPhCurQueueNumber"))
if mibBuilder.loadTexts: adMefPerCosPerUniPhCurEntry.setStatus('current')
adMefPerCosPerUniPhCurQueueNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 7)))
if mibBuilder.loadTexts: adMefPerCosPerUniPhCurQueueNumber.setStatus('current')
adMefPerCosPerUniPhCurTimeElapsed15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 1, 1, 2), HCPerfTimeElapsed()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerUniPhCurTimeElapsed15Min.setStatus('current')
adMefPerCosPerUniPhCurValidIntervals15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 1, 1, 3), HCPerfValidIntervals()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerUniPhCurValidIntervals15Min.setStatus('current')
adMefPerCosPerUniPhCurInvalidIntervals15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 1, 1, 4), HCPerfInvalidIntervals()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerUniPhCurInvalidIntervals15Min.setStatus('current')
adMefPerCosPerUniPhCurIngressGreenOctets15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 1, 1, 5), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerUniPhCurIngressGreenOctets15Min.setStatus('current')
adMefPerCosPerUniPhCurIngressGreenFrames15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 1, 1, 6), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerUniPhCurIngressGreenFrames15Min.setStatus('current')
adMefPerCosPerUniPhCurEgressGreenOctets15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 1, 1, 7), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerUniPhCurEgressGreenOctets15Min.setStatus('current')
adMefPerCosPerUniPhCurEgressGreenFrames15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 1, 1, 8), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerUniPhCurEgressGreenFrames15Min.setStatus('current')
adMefPerCosPerUniPhCurIngressGreenFrameDiscards15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 1, 1, 9), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerUniPhCurIngressGreenFrameDiscards15Min.setStatus('current')
adMefPerCosPerUniPhCurEgressGreenFrameDiscards15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 1, 1, 10), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerUniPhCurEgressGreenFrameDiscards15Min.setStatus('current')
adMefPerCosPerUniPhCurIngressGreenOctetDiscards15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 1, 1, 11), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerUniPhCurIngressGreenOctetDiscards15Min.setStatus('current')
adMefPerCosPerUniPhCurEgressGreenOctetDiscards15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 1, 1, 12), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerUniPhCurEgressGreenOctetDiscards15Min.setStatus('current')
adMefPerCosPerUniPhCurTimeElapsed1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 1, 1, 13), HCPerfTimeElapsed()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerUniPhCurTimeElapsed1Day.setStatus('current')
adMefPerCosPerUniPhCurValidIntervals1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 1, 1, 14), HCPerfValidIntervals()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerUniPhCurValidIntervals1Day.setStatus('current')
adMefPerCosPerUniPhCurInvalidIntervals1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 1, 1, 15), HCPerfInvalidIntervals()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerUniPhCurInvalidIntervals1Day.setStatus('current')
adMefPerCosPerUniPhCurIngressGreenOctets1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 1, 1, 16), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerUniPhCurIngressGreenOctets1Day.setStatus('current')
adMefPerCosPerUniPhCurIngressGreenFrames1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 1, 1, 17), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerUniPhCurIngressGreenFrames1Day.setStatus('current')
adMefPerCosPerUniPhCurEgressGreenOctets1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 1, 1, 18), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerUniPhCurEgressGreenOctets1Day.setStatus('current')
adMefPerCosPerUniPhCurEgressGreenFrames1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 1, 1, 19), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerUniPhCurEgressGreenFrames1Day.setStatus('current')
adMefPerCosPerUniPhCurIngressGreenFrameDiscards1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 1, 1, 20), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerUniPhCurIngressGreenFrameDiscards1Day.setStatus('current')
adMefPerCosPerUniPhCurEgressGreenFrameDiscards1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 1, 1, 21), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerUniPhCurEgressGreenFrameDiscards1Day.setStatus('current')
adMefPerCosPerUniPhCurIngressGreenOctetDiscards1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 1, 1, 22), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerUniPhCurIngressGreenOctetDiscards1Day.setStatus('current')
adMefPerCosPerUniPhCurEgressGreenOctetDiscards1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 1, 1, 23), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerUniPhCurEgressGreenOctetDiscards1Day.setStatus('current')
adMefPerCosPerUniPh15MinIntervalTable = MibTable((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 2), )
if mibBuilder.loadTexts: adMefPerCosPerUniPh15MinIntervalTable.setStatus('current')
adMefPerCosPerUniPh15MinIntervalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPh15MinQueueNumber"), (0, "ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPh15MinIntervalNumber"))
if mibBuilder.loadTexts: adMefPerCosPerUniPh15MinIntervalEntry.setStatus('current')
adMefPerCosPerUniPh15MinQueueNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 7)))
if mibBuilder.loadTexts: adMefPerCosPerUniPh15MinQueueNumber.setStatus('current')
adMefPerCosPerUniPh15MinIntervalNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 96)))
if mibBuilder.loadTexts: adMefPerCosPerUniPh15MinIntervalNumber.setStatus('current')
adMefPerCosPerUniPh15MinIngressGreenOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 2, 1, 3), HCPerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerUniPh15MinIngressGreenOctets.setStatus('current')
adMefPerCosPerUniPh15MinIngressGreenFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 2, 1, 4), HCPerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerUniPh15MinIngressGreenFrames.setStatus('current')
adMefPerCosPerUniPh15MinEgressGreenOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 2, 1, 5), HCPerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerUniPh15MinEgressGreenOctets.setStatus('current')
adMefPerCosPerUniPh15MinEgressGreenFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 2, 1, 6), HCPerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerUniPh15MinEgressGreenFrames.setStatus('current')
adMefPerCosPerUniPh15MinIngressGreenFrameDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 2, 1, 7), HCPerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerUniPh15MinIngressGreenFrameDiscards.setStatus('current')
adMefPerCosPerUniPh15MinEgressGreenFrameDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 2, 1, 8), HCPerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerUniPh15MinEgressGreenFrameDiscards.setStatus('current')
adMefPerCosPerUniPh15MinIngressGreenOctetDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 2, 1, 9), HCPerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerUniPh15MinIngressGreenOctetDiscards.setStatus('current')
adMefPerCosPerUniPh15MinEgressGreenOctetDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 2, 1, 10), HCPerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerUniPh15MinEgressGreenOctetDiscards.setStatus('current')
adMefPerCosPerUniPh1DayIntervalTable = MibTable((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 3), )
if mibBuilder.loadTexts: adMefPerCosPerUniPh1DayIntervalTable.setStatus('current')
adMefPerCosPerUniPh1DayIntervalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPh1DayQueueNumber"), (0, "ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPh1DayIntervalNumber"))
if mibBuilder.loadTexts: adMefPerCosPerUniPh1DayIntervalEntry.setStatus('current')
adMefPerCosPerUniPh1DayQueueNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 3, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 7)))
if mibBuilder.loadTexts: adMefPerCosPerUniPh1DayQueueNumber.setStatus('current')
adMefPerCosPerUniPh1DayIntervalNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 30)))
if mibBuilder.loadTexts: adMefPerCosPerUniPh1DayIntervalNumber.setStatus('current')
adMefPerCosPerUniPh1DayIngressGreenOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 3, 1, 3), HCPerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerUniPh1DayIngressGreenOctets.setStatus('current')
adMefPerCosPerUniPh1DayIngressGreenFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 3, 1, 4), HCPerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerUniPh1DayIngressGreenFrames.setStatus('current')
adMefPerCosPerUniPh1DayEgressGreenOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 3, 1, 5), HCPerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerUniPh1DayEgressGreenOctets.setStatus('current')
adMefPerCosPerUniPh1DayEgressGreenFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 3, 1, 6), HCPerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerUniPh1DayEgressGreenFrames.setStatus('current')
adMefPerCosPerUniPh1DayIngressGreenFrameDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 3, 1, 7), HCPerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerUniPh1DayIngressGreenFrameDiscards.setStatus('current')
adMefPerCosPerUniPh1DayEgressGreenFrameDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 3, 1, 8), HCPerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerUniPh1DayEgressGreenFrameDiscards.setStatus('current')
adMefPerCosPerUniPh1DayIngressGreenOctetDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 3, 1, 9), HCPerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerUniPh1DayIngressGreenOctetDiscards.setStatus('current')
adMefPerCosPerUniPh1DayEgressGreenOctetDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2, 3, 1, 10), HCPerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerUniPh1DayEgressGreenOctetDiscards.setStatus('current')
adGenAosMefPerCosPerUniPerfHistoryConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 21))
adGenAosMefPerCosPerUniPerfHistoryGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 21, 1))
adGenAosMefPerCosPerUniPerfHistoryCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 21, 2))
adGenAosMefPerCosPerUniPerfHistoryCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 21, 2, 1)).setObjects(("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPhCurGroup"), ("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPh15MinIntervalGroup"), ("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPh1DayIntervalGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAosMefPerCosPerUniPerfHistoryCompliance = adGenAosMefPerCosPerUniPerfHistoryCompliance.setStatus('current')
adMefPerCosPerUniPhCurGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 21, 1, 1)).setObjects(("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPhCurTimeElapsed15Min"), ("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPhCurValidIntervals15Min"), ("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPhCurInvalidIntervals15Min"), ("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPhCurIngressGreenOctets15Min"), ("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPhCurIngressGreenFrames15Min"), ("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPhCurEgressGreenOctets15Min"), ("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPhCurEgressGreenFrames15Min"), ("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPhCurIngressGreenFrameDiscards15Min"), ("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPhCurEgressGreenFrameDiscards15Min"), ("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPhCurIngressGreenOctetDiscards15Min"), ("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPhCurEgressGreenOctetDiscards15Min"), ("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPhCurTimeElapsed1Day"), ("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPhCurValidIntervals1Day"), ("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPhCurInvalidIntervals1Day"), ("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPhCurIngressGreenOctets1Day"), ("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPhCurIngressGreenFrames1Day"), ("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPhCurEgressGreenOctets1Day"), ("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPhCurEgressGreenFrames1Day"), ("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPhCurIngressGreenFrameDiscards1Day"), ("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPhCurEgressGreenFrameDiscards1Day"), ("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPhCurIngressGreenOctetDiscards1Day"), ("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPhCurEgressGreenOctetDiscards1Day"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adMefPerCosPerUniPhCurGroup = adMefPerCosPerUniPhCurGroup.setStatus('current')
adMefPerCosPerUniPh15MinIntervalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 21, 1, 2)).setObjects(("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPh15MinIngressGreenOctets"), ("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPh15MinIngressGreenFrames"), ("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPh15MinEgressGreenOctets"), ("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPh15MinEgressGreenFrames"), ("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPh15MinIngressGreenFrameDiscards"), ("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPh15MinEgressGreenFrameDiscards"), ("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPh15MinIngressGreenOctetDiscards"), ("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPh15MinEgressGreenOctetDiscards"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adMefPerCosPerUniPh15MinIntervalGroup = adMefPerCosPerUniPh15MinIntervalGroup.setStatus('current')
adMefPerCosPerUniPh1DayIntervalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 21, 1, 3)).setObjects(("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPh1DayIngressGreenOctets"), ("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPh1DayIngressGreenFrames"), ("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPh1DayEgressGreenOctets"), ("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPh1DayEgressGreenFrames"), ("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPh1DayIngressGreenFrameDiscards"), ("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPh1DayEgressGreenFrameDiscards"), ("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPh1DayIngressGreenOctetDiscards"), ("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", "adMefPerCosPerUniPh1DayEgressGreenOctetDiscards"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adMefPerCosPerUniPh1DayIntervalGroup = adMefPerCosPerUniPh1DayIntervalGroup.setStatus('current')
mibBuilder.exportSymbols("ADTRAN-MEF-PER-COS-PER-UNI-PERF-HISTORY-MIB", adMefPerCosPerUniPhCurInvalidIntervals1Day=adMefPerCosPerUniPhCurInvalidIntervals1Day, adGenAosMefPerCosPerUniPerfHistoryMib=adGenAosMefPerCosPerUniPerfHistoryMib, adMefPerCosPerUniPh15MinIntervalNumber=adMefPerCosPerUniPh15MinIntervalNumber, adGenAosMefPerCosPerUniPerfHistoryCompliance=adGenAosMefPerCosPerUniPerfHistoryCompliance, adMefPerCosPerUniPh15MinIntervalGroup=adMefPerCosPerUniPh15MinIntervalGroup, adMefPerCosPerUniPhCurEgressGreenFrames1Day=adMefPerCosPerUniPhCurEgressGreenFrames1Day, adMefPerCosPerUniPhCurTimeElapsed15Min=adMefPerCosPerUniPhCurTimeElapsed15Min, adMefPerCosPerUniPh1DayIngressGreenFrames=adMefPerCosPerUniPh1DayIngressGreenFrames, adMefPerCosPerUniPhCurIngressGreenOctets1Day=adMefPerCosPerUniPhCurIngressGreenOctets1Day, adGenAosMefPerCosPerUniPerfHistoryCompliances=adGenAosMefPerCosPerUniPerfHistoryCompliances, adMefPerCosPerUniPhCurEntry=adMefPerCosPerUniPhCurEntry, adMefPerCosPerUniPh1DayIntervalNumber=adMefPerCosPerUniPh1DayIntervalNumber, adMefPerCosPerUniPhCurValidIntervals1Day=adMefPerCosPerUniPhCurValidIntervals1Day, adGenAosMefPerCosPerUniPerfHistory=adGenAosMefPerCosPerUniPerfHistory, adGenAosMefPerCosPerUniPerfHistoryGroups=adGenAosMefPerCosPerUniPerfHistoryGroups, adMefPerCosPerUniPh1DayQueueNumber=adMefPerCosPerUniPh1DayQueueNumber, adMefPerCosPerUniPh1DayIntervalEntry=adMefPerCosPerUniPh1DayIntervalEntry, adMefPerCosPerUniPh1DayEgressGreenFrames=adMefPerCosPerUniPh1DayEgressGreenFrames, adMefPerCosPerUniPhCurEgressGreenOctets1Day=adMefPerCosPerUniPhCurEgressGreenOctets1Day, adMefPerCosPerUniPhCurIngressGreenOctets15Min=adMefPerCosPerUniPhCurIngressGreenOctets15Min, adMefPerCosPerUniPhCurEgressGreenOctetDiscards1Day=adMefPerCosPerUniPhCurEgressGreenOctetDiscards1Day, adMefPerCosPerUniPh15MinEgressGreenOctets=adMefPerCosPerUniPh15MinEgressGreenOctets, adMefPerCosPerUniPhCurEgressGreenFrameDiscards15Min=adMefPerCosPerUniPhCurEgressGreenFrameDiscards15Min, adMefPerCosPerUniPh15MinEgressGreenOctetDiscards=adMefPerCosPerUniPh15MinEgressGreenOctetDiscards, adMefPerCosPerUniPhCurIngressGreenFrames15Min=adMefPerCosPerUniPhCurIngressGreenFrames15Min, adMefPerCosPerUniPhCurTimeElapsed1Day=adMefPerCosPerUniPhCurTimeElapsed1Day, adMefPerCosPerUniPhCurIngressGreenFrameDiscards15Min=adMefPerCosPerUniPhCurIngressGreenFrameDiscards15Min, adMefPerCosPerUniPh1DayIntervalTable=adMefPerCosPerUniPh1DayIntervalTable, adMefPerCosPerUniPhCurEgressGreenOctets15Min=adMefPerCosPerUniPhCurEgressGreenOctets15Min, adMefPerCosPerUniPhCurInvalidIntervals15Min=adMefPerCosPerUniPhCurInvalidIntervals15Min, adMefPerCosPerUniPh15MinQueueNumber=adMefPerCosPerUniPh15MinQueueNumber, adMefPerCosPerUniPh1DayIngressGreenFrameDiscards=adMefPerCosPerUniPh1DayIngressGreenFrameDiscards, adMefPerCosPerUniPh15MinEgressGreenFrameDiscards=adMefPerCosPerUniPh15MinEgressGreenFrameDiscards, adMefPerCosPerUniPh1DayIngressGreenOctetDiscards=adMefPerCosPerUniPh1DayIngressGreenOctetDiscards, adMefPerCosPerUniPh15MinIngressGreenOctets=adMefPerCosPerUniPh15MinIngressGreenOctets, adMefPerCosPerUniPhCurEgressGreenFrames15Min=adMefPerCosPerUniPhCurEgressGreenFrames15Min, adMefPerCosPerUniPh15MinIntervalEntry=adMefPerCosPerUniPh15MinIntervalEntry, adMefPerCosPerUniPh15MinIngressGreenOctetDiscards=adMefPerCosPerUniPh15MinIngressGreenOctetDiscards, adMefPerCosPerUniPhCurIngressGreenOctetDiscards1Day=adMefPerCosPerUniPhCurIngressGreenOctetDiscards1Day, adMefPerCosPerUniPh1DayEgressGreenOctets=adMefPerCosPerUniPh1DayEgressGreenOctets, adMefPerCosPerUniPhCurEgressGreenOctetDiscards15Min=adMefPerCosPerUniPhCurEgressGreenOctetDiscards15Min, adMefPerCosPerUniPhCurIngressGreenFrames1Day=adMefPerCosPerUniPhCurIngressGreenFrames1Day, adMefPerCosPerUniPhCurTable=adMefPerCosPerUniPhCurTable, adMefPerCosPerUniPhCurValidIntervals15Min=adMefPerCosPerUniPhCurValidIntervals15Min, adMefPerCosPerUniPhCurEgressGreenFrameDiscards1Day=adMefPerCosPerUniPhCurEgressGreenFrameDiscards1Day, PYSNMP_MODULE_ID=adGenAosMefPerCosPerUniPerfHistoryMib, adMefPerCosPerUniPh1DayIngressGreenOctets=adMefPerCosPerUniPh1DayIngressGreenOctets, adMefPerCosPerUniPh15MinIngressGreenFrameDiscards=adMefPerCosPerUniPh15MinIngressGreenFrameDiscards, adMefPerCosPerUniPhCurIngressGreenOctetDiscards15Min=adMefPerCosPerUniPhCurIngressGreenOctetDiscards15Min, adMefPerCosPerUniPhCurIngressGreenFrameDiscards1Day=adMefPerCosPerUniPhCurIngressGreenFrameDiscards1Day, adMefPerCosPerUniPh15MinIntervalTable=adMefPerCosPerUniPh15MinIntervalTable, adGenAosMefPerCosPerUniPerfHistoryConformance=adGenAosMefPerCosPerUniPerfHistoryConformance, adMefPerCosPerUniPhCurQueueNumber=adMefPerCosPerUniPhCurQueueNumber, adMefPerCosPerUniPhCurGroup=adMefPerCosPerUniPhCurGroup, adMefPerCosPerUniPh15MinIngressGreenFrames=adMefPerCosPerUniPh15MinIngressGreenFrames, adMefPerCosPerUniPh1DayEgressGreenFrameDiscards=adMefPerCosPerUniPh1DayEgressGreenFrameDiscards, adMefPerCosPerUniPh1DayEgressGreenOctetDiscards=adMefPerCosPerUniPh1DayEgressGreenOctetDiscards, adMefPerCosPerUniPh1DayIntervalGroup=adMefPerCosPerUniPh1DayIntervalGroup, adMefPerCosPerUniPh15MinEgressGreenFrames=adMefPerCosPerUniPh15MinEgressGreenFrames)
