#
# PySNMP MIB module EATON-ATS2-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/eaton/EATON-ATS2-MIB
# Produced by pysmi-1.1.8 at Sun Jan 16 00:35:53 2022
# On host fv-az42-839 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
sts, = mibBuilder.importSymbols("EATON-OIDS", "sts")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, MibIdentifier, Integer32, TimeTicks, Unsigned32, NotificationType, Bits, Counter64, IpAddress, Counter32, iso, ModuleIdentity, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "MibIdentifier", "Integer32", "TimeTicks", "Unsigned32", "NotificationType", "Bits", "Counter64", "IpAddress", "Counter32", "iso", "ModuleIdentity", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ats2 = ModuleIdentity((1, 3, 6, 1, 4, 1, 534, 10, 2))
ats2.setRevisions(('2014-07-31 12:00',))
if mibBuilder.loadTexts: ats2.setLastUpdated('201407311200Z')
if mibBuilder.loadTexts: ats2.setOrganization('Eaton Corporation')
ats2Ident = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 10, 2, 1))
ats2Measure = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 10, 2, 2))
ats2Status = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 10, 2, 3))
ats2Config = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 10, 2, 4))
ats2Environment = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 10, 2, 5))
ats2Traps = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 10, 2, 10))
class UnixTimeStamp(TextualConvention, Counter32):
    status = 'current'
    displayHint = 'dddddddddd'

