#
# PySNMP MIB module PRVT-MST-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/telco-systems/binos/PRVT-MST-MIB
# Produced by pysmi-1.1.3 at Sun Nov 28 20:26:40 2021
# On host fv-az77-612 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
dot1dStpPortEntry, BridgeId, dot1dBasePort, Timeout = mibBuilder.importSymbols("BRIDGE-MIB", "dot1dStpPortEntry", "BridgeId", "dot1dBasePort", "Timeout")
switch, = mibBuilder.importSymbols("PRVT-SWITCH-MIB", "switch")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
NotificationType, Gauge32, TimeTicks, Integer32, Bits, Counter64, Unsigned32, iso, MibIdentifier, ObjectIdentity, ModuleIdentity, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Gauge32", "TimeTicks", "Integer32", "Bits", "Counter64", "Unsigned32", "iso", "MibIdentifier", "ObjectIdentity", "ModuleIdentity", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress")
TextualConvention, TruthValue, DisplayString, TimeStamp = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString", "TimeStamp")
prvtMSTMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 738, 1, 5, 107))
prvtMSTMib.setRevisions(('2005-02-16 00:00',))
if mibBuilder.loadTexts: prvtMSTMib.setLastUpdated('200502160000Z')
if mibBuilder.loadTexts: prvtMSTMib.setOrganization('BATM Advanced Communication')
prvtMSTNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 0))
prvtMSTObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1))
mSTRegion = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 1))
mSTBridgeParams = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 2))
mSTTimers = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 3))
mSTPort = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 4))
mSTRegionEditControl = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 1, 1))
mSTRegionParameters = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 1, 2))
mSTRegionEditBufferStatus = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("released", 1), ("acquiredBySnmp", 2), ("acquiredByNonSnmp", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mSTRegionEditBufferStatus.setStatus('current')
mSTRegionEditBufferOperation = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("acquire", 2), ("releaseWithForce", 3), ("commit", 4), ("rollBack", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mSTRegionEditBufferOperation.setStatus('current')
mSTRegionName = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 1, 2, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mSTRegionName.setStatus('current')
mSTRegionEditName = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 1, 2, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mSTRegionEditName.setStatus('current')
mSTRegionRevision = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 1, 2, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mSTRegionRevision.setStatus('current')
mSTRegionEditRevision = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 1, 2, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mSTRegionEditRevision.setStatus('current')
mSTInstanceVlanTable = MibTable((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 1, 2, 5), )
if mibBuilder.loadTexts: mSTInstanceVlanTable.setStatus('current')
mSTInstanceVlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 1, 2, 5, 1), ).setIndexNames((0, "PRVT-MST-MIB", "mSTInstanceIndex"))
if mibBuilder.loadTexts: mSTInstanceVlanEntry.setStatus('current')
mSTInstanceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 1, 2, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 256))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: mSTInstanceIndex.setStatus('current')
mSTInstanceVlansMapped = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 1, 2, 5, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mSTInstanceVlansMapped.setStatus('current')
mSTInstanceVlansMapped2k = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 1, 2, 5, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mSTInstanceVlansMapped2k.setStatus('current')
mSTInstanceVlansMapped3k = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 1, 2, 5, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mSTInstanceVlansMapped3k.setStatus('current')
mSTInstanceVlansMapped4k = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 1, 2, 5, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mSTInstanceVlansMapped4k.setStatus('current')
mSTInstanceVlanEditTable = MibTable((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 1, 2, 6), )
if mibBuilder.loadTexts: mSTInstanceVlanEditTable.setStatus('current')
mSTInstanceVlanEditEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 1, 2, 6, 1), ).setIndexNames((0, "PRVT-MST-MIB", "mSTInstanceIndex"))
if mibBuilder.loadTexts: mSTInstanceVlanEditEntry.setStatus('current')
mSTInstanceEditVlansMap = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 1, 2, 6, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mSTInstanceEditVlansMap.setStatus('current')
mSTInstanceEditVlansMap2k = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 1, 2, 6, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mSTInstanceEditVlansMap2k.setStatus('current')
mSTInstanceEditVlansMap3k = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 1, 2, 6, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mSTInstanceEditVlansMap3k.setStatus('current')
mSTInstanceEditVlansMap4k = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 1, 2, 6, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mSTInstanceEditVlansMap4k.setStatus('current')
mSTMaxHopCount = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 40))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mSTMaxHopCount.setStatus('current')
mSTMaxInstanceNumber = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 256))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mSTMaxInstanceNumber.setStatus('current')
mSTInstanceTable = MibTable((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 2, 3), )
if mibBuilder.loadTexts: mSTInstanceTable.setStatus('current')
mSTInstanceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 2, 3, 1), ).setIndexNames((0, "PRVT-MST-MIB", "mSTInstanceIndex"))
if mibBuilder.loadTexts: mSTInstanceEntry.setStatus('current')
mSTInstanceDesignatedRoot = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 2, 3, 1, 1), BridgeId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mSTInstanceDesignatedRoot.setStatus('current')
mSTInstanceRootCost = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 2, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mSTInstanceRootCost.setStatus('current')
mSTInstanceRootPort = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 2, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mSTInstanceRootPort.setStatus('current')
mSTInstanceDesignatedBridge = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 2, 3, 1, 4), BridgeId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mSTInstanceDesignatedBridge.setStatus('current')
mSTInstanceRootPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 2, 3, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mSTInstanceRootPriority.setStatus('current')
mSTInstanceRemainingHopCount = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 2, 3, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 40))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mSTInstanceRemainingHopCount.setStatus('current')
mSTInstancePriority = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 2, 3, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 61440)).clone(32768)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mSTInstancePriority.setStatus('current')
mSTMigrationTimer = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 3, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mSTMigrationTimer.setStatus('current')
mSTTxHoldCount = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 3, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mSTTxHoldCount.setStatus('current')
mSTMaxAge = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 3, 3), Timeout().subtype(subtypeSpec=ValueRangeConstraint(600, 4000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mSTMaxAge.setStatus('current')
mSTHelloTime = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 3, 4), Timeout().subtype(subtypeSpec=ValueRangeConstraint(100, 1000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mSTHelloTime.setStatus('current')
mSTForwardDelay = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 3, 5), Timeout().subtype(subtypeSpec=ValueRangeConstraint(400, 3000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mSTForwardDelay.setStatus('current')
mSTBridgeMaxAge = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 3, 6), Timeout().subtype(subtypeSpec=ValueRangeConstraint(600, 4000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mSTBridgeMaxAge.setStatus('current')
mSTBridgeHelloTime = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 3, 7), Timeout().subtype(subtypeSpec=ValueRangeConstraint(100, 1000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mSTBridgeHelloTime.setStatus('current')
mSTBridgeForwardDelay = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 3, 8), Timeout().subtype(subtypeSpec=ValueRangeConstraint(400, 3000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mSTBridgeForwardDelay.setStatus('current')
mSTPortTable = MibTable((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 4, 1), )
if mibBuilder.loadTexts: mSTPortTable.setStatus('current')
mSTPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 4, 1, 1), ).setIndexNames((0, "BRIDGE-MIB", "dot1dBasePort"))
if mibBuilder.loadTexts: mSTPortEntry.setStatus('current')
mSTPortAdminLinkType = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("pointToPoint", 1), ("shared", 2), ("auto", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mSTPortAdminLinkType.setStatus('current')
mSTPortOperLinkType = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 4, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("pointToPoint", 1), ("shared", 2), ("other", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mSTPortOperLinkType.setStatus('current')
mSTPortProtocolMigration = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 4, 1, 1, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mSTPortProtocolMigration.setStatus('current')
mSTPortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 4, 1, 1, 4), Bits().clone(namedValues=NamedValues(("edge", 0), ("boundary", 1), ("pvst", 2), ("stp", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mSTPortStatus.setStatus('current')
mSTPortAdminEdgePort = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 4, 1, 1, 5), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mSTPortAdminEdgePort.setStatus('current')
mSTPortOperEdgePort = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 4, 1, 1, 6), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mSTPortOperEdgePort.setStatus('current')
mSTPortEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 4, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mSTPortEnable.setStatus('current')
mSTPortPerMstTable = MibTable((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 4, 2), )
if mibBuilder.loadTexts: mSTPortPerMstTable.setStatus('current')
mSTPortPerMstEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 4, 2, 1), ).setIndexNames((0, "PRVT-MST-MIB", "mSTInstanceIndex"), (0, "BRIDGE-MIB", "dot1dBasePort"))
if mibBuilder.loadTexts: mSTPortPerMstEntry.setStatus('current')
mSTPortPerMstRoleValue = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 4, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("disabled", 1), ("root", 2), ("designated", 3), ("alternate", 4), ("backUp", 5), ("boundary", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mSTPortPerMstRoleValue.setStatus('current')
mSTPortPerMstPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 4, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mSTPortPerMstPriority.setStatus('current')
mSTPortPerMstState = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 4, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("disabled", 1), ("blocking", 2), ("listening", 3), ("learning", 4), ("forwarding", 5), ("broken", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mSTPortPerMstState.setStatus('current')
mSTPortPerMstPathCost = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 4, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 200000000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mSTPortPerMstPathCost.setStatus('current')
mSTPortPerMstDesignatedCost = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 4, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mSTPortPerMstDesignatedCost.setStatus('current')
mSTPortPerMstDesignatedBridge = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 4, 2, 1, 6), BridgeId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mSTPortPerMstDesignatedBridge.setStatus('current')
mSTPortPerMstDesignatedPort = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 4, 2, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: mSTPortPerMstDesignatedPort.setStatus('current')
mstpNewRoot = NotificationType((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 0, 1)).setObjects(("PRVT-MST-MIB", "mSTInstanceIndex"))
if mibBuilder.loadTexts: mstpNewRoot.setStatus('current')
mstpTopologyChange = NotificationType((1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 0, 2)).setObjects(("PRVT-MST-MIB", "mSTInstanceIndex"))
if mibBuilder.loadTexts: mstpTopologyChange.setStatus('current')
mibBuilder.exportSymbols("PRVT-MST-MIB", mSTPortTable=mSTPortTable, mSTInstanceEditVlansMap=mSTInstanceEditVlansMap, mSTTxHoldCount=mSTTxHoldCount, mSTInstanceRemainingHopCount=mSTInstanceRemainingHopCount, mSTRegionEditName=mSTRegionEditName, prvtMSTMib=prvtMSTMib, mstpTopologyChange=mstpTopologyChange, mSTPortPerMstPathCost=mSTPortPerMstPathCost, mSTTimers=mSTTimers, mSTRegion=mSTRegion, mSTPortPerMstTable=mSTPortPerMstTable, mSTBridgeForwardDelay=mSTBridgeForwardDelay, mSTPortPerMstPriority=mSTPortPerMstPriority, mSTInstanceVlanEntry=mSTInstanceVlanEntry, mSTInstanceEditVlansMap4k=mSTInstanceEditVlansMap4k, mSTHelloTime=mSTHelloTime, mSTRegionEditBufferOperation=mSTRegionEditBufferOperation, mSTPortPerMstDesignatedCost=mSTPortPerMstDesignatedCost, mSTRegionEditControl=mSTRegionEditControl, mSTInstanceVlanTable=mSTInstanceVlanTable, mSTInstanceIndex=mSTInstanceIndex, mSTPortPerMstDesignatedBridge=mSTPortPerMstDesignatedBridge, mSTPortProtocolMigration=mSTPortProtocolMigration, mSTInstanceTable=mSTInstanceTable, mSTPortPerMstDesignatedPort=mSTPortPerMstDesignatedPort, mSTInstanceVlanEditEntry=mSTInstanceVlanEditEntry, mSTPortOperLinkType=mSTPortOperLinkType, mSTInstanceEntry=mSTInstanceEntry, mSTPortPerMstState=mSTPortPerMstState, mSTMaxInstanceNumber=mSTMaxInstanceNumber, mSTPort=mSTPort, mSTPortAdminEdgePort=mSTPortAdminEdgePort, mSTPortStatus=mSTPortStatus, mSTMaxHopCount=mSTMaxHopCount, mSTInstanceDesignatedBridge=mSTInstanceDesignatedBridge, mSTPortAdminLinkType=mSTPortAdminLinkType, PYSNMP_MODULE_ID=prvtMSTMib, mSTInstanceRootPriority=mSTInstanceRootPriority, mSTForwardDelay=mSTForwardDelay, mSTInstanceRootPort=mSTInstanceRootPort, mSTInstanceVlansMapped4k=mSTInstanceVlansMapped4k, mSTInstanceRootCost=mSTInstanceRootCost, mSTPortEntry=mSTPortEntry, mSTInstanceVlansMapped3k=mSTInstanceVlansMapped3k, mSTPortPerMstRoleValue=mSTPortPerMstRoleValue, prvtMSTObjects=prvtMSTObjects, mSTRegionParameters=mSTRegionParameters, mSTBridgeHelloTime=mSTBridgeHelloTime, mSTPortPerMstEntry=mSTPortPerMstEntry, mSTRegionEditBufferStatus=mSTRegionEditBufferStatus, mSTInstanceVlanEditTable=mSTInstanceVlanEditTable, mSTRegionEditRevision=mSTRegionEditRevision, prvtMSTNotifications=prvtMSTNotifications, mSTInstanceVlansMapped2k=mSTInstanceVlansMapped2k, mSTBridgeMaxAge=mSTBridgeMaxAge, mSTRegionName=mSTRegionName, mSTInstanceEditVlansMap2k=mSTInstanceEditVlansMap2k, mSTBridgeParams=mSTBridgeParams, mSTInstanceVlansMapped=mSTInstanceVlansMapped, mSTMigrationTimer=mSTMigrationTimer, mstpNewRoot=mstpNewRoot, mSTPortEnable=mSTPortEnable, mSTInstanceEditVlansMap3k=mSTInstanceEditVlansMap3k, mSTInstancePriority=mSTInstancePriority, mSTRegionRevision=mSTRegionRevision, mSTInstanceDesignatedRoot=mSTInstanceDesignatedRoot, mSTPortOperEdgePort=mSTPortOperEdgePort, mSTMaxAge=mSTMaxAge)
