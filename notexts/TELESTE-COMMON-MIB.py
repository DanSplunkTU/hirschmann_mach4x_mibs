#
# PySNMP MIB module TELESTE-COMMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/teleste/TELESTE-COMMON-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:39:44 2022
# On host fv-az36-988 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, Bits, MibIdentifier, Integer32, ModuleIdentity, IpAddress, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, iso, TimeTicks, NotificationType, Counter32, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Bits", "MibIdentifier", "Integer32", "ModuleIdentity", "IpAddress", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "iso", "TimeTicks", "NotificationType", "Counter32", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
DateAndTime, common, TPhysAddress, Uint16 = mibBuilder.importSymbols("TELESTE-ROOT-MIB", "DateAndTime", "common", "TPhysAddress", "Uint16")
element = MibIdentifier((1, 3, 6, 1, 4, 1, 3715, 99, 1))
elementInformation = MibIdentifier((1, 3, 6, 1, 4, 1, 3715, 99, 1, 1))
elementName = MibScalar((1, 3, 6, 1, 4, 1, 3715, 99, 1, 1, 1), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: elementName.setStatus('mandatory')
elementStructure = MibScalar((1, 3, 6, 1, 4, 1, 3715, 99, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unknown", 1), ("compact", 2), ("modular", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: elementStructure.setStatus('mandatory')
elementConfigChangeCode = MibScalar((1, 3, 6, 1, 4, 1, 3715, 99, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: elementConfigChangeCode.setStatus('optional')
elementResetCount = MibScalar((1, 3, 6, 1, 4, 1, 3715, 99, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: elementResetCount.setStatus('optional')
elementTotalUpTime = MibScalar((1, 3, 6, 1, 4, 1, 3715, 99, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: elementTotalUpTime.setStatus('mandatory')
elementLatitude = MibScalar((1, 3, 6, 1, 4, 1, 3715, 99, 1, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: elementLatitude.setStatus('optional')
elementLongitude = MibScalar((1, 3, 6, 1, 4, 1, 3715, 99, 1, 1, 7), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: elementLongitude.setStatus('optional')
elementAltitude = MibScalar((1, 3, 6, 1, 4, 1, 3715, 99, 1, 1, 8), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: elementAltitude.setStatus('optional')
elementStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 3715, 99, 1, 2))
statusGeneral = MibScalar((1, 3, 6, 1, 4, 1, 3715, 99, 1, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("normal", 1), ("notification", 2), ("warning", 3), ("alarm", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: statusGeneral.setStatus('mandatory')
statusBusMaster = MibScalar((1, 3, 6, 1, 4, 1, 3715, 99, 1, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("slaveOnly", 1), ("configuredSlave", 2), ("currentlySlave", 3), ("currentlyMaster", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: statusBusMaster.setStatus('optional')
statusLmt = MibScalar((1, 3, 6, 1, 4, 1, 3715, 99, 1, 2, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("noLmtInterface", 1), ("stateUnknown", 2), ("notConnected", 3), ("connected", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: statusLmt.setStatus('optional')
statusLid = MibScalar((1, 3, 6, 1, 4, 1, 3715, 99, 1, 2, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noLid", 1), ("closed", 2), ("open", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: statusLid.setStatus('optional')
statusTemperature = MibScalar((1, 3, 6, 1, 4, 1, 3715, 99, 1, 2, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("tempNormal", 1), ("tempHIHI", 2), ("tempHi", 3), ("tempLo", 4), ("tempLOLO", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: statusTemperature.setStatus('optional')
statusFan = MibScalar((1, 3, 6, 1, 4, 1, 3715, 99, 1, 2, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("fanNormal", 1), ("fanFailure", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: statusFan.setStatus('mandatory')
statusHardware = MibScalar((1, 3, 6, 1, 4, 1, 3715, 99, 1, 2, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("hwNormal", 1), ("hwFailure", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: statusHardware.setStatus('mandatory')
statusSoftware = MibScalar((1, 3, 6, 1, 4, 1, 3715, 99, 1, 2, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("swNormal", 1), ("swFailure", 2), ("swMissing", 3), ("swInitialising", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: statusSoftware.setStatus('mandatory')
statusSettings = MibScalar((1, 3, 6, 1, 4, 1, 3715, 99, 1, 2, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("settingsStable", 1), ("settingsChanged", 2), ("settingsNotAvailable", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: statusSettings.setStatus('mandatory')
elementControl = MibIdentifier((1, 3, 6, 1, 4, 1, 3715, 99, 1, 3))
controlResetElement = MibScalar((1, 3, 6, 1, 4, 1, 3715, 99, 1, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noReset", 1), ("hardReset", 2), ("softReset", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: controlResetElement.setStatus('mandatory')
controlBusMasterAdminState = MibScalar((1, 3, 6, 1, 4, 1, 3715, 99, 1, 3, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("master", 1), ("slave", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: controlBusMasterAdminState.setStatus('optional')
controlAlarmDetection = MibScalar((1, 3, 6, 1, 4, 1, 3715, 99, 1, 3, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2), ("restart", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: controlAlarmDetection.setStatus('mandatory')
controlMaxNumberTrapReceivers = MibScalar((1, 3, 6, 1, 4, 1, 3715, 99, 1, 3, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: controlMaxNumberTrapReceivers.setStatus('mandatory')
controlTrapReceiverTable = MibTable((1, 3, 6, 1, 4, 1, 3715, 99, 1, 3, 5), )
if mibBuilder.loadTexts: controlTrapReceiverTable.setStatus('optional')
controlTrapReceiverEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3715, 99, 1, 3, 5, 1), ).setIndexNames((0, "TELESTE-COMMON-MIB", "receiverEntryId"))
if mibBuilder.loadTexts: controlTrapReceiverEntry.setStatus('optional')
receiverEntryId = MibTableColumn((1, 3, 6, 1, 4, 1, 3715, 99, 1, 3, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: receiverEntryId.setStatus('mandatory')
receiverAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 3715, 99, 1, 3, 5, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: receiverAddress.setStatus('mandatory')
receiverPort = MibTableColumn((1, 3, 6, 1, 4, 1, 3715, 99, 1, 3, 5, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: receiverPort.setStatus('mandatory')
receiverCommunity = MibTableColumn((1, 3, 6, 1, 4, 1, 3715, 99, 1, 3, 5, 1, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: receiverCommunity.setStatus('mandatory')
controlTrapSending = MibScalar((1, 3, 6, 1, 4, 1, 3715, 99, 1, 3, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: controlTrapSending.setStatus('optional')
controlTrapInterval = MibScalar((1, 3, 6, 1, 4, 1, 3715, 99, 1, 3, 7), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: controlTrapInterval.setStatus('optional')
controlTrapLifeTime = MibScalar((1, 3, 6, 1, 4, 1, 3715, 99, 1, 3, 8), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: controlTrapLifeTime.setStatus('optional')
controlAlarmOnDelay = MibScalar((1, 3, 6, 1, 4, 1, 3715, 99, 1, 3, 9), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: controlAlarmOnDelay.setStatus('optional')
controlAlarmOffDelay = MibScalar((1, 3, 6, 1, 4, 1, 3715, 99, 1, 3, 10), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: controlAlarmOffDelay.setStatus('optional')
controlTrapDelay = MibScalar((1, 3, 6, 1, 4, 1, 3715, 99, 1, 3, 11), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: controlTrapDelay.setStatus('optional')
elementProductKey = MibIdentifier((1, 3, 6, 1, 4, 1, 3715, 99, 1, 4))
productKeyNumberOfKeys = MibScalar((1, 3, 6, 1, 4, 1, 3715, 99, 1, 4, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: productKeyNumberOfKeys.setStatus('optional')
productKeyTable = MibTable((1, 3, 6, 1, 4, 1, 3715, 99, 1, 4, 5), )
if mibBuilder.loadTexts: productKeyTable.setStatus('mandatory')
productKeyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3715, 99, 1, 4, 5, 1), ).setIndexNames((0, "TELESTE-COMMON-MIB", "productKeyIndex"))
if mibBuilder.loadTexts: productKeyEntry.setStatus('mandatory')
productKeyIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3715, 99, 1, 4, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: productKeyIndex.setStatus('mandatory')
productKeyValue = MibTableColumn((1, 3, 6, 1, 4, 1, 3715, 99, 1, 4, 5, 1, 2), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: productKeyValue.setStatus('mandatory')
productKeyMask = MibTableColumn((1, 3, 6, 1, 4, 1, 3715, 99, 1, 4, 5, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: productKeyMask.setStatus('mandatory')
productKeyStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3715, 99, 1, 4, 5, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("keyInvalid", 1), ("keyValid", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: productKeyStatus.setStatus('mandatory')
productKeyCipher = MibTableColumn((1, 3, 6, 1, 4, 1, 3715, 99, 1, 4, 5, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("cipherOther", 1), ("cipherBlowFish", 2), ("cipherXXTEA", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: productKeyCipher.setStatus('mandatory')
productKeyNumberOfFeatures = MibTableColumn((1, 3, 6, 1, 4, 1, 3715, 99, 1, 4, 5, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: productKeyNumberOfFeatures.setStatus('mandatory')
productKeyFeatureTable = MibTable((1, 3, 6, 1, 4, 1, 3715, 99, 1, 4, 6), )
if mibBuilder.loadTexts: productKeyFeatureTable.setStatus('mandatory')
productKeyFeatureEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3715, 99, 1, 4, 6, 1), ).setIndexNames((0, "TELESTE-COMMON-MIB", "productKeyIndex"), (0, "TELESTE-COMMON-MIB", "productKeyFeatureIndex"))
if mibBuilder.loadTexts: productKeyFeatureEntry.setStatus('mandatory')
productKeyFeatureIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3715, 99, 1, 4, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: productKeyFeatureIndex.setStatus('mandatory')
productKeyFeatureName = MibTableColumn((1, 3, 6, 1, 4, 1, 3715, 99, 1, 4, 6, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: productKeyFeatureName.setStatus('mandatory')
productKeyFeatureEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 3715, 99, 1, 4, 6, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("featureDisable", 1), ("featureEnable", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: productKeyFeatureEnable.setStatus('mandatory')
productKeyFeatureExpirationTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3715, 99, 1, 4, 6, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: productKeyFeatureExpirationTime.setStatus('mandatory')
module = MibIdentifier((1, 3, 6, 1, 4, 1, 3715, 99, 2))
moduleInformation = MibIdentifier((1, 3, 6, 1, 4, 1, 3715, 99, 2, 1))
moduleTable = MibTable((1, 3, 6, 1, 4, 1, 3715, 99, 2, 1, 1), )
if mibBuilder.loadTexts: moduleTable.setStatus('mandatory')
moduleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3715, 99, 2, 1, 1, 1), ).setIndexNames((0, "TELESTE-COMMON-MIB", "moduleId"))
if mibBuilder.loadTexts: moduleEntry.setStatus('mandatory')
moduleId = MibTableColumn((1, 3, 6, 1, 4, 1, 3715, 99, 2, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: moduleId.setStatus('mandatory')
moduleName = MibTableColumn((1, 3, 6, 1, 4, 1, 3715, 99, 2, 1, 1, 1, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: moduleName.setStatus('optional')
moduleHwType = MibTableColumn((1, 3, 6, 1, 4, 1, 3715, 99, 2, 1, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: moduleHwType.setStatus('mandatory')
moduleRackNo = MibTableColumn((1, 3, 6, 1, 4, 1, 3715, 99, 2, 1, 1, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: moduleRackNo.setStatus('optional')
moduleSlotNo = MibTableColumn((1, 3, 6, 1, 4, 1, 3715, 99, 2, 1, 1, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: moduleSlotNo.setStatus('optional')
moduleDetailTable = MibTable((1, 3, 6, 1, 4, 1, 3715, 99, 2, 1, 2), )
if mibBuilder.loadTexts: moduleDetailTable.setStatus('mandatory')
moduleDetailEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3715, 99, 2, 1, 2, 1), ).setIndexNames((0, "TELESTE-COMMON-MIB", "moduleId"))
if mibBuilder.loadTexts: moduleDetailEntry.setStatus('mandatory')
moduleMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 3715, 99, 2, 1, 2, 1, 1), TPhysAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: moduleMacAddress.setStatus('optional')
moduleBusAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 3715, 99, 2, 1, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: moduleBusAddress.setStatus('optional')
moduleAppDate = MibTableColumn((1, 3, 6, 1, 4, 1, 3715, 99, 2, 1, 2, 1, 3), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: moduleAppDate.setStatus('mandatory')
moduleAppVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 3715, 99, 2, 1, 2, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: moduleAppVersion.setStatus('mandatory')
moduleBiosDate = MibTableColumn((1, 3, 6, 1, 4, 1, 3715, 99, 2, 1, 2, 1, 5), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: moduleBiosDate.setStatus('mandatory')
moduleBiosVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 3715, 99, 2, 1, 2, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: moduleBiosVersion.setStatus('mandatory')
moduleHwSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 3715, 99, 2, 1, 2, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: moduleHwSerialNumber.setStatus('mandatory')
moduleHwVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 3715, 99, 2, 1, 2, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: moduleHwVersion.setStatus('mandatory')
moduleStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 3715, 99, 2, 2))
moduleStatusTable = MibTable((1, 3, 6, 1, 4, 1, 3715, 99, 2, 2, 1), )
if mibBuilder.loadTexts: moduleStatusTable.setStatus('mandatory')
moduleStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3715, 99, 2, 2, 1, 1), ).setIndexNames((0, "TELESTE-COMMON-MIB", "moduleId"))
if mibBuilder.loadTexts: moduleStatusEntry.setStatus('mandatory')
statusResetCause = MibTableColumn((1, 3, 6, 1, 4, 1, 3715, 99, 2, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("unknown", 1), ("selfReset", 2), ("powerReset", 3), ("commandedReset", 4), ("softdownloadReset", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: statusResetCause.setStatus('mandatory')
statusRunningSwImage = MibTableColumn((1, 3, 6, 1, 4, 1, 3715, 99, 2, 2, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: statusRunningSwImage.setStatus('mandatory')
statusInternalTemperature = MibTableColumn((1, 3, 6, 1, 4, 1, 3715, 99, 2, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-600, 1300))).setMaxAccess("readonly")
if mibBuilder.loadTexts: statusInternalTemperature.setStatus('mandatory')
statusLidStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3715, 99, 2, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noLid", 1), ("closed", 2), ("open", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: statusLidStatus.setStatus('optional')
statusRestartCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 3715, 99, 2, 2, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: statusRestartCounter.setStatus('optional')
moduleControl = MibIdentifier((1, 3, 6, 1, 4, 1, 3715, 99, 2, 3))
moduleControlTable = MibTable((1, 3, 6, 1, 4, 1, 3715, 99, 2, 3, 1), )
if mibBuilder.loadTexts: moduleControlTable.setStatus('optional')
moduleControlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3715, 99, 2, 3, 1, 1), ).setIndexNames((0, "TELESTE-COMMON-MIB", "moduleId"))
if mibBuilder.loadTexts: moduleControlEntry.setStatus('optional')
controlLedUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 3715, 99, 2, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notSupported", 1), ("alwaysOn", 2), ("offWhenLidClosed", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: controlLedUsage.setStatus('optional')
controlMarkState = MibTableColumn((1, 3, 6, 1, 4, 1, 3715, 99, 2, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notSupported", 1), ("on", 2), ("off", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: controlMarkState.setStatus('optional')
controlReset = MibTableColumn((1, 3, 6, 1, 4, 1, 3715, 99, 2, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noReset", 1), ("hardReset", 2), ("softReset", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: controlReset.setStatus('optional')
controlTempLimitHiHi = MibTableColumn((1, 3, 6, 1, 4, 1, 3715, 99, 2, 3, 1, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: controlTempLimitHiHi.setStatus('optional')
controlTempLimitHi = MibTableColumn((1, 3, 6, 1, 4, 1, 3715, 99, 2, 3, 1, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: controlTempLimitHi.setStatus('optional')
controlTempLimitLo = MibTableColumn((1, 3, 6, 1, 4, 1, 3715, 99, 2, 3, 1, 1, 7), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: controlTempLimitLo.setStatus('optional')
controlTempLimitLoLo = MibTableColumn((1, 3, 6, 1, 4, 1, 3715, 99, 2, 3, 1, 1, 8), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: controlTempLimitLoLo.setStatus('optional')
controlTempDeadBand = MibTableColumn((1, 3, 6, 1, 4, 1, 3715, 99, 2, 3, 1, 1, 9), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: controlTempDeadBand.setStatus('optional')
controlInternalAppAccess = MibTableColumn((1, 3, 6, 1, 4, 1, 3715, 99, 2, 3, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("allowIntControl", 1), ("denyIntControl", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: controlInternalAppAccess.setStatus('optional')
controlLocalAccess = MibTableColumn((1, 3, 6, 1, 4, 1, 3715, 99, 2, 3, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: controlLocalAccess.setStatus('optional')
moduleSWUpdateTable = MibTable((1, 3, 6, 1, 4, 1, 3715, 99, 2, 3, 2), )
if mibBuilder.loadTexts: moduleSWUpdateTable.setStatus('optional')
moduleSWUpdateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3715, 99, 2, 3, 2, 1), ).setIndexNames((0, "TELESTE-COMMON-MIB", "moduleId"))
if mibBuilder.loadTexts: moduleSWUpdateEntry.setStatus('optional')
sWUpdateControl = MibTableColumn((1, 3, 6, 1, 4, 1, 3715, 99, 2, 3, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("updateIdle", 1), ("updateRunning", 2), ("updateFailed", 3), ("updateStart", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sWUpdateControl.setStatus('optional')
swUpdateURL = MibTableColumn((1, 3, 6, 1, 4, 1, 3715, 99, 2, 3, 2, 1, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swUpdateURL.setStatus('optional')
sWUpdateFileName = MibTableColumn((1, 3, 6, 1, 4, 1, 3715, 99, 2, 3, 2, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sWUpdateFileName.setStatus('optional')
sWUpdateStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3715, 99, 2, 3, 2, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sWUpdateStatus.setStatus('optional')
moduleRegistry = MibIdentifier((1, 3, 6, 1, 4, 1, 3715, 99, 2, 4))
moduleSizeOfTable = MibTable((1, 3, 6, 1, 4, 1, 3715, 99, 2, 4, 1), )
if mibBuilder.loadTexts: moduleSizeOfTable.setStatus('optional')
moduleSizeOfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3715, 99, 2, 4, 1, 1), ).setIndexNames((0, "TELESTE-COMMON-MIB", "moduleId"))
if mibBuilder.loadTexts: moduleSizeOfEntry.setStatus('optional')
sizeOfRegistry = MibTableColumn((1, 3, 6, 1, 4, 1, 3715, 99, 2, 4, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sizeOfRegistry.setStatus('mandatory')
sizeOfRepairlog = MibTableColumn((1, 3, 6, 1, 4, 1, 3715, 99, 2, 4, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sizeOfRepairlog.setStatus('optional')
sizeOfNotebook = MibTableColumn((1, 3, 6, 1, 4, 1, 3715, 99, 2, 4, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sizeOfNotebook.setStatus('optional')
moduleRegistryTable = MibTable((1, 3, 6, 1, 4, 1, 3715, 99, 2, 4, 2), )
if mibBuilder.loadTexts: moduleRegistryTable.setStatus('optional')
moduleRegistryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3715, 99, 2, 4, 2, 1), ).setIndexNames((0, "TELESTE-COMMON-MIB", "moduleId"), (0, "TELESTE-COMMON-MIB", "regIndex"))
if mibBuilder.loadTexts: moduleRegistryEntry.setStatus('optional')
regIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3715, 99, 2, 4, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: regIndex.setStatus('optional')
regName = MibTableColumn((1, 3, 6, 1, 4, 1, 3715, 99, 2, 4, 2, 1, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: regName.setStatus('optional')
regValue = MibTableColumn((1, 3, 6, 1, 4, 1, 3715, 99, 2, 4, 2, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: regValue.setStatus('optional')
moduleRepairLogTable = MibTable((1, 3, 6, 1, 4, 1, 3715, 99, 2, 4, 3), )
if mibBuilder.loadTexts: moduleRepairLogTable.setStatus('optional')
moduleRepairLogEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3715, 99, 2, 4, 3, 1), ).setIndexNames((0, "TELESTE-COMMON-MIB", "moduleId"), (0, "TELESTE-COMMON-MIB", "repairIndex"))
if mibBuilder.loadTexts: moduleRepairLogEntry.setStatus('optional')
repairIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3715, 99, 2, 4, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32767))).setMaxAccess("readonly")
if mibBuilder.loadTexts: repairIndex.setStatus('optional')
repairDate = MibTableColumn((1, 3, 6, 1, 4, 1, 3715, 99, 2, 4, 3, 1, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: repairDate.setStatus('optional')
repairReasonCode = MibTableColumn((1, 3, 6, 1, 4, 1, 3715, 99, 2, 4, 3, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(4, 4)).setFixedLength(4)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: repairReasonCode.setStatus('optional')
repairNameCode = MibTableColumn((1, 3, 6, 1, 4, 1, 3715, 99, 2, 4, 3, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(4, 4)).setFixedLength(4)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: repairNameCode.setStatus('optional')
repairComment = MibTableColumn((1, 3, 6, 1, 4, 1, 3715, 99, 2, 4, 3, 1, 5), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: repairComment.setStatus('optional')
moduleNotebookTable = MibTable((1, 3, 6, 1, 4, 1, 3715, 99, 2, 4, 4), )
if mibBuilder.loadTexts: moduleNotebookTable.setStatus('optional')
moduleNotebookEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3715, 99, 2, 4, 4, 1), ).setIndexNames((0, "TELESTE-COMMON-MIB", "moduleId"), (0, "TELESTE-COMMON-MIB", "notebookLineNumber"))
if mibBuilder.loadTexts: moduleNotebookEntry.setStatus('optional')
notebookLineNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 3715, 99, 2, 4, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: notebookLineNumber.setStatus('optional')
notebookLineText = MibTableColumn((1, 3, 6, 1, 4, 1, 3715, 99, 2, 4, 4, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 50))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: notebookLineText.setStatus('optional')
mibBuilder.exportSymbols("TELESTE-COMMON-MIB", moduleAppVersion=moduleAppVersion, productKeyFeatureExpirationTime=productKeyFeatureExpirationTime, repairIndex=repairIndex, statusLid=statusLid, swUpdateURL=swUpdateURL, controlAlarmOnDelay=controlAlarmOnDelay, elementTotalUpTime=elementTotalUpTime, elementInformation=elementInformation, productKeyEntry=productKeyEntry, moduleStatusTable=moduleStatusTable, moduleRegistry=moduleRegistry, controlAlarmOffDelay=controlAlarmOffDelay, moduleBiosDate=moduleBiosDate, controlLocalAccess=controlLocalAccess, statusHardware=statusHardware, moduleSizeOfTable=moduleSizeOfTable, productKeyMask=productKeyMask, controlTrapReceiverTable=controlTrapReceiverTable, moduleStatusEntry=moduleStatusEntry, controlMaxNumberTrapReceivers=controlMaxNumberTrapReceivers, receiverAddress=receiverAddress, moduleInformation=moduleInformation, controlTrapDelay=controlTrapDelay, elementProductKey=elementProductKey, controlResetElement=controlResetElement, productKeyCipher=productKeyCipher, receiverCommunity=receiverCommunity, moduleControl=moduleControl, sWUpdateFileName=sWUpdateFileName, controlTrapInterval=controlTrapInterval, statusResetCause=statusResetCause, controlTempLimitHiHi=controlTempLimitHiHi, controlTempDeadBand=controlTempDeadBand, sizeOfRegistry=sizeOfRegistry, elementLatitude=elementLatitude, productKeyFeatureIndex=productKeyFeatureIndex, moduleHwVersion=moduleHwVersion, moduleMacAddress=moduleMacAddress, statusTemperature=statusTemperature, controlBusMasterAdminState=controlBusMasterAdminState, notebookLineNumber=notebookLineNumber, elementResetCount=elementResetCount, statusSoftware=statusSoftware, statusSettings=statusSettings, productKeyIndex=productKeyIndex, sizeOfNotebook=sizeOfNotebook, statusLidStatus=statusLidStatus, module=module, moduleRepairLogEntry=moduleRepairLogEntry, statusBusMaster=statusBusMaster, controlMarkState=controlMarkState, moduleSizeOfEntry=moduleSizeOfEntry, controlAlarmDetection=controlAlarmDetection, moduleRepairLogTable=moduleRepairLogTable, productKeyFeatureEnable=productKeyFeatureEnable, repairReasonCode=repairReasonCode, productKeyStatus=productKeyStatus, receiverPort=receiverPort, element=element, regName=regName, elementControl=elementControl, regValue=regValue, controlInternalAppAccess=controlInternalAppAccess, moduleRegistryTable=moduleRegistryTable, moduleEntry=moduleEntry, controlLedUsage=controlLedUsage, statusInternalTemperature=statusInternalTemperature, moduleRegistryEntry=moduleRegistryEntry, moduleTable=moduleTable, productKeyTable=productKeyTable, elementStructure=elementStructure, elementLongitude=elementLongitude, statusFan=statusFan, elementConfigChangeCode=elementConfigChangeCode, productKeyFeatureName=productKeyFeatureName, controlTrapSending=controlTrapSending, repairComment=repairComment, moduleSWUpdateEntry=moduleSWUpdateEntry, moduleNotebookTable=moduleNotebookTable, productKeyNumberOfFeatures=productKeyNumberOfFeatures, controlTempLimitLoLo=controlTempLimitLoLo, controlTempLimitHi=controlTempLimitHi, moduleBiosVersion=moduleBiosVersion, elementName=elementName, moduleAppDate=moduleAppDate, elementStatus=elementStatus, statusRunningSwImage=statusRunningSwImage, productKeyFeatureEntry=productKeyFeatureEntry, moduleRackNo=moduleRackNo, sWUpdateStatus=sWUpdateStatus, controlTrapReceiverEntry=controlTrapReceiverEntry, moduleBusAddress=moduleBusAddress, repairDate=repairDate, moduleSlotNo=moduleSlotNo, productKeyFeatureTable=productKeyFeatureTable, moduleName=moduleName, controlTrapLifeTime=controlTrapLifeTime, moduleSWUpdateTable=moduleSWUpdateTable, moduleControlTable=moduleControlTable, moduleNotebookEntry=moduleNotebookEntry, productKeyNumberOfKeys=productKeyNumberOfKeys, moduleStatus=moduleStatus, elementAltitude=elementAltitude, statusRestartCounter=statusRestartCounter, moduleDetailTable=moduleDetailTable, statusGeneral=statusGeneral, moduleDetailEntry=moduleDetailEntry, statusLmt=statusLmt, moduleControlEntry=moduleControlEntry, controlTempLimitLo=controlTempLimitLo, moduleId=moduleId, productKeyValue=productKeyValue, notebookLineText=notebookLineText, sWUpdateControl=sWUpdateControl, repairNameCode=repairNameCode, controlReset=controlReset, sizeOfRepairlog=sizeOfRepairlog, receiverEntryId=receiverEntryId, regIndex=regIndex, moduleHwSerialNumber=moduleHwSerialNumber, moduleHwType=moduleHwType)
