#
# PySNMP MIB module SENSATRONICS-ITTM (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/sensatronics/SENSATRONICS-ITTM
# Produced by pysmi-1.1.8 at Fri Jan  7 16:37:45 2022
# On host fv-az36-988 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
envMonitors, = mibBuilder.importSymbols("SENSATRONICS-SMI", "envMonitors")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, ModuleIdentity, Integer32, Gauge32, TimeTicks, MibIdentifier, Counter64, iso, Bits, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, ObjectIdentity, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "ModuleIdentity", "Integer32", "Gauge32", "TimeTicks", "MibIdentifier", "Counter64", "iso", "Bits", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "ObjectIdentity", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
productITTM = ModuleIdentity((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1))
productITTM.setRevisions(('2004-02-23 09:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: productITTM.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: productITTM.setLastUpdated('200402230900Z')
if mibBuilder.loadTexts: productITTM.setOrganization('Sensatronics LLC')
if mibBuilder.loadTexts: productITTM.setContactInfo('Sensatronics LLC\n          Postal: 20A Dunklee Road\n                  Bow, NH 03304\n                  USA\n          Tel: +1 603 224 0617\n          E-mail: dthompson@sensatronics.com')
if mibBuilder.loadTexts: productITTM.setDescription('Description of ITTM code.')
unitInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 1))
configData = MibIdentifier((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 2))
sensorInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3))
unitName = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(32, 32)).setFixedLength(32)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: unitName.setStatus('current')
if mibBuilder.loadTexts: unitName.setDescription('A user-definable unit name for the module being managed.')
unitModel = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(5, 5)).setFixedLength(5)).setMaxAccess("readonly")
if mibBuilder.loadTexts: unitModel.setStatus('current')
if mibBuilder.loadTexts: unitModel.setDescription('The model number of the module being managed.')
unitManufacturer = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(12, 12)).setFixedLength(12)).setMaxAccess("readonly")
if mibBuilder.loadTexts: unitManufacturer.setStatus('current')
if mibBuilder.loadTexts: unitManufacturer.setDescription('Company name of unit producer.')
unitWeb = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(28, 28)).setFixedLength(28)).setMaxAccess("readonly")
if mibBuilder.loadTexts: unitWeb.setStatus('current')
if mibBuilder.loadTexts: unitWeb.setDescription('Website of manufacturer')
unitFirmware = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(5, 5)).setFixedLength(5)).setMaxAccess("readonly")
if mibBuilder.loadTexts: unitFirmware.setStatus('current')
if mibBuilder.loadTexts: unitFirmware.setDescription('Firmware revision of unit.')
unitFWReleaseDate = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(18, 18)).setFixedLength(18)).setMaxAccess("readonly")
if mibBuilder.loadTexts: unitFWReleaseDate.setStatus('current')
if mibBuilder.loadTexts: unitFWReleaseDate.setDescription('Release date of unit firmware.')
unitSerial = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(32, 32)).setFixedLength(32)).setMaxAccess("readonly")
if mibBuilder.loadTexts: unitSerial.setStatus('current')
if mibBuilder.loadTexts: unitSerial.setDescription('Serial number of unit being managed.')
unitConfig = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: unitConfig.setStatus('current')
if mibBuilder.loadTexts: unitConfig.setDescription('In-house configuration MIB - do not use.')
netInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 2, 1))
trapConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 2, 2))
measurementSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 2, 3))
netMode = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: netMode.setStatus('current')
if mibBuilder.loadTexts: netMode.setDescription('1 if the unit is self-configuring via DHCP, 0 if static IP assigned.')
netIP = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readonly")
if mibBuilder.loadTexts: netIP.setStatus('current')
if mibBuilder.loadTexts: netIP.setDescription('IP address of unit being managed.')
netNM = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readonly")
if mibBuilder.loadTexts: netNM.setStatus('current')
if mibBuilder.loadTexts: netNM.setDescription('Netmask of unit being managed.')
netGW = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 2, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readonly")
if mibBuilder.loadTexts: netGW.setStatus('current')
if mibBuilder.loadTexts: netGW.setDescription('Gateway of unit being managed.')
netHTTPPort = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: netHTTPPort.setStatus('current')
if mibBuilder.loadTexts: netHTTPPort.setDescription('Port the unit webserver listens on')
managerConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 2, 2, 1))
unitMode = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 2, 3, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: unitMode.setStatus('current')
if mibBuilder.loadTexts: unitMode.setDescription('Set to 0 for Celsius units in probe data, 1 for Fahrenheit, other values disallowed.')
managerIP = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 2, 2, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: managerIP.setStatus('current')
if mibBuilder.loadTexts: managerIP.setDescription('IP of trap manager.')
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
if mibBuilder.loadTexts: sensor1Name.setDescription('Name of sensor 1 - User configurable, 16 characters')
sensor1DataStr = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(5, 5)).setFixedLength(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensor1DataStr.setStatus('current')
if mibBuilder.loadTexts: sensor1DataStr.setDescription('Data from sensor 1, string format, to 1 decimal place')
sensor1DataInt = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-100, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensor1DataInt.setStatus('current')
if mibBuilder.loadTexts: sensor1DataInt.setDescription('Data from sensor 1, integer format, no decimal places')
sensor2Name = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 2, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensor2Name.setStatus('current')
if mibBuilder.loadTexts: sensor2Name.setDescription('Name of sensor 2 - User configurable, 16 characters')
sensor2DataStr = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 2, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(5, 5)).setFixedLength(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensor2DataStr.setStatus('current')
if mibBuilder.loadTexts: sensor2DataStr.setDescription('Data from sensor 2, string format, to 1 decimal place')
sensor2DataInt = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 2, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-100, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensor2DataInt.setStatus('current')
if mibBuilder.loadTexts: sensor2DataInt.setDescription('Data from sensor 2, integer format, no decimal places')
sensor3Name = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 3, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensor3Name.setStatus('current')
if mibBuilder.loadTexts: sensor3Name.setDescription('Name of sensor 3 - User configurable, 16 characters')
sensor3DataStr = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 3, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(5, 5)).setFixedLength(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensor3DataStr.setStatus('current')
if mibBuilder.loadTexts: sensor3DataStr.setDescription('Data from sensor 3, string format, to 1 decimal place')
sensor3DataInt = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 3, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-100, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensor3DataInt.setStatus('current')
if mibBuilder.loadTexts: sensor3DataInt.setDescription('Data from sensor 3, integer format, no decimal places')
sensor4Name = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 4, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensor4Name.setStatus('current')
if mibBuilder.loadTexts: sensor4Name.setDescription('Name of sensor 4 - User configurable, 16 characters')
sensor4DataStr = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 4, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(5, 5)).setFixedLength(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensor4DataStr.setStatus('current')
if mibBuilder.loadTexts: sensor4DataStr.setDescription('Data from sensor 4, string format, to 1 decimal place')
sensor4DataInt = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 4, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-100, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensor4DataInt.setStatus('current')
if mibBuilder.loadTexts: sensor4DataInt.setDescription('Data from sensor 4, integer format, no decimal places')
sensor5Name = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 5, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensor5Name.setStatus('current')
if mibBuilder.loadTexts: sensor5Name.setDescription('Name of sensor 5 - User configurable, 16 characters')
sensor5DataStr = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 5, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(5, 5)).setFixedLength(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensor5DataStr.setStatus('current')
if mibBuilder.loadTexts: sensor5DataStr.setDescription('Data from sensor 5, string format, to 1 decimal place')
sensor5DataInt = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 5, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-100, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensor5DataInt.setStatus('current')
if mibBuilder.loadTexts: sensor5DataInt.setDescription('Data from sensor 5, integer format, no decimal places')
sensor6Name = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 6, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensor6Name.setStatus('current')
if mibBuilder.loadTexts: sensor6Name.setDescription('Name of sensor 6 - User configurable, 16 characters')
sensor6DataStr = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 6, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(5, 5)).setFixedLength(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensor6DataStr.setStatus('current')
if mibBuilder.loadTexts: sensor6DataStr.setDescription('Data from sensor 6, string format, to 1 decimal place')
sensor6DataInt = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 6, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-100, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensor6DataInt.setStatus('current')
if mibBuilder.loadTexts: sensor6DataInt.setDescription('Data from sensor 6, integer format, no decimal places')
sensor7Name = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 7, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensor7Name.setStatus('current')
if mibBuilder.loadTexts: sensor7Name.setDescription('Name of sensor 7 - User configurable, 16 characters')
sensor7DataStr = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 7, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(5, 5)).setFixedLength(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensor7DataStr.setStatus('current')
if mibBuilder.loadTexts: sensor7DataStr.setDescription('Data from sensor 7, string format, to 1 decimal place')
sensor7DataInt = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 7, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-100, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensor7DataInt.setStatus('current')
if mibBuilder.loadTexts: sensor7DataInt.setDescription('Data from sensor 7, integer format, no decimal places')
sensor8Name = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 8, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensor8Name.setStatus('current')
if mibBuilder.loadTexts: sensor8Name.setDescription('Name of sensor 8 - User configurable, 16 characters')
sensor8DataStr = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 8, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(5, 5)).setFixedLength(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensor8DataStr.setStatus('current')
if mibBuilder.loadTexts: sensor8DataStr.setDescription('Data from sensor 8, string format, to 1 decimal place')
sensor8DataInt = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 8, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-100, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensor8DataInt.setStatus('current')
if mibBuilder.loadTexts: sensor8DataInt.setDescription('Data from sensor 8, integer format, no decimal places')
sensor9Name = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 9, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensor9Name.setStatus('current')
if mibBuilder.loadTexts: sensor9Name.setDescription('Name of sensor 9 - User configurable, 16 characters')
sensor9DataStr = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 9, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(5, 5)).setFixedLength(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensor9DataStr.setStatus('current')
if mibBuilder.loadTexts: sensor9DataStr.setDescription('Data from sensor 9, string format, to 1 decimal place')
sensor9DataInt = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 9, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-100, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensor9DataInt.setStatus('current')
if mibBuilder.loadTexts: sensor9DataInt.setDescription('Data from sensor 9, integer format, no decimal places')
sensor10Name = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 10, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensor10Name.setStatus('current')
if mibBuilder.loadTexts: sensor10Name.setDescription('Name of sensor 10 - User configurable, 16 characters')
sensor10DataStr = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 10, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(5, 5)).setFixedLength(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensor10DataStr.setStatus('current')
if mibBuilder.loadTexts: sensor10DataStr.setDescription('Data from sensor 10, string format, to 1 decimal place')
sensor10DataInt = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 10, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-100, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensor10DataInt.setStatus('current')
if mibBuilder.loadTexts: sensor10DataInt.setDescription('Data from sensor 10, integer format, no decimal places')
sensor11Name = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 11, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensor11Name.setStatus('current')
if mibBuilder.loadTexts: sensor11Name.setDescription('Name of sensor 11 - User configurable, 16 characters')
sensor11DataStr = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 11, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(5, 5)).setFixedLength(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensor11DataStr.setStatus('current')
if mibBuilder.loadTexts: sensor11DataStr.setDescription('Data from sensor 11, string format, to 1 decimal place')
sensor11DataInt = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 11, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-100, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensor11DataInt.setStatus('current')
if mibBuilder.loadTexts: sensor11DataInt.setDescription('Data from sensor 11, integer format, no decimal places')
sensor12Name = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 12, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensor12Name.setStatus('current')
if mibBuilder.loadTexts: sensor12Name.setDescription('Name of sensor 12 - User configurable, 16 characters')
sensor12DataStr = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 12, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(5, 5)).setFixedLength(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensor12DataStr.setStatus('current')
if mibBuilder.loadTexts: sensor12DataStr.setDescription('Data from sensor 12, string format, to 1 decimal place')
sensor12DataInt = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 12, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-100, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensor12DataInt.setStatus('current')
if mibBuilder.loadTexts: sensor12DataInt.setDescription('Data from sensor 12, integer format, no decimal places')
sensor13Name = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 13, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensor13Name.setStatus('current')
if mibBuilder.loadTexts: sensor13Name.setDescription('Name of sensor 13 - User configurable, 16 characters')
sensor13DataStr = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 13, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(5, 5)).setFixedLength(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensor13DataStr.setStatus('current')
if mibBuilder.loadTexts: sensor13DataStr.setDescription('Data from sensor 13, string format, to 1 decimal place')
sensor13DataInt = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 13, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-100, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensor13DataInt.setStatus('current')
if mibBuilder.loadTexts: sensor13DataInt.setDescription('Data from sensor 13, integer format, no decimal places')
sensor14Name = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 14, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensor14Name.setStatus('current')
if mibBuilder.loadTexts: sensor14Name.setDescription('Name of sensor 14 - User configurable, 16 characters')
sensor14DataStr = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 14, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(5, 5)).setFixedLength(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensor14DataStr.setStatus('current')
if mibBuilder.loadTexts: sensor14DataStr.setDescription('Data from sensor 14, string format, to 1 decimal place')
sensor14DataInt = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 14, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-100, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensor14DataInt.setStatus('current')
if mibBuilder.loadTexts: sensor14DataInt.setDescription('Data from sensor 14, integer format, no decimal places')
sensor15Name = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 15, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensor15Name.setStatus('current')
if mibBuilder.loadTexts: sensor15Name.setDescription('Name of sensor 15 - User configurable, 16 characters')
sensor15DataStr = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 15, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(5, 5)).setFixedLength(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensor15DataStr.setStatus('current')
if mibBuilder.loadTexts: sensor15DataStr.setDescription('Data from sensor 15, string format, to 1 decimal place')
sensor15DataInt = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 15, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-100, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensor15DataInt.setStatus('current')
if mibBuilder.loadTexts: sensor15DataInt.setDescription('Data from sensor 15, integer format, no decimal places')
sensor16Name = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 16, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensor16Name.setStatus('current')
if mibBuilder.loadTexts: sensor16Name.setDescription('Name of sensor 16 - User configurable, 16 characters')
sensor16DataStr = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 16, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(5, 5)).setFixedLength(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensor16DataStr.setStatus('current')
if mibBuilder.loadTexts: sensor16DataStr.setDescription('Data from sensor 16, string format, to 1 decimal place')
sensor16DataInt = MibScalar((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 16, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-100, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensor16DataInt.setStatus('current')
if mibBuilder.loadTexts: sensor16DataInt.setDescription('Data from sensor 16, integer format, no decimal places')
mibBuilder.exportSymbols("SENSATRONICS-ITTM", sensor10=sensor10, sensor5DataInt=sensor5DataInt, sensor9Name=sensor9Name, sensor12DataInt=sensor12DataInt, sensor12Name=sensor12Name, sensor4DataStr=sensor4DataStr, sensor13DataInt=sensor13DataInt, sensor16DataStr=sensor16DataStr, sensor11Name=sensor11Name, sensor15Name=sensor15Name, sensor8Name=sensor8Name, unitWeb=unitWeb, sensor2DataStr=sensor2DataStr, sensor14DataStr=sensor14DataStr, sensor6Name=sensor6Name, sensorInfo=sensorInfo, unitFWReleaseDate=unitFWReleaseDate, sensor13Name=sensor13Name, sensor8=sensor8, unitName=unitName, managerIP=managerIP, sensor14DataInt=sensor14DataInt, sensor1DataStr=sensor1DataStr, sensor11DataInt=sensor11DataInt, trapConfig=trapConfig, sensor7Name=sensor7Name, sensor9=sensor9, unitModel=unitModel, netIP=netIP, sensor8DataStr=sensor8DataStr, sensor1Name=sensor1Name, sensor2DataInt=sensor2DataInt, sensor15DataStr=sensor15DataStr, sensor15=sensor15, unitConfig=unitConfig, PYSNMP_MODULE_ID=productITTM, netInfo=netInfo, unitSerial=unitSerial, sensor5DataStr=sensor5DataStr, unitManufacturer=unitManufacturer, sensor4DataInt=sensor4DataInt, netGW=netGW, sensor6=sensor6, netHTTPPort=netHTTPPort, sensor3DataStr=sensor3DataStr, measurementSystem=measurementSystem, sensor1DataInt=sensor1DataInt, sensor11DataStr=sensor11DataStr, sensor16Name=sensor16Name, sensor6DataInt=sensor6DataInt, netMode=netMode, sensor3DataInt=sensor3DataInt, sensor8DataInt=sensor8DataInt, sensor13DataStr=sensor13DataStr, sensor15DataInt=sensor15DataInt, sensor13=sensor13, sensor14Name=sensor14Name, sensor3Name=sensor3Name, sensor12DataStr=sensor12DataStr, sensor9DataStr=sensor9DataStr, sensor10DataStr=sensor10DataStr, sensor16=sensor16, sensor7DataStr=sensor7DataStr, sensor7DataInt=sensor7DataInt, sensor12=sensor12, configData=configData, sensor4Name=sensor4Name, sensor2=sensor2, sensor10Name=sensor10Name, sensor14=sensor14, productITTM=productITTM, sensor4=sensor4, sensor16DataInt=sensor16DataInt, sensor5Name=sensor5Name, unitInfo=unitInfo, sensor7=sensor7, sensor6DataStr=sensor6DataStr, sensor5=sensor5, sensor10DataInt=sensor10DataInt, unitFirmware=unitFirmware, sensor3=sensor3, sensor1=sensor1, netNM=netNM, sensor9DataInt=sensor9DataInt, sensor11=sensor11, sensor2Name=sensor2Name, managerConfig=managerConfig, unitMode=unitMode)
