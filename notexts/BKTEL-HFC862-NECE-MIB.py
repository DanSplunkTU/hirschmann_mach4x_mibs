#
# PySNMP MIB module BKTEL-HFC862-NECE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/bktel/BKTEL-HFC862-NECE-MIB
# Produced by pysmi-1.1.3 at Sun Nov 21 00:45:25 2021
# On host fv-az39-63 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
modules, ModuleWidthValue, TruthValue, DisplayString, NESlotValue, PerceivedSeverityValue = mibBuilder.importSymbols("BKTEL-HFC862-BASE-MIB", "modules", "ModuleWidthValue", "TruthValue", "DisplayString", "NESlotValue", "PerceivedSeverityValue")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, IpAddress, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, enterprises, ObjectIdentity, Integer32, TimeTicks, MibIdentifier, experimental, NotificationType, Counter64, Unsigned32, Bits, Gauge32, Counter32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "IpAddress", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "enterprises", "ObjectIdentity", "Integer32", "TimeTicks", "MibIdentifier", "experimental", "NotificationType", "Counter64", "Unsigned32", "Bits", "Gauge32", "Counter32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
nece = MibIdentifier((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100))
neceCommon = MibIdentifier((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 1))
neceStates = MibIdentifier((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 2))
neceConfiguration = MibIdentifier((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3))
neceControl = MibIdentifier((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 4))
neceMeasuringValues = MibIdentifier((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 5))
neceDisplay = MibIdentifier((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 6))
class GpioType(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("gpioTypeNotSupported", 1), ("gpioTypeInputOnly", 2), ("gpioTypeInputOrOutput", 3), ("gpioTypeOutputOnly", 4))

class GpioMode(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("gpioModeInput", 1), ("gpioModeInputIsNotify", 2), ("gpioModeInputIsWarning", 3), ("gpioModeInputIsAlarm", 4), ("gpioModeOutputOnAnyAlarm", 5), ("gpioModeOutputOnAnyWarning", 6))

class GpioLogicLevel(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("gpioLevelActiveHigh", 1), ("gpioLevelActiveLow", 2))

class HmsTrapsComplianceValue(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("fullCompliant", 1), ("minorCompliant", 2))

class HfcInventoryFormatValue(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("format_DKS_T12_9", 1), ("format_T_Nova_E531i", 2))

