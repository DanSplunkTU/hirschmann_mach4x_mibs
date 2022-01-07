#
# PySNMP MIB module ADTRAN-IF-PERF-HISTORY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/adtran/ADTRAN-IF-PERF-HISTORY-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:08:26 2022
# On host fv-az36-988 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
adGenAOSConformance, adGenAOSCommon = mibBuilder.importSymbols("ADTRAN-AOS", "adGenAOSConformance", "adGenAOSCommon")
adIdentity, = mibBuilder.importSymbols("ADTRAN-MIB", "adIdentity")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
HCPerfIntervalCount, HCPerfTotalCount, HCPerfValidIntervals, HCPerfInvalidIntervals, HCPerfCurrentCount, HCPerfTimeElapsed = mibBuilder.importSymbols("HC-PerfHist-TC-MIB", "HCPerfIntervalCount", "HCPerfTotalCount", "HCPerfValidIntervals", "HCPerfInvalidIntervals", "HCPerfCurrentCount", "HCPerfTimeElapsed")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
TimeTicks, ObjectIdentity, Integer32, iso, Bits, ModuleIdentity, Counter32, NotificationType, IpAddress, Counter64, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "ObjectIdentity", "Integer32", "iso", "Bits", "ModuleIdentity", "Counter32", "NotificationType", "IpAddress", "Counter64", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
adGenAosIfPerfHistoryMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 664, 6, 10000, 53, 1, 7))
adGenAosIfPerfHistoryMib.setRevisions(('2013-08-23 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: adGenAosIfPerfHistoryMib.setRevisionsDescriptions(('Initial version',))
if mibBuilder.loadTexts: adGenAosIfPerfHistoryMib.setLastUpdated('201308230000Z')
if mibBuilder.loadTexts: adGenAosIfPerfHistoryMib.setOrganization('ADTRAN Inc.')
if mibBuilder.loadTexts: adGenAosIfPerfHistoryMib.setContactInfo('Info:   www.adtran.com\n      Postal: ADTRAN, Inc.\n              901 Explorer Blvd.\n              Huntsville, AL 35806\n      Tel:    +1 888 423-8726\n      E-mail: support@adtran.com')
if mibBuilder.loadTexts: adGenAosIfPerfHistoryMib.setDescription('This MIB module defines high capacity performance statistics for\n      interfaces within an AOS product.\n\n      Copyright (C) ADTRAN, Inc. (2013).')
adGenAosIfPerfHistory = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7))
adIfPhCurTable = MibTable((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 1), )
if mibBuilder.loadTexts: adIfPhCurTable.setStatus('current')
if mibBuilder.loadTexts: adIfPhCurTable.setDescription('This table contains current performance history information that has been\n      recorded since the last 15 minute interval ended and from when the last\n      1 day interval ended.  This table is indexed by by ifIndex which SHOULD be\n      maintained in a persistent manner.')
adIfPhCurEntry = MibTableRow((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: adIfPhCurEntry.setStatus('current')
if mibBuilder.loadTexts: adIfPhCurEntry.setDescription("This specifies the information contained in one entry of the\n      adIfPerfHistoryCurTable.  It is indexed by an interface's IfIndex.")
adIfPhCurTimeElapsed15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 1, 1, 1), HCPerfTimeElapsed()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPhCurTimeElapsed15Min.setStatus('current')
if mibBuilder.loadTexts: adIfPhCurTimeElapsed15Min.setDescription('Total elapsed seconds in the current 15 minute interval.')
adIfPhCurValidIntervals15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 1, 1, 2), HCPerfValidIntervals()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPhCurValidIntervals15Min.setStatus('current')
if mibBuilder.loadTexts: adIfPhCurValidIntervals15Min.setDescription('Number of valid 15 minute intervals over the last 24 hours.')
adIfPhCurInvalidIntervals15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 1, 1, 3), HCPerfInvalidIntervals()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPhCurInvalidIntervals15Min.setStatus('current')
if mibBuilder.loadTexts: adIfPhCurInvalidIntervals15Min.setDescription('Number of invalid 15 minute intervals over the last 24 hours.')
adIfPhCurInOctets15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 1, 1, 4), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPhCurInOctets15Min.setStatus('current')
if mibBuilder.loadTexts: adIfPhCurInOctets15Min.setDescription('Count of octets received in the current 15 minute interval.')
adIfPhCurInUcastPkts15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 1, 1, 5), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPhCurInUcastPkts15Min.setStatus('current')
if mibBuilder.loadTexts: adIfPhCurInUcastPkts15Min.setDescription('Count of unicast packets received in the current 15 minute interval.')
adIfPhCurInMcastPkts15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 1, 1, 6), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPhCurInMcastPkts15Min.setStatus('current')
if mibBuilder.loadTexts: adIfPhCurInMcastPkts15Min.setDescription('Count of multicast packets received in the current 15 minute interval.')
adIfPhCurInBcastPkts15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 1, 1, 7), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPhCurInBcastPkts15Min.setStatus('current')
if mibBuilder.loadTexts: adIfPhCurInBcastPkts15Min.setDescription('Count of broadcast packets received in the current 15 minute interval.')
adIfPhCurInDiscards15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 1, 1, 8), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPhCurInDiscards15Min.setStatus('current')
if mibBuilder.loadTexts: adIfPhCurInDiscards15Min.setDescription('Count of inbound packets discarded in the current 15 minute interval.')
adIfPhCurInErrors15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 1, 1, 9), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPhCurInErrors15Min.setStatus('current')
if mibBuilder.loadTexts: adIfPhCurInErrors15Min.setDescription('Count of inbound packets containing errors in the current 15 minute interval.')
adIfPhCurInUnknownProtos15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 1, 1, 10), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPhCurInUnknownProtos15Min.setStatus('current')
if mibBuilder.loadTexts: adIfPhCurInUnknownProtos15Min.setDescription('Count of inbound packets with an unknown or unsupported protocol in the\n      current 15 minute interval.')
adIfPhCurOutOctets15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 1, 1, 11), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPhCurOutOctets15Min.setStatus('current')
if mibBuilder.loadTexts: adIfPhCurOutOctets15Min.setDescription('Count of octets transmitted in the current 15 minute interval.')
adIfPhCurOutUcastPkts15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 1, 1, 12), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPhCurOutUcastPkts15Min.setStatus('current')
if mibBuilder.loadTexts: adIfPhCurOutUcastPkts15Min.setDescription('Count of transmitted unicast packets in the current 15 minute interval.')
adIfPhCurOutMcastPkts15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 1, 1, 13), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPhCurOutMcastPkts15Min.setStatus('current')
if mibBuilder.loadTexts: adIfPhCurOutMcastPkts15Min.setDescription('Count of transmitted multicast packets in the current 15 minute interval.')
adIfPhCurOutBcastPkts15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 1, 1, 14), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPhCurOutBcastPkts15Min.setStatus('current')
if mibBuilder.loadTexts: adIfPhCurOutBcastPkts15Min.setDescription('Count of transmitted broadcast packets in the current 15 minute interval.')
adIfPhCurOutDiscards15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 1, 1, 15), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPhCurOutDiscards15Min.setStatus('current')
if mibBuilder.loadTexts: adIfPhCurOutDiscards15Min.setDescription('Count of discarded outbound packets in the current 15 minute interval.')
adIfPhCurOutErrors15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 1, 1, 16), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPhCurOutErrors15Min.setStatus('current')
if mibBuilder.loadTexts: adIfPhCurOutErrors15Min.setDescription('Count of outbound packets that could not be transmitted due to error in\n      the current 15 minute interval.')
adIfPhCurTimeElapsed1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 1, 1, 17), HCPerfTimeElapsed()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPhCurTimeElapsed1Day.setStatus('current')
if mibBuilder.loadTexts: adIfPhCurTimeElapsed1Day.setDescription('Total elapsed seconds in the current 1 day interval.')
adIfPhCurValidIntervals1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 1, 1, 18), HCPerfValidIntervals()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPhCurValidIntervals1Day.setStatus('current')
if mibBuilder.loadTexts: adIfPhCurValidIntervals1Day.setDescription('Number of valid 1 day intervals available.')
adIfPhCurInvalidIntervals1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 1, 1, 19), HCPerfInvalidIntervals()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPhCurInvalidIntervals1Day.setStatus('current')
if mibBuilder.loadTexts: adIfPhCurInvalidIntervals1Day.setDescription('Number of invalid 1 day intervals available.')
adIfPhCurInOctets1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 1, 1, 20), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPhCurInOctets1Day.setStatus('current')
if mibBuilder.loadTexts: adIfPhCurInOctets1Day.setDescription('Count of octets received in the current 1 day interval.')
adIfPhCurInUcastPkts1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 1, 1, 21), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPhCurInUcastPkts1Day.setStatus('current')
if mibBuilder.loadTexts: adIfPhCurInUcastPkts1Day.setDescription('Count of unicast packets received in the current 1 day interval.')
adIfPhCurInMcastPkts1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 1, 1, 22), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPhCurInMcastPkts1Day.setStatus('current')
if mibBuilder.loadTexts: adIfPhCurInMcastPkts1Day.setDescription('Count of multicast packets received in the current 1 day interval.')
adIfPhCurInBcastPkts1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 1, 1, 23), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPhCurInBcastPkts1Day.setStatus('current')
if mibBuilder.loadTexts: adIfPhCurInBcastPkts1Day.setDescription('Count of broadcast packets received in the current 1 day interval.')
adIfPhCurInDiscards1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 1, 1, 24), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPhCurInDiscards1Day.setStatus('current')
if mibBuilder.loadTexts: adIfPhCurInDiscards1Day.setDescription('Count of inbound packets discarded in the current 1 day interval.')
adIfPhCurInErrors1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 1, 1, 25), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPhCurInErrors1Day.setStatus('current')
if mibBuilder.loadTexts: adIfPhCurInErrors1Day.setDescription('Count of inbound packets containing errors in the current 1 day interval.')
adIfPhCurInUnknownProtos1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 1, 1, 26), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPhCurInUnknownProtos1Day.setStatus('current')
if mibBuilder.loadTexts: adIfPhCurInUnknownProtos1Day.setDescription('Count of inbound packets with an unknown or unsupported protocol in the\n      current 1 day interval.')
adIfPhCurOutOctets1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 1, 1, 27), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPhCurOutOctets1Day.setStatus('current')
if mibBuilder.loadTexts: adIfPhCurOutOctets1Day.setDescription('Count of octets transmitted in the current 1 day interval.')
adIfPhCurOutUcastPkts1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 1, 1, 28), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPhCurOutUcastPkts1Day.setStatus('current')
if mibBuilder.loadTexts: adIfPhCurOutUcastPkts1Day.setDescription('Count of transmitted unicast packets in the current 1 day interval.')
adIfPhCurOutMcastPkts1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 1, 1, 29), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPhCurOutMcastPkts1Day.setStatus('current')
if mibBuilder.loadTexts: adIfPhCurOutMcastPkts1Day.setDescription('Count of transmitted multicast packets in the current 1 day interval.')
adIfPhCurOutBcastPkts1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 1, 1, 30), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPhCurOutBcastPkts1Day.setStatus('current')
if mibBuilder.loadTexts: adIfPhCurOutBcastPkts1Day.setDescription('Count of transmitted broadcast packets in the current 1 day interval.')
adIfPhCurOutDiscards1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 1, 1, 31), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPhCurOutDiscards1Day.setStatus('current')
if mibBuilder.loadTexts: adIfPhCurOutDiscards1Day.setDescription('Count of discarded outbound packets in the current 1 day interval.')
adIfPhCurOutErrors1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 1, 1, 32), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPhCurOutErrors1Day.setStatus('current')
if mibBuilder.loadTexts: adIfPhCurOutErrors1Day.setDescription('Count of outbound packets that could not be transmitted due to error in\n      the current 1 day interval.')
adIfPh15MinIntervalTable = MibTable((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 2), )
if mibBuilder.loadTexts: adIfPh15MinIntervalTable.setStatus('current')
if mibBuilder.loadTexts: adIfPh15MinIntervalTable.setDescription('This table contains performance history information for each valid 15\n      minute interval.  This table is indexed by by ifIndex and the interval\n      number.')
adIfPh15MinIntervalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "ADTRAN-IF-PERF-HISTORY-MIB", "adIfPh15MinIntervalNumber"))
if mibBuilder.loadTexts: adIfPh15MinIntervalEntry.setStatus('current')
if mibBuilder.loadTexts: adIfPh15MinIntervalEntry.setDescription('An entry in the adIfPh15MinIntervalTable.')
adIfPh15MinIntervalNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 96)))
if mibBuilder.loadTexts: adIfPh15MinIntervalNumber.setStatus('current')
if mibBuilder.loadTexts: adIfPh15MinIntervalNumber.setDescription('Performance history interval number.  Interval 1 is the most\n      recent previous interval; interval 96 is 24 hours ago.\n      Intervals 2..96 are optional.')
adIfPh15MinInOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 2, 1, 2), HCPerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPh15MinInOctets.setStatus('current')
if mibBuilder.loadTexts: adIfPh15MinInOctets.setDescription('Count of octets received in the 15 minute interval.')
adIfPh15MinInUcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 2, 1, 3), HCPerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPh15MinInUcastPkts.setStatus('current')
if mibBuilder.loadTexts: adIfPh15MinInUcastPkts.setDescription('Count of unicast packets received in the 15 minute interval.')
adIfPh15MinInMcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 2, 1, 4), HCPerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPh15MinInMcastPkts.setStatus('current')
if mibBuilder.loadTexts: adIfPh15MinInMcastPkts.setDescription('Count of multicast packets received in the 15 minute interval.')
adIfPh15MinInBcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 2, 1, 5), HCPerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPh15MinInBcastPkts.setStatus('current')
if mibBuilder.loadTexts: adIfPh15MinInBcastPkts.setDescription('Count of broadcast packets received in the 15 minute interval.')
adIfPh15MinInDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 2, 1, 6), HCPerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPh15MinInDiscards.setStatus('current')
if mibBuilder.loadTexts: adIfPh15MinInDiscards.setDescription('Count of inbound packets discarded in the 15 minute interval.')
adIfPh15MinInErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 2, 1, 7), HCPerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPh15MinInErrors.setStatus('current')
if mibBuilder.loadTexts: adIfPh15MinInErrors.setDescription('Count of inbound packets containing errors in the 15 minute interval.')
adIfPh15MinInUnknownProtos = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 2, 1, 8), HCPerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPh15MinInUnknownProtos.setStatus('current')
if mibBuilder.loadTexts: adIfPh15MinInUnknownProtos.setDescription('Count of inbound packets with an unknown or unsupported protocol in the\n      15 minute interval.')
adIfPh15MinOutOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 2, 1, 9), HCPerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPh15MinOutOctets.setStatus('current')
if mibBuilder.loadTexts: adIfPh15MinOutOctets.setDescription('Count of octets transmitted in the 15 minute interval.')
adIfPh15MinOutUcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 2, 1, 10), HCPerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPh15MinOutUcastPkts.setStatus('current')
if mibBuilder.loadTexts: adIfPh15MinOutUcastPkts.setDescription('Count of transmitted unicast packets in the 15 minute interval.')
adIfPh15MinOutMcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 2, 1, 11), HCPerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPh15MinOutMcastPkts.setStatus('current')
if mibBuilder.loadTexts: adIfPh15MinOutMcastPkts.setDescription('Count of transmitted multicast packets in the 15 minute interval.')
adIfPh15MinOutBcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 2, 1, 12), HCPerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPh15MinOutBcastPkts.setStatus('current')
if mibBuilder.loadTexts: adIfPh15MinOutBcastPkts.setDescription('Count of transmitted broadcast packets in the 15 minute interval.')
adIfPh15MinOutDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 2, 1, 13), HCPerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPh15MinOutDiscards.setStatus('current')
if mibBuilder.loadTexts: adIfPh15MinOutDiscards.setDescription('Count of discarded outbound packets in the 15 minute interval.')
adIfPh15MinOutErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 2, 1, 14), HCPerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPh15MinOutErrors.setStatus('current')
if mibBuilder.loadTexts: adIfPh15MinOutErrors.setDescription('Count of outbound packets that could not be transmitted due to error in\n      the 15 minute interval.')
adIfPh1DayIntervalTable = MibTable((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 3), )
if mibBuilder.loadTexts: adIfPh1DayIntervalTable.setStatus('current')
if mibBuilder.loadTexts: adIfPh1DayIntervalTable.setDescription('This table contains performance history information for each valid 1\n      day interval.  This table is indexed by by ifIndex and the interval\n      number.')
adIfPh1DayIntervalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "ADTRAN-IF-PERF-HISTORY-MIB", "adIfPh1DayIntervalNumber"))
if mibBuilder.loadTexts: adIfPh1DayIntervalEntry.setStatus('current')
if mibBuilder.loadTexts: adIfPh1DayIntervalEntry.setDescription('An entry in the adIfPh1DayIntervalTable.')
adIfPh1DayIntervalNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 30)))
if mibBuilder.loadTexts: adIfPh1DayIntervalNumber.setStatus('current')
if mibBuilder.loadTexts: adIfPh1DayIntervalNumber.setDescription('Performance history interval number.  Interval 1 is the most recent\n      previous day; interval 7 is 7 days ago.  Intervals 2..30 are optional.')
adIfPh1DayInOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 3, 1, 2), HCPerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPh1DayInOctets.setStatus('current')
if mibBuilder.loadTexts: adIfPh1DayInOctets.setDescription('Count of octets received in the 1 day interval.')
adIfPh1DayInUcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 3, 1, 3), HCPerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPh1DayInUcastPkts.setStatus('current')
if mibBuilder.loadTexts: adIfPh1DayInUcastPkts.setDescription('Count of unicast packets received in the 1 day interval.')
adIfPh1DayInMcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 3, 1, 4), HCPerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPh1DayInMcastPkts.setStatus('current')
if mibBuilder.loadTexts: adIfPh1DayInMcastPkts.setDescription('Count of multicast packets received in the 1 day interval.')
adIfPh1DayInBcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 3, 1, 5), HCPerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPh1DayInBcastPkts.setStatus('current')
if mibBuilder.loadTexts: adIfPh1DayInBcastPkts.setDescription('Count of broadcast packets received in the 1 day interval.')
adIfPh1DayInDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 3, 1, 6), HCPerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPh1DayInDiscards.setStatus('current')
if mibBuilder.loadTexts: adIfPh1DayInDiscards.setDescription('Count of inbound packets discarded in the 1 day interval.')
adIfPh1DayInErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 3, 1, 7), HCPerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPh1DayInErrors.setStatus('current')
if mibBuilder.loadTexts: adIfPh1DayInErrors.setDescription('Count of inbound packets containing errors in the 1 day interval.')
adIfPh1DayInUnknownProtos = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 3, 1, 8), HCPerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPh1DayInUnknownProtos.setStatus('current')
if mibBuilder.loadTexts: adIfPh1DayInUnknownProtos.setDescription('Count of inbound packets with an unknown or unsupported protocol in the\n      1 day interval.')
adIfPh1DayOutOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 3, 1, 9), HCPerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPh1DayOutOctets.setStatus('current')
if mibBuilder.loadTexts: adIfPh1DayOutOctets.setDescription('Count of octets transmitted in the 1 day interval.')
adIfPh1DayOutUcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 3, 1, 10), HCPerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPh1DayOutUcastPkts.setStatus('current')
if mibBuilder.loadTexts: adIfPh1DayOutUcastPkts.setDescription('Count of transmitted unicast packets in the 1 day interval.')
adIfPh1DayOutMcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 3, 1, 11), HCPerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPh1DayOutMcastPkts.setStatus('current')
if mibBuilder.loadTexts: adIfPh1DayOutMcastPkts.setDescription('Count of transmitted multicast packets in the 1 day interval.')
adIfPh1DayOutBcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 3, 1, 12), HCPerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPh1DayOutBcastPkts.setStatus('current')
if mibBuilder.loadTexts: adIfPh1DayOutBcastPkts.setDescription('Count of transmitted broadcast packets in the 1 day interval.')
adIfPh1DayOutDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 3, 1, 13), HCPerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPh1DayOutDiscards.setStatus('current')
if mibBuilder.loadTexts: adIfPh1DayOutDiscards.setDescription('Count of discarded outbound packets in the 1 day interval.')
adIfPh1DayOutErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 3, 1, 14), HCPerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPh1DayOutErrors.setStatus('current')
if mibBuilder.loadTexts: adIfPh1DayOutErrors.setDescription('Count of outbound packets that could not be transmitted due to error in\n      the 1 day interval.')
adGenAosIfPerfHistoryConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 16))
adGenAosIfPerfHistoryGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 16, 1))
adGenAosIfPerfHistoryCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 16, 2))
adGenAosIfPerfHistoryCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 16, 2, 1)).setObjects(("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPhCurGroup"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPh15MinIntervalGroup"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPh1DayIntervalGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAosIfPerfHistoryCompliance = adGenAosIfPerfHistoryCompliance.setStatus('current')
if mibBuilder.loadTexts: adGenAosIfPerfHistoryCompliance.setDescription('The compliance statement for SNMPv2 entities which\n      implement interface performance history.')
adIfPhCurGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 16, 1, 1)).setObjects(("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPhCurTimeElapsed15Min"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPhCurValidIntervals15Min"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPhCurInvalidIntervals15Min"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPhCurInOctets15Min"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPhCurInUcastPkts15Min"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPhCurInMcastPkts15Min"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPhCurInBcastPkts15Min"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPhCurInDiscards15Min"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPhCurInErrors15Min"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPhCurInUnknownProtos15Min"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPhCurOutOctets15Min"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPhCurOutUcastPkts15Min"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPhCurOutMcastPkts15Min"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPhCurOutBcastPkts15Min"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPhCurOutDiscards15Min"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPhCurOutErrors15Min"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPhCurTimeElapsed1Day"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPhCurValidIntervals1Day"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPhCurInvalidIntervals1Day"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPhCurInOctets1Day"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPhCurInUcastPkts1Day"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPhCurInMcastPkts1Day"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPhCurInBcastPkts1Day"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPhCurInDiscards1Day"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPhCurInErrors1Day"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPhCurInUnknownProtos1Day"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPhCurOutOctets1Day"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPhCurOutUcastPkts1Day"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPhCurOutMcastPkts1Day"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPhCurOutBcastPkts1Day"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPhCurOutDiscards1Day"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPhCurOutErrors1Day"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adIfPhCurGroup = adIfPhCurGroup.setStatus('current')
if mibBuilder.loadTexts: adIfPhCurGroup.setDescription('The Current Group.')
adIfPh15MinIntervalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 16, 1, 2)).setObjects(("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPh15MinInOctets"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPh15MinInUcastPkts"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPh15MinInMcastPkts"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPh15MinInBcastPkts"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPh15MinInDiscards"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPh15MinInErrors"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPh15MinInUnknownProtos"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPh15MinOutOctets"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPh15MinOutUcastPkts"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPh15MinOutMcastPkts"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPh15MinOutBcastPkts"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPh15MinOutDiscards"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPh15MinOutErrors"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adIfPh15MinIntervalGroup = adIfPh15MinIntervalGroup.setStatus('current')
if mibBuilder.loadTexts: adIfPh15MinIntervalGroup.setDescription('The 15 minute interval group.')
adIfPh1DayIntervalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 16, 1, 3)).setObjects(("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPh1DayInOctets"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPh1DayInUcastPkts"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPh1DayInMcastPkts"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPh1DayInBcastPkts"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPh1DayInDiscards"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPh1DayInErrors"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPh1DayInUnknownProtos"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPh1DayOutOctets"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPh1DayOutUcastPkts"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPh1DayOutMcastPkts"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPh1DayOutBcastPkts"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPh1DayOutDiscards"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPh1DayOutErrors"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adIfPh1DayIntervalGroup = adIfPh1DayIntervalGroup.setStatus('current')
if mibBuilder.loadTexts: adIfPh1DayIntervalGroup.setDescription('The 1 day interval group.')
mibBuilder.exportSymbols("ADTRAN-IF-PERF-HISTORY-MIB", adIfPh15MinOutBcastPkts=adIfPh15MinOutBcastPkts, adIfPhCurTimeElapsed1Day=adIfPhCurTimeElapsed1Day, adIfPhCurInUnknownProtos1Day=adIfPhCurInUnknownProtos1Day, adIfPh15MinOutOctets=adIfPh15MinOutOctets, adIfPh15MinInDiscards=adIfPh15MinInDiscards, adIfPh1DayOutDiscards=adIfPh1DayOutDiscards, adIfPh1DayOutOctets=adIfPh1DayOutOctets, adIfPhCurOutErrors1Day=adIfPhCurOutErrors1Day, adIfPhCurInBcastPkts1Day=adIfPhCurInBcastPkts1Day, adIfPh15MinInOctets=adIfPh15MinInOctets, adGenAosIfPerfHistoryCompliances=adGenAosIfPerfHistoryCompliances, adIfPh1DayIntervalGroup=adIfPh1DayIntervalGroup, adIfPhCurInDiscards1Day=adIfPhCurInDiscards1Day, adIfPhCurInvalidIntervals1Day=adIfPhCurInvalidIntervals1Day, adIfPh1DayInUnknownProtos=adIfPh1DayInUnknownProtos, adIfPh15MinOutMcastPkts=adIfPh15MinOutMcastPkts, adIfPhCurOutBcastPkts15Min=adIfPhCurOutBcastPkts15Min, adIfPhCurGroup=adIfPhCurGroup, adIfPhCurOutOctets15Min=adIfPhCurOutOctets15Min, adIfPh15MinOutErrors=adIfPh15MinOutErrors, adGenAosIfPerfHistoryCompliance=adGenAosIfPerfHistoryCompliance, adIfPh15MinIntervalGroup=adIfPh15MinIntervalGroup, adIfPhCurEntry=adIfPhCurEntry, adIfPh15MinInErrors=adIfPh15MinInErrors, adIfPhCurInUcastPkts15Min=adIfPhCurInUcastPkts15Min, adIfPhCurOutMcastPkts15Min=adIfPhCurOutMcastPkts15Min, adIfPh1DayInDiscards=adIfPh1DayInDiscards, adIfPh1DayOutUcastPkts=adIfPh1DayOutUcastPkts, adGenAosIfPerfHistoryGroups=adGenAosIfPerfHistoryGroups, adIfPhCurInBcastPkts15Min=adIfPhCurInBcastPkts15Min, adIfPh15MinOutDiscards=adIfPh15MinOutDiscards, adIfPh15MinIntervalTable=adIfPh15MinIntervalTable, adIfPhCurInOctets15Min=adIfPhCurInOctets15Min, adIfPhCurTimeElapsed15Min=adIfPhCurTimeElapsed15Min, adIfPh15MinInBcastPkts=adIfPh15MinInBcastPkts, adIfPhCurOutBcastPkts1Day=adIfPhCurOutBcastPkts1Day, adIfPh1DayOutErrors=adIfPh1DayOutErrors, adIfPhCurInUnknownProtos15Min=adIfPhCurInUnknownProtos15Min, adIfPh1DayInErrors=adIfPh1DayInErrors, adIfPhCurOutUcastPkts15Min=adIfPhCurOutUcastPkts15Min, adIfPhCurValidIntervals1Day=adIfPhCurValidIntervals1Day, adIfPh1DayIntervalEntry=adIfPh1DayIntervalEntry, adIfPh1DayIntervalNumber=adIfPh1DayIntervalNumber, adIfPh15MinIntervalNumber=adIfPh15MinIntervalNumber, adGenAosIfPerfHistoryMib=adGenAosIfPerfHistoryMib, adIfPhCurOutErrors15Min=adIfPhCurOutErrors15Min, adIfPh15MinOutUcastPkts=adIfPh15MinOutUcastPkts, adIfPhCurInDiscards15Min=adIfPhCurInDiscards15Min, adIfPhCurOutDiscards15Min=adIfPhCurOutDiscards15Min, adIfPhCurOutMcastPkts1Day=adIfPhCurOutMcastPkts1Day, adIfPhCurInvalidIntervals15Min=adIfPhCurInvalidIntervals15Min, adIfPhCurOutOctets1Day=adIfPhCurOutOctets1Day, adIfPh1DayInBcastPkts=adIfPh1DayInBcastPkts, adIfPhCurInOctets1Day=adIfPhCurInOctets1Day, adIfPh1DayInMcastPkts=adIfPh1DayInMcastPkts, adIfPh1DayIntervalTable=adIfPh1DayIntervalTable, adIfPh1DayOutMcastPkts=adIfPh1DayOutMcastPkts, adIfPhCurInUcastPkts1Day=adIfPhCurInUcastPkts1Day, adIfPh15MinIntervalEntry=adIfPh15MinIntervalEntry, adIfPh15MinInUnknownProtos=adIfPh15MinInUnknownProtos, adGenAosIfPerfHistoryConformance=adGenAosIfPerfHistoryConformance, adIfPhCurTable=adIfPhCurTable, adIfPhCurInMcastPkts15Min=adIfPhCurInMcastPkts15Min, adIfPh1DayInOctets=adIfPh1DayInOctets, adIfPhCurInErrors15Min=adIfPhCurInErrors15Min, adIfPhCurValidIntervals15Min=adIfPhCurValidIntervals15Min, adIfPhCurInMcastPkts1Day=adIfPhCurInMcastPkts1Day, adIfPhCurOutUcastPkts1Day=adIfPhCurOutUcastPkts1Day, adIfPh15MinInMcastPkts=adIfPh15MinInMcastPkts, adIfPhCurOutDiscards1Day=adIfPhCurOutDiscards1Day, adIfPh1DayOutBcastPkts=adIfPh1DayOutBcastPkts, adGenAosIfPerfHistory=adGenAosIfPerfHistory, adIfPhCurInErrors1Day=adIfPhCurInErrors1Day, adIfPh15MinInUcastPkts=adIfPh15MinInUcastPkts, adIfPh1DayInUcastPkts=adIfPh1DayInUcastPkts, PYSNMP_MODULE_ID=adGenAosIfPerfHistoryMib)
