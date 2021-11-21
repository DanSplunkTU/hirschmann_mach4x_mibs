#
# PySNMP MIB module UPS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/output/asn1/UPS-MIB
# Produced by pysmi-1.1.3 at Sun Nov 21 00:35:32 2021
# On host fv-az39-63 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, mib_2, TimeTicks, NotificationType, ModuleIdentity, Gauge32, Bits, Counter32, Integer32, ObjectIdentity, Counter64, Unsigned32, iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "mib-2", "TimeTicks", "NotificationType", "ModuleIdentity", "Gauge32", "Bits", "Counter32", "Integer32", "ObjectIdentity", "Counter64", "Unsigned32", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, TimeInterval, TimeStamp, DisplayString, AutonomousType, TestAndIncr = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TimeInterval", "TimeStamp", "DisplayString", "AutonomousType", "TestAndIncr")
upsMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 33))
if mibBuilder.loadTexts: upsMIB.setLastUpdated('9402230000Z')
if mibBuilder.loadTexts: upsMIB.setOrganization('IETF UPS MIB Working Group')
class PositiveInteger(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class NonNegativeInteger(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

upsObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 33, 1))
upsIdent = MibIdentifier((1, 3, 6, 1, 2, 1, 33, 1, 1))
upsIdentManufacturer = MibScalar((1, 3, 6, 1, 2, 1, 33, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: upsIdentManufacturer.setStatus('current')
upsIdentModel = MibScalar((1, 3, 6, 1, 2, 1, 33, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: upsIdentModel.setStatus('current')
upsIdentUPSSoftwareVersion = MibScalar((1, 3, 6, 1, 2, 1, 33, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: upsIdentUPSSoftwareVersion.setStatus('current')
upsIdentAgentSoftwareVersion = MibScalar((1, 3, 6, 1, 2, 1, 33, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: upsIdentAgentSoftwareVersion.setStatus('current')
upsIdentName = MibScalar((1, 3, 6, 1, 2, 1, 33, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: upsIdentName.setStatus('current')
upsIdentAttachedDevices = MibScalar((1, 3, 6, 1, 2, 1, 33, 1, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: upsIdentAttachedDevices.setStatus('current')
upsBattery = MibIdentifier((1, 3, 6, 1, 2, 1, 33, 1, 2))
upsBatteryStatus = MibScalar((1, 3, 6, 1, 2, 1, 33, 1, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("unknown", 1), ("batteryNormal", 2), ("batteryLow", 3), ("batteryDepleted", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: upsBatteryStatus.setStatus('current')
upsSecondsOnBattery = MibScalar((1, 3, 6, 1, 2, 1, 33, 1, 2, 2), NonNegativeInteger()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: upsSecondsOnBattery.setStatus('current')
upsEstimatedMinutesRemaining = MibScalar((1, 3, 6, 1, 2, 1, 33, 1, 2, 3), PositiveInteger()).setUnits('minutes').setMaxAccess("readonly")
if mibBuilder.loadTexts: upsEstimatedMinutesRemaining.setStatus('current')
upsEstimatedChargeRemaining = MibScalar((1, 3, 6, 1, 2, 1, 33, 1, 2, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setUnits('percent').setMaxAccess("readonly")
if mibBuilder.loadTexts: upsEstimatedChargeRemaining.setStatus('current')
upsBatteryVoltage = MibScalar((1, 3, 6, 1, 2, 1, 33, 1, 2, 5), NonNegativeInteger()).setUnits('0.1 Volt DC').setMaxAccess("readonly")
if mibBuilder.loadTexts: upsBatteryVoltage.setStatus('current')
upsBatteryCurrent = MibScalar((1, 3, 6, 1, 2, 1, 33, 1, 2, 6), Integer32()).setUnits('0.1 Amp DC').setMaxAccess("readonly")
if mibBuilder.loadTexts: upsBatteryCurrent.setStatus('current')
upsBatteryTemperature = MibScalar((1, 3, 6, 1, 2, 1, 33, 1, 2, 7), Integer32()).setUnits('degrees Centigrade').setMaxAccess("readonly")
if mibBuilder.loadTexts: upsBatteryTemperature.setStatus('current')
upsInput = MibIdentifier((1, 3, 6, 1, 2, 1, 33, 1, 3))
upsInputLineBads = MibScalar((1, 3, 6, 1, 2, 1, 33, 1, 3, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: upsInputLineBads.setStatus('current')
upsInputNumLines = MibScalar((1, 3, 6, 1, 2, 1, 33, 1, 3, 2), NonNegativeInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: upsInputNumLines.setStatus('current')
upsInputTable = MibTable((1, 3, 6, 1, 2, 1, 33, 1, 3, 3), )
if mibBuilder.loadTexts: upsInputTable.setStatus('current')
upsInputEntry = MibTableRow((1, 3, 6, 1, 2, 1, 33, 1, 3, 3, 1), ).setIndexNames((0, "UPS-MIB", "upsInputLineIndex"))
if mibBuilder.loadTexts: upsInputEntry.setStatus('current')
upsInputLineIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 33, 1, 3, 3, 1, 1), PositiveInteger())
if mibBuilder.loadTexts: upsInputLineIndex.setStatus('current')
upsInputFrequency = MibTableColumn((1, 3, 6, 1, 2, 1, 33, 1, 3, 3, 1, 2), NonNegativeInteger()).setUnits('0.1 Hertz').setMaxAccess("readonly")
if mibBuilder.loadTexts: upsInputFrequency.setStatus('current')
upsInputVoltage = MibTableColumn((1, 3, 6, 1, 2, 1, 33, 1, 3, 3, 1, 3), NonNegativeInteger()).setUnits('RMS Volts').setMaxAccess("readonly")
if mibBuilder.loadTexts: upsInputVoltage.setStatus('current')
upsInputCurrent = MibTableColumn((1, 3, 6, 1, 2, 1, 33, 1, 3, 3, 1, 4), NonNegativeInteger()).setUnits('0.1 RMS Amp').setMaxAccess("readonly")
if mibBuilder.loadTexts: upsInputCurrent.setStatus('current')
upsInputTruePower = MibTableColumn((1, 3, 6, 1, 2, 1, 33, 1, 3, 3, 1, 5), NonNegativeInteger()).setUnits('Watts').setMaxAccess("readonly")
if mibBuilder.loadTexts: upsInputTruePower.setStatus('current')
upsOutput = MibIdentifier((1, 3, 6, 1, 2, 1, 33, 1, 4))
upsOutputSource = MibScalar((1, 3, 6, 1, 2, 1, 33, 1, 4, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("other", 1), ("none", 2), ("normal", 3), ("bypass", 4), ("battery", 5), ("booster", 6), ("reducer", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: upsOutputSource.setStatus('current')
upsOutputFrequency = MibScalar((1, 3, 6, 1, 2, 1, 33, 1, 4, 2), NonNegativeInteger()).setUnits('0.1 Hertz').setMaxAccess("readonly")
if mibBuilder.loadTexts: upsOutputFrequency.setStatus('current')
upsOutputNumLines = MibScalar((1, 3, 6, 1, 2, 1, 33, 1, 4, 3), NonNegativeInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: upsOutputNumLines.setStatus('current')
upsOutputTable = MibTable((1, 3, 6, 1, 2, 1, 33, 1, 4, 4), )
if mibBuilder.loadTexts: upsOutputTable.setStatus('current')
upsOutputEntry = MibTableRow((1, 3, 6, 1, 2, 1, 33, 1, 4, 4, 1), ).setIndexNames((0, "UPS-MIB", "upsOutputLineIndex"))
if mibBuilder.loadTexts: upsOutputEntry.setStatus('current')
upsOutputLineIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 33, 1, 4, 4, 1, 1), PositiveInteger())
if mibBuilder.loadTexts: upsOutputLineIndex.setStatus('current')
upsOutputVoltage = MibTableColumn((1, 3, 6, 1, 2, 1, 33, 1, 4, 4, 1, 2), NonNegativeInteger()).setUnits('RMS Volts').setMaxAccess("readonly")
if mibBuilder.loadTexts: upsOutputVoltage.setStatus('current')
upsOutputCurrent = MibTableColumn((1, 3, 6, 1, 2, 1, 33, 1, 4, 4, 1, 3), NonNegativeInteger()).setUnits('0.1 RMS Amp').setMaxAccess("readonly")
if mibBuilder.loadTexts: upsOutputCurrent.setStatus('current')
upsOutputPower = MibTableColumn((1, 3, 6, 1, 2, 1, 33, 1, 4, 4, 1, 4), NonNegativeInteger()).setUnits('Watts').setMaxAccess("readonly")
if mibBuilder.loadTexts: upsOutputPower.setStatus('current')
upsOutputPercentLoad = MibTableColumn((1, 3, 6, 1, 2, 1, 33, 1, 4, 4, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 200))).setUnits('percent').setMaxAccess("readonly")
if mibBuilder.loadTexts: upsOutputPercentLoad.setStatus('current')
upsBypass = MibIdentifier((1, 3, 6, 1, 2, 1, 33, 1, 5))
upsBypassFrequency = MibScalar((1, 3, 6, 1, 2, 1, 33, 1, 5, 1), NonNegativeInteger()).setUnits('0.1 Hertz').setMaxAccess("readonly")
if mibBuilder.loadTexts: upsBypassFrequency.setStatus('current')
upsBypassNumLines = MibScalar((1, 3, 6, 1, 2, 1, 33, 1, 5, 2), NonNegativeInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: upsBypassNumLines.setStatus('current')
upsBypassTable = MibTable((1, 3, 6, 1, 2, 1, 33, 1, 5, 3), )
if mibBuilder.loadTexts: upsBypassTable.setStatus('current')
upsBypassEntry = MibTableRow((1, 3, 6, 1, 2, 1, 33, 1, 5, 3, 1), ).setIndexNames((0, "UPS-MIB", "upsBypassLineIndex"))
if mibBuilder.loadTexts: upsBypassEntry.setStatus('current')
upsBypassLineIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 33, 1, 5, 3, 1, 1), PositiveInteger())
if mibBuilder.loadTexts: upsBypassLineIndex.setStatus('current')
upsBypassVoltage = MibTableColumn((1, 3, 6, 1, 2, 1, 33, 1, 5, 3, 1, 2), NonNegativeInteger()).setUnits('RMS Volts').setMaxAccess("readonly")
if mibBuilder.loadTexts: upsBypassVoltage.setStatus('current')
upsBypassCurrent = MibTableColumn((1, 3, 6, 1, 2, 1, 33, 1, 5, 3, 1, 3), NonNegativeInteger()).setUnits('0.1 RMS Amp').setMaxAccess("readonly")
if mibBuilder.loadTexts: upsBypassCurrent.setStatus('current')
upsBypassPower = MibTableColumn((1, 3, 6, 1, 2, 1, 33, 1, 5, 3, 1, 4), NonNegativeInteger()).setUnits('Watts').setMaxAccess("readonly")
if mibBuilder.loadTexts: upsBypassPower.setStatus('current')
upsAlarm = MibIdentifier((1, 3, 6, 1, 2, 1, 33, 1, 6))
upsAlarmsPresent = MibScalar((1, 3, 6, 1, 2, 1, 33, 1, 6, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: upsAlarmsPresent.setStatus('current')
upsAlarmTable = MibTable((1, 3, 6, 1, 2, 1, 33, 1, 6, 2), )
if mibBuilder.loadTexts: upsAlarmTable.setStatus('current')
upsAlarmEntry = MibTableRow((1, 3, 6, 1, 2, 1, 33, 1, 6, 2, 1), ).setIndexNames((0, "UPS-MIB", "upsAlarmId"))
if mibBuilder.loadTexts: upsAlarmEntry.setStatus('current')
upsAlarmId = MibTableColumn((1, 3, 6, 1, 2, 1, 33, 1, 6, 2, 1, 1), PositiveInteger())
if mibBuilder.loadTexts: upsAlarmId.setStatus('current')
upsAlarmDescr = MibTableColumn((1, 3, 6, 1, 2, 1, 33, 1, 6, 2, 1, 2), AutonomousType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: upsAlarmDescr.setStatus('current')
upsAlarmTime = MibTableColumn((1, 3, 6, 1, 2, 1, 33, 1, 6, 2, 1, 3), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: upsAlarmTime.setStatus('current')
upsWellKnownAlarms = MibIdentifier((1, 3, 6, 1, 2, 1, 33, 1, 6, 3))
upsAlarmBatteryBad = ObjectIdentity((1, 3, 6, 1, 2, 1, 33, 1, 6, 3, 1))
if mibBuilder.loadTexts: upsAlarmBatteryBad.setStatus('current')
upsAlarmOnBattery = ObjectIdentity((1, 3, 6, 1, 2, 1, 33, 1, 6, 3, 2))
if mibBuilder.loadTexts: upsAlarmOnBattery.setStatus('current')
upsAlarmLowBattery = ObjectIdentity((1, 3, 6, 1, 2, 1, 33, 1, 6, 3, 3))
if mibBuilder.loadTexts: upsAlarmLowBattery.setStatus('current')
upsAlarmDepletedBattery = ObjectIdentity((1, 3, 6, 1, 2, 1, 33, 1, 6, 3, 4))
if mibBuilder.loadTexts: upsAlarmDepletedBattery.setStatus('current')
upsAlarmTempBad = ObjectIdentity((1, 3, 6, 1, 2, 1, 33, 1, 6, 3, 5))
if mibBuilder.loadTexts: upsAlarmTempBad.setStatus('current')
upsAlarmInputBad = ObjectIdentity((1, 3, 6, 1, 2, 1, 33, 1, 6, 3, 6))
if mibBuilder.loadTexts: upsAlarmInputBad.setStatus('current')
upsAlarmOutputBad = ObjectIdentity((1, 3, 6, 1, 2, 1, 33, 1, 6, 3, 7))
if mibBuilder.loadTexts: upsAlarmOutputBad.setStatus('current')
upsAlarmOutputOverload = ObjectIdentity((1, 3, 6, 1, 2, 1, 33, 1, 6, 3, 8))
if mibBuilder.loadTexts: upsAlarmOutputOverload.setStatus('current')
upsAlarmOnBypass = ObjectIdentity((1, 3, 6, 1, 2, 1, 33, 1, 6, 3, 9))
if mibBuilder.loadTexts: upsAlarmOnBypass.setStatus('current')
upsAlarmBypassBad = ObjectIdentity((1, 3, 6, 1, 2, 1, 33, 1, 6, 3, 10))
if mibBuilder.loadTexts: upsAlarmBypassBad.setStatus('current')
upsAlarmOutputOffAsRequested = ObjectIdentity((1, 3, 6, 1, 2, 1, 33, 1, 6, 3, 11))
if mibBuilder.loadTexts: upsAlarmOutputOffAsRequested.setStatus('current')
upsAlarmUpsOffAsRequested = ObjectIdentity((1, 3, 6, 1, 2, 1, 33, 1, 6, 3, 12))
if mibBuilder.loadTexts: upsAlarmUpsOffAsRequested.setStatus('current')
upsAlarmChargerFailed = ObjectIdentity((1, 3, 6, 1, 2, 1, 33, 1, 6, 3, 13))
if mibBuilder.loadTexts: upsAlarmChargerFailed.setStatus('current')
upsAlarmUpsOutputOff = ObjectIdentity((1, 3, 6, 1, 2, 1, 33, 1, 6, 3, 14))
if mibBuilder.loadTexts: upsAlarmUpsOutputOff.setStatus('current')
upsAlarmUpsSystemOff = ObjectIdentity((1, 3, 6, 1, 2, 1, 33, 1, 6, 3, 15))
if mibBuilder.loadTexts: upsAlarmUpsSystemOff.setStatus('current')
upsAlarmFanFailure = ObjectIdentity((1, 3, 6, 1, 2, 1, 33, 1, 6, 3, 16))
if mibBuilder.loadTexts: upsAlarmFanFailure.setStatus('current')
upsAlarmFuseFailure = ObjectIdentity((1, 3, 6, 1, 2, 1, 33, 1, 6, 3, 17))
if mibBuilder.loadTexts: upsAlarmFuseFailure.setStatus('current')
upsAlarmGeneralFault = ObjectIdentity((1, 3, 6, 1, 2, 1, 33, 1, 6, 3, 18))
if mibBuilder.loadTexts: upsAlarmGeneralFault.setStatus('current')
upsAlarmDiagnosticTestFailed = ObjectIdentity((1, 3, 6, 1, 2, 1, 33, 1, 6, 3, 19))
if mibBuilder.loadTexts: upsAlarmDiagnosticTestFailed.setStatus('current')
upsAlarmCommunicationsLost = ObjectIdentity((1, 3, 6, 1, 2, 1, 33, 1, 6, 3, 20))
if mibBuilder.loadTexts: upsAlarmCommunicationsLost.setStatus('current')
upsAlarmAwaitingPower = ObjectIdentity((1, 3, 6, 1, 2, 1, 33, 1, 6, 3, 21))
if mibBuilder.loadTexts: upsAlarmAwaitingPower.setStatus('current')
upsAlarmShutdownPending = ObjectIdentity((1, 3, 6, 1, 2, 1, 33, 1, 6, 3, 22))
if mibBuilder.loadTexts: upsAlarmShutdownPending.setStatus('current')
upsAlarmShutdownImminent = ObjectIdentity((1, 3, 6, 1, 2, 1, 33, 1, 6, 3, 23))
if mibBuilder.loadTexts: upsAlarmShutdownImminent.setStatus('current')
upsAlarmTestInProgress = ObjectIdentity((1, 3, 6, 1, 2, 1, 33, 1, 6, 3, 24))
if mibBuilder.loadTexts: upsAlarmTestInProgress.setStatus('current')
upsTest = MibIdentifier((1, 3, 6, 1, 2, 1, 33, 1, 7))
upsTestId = MibScalar((1, 3, 6, 1, 2, 1, 33, 1, 7, 1), ObjectIdentifier()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: upsTestId.setStatus('current')
upsTestSpinLock = MibScalar((1, 3, 6, 1, 2, 1, 33, 1, 7, 2), TestAndIncr()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: upsTestSpinLock.setStatus('current')
upsTestResultsSummary = MibScalar((1, 3, 6, 1, 2, 1, 33, 1, 7, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("donePass", 1), ("doneWarning", 2), ("doneError", 3), ("aborted", 4), ("inProgress", 5), ("noTestsInitiated", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: upsTestResultsSummary.setStatus('current')
upsTestResultsDetail = MibScalar((1, 3, 6, 1, 2, 1, 33, 1, 7, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: upsTestResultsDetail.setStatus('current')
upsTestStartTime = MibScalar((1, 3, 6, 1, 2, 1, 33, 1, 7, 5), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: upsTestStartTime.setStatus('current')
upsTestElapsedTime = MibScalar((1, 3, 6, 1, 2, 1, 33, 1, 7, 6), TimeInterval()).setMaxAccess("readonly")
if mibBuilder.loadTexts: upsTestElapsedTime.setStatus('current')
upsWellKnownTests = MibIdentifier((1, 3, 6, 1, 2, 1, 33, 1, 7, 7))
upsTestNoTestsInitiated = ObjectIdentity((1, 3, 6, 1, 2, 1, 33, 1, 7, 7, 1))
if mibBuilder.loadTexts: upsTestNoTestsInitiated.setStatus('current')
upsTestAbortTestInProgress = ObjectIdentity((1, 3, 6, 1, 2, 1, 33, 1, 7, 7, 2))
if mibBuilder.loadTexts: upsTestAbortTestInProgress.setStatus('current')
upsTestGeneralSystemsTest = ObjectIdentity((1, 3, 6, 1, 2, 1, 33, 1, 7, 7, 3))
if mibBuilder.loadTexts: upsTestGeneralSystemsTest.setStatus('current')
upsTestQuickBatteryTest = ObjectIdentity((1, 3, 6, 1, 2, 1, 33, 1, 7, 7, 4))
if mibBuilder.loadTexts: upsTestQuickBatteryTest.setStatus('current')
upsTestDeepBatteryCalibration = ObjectIdentity((1, 3, 6, 1, 2, 1, 33, 1, 7, 7, 5))
if mibBuilder.loadTexts: upsTestDeepBatteryCalibration.setStatus('current')
upsControl = MibIdentifier((1, 3, 6, 1, 2, 1, 33, 1, 8))
upsShutdownType = MibScalar((1, 3, 6, 1, 2, 1, 33, 1, 8, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("output", 1), ("system", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: upsShutdownType.setStatus('current')
upsShutdownAfterDelay = MibScalar((1, 3, 6, 1, 2, 1, 33, 1, 8, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 2147483648))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: upsShutdownAfterDelay.setStatus('current')
upsStartupAfterDelay = MibScalar((1, 3, 6, 1, 2, 1, 33, 1, 8, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 2147483648))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: upsStartupAfterDelay.setStatus('current')
upsRebootWithDuration = MibScalar((1, 3, 6, 1, 2, 1, 33, 1, 8, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 300))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: upsRebootWithDuration.setStatus('current')
upsAutoRestart = MibScalar((1, 3, 6, 1, 2, 1, 33, 1, 8, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: upsAutoRestart.setStatus('current')
upsConfig = MibIdentifier((1, 3, 6, 1, 2, 1, 33, 1, 9))
upsConfigInputVoltage = MibScalar((1, 3, 6, 1, 2, 1, 33, 1, 9, 1), NonNegativeInteger()).setUnits('RMS Volts').setMaxAccess("readwrite")
if mibBuilder.loadTexts: upsConfigInputVoltage.setStatus('current')
upsConfigInputFreq = MibScalar((1, 3, 6, 1, 2, 1, 33, 1, 9, 2), NonNegativeInteger()).setUnits('0.1 Hertz').setMaxAccess("readwrite")
if mibBuilder.loadTexts: upsConfigInputFreq.setStatus('current')
upsConfigOutputVoltage = MibScalar((1, 3, 6, 1, 2, 1, 33, 1, 9, 3), NonNegativeInteger()).setUnits('RMS Volts').setMaxAccess("readwrite")
if mibBuilder.loadTexts: upsConfigOutputVoltage.setStatus('current')
upsConfigOutputFreq = MibScalar((1, 3, 6, 1, 2, 1, 33, 1, 9, 4), NonNegativeInteger()).setUnits('0.1 Hertz').setMaxAccess("readwrite")
if mibBuilder.loadTexts: upsConfigOutputFreq.setStatus('current')
upsConfigOutputVA = MibScalar((1, 3, 6, 1, 2, 1, 33, 1, 9, 5), NonNegativeInteger()).setUnits('Volt-Amps').setMaxAccess("readonly")
if mibBuilder.loadTexts: upsConfigOutputVA.setStatus('current')
upsConfigOutputPower = MibScalar((1, 3, 6, 1, 2, 1, 33, 1, 9, 6), NonNegativeInteger()).setUnits('Watts').setMaxAccess("readonly")
if mibBuilder.loadTexts: upsConfigOutputPower.setStatus('current')
upsConfigLowBattTime = MibScalar((1, 3, 6, 1, 2, 1, 33, 1, 9, 7), NonNegativeInteger()).setUnits('minutes').setMaxAccess("readwrite")
if mibBuilder.loadTexts: upsConfigLowBattTime.setStatus('current')
upsConfigAudibleStatus = MibScalar((1, 3, 6, 1, 2, 1, 33, 1, 9, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2), ("muted", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: upsConfigAudibleStatus.setStatus('current')
upsConfigLowVoltageTransferPoint = MibScalar((1, 3, 6, 1, 2, 1, 33, 1, 9, 9), NonNegativeInteger()).setUnits('RMS Volts').setMaxAccess("readwrite")
if mibBuilder.loadTexts: upsConfigLowVoltageTransferPoint.setStatus('current')
upsConfigHighVoltageTransferPoint = MibScalar((1, 3, 6, 1, 2, 1, 33, 1, 9, 10), NonNegativeInteger()).setUnits('RMS Volts').setMaxAccess("readwrite")
if mibBuilder.loadTexts: upsConfigHighVoltageTransferPoint.setStatus('current')
upsTraps = MibIdentifier((1, 3, 6, 1, 2, 1, 33, 2))
upsTrapOnBattery = NotificationType((1, 3, 6, 1, 2, 1, 33, 2, 1)).setObjects(("UPS-MIB", "upsEstimatedMinutesRemaining"), ("UPS-MIB", "upsSecondsOnBattery"), ("UPS-MIB", "upsConfigLowBattTime"))
if mibBuilder.loadTexts: upsTrapOnBattery.setStatus('current')
upsTrapTestCompleted = NotificationType((1, 3, 6, 1, 2, 1, 33, 2, 2)).setObjects(("UPS-MIB", "upsTestId"), ("UPS-MIB", "upsTestSpinLock"), ("UPS-MIB", "upsTestResultsSummary"), ("UPS-MIB", "upsTestResultsDetail"), ("UPS-MIB", "upsTestStartTime"), ("UPS-MIB", "upsTestElapsedTime"))
if mibBuilder.loadTexts: upsTrapTestCompleted.setStatus('current')
upsTrapAlarmEntryAdded = NotificationType((1, 3, 6, 1, 2, 1, 33, 2, 3)).setObjects(("UPS-MIB", "upsAlarmId"), ("UPS-MIB", "upsAlarmDescr"))
if mibBuilder.loadTexts: upsTrapAlarmEntryAdded.setStatus('current')
upsTrapAlarmEntryRemoved = NotificationType((1, 3, 6, 1, 2, 1, 33, 2, 4)).setObjects(("UPS-MIB", "upsAlarmId"), ("UPS-MIB", "upsAlarmDescr"))
if mibBuilder.loadTexts: upsTrapAlarmEntryRemoved.setStatus('current')
upsConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 33, 3))
upsCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 33, 3, 1))
upsSubsetCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 33, 3, 1, 1)).setObjects(("UPS-MIB", "upsSubsetIdentGroup"), ("UPS-MIB", "upsSubsetBatteryGroup"), ("UPS-MIB", "upsSubsetInputGroup"), ("UPS-MIB", "upsSubsetOutputGroup"), ("UPS-MIB", "upsSubsetAlarmGroup"), ("UPS-MIB", "upsSubsetControlGroup"), ("UPS-MIB", "upsSubsetConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    upsSubsetCompliance = upsSubsetCompliance.setStatus('current')
upsBasicCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 33, 3, 1, 2)).setObjects(("UPS-MIB", "upsBasicIdentGroup"), ("UPS-MIB", "upsBasicBatteryGroup"), ("UPS-MIB", "upsBasicInputGroup"), ("UPS-MIB", "upsBasicOutputGroup"), ("UPS-MIB", "upsBasicAlarmGroup"), ("UPS-MIB", "upsBasicTestGroup"), ("UPS-MIB", "upsBasicControlGroup"), ("UPS-MIB", "upsBasicConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    upsBasicCompliance = upsBasicCompliance.setStatus('current')
upsFullCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 33, 3, 1, 3)).setObjects(("UPS-MIB", "upsFullIdentGroup"), ("UPS-MIB", "upsFullBatteryGroup"), ("UPS-MIB", "upsFullInputGroup"), ("UPS-MIB", "upsFullOutputGroup"), ("UPS-MIB", "upsFullAlarmGroup"), ("UPS-MIB", "upsFullTestGroup"), ("UPS-MIB", "upsFullControlGroup"), ("UPS-MIB", "upsFullConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    upsFullCompliance = upsFullCompliance.setStatus('current')
upsGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 33, 3, 2))
upsSubsetGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 33, 3, 2, 1))
upsSubsetIdentGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 33, 3, 2, 1, 1)).setObjects(("UPS-MIB", "upsIdentManufacturer"), ("UPS-MIB", "upsIdentModel"), ("UPS-MIB", "upsIdentAgentSoftwareVersion"), ("UPS-MIB", "upsIdentName"), ("UPS-MIB", "upsIdentAttachedDevices"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    upsSubsetIdentGroup = upsSubsetIdentGroup.setStatus('current')
upsSubsetBatteryGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 33, 3, 2, 1, 2)).setObjects(("UPS-MIB", "upsBatteryStatus"), ("UPS-MIB", "upsSecondsOnBattery"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    upsSubsetBatteryGroup = upsSubsetBatteryGroup.setStatus('current')
upsSubsetInputGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 33, 3, 2, 1, 3)).setObjects(("UPS-MIB", "upsInputLineBads"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    upsSubsetInputGroup = upsSubsetInputGroup.setStatus('current')
upsSubsetOutputGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 33, 3, 2, 1, 4)).setObjects(("UPS-MIB", "upsOutputSource"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    upsSubsetOutputGroup = upsSubsetOutputGroup.setStatus('current')
upsSubsetAlarmGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 33, 3, 2, 1, 6)).setObjects(("UPS-MIB", "upsAlarmsPresent"), ("UPS-MIB", "upsAlarmDescr"), ("UPS-MIB", "upsAlarmTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    upsSubsetAlarmGroup = upsSubsetAlarmGroup.setStatus('current')
upsSubsetControlGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 33, 3, 2, 1, 8)).setObjects(("UPS-MIB", "upsShutdownType"), ("UPS-MIB", "upsShutdownAfterDelay"), ("UPS-MIB", "upsAutoRestart"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    upsSubsetControlGroup = upsSubsetControlGroup.setStatus('current')
upsSubsetConfigGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 33, 3, 2, 1, 9)).setObjects(("UPS-MIB", "upsConfigInputVoltage"), ("UPS-MIB", "upsConfigInputFreq"), ("UPS-MIB", "upsConfigOutputVoltage"), ("UPS-MIB", "upsConfigOutputFreq"), ("UPS-MIB", "upsConfigOutputVA"), ("UPS-MIB", "upsConfigOutputPower"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    upsSubsetConfigGroup = upsSubsetConfigGroup.setStatus('current')
upsBasicGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 33, 3, 2, 2))
upsBasicIdentGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 33, 3, 2, 2, 1)).setObjects(("UPS-MIB", "upsIdentManufacturer"), ("UPS-MIB", "upsIdentModel"), ("UPS-MIB", "upsIdentUPSSoftwareVersion"), ("UPS-MIB", "upsIdentAgentSoftwareVersion"), ("UPS-MIB", "upsIdentName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    upsBasicIdentGroup = upsBasicIdentGroup.setStatus('current')
upsBasicBatteryGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 33, 3, 2, 2, 2)).setObjects(("UPS-MIB", "upsBatteryStatus"), ("UPS-MIB", "upsSecondsOnBattery"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    upsBasicBatteryGroup = upsBasicBatteryGroup.setStatus('current')
upsBasicInputGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 33, 3, 2, 2, 3)).setObjects(("UPS-MIB", "upsInputLineBads"), ("UPS-MIB", "upsInputNumLines"), ("UPS-MIB", "upsInputFrequency"), ("UPS-MIB", "upsInputVoltage"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    upsBasicInputGroup = upsBasicInputGroup.setStatus('current')
upsBasicOutputGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 33, 3, 2, 2, 4)).setObjects(("UPS-MIB", "upsOutputSource"), ("UPS-MIB", "upsOutputFrequency"), ("UPS-MIB", "upsOutputNumLines"), ("UPS-MIB", "upsOutputVoltage"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    upsBasicOutputGroup = upsBasicOutputGroup.setStatus('current')
upsBasicBypassGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 33, 3, 2, 2, 5)).setObjects(("UPS-MIB", "upsBypassFrequency"), ("UPS-MIB", "upsBypassNumLines"), ("UPS-MIB", "upsBypassVoltage"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    upsBasicBypassGroup = upsBasicBypassGroup.setStatus('current')
upsBasicAlarmGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 33, 3, 2, 2, 6)).setObjects(("UPS-MIB", "upsAlarmsPresent"), ("UPS-MIB", "upsAlarmDescr"), ("UPS-MIB", "upsAlarmTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    upsBasicAlarmGroup = upsBasicAlarmGroup.setStatus('current')
upsBasicTestGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 33, 3, 2, 2, 7)).setObjects(("UPS-MIB", "upsTestId"), ("UPS-MIB", "upsTestSpinLock"), ("UPS-MIB", "upsTestResultsSummary"), ("UPS-MIB", "upsTestResultsDetail"), ("UPS-MIB", "upsTestStartTime"), ("UPS-MIB", "upsTestElapsedTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    upsBasicTestGroup = upsBasicTestGroup.setStatus('current')
upsBasicControlGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 33, 3, 2, 2, 8)).setObjects(("UPS-MIB", "upsShutdownType"), ("UPS-MIB", "upsShutdownAfterDelay"), ("UPS-MIB", "upsStartupAfterDelay"), ("UPS-MIB", "upsRebootWithDuration"), ("UPS-MIB", "upsAutoRestart"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    upsBasicControlGroup = upsBasicControlGroup.setStatus('current')
upsBasicConfigGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 33, 3, 2, 2, 9)).setObjects(("UPS-MIB", "upsConfigInputVoltage"), ("UPS-MIB", "upsConfigInputFreq"), ("UPS-MIB", "upsConfigOutputVoltage"), ("UPS-MIB", "upsConfigOutputFreq"), ("UPS-MIB", "upsConfigOutputVA"), ("UPS-MIB", "upsConfigOutputPower"), ("UPS-MIB", "upsConfigLowBattTime"), ("UPS-MIB", "upsConfigAudibleStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    upsBasicConfigGroup = upsBasicConfigGroup.setStatus('current')
upsFullGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 33, 3, 2, 3))
upsFullIdentGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 33, 3, 2, 3, 1)).setObjects(("UPS-MIB", "upsIdentManufacturer"), ("UPS-MIB", "upsIdentModel"), ("UPS-MIB", "upsIdentUPSSoftwareVersion"), ("UPS-MIB", "upsIdentAgentSoftwareVersion"), ("UPS-MIB", "upsIdentName"), ("UPS-MIB", "upsIdentAttachedDevices"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    upsFullIdentGroup = upsFullIdentGroup.setStatus('current')
upsFullBatteryGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 33, 3, 2, 3, 2)).setObjects(("UPS-MIB", "upsBatteryStatus"), ("UPS-MIB", "upsSecondsOnBattery"), ("UPS-MIB", "upsEstimatedMinutesRemaining"), ("UPS-MIB", "upsEstimatedChargeRemaining"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    upsFullBatteryGroup = upsFullBatteryGroup.setStatus('current')
upsFullInputGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 33, 3, 2, 3, 3)).setObjects(("UPS-MIB", "upsInputLineBads"), ("UPS-MIB", "upsInputNumLines"), ("UPS-MIB", "upsInputFrequency"), ("UPS-MIB", "upsInputVoltage"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    upsFullInputGroup = upsFullInputGroup.setStatus('current')
upsFullOutputGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 33, 3, 2, 3, 4)).setObjects(("UPS-MIB", "upsOutputSource"), ("UPS-MIB", "upsOutputFrequency"), ("UPS-MIB", "upsOutputNumLines"), ("UPS-MIB", "upsOutputVoltage"), ("UPS-MIB", "upsOutputCurrent"), ("UPS-MIB", "upsOutputPower"), ("UPS-MIB", "upsOutputPercentLoad"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    upsFullOutputGroup = upsFullOutputGroup.setStatus('current')
upsFullBypassGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 33, 3, 2, 3, 5)).setObjects(("UPS-MIB", "upsBypassFrequency"), ("UPS-MIB", "upsBypassNumLines"), ("UPS-MIB", "upsBypassVoltage"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    upsFullBypassGroup = upsFullBypassGroup.setStatus('current')
upsFullAlarmGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 33, 3, 2, 3, 6)).setObjects(("UPS-MIB", "upsAlarmsPresent"), ("UPS-MIB", "upsAlarmDescr"), ("UPS-MIB", "upsAlarmTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    upsFullAlarmGroup = upsFullAlarmGroup.setStatus('current')
upsFullTestGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 33, 3, 2, 3, 7)).setObjects(("UPS-MIB", "upsTestId"), ("UPS-MIB", "upsTestSpinLock"), ("UPS-MIB", "upsTestResultsSummary"), ("UPS-MIB", "upsTestResultsDetail"), ("UPS-MIB", "upsTestStartTime"), ("UPS-MIB", "upsTestElapsedTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    upsFullTestGroup = upsFullTestGroup.setStatus('current')
upsFullControlGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 33, 3, 2, 3, 8)).setObjects(("UPS-MIB", "upsShutdownType"), ("UPS-MIB", "upsShutdownAfterDelay"), ("UPS-MIB", "upsStartupAfterDelay"), ("UPS-MIB", "upsRebootWithDuration"), ("UPS-MIB", "upsAutoRestart"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    upsFullControlGroup = upsFullControlGroup.setStatus('current')
upsFullConfigGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 33, 3, 2, 3, 9)).setObjects(("UPS-MIB", "upsConfigInputVoltage"), ("UPS-MIB", "upsConfigInputFreq"), ("UPS-MIB", "upsConfigOutputVoltage"), ("UPS-MIB", "upsConfigOutputFreq"), ("UPS-MIB", "upsConfigOutputVA"), ("UPS-MIB", "upsConfigOutputPower"), ("UPS-MIB", "upsConfigLowBattTime"), ("UPS-MIB", "upsConfigAudibleStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    upsFullConfigGroup = upsFullConfigGroup.setStatus('current')
mibBuilder.exportSymbols("UPS-MIB", upsBatteryTemperature=upsBatteryTemperature, upsConformance=upsConformance, upsInputCurrent=upsInputCurrent, upsFullCompliance=upsFullCompliance, upsInputLineIndex=upsInputLineIndex, upsTestSpinLock=upsTestSpinLock, upsSubsetConfigGroup=upsSubsetConfigGroup, upsAlarmOutputOverload=upsAlarmOutputOverload, upsAlarmShutdownImminent=upsAlarmShutdownImminent, upsIdentManufacturer=upsIdentManufacturer, upsConfigOutputVA=upsConfigOutputVA, upsAlarmCommunicationsLost=upsAlarmCommunicationsLost, upsAlarmDepletedBattery=upsAlarmDepletedBattery, upsObjects=upsObjects, upsFullBatteryGroup=upsFullBatteryGroup, upsAlarmChargerFailed=upsAlarmChargerFailed, upsOutputFrequency=upsOutputFrequency, upsWellKnownTests=upsWellKnownTests, upsFullBypassGroup=upsFullBypassGroup, upsWellKnownAlarms=upsWellKnownAlarms, upsFullGroups=upsFullGroups, upsAlarmDescr=upsAlarmDescr, upsTrapAlarmEntryAdded=upsTrapAlarmEntryAdded, upsAutoRestart=upsAutoRestart, upsAlarmAwaitingPower=upsAlarmAwaitingPower, upsBypassNumLines=upsBypassNumLines, upsConfigLowVoltageTransferPoint=upsConfigLowVoltageTransferPoint, upsAlarmUpsOffAsRequested=upsAlarmUpsOffAsRequested, upsTestId=upsTestId, upsAlarmTestInProgress=upsAlarmTestInProgress, upsSubsetInputGroup=upsSubsetInputGroup, upsBatteryVoltage=upsBatteryVoltage, upsSubsetOutputGroup=upsSubsetOutputGroup, upsInputFrequency=upsInputFrequency, upsTestNoTestsInitiated=upsTestNoTestsInitiated, upsConfigOutputFreq=upsConfigOutputFreq, upsInputVoltage=upsInputVoltage, upsSubsetCompliance=upsSubsetCompliance, upsAlarmId=upsAlarmId, upsAlarmOnBypass=upsAlarmOnBypass, upsBypassFrequency=upsBypassFrequency, upsAlarmFuseFailure=upsAlarmFuseFailure, upsAlarm=upsAlarm, upsSecondsOnBattery=upsSecondsOnBattery, upsTestResultsDetail=upsTestResultsDetail, upsEstimatedMinutesRemaining=upsEstimatedMinutesRemaining, upsIdentModel=upsIdentModel, upsInputNumLines=upsInputNumLines, upsOutputPercentLoad=upsOutputPercentLoad, upsAlarmFanFailure=upsAlarmFanFailure, upsCompliances=upsCompliances, PYSNMP_MODULE_ID=upsMIB, upsStartupAfterDelay=upsStartupAfterDelay, upsAlarmGeneralFault=upsAlarmGeneralFault, upsOutputCurrent=upsOutputCurrent, upsAlarmEntry=upsAlarmEntry, upsOutputNumLines=upsOutputNumLines, upsOutputSource=upsOutputSource, upsShutdownType=upsShutdownType, upsTrapOnBattery=upsTrapOnBattery, upsBattery=upsBattery, upsFullInputGroup=upsFullInputGroup, upsConfigHighVoltageTransferPoint=upsConfigHighVoltageTransferPoint, upsSubsetControlGroup=upsSubsetControlGroup, upsBasicInputGroup=upsBasicInputGroup, PositiveInteger=PositiveInteger, upsAlarmBypassBad=upsAlarmBypassBad, upsBasicBypassGroup=upsBasicBypassGroup, upsInputLineBads=upsInputLineBads, upsBatteryCurrent=upsBatteryCurrent, upsTestResultsSummary=upsTestResultsSummary, upsSubsetIdentGroup=upsSubsetIdentGroup, upsAlarmLowBattery=upsAlarmLowBattery, upsBasicOutputGroup=upsBasicOutputGroup, upsTestDeepBatteryCalibration=upsTestDeepBatteryCalibration, upsBasicTestGroup=upsBasicTestGroup, upsAlarmInputBad=upsAlarmInputBad, upsSubsetAlarmGroup=upsSubsetAlarmGroup, upsTrapTestCompleted=upsTrapTestCompleted, upsIdentUPSSoftwareVersion=upsIdentUPSSoftwareVersion, upsRebootWithDuration=upsRebootWithDuration, upsAlarmOutputBad=upsAlarmOutputBad, upsOutput=upsOutput, upsIdentName=upsIdentName, upsIdent=upsIdent, upsInputTruePower=upsInputTruePower, upsControl=upsControl, upsBypassVoltage=upsBypassVoltage, upsAlarmTempBad=upsAlarmTempBad, upsAlarmOutputOffAsRequested=upsAlarmOutputOffAsRequested, upsBypassCurrent=upsBypassCurrent, upsIdentAgentSoftwareVersion=upsIdentAgentSoftwareVersion, upsBasicAlarmGroup=upsBasicAlarmGroup, upsOutputEntry=upsOutputEntry, upsBypass=upsBypass, upsAlarmShutdownPending=upsAlarmShutdownPending, upsAlarmUpsSystemOff=upsAlarmUpsSystemOff, upsTraps=upsTraps, upsSubsetBatteryGroup=upsSubsetBatteryGroup, upsShutdownAfterDelay=upsShutdownAfterDelay, upsBypassLineIndex=upsBypassLineIndex, upsInputTable=upsInputTable, upsBasicGroups=upsBasicGroups, upsFullIdentGroup=upsFullIdentGroup, upsFullControlGroup=upsFullControlGroup, upsBasicBatteryGroup=upsBasicBatteryGroup, upsAlarmBatteryBad=upsAlarmBatteryBad, upsAlarmTable=upsAlarmTable, upsIdentAttachedDevices=upsIdentAttachedDevices, upsOutputPower=upsOutputPower, upsOutputLineIndex=upsOutputLineIndex, upsTestQuickBatteryTest=upsTestQuickBatteryTest, upsBatteryStatus=upsBatteryStatus, upsTestGeneralSystemsTest=upsTestGeneralSystemsTest, upsSubsetGroups=upsSubsetGroups, upsBasicIdentGroup=upsBasicIdentGroup, upsConfigLowBattTime=upsConfigLowBattTime, upsFullOutputGroup=upsFullOutputGroup, upsFullTestGroup=upsFullTestGroup, upsTest=upsTest, upsTestStartTime=upsTestStartTime, upsMIB=upsMIB, upsFullAlarmGroup=upsFullAlarmGroup, upsAlarmUpsOutputOff=upsAlarmUpsOutputOff, upsAlarmDiagnosticTestFailed=upsAlarmDiagnosticTestFailed, upsEstimatedChargeRemaining=upsEstimatedChargeRemaining, upsBypassEntry=upsBypassEntry, upsBasicCompliance=upsBasicCompliance, upsOutputVoltage=upsOutputVoltage, upsOutputTable=upsOutputTable, upsConfigOutputVoltage=upsConfigOutputVoltage, upsConfigInputVoltage=upsConfigInputVoltage, upsBypassPower=upsBypassPower, upsTestAbortTestInProgress=upsTestAbortTestInProgress, upsConfigAudibleStatus=upsConfigAudibleStatus, upsInput=upsInput, upsBasicControlGroup=upsBasicControlGroup, upsGroups=upsGroups, upsFullConfigGroup=upsFullConfigGroup, upsConfigOutputPower=upsConfigOutputPower, upsTestElapsedTime=upsTestElapsedTime, upsAlarmsPresent=upsAlarmsPresent, NonNegativeInteger=NonNegativeInteger, upsTrapAlarmEntryRemoved=upsTrapAlarmEntryRemoved, upsConfigInputFreq=upsConfigInputFreq, upsBypassTable=upsBypassTable, upsBasicConfigGroup=upsBasicConfigGroup, upsAlarmOnBattery=upsAlarmOnBattery, upsConfig=upsConfig, upsInputEntry=upsInputEntry, upsAlarmTime=upsAlarmTime)
