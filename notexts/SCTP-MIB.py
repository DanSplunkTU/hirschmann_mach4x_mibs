#
# PySNMP MIB module SCTP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/SCTP-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 17:49:35 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
InetAddressType, InetAddress, InetPortNumber = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress", "InetPortNumber")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
TimeTicks, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, iso, ObjectIdentity, IpAddress, Counter64, mib_2, Bits, Counter32, NotificationType, Unsigned32, Gauge32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "iso", "ObjectIdentity", "IpAddress", "Counter64", "mib-2", "Bits", "Counter32", "NotificationType", "Unsigned32", "Gauge32", "MibIdentifier")
DisplayString, TextualConvention, TimeStamp, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TimeStamp", "TruthValue")
sctpMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 104))
sctpMIB.setRevisions(('2004-09-02 00:00',))
if mibBuilder.loadTexts: sctpMIB.setLastUpdated('200409020000Z')
if mibBuilder.loadTexts: sctpMIB.setOrganization('IETF SIGTRAN Working Group')
sctpObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 104, 1))
sctpStats = MibIdentifier((1, 3, 6, 1, 2, 1, 104, 1, 1))
sctpParams = MibIdentifier((1, 3, 6, 1, 2, 1, 104, 1, 2))
sctpCurrEstab = MibScalar((1, 3, 6, 1, 2, 1, 104, 1, 1, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sctpCurrEstab.setStatus('current')
sctpActiveEstabs = MibScalar((1, 3, 6, 1, 2, 1, 104, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sctpActiveEstabs.setStatus('current')
sctpPassiveEstabs = MibScalar((1, 3, 6, 1, 2, 1, 104, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sctpPassiveEstabs.setStatus('current')
sctpAborteds = MibScalar((1, 3, 6, 1, 2, 1, 104, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sctpAborteds.setStatus('current')
sctpShutdowns = MibScalar((1, 3, 6, 1, 2, 1, 104, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sctpShutdowns.setStatus('current')
sctpOutOfBlues = MibScalar((1, 3, 6, 1, 2, 1, 104, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sctpOutOfBlues.setStatus('current')
sctpChecksumErrors = MibScalar((1, 3, 6, 1, 2, 1, 104, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sctpChecksumErrors.setStatus('current')
sctpOutCtrlChunks = MibScalar((1, 3, 6, 1, 2, 1, 104, 1, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sctpOutCtrlChunks.setStatus('current')
sctpOutOrderChunks = MibScalar((1, 3, 6, 1, 2, 1, 104, 1, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sctpOutOrderChunks.setStatus('current')
sctpOutUnorderChunks = MibScalar((1, 3, 6, 1, 2, 1, 104, 1, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sctpOutUnorderChunks.setStatus('current')
sctpInCtrlChunks = MibScalar((1, 3, 6, 1, 2, 1, 104, 1, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sctpInCtrlChunks.setStatus('current')
sctpInOrderChunks = MibScalar((1, 3, 6, 1, 2, 1, 104, 1, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sctpInOrderChunks.setStatus('current')
sctpInUnorderChunks = MibScalar((1, 3, 6, 1, 2, 1, 104, 1, 1, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sctpInUnorderChunks.setStatus('current')
sctpFragUsrMsgs = MibScalar((1, 3, 6, 1, 2, 1, 104, 1, 1, 14), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sctpFragUsrMsgs.setStatus('current')
sctpReasmUsrMsgs = MibScalar((1, 3, 6, 1, 2, 1, 104, 1, 1, 15), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sctpReasmUsrMsgs.setStatus('current')
sctpOutSCTPPacks = MibScalar((1, 3, 6, 1, 2, 1, 104, 1, 1, 16), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sctpOutSCTPPacks.setStatus('current')
sctpInSCTPPacks = MibScalar((1, 3, 6, 1, 2, 1, 104, 1, 1, 17), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sctpInSCTPPacks.setStatus('current')
sctpDiscontinuityTime = MibScalar((1, 3, 6, 1, 2, 1, 104, 1, 1, 18), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sctpDiscontinuityTime.setStatus('current')
sctpRtoAlgorithm = MibScalar((1, 3, 6, 1, 2, 1, 104, 1, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("other", 1), ("vanj", 2))).clone('vanj')).setMaxAccess("readonly")
if mibBuilder.loadTexts: sctpRtoAlgorithm.setStatus('current')
sctpRtoMin = MibScalar((1, 3, 6, 1, 2, 1, 104, 1, 2, 2), Unsigned32().clone(1000)).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: sctpRtoMin.setStatus('current')
sctpRtoMax = MibScalar((1, 3, 6, 1, 2, 1, 104, 1, 2, 3), Unsigned32().clone(60000)).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: sctpRtoMax.setStatus('current')
sctpRtoInitial = MibScalar((1, 3, 6, 1, 2, 1, 104, 1, 2, 4), Unsigned32().clone(3000)).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: sctpRtoInitial.setStatus('current')
sctpMaxAssocs = MibScalar((1, 3, 6, 1, 2, 1, 104, 1, 2, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 2147483647), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sctpMaxAssocs.setStatus('current')
sctpValCookieLife = MibScalar((1, 3, 6, 1, 2, 1, 104, 1, 2, 6), Unsigned32().clone(60000)).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: sctpValCookieLife.setStatus('current')
sctpMaxInitRetr = MibScalar((1, 3, 6, 1, 2, 1, 104, 1, 2, 7), Unsigned32().clone(8)).setMaxAccess("readonly")
if mibBuilder.loadTexts: sctpMaxInitRetr.setStatus('current')
sctpAssocTable = MibTable((1, 3, 6, 1, 2, 1, 104, 1, 3), )
if mibBuilder.loadTexts: sctpAssocTable.setStatus('current')
sctpAssocEntry = MibTableRow((1, 3, 6, 1, 2, 1, 104, 1, 3, 1), ).setIndexNames((0, "SCTP-MIB", "sctpAssocId"))
if mibBuilder.loadTexts: sctpAssocEntry.setStatus('current')
sctpAssocId = MibTableColumn((1, 3, 6, 1, 2, 1, 104, 1, 3, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: sctpAssocId.setStatus('current')
sctpAssocRemHostName = MibTableColumn((1, 3, 6, 1, 2, 1, 104, 1, 3, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sctpAssocRemHostName.setStatus('current')
sctpAssocLocalPort = MibTableColumn((1, 3, 6, 1, 2, 1, 104, 1, 3, 1, 3), InetPortNumber().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sctpAssocLocalPort.setStatus('current')
sctpAssocRemPort = MibTableColumn((1, 3, 6, 1, 2, 1, 104, 1, 3, 1, 4), InetPortNumber().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sctpAssocRemPort.setStatus('current')
sctpAssocRemPrimAddrType = MibTableColumn((1, 3, 6, 1, 2, 1, 104, 1, 3, 1, 5), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sctpAssocRemPrimAddrType.setStatus('current')
sctpAssocRemPrimAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 104, 1, 3, 1, 6), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sctpAssocRemPrimAddr.setStatus('current')
sctpAssocHeartBeatInterval = MibTableColumn((1, 3, 6, 1, 2, 1, 104, 1, 3, 1, 7), Unsigned32().clone(30000)).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: sctpAssocHeartBeatInterval.setStatus('current')
sctpAssocState = MibTableColumn((1, 3, 6, 1, 2, 1, 104, 1, 3, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("closed", 1), ("cookieWait", 2), ("cookieEchoed", 3), ("established", 4), ("shutdownPending", 5), ("shutdownSent", 6), ("shutdownReceived", 7), ("shutdownAckSent", 8), ("deleteTCB", 9)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sctpAssocState.setStatus('current')
sctpAssocInStreams = MibTableColumn((1, 3, 6, 1, 2, 1, 104, 1, 3, 1, 9), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sctpAssocInStreams.setStatus('current')
sctpAssocOutStreams = MibTableColumn((1, 3, 6, 1, 2, 1, 104, 1, 3, 1, 10), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sctpAssocOutStreams.setStatus('current')
sctpAssocMaxRetr = MibTableColumn((1, 3, 6, 1, 2, 1, 104, 1, 3, 1, 11), Unsigned32().clone(10)).setMaxAccess("readonly")
if mibBuilder.loadTexts: sctpAssocMaxRetr.setStatus('current')
sctpAssocPrimProcess = MibTableColumn((1, 3, 6, 1, 2, 1, 104, 1, 3, 1, 12), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sctpAssocPrimProcess.setStatus('current')
sctpAssocT1expireds = MibTableColumn((1, 3, 6, 1, 2, 1, 104, 1, 3, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sctpAssocT1expireds.setStatus('current')
sctpAssocT2expireds = MibTableColumn((1, 3, 6, 1, 2, 1, 104, 1, 3, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sctpAssocT2expireds.setStatus('current')
sctpAssocRtxChunks = MibTableColumn((1, 3, 6, 1, 2, 1, 104, 1, 3, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sctpAssocRtxChunks.setStatus('current')
sctpAssocStartTime = MibTableColumn((1, 3, 6, 1, 2, 1, 104, 1, 3, 1, 16), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sctpAssocStartTime.setStatus('current')
sctpAssocDiscontinuityTime = MibTableColumn((1, 3, 6, 1, 2, 1, 104, 1, 3, 1, 17), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sctpAssocDiscontinuityTime.setStatus('current')
sctpAssocLocalAddrTable = MibTable((1, 3, 6, 1, 2, 1, 104, 1, 4), )
if mibBuilder.loadTexts: sctpAssocLocalAddrTable.setStatus('current')
sctpAssocLocalAddrEntry = MibTableRow((1, 3, 6, 1, 2, 1, 104, 1, 4, 1), ).setIndexNames((0, "SCTP-MIB", "sctpAssocId"), (0, "SCTP-MIB", "sctpAssocLocalAddrType"), (0, "SCTP-MIB", "sctpAssocLocalAddr"))
if mibBuilder.loadTexts: sctpAssocLocalAddrEntry.setStatus('current')
sctpAssocLocalAddrType = MibTableColumn((1, 3, 6, 1, 2, 1, 104, 1, 4, 1, 1), InetAddressType())
if mibBuilder.loadTexts: sctpAssocLocalAddrType.setStatus('current')
sctpAssocLocalAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 104, 1, 4, 1, 2), InetAddress())
if mibBuilder.loadTexts: sctpAssocLocalAddr.setStatus('current')
sctpAssocLocalAddrStartTime = MibTableColumn((1, 3, 6, 1, 2, 1, 104, 1, 4, 1, 3), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sctpAssocLocalAddrStartTime.setStatus('current')
sctpAssocRemAddrTable = MibTable((1, 3, 6, 1, 2, 1, 104, 1, 5), )
if mibBuilder.loadTexts: sctpAssocRemAddrTable.setStatus('current')
sctpAssocRemAddrEntry = MibTableRow((1, 3, 6, 1, 2, 1, 104, 1, 5, 1), ).setIndexNames((0, "SCTP-MIB", "sctpAssocId"), (0, "SCTP-MIB", "sctpAssocRemAddrType"), (0, "SCTP-MIB", "sctpAssocRemAddr"))
if mibBuilder.loadTexts: sctpAssocRemAddrEntry.setStatus('current')
sctpAssocRemAddrType = MibTableColumn((1, 3, 6, 1, 2, 1, 104, 1, 5, 1, 1), InetAddressType())
if mibBuilder.loadTexts: sctpAssocRemAddrType.setStatus('current')
sctpAssocRemAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 104, 1, 5, 1, 2), InetAddress())
if mibBuilder.loadTexts: sctpAssocRemAddr.setStatus('current')
sctpAssocRemAddrActive = MibTableColumn((1, 3, 6, 1, 2, 1, 104, 1, 5, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sctpAssocRemAddrActive.setStatus('current')
sctpAssocRemAddrHBActive = MibTableColumn((1, 3, 6, 1, 2, 1, 104, 1, 5, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sctpAssocRemAddrHBActive.setStatus('current')
sctpAssocRemAddrRTO = MibTableColumn((1, 3, 6, 1, 2, 1, 104, 1, 5, 1, 5), Unsigned32()).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: sctpAssocRemAddrRTO.setStatus('current')
sctpAssocRemAddrMaxPathRtx = MibTableColumn((1, 3, 6, 1, 2, 1, 104, 1, 5, 1, 6), Unsigned32().clone(5)).setMaxAccess("readonly")
if mibBuilder.loadTexts: sctpAssocRemAddrMaxPathRtx.setStatus('current')
sctpAssocRemAddrRtx = MibTableColumn((1, 3, 6, 1, 2, 1, 104, 1, 5, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sctpAssocRemAddrRtx.setStatus('current')
sctpAssocRemAddrStartTime = MibTableColumn((1, 3, 6, 1, 2, 1, 104, 1, 5, 1, 8), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sctpAssocRemAddrStartTime.setStatus('current')
sctpLookupLocalPortTable = MibTable((1, 3, 6, 1, 2, 1, 104, 1, 6), )
if mibBuilder.loadTexts: sctpLookupLocalPortTable.setStatus('current')
sctpLookupLocalPortEntry = MibTableRow((1, 3, 6, 1, 2, 1, 104, 1, 6, 1), ).setIndexNames((0, "SCTP-MIB", "sctpAssocLocalPort"), (0, "SCTP-MIB", "sctpAssocId"))
if mibBuilder.loadTexts: sctpLookupLocalPortEntry.setStatus('current')
sctpLookupLocalPortStartTime = MibTableColumn((1, 3, 6, 1, 2, 1, 104, 1, 6, 1, 1), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sctpLookupLocalPortStartTime.setStatus('current')
sctpLookupRemPortTable = MibTable((1, 3, 6, 1, 2, 1, 104, 1, 7), )
if mibBuilder.loadTexts: sctpLookupRemPortTable.setStatus('current')
sctpLookupRemPortEntry = MibTableRow((1, 3, 6, 1, 2, 1, 104, 1, 7, 1), ).setIndexNames((0, "SCTP-MIB", "sctpAssocRemPort"), (0, "SCTP-MIB", "sctpAssocId"))
if mibBuilder.loadTexts: sctpLookupRemPortEntry.setStatus('current')
sctpLookupRemPortStartTime = MibTableColumn((1, 3, 6, 1, 2, 1, 104, 1, 7, 1, 1), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sctpLookupRemPortStartTime.setStatus('current')
sctpLookupRemHostNameTable = MibTable((1, 3, 6, 1, 2, 1, 104, 1, 8), )
if mibBuilder.loadTexts: sctpLookupRemHostNameTable.setStatus('current')
sctpLookupRemHostNameEntry = MibTableRow((1, 3, 6, 1, 2, 1, 104, 1, 8, 1), ).setIndexNames((0, "SCTP-MIB", "sctpAssocRemHostName"), (0, "SCTP-MIB", "sctpAssocId"))
if mibBuilder.loadTexts: sctpLookupRemHostNameEntry.setStatus('current')
sctpLookupRemHostNameStartTime = MibTableColumn((1, 3, 6, 1, 2, 1, 104, 1, 8, 1, 1), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sctpLookupRemHostNameStartTime.setStatus('current')
sctpLookupRemPrimIPAddrTable = MibTable((1, 3, 6, 1, 2, 1, 104, 1, 9), )
if mibBuilder.loadTexts: sctpLookupRemPrimIPAddrTable.setStatus('current')
sctpLookupRemPrimIPAddrEntry = MibTableRow((1, 3, 6, 1, 2, 1, 104, 1, 9, 1), ).setIndexNames((0, "SCTP-MIB", "sctpAssocRemPrimAddrType"), (0, "SCTP-MIB", "sctpAssocRemPrimAddr"), (0, "SCTP-MIB", "sctpAssocId"))
if mibBuilder.loadTexts: sctpLookupRemPrimIPAddrEntry.setStatus('current')
sctpLookupRemPrimIPAddrStartTime = MibTableColumn((1, 3, 6, 1, 2, 1, 104, 1, 9, 1, 1), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sctpLookupRemPrimIPAddrStartTime.setStatus('current')
sctpLookupRemIPAddrTable = MibTable((1, 3, 6, 1, 2, 1, 104, 1, 10), )
if mibBuilder.loadTexts: sctpLookupRemIPAddrTable.setStatus('current')
sctpLookupRemIPAddrEntry = MibTableRow((1, 3, 6, 1, 2, 1, 104, 1, 10, 1), ).setIndexNames((0, "SCTP-MIB", "sctpAssocRemAddrType"), (0, "SCTP-MIB", "sctpAssocRemAddr"), (0, "SCTP-MIB", "sctpAssocId"))
if mibBuilder.loadTexts: sctpLookupRemIPAddrEntry.setStatus('current')
sctpLookupRemIPAddrStartTime = MibTableColumn((1, 3, 6, 1, 2, 1, 104, 1, 10, 1, 1), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sctpLookupRemIPAddrStartTime.setStatus('current')
sctpMibConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 104, 2))
sctpMibCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 104, 2, 1))
sctpMibGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 104, 2, 2))
sctpLayerParamsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 104, 2, 2, 1)).setObjects(("SCTP-MIB", "sctpRtoAlgorithm"), ("SCTP-MIB", "sctpRtoMin"), ("SCTP-MIB", "sctpRtoMax"), ("SCTP-MIB", "sctpRtoInitial"), ("SCTP-MIB", "sctpMaxAssocs"), ("SCTP-MIB", "sctpValCookieLife"), ("SCTP-MIB", "sctpMaxInitRetr"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sctpLayerParamsGroup = sctpLayerParamsGroup.setStatus('current')
sctpStatsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 104, 2, 2, 2)).setObjects(("SCTP-MIB", "sctpCurrEstab"), ("SCTP-MIB", "sctpActiveEstabs"), ("SCTP-MIB", "sctpPassiveEstabs"), ("SCTP-MIB", "sctpAborteds"), ("SCTP-MIB", "sctpShutdowns"), ("SCTP-MIB", "sctpOutOfBlues"), ("SCTP-MIB", "sctpChecksumErrors"), ("SCTP-MIB", "sctpOutCtrlChunks"), ("SCTP-MIB", "sctpOutOrderChunks"), ("SCTP-MIB", "sctpOutUnorderChunks"), ("SCTP-MIB", "sctpInCtrlChunks"), ("SCTP-MIB", "sctpInOrderChunks"), ("SCTP-MIB", "sctpInUnorderChunks"), ("SCTP-MIB", "sctpFragUsrMsgs"), ("SCTP-MIB", "sctpReasmUsrMsgs"), ("SCTP-MIB", "sctpOutSCTPPacks"), ("SCTP-MIB", "sctpInSCTPPacks"), ("SCTP-MIB", "sctpDiscontinuityTime"), ("SCTP-MIB", "sctpAssocT1expireds"), ("SCTP-MIB", "sctpAssocT2expireds"), ("SCTP-MIB", "sctpAssocRtxChunks"), ("SCTP-MIB", "sctpAssocRemAddrRtx"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sctpStatsGroup = sctpStatsGroup.setStatus('current')
sctpPerAssocParamsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 104, 2, 2, 3)).setObjects(("SCTP-MIB", "sctpAssocRemHostName"), ("SCTP-MIB", "sctpAssocLocalPort"), ("SCTP-MIB", "sctpAssocRemPort"), ("SCTP-MIB", "sctpAssocRemPrimAddrType"), ("SCTP-MIB", "sctpAssocRemPrimAddr"), ("SCTP-MIB", "sctpAssocHeartBeatInterval"), ("SCTP-MIB", "sctpAssocState"), ("SCTP-MIB", "sctpAssocInStreams"), ("SCTP-MIB", "sctpAssocOutStreams"), ("SCTP-MIB", "sctpAssocMaxRetr"), ("SCTP-MIB", "sctpAssocPrimProcess"), ("SCTP-MIB", "sctpAssocStartTime"), ("SCTP-MIB", "sctpAssocDiscontinuityTime"), ("SCTP-MIB", "sctpAssocLocalAddrStartTime"), ("SCTP-MIB", "sctpAssocRemAddrActive"), ("SCTP-MIB", "sctpAssocRemAddrHBActive"), ("SCTP-MIB", "sctpAssocRemAddrRTO"), ("SCTP-MIB", "sctpAssocRemAddrMaxPathRtx"), ("SCTP-MIB", "sctpAssocRemAddrStartTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sctpPerAssocParamsGroup = sctpPerAssocParamsGroup.setStatus('current')
sctpPerAssocStatsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 104, 2, 2, 4)).setObjects(("SCTP-MIB", "sctpAssocT1expireds"), ("SCTP-MIB", "sctpAssocT2expireds"), ("SCTP-MIB", "sctpAssocRtxChunks"), ("SCTP-MIB", "sctpAssocRemAddrRtx"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sctpPerAssocStatsGroup = sctpPerAssocStatsGroup.setStatus('current')
sctpInverseGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 104, 2, 2, 5)).setObjects(("SCTP-MIB", "sctpLookupLocalPortStartTime"), ("SCTP-MIB", "sctpLookupRemPortStartTime"), ("SCTP-MIB", "sctpLookupRemHostNameStartTime"), ("SCTP-MIB", "sctpLookupRemPrimIPAddrStartTime"), ("SCTP-MIB", "sctpLookupRemIPAddrStartTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sctpInverseGroup = sctpInverseGroup.setStatus('current')
sctpMibCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 104, 2, 1, 1)).setObjects(("SCTP-MIB", "sctpLayerParamsGroup"), ("SCTP-MIB", "sctpPerAssocParamsGroup"), ("SCTP-MIB", "sctpStatsGroup"), ("SCTP-MIB", "sctpPerAssocStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sctpMibCompliance = sctpMibCompliance.setStatus('current')
mibBuilder.exportSymbols("SCTP-MIB", sctpAssocRtxChunks=sctpAssocRtxChunks, sctpLookupRemPortStartTime=sctpLookupRemPortStartTime, sctpActiveEstabs=sctpActiveEstabs, sctpAborteds=sctpAborteds, sctpShutdowns=sctpShutdowns, sctpAssocLocalAddrType=sctpAssocLocalAddrType, sctpAssocRemAddrType=sctpAssocRemAddrType, sctpValCookieLife=sctpValCookieLife, sctpPerAssocStatsGroup=sctpPerAssocStatsGroup, sctpAssocInStreams=sctpAssocInStreams, sctpAssocRemAddrHBActive=sctpAssocRemAddrHBActive, sctpStats=sctpStats, sctpLookupRemHostNameStartTime=sctpLookupRemHostNameStartTime, sctpOutUnorderChunks=sctpOutUnorderChunks, sctpAssocHeartBeatInterval=sctpAssocHeartBeatInterval, sctpAssocRemPrimAddrType=sctpAssocRemPrimAddrType, sctpAssocEntry=sctpAssocEntry, sctpInCtrlChunks=sctpInCtrlChunks, sctpAssocRemAddrEntry=sctpAssocRemAddrEntry, sctpAssocT1expireds=sctpAssocT1expireds, sctpLookupRemIPAddrEntry=sctpLookupRemIPAddrEntry, sctpAssocDiscontinuityTime=sctpAssocDiscontinuityTime, sctpLookupRemPrimIPAddrStartTime=sctpLookupRemPrimIPAddrStartTime, sctpInOrderChunks=sctpInOrderChunks, sctpRtoMin=sctpRtoMin, sctpMaxAssocs=sctpMaxAssocs, sctpAssocId=sctpAssocId, sctpLookupRemPrimIPAddrEntry=sctpLookupRemPrimIPAddrEntry, sctpInUnorderChunks=sctpInUnorderChunks, sctpReasmUsrMsgs=sctpReasmUsrMsgs, sctpRtoAlgorithm=sctpRtoAlgorithm, sctpAssocLocalAddrStartTime=sctpAssocLocalAddrStartTime, sctpLookupRemPortEntry=sctpLookupRemPortEntry, sctpAssocLocalPort=sctpAssocLocalPort, sctpMaxInitRetr=sctpMaxInitRetr, sctpRtoMax=sctpRtoMax, sctpLookupLocalPortStartTime=sctpLookupLocalPortStartTime, sctpAssocRemAddrRtx=sctpAssocRemAddrRtx, sctpAssocRemAddrActive=sctpAssocRemAddrActive, sctpAssocT2expireds=sctpAssocT2expireds, sctpLookupRemHostNameEntry=sctpLookupRemHostNameEntry, sctpAssocMaxRetr=sctpAssocMaxRetr, sctpLookupLocalPortEntry=sctpLookupLocalPortEntry, sctpPassiveEstabs=sctpPassiveEstabs, sctpOutOfBlues=sctpOutOfBlues, PYSNMP_MODULE_ID=sctpMIB, sctpPerAssocParamsGroup=sctpPerAssocParamsGroup, sctpOutOrderChunks=sctpOutOrderChunks, sctpAssocLocalAddrEntry=sctpAssocLocalAddrEntry, sctpLookupRemIPAddrStartTime=sctpLookupRemIPAddrStartTime, sctpAssocRemAddrTable=sctpAssocRemAddrTable, sctpLookupLocalPortTable=sctpLookupLocalPortTable, sctpAssocRemPort=sctpAssocRemPort, sctpStatsGroup=sctpStatsGroup, sctpDiscontinuityTime=sctpDiscontinuityTime, sctpAssocTable=sctpAssocTable, sctpAssocOutStreams=sctpAssocOutStreams, sctpAssocRemAddr=sctpAssocRemAddr, sctpAssocRemAddrStartTime=sctpAssocRemAddrStartTime, sctpAssocRemHostName=sctpAssocRemHostName, sctpCurrEstab=sctpCurrEstab, sctpLookupRemIPAddrTable=sctpLookupRemIPAddrTable, sctpChecksumErrors=sctpChecksumErrors, sctpAssocRemAddrMaxPathRtx=sctpAssocRemAddrMaxPathRtx, sctpAssocRemAddrRTO=sctpAssocRemAddrRTO, sctpFragUsrMsgs=sctpFragUsrMsgs, sctpOutSCTPPacks=sctpOutSCTPPacks, sctpAssocLocalAddr=sctpAssocLocalAddr, sctpLookupRemHostNameTable=sctpLookupRemHostNameTable, sctpAssocPrimProcess=sctpAssocPrimProcess, sctpLookupRemPrimIPAddrTable=sctpLookupRemPrimIPAddrTable, sctpAssocLocalAddrTable=sctpAssocLocalAddrTable, sctpParams=sctpParams, sctpMibConformance=sctpMibConformance, sctpRtoInitial=sctpRtoInitial, sctpMibCompliance=sctpMibCompliance, sctpAssocState=sctpAssocState, sctpObjects=sctpObjects, sctpMibCompliances=sctpMibCompliances, sctpMibGroups=sctpMibGroups, sctpLookupRemPortTable=sctpLookupRemPortTable, sctpOutCtrlChunks=sctpOutCtrlChunks, sctpAssocStartTime=sctpAssocStartTime, sctpInverseGroup=sctpInverseGroup, sctpInSCTPPacks=sctpInSCTPPacks, sctpAssocRemPrimAddr=sctpAssocRemPrimAddr, sctpLayerParamsGroup=sctpLayerParamsGroup, sctpMIB=sctpMIB)
