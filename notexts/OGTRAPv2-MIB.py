#
# PySNMP MIB module OGTRAPv2-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/opengear/OGTRAPv2-MIB
# Produced by pysmi-1.1.8 at Mon Feb  7 16:17:32 2022
# On host fv-az42-619 platform Linux version 5.11.0-1028-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, enterprises, ObjectIdentity, iso, Integer32, Bits, IpAddress, NotificationType, Unsigned32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, TimeTicks, NotificationType, ModuleIdentity, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "enterprises", "ObjectIdentity", "iso", "Integer32", "Bits", "IpAddress", "NotificationType", "Unsigned32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "TimeTicks", "NotificationType", "ModuleIdentity", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
opengear = MibIdentifier((1, 3, 6, 1, 4, 1, 25049))
ogLegacyMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2))
ogNotification = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 0))
ogAlarmMib = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 101))
ogSerialSignalMib = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 102))
ogSerialPatternMib = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 103))
ogSerialUserMib = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 104))
ogHostMib = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 105))
ogWebMib = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 106))
ogEmdMib = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 107))
ogPowerSupplyMib = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 108))
ogUpsMib = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 109))
ogRpcMib = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 110))
ogNetMib = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 111))
ogCellMib = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 112))
ogWifiMib = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 113))
ogDialPoolMib = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 114))
ogCustomMib = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 115))
ogCliMib = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 116))
ogAlarmMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 101, 1))
ogAlarm = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 101, 1, 1))
ogAlarmTable = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 101, 1, 1, 1))
ogAlarmEntry = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 101, 1, 1, 1, 1))
ogAlarmIndex = MibScalar((1, 3, 6, 1, 4, 1, 25049, 2, 101, 1, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogAlarmIndex.setStatus('mandatory')
ogAlarmEventId = MibScalar((1, 3, 6, 1, 4, 1, 25049, 2, 101, 1, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogAlarmEventId.setStatus('mandatory')
ogAlarmName = MibScalar((1, 3, 6, 1, 4, 1, 25049, 2, 101, 1, 1, 1, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogAlarmName.setStatus('mandatory')
ogAlarmCheck = MibScalar((1, 3, 6, 1, 4, 1, 25049, 2, 101, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogAlarmCheck.setStatus('mandatory')
ogAlarmInstance = MibScalar((1, 3, 6, 1, 4, 1, 25049, 2, 101, 1, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogAlarmInstance.setStatus('mandatory')
ogAlarmTime = MibScalar((1, 3, 6, 1, 4, 1, 25049, 2, 101, 1, 1, 1, 1, 6), OctetString().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(8, 8), ValueSizeConstraint(11, 11), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogAlarmTime.setStatus('mandatory')
ogAlarmType = MibScalar((1, 3, 6, 1, 4, 1, 25049, 2, 101, 1, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 255, 65535))).clone(namedValues=NamedValues(("serialSignalCts", 1), ("serialSignalDcd", 2), ("serialSignalDsr", 3), ("serialPatternTx", 4), ("serialPatternRx", 5), ("serialUserSession", 6), ("hostPingDown", 7), ("hostPingUp", 8), ("hostServiceDown", 9), ("hostServiceUp", 10), ("hostUserSession", 11), ("webUserSession", 12), ("envTemperatureLow", 13), ("envTemperatureHigh", 14), ("envHumidityLow", 15), ("envHumidityHigh", 16), ("dioSignalOpened", 17), ("dioSignalClosed", 18), ("netInterfaceDown", 19), ("netInterfaceStarting", 20), ("netInterfaceUp", 21), ("netInterfaceStopping", 22), ("powerSupplyInputVoltageLow", 23), ("powerSupplyInputVoltageHigh", 24), ("powerSupplyOutputCurrentLow", 25), ("powerSupplyOutputCurrentHigh", 26), ("powerSupplyTemperatureLow", 27), ("powerSupplyTemperatureHigh", 28), ("upsTemperatureHigh", 29), ("upsTemperatureLow", 30), ("upsHumidityHigh", 31), ("upsHumidityLow", 32), ("upsOnBattery", 33), ("upsLowBattery", 34), ("upsBatteryChargeLow", 35), ("upsBatteryChargeHigh", 36), ("upsBatteryVoltageLow", 37), ("upsBatteryVoltageHigh", 38), ("upsBatteryCurrentLow", 39), ("upsBatteryCurrentHigh", 40), ("upsBatteryTemperatureLow", 41), ("upsBatteryTemperatureHigh", 42), ("upsInputFrequencyLow", 43), ("upsInputFrequencyHigh", 44), ("upsInputVoltageLow", 45), ("upsInputVoltageHigh", 46), ("upsInputCurrentLow", 47), ("upsInputCurrentHigh", 48), ("upsOutputFrequencyLow", 49), ("upsOutputFrequencyHigh", 50), ("upsOutputVoltageLow", 51), ("upsOutputVoltageHigh", 52), ("upsOutputCurrentLow", 53), ("upsOutputCurrentHigh", 54), ("upsOutputLoadLow", 55), ("upsOutputLoadHigh", 56), ("upsOutputPowerLow", 57), ("upsOutputPowerHigh", 58), ("upsOutputTruePowerLow", 59), ("upsOutputTruePowerHigh", 60), ("rpcInputFrequencyLow", 61), ("rpcInputFrequencyHigh", 62), ("rpcInputVoltageLow", 63), ("rpcInputVoltageHigh", 64), ("rpcInputCurrentLow", 65), ("rpcInputCurrentHigh", 66), ("rpcOutletFrequencyHigh", 67), ("rpcOutletFrequencyLow", 68), ("rpcOutletVoltageHigh", 69), ("rpcOutletVoltageLow", 70), ("rpcOutletCurrentHigh", 71), ("rpcOutletCurrentLow", 72), ("rpcOutletStateOff", 73), ("rpcOutletStateOn", 74), ("cellDataUsage", 75), ("cellMessageReceived", 76), ("cellSignalLow", 77), ("cellSignalHigh", 78), ("cellApnChanged", 79), ("cellTowerChanged", 80), ("cellNetworkChanged", 81), ("wirelessClientConnected", 82), ("wirelessClientDisconnected", 83), ("wirelessClientSignalLow", 84), ("wirelessClientSignalHigh", 85), ("wirelessApAssociation", 86), ("wirelessApDisassociation", 87), ("wirelessApAuthenticationFailure", 88), ("dialPoolHealth", 89), ("cliUserSession", 90), ("customCheckFailure", 255), ("unknown", 65535)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogAlarmType.setStatus('mandatory')
ogAlarmSummary = MibScalar((1, 3, 6, 1, 4, 1, 25049, 2, 101, 1, 1, 1, 1, 8), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogAlarmSummary.setStatus('mandatory')
ogAlarmDevice = MibScalar((1, 3, 6, 1, 4, 1, 25049, 2, 101, 1, 1, 1, 1, 9), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogAlarmDevice.setStatus('mandatory')
ogAlarmUser = MibScalar((1, 3, 6, 1, 4, 1, 25049, 2, 101, 1, 1, 1, 1, 10), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogAlarmUser.setStatus('mandatory')
ogAlarmTriggerValue = MibScalar((1, 3, 6, 1, 4, 1, 25049, 2, 101, 1, 1, 1, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogAlarmTriggerValue.setStatus('mandatory')
ogAlarmCurrentValue = MibScalar((1, 3, 6, 1, 4, 1, 25049, 2, 101, 1, 1, 1, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogAlarmCurrentValue.setStatus('mandatory')
ogAlarmPreviousValue = MibScalar((1, 3, 6, 1, 4, 1, 25049, 2, 101, 1, 1, 1, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogAlarmPreviousValue.setStatus('mandatory')
ogAlarmState = MibScalar((1, 3, 6, 1, 4, 1, 25049, 2, 101, 1, 1, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("normal", 1), ("triggered", 2), ("resolving", 3), ("waiting", 4), ("disabled", 5), ("unresolvable", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogAlarmState.setStatus('mandatory')
ogSerialSignalMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 102, 1))
ogSerialSignalAlarm = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 102, 1, 1))
ogSerialSignalAlarmTable = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 102, 1, 1, 1))
ogSerialSignalAlarmEntry = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 102, 1, 1, 1, 1))
ogSerialSignalNotification = NotificationType((1, 3, 6, 1, 4, 1, 25049) + (0,1)).setObjects(("OGTRAPv2-MIB", "ogAlarmEventId"), ("OGTRAPv2-MIB", "ogAlarmName"), ("OGTRAPv2-MIB", "ogAlarmCheck"), ("OGTRAPv2-MIB", "ogAlarmInstance"), ("OGTRAPv2-MIB", "ogAlarmTime"), ("OGTRAPv2-MIB", "ogAlarmType"), ("OGTRAPv2-MIB", "ogAlarmSummary"), ("OGTRAPv2-MIB", "ogAlarmDevice"), ("OGTRAPv2-MIB", "ogAlarmTriggerValue"), ("OGTRAPv2-MIB", "ogAlarmCurrentValue"), ("OGTRAPv2-MIB", "ogAlarmPreviousValue"), ("OGTRAPv2-MIB", "ogAlarmState"))
ogSerialPatternMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 103, 1))
ogSerialPatternAlarm = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 103, 1, 1))
ogSerialPatternAlarmTable = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 103, 1, 1, 1))
ogSerialPatternAlarmEntry = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 103, 1, 1, 1, 1))
ogSerialPatternNotification = NotificationType((1, 3, 6, 1, 4, 1, 25049) + (0,2)).setObjects(("OGTRAPv2-MIB", "ogAlarmEventId"), ("OGTRAPv2-MIB", "ogAlarmName"), ("OGTRAPv2-MIB", "ogAlarmCheck"), ("OGTRAPv2-MIB", "ogAlarmInstance"), ("OGTRAPv2-MIB", "ogAlarmTime"), ("OGTRAPv2-MIB", "ogAlarmType"), ("OGTRAPv2-MIB", "ogAlarmSummary"), ("OGTRAPv2-MIB", "ogAlarmDevice"), ("OGTRAPv2-MIB", "ogAlarmTriggerValue"), ("OGTRAPv2-MIB", "ogAlarmCurrentValue"), ("OGTRAPv2-MIB", "ogAlarmState"))
ogSerialUserMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 104, 1))
ogSerialUserAlarm = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 104, 1, 1))
ogSerialUserAlarmTable = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 104, 1, 1, 1))
ogSerialUserAlarmEntry = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 104, 1, 1, 1, 1))
ogSerialUserNotification = NotificationType((1, 3, 6, 1, 4, 1, 25049) + (0,3)).setObjects(("OGTRAPv2-MIB", "ogAlarmEventId"), ("OGTRAPv2-MIB", "ogAlarmName"), ("OGTRAPv2-MIB", "ogAlarmCheck"), ("OGTRAPv2-MIB", "ogAlarmInstance"), ("OGTRAPv2-MIB", "ogAlarmTime"), ("OGTRAPv2-MIB", "ogAlarmType"), ("OGTRAPv2-MIB", "ogAlarmSummary"), ("OGTRAPv2-MIB", "ogAlarmDevice"), ("OGTRAPv2-MIB", "ogAlarmTriggerValue"), ("OGTRAPv2-MIB", "ogAlarmCurrentValue"), ("OGTRAPv2-MIB", "ogAlarmPreviousValue"), ("OGTRAPv2-MIB", "ogAlarmState"))
ogHostMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 105, 1))
ogHostEvent = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 105, 1, 1))
ogHostEventTable = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 105, 1, 1, 1))
ogHostEventEntry = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 105, 1, 1, 1, 1))
ogHostPingNotification = NotificationType((1, 3, 6, 1, 4, 1, 25049) + (0,4)).setObjects(("OGTRAPv2-MIB", "ogAlarmEventId"), ("OGTRAPv2-MIB", "ogAlarmName"), ("OGTRAPv2-MIB", "ogAlarmCheck"), ("OGTRAPv2-MIB", "ogAlarmInstance"), ("OGTRAPv2-MIB", "ogAlarmTime"), ("OGTRAPv2-MIB", "ogAlarmType"), ("OGTRAPv2-MIB", "ogAlarmSummary"), ("OGTRAPv2-MIB", "ogAlarmDevice"), ("OGTRAPv2-MIB", "ogAlarmTriggerValue"), ("OGTRAPv2-MIB", "ogAlarmCurrentValue"), ("OGTRAPv2-MIB", "ogAlarmPreviousValue"), ("OGTRAPv2-MIB", "ogAlarmState"))
ogHostServiceNotification = NotificationType((1, 3, 6, 1, 4, 1, 25049) + (0,5)).setObjects(("OGTRAPv2-MIB", "ogAlarmEventId"), ("OGTRAPv2-MIB", "ogAlarmName"), ("OGTRAPv2-MIB", "ogAlarmCheck"), ("OGTRAPv2-MIB", "ogAlarmInstance"), ("OGTRAPv2-MIB", "ogAlarmTime"), ("OGTRAPv2-MIB", "ogAlarmType"), ("OGTRAPv2-MIB", "ogAlarmSummary"), ("OGTRAPv2-MIB", "ogAlarmDevice"), ("OGTRAPv2-MIB", "ogAlarmTriggerValue"), ("OGTRAPv2-MIB", "ogAlarmCurrentValue"), ("OGTRAPv2-MIB", "ogAlarmPreviousValue"), ("OGTRAPv2-MIB", "ogAlarmState"))
ogHostUserNotification = NotificationType((1, 3, 6, 1, 4, 1, 25049) + (0,6)).setObjects(("OGTRAPv2-MIB", "ogAlarmEventId"), ("OGTRAPv2-MIB", "ogAlarmName"), ("OGTRAPv2-MIB", "ogAlarmCheck"), ("OGTRAPv2-MIB", "ogAlarmInstance"), ("OGTRAPv2-MIB", "ogAlarmTime"), ("OGTRAPv2-MIB", "ogAlarmType"), ("OGTRAPv2-MIB", "ogAlarmSummary"), ("OGTRAPv2-MIB", "ogAlarmDevice"), ("OGTRAPv2-MIB", "ogAlarmTriggerValue"), ("OGTRAPv2-MIB", "ogAlarmCurrentValue"), ("OGTRAPv2-MIB", "ogAlarmPreviousValue"), ("OGTRAPv2-MIB", "ogAlarmState"))
ogWebMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 106, 1))
ogWebEvent = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 106, 1, 1))
ogWebEventTable = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 106, 1, 1, 1))
ogWebEventEntry = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 106, 1, 1, 1, 1))
ogWebUserNotification = NotificationType((1, 3, 6, 1, 4, 1, 25049) + (0,7)).setObjects(("OGTRAPv2-MIB", "ogAlarmEventId"), ("OGTRAPv2-MIB", "ogAlarmName"), ("OGTRAPv2-MIB", "ogAlarmCheck"), ("OGTRAPv2-MIB", "ogAlarmInstance"), ("OGTRAPv2-MIB", "ogAlarmTime"), ("OGTRAPv2-MIB", "ogAlarmType"), ("OGTRAPv2-MIB", "ogAlarmSummary"), ("OGTRAPv2-MIB", "ogAlarmDevice"), ("OGTRAPv2-MIB", "ogAlarmTriggerValue"), ("OGTRAPv2-MIB", "ogAlarmCurrentValue"), ("OGTRAPv2-MIB", "ogAlarmPreviousValue"), ("OGTRAPv2-MIB", "ogAlarmState"))
ogEmdMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 107, 1))
ogEmdAlarm = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 107, 1, 1))
ogEmdAlarmTable = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 107, 1, 1, 1))
ogEmdAlarmEntry = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 107, 1, 1, 1, 1))
ogEmdTemperatureNotification = NotificationType((1, 3, 6, 1, 4, 1, 25049) + (0,8)).setObjects(("OGTRAPv2-MIB", "ogAlarmEventId"), ("OGTRAPv2-MIB", "ogAlarmName"), ("OGTRAPv2-MIB", "ogAlarmCheck"), ("OGTRAPv2-MIB", "ogAlarmInstance"), ("OGTRAPv2-MIB", "ogAlarmTime"), ("OGTRAPv2-MIB", "ogAlarmType"), ("OGTRAPv2-MIB", "ogAlarmSummary"), ("OGTRAPv2-MIB", "ogAlarmDevice"), ("OGTRAPv2-MIB", "ogAlarmTriggerValue"), ("OGTRAPv2-MIB", "ogAlarmCurrentValue"), ("OGTRAPv2-MIB", "ogAlarmPreviousValue"), ("OGTRAPv2-MIB", "ogAlarmState"))
ogEmdHumidityNotification = NotificationType((1, 3, 6, 1, 4, 1, 25049) + (0,9)).setObjects(("OGTRAPv2-MIB", "ogAlarmEventId"), ("OGTRAPv2-MIB", "ogAlarmName"), ("OGTRAPv2-MIB", "ogAlarmCheck"), ("OGTRAPv2-MIB", "ogAlarmInstance"), ("OGTRAPv2-MIB", "ogAlarmTime"), ("OGTRAPv2-MIB", "ogAlarmType"), ("OGTRAPv2-MIB", "ogAlarmSummary"), ("OGTRAPv2-MIB", "ogAlarmDevice"), ("OGTRAPv2-MIB", "ogAlarmTriggerValue"), ("OGTRAPv2-MIB", "ogAlarmCurrentValue"), ("OGTRAPv2-MIB", "ogAlarmPreviousValue"), ("OGTRAPv2-MIB", "ogAlarmState"))
ogEmdDioNotification = NotificationType((1, 3, 6, 1, 4, 1, 25049) + (0,10)).setObjects(("OGTRAPv2-MIB", "ogAlarmEventId"), ("OGTRAPv2-MIB", "ogAlarmName"), ("OGTRAPv2-MIB", "ogAlarmCheck"), ("OGTRAPv2-MIB", "ogAlarmInstance"), ("OGTRAPv2-MIB", "ogAlarmTime"), ("OGTRAPv2-MIB", "ogAlarmType"), ("OGTRAPv2-MIB", "ogAlarmSummary"), ("OGTRAPv2-MIB", "ogAlarmDevice"), ("OGTRAPv2-MIB", "ogAlarmTriggerValue"), ("OGTRAPv2-MIB", "ogAlarmCurrentValue"), ("OGTRAPv2-MIB", "ogAlarmPreviousValue"), ("OGTRAPv2-MIB", "ogAlarmState"))
ogPowerSupplyMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 108, 1))
ogPowerSupplyAlarm = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 108, 1, 1))
ogPowerSupplyAlarmTable = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 108, 1, 1, 1))
ogPowerSupplyAlarmEntry = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 108, 1, 1, 1, 1))
ogPowerSupplyInputNotification = NotificationType((1, 3, 6, 1, 4, 1, 25049) + (0,11)).setObjects(("OGTRAPv2-MIB", "ogAlarmEventId"), ("OGTRAPv2-MIB", "ogAlarmName"), ("OGTRAPv2-MIB", "ogAlarmCheck"), ("OGTRAPv2-MIB", "ogAlarmInstance"), ("OGTRAPv2-MIB", "ogAlarmTime"), ("OGTRAPv2-MIB", "ogAlarmType"), ("OGTRAPv2-MIB", "ogAlarmSummary"), ("OGTRAPv2-MIB", "ogAlarmDevice"), ("OGTRAPv2-MIB", "ogAlarmUser"), ("OGTRAPv2-MIB", "ogAlarmTriggerValue"), ("OGTRAPv2-MIB", "ogAlarmCurrentValue"), ("OGTRAPv2-MIB", "ogAlarmPreviousValue"), ("OGTRAPv2-MIB", "ogAlarmState"))
ogPowerSupplyOutputNotification = NotificationType((1, 3, 6, 1, 4, 1, 25049) + (0,12)).setObjects(("OGTRAPv2-MIB", "ogAlarmEventId"), ("OGTRAPv2-MIB", "ogAlarmName"), ("OGTRAPv2-MIB", "ogAlarmCheck"), ("OGTRAPv2-MIB", "ogAlarmInstance"), ("OGTRAPv2-MIB", "ogAlarmTime"), ("OGTRAPv2-MIB", "ogAlarmType"), ("OGTRAPv2-MIB", "ogAlarmSummary"), ("OGTRAPv2-MIB", "ogAlarmDevice"), ("OGTRAPv2-MIB", "ogAlarmUser"), ("OGTRAPv2-MIB", "ogAlarmTriggerValue"), ("OGTRAPv2-MIB", "ogAlarmCurrentValue"), ("OGTRAPv2-MIB", "ogAlarmPreviousValue"), ("OGTRAPv2-MIB", "ogAlarmState"))
ogPowerSupplyTempNotification = NotificationType((1, 3, 6, 1, 4, 1, 25049) + (0,13)).setObjects(("OGTRAPv2-MIB", "ogAlarmEventId"), ("OGTRAPv2-MIB", "ogAlarmName"), ("OGTRAPv2-MIB", "ogAlarmCheck"), ("OGTRAPv2-MIB", "ogAlarmInstance"), ("OGTRAPv2-MIB", "ogAlarmTime"), ("OGTRAPv2-MIB", "ogAlarmType"), ("OGTRAPv2-MIB", "ogAlarmSummary"), ("OGTRAPv2-MIB", "ogAlarmDevice"), ("OGTRAPv2-MIB", "ogAlarmUser"), ("OGTRAPv2-MIB", "ogAlarmTriggerValue"), ("OGTRAPv2-MIB", "ogAlarmCurrentValue"), ("OGTRAPv2-MIB", "ogAlarmPreviousValue"), ("OGTRAPv2-MIB", "ogAlarmState"))
ogUpsMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 109, 1))
ogUpsAlarm = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 109, 1, 1))
ogUpsAlarmTable = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 109, 1, 1, 1))
ogUpsAlarmEntry = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 109, 1, 1, 1, 1))
ogUpsNotification = NotificationType((1, 3, 6, 1, 4, 1, 25049) + (0,14)).setObjects(("OGTRAPv2-MIB", "ogAlarmEventId"), ("OGTRAPv2-MIB", "ogAlarmName"), ("OGTRAPv2-MIB", "ogAlarmCheck"), ("OGTRAPv2-MIB", "ogAlarmInstance"), ("OGTRAPv2-MIB", "ogAlarmTime"), ("OGTRAPv2-MIB", "ogAlarmType"), ("OGTRAPv2-MIB", "ogAlarmSummary"), ("OGTRAPv2-MIB", "ogAlarmDevice"), ("OGTRAPv2-MIB", "ogAlarmUser"), ("OGTRAPv2-MIB", "ogAlarmTriggerValue"), ("OGTRAPv2-MIB", "ogAlarmCurrentValue"), ("OGTRAPv2-MIB", "ogAlarmPreviousValue"), ("OGTRAPv2-MIB", "ogAlarmState"))
ogUpsBatteryNotification = NotificationType((1, 3, 6, 1, 4, 1, 25049) + (0,15)).setObjects(("OGTRAPv2-MIB", "ogAlarmEventId"), ("OGTRAPv2-MIB", "ogAlarmName"), ("OGTRAPv2-MIB", "ogAlarmCheck"), ("OGTRAPv2-MIB", "ogAlarmInstance"), ("OGTRAPv2-MIB", "ogAlarmTime"), ("OGTRAPv2-MIB", "ogAlarmType"), ("OGTRAPv2-MIB", "ogAlarmSummary"), ("OGTRAPv2-MIB", "ogAlarmDevice"), ("OGTRAPv2-MIB", "ogAlarmUser"), ("OGTRAPv2-MIB", "ogAlarmTriggerValue"), ("OGTRAPv2-MIB", "ogAlarmCurrentValue"), ("OGTRAPv2-MIB", "ogAlarmPreviousValue"), ("OGTRAPv2-MIB", "ogAlarmState"))
ogUpsInputNotification = NotificationType((1, 3, 6, 1, 4, 1, 25049) + (0,16)).setObjects(("OGTRAPv2-MIB", "ogAlarmEventId"), ("OGTRAPv2-MIB", "ogAlarmName"), ("OGTRAPv2-MIB", "ogAlarmCheck"), ("OGTRAPv2-MIB", "ogAlarmInstance"), ("OGTRAPv2-MIB", "ogAlarmTime"), ("OGTRAPv2-MIB", "ogAlarmType"), ("OGTRAPv2-MIB", "ogAlarmSummary"), ("OGTRAPv2-MIB", "ogAlarmDevice"), ("OGTRAPv2-MIB", "ogAlarmUser"), ("OGTRAPv2-MIB", "ogAlarmTriggerValue"), ("OGTRAPv2-MIB", "ogAlarmCurrentValue"), ("OGTRAPv2-MIB", "ogAlarmPreviousValue"), ("OGTRAPv2-MIB", "ogAlarmState"))
ogUpsOutputNotification = NotificationType((1, 3, 6, 1, 4, 1, 25049) + (0,17)).setObjects(("OGTRAPv2-MIB", "ogAlarmEventId"), ("OGTRAPv2-MIB", "ogAlarmName"), ("OGTRAPv2-MIB", "ogAlarmCheck"), ("OGTRAPv2-MIB", "ogAlarmInstance"), ("OGTRAPv2-MIB", "ogAlarmTime"), ("OGTRAPv2-MIB", "ogAlarmType"), ("OGTRAPv2-MIB", "ogAlarmSummary"), ("OGTRAPv2-MIB", "ogAlarmDevice"), ("OGTRAPv2-MIB", "ogAlarmUser"), ("OGTRAPv2-MIB", "ogAlarmTriggerValue"), ("OGTRAPv2-MIB", "ogAlarmCurrentValue"), ("OGTRAPv2-MIB", "ogAlarmPreviousValue"), ("OGTRAPv2-MIB", "ogAlarmState"))
ogRpcMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 110, 1))
ogRpcAlarm = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 110, 1, 1))
ogRpcAlarmTable = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 110, 1, 1, 1))
ogRpcAlarmEntry = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 110, 1, 1, 1, 1))
ogRpcInputNotification = NotificationType((1, 3, 6, 1, 4, 1, 25049) + (0,18)).setObjects(("OGTRAPv2-MIB", "ogAlarmEventId"), ("OGTRAPv2-MIB", "ogAlarmName"), ("OGTRAPv2-MIB", "ogAlarmCheck"), ("OGTRAPv2-MIB", "ogAlarmInstance"), ("OGTRAPv2-MIB", "ogAlarmTime"), ("OGTRAPv2-MIB", "ogAlarmType"), ("OGTRAPv2-MIB", "ogAlarmSummary"), ("OGTRAPv2-MIB", "ogAlarmDevice"), ("OGTRAPv2-MIB", "ogAlarmUser"), ("OGTRAPv2-MIB", "ogAlarmTriggerValue"), ("OGTRAPv2-MIB", "ogAlarmCurrentValue"), ("OGTRAPv2-MIB", "ogAlarmPreviousValue"), ("OGTRAPv2-MIB", "ogAlarmState"))
ogRpcOutputNotification = NotificationType((1, 3, 6, 1, 4, 1, 25049) + (0,19)).setObjects(("OGTRAPv2-MIB", "ogAlarmEventId"), ("OGTRAPv2-MIB", "ogAlarmName"), ("OGTRAPv2-MIB", "ogAlarmCheck"), ("OGTRAPv2-MIB", "ogAlarmInstance"), ("OGTRAPv2-MIB", "ogAlarmTime"), ("OGTRAPv2-MIB", "ogAlarmType"), ("OGTRAPv2-MIB", "ogAlarmSummary"), ("OGTRAPv2-MIB", "ogAlarmDevice"), ("OGTRAPv2-MIB", "ogAlarmUser"), ("OGTRAPv2-MIB", "ogAlarmTriggerValue"), ("OGTRAPv2-MIB", "ogAlarmCurrentValue"), ("OGTRAPv2-MIB", "ogAlarmPreviousValue"), ("OGTRAPv2-MIB", "ogAlarmState"))
ogRpcOutletNotification = NotificationType((1, 3, 6, 1, 4, 1, 25049) + (0,20)).setObjects(("OGTRAPv2-MIB", "ogAlarmEventId"), ("OGTRAPv2-MIB", "ogAlarmName"), ("OGTRAPv2-MIB", "ogAlarmCheck"), ("OGTRAPv2-MIB", "ogAlarmInstance"), ("OGTRAPv2-MIB", "ogAlarmTime"), ("OGTRAPv2-MIB", "ogAlarmType"), ("OGTRAPv2-MIB", "ogAlarmSummary"), ("OGTRAPv2-MIB", "ogAlarmDevice"), ("OGTRAPv2-MIB", "ogAlarmUser"), ("OGTRAPv2-MIB", "ogAlarmTriggerValue"), ("OGTRAPv2-MIB", "ogAlarmCurrentValue"), ("OGTRAPv2-MIB", "ogAlarmPreviousValue"), ("OGTRAPv2-MIB", "ogAlarmState"))
ogNetMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 111, 1))
ogNetAlarm = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 111, 1, 1))
ogNetAlarmTable = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 111, 1, 1, 1))
ogNetAlarmEntry = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 111, 1, 1, 1, 1))
ogNetInterfaceNotification = NotificationType((1, 3, 6, 1, 4, 1, 25049) + (0,21)).setObjects(("OGTRAPv2-MIB", "ogAlarmEventId"), ("OGTRAPv2-MIB", "ogAlarmName"), ("OGTRAPv2-MIB", "ogAlarmCheck"), ("OGTRAPv2-MIB", "ogAlarmInstance"), ("OGTRAPv2-MIB", "ogAlarmTime"), ("OGTRAPv2-MIB", "ogAlarmType"), ("OGTRAPv2-MIB", "ogAlarmSummary"), ("OGTRAPv2-MIB", "ogAlarmDevice"), ("OGTRAPv2-MIB", "ogAlarmTriggerValue"), ("OGTRAPv2-MIB", "ogAlarmCurrentValue"), ("OGTRAPv2-MIB", "ogAlarmPreviousValue"), ("OGTRAPv2-MIB", "ogAlarmState"))
ogCellMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 112, 1))
ogCellAlarm = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 112, 1, 1))
ogCellAlarmTable = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 112, 1, 1, 1))
ogCellAlarmEntry = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 112, 1, 1, 1, 1))
ogCellDataNotification = NotificationType((1, 3, 6, 1, 4, 1, 25049) + (0,22)).setObjects(("OGTRAPv2-MIB", "ogAlarmEventId"), ("OGTRAPv2-MIB", "ogAlarmName"), ("OGTRAPv2-MIB", "ogAlarmCheck"), ("OGTRAPv2-MIB", "ogAlarmInstance"), ("OGTRAPv2-MIB", "ogAlarmTime"), ("OGTRAPv2-MIB", "ogAlarmType"), ("OGTRAPv2-MIB", "ogAlarmSummary"), ("OGTRAPv2-MIB", "ogAlarmDevice"), ("OGTRAPv2-MIB", "ogAlarmUser"), ("OGTRAPv2-MIB", "ogAlarmTriggerValue"), ("OGTRAPv2-MIB", "ogAlarmCurrentValue"), ("OGTRAPv2-MIB", "ogAlarmPreviousValue"), ("OGTRAPv2-MIB", "ogAlarmState"))
ogCellMessageNotification = NotificationType((1, 3, 6, 1, 4, 1, 25049) + (0,23)).setObjects(("OGTRAPv2-MIB", "ogAlarmEventId"), ("OGTRAPv2-MIB", "ogAlarmName"), ("OGTRAPv2-MIB", "ogAlarmCheck"), ("OGTRAPv2-MIB", "ogAlarmInstance"), ("OGTRAPv2-MIB", "ogAlarmTime"), ("OGTRAPv2-MIB", "ogAlarmType"), ("OGTRAPv2-MIB", "ogAlarmSummary"), ("OGTRAPv2-MIB", "ogAlarmDevice"), ("OGTRAPv2-MIB", "ogAlarmUser"), ("OGTRAPv2-MIB", "ogAlarmTriggerValue"), ("OGTRAPv2-MIB", "ogAlarmCurrentValue"), ("OGTRAPv2-MIB", "ogAlarmPreviousValue"), ("OGTRAPv2-MIB", "ogAlarmState"))
ogCellSignalNotification = NotificationType((1, 3, 6, 1, 4, 1, 25049) + (0,24)).setObjects(("OGTRAPv2-MIB", "ogAlarmEventId"), ("OGTRAPv2-MIB", "ogAlarmName"), ("OGTRAPv2-MIB", "ogAlarmCheck"), ("OGTRAPv2-MIB", "ogAlarmInstance"), ("OGTRAPv2-MIB", "ogAlarmTime"), ("OGTRAPv2-MIB", "ogAlarmType"), ("OGTRAPv2-MIB", "ogAlarmSummary"), ("OGTRAPv2-MIB", "ogAlarmDevice"), ("OGTRAPv2-MIB", "ogAlarmUser"), ("OGTRAPv2-MIB", "ogAlarmTriggerValue"), ("OGTRAPv2-MIB", "ogAlarmCurrentValue"), ("OGTRAPv2-MIB", "ogAlarmPreviousValue"), ("OGTRAPv2-MIB", "ogAlarmState"))
ogCellApnNotification = NotificationType((1, 3, 6, 1, 4, 1, 25049) + (0,25)).setObjects(("OGTRAPv2-MIB", "ogAlarmEventId"), ("OGTRAPv2-MIB", "ogAlarmName"), ("OGTRAPv2-MIB", "ogAlarmCheck"), ("OGTRAPv2-MIB", "ogAlarmInstance"), ("OGTRAPv2-MIB", "ogAlarmTime"), ("OGTRAPv2-MIB", "ogAlarmType"), ("OGTRAPv2-MIB", "ogAlarmSummary"), ("OGTRAPv2-MIB", "ogAlarmDevice"), ("OGTRAPv2-MIB", "ogAlarmUser"), ("OGTRAPv2-MIB", "ogAlarmTriggerValue"), ("OGTRAPv2-MIB", "ogAlarmCurrentValue"), ("OGTRAPv2-MIB", "ogAlarmPreviousValue"), ("OGTRAPv2-MIB", "ogAlarmState"))
ogCellTowerNotification = NotificationType((1, 3, 6, 1, 4, 1, 25049) + (0,26)).setObjects(("OGTRAPv2-MIB", "ogAlarmEventId"), ("OGTRAPv2-MIB", "ogAlarmName"), ("OGTRAPv2-MIB", "ogAlarmCheck"), ("OGTRAPv2-MIB", "ogAlarmInstance"), ("OGTRAPv2-MIB", "ogAlarmTime"), ("OGTRAPv2-MIB", "ogAlarmType"), ("OGTRAPv2-MIB", "ogAlarmSummary"), ("OGTRAPv2-MIB", "ogAlarmDevice"), ("OGTRAPv2-MIB", "ogAlarmUser"), ("OGTRAPv2-MIB", "ogAlarmTriggerValue"), ("OGTRAPv2-MIB", "ogAlarmCurrentValue"), ("OGTRAPv2-MIB", "ogAlarmPreviousValue"), ("OGTRAPv2-MIB", "ogAlarmState"))
ogCellNetworkNotification = NotificationType((1, 3, 6, 1, 4, 1, 25049) + (0,27)).setObjects(("OGTRAPv2-MIB", "ogAlarmEventId"), ("OGTRAPv2-MIB", "ogAlarmName"), ("OGTRAPv2-MIB", "ogAlarmCheck"), ("OGTRAPv2-MIB", "ogAlarmInstance"), ("OGTRAPv2-MIB", "ogAlarmTime"), ("OGTRAPv2-MIB", "ogAlarmType"), ("OGTRAPv2-MIB", "ogAlarmSummary"), ("OGTRAPv2-MIB", "ogAlarmDevice"), ("OGTRAPv2-MIB", "ogAlarmUser"), ("OGTRAPv2-MIB", "ogAlarmTriggerValue"), ("OGTRAPv2-MIB", "ogAlarmCurrentValue"), ("OGTRAPv2-MIB", "ogAlarmPreviousValue"), ("OGTRAPv2-MIB", "ogAlarmState"))
ogWifiMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 113, 1))
ogWifiAlarm = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 113, 1, 1))
ogWifiAlarmTable = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 113, 1, 1, 1))
ogWifiAlarmEntry = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 113, 1, 1, 1, 1))
ogWifiClientConnectNotification = NotificationType((1, 3, 6, 1, 4, 1, 25049) + (0,28)).setObjects(("OGTRAPv2-MIB", "ogAlarmEventId"), ("OGTRAPv2-MIB", "ogAlarmName"), ("OGTRAPv2-MIB", "ogAlarmCheck"), ("OGTRAPv2-MIB", "ogAlarmInstance"), ("OGTRAPv2-MIB", "ogAlarmTime"), ("OGTRAPv2-MIB", "ogAlarmType"), ("OGTRAPv2-MIB", "ogAlarmSummary"), ("OGTRAPv2-MIB", "ogAlarmDevice"), ("OGTRAPv2-MIB", "ogAlarmUser"), ("OGTRAPv2-MIB", "ogAlarmTriggerValue"), ("OGTRAPv2-MIB", "ogAlarmCurrentValue"), ("OGTRAPv2-MIB", "ogAlarmPreviousValue"), ("OGTRAPv2-MIB", "ogAlarmState"))
ogWifiClientSignalNotification = NotificationType((1, 3, 6, 1, 4, 1, 25049) + (0,29)).setObjects(("OGTRAPv2-MIB", "ogAlarmEventId"), ("OGTRAPv2-MIB", "ogAlarmName"), ("OGTRAPv2-MIB", "ogAlarmCheck"), ("OGTRAPv2-MIB", "ogAlarmInstance"), ("OGTRAPv2-MIB", "ogAlarmTime"), ("OGTRAPv2-MIB", "ogAlarmType"), ("OGTRAPv2-MIB", "ogAlarmSummary"), ("OGTRAPv2-MIB", "ogAlarmDevice"), ("OGTRAPv2-MIB", "ogAlarmUser"), ("OGTRAPv2-MIB", "ogAlarmTriggerValue"), ("OGTRAPv2-MIB", "ogAlarmCurrentValue"), ("OGTRAPv2-MIB", "ogAlarmPreviousValue"), ("OGTRAPv2-MIB", "ogAlarmState"))
ogWifiApAssociationNotification = NotificationType((1, 3, 6, 1, 4, 1, 25049) + (0,30)).setObjects(("OGTRAPv2-MIB", "ogAlarmEventId"), ("OGTRAPv2-MIB", "ogAlarmName"), ("OGTRAPv2-MIB", "ogAlarmCheck"), ("OGTRAPv2-MIB", "ogAlarmInstance"), ("OGTRAPv2-MIB", "ogAlarmTime"), ("OGTRAPv2-MIB", "ogAlarmType"), ("OGTRAPv2-MIB", "ogAlarmSummary"), ("OGTRAPv2-MIB", "ogAlarmDevice"), ("OGTRAPv2-MIB", "ogAlarmUser"), ("OGTRAPv2-MIB", "ogAlarmTriggerValue"), ("OGTRAPv2-MIB", "ogAlarmCurrentValue"), ("OGTRAPv2-MIB", "ogAlarmPreviousValue"), ("OGTRAPv2-MIB", "ogAlarmState"))
ogWifiApAuthNotification = NotificationType((1, 3, 6, 1, 4, 1, 25049) + (0,31)).setObjects(("OGTRAPv2-MIB", "ogAlarmEventId"), ("OGTRAPv2-MIB", "ogAlarmName"), ("OGTRAPv2-MIB", "ogAlarmCheck"), ("OGTRAPv2-MIB", "ogAlarmInstance"), ("OGTRAPv2-MIB", "ogAlarmTime"), ("OGTRAPv2-MIB", "ogAlarmType"), ("OGTRAPv2-MIB", "ogAlarmSummary"), ("OGTRAPv2-MIB", "ogAlarmDevice"), ("OGTRAPv2-MIB", "ogAlarmUser"), ("OGTRAPv2-MIB", "ogAlarmTriggerValue"), ("OGTRAPv2-MIB", "ogAlarmCurrentValue"), ("OGTRAPv2-MIB", "ogAlarmPreviousValue"), ("OGTRAPv2-MIB", "ogAlarmState"))
ogDialPoolMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 114, 1))
ogDialPoolAlarm = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 114, 1, 1))
ogDialPoolAlarmTable = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 114, 1, 1, 1))
ogDialPoolAlarmEntry = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 114, 1, 1, 1, 1))
ogDialPoolHealthNotification = NotificationType((1, 3, 6, 1, 4, 1, 25049) + (0,32)).setObjects(("OGTRAPv2-MIB", "ogAlarmEventId"), ("OGTRAPv2-MIB", "ogAlarmName"), ("OGTRAPv2-MIB", "ogAlarmCheck"), ("OGTRAPv2-MIB", "ogAlarmInstance"), ("OGTRAPv2-MIB", "ogAlarmTime"), ("OGTRAPv2-MIB", "ogAlarmType"), ("OGTRAPv2-MIB", "ogAlarmSummary"), ("OGTRAPv2-MIB", "ogAlarmDevice"), ("OGTRAPv2-MIB", "ogAlarmUser"), ("OGTRAPv2-MIB", "ogAlarmTriggerValue"), ("OGTRAPv2-MIB", "ogAlarmCurrentValue"), ("OGTRAPv2-MIB", "ogAlarmPreviousValue"), ("OGTRAPv2-MIB", "ogAlarmState"))
ogCustomMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 115, 1))
ogCustomAlarm = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 115, 1, 1))
ogCustomAlarmTable = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 115, 1, 1, 1))
ogCustomAlarmEntry = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 115, 1, 1, 1, 1))
ogCustomNotification = NotificationType((1, 3, 6, 1, 4, 1, 25049) + (0,33)).setObjects(("OGTRAPv2-MIB", "ogAlarmEventId"), ("OGTRAPv2-MIB", "ogAlarmName"), ("OGTRAPv2-MIB", "ogAlarmCheck"), ("OGTRAPv2-MIB", "ogAlarmInstance"), ("OGTRAPv2-MIB", "ogAlarmTime"), ("OGTRAPv2-MIB", "ogAlarmType"), ("OGTRAPv2-MIB", "ogAlarmSummary"), ("OGTRAPv2-MIB", "ogAlarmDevice"), ("OGTRAPv2-MIB", "ogAlarmUser"), ("OGTRAPv2-MIB", "ogAlarmTriggerValue"), ("OGTRAPv2-MIB", "ogAlarmCurrentValue"), ("OGTRAPv2-MIB", "ogAlarmPreviousValue"), ("OGTRAPv2-MIB", "ogAlarmState"))
ogCliMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 116, 1))
ogCliEvent = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 116, 1, 1))
ogCliEventTable = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 116, 1, 1, 1))
ogCliEventEntry = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 2, 116, 1, 1, 1, 1))
ogCliUserNotification = NotificationType((1, 3, 6, 1, 4, 1, 25049) + (0,34)).setObjects(("OGTRAPv2-MIB", "ogAlarmEventId"), ("OGTRAPv2-MIB", "ogAlarmName"), ("OGTRAPv2-MIB", "ogAlarmCheck"), ("OGTRAPv2-MIB", "ogAlarmInstance"), ("OGTRAPv2-MIB", "ogAlarmTime"), ("OGTRAPv2-MIB", "ogAlarmType"), ("OGTRAPv2-MIB", "ogAlarmSummary"), ("OGTRAPv2-MIB", "ogAlarmDevice"), ("OGTRAPv2-MIB", "ogAlarmTriggerValue"), ("OGTRAPv2-MIB", "ogAlarmCurrentValue"), ("OGTRAPv2-MIB", "ogAlarmPreviousValue"), ("OGTRAPv2-MIB", "ogAlarmState"))
mibBuilder.exportSymbols("OGTRAPv2-MIB", ogEmdMibObjects=ogEmdMibObjects, ogWifiAlarmTable=ogWifiAlarmTable, ogUpsAlarmEntry=ogUpsAlarmEntry, ogCustomNotification=ogCustomNotification, ogHostMib=ogHostMib, ogNetAlarmEntry=ogNetAlarmEntry, ogAlarm=ogAlarm, ogAlarmState=ogAlarmState, ogUpsInputNotification=ogUpsInputNotification, ogWifiMibObjects=ogWifiMibObjects, ogDialPoolHealthNotification=ogDialPoolHealthNotification, ogEmdMib=ogEmdMib, ogNotification=ogNotification, ogCellMibObjects=ogCellMibObjects, ogEmdAlarmEntry=ogEmdAlarmEntry, ogSerialSignalMib=ogSerialSignalMib, ogAlarmEntry=ogAlarmEntry, ogSerialPatternMibObjects=ogSerialPatternMibObjects, ogSerialPatternAlarm=ogSerialPatternAlarm, ogAlarmPreviousValue=ogAlarmPreviousValue, ogEmdHumidityNotification=ogEmdHumidityNotification, ogWifiApAuthNotification=ogWifiApAuthNotification, ogWebEventEntry=ogWebEventEntry, ogHostUserNotification=ogHostUserNotification, ogCustomMibObjects=ogCustomMibObjects, ogWebUserNotification=ogWebUserNotification, ogUpsBatteryNotification=ogUpsBatteryNotification, ogHostMibObjects=ogHostMibObjects, ogCellApnNotification=ogCellApnNotification, ogRpcInputNotification=ogRpcInputNotification, ogNetInterfaceNotification=ogNetInterfaceNotification, ogAlarmName=ogAlarmName, ogPowerSupplyOutputNotification=ogPowerSupplyOutputNotification, ogSerialSignalAlarmTable=ogSerialSignalAlarmTable, ogDialPoolAlarmTable=ogDialPoolAlarmTable, ogAlarmMib=ogAlarmMib, ogEmdAlarmTable=ogEmdAlarmTable, ogPowerSupplyTempNotification=ogPowerSupplyTempNotification, ogCustomAlarmTable=ogCustomAlarmTable, ogWifiClientSignalNotification=ogWifiClientSignalNotification, ogCliMibObjects=ogCliMibObjects, ogCliUserNotification=ogCliUserNotification, ogPowerSupplyInputNotification=ogPowerSupplyInputNotification, ogSerialUserAlarmTable=ogSerialUserAlarmTable, ogSerialSignalAlarm=ogSerialSignalAlarm, ogAlarmSummary=ogAlarmSummary, ogCellAlarmEntry=ogCellAlarmEntry, ogCellMib=ogCellMib, ogRpcMibObjects=ogRpcMibObjects, ogUpsNotification=ogUpsNotification, ogWifiMib=ogWifiMib, ogPowerSupplyMibObjects=ogPowerSupplyMibObjects, ogRpcOutletNotification=ogRpcOutletNotification, ogWebMib=ogWebMib, ogSerialUserAlarmEntry=ogSerialUserAlarmEntry, ogWifiAlarmEntry=ogWifiAlarmEntry, ogSerialSignalNotification=ogSerialSignalNotification, ogAlarmInstance=ogAlarmInstance, ogCellAlarmTable=ogCellAlarmTable, ogWebEventTable=ogWebEventTable, ogPowerSupplyAlarmTable=ogPowerSupplyAlarmTable, ogCellMessageNotification=ogCellMessageNotification, ogCliMib=ogCliMib, ogUpsAlarm=ogUpsAlarm, ogAlarmEventId=ogAlarmEventId, ogSerialUserMibObjects=ogSerialUserMibObjects, ogNetMib=ogNetMib, ogCustomAlarm=ogCustomAlarm, ogCustomAlarmEntry=ogCustomAlarmEntry, ogAlarmTable=ogAlarmTable, opengear=opengear, ogCellDataNotification=ogCellDataNotification, ogNetAlarmTable=ogNetAlarmTable, ogCellNetworkNotification=ogCellNetworkNotification, ogCellAlarm=ogCellAlarm, ogAlarmType=ogAlarmType, ogAlarmIndex=ogAlarmIndex, ogCliEventEntry=ogCliEventEntry, ogPowerSupplyMib=ogPowerSupplyMib, ogAlarmCheck=ogAlarmCheck, ogAlarmMibObjects=ogAlarmMibObjects, ogEmdDioNotification=ogEmdDioNotification, ogCliEventTable=ogCliEventTable, ogUpsMibObjects=ogUpsMibObjects, ogSerialUserAlarm=ogSerialUserAlarm, ogSerialPatternAlarmTable=ogSerialPatternAlarmTable, ogSerialSignalAlarmEntry=ogSerialSignalAlarmEntry, ogEmdAlarm=ogEmdAlarm, ogDialPoolAlarm=ogDialPoolAlarm, ogAlarmDevice=ogAlarmDevice, ogHostEventEntry=ogHostEventEntry, ogWifiApAssociationNotification=ogWifiApAssociationNotification, ogUpsOutputNotification=ogUpsOutputNotification, ogAlarmCurrentValue=ogAlarmCurrentValue, ogCellSignalNotification=ogCellSignalNotification, ogCustomMib=ogCustomMib, ogPowerSupplyAlarm=ogPowerSupplyAlarm, ogAlarmUser=ogAlarmUser, ogHostServiceNotification=ogHostServiceNotification, ogSerialUserNotification=ogSerialUserNotification, ogUpsMib=ogUpsMib, ogSerialPatternMib=ogSerialPatternMib, ogSerialUserMib=ogSerialUserMib, ogPowerSupplyAlarmEntry=ogPowerSupplyAlarmEntry, ogDialPoolMib=ogDialPoolMib, ogRpcAlarmEntry=ogRpcAlarmEntry, ogRpcAlarmTable=ogRpcAlarmTable, ogRpcMib=ogRpcMib, ogWifiAlarm=ogWifiAlarm, ogWifiClientConnectNotification=ogWifiClientConnectNotification, ogSerialPatternAlarmEntry=ogSerialPatternAlarmEntry, ogDialPoolMibObjects=ogDialPoolMibObjects, ogHostEventTable=ogHostEventTable, ogSerialPatternNotification=ogSerialPatternNotification, ogHostPingNotification=ogHostPingNotification, ogAlarmTriggerValue=ogAlarmTriggerValue, ogHostEvent=ogHostEvent, ogUpsAlarmTable=ogUpsAlarmTable, ogNetMibObjects=ogNetMibObjects, ogNetAlarm=ogNetAlarm, ogEmdTemperatureNotification=ogEmdTemperatureNotification, ogSerialSignalMibObjects=ogSerialSignalMibObjects, ogDialPoolAlarmEntry=ogDialPoolAlarmEntry, ogRpcAlarm=ogRpcAlarm, ogLegacyMgmt=ogLegacyMgmt, ogRpcOutputNotification=ogRpcOutputNotification, ogWebMibObjects=ogWebMibObjects, ogWebEvent=ogWebEvent, ogAlarmTime=ogAlarmTime, ogCliEvent=ogCliEvent, ogCellTowerNotification=ogCellTowerNotification)
