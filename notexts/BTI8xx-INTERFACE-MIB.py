#
# PySNMP MIB module BTI8xx-INTERFACE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/bti/BTI8xx-INTERFACE-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 17:53:19 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
mainSystem, = mibBuilder.importSymbols("BTI8xx-TC-MIB", "mainSystem")
InterfaceIndex, ifIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "ifIndex")
PerfCurrentCount, PerfTotalCount, PerfIntervalCount = mibBuilder.importSymbols("PerfHist-TC-MIB", "PerfCurrentCount", "PerfTotalCount", "PerfIntervalCount")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
NotificationType, TimeTicks, Integer32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, IpAddress, Counter32, Bits, ObjectIdentity, Unsigned32, ModuleIdentity, MibIdentifier, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "TimeTicks", "Integer32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "IpAddress", "Counter32", "Bits", "ObjectIdentity", "Unsigned32", "ModuleIdentity", "MibIdentifier", "Gauge32")
RowStatus, DisplayString, DateAndTime, TextualConvention, TruthValue, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "DateAndTime", "TextualConvention", "TruthValue", "MacAddress")
interfaceConfig = ModuleIdentity((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5))
interfaceConfig.setRevisions(('2015-11-20 12:00', '2015-02-25 15:00', '2014-11-14 12:00', '2014-10-29 12:00', '2014-06-13 12:00', '2013-12-27 12:00',))
if mibBuilder.loadTexts: interfaceConfig.setLastUpdated('201511201200Z')
if mibBuilder.loadTexts: interfaceConfig.setOrganization('Actus Networks Ltd.')
interfaceConfigTable = MibTable((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 1), )
if mibBuilder.loadTexts: interfaceConfigTable.setStatus('current')
interfaceConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 1, 1), ).setIndexNames((0, "BTI8xx-INTERFACE-MIB", "interfaceConfigIndex"))
if mibBuilder.loadTexts: interfaceConfigEntry.setStatus('current')
interfaceConfigIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8191))).setMaxAccess("readonly")
if mibBuilder.loadTexts: interfaceConfigIndex.setStatus('current')
interfaceConfigPort = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: interfaceConfigPort.setStatus('current')
interfaceConfigMTU = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(64, 9600))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: interfaceConfigMTU.setStatus('current')
interfaceConfigTPID = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 6))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: interfaceConfigTPID.setStatus('current')
interfaceConfigPVID = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: interfaceConfigPVID.setStatus('current')
interfaceConfigAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: interfaceConfigAdminStatus.setStatus('current')
interfaceConfigOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: interfaceConfigOperStatus.setStatus('current')
interfaceConfigMode = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("auto", 1), ("force", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: interfaceConfigMode.setStatus('current')
interfaceConfigDuplex = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("full", 1), ("half", 2), ("auto", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: interfaceConfigDuplex.setStatus('current')
interfaceConfigSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: interfaceConfigSpeed.setStatus('current')
interfaceConfigAdminFlowCtrl = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: interfaceConfigAdminFlowCtrl.setStatus('current')
interfaceConfigOperFlowCtrl = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: interfaceConfigOperFlowCtrl.setStatus('current')
interfaceConfigAct = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 1, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("act", 1), ("deAct", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: interfaceConfigAct.setStatus('current')
interfaceConfigDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 1, 1, 14), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: interfaceConfigDescription.setStatus('current')
interfaceConfigPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 1, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: interfaceConfigPriority.setStatus('current')
interfaceConfigLag = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 1, 1, 16), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: interfaceConfigLag.setStatus('current')
interfaceConfigLearning = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 1, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: interfaceConfigLearning.setStatus('current')
interfaceStatisticsTable = MibTable((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 2), )
if mibBuilder.loadTexts: interfaceStatisticsTable.setStatus('current')
interfaceStatisticsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 2, 1), ).setIndexNames((0, "BTI8xx-INTERFACE-MIB", "interfaceStatisticsIndex"))
if mibBuilder.loadTexts: interfaceStatisticsEntry.setStatus('current')
interfaceStatisticsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8191))).setMaxAccess("readonly")
if mibBuilder.loadTexts: interfaceStatisticsIndex.setStatus('current')
interfaceStatisticsInOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 2, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: interfaceStatisticsInOctets.setStatus('current')
interfaceStatisticsInFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 2, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: interfaceStatisticsInFrames.setStatus('current')
interfaceStatisticsInUcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 2, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: interfaceStatisticsInUcastPkts.setStatus('current')
interfaceStatisticsInMulticastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 2, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: interfaceStatisticsInMulticastPkts.setStatus('current')
interfaceStatisticsInBroadcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 2, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: interfaceStatisticsInBroadcastPkts.setStatus('current')
interfaceStatisticsOutOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 2, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: interfaceStatisticsOutOctets.setStatus('current')
interfaceStatisticsOutFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 2, 1, 8), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: interfaceStatisticsOutFrames.setStatus('current')
interfaceStatisticsOutUcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 2, 1, 9), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: interfaceStatisticsOutUcastPkts.setStatus('current')
interfaceStatisticsOutMulticastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 2, 1, 10), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: interfaceStatisticsOutMulticastPkts.setStatus('current')
interfaceStatisticsOutBroadcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 2, 1, 11), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: interfaceStatisticsOutBroadcastPkts.setStatus('current')
interfaceStatisticsDropEvents = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 2, 1, 12), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: interfaceStatisticsDropEvents.setStatus('current')
interfaceStatisticsFCSErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 2, 1, 13), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: interfaceStatisticsFCSErrors.setStatus('current')
interfaceStatisticsUndersizePkts = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 2, 1, 14), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: interfaceStatisticsUndersizePkts.setStatus('current')
interfaceStatisticsOversizePkts = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 2, 1, 15), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: interfaceStatisticsOversizePkts.setStatus('current')
interfaceStatisticsFragments = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 2, 1, 16), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: interfaceStatisticsFragments.setStatus('current')
interfaceStatisticsJabbers = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 2, 1, 17), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: interfaceStatisticsJabbers.setStatus('current')
interfaceStatisticsSymbolErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 2, 1, 18), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: interfaceStatisticsSymbolErrors.setStatus('current')
remotePortIdTable = MibTable((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 3), )
if mibBuilder.loadTexts: remotePortIdTable.setStatus('current')
remotePortIdEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: remotePortIdEntry.setStatus('current')
remotePortIdLocalPort = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 3, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: remotePortIdLocalPort.setStatus('current')
remotePortIdLocalType = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 3, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: remotePortIdLocalType.setStatus('current')
remotePortIdDesc = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 3, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: remotePortIdDesc.setStatus('current')
rateLimitTable = MibTable((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 4), )
if mibBuilder.loadTexts: rateLimitTable.setStatus('current')
rateLimitEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 4, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: rateLimitEntry.setStatus('current')
rateLimitPort = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 4, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rateLimitPort.setStatus('current')
rateLimitIngressRate = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1000000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rateLimitIngressRate.setStatus('current')
rateLimitIngressBurst = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 4, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1000000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rateLimitIngressBurst.setStatus('current')
rateLimitIngressState = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 4, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rateLimitIngressState.setStatus('current')
rateLimitEgressRate = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 4, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1000000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rateLimitEgressRate.setStatus('current')
rateLimitEgressBurst = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 4, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1000000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rateLimitEgressBurst.setStatus('current')
rateLimitEgressState = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 4, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rateLimitEgressState.setStatus('current')
rateLimitShapingMode = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 4, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("layer1", 0), ("layer2", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rateLimitShapingMode.setStatus('current')
stormCtrlTable = MibTable((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 5), )
if mibBuilder.loadTexts: stormCtrlTable.setStatus('current')
stormCtrlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 5, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: stormCtrlEntry.setStatus('current')
stormCtrlPort = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 5, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: stormCtrlPort.setStatus('current')
stormCtrlBroadcastPps = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 5, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1000000000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: stormCtrlBroadcastPps.setStatus('current')
stormCtrlBroadcastState = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 5, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: stormCtrlBroadcastState.setStatus('current')
stormCtrlMulticastPps = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 5, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1000000000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: stormCtrlMulticastPps.setStatus('current')
stormCtrlMulticastState = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 5, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: stormCtrlMulticastState.setStatus('current')
stormCtrlDlfPps = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 5, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1000000000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: stormCtrlDlfPps.setStatus('current')
stormCtrlDlfState = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 5, 5, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: stormCtrlDlfState.setStatus('current')
mibBuilder.exportSymbols("BTI8xx-INTERFACE-MIB", rateLimitIngressState=rateLimitIngressState, interfaceConfigSpeed=interfaceConfigSpeed, interfaceStatisticsInUcastPkts=interfaceStatisticsInUcastPkts, interfaceStatisticsOutFrames=interfaceStatisticsOutFrames, rateLimitPort=rateLimitPort, rateLimitTable=rateLimitTable, rateLimitEntry=rateLimitEntry, interfaceStatisticsInMulticastPkts=interfaceStatisticsInMulticastPkts, interfaceStatisticsOutMulticastPkts=interfaceStatisticsOutMulticastPkts, stormCtrlTable=stormCtrlTable, interfaceConfigPVID=interfaceConfigPVID, interfaceConfigLag=interfaceConfigLag, stormCtrlEntry=stormCtrlEntry, stormCtrlMulticastPps=stormCtrlMulticastPps, stormCtrlMulticastState=stormCtrlMulticastState, interfaceStatisticsJabbers=interfaceStatisticsJabbers, interfaceConfigPort=interfaceConfigPort, interfaceConfigAct=interfaceConfigAct, interfaceStatisticsSymbolErrors=interfaceStatisticsSymbolErrors, interfaceStatisticsDropEvents=interfaceStatisticsDropEvents, remotePortIdLocalPort=remotePortIdLocalPort, interfaceConfigDuplex=interfaceConfigDuplex, interfaceStatisticsInBroadcastPkts=interfaceStatisticsInBroadcastPkts, interfaceConfigMTU=interfaceConfigMTU, interfaceStatisticsInOctets=interfaceStatisticsInOctets, interfaceStatisticsOutOctets=interfaceStatisticsOutOctets, rateLimitIngressRate=rateLimitIngressRate, stormCtrlDlfState=stormCtrlDlfState, interfaceStatisticsFragments=interfaceStatisticsFragments, stormCtrlBroadcastState=stormCtrlBroadcastState, interfaceStatisticsUndersizePkts=interfaceStatisticsUndersizePkts, interfaceConfigAdminFlowCtrl=interfaceConfigAdminFlowCtrl, interfaceConfigTPID=interfaceConfigTPID, rateLimitEgressState=rateLimitEgressState, interfaceConfigLearning=interfaceConfigLearning, interfaceConfigIndex=interfaceConfigIndex, interfaceStatisticsIndex=interfaceStatisticsIndex, remotePortIdLocalType=remotePortIdLocalType, rateLimitEgressRate=rateLimitEgressRate, stormCtrlPort=stormCtrlPort, interfaceConfigAdminStatus=interfaceConfigAdminStatus, interfaceStatisticsFCSErrors=interfaceStatisticsFCSErrors, remotePortIdDesc=remotePortIdDesc, interfaceStatisticsOutUcastPkts=interfaceStatisticsOutUcastPkts, interfaceStatisticsInFrames=interfaceStatisticsInFrames, interfaceConfigEntry=interfaceConfigEntry, rateLimitIngressBurst=rateLimitIngressBurst, interfaceStatisticsTable=interfaceStatisticsTable, interfaceStatisticsOversizePkts=interfaceStatisticsOversizePkts, stormCtrlBroadcastPps=stormCtrlBroadcastPps, interfaceConfigOperStatus=interfaceConfigOperStatus, remotePortIdEntry=remotePortIdEntry, interfaceConfigTable=interfaceConfigTable, PYSNMP_MODULE_ID=interfaceConfig, interfaceConfigMode=interfaceConfigMode, stormCtrlDlfPps=stormCtrlDlfPps, interfaceStatisticsEntry=interfaceStatisticsEntry, rateLimitEgressBurst=rateLimitEgressBurst, interfaceConfig=interfaceConfig, rateLimitShapingMode=rateLimitShapingMode, interfaceConfigDescription=interfaceConfigDescription, interfaceConfigOperFlowCtrl=interfaceConfigOperFlowCtrl, interfaceStatisticsOutBroadcastPkts=interfaceStatisticsOutBroadcastPkts, interfaceConfigPriority=interfaceConfigPriority, remotePortIdTable=remotePortIdTable)
