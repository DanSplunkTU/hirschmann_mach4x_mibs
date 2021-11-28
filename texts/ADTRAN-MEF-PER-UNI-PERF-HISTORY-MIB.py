#
# PySNMP MIB module ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/adtran/ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB
# Produced by pysmi-1.1.3 at Sun Nov 28 20:21:46 2021
# On host fv-az77-612 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
adGenAOSConformance, adGenAOSMef = mibBuilder.importSymbols("ADTRAN-AOS", "adGenAOSConformance", "adGenAOSMef")
adIdentity, = mibBuilder.importSymbols("ADTRAN-MIB", "adIdentity")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
HCPerfIntervalCount, HCPerfValidIntervals, HCPerfTimeElapsed, HCPerfInvalidIntervals, HCPerfCurrentCount, HCPerfTotalCount = mibBuilder.importSymbols("HC-PerfHist-TC-MIB", "HCPerfIntervalCount", "HCPerfValidIntervals", "HCPerfTimeElapsed", "HCPerfInvalidIntervals", "HCPerfCurrentCount", "HCPerfTotalCount")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ObjectIdentity, MibIdentifier, Integer32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, iso, Counter64, NotificationType, Unsigned32, ModuleIdentity, IpAddress, Counter32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "MibIdentifier", "Integer32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "iso", "Counter64", "NotificationType", "Unsigned32", "ModuleIdentity", "IpAddress", "Counter32", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
adGenAosMefPerUniPerfHistoryMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 664, 6, 10000, 53, 9, 1))
adGenAosMefPerUniPerfHistoryMib.setRevisions(('2014-09-10 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: adGenAosMefPerUniPerfHistoryMib.setRevisionsDescriptions(('Initial version',))
if mibBuilder.loadTexts: adGenAosMefPerUniPerfHistoryMib.setLastUpdated('201409100000Z')
if mibBuilder.loadTexts: adGenAosMefPerUniPerfHistoryMib.setOrganization('ADTRAN Inc.')
if mibBuilder.loadTexts: adGenAosMefPerUniPerfHistoryMib.setContactInfo('Info:   www.adtran.com\n      Postal: ADTRAN, Inc.\n              901 Explorer Blvd.\n              Huntsville, AL 35806\n      Tel:    +1 888 423-8726\n      E-mail: support@adtran.com')
if mibBuilder.loadTexts: adGenAosMefPerUniPerfHistoryMib.setDescription('This MIB module defines high capacity performance statistics\n      per UNI within an AOS product.\n\n      Copyright (C) ADTRAN, Inc. (2014).')
adGenAosMefPerUniPerfHistory = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1))
adMefPerUniPhCurTable = MibTable((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 1), )
if mibBuilder.loadTexts: adMefPerUniPhCurTable.setStatus('current')
if mibBuilder.loadTexts: adMefPerUniPhCurTable.setDescription('This table contains current performance history information that has been\n      recorded since the last 15 minute interval ended and from when the last\n      1 day interval ended.  This table is indexed by ifIndex which SHOULD be\n      maintained in a persistent manner.')
adMefPerUniPhCurEntry = MibTableRow((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: adMefPerUniPhCurEntry.setStatus('current')
if mibBuilder.loadTexts: adMefPerUniPhCurEntry.setDescription("This specifies the information contained in one entry of the\n      adMefPerUniPhCurTable.  It is indexed by an interface's ifIndex.")
adMefPerUniPhCurTimeElapsed15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 1, 1, 1), HCPerfTimeElapsed()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerUniPhCurTimeElapsed15Min.setStatus('current')
if mibBuilder.loadTexts: adMefPerUniPhCurTimeElapsed15Min.setDescription('Total elapsed seconds in the current 15 minute interval.')
adMefPerUniPhCurValidIntervals15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 1, 1, 2), HCPerfValidIntervals()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerUniPhCurValidIntervals15Min.setStatus('current')
if mibBuilder.loadTexts: adMefPerUniPhCurValidIntervals15Min.setDescription('Number of valid 15 minute intervals over the last 24 hours.')
adMefPerUniPhCurInvalidIntervals15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 1, 1, 3), HCPerfInvalidIntervals()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerUniPhCurInvalidIntervals15Min.setStatus('current')
if mibBuilder.loadTexts: adMefPerUniPhCurInvalidIntervals15Min.setDescription('Number of invalid 15 minute intervals over the last 24 hours.')
adMefPerUniPhCurIngressGreenOctets15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 1, 1, 4), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerUniPhCurIngressGreenOctets15Min.setStatus('current')
if mibBuilder.loadTexts: adMefPerUniPhCurIngressGreenOctets15Min.setDescription('Count of ingress green octets in the current 15 minute interval.')
adMefPerUniPhCurIngressGreenFrames15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 1, 1, 5), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerUniPhCurIngressGreenFrames15Min.setStatus('current')
if mibBuilder.loadTexts: adMefPerUniPhCurIngressGreenFrames15Min.setDescription('Count of ingress green frames in the current 15 minute interval.')
adMefPerUniPhCurEgressGreenOctets15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 1, 1, 6), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerUniPhCurEgressGreenOctets15Min.setStatus('current')
if mibBuilder.loadTexts: adMefPerUniPhCurEgressGreenOctets15Min.setDescription('Count of egress green octets in the current 15 minute interval.')
adMefPerUniPhCurEgressGreenFrames15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 1, 1, 7), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerUniPhCurEgressGreenFrames15Min.setStatus('current')
if mibBuilder.loadTexts: adMefPerUniPhCurEgressGreenFrames15Min.setDescription('Count of egress green frames in the current 15 minute interval.')
adMefPerUniPhCurIngressGreenFrameDiscards15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 1, 1, 8), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerUniPhCurIngressGreenFrameDiscards15Min.setStatus('current')
if mibBuilder.loadTexts: adMefPerUniPhCurIngressGreenFrameDiscards15Min.setDescription('Count of ingress green frames discarded in the current 15 minute interval.')
adMefPerUniPhCurEgressGreenFrameDiscards15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 1, 1, 9), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerUniPhCurEgressGreenFrameDiscards15Min.setStatus('current')
if mibBuilder.loadTexts: adMefPerUniPhCurEgressGreenFrameDiscards15Min.setDescription('Count of egress green frames discarded in the current 15 minute interval.')
adMefPerUniPhCurIngressGreenOctetDiscards15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 1, 1, 10), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerUniPhCurIngressGreenOctetDiscards15Min.setStatus('current')
if mibBuilder.loadTexts: adMefPerUniPhCurIngressGreenOctetDiscards15Min.setDescription('Count of ingress green octets discarded in the current 15 minute interval.')
adMefPerUniPhCurEgressGreenOctetDiscards15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 1, 1, 11), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerUniPhCurEgressGreenOctetDiscards15Min.setStatus('current')
if mibBuilder.loadTexts: adMefPerUniPhCurEgressGreenOctetDiscards15Min.setDescription('Count of egress green octets discarded in the current 15 minute interval.')
adMefPerUniPhCurTimeElapsed1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 1, 1, 12), HCPerfTimeElapsed()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerUniPhCurTimeElapsed1Day.setStatus('current')
if mibBuilder.loadTexts: adMefPerUniPhCurTimeElapsed1Day.setDescription('Total elapsed seconds in the current 1 day interval.')
adMefPerUniPhCurValidIntervals1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 1, 1, 13), HCPerfValidIntervals()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerUniPhCurValidIntervals1Day.setStatus('current')
if mibBuilder.loadTexts: adMefPerUniPhCurValidIntervals1Day.setDescription('Number of valid 1 day intervals available.')
adMefPerUniPhCurInvalidIntervals1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 1, 1, 14), HCPerfInvalidIntervals()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerUniPhCurInvalidIntervals1Day.setStatus('current')
if mibBuilder.loadTexts: adMefPerUniPhCurInvalidIntervals1Day.setDescription('Number of invalid 1 day intervals available.')
adMefPerUniPhCurIngressGreenOctets1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 1, 1, 15), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerUniPhCurIngressGreenOctets1Day.setStatus('current')
if mibBuilder.loadTexts: adMefPerUniPhCurIngressGreenOctets1Day.setDescription('Count of ingress green octets in the current 1 day interval.')
adMefPerUniPhCurIngressGreenFrames1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 1, 1, 16), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerUniPhCurIngressGreenFrames1Day.setStatus('current')
if mibBuilder.loadTexts: adMefPerUniPhCurIngressGreenFrames1Day.setDescription('Count of ingress green framess in the current 1 day interval.')
adMefPerUniPhCurEgressGreenOctets1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 1, 1, 17), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerUniPhCurEgressGreenOctets1Day.setStatus('current')
if mibBuilder.loadTexts: adMefPerUniPhCurEgressGreenOctets1Day.setDescription('Count of egress green octets in the current 1 day interval.')
adMefPerUniPhCurEgressGreenFrames1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 1, 1, 18), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerUniPhCurEgressGreenFrames1Day.setStatus('current')
if mibBuilder.loadTexts: adMefPerUniPhCurEgressGreenFrames1Day.setDescription('Count of egress green frames in the current 1 day interval.')
adMefPerUniPhCurIngressGreenFrameDiscards1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 1, 1, 19), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerUniPhCurIngressGreenFrameDiscards1Day.setStatus('current')
if mibBuilder.loadTexts: adMefPerUniPhCurIngressGreenFrameDiscards1Day.setDescription('Count of ingress green frames discarded in the current 1 day interval.')
adMefPerUniPhCurEgressGreenFrameDiscards1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 1, 1, 20), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerUniPhCurEgressGreenFrameDiscards1Day.setStatus('current')
if mibBuilder.loadTexts: adMefPerUniPhCurEgressGreenFrameDiscards1Day.setDescription('Count of egress green frames discarded in the current 1 day interval.')
adMefPerUniPhCurIngressGreenOctetDiscards1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 1, 1, 21), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerUniPhCurIngressGreenOctetDiscards1Day.setStatus('current')
if mibBuilder.loadTexts: adMefPerUniPhCurIngressGreenOctetDiscards1Day.setDescription('Count of ingress green octets discarded in the current 1 day interval.')
adMefPerUniPhCurEgressGreenOctetDiscards1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 1, 1, 22), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerUniPhCurEgressGreenOctetDiscards1Day.setStatus('current')
if mibBuilder.loadTexts: adMefPerUniPhCurEgressGreenOctetDiscards1Day.setDescription('Count of egress green octets discarded in the current 1 day interval.')
adMefPerUniPh15MinIntervalTable = MibTable((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 2), )
if mibBuilder.loadTexts: adMefPerUniPh15MinIntervalTable.setStatus('current')
if mibBuilder.loadTexts: adMefPerUniPh15MinIntervalTable.setDescription('This table contains performance history information for each valid 15\n      minute interval.  This table is indexed by ifIndex and the interval\n      number.')
adMefPerUniPh15MinIntervalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPh15MinIntervalNumber"))
if mibBuilder.loadTexts: adMefPerUniPh15MinIntervalEntry.setStatus('current')
if mibBuilder.loadTexts: adMefPerUniPh15MinIntervalEntry.setDescription('An entry in the adMefPerUniPh15MinIntervalTable.')
adMefPerUniPh15MinIntervalNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 96)))
if mibBuilder.loadTexts: adMefPerUniPh15MinIntervalNumber.setStatus('current')
if mibBuilder.loadTexts: adMefPerUniPh15MinIntervalNumber.setDescription('Performance history interval number.  Interval 1 is the most\n      recent previous interval; interval 96 is 24 hours ago.\n      Intervals 2..96 are optional.')
adMefPerUniPh15MinIngressGreenOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 2, 1, 2), HCPerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerUniPh15MinIngressGreenOctets.setStatus('current')
if mibBuilder.loadTexts: adMefPerUniPh15MinIngressGreenOctets.setDescription('Count of ingress green octets in the 15 minute interval.')
adMefPerUniPh15MinIngressGreenFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 2, 1, 3), HCPerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerUniPh15MinIngressGreenFrames.setStatus('current')
if mibBuilder.loadTexts: adMefPerUniPh15MinIngressGreenFrames.setDescription('Count of ingress green frames in the 15 minute interval.')
adMefPerUniPh15MinEgressGreenOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 2, 1, 4), HCPerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerUniPh15MinEgressGreenOctets.setStatus('current')
if mibBuilder.loadTexts: adMefPerUniPh15MinEgressGreenOctets.setDescription('Count of egress green octets in the 15 minute interval.')
adMefPerUniPh15MinEgressGreenFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 2, 1, 5), HCPerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerUniPh15MinEgressGreenFrames.setStatus('current')
if mibBuilder.loadTexts: adMefPerUniPh15MinEgressGreenFrames.setDescription('Count of egress green frames in the 15 minute interval.')
adMefPerUniPh15MinIngressGreenFrameDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 2, 1, 6), HCPerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerUniPh15MinIngressGreenFrameDiscards.setStatus('current')
if mibBuilder.loadTexts: adMefPerUniPh15MinIngressGreenFrameDiscards.setDescription('Count of ingress green frames discarded in the 15 minute interval.')
adMefPerUniPh15MinEgressGreenFrameDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 2, 1, 7), HCPerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerUniPh15MinEgressGreenFrameDiscards.setStatus('current')
if mibBuilder.loadTexts: adMefPerUniPh15MinEgressGreenFrameDiscards.setDescription('Count of egress green frames discarded in the 15 minute interval.')
adMefPerUniPh15MinIngressGreenOctetDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 2, 1, 8), HCPerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerUniPh15MinIngressGreenOctetDiscards.setStatus('current')
if mibBuilder.loadTexts: adMefPerUniPh15MinIngressGreenOctetDiscards.setDescription('Count of ingress green octets discarded in the 15 minute interval.')
adMefPerUniPh15MinEgressGreenOctetDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 2, 1, 9), HCPerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerUniPh15MinEgressGreenOctetDiscards.setStatus('current')
if mibBuilder.loadTexts: adMefPerUniPh15MinEgressGreenOctetDiscards.setDescription('Count of egress green octets discarded in the 15 minute interval.')
adMefPerUniPh1DayIntervalTable = MibTable((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 3), )
if mibBuilder.loadTexts: adMefPerUniPh1DayIntervalTable.setStatus('current')
if mibBuilder.loadTexts: adMefPerUniPh1DayIntervalTable.setDescription('This table contains performance history information for each valid 1\n      day interval.  This table is indexed by ifIndex and the interval\n      number.')
adMefPerUniPh1DayIntervalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPh1DayIntervalNumber"))
if mibBuilder.loadTexts: adMefPerUniPh1DayIntervalEntry.setStatus('current')
if mibBuilder.loadTexts: adMefPerUniPh1DayIntervalEntry.setDescription('An entry in the adMefPerUniPh1DayIntervalTable.')
adMefPerUniPh1DayIntervalNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 30)))
if mibBuilder.loadTexts: adMefPerUniPh1DayIntervalNumber.setStatus('current')
if mibBuilder.loadTexts: adMefPerUniPh1DayIntervalNumber.setDescription('Performance history interval number.  Interval 1 is the most recent\n      previous day; interval 7 is 7 days ago.  Intervals 2..30 are optional.')
adMefPerUniPh1DayIngressGreenOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 3, 1, 2), HCPerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerUniPh1DayIngressGreenOctets.setStatus('current')
if mibBuilder.loadTexts: adMefPerUniPh1DayIngressGreenOctets.setDescription('Count of ingress green octets in the 1 day interval.')
adMefPerUniPh1DayIngressGreenFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 3, 1, 3), HCPerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerUniPh1DayIngressGreenFrames.setStatus('current')
if mibBuilder.loadTexts: adMefPerUniPh1DayIngressGreenFrames.setDescription('Count of ingress green frames in the 1 day interval.')
adMefPerUniPh1DayEgressGreenOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 3, 1, 4), HCPerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerUniPh1DayEgressGreenOctets.setStatus('current')
if mibBuilder.loadTexts: adMefPerUniPh1DayEgressGreenOctets.setDescription('Count of egress green octets in the 1 day interval.')
adMefPerUniPh1DayEgressGreenFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 3, 1, 5), HCPerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerUniPh1DayEgressGreenFrames.setStatus('current')
if mibBuilder.loadTexts: adMefPerUniPh1DayEgressGreenFrames.setDescription('Count of egress green frames in the 1 day interval.')
adMefPerUniPh1DayIngressGreenFrameDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 3, 1, 6), HCPerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerUniPh1DayIngressGreenFrameDiscards.setStatus('current')
if mibBuilder.loadTexts: adMefPerUniPh1DayIngressGreenFrameDiscards.setDescription('Count of ingress green frames discarded in the 1 day interval.')
adMefPerUniPh1DayEgressGreenFrameDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 3, 1, 7), HCPerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerUniPh1DayEgressGreenFrameDiscards.setStatus('current')
if mibBuilder.loadTexts: adMefPerUniPh1DayEgressGreenFrameDiscards.setDescription('Count of egress green frames discarded in the 1 day interval.')
adMefPerUniPh1DayIngressGreenOctetDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 3, 1, 8), HCPerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerUniPh1DayIngressGreenOctetDiscards.setStatus('current')
if mibBuilder.loadTexts: adMefPerUniPh1DayIngressGreenOctetDiscards.setDescription('Count of ingress green octets discarded in the 1 day interval.')
adMefPerUniPh1DayEgressGreenOctetDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1, 3, 1, 9), HCPerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerUniPh1DayEgressGreenOctetDiscards.setStatus('current')
if mibBuilder.loadTexts: adMefPerUniPh1DayEgressGreenOctetDiscards.setDescription('Count of egress green octets discarded in the 1 day interval.')
adGenAosMefPerUniPerfHistoryConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 22))
adGenAosMefPerUniPerfHistoryGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 22, 1))
adGenAosMefPerUniPerfHistoryCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 22, 2))
adGenAosMefPerUniPerfHistoryCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 22, 2, 1)).setObjects(("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPhCurGroup"), ("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPh15MinIntervalGroup"), ("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPh1DayIntervalGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAosMefPerUniPerfHistoryCompliance = adGenAosMefPerUniPerfHistoryCompliance.setStatus('current')
if mibBuilder.loadTexts: adGenAosMefPerUniPerfHistoryCompliance.setDescription('The compliance statement for SNMPv2 entities which\n      implement UNI interface per-queue performance history.')
adMefPerUniPhCurGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 22, 1, 1)).setObjects(("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPhCurTimeElapsed15Min"), ("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPhCurValidIntervals15Min"), ("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPhCurInvalidIntervals15Min"), ("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPhCurIngressGreenOctets15Min"), ("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPhCurIngressGreenFrames15Min"), ("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPhCurEgressGreenOctets15Min"), ("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPhCurEgressGreenFrames15Min"), ("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPhCurIngressGreenFrameDiscards15Min"), ("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPhCurEgressGreenFrameDiscards15Min"), ("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPhCurIngressGreenOctetDiscards15Min"), ("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPhCurEgressGreenOctetDiscards15Min"), ("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPhCurTimeElapsed1Day"), ("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPhCurValidIntervals1Day"), ("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPhCurInvalidIntervals1Day"), ("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPhCurIngressGreenOctets1Day"), ("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPhCurIngressGreenFrames1Day"), ("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPhCurEgressGreenOctets1Day"), ("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPhCurEgressGreenFrames1Day"), ("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPhCurIngressGreenFrameDiscards1Day"), ("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPhCurEgressGreenFrameDiscards1Day"), ("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPhCurIngressGreenOctetDiscards1Day"), ("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPhCurEgressGreenOctetDiscards1Day"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adMefPerUniPhCurGroup = adMefPerUniPhCurGroup.setStatus('current')
if mibBuilder.loadTexts: adMefPerUniPhCurGroup.setDescription('The Current Group.')
adMefPerUniPh15MinIntervalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 22, 1, 2)).setObjects(("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPh15MinIngressGreenOctets"), ("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPh15MinIngressGreenFrames"), ("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPh15MinEgressGreenOctets"), ("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPh15MinEgressGreenFrames"), ("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPh15MinIngressGreenFrameDiscards"), ("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPh15MinEgressGreenFrameDiscards"), ("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPh15MinIngressGreenOctetDiscards"), ("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPh15MinEgressGreenOctetDiscards"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adMefPerUniPh15MinIntervalGroup = adMefPerUniPh15MinIntervalGroup.setStatus('current')
if mibBuilder.loadTexts: adMefPerUniPh15MinIntervalGroup.setDescription('The 15 minute interval group.')
adMefPerUniPh1DayIntervalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 22, 1, 3)).setObjects(("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPh1DayIngressGreenOctets"), ("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPh1DayIngressGreenFrames"), ("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPh1DayEgressGreenOctets"), ("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPh1DayEgressGreenFrames"), ("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPh1DayIngressGreenFrameDiscards"), ("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPh1DayEgressGreenFrameDiscards"), ("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPh1DayIngressGreenOctetDiscards"), ("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", "adMefPerUniPh1DayEgressGreenOctetDiscards"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adMefPerUniPh1DayIntervalGroup = adMefPerUniPh1DayIntervalGroup.setStatus('current')
if mibBuilder.loadTexts: adMefPerUniPh1DayIntervalGroup.setDescription('The 1 day interval group.')
mibBuilder.exportSymbols("ADTRAN-MEF-PER-UNI-PERF-HISTORY-MIB", adMefPerUniPhCurIngressGreenFrameDiscards1Day=adMefPerUniPhCurIngressGreenFrameDiscards1Day, adMefPerUniPh1DayIntervalTable=adMefPerUniPh1DayIntervalTable, adGenAosMefPerUniPerfHistoryGroups=adGenAosMefPerUniPerfHistoryGroups, adMefPerUniPh15MinIntervalTable=adMefPerUniPh15MinIntervalTable, adGenAosMefPerUniPerfHistoryCompliances=adGenAosMefPerUniPerfHistoryCompliances, adMefPerUniPhCurTimeElapsed1Day=adMefPerUniPhCurTimeElapsed1Day, adMefPerUniPh1DayIntervalNumber=adMefPerUniPh1DayIntervalNumber, adMefPerUniPh1DayIngressGreenFrameDiscards=adMefPerUniPh1DayIngressGreenFrameDiscards, adMefPerUniPhCurEgressGreenFrameDiscards1Day=adMefPerUniPhCurEgressGreenFrameDiscards1Day, adMefPerUniPh15MinIngressGreenOctetDiscards=adMefPerUniPh15MinIngressGreenOctetDiscards, adGenAosMefPerUniPerfHistoryCompliance=adGenAosMefPerUniPerfHistoryCompliance, adMefPerUniPh1DayIngressGreenOctetDiscards=adMefPerUniPh1DayIngressGreenOctetDiscards, adMefPerUniPhCurTimeElapsed15Min=adMefPerUniPhCurTimeElapsed15Min, adMefPerUniPhCurValidIntervals15Min=adMefPerUniPhCurValidIntervals15Min, adMefPerUniPhCurIngressGreenFrames1Day=adMefPerUniPhCurIngressGreenFrames1Day, adMefPerUniPhCurIngressGreenFrames15Min=adMefPerUniPhCurIngressGreenFrames15Min, adMefPerUniPh15MinIntervalEntry=adMefPerUniPh15MinIntervalEntry, adMefPerUniPh15MinIntervalGroup=adMefPerUniPh15MinIntervalGroup, adMefPerUniPh1DayIntervalGroup=adMefPerUniPh1DayIntervalGroup, adMefPerUniPh1DayIngressGreenFrames=adMefPerUniPh1DayIngressGreenFrames, adMefPerUniPh15MinIngressGreenOctets=adMefPerUniPh15MinIngressGreenOctets, adMefPerUniPhCurEgressGreenFrameDiscards15Min=adMefPerUniPhCurEgressGreenFrameDiscards15Min, adMefPerUniPhCurIngressGreenOctetDiscards15Min=adMefPerUniPhCurIngressGreenOctetDiscards15Min, adMefPerUniPhCurEgressGreenOctetDiscards15Min=adMefPerUniPhCurEgressGreenOctetDiscards15Min, adMefPerUniPh1DayEgressGreenFrames=adMefPerUniPh1DayEgressGreenFrames, adMefPerUniPh1DayEgressGreenOctets=adMefPerUniPh1DayEgressGreenOctets, adMefPerUniPh1DayIngressGreenOctets=adMefPerUniPh1DayIngressGreenOctets, adMefPerUniPhCurInvalidIntervals15Min=adMefPerUniPhCurInvalidIntervals15Min, adGenAosMefPerUniPerfHistory=adGenAosMefPerUniPerfHistory, adMefPerUniPhCurTable=adMefPerUniPhCurTable, adMefPerUniPhCurEntry=adMefPerUniPhCurEntry, adGenAosMefPerUniPerfHistoryMib=adGenAosMefPerUniPerfHistoryMib, adMefPerUniPhCurValidIntervals1Day=adMefPerUniPhCurValidIntervals1Day, adMefPerUniPhCurEgressGreenOctetDiscards1Day=adMefPerUniPhCurEgressGreenOctetDiscards1Day, adMefPerUniPh15MinIntervalNumber=adMefPerUniPh15MinIntervalNumber, adMefPerUniPhCurIngressGreenOctets15Min=adMefPerUniPhCurIngressGreenOctets15Min, adMefPerUniPhCurEgressGreenOctets1Day=adMefPerUniPhCurEgressGreenOctets1Day, adMefPerUniPhCurIngressGreenOctets1Day=adMefPerUniPhCurIngressGreenOctets1Day, adMefPerUniPh15MinIngressGreenFrameDiscards=adMefPerUniPh15MinIngressGreenFrameDiscards, PYSNMP_MODULE_ID=adGenAosMefPerUniPerfHistoryMib, adMefPerUniPhCurEgressGreenFrames15Min=adMefPerUniPhCurEgressGreenFrames15Min, adGenAosMefPerUniPerfHistoryConformance=adGenAosMefPerUniPerfHistoryConformance, adMefPerUniPhCurInvalidIntervals1Day=adMefPerUniPhCurInvalidIntervals1Day, adMefPerUniPhCurEgressGreenOctets15Min=adMefPerUniPhCurEgressGreenOctets15Min, adMefPerUniPhCurEgressGreenFrames1Day=adMefPerUniPhCurEgressGreenFrames1Day, adMefPerUniPhCurIngressGreenFrameDiscards15Min=adMefPerUniPhCurIngressGreenFrameDiscards15Min, adMefPerUniPh15MinEgressGreenOctets=adMefPerUniPh15MinEgressGreenOctets, adMefPerUniPh15MinEgressGreenOctetDiscards=adMefPerUniPh15MinEgressGreenOctetDiscards, adMefPerUniPhCurIngressGreenOctetDiscards1Day=adMefPerUniPhCurIngressGreenOctetDiscards1Day, adMefPerUniPh15MinEgressGreenFrameDiscards=adMefPerUniPh15MinEgressGreenFrameDiscards, adMefPerUniPh1DayEgressGreenOctetDiscards=adMefPerUniPh1DayEgressGreenOctetDiscards, adMefPerUniPhCurGroup=adMefPerUniPhCurGroup, adMefPerUniPh1DayIntervalEntry=adMefPerUniPh1DayIntervalEntry, adMefPerUniPh1DayEgressGreenFrameDiscards=adMefPerUniPh1DayEgressGreenFrameDiscards, adMefPerUniPh15MinIngressGreenFrames=adMefPerUniPh15MinIngressGreenFrames, adMefPerUniPh15MinEgressGreenFrames=adMefPerUniPh15MinEgressGreenFrames)
