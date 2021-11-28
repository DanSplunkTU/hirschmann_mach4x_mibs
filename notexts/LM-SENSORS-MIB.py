#
# PySNMP MIB module LM-SENSORS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/LM-SENSORS-MIB
# Produced by pysmi-1.1.3 at Sun Nov 28 20:09:00 2021
# On host fv-az77-612 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, ObjectIdentity, iso, Counter64, Gauge32, MibIdentifier, Counter32, Bits, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, NotificationType, Unsigned32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "ObjectIdentity", "iso", "Counter64", "Gauge32", "MibIdentifier", "Counter32", "Bits", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "NotificationType", "Unsigned32", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ucdExperimental, = mibBuilder.importSymbols("UCD-SNMP-MIB", "ucdExperimental")
lmSensorsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2021, 13, 16, 1))
lmSensorsMIB.setRevisions(('2000-11-05 00:00',))
if mibBuilder.loadTexts: lmSensorsMIB.setLastUpdated('200011050000Z')
if mibBuilder.loadTexts: lmSensorsMIB.setOrganization('AdamsNames Ltd')
lmSensors = MibIdentifier((1, 3, 6, 1, 4, 1, 2021, 13, 16))
lmTempSensorsTable = MibTable((1, 3, 6, 1, 4, 1, 2021, 13, 16, 2), )
if mibBuilder.loadTexts: lmTempSensorsTable.setStatus('current')
lmTempSensorsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2021, 13, 16, 2, 1), ).setIndexNames((0, "LM-SENSORS-MIB", "lmTempSensorsIndex"))
if mibBuilder.loadTexts: lmTempSensorsEntry.setStatus('current')
lmTempSensorsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 16, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lmTempSensorsIndex.setStatus('current')
lmTempSensorsDevice = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 16, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lmTempSensorsDevice.setStatus('current')
lmTempSensorsValue = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 16, 2, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lmTempSensorsValue.setStatus('current')
lmFanSensorsTable = MibTable((1, 3, 6, 1, 4, 1, 2021, 13, 16, 3), )
if mibBuilder.loadTexts: lmFanSensorsTable.setStatus('current')
lmFanSensorsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2021, 13, 16, 3, 1), ).setIndexNames((0, "LM-SENSORS-MIB", "lmFanSensorsIndex"))
if mibBuilder.loadTexts: lmFanSensorsEntry.setStatus('current')
lmFanSensorsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 16, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lmFanSensorsIndex.setStatus('current')
lmFanSensorsDevice = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 16, 3, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lmFanSensorsDevice.setStatus('current')
lmFanSensorsValue = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 16, 3, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lmFanSensorsValue.setStatus('current')
lmVoltSensorsTable = MibTable((1, 3, 6, 1, 4, 1, 2021, 13, 16, 4), )
if mibBuilder.loadTexts: lmVoltSensorsTable.setStatus('current')
lmVoltSensorsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2021, 13, 16, 4, 1), ).setIndexNames((0, "LM-SENSORS-MIB", "lmVoltSensorsIndex"))
if mibBuilder.loadTexts: lmVoltSensorsEntry.setStatus('current')
lmVoltSensorsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 16, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lmVoltSensorsIndex.setStatus('current')
lmVoltSensorsDevice = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 16, 4, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lmVoltSensorsDevice.setStatus('current')
lmVoltSensorsValue = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 16, 4, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lmVoltSensorsValue.setStatus('current')
lmMiscSensorsTable = MibTable((1, 3, 6, 1, 4, 1, 2021, 13, 16, 5), )
if mibBuilder.loadTexts: lmMiscSensorsTable.setStatus('current')
lmMiscSensorsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2021, 13, 16, 5, 1), ).setIndexNames((0, "LM-SENSORS-MIB", "lmMiscSensorsIndex"))
if mibBuilder.loadTexts: lmMiscSensorsEntry.setStatus('current')
lmMiscSensorsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 16, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lmMiscSensorsIndex.setStatus('current')
lmMiscSensorsDevice = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 16, 5, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lmMiscSensorsDevice.setStatus('current')
lmMiscSensorsValue = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 16, 5, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lmMiscSensorsValue.setStatus('current')
mibBuilder.exportSymbols("LM-SENSORS-MIB", lmMiscSensorsEntry=lmMiscSensorsEntry, lmSensorsMIB=lmSensorsMIB, lmTempSensorsEntry=lmTempSensorsEntry, lmSensors=lmSensors, lmFanSensorsIndex=lmFanSensorsIndex, lmFanSensorsEntry=lmFanSensorsEntry, lmFanSensorsTable=lmFanSensorsTable, lmMiscSensorsTable=lmMiscSensorsTable, lmVoltSensorsTable=lmVoltSensorsTable, lmMiscSensorsIndex=lmMiscSensorsIndex, lmFanSensorsValue=lmFanSensorsValue, lmVoltSensorsValue=lmVoltSensorsValue, lmTempSensorsTable=lmTempSensorsTable, lmTempSensorsIndex=lmTempSensorsIndex, lmVoltSensorsDevice=lmVoltSensorsDevice, lmVoltSensorsEntry=lmVoltSensorsEntry, lmMiscSensorsDevice=lmMiscSensorsDevice, lmVoltSensorsIndex=lmVoltSensorsIndex, lmMiscSensorsValue=lmMiscSensorsValue, PYSNMP_MODULE_ID=lmSensorsMIB, lmFanSensorsDevice=lmFanSensorsDevice, lmTempSensorsValue=lmTempSensorsValue, lmTempSensorsDevice=lmTempSensorsDevice)
