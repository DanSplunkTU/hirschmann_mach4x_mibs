#
# PySNMP MIB module ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/adtran/ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:08:25 2022
# On host fv-az36-988 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
adGenAOSMef, adGenAOSConformance = mibBuilder.importSymbols("ADTRAN-AOS", "adGenAOSMef", "adGenAOSConformance")
adIdentity, = mibBuilder.importSymbols("ADTRAN-MIB", "adIdentity")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
HCPerfInvalidIntervals, HCPerfCurrentCount, HCPerfValidIntervals, HCPerfIntervalCount, HCPerfTimeElapsed, HCPerfTotalCount = mibBuilder.importSymbols("HC-PerfHist-TC-MIB", "HCPerfInvalidIntervals", "HCPerfCurrentCount", "HCPerfValidIntervals", "HCPerfIntervalCount", "HCPerfTimeElapsed", "HCPerfTotalCount")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Gauge32, NotificationType, MibIdentifier, iso, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Counter64, ModuleIdentity, IpAddress, Bits, Integer32, Unsigned32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "NotificationType", "MibIdentifier", "iso", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Counter64", "ModuleIdentity", "IpAddress", "Bits", "Integer32", "Unsigned32", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
adGenAosMefPerUniPerfHistoryMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 664, 6, 10000, 53, 9, 1))
adGenAosMefPerUniPerfHistoryMib.setRevisions(('2014-09-10 00:00',))
if mibBuilder.loadTexts: adGenAosMefPerUniPerfHistoryMib.setLastUpdated('201409100000Z')
if mibBuilder.loadTexts: adGenAosMefPerUniPerfHistoryMib.setOrganization('ADTRAN Inc.')
adGenAosMefPerUniPerfHistory = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1))
adMefPerUniPhCurTable = MibTable((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 1), )
if mibBuilder.loadTexts: adMefPerUniPhCurTable.setStatus('current')
adMefPerUniPhCurEntry = MibTableRow((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: adMefPerUniPhCurEntry.setStatus('current')
adMefPerUniPhCurTimeElapsed15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 1, 1, 1), HCPerfTimeElapsed()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerUniPhCurTimeElapsed15Min.setStatus('current')
adMefPerUniPhCurValidIntervals15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 1, 1, 2), HCPerfValidIntervals()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerUniPhCurValidIntervals15Min.setStatus('current')
adMefPerUniPhCurInvalidIntervals15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 1, 1, 3), HCPerfInvalidIntervals()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerUniPhCurInvalidIntervals15Min.setStatus('current')
adMefPerUniPhCurIngressGreenOctets15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 1, 1, 4), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerUniPhCurIngressGreenOctets15Min.setStatus('current')
adMefPerUniPhCurIngressGreenFrames15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 1, 1, 5), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerUniPhCurIngressGreenFrames15Min.setStatus('current')
adMefPerUniPhCurEgressGreenOctets15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 1, 1, 6), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerUniPhCurEgressGreenOctets15Min.setStatus('current')
adMefPerUniPhCurEgressGreenFrames15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 1, 1, 7), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerUniPhCurEgressGreenFrames15Min.setStatus('current')
adMefPerUniPhCurIngressGreenFrameDiscards15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 1, 1, 8), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerUniPhCurIngressGreenFrameDiscards15Min.setStatus('current')
adMefPerUniPhCurEgressGreenFrameDiscards15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 1, 1, 9), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerUniPhCurEgressGreenFrameDiscards15Min.setStatus('current')
adMefPerUniPhCurIngressGreenOctetDiscards15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 1, 1, 10), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerUniPhCurIngressGreenOctetDiscards15Min.setStatus('current')
adMefPerUniPhCurEgressGreenOctetDiscards15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 1, 1, 11), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerUniPhCurEgressGreenOctetDiscards15Min.setStatus('current')
adMefPerUniPhCurTimeElapsed1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 1, 1, 12), HCPerfTimeElapsed()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerUniPhCurTimeElapsed1Day.setStatus('current')
adMefPerUniPhCurValidIntervals1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 1, 1, 13), HCPerfValidIntervals()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerUniPhCurValidIntervals1Day.setStatus('current')
adMefPerUniPhCurInvalidIntervals1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 1, 1, 14), HCPerfInvalidIntervals()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerUniPhCurInvalidIntervals1Day.setStatus('current')
adMefPerUniPhCurIngressGreenOctets1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 1, 1, 15), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerUniPhCurIngressGreenOctets1Day.setStatus('current')
adMefPerUniPhCurIngressGreenFrames1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 1, 1, 16), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerUniPhCurIngressGreenFrames1Day.setStatus('current')
adMefPerUniPhCurEgressGreenOctets1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 1, 1, 17), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerUniPhCurEgressGreenOctets1Day.setStatus('current')
adMefPerUniPhCurEgressGreenFrames1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 1, 1, 18), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerUniPhCurEgressGreenFrames1Day.setStatus('current')
adMefPerUniPhCurIngressGreenFrameDiscards1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 1, 1, 19), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerUniPhCurIngressGreenFrameDiscards1Day.setStatus('current')
adMefPerUniPhCurEgressGreenFrameDiscards1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 1, 1, 20), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerUniPhCurEgressGreenFrameDiscards1Day.setStatus('current')
adMefPerUniPhCurIngressGreenOctetDiscards1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 1, 1, 21), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerUniPhCurIngressGreenOctetDiscards1Day.setStatus('current')
adMefPerUniPhCurEgressGreenOctetDiscards1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 1, 1, 22), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerUniPhCurEgressGreenOctetDiscards1Day.setStatus('current')
adMefPerUniPh15MinIntervalTable = MibTable((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 2), )
if mibBuilder.loadTexts: adMefPerUniPh15MinIntervalTable.setStatus('current')
adMefPerUniPh15MinIntervalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPh15MinIntervalNumber"))
if mibBuilder.loadTexts: adMefPerUniPh15MinIntervalEntry.setStatus('current')
adMefPerUniPh15MinIntervalNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 96)))
if mibBuilder.loadTexts: adMefPerUniPh15MinIntervalNumber.setStatus('current')
adMefPerUniPh15MinIngressGreenOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 2, 1, 2), HCPerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerUniPh15MinIngressGreenOctets.setStatus('current')
adMefPerUniPh15MinIngressGreenFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 2, 1, 3), HCPerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerUniPh15MinIngressGreenFrames.setStatus('current')
adMefPerUniPh15MinEgressGreenOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 2, 1, 4), HCPerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerUniPh15MinEgressGreenOctets.setStatus('current')
adMefPerUniPh15MinEgressGreenFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 2, 1, 5), HCPerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerUniPh15MinEgressGreenFrames.setStatus('current')
adMefPerUniPh15MinIngressGreenFrameDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 2, 1, 6), HCPerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerUniPh15MinIngressGreenFrameDiscards.setStatus('current')
adMefPerUniPh15MinEgressGreenFrameDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 2, 1, 7), HCPerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerUniPh15MinEgressGreenFrameDiscards.setStatus('current')
adMefPerUniPh15MinIngressGreenOctetDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 2, 1, 8), HCPerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerUniPh15MinIngressGreenOctetDiscards.setStatus('current')
adMefPerUniPh15MinEgressGreenOctetDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 2, 1, 9), HCPerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerUniPh15MinEgressGreenOctetDiscards.setStatus('current')
adMefPerUniPh1DayIntervalTable = MibTable((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 3), )
if mibBuilder.loadTexts: adMefPerUniPh1DayIntervalTable.setStatus('current')
adMefPerUniPh1DayIntervalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPh1DayIntervalNumber"))
if mibBuilder.loadTexts: adMefPerUniPh1DayIntervalEntry.setStatus('current')
adMefPerUniPh1DayIntervalNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 30)))
if mibBuilder.loadTexts: adMefPerUniPh1DayIntervalNumber.setStatus('current')
adMefPerUniPh1DayIngressGreenOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 3, 1, 2), HCPerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerUniPh1DayIngressGreenOctets.setStatus('current')
adMefPerUniPh1DayIngressGreenFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 3, 1, 3), HCPerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerUniPh1DayIngressGreenFrames.setStatus('current')
adMefPerUniPh1DayEgressGreenOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 3, 1, 4), HCPerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerUniPh1DayEgressGreenOctets.setStatus('current')
adMefPerUniPh1DayEgressGreenFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 3, 1, 5), HCPerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerUniPh1DayEgressGreenFrames.setStatus('current')
adMefPerUniPh1DayIngressGreenFrameDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 3, 1, 6), HCPerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerUniPh1DayIngressGreenFrameDiscards.setStatus('current')
adMefPerUniPh1DayEgressGreenFrameDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 3, 1, 7), HCPerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerUniPh1DayEgressGreenFrameDiscards.setStatus('current')
adMefPerUniPh1DayIngressGreenOctetDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 3, 1, 8), HCPerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerUniPh1DayIngressGreenOctetDiscards.setStatus('current')
adMefPerUniPh1DayEgressGreenOctetDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 3, 1, 9), HCPerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerUniPh1DayEgressGreenOctetDiscards.setStatus('current')
adGenAosMefPerUniPerfHistoryConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 22))
adGenAosMefPerUniPerfHistoryGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 22, 1))
adGenAosMefPerUniPerfHistoryCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 22, 2))
adGenAosMefPerUniPerfHistoryCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 22, 2, 1)).setObjects(("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPhCurGroup"), ("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPh15MinIntervalGroup"), ("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPh1DayIntervalGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAosMefPerUniPerfHistoryCompliance = adGenAosMefPerUniPerfHistoryCompliance.setStatus('current')
adMefPerUniPhCurGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 22, 1, 1)).setObjects(("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPhCurTimeElapsed15Min"), ("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPhCurValidIntervals15Min"), ("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPhCurInvalidIntervals15Min"), ("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPhCurIngressGreenOctets15Min"), ("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPhCurIngressGreenFrames15Min"), ("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPhCurEgressGreenOctets15Min"), ("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPhCurEgressGreenFrames15Min"), ("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPhCurIngressGreenFrameDiscards15Min"), ("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPhCurEgressGreenFrameDiscards15Min"), ("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPhCurIngressGreenOctetDiscards15Min"), ("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPhCurEgressGreenOctetDiscards15Min"), ("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPhCurTimeElapsed1Day"), ("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPhCurValidIntervals1Day"), ("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPhCurInvalidIntervals1Day"), ("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPhCurIngressGreenOctets1Day"), ("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPhCurIngressGreenFrames1Day"), ("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPhCurEgressGreenOctets1Day"), ("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPhCurEgressGreenFrames1Day"), ("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPhCurIngressGreenFrameDiscards1Day"), ("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPhCurEgressGreenFrameDiscards1Day"), ("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPhCurIngressGreenOctetDiscards1Day"), ("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPhCurEgressGreenOctetDiscards1Day"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adMefPerUniPhCurGroup = adMefPerUniPhCurGroup.setStatus('current')
adMefPerUniPh15MinIntervalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 22, 1, 2)).setObjects(("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPh15MinIngressGreenOctets"), ("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPh15MinIngressGreenFrames"), ("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPh15MinEgressGreenOctets"), ("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPh15MinEgressGreenFrames"), ("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPh15MinIngressGreenFrameDiscards"), ("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPh15MinEgressGreenFrameDiscards"), ("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPh15MinIngressGreenOctetDiscards"), ("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPh15MinEgressGreenOctetDiscards"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adMefPerUniPh15MinIntervalGroup = adMefPerUniPh15MinIntervalGroup.setStatus('current')
adMefPerUniPh1DayIntervalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 22, 1, 3)).setObjects(("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPh1DayIngressGreenOctets"), ("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPh1DayIngressGreenFrames"), ("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPh1DayEgressGreenOctets"), ("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPh1DayEgressGreenFrames"), ("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPh1DayIngressGreenFrameDiscards"), ("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPh1DayEgressGreenFrameDiscards"), ("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPh1DayIngressGreenOctetDiscards"), ("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPh1DayEgressGreenOctetDiscards"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adMefPerUniPh1DayIntervalGroup = adMefPerUniPh1DayIntervalGroup.setStatus('current')
mibBuilder.exportSymbols("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", adMefPerUniPh1DayEgressGreenFrameDiscards=adMefPerUniPh1DayEgressGreenFrameDiscards, adMefPerUniPhCurIngressGreenFrames1Day=adMefPerUniPhCurIngressGreenFrames1Day, adMefPerUniPhCurIngressGreenOctetDiscards1Day=adMefPerUniPhCurIngressGreenOctetDiscards1Day, adMefPerUniPhCurTable=adMefPerUniPhCurTable, adMefPerUniPhCurEgressGreenFrames15Min=adMefPerUniPhCurEgressGreenFrames15Min, adMefPerUniPhCurEntry=adMefPerUniPhCurEntry, adMefPerUniPh15MinIngressGreenFrames=adMefPerUniPh15MinIngressGreenFrames, adMefPerUniPh15MinEgressGreenOctets=adMefPerUniPh15MinEgressGreenOctets, adMefPerUniPh15MinIntervalEntry=adMefPerUniPh15MinIntervalEntry, adMefPerUniPhCurIngressGreenOctets15Min=adMefPerUniPhCurIngressGreenOctets15Min, adMefPerUniPh1DayIntervalEntry=adMefPerUniPh1DayIntervalEntry, adMefPerUniPhCurValidIntervals15Min=adMefPerUniPhCurValidIntervals15Min, adMefPerUniPh1DayIngressGreenFrameDiscards=adMefPerUniPh1DayIngressGreenFrameDiscards, adMefPerUniPh15MinIntervalGroup=adMefPerUniPh15MinIntervalGroup, adGenAosMefPerUniPerfHistoryGroups=adGenAosMefPerUniPerfHistoryGroups, adMefPerUniPh15MinEgressGreenFrames=adMefPerUniPh15MinEgressGreenFrames, adMefPerUniPh1DayIngressGreenOctets=adMefPerUniPh1DayIngressGreenOctets, adMefPerUniPhCurIngressGreenFrameDiscards1Day=adMefPerUniPhCurIngressGreenFrameDiscards1Day, adMefPerUniPhCurIngressGreenFrames15Min=adMefPerUniPhCurIngressGreenFrames15Min, adMefPerUniPh1DayIngressGreenOctetDiscards=adMefPerUniPh1DayIngressGreenOctetDiscards, adMefPerUniPh1DayEgressGreenOctetDiscards=adMefPerUniPh1DayEgressGreenOctetDiscards, adMefPerUniPh15MinIntervalNumber=adMefPerUniPh15MinIntervalNumber, adMefPerUniPhCurInvalidIntervals1Day=adMefPerUniPhCurInvalidIntervals1Day, adMefPerUniPhCurIngressGreenOctets1Day=adMefPerUniPhCurIngressGreenOctets1Day, adGenAosMefPerUniPerfHistoryCompliance=adGenAosMefPerUniPerfHistoryCompliance, adMefPerUniPhCurEgressGreenOctetDiscards15Min=adMefPerUniPhCurEgressGreenOctetDiscards15Min, adMefPerUniPh1DayIntervalGroup=adMefPerUniPh1DayIntervalGroup, adMefPerUniPh15MinIngressGreenOctets=adMefPerUniPh15MinIngressGreenOctets, adMefPerUniPhCurGroup=adMefPerUniPhCurGroup, adMefPerUniPhCurInvalidIntervals15Min=adMefPerUniPhCurInvalidIntervals15Min, adMefPerUniPhCurTimeElapsed1Day=adMefPerUniPhCurTimeElapsed1Day, adMefPerUniPhCurIngressGreenFrameDiscards15Min=adMefPerUniPhCurIngressGreenFrameDiscards15Min, adGenAosMefPerUniPerfHistory=adGenAosMefPerUniPerfHistory, adMefPerUniPhCurEgressGreenFrameDiscards15Min=adMefPerUniPhCurEgressGreenFrameDiscards15Min, adMefPerUniPh15MinIngressGreenOctetDiscards=adMefPerUniPh15MinIngressGreenOctetDiscards, adMefPerUniPh1DayIntervalTable=adMefPerUniPh1DayIntervalTable, adMefPerUniPh1DayEgressGreenOctets=adMefPerUniPh1DayEgressGreenOctets, adMefPerUniPhCurTimeElapsed15Min=adMefPerUniPhCurTimeElapsed15Min, adGenAosMefPerUniPerfHistoryMib=adGenAosMefPerUniPerfHistoryMib, adMefPerUniPhCurEgressGreenOctets1Day=adMefPerUniPhCurEgressGreenOctets1Day, adMefPerUniPh1DayIngressGreenFrames=adMefPerUniPh1DayIngressGreenFrames, adMefPerUniPhCurEgressGreenFrameDiscards1Day=adMefPerUniPhCurEgressGreenFrameDiscards1Day, adMefPerUniPh15MinIntervalTable=adMefPerUniPh15MinIntervalTable, adMefPerUniPh15MinIngressGreenFrameDiscards=adMefPerUniPh15MinIngressGreenFrameDiscards, adMefPerUniPh15MinEgressGreenOctetDiscards=adMefPerUniPh15MinEgressGreenOctetDiscards, adMefPerUniPh15MinEgressGreenFrameDiscards=adMefPerUniPh15MinEgressGreenFrameDiscards, adMefPerUniPhCurEgressGreenOctets15Min=adMefPerUniPhCurEgressGreenOctets15Min, PYSNMP_MODULE_ID=adGenAosMefPerUniPerfHistoryMib, adMefPerUniPh1DayEgressGreenFrames=adMefPerUniPh1DayEgressGreenFrames, adMefPerUniPhCurEgressGreenOctetDiscards1Day=adMefPerUniPhCurEgressGreenOctetDiscards1Day, adMefPerUniPhCurIngressGreenOctetDiscards15Min=adMefPerUniPhCurIngressGreenOctetDiscards15Min, adMefPerUniPhCurEgressGreenFrames1Day=adMefPerUniPhCurEgressGreenFrames1Day, adMefPerUniPh1DayIntervalNumber=adMefPerUniPh1DayIntervalNumber, adGenAosMefPerUniPerfHistoryConformance=adGenAosMefPerUniPerfHistoryConformance, adGenAosMefPerUniPerfHistoryCompliances=adGenAosMefPerUniPerfHistoryCompliances, adMefPerUniPhCurValidIntervals1Day=adMefPerUniPhCurValidIntervals1Day)
