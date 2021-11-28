#
# PySNMP MIB module PEGASUS-LEAN-TRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/pegasus/PEGASUS-LEAN-TRAP-MIB
# Produced by pysmi-1.1.3 at Sun Nov 28 20:09:15 2021
# On host fv-az77-612 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
pegasusMibModule, = mibBuilder.importSymbols("PEGASUS-MIB", "pegasusMibModule")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, Integer32, iso, Unsigned32, Counter64, ModuleIdentity, Counter32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Gauge32, ObjectIdentity, Bits, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Integer32", "iso", "Unsigned32", "Counter64", "ModuleIdentity", "Counter32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Gauge32", "ObjectIdentity", "Bits", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
pegasusLeanTrapModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 6368, 2, 5))
pegasusLeanTrapModule.setRevisions(('2005-02-02 00:00', '2004-12-17 00:00', '2004-03-18 00:00', '2004-01-15 00:00', '2003-11-11 00:00', '2003-03-21 00:00', '2002-09-19 00:00', '2002-04-25 00:00', '2002-04-02 00:00', '2002-03-14 00:00', '2002-02-18 00:00', '2002-02-14 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: pegasusLeanTrapModule.setRevisionsDescriptions(('Added new probableCause values.', 'Updated probableCause values.', 'Updated probableCause. Added some new values and modified existing \n     values.', 'Updated probableCause. New value writeError(77).', 'Updated probableCause. New last value is m16ProgramTransfer(76).', 'Appended five new literals into enumeration ProbableCause:\n    - unsupported2ndV5Card(47),\n    - currentLimit(48),\n    - watsonDTRFailed(49),\n    - softwareMismatch(50),\n    - hardwareProblem(51)', 'Inserted four new literals into enumeration ProbableCause:\n    - iadDCContinuity(34),\n    - v5InterfaceIDFailure(44),\n    - v5InterfaceProvisMismatch(45),\n    - v5LinkIdFailure(46)\n    Warning: dslConfig and all other old literals defined after it have\n    changed their ordinal values!', "Added senderDescription. Renamed 'alarm' to 'pegasusAlarm', to help with\n    name conflicts. Made corresponding changes to trap examples above.", 'Added missing import of DisplayString.', 'Added some trap example dumps and explanation to the module description.', "The two trap types were collapsed into one. The former changedAlarm is now\n    represented by an 'alarm' with exactly the same parameters. The former\n    newAlarm was used when the perceivedSeverity changed from CLEARED (i.e.\n    alarm not present) to other than cleared. This is now also reported through\n    the single trap type 'alarm'.\n    The senderText variable was removed. Each of sender and senderObjectName\n    alone exactly identifies the object affected, and senderText was redundant.", 'Initial revision.',))
if mibBuilder.loadTexts: pegasusLeanTrapModule.setLastUpdated('200502020000Z')
if mibBuilder.loadTexts: pegasusLeanTrapModule.setOrganization('Schmid Telecom, Zurich')
if mibBuilder.loadTexts: pegasusLeanTrapModule.setContactInfo('Schmid Telecom AG\n     Binzstrasse 35, CH-8048 Zurich\n     Switzerland\n\n     Email: xdslsupport@schmid-telecom.ch')
if mibBuilder.loadTexts: pegasusLeanTrapModule.setDescription("Pegasus is an SDSL system manufactured by Schmid Telecom Zurich.\n    The information base is defined in PEGASUS-MIB. This MIB singles out\n    the definitions of notification types from that MIB. This allows us to\n    keep the base MIB clearer, and also to have alternative sets of\n    notifications as separate MIBs.\n    The notification types defined in this module are centered around the\n    idea of having a minimal set of notification types, and add the information\n    to the varbindings list of the notification. Here are some examples. The\n    first two were caused by interrupting the DSL line of an running Iad (DSL\n    link and card both unlocked). The third and fourth are generated when the\n    DSL line is restored.\n\n     sysUpTime.0             0:0:42:36.21\n     snmpTrapOID.0           pegasusAlarm\n     sender                  dslInterfaceAvailabilityStatus.5.1.ltu\n     senderObjectName        LineCard:DSLInterfaceId=LTU,DSLLinkId=0,slotId=5\n     senderDescription       dslInterface 5.1.ltu\n     probableCause           dslLoswFailure\n     probableCauseText       DSL_LOSW_FAILURE\n     perceivedSeverity       minor\n     perceivedSeverityText   MINOR\n\n     sysUpTime.0             0:0:42:36.22\n     snmpTrapOID.0           pegasusAlarm\n     sender                  dslLinkActiveLoop.5.1\n     senderObjectName        LineCard:DSLLinkId=0,slotId=5\n     senderDescription       dslLink 5.1\n     probableCause           dslUserService\n     probableCauseText       DSL_USER_SERVICE\n     perceivedSeverity       minor\n     perceivedSeverityText   MINOR\n\n     sysUpTime.0             0:0:42:56.21\n     snmpTrapOID.0           pegasusAlarm\n     sender                  dslInterfaceAvailabilityStatus.5.1.ltu\n     senderObjectName        LineCard:DSLInterfaceId=LTU,DSLLinkId=0,slotId=5\n     senderDescription       dslInterface 5.1.ltu\n     probableCause           dslLoswFailure\n     probableCauseText       DSL_LOSW_FAILURE\n     perceivedSeverity       cleared\n     perceivedSeverityText   CLEARED\n\n     sysUpTime.0             0:0:42:59.21\n     snmpTrapOID.0           pegasusAlarm\n     sender                  dslLinkActiveLoop.5.1\n     senderObjectName        LineCard:DSLLinkId=0,slotId=5\n     senderDescription       dslLink 5.1\n     probableCause           dslUserService\n     probableCauseText       DSL_USER_SERVICE\n     perceivedSeverity       cleared\n     perceivedSeverityText   CLEARED\n\n    Note\n\n    - If the Dsl link (or the DSL card) is locked, the traps would have been\n      suppressed.\n    - Two traps are for the DSL interface, with probableCause dslLoswFailure,\n      indicating a condition of loss of synchronization word. The first has\n      perceivedSeverity minor, the second cleared, to show that the condition\n      has ceased and synchronization regained.\n    - Likewise, for the DSL link, a pair of probableCause dslUserService is\n      sent, with severity minor and then again cleared.\n    - The 'affected managed object' is identified by the JMX object name in\n      senderObjectName, and also be the variable name (OID) in sender. The\n      choice of the variable is arbitrary, usually it is the variable with the\n      lowest OID value (the first variable) of tha 'affected managed object'.\n    - The JMX senderObjectName contains a domain (LineCard in our examples), and\n      a list of attributes, e.g. link, interface and slot numbers. The numbers\n      usually start at zero, while the SNMP index values start at one, as is\n      usual with SNMP. To get the SNMP index value, add one to the JMX value.")
leanTrapObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6368, 2, 5, 1))
leanNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 6368, 2, 5, 2))
leanTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 6368, 2, 5, 2, 0))
sender = MibScalar((1, 3, 6, 1, 4, 1, 6368, 2, 5, 1, 1), ObjectIdentifier()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: sender.setStatus('current')
if mibBuilder.loadTexts: sender.setDescription("The 'sender' of the trap is the SNMP object which caused the event\n         or experienced the condition reported by this trap.\n         Typically, the object identifier is the first accessible column of\n         the table entry representing the sender, in the SNMP table representing\n         objects of the senders type.")
senderObjectName = MibScalar((1, 3, 6, 1, 4, 1, 6368, 2, 5, 1, 2), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: senderObjectName.setStatus('current')
if mibBuilder.loadTexts: senderObjectName.setDescription('The canonical form of the JMX object name for the object which sent\n         the trap. This is a compact and unique representation readable both to\n         man and machine. ')
senderDescription = MibScalar((1, 3, 6, 1, 4, 1, 6368, 2, 5, 1, 3), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: senderDescription.setStatus('current')
if mibBuilder.loadTexts: senderDescription.setDescription("A description of the sender (affected managed object). The description\n         is human readable, unique, and easy to parse. It consists of a single\n\t word describing the kind of sender, optionally followed by a space and\n\t a complete SNMP index value for the MIB table related to the sender.\n\t The space is omitted if there is no index (pegasusSystem only). The\n\t index value is expressed as a sequence of numbers separated by dots.\n\t The last number may actually be a string (only with dslInterface, 'ltu'\n\t or 'ntu'). The table below contains schematic representations for all\n\t types of objects, with ranges for the index values, and examples.\n\t In the table, s is a slot number, l a link or trunk number, i an\n\t interface number, n a user port number (on the Iad) or a logical comm\n\t channel number.\n\n         dataPort s.l         s=1,0<l<6                dataPort 1.3\n\t dslInterface s.l.t   4<s<13,0<l<9,t=ntu|ltu   dslInterface 5.1.ltu\n\t dslLink s.l          4<s<13,0<l<9             dslLink 5.1\n         dataCard s           s=1                      dataCard 1\n\t dslCard s            4<s<13                   dslCard 12\n\t iad s.l              4<s<13,0<l<9             iad 5.1\n\t v5Card s             s=3                      v5Card 3\n\t pegasusSystem                                 pegasusSystem\n\t v5Interface s.i      s=3,0<i                  v5Interface 3.1\n\t v5IsdnPort s.l.n     4<s<13,0<l<9,0<n<5       v5IsdnPort 5.1.1\n\t v5Lcc s.i.n          s=3,0<i,0<n              v5Lcc 3.1.3\n\t v5Link s.l           s=3,0<l<9                v5Link 3.1")
probableCause = MibScalar((1, 3, 6, 1, 4, 1, 6368, 2, 5, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96))).clone(namedValues=NamedValues(("disconnectionError", 1), ("communicationError", 2), ("outOfMemory", 3), ("cfgUploadProblem", 4), ("cfgDownloadProblem", 5), ("statusSyncProblem", 6), ("operStateDisabled", 7), ("activeMaintenanceLoop", 8), ("deviceFailure", 9), ("lossOfSignal", 10), ("lossOfFrameAlignement", 11), ("alarmIndicationSignal", 12), ("bitErrorRateToHigh", 13), ("lossOfExternalClock", 14), ("remoteAlarmIndication", 15), ("deviceInactive", 16), ("wrongProgram", 17), ("inTest", 18), ("failed", 19), ("powerOff", 20), ("offLine", 21), ("offDuty", 22), ("dependency", 23), ("degraded", 24), ("notInstalled", 25), ("logFull", 26), ("blocked", 27), ("l1Activation", 28), ("hasLosAtTrefPoint", 29), ("hasL1ActivationFault", 30), ("hasLosAtDigSection", 31), ("iadPowerLoss", 32), ("iadLifeline", 33), ("iadDCContinuity", 34), ("dslConfig", 35), ("dslUserService", 36), ("dslLoopAtt", 37), ("dslLoswFailure", 38), ("dataswitchPsu1Fail", 39), ("dataswitchPsu2Fail", 40), ("dataswitchFanFail", 41), ("dataswitchUrgentExt", 42), ("dataswitchNonurgentExt", 43), ("v5InterfaceIDFailure", 44), ("v5InterfaceProvisMismatch", 45), ("v5LinkIdFailure", 46), ("unsupported2ndV5Card", 47), ("currentLimit", 48), ("watsonDTRFailed", 49), ("softwareMismatch", 50), ("hardwareProblem", 51), ("ethernetIfLinkIntegrityFailed", 52), ("ethernetIfFifoError", 53), ("unknownProbableCause", 54), ("lossOfFrame", 55), ("traceIdMissmatch", 56), ("lossOfMultiframe", 57), ("multiplexSectionRemoteDefectIndication", 58), ("multiplexSectionAlarmIndicationSignal", 59), ("regeneratorSectionTraceIdMismatch", 60), ("outOfLock", 61), ("lossOfPointer", 62), ("remoteDefectIndication", 63), ("payloadLabelMismatch", 64), ("unequipped", 65), ("initFailed", 66), ("watsonRegW2-AlarmA", 67), ("watsonRegW2-AlarmB", 68), ("watsonRegR-LoswFailure", 69), ("watsonRegC-LoswFailure", 70), ("watsonRegR-BerToHigh", 71), ("watsonRegC-BerToHigh", 72), ("watsonTrapPortBindFailed", 73), ("watsonHPOVConnectFailed", 74), ("dslCurrentLimit", 75), ("m16ProgramTransfer", 76), ("writeError", 77), ("maintenance", 78), ("remoteFailureIndication", 79), ("lcasCrcError", 80), ("nonLcasSequenceError", 81), ("rxLowOrderGroupIdMismatch", 82), ("rxHighOrderGroupIdMismatch", 83), ("rxLowOrderDifferentialDelay", 84), ("rxHighOrderDifferentialDelay", 85), ("rxLowOrderDifferentialDelayAllVT", 86), ("rxHighOrderDifferentialDelayAllVT", 87), ("txFifoOverflow", 88), ("rxFifoOverflow", 89), ("emailServiceAlarm", 90), ("licenseMissing", 91), ("licenseInvalid", 92), ("licenseWrongHostId", 93), ("licenseMaxNetworkNodesExceeded", 94), ("alarmFilteringParseError", 95), ("iadNoCOS", 96)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: probableCause.setStatus('current')
if mibBuilder.loadTexts: probableCause.setDescription('')
probableCauseText = MibScalar((1, 3, 6, 1, 4, 1, 6368, 2, 5, 1, 5), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: probableCauseText.setStatus('current')
if mibBuilder.loadTexts: probableCauseText.setDescription('')
perceivedSeverity = MibScalar((1, 3, 6, 1, 4, 1, 6368, 2, 5, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("critical", 1), ("major", 2), ("minor", 3), ("warning", 4), ("cleared", 5), ("indeterminate", 6)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: perceivedSeverity.setStatus('current')
if mibBuilder.loadTexts: perceivedSeverity.setDescription('')
perceivedSeverityText = MibScalar((1, 3, 6, 1, 4, 1, 6368, 2, 5, 1, 7), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: perceivedSeverityText.setStatus('current')
if mibBuilder.loadTexts: perceivedSeverityText.setDescription('')
pegasusAlarm = NotificationType((1, 3, 6, 1, 4, 1, 6368, 2, 5, 2, 0, 1)).setObjects(("PEGASUS-LEAN-TRAP-MIB", "sender"), ("PEGASUS-LEAN-TRAP-MIB", "senderObjectName"), ("PEGASUS-LEAN-TRAP-MIB", "senderDescription"), ("PEGASUS-LEAN-TRAP-MIB", "probableCause"), ("PEGASUS-LEAN-TRAP-MIB", "probableCauseText"), ("PEGASUS-LEAN-TRAP-MIB", "perceivedSeverity"), ("PEGASUS-LEAN-TRAP-MIB", "perceivedSeverityText"))
if mibBuilder.loadTexts: pegasusAlarm.setStatus('current')
if mibBuilder.loadTexts: pegasusAlarm.setDescription('The perceivedSeverity changed since the last notification with\n         this probableCause for this sender. If the perceivedSeverity is\n         CLEARED, the alarm condition is no longer present.')
mibBuilder.exportSymbols("PEGASUS-LEAN-TRAP-MIB", perceivedSeverityText=perceivedSeverityText, pegasusLeanTrapModule=pegasusLeanTrapModule, perceivedSeverity=perceivedSeverity, PYSNMP_MODULE_ID=pegasusLeanTrapModule, senderDescription=senderDescription, senderObjectName=senderObjectName, leanTraps=leanTraps, leanTrapObjects=leanTrapObjects, pegasusAlarm=pegasusAlarm, probableCauseText=probableCauseText, probableCause=probableCause, leanNotifications=leanNotifications, sender=sender)
