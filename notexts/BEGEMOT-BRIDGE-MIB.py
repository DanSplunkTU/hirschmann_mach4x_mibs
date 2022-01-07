#
# PySNMP MIB module BEGEMOT-BRIDGE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/pfsense/BEGEMOT-BRIDGE-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:34:33 2022
# On host fv-az36-988 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
begemot, = mibBuilder.importSymbols("BEGEMOT-MIB", "begemot")
Timeout, BridgeId = mibBuilder.importSymbols("BRIDGE-MIB", "Timeout", "BridgeId")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, mib_2, Counter32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, iso, ObjectIdentity, ModuleIdentity, Bits, MibIdentifier, Gauge32, Counter64, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "mib-2", "Counter32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "iso", "ObjectIdentity", "ModuleIdentity", "Bits", "MibIdentifier", "Gauge32", "Counter64", "TimeTicks", "IpAddress")
RowStatus, TextualConvention, DisplayString, MacAddress, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString", "MacAddress", "TruthValue")
begemotBridge = ModuleIdentity((1, 3, 6, 1, 4, 1, 12325, 1, 205))
begemotBridge.setRevisions(('2007-08-06 00:00', '2006-11-21 00:00', '2006-07-27 00:00',))
if mibBuilder.loadTexts: begemotBridge.setLastUpdated('200708060000Z')
if mibBuilder.loadTexts: begemotBridge.setOrganization('Sofia University St. Kliment Ohridski')
class BridgeIfName(TextualConvention, OctetString):
    status = 'current'
    displayHint = '16a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 16)

class BridgeIfNameOrEmpty(TextualConvention, OctetString):
    status = 'current'
    displayHint = '16a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 16)