class TrapVerifyTimeoutValue(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(30, 600)

class TrapAccumulationTimeValue(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 60)

class NESlotWriteValue(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-1, 99)

neceCommonNumberOfModules = MibScalar((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neceCommonNumberOfModules.setStatus('mandatory')
neceCommonTable = MibTable((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 1, 2), )
if mibBuilder.loadTexts: neceCommonTable.setStatus('mandatory')
neceCommonEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 1, 2, 1), ).setIndexNames((0, "BKTEL-HFC862-NECE-MIB", "neceNESlot"))
if mibBuilder.loadTexts: neceCommonEntry.setStatus('mandatory')
neceNESlot = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 1, 2, 1, 1), NESlotValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neceNESlot.setStatus('mandatory')
neceCommonType = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 1, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: neceCommonType.setStatus('mandatory')
neceCommonDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 1, 2, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neceCommonDescr.setStatus('mandatory')
neceCommonFirmwareId = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 1, 2, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: neceCommonFirmwareId.setStatus('mandatory')
neceCommonModuleWidth = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 1, 2, 1, 5), ModuleWidthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neceCommonModuleWidth.setStatus('optional')
neceStatesTable = MibTable((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 2, 1), )
if mibBuilder.loadTexts: neceStatesTable.setStatus('mandatory')
neceStatesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 2, 1, 1), ).setIndexNames((0, "BKTEL-HFC862-NECE-MIB", "neceNESlot"))
if mibBuilder.loadTexts: neceStatesEntry.setStatus('mandatory')
neceStatesGpInput1 = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 2, 1, 1, 1), PerceivedSeverityValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neceStatesGpInput1.setStatus('mandatory')
neceStatesGpInput2 = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 2, 1, 1, 2), PerceivedSeverityValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neceStatesGpInput2.setStatus('mandatory')
neceStatesGpInput3 = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 2, 1, 1, 3), PerceivedSeverityValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neceStatesGpInput3.setStatus('mandatory')
neceStatesGpInput4 = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 2, 1, 1, 4), PerceivedSeverityValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neceStatesGpInput4.setStatus('mandatory')
neceStatesGpInput5 = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 2, 1, 1, 5), PerceivedSeverityValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neceStatesGpInput5.setStatus('mandatory')
neceStatesGpInput6 = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 2, 1, 1, 6), PerceivedSeverityValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neceStatesGpInput6.setStatus('mandatory')
neceStatesGpInput7 = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 2, 1, 1, 7), PerceivedSeverityValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neceStatesGpInput7.setStatus('mandatory')
neceStatesGpInput8 = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 2, 1, 1, 8), PerceivedSeverityValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neceStatesGpInput8.setStatus('mandatory')
neceStatesGpInput9 = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 2, 1, 1, 9), PerceivedSeverityValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neceStatesGpInput9.setStatus('mandatory')
neceStatesGpInput10 = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 2, 1, 1, 10), PerceivedSeverityValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neceStatesGpInput10.setStatus('mandatory')
neceStatesGpInput11 = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 2, 1, 1, 11), PerceivedSeverityValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neceStatesGpInput11.setStatus('mandatory')
neceStatesGpInput12 = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 2, 1, 1, 12), PerceivedSeverityValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neceStatesGpInput12.setStatus('mandatory')
neceStatesPowerSupplyLeft = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 2, 1, 1, 13), PerceivedSeverityValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neceStatesPowerSupplyLeft.setStatus('mandatory')
neceStatesPowerSupplyRight = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 2, 1, 1, 14), PerceivedSeverityValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neceStatesPowerSupplyRight.setStatus('mandatory')
neceStatesFanLeft = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 2, 1, 1, 15), PerceivedSeverityValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neceStatesFanLeft.setStatus('mandatory')
neceStatesFanRight = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 2, 1, 1, 16), PerceivedSeverityValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neceStatesFanRight.setStatus('mandatory')
neceConfigurationTable = MibTable((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1), )
if mibBuilder.loadTexts: neceConfigurationTable.setStatus('mandatory')
neceConfigurationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1), ).setIndexNames((0, "BKTEL-HFC862-NECE-MIB", "neceNESlot"))
if mibBuilder.loadTexts: neceConfigurationEntry.setStatus('mandatory')
neceConfigGpio1Type = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 1), GpioType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neceConfigGpio1Type.setStatus('mandatory')
neceConfigGpio1Mode = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 2), GpioMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neceConfigGpio1Mode.setStatus('mandatory')
neceConfigGpio1LogicLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 3), GpioLogicLevel()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neceConfigGpio1LogicLevel.setStatus('mandatory')
neceConfigGpio1Description = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neceConfigGpio1Description.setStatus('mandatory')
neceConfigGpio2Type = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 5), GpioType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neceConfigGpio2Type.setStatus('mandatory')
neceConfigGpio2Mode = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 6), GpioMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neceConfigGpio2Mode.setStatus('mandatory')
neceConfigGpio2LogicLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 7), GpioLogicLevel()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neceConfigGpio2LogicLevel.setStatus('mandatory')
neceConfigGpio2Description = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neceConfigGpio2Description.setStatus('mandatory')
neceConfigGpio3Type = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 9), GpioType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neceConfigGpio3Type.setStatus('mandatory')
neceConfigGpio3Mode = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 10), GpioMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neceConfigGpio3Mode.setStatus('mandatory')
neceConfigGpio3LogicLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 11), GpioLogicLevel()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neceConfigGpio3LogicLevel.setStatus('mandatory')
neceConfigGpio3Description = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 12), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neceConfigGpio3Description.setStatus('mandatory')
neceConfigGpio4Type = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 13), GpioType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neceConfigGpio4Type.setStatus('mandatory')
neceConfigGpio4Mode = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 14), GpioMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neceConfigGpio4Mode.setStatus('mandatory')
neceConfigGpio4LogicLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 15), GpioLogicLevel()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neceConfigGpio4LogicLevel.setStatus('mandatory')
neceConfigGpio4Description = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 16), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neceConfigGpio4Description.setStatus('mandatory')
neceConfigGpio5Type = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 17), GpioType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neceConfigGpio5Type.setStatus('mandatory')
neceConfigGpio5Mode = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 18), GpioMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neceConfigGpio5Mode.setStatus('mandatory')
neceConfigGpio5LogicLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 19), GpioLogicLevel()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neceConfigGpio5LogicLevel.setStatus('mandatory')
neceConfigGpio5Description = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 20), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neceConfigGpio5Description.setStatus('mandatory')
neceConfigGpio6Type = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 21), GpioType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neceConfigGpio6Type.setStatus('mandatory')
neceConfigGpio6Mode = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 22), GpioMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neceConfigGpio6Mode.setStatus('mandatory')
neceConfigGpio6LogicLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 23), GpioLogicLevel()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neceConfigGpio6LogicLevel.setStatus('mandatory')
neceConfigGpio6Description = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 24), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neceConfigGpio6Description.setStatus('mandatory')
neceConfigGpio7Type = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 25), GpioType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neceConfigGpio7Type.setStatus('mandatory')
neceConfigGpio7Mode = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 26), GpioMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neceConfigGpio7Mode.setStatus('mandatory')
neceConfigGpio7LogicLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 27), GpioLogicLevel()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neceConfigGpio7LogicLevel.setStatus('mandatory')
neceConfigGpio7Description = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 28), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neceConfigGpio7Description.setStatus('mandatory')
neceConfigGpio8Type = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 29), GpioType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neceConfigGpio8Type.setStatus('mandatory')
neceConfigGpio8Mode = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 30), GpioMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neceConfigGpio8Mode.setStatus('mandatory')
neceConfigGpio8LogicLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 31), GpioLogicLevel()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neceConfigGpio8LogicLevel.setStatus('mandatory')
neceConfigGpio8Description = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 32), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neceConfigGpio8Description.setStatus('mandatory')
neceConfigGpio9Type = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 33), GpioType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neceConfigGpio9Type.setStatus('mandatory')
neceConfigGpio9Mode = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 34), GpioMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neceConfigGpio9Mode.setStatus('mandatory')
neceConfigGpio9LogicLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 35), GpioLogicLevel()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neceConfigGpio9LogicLevel.setStatus('mandatory')
neceConfigGpio9Description = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 36), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neceConfigGpio9Description.setStatus('mandatory')
neceConfigGpio10Type = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 37), GpioType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neceConfigGpio10Type.setStatus('mandatory')
neceConfigGpio10Mode = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 38), GpioMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neceConfigGpio10Mode.setStatus('mandatory')
neceConfigGpio10LogicLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 39), GpioLogicLevel()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neceConfigGpio10LogicLevel.setStatus('mandatory')
neceConfigGpio10Description = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 40), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neceConfigGpio10Description.setStatus('mandatory')
neceConfigGpio11Type = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 41), GpioType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neceConfigGpio11Type.setStatus('mandatory')
neceConfigGpio11Mode = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 42), GpioMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neceConfigGpio11Mode.setStatus('mandatory')
neceConfigGpio11LogicLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 43), GpioLogicLevel()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neceConfigGpio11LogicLevel.setStatus('mandatory')
neceConfigGpio11Description = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 44), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neceConfigGpio11Description.setStatus('mandatory')
neceConfigGpio12Type = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 45), GpioType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neceConfigGpio12Type.setStatus('mandatory')
neceConfigGpio12Mode = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 46), GpioMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neceConfigGpio12Mode.setStatus('mandatory')
neceConfigGpio12LogicLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 47), GpioLogicLevel()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neceConfigGpio12LogicLevel.setStatus('mandatory')
neceConfigGpio12Description = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 48), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neceConfigGpio12Description.setStatus('mandatory')
neceConfigNESlotWrite = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 49), NESlotWriteValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neceConfigNESlotWrite.setStatus('optional')
neceConfigIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 50), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neceConfigIpAddress.setStatus('mandatory')
neceConfigNetmask = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 51), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neceConfigNetmask.setStatus('mandatory')
neceConfigDefaultrouter = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 52), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neceConfigDefaultrouter.setStatus('mandatory')
neceConfigTrapReceiver1HostIp = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 53), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neceConfigTrapReceiver1HostIp.setStatus('mandatory')
neceConfigTrapReceiver1Community = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 54), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(4, 31))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neceConfigTrapReceiver1Community.setStatus('mandatory')
neceConfigTrapReceiver2HostIp = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 55), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neceConfigTrapReceiver2HostIp.setStatus('mandatory')
neceConfigTrapReceiver2to4Community = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 56), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(4, 31))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neceConfigTrapReceiver2to4Community.setStatus('mandatory')
neceConfigTrapReceiver3HostIp = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 57), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neceConfigTrapReceiver3HostIp.setStatus('mandatory')
neceConfigTrapReceiver4HostIp = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 58), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neceConfigTrapReceiver4HostIp.setStatus('mandatory')
neceConfigGetCommunity = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 59), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neceConfigGetCommunity.setStatus('mandatory')
neceConfigSetCommunity = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 60), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neceConfigSetCommunity.setStatus('mandatory')
neceConfigTrapReceiverVerify = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 61), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neceConfigTrapReceiverVerify.setStatus('mandatory')
neceConfigTrapVerifyReceiverIp = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 62), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neceConfigTrapVerifyReceiverIp.setStatus('mandatory')
neceConfigTrapVerifyTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 63), TrapVerifyTimeoutValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neceConfigTrapVerifyTimeout.setStatus('mandatory')
neceConfigTrapAccumulationTime = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 64), TrapAccumulationTimeValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neceConfigTrapAccumulationTime.setStatus('mandatory')
neceConfigCableWatchUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 65), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neceConfigCableWatchUsed.setStatus('mandatory')
neceConfigHmsTrapsCompliance = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 66), HmsTrapsComplianceValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neceConfigHmsTrapsCompliance.setStatus('mandatory')
neceConfigHmsNotificationsEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 67), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neceConfigHmsNotificationsEnable.setStatus('mandatory')
neceConfigHfcInventoryFormat = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 68), HfcInventoryFormatValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neceConfigHfcInventoryFormat.setStatus('mandatory')
neceConfigTimezone = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 69), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-24, 24))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neceConfigTimezone.setStatus('mandatory')
neceConfigNtpServerIp = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 70), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neceConfigNtpServerIp.setStatus('mandatory')
neceConfigFactoryCommandLine = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 71), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neceConfigFactoryCommandLine.setStatus('mandatory')
neceConfigDaylightSavingFrom = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 72), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neceConfigDaylightSavingFrom.setStatus('mandatory')
neceConfigDaylightSavingTo = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 3, 1, 1, 73), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neceConfigDaylightSavingTo.setStatus('mandatory')
neceControlTable = MibTable((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 4, 1), )
if mibBuilder.loadTexts: neceControlTable.setStatus('mandatory')
neceControlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 4, 1, 1), ).setIndexNames((0, "BKTEL-HFC862-NECE-MIB", "neceNESlot"))
if mibBuilder.loadTexts: neceControlEntry.setStatus('mandatory')
neceControlReset = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 4, 1, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neceControlReset.setStatus('mandatory')
neceMeasuringValuesTable = MibTable((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 5, 1), )
if mibBuilder.loadTexts: neceMeasuringValuesTable.setStatus('mandatory')
neceMeasuringValuesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 5, 1, 1), ).setIndexNames((0, "BKTEL-HFC862-NECE-MIB", "neceNESlot"))
if mibBuilder.loadTexts: neceMeasuringValuesEntry.setStatus('mandatory')
neceTemperatureLoLo = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 5, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neceTemperatureLoLo.setStatus('mandatory')
neceTemperatureLo = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 5, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neceTemperatureLo.setStatus('mandatory')
neceTemperatureValue = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 5, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neceTemperatureValue.setStatus('mandatory')
neceTemperatureHi = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 5, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neceTemperatureHi.setStatus('mandatory')
neceTemperatureHiHi = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 5, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neceTemperatureHiHi.setStatus('mandatory')
neceDisplayTable = MibTable((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 6, 1), )
if mibBuilder.loadTexts: neceDisplayTable.setStatus('mandatory')
neceDisplayEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 6, 1, 1), ).setIndexNames((0, "BKTEL-HFC862-NECE-MIB", "neceNESlot"))
if mibBuilder.loadTexts: neceDisplayEntry.setStatus('mandatory')
neceDisplayTrapsSent = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 6, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neceDisplayTrapsSent.setStatus('mandatory')
neceDisplayTrapsDiscarded = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 2, 100, 6, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neceDisplayTrapsDiscarded.setStatus('mandatory')
mibBuilder.exportSymbols("BKTEL-HFC862-NECE-MIB", neceConfigTrapReceiver2to4Community=neceConfigTrapReceiver2to4Community, neceConfigGpio8LogicLevel=neceConfigGpio8LogicLevel, neceConfigDefaultrouter=neceConfigDefaultrouter, neceConfigTrapReceiver1Community=neceConfigTrapReceiver1Community, neceConfigHfcInventoryFormat=neceConfigHfcInventoryFormat, GpioLogicLevel=GpioLogicLevel, neceStatesGpInput11=neceStatesGpInput11, neceStatesFanRight=neceStatesFanRight, neceStates=neceStates, neceConfigGpio10Mode=neceConfigGpio10Mode, neceConfigGpio10LogicLevel=neceConfigGpio10LogicLevel, neceConfigGpio3LogicLevel=neceConfigGpio3LogicLevel, neceConfigGpio6Mode=neceConfigGpio6Mode, neceConfigTrapReceiver4HostIp=neceConfigTrapReceiver4HostIp, neceConfigGpio4LogicLevel=neceConfigGpio4LogicLevel, neceStatesTable=neceStatesTable, neceStatesFanLeft=neceStatesFanLeft, neceConfigGpio10Type=neceConfigGpio10Type, neceConfiguration=neceConfiguration, neceMeasuringValues=neceMeasuringValues, neceConfigGpio1LogicLevel=neceConfigGpio1LogicLevel, GpioMode=GpioMode, neceConfigGpio12Type=neceConfigGpio12Type, neceConfigGpio7Type=neceConfigGpio7Type, neceCommonTable=neceCommonTable, neceStatesPowerSupplyLeft=neceStatesPowerSupplyLeft, neceCommonDescr=neceCommonDescr, neceStatesGpInput8=neceStatesGpInput8, neceConfigNtpServerIp=neceConfigNtpServerIp, neceConfigGpio4Mode=neceConfigGpio4Mode, neceDisplay=neceDisplay, neceCommonEntry=neceCommonEntry, neceConfigTrapReceiver3HostIp=neceConfigTrapReceiver3HostIp, neceTemperatureLo=neceTemperatureLo, neceStatesPowerSupplyRight=neceStatesPowerSupplyRight, neceConfigGpio8Mode=neceConfigGpio8Mode, neceStatesGpInput10=neceStatesGpInput10, neceConfigGpio6Description=neceConfigGpio6Description, neceStatesGpInput2=neceStatesGpInput2, neceControlEntry=neceControlEntry, neceConfigTrapReceiverVerify=neceConfigTrapReceiverVerify, neceStatesGpInput7=neceStatesGpInput7, neceConfigGpio6Type=neceConfigGpio6Type, neceConfigGpio1Description=neceConfigGpio1Description, neceCommonFirmwareId=neceCommonFirmwareId, neceConfigGpio3Type=neceConfigGpio3Type, neceConfigGpio1Type=neceConfigGpio1Type, neceDisplayTrapsDiscarded=neceDisplayTrapsDiscarded, neceConfigTimezone=neceConfigTimezone, neceConfigGpio9LogicLevel=neceConfigGpio9LogicLevel, neceConfigGpio2LogicLevel=neceConfigGpio2LogicLevel, neceConfigGpio4Description=neceConfigGpio4Description, neceCommonType=neceCommonType, neceConfigDaylightSavingFrom=neceConfigDaylightSavingFrom, HmsTrapsComplianceValue=HmsTrapsComplianceValue, neceConfigSetCommunity=neceConfigSetCommunity, neceConfigDaylightSavingTo=neceConfigDaylightSavingTo, neceConfigHmsNotificationsEnable=neceConfigHmsNotificationsEnable, neceDisplayEntry=neceDisplayEntry, neceConfigGpio11LogicLevel=neceConfigGpio11LogicLevel, neceConfigGpio10Description=neceConfigGpio10Description, nece=nece, TrapAccumulationTimeValue=TrapAccumulationTimeValue, neceConfigGpio12Mode=neceConfigGpio12Mode, neceConfigCableWatchUsed=neceConfigCableWatchUsed, neceStatesEntry=neceStatesEntry, neceStatesGpInput4=neceStatesGpInput4, HfcInventoryFormatValue=HfcInventoryFormatValue, neceConfigGpio11Mode=neceConfigGpio11Mode, neceStatesGpInput12=neceStatesGpInput12, neceConfigGpio5Mode=neceConfigGpio5Mode, neceConfigGpio8Type=neceConfigGpio8Type, neceConfigGetCommunity=neceConfigGetCommunity, TrapVerifyTimeoutValue=TrapVerifyTimeoutValue, neceConfigGpio7LogicLevel=neceConfigGpio7LogicLevel, neceMeasuringValuesTable=neceMeasuringValuesTable, neceTemperatureValue=neceTemperatureValue, neceNESlot=neceNESlot, NESlotWriteValue=NESlotWriteValue, neceConfigGpio12LogicLevel=neceConfigGpio12LogicLevel, neceConfigurationTable=neceConfigurationTable, neceCommon=neceCommon, neceConfigTrapReceiver1HostIp=neceConfigTrapReceiver1HostIp, GpioType=GpioType, neceConfigTrapVerifyTimeout=neceConfigTrapVerifyTimeout, neceConfigFactoryCommandLine=neceConfigFactoryCommandLine, neceConfigGpio12Description=neceConfigGpio12Description, neceConfigGpio3Mode=neceConfigGpio3Mode, neceCommonModuleWidth=neceCommonModuleWidth, neceConfigGpio6LogicLevel=neceConfigGpio6LogicLevel, neceConfigHmsTrapsCompliance=neceConfigHmsTrapsCompliance, neceConfigGpio11Description=neceConfigGpio11Description, neceConfigGpio4Type=neceConfigGpio4Type, neceStatesGpInput6=neceStatesGpInput6, neceConfigGpio2Type=neceConfigGpio2Type, neceConfigNetmask=neceConfigNetmask, neceConfigGpio11Type=neceConfigGpio11Type, neceConfigGpio1Mode=neceConfigGpio1Mode, neceStatesGpInput5=neceStatesGpInput5, neceConfigGpio5LogicLevel=neceConfigGpio5LogicLevel, neceConfigGpio9Type=neceConfigGpio9Type, neceConfigNESlotWrite=neceConfigNESlotWrite, neceConfigGpio9Mode=neceConfigGpio9Mode, neceConfigGpio3Description=neceConfigGpio3Description, neceConfigurationEntry=neceConfigurationEntry, neceMeasuringValuesEntry=neceMeasuringValuesEntry, neceControl=neceControl, neceConfigGpio5Description=neceConfigGpio5Description, neceTemperatureHi=neceTemperatureHi, neceStatesGpInput3=neceStatesGpInput3, neceStatesGpInput9=neceStatesGpInput9, neceConfigGpio2Description=neceConfigGpio2Description, neceConfigGpio9Description=neceConfigGpio9Description, neceConfigIpAddress=neceConfigIpAddress, neceConfigTrapReceiver2HostIp=neceConfigTrapReceiver2HostIp, neceCommonNumberOfModules=neceCommonNumberOfModules, neceTemperatureLoLo=neceTemperatureLoLo, neceControlReset=neceControlReset, neceConfigGpio8Description=neceConfigGpio8Description, neceConfigGpio2Mode=neceConfigGpio2Mode, neceControlTable=neceControlTable, neceDisplayTable=neceDisplayTable, neceStatesGpInput1=neceStatesGpInput1, neceConfigGpio5Type=neceConfigGpio5Type, neceConfigGpio7Mode=neceConfigGpio7Mode, neceConfigTrapAccumulationTime=neceConfigTrapAccumulationTime, neceDisplayTrapsSent=neceDisplayTrapsSent, neceTemperatureHiHi=neceTemperatureHiHi, neceConfigTrapVerifyReceiverIp=neceConfigTrapVerifyReceiverIp, neceConfigGpio7Description=neceConfigGpio7Description)
