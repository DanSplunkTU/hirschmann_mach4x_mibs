#
# PySNMP MIB module POSEIDON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/hwg/POSEIDON-MIB
# Produced by pysmi-1.1.8 at Mon Feb  7 16:14:08 2022
# On host fv-az42-619 platform Linux version 5.11.0-1028-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
sysName, = mibBuilder.importSymbols("SNMPv2-MIB", "sysName")
Bits, IpAddress, ObjectIdentity, Counter32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Counter64, Integer32, NotificationType, MibIdentifier, Unsigned32, enterprises, ModuleIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "IpAddress", "ObjectIdentity", "Counter32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Counter64", "Integer32", "NotificationType", "MibIdentifier", "Unsigned32", "enterprises", "ModuleIdentity", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class PositiveInteger(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class OnOff(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("off", 0), ("on", 1))

class OutputType(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("onOff", 0), ("rts", 1), ("dtr", 2))

class OutputMode(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("manual", 0), ("autoAlarm", 1), ("autoTriggerEq", 2), ("autoTriggerHi", 3), ("autoTriggerLo", 4))

class UnitType(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    namedValues = NamedValues(("celsius", 0), ("fahrenheit", 1), ("kelvin", 2), ("percent", 3), ("volt", 4), ("miliAmper", 5), ("noUnit", 6), ("pulse", 7), ("switch", 8), ("dewPoint", 9), ("absoluteHumidity", 10), ("pressure", 11), ("universal", 12))

class InputAlarmSetup(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("inactive", 0), ("activeOff", 1), ("activeOn", 2))

class InputAlarmState(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("normal", 0), ("alarm", 1))

class SensorState(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("invalid", 0), ("normal", 1), ("alarmstate", 2), ("alarm", 3))

class SensorID(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 65535)

class IOName(DisplayString):
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 20)

class SensorName(DisplayString):
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 15)

class SensorValue(Integer32):
    pass

class SensorString(DisplayString):
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 10)

class SensorUnitString(DisplayString):
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 4)

class SensorFlags(Integer32):
    pass

class TimeStamp(TimeTicks):
    pass

