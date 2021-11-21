#
# PySNMP MIB module PICA-PRIVATE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/picos/PICA-PRIVATE-MIB
# Produced by pysmi-1.1.3 at Sun Nov 21 00:34:59 2021
# On host fv-az39-63 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
IANAifType, = mibBuilder.importSymbols("IANAifType-MIB", "IANAifType")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
snmpTraps, = mibBuilder.importSymbols("SNMPv2-MIB", "snmpTraps")
MibIdentifier, Gauge32, snmpModules, enterprises, mib_2, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Unsigned32, ObjectIdentity, Counter32, TimeTicks, NotificationType, ModuleIdentity, Integer32, IpAddress, Counter64, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Gauge32", "snmpModules", "enterprises", "mib-2", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Unsigned32", "ObjectIdentity", "Counter32", "TimeTicks", "NotificationType", "ModuleIdentity", "Integer32", "IpAddress", "Counter64", "Bits")
TruthValue, RowStatus, DisplayString, AutonomousType, TextualConvention, TimeStamp, TestAndIncr, PhysAddress = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "RowStatus", "DisplayString", "AutonomousType", "TextualConvention", "TimeStamp", "TestAndIncr", "PhysAddress")
picaPrivateMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 35098))
picaPrivateMib.setRevisions(('2011-04-28 00:00',))
if mibBuilder.loadTexts: picaPrivateMib.setLastUpdated('201104280000Z')
if mibBuilder.loadTexts: picaPrivateMib.setOrganization('Pica8 Inc.')
hostStatusGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 35098, 1))
cpuUsage = MibScalar((1, 3, 6, 1, 4, 1, 35098, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpuUsage.setStatus('current')
totalPhyMemory = MibScalar((1, 3, 6, 1, 4, 1, 35098, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: totalPhyMemory.setStatus('current')
usedPhyMemory = MibScalar((1, 3, 6, 1, 4, 1, 35098, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usedPhyMemory.setStatus('current')
freePhyMemory = MibScalar((1, 3, 6, 1, 4, 1, 35098, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: freePhyMemory.setStatus('current')
switchTemperature = MibScalar((1, 3, 6, 1, 4, 1, 35098, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: switchTemperature.setStatus('current')
cpuTemperature = MibScalar((1, 3, 6, 1, 4, 1, 35098, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpuTemperature.setStatus('current')
switchChipTemperature = MibScalar((1, 3, 6, 1, 4, 1, 35098, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: switchChipTemperature.setStatus('current')
switchFanSpeed = MibScalar((1, 3, 6, 1, 4, 1, 35098, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: switchFanSpeed.setStatus('current')
switchPWM = MibScalar((1, 3, 6, 1, 4, 1, 35098, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: switchPWM.setStatus('current')
sfpstatusTable = MibTable((1, 3, 6, 1, 4, 1, 35098, 1, 10), )
if mibBuilder.loadTexts: sfpstatusTable.setStatus('current')
sfpstatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 35098, 1, 10, 1), ).setIndexNames((0, "PICA-PRIVATE-MIB", "sfpIndex"))
if mibBuilder.loadTexts: sfpstatusEntry.setStatus('current')
sfpIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 35098, 1, 10, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpIndex.setStatus('current')
sfpVendorName = MibTableColumn((1, 3, 6, 1, 4, 1, 35098, 1, 10, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpVendorName.setStatus('current')
sfpSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 35098, 1, 10, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpSerialNumber.setStatus('current')
sfpTemp = MibTableColumn((1, 3, 6, 1, 4, 1, 35098, 1, 10, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpTemp.setStatus('current')
sfpVoltage = MibTableColumn((1, 3, 6, 1, 4, 1, 35098, 1, 10, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpVoltage.setStatus('current')
sfpBias = MibTableColumn((1, 3, 6, 1, 4, 1, 35098, 1, 10, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpBias.setStatus('current')
sfpTxPower = MibTableColumn((1, 3, 6, 1, 4, 1, 35098, 1, 10, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpTxPower.setStatus('current')
sfpRxPower = MibTableColumn((1, 3, 6, 1, 4, 1, 35098, 1, 10, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpRxPower.setStatus('current')
sfpType = MibTableColumn((1, 3, 6, 1, 4, 1, 35098, 1, 10, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpType.setStatus('current')
rpsustatusTable = MibTable((1, 3, 6, 1, 4, 1, 35098, 1, 11), )
if mibBuilder.loadTexts: rpsustatusTable.setStatus('current')
rpsustatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 35098, 1, 11, 1), ).setIndexNames((0, "PICA-PRIVATE-MIB", "rpsuIndex"))
if mibBuilder.loadTexts: rpsustatusEntry.setStatus('current')
rpsuIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 35098, 1, 11, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 10))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rpsuIndex.setStatus('current')
serialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 35098, 1, 11, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: serialNumber.setStatus('current')
rpsuStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 35098, 1, 11, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rpsuStatus.setStatus('current')
rpsuTemprature = MibTableColumn((1, 3, 6, 1, 4, 1, 35098, 1, 11, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rpsuTemprature.setStatus('current')
rpsuFanSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 35098, 1, 11, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rpsuFanSpeed.setStatus('current')
rpsuPWM = MibTableColumn((1, 3, 6, 1, 4, 1, 35098, 1, 11, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rpsuPWM.setStatus('current')
switchConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 35098, 2))
tftpConfigFilePath = MibScalar((1, 3, 6, 1, 4, 1, 35098, 2, 0), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tftpConfigFilePath.setStatus('current')
tftpBatchFilePath = MibScalar((1, 3, 6, 1, 4, 1, 35098, 2, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tftpBatchFilePath.setStatus('current')
picaConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 35098, 20))
picaGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 35098, 20, 1))
picaCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 35098, 20, 2))
picaBasicGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 35098, 20, 1, 1)).setObjects(("PICA-PRIVATE-MIB", "cpuUsage"), ("PICA-PRIVATE-MIB", "totalPhyMemory"), ("PICA-PRIVATE-MIB", "usedPhyMemory"), ("PICA-PRIVATE-MIB", "freePhyMemory"), ("PICA-PRIVATE-MIB", "switchTemperature"), ("PICA-PRIVATE-MIB", "cpuTemperature"), ("PICA-PRIVATE-MIB", "switchChipTemperature"), ("PICA-PRIVATE-MIB", "switchFanSpeed"), ("PICA-PRIVATE-MIB", "switchPWM"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    picaBasicGroup = picaBasicGroup.setStatus('current')
picasfpGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 35098, 20, 1, 2)).setObjects(("PICA-PRIVATE-MIB", "sfpIndex"), ("PICA-PRIVATE-MIB", "sfpVendorName"), ("PICA-PRIVATE-MIB", "sfpSerialNumber"), ("PICA-PRIVATE-MIB", "sfpTemp"), ("PICA-PRIVATE-MIB", "sfpVoltage"), ("PICA-PRIVATE-MIB", "sfpBias"), ("PICA-PRIVATE-MIB", "sfpTxPower"), ("PICA-PRIVATE-MIB", "sfpRxPower"), ("PICA-PRIVATE-MIB", "sfpType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    picasfpGroup = picasfpGroup.setStatus('current')
picarpsuGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 35098, 20, 1, 3)).setObjects(("PICA-PRIVATE-MIB", "rpsuIndex"), ("PICA-PRIVATE-MIB", "serialNumber"), ("PICA-PRIVATE-MIB", "rpsuStatus"), ("PICA-PRIVATE-MIB", "rpsuTemprature"), ("PICA-PRIVATE-MIB", "rpsuFanSpeed"), ("PICA-PRIVATE-MIB", "rpsuPWM"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    picarpsuGroup = picarpsuGroup.setStatus('current')
picaConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 35098, 20, 1, 4)).setObjects(("PICA-PRIVATE-MIB", "tftpConfigFilePath"), ("PICA-PRIVATE-MIB", "tftpBatchFilePath"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    picaConfigGroup = picaConfigGroup.setStatus('current')
picaCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 35098, 20, 2, 1)).setObjects(("PICA-PRIVATE-MIB", "picaBasicGroup"), ("PICA-PRIVATE-MIB", "picasfpGroup"), ("PICA-PRIVATE-MIB", "picarpsuGroup"), ("PICA-PRIVATE-MIB", "picaConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    picaCompliance = picaCompliance.setStatus('current')
mibBuilder.exportSymbols("PICA-PRIVATE-MIB", sfpBias=sfpBias, tftpConfigFilePath=tftpConfigFilePath, sfpVoltage=sfpVoltage, picasfpGroup=picasfpGroup, picaBasicGroup=picaBasicGroup, sfpTxPower=sfpTxPower, freePhyMemory=freePhyMemory, sfpRxPower=sfpRxPower, picaGroups=picaGroups, rpsustatusEntry=rpsustatusEntry, rpsuTemprature=rpsuTemprature, switchPWM=switchPWM, sfpType=sfpType, picaPrivateMib=picaPrivateMib, sfpSerialNumber=sfpSerialNumber, rpsuFanSpeed=rpsuFanSpeed, picaConformance=picaConformance, usedPhyMemory=usedPhyMemory, PYSNMP_MODULE_ID=picaPrivateMib, switchFanSpeed=switchFanSpeed, hostStatusGroup=hostStatusGroup, rpsuPWM=rpsuPWM, sfpstatusTable=sfpstatusTable, switchChipTemperature=switchChipTemperature, rpsuIndex=rpsuIndex, switchTemperature=switchTemperature, picarpsuGroup=picarpsuGroup, sfpVendorName=sfpVendorName, totalPhyMemory=totalPhyMemory, sfpstatusEntry=sfpstatusEntry, sfpIndex=sfpIndex, rpsuStatus=rpsuStatus, picaConfigGroup=picaConfigGroup, cpuUsage=cpuUsage, picaCompliance=picaCompliance, sfpTemp=sfpTemp, serialNumber=serialNumber, picaCompliances=picaCompliances, cpuTemperature=cpuTemperature, rpsustatusTable=rpsustatusTable, tftpBatchFilePath=tftpBatchFilePath, switchConfigGroup=switchConfigGroup)
