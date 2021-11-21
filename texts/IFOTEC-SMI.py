#
# PySNMP MIB module IFOTEC-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/ifotec/IFOTEC-SMI
# Produced by pysmi-1.1.3 at Sun Nov 21 00:46:30 2021
# On host fv-az39-63 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, ObjectIdentity, iso, NotificationType, Integer32, Bits, Unsigned32, TimeTicks, Counter64, enterprises, Counter32, ModuleIdentity, Gauge32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "ObjectIdentity", "iso", "NotificationType", "Integer32", "Bits", "Unsigned32", "TimeTicks", "Counter64", "enterprises", "Counter32", "ModuleIdentity", "Gauge32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ifotec = ModuleIdentity((1, 3, 6, 1, 4, 1, 21362))
if mibBuilder.loadTexts: ifotec.setLastUpdated('202007280000Z')
if mibBuilder.loadTexts: ifotec.setOrganization('IFOTEC')
if mibBuilder.loadTexts: ifotec.setContactInfo('contact@ifotec.com')
if mibBuilder.loadTexts: ifotec.setDescription('The Structure of Management Information for the\n        IFOTEC enterprise.')
class IfotecDataStatus(TextualConvention, Integer32):
    description = 'Represents the data status.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("noData", 1), ("ok", 2), ("warning", 3), ("warningLowThreshold", 4), ("warningHighThreshold", 5), ("error", 6), ("errorLowThreshold", 7), ("errorHighThreshold", 8), ("errorWrongData", 9), ("errorLowDataOverflow", 10), ("errorHighDataOverflow", 11))

