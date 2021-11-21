#
# PySNMP MIB module PRVT-EVENT-PROPAGATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/telco-systems/binox/PRVT-EVENT-PROPAGATION-MIB
# Produced by pysmi-1.1.3 at Sun Nov 21 00:45:53 2021
# On host fv-az39-63 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
switch, = mibBuilder.importSymbols("PRVT-SWITCH-MIB", "switch")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, Counter64, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Gauge32, TimeTicks, IpAddress, NotificationType, Counter32, MibIdentifier, Bits, ModuleIdentity, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Counter64", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Gauge32", "TimeTicks", "IpAddress", "NotificationType", "Counter32", "MibIdentifier", "Bits", "ModuleIdentity", "Integer32")
TextualConvention, DisplayString, TruthValue, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TruthValue", "RowStatus")
prvtEventPropagationMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 738, 10, 5, 166))
prvtEventPropagationMIB.setRevisions(('2014-11-10 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: prvtEventPropagationMIB.setRevisionsDescriptions(('Initial version',))
if mibBuilder.loadTexts: prvtEventPropagationMIB.setLastUpdated('201411100000Z')
if mibBuilder.loadTexts: prvtEventPropagationMIB.setOrganization('BATM Advanced Communication')
if mibBuilder.loadTexts: prvtEventPropagationMIB.setContactInfo('BATM/Telco Systems Support team\n         Email:\n         For North America: techsupport@telco.com\n         For North Europe: support@batm.de, info@batm.de\n         For the rest of the world: techsupport@telco.com')
if mibBuilder.loadTexts: prvtEventPropagationMIB.setDescription('This MIB provides control over the Event Propagation feature')
prvtEventPropagationObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 10, 5, 166, 1))
prvtEventPropagationProfileTable = MibTable((1, 3, 6, 1, 4, 1, 738, 10, 5, 166, 1, 1), )
if mibBuilder.loadTexts: prvtEventPropagationProfileTable.setStatus('current')
if mibBuilder.loadTexts: prvtEventPropagationProfileTable.setDescription('Profile table holds the settings for the\n         Event Propagation')
prvtEventPropagationProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 10, 5, 166, 1, 1, 1), ).setIndexNames((0, "PRVT-EVENT-PROPAGATION-MIB", "prvtEventPropagationProfileName"))
if mibBuilder.loadTexts: prvtEventPropagationProfileEntry.setStatus('current')
if mibBuilder.loadTexts: prvtEventPropagationProfileEntry.setDescription('NONE')
prvtEventPropagationProfileName = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 166, 1, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: prvtEventPropagationProfileName.setStatus('current')
if mibBuilder.loadTexts: prvtEventPropagationProfileName.setDescription('This is a unique identifier of the\n         Event Propagation profile tabel.')
prvtEventPropagationProfileRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 166, 1, 1, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtEventPropagationProfileRowStatus.setStatus('current')
if mibBuilder.loadTexts: prvtEventPropagationProfileRowStatus.setDescription('Creation/delete/edit of the Event Propagation profile. ')
prvtEventPropagationSourceRemMep = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 166, 1, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 8191))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtEventPropagationSourceRemMep.setStatus('current')
if mibBuilder.loadTexts: prvtEventPropagationSourceRemMep.setDescription('Event received from remote MEP')
prvtEventPropagationSourceLocalMep = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 166, 1, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 8191))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtEventPropagationSourceLocalMep.setStatus('current')
if mibBuilder.loadTexts: prvtEventPropagationSourceLocalMep.setDescription('Event received from local MEP')
prvtEventPropagationSourceVrrpGroup = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 166, 1, 1, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtEventPropagationSourceVrrpGroup.setStatus('current')
if mibBuilder.loadTexts: prvtEventPropagationSourceVrrpGroup.setDescription('Event received from VRRP')
prvtEventPropagationEvent = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 166, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 4, 5, 6))).clone(namedValues=NamedValues(("none", 0), ("statusDown", 1), ("conLost", 2), ("aisLck", 4), ("rcvdTcBpdu", 5), ("vrrpStatusBackup", 6)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtEventPropagationEvent.setStatus('current')
if mibBuilder.loadTexts: prvtEventPropagationEvent.setDescription('This leaf defines the type of event that will be monitored.')
prvtEventPropagationAction = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 166, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("none", 0), ("linkDrop", 1), ("macWithdraw", 2), ("lacpStandby", 3), ("restrictForwarding", 4), ("noRestrictForwarding", 5)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtEventPropagationAction.setStatus('current')
if mibBuilder.loadTexts: prvtEventPropagationAction.setDescription('Defines the action to be take in case of an event. ')
prvtEventPropagationReverse = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 166, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 0), ("linkRestore", 1), ("lacpActive", 2), ("restrictForwarding", 3), ("noRestrictForwarding", 4)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtEventPropagationReverse.setStatus('current')
if mibBuilder.loadTexts: prvtEventPropagationReverse.setDescription('Specify reverse action, performed when configured event stops')
prvtEventPropagationThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 166, 1, 1, 1, 9), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtEventPropagationThreshold.setStatus('current')
if mibBuilder.loadTexts: prvtEventPropagationThreshold.setDescription('Specify threshold for specified source port')
prvtEventPropagationTimerWaitToRestore = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 166, 1, 1, 1, 10), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 600000))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtEventPropagationTimerWaitToRestore.setStatus('current')
if mibBuilder.loadTexts: prvtEventPropagationTimerWaitToRestore.setDescription('Specify time to wait before configured action is reversed (<0-600000> milliseconds)')
prvtEventPropagationTimerHoldOff = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 166, 1, 1, 1, 11), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 600000))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtEventPropagationTimerHoldOff.setStatus('current')
if mibBuilder.loadTexts: prvtEventPropagationTimerHoldOff.setDescription('Specify time to wait before configured action occurs (<0-600000> milliseconds)')
prvtEventPropagationPerformMacFlush = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 166, 1, 1, 1, 12), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtEventPropagationPerformMacFlush.setStatus('current')
if mibBuilder.loadTexts: prvtEventPropagationPerformMacFlush.setDescription('Specify whether to perform MAC flush upon receiving of defined event.')
prvtEventPropagationSourcePortTable = MibTable((1, 3, 6, 1, 4, 1, 738, 10, 5, 166, 1, 2), )
if mibBuilder.loadTexts: prvtEventPropagationSourcePortTable.setStatus('current')
if mibBuilder.loadTexts: prvtEventPropagationSourcePortTable.setDescription('Sourceport table holds the settings for the\n         Event Propagation')
prvtEventPropagationSourcePortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 10, 5, 166, 1, 2, 1), ).setIndexNames((0, "PRVT-EVENT-PROPAGATION-MIB", "prvtEventPropagationProfileName"), (0, "PRVT-EVENT-PROPAGATION-MIB", "prvtEventPropagationSourcePortName"))
if mibBuilder.loadTexts: prvtEventPropagationSourcePortEntry.setStatus('current')
if mibBuilder.loadTexts: prvtEventPropagationSourcePortEntry.setDescription('NONE')
prvtEventPropagationSourcePortName = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 166, 1, 2, 1, 1), OctetString())
if mibBuilder.loadTexts: prvtEventPropagationSourcePortName.setStatus('current')
if mibBuilder.loadTexts: prvtEventPropagationSourcePortName.setDescription('Specify port number (in format UU/SS/PP or AG)')
prvtEventPropagationSourcePortRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 166, 1, 2, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtEventPropagationSourcePortRowStatus.setStatus('current')
if mibBuilder.loadTexts: prvtEventPropagationSourcePortRowStatus.setDescription('Creation/delete/edit of the Event Propagation source port. ')
prvtEventPropagationSessionTable = MibTable((1, 3, 6, 1, 4, 1, 738, 10, 5, 166, 1, 3), )
if mibBuilder.loadTexts: prvtEventPropagationSessionTable.setStatus('current')
if mibBuilder.loadTexts: prvtEventPropagationSessionTable.setDescription('')
prvtEventPropagationSessionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 10, 5, 166, 1, 3, 1), ).setIndexNames((0, "PRVT-EVENT-PROPAGATION-MIB", "prvtEventPropagationProfileName"), (0, "PRVT-EVENT-PROPAGATION-MIB", "prvtEventPropagationSessionIndex"))
if mibBuilder.loadTexts: prvtEventPropagationSessionEntry.setStatus('current')
if mibBuilder.loadTexts: prvtEventPropagationSessionEntry.setDescription('NONE')
prvtEventPropagationSessionIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 166, 1, 3, 1, 1), Unsigned32())
if mibBuilder.loadTexts: prvtEventPropagationSessionIndex.setStatus('current')
if mibBuilder.loadTexts: prvtEventPropagationSessionIndex.setDescription('Event-propagation session index')
prvtEventPropagationSessionProfileName = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 166, 1, 3, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtEventPropagationSessionProfileName.setStatus('current')
if mibBuilder.loadTexts: prvtEventPropagationSessionProfileName.setDescription('')
prvtEventPropagationSessionTarget = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 166, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 0), ("sap", 1), ("port", 2), ("lag", 3), ("sdp", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtEventPropagationSessionTarget.setStatus('current')
if mibBuilder.loadTexts: prvtEventPropagationSessionTarget.setDescription('')
prvtEventPropagationSessionId = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 166, 1, 3, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtEventPropagationSessionId.setStatus('current')
if mibBuilder.loadTexts: prvtEventPropagationSessionId.setDescription('')
prvtEventPropagationSessionState = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 166, 1, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 0), ("linkDropped", 1), ("linkRestored", 2), ("linkActionPend", 3), ("linkRevertivePend", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtEventPropagationSessionState.setStatus('current')
if mibBuilder.loadTexts: prvtEventPropagationSessionState.setDescription('')
prvtEventPropagationSessionActions = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 166, 1, 3, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtEventPropagationSessionActions.setStatus('current')
if mibBuilder.loadTexts: prvtEventPropagationSessionActions.setDescription('')
prvtEventPropagationSessionRevertives = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 166, 1, 3, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtEventPropagationSessionRevertives.setStatus('current')
if mibBuilder.loadTexts: prvtEventPropagationSessionRevertives.setDescription('')
epappPortTable = MibTable((1, 3, 6, 1, 4, 1, 738, 10, 5, 166, 1, 4), )
if mibBuilder.loadTexts: epappPortTable.setStatus('current')
if mibBuilder.loadTexts: epappPortTable.setDescription('A table that contains event propagation profiles enabled on each port.')
epappPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 10, 5, 166, 1, 4, 1), ).setIndexNames((0, "PRVT-EVENT-PROPAGATION-MIB", "epappPortName"))
if mibBuilder.loadTexts: epappPortEntry.setStatus('current')
if mibBuilder.loadTexts: epappPortEntry.setDescription('Event propagation profile on port.')
epappPortName = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 166, 1, 4, 1, 1), OctetString())
if mibBuilder.loadTexts: epappPortName.setStatus('current')
if mibBuilder.loadTexts: epappPortName.setDescription('Port name.')
epappPortRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 166, 1, 4, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: epappPortRowStatus.setStatus('current')
if mibBuilder.loadTexts: epappPortRowStatus.setDescription('Creation/delete/edit of the Event Propagation port. ')
epappPortProfile = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 166, 1, 4, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: epappPortProfile.setStatus('current')
if mibBuilder.loadTexts: epappPortProfile.setDescription('Specify the name of event propagation profile, applied to this port. ')
mibBuilder.exportSymbols("PRVT-EVENT-PROPAGATION-MIB", prvtEventPropagationAction=prvtEventPropagationAction, prvtEventPropagationEvent=prvtEventPropagationEvent, prvtEventPropagationSessionTarget=prvtEventPropagationSessionTarget, prvtEventPropagationSourcePortTable=prvtEventPropagationSourcePortTable, prvtEventPropagationSessionId=prvtEventPropagationSessionId, epappPortEntry=epappPortEntry, epappPortProfile=epappPortProfile, prvtEventPropagationProfileName=prvtEventPropagationProfileName, prvtEventPropagationSessionIndex=prvtEventPropagationSessionIndex, epappPortTable=epappPortTable, epappPortName=epappPortName, prvtEventPropagationObjects=prvtEventPropagationObjects, prvtEventPropagationSessionTable=prvtEventPropagationSessionTable, prvtEventPropagationThreshold=prvtEventPropagationThreshold, prvtEventPropagationReverse=prvtEventPropagationReverse, prvtEventPropagationSourceLocalMep=prvtEventPropagationSourceLocalMep, prvtEventPropagationSessionActions=prvtEventPropagationSessionActions, prvtEventPropagationSessionState=prvtEventPropagationSessionState, prvtEventPropagationMIB=prvtEventPropagationMIB, PYSNMP_MODULE_ID=prvtEventPropagationMIB, prvtEventPropagationSourceVrrpGroup=prvtEventPropagationSourceVrrpGroup, prvtEventPropagationProfileEntry=prvtEventPropagationProfileEntry, prvtEventPropagationSourcePortRowStatus=prvtEventPropagationSourcePortRowStatus, prvtEventPropagationPerformMacFlush=prvtEventPropagationPerformMacFlush, prvtEventPropagationProfileRowStatus=prvtEventPropagationProfileRowStatus, prvtEventPropagationSourceRemMep=prvtEventPropagationSourceRemMep, prvtEventPropagationTimerHoldOff=prvtEventPropagationTimerHoldOff, prvtEventPropagationTimerWaitToRestore=prvtEventPropagationTimerWaitToRestore, prvtEventPropagationProfileTable=prvtEventPropagationProfileTable, prvtEventPropagationSourcePortName=prvtEventPropagationSourcePortName, prvtEventPropagationSessionEntry=prvtEventPropagationSessionEntry, prvtEventPropagationSessionProfileName=prvtEventPropagationSessionProfileName, prvtEventPropagationSessionRevertives=prvtEventPropagationSessionRevertives, prvtEventPropagationSourcePortEntry=prvtEventPropagationSourcePortEntry, epappPortRowStatus=epappPortRowStatus)