class BridgePortId(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1x.1x'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(2, 2)
    fixedLength = 2

begemotBridgeNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 12325, 1, 205, 0))
begemotBridgeBase = MibIdentifier((1, 3, 6, 1, 4, 1, 12325, 1, 205, 1))
begemotBridgeStp = MibIdentifier((1, 3, 6, 1, 4, 1, 12325, 1, 205, 2))
begemotBridgeTp = MibIdentifier((1, 3, 6, 1, 4, 1, 12325, 1, 205, 3))
begemotBridgePf = MibIdentifier((1, 3, 6, 1, 4, 1, 12325, 1, 205, 4))
begemotBridgeConfigObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 12325, 1, 205, 5))
begemotBridgeBaseTable = MibTable((1, 3, 6, 1, 4, 1, 12325, 1, 205, 1, 1), )
if mibBuilder.loadTexts: begemotBridgeBaseTable.setStatus('current')
begemotBridgeBaseEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12325, 1, 205, 1, 1, 1), ).setIndexNames((0, "BEGEMOT-BRIDGE-MIB", "begemotBridgeBaseName"))
if mibBuilder.loadTexts: begemotBridgeBaseEntry.setStatus('current')
begemotBridgeBaseName = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 205, 1, 1, 1, 1), BridgeIfName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotBridgeBaseName.setStatus('current')
begemotBridgeBaseAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 205, 1, 1, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotBridgeBaseAddress.setStatus('current')
begemotBridgeBaseNumPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 205, 1, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotBridgeBaseNumPorts.setStatus('current')
begemotBridgeBaseType = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 205, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("unknown", 1), ("transparent-only", 2), ("sourceroute-only", 3), ("srt", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotBridgeBaseType.setStatus('current')
begemotBridgeBaseStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 205, 1, 1, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: begemotBridgeBaseStatus.setStatus('current')
begemotBridgeBasePortTable = MibTable((1, 3, 6, 1, 4, 1, 12325, 1, 205, 1, 2), )
if mibBuilder.loadTexts: begemotBridgeBasePortTable.setStatus('current')
begemotBridgeBasePortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12325, 1, 205, 1, 2, 1), ).setIndexNames((0, "BEGEMOT-BRIDGE-MIB", "begemotBridgeBaseName"), (0, "BEGEMOT-BRIDGE-MIB", "begemotBridgeBasePortIfIndex"))
if mibBuilder.loadTexts: begemotBridgeBasePortEntry.setStatus('current')
begemotBridgeBasePort = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 205, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotBridgeBasePort.setStatus('current')
begemotBridgeBasePortIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 205, 1, 2, 1, 2), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotBridgeBasePortIfIndex.setStatus('current')
begemotBridgeBaseSpanEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 205, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: begemotBridgeBaseSpanEnabled.setStatus('current')
begemotBridgeBasePortDelayExceededDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 205, 1, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotBridgeBasePortDelayExceededDiscards.setStatus('current')
begemotBridgeBasePortMtuExceededDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 205, 1, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotBridgeBasePortMtuExceededDiscards.setStatus('current')
begemotBridgeBasePortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 205, 1, 2, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: begemotBridgeBasePortStatus.setStatus('current')
begemotBridgeBasePortPrivate = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 205, 1, 2, 1, 7), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: begemotBridgeBasePortPrivate.setStatus('current')
begemotBridgeStpTable = MibTable((1, 3, 6, 1, 4, 1, 12325, 1, 205, 2, 1), )
if mibBuilder.loadTexts: begemotBridgeStpTable.setStatus('current')
begemotBridgeStpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12325, 1, 205, 2, 1, 1), )
begemotBridgeBaseEntry.registerAugmentions(("BEGEMOT-BRIDGE-MIB", "begemotBridgeStpEntry"))
begemotBridgeStpEntry.setIndexNames(*begemotBridgeBaseEntry.getIndexNames())
if mibBuilder.loadTexts: begemotBridgeStpEntry.setStatus('current')
begemotBridgeStpProtocolSpecification = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 205, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unknown", 1), ("decLb100", 2), ("ieee8021d", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotBridgeStpProtocolSpecification.setStatus('current')
begemotBridgeStpPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 205, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: begemotBridgeStpPriority.setStatus('current')
begemotBridgeStpTimeSinceTopologyChange = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 205, 2, 1, 1, 3), TimeTicks()).setUnits('centi-seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotBridgeStpTimeSinceTopologyChange.setStatus('current')
begemotBridgeStpTopChanges = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 205, 2, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotBridgeStpTopChanges.setStatus('current')
begemotBridgeStpDesignatedRoot = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 205, 2, 1, 1, 5), BridgeId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotBridgeStpDesignatedRoot.setStatus('current')
begemotBridgeStpRootCost = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 205, 2, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotBridgeStpRootCost.setStatus('current')
begemotBridgeStpRootPort = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 205, 2, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotBridgeStpRootPort.setStatus('current')
begemotBridgeStpMaxAge = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 205, 2, 1, 1, 8), Timeout()).setUnits('centi-seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotBridgeStpMaxAge.setStatus('current')
begemotBridgeStpHelloTime = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 205, 2, 1, 1, 9), Timeout()).setUnits('centi-seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotBridgeStpHelloTime.setStatus('current')
begemotBridgeStpHoldTime = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 205, 2, 1, 1, 10), Integer32()).setUnits('centi-seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotBridgeStpHoldTime.setStatus('current')
begemotBridgeStpForwardDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 205, 2, 1, 1, 11), Timeout()).setUnits('centi-seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotBridgeStpForwardDelay.setStatus('current')
begemotBridgeStpBridgeMaxAge = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 205, 2, 1, 1, 12), Timeout().subtype(subtypeSpec=ValueRangeConstraint(600, 4000))).setUnits('centi-seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: begemotBridgeStpBridgeMaxAge.setStatus('current')
begemotBridgeStpBridgeHelloTime = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 205, 2, 1, 1, 13), Timeout().subtype(subtypeSpec=ValueRangeConstraint(100, 1000))).setUnits('centi-seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: begemotBridgeStpBridgeHelloTime.setStatus('current')
begemotBridgeStpBridgeForwardDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 205, 2, 1, 1, 14), Timeout().subtype(subtypeSpec=ValueRangeConstraint(400, 3000))).setUnits('centi-seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: begemotBridgeStpBridgeForwardDelay.setStatus('current')
begemotBridgeStpVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 205, 2, 1, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 2))).clone(namedValues=NamedValues(("stpCompatible", 0), ("rstp", 2))).clone('rstp')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: begemotBridgeStpVersion.setStatus('current')
begemotBridgeStpTxHoldCount = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 205, 2, 1, 1, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10)).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: begemotBridgeStpTxHoldCount.setStatus('current')
begemotBridgeStpPortTable = MibTable((1, 3, 6, 1, 4, 1, 12325, 1, 205, 2, 2), )
if mibBuilder.loadTexts: begemotBridgeStpPortTable.setStatus('current')
begemotBridgeStpPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12325, 1, 205, 2, 2, 1), ).setIndexNames((0, "BEGEMOT-BRIDGE-MIB", "begemotBridgeBaseName"), (0, "BEGEMOT-BRIDGE-MIB", "begemotBridgeBasePortIfIndex"))
if mibBuilder.loadTexts: begemotBridgeStpPortEntry.setStatus('current')
begemotBridgeStpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 205, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotBridgeStpPort.setStatus('current')
begemotBridgeStpPortPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 205, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: begemotBridgeStpPortPriority.setStatus('current')
begemotBridgeStpPortState = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 205, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("disabled", 1), ("blocking", 2), ("listening", 3), ("learning", 4), ("forwarding", 5), ("broken", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotBridgeStpPortState.setStatus('current')
begemotBridgeStpPortEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 205, 2, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: begemotBridgeStpPortEnable.setStatus('current')
begemotBridgeStpPortPathCost = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 205, 2, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: begemotBridgeStpPortPathCost.setStatus('current')
begemotBridgeStpPortDesignatedRoot = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 205, 2, 2, 1, 6), BridgeId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotBridgeStpPortDesignatedRoot.setStatus('current')
begemotBridgeStpPortDesignatedCost = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 205, 2, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotBridgeStpPortDesignatedCost.setStatus('current')
begemotBridgeStpPortDesignatedBridge = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 205, 2, 2, 1, 8), BridgeId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotBridgeStpPortDesignatedBridge.setStatus('current')
begemotBridgeStpPortDesignatedPort = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 205, 2, 2, 1, 9), BridgePortId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotBridgeStpPortDesignatedPort.setStatus('current')
begemotBridgeStpPortForwardTransitions = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 205, 2, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotBridgeStpPortForwardTransitions.setStatus('current')
begemotBridgeStpExtPortTable = MibTable((1, 3, 6, 1, 4, 1, 12325, 1, 205, 2, 3), )
if mibBuilder.loadTexts: begemotBridgeStpExtPortTable.setStatus('current')
begemotBridgeStpExtPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12325, 1, 205, 2, 3, 1), )
begemotBridgeStpPortEntry.registerAugmentions(("BEGEMOT-BRIDGE-MIB", "begemotBridgeStpExtPortEntry"))
begemotBridgeStpExtPortEntry.setIndexNames(*begemotBridgeStpPortEntry.getIndexNames())
if mibBuilder.loadTexts: begemotBridgeStpExtPortEntry.setStatus('current')
begemotBridgeStpPortProtocolMigration = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 205, 2, 3, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: begemotBridgeStpPortProtocolMigration.setStatus('current')
begemotBridgeStpPortAdminEdgePort = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 205, 2, 3, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: begemotBridgeStpPortAdminEdgePort.setStatus('current')
begemotBridgeStpPortOperEdgePort = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 205, 2, 3, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotBridgeStpPortOperEdgePort.setStatus('current')
begemotBridgeStpPortAdminPointToPoint = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 205, 2, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("forceTrue", 0), ("forceFalse", 1), ("auto", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: begemotBridgeStpPortAdminPointToPoint.setStatus('current')
begemotBridgeStpPortOperPointToPoint = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 205, 2, 3, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotBridgeStpPortOperPointToPoint.setStatus('current')
begemotBridgeStpPortAdminPathCost = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 205, 2, 3, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 200000000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: begemotBridgeStpPortAdminPathCost.setStatus('current')
begemotBridgeTpTable = MibTable((1, 3, 6, 1, 4, 1, 12325, 1, 205, 3, 1), )
if mibBuilder.loadTexts: begemotBridgeTpTable.setStatus('current')
begemotBridgeTpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12325, 1, 205, 3, 1, 1), )
begemotBridgeBaseEntry.registerAugmentions(("BEGEMOT-BRIDGE-MIB", "begemotBridgeTpEntry"))
begemotBridgeTpEntry.setIndexNames(*begemotBridgeBaseEntry.getIndexNames())
if mibBuilder.loadTexts: begemotBridgeTpEntry.setStatus('current')
begemotBridgeTpLearnedEntryDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 205, 3, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotBridgeTpLearnedEntryDiscards.setStatus('current')
begemotBridgeTpAgingTime = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 205, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 1000000))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: begemotBridgeTpAgingTime.setStatus('current')
begemotBridgeTpMaxAddresses = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 205, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: begemotBridgeTpMaxAddresses.setStatus('current')
begemotBridgeTpFdbTable = MibTable((1, 3, 6, 1, 4, 1, 12325, 1, 205, 3, 2), )
if mibBuilder.loadTexts: begemotBridgeTpFdbTable.setStatus('current')
begemotBridgeTpFdbEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12325, 1, 205, 3, 2, 1), ).setIndexNames((0, "BEGEMOT-BRIDGE-MIB", "begemotBridgeBaseName"), (0, "BEGEMOT-BRIDGE-MIB", "begemotBridgeTpFdbAddress"))
if mibBuilder.loadTexts: begemotBridgeTpFdbEntry.setStatus('current')
begemotBridgeTpFdbAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 205, 3, 2, 1, 1), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotBridgeTpFdbAddress.setStatus('current')
begemotBridgeTpFdbPort = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 205, 3, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotBridgeTpFdbPort.setStatus('current')
begemotBridgeTpFdbStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 205, 3, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("invalid", 2), ("learned", 3), ("self", 4), ("mgmt", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotBridgeTpFdbStatus.setStatus('current')
begemotBridgeTpPortTable = MibTable((1, 3, 6, 1, 4, 1, 12325, 1, 205, 3, 3), )
if mibBuilder.loadTexts: begemotBridgeTpPortTable.setStatus('current')
begemotBridgeTpPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12325, 1, 205, 3, 3, 1), ).setIndexNames((0, "BEGEMOT-BRIDGE-MIB", "begemotBridgeBaseName"), (0, "BEGEMOT-BRIDGE-MIB", "begemotBridgeBasePortIfIndex"))
if mibBuilder.loadTexts: begemotBridgeTpPortEntry.setStatus('current')
begemotBridgeTpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 205, 3, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotBridgeTpPort.setStatus('current')
begemotBridgeTpPortMaxInfo = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 205, 3, 3, 1, 2), Integer32()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotBridgeTpPortMaxInfo.setStatus('current')
begemotBridgeTpPortInFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 205, 3, 3, 1, 3), Counter32()).setUnits('frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotBridgeTpPortInFrames.setStatus('current')
begemotBridgeTpPortOutFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 205, 3, 3, 1, 4), Counter32()).setUnits('frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotBridgeTpPortOutFrames.setStatus('current')
begemotBridgeTpPortInDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 205, 3, 3, 1, 5), Counter32()).setUnits('frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotBridgeTpPortInDiscards.setStatus('current')
begemotBridgePfilStatus = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 205, 4, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: begemotBridgePfilStatus.setStatus('current')
begemotBridgePfilMembers = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 205, 4, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: begemotBridgePfilMembers.setStatus('current')
begemotBridgePfilIpOnly = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 205, 4, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: begemotBridgePfilIpOnly.setStatus('current')
begemotBridgeLayer2PfStatus = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 205, 4, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: begemotBridgeLayer2PfStatus.setStatus('current')
begemotBridgeDefaultBridgeIf = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 205, 5, 1), BridgeIfNameOrEmpty().clone('bridge0')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: begemotBridgeDefaultBridgeIf.setStatus('current')
begemotBridgeDataUpdate = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 205, 5, 2), Timeout().subtype(subtypeSpec=ValueRangeConstraint(1, 300)).clone(10)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: begemotBridgeDataUpdate.setStatus('current')
begemotBridgeDataPoll = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 205, 5, 3), Timeout().subtype(subtypeSpec=ValueRangeConstraint(1, 3600)).clone(300)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: begemotBridgeDataPoll.setStatus('current')
begemotBridgeNewRoot = NotificationType((1, 3, 6, 1, 4, 1, 12325, 1, 205, 0, 1)).setObjects(("BEGEMOT-BRIDGE-MIB", "begemotBridgeBaseName"))
if mibBuilder.loadTexts: begemotBridgeNewRoot.setStatus('current')
begemotBridgeTopologyChange = NotificationType((1, 3, 6, 1, 4, 1, 12325, 1, 205, 0, 2)).setObjects(("BEGEMOT-BRIDGE-MIB", "begemotBridgeBaseName"))
if mibBuilder.loadTexts: begemotBridgeTopologyChange.setStatus('current')
mibBuilder.exportSymbols("BEGEMOT-BRIDGE-MIB", begemotBridgeTpAgingTime=begemotBridgeTpAgingTime, begemotBridgeStpVersion=begemotBridgeStpVersion, begemotBridgeStpBridgeForwardDelay=begemotBridgeStpBridgeForwardDelay, begemotBridgeStpPortOperEdgePort=begemotBridgeStpPortOperEdgePort, PYSNMP_MODULE_ID=begemotBridge, BridgePortId=BridgePortId, begemotBridgeStpPortPathCost=begemotBridgeStpPortPathCost, BridgeIfName=BridgeIfName, begemotBridgeStpRootCost=begemotBridgeStpRootCost, begemotBridgeStpPortTable=begemotBridgeStpPortTable, begemotBridgeBaseSpanEnabled=begemotBridgeBaseSpanEnabled, begemotBridgePfilMembers=begemotBridgePfilMembers, begemotBridgeNewRoot=begemotBridgeNewRoot, BridgeIfNameOrEmpty=BridgeIfNameOrEmpty, begemotBridgeStpBridgeHelloTime=begemotBridgeStpBridgeHelloTime, begemotBridgeTopologyChange=begemotBridgeTopologyChange, begemotBridgeStp=begemotBridgeStp, begemotBridgeStpEntry=begemotBridgeStpEntry, begemotBridgeStpDesignatedRoot=begemotBridgeStpDesignatedRoot, begemotBridgeStpPortPriority=begemotBridgeStpPortPriority, begemotBridgeStpPortDesignatedCost=begemotBridgeStpPortDesignatedCost, begemotBridgeTpPort=begemotBridgeTpPort, begemotBridgeStpTopChanges=begemotBridgeStpTopChanges, begemotBridgeStpPortDesignatedRoot=begemotBridgeStpPortDesignatedRoot, begemotBridgeTpPortOutFrames=begemotBridgeTpPortOutFrames, begemotBridgeStpHoldTime=begemotBridgeStpHoldTime, begemotBridgeStpPortState=begemotBridgeStpPortState, begemotBridgeBase=begemotBridgeBase, begemotBridgeStpMaxAge=begemotBridgeStpMaxAge, begemotBridgeTpFdbEntry=begemotBridgeTpFdbEntry, begemotBridgeStpProtocolSpecification=begemotBridgeStpProtocolSpecification, begemotBridgeBasePortEntry=begemotBridgeBasePortEntry, begemotBridgeTpLearnedEntryDiscards=begemotBridgeTpLearnedEntryDiscards, begemotBridgeTpMaxAddresses=begemotBridgeTpMaxAddresses, begemotBridgeBasePortDelayExceededDiscards=begemotBridgeBasePortDelayExceededDiscards, begemotBridgeStpPortAdminEdgePort=begemotBridgeStpPortAdminEdgePort, begemotBridgeTpTable=begemotBridgeTpTable, begemotBridgeTpFdbTable=begemotBridgeTpFdbTable, begemotBridgeNotifications=begemotBridgeNotifications, begemotBridgeStpTable=begemotBridgeStpTable, begemotBridgeTpPortTable=begemotBridgeTpPortTable, begemotBridgeStpHelloTime=begemotBridgeStpHelloTime, begemotBridgeTpFdbStatus=begemotBridgeTpFdbStatus, begemotBridgeTpPortInFrames=begemotBridgeTpPortInFrames, begemotBridgeTp=begemotBridgeTp, begemotBridgeStpPortProtocolMigration=begemotBridgeStpPortProtocolMigration, begemotBridgeStpPortEntry=begemotBridgeStpPortEntry, begemotBridgeBaseTable=begemotBridgeBaseTable, begemotBridgeBaseStatus=begemotBridgeBaseStatus, begemotBridgeStpPortAdminPathCost=begemotBridgeStpPortAdminPathCost, begemotBridgeBaseAddress=begemotBridgeBaseAddress, begemotBridgeBasePort=begemotBridgeBasePort, begemotBridgeBaseName=begemotBridgeBaseName, begemotBridgeTpPortInDiscards=begemotBridgeTpPortInDiscards, begemotBridgeTpPortEntry=begemotBridgeTpPortEntry, begemotBridgeBasePortMtuExceededDiscards=begemotBridgeBasePortMtuExceededDiscards, begemotBridgeDataPoll=begemotBridgeDataPoll, begemotBridgeBasePortTable=begemotBridgeBasePortTable, begemotBridgeBasePortPrivate=begemotBridgeBasePortPrivate, begemotBridgeDefaultBridgeIf=begemotBridgeDefaultBridgeIf, begemotBridgeTpEntry=begemotBridgeTpEntry, begemotBridgeStpTxHoldCount=begemotBridgeStpTxHoldCount, begemotBridgeStpPortOperPointToPoint=begemotBridgeStpPortOperPointToPoint, begemotBridgeStpExtPortTable=begemotBridgeStpExtPortTable, begemotBridgeStpPortAdminPointToPoint=begemotBridgeStpPortAdminPointToPoint, begemotBridgeBaseType=begemotBridgeBaseType, begemotBridgeStpPort=begemotBridgeStpPort, begemotBridgeStpExtPortEntry=begemotBridgeStpExtPortEntry, begemotBridgeBaseNumPorts=begemotBridgeBaseNumPorts, begemotBridgeStpPriority=begemotBridgeStpPriority, begemotBridgeBaseEntry=begemotBridgeBaseEntry, begemotBridgeStpPortDesignatedPort=begemotBridgeStpPortDesignatedPort, begemotBridgePf=begemotBridgePf, begemotBridge=begemotBridge, begemotBridgeStpForwardDelay=begemotBridgeStpForwardDelay, begemotBridgeStpPortForwardTransitions=begemotBridgeStpPortForwardTransitions, begemotBridgeStpBridgeMaxAge=begemotBridgeStpBridgeMaxAge, begemotBridgeStpTimeSinceTopologyChange=begemotBridgeStpTimeSinceTopologyChange, begemotBridgeStpPortEnable=begemotBridgeStpPortEnable, begemotBridgeTpPortMaxInfo=begemotBridgeTpPortMaxInfo, begemotBridgePfilStatus=begemotBridgePfilStatus, begemotBridgePfilIpOnly=begemotBridgePfilIpOnly, begemotBridgeTpFdbAddress=begemotBridgeTpFdbAddress, begemotBridgeBasePortStatus=begemotBridgeBasePortStatus, begemotBridgeBasePortIfIndex=begemotBridgeBasePortIfIndex, begemotBridgeStpRootPort=begemotBridgeStpRootPort, begemotBridgeConfigObjects=begemotBridgeConfigObjects, begemotBridgeLayer2PfStatus=begemotBridgeLayer2PfStatus, begemotBridgeDataUpdate=begemotBridgeDataUpdate, begemotBridgeStpPortDesignatedBridge=begemotBridgeStpPortDesignatedBridge, begemotBridgeTpFdbPort=begemotBridgeTpFdbPort)
