#
# PySNMP MIB module PRVT-ELMI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/telco-systems/binos/PRVT-ELMI-MIB
# Produced by pysmi-1.1.3 at Sun Nov 28 20:26:43 2021
# On host fv-az77-612 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
InterfaceIndex, ifIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "ifIndex")
switch, = mibBuilder.importSymbols("PRVT-SWITCH-MIB", "switch")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Counter32, Counter64, Bits, IpAddress, transmission, MibIdentifier, Gauge32, ObjectIdentity, Unsigned32, ModuleIdentity, TimeTicks, Integer32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Counter32", "Counter64", "Bits", "IpAddress", "transmission", "MibIdentifier", "Gauge32", "ObjectIdentity", "Unsigned32", "ModuleIdentity", "TimeTicks", "Integer32", "NotificationType")
RowStatus, DisplayString, TimeStamp, StorageType, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TimeStamp", "StorageType", "TextualConvention", "TruthValue")
prvtELMIMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 738, 1, 5, 120))
prvtELMIMib.setRevisions(('2009-07-13 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: prvtELMIMib.setRevisionsDescriptions(('Initial version.',))
if mibBuilder.loadTexts: prvtELMIMib.setLastUpdated('200907130000Z')
if mibBuilder.loadTexts: prvtELMIMib.setOrganization('BATM Advanced Communication')
if mibBuilder.loadTexts: prvtELMIMib.setContactInfo('BATM/Telco Systems Support team\nEmail: \nFor North America: techsupport@telco.com\nFor North Europe: support@batm.de, info@batm.de\nFor the rest of the world: techsupport@telco.com')
if mibBuilder.loadTexts: prvtELMIMib.setDescription('This MIB contains managed object definitions for\nencapsulating E-LMI that is terminated by the UNI-C \non the CE side of the UNI and by the UNI-N on the MEN side of the UNI.')
prvtELMINotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 120, 0))
prvtELMIObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 120, 1))
prvtELMIConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 120, 2))
prvtELMIEnable = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 5, 120, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtELMIEnable.setStatus('current')
if mibBuilder.loadTexts: prvtELMIEnable.setDescription('E-LMI enable protocol')
prvtELMICfgTable = MibTable((1, 3, 6, 1, 4, 1, 738, 1, 5, 120, 1, 2), )
if mibBuilder.loadTexts: prvtELMICfgTable.setStatus('current')
if mibBuilder.loadTexts: prvtELMICfgTable.setDescription('This table contains object for configuring E-LMI protocol.')
prvtELMICfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 1, 5, 120, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: prvtELMICfgEntry.setStatus('current')
if mibBuilder.loadTexts: prvtELMICfgEntry.setDescription('')
prvtELMIIfEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 120, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtELMIIfEnable.setStatus('current')
if mibBuilder.loadTexts: prvtELMIIfEnable.setDescription(' Enables or disables E-LMI feature per interface.')
prvtELMIIfMode = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 120, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("uni-n", 1), ("uni-c", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtELMIIfMode.setStatus('current')
if mibBuilder.loadTexts: prvtELMIIfMode.setDescription(' E-LMI working mode per interface.')
prvtELMIPollingCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 120, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(360)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtELMIPollingCnt.setStatus('current')
if mibBuilder.loadTexts: prvtELMIPollingCnt.setDescription(' Polling counter -  controls the number of polling cycles between Full Status exchanges.\nAplicable only in UNI-C mode')
prvtELMIPollingTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 120, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 30)).clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtELMIPollingTimer.setStatus('current')
if mibBuilder.loadTexts: prvtELMIPollingTimer.setDescription(' Polling timer - controls the interval at which STATUS ENQUIRY messages are transmitted.\nAplicable only in UNI-C mode')
prvtELMIVerifPollTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 120, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 30)).clone(15)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtELMIVerifPollTimer.setStatus('current')
if mibBuilder.loadTexts: prvtELMIVerifPollTimer.setDescription(' Polling Verification Timer - controls the interval during which information sent to the UNI-C in a STATUS message is consider valid.\n The Polling Verification Timer MAY be disabled and thus the PVT never expires.\n Polling Verification Timer is valid only for UNI-N mode.\n For disable the counter SET 0 value')
prvtELMIStatusCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 120, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(2, 10)).clone(4)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtELMIStatusCnt.setStatus('current')
if mibBuilder.loadTexts: prvtELMIStatusCnt.setDescription(' Status Counter - controls the number of consecutive errors that must occur before E-LMI at the UNI is declared as not operational.\nAplicable in both UNI-Cand UNI-N mode')
prvtELMIClearStatistics = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 120, 1, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("none", 0), ("clear", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtELMIClearStatistics.setStatus('current')
if mibBuilder.loadTexts: prvtELMIClearStatistics.setDescription('Clear ELMI statistics per interface.')
prvtELMIMapEvcCEVlanType = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 120, 1, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("allToOneBundling", 1), ("serviceMultiplexingWithNoBund", 2), ("budling", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtELMIMapEvcCEVlanType.setStatus('current')
if mibBuilder.loadTexts: prvtELMIMapEvcCEVlanType.setDescription('CE-VLAN ID/EVC Map Type .')
prvtELMIStatisticsTable = MibTable((1, 3, 6, 1, 4, 1, 738, 1, 5, 120, 1, 3), )
if mibBuilder.loadTexts: prvtELMIStatisticsTable.setStatus('current')
if mibBuilder.loadTexts: prvtELMIStatisticsTable.setDescription('This table contains objects for displaing E-LMI statistics.')
prvtELMIStatisticsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 1, 5, 120, 1, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: prvtELMIStatisticsEntry.setStatus('current')
if mibBuilder.loadTexts: prvtELMIStatisticsEntry.setDescription('')
prvtELMIStatusChange = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 120, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtELMIStatusChange.setStatus('current')
if mibBuilder.loadTexts: prvtELMIStatusChange.setDescription('E-LMI operational status')
prvtELMILastFullReport = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 120, 1, 3, 1, 2), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtELMILastFullReport.setStatus('current')
if mibBuilder.loadTexts: prvtELMILastFullReport.setDescription('E-LMI \tTime of the last full status report.')
prvtELMITimeOuts = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 120, 1, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtELMITimeOuts.setStatus('current')
if mibBuilder.loadTexts: prvtELMITimeOuts.setDescription('Number of Status Timeouts.')
prvtELMIMsgISN = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 120, 1, 3, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtELMIMsgISN.setStatus('current')
if mibBuilder.loadTexts: prvtELMIMsgISN.setDescription('Number of messages with Invalid Sequence Number.')
prvtELMIInavlidProtocolVers = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 120, 1, 3, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtELMIInavlidProtocolVers.setStatus('current')
if mibBuilder.loadTexts: prvtELMIInavlidProtocolVers.setDescription('Invalid Protocol Version.')
prvtELMIEVCInvalidRefId = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 120, 1, 3, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtELMIEVCInvalidRefId.setStatus('current')
if mibBuilder.loadTexts: prvtELMIEVCInvalidRefId.setDescription('Invalid Ethernet Virtual Connection Reference Id.')
prvtELMIInavlidMsgType = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 120, 1, 3, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtELMIInavlidMsgType.setStatus('current')
if mibBuilder.loadTexts: prvtELMIInavlidMsgType.setDescription('Invalid Message Type.')
prvtELMIOOSIE = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 120, 1, 3, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtELMIOOSIE.setStatus('current')
if mibBuilder.loadTexts: prvtELMIOOSIE.setDescription('Out of Sequence IE.')
prvtELMIDuplicateIE = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 120, 1, 3, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtELMIDuplicateIE.setStatus('current')
if mibBuilder.loadTexts: prvtELMIDuplicateIE.setDescription('Duplicate IE.')
prvtELMIMandatoryIEMissing = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 120, 1, 3, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtELMIMandatoryIEMissing.setStatus('current')
if mibBuilder.loadTexts: prvtELMIMandatoryIEMissing.setDescription('Mandatory IE Missing.')
prvtELMIInavlidMandatoryIE = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 120, 1, 3, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtELMIInavlidMandatoryIE.setStatus('current')
if mibBuilder.loadTexts: prvtELMIInavlidMandatoryIE.setDescription('Invalid Mandatory IE.')
prvtELMIInvalidNonMandatoryIE = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 120, 1, 3, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtELMIInvalidNonMandatoryIE.setStatus('current')
if mibBuilder.loadTexts: prvtELMIInvalidNonMandatoryIE.setDescription('Invalid non-Mandatory IE.')
prvtELMIUnrecognizedIE = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 120, 1, 3, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtELMIUnrecognizedIE.setStatus('current')
if mibBuilder.loadTexts: prvtELMIUnrecognizedIE.setDescription('Unrecognized  IE.')
prvtELMIUnexpectedIE = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 120, 1, 3, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtELMIUnexpectedIE.setStatus('current')
if mibBuilder.loadTexts: prvtELMIUnexpectedIE.setDescription('Unexpected  IE.')
prvtELMIShortMessage = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 120, 1, 3, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtELMIShortMessage.setStatus('current')
if mibBuilder.loadTexts: prvtELMIShortMessage.setDescription('Short Message.')
prvtELMIEVCTable = MibTable((1, 3, 6, 1, 4, 1, 738, 1, 5, 120, 1, 4), )
if mibBuilder.loadTexts: prvtELMIEVCTable.setStatus('current')
if mibBuilder.loadTexts: prvtELMIEVCTable.setDescription('This table contains objects for displaing EVC informations.')
prvtELMIEVCEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 1, 5, 120, 1, 4, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "PRVT-ELMI-MIB", "prvtELMIEVCId"))
if mibBuilder.loadTexts: prvtELMIEVCEntry.setStatus('current')
if mibBuilder.loadTexts: prvtELMIEVCEntry.setDescription('An entry display information about EVC.')
prvtELMIEVCId = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 120, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: prvtELMIEVCId.setStatus('current')
if mibBuilder.loadTexts: prvtELMIEVCId.setDescription('An integer that uniquely identifies EVC Refernces id.')
prvtELMIServicesId = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 120, 1, 4, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtELMIServicesId.setStatus('current')
if mibBuilder.loadTexts: prvtELMIServicesId.setDescription('An integer that uniquely identifies Services id.')
prvtELMIEVCStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 120, 1, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("non-active", 0), ("new-non-active", 1), ("active", 2), ("new-active", 3), ("partially-active", 4), ("new-partially-active", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtELMIEVCStatus.setStatus('current')
if mibBuilder.loadTexts: prvtELMIEVCStatus.setDescription('EVC State.')
prvtELMIEVCType = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 120, 1, 4, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("point-to-point", 1), ("multi-point-to-point", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtELMIEVCType.setStatus('current')
if mibBuilder.loadTexts: prvtELMIEVCType.setDescription('EVC Type.')
prvtELMIMapEvcCEVlanTable = MibTable((1, 3, 6, 1, 4, 1, 738, 1, 5, 120, 1, 5), )
if mibBuilder.loadTexts: prvtELMIMapEvcCEVlanTable.setStatus('current')
if mibBuilder.loadTexts: prvtELMIMapEvcCEVlanTable.setDescription('This table contains objects for displaying the map between EVC and CE-VLAN')
prvtELMIMapEvcCEVlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 1, 5, 120, 1, 5, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "PRVT-ELMI-MIB", "prvtELMIMapEVCId"), (0, "PRVT-ELMI-MIB", "prvtELMIMapCeVlanId"))
if mibBuilder.loadTexts: prvtELMIMapEvcCEVlanEntry.setStatus('current')
if mibBuilder.loadTexts: prvtELMIMapEvcCEVlanEntry.setDescription('An entry links EVC id with CE-VLAN id.')
prvtELMIMapEVCId = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 120, 1, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtELMIMapEVCId.setStatus('current')
if mibBuilder.loadTexts: prvtELMIMapEVCId.setDescription('An integer that uniquely identifies EVC id.')
prvtELMIMapCeVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 120, 1, 5, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtELMIMapCeVlanId.setStatus('current')
if mibBuilder.loadTexts: prvtELMIMapCeVlanId.setDescription('An integer that uniquely identifies CE-VLAN id.')
prvtELMIStatus = NotificationType((1, 3, 6, 1, 4, 1, 738, 1, 5, 120, 0, 1)).setObjects(("PRVT-ELMI-MIB", "prvtELMIEnable"), ("PRVT-ELMI-MIB", "prvtELMIStatusChange"))
if mibBuilder.loadTexts: prvtELMIStatus.setStatus('current')
if mibBuilder.loadTexts: prvtELMIStatus.setDescription('This notification is sent  when status of ELMI changes.')
prvtELMIChangeEVC = NotificationType((1, 3, 6, 1, 4, 1, 738, 1, 5, 120, 0, 2)).setObjects(("PRVT-ELMI-MIB", "prvtELMIEVCId"))
if mibBuilder.loadTexts: prvtELMIChangeEVC.setStatus('current')
if mibBuilder.loadTexts: prvtELMIChangeEVC.setDescription('This notification is sent  when status of CE-VLAN ID/EVC Map per interface changes.')
mibBuilder.exportSymbols("PRVT-ELMI-MIB", prvtELMIEVCType=prvtELMIEVCType, prvtELMIOOSIE=prvtELMIOOSIE, prvtELMIServicesId=prvtELMIServicesId, prvtELMIChangeEVC=prvtELMIChangeEVC, prvtELMIShortMessage=prvtELMIShortMessage, prvtELMIConformance=prvtELMIConformance, prvtELMIClearStatistics=prvtELMIClearStatistics, prvtELMIInavlidProtocolVers=prvtELMIInavlidProtocolVers, prvtELMIEnable=prvtELMIEnable, prvtELMIPollingTimer=prvtELMIPollingTimer, prvtELMIMib=prvtELMIMib, prvtELMIInavlidMsgType=prvtELMIInavlidMsgType, prvtELMINotifications=prvtELMINotifications, prvtELMIEVCInvalidRefId=prvtELMIEVCInvalidRefId, prvtELMIEVCId=prvtELMIEVCId, prvtELMICfgEntry=prvtELMICfgEntry, prvtELMICfgTable=prvtELMICfgTable, PYSNMP_MODULE_ID=prvtELMIMib, prvtELMIUnexpectedIE=prvtELMIUnexpectedIE, prvtELMIInavlidMandatoryIE=prvtELMIInavlidMandatoryIE, prvtELMIEVCTable=prvtELMIEVCTable, prvtELMIMapEvcCEVlanEntry=prvtELMIMapEvcCEVlanEntry, prvtELMIObjects=prvtELMIObjects, prvtELMIStatusCnt=prvtELMIStatusCnt, prvtELMIIfEnable=prvtELMIIfEnable, prvtELMIMapEvcCEVlanType=prvtELMIMapEvcCEVlanType, prvtELMIStatus=prvtELMIStatus, prvtELMIStatisticsEntry=prvtELMIStatisticsEntry, prvtELMIStatisticsTable=prvtELMIStatisticsTable, prvtELMIMapEVCId=prvtELMIMapEVCId, prvtELMIUnrecognizedIE=prvtELMIUnrecognizedIE, prvtELMIMapEvcCEVlanTable=prvtELMIMapEvcCEVlanTable, prvtELMIEVCStatus=prvtELMIEVCStatus, prvtELMITimeOuts=prvtELMITimeOuts, prvtELMIInvalidNonMandatoryIE=prvtELMIInvalidNonMandatoryIE, prvtELMIEVCEntry=prvtELMIEVCEntry, prvtELMIVerifPollTimer=prvtELMIVerifPollTimer, prvtELMIIfMode=prvtELMIIfMode, prvtELMILastFullReport=prvtELMILastFullReport, prvtELMIPollingCnt=prvtELMIPollingCnt, prvtELMIStatusChange=prvtELMIStatusChange, prvtELMIDuplicateIE=prvtELMIDuplicateIE, prvtELMIMsgISN=prvtELMIMsgISN, prvtELMIMandatoryIEMissing=prvtELMIMandatoryIEMissing, prvtELMIMapCeVlanId=prvtELMIMapCeVlanId)
