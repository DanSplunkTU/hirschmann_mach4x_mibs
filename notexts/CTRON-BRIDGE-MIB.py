#
# PySNMP MIB module CTRON-BRIDGE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-BRIDGE-MIB
# Produced by pysmi-1.1.8 at Sun Jan 16 00:36:32 2022
# On host fv-az42-839 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
BridgeId, = mibBuilder.importSymbols("BRIDGE-MIB", "BridgeId")
ctBridge, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctBridge")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, ObjectIdentity, MibIdentifier, iso, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Bits, Counter64, ModuleIdentity, NotificationType, Counter32, Gauge32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "ObjectIdentity", "MibIdentifier", "iso", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Bits", "Counter64", "ModuleIdentity", "NotificationType", "Counter32", "Gauge32", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ctBridgeStp = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 2))
ctBridgeSr = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 3))
ctBridgeTp = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 4))
ctBridgeSdbEnet = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 5))
ctBridgeSdbTr = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 6))
ctBridgeTransTrEnet = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 7))
ctBridgeExtendedControl = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 8))
ctBridgeSdbGeneric = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 9))
ctBridgeLoadShare = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 10))
ctBridgeStpProtocolSpecification = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("decLb100", 2), ("ieee8021d", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctBridgeStpProtocolSpecification.setStatus('mandatory')
ctBridgePvst = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 2, 2))
ctPvstStpMode = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 2, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("dot1qMode", 1), ("pvstMode", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctPvstStpMode.setStatus('deprecated')
ctPvstMaxNumStp = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 2, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPvstMaxNumStp.setStatus('deprecated')
ctPvstNumStps = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 2, 2, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctPvstNumStps.setStatus('deprecated')
ctPvstLastTopologyChange = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 2, 2, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPvstLastTopologyChange.setStatus('deprecated')
ctPvstStpTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 2, 2, 5), )
if mibBuilder.loadTexts: ctPvstStpTable.setStatus('deprecated')
ctPvstStpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 2, 2, 5, 1), ).setIndexNames((0, "CTRON-BRIDGE-MIB", "ctPvstStpVlanId"))
if mibBuilder.loadTexts: ctPvstStpEntry.setStatus('deprecated')
ctPvstStpVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 2, 2, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctPvstStpVlanId.setStatus('deprecated')
ctPvstStpProtocolSpecification = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 2, 2, 5, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unknown", 1), ("decLb100", 2), ("ieee8021d", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPvstStpProtocolSpecification.setStatus('deprecated')
ctPvstStpPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 2, 2, 5, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctPvstStpPriority.setStatus('deprecated')
ctPvstStpTimeSinceTopologyChange = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 2, 2, 5, 1, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPvstStpTimeSinceTopologyChange.setStatus('deprecated')
ctPvstStpTopChanges = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 2, 2, 5, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPvstStpTopChanges.setStatus('deprecated')
ctPvstStpDesignatedRoot = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 2, 2, 5, 1, 6), BridgeId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPvstStpDesignatedRoot.setStatus('deprecated')
ctPvstStpRootCost = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 2, 2, 5, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPvstStpRootCost.setStatus('deprecated')
ctPvstStpRootPort = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 2, 2, 5, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPvstStpRootPort.setStatus('deprecated')
ctPvstStpMaxAge = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 2, 2, 5, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPvstStpMaxAge.setStatus('deprecated')
ctPvstStpHelloTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 2, 2, 5, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPvstStpHelloTime.setStatus('deprecated')
ctPvstStpHoldTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 2, 2, 5, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPvstStpHoldTime.setStatus('deprecated')
ctPvstStpForwardDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 2, 2, 5, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPvstStpForwardDelay.setStatus('deprecated')
ctPvstStpBridgeMaxAge = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 2, 2, 5, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(600, 4000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctPvstStpBridgeMaxAge.setStatus('deprecated')
ctPvstStpBridgeHelloTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 2, 2, 5, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(100, 1000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctPvstStpBridgeHelloTime.setStatus('deprecated')
ctPvstStpBridgeForwardDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 2, 2, 5, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(400, 3000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctPvstStpBridgeForwardDelay.setStatus('deprecated')
ctPvstStpPortTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 2, 2, 6), )
if mibBuilder.loadTexts: ctPvstStpPortTable.setStatus('deprecated')
ctPvstStpPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 2, 2, 6, 1), ).setIndexNames((0, "CTRON-BRIDGE-MIB", "ctPvstStpVlanId"), (0, "CTRON-BRIDGE-MIB", "ctPvstStpPort"))
if mibBuilder.loadTexts: ctPvstStpPortEntry.setStatus('deprecated')
ctPvstStpPortVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 2, 2, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPvstStpPortVlanId.setStatus('deprecated')
ctPvstStpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 2, 2, 6, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPvstStpPort.setStatus('deprecated')
ctPvstStpPortPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 2, 2, 6, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctPvstStpPortPriority.setStatus('deprecated')
ctPvstStpPortState = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 2, 2, 6, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("disabled", 1), ("blocking", 2), ("listening", 3), ("learning", 4), ("forwarding", 5), ("broken", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPvstStpPortState.setStatus('deprecated')
ctPvstStpPortEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 2, 2, 6, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctPvstStpPortEnable.setStatus('deprecated')
ctPvstStpPortPathCost = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 2, 2, 6, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctPvstStpPortPathCost.setStatus('deprecated')
ctPvstStpPortDesignatedRoot = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 2, 2, 6, 1, 7), BridgeId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPvstStpPortDesignatedRoot.setStatus('deprecated')
ctPvstStpPortDesignatedCost = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 2, 2, 6, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPvstStpPortDesignatedCost.setStatus('deprecated')
ctPvstStpPortDesignatedBridge = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 2, 2, 6, 1, 9), BridgeId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPvstStpPortDesignatedBridge.setStatus('deprecated')
ctPvstStpPortDesignatedPort = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 2, 2, 6, 1, 10), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPvstStpPortDesignatedPort.setStatus('deprecated')
ctPvstStpPortForwardTransitions = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 2, 2, 6, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPvstStpPortForwardTransitions.setStatus('deprecated')
ctBridgeSrPortPairTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 3, 1), )
if mibBuilder.loadTexts: ctBridgeSrPortPairTable.setStatus('mandatory')
ctBridgeSrPortPairEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 3, 1, 1), ).setIndexNames((0, "CTRON-BRIDGE-MIB", "ctBridgeSrPortPairSrcPort"), (0, "CTRON-BRIDGE-MIB", "ctBridgeSrPortPairDestPort"))
if mibBuilder.loadTexts: ctBridgeSrPortPairEntry.setStatus('mandatory')
ctBridgeSrPortPairSrcPort = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 3, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctBridgeSrPortPairSrcPort.setStatus('mandatory')
ctBridgeSrPortPairDestPort = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 3, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctBridgeSrPortPairDestPort.setStatus('mandatory')
ctBridgeSrPortPairPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 3, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctBridgeSrPortPairPackets.setStatus('mandatory')
ctBridgeSrPortPairState = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctBridgeSrPortPairState.setStatus('mandatory')
ctBridgeSrConfigPortType = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 3, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("transparentonly", 1), ("sourcerouteonly", 2), ("srt", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctBridgeSrConfigPortType.setStatus('mandatory')
ctBridgeTpPortPairTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 4, 1), )
if mibBuilder.loadTexts: ctBridgeTpPortPairTable.setStatus('mandatory')
ctBridgeTpPortPairEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 4, 1, 1), ).setIndexNames((0, "CTRON-BRIDGE-MIB", "ctBridgeTpPortPairSrcPort"), (0, "CTRON-BRIDGE-MIB", "ctBridgeTpPortPairDestPort"))
if mibBuilder.loadTexts: ctBridgeTpPortPairEntry.setStatus('mandatory')
ctBridgeTpPortPairSrcPort = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 4, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctBridgeTpPortPairSrcPort.setStatus('mandatory')
ctBridgeTpPortPairDestPort = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 4, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctBridgeTpPortPairDestPort.setStatus('mandatory')
ctBridgeTpPortPairPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 4, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctBridgeTpPortPairPackets.setStatus('mandatory')
ctBridgeTpPortPairState = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 4, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctBridgeTpPortPairState.setStatus('mandatory')
ctBridgeSdbEnetTotFtrs = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 5, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctBridgeSdbEnetTotFtrs.setStatus('mandatory')
ctBridgeSdbEnetNoMatch = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 5, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("filter", 1), ("forward", 2), ("searchFDB", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctBridgeSdbEnetNoMatch.setStatus('mandatory')
ctBridgeSdbEnetTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 5, 3), )
if mibBuilder.loadTexts: ctBridgeSdbEnetTable.setStatus('mandatory')
ctBridgeSdbEnetEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 5, 3, 1), ).setIndexNames((0, "CTRON-BRIDGE-MIB", "ctBridgeSdbEnetFtrNo"))
if mibBuilder.loadTexts: ctBridgeSdbEnetEntry.setStatus('mandatory')
ctBridgeSdbEnetFtrNo = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 5, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctBridgeSdbEnetFtrNo.setStatus('mandatory')
ctBridgeSdbEnetState = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 5, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctBridgeSdbEnetState.setStatus('mandatory')
ctBridgeSdbEnetFtrData = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 5, 3, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 78))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctBridgeSdbEnetFtrData.setStatus('mandatory')
ctBridgeSdbEnetDataOffset = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 5, 3, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctBridgeSdbEnetDataOffset.setStatus('mandatory')
ctBridgeSdbEnetIOTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 5, 4), )
if mibBuilder.loadTexts: ctBridgeSdbEnetIOTable.setStatus('mandatory')
ctBridgeSdbEnetIOEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 5, 4, 1), ).setIndexNames((0, "CTRON-BRIDGE-MIB", "ctBridgeSdbEnetIOFtrNo"), (0, "CTRON-BRIDGE-MIB", "ctBridgeSdbEnetIORcvPort"))
if mibBuilder.loadTexts: ctBridgeSdbEnetIOEntry.setStatus('mandatory')
ctBridgeSdbEnetIOFtrNo = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 5, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctBridgeSdbEnetIOFtrNo.setStatus('mandatory')
ctBridgeSdbEnetIORcvPort = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 5, 4, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctBridgeSdbEnetIORcvPort.setStatus('mandatory')
ctBridgeSdbEnetIOAllowedToGoTo = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 5, 4, 1, 3), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctBridgeSdbEnetIOAllowedToGoTo.setStatus('mandatory')
ctBridgeSdbEnetIODelEntry = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 5, 4, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("deleteEntry", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctBridgeSdbEnetIODelEntry.setStatus('mandatory')
ctBridgeSdbTrTotFtrs = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 6, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctBridgeSdbTrTotFtrs.setStatus('mandatory')
ctBridgeSdbTrNoMatch = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 6, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("filter", 1), ("forward", 2), ("searchFDB", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctBridgeSdbTrNoMatch.setStatus('mandatory')
ctBridgeSdbTrTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 6, 3), )
if mibBuilder.loadTexts: ctBridgeSdbTrTable.setStatus('mandatory')
ctBridgeSdbTrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 6, 3, 1), ).setIndexNames((0, "CTRON-BRIDGE-MIB", "ctBridgeSdbTrFtrNo"))
if mibBuilder.loadTexts: ctBridgeSdbTrEntry.setStatus('mandatory')
ctBridgeSdbTrFtrNo = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 6, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctBridgeSdbTrFtrNo.setStatus('mandatory')
ctBridgeSdbTrState = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 6, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctBridgeSdbTrState.setStatus('mandatory')
ctBridgeSdbTrFtrData = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 6, 3, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 78))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctBridgeSdbTrFtrData.setStatus('mandatory')
ctBridgeSdbTrDataOffset = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 6, 3, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctBridgeSdbTrDataOffset.setStatus('mandatory')
ctBridgeSdbTrIOTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 6, 4), )
if mibBuilder.loadTexts: ctBridgeSdbTrIOTable.setStatus('mandatory')
ctBridgeSdbTrIOEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 6, 4, 1), ).setIndexNames((0, "CTRON-BRIDGE-MIB", "ctBridgeSdbTrIOFtrNo"), (0, "CTRON-BRIDGE-MIB", "ctBridgeSdbTrIORcvPort"))
if mibBuilder.loadTexts: ctBridgeSdbTrIOEntry.setStatus('mandatory')
ctBridgeSdbTrIOFtrNo = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 6, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctBridgeSdbTrIOFtrNo.setStatus('mandatory')
ctBridgeSdbTrIORcvPort = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 6, 4, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctBridgeSdbTrIORcvPort.setStatus('mandatory')
ctBridgeSdbTrIOAllowedToGoTo = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 6, 4, 1, 3), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctBridgeSdbTrIOAllowedToGoTo.setStatus('mandatory')
ctBridgeSdbTrIODelEntry = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 6, 4, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("deleteEntry", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctBridgeSdbTrIODelEntry.setStatus('mandatory')
ctBridgeTransTrEnetAutoMode = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 7, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctBridgeTransTrEnetAutoMode.setStatus('mandatory')
ctBridgeTransTrEnetDualMode = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 7, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctBridgeTransTrEnetDualMode.setStatus('mandatory')
ctBridgeTransTrEnetNovell = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 7, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ethernet", 1), ("ieee8023snap", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctBridgeTransTrEnetNovell.setStatus('mandatory')
ctBridgeTransTrEnetIP = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 7, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ethernet", 1), ("ieee8023snap", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctBridgeTransTrEnetIP.setStatus('mandatory')
ctBridgeTransTrEnetAARP = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 7, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ethernet", 1), ("ieee8023snap", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctBridgeTransTrEnetAARP.setStatus('mandatory')
ctBridgeTransTrEnetNovAdd = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 7, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("msb", 1), ("lsb", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctBridgeTransTrEnetNovAdd.setStatus('mandatory')
ctBridgeTransTrEnetIBMTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 7, 7), )
if mibBuilder.loadTexts: ctBridgeTransTrEnetIBMTable.setStatus('mandatory')
ctBridgeTransTrEnetIBMEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 7, 7, 1), ).setIndexNames((0, "CTRON-BRIDGE-MIB", "ctBridgeTransTrEnetIBMIndex"))
if mibBuilder.loadTexts: ctBridgeTransTrEnetIBMEntry.setStatus('mandatory')
ctBridgeTransTrEnetIBMIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 7, 7, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctBridgeTransTrEnetIBMIndex.setStatus('mandatory')
ctBridgeTransTrEnetIBMSap = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 7, 7, 1, 2), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctBridgeTransTrEnetIBMSap.setStatus('mandatory')
ctBridgeTransTrEnetIBMState = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 7, 7, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctBridgeTransTrEnetIBMState.setStatus('mandatory')
ctBridgeTransTrEnetSnapFormat = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 7, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ethernet", 1), ("ieee8023snap", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctBridgeTransTrEnetSnapFormat.setStatus('mandatory')
ctBridgeTransTrEnetSnapTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 7, 9), )
if mibBuilder.loadTexts: ctBridgeTransTrEnetSnapTable.setStatus('mandatory')
ctBridgeTransTrEnetSnapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 7, 9, 1), ).setIndexNames((0, "CTRON-BRIDGE-MIB", "ctBridgeTransTrEnetSnapIndex"))
if mibBuilder.loadTexts: ctBridgeTransTrEnetSnapEntry.setStatus('mandatory')
ctBridgeTransTrEnetSnapIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 7, 9, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctBridgeTransTrEnetSnapIndex.setStatus('mandatory')
ctBridgeTransTrEnetSnapType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 7, 9, 1, 2), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctBridgeTransTrEnetSnapType.setStatus('mandatory')
ctBridgeTransTrEnetSnapState = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 7, 9, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctBridgeTransTrEnetSnapState.setStatus('mandatory')
ctBridgeBaseChassisMgr = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 8, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notSupported", 1), ("managementDisabled", 2), ("managementEnabled", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctBridgeBaseChassisMgr.setStatus('mandatory')
ctBridgeSdbGenericTotFtrs = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 9, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctBridgeSdbGenericTotFtrs.setStatus('mandatory')
ctBridgeSdbGenericNoMatch = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 9, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("filter", 1), ("forward", 2), ("searchFDB", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctBridgeSdbGenericNoMatch.setStatus('mandatory')
ctBridgeSdbGenericTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 9, 3), )
if mibBuilder.loadTexts: ctBridgeSdbGenericTable.setStatus('mandatory')
ctBridgeSdbGenericEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 9, 3, 1), ).setIndexNames((0, "CTRON-BRIDGE-MIB", "ctBridgeSdbGenericFtrNo"))
if mibBuilder.loadTexts: ctBridgeSdbGenericEntry.setStatus('mandatory')
ctBridgeSdbGenericFtrNo = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 9, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctBridgeSdbGenericFtrNo.setStatus('mandatory')
ctBridgeSdbGenericState = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 9, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctBridgeSdbGenericState.setStatus('mandatory')
ctBridgeSdbGenericFtrData = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 9, 3, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 78))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctBridgeSdbGenericFtrData.setStatus('mandatory')
ctBridgeSdbGenericDataOffset = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 9, 3, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctBridgeSdbGenericDataOffset.setStatus('mandatory')
ctBridgeSdbGenericFilterType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 9, 3, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctBridgeSdbGenericFilterType.setStatus('mandatory')
ctBridgeSdbGenericIOTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 9, 4), )
if mibBuilder.loadTexts: ctBridgeSdbGenericIOTable.setStatus('mandatory')
ctBridgeSdbGenericIOEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 9, 4, 1), ).setIndexNames((0, "CTRON-BRIDGE-MIB", "ctBridgeSdbGenericIOFtrNo"), (0, "CTRON-BRIDGE-MIB", "ctBridgeSdbGenericIORcvPort"))
if mibBuilder.loadTexts: ctBridgeSdbGenericIOEntry.setStatus('mandatory')
ctBridgeSdbGenericIOFtrNo = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 9, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctBridgeSdbGenericIOFtrNo.setStatus('mandatory')
ctBridgeSdbGenericIORcvPort = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 9, 4, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctBridgeSdbGenericIORcvPort.setStatus('mandatory')
ctBridgeSdbGenericIOAllowedToGoTo = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 9, 4, 1, 3), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctBridgeSdbGenericIOAllowedToGoTo.setStatus('mandatory')
ctBridgeSdbGenericIODelEntry = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 9, 4, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("deleteEntry", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctBridgeSdbGenericIODelEntry.setStatus('mandatory')
ctBridgeLoadShareInstanceTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 10, 1), )
if mibBuilder.loadTexts: ctBridgeLoadShareInstanceTable.setStatus('mandatory')
ctBridgeLoadShareInstanceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 10, 1, 1), ).setIndexNames((0, "CTRON-BRIDGE-MIB", "ctBridgeLoadShareInstanceId"))
if mibBuilder.loadTexts: ctBridgeLoadShareInstanceEntry.setStatus('mandatory')
ctBridgeLoadShareInstanceId = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 10, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctBridgeLoadShareInstanceId.setStatus('mandatory')
ctBridgeLoadShareAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 10, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctBridgeLoadShareAdminStatus.setStatus('mandatory')
ctBridgeLoadShareOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 10, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctBridgeLoadShareOperStatus.setStatus('mandatory')
ctBridgeLoadSharePortTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 10, 2), )
if mibBuilder.loadTexts: ctBridgeLoadSharePortTable.setStatus('mandatory')
ctBridgeLoadSharePortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 10, 2, 1), ).setIndexNames((0, "CTRON-BRIDGE-MIB", "ctBridgeLoadSharePortInstanceId"), (0, "CTRON-BRIDGE-MIB", "ctBridgeLoadSharePortNum"))
if mibBuilder.loadTexts: ctBridgeLoadSharePortEntry.setStatus('mandatory')
ctBridgeLoadSharePortNum = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 10, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctBridgeLoadSharePortNum.setStatus('mandatory')
ctBridgeLoadSharePortInstanceId = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 10, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctBridgeLoadSharePortInstanceId.setStatus('mandatory')
ctBridgeLoadSharePortAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 10, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctBridgeLoadSharePortAdminStatus.setStatus('mandatory')
ctBridgeLoadSharePortOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 10, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctBridgeLoadSharePortOperStatus.setStatus('mandatory')
ctBridgeLoadSharePortForwardMask = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 10, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctBridgeLoadSharePortForwardMask.setStatus('mandatory')
ctBridgeLoadSharePortForwardInstance = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 10, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctBridgeLoadSharePortForwardInstance.setStatus('mandatory')
ctBridgeLoadSharePortNumPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3, 10, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctBridgeLoadSharePortNumPorts.setStatus('mandatory')
mibBuilder.exportSymbols("CTRON-BRIDGE-MIB", ctBridgeTpPortPairDestPort=ctBridgeTpPortPairDestPort, ctBridgeSdbTrDataOffset=ctBridgeSdbTrDataOffset, ctBridgeLoadSharePortAdminStatus=ctBridgeLoadSharePortAdminStatus, ctPvstStpBridgeMaxAge=ctPvstStpBridgeMaxAge, ctPvstStpTable=ctPvstStpTable, ctBridgeSdbEnetTotFtrs=ctBridgeSdbEnetTotFtrs, ctBridgeSdbTr=ctBridgeSdbTr, ctBridgeTpPortPairTable=ctBridgeTpPortPairTable, ctPvstStpTopChanges=ctPvstStpTopChanges, ctBridgeSdbGenericIOFtrNo=ctBridgeSdbGenericIOFtrNo, ctBridgeTpPortPairEntry=ctBridgeTpPortPairEntry, ctBridgeTransTrEnetIBMEntry=ctBridgeTransTrEnetIBMEntry, ctBridgeSdbGenericFilterType=ctBridgeSdbGenericFilterType, ctBridgeStp=ctBridgeStp, ctPvstStpPortDesignatedPort=ctPvstStpPortDesignatedPort, ctBridgeLoadShareInstanceTable=ctBridgeLoadShareInstanceTable, ctPvstStpRootCost=ctPvstStpRootCost, ctPvstStpPriority=ctPvstStpPriority, ctBridgePvst=ctBridgePvst, ctBridgeTransTrEnetSnapType=ctBridgeTransTrEnetSnapType, ctBridgeTransTrEnetIBMState=ctBridgeTransTrEnetIBMState, ctPvstStpDesignatedRoot=ctPvstStpDesignatedRoot, ctBridgeSdbTrFtrNo=ctBridgeSdbTrFtrNo, ctBridgeTransTrEnetIP=ctBridgeTransTrEnetIP, ctBridgeSdbEnetIOTable=ctBridgeSdbEnetIOTable, ctPvstStpMaxAge=ctPvstStpMaxAge, ctBridgeSdbEnetFtrNo=ctBridgeSdbEnetFtrNo, ctBridgeSdbGenericFtrNo=ctBridgeSdbGenericFtrNo, ctBridgeLoadSharePortEntry=ctBridgeLoadSharePortEntry, ctBridgeTransTrEnetSnapFormat=ctBridgeTransTrEnetSnapFormat, ctBridgeSdbGenericNoMatch=ctBridgeSdbGenericNoMatch, ctBridgeStpProtocolSpecification=ctBridgeStpProtocolSpecification, ctBridgeBaseChassisMgr=ctBridgeBaseChassisMgr, ctBridgeSrPortPairSrcPort=ctBridgeSrPortPairSrcPort, ctPvstMaxNumStp=ctPvstMaxNumStp, ctBridgeSdbGenericIOAllowedToGoTo=ctBridgeSdbGenericIOAllowedToGoTo, ctBridgeTp=ctBridgeTp, ctBridgeSdbGenericIODelEntry=ctBridgeSdbGenericIODelEntry, ctPvstStpPortTable=ctPvstStpPortTable, ctPvstStpPortDesignatedBridge=ctPvstStpPortDesignatedBridge, ctPvstStpPortEnable=ctPvstStpPortEnable, ctPvstStpHoldTime=ctPvstStpHoldTime, ctBridgeTransTrEnetNovAdd=ctBridgeTransTrEnetNovAdd, ctBridgeTpPortPairPackets=ctBridgeTpPortPairPackets, ctBridgeTransTrEnetDualMode=ctBridgeTransTrEnetDualMode, ctBridgeSdbGenericIOEntry=ctBridgeSdbGenericIOEntry, ctBridgeSdbTrEntry=ctBridgeSdbTrEntry, ctBridgeSdbGenericState=ctBridgeSdbGenericState, ctPvstStpPortVlanId=ctPvstStpPortVlanId, ctBridgeSdbEnet=ctBridgeSdbEnet, ctBridgeSdbTrNoMatch=ctBridgeSdbTrNoMatch, ctBridgeSrPortPairDestPort=ctBridgeSrPortPairDestPort, ctBridgeTransTrEnetIBMIndex=ctBridgeTransTrEnetIBMIndex, ctBridgeLoadShareAdminStatus=ctBridgeLoadShareAdminStatus, ctBridgeLoadSharePortNumPorts=ctBridgeLoadSharePortNumPorts, ctBridgeSdbEnetIOEntry=ctBridgeSdbEnetIOEntry, ctBridgeSdbEnetEntry=ctBridgeSdbEnetEntry, ctBridgeSdbGenericTable=ctBridgeSdbGenericTable, ctBridgeSdbGenericDataOffset=ctBridgeSdbGenericDataOffset, ctBridgeSdbGenericEntry=ctBridgeSdbGenericEntry, ctBridgeTransTrEnetSnapState=ctBridgeTransTrEnetSnapState, ctBridgeSdbGenericIOTable=ctBridgeSdbGenericIOTable, ctBridgeExtendedControl=ctBridgeExtendedControl, ctBridgeLoadShareInstanceId=ctBridgeLoadShareInstanceId, ctBridgeSdbGenericIORcvPort=ctBridgeSdbGenericIORcvPort, ctBridgeSdbTrFtrData=ctBridgeSdbTrFtrData, ctPvstStpTimeSinceTopologyChange=ctPvstStpTimeSinceTopologyChange, ctBridgeSdbGenericFtrData=ctBridgeSdbGenericFtrData, ctPvstStpForwardDelay=ctPvstStpForwardDelay, ctBridgeLoadSharePortForwardInstance=ctBridgeLoadSharePortForwardInstance, ctBridgeSdbEnetIORcvPort=ctBridgeSdbEnetIORcvPort, ctBridgeTransTrEnetSnapIndex=ctBridgeTransTrEnetSnapIndex, ctBridgeTransTrEnetNovell=ctBridgeTransTrEnetNovell, ctPvstStpPortDesignatedRoot=ctPvstStpPortDesignatedRoot, ctPvstStpPortState=ctPvstStpPortState, ctBridgeTransTrEnetSnapEntry=ctBridgeTransTrEnetSnapEntry, ctBridgeSrPortPairPackets=ctBridgeSrPortPairPackets, ctBridgeSdbEnetIOAllowedToGoTo=ctBridgeSdbEnetIOAllowedToGoTo, ctBridgeSr=ctBridgeSr, ctBridgeTransTrEnetIBMSap=ctBridgeTransTrEnetIBMSap, ctBridgeSrConfigPortType=ctBridgeSrConfigPortType, ctPvstStpPortPriority=ctPvstStpPortPriority, ctBridgeTransTrEnetAARP=ctBridgeTransTrEnetAARP, ctBridgeSdbTrTable=ctBridgeSdbTrTable, ctBridgeSdbGenericTotFtrs=ctBridgeSdbGenericTotFtrs, ctBridgeSdbEnetDataOffset=ctBridgeSdbEnetDataOffset, ctPvstStpVlanId=ctPvstStpVlanId, ctBridgeTpPortPairSrcPort=ctBridgeTpPortPairSrcPort, ctBridgeSrPortPairEntry=ctBridgeSrPortPairEntry, ctBridgeLoadSharePortTable=ctBridgeLoadSharePortTable, ctBridgeTpPortPairState=ctBridgeTpPortPairState, ctBridgeLoadSharePortOperStatus=ctBridgeLoadSharePortOperStatus, ctBridgeTransTrEnetSnapTable=ctBridgeTransTrEnetSnapTable, ctBridgeSdbEnetNoMatch=ctBridgeSdbEnetNoMatch, ctBridgeSdbEnetIODelEntry=ctBridgeSdbEnetIODelEntry, ctBridgeSdbTrIOEntry=ctBridgeSdbTrIOEntry, ctPvstStpProtocolSpecification=ctPvstStpProtocolSpecification, ctBridgeSrPortPairState=ctBridgeSrPortPairState, ctPvstStpRootPort=ctPvstStpRootPort, ctBridgeSdbEnetIOFtrNo=ctBridgeSdbEnetIOFtrNo, ctBridgeLoadShareOperStatus=ctBridgeLoadShareOperStatus, ctPvstNumStps=ctPvstNumStps, ctBridgeLoadSharePortInstanceId=ctBridgeLoadSharePortInstanceId, ctPvstStpPortDesignatedCost=ctPvstStpPortDesignatedCost, ctBridgeLoadSharePortForwardMask=ctBridgeLoadSharePortForwardMask, ctBridgeSdbTrIODelEntry=ctBridgeSdbTrIODelEntry, ctBridgeSrPortPairTable=ctBridgeSrPortPairTable, ctBridgeSdbTrIOFtrNo=ctBridgeSdbTrIOFtrNo, ctBridgeSdbTrIOAllowedToGoTo=ctBridgeSdbTrIOAllowedToGoTo, ctPvstStpEntry=ctPvstStpEntry, ctBridgeSdbEnetState=ctBridgeSdbEnetState, ctBridgeSdbTrState=ctBridgeSdbTrState, ctPvstStpMode=ctPvstStpMode, ctBridgeSdbEnetFtrData=ctBridgeSdbEnetFtrData, ctPvstStpBridgeHelloTime=ctPvstStpBridgeHelloTime, ctBridgeSdbTrIOTable=ctBridgeSdbTrIOTable, ctPvstStpPort=ctPvstStpPort, ctPvstStpBridgeForwardDelay=ctPvstStpBridgeForwardDelay, ctPvstLastTopologyChange=ctPvstLastTopologyChange, ctBridgeLoadShareInstanceEntry=ctBridgeLoadShareInstanceEntry, ctPvstStpPortPathCost=ctPvstStpPortPathCost, ctBridgeSdbTrTotFtrs=ctBridgeSdbTrTotFtrs, ctBridgeLoadShare=ctBridgeLoadShare, ctBridgeTransTrEnet=ctBridgeTransTrEnet, ctBridgeSdbEnetTable=ctBridgeSdbEnetTable, ctPvstStpHelloTime=ctPvstStpHelloTime, ctPvstStpPortForwardTransitions=ctPvstStpPortForwardTransitions, ctBridgeSdbTrIORcvPort=ctBridgeSdbTrIORcvPort, ctBridgeTransTrEnetIBMTable=ctBridgeTransTrEnetIBMTable, ctBridgeSdbGeneric=ctBridgeSdbGeneric, ctBridgeTransTrEnetAutoMode=ctBridgeTransTrEnetAutoMode, ctPvstStpPortEntry=ctPvstStpPortEntry, ctBridgeLoadSharePortNum=ctBridgeLoadSharePortNum)