hwgroup = MibIdentifier((1, 3, 6, 1, 4, 1, 21796))
charonII = MibIdentifier((1, 3, 6, 1, 4, 1, 21796, 3))
poseidon = MibIdentifier((1, 3, 6, 1, 4, 1, 21796, 3, 3))
info = MibIdentifier((1, 3, 6, 1, 4, 1, 21796, 3, 3, 70))
setup = MibIdentifier((1, 3, 6, 1, 4, 1, 21796, 3, 3, 99))
inpTable = MibTable((1, 3, 6, 1, 4, 1, 21796, 3, 3, 1), )
if mibBuilder.loadTexts: inpTable.setStatus('current')
inpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 21796, 3, 3, 1, 1), ).setIndexNames((0, "POSEIDON-MIB", "inpIndex"))
if mibBuilder.loadTexts: inpEntry.setStatus('current')
inpIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 3, 3, 1, 1, 1), PositiveInteger())
if mibBuilder.loadTexts: inpIndex.setStatus('current')
inpValue = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 3, 3, 1, 1, 2), OnOff()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inpValue.setStatus('current')
inpName = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 3, 3, 1, 1, 3), IOName()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: inpName.setStatus('current')
inpAlarmSetup = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 3, 3, 1, 1, 4), InputAlarmSetup()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: inpAlarmSetup.setStatus('current')
inpAlarmState = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 3, 3, 1, 1, 5), InputAlarmState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inpAlarmState.setStatus('current')
outTable = MibTable((1, 3, 6, 1, 4, 1, 21796, 3, 3, 2), )
if mibBuilder.loadTexts: outTable.setStatus('current')
outEntry = MibTableRow((1, 3, 6, 1, 4, 1, 21796, 3, 3, 2, 1), ).setIndexNames((0, "POSEIDON-MIB", "outIndex"))
if mibBuilder.loadTexts: outEntry.setStatus('current')
outIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 3, 3, 2, 1, 1), PositiveInteger())
if mibBuilder.loadTexts: outIndex.setStatus('current')
outValue = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 3, 3, 2, 1, 2), OnOff()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: outValue.setStatus('current')
outName = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 3, 3, 2, 1, 3), IOName()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: outName.setStatus('current')
outType = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 3, 3, 2, 1, 4), OutputType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: outType.setStatus('current')
outMode = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 3, 3, 2, 1, 5), OutputMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: outMode.setStatus('current')
sensTable = MibTable((1, 3, 6, 1, 4, 1, 21796, 3, 3, 3), )
if mibBuilder.loadTexts: sensTable.setStatus('current')
sensEntry = MibTableRow((1, 3, 6, 1, 4, 1, 21796, 3, 3, 3, 1), ).setIndexNames((0, "POSEIDON-MIB", "sensIndex"))
if mibBuilder.loadTexts: sensEntry.setStatus('current')
sensIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 3, 3, 3, 1, 1), PositiveInteger())
if mibBuilder.loadTexts: sensIndex.setStatus('current')
sensName = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 3, 3, 3, 1, 2), SensorName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensName.setStatus('current')
sensState = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 3, 3, 3, 1, 4), SensorState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensState.setStatus('current')
sensString = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 3, 3, 3, 1, 5), SensorString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensString.setStatus('current')
sensValue = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 3, 3, 3, 1, 6), SensorValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensValue.setStatus('current')
sensValueRaw = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 3, 3, 3, 1, 7), SensorValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensValueRaw.setStatus('current')
sensID = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 3, 3, 3, 1, 8), SensorID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensID.setStatus('current')
sensUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 3, 3, 3, 1, 9), UnitType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensUnit.setStatus('current')
sensUnitString = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 3, 3, 3, 1, 10), SensorUnitString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensUnitString.setStatus('current')
tsAlarm = MibIdentifier((1, 3, 6, 1, 4, 1, 21796, 3, 3, 50))
tsAlarmsPresent = MibScalar((1, 3, 6, 1, 4, 1, 21796, 3, 3, 50, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tsAlarmsPresent.setStatus('current')
tsAlarmTable = MibTable((1, 3, 6, 1, 4, 1, 21796, 3, 3, 50, 2), )
if mibBuilder.loadTexts: tsAlarmTable.setStatus('current')
tsAlarmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 21796, 3, 3, 50, 2, 1), ).setIndexNames((0, "POSEIDON-MIB", "tsAlarmIdx"))
if mibBuilder.loadTexts: tsAlarmEntry.setStatus('current')
tsAlarmIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 3, 3, 50, 2, 1, 1), PositiveInteger())
if mibBuilder.loadTexts: tsAlarmIdx.setStatus('current')
tsAlarmId = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 3, 3, 50, 2, 1, 2), PositiveInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tsAlarmId.setStatus('current')
tsAlarmDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 3, 3, 50, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("inputStateAlarm", 1), ("temperatureOutOfRange", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tsAlarmDescr.setStatus('current')
tsAlarmSensName = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 3, 3, 50, 2, 1, 4), SensorName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tsAlarmSensName.setStatus('current')
tsAlarmTime = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 3, 3, 50, 2, 1, 5), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tsAlarmTime.setStatus('current')
infoAddressMAC = MibScalar((1, 3, 6, 1, 4, 1, 21796, 3, 3, 70, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 17))).setMaxAccess("readonly")
if mibBuilder.loadTexts: infoAddressMAC.setStatus('current')
sensSetup = MibIdentifier((1, 3, 6, 1, 4, 1, 21796, 3, 3, 99, 1))
unitType = MibScalar((1, 3, 6, 1, 4, 1, 21796, 3, 3, 99, 1, 1), UnitType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: unitType.setStatus('current')
sensSetupTable = MibTable((1, 3, 6, 1, 4, 1, 21796, 3, 3, 99, 1, 2), )
if mibBuilder.loadTexts: sensSetupTable.setStatus('current')
sensSetupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 21796, 3, 3, 99, 1, 2, 1), ).setIndexNames((0, "POSEIDON-MIB", "sensSetupIndex"))
if mibBuilder.loadTexts: sensSetupEntry.setStatus('current')
sensSetupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 3, 3, 99, 1, 2, 1, 1), PositiveInteger())
if mibBuilder.loadTexts: sensSetupIndex.setStatus('current')
sensSetupName = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 3, 3, 99, 1, 2, 1, 2), SensorName()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensSetupName.setStatus('current')
sensFlags = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 3, 3, 99, 1, 2, 1, 5), SensorFlags()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensFlags.setStatus('current')
sensLimitMin = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 3, 3, 99, 1, 2, 1, 6), SensorValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensLimitMin.setStatus('current')
sensLimitMax = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 3, 3, 99, 1, 2, 1, 7), SensorValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensLimitMax.setStatus('current')
sensHysteresis = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 3, 3, 99, 1, 2, 1, 8), SensorValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensHysteresis.setStatus('current')
inpAlarmStateChanged = NotificationType((1, 3, 6, 1, 4, 1, 21796, 3, 3) + (0,1)).setObjects(("SNMPv2-MIB", "sysName"), ("POSEIDON-MIB", "infoAddressMAC"), ("POSEIDON-MIB", "inpName"), ("POSEIDON-MIB", "inpValue"), ("POSEIDON-MIB", "inpAlarmState"))
sensAlarmStateChanged = NotificationType((1, 3, 6, 1, 4, 1, 21796, 3, 3) + (0,2)).setObjects(("SNMPv2-MIB", "sysName"), ("POSEIDON-MIB", "infoAddressMAC"), ("POSEIDON-MIB", "sensName"), ("POSEIDON-MIB", "sensID"), ("POSEIDON-MIB", "sensState"), ("POSEIDON-MIB", "sensValue"), ("POSEIDON-MIB", "sensUnit"))
tsTrapAlarmStart = NotificationType((1, 3, 6, 1, 4, 1, 21796, 3, 3) + (0,3)).setObjects(("SNMPv2-MIB", "sysName"), ("POSEIDON-MIB", "infoAddressMAC"), ("POSEIDON-MIB", "tsAlarmId"), ("POSEIDON-MIB", "tsAlarmDescr"))
tsTrapAlarmEnd = NotificationType((1, 3, 6, 1, 4, 1, 21796, 3, 3) + (0,4)).setObjects(("SNMPv2-MIB", "sysName"), ("POSEIDON-MIB", "infoAddressMAC"), ("POSEIDON-MIB", "tsAlarmId"), ("POSEIDON-MIB", "tsAlarmDescr"))
mibBuilder.exportSymbols("POSEIDON-MIB", sensString=sensString, tsAlarmsPresent=tsAlarmsPresent, charonII=charonII, OutputType=OutputType, OnOff=OnOff, inpEntry=inpEntry, tsAlarmId=tsAlarmId, sensSetupIndex=sensSetupIndex, unitType=unitType, inpAlarmStateChanged=inpAlarmStateChanged, sensAlarmStateChanged=sensAlarmStateChanged, tsTrapAlarmEnd=tsTrapAlarmEnd, sensSetupTable=sensSetupTable, InputAlarmState=InputAlarmState, setup=setup, infoAddressMAC=infoAddressMAC, tsTrapAlarmStart=tsTrapAlarmStart, sensName=sensName, outEntry=outEntry, poseidon=poseidon, IOName=IOName, outTable=outTable, outValue=outValue, sensUnit=sensUnit, sensLimitMin=sensLimitMin, SensorValue=SensorValue, tsAlarmTime=tsAlarmTime, tsAlarmSensName=tsAlarmSensName, sensSetupName=sensSetupName, inpIndex=inpIndex, tsAlarm=tsAlarm, outName=outName, sensValue=sensValue, inpAlarmSetup=inpAlarmSetup, inpName=inpName, sensValueRaw=sensValueRaw, sensID=sensID, outIndex=outIndex, tsAlarmDescr=tsAlarmDescr, tsAlarmIdx=tsAlarmIdx, sensState=sensState, inpAlarmState=inpAlarmState, sensLimitMax=sensLimitMax, tsAlarmTable=tsAlarmTable, SensorState=SensorState, SensorName=SensorName, SensorString=SensorString, info=info, inpTable=inpTable, sensUnitString=sensUnitString, sensSetup=sensSetup, outMode=outMode, tsAlarmEntry=tsAlarmEntry, sensTable=sensTable, SensorUnitString=SensorUnitString, hwgroup=hwgroup, inpValue=inpValue, OutputMode=OutputMode, TimeStamp=TimeStamp, sensHysteresis=sensHysteresis, sensSetupEntry=sensSetupEntry, PositiveInteger=PositiveInteger, InputAlarmSetup=InputAlarmSetup, sensEntry=sensEntry, outType=outType, sensIndex=sensIndex, SensorFlags=SensorFlags, sensFlags=sensFlags, SensorID=SensorID, UnitType=UnitType)
