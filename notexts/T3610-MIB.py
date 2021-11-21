#
# PySNMP MIB module T3610-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/comet/T3610-MIB
# Produced by pysmi-1.1.3 at Sun Nov 21 00:46:48 2021
# On host fv-az39-63 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, Unsigned32, Counter32, Gauge32, TimeTicks, NotificationType, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, enterprises, Counter64, ModuleIdentity, ObjectIdentity, NotificationType, MibIdentifier, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Unsigned32", "Counter32", "Gauge32", "TimeTicks", "NotificationType", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "enterprises", "Counter64", "ModuleIdentity", "ObjectIdentity", "NotificationType", "MibIdentifier", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class DisplayString(OctetString):
    pass

comet = MibIdentifier((1, 3, 6, 1, 4, 1, 22626))
products = MibIdentifier((1, 3, 6, 1, 4, 1, 22626, 1))
t3610 = MibIdentifier((1, 3, 6, 1, 4, 1, 22626, 1, 2))
values = MibIdentifier((1, 3, 6, 1, 4, 1, 22626, 1, 2, 1))
pysmi_global = MibIdentifier((1, 3, 6, 1, 4, 1, 22626, 1, 2, 2)).setLabel("global")
valuesInt = MibIdentifier((1, 3, 6, 1, 4, 1, 22626, 1, 2, 3))
settings = MibIdentifier((1, 3, 6, 1, 4, 1, 22626, 1, 2, 4))
traps = MibIdentifier((1, 3, 6, 1, 4, 1, 22626, 1, 2, 5))
tables = MibIdentifier((1, 3, 6, 1, 4, 1, 22626, 1, 2, 6))
temp = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: temp.setStatus('mandatory')
hum = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hum.setStatus('mandatory')
compVal = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: compVal.setStatus('mandatory')
tempAlarm = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tempAlarm.setStatus('mandatory')
humAlarm = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: humAlarm.setStatus('mandatory')
compValAlarm = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: compValAlarm.setStatus('mandatory')
tempUnit = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tempUnit.setStatus('mandatory')
humUnit = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 1, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: humUnit.setStatus('mandatory')
compValUnit = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 1, 11), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: compValUnit.setStatus('mandatory')
tempMin = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 1, 13), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tempMin.setStatus('mandatory')
humMin = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 1, 14), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: humMin.setStatus('mandatory')
compValMin = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 1, 15), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: compValMin.setStatus('mandatory')
tempMax = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 1, 17), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tempMax.setStatus('mandatory')
humMax = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 1, 18), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: humMax.setStatus('mandatory')
compValMax = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 1, 19), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: compValMax.setStatus('mandatory')
sensorName = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 2, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 68))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensorName.setStatus('mandatory')
serialNumber = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 2, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: serialNumber.setStatus('mandatory')
deviceType = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 2, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65534))).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceType.setStatus('mandatory')
tempInt = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 3, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-5000, 20000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tempInt.setStatus('mandatory')
humInt = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 3, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-5000, 20000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: humInt.setStatus('mandatory')
compValInt = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 3, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-5000, 20000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: compValInt.setStatus('mandatory')
tempAlarmInt = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 3, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tempAlarmInt.setStatus('mandatory')
humAlarmInt = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 3, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: humAlarmInt.setStatus('mandatory')
compValAlarmInt = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 3, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: compValAlarmInt.setStatus('mandatory')
tempLowInt = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-5000, 20000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tempLowInt.setStatus('mandatory')
tempHighInt = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-5000, 20000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tempHighInt.setStatus('mandatory')
humLowInt = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-5000, 20000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: humLowInt.setStatus('mandatory')
humHighInt = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-5000, 20000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: humHighInt.setStatus('mandatory')
compValLowInt = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-5000, 20000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: compValLowInt.setStatus('mandatory')
compValHighInt = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-5000, 20000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: compValHighInt.setStatus('mandatory')
tempDelayInt = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4500))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tempDelayInt.setStatus('mandatory')
humDelayInt = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4500))).setMaxAccess("readonly")
if mibBuilder.loadTexts: humDelayInt.setStatus('mandatory')
compValDelayInt = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4500))).setMaxAccess("readonly")
if mibBuilder.loadTexts: compValDelayInt.setStatus('mandatory')
tempHystInt = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 10000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tempHystInt.setStatus('mandatory')
humHystInt = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 10000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: humHystInt.setStatus('mandatory')
compValHystInt = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 10000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: compValHystInt.setStatus('mandatory')
messageString = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 5, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: messageString.setStatus('mandatory')
historyTable = MibTable((1, 3, 6, 1, 4, 1, 22626, 1, 2, 6, 1), )
if mibBuilder.loadTexts: historyTable.setStatus('mandatory')
historyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 22626, 1, 2, 6, 1, 1), ).setIndexNames((0, "T3610-MIB", "histTemp"))
if mibBuilder.loadTexts: historyEntry.setStatus('optional')
histTemp = MibTableColumn((1, 3, 6, 1, 4, 1, 22626, 1, 2, 6, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-5000, 20000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: histTemp.setStatus('mandatory')
histHum = MibTableColumn((1, 3, 6, 1, 4, 1, 22626, 1, 2, 6, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-5000, 20000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: histHum.setStatus('mandatory')
histCompVal = MibTableColumn((1, 3, 6, 1, 4, 1, 22626, 1, 2, 6, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-5000, 20000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: histCompVal.setStatus('mandatory')
trapTest = NotificationType((1, 3, 6, 1, 4, 1, 22626) + (0,0)).setObjects(("T3610-MIB", "sensorName"), ("T3610-MIB", "messageString"))
trapNTPError = NotificationType((1, 3, 6, 1, 4, 1, 22626) + (0,1)).setObjects(("T3610-MIB", "sensorName"), ("T3610-MIB", "messageString"))
trapEmailErrLogin = NotificationType((1, 3, 6, 1, 4, 1, 22626) + (0,2)).setObjects(("T3610-MIB", "sensorName"), ("T3610-MIB", "messageString"))
trapEmailErrAuth = NotificationType((1, 3, 6, 1, 4, 1, 22626) + (0,3)).setObjects(("T3610-MIB", "sensorName"), ("T3610-MIB", "messageString"))
trapEmailErrSome = NotificationType((1, 3, 6, 1, 4, 1, 22626) + (0,4)).setObjects(("T3610-MIB", "sensorName"), ("T3610-MIB", "messageString"))
trapEmailErrSocket = NotificationType((1, 3, 6, 1, 4, 1, 22626) + (0,5)).setObjects(("T3610-MIB", "sensorName"), ("T3610-MIB", "messageString"))
trapEmailErrDNS = NotificationType((1, 3, 6, 1, 4, 1, 22626) + (0,6)).setObjects(("T3610-MIB", "sensorName"), ("T3610-MIB", "messageString"))
trapSOAPErrFile = NotificationType((1, 3, 6, 1, 4, 1, 22626) + (0,7)).setObjects(("T3610-MIB", "sensorName"), ("T3610-MIB", "messageString"))
trapSOAPErrDNS = NotificationType((1, 3, 6, 1, 4, 1, 22626) + (0,8)).setObjects(("T3610-MIB", "sensorName"), ("T3610-MIB", "messageString"))
trapSOAPErrSocket = NotificationType((1, 3, 6, 1, 4, 1, 22626) + (0,9)).setObjects(("T3610-MIB", "sensorName"), ("T3610-MIB", "messageString"))
trapSOAPErrDelivery = NotificationType((1, 3, 6, 1, 4, 1, 22626) + (0,10)).setObjects(("T3610-MIB", "sensorName"), ("T3610-MIB", "messageString"))
trapTempHighAlarm = NotificationType((1, 3, 6, 1, 4, 1, 22626) + (0,11)).setObjects(("T3610-MIB", "sensorName"), ("T3610-MIB", "messageString"), ("T3610-MIB", "temp"), ("T3610-MIB", "tempAlarmInt"))
trapHumHighAlarm = NotificationType((1, 3, 6, 1, 4, 1, 22626) + (0,12)).setObjects(("T3610-MIB", "sensorName"), ("T3610-MIB", "messageString"), ("T3610-MIB", "hum"), ("T3610-MIB", "humAlarmInt"))
trapCompValHighAlarm = NotificationType((1, 3, 6, 1, 4, 1, 22626) + (0,13)).setObjects(("T3610-MIB", "sensorName"), ("T3610-MIB", "messageString"), ("T3610-MIB", "compVal"), ("T3610-MIB", "compValAlarmInt"))
trapTempLowAlarm = NotificationType((1, 3, 6, 1, 4, 1, 22626) + (0,21)).setObjects(("T3610-MIB", "sensorName"), ("T3610-MIB", "messageString"), ("T3610-MIB", "temp"), ("T3610-MIB", "tempAlarmInt"))
trapHumLowAlarm = NotificationType((1, 3, 6, 1, 4, 1, 22626) + (0,22)).setObjects(("T3610-MIB", "sensorName"), ("T3610-MIB", "messageString"), ("T3610-MIB", "hum"), ("T3610-MIB", "humAlarmInt"))
trapCompValLowAlarm = NotificationType((1, 3, 6, 1, 4, 1, 22626) + (0,23)).setObjects(("T3610-MIB", "sensorName"), ("T3610-MIB", "messageString"), ("T3610-MIB", "compVal"), ("T3610-MIB", "compValAlarmInt"))
trapTempClrAlarm = NotificationType((1, 3, 6, 1, 4, 1, 22626) + (0,31)).setObjects(("T3610-MIB", "sensorName"), ("T3610-MIB", "messageString"), ("T3610-MIB", "temp"), ("T3610-MIB", "tempAlarmInt"))
trapHumClrAlarm = NotificationType((1, 3, 6, 1, 4, 1, 22626) + (0,32)).setObjects(("T3610-MIB", "sensorName"), ("T3610-MIB", "messageString"), ("T3610-MIB", "hum"), ("T3610-MIB", "humAlarmInt"))
trapCompValClrAlarm = NotificationType((1, 3, 6, 1, 4, 1, 22626) + (0,33)).setObjects(("T3610-MIB", "sensorName"), ("T3610-MIB", "messageString"), ("T3610-MIB", "compVal"), ("T3610-MIB", "compValAlarmInt"))
trapTempError = NotificationType((1, 3, 6, 1, 4, 1, 22626) + (0,41)).setObjects(("T3610-MIB", "sensorName"), ("T3610-MIB", "messageString"), ("T3610-MIB", "temp"), ("T3610-MIB", "tempAlarmInt"))
trapHumError = NotificationType((1, 3, 6, 1, 4, 1, 22626) + (0,42)).setObjects(("T3610-MIB", "sensorName"), ("T3610-MIB", "messageString"), ("T3610-MIB", "hum"), ("T3610-MIB", "humAlarmInt"))
trapCompValError = NotificationType((1, 3, 6, 1, 4, 1, 22626) + (0,43)).setObjects(("T3610-MIB", "sensorName"), ("T3610-MIB", "messageString"), ("T3610-MIB", "compVal"), ("T3610-MIB", "compValAlarmInt"))
mibBuilder.exportSymbols("T3610-MIB", trapTest=trapTest, historyEntry=historyEntry, tables=tables, tempAlarm=tempAlarm, humAlarm=humAlarm, humUnit=humUnit, compValHystInt=compValHystInt, trapSOAPErrDNS=trapSOAPErrDNS, settings=settings, trapCompValError=trapCompValError, tempUnit=tempUnit, messageString=messageString, hum=hum, compVal=compVal, trapHumLowAlarm=trapHumLowAlarm, compValAlarm=compValAlarm, compValInt=compValInt, tempMax=tempMax, trapTempClrAlarm=trapTempClrAlarm, trapTempError=trapTempError, historyTable=historyTable, serialNumber=serialNumber, trapCompValHighAlarm=trapCompValHighAlarm, humInt=humInt, humAlarmInt=humAlarmInt, compValMin=compValMin, trapEmailErrDNS=trapEmailErrDNS, valuesInt=valuesInt, t3610=t3610, compValMax=compValMax, trapSOAPErrFile=trapSOAPErrFile, trapHumError=trapHumError, tempLowInt=tempLowInt, humLowInt=humLowInt, DisplayString=DisplayString, trapSOAPErrSocket=trapSOAPErrSocket, trapNTPError=trapNTPError, trapCompValLowAlarm=trapCompValLowAlarm, trapEmailErrLogin=trapEmailErrLogin, tempMin=tempMin, values=values, tempAlarmInt=tempAlarmInt, pysmi_global=pysmi_global, humMin=humMin, trapHumHighAlarm=trapHumHighAlarm, products=products, tempDelayInt=tempDelayInt, humDelayInt=humDelayInt, trapEmailErrSocket=trapEmailErrSocket, trapTempHighAlarm=trapTempHighAlarm, compValLowInt=compValLowInt, histCompVal=histCompVal, humMax=humMax, traps=traps, trapEmailErrSome=trapEmailErrSome, deviceType=deviceType, tempHystInt=tempHystInt, compValHighInt=compValHighInt, temp=temp, humHystInt=humHystInt, histHum=histHum, trapCompValClrAlarm=trapCompValClrAlarm, trapSOAPErrDelivery=trapSOAPErrDelivery, humHighInt=humHighInt, histTemp=histTemp, compValDelayInt=compValDelayInt, trapTempLowAlarm=trapTempLowAlarm, trapHumClrAlarm=trapHumClrAlarm, tempInt=tempInt, compValUnit=compValUnit, compValAlarmInt=compValAlarmInt, comet=comet, trapEmailErrAuth=trapEmailErrAuth, tempHighInt=tempHighInt, sensorName=sensorName)
