#
# PySNMP MIB module SIAE-SFP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/siae/SIAE-SFP-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 18:19:21 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
AlarmSeverityCode, AlarmStatus = mibBuilder.importSymbols("SIAE-ALARM-MIB", "AlarmSeverityCode", "AlarmStatus")
siaeMib, = mibBuilder.importSymbols("SIAE-TREE-MIB", "siaeMib")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, NotificationType, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, iso, Bits, TimeTicks, IpAddress, MibIdentifier, ObjectIdentity, Counter32, Gauge32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "NotificationType", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "iso", "Bits", "TimeTicks", "IpAddress", "MibIdentifier", "ObjectIdentity", "Counter32", "Gauge32", "Counter64")
TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString")
sfp = ModuleIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 74))
sfp.setRevisions(('2016-12-15 00:00', '2016-09-29 00:00', '2014-02-03 00:00', '2013-12-05 00:00',))
if mibBuilder.loadTexts: sfp.setLastUpdated('201612150000Z')
if mibBuilder.loadTexts: sfp.setOrganization('SIAE MICROELETTRONICA spa')
class Temperature(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-2000, 2000)

class PhysicalQuantity(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("phyQtTemperature", 1), ("phyQtVoltage", 2), ("phyQtTxBias", 3), ("phyQtTxPower", 4), ("phyQtRxPower", 5))

sfpMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 74, 1), Integer32().clone(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpMibVersion.setStatus('current')
sfpSerialIdTable = MibTable((1, 3, 6, 1, 4, 1, 3373, 1103, 74, 2), )
if mibBuilder.loadTexts: sfpSerialIdTable.setStatus('current')
sfpSerialIdEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3373, 1103, 74, 2, 1), ).setIndexNames((0, "SIAE-SFP-MIB", "sfpModuleId"))
if mibBuilder.loadTexts: sfpSerialIdEntry.setStatus('current')
sfpModuleId = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 74, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpModuleId.setStatus('current')
sfpSerialIdValid = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 74, 2, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpSerialIdValid.setStatus('current')
sfpVendorName = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 74, 2, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpVendorName.setStatus('current')
sfpVendorPartNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 74, 2, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpVendorPartNumber.setStatus('current')
sfpVendorRev = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 74, 2, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpVendorRev.setStatus('current')
sfpVendorSN = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 74, 2, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpVendorSN.setStatus('current')
sfpVendorDateCode = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 74, 2, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpVendorDateCode.setStatus('current')
sfpDiagMonitorCode = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 74, 2, 1, 8), Bits().clone(namedValues=NamedValues(("sfpDMCtypeLegacy", 0), ("sfpDMCtypeImplemented", 1), ("sfpDMCtypeInternalCal", 2), ("sfpDMCtypeExternalCal", 3), ("sfpDMCtypeRxAvgPwr", 4), ("sfpDMCtypeAddrChngReqrd", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpDiagMonitorCode.setStatus('current')
sfpEnhancedOptionsCode = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 74, 2, 1, 9), Bits().clone(namedValues=NamedValues(("sfpEOCalarmsImplemented", 0), ("sfpEOCSoftTxDisable", 1), ("sfpEOCSoftTxFault", 2), ("sfpEOCSoftRxLOS", 3), ("sfpEOCSoftRateSelect", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpEnhancedOptionsCode.setStatus('current')
sfpOptions = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 74, 2, 1, 10), Bits().clone(namedValues=NamedValues(("sfpOPTRateSelect", 0), ("sfpOPTTxDisable", 1), ("sfpOPTTxFault", 2), ("sfpOPTInvertedLOS", 3), ("sfpOPTlos", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpOptions.setStatus('current')
sfpFibreChannelMedia = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 74, 2, 1, 11), Bits().clone(namedValues=NamedValues(("sfpMultiMode62u5", 0), ("sfpMultiMode50u0", 1), ("sfpSingleMode", 2), ("sfpTwistedAxialPair", 3), ("sfpShieldedTwistedPair", 4), ("sfpMiniatureCoax", 5), ("sfpVideoCoax", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpFibreChannelMedia.setStatus('current')
sfpCompliance = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 74, 2, 1, 12), Bits().clone(namedValues=NamedValues(("sfpSonetReachSpecifier1", 0), ("sfpSonetReachSpecifier2", 1), ("sfpSonetOC48LongReach", 2), ("sfpSonetOC48IntermediateReach", 3), ("sfpSonetOC48ShortReach", 4), ("sfpSonetOC12LongReach", 5), ("sfpSonetOC12IntermediateReach", 6), ("sfpSonetOC12ShortReach", 7), ("sfpSonetOC3LongReach", 8), ("sfpSonetOC3IntermediateReach", 9), ("sfpSonetOC3ShortReach", 10), ("sfp1000BaseT", 11), ("sfp1000BaseCX", 12), ("sfp1000BaseLX", 13), ("sfp1000baseSX", 14), ("sfpBasePX", 15), ("sfpBaseBX10", 16), ("sfp100BaseFX", 17), ("sfp100BaseLX", 18)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpCompliance.setStatus('current')
sfpWavelength = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 74, 2, 1, 13), Integer32()).setUnits('nm').setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpWavelength.setStatus('current')
sfpNominalBitRate = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 74, 2, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpNominalBitRate.setStatus('current')
sfpLinkLength9u = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 74, 2, 1, 15), Integer32()).setUnits('m').setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpLinkLength9u.setStatus('current')
sfpLinkLength50u = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 74, 2, 1, 16), Integer32()).setUnits('m').setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpLinkLength50u.setStatus('current')
sfpLinkLength62u5 = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 74, 2, 1, 17), Integer32()).setUnits('m').setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpLinkLength62u5.setStatus('current')
sfpLinkLengthCopper = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 74, 2, 1, 18), Integer32()).setUnits('m').setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpLinkLengthCopper.setStatus('current')
sfpLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 74, 2, 1, 19), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpLabel.setStatus('current')
sfpFailAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 74, 2, 1, 20), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpFailAlarm.setStatus('current')
sfpFailAlarmSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 74, 6), AlarmSeverityCode().clone('majorTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpFailAlarmSeverityCode.setStatus('current')
sfpDiagnosticTable = MibTable((1, 3, 6, 1, 4, 1, 3373, 1103, 74, 7), )
if mibBuilder.loadTexts: sfpDiagnosticTable.setStatus('current')
sfpDiagnosticEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3373, 1103, 74, 7, 1), ).setIndexNames((0, "SIAE-SFP-MIB", "sfpModuleId"))
if mibBuilder.loadTexts: sfpDiagnosticEntry.setStatus('current')
sfpDiagnosticValid = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 74, 7, 1, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpDiagnosticValid.setStatus('current')
sfpLOSPinOut = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 74, 7, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpLOSPinOut.setStatus('current')
sfpTxFaultPinOut = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 74, 7, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpTxFaultPinOut.setStatus('current')
sfpRateSelectPinIn = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 74, 7, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpRateSelectPinIn.setStatus('current')
sfpTxDisablePinIn = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 74, 7, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpTxDisablePinIn.setStatus('current')
sfpTemperature = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 74, 7, 1, 6), Temperature()).setUnits('C/10').setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpTemperature.setStatus('current')
sfpVoltage = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 74, 7, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setUnits('milliVolts (mV)').setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpVoltage.setStatus('current')
sfpTxBias = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 74, 7, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 131000))).setUnits('microAmps (uA)').setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpTxBias.setStatus('current')
sfpTxPower = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 74, 7, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setUnits('microWatts (uW)').setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpTxPower.setStatus('current')
sfpRxPower = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 74, 7, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setUnits('microWatts (uW)').setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpRxPower.setStatus('current')
sfpInternalAlarms = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 74, 7, 1, 11), Bits().clone(namedValues=NamedValues(("sfpIntAlarmTempHigh", 0), ("sfpIntAlarmTempLow", 1), ("sfpIntAlarmVoltageHigh", 2), ("sfpIntAlarmVoltageLow", 3), ("sfpIntAlarmTxBiasHigh", 4), ("sfpIntAlarmTxBiasLow", 5), ("sfpIntAlarmTxPowerHigh", 6), ("sfpIntAlarmTxPowerLow", 7), ("sfpIntAlarmRxPowerHigh", 8), ("sfpIntAlarmRxPowerLow", 9)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpInternalAlarms.setStatus('current')
sfpInternalWarnings = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 74, 7, 1, 12), Bits().clone(namedValues=NamedValues(("sfpIntWarnTempHigh", 0), ("sfpIntWarnTempLow", 1), ("sfpIntWarnVoltageHigh", 2), ("sfpIntWarnVoltageLow", 3), ("sfpIntWarnTxBiasHigh", 4), ("sfpIntWarnTxBiasLow", 5), ("sfpIntWarnTxPowerHigh", 6), ("sfpIntWarnTxPowerLow", 7), ("sfpIntWarnRxPowerHigh", 8), ("sfpIntWarnRxPowerLow", 9)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpInternalWarnings.setStatus('current')
sfpAlarmTable = MibTable((1, 3, 6, 1, 4, 1, 3373, 1103, 74, 10), )
if mibBuilder.loadTexts: sfpAlarmTable.setStatus('current')
sfpAlarmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3373, 1103, 74, 10, 1), ).setIndexNames((0, "SIAE-SFP-MIB", "sfpModuleId"), (0, "SIAE-SFP-MIB", "sfpPhysicalQuantity"))
if mibBuilder.loadTexts: sfpAlarmEntry.setStatus('current')
sfpPhysicalQuantity = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 74, 10, 1, 1), PhysicalQuantity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpPhysicalQuantity.setStatus('current')
sfpThresholdHighAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 74, 10, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpThresholdHighAlarm.setStatus('current')
sfpThresholdHighWarning = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 74, 10, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpThresholdHighWarning.setStatus('current')
sfpThresholdLowAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 74, 10, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpThresholdLowAlarm.setStatus('current')
sfpThresholdLowWarning = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 74, 10, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpThresholdLowWarning.setStatus('current')
sfpHighAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 74, 10, 1, 6), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpHighAlarm.setStatus('current')
sfpHighWarningAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 74, 10, 1, 7), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpHighWarningAlarm.setStatus('current')
sfpLowAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 74, 10, 1, 8), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpLowAlarm.setStatus('current')
sfpLowWarningAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 74, 10, 1, 9), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpLowWarningAlarm.setStatus('current')
sfpHighAlarmSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 74, 11), AlarmSeverityCode().clone('majorTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpHighAlarmSeverityCode.setStatus('current')
sfpHighWarningAlarmSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 74, 12), AlarmSeverityCode().clone('warningTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpHighWarningAlarmSeverityCode.setStatus('current')
sfpLowAlarmSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 74, 13), AlarmSeverityCode().clone('majorTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpLowAlarmSeverityCode.setStatus('current')
sfpLowWarningAlarmSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 74, 14), AlarmSeverityCode().clone('warningTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpLowWarningAlarmSeverityCode.setStatus('current')
mibBuilder.exportSymbols("SIAE-SFP-MIB", sfpTemperature=sfpTemperature, sfpLabel=sfpLabel, sfpRateSelectPinIn=sfpRateSelectPinIn, sfpLowAlarmSeverityCode=sfpLowAlarmSeverityCode, sfpVendorDateCode=sfpVendorDateCode, sfpInternalWarnings=sfpInternalWarnings, sfpDiagnosticValid=sfpDiagnosticValid, sfpDiagnosticEntry=sfpDiagnosticEntry, sfpLOSPinOut=sfpLOSPinOut, sfpHighWarningAlarmSeverityCode=sfpHighWarningAlarmSeverityCode, sfpInternalAlarms=sfpInternalAlarms, sfpDiagnosticTable=sfpDiagnosticTable, sfpVendorRev=sfpVendorRev, sfpVendorSN=sfpVendorSN, sfpLinkLength62u5=sfpLinkLength62u5, sfpLowWarningAlarmSeverityCode=sfpLowWarningAlarmSeverityCode, sfpModuleId=sfpModuleId, sfpTxFaultPinOut=sfpTxFaultPinOut, sfpLinkLengthCopper=sfpLinkLengthCopper, PYSNMP_MODULE_ID=sfp, sfpMibVersion=sfpMibVersion, PhysicalQuantity=PhysicalQuantity, sfpFailAlarm=sfpFailAlarm, sfpTxDisablePinIn=sfpTxDisablePinIn, sfpVendorName=sfpVendorName, sfpVoltage=sfpVoltage, sfpHighWarningAlarm=sfpHighWarningAlarm, sfpSerialIdTable=sfpSerialIdTable, sfpRxPower=sfpRxPower, sfpLowAlarm=sfpLowAlarm, sfpTxBias=sfpTxBias, sfpWavelength=sfpWavelength, sfpFibreChannelMedia=sfpFibreChannelMedia, sfpThresholdHighWarning=sfpThresholdHighWarning, sfp=sfp, sfpEnhancedOptionsCode=sfpEnhancedOptionsCode, sfpSerialIdEntry=sfpSerialIdEntry, sfpHighAlarmSeverityCode=sfpHighAlarmSeverityCode, sfpDiagMonitorCode=sfpDiagMonitorCode, sfpPhysicalQuantity=sfpPhysicalQuantity, sfpLinkLength9u=sfpLinkLength9u, sfpThresholdLowAlarm=sfpThresholdLowAlarm, sfpOptions=sfpOptions, sfpFailAlarmSeverityCode=sfpFailAlarmSeverityCode, sfpAlarmEntry=sfpAlarmEntry, sfpTxPower=sfpTxPower, sfpThresholdLowWarning=sfpThresholdLowWarning, sfpAlarmTable=sfpAlarmTable, sfpCompliance=sfpCompliance, sfpSerialIdValid=sfpSerialIdValid, sfpLinkLength50u=sfpLinkLength50u, sfpThresholdHighAlarm=sfpThresholdHighAlarm, sfpHighAlarm=sfpHighAlarm, sfpNominalBitRate=sfpNominalBitRate, sfpVendorPartNumber=sfpVendorPartNumber, sfpLowWarningAlarm=sfpLowWarningAlarm, Temperature=Temperature)