ats2IdentManufacturer = MibScalar((1, 3, 6, 1, 4, 1, 534, 10, 2, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ats2IdentManufacturer.setStatus('current')
ats2IdentModel = MibScalar((1, 3, 6, 1, 4, 1, 534, 10, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ats2IdentModel.setStatus('current')
ats2IdentFWVersion = MibScalar((1, 3, 6, 1, 4, 1, 534, 10, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ats2IdentFWVersion.setStatus('current')
ats2IdentRelease = MibScalar((1, 3, 6, 1, 4, 1, 534, 10, 2, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ats2IdentRelease.setStatus('current')
ats2IdentSerialNumber = MibScalar((1, 3, 6, 1, 4, 1, 534, 10, 2, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ats2IdentSerialNumber.setStatus('current')
ats2IdentPartNumber = MibScalar((1, 3, 6, 1, 4, 1, 534, 10, 2, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ats2IdentPartNumber.setStatus('current')
ats2IdentAgentVersion = MibScalar((1, 3, 6, 1, 4, 1, 534, 10, 2, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ats2IdentAgentVersion.setStatus('current')
ats2Input = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 10, 2, 2, 1))
ats2InputDephasing = MibScalar((1, 3, 6, 1, 4, 1, 534, 10, 2, 2, 1, 1), Integer32()).setUnits('degrees').setMaxAccess("readonly")
if mibBuilder.loadTexts: ats2InputDephasing.setStatus('current')
ats2InputTable = MibTable((1, 3, 6, 1, 4, 1, 534, 10, 2, 2, 2), )
if mibBuilder.loadTexts: ats2InputTable.setStatus('current')
ats2Output = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 10, 2, 2, 3))
ats2OperationMode = MibScalar((1, 3, 6, 1, 4, 1, 534, 10, 2, 2, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("initialization", 1), ("diagnosis", 2), ("off", 3), ("source1", 4), ("source2", 5), ("safe", 6), ("fault", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ats2OperationMode.setStatus('current')
ats2InputEntry = MibTableRow((1, 3, 6, 1, 4, 1, 534, 10, 2, 2, 2, 1), ).setIndexNames((0, "EATON-ATS2-MIB", "ats2InputIndex"))
if mibBuilder.loadTexts: ats2InputEntry.setStatus('current')
ats2InputIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 10, 2, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("source1", 1), ("source2", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ats2InputIndex.setStatus('current')
ats2InputVoltage = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 10, 2, 2, 2, 1, 2), Integer32()).setUnits('0.1 V').setMaxAccess("readonly")
if mibBuilder.loadTexts: ats2InputVoltage.setStatus('current')
ats2InputFrequency = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 10, 2, 2, 2, 1, 3), Integer32()).setUnits('0.1 Hz').setMaxAccess("readonly")
if mibBuilder.loadTexts: ats2InputFrequency.setStatus('current')
ats2OutputVoltage = MibScalar((1, 3, 6, 1, 4, 1, 534, 10, 2, 2, 3, 1), Integer32()).setUnits('0.1 V').setMaxAccess("readonly")
if mibBuilder.loadTexts: ats2OutputVoltage.setStatus('current')
ats2OutputCurrent = MibScalar((1, 3, 6, 1, 4, 1, 534, 10, 2, 2, 3, 2), Integer32()).setUnits('0.1 A').setMaxAccess("readonly")
if mibBuilder.loadTexts: ats2OutputCurrent.setStatus('current')
ats2InputStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 10, 2, 3, 1))
ats2InputStatusDephasing = MibScalar((1, 3, 6, 1, 4, 1, 534, 10, 2, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("normal", 1), ("outOfRange", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ats2InputStatusDephasing.setStatus('current')
ats2InputStatusTable = MibTable((1, 3, 6, 1, 4, 1, 534, 10, 2, 3, 2), )
if mibBuilder.loadTexts: ats2InputStatusTable.setStatus('current')
ats2OutputStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 10, 2, 3, 3))
ats2InputStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 534, 10, 2, 3, 2, 1), ).setIndexNames((0, "EATON-ATS2-MIB", "ats2InputStatusIndex"))
if mibBuilder.loadTexts: ats2InputStatusEntry.setStatus('current')
ats2InputStatusIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 10, 2, 3, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("source1", 1), ("source2", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ats2InputStatusIndex.setStatus('current')
ats2InputStatusFrequency = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 10, 2, 3, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("good", 1), ("outOfRange", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ats2InputStatusFrequency.setStatus('current')
ats2InputStatusGood = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 10, 2, 3, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("voltageOrFreqOutofRange", 1), ("voltageAndFreqNormalRange", 2), ("voltageDeratedRangeAndFreqNormalRange", 3), ("voltageAndFreqNormalRangeWaveformNok", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ats2InputStatusGood.setStatus('current')
ats2InputStatusInternalFailure = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 10, 2, 3, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("good", 1), ("internalFailure", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ats2InputStatusInternalFailure.setStatus('current')
ats2InputStatusVoltage = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 10, 2, 3, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("normalRange", 1), ("deratedRange", 2), ("outofRange", 3), ("missing", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ats2InputStatusVoltage.setStatus('current')
ats2InputStatusUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 10, 2, 3, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("notPoweringLoad", 1), ("poweringLoad", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ats2InputStatusUsed.setStatus('current')
ats2StatusInternalFailure = MibScalar((1, 3, 6, 1, 4, 1, 534, 10, 2, 3, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("good", 1), ("internalFailure", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ats2StatusInternalFailure.setStatus('current')
ats2StatusOutput = MibScalar((1, 3, 6, 1, 4, 1, 534, 10, 2, 3, 3, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("outputNotPowered", 1), ("outputPowered", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ats2StatusOutput.setStatus('current')
ats2StatusOverload = MibScalar((1, 3, 6, 1, 4, 1, 534, 10, 2, 3, 3, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noOverload", 1), ("warningOverload", 2), ("criticalOverload", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ats2StatusOverload.setStatus('current')
ats2StatusOverTemperature = MibScalar((1, 3, 6, 1, 4, 1, 534, 10, 2, 3, 3, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noOverTemperature", 1), ("overTemperature", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ats2StatusOverTemperature.setStatus('current')
ats2StatusShortCircuit = MibScalar((1, 3, 6, 1, 4, 1, 534, 10, 2, 3, 3, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noShortCircuit", 1), ("shortCircuit", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ats2StatusShortCircuit.setStatus('current')
ats2StatusCommunicationLost = MibScalar((1, 3, 6, 1, 4, 1, 534, 10, 2, 3, 3, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("good", 1), ("communicationLost", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ats2StatusCommunicationLost.setStatus('current')
ats2StatusConfigurationFailure = MibScalar((1, 3, 6, 1, 4, 1, 534, 10, 2, 3, 3, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("good", 1), ("configurationFailure", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ats2StatusConfigurationFailure.setStatus('current')
ats2ConfigTime = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 10, 2, 4, 1))
ats2ConfigInputVoltageRating = MibScalar((1, 3, 6, 1, 4, 1, 534, 10, 2, 4, 2), Integer32()).setUnits('1 V').setMaxAccess("readonly")
if mibBuilder.loadTexts: ats2ConfigInputVoltageRating.setStatus('current')
ats2ConfigInputFrequencyRating = MibScalar((1, 3, 6, 1, 4, 1, 534, 10, 2, 4, 3), Integer32()).setUnits('Hz').setMaxAccess("readonly")
if mibBuilder.loadTexts: ats2ConfigInputFrequencyRating.setStatus('current')
ats2ConfigOutputVoltage = MibScalar((1, 3, 6, 1, 4, 1, 534, 10, 2, 4, 4), Integer32()).setUnits('1 V').setMaxAccess("readwrite")
if mibBuilder.loadTexts: ats2ConfigOutputVoltage.setStatus('current')
ats2ConfigPreferred = MibScalar((1, 3, 6, 1, 4, 1, 534, 10, 2, 4, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("source1", 1), ("source2", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ats2ConfigPreferred.setStatus('current')
ats2ConfigSensitivity = MibScalar((1, 3, 6, 1, 4, 1, 534, 10, 2, 4, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("normal", 1), ("highSensitivity", 2), ("lowSensitivity", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ats2ConfigSensitivity.setStatus('current')
ats2ConfigTransferMode = MibScalar((1, 3, 6, 1, 4, 1, 534, 10, 2, 4, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("standard", 1), ("gap", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ats2ConfigTransferMode.setStatus('current')
ats2ConfigTransferTest = MibScalar((1, 3, 6, 1, 4, 1, 534, 10, 2, 4, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("doneAndPassed", 1), ("doneAndWarning", 2), ("doneAndError", 3), ("aborted", 4), ("inProgress", 5), ("noTestInitiated", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ats2ConfigTransferTest.setStatus('current')
ats2ConfigBrownoutLow = MibScalar((1, 3, 6, 1, 4, 1, 534, 10, 2, 4, 9), Integer32()).setUnits('1 V').setMaxAccess("readonly")
if mibBuilder.loadTexts: ats2ConfigBrownoutLow.setStatus('current')
ats2ConfigBrownoutLowDerated = MibScalar((1, 3, 6, 1, 4, 1, 534, 10, 2, 4, 10), Integer32()).setUnits('1 V').setMaxAccess("readonly")
if mibBuilder.loadTexts: ats2ConfigBrownoutLowDerated.setStatus('current')
ats2ConfigBrownoutHigh = MibScalar((1, 3, 6, 1, 4, 1, 534, 10, 2, 4, 11), Integer32()).setUnits('1 V').setMaxAccess("readonly")
if mibBuilder.loadTexts: ats2ConfigBrownoutHigh.setStatus('current')
ats2ConfigHysteresisVoltage = MibScalar((1, 3, 6, 1, 4, 1, 534, 10, 2, 4, 12), Integer32()).setUnits('1 V').setMaxAccess("readonly")
if mibBuilder.loadTexts: ats2ConfigHysteresisVoltage.setStatus('current')
ats2ConfigTimeRTC = MibScalar((1, 3, 6, 1, 4, 1, 534, 10, 2, 4, 1, 1), UnixTimeStamp()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ats2ConfigTimeRTC.setStatus('current')
ats2ConfigTimeTextDate = MibScalar((1, 3, 6, 1, 4, 1, 534, 10, 2, 4, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 10))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ats2ConfigTimeTextDate.setStatus('current')
ats2ConfigTimeTextTime = MibScalar((1, 3, 6, 1, 4, 1, 534, 10, 2, 4, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ats2ConfigTimeTextTime.setStatus('current')
ats2EnvRemoteTemp = MibScalar((1, 3, 6, 1, 4, 1, 534, 10, 2, 5, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-100, 200))).setUnits('degrees Centigrade').setMaxAccess("readonly")
if mibBuilder.loadTexts: ats2EnvRemoteTemp.setStatus('current')
ats2EnvRemoteHumidity = MibScalar((1, 3, 6, 1, 4, 1, 534, 10, 2, 5, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setUnits('percent').setMaxAccess("readonly")
if mibBuilder.loadTexts: ats2EnvRemoteHumidity.setStatus('current')
ats2EnvNumContacts = MibScalar((1, 3, 6, 1, 4, 1, 534, 10, 2, 5, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ats2EnvNumContacts.setStatus('current')
ats2ContactSenseTable = MibTable((1, 3, 6, 1, 4, 1, 534, 10, 2, 5, 4), )
if mibBuilder.loadTexts: ats2ContactSenseTable.setStatus('current')
ats2ContactsTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 534, 10, 2, 5, 4, 1), ).setIndexNames((0, "EATON-ATS2-MIB", "ats2ContactIndex"))
if mibBuilder.loadTexts: ats2ContactsTableEntry.setStatus('current')
ats2ContactIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 10, 2, 5, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ats2ContactIndex.setStatus('current')
ats2ContactType = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 10, 2, 5, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("normallyOpen", 1), ("normallyClosed", 2), ("anyChange", 3), ("notUsed", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ats2ContactType.setStatus('current')
ats2ContactState = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 10, 2, 5, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("open", 1), ("closed", 2), ("openWithNotice", 3), ("closedWithNotice", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ats2ContactState.setStatus('current')
ats2ContactDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 534, 10, 2, 5, 4, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ats2ContactDescr.setStatus('current')
ats2EnvRemoteTempLowerLimit = MibScalar((1, 3, 6, 1, 4, 1, 534, 10, 2, 5, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-100, 200))).setUnits('degrees Centigrade').setMaxAccess("readwrite")
if mibBuilder.loadTexts: ats2EnvRemoteTempLowerLimit.setStatus('current')
ats2EnvRemoteTempUpperLimit = MibScalar((1, 3, 6, 1, 4, 1, 534, 10, 2, 5, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-100, 200))).setUnits('degrees Centigrade').setMaxAccess("readwrite")
if mibBuilder.loadTexts: ats2EnvRemoteTempUpperLimit.setStatus('current')
ats2EnvRemoteHumidityLowerLimit = MibScalar((1, 3, 6, 1, 4, 1, 534, 10, 2, 5, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setUnits('percent').setMaxAccess("readwrite")
if mibBuilder.loadTexts: ats2EnvRemoteHumidityLowerLimit.setStatus('current')
ats2EnvRemoteHumidityUpperLimit = MibScalar((1, 3, 6, 1, 4, 1, 534, 10, 2, 5, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setUnits('percent').setMaxAccess("readwrite")
if mibBuilder.loadTexts: ats2EnvRemoteHumidityUpperLimit.setStatus('current')
ats2TrapCommunicationLost = NotificationType((1, 3, 6, 1, 4, 1, 534, 10, 2, 10, 1))
if mibBuilder.loadTexts: ats2TrapCommunicationLost.setStatus('current')
ats2TrapCommunicationRecovered = NotificationType((1, 3, 6, 1, 4, 1, 534, 10, 2, 10, 2))
if mibBuilder.loadTexts: ats2TrapCommunicationRecovered.setStatus('current')
ats2TrapOutputPowered = NotificationType((1, 3, 6, 1, 4, 1, 534, 10, 2, 10, 3))
if mibBuilder.loadTexts: ats2TrapOutputPowered.setStatus('current')
ats2TrapOutputNotPowered = NotificationType((1, 3, 6, 1, 4, 1, 534, 10, 2, 10, 4))
if mibBuilder.loadTexts: ats2TrapOutputNotPowered.setStatus('current')
ats2TrapOverload = NotificationType((1, 3, 6, 1, 4, 1, 534, 10, 2, 10, 5))
if mibBuilder.loadTexts: ats2TrapOverload.setStatus('current')
ats2TrapNoOverLoad = NotificationType((1, 3, 6, 1, 4, 1, 534, 10, 2, 10, 6))
if mibBuilder.loadTexts: ats2TrapNoOverLoad.setStatus('current')
ats2TrapInternalFailure = NotificationType((1, 3, 6, 1, 4, 1, 534, 10, 2, 10, 7))
if mibBuilder.loadTexts: ats2TrapInternalFailure.setStatus('current')
ats2TrapNoInternalFailure = NotificationType((1, 3, 6, 1, 4, 1, 534, 10, 2, 10, 8))
if mibBuilder.loadTexts: ats2TrapNoInternalFailure.setStatus('current')
ats2TrapSource1Normal = NotificationType((1, 3, 6, 1, 4, 1, 534, 10, 2, 10, 9))
if mibBuilder.loadTexts: ats2TrapSource1Normal.setStatus('current')
ats2TrapSource1OutOfRange = NotificationType((1, 3, 6, 1, 4, 1, 534, 10, 2, 10, 10))
if mibBuilder.loadTexts: ats2TrapSource1OutOfRange.setStatus('current')
ats2TrapSource2Normal = NotificationType((1, 3, 6, 1, 4, 1, 534, 10, 2, 10, 11))
if mibBuilder.loadTexts: ats2TrapSource2Normal.setStatus('current')
ats2TrapSource2OutOfRange = NotificationType((1, 3, 6, 1, 4, 1, 534, 10, 2, 10, 12))
if mibBuilder.loadTexts: ats2TrapSource2OutOfRange.setStatus('current')
ats2TrapSourceDesynchronized = NotificationType((1, 3, 6, 1, 4, 1, 534, 10, 2, 10, 13))
if mibBuilder.loadTexts: ats2TrapSourceDesynchronized.setStatus('current')
ats2TrapSourceSynchronized = NotificationType((1, 3, 6, 1, 4, 1, 534, 10, 2, 10, 14))
if mibBuilder.loadTexts: ats2TrapSourceSynchronized.setStatus('current')
ats2TrapOutputPoweredBySource1 = NotificationType((1, 3, 6, 1, 4, 1, 534, 10, 2, 10, 15))
if mibBuilder.loadTexts: ats2TrapOutputPoweredBySource1.setStatus('current')
ats2TrapOutputPoweredBySource2 = NotificationType((1, 3, 6, 1, 4, 1, 534, 10, 2, 10, 16))
if mibBuilder.loadTexts: ats2TrapOutputPoweredBySource2.setStatus('current')
ats2TrapRemoteTempLow = NotificationType((1, 3, 6, 1, 4, 1, 534, 10, 2, 10, 20))
if mibBuilder.loadTexts: ats2TrapRemoteTempLow.setStatus('current')
ats2TrapRemoteTempHigh = NotificationType((1, 3, 6, 1, 4, 1, 534, 10, 2, 10, 21))
if mibBuilder.loadTexts: ats2TrapRemoteTempHigh.setStatus('current')
ats2TrapRemoteTempNormal = NotificationType((1, 3, 6, 1, 4, 1, 534, 10, 2, 10, 22))
if mibBuilder.loadTexts: ats2TrapRemoteTempNormal.setStatus('current')
ats2TrapRemoteHumidityLow = NotificationType((1, 3, 6, 1, 4, 1, 534, 10, 2, 10, 23))
if mibBuilder.loadTexts: ats2TrapRemoteHumidityLow.setStatus('current')
ats2TrapRemoteHumidityHigh = NotificationType((1, 3, 6, 1, 4, 1, 534, 10, 2, 10, 24))
if mibBuilder.loadTexts: ats2TrapRemoteHumidityHigh.setStatus('current')
ats2TrapRemoteHumidityNormal = NotificationType((1, 3, 6, 1, 4, 1, 534, 10, 2, 10, 25))
if mibBuilder.loadTexts: ats2TrapRemoteHumidityNormal.setStatus('current')
ats2Contact1ActiveNotice = NotificationType((1, 3, 6, 1, 4, 1, 534, 10, 2, 10, 26))
if mibBuilder.loadTexts: ats2Contact1ActiveNotice.setStatus('current')
ats2Contact1InactiveNotice = NotificationType((1, 3, 6, 1, 4, 1, 534, 10, 2, 10, 27))
if mibBuilder.loadTexts: ats2Contact1InactiveNotice.setStatus('current')
ats2Contact2ActiveNotice = NotificationType((1, 3, 6, 1, 4, 1, 534, 10, 2, 10, 28))
if mibBuilder.loadTexts: ats2Contact2ActiveNotice.setStatus('current')
ats2Contact2InactiveNotice = NotificationType((1, 3, 6, 1, 4, 1, 534, 10, 2, 10, 29))
if mibBuilder.loadTexts: ats2Contact2InactiveNotice.setStatus('current')
ats2TestTrap = NotificationType((1, 3, 6, 1, 4, 1, 534, 10, 2, 10, 40))
if mibBuilder.loadTexts: ats2TestTrap.setStatus('current')
mibBuilder.exportSymbols("EATON-ATS2-MIB", ats2ConfigPreferred=ats2ConfigPreferred, ats2Contact2ActiveNotice=ats2Contact2ActiveNotice, ats2OutputVoltage=ats2OutputVoltage, ats2TrapOutputPowered=ats2TrapOutputPowered, ats2TrapRemoteHumidityNormal=ats2TrapRemoteHumidityNormal, ats2InputVoltage=ats2InputVoltage, ats2ConfigOutputVoltage=ats2ConfigOutputVoltage, ats2TrapOutputPoweredBySource2=ats2TrapOutputPoweredBySource2, ats2=ats2, ats2StatusConfigurationFailure=ats2StatusConfigurationFailure, ats2TrapOutputNotPowered=ats2TrapOutputNotPowered, ats2InputStatusVoltage=ats2InputStatusVoltage, ats2TrapOverload=ats2TrapOverload, ats2TrapNoInternalFailure=ats2TrapNoInternalFailure, ats2TrapRemoteTempLow=ats2TrapRemoteTempLow, ats2StatusOutput=ats2StatusOutput, ats2ConfigSensitivity=ats2ConfigSensitivity, ats2IdentFWVersion=ats2IdentFWVersion, ats2InputStatusFrequency=ats2InputStatusFrequency, ats2Contact2InactiveNotice=ats2Contact2InactiveNotice, ats2ContactSenseTable=ats2ContactSenseTable, ats2TrapCommunicationRecovered=ats2TrapCommunicationRecovered, ats2ConfigTimeRTC=ats2ConfigTimeRTC, ats2ConfigBrownoutLowDerated=ats2ConfigBrownoutLowDerated, ats2StatusCommunicationLost=ats2StatusCommunicationLost, ats2ContactsTableEntry=ats2ContactsTableEntry, ats2TrapRemoteTempNormal=ats2TrapRemoteTempNormal, ats2InputDephasing=ats2InputDephasing, ats2InputStatus=ats2InputStatus, ats2InputIndex=ats2InputIndex, ats2TrapRemoteHumidityHigh=ats2TrapRemoteHumidityHigh, ats2Contact1ActiveNotice=ats2Contact1ActiveNotice, ats2IdentModel=ats2IdentModel, ats2EnvRemoteHumidity=ats2EnvRemoteHumidity, ats2TrapCommunicationLost=ats2TrapCommunicationLost, ats2Input=ats2Input, ats2ConfigTimeTextTime=ats2ConfigTimeTextTime, ats2TrapSource1Normal=ats2TrapSource1Normal, ats2EnvRemoteHumidityLowerLimit=ats2EnvRemoteHumidityLowerLimit, ats2InputEntry=ats2InputEntry, ats2Config=ats2Config, ats2IdentManufacturer=ats2IdentManufacturer, ats2OutputStatus=ats2OutputStatus, ats2EnvRemoteTemp=ats2EnvRemoteTemp, ats2TrapNoOverLoad=ats2TrapNoOverLoad, ats2TrapSourceSynchronized=ats2TrapSourceSynchronized, ats2InputStatusEntry=ats2InputStatusEntry, ats2ConfigTransferMode=ats2ConfigTransferMode, ats2ContactIndex=ats2ContactIndex, ats2ContactType=ats2ContactType, ats2StatusOverTemperature=ats2StatusOverTemperature, ats2StatusInternalFailure=ats2StatusInternalFailure, ats2Measure=ats2Measure, ats2TrapInternalFailure=ats2TrapInternalFailure, ats2TrapSourceDesynchronized=ats2TrapSourceDesynchronized, ats2ConfigInputFrequencyRating=ats2ConfigInputFrequencyRating, ats2TrapSource2Normal=ats2TrapSource2Normal, ats2TrapRemoteTempHigh=ats2TrapRemoteTempHigh, ats2IdentSerialNumber=ats2IdentSerialNumber, ats2Traps=ats2Traps, ats2InputStatusTable=ats2InputStatusTable, ats2StatusOverload=ats2StatusOverload, ats2ContactState=ats2ContactState, ats2EnvRemoteTempUpperLimit=ats2EnvRemoteTempUpperLimit, ats2OperationMode=ats2OperationMode, ats2TrapSource1OutOfRange=ats2TrapSource1OutOfRange, ats2EnvRemoteTempLowerLimit=ats2EnvRemoteTempLowerLimit, ats2ConfigTime=ats2ConfigTime, ats2IdentPartNumber=ats2IdentPartNumber, ats2ContactDescr=ats2ContactDescr, ats2InputStatusInternalFailure=ats2InputStatusInternalFailure, ats2ConfigTimeTextDate=ats2ConfigTimeTextDate, ats2ConfigBrownoutLow=ats2ConfigBrownoutLow, ats2ConfigInputVoltageRating=ats2ConfigInputVoltageRating, ats2TrapSource2OutOfRange=ats2TrapSource2OutOfRange, ats2OutputCurrent=ats2OutputCurrent, ats2IdentRelease=ats2IdentRelease, ats2IdentAgentVersion=ats2IdentAgentVersion, ats2InputStatusIndex=ats2InputStatusIndex, ats2InputTable=ats2InputTable, ats2StatusShortCircuit=ats2StatusShortCircuit, ats2ConfigHysteresisVoltage=ats2ConfigHysteresisVoltage, ats2Output=ats2Output, ats2Status=ats2Status, ats2TrapOutputPoweredBySource1=ats2TrapOutputPoweredBySource1, ats2EnvRemoteHumidityUpperLimit=ats2EnvRemoteHumidityUpperLimit, ats2ConfigBrownoutHigh=ats2ConfigBrownoutHigh, ats2Contact1InactiveNotice=ats2Contact1InactiveNotice, ats2InputStatusDephasing=ats2InputStatusDephasing, PYSNMP_MODULE_ID=ats2, ats2InputFrequency=ats2InputFrequency, ats2EnvNumContacts=ats2EnvNumContacts, ats2InputStatusUsed=ats2InputStatusUsed, ats2Environment=ats2Environment, ats2Ident=ats2Ident, UnixTimeStamp=UnixTimeStamp, ats2TestTrap=ats2TestTrap, ats2InputStatusGood=ats2InputStatusGood, ats2TrapRemoteHumidityLow=ats2TrapRemoteHumidityLow, ats2ConfigTransferTest=ats2ConfigTransferTest)
