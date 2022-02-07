#
# PySNMP MIB module MDS-SYSTEM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/gemds/MDS-SYSTEM-MIB
# Produced by pysmi-1.1.8 at Mon Feb  7 16:12:52 2022
# On host fv-az42-619 platform Linux version 5.11.0-1028-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
mdsSystem, = mibBuilder.importSymbols("MDS-ORBIT-SMI-MIB", "mdsSystem")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
IpAddress, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, MibIdentifier, Counter32, Integer32, Gauge32, NotificationType, Unsigned32, ObjectIdentity, ModuleIdentity, Counter64, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "MibIdentifier", "Counter32", "Integer32", "Gauge32", "NotificationType", "Unsigned32", "ObjectIdentity", "ModuleIdentity", "Counter64", "TimeTicks")
DisplayString, TextualConvention, TruthValue, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue", "DateAndTime")
mdsSystemMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4130, 10, 1, 1))
mdsSystemMIB.setRevisions(('2019-11-18 00:00', '2018-05-16 00:00', '2014-02-10 00:00',))
if mibBuilder.loadTexts: mdsSystemMIB.setLastUpdated('201805160000Z')
if mibBuilder.loadTexts: mdsSystemMIB.setOrganization('GE MDS LLC http://www.gemds.com')
mSysMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 1, 1, 1))
mSysConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 1, 1, 1, 1))
mSysStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 1, 1, 1, 2))
class FirmwareLocation(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 255)

