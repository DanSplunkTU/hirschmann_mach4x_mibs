#
# PySNMP MIB module PEGASUS-LEAN-TRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/pegasus/PEGASUS-LEAN-TRAP-MIB
# Produced by pysmi-1.1.3 at Sun Nov 28 20:09:13 2021
# On host fv-az77-612 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
pegasusMibModule, = mibBuilder.importSymbols("PEGASUS-MIB", "pegasusMibModule")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, MibIdentifier, ModuleIdentity, Integer32, NotificationType, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Counter64, IpAddress, Counter32, Unsigned32, ObjectIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "MibIdentifier", "ModuleIdentity", "Integer32", "NotificationType", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Counter64", "IpAddress", "Counter32", "Unsigned32", "ObjectIdentity", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
pegasusLeanTrapModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 6368, 2, 5))
pegasusLeanTrapModule.setRevisions(('2005-02-02 00:00', '2004-12-17 00:00', '2004-03-18 00:00', '2004-01-15 00:00', '2003-11-11 00:00', '2003-03-21 00:00', '2002-09-19 00:00', '2002-04-25 00:00', '2002-04-02 00:00', '2002-03-14 00:00', '2002-02-18 00:00', '2002-02-14 00:00',))
if mibBuilder.loadTexts: pegasusLeanTrapModule.setLastUpdated('200502020000Z')
if mibBuilder.loadTexts: pegasusLeanTrapModule.setOrganization('Schmid Telecom, Zurich')
leanTrapObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6368, 2, 5, 1))
leanNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 6368, 2, 5, 2))
leanTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 6368, 2, 5, 2, 0))
sender = MibScalar((1, 3, 6, 1, 4, 1, 6368, 2, 5, 1, 1), ObjectIdentifier()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: sender.setStatus('current')
senderObjectName = MibScalar((1, 3, 6, 1, 4, 1, 6368, 2, 5, 1, 2), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: senderObjectName.setStatus('current')
senderDescription = MibScalar((1, 3, 6, 1, 4, 1, 6368, 2, 5, 1, 3), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: senderDescription.setStatus('current')
probableCause = MibScalar((1, 3, 6, 1, 4, 1, 6368, 2, 5, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96))).clone(namedValues=NamedValues(("disconnectionError", 1), ("communicationError", 2), ("outOfMemory", 3), ("cfgUploadProblem", 4), ("cfgDownloadProblem", 5), ("statusSyncProblem", 6), ("operStateDisabled", 7), ("activeMaintenanceLoop", 8), ("deviceFailure", 9), ("lossOfSignal", 10), ("lossOfFrameAlignement", 11), ("alarmIndicationSignal", 12), ("bitErrorRateToHigh", 13), ("lossOfExternalClock", 14), ("remoteAlarmIndication", 15), ("deviceInactive", 16), ("wrongProgram", 17), ("inTest", 18), ("failed", 19), ("powerOff", 20), ("offLine", 21), ("offDuty", 22), ("dependency", 23), ("degraded", 24), ("notInstalled", 25), ("logFull", 26), ("blocked", 27), ("l1Activation", 28), ("hasLosAtTrefPoint", 29), ("hasL1ActivationFault", 30), ("hasLosAtDigSection", 31), ("iadPowerLoss", 32), ("iadLifeline", 33), ("iadDCContinuity", 34), ("dslConfig", 35), ("dslUserService", 36), ("dslLoopAtt", 37), ("dslLoswFailure", 38), ("dataswitchPsu1Fail", 39), ("dataswitchPsu2Fail", 40), ("dataswitchFanFail", 41), ("dataswitchUrgentExt", 42), ("dataswitchNonurgentExt", 43), ("v5InterfaceIDFailure", 44), ("v5InterfaceProvisMismatch", 45), ("v5LinkIdFailure", 46), ("unsupported2ndV5Card", 47), ("currentLimit", 48), ("watsonDTRFailed", 49), ("softwareMismatch", 50), ("hardwareProblem", 51), ("ethernetIfLinkIntegrityFailed", 52), ("ethernetIfFifoError", 53), ("unknownProbableCause", 54), ("lossOfFrame", 55), ("traceIdMissmatch", 56), ("lossOfMultiframe", 57), ("multiplexSectionRemoteDefectIndication", 58), ("multiplexSectionAlarmIndicationSignal", 59), ("regeneratorSectionTraceIdMismatch", 60), ("outOfLock", 61), ("lossOfPointer", 62), ("remoteDefectIndication", 63), ("payloadLabelMismatch", 64), ("unequipped", 65), ("initFailed", 66), ("watsonRegW2-AlarmA", 67), ("watsonRegW2-AlarmB", 68), ("watsonRegR-LoswFailure", 69), ("watsonRegC-LoswFailure", 70), ("watsonRegR-BerToHigh", 71), ("watsonRegC-BerToHigh", 72), ("watsonTrapPortBindFailed", 73), ("watsonHPOVConnectFailed", 74), ("dslCurrentLimit", 75), ("m16ProgramTransfer", 76), ("writeError", 77), ("maintenance", 78), ("remoteFailureIndication", 79), ("lcasCrcError", 80), ("nonLcasSequenceError", 81), ("rxLowOrderGroupIdMismatch", 82), ("rxHighOrderGroupIdMismatch", 83), ("rxLowOrderDifferentialDelay", 84), ("rxHighOrderDifferentialDelay", 85), ("rxLowOrderDifferentialDelayAllVT", 86), ("rxHighOrderDifferentialDelayAllVT", 87), ("txFifoOverflow", 88), ("rxFifoOverflow", 89), ("emailServiceAlarm", 90), ("licenseMissing", 91), ("licenseInvalid", 92), ("licenseWrongHostId", 93), ("licenseMaxNetworkNodesExceeded", 94), ("alarmFilteringParseError", 95), ("iadNoCOS", 96)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: probableCause.setStatus('current')
probableCauseText = MibScalar((1, 3, 6, 1, 4, 1, 6368, 2, 5, 1, 5), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: probableCauseText.setStatus('current')
perceivedSeverity = MibScalar((1, 3, 6, 1, 4, 1, 6368, 2, 5, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("critical", 1), ("major", 2), ("minor", 3), ("warning", 4), ("cleared", 5), ("indeterminate", 6)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: perceivedSeverity.setStatus('current')
perceivedSeverityText = MibScalar((1, 3, 6, 1, 4, 1, 6368, 2, 5, 1, 7), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: perceivedSeverityText.setStatus('current')
pegasusAlarm = NotificationType((1, 3, 6, 1, 4, 1, 6368, 2, 5, 2, 0, 1)).setObjects(("PEGASUS-LEAN-TRAP-MIB", "sender"), ("PEGASUS-LEAN-TRAP-MIB", "senderObjectName"), ("PEGASUS-LEAN-TRAP-MIB", "senderDescription"), ("PEGASUS-LEAN-TRAP-MIB", "probableCause"), ("PEGASUS-LEAN-TRAP-MIB", "probableCauseText"), ("PEGASUS-LEAN-TRAP-MIB", "perceivedSeverity"), ("PEGASUS-LEAN-TRAP-MIB", "perceivedSeverityText"))
if mibBuilder.loadTexts: pegasusAlarm.setStatus('current')
mibBuilder.exportSymbols("PEGASUS-LEAN-TRAP-MIB", perceivedSeverityText=perceivedSeverityText, leanTraps=leanTraps, leanNotifications=leanNotifications, pegasusAlarm=pegasusAlarm, PYSNMP_MODULE_ID=pegasusLeanTrapModule, probableCauseText=probableCauseText, perceivedSeverity=perceivedSeverity, sender=sender, leanTrapObjects=leanTrapObjects, probableCause=probableCause, senderObjectName=senderObjectName, pegasusLeanTrapModule=pegasusLeanTrapModule, senderDescription=senderDescription)
