#
# PySNMP MIB module SENSATRONICS-ITTM (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/sensatronics/SENSATRONICS-ITTM
# Produced by pysmi-1.1.8 at Sat Jan 15 18:19:08 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
envMonitors, = mibBuilder.importSymbols("SENSATRONICS-SMI", "envMonitors")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, Integer32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Gauge32, MibIdentifier, iso, Unsigned32, ModuleIdentity, IpAddress, Counter64, NotificationType, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Integer32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Gauge32", "MibIdentifier", "iso", "Unsigned32", "ModuleIdentity", "IpAddress", "Counter64", "NotificationType", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
productITTM = ModuleIdentity((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1))
productITTM.setRevisions(('2004-02-23 09:00',))
if mibBuilder.loadTexts: productITTM.setLastUpdated('200402230900Z')
if mibBuilder.loadTexts: productITTM.setOrganization('Sensatronics LLC')
unitInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 1))
configData = MibIdentifier((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 2))
sensorInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3))
unitName = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(32, 32)).setFixedLength(32)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: unitName.setStatus('current')
unitModel = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(5, 5)).setFixedLength(5)).setMaxAccess("readonly")
if mibBuilder.loadTexts: unitModel.setStatus('current')
unitManufacturer = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(12, 12)).setFixedLength(12)).setMaxAccess("readonly")
if mibBuilder.loadTexts: unitManufacturer.setStatus('current')
unitWeb = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(28, 28)).setFixedLength(28)).setMaxAccess("readonly")
if mibBuilder.loadTexts: unitWeb.setStatus('current')
unitFirmware = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(5, 5)).setFixedLength(5)).setMaxAccess("readonly")
if mibBuilder.loadTexts: unitFirmware.setStatus('current')
unitFWReleaseDate = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(18, 18)).setFixedLength(18)).setMaxAccess("readonly")
if mibBuilder.loadTexts: unitFWReleaseDate.setStatus('current')
unitSerial = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(32, 32)).setFixedLength(32)).setMaxAccess("readonly")
if mibBuilder.loadTexts: unitSerial.setStatus('current')
unitConfig = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: unitConfig.setStatus('current')
netInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 2, 1))
trapConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 2, 2))
measurementSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 2, 3))
netMode = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: netMode.setStatus('current')
netIP = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readonly")
if mibBuilder.loadTexts: netIP.setStatus('current')
netNM = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readonly")
if mibBuilder.loadTexts: netNM.setStatus('current')
netGW = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 2, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readonly")
if mibBuilder.loadTexts: netGW.setStatus('current')
netHTTPPort = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: netHTTPPort.setStatus('current')
managerConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 2, 2, 1))
unitMode = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 2, 3, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: unitMode.setStatus('current')
managerIP = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 2, 2, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: managerIP.setStatus('current')
sensor1 = MibIdentifier((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 1))
sensor2 = MibIdentifier((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 2))
sensor3 = MibIdentifier((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 3))
sensor4 = MibIdentifier((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 4))
sensor5 = MibIdentifier((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 5))
sensor6 = MibIdentifier((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 6))
sensor7 = MibIdentifier((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 7))
sensor8 = MibIdentifier((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 8))
sensor9 = MibIdentifier((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 9))
sensor10 = MibIdentifier((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 10))
sensor11 = MibIdentifier((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 11))
sensor12 = MibIdentifier((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 12))
sensor13 = MibIdentifier((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 13))
sensor14 = MibIdentifier((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 14))
sensor15 = MibIdentifier((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 15))
sensor16 = MibIdentifier((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 16))
sensor1Name = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensor1Name.setStatus('current')
sensor1DataStr = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(5, 5)).setFixedLength(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensor1DataStr.setStatus('current')
sensor1DataInt = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-100, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensor1DataInt.setStatus('current')
sensor2Name = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 2, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensor2Name.setStatus('current')
sensor2DataStr = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 2, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(5, 5)).setFixedLength(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensor2DataStr.setStatus('current')
sensor2DataInt = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 2, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-100, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensor2DataInt.setStatus('current')
sensor3Name = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 3, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensor3Name.setStatus('current')
sensor3DataStr = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 3, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(5, 5)).setFixedLength(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensor3DataStr.setStatus('current')
sensor3DataInt = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 3, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-100, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensor3DataInt.setStatus('current')
sensor4Name = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 4, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensor4Name.setStatus('current')
sensor4DataStr = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 4, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(5, 5)).setFixedLength(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensor4DataStr.setStatus('current')
sensor4DataInt = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 4, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-100, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensor4DataInt.setStatus('current')
sensor5Name = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 5, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensor5Name.setStatus('current')
sensor5DataStr = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 5, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(5, 5)).setFixedLength(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensor5DataStr.setStatus('current')
sensor5DataInt = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 5, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-100, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensor5DataInt.setStatus('current')
sensor6Name = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 6, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensor6Name.setStatus('current')
sensor6DataStr = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 6, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(5, 5)).setFixedLength(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensor6DataStr.setStatus('current')
sensor6DataInt = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 6, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-100, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensor6DataInt.setStatus('current')
sensor7Name = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 7, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensor7Name.setStatus('current')
sensor7DataStr = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 7, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(5, 5)).setFixedLength(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensor7DataStr.setStatus('current')
sensor7DataInt = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 7, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-100, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensor7DataInt.setStatus('current')
sensor8Name = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 8, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensor8Name.setStatus('current')
sensor8DataStr = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 8, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(5, 5)).setFixedLength(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensor8DataStr.setStatus('current')
sensor8DataInt = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 8, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-100, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensor8DataInt.setStatus('current')
sensor9Name = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 9, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensor9Name.setStatus('current')
sensor9DataStr = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 9, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(5, 5)).setFixedLength(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensor9DataStr.setStatus('current')
sensor9DataInt = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 9, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-100, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensor9DataInt.setStatus('current')
sensor10Name = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 10, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensor10Name.setStatus('current')
sensor10DataStr = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 10, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(5, 5)).setFixedLength(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensor10DataStr.setStatus('current')
sensor10DataInt = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 10, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-100, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensor10DataInt.setStatus('current')
sensor11Name = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 11, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensor11Name.setStatus('current')
sensor11DataStr = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 11, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(5, 5)).setFixedLength(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensor11DataStr.setStatus('current')
sensor11DataInt = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 11, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-100, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensor11DataInt.setStatus('current')
sensor12Name = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 12, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensor12Name.setStatus('current')
sensor12DataStr = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 12, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(5, 5)).setFixedLength(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensor12DataStr.setStatus('current')
sensor12DataInt = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 12, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-100, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensor12DataInt.setStatus('current')
sensor13Name = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 13, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensor13Name.setStatus('current')
sensor13DataStr = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 13, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(5, 5)).setFixedLength(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensor13DataStr.setStatus('current')
sensor13DataInt = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 13, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-100, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensor13DataInt.setStatus('current')
sensor14Name = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 14, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensor14Name.setStatus('current')
sensor14DataStr = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 14, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(5, 5)).setFixedLength(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensor14DataStr.setStatus('current')
sensor14DataInt = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 14, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-100, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensor14DataInt.setStatus('current')
sensor15Name = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 15, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensor15Name.setStatus('current')
sensor15DataStr = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 15, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(5, 5)).setFixedLength(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensor15DataStr.setStatus('current')
sensor15DataInt = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 15, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-100, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensor15DataInt.setStatus('current')
sensor16Name = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 16, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensor16Name.setStatus('current')
sensor16DataStr = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 16, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(5, 5)).setFixedLength(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensor16DataStr.setStatus('current')
sensor16DataInt = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 16, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-100, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensor16DataInt.setStatus('current')
mibBuilder.exportSymbols("SENSATRONICS-ITTM", sensor3Name=sensor3Name, unitInfo=unitInfo, sensor14=sensor14, sensor15Name=sensor15Name, sensor15DataInt=sensor15DataInt, unitSerial=unitSerial, sensor1=sensor1, sensor12DataStr=sensor12DataStr, sensor4DataStr=sensor4DataStr, sensor11Name=sensor11Name, unitModel=unitModel, unitMode=unitMode, sensor4=sensor4, sensor14DataStr=sensor14DataStr, netHTTPPort=netHTTPPort, sensor13DataInt=sensor13DataInt, sensor16DataStr=sensor16DataStr, sensor11=sensor11, sensor5DataStr=sensor5DataStr, sensor16=sensor16, netMode=netMode, unitManufacturer=unitManufacturer, trapConfig=trapConfig, netInfo=netInfo, sensor7=sensor7, netIP=netIP, sensor2DataStr=sensor2DataStr, sensor2DataInt=sensor2DataInt, measurementSystem=measurementSystem, sensor10DataInt=sensor10DataInt, sensor15DataStr=sensor15DataStr, unitFWReleaseDate=unitFWReleaseDate, sensor11DataStr=sensor11DataStr, sensor12=sensor12, sensor1DataStr=sensor1DataStr, productITTM=productITTM, sensor16Name=sensor16Name, sensor1Name=sensor1Name, sensor8=sensor8, sensor15=sensor15, sensorInfo=sensorInfo, sensor9DataInt=sensor9DataInt, sensor5Name=sensor5Name, sensor10=sensor10, sensor3=sensor3, sensor9Name=sensor9Name, unitConfig=unitConfig, sensor14DataInt=sensor14DataInt, sensor6DataInt=sensor6DataInt, sensor8Name=sensor8Name, sensor9=sensor9, sensor2=sensor2, unitWeb=unitWeb, sensor12DataInt=sensor12DataInt, sensor5=sensor5, sensor3DataInt=sensor3DataInt, sensor9DataStr=sensor9DataStr, sensor10Name=sensor10Name, sensor7DataStr=sensor7DataStr, sensor5DataInt=sensor5DataInt, sensor14Name=sensor14Name, configData=configData, sensor7Name=sensor7Name, sensor4DataInt=sensor4DataInt, sensor13=sensor13, managerIP=managerIP, sensor4Name=sensor4Name, sensor6DataStr=sensor6DataStr, unitName=unitName, sensor3DataStr=sensor3DataStr, sensor2Name=sensor2Name, netGW=netGW, sensor10DataStr=sensor10DataStr, sensor7DataInt=sensor7DataInt, sensor11DataInt=sensor11DataInt, PYSNMP_MODULE_ID=productITTM, managerConfig=managerConfig, sensor6Name=sensor6Name, sensor6=sensor6, sensor1DataInt=sensor1DataInt, sensor16DataInt=sensor16DataInt, netNM=netNM, sensor8DataStr=sensor8DataStr, sensor13Name=sensor13Name, unitFirmware=unitFirmware, sensor8DataInt=sensor8DataInt, sensor12Name=sensor12Name, sensor13DataStr=sensor13DataStr)
