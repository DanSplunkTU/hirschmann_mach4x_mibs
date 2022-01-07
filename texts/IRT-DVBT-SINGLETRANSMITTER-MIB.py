#
# PySNMP MIB module IRT-DVBT-SINGLETRANSMITTER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/rs/IRT-DVBT-SINGLETRANSMITTER-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:37:06 2022
# On host fv-az36-988 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
eventCounter, eventPriority, mibRelease, eventTimeStamp = mibBuilder.importSymbols("IRT-COMMONVARBINDS-MIB", "eventCounter", "eventPriority", "mibRelease", "eventTimeStamp")
MuteOk, LocalRemote, dvbT, Input1Input2, OkNotOk, SFNMFN, FaultOK, WarningOK, PresentNotPresent, SelectManualAuto, SelectOnOff = mibBuilder.importSymbols("IRT-TRANSMITTER-SMI-MIB", "MuteOk", "LocalRemote", "dvbT", "Input1Input2", "OkNotOk", "SFNMFN", "FaultOK", "WarningOK", "PresentNotPresent", "SelectManualAuto", "SelectOnOff")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
sysLocation, sysName, sysDescr = mibBuilder.importSymbols("SNMPv2-MIB", "sysLocation", "sysName", "sysDescr")
MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Gauge32, Integer32, Counter64, NotificationType, Counter32, IpAddress, ModuleIdentity, TimeTicks, Bits, ObjectIdentity, iso, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Gauge32", "Integer32", "Counter64", "NotificationType", "Counter32", "IpAddress", "ModuleIdentity", "TimeTicks", "Bits", "ObjectIdentity", "iso", "Unsigned32")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
dvbSingleTransmitter = ModuleIdentity((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1))
dvbSingleTransmitter.setRevisions(('2007-05-04 14:00', '2006-12-20 14:00', '2006-09-21 14:00', '2006-09-19 14:00', '2006-09-07 14:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: dvbSingleTransmitter.setRevisionsDescriptions(('change SFNMode,LocalMode (description) and Module-COMPLIANCE', 'Corrections', 'Adding Compliance Statement', 'Correcting Imports', 'Relocation of the TC-MIB from the standard OID area at IEC into the private OID area of the IRT',))
if mibBuilder.loadTexts: dvbSingleTransmitter.setLastUpdated('200705041400Z')
if mibBuilder.loadTexts: dvbSingleTransmitter.setOrganization('IRT for WORKING-GROUP-TC-MIB')
if mibBuilder.loadTexts: dvbSingleTransmitter.setContactInfo('Contact-info.\n\t\t\t\t\n\t\t\t\tAndreas Metz\n\t\t\t\t\n\t\t\t\tInstitut fuer Rundfunktechnik GmbH\n\t\t\t\tBroadcast Networks and Servers (SN)\n\t\t\t\t\n\t\t\t\tFloriansmuehlstr.60\n\t\t\t\t80939 Munich\n\t\t\t\tGermany\n\t\t\t\t\n\t\t\t\tPhone: +49 89 32399 325\n\t\t\t\tFax: +49 89 32399 354\n\t\t\t\t')
if mibBuilder.loadTexts: dvbSingleTransmitter.setDescription('DVB Single Transmitter\n\t\t\t\t\n\t\t\t\tbranch definition\n\t\t\t\t\n\t\t\t\t1st level\n\t\t\t\t\n\t\t\t\tevents               OBJECT IDENTIFIER ::= { dvbSingleTransmitter 0 }\n\t\t\t\tdvbSTGeneral         OBJECT IDENTIFIER ::= { dvbSingleTransmitter 1 }\n\t\t\t\tdvbSTEventEnable     OBJECT IDENTIFIER ::= { dvbSingleTransmitter 2 }\n\t\t\t\tdvbSTEventPriority   OBJECT IDENTIFIER ::= { dvbSingleTransmitter 3 }\n\t\t\t\tgroups               OBJECT IDENTIFIER ::= { dvbSingleTransmitter 4 }\n\t\t\t\t\n\t\t\t\t2nd level\n\t\t\t\t\n\t\t\t\tdvbSTEventEnableGeneral     OBJECT IDENTIFIER ::= { dvbSTEventEnable 1 }\n\t\t\t\tdvbSTEventPriorityGeneral   OBJECT IDENTIFIER ::= { dvbSTEventPriority 1 }\n\t\t\t\t\n\t\t\t\tend branch\n\t\t\t\t\n\t\t\t\t')
dvbEventsST = MibIdentifier((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 0))
dvbSTInputPreselectionEvent = NotificationType((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 0, 1)).setObjects(("SNMPv2-MIB", "sysDescr"), ("SNMPv2-MIB", "sysName"), ("SNMPv2-MIB", "sysLocation"), ("IRT-COMMONVARBINDS-MIB", "eventTimeStamp"), ("IRT-COMMONVARBINDS-MIB", "eventPriority"), ("IRT-COMMONVARBINDS-MIB", "eventCounter"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTInputPreselection"))
if mibBuilder.loadTexts: dvbSTInputPreselectionEvent.setStatus('current')
if mibBuilder.loadTexts: dvbSTInputPreselectionEvent.setDescription('Description.dvbSTInputPreselection notification')
dvbSTInputAutomaticEvent = NotificationType((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 0, 2)).setObjects(("SNMPv2-MIB", "sysDescr"), ("SNMPv2-MIB", "sysName"), ("SNMPv2-MIB", "sysLocation"), ("IRT-COMMONVARBINDS-MIB", "eventTimeStamp"), ("IRT-COMMONVARBINDS-MIB", "eventPriority"), ("IRT-COMMONVARBINDS-MIB", "eventCounter"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTInputAutomatic"))
if mibBuilder.loadTexts: dvbSTInputAutomaticEvent.setStatus('current')
if mibBuilder.loadTexts: dvbSTInputAutomaticEvent.setDescription('Description. dvbSTInputAutomatic notification')
dvbSTTransmitterOpModeEvent = NotificationType((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 0, 3)).setObjects(("SNMPv2-MIB", "sysDescr"), ("SNMPv2-MIB", "sysName"), ("SNMPv2-MIB", "sysLocation"), ("IRT-COMMONVARBINDS-MIB", "eventTimeStamp"), ("IRT-COMMONVARBINDS-MIB", "eventPriority"), ("IRT-COMMONVARBINDS-MIB", "eventCounter"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTTransmitterOpMode"))
if mibBuilder.loadTexts: dvbSTTransmitterOpModeEvent.setStatus('current')
if mibBuilder.loadTexts: dvbSTTransmitterOpModeEvent.setDescription('Description. dvbSTTransmitterOpMode notification')
dvbSTRFPresentEvent = NotificationType((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 0, 4)).setObjects(("SNMPv2-MIB", "sysDescr"), ("SNMPv2-MIB", "sysName"), ("SNMPv2-MIB", "sysLocation"), ("IRT-COMMONVARBINDS-MIB", "eventTimeStamp"), ("IRT-COMMONVARBINDS-MIB", "eventPriority"), ("IRT-COMMONVARBINDS-MIB", "eventCounter"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTRFPresent"))
if mibBuilder.loadTexts: dvbSTRFPresentEvent.setStatus('current')
if mibBuilder.loadTexts: dvbSTRFPresentEvent.setDescription('Description. dvbSTRFPresent notification')
dvbSTResetFaultEvent = NotificationType((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 0, 5)).setObjects(("SNMPv2-MIB", "sysDescr"), ("SNMPv2-MIB", "sysName"), ("SNMPv2-MIB", "sysLocation"), ("IRT-COMMONVARBINDS-MIB", "eventTimeStamp"), ("IRT-COMMONVARBINDS-MIB", "eventPriority"), ("IRT-COMMONVARBINDS-MIB", "eventCounter"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTResetFault"))
if mibBuilder.loadTexts: dvbSTResetFaultEvent.setStatus('obsolete')
if mibBuilder.loadTexts: dvbSTResetFaultEvent.setDescription('Notification is inctive!\n\t\t\t\t\n\t\t\t\tDescription.dvbSTResetFault notification')
dvbSTFaultEvent = NotificationType((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 0, 6)).setObjects(("SNMPv2-MIB", "sysDescr"), ("SNMPv2-MIB", "sysName"), ("SNMPv2-MIB", "sysLocation"), ("IRT-COMMONVARBINDS-MIB", "eventTimeStamp"), ("IRT-COMMONVARBINDS-MIB", "eventPriority"), ("IRT-COMMONVARBINDS-MIB", "eventCounter"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTFault"))
if mibBuilder.loadTexts: dvbSTFaultEvent.setStatus('current')
if mibBuilder.loadTexts: dvbSTFaultEvent.setDescription('Description. dvbSTFault notification')
dvbSTWarningEvent = NotificationType((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 0, 7)).setObjects(("SNMPv2-MIB", "sysDescr"), ("SNMPv2-MIB", "sysName"), ("SNMPv2-MIB", "sysLocation"), ("IRT-COMMONVARBINDS-MIB", "eventTimeStamp"), ("IRT-COMMONVARBINDS-MIB", "eventPriority"), ("IRT-COMMONVARBINDS-MIB", "eventCounter"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTWarning"))
if mibBuilder.loadTexts: dvbSTWarningEvent.setStatus('current')
if mibBuilder.loadTexts: dvbSTWarningEvent.setDescription('Description. dvbSTWarning notification')
dvbSTInput1OKEvent = NotificationType((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 0, 8)).setObjects(("SNMPv2-MIB", "sysDescr"), ("SNMPv2-MIB", "sysName"), ("SNMPv2-MIB", "sysLocation"), ("IRT-COMMONVARBINDS-MIB", "eventTimeStamp"), ("IRT-COMMONVARBINDS-MIB", "eventPriority"), ("IRT-COMMONVARBINDS-MIB", "eventCounter"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTInput1OK"))
if mibBuilder.loadTexts: dvbSTInput1OKEvent.setStatus('current')
if mibBuilder.loadTexts: dvbSTInput1OKEvent.setDescription('Description.vdvbSTInput1OK notification')
dvbSTInput2OKEvent = NotificationType((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 0, 9)).setObjects(("SNMPv2-MIB", "sysDescr"), ("SNMPv2-MIB", "sysName"), ("SNMPv2-MIB", "sysLocation"), ("IRT-COMMONVARBINDS-MIB", "eventTimeStamp"), ("IRT-COMMONVARBINDS-MIB", "eventPriority"), ("IRT-COMMONVARBINDS-MIB", "eventCounter"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTInput2OK"))
if mibBuilder.loadTexts: dvbSTInput2OKEvent.setStatus('current')
if mibBuilder.loadTexts: dvbSTInput2OKEvent.setDescription('Description.dvbSTInput2OK notification')
dvbSTLocalModeEvent = NotificationType((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 0, 10)).setObjects(("SNMPv2-MIB", "sysDescr"), ("SNMPv2-MIB", "sysName"), ("SNMPv2-MIB", "sysLocation"), ("IRT-COMMONVARBINDS-MIB", "eventTimeStamp"), ("IRT-COMMONVARBINDS-MIB", "eventPriority"), ("IRT-COMMONVARBINDS-MIB", "eventCounter"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTLocalMode"))
if mibBuilder.loadTexts: dvbSTLocalModeEvent.setStatus('current')
if mibBuilder.loadTexts: dvbSTLocalModeEvent.setDescription('Description. dvbSTLocalMode notification')
dvbSTActiveInputEvent = NotificationType((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 0, 11)).setObjects(("SNMPv2-MIB", "sysDescr"), ("SNMPv2-MIB", "sysName"), ("SNMPv2-MIB", "sysLocation"), ("IRT-COMMONVARBINDS-MIB", "eventTimeStamp"), ("IRT-COMMONVARBINDS-MIB", "eventPriority"), ("IRT-COMMONVARBINDS-MIB", "eventCounter"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTActiveInput"))
if mibBuilder.loadTexts: dvbSTActiveInputEvent.setStatus('current')
if mibBuilder.loadTexts: dvbSTActiveInputEvent.setDescription('Description. dvbSTActiveInput notification')
dvbSTSFNModeEvent = NotificationType((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 0, 12)).setObjects(("SNMPv2-MIB", "sysDescr"), ("SNMPv2-MIB", "sysName"), ("SNMPv2-MIB", "sysLocation"), ("IRT-COMMONVARBINDS-MIB", "eventTimeStamp"), ("IRT-COMMONVARBINDS-MIB", "eventPriority"), ("IRT-COMMONVARBINDS-MIB", "eventCounter"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTSFNMode"))
if mibBuilder.loadTexts: dvbSTSFNModeEvent.setStatus('current')
if mibBuilder.loadTexts: dvbSTSFNModeEvent.setDescription('Description. dvbSTSFNMode notification')
dvbSTRefFaultEvent = NotificationType((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 0, 13)).setObjects(("SNMPv2-MIB", "sysDescr"), ("SNMPv2-MIB", "sysName"), ("SNMPv2-MIB", "sysLocation"), ("IRT-COMMONVARBINDS-MIB", "eventTimeStamp"), ("IRT-COMMONVARBINDS-MIB", "eventPriority"), ("IRT-COMMONVARBINDS-MIB", "eventCounter"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTRefFault"))
if mibBuilder.loadTexts: dvbSTRefFaultEvent.setStatus('current')
if mibBuilder.loadTexts: dvbSTRefFaultEvent.setDescription('Description. dvbSTRefFault notification')
dvbSTMuteEvent = NotificationType((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 0, 14)).setObjects(("SNMPv2-MIB", "sysDescr"), ("SNMPv2-MIB", "sysName"), ("SNMPv2-MIB", "sysLocation"), ("IRT-COMMONVARBINDS-MIB", "eventTimeStamp"), ("IRT-COMMONVARBINDS-MIB", "eventPriority"), ("IRT-COMMONVARBINDS-MIB", "eventCounter"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTMute"))
if mibBuilder.loadTexts: dvbSTMuteEvent.setStatus('current')
if mibBuilder.loadTexts: dvbSTMuteEvent.setDescription('Description. dvbSTMute notification')
dvbSTFaultMIPEvent = NotificationType((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 0, 15)).setObjects(("SNMPv2-MIB", "sysDescr"), ("SNMPv2-MIB", "sysName"), ("SNMPv2-MIB", "sysLocation"), ("IRT-COMMONVARBINDS-MIB", "eventTimeStamp"), ("IRT-COMMONVARBINDS-MIB", "eventPriority"), ("IRT-COMMONVARBINDS-MIB", "eventCounter"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTFaultMIP"))
if mibBuilder.loadTexts: dvbSTFaultMIPEvent.setStatus('current')
if mibBuilder.loadTexts: dvbSTFaultMIPEvent.setDescription('Description. dvbSTFaultMIP notification')
dvbSTStuffingModeEvent = NotificationType((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 0, 16)).setObjects(("SNMPv2-MIB", "sysDescr"), ("SNMPv2-MIB", "sysName"), ("SNMPv2-MIB", "sysLocation"), ("IRT-COMMONVARBINDS-MIB", "eventTimeStamp"), ("IRT-COMMONVARBINDS-MIB", "eventPriority"), ("IRT-COMMONVARBINDS-MIB", "eventCounter"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTStuffingMode"))
if mibBuilder.loadTexts: dvbSTStuffingModeEvent.setStatus('current')
if mibBuilder.loadTexts: dvbSTStuffingModeEvent.setDescription('Description. dvbSTSStuffingMode notification')
dvbSTGeneral = MibIdentifier((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 1))
dvbSTInputPreselection = MibScalar((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 1, 1), Input1Input2()).setUnits(' ').setMaxAccess("readwrite")
if mibBuilder.loadTexts: dvbSTInputPreselection.setStatus('current')
if mibBuilder.loadTexts: dvbSTInputPreselection.setDescription('Single transmitter. Preselection input of single transmitter\n\t\t\t\t\n\t\t\t\t(0) undefined\n\t\t\t\t(1) Input 1\n\t\t\t\t(2) Input 2')
dvbSTInputAutomatic = MibScalar((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 1, 2), SelectManualAuto()).setUnits(' ').setMaxAccess("readwrite")
if mibBuilder.loadTexts: dvbSTInputAutomatic.setStatus('current')
if mibBuilder.loadTexts: dvbSTInputAutomatic.setDescription('Single transmitter. Input selection mode of single  transmitter:  manual or automatic\n\t\t\t\t\n\t\t\t\t(0) undefined\n\t\t\t\t(1) manual \n\t\t\t\t(2) automatic')
dvbSTTransmitterOpMode = MibScalar((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 1, 3), SelectOnOff()).setUnits(' ').setMaxAccess("readwrite")
if mibBuilder.loadTexts: dvbSTTransmitterOpMode.setStatus('current')
if mibBuilder.loadTexts: dvbSTTransmitterOpMode.setDescription('Single transmitter. Transmitter control of single  transmitter\n\t\t\t\t\n\t\t\t\t(0) undefined\n\t\t\t\t(1) ON\n\t\t\t\t(2) OFF')
dvbSTRFPresent = MibScalar((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 1, 4), PresentNotPresent()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvbSTRFPresent.setStatus('current')
if mibBuilder.loadTexts: dvbSTRFPresent.setDescription('Single  transmitter. Describes if  the output power is present\n\t\t\t\t\n\t\t\t\t(0) undefined\n\t\t\t\t(1) present\n\t\t\t\t(2) not present\n\t\t\t\t')
dvbSTResetFault = MibScalar((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 1, 5), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dvbSTResetFault.setStatus('obsolete')
if mibBuilder.loadTexts: dvbSTResetFault.setDescription('Description.  Massage is inctive!\n\t\t\t\t\n\t\t\t\t\n\t\t\t\tSingle  transmitter. Reset fault. Trigger for reset the sum fault\n\t\t\t\t\n\t\t\t\t<1>\n\t\t\t\t\n\t\t\t\t1: reset sum fault\n\t\t\t\t\n\t\t\t\t')
dvbSTFault = MibScalar((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 1, 6), FaultOK()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvbSTFault.setStatus('current')
if mibBuilder.loadTexts: dvbSTFault.setDescription('Single transmitter. Fault state of transmitter\n\t\t\t\t\n\t\t\t\t(0) undefined\n\t\t\t\t(1) fault\n\t\t\t\t(2) ok')
dvbSTWarning = MibScalar((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 1, 7), WarningOK()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvbSTWarning.setStatus('current')
if mibBuilder.loadTexts: dvbSTWarning.setDescription('Single transmitter. Warning state of single transmitter\n\t\t\t\t\n\t\t\t\t(0) undefined\n\t\t\t\t(1) warning\n\t\t\t\t(2) ok')
dvbSTInput1OK = MibScalar((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 1, 8), OkNotOk()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvbSTInput1OK.setStatus('current')
if mibBuilder.loadTexts: dvbSTInput1OK.setDescription('Single transmitter.Describes if the input signal at the input 1 of single transmitter  is ok\n\t\t\t\t\n\t\t\t\t(0) undefined\n\t\t\t\t(1) signal ok\n\t\t\t\t(2) signal is not ok ')
dvbSTInput2OK = MibScalar((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 1, 9), OkNotOk()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvbSTInput2OK.setStatus('current')
if mibBuilder.loadTexts: dvbSTInput2OK.setDescription('Describes if the input signal at the input 2 of single transmitters  is ok\n\t\t\t\t\n\t\t\t\t(0) undefined\n\t\t\t\t(1) signal ok\n\t\t\t\t(2) signal is not ok ')
dvbSTLocalMode = MibScalar((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 1, 10), LocalRemote()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvbSTLocalMode.setStatus('current')
if mibBuilder.loadTexts: dvbSTLocalMode.setDescription('Single transmitter. Local  mode\n\t\t\t\t\n\t\t\t\t(0) undefined\n\t\t\t\t(1) local\n\t\t\t\t(2) remote')
dvbSTActiveInput = MibScalar((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("undefined", 0), ("input1", 1), ("input2", 2), ("seamless", 3), ("hmHierarchicalModulation", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvbSTActiveInput.setStatus('current')
if mibBuilder.loadTexts: dvbSTActiveInput.setDescription('Single transmitter.Active input of the single transmitter \n\t\t\t\t\n\t\t\t\t')
dvbSTSFNMode = MibScalar((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 1, 12), SFNMFN()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvbSTSFNMode.setStatus('current')
if mibBuilder.loadTexts: dvbSTSFNMode.setDescription('Single transmitter. SFN mode of single transmitter \n\t\t\t\t\n\t\t\t\t(0) undefined\n\t\t\t\t(1) SFN\n\t\t\t\t(2) MFN\n\t\t\t\t\n\t\t\t\t\n\t\t\t\t')
dvbSTRefFault = MibScalar((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 1, 13), FaultOK()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvbSTRefFault.setStatus('current')
if mibBuilder.loadTexts: dvbSTRefFault.setDescription('Single transmitter.Fault state of the GPS input or the reference frequency of single transmitter \n\t\t\t\t\n\t\t\t\t(0) undefined\n\t\t\t\t(1) fault\n\t\t\t\t(2) ok')
dvbSTMute = MibScalar((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 1, 14), MuteOk()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvbSTMute.setStatus('current')
if mibBuilder.loadTexts: dvbSTMute.setDescription('Single transmitter. Mute state of single transmitter\n\t\t\t\t\n\t\t\t\t(0) undefined\n\t\t\t\t(1) mute\n\t\t\t\t(2) ok')
dvbSTFaultMIP = MibScalar((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 1, 15), FaultOK()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvbSTFaultMIP.setStatus('current')
if mibBuilder.loadTexts: dvbSTFaultMIP.setDescription('MIP fault state of single transmitter\n\t\t\t\t\n\t\t\t\t(0) undefined\n\t\t\t\t(1) fault\n\t\t\t\t(2) ok')
dvbSTStuffingMode = MibScalar((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 1, 16), SelectOnOff()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvbSTStuffingMode.setStatus('current')
if mibBuilder.loadTexts: dvbSTStuffingMode.setDescription('Stuffing state of single transmitter\n\t\t\t\t\n\t\t\t\t(0) undefined\n\t\t\t\t(1) ON \n\t\t\t\t(2) OFF ')
dvbSTEventEnable = MibIdentifier((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 2))
dvbSTEventEnableGeneral = MibIdentifier((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 2, 1))
dvbSTInputPreselectionEnable = MibScalar((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 2, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dvbSTInputPreselectionEnable.setStatus('current')
if mibBuilder.loadTexts: dvbSTInputPreselectionEnable.setDescription('Description.Enable/Disable switch for dvbSTInputPreselection event')
dvbSTInputAutomaticEnable = MibScalar((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 2, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dvbSTInputAutomaticEnable.setStatus('current')
if mibBuilder.loadTexts: dvbSTInputAutomaticEnable.setDescription('Description.Enable/Disable switch for dvbSTInputAutomatic event')
dvbSTTransmitterOpModeEnable = MibScalar((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 2, 1, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dvbSTTransmitterOpModeEnable.setStatus('current')
if mibBuilder.loadTexts: dvbSTTransmitterOpModeEnable.setDescription('Description.Enable/Disable switch for dvbSTTransmitterOpMode event')
dvbSTRFPresentEnable = MibScalar((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 2, 1, 4), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dvbSTRFPresentEnable.setStatus('current')
if mibBuilder.loadTexts: dvbSTRFPresentEnable.setDescription('Description.Enable/Disable switch for dvbSTRFPresent event')
dvbSTResetFaultEnable = MibScalar((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 2, 1, 5), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dvbSTResetFaultEnable.setStatus('obsolete')
if mibBuilder.loadTexts: dvbSTResetFaultEnable.setDescription('Massage ist inactive!\n\t\t\t\t\n\t\t\t\tDescription. Enable/Disable switch for dvbSTResetFault event')
dvbSTFaultEnable = MibScalar((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 2, 1, 6), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dvbSTFaultEnable.setStatus('current')
if mibBuilder.loadTexts: dvbSTFaultEnable.setDescription('Description.Enable/Disable switch for dvbSTFault event')
dvbSTWarningEnable = MibScalar((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 2, 1, 7), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dvbSTWarningEnable.setStatus('current')
if mibBuilder.loadTexts: dvbSTWarningEnable.setDescription('Description.Enable/Disable switch for dvbSTWarning event')
dvbSTInput1OKEnable = MibScalar((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 2, 1, 8), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dvbSTInput1OKEnable.setStatus('current')
if mibBuilder.loadTexts: dvbSTInput1OKEnable.setDescription('Description.Enable/Disable switch for dvbSTInput1OK event')
dvbSTInput2OKEnable = MibScalar((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 2, 1, 9), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dvbSTInput2OKEnable.setStatus('current')
if mibBuilder.loadTexts: dvbSTInput2OKEnable.setDescription('Description.Enable/Disable switch for dvbSTInput2OK event')
dvbSTLocalModeEnable = MibScalar((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 2, 1, 10), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dvbSTLocalModeEnable.setStatus('current')
if mibBuilder.loadTexts: dvbSTLocalModeEnable.setDescription('Description.Enable/Disable switch for dvbSTLocalMode event')
dvbSTActiveInputEnable = MibScalar((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 2, 1, 11), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dvbSTActiveInputEnable.setStatus('current')
if mibBuilder.loadTexts: dvbSTActiveInputEnable.setDescription('Description.Enable/Disable switch for dvbSTActiveInput event')
dvbSTSFNModeEnable = MibScalar((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 2, 1, 12), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dvbSTSFNModeEnable.setStatus('current')
if mibBuilder.loadTexts: dvbSTSFNModeEnable.setDescription('Description.Enable/Disable switch for dvbSTSFNMode event')
dvbSTRefFaultEnable = MibScalar((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 2, 1, 13), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dvbSTRefFaultEnable.setStatus('current')
if mibBuilder.loadTexts: dvbSTRefFaultEnable.setDescription('Description.Enable/Disable switch for dvbSTRefFault event')
dvbSTMuteEnable = MibScalar((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 2, 1, 14), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dvbSTMuteEnable.setStatus('current')
if mibBuilder.loadTexts: dvbSTMuteEnable.setDescription('Description.Enable/Disable switch for dvbSTMute event')
dvbSTFaultMIPEnable = MibScalar((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 2, 1, 15), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dvbSTFaultMIPEnable.setStatus('current')
if mibBuilder.loadTexts: dvbSTFaultMIPEnable.setDescription('Description.Enable/Disable switch for dvbSTFaultMIP event')
dvbSTStuffingModeEnable = MibScalar((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 2, 1, 16), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dvbSTStuffingModeEnable.setStatus('current')
if mibBuilder.loadTexts: dvbSTStuffingModeEnable.setDescription('Description.Enable/Disable switch for dvbSTStuffingMode event')
dvbSTEventPriority = MibIdentifier((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 3))
dvbSTEventPriorityGeneral = MibIdentifier((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 3, 1))
dvbSTInputPreselectionPriority = MibScalar((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 3, 1, 1), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dvbSTInputPreselectionPriority.setStatus('current')
if mibBuilder.loadTexts: dvbSTInputPreselectionPriority.setDescription('Description.Priority for dvbSTInputPreselection event')
dvbSTInputAutomaticPriority = MibScalar((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 3, 1, 2), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dvbSTInputAutomaticPriority.setStatus('current')
if mibBuilder.loadTexts: dvbSTInputAutomaticPriority.setDescription('Description.Priority for dvbSTInputAutomatic event')
dvbSTTransmitterOpModePriority = MibScalar((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 3, 1, 3), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dvbSTTransmitterOpModePriority.setStatus('current')
if mibBuilder.loadTexts: dvbSTTransmitterOpModePriority.setDescription('Description.Priority for dvbSTTransmitterOpMode event')
dvbSTRFPresentPriority = MibScalar((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 3, 1, 4), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dvbSTRFPresentPriority.setStatus('current')
if mibBuilder.loadTexts: dvbSTRFPresentPriority.setDescription('Description.Priority for dvbSTRFPresent event')
dvbSTResetFaultPriority = MibScalar((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 3, 1, 5), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dvbSTResetFaultPriority.setStatus('obsolete')
if mibBuilder.loadTexts: dvbSTResetFaultPriority.setDescription('Massage ist inactive!\n\t\t\t\t\n\t\t\t\t\n\t\t\t\tDescription. Priority for dvbSTResetFault event')
dvbSTFaultPriority = MibScalar((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 3, 1, 6), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dvbSTFaultPriority.setStatus('current')
if mibBuilder.loadTexts: dvbSTFaultPriority.setDescription('Description.Priority for dvbSTFault event')
dvbSTWarningPriority = MibScalar((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 3, 1, 7), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dvbSTWarningPriority.setStatus('current')
if mibBuilder.loadTexts: dvbSTWarningPriority.setDescription('Description.Priority for dvbSTWarning event')
dvbSTInput1OKPriority = MibScalar((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 3, 1, 8), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dvbSTInput1OKPriority.setStatus('current')
if mibBuilder.loadTexts: dvbSTInput1OKPriority.setDescription('Description.Priority for dvbSTInput1OK event')
dvbSTInput2OKPriority = MibScalar((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 3, 1, 9), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dvbSTInput2OKPriority.setStatus('current')
if mibBuilder.loadTexts: dvbSTInput2OKPriority.setDescription('Description.Priority for dvbSTInput2OK event')
dvbSTLocalModePriority = MibScalar((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 3, 1, 10), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dvbSTLocalModePriority.setStatus('current')
if mibBuilder.loadTexts: dvbSTLocalModePriority.setDescription('Description.Priority for dvbSTLocalMode event')
dvbSTActiveInputPriority = MibScalar((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 3, 1, 11), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dvbSTActiveInputPriority.setStatus('current')
if mibBuilder.loadTexts: dvbSTActiveInputPriority.setDescription('Description.Priority for dvbSTActiveInput event')
dvbSTSFNModePriority = MibScalar((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 3, 1, 12), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dvbSTSFNModePriority.setStatus('current')
if mibBuilder.loadTexts: dvbSTSFNModePriority.setDescription('Description.Priority for dvbSTSFNMode event')
dvbSTRefFaultPriority = MibScalar((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 3, 1, 13), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dvbSTRefFaultPriority.setStatus('current')
if mibBuilder.loadTexts: dvbSTRefFaultPriority.setDescription('Description.Priority for dvbSTRefFault event')
dvbSTMutePriority = MibScalar((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 3, 1, 14), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dvbSTMutePriority.setStatus('current')
if mibBuilder.loadTexts: dvbSTMutePriority.setDescription('Description.Priority for dvbSTMute event')
dvbSTFaultMIPPriority = MibScalar((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 3, 1, 15), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dvbSTFaultMIPPriority.setStatus('current')
if mibBuilder.loadTexts: dvbSTFaultMIPPriority.setDescription('Description.Priority for dvbSTFaultMIP event')
dvbSTStuffingModePriority = MibScalar((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 3, 1, 16), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dvbSTStuffingModePriority.setStatus('current')
if mibBuilder.loadTexts: dvbSTStuffingModePriority.setDescription('Description.Priority for dvbSTStuffingMode event')
groupST = MibIdentifier((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 4))
objectGroupST = ObjectGroup((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 4, 1)).setObjects(("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTInputPreselection"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTInputAutomatic"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTTransmitterOpMode"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTRFPresent"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTFault"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTWarning"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTInput1OK"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTInput2OK"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTLocalMode"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTActiveInput"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTSFNMode"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTRefFault"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTMute"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTFaultMIP"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTStuffingMode"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTInputPreselectionEnable"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTInputAutomaticEnable"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTTransmitterOpModeEnable"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTRFPresentEnable"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTFaultEnable"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTWarningEnable"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTInput1OKEnable"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTInput2OKEnable"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTLocalModeEnable"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTActiveInputEnable"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTSFNModeEnable"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTRefFaultEnable"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTMuteEnable"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTFaultMIPEnable"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTStuffingModeEnable"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTInputPreselectionPriority"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTInputAutomaticPriority"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTTransmitterOpModePriority"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTRFPresentPriority"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTFaultPriority"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTWarningPriority"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTFaultMIPPriority"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTMutePriority"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTRefFaultPriority"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTSFNModePriority"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTStuffingModePriority"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTInput1OKPriority"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTInput2OKPriority"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTLocalModePriority"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTActiveInputPriority"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    objectGroupST = objectGroupST.setStatus('current')
if mibBuilder.loadTexts: objectGroupST.setDescription('Description. dvb single transmitter  objects')
eventGroupST = NotificationGroup((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 4, 2)).setObjects(("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTInputPreselectionEvent"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTInputAutomaticEvent"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTTransmitterOpModeEvent"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTRFPresentEvent"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTFaultEvent"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTWarningEvent"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTInput1OKEvent"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTInput2OKEvent"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTLocalModeEvent"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTActiveInputEvent"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTSFNModeEvent"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTRefFaultEvent"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTStuffingModeEvent"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTMuteEvent"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTFaultMIPEvent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    eventGroupST = eventGroupST.setStatus('current')
if mibBuilder.loadTexts: eventGroupST.setDescription('Description. dvb single transmitter  events')
objectGroupSTobsolete = ObjectGroup((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 4, 3)).setObjects(("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTResetFault"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTResetFaultEnable"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTResetFaultPriority"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    objectGroupSTobsolete = objectGroupSTobsolete.setStatus('obsolete')
if mibBuilder.loadTexts: objectGroupSTobsolete.setDescription('Description. Inactive objects')
eventGroupSTobsolete = NotificationGroup((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 4, 4)).setObjects(("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTResetFaultEvent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    eventGroupSTobsolete = eventGroupSTobsolete.setStatus('obsolete')
if mibBuilder.loadTexts: eventGroupSTobsolete.setDescription('Description. Inactive notifications')
complianceST = MibIdentifier((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 5))
dvbSingleTransmitterCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 5, 1)).setObjects(("IRT-DVBT-SINGLETRANSMITTER-MIB", "objectGroupST"), ("IRT-DVBT-SINGLETRANSMITTER-MIB", "eventGroupST"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dvbSingleTransmitterCompliance = dvbSingleTransmitterCompliance.setStatus('current')
if mibBuilder.loadTexts: dvbSingleTransmitterCompliance.setDescription('Compliance Statement')
mibBuilder.exportSymbols("IRT-DVBT-SINGLETRANSMITTER-MIB", dvbSTMute=dvbSTMute, dvbSTRefFaultEnable=dvbSTRefFaultEnable, dvbSTInputPreselectionPriority=dvbSTInputPreselectionPriority, objectGroupSTobsolete=objectGroupSTobsolete, dvbSTStuffingModeEnable=dvbSTStuffingModeEnable, complianceST=complianceST, dvbSTActiveInput=dvbSTActiveInput, dvbSTRFPresentEnable=dvbSTRFPresentEnable, dvbSTInput2OKEnable=dvbSTInput2OKEnable, dvbSTFaultMIPEvent=dvbSTFaultMIPEvent, dvbSTRefFault=dvbSTRefFault, dvbSTInput1OKEnable=dvbSTInput1OKEnable, dvbSTRefFaultEvent=dvbSTRefFaultEvent, dvbSTFaultEvent=dvbSTFaultEvent, dvbSingleTransmitter=dvbSingleTransmitter, dvbSTInputPreselectionEnable=dvbSTInputPreselectionEnable, eventGroupSTobsolete=eventGroupSTobsolete, dvbSTLocalMode=dvbSTLocalMode, dvbSingleTransmitterCompliance=dvbSingleTransmitterCompliance, dvbSTMutePriority=dvbSTMutePriority, dvbSTInputPreselection=dvbSTInputPreselection, dvbSTFault=dvbSTFault, dvbSTStuffingMode=dvbSTStuffingMode, dvbSTInputPreselectionEvent=dvbSTInputPreselectionEvent, dvbSTTransmitterOpModeEvent=dvbSTTransmitterOpModeEvent, eventGroupST=eventGroupST, dvbSTRFPresentPriority=dvbSTRFPresentPriority, dvbSTResetFault=dvbSTResetFault, dvbSTFaultEnable=dvbSTFaultEnable, dvbSTEventEnable=dvbSTEventEnable, dvbSTStuffingModeEvent=dvbSTStuffingModeEvent, dvbSTInput2OKEvent=dvbSTInput2OKEvent, dvbSTSFNMode=dvbSTSFNMode, dvbSTRefFaultPriority=dvbSTRefFaultPriority, dvbSTActiveInputPriority=dvbSTActiveInputPriority, dvbSTActiveInputEvent=dvbSTActiveInputEvent, dvbSTWarningEnable=dvbSTWarningEnable, dvbSTEventEnableGeneral=dvbSTEventEnableGeneral, dvbSTRFPresentEvent=dvbSTRFPresentEvent, dvbSTFaultMIPPriority=dvbSTFaultMIPPriority, dvbSTMuteEvent=dvbSTMuteEvent, dvbSTInputAutomaticEnable=dvbSTInputAutomaticEnable, objectGroupST=objectGroupST, dvbSTResetFaultPriority=dvbSTResetFaultPriority, dvbSTTransmitterOpModeEnable=dvbSTTransmitterOpModeEnable, dvbSTFaultMIPEnable=dvbSTFaultMIPEnable, dvbSTInputAutomatic=dvbSTInputAutomatic, dvbSTInput2OK=dvbSTInput2OK, dvbSTSFNModeEnable=dvbSTSFNModeEnable, PYSNMP_MODULE_ID=dvbSingleTransmitter, dvbSTInput1OKEvent=dvbSTInput1OKEvent, dvbSTEventPriorityGeneral=dvbSTEventPriorityGeneral, dvbSTLocalModeEvent=dvbSTLocalModeEvent, dvbSTWarning=dvbSTWarning, dvbSTResetFaultEvent=dvbSTResetFaultEvent, dvbSTInput1OKPriority=dvbSTInput1OKPriority, dvbSTGeneral=dvbSTGeneral, dvbSTActiveInputEnable=dvbSTActiveInputEnable, dvbSTTransmitterOpModePriority=dvbSTTransmitterOpModePriority, dvbSTLocalModeEnable=dvbSTLocalModeEnable, dvbSTRFPresent=dvbSTRFPresent, dvbSTFaultPriority=dvbSTFaultPriority, dvbSTEventPriority=dvbSTEventPriority, dvbSTSFNModeEvent=dvbSTSFNModeEvent, dvbSTSFNModePriority=dvbSTSFNModePriority, dvbSTInputAutomaticEvent=dvbSTInputAutomaticEvent, dvbSTWarningPriority=dvbSTWarningPriority, dvbSTMuteEnable=dvbSTMuteEnable, dvbSTWarningEvent=dvbSTWarningEvent, groupST=groupST, dvbSTResetFaultEnable=dvbSTResetFaultEnable, dvbSTInputAutomaticPriority=dvbSTInputAutomaticPriority, dvbSTInput1OK=dvbSTInput1OK, dvbSTLocalModePriority=dvbSTLocalModePriority, dvbSTFaultMIP=dvbSTFaultMIP, dvbSTTransmitterOpMode=dvbSTTransmitterOpMode, dvbSTStuffingModePriority=dvbSTStuffingModePriority, dvbEventsST=dvbEventsST, dvbSTInput2OKPriority=dvbSTInput2OKPriority)
