#
# PySNMP MIB module PRVT-EVENT-PROPAGATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/telco-systems/binox/PRVT-EVENT-PROPAGATION-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:39:32 2022
# On host fv-az36-988 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
switch, = mibBuilder.importSymbols("PRVT-SWITCH-MIB", "switch")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, Unsigned32, NotificationType, ObjectIdentity, Counter64, MibIdentifier, iso, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, ModuleIdentity, TimeTicks, IpAddress, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Unsigned32", "NotificationType", "ObjectIdentity", "Counter64", "MibIdentifier", "iso", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "ModuleIdentity", "TimeTicks", "IpAddress", "Bits")
TruthValue, DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "RowStatus", "TextualConvention")
prvtEventPropagationMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 738, 10, 5, 166))
prvtEventPropagationMIB.setRevisions(('2014-11-10 00:00',))
if mibBuilder.loadTexts: prvtEventPropagationMIB.setLastUpdated('201411100000Z')
if mibBuilder.loadTexts: prvtEventPropagationMIB.setOrganization('BATM Advanced Communication')
prvtEventPropagationObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 10, 5, 166, 1))
prvtEventPropagationProfileTable = MibTable((1, 3, 6, 1, 4, 1, 738, 10, 5, 166, 1, 1), )
if mibBuilder.loadTexts: prvtEventPropagationProfileTable.setStatus('current')
prvtEventPropagationProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 10, 5, 166, 1, 1, 1), ).setIndexNames((0, "PRVT-EVENT-PROPAGATION-MIB", "prvtEventPropagationProfileName"))
if mibBuilder.loadTexts: prvtEventPropagationProfileEntry.setStatus('current')
prvtEventPropagationProfileName = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 166, 1, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: prvtEventPropagationProfileName.setStatus('current')
prvtEventPropagationProfileRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 166, 1, 1, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtEventPropagationProfileRowStatus.setStatus('current')
prvtEventPropagationSourceRemMep = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 166, 1, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 8191))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtEventPropagationSourceRemMep.setStatus('current')
prvtEventPropagationSourceLocalMep = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 166, 1, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 8191))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtEventPropagationSourceLocalMep.setStatus('current')
prvtEventPropagationSourceVrrpGroup = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 166, 1, 1, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtEventPropagationSourceVrrpGroup.setStatus('current')
prvtEventPropagationEvent = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 166, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 4, 5, 6))).clone(namedValues=NamedValues(("none", 0), ("statusDown", 1), ("conLost", 2), ("aisLck", 4), ("rcvdTcBpdu", 5), ("vrrpStatusBackup", 6)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtEventPropagationEvent.setStatus('current')
prvtEventPropagationAction = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 166, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("none", 0), ("linkDrop", 1), ("macWithdraw", 2), ("lacpStandby", 3), ("restrictForwarding", 4), ("noRestrictForwarding", 5)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtEventPropagationAction.setStatus('current')
prvtEventPropagationReverse = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 166, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 0), ("linkRestore", 1), ("lacpActive", 2), ("restrictForwarding", 3), ("noRestrictForwarding", 4)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtEventPropagationReverse.setStatus('current')
prvtEventPropagationThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 166, 1, 1, 1, 9), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtEventPropagationThreshold.setStatus('current')
prvtEventPropagationTimerWaitToRestore = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 166, 1, 1, 1, 10), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 600000))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtEventPropagationTimerWaitToRestore.setStatus('current')
prvtEventPropagationTimerHoldOff = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 166, 1, 1, 1, 11), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 600000))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtEventPropagationTimerHoldOff.setStatus('current')
prvtEventPropagationPerformMacFlush = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 166, 1, 1, 1, 12), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtEventPropagationPerformMacFlush.setStatus('current')
prvtEventPropagationSourcePortTable = MibTable((1, 3, 6, 1, 4, 1, 738, 10, 5, 166, 1, 2), )
if mibBuilder.loadTexts: prvtEventPropagationSourcePortTable.setStatus('current')
prvtEventPropagationSourcePortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 10, 5, 166, 1, 2, 1), ).setIndexNames((0, "PRVT-EVENT-PROPAGATION-MIB", "prvtEventPropagationProfileName"), (0, "PRVT-EVENT-PROPAGATION-MIB", "prvtEventPropagationSourcePortName"))
if mibBuilder.loadTexts: prvtEventPropagationSourcePortEntry.setStatus('current')
prvtEventPropagationSourcePortName = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 166, 1, 2, 1, 1), OctetString())
if mibBuilder.loadTexts: prvtEventPropagationSourcePortName.setStatus('current')
prvtEventPropagationSourcePortRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 166, 1, 2, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtEventPropagationSourcePortRowStatus.setStatus('current')
prvtEventPropagationSessionTable = MibTable((1, 3, 6, 1, 4, 1, 738, 10, 5, 166, 1, 3), )
if mibBuilder.loadTexts: prvtEventPropagationSessionTable.setStatus('current')
prvtEventPropagationSessionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 10, 5, 166, 1, 3, 1), ).setIndexNames((0, "PRVT-EVENT-PROPAGATION-MIB", "prvtEventPropagationProfileName"), (0, "PRVT-EVENT-PROPAGATION-MIB", "prvtEventPropagationSessionIndex"))
if mibBuilder.loadTexts: prvtEventPropagationSessionEntry.setStatus('current')
prvtEventPropagationSessionIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 166, 1, 3, 1, 1), Unsigned32())
if mibBuilder.loadTexts: prvtEventPropagationSessionIndex.setStatus('current')
prvtEventPropagationSessionProfileName = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 166, 1, 3, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtEventPropagationSessionProfileName.setStatus('current')
prvtEventPropagationSessionTarget = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 166, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 0), ("sap", 1), ("port", 2), ("lag", 3), ("sdp", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtEventPropagationSessionTarget.setStatus('current')
prvtEventPropagationSessionId = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 166, 1, 3, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtEventPropagationSessionId.setStatus('current')
prvtEventPropagationSessionState = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 166, 1, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 0), ("linkDropped", 1), ("linkRestored", 2), ("linkActionPend", 3), ("linkRevertivePend", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtEventPropagationSessionState.setStatus('current')
prvtEventPropagationSessionActions = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 166, 1, 3, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtEventPropagationSessionActions.setStatus('current')
prvtEventPropagationSessionRevertives = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 166, 1, 3, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtEventPropagationSessionRevertives.setStatus('current')
epappPortTable = MibTable((1, 3, 6, 1, 4, 1, 738, 10, 5, 166, 1, 4), )
if mibBuilder.loadTexts: epappPortTable.setStatus('current')
epappPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 10, 5, 166, 1, 4, 1), ).setIndexNames((0, "PRVT-EVENT-PROPAGATION-MIB", "epappPortName"))
if mibBuilder.loadTexts: epappPortEntry.setStatus('current')
epappPortName = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 166, 1, 4, 1, 1), OctetString())
if mibBuilder.loadTexts: epappPortName.setStatus('current')
epappPortRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 166, 1, 4, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: epappPortRowStatus.setStatus('current')
epappPortProfile = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 166, 1, 4, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: epappPortProfile.setStatus('current')
mibBuilder.exportSymbols("PRVT-EVENT-PROPAGATION-MIB", prvtEventPropagationAction=prvtEventPropagationAction, prvtEventPropagationSourcePortName=prvtEventPropagationSourcePortName, prvtEventPropagationSessionState=prvtEventPropagationSessionState, prvtEventPropagationTimerHoldOff=prvtEventPropagationTimerHoldOff, prvtEventPropagationSessionTable=prvtEventPropagationSessionTable, prvtEventPropagationEvent=prvtEventPropagationEvent, PYSNMP_MODULE_ID=prvtEventPropagationMIB, epappPortProfile=epappPortProfile, prvtEventPropagationTimerWaitToRestore=prvtEventPropagationTimerWaitToRestore, prvtEventPropagationSessionProfileName=prvtEventPropagationSessionProfileName, prvtEventPropagationProfileEntry=prvtEventPropagationProfileEntry, prvtEventPropagationSessionActions=prvtEventPropagationSessionActions, prvtEventPropagationSourcePortTable=prvtEventPropagationSourcePortTable, prvtEventPropagationSessionEntry=prvtEventPropagationSessionEntry, prvtEventPropagationSessionIndex=prvtEventPropagationSessionIndex, epappPortEntry=epappPortEntry, prvtEventPropagationProfileTable=prvtEventPropagationProfileTable, prvtEventPropagationMIB=prvtEventPropagationMIB, prvtEventPropagationSourceVrrpGroup=prvtEventPropagationSourceVrrpGroup, prvtEventPropagationProfileRowStatus=prvtEventPropagationProfileRowStatus, prvtEventPropagationPerformMacFlush=prvtEventPropagationPerformMacFlush, prvtEventPropagationSourcePortEntry=prvtEventPropagationSourcePortEntry, prvtEventPropagationSessionId=prvtEventPropagationSessionId, prvtEventPropagationThreshold=prvtEventPropagationThreshold, epappPortRowStatus=epappPortRowStatus, prvtEventPropagationSourcePortRowStatus=prvtEventPropagationSourcePortRowStatus, prvtEventPropagationProfileName=prvtEventPropagationProfileName, prvtEventPropagationSessionRevertives=prvtEventPropagationSessionRevertives, prvtEventPropagationSourceLocalMep=prvtEventPropagationSourceLocalMep, prvtEventPropagationSourceRemMep=prvtEventPropagationSourceRemMep, epappPortTable=epappPortTable, epappPortName=epappPortName, prvtEventPropagationReverse=prvtEventPropagationReverse, prvtEventPropagationSessionTarget=prvtEventPropagationSessionTarget, prvtEventPropagationObjects=prvtEventPropagationObjects)
