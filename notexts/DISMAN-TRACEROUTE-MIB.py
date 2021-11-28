#
# PySNMP MIB module DISMAN-TRACEROUTE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/DISMAN-TRACEROUTE-MIB
# Produced by pysmi-1.1.3 at Sun Nov 28 20:09:00 2021
# On host fv-az77-612 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
OperationResponseStatus, = mibBuilder.importSymbols("DISMAN-PING-MIB", "OperationResponseStatus")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, ObjectIdentity, iso, Counter64, Gauge32, mib_2, Counter32, MibIdentifier, Unsigned32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "ObjectIdentity", "iso", "Counter64", "Gauge32", "mib-2", "Counter32", "MibIdentifier", "Unsigned32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Bits", "TimeTicks", "IpAddress")
RowStatus, TruthValue, DisplayString, StorageType, TextualConvention, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TruthValue", "DisplayString", "StorageType", "TextualConvention", "DateAndTime")
traceRouteMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 81))
traceRouteMIB.setRevisions(('2006-06-13 00:00', '2000-09-21 00:00',))
if mibBuilder.loadTexts: traceRouteMIB.setLastUpdated('200606130000Z')
if mibBuilder.loadTexts: traceRouteMIB.setOrganization('IETF Distributed Management Working Group')
traceRouteNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 81, 0))
traceRouteObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 81, 1))
traceRouteConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 81, 2))
traceRouteImplementationTypeDomains = MibIdentifier((1, 3, 6, 1, 2, 1, 81, 3))
traceRouteUsingUdpProbes = ObjectIdentity((1, 3, 6, 1, 2, 1, 81, 3, 1))
if mibBuilder.loadTexts: traceRouteUsingUdpProbes.setStatus('current')
traceRouteMaxConcurrentRequests = MibScalar((1, 3, 6, 1, 2, 1, 81, 1, 1), Unsigned32().clone(10)).setUnits('requests').setMaxAccess("readwrite")
if mibBuilder.loadTexts: traceRouteMaxConcurrentRequests.setStatus('current')
traceRouteCtlTable = MibTable((1, 3, 6, 1, 2, 1, 81, 1, 2), )
if mibBuilder.loadTexts: traceRouteCtlTable.setStatus('current')
traceRouteCtlEntry = MibTableRow((1, 3, 6, 1, 2, 1, 81, 1, 2, 1), ).setIndexNames((0, "DISMAN-TRACEROUTE-MIB", "traceRouteCtlOwnerIndex"), (0, "DISMAN-TRACEROUTE-MIB", "traceRouteCtlTestName"))
if mibBuilder.loadTexts: traceRouteCtlEntry.setStatus('current')
traceRouteCtlOwnerIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 81, 1, 2, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32)))
if mibBuilder.loadTexts: traceRouteCtlOwnerIndex.setStatus('current')
traceRouteCtlTestName = MibTableColumn((1, 3, 6, 1, 2, 1, 81, 1, 2, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32)))
if mibBuilder.loadTexts: traceRouteCtlTestName.setStatus('current')
traceRouteCtlTargetAddressType = MibTableColumn((1, 3, 6, 1, 2, 1, 81, 1, 2, 1, 3), InetAddressType().clone('unknown')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: traceRouteCtlTargetAddressType.setStatus('current')
traceRouteCtlTargetAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 81, 1, 2, 1, 4), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: traceRouteCtlTargetAddress.setStatus('current')
traceRouteCtlByPassRouteTable = MibTableColumn((1, 3, 6, 1, 2, 1, 81, 1, 2, 1, 5), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: traceRouteCtlByPassRouteTable.setStatus('current')
traceRouteCtlDataSize = MibTableColumn((1, 3, 6, 1, 2, 1, 81, 1, 2, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65507))).setUnits('octets').setMaxAccess("readcreate")
if mibBuilder.loadTexts: traceRouteCtlDataSize.setStatus('current')
traceRouteCtlTimeOut = MibTableColumn((1, 3, 6, 1, 2, 1, 81, 1, 2, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 60)).clone(3)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: traceRouteCtlTimeOut.setStatus('current')
traceRouteCtlProbesPerHop = MibTableColumn((1, 3, 6, 1, 2, 1, 81, 1, 2, 1, 8), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 10)).clone(3)).setUnits('probes').setMaxAccess("readcreate")
if mibBuilder.loadTexts: traceRouteCtlProbesPerHop.setStatus('current')
traceRouteCtlPort = MibTableColumn((1, 3, 6, 1, 2, 1, 81, 1, 2, 1, 9), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(33434)).setUnits('UDP Port').setMaxAccess("readcreate")
if mibBuilder.loadTexts: traceRouteCtlPort.setStatus('current')
traceRouteCtlMaxTtl = MibTableColumn((1, 3, 6, 1, 2, 1, 81, 1, 2, 1, 10), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)).clone(30)).setUnits('time-to-live value').setMaxAccess("readcreate")
if mibBuilder.loadTexts: traceRouteCtlMaxTtl.setStatus('current')
traceRouteCtlDSField = MibTableColumn((1, 3, 6, 1, 2, 1, 81, 1, 2, 1, 11), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: traceRouteCtlDSField.setStatus('current')
traceRouteCtlSourceAddressType = MibTableColumn((1, 3, 6, 1, 2, 1, 81, 1, 2, 1, 12), InetAddressType().clone('unknown')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: traceRouteCtlSourceAddressType.setStatus('current')
traceRouteCtlSourceAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 81, 1, 2, 1, 13), InetAddress().clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: traceRouteCtlSourceAddress.setStatus('current')
traceRouteCtlIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 81, 1, 2, 1, 14), InterfaceIndexOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: traceRouteCtlIfIndex.setStatus('current')
traceRouteCtlMiscOptions = MibTableColumn((1, 3, 6, 1, 2, 1, 81, 1, 2, 1, 15), SnmpAdminString().clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: traceRouteCtlMiscOptions.setStatus('current')
traceRouteCtlMaxFailures = MibTableColumn((1, 3, 6, 1, 2, 1, 81, 1, 2, 1, 16), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)).clone(5)).setUnits('timeouts').setMaxAccess("readcreate")
if mibBuilder.loadTexts: traceRouteCtlMaxFailures.setStatus('current')
traceRouteCtlDontFragment = MibTableColumn((1, 3, 6, 1, 2, 1, 81, 1, 2, 1, 17), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: traceRouteCtlDontFragment.setStatus('current')
traceRouteCtlInitialTtl = MibTableColumn((1, 3, 6, 1, 2, 1, 81, 1, 2, 1, 18), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: traceRouteCtlInitialTtl.setStatus('current')
traceRouteCtlFrequency = MibTableColumn((1, 3, 6, 1, 2, 1, 81, 1, 2, 1, 19), Unsigned32()).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: traceRouteCtlFrequency.setStatus('current')
traceRouteCtlStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 81, 1, 2, 1, 20), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: traceRouteCtlStorageType.setStatus('current')
traceRouteCtlAdminStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 81, 1, 2, 1, 21), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: traceRouteCtlAdminStatus.setStatus('current')
traceRouteCtlDescr = MibTableColumn((1, 3, 6, 1, 2, 1, 81, 1, 2, 1, 22), SnmpAdminString().clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: traceRouteCtlDescr.setStatus('current')
traceRouteCtlMaxRows = MibTableColumn((1, 3, 6, 1, 2, 1, 81, 1, 2, 1, 23), Unsigned32().clone(50)).setUnits('rows').setMaxAccess("readcreate")
if mibBuilder.loadTexts: traceRouteCtlMaxRows.setStatus('current')
traceRouteCtlTrapGeneration = MibTableColumn((1, 3, 6, 1, 2, 1, 81, 1, 2, 1, 24), Bits().clone(namedValues=NamedValues(("pathChange", 0), ("testFailure", 1), ("testCompletion", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: traceRouteCtlTrapGeneration.setStatus('current')
traceRouteCtlCreateHopsEntries = MibTableColumn((1, 3, 6, 1, 2, 1, 81, 1, 2, 1, 25), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: traceRouteCtlCreateHopsEntries.setStatus('current')
traceRouteCtlType = MibTableColumn((1, 3, 6, 1, 2, 1, 81, 1, 2, 1, 26), ObjectIdentifier().clone((1, 3, 6, 1, 2, 1, 81, 3, 1))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: traceRouteCtlType.setStatus('current')
traceRouteCtlRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 81, 1, 2, 1, 27), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: traceRouteCtlRowStatus.setStatus('current')
traceRouteResultsTable = MibTable((1, 3, 6, 1, 2, 1, 81, 1, 3), )
if mibBuilder.loadTexts: traceRouteResultsTable.setStatus('current')
traceRouteResultsEntry = MibTableRow((1, 3, 6, 1, 2, 1, 81, 1, 3, 1), ).setIndexNames((0, "DISMAN-TRACEROUTE-MIB", "traceRouteCtlOwnerIndex"), (0, "DISMAN-TRACEROUTE-MIB", "traceRouteCtlTestName"))
if mibBuilder.loadTexts: traceRouteResultsEntry.setStatus('current')
traceRouteResultsOperStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 81, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ("completed", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: traceRouteResultsOperStatus.setStatus('current')
traceRouteResultsCurHopCount = MibTableColumn((1, 3, 6, 1, 2, 1, 81, 1, 3, 1, 2), Gauge32()).setUnits('hops').setMaxAccess("readonly")
if mibBuilder.loadTexts: traceRouteResultsCurHopCount.setStatus('current')
traceRouteResultsCurProbeCount = MibTableColumn((1, 3, 6, 1, 2, 1, 81, 1, 3, 1, 3), Gauge32()).setUnits('probes').setMaxAccess("readonly")
if mibBuilder.loadTexts: traceRouteResultsCurProbeCount.setStatus('current')
traceRouteResultsIpTgtAddrType = MibTableColumn((1, 3, 6, 1, 2, 1, 81, 1, 3, 1, 4), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: traceRouteResultsIpTgtAddrType.setStatus('current')
traceRouteResultsIpTgtAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 81, 1, 3, 1, 5), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: traceRouteResultsIpTgtAddr.setStatus('current')
traceRouteResultsTestAttempts = MibTableColumn((1, 3, 6, 1, 2, 1, 81, 1, 3, 1, 6), Gauge32()).setUnits('tests').setMaxAccess("readonly")
if mibBuilder.loadTexts: traceRouteResultsTestAttempts.setStatus('current')
traceRouteResultsTestSuccesses = MibTableColumn((1, 3, 6, 1, 2, 1, 81, 1, 3, 1, 7), Gauge32()).setUnits('tests').setMaxAccess("readonly")
if mibBuilder.loadTexts: traceRouteResultsTestSuccesses.setStatus('current')
traceRouteResultsLastGoodPath = MibTableColumn((1, 3, 6, 1, 2, 1, 81, 1, 3, 1, 8), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: traceRouteResultsLastGoodPath.setStatus('current')
traceRouteProbeHistoryTable = MibTable((1, 3, 6, 1, 2, 1, 81, 1, 4), )
if mibBuilder.loadTexts: traceRouteProbeHistoryTable.setStatus('current')
traceRouteProbeHistoryEntry = MibTableRow((1, 3, 6, 1, 2, 1, 81, 1, 4, 1), ).setIndexNames((0, "DISMAN-TRACEROUTE-MIB", "traceRouteCtlOwnerIndex"), (0, "DISMAN-TRACEROUTE-MIB", "traceRouteCtlTestName"), (0, "DISMAN-TRACEROUTE-MIB", "traceRouteProbeHistoryIndex"), (0, "DISMAN-TRACEROUTE-MIB", "traceRouteProbeHistoryHopIndex"), (0, "DISMAN-TRACEROUTE-MIB", "traceRouteProbeHistoryProbeIndex"))
if mibBuilder.loadTexts: traceRouteProbeHistoryEntry.setStatus('current')
traceRouteProbeHistoryIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 81, 1, 4, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: traceRouteProbeHistoryIndex.setStatus('current')
traceRouteProbeHistoryHopIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 81, 1, 4, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)))
if mibBuilder.loadTexts: traceRouteProbeHistoryHopIndex.setStatus('current')
traceRouteProbeHistoryProbeIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 81, 1, 4, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 10)))
if mibBuilder.loadTexts: traceRouteProbeHistoryProbeIndex.setStatus('current')
traceRouteProbeHistoryHAddrType = MibTableColumn((1, 3, 6, 1, 2, 1, 81, 1, 4, 1, 4), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: traceRouteProbeHistoryHAddrType.setStatus('current')
traceRouteProbeHistoryHAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 81, 1, 4, 1, 5), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: traceRouteProbeHistoryHAddr.setStatus('current')
traceRouteProbeHistoryResponse = MibTableColumn((1, 3, 6, 1, 2, 1, 81, 1, 4, 1, 6), Unsigned32()).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: traceRouteProbeHistoryResponse.setStatus('current')
traceRouteProbeHistoryStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 81, 1, 4, 1, 7), OperationResponseStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: traceRouteProbeHistoryStatus.setStatus('current')
traceRouteProbeHistoryLastRC = MibTableColumn((1, 3, 6, 1, 2, 1, 81, 1, 4, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: traceRouteProbeHistoryLastRC.setStatus('current')
traceRouteProbeHistoryTime = MibTableColumn((1, 3, 6, 1, 2, 1, 81, 1, 4, 1, 9), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: traceRouteProbeHistoryTime.setStatus('current')
traceRouteHopsTable = MibTable((1, 3, 6, 1, 2, 1, 81, 1, 5), )
if mibBuilder.loadTexts: traceRouteHopsTable.setStatus('current')
traceRouteHopsEntry = MibTableRow((1, 3, 6, 1, 2, 1, 81, 1, 5, 1), ).setIndexNames((0, "DISMAN-TRACEROUTE-MIB", "traceRouteCtlOwnerIndex"), (0, "DISMAN-TRACEROUTE-MIB", "traceRouteCtlTestName"), (0, "DISMAN-TRACEROUTE-MIB", "traceRouteHopsHopIndex"))
if mibBuilder.loadTexts: traceRouteHopsEntry.setStatus('current')
traceRouteHopsHopIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 81, 1, 5, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: traceRouteHopsHopIndex.setStatus('current')
traceRouteHopsIpTgtAddressType = MibTableColumn((1, 3, 6, 1, 2, 1, 81, 1, 5, 1, 2), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: traceRouteHopsIpTgtAddressType.setStatus('current')
traceRouteHopsIpTgtAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 81, 1, 5, 1, 3), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: traceRouteHopsIpTgtAddress.setStatus('current')
traceRouteHopsMinRtt = MibTableColumn((1, 3, 6, 1, 2, 1, 81, 1, 5, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: traceRouteHopsMinRtt.setStatus('current')
traceRouteHopsMaxRtt = MibTableColumn((1, 3, 6, 1, 2, 1, 81, 1, 5, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: traceRouteHopsMaxRtt.setStatus('current')
traceRouteHopsAverageRtt = MibTableColumn((1, 3, 6, 1, 2, 1, 81, 1, 5, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: traceRouteHopsAverageRtt.setStatus('current')
traceRouteHopsRttSumOfSquares = MibTableColumn((1, 3, 6, 1, 2, 1, 81, 1, 5, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: traceRouteHopsRttSumOfSquares.setStatus('current')
traceRouteHopsSentProbes = MibTableColumn((1, 3, 6, 1, 2, 1, 81, 1, 5, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: traceRouteHopsSentProbes.setStatus('current')
traceRouteHopsProbeResponses = MibTableColumn((1, 3, 6, 1, 2, 1, 81, 1, 5, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: traceRouteHopsProbeResponses.setStatus('current')
traceRouteHopsLastGoodProbe = MibTableColumn((1, 3, 6, 1, 2, 1, 81, 1, 5, 1, 10), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: traceRouteHopsLastGoodProbe.setStatus('current')
traceRoutePathChange = NotificationType((1, 3, 6, 1, 2, 1, 81, 0, 1)).setObjects(("DISMAN-TRACEROUTE-MIB", "traceRouteCtlTargetAddressType"), ("DISMAN-TRACEROUTE-MIB", "traceRouteCtlTargetAddress"), ("DISMAN-TRACEROUTE-MIB", "traceRouteResultsIpTgtAddrType"), ("DISMAN-TRACEROUTE-MIB", "traceRouteResultsIpTgtAddr"))
if mibBuilder.loadTexts: traceRoutePathChange.setStatus('current')
traceRouteTestFailed = NotificationType((1, 3, 6, 1, 2, 1, 81, 0, 2)).setObjects(("DISMAN-TRACEROUTE-MIB", "traceRouteCtlTargetAddressType"), ("DISMAN-TRACEROUTE-MIB", "traceRouteCtlTargetAddress"), ("DISMAN-TRACEROUTE-MIB", "traceRouteResultsIpTgtAddrType"), ("DISMAN-TRACEROUTE-MIB", "traceRouteResultsIpTgtAddr"))
if mibBuilder.loadTexts: traceRouteTestFailed.setStatus('current')
traceRouteTestCompleted = NotificationType((1, 3, 6, 1, 2, 1, 81, 0, 3)).setObjects(("DISMAN-TRACEROUTE-MIB", "traceRouteCtlTargetAddressType"), ("DISMAN-TRACEROUTE-MIB", "traceRouteCtlTargetAddress"), ("DISMAN-TRACEROUTE-MIB", "traceRouteResultsIpTgtAddrType"), ("DISMAN-TRACEROUTE-MIB", "traceRouteResultsIpTgtAddr"))
if mibBuilder.loadTexts: traceRouteTestCompleted.setStatus('current')
traceRouteCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 81, 2, 1))
traceRouteGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 81, 2, 2))
traceRouteFullCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 81, 2, 1, 2)).setObjects(("DISMAN-TRACEROUTE-MIB", "traceRouteMinimumGroup"), ("DISMAN-TRACEROUTE-MIB", "traceRouteCtlRowStatusGroup"), ("DISMAN-TRACEROUTE-MIB", "traceRouteHistoryGroup"), ("DISMAN-TRACEROUTE-MIB", "traceRouteHopsTableGroup"), ("DISMAN-TRACEROUTE-MIB", "traceRouteNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    traceRouteFullCompliance = traceRouteFullCompliance.setStatus('current')
traceRouteMinimumCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 81, 2, 1, 3)).setObjects(("DISMAN-TRACEROUTE-MIB", "traceRouteMinimumGroup"), ("DISMAN-TRACEROUTE-MIB", "traceRouteCtlRowStatusGroup"), ("DISMAN-TRACEROUTE-MIB", "traceRouteHistoryGroup"), ("DISMAN-TRACEROUTE-MIB", "traceRouteHopsTableGroup"), ("DISMAN-TRACEROUTE-MIB", "traceRouteNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    traceRouteMinimumCompliance = traceRouteMinimumCompliance.setStatus('current')
traceRouteCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 81, 2, 1, 1)).setObjects(("DISMAN-TRACEROUTE-MIB", "traceRouteGroup"), ("DISMAN-TRACEROUTE-MIB", "traceRouteTimeStampGroup"), ("DISMAN-TRACEROUTE-MIB", "traceRouteNotificationsGroup"), ("DISMAN-TRACEROUTE-MIB", "traceRouteHopsTableGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    traceRouteCompliance = traceRouteCompliance.setStatus('deprecated')
traceRouteMinimumGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 81, 2, 2, 5)).setObjects(("DISMAN-TRACEROUTE-MIB", "traceRouteMaxConcurrentRequests"), ("DISMAN-TRACEROUTE-MIB", "traceRouteCtlTargetAddressType"), ("DISMAN-TRACEROUTE-MIB", "traceRouteCtlTargetAddress"), ("DISMAN-TRACEROUTE-MIB", "traceRouteCtlByPassRouteTable"), ("DISMAN-TRACEROUTE-MIB", "traceRouteCtlDataSize"), ("DISMAN-TRACEROUTE-MIB", "traceRouteCtlTimeOut"), ("DISMAN-TRACEROUTE-MIB", "traceRouteCtlProbesPerHop"), ("DISMAN-TRACEROUTE-MIB", "traceRouteCtlPort"), ("DISMAN-TRACEROUTE-MIB", "traceRouteCtlMaxTtl"), ("DISMAN-TRACEROUTE-MIB", "traceRouteCtlDSField"), ("DISMAN-TRACEROUTE-MIB", "traceRouteCtlSourceAddressType"), ("DISMAN-TRACEROUTE-MIB", "traceRouteCtlSourceAddress"), ("DISMAN-TRACEROUTE-MIB", "traceRouteCtlIfIndex"), ("DISMAN-TRACEROUTE-MIB", "traceRouteCtlMiscOptions"), ("DISMAN-TRACEROUTE-MIB", "traceRouteCtlMaxFailures"), ("DISMAN-TRACEROUTE-MIB", "traceRouteCtlDontFragment"), ("DISMAN-TRACEROUTE-MIB", "traceRouteCtlInitialTtl"), ("DISMAN-TRACEROUTE-MIB", "traceRouteCtlFrequency"), ("DISMAN-TRACEROUTE-MIB", "traceRouteCtlStorageType"), ("DISMAN-TRACEROUTE-MIB", "traceRouteCtlAdminStatus"), ("DISMAN-TRACEROUTE-MIB", "traceRouteCtlMaxRows"), ("DISMAN-TRACEROUTE-MIB", "traceRouteCtlTrapGeneration"), ("DISMAN-TRACEROUTE-MIB", "traceRouteCtlDescr"), ("DISMAN-TRACEROUTE-MIB", "traceRouteCtlCreateHopsEntries"), ("DISMAN-TRACEROUTE-MIB", "traceRouteCtlType"), ("DISMAN-TRACEROUTE-MIB", "traceRouteResultsOperStatus"), ("DISMAN-TRACEROUTE-MIB", "traceRouteResultsCurHopCount"), ("DISMAN-TRACEROUTE-MIB", "traceRouteResultsCurProbeCount"), ("DISMAN-TRACEROUTE-MIB", "traceRouteResultsIpTgtAddrType"), ("DISMAN-TRACEROUTE-MIB", "traceRouteResultsIpTgtAddr"), ("DISMAN-TRACEROUTE-MIB", "traceRouteResultsTestAttempts"), ("DISMAN-TRACEROUTE-MIB", "traceRouteResultsTestSuccesses"), ("DISMAN-TRACEROUTE-MIB", "traceRouteResultsLastGoodPath"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    traceRouteMinimumGroup = traceRouteMinimumGroup.setStatus('current')
traceRouteCtlRowStatusGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 81, 2, 2, 6)).setObjects(("DISMAN-TRACEROUTE-MIB", "traceRouteCtlRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    traceRouteCtlRowStatusGroup = traceRouteCtlRowStatusGroup.setStatus('current')
traceRouteHistoryGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 81, 2, 2, 7)).setObjects(("DISMAN-TRACEROUTE-MIB", "traceRouteProbeHistoryHAddrType"), ("DISMAN-TRACEROUTE-MIB", "traceRouteProbeHistoryHAddr"), ("DISMAN-TRACEROUTE-MIB", "traceRouteProbeHistoryResponse"), ("DISMAN-TRACEROUTE-MIB", "traceRouteProbeHistoryStatus"), ("DISMAN-TRACEROUTE-MIB", "traceRouteProbeHistoryLastRC"), ("DISMAN-TRACEROUTE-MIB", "traceRouteProbeHistoryTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    traceRouteHistoryGroup = traceRouteHistoryGroup.setStatus('current')
traceRouteNotificationsGroup = NotificationGroup((1, 3, 6, 1, 2, 1, 81, 2, 2, 3)).setObjects(("DISMAN-TRACEROUTE-MIB", "traceRoutePathChange"), ("DISMAN-TRACEROUTE-MIB", "traceRouteTestFailed"), ("DISMAN-TRACEROUTE-MIB", "traceRouteTestCompleted"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    traceRouteNotificationsGroup = traceRouteNotificationsGroup.setStatus('current')
traceRouteHopsTableGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 81, 2, 2, 4)).setObjects(("DISMAN-TRACEROUTE-MIB", "traceRouteHopsIpTgtAddressType"), ("DISMAN-TRACEROUTE-MIB", "traceRouteHopsIpTgtAddress"), ("DISMAN-TRACEROUTE-MIB", "traceRouteHopsMinRtt"), ("DISMAN-TRACEROUTE-MIB", "traceRouteHopsMaxRtt"), ("DISMAN-TRACEROUTE-MIB", "traceRouteHopsAverageRtt"), ("DISMAN-TRACEROUTE-MIB", "traceRouteHopsRttSumOfSquares"), ("DISMAN-TRACEROUTE-MIB", "traceRouteHopsSentProbes"), ("DISMAN-TRACEROUTE-MIB", "traceRouteHopsProbeResponses"), ("DISMAN-TRACEROUTE-MIB", "traceRouteHopsLastGoodProbe"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    traceRouteHopsTableGroup = traceRouteHopsTableGroup.setStatus('current')
traceRouteGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 81, 2, 2, 1)).setObjects(("DISMAN-TRACEROUTE-MIB", "traceRouteMaxConcurrentRequests"), ("DISMAN-TRACEROUTE-MIB", "traceRouteCtlTargetAddressType"), ("DISMAN-TRACEROUTE-MIB", "traceRouteCtlTargetAddress"), ("DISMAN-TRACEROUTE-MIB", "traceRouteCtlByPassRouteTable"), ("DISMAN-TRACEROUTE-MIB", "traceRouteCtlDataSize"), ("DISMAN-TRACEROUTE-MIB", "traceRouteCtlTimeOut"), ("DISMAN-TRACEROUTE-MIB", "traceRouteCtlProbesPerHop"), ("DISMAN-TRACEROUTE-MIB", "traceRouteCtlPort"), ("DISMAN-TRACEROUTE-MIB", "traceRouteCtlMaxTtl"), ("DISMAN-TRACEROUTE-MIB", "traceRouteCtlDSField"), ("DISMAN-TRACEROUTE-MIB", "traceRouteCtlSourceAddressType"), ("DISMAN-TRACEROUTE-MIB", "traceRouteCtlSourceAddress"), ("DISMAN-TRACEROUTE-MIB", "traceRouteCtlIfIndex"), ("DISMAN-TRACEROUTE-MIB", "traceRouteCtlMiscOptions"), ("DISMAN-TRACEROUTE-MIB", "traceRouteCtlMaxFailures"), ("DISMAN-TRACEROUTE-MIB", "traceRouteCtlDontFragment"), ("DISMAN-TRACEROUTE-MIB", "traceRouteCtlInitialTtl"), ("DISMAN-TRACEROUTE-MIB", "traceRouteCtlFrequency"), ("DISMAN-TRACEROUTE-MIB", "traceRouteCtlStorageType"), ("DISMAN-TRACEROUTE-MIB", "traceRouteCtlAdminStatus"), ("DISMAN-TRACEROUTE-MIB", "traceRouteCtlMaxRows"), ("DISMAN-TRACEROUTE-MIB", "traceRouteCtlTrapGeneration"), ("DISMAN-TRACEROUTE-MIB", "traceRouteCtlDescr"), ("DISMAN-TRACEROUTE-MIB", "traceRouteCtlCreateHopsEntries"), ("DISMAN-TRACEROUTE-MIB", "traceRouteCtlType"), ("DISMAN-TRACEROUTE-MIB", "traceRouteCtlRowStatus"), ("DISMAN-TRACEROUTE-MIB", "traceRouteResultsOperStatus"), ("DISMAN-TRACEROUTE-MIB", "traceRouteResultsCurHopCount"), ("DISMAN-TRACEROUTE-MIB", "traceRouteResultsCurProbeCount"), ("DISMAN-TRACEROUTE-MIB", "traceRouteResultsIpTgtAddrType"), ("DISMAN-TRACEROUTE-MIB", "traceRouteResultsIpTgtAddr"), ("DISMAN-TRACEROUTE-MIB", "traceRouteResultsTestAttempts"), ("DISMAN-TRACEROUTE-MIB", "traceRouteResultsTestSuccesses"), ("DISMAN-TRACEROUTE-MIB", "traceRouteProbeHistoryHAddrType"), ("DISMAN-TRACEROUTE-MIB", "traceRouteProbeHistoryHAddr"), ("DISMAN-TRACEROUTE-MIB", "traceRouteProbeHistoryResponse"), ("DISMAN-TRACEROUTE-MIB", "traceRouteProbeHistoryStatus"), ("DISMAN-TRACEROUTE-MIB", "traceRouteProbeHistoryLastRC"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    traceRouteGroup = traceRouteGroup.setStatus('deprecated')
traceRouteTimeStampGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 81, 2, 2, 2)).setObjects(("DISMAN-TRACEROUTE-MIB", "traceRouteResultsLastGoodPath"), ("DISMAN-TRACEROUTE-MIB", "traceRouteProbeHistoryTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    traceRouteTimeStampGroup = traceRouteTimeStampGroup.setStatus('deprecated')
mibBuilder.exportSymbols("DISMAN-TRACEROUTE-MIB", traceRouteHopsTable=traceRouteHopsTable, traceRouteHopsMaxRtt=traceRouteHopsMaxRtt, traceRouteProbeHistoryStatus=traceRouteProbeHistoryStatus, traceRouteProbeHistoryTime=traceRouteProbeHistoryTime, traceRouteConformance=traceRouteConformance, traceRouteCtlDSField=traceRouteCtlDSField, traceRouteGroup=traceRouteGroup, traceRouteCtlTrapGeneration=traceRouteCtlTrapGeneration, traceRouteCtlMiscOptions=traceRouteCtlMiscOptions, traceRouteMinimumCompliance=traceRouteMinimumCompliance, traceRouteCtlRowStatus=traceRouteCtlRowStatus, traceRouteCtlProbesPerHop=traceRouteCtlProbesPerHop, traceRouteResultsCurHopCount=traceRouteResultsCurHopCount, traceRouteCtlTestName=traceRouteCtlTestName, traceRouteTimeStampGroup=traceRouteTimeStampGroup, traceRouteResultsTestAttempts=traceRouteResultsTestAttempts, traceRouteHopsHopIndex=traceRouteHopsHopIndex, traceRouteMaxConcurrentRequests=traceRouteMaxConcurrentRequests, traceRouteProbeHistoryHopIndex=traceRouteProbeHistoryHopIndex, traceRouteProbeHistoryHAddrType=traceRouteProbeHistoryHAddrType, traceRouteProbeHistoryEntry=traceRouteProbeHistoryEntry, PYSNMP_MODULE_ID=traceRouteMIB, traceRouteHistoryGroup=traceRouteHistoryGroup, traceRouteImplementationTypeDomains=traceRouteImplementationTypeDomains, traceRouteCtlMaxFailures=traceRouteCtlMaxFailures, traceRouteCtlTable=traceRouteCtlTable, traceRouteCtlEntry=traceRouteCtlEntry, traceRouteHopsLastGoodProbe=traceRouteHopsLastGoodProbe, traceRouteUsingUdpProbes=traceRouteUsingUdpProbes, traceRouteProbeHistoryResponse=traceRouteProbeHistoryResponse, traceRouteCtlDataSize=traceRouteCtlDataSize, traceRouteProbeHistoryHAddr=traceRouteProbeHistoryHAddr, traceRouteProbeHistoryProbeIndex=traceRouteProbeHistoryProbeIndex, traceRouteCtlAdminStatus=traceRouteCtlAdminStatus, traceRouteProbeHistoryIndex=traceRouteProbeHistoryIndex, traceRouteCtlDontFragment=traceRouteCtlDontFragment, traceRouteCompliances=traceRouteCompliances, traceRouteResultsEntry=traceRouteResultsEntry, traceRouteResultsTable=traceRouteResultsTable, traceRouteResultsLastGoodPath=traceRouteResultsLastGoodPath, traceRouteTestCompleted=traceRouteTestCompleted, traceRouteNotifications=traceRouteNotifications, traceRouteResultsIpTgtAddrType=traceRouteResultsIpTgtAddrType, traceRouteHopsIpTgtAddress=traceRouteHopsIpTgtAddress, traceRouteProbeHistoryTable=traceRouteProbeHistoryTable, traceRouteResultsOperStatus=traceRouteResultsOperStatus, traceRouteNotificationsGroup=traceRouteNotificationsGroup, traceRouteCtlSourceAddressType=traceRouteCtlSourceAddressType, traceRouteHopsTableGroup=traceRouteHopsTableGroup, traceRouteResultsTestSuccesses=traceRouteResultsTestSuccesses, traceRouteHopsProbeResponses=traceRouteHopsProbeResponses, traceRouteCompliance=traceRouteCompliance, traceRouteMIB=traceRouteMIB, traceRouteCtlStorageType=traceRouteCtlStorageType, traceRouteHopsIpTgtAddressType=traceRouteHopsIpTgtAddressType, traceRouteHopsRttSumOfSquares=traceRouteHopsRttSumOfSquares, traceRouteHopsAverageRtt=traceRouteHopsAverageRtt, traceRouteResultsCurProbeCount=traceRouteResultsCurProbeCount, traceRouteCtlFrequency=traceRouteCtlFrequency, traceRouteCtlOwnerIndex=traceRouteCtlOwnerIndex, traceRouteCtlCreateHopsEntries=traceRouteCtlCreateHopsEntries, traceRouteCtlSourceAddress=traceRouteCtlSourceAddress, traceRouteCtlByPassRouteTable=traceRouteCtlByPassRouteTable, traceRouteCtlDescr=traceRouteCtlDescr, traceRouteFullCompliance=traceRouteFullCompliance, traceRouteGroups=traceRouteGroups, traceRouteHopsSentProbes=traceRouteHopsSentProbes, traceRouteCtlMaxTtl=traceRouteCtlMaxTtl, traceRouteCtlMaxRows=traceRouteCtlMaxRows, traceRouteHopsMinRtt=traceRouteHopsMinRtt, traceRouteCtlType=traceRouteCtlType, traceRouteProbeHistoryLastRC=traceRouteProbeHistoryLastRC, traceRouteMinimumGroup=traceRouteMinimumGroup, traceRouteObjects=traceRouteObjects, traceRouteCtlRowStatusGroup=traceRouteCtlRowStatusGroup, traceRouteCtlPort=traceRouteCtlPort, traceRouteHopsEntry=traceRouteHopsEntry, traceRouteTestFailed=traceRouteTestFailed, traceRouteCtlTargetAddress=traceRouteCtlTargetAddress, traceRouteResultsIpTgtAddr=traceRouteResultsIpTgtAddr, traceRouteCtlInitialTtl=traceRouteCtlInitialTtl, traceRouteCtlIfIndex=traceRouteCtlIfIndex, traceRouteCtlTimeOut=traceRouteCtlTimeOut, traceRoutePathChange=traceRoutePathChange, traceRouteCtlTargetAddressType=traceRouteCtlTargetAddressType)
