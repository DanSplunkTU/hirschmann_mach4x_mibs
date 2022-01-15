#
# PySNMP MIB module ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/adtran/ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 17:50:20 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
adGenAOSConformance, adGenAOSMef = mibBuilder.importSymbols("ADTRAN-AOS", "adGenAOSConformance", "adGenAOSMef")
adIdentity, = mibBuilder.importSymbols("ADTRAN-MIB", "adIdentity")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
HCPerfIntervalCount, HCPerfCurrentCount, HCPerfValidIntervals, HCPerfTotalCount, HCPerfTimeElapsed, HCPerfInvalidIntervals = mibBuilder.importSymbols("HC-PerfHist-TC-MIB", "HCPerfIntervalCount", "HCPerfCurrentCount", "HCPerfValidIntervals", "HCPerfTotalCount", "HCPerfTimeElapsed", "HCPerfInvalidIntervals")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
ModuleIdentity, Counter64, ObjectIdentity, iso, MibIdentifier, IpAddress, Counter32, NotificationType, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Unsigned32, TimeTicks, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "ObjectIdentity", "iso", "MibIdentifier", "IpAddress", "Counter32", "NotificationType", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Unsigned32", "TimeTicks", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
adGenAosMefPerEvcPerfHistoryMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 664, 6, 10000, 53, 9, 3))
adGenAosMefPerEvcPerfHistoryMib.setRevisions(('2014-09-10 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: adGenAosMefPerEvcPerfHistoryMib.setRevisionsDescriptions(('Initial version',))
if mibBuilder.loadTexts: adGenAosMefPerEvcPerfHistoryMib.setLastUpdated('201409100000Z')
if mibBuilder.loadTexts: adGenAosMefPerEvcPerfHistoryMib.setOrganization('ADTRAN Inc.')
if mibBuilder.loadTexts: adGenAosMefPerEvcPerfHistoryMib.setContactInfo('Info:   www.adtran.com\n      Postal: ADTRAN, Inc.\n              901 Explorer Blvd.\n              Huntsville, AL 35806\n      Tel:    +1 888 423-8726\n      E-mail: support@adtran.com')
if mibBuilder.loadTexts: adGenAosMefPerEvcPerfHistoryMib.setDescription('This MIB module defines high capacity performance statistics\n      per EVC within an AOS product.\n\n      Copyright (C) ADTRAN, Inc. (2014).')
adGenAosMefPerEvcPerfHistory = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3))
adMefPerEvcPhCurTable = MibTable((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 1), )
if mibBuilder.loadTexts: adMefPerEvcPhCurTable.setStatus('current')
if mibBuilder.loadTexts: adMefPerEvcPhCurTable.setDescription('This table contains current performance history information that has been\n      recorded since the last 15 minute interval ended and from when the last\n      1 day interval ended.  This table is indexed by adMefPerEvcPhCurEvcNameFixedLen.')
adMefPerEvcPhCurEntry = MibTableRow((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 1, 1), ).setIndexNames((0, "ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPhCurEvcNameFixedLen"))
if mibBuilder.loadTexts: adMefPerEvcPhCurEntry.setStatus('current')
if mibBuilder.loadTexts: adMefPerEvcPhCurEntry.setDescription("This specifies the information contained in one entry of the\n      adMefPerEvcPhCurTable.  It is indexed by an EVC's adMefPerEvcPhCurEvcNameFixedLen.")
adMefPerEvcPhCurEvcNameFixedLen = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(50, 50)).setFixedLength(50))
if mibBuilder.loadTexts: adMefPerEvcPhCurEvcNameFixedLen.setStatus('current')
if mibBuilder.loadTexts: adMefPerEvcPhCurEvcNameFixedLen.setDescription('The name of the EVC.  This string is padded at the end with 0x00 so that \n      this table index has a fixed length of characters of the specified SIZE.')
adMefPerEvcPhCurTimeElapsed15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 1, 1, 2), HCPerfTimeElapsed()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerEvcPhCurTimeElapsed15Min.setStatus('current')
if mibBuilder.loadTexts: adMefPerEvcPhCurTimeElapsed15Min.setDescription('Total elapsed seconds in the current 15 minute interval.')
adMefPerEvcPhCurValidIntervals15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 1, 1, 3), HCPerfValidIntervals()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerEvcPhCurValidIntervals15Min.setStatus('current')
if mibBuilder.loadTexts: adMefPerEvcPhCurValidIntervals15Min.setDescription('Number of valid 15 minute intervals over the last 24 hours.')
adMefPerEvcPhCurInvalidIntervals15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 1, 1, 4), HCPerfInvalidIntervals()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerEvcPhCurInvalidIntervals15Min.setStatus('current')
if mibBuilder.loadTexts: adMefPerEvcPhCurInvalidIntervals15Min.setDescription('Number of invalid 15 minute intervals over the last 24 hours.')
adMefPerEvcPhCurIngressGreenOctets15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 1, 1, 5), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerEvcPhCurIngressGreenOctets15Min.setStatus('current')
if mibBuilder.loadTexts: adMefPerEvcPhCurIngressGreenOctets15Min.setDescription('Count of ingress green octets in the current 15 minute interval.')
adMefPerEvcPhCurIngressGreenFrames15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 1, 1, 6), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerEvcPhCurIngressGreenFrames15Min.setStatus('current')
if mibBuilder.loadTexts: adMefPerEvcPhCurIngressGreenFrames15Min.setDescription('Count of ingress green frames in the current 15 minute interval.')
adMefPerEvcPhCurEgressGreenOctets15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 1, 1, 7), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerEvcPhCurEgressGreenOctets15Min.setStatus('current')
if mibBuilder.loadTexts: adMefPerEvcPhCurEgressGreenOctets15Min.setDescription('Count of egress green octets in the current 15 minute interval.')
adMefPerEvcPhCurEgressGreenFrames15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 1, 1, 8), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerEvcPhCurEgressGreenFrames15Min.setStatus('current')
if mibBuilder.loadTexts: adMefPerEvcPhCurEgressGreenFrames15Min.setDescription('Count of egress green frames in the current 15 minute interval.')
adMefPerEvcPhCurIngressGreenFrameDiscards15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 1, 1, 9), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerEvcPhCurIngressGreenFrameDiscards15Min.setStatus('current')
if mibBuilder.loadTexts: adMefPerEvcPhCurIngressGreenFrameDiscards15Min.setDescription('Count of ingress green frames discarded in the current 15 minute interval.')
adMefPerEvcPhCurEgressGreenFrameDiscards15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 1, 1, 10), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerEvcPhCurEgressGreenFrameDiscards15Min.setStatus('current')
if mibBuilder.loadTexts: adMefPerEvcPhCurEgressGreenFrameDiscards15Min.setDescription('Count of egress green frames discarded in the current 15 minute interval.')
adMefPerEvcPhCurIngressGreenOctetDiscards15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 1, 1, 11), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerEvcPhCurIngressGreenOctetDiscards15Min.setStatus('current')
if mibBuilder.loadTexts: adMefPerEvcPhCurIngressGreenOctetDiscards15Min.setDescription('Count of ingress green octets discarded in the current 15 minute interval.')
adMefPerEvcPhCurEgressGreenOctetDiscards15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 1, 1, 12), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerEvcPhCurEgressGreenOctetDiscards15Min.setStatus('current')
if mibBuilder.loadTexts: adMefPerEvcPhCurEgressGreenOctetDiscards15Min.setDescription('Count of egress green octets discarded in the current 15 minute interval.')
adMefPerEvcPhCurTimeElapsed1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 1, 1, 13), HCPerfTimeElapsed()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerEvcPhCurTimeElapsed1Day.setStatus('current')
if mibBuilder.loadTexts: adMefPerEvcPhCurTimeElapsed1Day.setDescription('Total elapsed seconds in the current 1 day interval.')
adMefPerEvcPhCurValidIntervals1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 1, 1, 14), HCPerfValidIntervals()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerEvcPhCurValidIntervals1Day.setStatus('current')
if mibBuilder.loadTexts: adMefPerEvcPhCurValidIntervals1Day.setDescription('Number of valid 1 day intervals available.')
adMefPerEvcPhCurInvalidIntervals1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 1, 1, 15), HCPerfInvalidIntervals()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerEvcPhCurInvalidIntervals1Day.setStatus('current')
if mibBuilder.loadTexts: adMefPerEvcPhCurInvalidIntervals1Day.setDescription('Number of invalid 1 day intervals available.')
adMefPerEvcPhCurIngressGreenOctets1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 1, 1, 16), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerEvcPhCurIngressGreenOctets1Day.setStatus('current')
if mibBuilder.loadTexts: adMefPerEvcPhCurIngressGreenOctets1Day.setDescription('Count of ingress green octets in the current 1 day interval.')
adMefPerEvcPhCurIngressGreenFrames1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 1, 1, 17), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerEvcPhCurIngressGreenFrames1Day.setStatus('current')
if mibBuilder.loadTexts: adMefPerEvcPhCurIngressGreenFrames1Day.setDescription('Count of ingress green frames in the current 1 day interval.')
adMefPerEvcPhCurEgressGreenOctets1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 1, 1, 18), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerEvcPhCurEgressGreenOctets1Day.setStatus('current')
if mibBuilder.loadTexts: adMefPerEvcPhCurEgressGreenOctets1Day.setDescription('Count of egress green octets in the current 1 day interval.')
adMefPerEvcPhCurEgressGreenFrames1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 1, 1, 19), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerEvcPhCurEgressGreenFrames1Day.setStatus('current')
if mibBuilder.loadTexts: adMefPerEvcPhCurEgressGreenFrames1Day.setDescription('Count of egress green frames in the current 1 day interval.')
adMefPerEvcPhCurIngressGreenFrameDiscards1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 1, 1, 20), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerEvcPhCurIngressGreenFrameDiscards1Day.setStatus('current')
if mibBuilder.loadTexts: adMefPerEvcPhCurIngressGreenFrameDiscards1Day.setDescription('Count of ingress green frames discarded in the current 1 day interval.')
adMefPerEvcPhCurEgressGreenFrameDiscards1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 1, 1, 21), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerEvcPhCurEgressGreenFrameDiscards1Day.setStatus('current')
if mibBuilder.loadTexts: adMefPerEvcPhCurEgressGreenFrameDiscards1Day.setDescription('Count of egress green frames discarded in the current 1 day interval.')
adMefPerEvcPhCurIngressGreenOctetDiscards1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 1, 1, 22), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerEvcPhCurIngressGreenOctetDiscards1Day.setStatus('current')
if mibBuilder.loadTexts: adMefPerEvcPhCurIngressGreenOctetDiscards1Day.setDescription('Count of ingress green octets discarded in the current 1 day interval.')
adMefPerEvcPhCurEgressGreenOctetDiscards1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 1, 1, 23), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerEvcPhCurEgressGreenOctetDiscards1Day.setStatus('current')
if mibBuilder.loadTexts: adMefPerEvcPhCurEgressGreenOctetDiscards1Day.setDescription('Count of egress green octets discarded in the current 1 day interval.')
adMefPerEvcPh15MinIntervalTable = MibTable((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 2), )
if mibBuilder.loadTexts: adMefPerEvcPh15MinIntervalTable.setStatus('current')
if mibBuilder.loadTexts: adMefPerEvcPh15MinIntervalTable.setDescription('This table contains performance history information for each valid 15\n      minute interval.  This table is indexed by adMefPerEvcPh15MinEvcNameFixedLen,\n      and the interval number.')
adMefPerEvcPh15MinIntervalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 2, 1), ).setIndexNames((0, "ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPh15MinEvcNameFixedLen"), (0, "ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPh15MinIntervalNumber"))
if mibBuilder.loadTexts: adMefPerEvcPh15MinIntervalEntry.setStatus('current')
if mibBuilder.loadTexts: adMefPerEvcPh15MinIntervalEntry.setDescription('An entry in the adMefPerEvcPh15MinIntervalTable.')
adMefPerEvcPh15MinEvcNameFixedLen = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 2, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(50, 50)).setFixedLength(50))
if mibBuilder.loadTexts: adMefPerEvcPh15MinEvcNameFixedLen.setStatus('current')
if mibBuilder.loadTexts: adMefPerEvcPh15MinEvcNameFixedLen.setDescription('The name of the EVC.  This string is padded at the end with 0x00 so that \n      this table index has a fixed length of characters of the specified SIZE.')
adMefPerEvcPh15MinIntervalNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 96)))
if mibBuilder.loadTexts: adMefPerEvcPh15MinIntervalNumber.setStatus('current')
if mibBuilder.loadTexts: adMefPerEvcPh15MinIntervalNumber.setDescription('Performance history interval number.  Interval 1 is the most\n      recent previous interval; interval 96 is 24 hours ago.\n      Intervals 2..96 are optional.')
adMefPerEvcPh15MinIngressGreenOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 2, 1, 3), HCPerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerEvcPh15MinIngressGreenOctets.setStatus('current')
if mibBuilder.loadTexts: adMefPerEvcPh15MinIngressGreenOctets.setDescription('Count of ingress green octets in the 15 minute interval.')
adMefPerEvcPh15MinIngressGreenFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 2, 1, 4), HCPerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerEvcPh15MinIngressGreenFrames.setStatus('current')
if mibBuilder.loadTexts: adMefPerEvcPh15MinIngressGreenFrames.setDescription('Count of ingress green frames in the 15 minute interval.')
adMefPerEvcPh15MinEgressGreenOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 2, 1, 5), HCPerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerEvcPh15MinEgressGreenOctets.setStatus('current')
if mibBuilder.loadTexts: adMefPerEvcPh15MinEgressGreenOctets.setDescription('Count of egress green octets in the 15 minute interval.')
adMefPerEvcPh15MinEgressGreenFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 2, 1, 6), HCPerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerEvcPh15MinEgressGreenFrames.setStatus('current')
if mibBuilder.loadTexts: adMefPerEvcPh15MinEgressGreenFrames.setDescription('Count of egress green frames in the 15 minute interval.')
adMefPerEvcPh15MinIngressGreenFrameDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 2, 1, 7), HCPerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerEvcPh15MinIngressGreenFrameDiscards.setStatus('current')
if mibBuilder.loadTexts: adMefPerEvcPh15MinIngressGreenFrameDiscards.setDescription('Count of ingress green frames discarded in the 15 minute interval.')
adMefPerEvcPh15MinEgressGreenFrameDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 2, 1, 8), HCPerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerEvcPh15MinEgressGreenFrameDiscards.setStatus('current')
if mibBuilder.loadTexts: adMefPerEvcPh15MinEgressGreenFrameDiscards.setDescription('Count of egress green frames discarded in the 15 minute interval.')
adMefPerEvcPh15MinIngressGreenOctetDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 2, 1, 9), HCPerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerEvcPh15MinIngressGreenOctetDiscards.setStatus('current')
if mibBuilder.loadTexts: adMefPerEvcPh15MinIngressGreenOctetDiscards.setDescription('Count of ingress green frames discarded in the 15 minute interval.')
adMefPerEvcPh15MinEgressGreenOctetDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 2, 1, 10), HCPerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerEvcPh15MinEgressGreenOctetDiscards.setStatus('current')
if mibBuilder.loadTexts: adMefPerEvcPh15MinEgressGreenOctetDiscards.setDescription('Count of egress green octets discarded in the 15 minute interval.')
adMefPerEvcPh1DayIntervalTable = MibTable((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 3), )
if mibBuilder.loadTexts: adMefPerEvcPh1DayIntervalTable.setStatus('current')
if mibBuilder.loadTexts: adMefPerEvcPh1DayIntervalTable.setDescription('This table contains performance history information for each valid 1\n      day interval.  This table is indexed by adMefPerEvcPh1DayEvcNameFixedLen,\n      and the interval number.')
adMefPerEvcPh1DayIntervalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 3, 1), ).setIndexNames((0, "ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPh1DayEvcNameFixedLen"), (0, "ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPh1DayIntervalNumber"))
if mibBuilder.loadTexts: adMefPerEvcPh1DayIntervalEntry.setStatus('current')
if mibBuilder.loadTexts: adMefPerEvcPh1DayIntervalEntry.setDescription('An entry in the adMefPerEvcPh1DayIntervalTable.')
adMefPerEvcPh1DayEvcNameFixedLen = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 3, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(50, 50)).setFixedLength(50))
if mibBuilder.loadTexts: adMefPerEvcPh1DayEvcNameFixedLen.setStatus('current')
if mibBuilder.loadTexts: adMefPerEvcPh1DayEvcNameFixedLen.setDescription('The name of the EVC.  This string is padded at the end with 0x00 so that \n      this table index has a fixed length of characters of the specified SIZE.')
adMefPerEvcPh1DayIntervalNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 30)))
if mibBuilder.loadTexts: adMefPerEvcPh1DayIntervalNumber.setStatus('current')
if mibBuilder.loadTexts: adMefPerEvcPh1DayIntervalNumber.setDescription('Performance history interval number.  Interval 1 is the most recent\n      previous day; interval 7 is 7 days ago.  Intervals 2..30 are optional.')
adMefPerEvcPh1DayIngressGreenOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 3, 1, 3), HCPerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerEvcPh1DayIngressGreenOctets.setStatus('current')
if mibBuilder.loadTexts: adMefPerEvcPh1DayIngressGreenOctets.setDescription('Count of ingress green octets in the 1 day interval.')
adMefPerEvcPh1DayIngressGreenFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 3, 1, 4), HCPerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerEvcPh1DayIngressGreenFrames.setStatus('current')
if mibBuilder.loadTexts: adMefPerEvcPh1DayIngressGreenFrames.setDescription('Count of ingress green frames in the 1 day interval.')
adMefPerEvcPh1DayEgressGreenOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 3, 1, 5), HCPerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerEvcPh1DayEgressGreenOctets.setStatus('current')
if mibBuilder.loadTexts: adMefPerEvcPh1DayEgressGreenOctets.setDescription('Count of egress green octets in the 1 day interval.')
adMefPerEvcPh1DayEgressGreenFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 3, 1, 6), HCPerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerEvcPh1DayEgressGreenFrames.setStatus('current')
if mibBuilder.loadTexts: adMefPerEvcPh1DayEgressGreenFrames.setDescription('Count of egress green frames in the 1 day interval.')
adMefPerEvcPh1DayIngressGreenFrameDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 3, 1, 7), HCPerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerEvcPh1DayIngressGreenFrameDiscards.setStatus('current')
if mibBuilder.loadTexts: adMefPerEvcPh1DayIngressGreenFrameDiscards.setDescription('Count of ingress green frames discarded in the 1 day interval.')
adMefPerEvcPh1DayEgressGreenFrameDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 3, 1, 8), HCPerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerEvcPh1DayEgressGreenFrameDiscards.setStatus('current')
if mibBuilder.loadTexts: adMefPerEvcPh1DayEgressGreenFrameDiscards.setDescription('Count of egress green frames discarded in the 1 day interval.')
adMefPerEvcPh1DayIngressGreenOctetDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 3, 1, 9), HCPerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerEvcPh1DayIngressGreenOctetDiscards.setStatus('current')
if mibBuilder.loadTexts: adMefPerEvcPh1DayIngressGreenOctetDiscards.setDescription('Count of ingress green octets discarded in the 1 day interval.')
adMefPerEvcPh1DayEgressGreenOctetDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 3, 1, 10), HCPerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerEvcPh1DayEgressGreenOctetDiscards.setStatus('current')
if mibBuilder.loadTexts: adMefPerEvcPh1DayEgressGreenOctetDiscards.setDescription('Count of egress green octets discarded in the 1 day interval.')
adGenAosMefPerEvcPerfHistoryConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 23))
adGenAosMefPerEvcPerfHistoryGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 23, 1))
adGenAosMefPerEvcPerfHistoryCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 23, 2))
adGenAosMefPerEvcPerfHistoryCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 23, 2, 1)).setObjects(("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPhCurGroup"), ("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPh15MinIntervalGroup"), ("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPh1DayIntervalGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAosMefPerEvcPerfHistoryCompliance = adGenAosMefPerEvcPerfHistoryCompliance.setStatus('current')
if mibBuilder.loadTexts: adGenAosMefPerEvcPerfHistoryCompliance.setDescription('The compliance statement for SNMPv2 entities which\n      implement UNI interface per-queue performance history.')
adMefPerEvcPhCurGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 23, 1, 1)).setObjects(("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPhCurTimeElapsed15Min"), ("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPhCurValidIntervals15Min"), ("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPhCurInvalidIntervals15Min"), ("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPhCurIngressGreenOctets15Min"), ("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPhCurIngressGreenFrames15Min"), ("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPhCurEgressGreenOctets15Min"), ("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPhCurEgressGreenFrames15Min"), ("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPhCurIngressGreenFrameDiscards15Min"), ("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPhCurEgressGreenFrameDiscards15Min"), ("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPhCurIngressGreenOctetDiscards15Min"), ("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPhCurEgressGreenOctetDiscards15Min"), ("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPhCurTimeElapsed1Day"), ("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPhCurValidIntervals1Day"), ("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPhCurInvalidIntervals1Day"), ("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPhCurIngressGreenOctets1Day"), ("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPhCurIngressGreenFrames1Day"), ("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPhCurEgressGreenOctets1Day"), ("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPhCurEgressGreenFrames1Day"), ("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPhCurIngressGreenFrameDiscards1Day"), ("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPhCurEgressGreenFrameDiscards1Day"), ("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPhCurIngressGreenOctetDiscards1Day"), ("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPhCurEgressGreenOctetDiscards1Day"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adMefPerEvcPhCurGroup = adMefPerEvcPhCurGroup.setStatus('current')
if mibBuilder.loadTexts: adMefPerEvcPhCurGroup.setDescription('The Current Group.')
adMefPerEvcPh15MinIntervalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 23, 1, 2)).setObjects(("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPh15MinIngressGreenOctets"), ("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPh15MinIngressGreenFrames"), ("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPh15MinEgressGreenOctets"), ("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPh15MinEgressGreenFrames"), ("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPh15MinIngressGreenFrameDiscards"), ("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPh15MinEgressGreenFrameDiscards"), ("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPh15MinIngressGreenOctetDiscards"), ("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPh15MinEgressGreenOctetDiscards"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adMefPerEvcPh15MinIntervalGroup = adMefPerEvcPh15MinIntervalGroup.setStatus('current')
if mibBuilder.loadTexts: adMefPerEvcPh15MinIntervalGroup.setDescription('The 15 minute interval group.')
adMefPerEvcPh1DayIntervalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 23, 1, 3)).setObjects(("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPh1DayIngressGreenOctets"), ("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPh1DayIngressGreenFrames"), ("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPh1DayEgressGreenOctets"), ("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPh1DayEgressGreenFrames"), ("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPh1DayIngressGreenFrameDiscards"), ("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPh1DayEgressGreenFrameDiscards"), ("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPh1DayIngressGreenOctetDiscards"), ("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPh1DayEgressGreenOctetDiscards"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adMefPerEvcPh1DayIntervalGroup = adMefPerEvcPh1DayIntervalGroup.setStatus('current')
if mibBuilder.loadTexts: adMefPerEvcPh1DayIntervalGroup.setDescription('The 1 day interval group.')
mibBuilder.exportSymbols("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", adMefPerEvcPhCurIngressGreenOctetDiscards1Day=adMefPerEvcPhCurIngressGreenOctetDiscards1Day, adMefPerEvcPhCurEntry=adMefPerEvcPhCurEntry, adMefPerEvcPh1DayIngressGreenFrameDiscards=adMefPerEvcPh1DayIngressGreenFrameDiscards, adMefPerEvcPh1DayIngressGreenOctets=adMefPerEvcPh1DayIngressGreenOctets, adMefPerEvcPh1DayEgressGreenOctetDiscards=adMefPerEvcPh1DayEgressGreenOctetDiscards, adMefPerEvcPh1DayIntervalEntry=adMefPerEvcPh1DayIntervalEntry, adMefPerEvcPhCurInvalidIntervals1Day=adMefPerEvcPhCurInvalidIntervals1Day, adMefPerEvcPh15MinEgressGreenFrameDiscards=adMefPerEvcPh15MinEgressGreenFrameDiscards, adMefPerEvcPhCurEgressGreenOctetDiscards15Min=adMefPerEvcPhCurEgressGreenOctetDiscards15Min, adMefPerEvcPh1DayEgressGreenFrameDiscards=adMefPerEvcPh1DayEgressGreenFrameDiscards, adMefPerEvcPhCurValidIntervals1Day=adMefPerEvcPhCurValidIntervals1Day, adMefPerEvcPhCurInvalidIntervals15Min=adMefPerEvcPhCurInvalidIntervals15Min, adMefPerEvcPhCurEgressGreenFrames15Min=adMefPerEvcPhCurEgressGreenFrames15Min, adMefPerEvcPh15MinIntervalTable=adMefPerEvcPh15MinIntervalTable, adMefPerEvcPh1DayIngressGreenFrames=adMefPerEvcPh1DayIngressGreenFrames, adMefPerEvcPh15MinEvcNameFixedLen=adMefPerEvcPh15MinEvcNameFixedLen, adMefPerEvcPh15MinIntervalNumber=adMefPerEvcPh15MinIntervalNumber, adGenAosMefPerEvcPerfHistory=adGenAosMefPerEvcPerfHistory, adMefPerEvcPh15MinIngressGreenOctetDiscards=adMefPerEvcPh15MinIngressGreenOctetDiscards, adGenAosMefPerEvcPerfHistoryCompliance=adGenAosMefPerEvcPerfHistoryCompliance, adGenAosMefPerEvcPerfHistoryGroups=adGenAosMefPerEvcPerfHistoryGroups, adMefPerEvcPh15MinIngressGreenOctets=adMefPerEvcPh15MinIngressGreenOctets, adMefPerEvcPh15MinIngressGreenFrameDiscards=adMefPerEvcPh15MinIngressGreenFrameDiscards, adMefPerEvcPh1DayEvcNameFixedLen=adMefPerEvcPh1DayEvcNameFixedLen, adMefPerEvcPh1DayEgressGreenOctets=adMefPerEvcPh1DayEgressGreenOctets, adMefPerEvcPh15MinEgressGreenOctets=adMefPerEvcPh15MinEgressGreenOctets, adGenAosMefPerEvcPerfHistoryCompliances=adGenAosMefPerEvcPerfHistoryCompliances, adMefPerEvcPhCurIngressGreenOctets15Min=adMefPerEvcPhCurIngressGreenOctets15Min, adMefPerEvcPhCurTimeElapsed15Min=adMefPerEvcPhCurTimeElapsed15Min, adMefPerEvcPh1DayIntervalGroup=adMefPerEvcPh1DayIntervalGroup, adMefPerEvcPhCurGroup=adMefPerEvcPhCurGroup, adMefPerEvcPh15MinIntervalEntry=adMefPerEvcPh15MinIntervalEntry, adMefPerEvcPhCurEvcNameFixedLen=adMefPerEvcPhCurEvcNameFixedLen, adMefPerEvcPhCurTimeElapsed1Day=adMefPerEvcPhCurTimeElapsed1Day, adMefPerEvcPhCurEgressGreenOctetDiscards1Day=adMefPerEvcPhCurEgressGreenOctetDiscards1Day, adMefPerEvcPh15MinIngressGreenFrames=adMefPerEvcPh15MinIngressGreenFrames, adMefPerEvcPh1DayEgressGreenFrames=adMefPerEvcPh1DayEgressGreenFrames, adGenAosMefPerEvcPerfHistoryMib=adGenAosMefPerEvcPerfHistoryMib, adMefPerEvcPhCurEgressGreenOctets15Min=adMefPerEvcPhCurEgressGreenOctets15Min, adMefPerEvcPhCurIngressGreenFrameDiscards15Min=adMefPerEvcPhCurIngressGreenFrameDiscards15Min, adMefPerEvcPhCurEgressGreenFrameDiscards1Day=adMefPerEvcPhCurEgressGreenFrameDiscards1Day, adMefPerEvcPh15MinIntervalGroup=adMefPerEvcPh15MinIntervalGroup, adMefPerEvcPhCurEgressGreenFrameDiscards15Min=adMefPerEvcPhCurEgressGreenFrameDiscards15Min, adMefPerEvcPhCurIngressGreenOctets1Day=adMefPerEvcPhCurIngressGreenOctets1Day, adMefPerEvcPhCurIngressGreenOctetDiscards15Min=adMefPerEvcPhCurIngressGreenOctetDiscards15Min, adMefPerEvcPh1DayIngressGreenOctetDiscards=adMefPerEvcPh1DayIngressGreenOctetDiscards, adMefPerEvcPhCurIngressGreenFrames15Min=adMefPerEvcPhCurIngressGreenFrames15Min, adGenAosMefPerEvcPerfHistoryConformance=adGenAosMefPerEvcPerfHistoryConformance, adMefPerEvcPhCurValidIntervals15Min=adMefPerEvcPhCurValidIntervals15Min, adMefPerEvcPh15MinEgressGreenOctetDiscards=adMefPerEvcPh15MinEgressGreenOctetDiscards, adMefPerEvcPh1DayIntervalNumber=adMefPerEvcPh1DayIntervalNumber, PYSNMP_MODULE_ID=adGenAosMefPerEvcPerfHistoryMib, adMefPerEvcPhCurIngressGreenFrames1Day=adMefPerEvcPhCurIngressGreenFrames1Day, adMefPerEvcPhCurIngressGreenFrameDiscards1Day=adMefPerEvcPhCurIngressGreenFrameDiscards1Day, adMefPerEvcPhCurTable=adMefPerEvcPhCurTable, adMefPerEvcPh1DayIntervalTable=adMefPerEvcPh1DayIntervalTable, adMefPerEvcPh15MinEgressGreenFrames=adMefPerEvcPh15MinEgressGreenFrames, adMefPerEvcPhCurEgressGreenFrames1Day=adMefPerEvcPhCurEgressGreenFrames1Day, adMefPerEvcPhCurEgressGreenOctets1Day=adMefPerEvcPhCurEgressGreenOctets1Day)
