#
# PySNMP MIB module PRVT-SYNC-ETHERNET-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/telco-systems/binox/PRVT-SYNC-ETHERNET-MIB
# Produced by pysmi-1.1.3 at Sun Nov 21 00:45:53 2021
# On host fv-az39-63 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
switch, = mibBuilder.importSymbols("PRVT-SWITCH-MIB", "switch")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, Counter64, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Gauge32, TimeTicks, IpAddress, NotificationType, Counter32, MibIdentifier, Bits, ModuleIdentity, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Counter64", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Gauge32", "TimeTicks", "IpAddress", "NotificationType", "Counter32", "MibIdentifier", "Bits", "ModuleIdentity", "Integer32")
TextualConvention, DisplayString, TruthValue, RowStatus, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TruthValue", "RowStatus", "DateAndTime")
prvtSyncEthernetMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 738, 10, 5, 170))
prvtSyncEthernetMIB.setRevisions(('2010-11-10 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: prvtSyncEthernetMIB.setRevisionsDescriptions(('Initial',))
if mibBuilder.loadTexts: prvtSyncEthernetMIB.setLastUpdated('201011100000Z')
if mibBuilder.loadTexts: prvtSyncEthernetMIB.setOrganization('BATM Advanced Communication')
if mibBuilder.loadTexts: prvtSyncEthernetMIB.setContactInfo('BATM/Telco Systems Support team\n         Email:\n         For North America: techsupport@telco.com\n         For North Europe: support@batm.de, info@batm.de\n         For the rest of the world: techsupport@telco.com')
if mibBuilder.loadTexts: prvtSyncEthernetMIB.setDescription('This is the MIB module to manage\n         synchronization over ethernet.')
class PrvtSyncEthernetQualityLevelType(TextualConvention, Integer32):
    description = 'Clock Quality Levels.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(2, 4, 8, 11, 15, 16, 17, 20, 23, 26, 28, 29, 30, 31, 64, 65))
    namedValues = NamedValues(("prc", 2), ("ssuA", 4), ("ssuB", 8), ("sec", 11), ("dnu", 15), ("stu", 16), ("prs", 17), ("tnc", 20), ("st2", 23), ("st3", 26), ("smc", 28), ("st3e", 29), ("prov", 30), ("dus", 31), ("invalid", 64), ("failed", 65))

prvtSyncEthernetMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 10, 5, 170, 0))
prvtSyncEthernetMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 10, 5, 170, 1))
syncEthernetHoldOffTime = MibScalar((1, 3, 6, 1, 4, 1, 738, 10, 5, 170, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(300, 1800))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: syncEthernetHoldOffTime.setStatus('current')
if mibBuilder.loadTexts: syncEthernetHoldOffTime.setDescription('Timeout value, in millisseconds, for the hold-off timer.')
syncEthernetWaitToRestoreTime = MibScalar((1, 3, 6, 1, 4, 1, 738, 10, 5, 170, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 12))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: syncEthernetWaitToRestoreTime.setStatus('current')
if mibBuilder.loadTexts: syncEthernetWaitToRestoreTime.setDescription('Timeout value, in minutes, for the wait-to-restore timer.')
syncEthernetG781OptionMode = MibScalar((1, 3, 6, 1, 4, 1, 738, 10, 5, 170, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("option1", 1), ("option2", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: syncEthernetG781OptionMode.setStatus('current')
if mibBuilder.loadTexts: syncEthernetG781OptionMode.setDescription('Specify which G.781 option mode to operate in.')
syncEthernetClockSourceTable = MibTable((1, 3, 6, 1, 4, 1, 738, 10, 5, 170, 1, 10), )
if mibBuilder.loadTexts: syncEthernetClockSourceTable.setStatus('current')
if mibBuilder.loadTexts: syncEthernetClockSourceTable.setDescription('Source clock synchronization table.')
syncEthernetClockSourceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 10, 5, 170, 1, 10, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: syncEthernetClockSourceEntry.setStatus('current')
if mibBuilder.loadTexts: syncEthernetClockSourceEntry.setDescription('Source clock synchronization entry.')
syncEthernetClockSourceRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 170, 1, 10, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: syncEthernetClockSourceRowStatus.setStatus('current')
if mibBuilder.loadTexts: syncEthernetClockSourceRowStatus.setDescription('Clock source synchronization table rowstatus.')
syncEthernetClockSourceAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 170, 1, 10, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: syncEthernetClockSourceAdminStatus.setStatus('current')
if mibBuilder.loadTexts: syncEthernetClockSourceAdminStatus.setDescription('Enable clock source.')
syncEthernetClockSourceEsmc = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 170, 1, 10, 1, 4), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: syncEthernetClockSourceEsmc.setStatus('current')
if mibBuilder.loadTexts: syncEthernetClockSourceEsmc.setDescription('Enable receiving ESMC messages (Synchronization Status Messages).\n         Only applicable for BITS clock sources.')
syncEthernetClockSourceFrequency = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 170, 1, 10, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2431))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: syncEthernetClockSourceFrequency.setStatus('current')
if mibBuilder.loadTexts: syncEthernetClockSourceFrequency.setDescription('Specify input frequency - N*8kHz\n         Only applicable for BITS clock sources.')
syncEthernetClockSourceQuality = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 170, 1, 10, 1, 6), PrvtSyncEthernetQualityLevelType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: syncEthernetClockSourceQuality.setStatus('current')
if mibBuilder.loadTexts: syncEthernetClockSourceQuality.setDescription('Specify quality level\n         In G781-option I mode, valid values are prs, ssuA, ssuB, dnu.\n         In G781-option II mode, valid values are stu, prs, tnc, st2, st3, smc, st3e, dus, prov.')
syncEthernetClockSourceQualityChangeNotify = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 170, 1, 10, 1, 7), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: syncEthernetClockSourceQualityChangeNotify.setStatus('current')
if mibBuilder.loadTexts: syncEthernetClockSourceQualityChangeNotify.setDescription('Enable quality level change notifications')
syncEthernetClockSourceRecvQualityLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 170, 1, 10, 1, 8), PrvtSyncEthernetQualityLevelType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: syncEthernetClockSourceRecvQualityLevel.setStatus('current')
if mibBuilder.loadTexts: syncEthernetClockSourceRecvQualityLevel.setDescription('The received quality level value.')
syncEthernetClockSourceLastRecvEsmcPduTime = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 170, 1, 10, 1, 9), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: syncEthernetClockSourceLastRecvEsmcPduTime.setStatus('current')
if mibBuilder.loadTexts: syncEthernetClockSourceLastRecvEsmcPduTime.setDescription('Time elapsed since the last valid ESMC message received')
syncEthernetClockSourceLastRecvEsmcErrorPduTime = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 170, 1, 10, 1, 10), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: syncEthernetClockSourceLastRecvEsmcErrorPduTime.setStatus('current')
if mibBuilder.loadTexts: syncEthernetClockSourceLastRecvEsmcErrorPduTime.setDescription('Time elapsed since the last invalid ESMC message received')
syncEthernetClockSourceLastRecvEsmcPduType = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 170, 1, 10, 1, 11), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: syncEthernetClockSourceLastRecvEsmcPduType.setStatus('current')
if mibBuilder.loadTexts: syncEthernetClockSourceLastRecvEsmcPduType.setDescription('Last received ESMC message type')
syncEthernetClockSourceLastRecvLastError = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 170, 1, 10, 1, 12), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: syncEthernetClockSourceLastRecvLastError.setStatus('current')
if mibBuilder.loadTexts: syncEthernetClockSourceLastRecvLastError.setDescription('Last error code')
syncEthernetClockSourceNumRecvEsmcPdu = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 170, 1, 10, 1, 13), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: syncEthernetClockSourceNumRecvEsmcPdu.setStatus('current')
if mibBuilder.loadTexts: syncEthernetClockSourceNumRecvEsmcPdu.setDescription('Total number of received ESMC messages')
syncEthernetClockSourceNumDiscEsmcPdu = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 170, 1, 10, 1, 14), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: syncEthernetClockSourceNumDiscEsmcPdu.setStatus('current')
if mibBuilder.loadTexts: syncEthernetClockSourceNumDiscEsmcPdu.setDescription('Total number of discarded ESMC messages')
syncEthernetClockSourceNumSignalFail = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 170, 1, 10, 1, 15), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: syncEthernetClockSourceNumSignalFail.setStatus('current')
if mibBuilder.loadTexts: syncEthernetClockSourceNumSignalFail.setDescription('Total number of generated signal failure events')
syncEthernetClockSourceQualityInvalidNotify = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 170, 1, 10, 1, 16), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: syncEthernetClockSourceQualityInvalidNotify.setStatus('current')
if mibBuilder.loadTexts: syncEthernetClockSourceQualityInvalidNotify.setDescription('Enable invalid quality notifications')
syncEthernetClockSourceEsmcInvalidNotify = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 170, 1, 10, 1, 17), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: syncEthernetClockSourceEsmcInvalidNotify.setStatus('current')
if mibBuilder.loadTexts: syncEthernetClockSourceEsmcInvalidNotify.setDescription('Enable invalid ESMC notifications')
syncEthernetClockOutputTable = MibTable((1, 3, 6, 1, 4, 1, 738, 10, 5, 170, 1, 12), )
if mibBuilder.loadTexts: syncEthernetClockOutputTable.setStatus('current')
if mibBuilder.loadTexts: syncEthernetClockOutputTable.setDescription('Output clock synchronization table.')
syncEthernetClockOutputEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 10, 5, 170, 1, 12, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: syncEthernetClockOutputEntry.setStatus('current')
if mibBuilder.loadTexts: syncEthernetClockOutputEntry.setDescription('Output clock synchronization entry.')
syncEthernetClockOutputRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 170, 1, 12, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: syncEthernetClockOutputRowStatus.setStatus('current')
if mibBuilder.loadTexts: syncEthernetClockOutputRowStatus.setDescription('syncEthernetClockOutput table rowStatus')
syncEthernetClockOutputEsmc = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 170, 1, 12, 1, 3), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: syncEthernetClockOutputEsmc.setStatus('current')
if mibBuilder.loadTexts: syncEthernetClockOutputEsmc.setDescription('Enable sending ESMC messages\n         Only applicable for BITS clock outputs.')
syncEthernetClockOutputFrequency = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 170, 1, 12, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2431))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: syncEthernetClockOutputFrequency.setStatus('current')
if mibBuilder.loadTexts: syncEthernetClockOutputFrequency.setDescription('Specify output frequency - N*8kHz\n         Only applicable for BITS clock outputs.')
syncEthernetClockOutputDpll = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 170, 1, 12, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: syncEthernetClockOutputDpll.setStatus('current')
if mibBuilder.loadTexts: syncEthernetClockOutputDpll.setDescription('Assign output clock to DPLL\n         Only applicable for BITS clock outputs.\n         Must be set to the syncEthernetDpllModuleId value of an existing\n         row in syncEthernetDpllTable.')
syncEthernetClockOutputQualityLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 170, 1, 12, 1, 6), PrvtSyncEthernetQualityLevelType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: syncEthernetClockOutputQualityLevel.setStatus('current')
if mibBuilder.loadTexts: syncEthernetClockOutputQualityLevel.setDescription('Last quality level value sent')
syncEthernetClockOutputLastQualityLevelChange = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 170, 1, 12, 1, 7), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: syncEthernetClockOutputLastQualityLevelChange.setStatus('current')
if mibBuilder.loadTexts: syncEthernetClockOutputLastQualityLevelChange.setDescription('Time elapsed since the last quality level change')
syncEthernetClockOutputMsgEvent = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 170, 1, 12, 1, 8), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: syncEthernetClockOutputMsgEvent.setStatus('current')
if mibBuilder.loadTexts: syncEthernetClockOutputMsgEvent.setDescription('Last ESMC message type sent')
syncEthernetClockOutputNumTransmittedEsmcPdu = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 170, 1, 12, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: syncEthernetClockOutputNumTransmittedEsmcPdu.setStatus('current')
if mibBuilder.loadTexts: syncEthernetClockOutputNumTransmittedEsmcPdu.setDescription('Total number of ESMC messages sent')
syncEthernetClockOutputNumTransmittedEventEsmcPdu = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 170, 1, 12, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: syncEthernetClockOutputNumTransmittedEventEsmcPdu.setStatus('current')
if mibBuilder.loadTexts: syncEthernetClockOutputNumTransmittedEventEsmcPdu.setDescription('Total number of ESMC messages sent')
syncEthernetDpllTable = MibTable((1, 3, 6, 1, 4, 1, 738, 10, 5, 170, 1, 14), )
if mibBuilder.loadTexts: syncEthernetDpllTable.setStatus('current')
if mibBuilder.loadTexts: syncEthernetDpllTable.setDescription('Synchronization DPLL table')
syncEthernetDpllEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 10, 5, 170, 1, 14, 1), ).setIndexNames((0, "PRVT-SYNC-ETHERNET-MIB", "syncEthernetDpllModuleId"))
if mibBuilder.loadTexts: syncEthernetDpllEntry.setStatus('current')
if mibBuilder.loadTexts: syncEthernetDpllEntry.setDescription('Synchronization DPLL entry')
syncEthernetDpllModuleId = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 170, 1, 14, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1)))
if mibBuilder.loadTexts: syncEthernetDpllModuleId.setStatus('current')
if mibBuilder.loadTexts: syncEthernetDpllModuleId.setDescription('Synchronization DPLL module index')
syncEthernetDpllRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 170, 1, 14, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: syncEthernetDpllRowStatus.setStatus('current')
if mibBuilder.loadTexts: syncEthernetDpllRowStatus.setDescription('Synchronization DPLL rowstatus')
syncEthernetDpllAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 170, 1, 14, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: syncEthernetDpllAdminStatus.setStatus('current')
if mibBuilder.loadTexts: syncEthernetDpllAdminStatus.setDescription('Administrative status of the DPLL')
syncEthernetDpllReferenceSelection = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 170, 1, 14, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("freerun", 1), ("static", 2), ("g781", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: syncEthernetDpllReferenceSelection.setStatus('current')
if mibBuilder.loadTexts: syncEthernetDpllReferenceSelection.setDescription('Specify reference selection mode')
syncEthernetDpllEnableQualityLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 170, 1, 14, 1, 5), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: syncEthernetDpllEnableQualityLevel.setStatus('current')
if mibBuilder.loadTexts: syncEthernetDpllEnableQualityLevel.setDescription('Enable reference selection based on quality level\n         Only applicable when syncEthernetDpllReferenceSelection equals g781.')
syncEthernetDpllStatusChangeNotify = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 170, 1, 14, 1, 6), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: syncEthernetDpllStatusChangeNotify.setStatus('current')
if mibBuilder.loadTexts: syncEthernetDpllStatusChangeNotify.setDescription('Enable DPLL status change notifications')
syncEthernetDpllReferenceChangeNotify = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 170, 1, 14, 1, 7), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: syncEthernetDpllReferenceChangeNotify.setStatus('current')
if mibBuilder.loadTexts: syncEthernetDpllReferenceChangeNotify.setDescription('Enable reference clock change notifications')
syncEthernetDpllStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 170, 1, 14, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("freerun", 0), ("locked", 1), ("holdover", 2), ("refFailure", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: syncEthernetDpllStatus.setStatus('current')
if mibBuilder.loadTexts: syncEthernetDpllStatus.setDescription('DPLL operational status')
syncEthernetDpllStatusLastChange = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 170, 1, 14, 1, 9), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: syncEthernetDpllStatusLastChange.setStatus('current')
if mibBuilder.loadTexts: syncEthernetDpllStatusLastChange.setDescription('Time since last DPLL status change')
syncEthernetDpllSystemQualityLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 170, 1, 14, 1, 10), PrvtSyncEthernetQualityLevelType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: syncEthernetDpllSystemQualityLevel.setStatus('current')
if mibBuilder.loadTexts: syncEthernetDpllSystemQualityLevel.setDescription('System quality level')
syncEthernetDpllSystemQualityLevelLastChange = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 170, 1, 14, 1, 11), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: syncEthernetDpllSystemQualityLevelLastChange.setStatus('current')
if mibBuilder.loadTexts: syncEthernetDpllSystemQualityLevelLastChange.setDescription('Time since last system quality level change')
syncEthernetDpllSelectedReferenceClock = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 170, 1, 14, 1, 12), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: syncEthernetDpllSelectedReferenceClock.setStatus('current')
if mibBuilder.loadTexts: syncEthernetDpllSelectedReferenceClock.setDescription('The selected reference clock source')
syncEthernetDpllSelectedReferenceClockChange = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 170, 1, 14, 1, 13), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: syncEthernetDpllSelectedReferenceClockChange.setStatus('current')
if mibBuilder.loadTexts: syncEthernetDpllSelectedReferenceClockChange.setDescription('Time since last reference clock change')
syncEthernetDpllClkRefTable = MibTable((1, 3, 6, 1, 4, 1, 738, 10, 5, 170, 1, 16), )
if mibBuilder.loadTexts: syncEthernetDpllClkRefTable.setStatus('current')
if mibBuilder.loadTexts: syncEthernetDpllClkRefTable.setDescription('Synchronization DPLL clock reference table')
syncEthernetDpllClkRefEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 10, 5, 170, 1, 16, 1), ).setIndexNames((0, "PRVT-SYNC-ETHERNET-MIB", "syncEthernetDpllModuleId"), (0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: syncEthernetDpllClkRefEntry.setStatus('current')
if mibBuilder.loadTexts: syncEthernetDpllClkRefEntry.setDescription('Synchronization DPLL clock reference entry')
syncEthernetDpllClkRefRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 170, 1, 16, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: syncEthernetDpllClkRefRowStatus.setStatus('current')
if mibBuilder.loadTexts: syncEthernetDpllClkRefRowStatus.setDescription('Synchronization DPLL clock reference rowstatus')
syncEthernetDpllClkRefPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 170, 1, 16, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 256))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: syncEthernetDpllClkRefPriority.setStatus('current')
if mibBuilder.loadTexts: syncEthernetDpllClkRefPriority.setDescription('Specify reference clock priority')
syncEthernetDpllClkRefLockOut = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 170, 1, 16, 1, 4), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: syncEthernetDpllClkRefLockOut.setStatus('current')
if mibBuilder.loadTexts: syncEthernetDpllClkRefLockOut.setDescription('Lock reference clock')
syncEthernetDpllClkRefFailStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 170, 1, 16, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: syncEthernetDpllClkRefFailStatus.setStatus('current')
if mibBuilder.loadTexts: syncEthernetDpllClkRefFailStatus.setDescription('DPLL reference clock status')
syncEthernetInvalidESMC = NotificationType((1, 3, 6, 1, 4, 1, 738, 10, 5, 170, 0, 1)).setObjects(("PRVT-SYNC-ETHERNET-MIB", "syncEthernetClockSourceLastRecvLastError"))
if mibBuilder.loadTexts: syncEthernetInvalidESMC.setStatus('current')
if mibBuilder.loadTexts: syncEthernetInvalidESMC.setDescription('Invalid ESMC has been received.')
syncEthernetQualityLevelChange = NotificationType((1, 3, 6, 1, 4, 1, 738, 10, 5, 170, 0, 2)).setObjects(("PRVT-SYNC-ETHERNET-MIB", "syncEthernetClockSourceQuality"))
if mibBuilder.loadTexts: syncEthernetQualityLevelChange.setStatus('current')
if mibBuilder.loadTexts: syncEthernetQualityLevelChange.setDescription('Current value of syncEthernetClockSourceQuality has\n         been changed.')
syncEthernetInvalidQualityLevelReceived = NotificationType((1, 3, 6, 1, 4, 1, 738, 10, 5, 170, 0, 3)).setObjects(("PRVT-SYNC-ETHERNET-MIB", "syncEthernetClockSourceRecvQualityLevel"))
if mibBuilder.loadTexts: syncEthernetInvalidQualityLevelReceived.setStatus('current')
if mibBuilder.loadTexts: syncEthernetInvalidQualityLevelReceived.setDescription('Invalid Quality level equals to QL-INVx has been received.')
syncEthernetDPLLReferenceChange = NotificationType((1, 3, 6, 1, 4, 1, 738, 10, 5, 170, 0, 4)).setObjects(("PRVT-SYNC-ETHERNET-MIB", "syncEthernetDpllSelectedReferenceClockChange"))
if mibBuilder.loadTexts: syncEthernetDPLLReferenceChange.setStatus('current')
if mibBuilder.loadTexts: syncEthernetDPLLReferenceChange.setDescription("DPLL's reference clock changed.")
syncEthernetDPLLChanged = NotificationType((1, 3, 6, 1, 4, 1, 738, 10, 5, 170, 0, 5)).setObjects(("PRVT-SYNC-ETHERNET-MIB", "syncEthernetDpllStatus"))
if mibBuilder.loadTexts: syncEthernetDPLLChanged.setStatus('current')
if mibBuilder.loadTexts: syncEthernetDPLLChanged.setDescription("Some of the DPLL's operational status changes.")
syncEthernetDPLLLockFailed = NotificationType((1, 3, 6, 1, 4, 1, 738, 10, 5, 170, 0, 6)).setObjects(("PRVT-SYNC-ETHERNET-MIB", "syncEthernetDpllClkRefFailStatus"))
if mibBuilder.loadTexts: syncEthernetDPLLLockFailed.setStatus('current')
if mibBuilder.loadTexts: syncEthernetDPLLLockFailed.setDescription("If after new Reference selection the DPLL can't\n         lock onto it, this will affect the Clock Source\n         associated with that reference")
mibBuilder.exportSymbols("PRVT-SYNC-ETHERNET-MIB", syncEthernetDpllClkRefPriority=syncEthernetDpllClkRefPriority, syncEthernetClockSourceEntry=syncEthernetClockSourceEntry, syncEthernetClockOutputNumTransmittedEsmcPdu=syncEthernetClockOutputNumTransmittedEsmcPdu, syncEthernetClockOutputNumTransmittedEventEsmcPdu=syncEthernetClockOutputNumTransmittedEventEsmcPdu, syncEthernetClockSourceFrequency=syncEthernetClockSourceFrequency, syncEthernetDpllEntry=syncEthernetDpllEntry, syncEthernetClockOutputEsmc=syncEthernetClockOutputEsmc, syncEthernetDpllClkRefTable=syncEthernetDpllClkRefTable, syncEthernetDpllModuleId=syncEthernetDpllModuleId, syncEthernetClockOutputTable=syncEthernetClockOutputTable, syncEthernetDpllStatusLastChange=syncEthernetDpllStatusLastChange, syncEthernetHoldOffTime=syncEthernetHoldOffTime, syncEthernetG781OptionMode=syncEthernetG781OptionMode, syncEthernetClockSourceLastRecvEsmcErrorPduTime=syncEthernetClockSourceLastRecvEsmcErrorPduTime, syncEthernetClockSourceNumSignalFail=syncEthernetClockSourceNumSignalFail, syncEthernetDpllRowStatus=syncEthernetDpllRowStatus, syncEthernetDpllSelectedReferenceClockChange=syncEthernetDpllSelectedReferenceClockChange, syncEthernetClockSourceNumRecvEsmcPdu=syncEthernetClockSourceNumRecvEsmcPdu, syncEthernetDpllClkRefRowStatus=syncEthernetDpllClkRefRowStatus, syncEthernetClockOutputDpll=syncEthernetClockOutputDpll, syncEthernetDpllClkRefEntry=syncEthernetDpllClkRefEntry, syncEthernetDpllClkRefLockOut=syncEthernetDpllClkRefLockOut, prvtSyncEthernetMIBNotifications=prvtSyncEthernetMIBNotifications, syncEthernetClockOutputFrequency=syncEthernetClockOutputFrequency, syncEthernetQualityLevelChange=syncEthernetQualityLevelChange, syncEthernetDpllStatus=syncEthernetDpllStatus, syncEthernetClockSourceQualityChangeNotify=syncEthernetClockSourceQualityChangeNotify, syncEthernetClockSourceLastRecvEsmcPduTime=syncEthernetClockSourceLastRecvEsmcPduTime, syncEthernetClockOutputQualityLevel=syncEthernetClockOutputQualityLevel, syncEthernetDpllSelectedReferenceClock=syncEthernetDpllSelectedReferenceClock, syncEthernetDpllEnableQualityLevel=syncEthernetDpllEnableQualityLevel, syncEthernetDPLLLockFailed=syncEthernetDPLLLockFailed, syncEthernetInvalidESMC=syncEthernetInvalidESMC, syncEthernetClockSourceEsmc=syncEthernetClockSourceEsmc, syncEthernetDpllReferenceChangeNotify=syncEthernetDpllReferenceChangeNotify, syncEthernetWaitToRestoreTime=syncEthernetWaitToRestoreTime, syncEthernetClockOutputLastQualityLevelChange=syncEthernetClockOutputLastQualityLevelChange, syncEthernetClockSourceLastRecvEsmcPduType=syncEthernetClockSourceLastRecvEsmcPduType, syncEthernetInvalidQualityLevelReceived=syncEthernetInvalidQualityLevelReceived, syncEthernetDPLLChanged=syncEthernetDPLLChanged, syncEthernetDpllSystemQualityLevelLastChange=syncEthernetDpllSystemQualityLevelLastChange, syncEthernetClockOutputMsgEvent=syncEthernetClockOutputMsgEvent, syncEthernetClockOutputEntry=syncEthernetClockOutputEntry, prvtSyncEthernetMIBObjects=prvtSyncEthernetMIBObjects, syncEthernetClockSourceRecvQualityLevel=syncEthernetClockSourceRecvQualityLevel, syncEthernetClockSourceLastRecvLastError=syncEthernetClockSourceLastRecvLastError, syncEthernetClockSourceAdminStatus=syncEthernetClockSourceAdminStatus, syncEthernetClockOutputRowStatus=syncEthernetClockOutputRowStatus, syncEthernetClockSourceQuality=syncEthernetClockSourceQuality, syncEthernetDpllReferenceSelection=syncEthernetDpllReferenceSelection, syncEthernetDpllStatusChangeNotify=syncEthernetDpllStatusChangeNotify, syncEthernetClockSourceTable=syncEthernetClockSourceTable, syncEthernetDpllSystemQualityLevel=syncEthernetDpllSystemQualityLevel, prvtSyncEthernetMIB=prvtSyncEthernetMIB, syncEthernetClockSourceEsmcInvalidNotify=syncEthernetClockSourceEsmcInvalidNotify, syncEthernetClockSourceRowStatus=syncEthernetClockSourceRowStatus, syncEthernetClockSourceNumDiscEsmcPdu=syncEthernetClockSourceNumDiscEsmcPdu, PrvtSyncEthernetQualityLevelType=PrvtSyncEthernetQualityLevelType, syncEthernetClockSourceQualityInvalidNotify=syncEthernetClockSourceQualityInvalidNotify, PYSNMP_MODULE_ID=prvtSyncEthernetMIB, syncEthernetDpllTable=syncEthernetDpllTable, syncEthernetDpllAdminStatus=syncEthernetDpllAdminStatus, syncEthernetDpllClkRefFailStatus=syncEthernetDpllClkRefFailStatus, syncEthernetDPLLReferenceChange=syncEthernetDPLLReferenceChange)
