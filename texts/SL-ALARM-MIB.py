#
# PySNMP MIB module SL-ALARM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/packetlight/SL-ALARM-MIB
# Produced by pysmi-1.1.8 at Mon Feb  7 16:17:48 2022
# On host fv-az42-619 platform Linux version 5.11.0-1028-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
PerfCurrentCount, PerfIntervalCount, PerfTotalCount = mibBuilder.importSymbols("PerfHist-TC-MIB", "PerfCurrentCount", "PerfIntervalCount", "PerfTotalCount")
slMain, = mibBuilder.importSymbols("SL-MAIN-MIB", "slMain")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
iso, ModuleIdentity, MibIdentifier, TimeTicks, ObjectIdentity, Unsigned32, IpAddress, Counter32, Gauge32, Counter64, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "ModuleIdentity", "MibIdentifier", "TimeTicks", "ObjectIdentity", "Unsigned32", "IpAddress", "Counter32", "Gauge32", "Counter64", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "NotificationType")
DisplayString, TimeStamp, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TimeStamp", "TruthValue", "TextualConvention")
slAlarmMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 4515, 1, 3, 20))
if mibBuilder.loadTexts: slAlarmMib.setLastUpdated('0008280000Z')
if mibBuilder.loadTexts: slAlarmMib.setOrganization('PacketLight Networks Ltd.')
if mibBuilder.loadTexts: slAlarmMib.setContactInfo('Omri_Viner@PacketLight.com')
if mibBuilder.loadTexts: slAlarmMib.setDescription('This MIB module describes the ALARMS.')
class SlAlarmType(TextualConvention, Integer32):
    description = 'The Alarms Types.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 21, 22, 23, 24, 25, 26, 27, 101, 102, 103, 104, 105, 106, 107, 108, 151, 152, 201, 202, 203, 204, 301, 302, 303, 304, 306, 307, 311, 312, 313, 314, 315, 351, 352, 353, 354, 401, 403, 404, 406, 407, 408, 409, 410, 411, 412, 451, 452, 453, 454, 455, 456, 470, 471, 472, 501, 502, 503, 602, 603, 604, 606, 608, 621, 622, 623, 624, 625, 701, 702, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713, 720, 721, 726, 727, 728, 729, 730, 731, 732, 733, 734, 735, 736, 737, 750, 751, 752, 753, 754, 755, 756, 757, 758, 759, 780, 781, 782, 783, 784, 785, 801, 803, 804, 806, 807, 808, 820, 821, 902, 903, 904, 905, 906, 907, 908, 909, 910, 1001, 1002, 1003, 1004))
    namedValues = NamedValues(("losSonetAlarm", 1), ("lofSonetAlarm", 2), ("lopSonetAlarm", 3), ("aisLineSonetAlarm", 4), ("rfiLineSonetAlarm", 5), ("uneqSonetAlarm", 6), ("timLine", 7), ("slm", 8), ("sd", 9), ("sf", 10), ("hwfail", 11), ("aisPathSonetAlarm", 12), ("rfiPathSonetAlarm", 13), ("timPath", 14), ("uplinkTransmitMismatch", 15), ("uplinkClockSourceLol", 16), ("aisVtSonetAlarm", 21), ("lopVtSonetAlarm", 22), ("rfiVtSonetAlarm", 23), ("timVt", 24), ("slmVt", 25), ("uneqVtSonetAlarm", 26), ("lomVt", 27), ("vcgFarLossClientSignal", 101), ("vcgFarLossClientSync", 102), ("vcgLossAlignment", 103), ("vcgLossMultiframe", 104), ("vcgLossSequence", 105), ("vcgGfpLossSync", 106), ("vcgFarGfpLossSync", 107), ("vcgBadGidMember", 108), ("provUnequipped", 151), ("provMismatch", 152), ("ethConfigTransmitFault", 201), ("ethConfigLossOfSignal", 202), ("ethConfigLinkFail", 203), ("ethConfigPcsLossSync", 204), ("fcBxPortTransmitFault", 301), ("fcBxPortLossOfSignal", 302), ("fcBxPortNoLink", 303), ("fcBxPortLossOfSync", 304), ("fcBxPortTransmitMismatch", 306), ("fcBxPortPcsLossSync", 307), ("fcipLinkNoLink", 311), ("fcipLinkLossOfSync", 312), ("fcipSntpFailure", 313), ("fcipIpsecFailure", 314), ("fcipFarLossOfClient", 315), ("esconPortTransmitFault", 351), ("esconPortLossOfSignal", 352), ("esconPortNoLink", 353), ("esconPortLossOfSync", 354), ("edfaPumpTemperuture", 401), ("edfaHwFail", 403), ("edfaRvcSignalDetect", 404), ("edfaRcvPower", 406), ("edfaTemprature", 407), ("edfaEyeSafty", 408), ("edafGainFlatness", 409), ("edfaXmtPower", 410), ("edfaGain", 411), ("edfaEol", 412), ("muxAisPath", 451), ("muxLof", 452), ("muxRdi", 453), ("muxInbandFail", 454), ("muxTempLicense", 455), ("muxNoLicense", 456), ("oswHwFail", 470), ("oswLossOfSignal", 471), ("oswEdfaLossProp", 472), ("loopback", 501), ("apsForceActive", 502), ("apsManualActive", 503), ("cluHoldoverState", 602), ("cluFreerunState", 603), ("cluBelowLevel", 604), ("cluFail", 606), ("cluJittered", 608), ("channelLowDegrade", 621), ("channelHighDegrade", 622), ("channelLowFail", 623), ("channelHighFail", 624), ("unequalizedOuputPower", 625), ("sfpTransmitFault", 701), ("sfpRemoved", 702), ("sfpMuxWlMismatch", 703), ("sfpBitRateMismatch", 704), ("sfpLossOfLock", 705), ("sfpSfpWlMismatch", 706), ("sfpLossOfLight", 707), ("sfpLaserEndOfLife", 708), ("sfpMuxSpacingMismatch", 709), ("sfpHardwareFault", 710), ("sfpBlocked", 711), ("sfpLossPropagation", 712), ("sfpUnknownType", 713), ("sfpHighTemp", 720), ("sfpLowTemp", 721), ("sfpHighTxPower", 726), ("sfpLowTxPower", 727), ("sfpHighRxPower", 728), ("sfpLowRxPower", 729), ("sfpHighLaserTemp", 730), ("sfpLowLaserTemp", 731), ("sfpHighLaserWl", 732), ("sfpLowLaserWl", 733), ("xfpTxNR", 734), ("xfpTxCdrNotLocked", 735), ("xfpRxNR", 736), ("xfpRxCdrNotLocked", 737), ("otnFecExc", 750), ("otnFecDeg", 751), ("otnOtuDeg", 752), ("otnOduDeg", 753), ("otnLos", 754), ("otnLof", 755), ("otnLom", 756), ("otuAis", 757), ("otuBdi", 758), ("otuTtim", 759), ("oduAis", 780), ("oduOci", 781), ("oduLck", 782), ("oduBdi", 783), ("oduTtim", 784), ("oduPtm", 785), ("entityRemoved", 801), ("entityClockFail", 803), ("entityHwTxFail", 804), ("entitySwMismatch", 806), ("entitySwUpgrade", 807), ("entitySwInvalidBank", 808), ("entityIpLanPending", 820), ("entityIpOscPending", 821), ("nePowerFault", 902), ("neFanFault", 903), ("neLowVoltagePower", 904), ("entitySwUpgradeFail", 905), ("entityRadiusPrimFail", 906), ("entityRadiusSecFail", 907), ("entityDbRestoreFail", 908), ("entityDbRestoreInProgress", 909), ("entitySntpFail", 910), ("dcActive", 1001), ("lcpDown", 1002), ("ncpDown", 1003), ("rtcFailure", 1004))

slAlarmConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 3, 20, 1))
slAlarmTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 3, 20, 2))
slAlarmTraps0 = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 3, 20, 2, 0))
slAlarmConfigTable = MibTable((1, 3, 6, 1, 4, 1, 4515, 1, 3, 20, 1, 1), )
if mibBuilder.loadTexts: slAlarmConfigTable.setStatus('current')
if mibBuilder.loadTexts: slAlarmConfigTable.setDescription('This table contains objects to configure the SL Alarms.')
slAlarmConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4515, 1, 3, 20, 1, 1, 1), ).setIndexNames((0, "SL-ALARM-MIB", "slAlarmIfIndex"), (0, "SL-ALARM-MIB", "slAlarmType"))
if mibBuilder.loadTexts: slAlarmConfigEntry.setStatus('current')
if mibBuilder.loadTexts: slAlarmConfigEntry.setDescription('An entry exist for each type of alarm.\n             The entry describes the alarm properties.')
slAlarmIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 20, 1, 1, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slAlarmIfIndex.setStatus('current')
if mibBuilder.loadTexts: slAlarmIfIndex.setDescription('The corresponding interface index.\n         The interface type may be one of:\n         \t- Sonet Line, \n         \t- Sonet Path, \n         \t- CLU\n         \t- NE.')
slAlarmType = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 20, 1, 1, 1, 2), SlAlarmType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slAlarmType.setStatus('current')
if mibBuilder.loadTexts: slAlarmType.setDescription('The alarm type.')
slAlarmSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 20, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("noAlarm", 0), ("critical", 1), ("major", 2), ("minor", 3), ("cleared", 4), ("notification", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: slAlarmSeverity.setStatus('current')
if mibBuilder.loadTexts: slAlarmSeverity.setDescription('The alarm severity.')
slAlarmServiceAffect = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 20, 1, 1, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slAlarmServiceAffect.setStatus('current')
if mibBuilder.loadTexts: slAlarmServiceAffect.setDescription('The alarm service affecting Yes/No.')
slAlarmTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 20, 1, 1, 1, 5), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slAlarmTimeStamp.setStatus('current')
if mibBuilder.loadTexts: slAlarmTimeStamp.setDescription('The calendar time of the alarm.')
slAlarmAcknowledged = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 20, 1, 1, 1, 6), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slAlarmAcknowledged.setStatus('current')
if mibBuilder.loadTexts: slAlarmAcknowledged.setDescription('Allow the NMS to acknowledge an active alarm.')
slAlarmAckUser = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 20, 1, 1, 1, 7), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slAlarmAckUser.setStatus('current')
if mibBuilder.loadTexts: slAlarmAckUser.setDescription('The name of the user that performed the Ack.')
slAlarmText = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 20, 1, 1, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slAlarmText.setStatus('current')
if mibBuilder.loadTexts: slAlarmText.setDescription('The alarm text.')
slAlarmActive = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 20, 2, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slAlarmActive.setStatus('current')
if mibBuilder.loadTexts: slAlarmActive.setDescription('The alarm is active Yes/No.')
slAlarmTrap = NotificationType((1, 3, 6, 1, 4, 1, 4515, 1, 3, 20, 2, 2)).setObjects(("SL-ALARM-MIB", "slAlarmIfIndex"), ("SL-ALARM-MIB", "slAlarmType"), ("SL-ALARM-MIB", "slAlarmSeverity"), ("SL-ALARM-MIB", "slAlarmServiceAffect"), ("SL-ALARM-MIB", "slAlarmActive"), ("SL-ALARM-MIB", "slAlarmText"))
if mibBuilder.loadTexts: slAlarmTrap.setStatus('current')
if mibBuilder.loadTexts: slAlarmTrap.setDescription('An slAlarmTrap notification is sent when an alarm occures.')
slAlarmTrap0 = NotificationType((1, 3, 6, 1, 4, 1, 4515, 1, 3, 20, 2, 0, 2)).setObjects(("SL-ALARM-MIB", "slAlarmIfIndex"), ("SL-ALARM-MIB", "slAlarmType"), ("SL-ALARM-MIB", "slAlarmSeverity"), ("SL-ALARM-MIB", "slAlarmServiceAffect"), ("SL-ALARM-MIB", "slAlarmActive"), ("SL-ALARM-MIB", "slAlarmText"))
if mibBuilder.loadTexts: slAlarmTrap0.setStatus('current')
if mibBuilder.loadTexts: slAlarmTrap0.setDescription("An slAlarmTrap0 notification is sent when an alarm occures.\n                It is defined to support browsers that don't recognize RFC 2576.")
mibBuilder.exportSymbols("SL-ALARM-MIB", slAlarmText=slAlarmText, slAlarmTraps=slAlarmTraps, slAlarmConfig=slAlarmConfig, slAlarmTrap0=slAlarmTrap0, slAlarmTraps0=slAlarmTraps0, slAlarmConfigEntry=slAlarmConfigEntry, slAlarmType=slAlarmType, slAlarmActive=slAlarmActive, slAlarmMib=slAlarmMib, slAlarmTimeStamp=slAlarmTimeStamp, PYSNMP_MODULE_ID=slAlarmMib, slAlarmSeverity=slAlarmSeverity, slAlarmTrap=slAlarmTrap, SlAlarmType=SlAlarmType, slAlarmServiceAffect=slAlarmServiceAffect, slAlarmConfigTable=slAlarmConfigTable, slAlarmAcknowledged=slAlarmAcknowledged, slAlarmAckUser=slAlarmAckUser, slAlarmIfIndex=slAlarmIfIndex)