ifotecGeneral = ObjectIdentity((1, 3, 6, 1, 4, 1, 21362, 101))
if mibBuilder.loadTexts: ifotecGeneral.setStatus('current')
if mibBuilder.loadTexts: ifotecGeneral.setDescription('General informations about the IFOTEC product.')
ifotecSystem = ObjectIdentity((1, 3, 6, 1, 4, 1, 21362, 101, 1))
if mibBuilder.loadTexts: ifotecSystem.setStatus('current')
if mibBuilder.loadTexts: ifotecSystem.setDescription('IFOTEC System informations.')
ifoSysProductIndex = MibScalar((1, 3, 6, 1, 4, 1, 21362, 101, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifoSysProductIndex.setStatus('current')
if mibBuilder.loadTexts: ifoSysProductIndex.setDescription('The ifoSysIndex of the product.')
ifoSysTable = MibTable((1, 3, 6, 1, 4, 1, 21362, 101, 1, 2), )
if mibBuilder.loadTexts: ifoSysTable.setStatus('current')
if mibBuilder.loadTexts: ifoSysTable.setDescription('list of systems present.')
ifoSysEntry = MibTableRow((1, 3, 6, 1, 4, 1, 21362, 101, 1, 2, 1), ).setIndexNames((0, "IFOTEC-SMI", "ifoSysIndex"))
if mibBuilder.loadTexts: ifoSysEntry.setStatus('current')
if mibBuilder.loadTexts: ifoSysEntry.setDescription('An entry containing system informations.')
ifoSysIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 21362, 101, 1, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: ifoSysIndex.setStatus('current')
if mibBuilder.loadTexts: ifoSysIndex.setDescription('A unique value, greater than zero, for each product.')
ifoSysRef = MibTableColumn((1, 3, 6, 1, 4, 1, 21362, 101, 1, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifoSysRef.setStatus('current')
if mibBuilder.loadTexts: ifoSysRef.setDescription('Product reference')
ifoSysInfo = MibTableColumn((1, 3, 6, 1, 4, 1, 21362, 101, 1, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifoSysInfo.setStatus('current')
if mibBuilder.loadTexts: ifoSysInfo.setDescription('Product information')
ifoSysFamilly = MibTableColumn((1, 3, 6, 1, 4, 1, 21362, 101, 1, 2, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifoSysFamilly.setStatus('current')
if mibBuilder.loadTexts: ifoSysFamilly.setDescription('Product familly')
ifoSysSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 21362, 101, 1, 2, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifoSysSerialNumber.setStatus('current')
if mibBuilder.loadTexts: ifoSysSerialNumber.setDescription('Serial number')
ifoSysDateCode = MibTableColumn((1, 3, 6, 1, 4, 1, 21362, 101, 1, 2, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifoSysDateCode.setStatus('current')
if mibBuilder.loadTexts: ifoSysDateCode.setDescription('Date code')
ifoSysFirmware = MibTableColumn((1, 3, 6, 1, 4, 1, 21362, 101, 1, 2, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifoSysFirmware.setStatus('current')
if mibBuilder.loadTexts: ifoSysFirmware.setDescription('Firmware version')
ifoSysBootloader = MibTableColumn((1, 3, 6, 1, 4, 1, 21362, 101, 1, 2, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifoSysBootloader.setStatus('current')
if mibBuilder.loadTexts: ifoSysBootloader.setDescription('Bootloader version')
ifoSysDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 21362, 101, 1, 2, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifoSysDescr.setStatus('current')
if mibBuilder.loadTexts: ifoSysDescr.setDescription('Administratively-assigned name (sysName)')
ifoSysLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 21362, 101, 1, 2, 1, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifoSysLocation.setStatus('current')
if mibBuilder.loadTexts: ifoSysLocation.setDescription('Physical location (sysLocation)')
ifoSysContact = MibTableColumn((1, 3, 6, 1, 4, 1, 21362, 101, 1, 2, 1, 11), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifoSysContact.setStatus('current')
if mibBuilder.loadTexts: ifoSysContact.setDescription('Physical location (sysContact)')
ifoSysUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 21362, 101, 1, 2, 1, 12), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifoSysUpTime.setStatus('current')
if mibBuilder.loadTexts: ifoSysUpTime.setDescription('The time (in hundredths of a second) since the \n               network management portion of the system was last \n               re-initialized (sysUpTime).')
ifoSysMibTable = MibTable((1, 3, 6, 1, 4, 1, 21362, 101, 1, 3), )
if mibBuilder.loadTexts: ifoSysMibTable.setStatus('current')
if mibBuilder.loadTexts: ifoSysMibTable.setDescription('list of mibs presents in the system.')
ifoSysMibEntry = MibTableRow((1, 3, 6, 1, 4, 1, 21362, 101, 1, 3, 1), ).setIndexNames((0, "IFOTEC-SMI", "ifoSysORIfoSysIndex"), (0, "IFOTEC-SMI", "ifoSysORIndex"))
if mibBuilder.loadTexts: ifoSysMibEntry.setStatus('current')
if mibBuilder.loadTexts: ifoSysMibEntry.setDescription('An entry containing mib informations.')
ifoSysORIfoSysIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 21362, 101, 1, 3, 1, 1), Integer32())
if mibBuilder.loadTexts: ifoSysORIfoSysIndex.setStatus('current')
if mibBuilder.loadTexts: ifoSysORIfoSysIndex.setDescription('The index value which uniquely identifies the system in ifoSysMibTable. It is the same value used by ifoSysIndex.')
ifoSysORIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 21362, 101, 1, 3, 1, 2), Integer32())
if mibBuilder.loadTexts: ifoSysORIndex.setStatus('current')
if mibBuilder.loadTexts: ifoSysORIndex.setDescription('A unique value, greater than zero, for each mib presents in the system.')
ifoSysORID = MibTableColumn((1, 3, 6, 1, 4, 1, 21362, 101, 1, 3, 1, 3), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifoSysORID.setStatus('current')
if mibBuilder.loadTexts: ifoSysORID.setDescription('An unique identifier to designate the mib.')
ifoSysORDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 21362, 101, 1, 3, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifoSysORDescr.setStatus('current')
if mibBuilder.loadTexts: ifoSysORDescr.setDescription('Description of the mib.')
ifotecTemperatures = ObjectIdentity((1, 3, 6, 1, 4, 1, 21362, 101, 2))
if mibBuilder.loadTexts: ifotecTemperatures.setStatus('current')
if mibBuilder.loadTexts: ifotecTemperatures.setDescription('IFOTEC Temperature Sensors.')
ifoTemperatureTable = MibTable((1, 3, 6, 1, 4, 1, 21362, 101, 2, 1), )
if mibBuilder.loadTexts: ifoTemperatureTable.setStatus('current')
if mibBuilder.loadTexts: ifoTemperatureTable.setDescription('A list of sensors.')
ifoTemperatureEntry = MibTableRow((1, 3, 6, 1, 4, 1, 21362, 101, 2, 1, 1), ).setIndexNames((0, "IFOTEC-SMI", "ifoTempIfoSysIndex"), (0, "IFOTEC-SMI", "ifoTempIndex"))
if mibBuilder.loadTexts: ifoTemperatureEntry.setStatus('current')
if mibBuilder.loadTexts: ifoTemperatureEntry.setDescription('An entry containing sensor informations.')
ifoTempIfoSysIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 21362, 101, 2, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: ifoTempIfoSysIndex.setStatus('current')
if mibBuilder.loadTexts: ifoTempIfoSysIndex.setDescription('The index value which uniquely identifies the system in ifoSysMibTable. It is the same value used by ifoSysIndex.')
ifoTempIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 21362, 101, 2, 1, 1, 2), Integer32())
if mibBuilder.loadTexts: ifoTempIndex.setStatus('current')
if mibBuilder.loadTexts: ifoTempIndex.setDescription('A unique value, greater than zero, for each temperature sensor.')
ifoTempName = MibTableColumn((1, 3, 6, 1, 4, 1, 21362, 101, 2, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifoTempName.setStatus('current')
if mibBuilder.loadTexts: ifoTempName.setDescription('The name of the temperature sensor.')
ifoTempDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 21362, 101, 2, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifoTempDescr.setStatus('current')
if mibBuilder.loadTexts: ifoTempDescr.setDescription('The description of the temeprature sensor.')
ifoTempValue = MibTableColumn((1, 3, 6, 1, 4, 1, 21362, 101, 2, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifoTempValue.setStatus('current')
if mibBuilder.loadTexts: ifoTempValue.setDescription('the value of the sensor in 0.1 degree Celsius.')
ifoTempAlarmStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 21362, 101, 2, 1, 1, 6), IfotecDataStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifoTempAlarmStatus.setStatus('current')
if mibBuilder.loadTexts: ifoTempAlarmStatus.setDescription('Indicates the sensor alarm status.')
ifoTempLowThldAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 21362, 101, 2, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifoTempLowThldAlarm.setStatus('current')
if mibBuilder.loadTexts: ifoTempLowThldAlarm.setDescription('the value in 0.1 degree Celsius of the low threshold alarm.')
ifoTempHighThldAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 21362, 101, 2, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifoTempHighThldAlarm.setStatus('current')
if mibBuilder.loadTexts: ifoTempHighThldAlarm.setDescription('the value in 0.1 degree Celsius of the high threshold alarm.')
ifoTempLowThldWarning = MibTableColumn((1, 3, 6, 1, 4, 1, 21362, 101, 2, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifoTempLowThldWarning.setStatus('current')
if mibBuilder.loadTexts: ifoTempLowThldWarning.setDescription('the value in 0.1 degree Celsius of the low threshold warning.')
ifoTempHighThldWarning = MibTableColumn((1, 3, 6, 1, 4, 1, 21362, 101, 2, 1, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifoTempHighThldWarning.setStatus('current')
if mibBuilder.loadTexts: ifoTempHighThldWarning.setDescription('the value in 0.1 degree Celsius of the high threshold warning.')
ifotecModules = ObjectIdentity((1, 3, 6, 1, 4, 1, 21362, 102))
if mibBuilder.loadTexts: ifotecModules.setStatus('current')
if mibBuilder.loadTexts: ifotecModules.setDescription('ifotecModules provides a root object identifier\n        from which MODULE-IDENTITY values may be assigned.')
mibBuilder.exportSymbols("IFOTEC-SMI", ifoSysSerialNumber=ifoSysSerialNumber, ifoTemperatureEntry=ifoTemperatureEntry, ifoTempIndex=ifoTempIndex, IfotecDataStatus=IfotecDataStatus, ifoTemperatureTable=ifoTemperatureTable, ifoTempHighThldWarning=ifoTempHighThldWarning, ifoSysEntry=ifoSysEntry, ifoTempValue=ifoTempValue, ifoSysIndex=ifoSysIndex, ifoSysTable=ifoSysTable, ifoSysDateCode=ifoSysDateCode, ifoTempDescr=ifoTempDescr, ifotecGeneral=ifotecGeneral, ifoSysRef=ifoSysRef, ifoSysFirmware=ifoSysFirmware, ifoSysMibEntry=ifoSysMibEntry, ifotecModules=ifotecModules, ifoSysORDescr=ifoSysORDescr, ifoSysProductIndex=ifoSysProductIndex, ifotecSystem=ifotecSystem, ifoSysMibTable=ifoSysMibTable, ifoSysDescr=ifoSysDescr, ifoSysORIndex=ifoSysORIndex, ifoSysORIfoSysIndex=ifoSysORIfoSysIndex, ifoTempLowThldWarning=ifoTempLowThldWarning, ifoTempIfoSysIndex=ifoTempIfoSysIndex, ifotec=ifotec, ifoTempName=ifoTempName, ifoTempAlarmStatus=ifoTempAlarmStatus, ifoSysUpTime=ifoSysUpTime, ifoSysInfo=ifoSysInfo, ifotecTemperatures=ifotecTemperatures, ifoSysLocation=ifoSysLocation, ifoSysORID=ifoSysORID, PYSNMP_MODULE_ID=ifotec, ifoTempLowThldAlarm=ifoTempLowThldAlarm, ifoTempHighThldAlarm=ifoTempHighThldAlarm, ifoSysBootloader=ifoSysBootloader, ifoSysContact=ifoSysContact, ifoSysFamilly=ifoSysFamilly)