mSysSerialNumberCore = MibScalar((1, 3, 6, 1, 4, 1, 4130, 10, 1, 1, 1, 2, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mSysSerialNumberCore.setStatus('current')
mSysSerialNumberPlatform = MibScalar((1, 3, 6, 1, 4, 1, 4130, 10, 1, 1, 1, 2, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mSysSerialNumberPlatform.setStatus('current')
mSysProductConfiguration = MibScalar((1, 3, 6, 1, 4, 1, 4130, 10, 1, 1, 1, 2, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mSysProductConfiguration.setStatus('current')
mSysGuid = MibScalar((1, 3, 6, 1, 4, 1, 4130, 10, 1, 1, 1, 2, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mSysGuid.setStatus('current')
mSysUptime = MibScalar((1, 3, 6, 1, 4, 1, 4130, 10, 1, 1, 1, 2, 5), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mSysUptime.setStatus('current')
mSysTemperature = MibScalar((1, 3, 6, 1, 4, 1, 4130, 10, 1, 1, 1, 2, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mSysTemperature.setStatus('current')
mSysFirmwareVersionTable = MibTable((1, 3, 6, 1, 4, 1, 4130, 10, 1, 1, 1, 2, 7), )
if mibBuilder.loadTexts: mSysFirmwareVersionTable.setStatus('current')
mSysPowerSupplyVoltage = MibScalar((1, 3, 6, 1, 4, 1, 4130, 10, 1, 1, 1, 2, 9), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mSysPowerSupplyVoltage.setStatus('current')
mSysCurrentDateTime = MibScalar((1, 3, 6, 1, 4, 1, 4130, 10, 1, 1, 1, 2, 10), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mSysCurrentDateTime.setStatus('current')
mSysBootDateTime = MibScalar((1, 3, 6, 1, 4, 1, 4130, 10, 1, 1, 1, 2, 11), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mSysBootDateTime.setStatus('current')
mSysFirmwareVersionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4130, 10, 1, 1, 1, 2, 7, 1), ).setIndexNames((0, "MDS-SYSTEM-MIB", "mSysLocation"))
if mibBuilder.loadTexts: mSysFirmwareVersionEntry.setStatus('current')
mSysLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 1, 1, 1, 2, 7, 1, 1), FirmwareLocation()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mSysLocation.setStatus('current')
mSysVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 1, 1, 1, 2, 7, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mSysVersion.setStatus('current')
mSysActive = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 1, 1, 1, 2, 7, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mSysActive.setStatus('current')
mSysAutoUpdateState = MibScalar((1, 3, 6, 1, 4, 1, 4130, 10, 1, 1, 1, 2, 12), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mSysAutoUpdateState.setStatus('current')
mSysAutoUpdateDetails = MibScalar((1, 3, 6, 1, 4, 1, 4130, 10, 1, 1, 1, 2, 13), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mSysAutoUpdateDetails.setStatus('current')
mSysMprStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 1, 1, 1, 2, 8))
mSysMprHeatsinkTemperature1 = MibScalar((1, 3, 6, 1, 4, 1, 4130, 10, 1, 1, 1, 2, 8, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mSysMprHeatsinkTemperature1.setStatus('current')
mSysMprHeatsinkTemperature2 = MibScalar((1, 3, 6, 1, 4, 1, 4130, 10, 1, 1, 1, 2, 8, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mSysMprHeatsinkTemperature2.setStatus('current')
mSysMprPowerSupplyVoltage1 = MibScalar((1, 3, 6, 1, 4, 1, 4130, 10, 1, 1, 1, 2, 8, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mSysMprPowerSupplyVoltage1.setStatus('current')
mSysMprPowerSupplyVoltage2 = MibScalar((1, 3, 6, 1, 4, 1, 4130, 10, 1, 1, 1, 2, 8, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mSysMprPowerSupplyVoltage2.setStatus('current')
mSysMprRelaySwitchPosition = MibScalar((1, 3, 6, 1, 4, 1, 4130, 10, 1, 1, 1, 2, 8, 5), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mSysMprRelaySwitchPosition.setStatus('current')
mdsSysMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 1, 1, 3))
mdsSysMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 1, 1, 3, 1))
mdsSysMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 1, 1, 3, 2))
mSysCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4130, 10, 1, 1, 3, 1, 1)).setObjects(("MDS-SYSTEM-MIB", "mSysStatusGroup"), ("MDS-SYSTEM-MIB", "mSysMprStatusGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mSysCompliance = mSysCompliance.setStatus('current')
mSysStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4130, 10, 1, 1, 3, 2, 1)).setObjects(("MDS-SYSTEM-MIB", "mSysSerialNumberCore"), ("MDS-SYSTEM-MIB", "mSysSerialNumberPlatform"), ("MDS-SYSTEM-MIB", "mSysProductConfiguration"), ("MDS-SYSTEM-MIB", "mSysGuid"), ("MDS-SYSTEM-MIB", "mSysUptime"), ("MDS-SYSTEM-MIB", "mSysTemperature"), ("MDS-SYSTEM-MIB", "mSysPowerSupplyVoltage"), ("MDS-SYSTEM-MIB", "mSysLocation"), ("MDS-SYSTEM-MIB", "mSysVersion"), ("MDS-SYSTEM-MIB", "mSysActive"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mSysStatusGroup = mSysStatusGroup.setStatus('current')
mSysMprStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4130, 10, 1, 1, 3, 2, 2)).setObjects(("MDS-SYSTEM-MIB", "mSysMprHeatsinkTemperature1"), ("MDS-SYSTEM-MIB", "mSysMprHeatsinkTemperature2"), ("MDS-SYSTEM-MIB", "mSysMprPowerSupplyVoltage1"), ("MDS-SYSTEM-MIB", "mSysMprPowerSupplyVoltage2"), ("MDS-SYSTEM-MIB", "mSysMprRelaySwitchPosition"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mSysMprStatusGroup = mSysMprStatusGroup.setStatus('current')
mibBuilder.exportSymbols("MDS-SYSTEM-MIB", mSysBootDateTime=mSysBootDateTime, mdsSysMIBConformance=mdsSysMIBConformance, mSysVersion=mSysVersion, mSysFirmwareVersionTable=mSysFirmwareVersionTable, mSysMprStatus=mSysMprStatus, mSysMprRelaySwitchPosition=mSysMprRelaySwitchPosition, mSysFirmwareVersionEntry=mSysFirmwareVersionEntry, mSysAutoUpdateDetails=mSysAutoUpdateDetails, mSysMIBObjects=mSysMIBObjects, mSysSerialNumberCore=mSysSerialNumberCore, mSysAutoUpdateState=mSysAutoUpdateState, mSysStatusGroup=mSysStatusGroup, FirmwareLocation=FirmwareLocation, mSysCurrentDateTime=mSysCurrentDateTime, mSysConfig=mSysConfig, mSysMprPowerSupplyVoltage2=mSysMprPowerSupplyVoltage2, mSysMprHeatsinkTemperature2=mSysMprHeatsinkTemperature2, mSysLocation=mSysLocation, mSysCompliance=mSysCompliance, mSysMprHeatsinkTemperature1=mSysMprHeatsinkTemperature1, mSysUptime=mSysUptime, mSysPowerSupplyVoltage=mSysPowerSupplyVoltage, mdsSysMIBCompliances=mdsSysMIBCompliances, mdsSystemMIB=mdsSystemMIB, mSysGuid=mSysGuid, mSysMprPowerSupplyVoltage1=mSysMprPowerSupplyVoltage1, PYSNMP_MODULE_ID=mdsSystemMIB, mSysMprStatusGroup=mSysMprStatusGroup, mSysActive=mSysActive, mSysTemperature=mSysTemperature, mdsSysMIBGroups=mdsSysMIBGroups, mSysStatus=mSysStatus, mSysProductConfiguration=mSysProductConfiguration, mSysSerialNumberPlatform=mSysSerialNumberPlatform)
