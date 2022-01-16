#
# PySNMP MIB module IRT-DVBT-SINGLETRANSMITTER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/rs/IRT-DVBT-SINGLETRANSMITTER-MIB
# Produced by pysmi-1.1.8 at Sun Jan 16 00:43:52 2022
# On host fv-az42-839 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
eventCounter, mibRelease, eventPriority, eventTimeStamp = mibBuilder.importSymbols("IRT-COMMONVARBINDS-MIB", "eventCounter", "mibRelease", "eventPriority", "eventTimeStamp")
dvbT, PresentNotPresent, SelectManualAuto, MuteOk, WarningOK, Input1Input2, SelectOnOff, SFNMFN, LocalRemote, FaultOK, OkNotOk = mibBuilder.importSymbols("IRT-TRANSMITTER-SMI-MIB", "dvbT", "PresentNotPresent", "SelectManualAuto", "MuteOk", "WarningOK", "Input1Input2", "SelectOnOff", "SFNMFN", "LocalRemote", "FaultOK", "OkNotOk")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
sysName, sysDescr, sysLocation = mibBuilder.importSymbols("SNMPv2-MIB", "sysName", "sysDescr", "sysLocation")
Gauge32, Unsigned32, Counter32, MibIdentifier, TimeTicks, ObjectIdentity, Counter64, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, IpAddress, Bits, Integer32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Unsigned32", "Counter32", "MibIdentifier", "TimeTicks", "ObjectIdentity", "Counter64", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "IpAddress", "Bits", "Integer32", "NotificationType")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
dvbSingleTransmitter = ModuleIdentity((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1))
dvbSingleTransmitter.setRevisions(('2007-05-04 14:00', '2006-12-20 14:00', '2006-09-21 14:00', '2006-09-19 14:00', '2006-09-07 14:00',))
if mibBuilder.loadTexts: dvbSingleTransmitter.setLastUpdated('200705041400Z')
if mibBuilder.loadTexts: dvbSingleTransmitter.setOrganization('IRT for WORKING-GROUP-TC-MIB')
dvbEventsST = MibIdentifier((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 0))
dvbSTInputPreselectionEvent = NotificationType((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 0, 1)).setObjects(("SNMPv2-MIB", "sysDescr"), ("SNMPv2-MIB", "sysName"), ("SNMPv2-MIB", "sysLocation"), ("IRT-COMMONVARBINDS-MIB", "eventTimeStamp"), ("IRT-COMMONVARBINDS-MIB", "eventPriority"), ("IRT-COMMONVARBINDS-MIB", "eventCounter"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTInputPreselection"))
if mibBuilder.loadTexts: dvbSTInputPreselectionEvent.setStatus('current')
dvbSTInputAutomaticEvent = NotificationType((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 0, 2)).setObjects(("SNMPv2-MIB", "sysDescr"), ("SNMPv2-MIB", "sysName"), ("SNMPv2-MIB", "sysLocation"), ("IRT-COMMONVARBINDS-MIB", "eventTimeStamp"), ("IRT-COMMONVARBINDS-MIB", "eventPriority"), ("IRT-COMMONVARBINDS-MIB", "eventCounter"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTInputAutomatic"))
if mibBuilder.loadTexts: dvbSTInputAutomaticEvent.setStatus('current')
dvbSTTransmitterOpModeEvent = NotificationType((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 0, 3)).setObjects(("SNMPv2-MIB", "sysDescr"), ("SNMPv2-MIB", "sysName"), ("SNMPv2-MIB", "sysLocation"), ("IRT-COMMONVARBINDS-MIB", "eventTimeStamp"), ("IRT-COMMONVARBINDS-MIB", "eventPriority"), ("IRT-COMMONVARBINDS-MIB", "eventCounter"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTTransmitterOpMode"))
if mibBuilder.loadTexts: dvbSTTransmitterOpModeEvent.setStatus('current')
dvbSTRFPresentEvent = NotificationType((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 0, 4)).setObjects(("SNMPv2-MIB", "sysDescr"), ("SNMPv2-MIB", "sysName"), ("SNMPv2-MIB", "sysLocation"), ("IRT-COMMONVARBINDS-MIB", "eventTimeStamp"), ("IRT-COMMONVARBINDS-MIB", "eventPriority"), ("IRT-COMMONVARBINDS-MIB", "eventCounter"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTRFPresent"))
if mibBuilder.loadTexts: dvbSTRFPresentEvent.setStatus('current')
dvbSTResetFaultEvent = NotificationType((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 0, 5)).setObjects(("SNMPv2-MIB", "sysDescr"), ("SNMPv2-MIB", "sysName"), ("SNMPv2-MIB", "sysLocation"), ("IRT-COMMONVARBINDS-MIB", "eventTimeStamp"), ("IRT-COMMONVARBINDS-MIB", "eventPriority"), ("IRT-COMMONVARBINDS-MIB", "eventCounter"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTResetFault"))
if mibBuilder.loadTexts: dvbSTResetFaultEvent.setStatus('obsolete')
dvbSTFaultEvent = NotificationType((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 0, 6)).setObjects(("SNMPv2-MIB", "sysDescr"), ("SNMPv2-MIB", "sysName"), ("SNMPv2-MIB", "sysLocation"), ("IRT-COMMONVARBINDS-MIB", "eventTimeStamp"), ("IRT-COMMONVARBINDS-MIB", "eventPriority"), ("IRT-COMMONVARBINDS-MIB", "eventCounter"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTFault"))
if mibBuilder.loadTexts: dvbSTFaultEvent.setStatus('current')
dvbSTWarningEvent = NotificationType((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 0, 7)).setObjects(("SNMPv2-MIB", "sysDescr"), ("SNMPv2-MIB", "sysName"), ("SNMPv2-MIB", "sysLocation"), ("IRT-COMMONVARBINDS-MIB", "eventTimeStamp"), ("IRT-COMMONVARBINDS-MIB", "eventPriority"), ("IRT-COMMONVARBINDS-MIB", "eventCounter"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTWarning"))
if mibBuilder.loadTexts: dvbSTWarningEvent.setStatus('current')
dvbSTInput1OKEvent = NotificationType((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 0, 8)).setObjects(("SNMPv2-MIB", "sysDescr"), ("SNMPv2-MIB", "sysName"), ("SNMPv2-MIB", "sysLocation"), ("IRT-COMMONVARBINDS-MIB", "eventTimeStamp"), ("IRT-COMMONVARBINDS-MIB", "eventPriority"), ("IRT-COMMONVARBINDS-MIB", "eventCounter"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTInput1OK"))
if mibBuilder.loadTexts: dvbSTInput1OKEvent.setStatus('current')
dvbSTInput2OKEvent = NotificationType((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 0, 9)).setObjects(("SNMPv2-MIB", "sysDescr"), ("SNMPv2-MIB", "sysName"), ("SNMPv2-MIB", "sysLocation"), ("IRT-COMMONVARBINDS-MIB", "eventTimeStamp"), ("IRT-COMMONVARBINDS-MIB", "eventPriority"), ("IRT-COMMONVARBINDS-MIB", "eventCounter"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTInput2OK"))
if mibBuilder.loadTexts: dvbSTInput2OKEvent.setStatus('current')
dvbSTLocalModeEvent = NotificationType((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 0, 10)).setObjects(("SNMPv2-MIB", "sysDescr"), ("SNMPv2-MIB", "sysName"), ("SNMPv2-MIB", "sysLocation"), ("IRT-COMMONVARBINDS-MIB", "eventTimeStamp"), ("IRT-COMMONVARBINDS-MIB", "eventPriority"), ("IRT-COMMONVARBINDS-MIB", "eventCounter"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTLocalMode"))
if mibBuilder.loadTexts: dvbSTLocalModeEvent.setStatus('current')
dvbSTActiveInputEvent = NotificationType((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 0, 11)).setObjects(("SNMPv2-MIB", "sysDescr"), ("SNMPv2-MIB", "sysName"), ("SNMPv2-MIB", "sysLocation"), ("IRT-COMMONVARBINDS-MIB", "eventTimeStamp"), ("IRT-COMMONVARBINDS-MIB", "eventPriority"), ("IRT-COMMONVARBINDS-MIB", "eventCounter"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTActiveInput"))
if mibBuilder.loadTexts: dvbSTActiveInputEvent.setStatus('current')
dvbSTSFNModeEvent = NotificationType((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 0, 12)).setObjects(("SNMPv2-MIB", "sysDescr"), ("SNMPv2-MIB", "sysName"), ("SNMPv2-MIB", "sysLocation"), ("IRT-COMMONVARBINDS-MIB", "eventTimeStamp"), ("IRT-COMMONVARBINDS-MIB", "eventPriority"), ("IRT-COMMONVARBINDS-MIB", "eventCounter"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTSFNMode"))
if mibBuilder.loadTexts: dvbSTSFNModeEvent.setStatus('current')
dvbSTRefFaultEvent = NotificationType((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 0, 13)).setObjects(("SNMPv2-MIB", "sysDescr"), ("SNMPv2-MIB", "sysName"), ("SNMPv2-MIB", "sysLocation"), ("IRT-COMMONVARBINDS-MIB", "eventTimeStamp"), ("IRT-COMMONVARBINDS-MIB", "eventPriority"), ("IRT-COMMONVARBINDS-MIB", "eventCounter"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTRefFault"))
if mibBuilder.loadTexts: dvbSTRefFaultEvent.setStatus('current')
dvbSTMuteEvent = NotificationType((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 0, 14)).setObjects(("SNMPv2-MIB", "sysDescr"), ("SNMPv2-MIB", "sysName"), ("SNMPv2-MIB", "sysLocation"), ("IRT-COMMONVARBINDS-MIB", "eventTimeStamp"), ("IRT-COMMONVARBINDS-MIB", "eventPriority"), ("IRT-COMMONVARBINDS-MIB", "eventCounter"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTMute"))
if mibBuilder.loadTexts: dvbSTMuteEvent.setStatus('current')
dvbSTFaultMIPEvent = NotificationType((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 0, 15)).setObjects(("SNMPv2-MIB", "sysDescr"), ("SNMPv2-MIB", "sysName"), ("SNMPv2-MIB", "sysLocation"), ("IRT-COMMONVARBINDS-MIB", "eventTimeStamp"), ("IRT-COMMONVARBINDS-MIB", "eventPriority"), ("IRT-COMMONVARBINDS-MIB", "eventCounter"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTFaultMIP"))
if mibBuilder.loadTexts: dvbSTFaultMIPEvent.setStatus('current')
dvbSTStuffingModeEvent = NotificationType((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 0, 16)).setObjects(("SNMPv2-MIB", "sysDescr"), ("SNMPv2-MIB", "sysName"), ("SNMPv2-MIB", "sysLocation"), ("IRT-COMMONVARBINDS-MIB", "eventTimeStamp"), ("IRT-COMMONVARBINDS-MIB", "eventPriority"), ("IRT-COMMONVARBINDS-MIB", "eventCounter"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTStuffingMode"))
if mibBuilder.loadTexts: dvbSTStuffingModeEvent.setStatus('current')
dvbSTGeneral = MibIdentifier((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 1))
dvbSTInputPreselection = MibScalar((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 1, 1), Input1Input2()).setUnits(' ').setMaxAccess("readwrite")
if mibBuilder.loadTexts: dvbSTInputPreselection.setStatus('current')
dvbSTInputAutomatic = MibScalar((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 1, 2), SelectManualAuto()).setUnits(' ').setMaxAccess("readwrite")
if mibBuilder.loadTexts: dvbSTInputAutomatic.setStatus('current')
dvbSTTransmitterOpMode = MibScalar((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 1, 3), SelectOnOff()).setUnits(' ').setMaxAccess("readwrite")
if mibBuilder.loadTexts: dvbSTTransmitterOpMode.setStatus('current')
dvbSTRFPresent = MibScalar((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 1, 4), PresentNotPresent()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvbSTRFPresent.setStatus('current')
dvbSTResetFault = MibScalar((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 1, 5), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dvbSTResetFault.setStatus('obsolete')
dvbSTFault = MibScalar((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 1, 6), FaultOK()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvbSTFault.setStatus('current')
dvbSTWarning = MibScalar((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 1, 7), WarningOK()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvbSTWarning.setStatus('current')
dvbSTInput1OK = MibScalar((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 1, 8), OkNotOk()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvbSTInput1OK.setStatus('current')
dvbSTInput2OK = MibScalar((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 1, 9), OkNotOk()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvbSTInput2OK.setStatus('current')
dvbSTLocalMode = MibScalar((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 1, 10), LocalRemote()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvbSTLocalMode.setStatus('current')
dvbSTActiveInput = MibScalar((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("undefined", 0), ("input1", 1), ("input2", 2), ("seamless", 3), ("hmHierarchicalModulation", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvbSTActiveInput.setStatus('current')
dvbSTSFNMode = MibScalar((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 1, 12), SFNMFN()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvbSTSFNMode.setStatus('current')
dvbSTRefFault = MibScalar((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 1, 13), FaultOK()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvbSTRefFault.setStatus('current')
dvbSTMute = MibScalar((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 1, 14), MuteOk()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvbSTMute.setStatus('current')
dvbSTFaultMIP = MibScalar((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 1, 15), FaultOK()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvbSTFaultMIP.setStatus('current')
dvbSTStuffingMode = MibScalar((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 1, 16), SelectOnOff()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvbSTStuffingMode.setStatus('current')
dvbSTEventEnable = MibIdentifier((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 2))
dvbSTEventEnableGeneral = MibIdentifier((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 2, 1))
dvbSTInputPreselectionEnable = MibScalar((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 2, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dvbSTInputPreselectionEnable.setStatus('current')
dvbSTInputAutomaticEnable = MibScalar((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 2, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dvbSTInputAutomaticEnable.setStatus('current')
dvbSTTransmitterOpModeEnable = MibScalar((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 2, 1, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dvbSTTransmitterOpModeEnable.setStatus('current')
dvbSTRFPresentEnable = MibScalar((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 2, 1, 4), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dvbSTRFPresentEnable.setStatus('current')
dvbSTResetFaultEnable = MibScalar((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 2, 1, 5), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dvbSTResetFaultEnable.setStatus('obsolete')
dvbSTFaultEnable = MibScalar((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 2, 1, 6), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dvbSTFaultEnable.setStatus('current')
dvbSTWarningEnable = MibScalar((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 2, 1, 7), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dvbSTWarningEnable.setStatus('current')
dvbSTInput1OKEnable = MibScalar((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 2, 1, 8), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dvbSTInput1OKEnable.setStatus('current')
dvbSTInput2OKEnable = MibScalar((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 2, 1, 9), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dvbSTInput2OKEnable.setStatus('current')
dvbSTLocalModeEnable = MibScalar((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 2, 1, 10), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dvbSTLocalModeEnable.setStatus('current')
dvbSTActiveInputEnable = MibScalar((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 2, 1, 11), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dvbSTActiveInputEnable.setStatus('current')
dvbSTSFNModeEnable = MibScalar((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 2, 1, 12), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dvbSTSFNModeEnable.setStatus('current')
dvbSTRefFaultEnable = MibScalar((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 2, 1, 13), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dvbSTRefFaultEnable.setStatus('current')
dvbSTMuteEnable = MibScalar((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 2, 1, 14), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dvbSTMuteEnable.setStatus('current')
dvbSTFaultMIPEnable = MibScalar((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 2, 1, 15), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dvbSTFaultMIPEnable.setStatus('current')
dvbSTStuffingModeEnable = MibScalar((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 2, 1, 16), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dvbSTStuffingModeEnable.setStatus('current')
dvbSTEventPriority = MibIdentifier((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 3))
dvbSTEventPriorityGeneral = MibIdentifier((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 3, 1))
dvbSTInputPreselectionPriority = MibScalar((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 3, 1, 1), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dvbSTInputPreselectionPriority.setStatus('current')
dvbSTInputAutomaticPriority = MibScalar((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 3, 1, 2), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dvbSTInputAutomaticPriority.setStatus('current')
dvbSTTransmitterOpModePriority = MibScalar((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 3, 1, 3), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dvbSTTransmitterOpModePriority.setStatus('current')
dvbSTRFPresentPriority = MibScalar((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 3, 1, 4), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dvbSTRFPresentPriority.setStatus('current')
dvbSTResetFaultPriority = MibScalar((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 3, 1, 5), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dvbSTResetFaultPriority.setStatus('obsolete')
dvbSTFaultPriority = MibScalar((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 3, 1, 6), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dvbSTFaultPriority.setStatus('current')
dvbSTWarningPriority = MibScalar((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 3, 1, 7), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dvbSTWarningPriority.setStatus('current')
dvbSTInput1OKPriority = MibScalar((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 3, 1, 8), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dvbSTInput1OKPriority.setStatus('current')
dvbSTInput2OKPriority = MibScalar((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 3, 1, 9), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dvbSTInput2OKPriority.setStatus('current')
dvbSTLocalModePriority = MibScalar((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 3, 1, 10), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dvbSTLocalModePriority.setStatus('current')
dvbSTActiveInputPriority = MibScalar((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 3, 1, 11), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dvbSTActiveInputPriority.setStatus('current')
dvbSTSFNModePriority = MibScalar((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 3, 1, 12), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dvbSTSFNModePriority.setStatus('current')
dvbSTRefFaultPriority = MibScalar((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 3, 1, 13), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dvbSTRefFaultPriority.setStatus('current')
dvbSTMutePriority = MibScalar((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 3, 1, 14), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dvbSTMutePriority.setStatus('current')
dvbSTFaultMIPPriority = MibScalar((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 3, 1, 15), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dvbSTFaultMIPPriority.setStatus('current')
dvbSTStuffingModePriority = MibScalar((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 3, 1, 16), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dvbSTStuffingModePriority.setStatus('current')
groupST = MibIdentifier((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 4))
objectGroupST = ObjectGroup((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 4, 1)).setObjects(("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTInputPreselection"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTInputAutomatic"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTTransmitterOpMode"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTRFPresent"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTFault"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTWarning"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTInput1OK"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTInput2OK"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTLocalMode"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTActiveInput"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTSFNMode"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTRefFault"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTMute"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTFaultMIP"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTStuffingMode"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTInputPreselectionEnable"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTInputAutomaticEnable"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTTransmitterOpModeEnable"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTRFPresentEnable"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTFaultEnable"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTWarningEnable"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTInput1OKEnable"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTInput2OKEnable"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTLocalModeEnable"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTActiveInputEnable"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTSFNModeEnable"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTRefFaultEnable"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTMuteEnable"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTFaultMIPEnable"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTStuffingModeEnable"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTInputPreselectionPriority"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTInputAutomaticPriority"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTTransmitterOpModePriority"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTRFPresentPriority"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTFaultPriority"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTWarningPriority"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTFaultMIPPriority"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTMutePriority"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTRefFaultPriority"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTSFNModePriority"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTStuffingModePriority"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTInput1OKPriority"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTInput2OKPriority"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTLocalModePriority"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTActiveInputPriority"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    objectGroupST = objectGroupST.setStatus('current')
eventGroupST = NotificationGroup((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 4, 2)).setObjects(("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTInputPreselectionEvent"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTInputAutomaticEvent"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTTransmitterOpModeEvent"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTRFPresentEvent"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTFaultEvent"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTWarningEvent"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTInput1OKEvent"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTInput2OKEvent"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTLocalModeEvent"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTActiveInputEvent"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTSFNModeEvent"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTRefFaultEvent"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTStuffingModeEvent"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTMuteEvent"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTFaultMIPEvent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    eventGroupST = eventGroupST.setStatus('current')
objectGroupSTobsolete = ObjectGroup((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 4, 3)).setObjects(("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTResetFault"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTResetFaultEnable"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTResetFaultPriority"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    objectGroupSTobsolete = objectGroupSTobsolete.setStatus('obsolete')
eventGroupSTobsolete = NotificationGroup((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 4, 4)).setObjects(("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTResetFaultEvent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    eventGroupSTobsolete = eventGroupSTobsolete.setStatus('obsolete')
complianceST = MibIdentifier((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 5))
dvbSingleTransmitterCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 5, 1)).setObjects(("IRT-DVBT-SINGLETRANSMITTER-MIB", "objectGroupST"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "eventGroupST"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dvbSingleTransmitterCompliance = dvbSingleTransmitterCompliance.setStatus('current')
mibBuilder.exportSymbols("IRT-DVBT-SINGLETRANSMITTER-MIB", dvbSTStuffingModeEvent=dvbSTStuffingModeEvent, PYSNMP_MODULE_ID=dvbSingleTransmitter, dvbSTMute=dvbSTMute, dvbSTActiveInputEvent=dvbSTActiveInputEvent, dvbSTWarningPriority=dvbSTWarningPriority, dvbSTRFPresentEvent=dvbSTRFPresentEvent, dvbSTFault=dvbSTFault, dvbSTEventPriority=dvbSTEventPriority, dvbSTFaultMIPEvent=dvbSTFaultMIPEvent, dvbSTInputAutomaticPriority=dvbSTInputAutomaticPriority, dvbSTLocalMode=dvbSTLocalMode, dvbSTInput1OKPriority=dvbSTInput1OKPriority, dvbSTInput2OK=dvbSTInput2OK, dvbSTRefFault=dvbSTRefFault, dvbSTSFNMode=dvbSTSFNMode, dvbSTStuffingModePriority=dvbSTStuffingModePriority, dvbSTInput2OKEvent=dvbSTInput2OKEvent, dvbSTSFNModePriority=dvbSTSFNModePriority, dvbSTInputPreselection=dvbSTInputPreselection, dvbSTInput1OKEnable=dvbSTInput1OKEnable, dvbEventsST=dvbEventsST, dvbSTActiveInputPriority=dvbSTActiveInputPriority, dvbSTMutePriority=dvbSTMutePriority, dvbSTStuffingModeEnable=dvbSTStuffingModeEnable, dvbSTInput1OKEvent=dvbSTInput1OKEvent, dvbSTInput1OK=dvbSTInput1OK, dvbSTRefFaultEvent=dvbSTRefFaultEvent, dvbSTResetFaultEnable=dvbSTResetFaultEnable, dvbSTInputPreselectionPriority=dvbSTInputPreselectionPriority, dvbSTEventEnable=dvbSTEventEnable, dvbSTInput2OKEnable=dvbSTInput2OKEnable, dvbSTActiveInputEnable=dvbSTActiveInputEnable, dvbSTFaultPriority=dvbSTFaultPriority, dvbSTInput2OKPriority=dvbSTInput2OKPriority, objectGroupST=objectGroupST, dvbSTFaultMIP=dvbSTFaultMIP, complianceST=complianceST, dvbSTSFNModeEvent=dvbSTSFNModeEvent, dvbSTFaultEnable=dvbSTFaultEnable, dvbSTWarningEvent=dvbSTWarningEvent, dvbSTStuffingMode=dvbSTStuffingMode, dvbSTTransmitterOpModeEvent=dvbSTTransmitterOpModeEvent, dvbSTTransmitterOpModeEnable=dvbSTTransmitterOpModeEnable, dvbSTLocalModeEvent=dvbSTLocalModeEvent, dvbSTResetFault=dvbSTResetFault, dvbSTWarning=dvbSTWarning, dvbSTMuteEvent=dvbSTMuteEvent, dvbSTInputAutomaticEvent=dvbSTInputAutomaticEvent, eventGroupSTobsolete=eventGroupSTobsolete, eventGroupST=eventGroupST, dvbSTEventPriorityGeneral=dvbSTEventPriorityGeneral, dvbSTInputAutomaticEnable=dvbSTInputAutomaticEnable, objectGroupSTobsolete=objectGroupSTobsolete, dvbSTRFPresentEnable=dvbSTRFPresentEnable, dvbSTRefFaultEnable=dvbSTRefFaultEnable, dvbSTFaultMIPEnable=dvbSTFaultMIPEnable, dvbSTActiveInput=dvbSTActiveInput, dvbSTTransmitterOpMode=dvbSTTransmitterOpMode, dvbSTInputPreselectionEnable=dvbSTInputPreselectionEnable, dvbSTInputAutomatic=dvbSTInputAutomatic, dvbSTRFPresentPriority=dvbSTRFPresentPriority, groupST=groupST, dvbSTResetFaultEvent=dvbSTResetFaultEvent, dvbSTMuteEnable=dvbSTMuteEnable, dvbSTLocalModePriority=dvbSTLocalModePriority, dvbSTWarningEnable=dvbSTWarningEnable, dvbSTLocalModeEnable=dvbSTLocalModeEnable, dvbSTEventEnableGeneral=dvbSTEventEnableGeneral, dvbSTTransmitterOpModePriority=dvbSTTransmitterOpModePriority, dvbSTResetFaultPriority=dvbSTResetFaultPriority, dvbSTRefFaultPriority=dvbSTRefFaultPriority, dvbSTFaultMIPPriority=dvbSTFaultMIPPriority, dvbSTFaultEvent=dvbSTFaultEvent, dvbSingleTransmitterCompliance=dvbSingleTransmitterCompliance, dvbSingleTransmitter=dvbSingleTransmitter, dvbSTInputPreselectionEvent=dvbSTInputPreselectionEvent, dvbSTGeneral=dvbSTGeneral, dvbSTSFNModeEnable=dvbSTSFNModeEnable, dvbSTRFPresent=dvbSTRFPresent)
