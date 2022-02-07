#
# PySNMP MIB module AH-SYSTEM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/aerohive/AH-SYSTEM-MIB
# Produced by pysmi-1.1.8 at Mon Feb  7 16:07:01 2022
# On host fv-az42-619 platform Linux version 5.11.0-1028-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
ahProduct, = mibBuilder.importSymbols("AH-SMI-MIB", "ahProduct")
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, ObjectIdentity, Counter32, ModuleIdentity, IpAddress, TimeTicks, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Counter64, Gauge32, iso, Unsigned32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "ObjectIdentity", "Counter32", "ModuleIdentity", "IpAddress", "TimeTicks", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Counter64", "Gauge32", "iso", "Unsigned32", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ahSystem = ModuleIdentity((1, 3, 6, 1, 4, 1, 26928, 1, 2))
if mibBuilder.loadTexts: ahSystem.setLastUpdated('201608310000Z')
if mibBuilder.loadTexts: ahSystem.setOrganization('Aerohive Networks, Inc')
if mibBuilder.loadTexts: ahSystem.setContactInfo('info@aerohive.com\n                        1011 McCarthy Boulevard\n                        Milpitas, CA 95035')
if mibBuilder.loadTexts: ahSystem.setDescription('This module contains the MIB definition of \n\t\t\taerohive system related information.')
ahSystemName = MibScalar((1, 3, 6, 1, 4, 1, 26928, 1, 2, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahSystemName.setStatus('current')
if mibBuilder.loadTexts: ahSystemName.setDescription('aerohive platform system name')
ahSystemDescription = MibScalar((1, 3, 6, 1, 4, 1, 26928, 1, 2, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahSystemDescription.setStatus('current')
if mibBuilder.loadTexts: ahSystemDescription.setDescription('aerohive platform system description')
ahCpuUtilization = MibScalar((1, 3, 6, 1, 4, 1, 26928, 1, 2, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahCpuUtilization.setStatus('current')
if mibBuilder.loadTexts: ahCpuUtilization.setDescription('aerohive platform cpu utilization')
ahMemUtilization = MibScalar((1, 3, 6, 1, 4, 1, 26928, 1, 2, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahMemUtilization.setStatus('current')
if mibBuilder.loadTexts: ahMemUtilization.setDescription('aerohive platform memory utilization')
ahSystemSerial = MibScalar((1, 3, 6, 1, 4, 1, 26928, 1, 2, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahSystemSerial.setStatus('current')
if mibBuilder.loadTexts: ahSystemSerial.setDescription('aerohive platform system serial-number')
ahDeviceMode = MibScalar((1, 3, 6, 1, 4, 1, 26928, 1, 2, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahDeviceMode.setStatus('current')
if mibBuilder.loadTexts: ahDeviceMode.setDescription('aerohive device mode type')
ahUpTime = MibScalar((1, 3, 6, 1, 4, 1, 26928, 1, 2, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahUpTime.setStatus('current')
if mibBuilder.loadTexts: ahUpTime.setDescription('aerohive platform up time')
ahHwVersion = MibScalar((1, 3, 6, 1, 4, 1, 26928, 1, 2, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahHwVersion.setStatus('current')
if mibBuilder.loadTexts: ahHwVersion.setDescription('aerohive platform hardware version')
ahClientCount = MibScalar((1, 3, 6, 1, 4, 1, 26928, 1, 2, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 10000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahClientCount.setStatus('current')
if mibBuilder.loadTexts: ahClientCount.setDescription('the counter of devices connected to aerohive products')
ahEnvirmentTemp = MibScalar((1, 3, 6, 1, 4, 1, 26928, 1, 2, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahEnvirmentTemp.setStatus('current')
if mibBuilder.loadTexts: ahEnvirmentTemp.setDescription('aerohive envirment temp-ditection')
ahEnvirmentFan = MibScalar((1, 3, 6, 1, 4, 1, 26928, 1, 2, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 10000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahEnvirmentFan.setStatus('current')
if mibBuilder.loadTexts: ahEnvirmentFan.setDescription('aerohive envirment fan speed,  unit as RPM')
ahFirmwareVersion = MibScalar((1, 3, 6, 1, 4, 1, 26928, 1, 2, 12), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ahFirmwareVersion.setStatus('current')
if mibBuilder.loadTexts: ahFirmwareVersion.setDescription('aerohive platform fireware version')
mibBuilder.exportSymbols("AH-SYSTEM-MIB", ahSystemDescription=ahSystemDescription, ahSystem=ahSystem, ahMemUtilization=ahMemUtilization, ahSystemName=ahSystemName, ahEnvirmentTemp=ahEnvirmentTemp, ahCpuUtilization=ahCpuUtilization, ahHwVersion=ahHwVersion, ahClientCount=ahClientCount, ahFirmwareVersion=ahFirmwareVersion, ahDeviceMode=ahDeviceMode, ahSystemSerial=ahSystemSerial, PYSNMP_MODULE_ID=ahSystem, ahEnvirmentFan=ahEnvirmentFan, ahUpTime=ahUpTime)
