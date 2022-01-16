#
# PySNMP MIB module PACKETLOGIC-HW-SENSORS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/procera/PACKETLOGIC-HW-SENSORS-MIB
# Produced by pysmi-1.1.8 at Sun Jan 16 00:42:59 2022
# On host fv-az42-839 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
CounterBasedGauge64, = mibBuilder.importSymbols("HCNUM-TC", "CounterBasedGauge64")
hw, = mibBuilder.importSymbols("PACKETLOGIC-HW-MIB", "hw")
packetlogic2, = mibBuilder.importSymbols("PACKETLOGIC-MIB", "packetlogic2")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, TimeTicks, iso, Counter64, NotificationType, ModuleIdentity, Counter32, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Bits, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "TimeTicks", "iso", "Counter64", "NotificationType", "ModuleIdentity", "Counter32", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Bits", "MibIdentifier")
DateAndTime, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "DisplayString", "TextualConvention")
sensors = ModuleIdentity((1, 3, 6, 1, 4, 1, 15397, 2, 30, 3))
sensors.setRevisions(('2019-09-12 15:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: sensors.setRevisionsDescriptions((' Latest version at the revision date for version GET VERSION HERE',))
if mibBuilder.loadTexts: sensors.setLastUpdated('201909121500Z')
if mibBuilder.loadTexts: sensors.setOrganization('Procera Networks, Inc.')
if mibBuilder.loadTexts: sensors.setContactInfo('support@proceranetworks.com')
if mibBuilder.loadTexts: sensors.setDescription('PacketLogic2 MIB which describes BMC sensor properties')
tempSensors = MibTable((1, 3, 6, 1, 4, 1, 15397, 2, 30, 3, 1), )
if mibBuilder.loadTexts: tempSensors.setStatus('current')
if mibBuilder.loadTexts: tempSensors.setDescription('Conceptual Table')
tempSensorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 15397, 2, 30, 3, 1, 1), ).setIndexNames((0, "PACKETLOGIC-HW-SENSORS-MIB", "tempSensorEntryIndex"))
if mibBuilder.loadTexts: tempSensorEntry.setStatus('current')
if mibBuilder.loadTexts: tempSensorEntry.setDescription('Conceptual Table')
tempSensorEntryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 30, 3, 1, 1, 999), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: tempSensorEntryIndex.setStatus('current')
if mibBuilder.loadTexts: tempSensorEntryIndex.setDescription('Unique Row Index for Conceptual Table')
fanSensors = MibTable((1, 3, 6, 1, 4, 1, 15397, 2, 30, 3, 4), )
if mibBuilder.loadTexts: fanSensors.setStatus('current')
if mibBuilder.loadTexts: fanSensors.setDescription('Conceptual Table')
fanSensorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 15397, 2, 30, 3, 4, 1), ).setIndexNames((0, "PACKETLOGIC-HW-SENSORS-MIB", "fanSensorEntryIndex"))
if mibBuilder.loadTexts: fanSensorEntry.setStatus('current')
if mibBuilder.loadTexts: fanSensorEntry.setDescription('Conceptual Table')
fanSensorEntryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 30, 3, 4, 1, 999), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: fanSensorEntryIndex.setStatus('current')
if mibBuilder.loadTexts: fanSensorEntryIndex.setDescription('Unique Row Index for Conceptual Table')
tempSensorId = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 30, 3, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tempSensorId.setStatus('current')
if mibBuilder.loadTexts: tempSensorId.setDescription('Sensor ID')
tempSensorReading = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 30, 3, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tempSensorReading.setStatus('current')
if mibBuilder.loadTexts: tempSensorReading.setDescription('Sensor Temperature')
tempSensorStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 30, 3, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tempSensorStatus.setStatus('current')
if mibBuilder.loadTexts: tempSensorStatus.setDescription('Temperature Sensor Status')
tempSensorUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 30, 3, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tempSensorUnit.setStatus('current')
if mibBuilder.loadTexts: tempSensorUnit.setDescription('Temperature Sensor Reading Unit')
fanSensorId = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 30, 3, 4, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fanSensorId.setStatus('current')
if mibBuilder.loadTexts: fanSensorId.setDescription('Fan ID')
fanSensorSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 30, 3, 4, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fanSensorSpeed.setStatus('current')
if mibBuilder.loadTexts: fanSensorSpeed.setDescription('Fan Speed')
fanSensorStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 30, 3, 4, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fanSensorStatus.setStatus('current')
if mibBuilder.loadTexts: fanSensorStatus.setDescription('Fan Sensor Status')
fanSensorUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 30, 3, 4, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fanSensorUnit.setStatus('current')
if mibBuilder.loadTexts: fanSensorUnit.setDescription('Fan Sensor Reading Unit')
mibBuilder.exportSymbols("PACKETLOGIC-HW-SENSORS-MIB", fanSensorId=fanSensorId, tempSensors=tempSensors, fanSensorStatus=fanSensorStatus, tempSensorId=tempSensorId, tempSensorEntry=tempSensorEntry, tempSensorUnit=tempSensorUnit, fanSensorEntryIndex=fanSensorEntryIndex, tempSensorEntryIndex=tempSensorEntryIndex, fanSensors=fanSensors, tempSensorReading=tempSensorReading, sensors=sensors, tempSensorStatus=tempSensorStatus, fanSensorUnit=fanSensorUnit, PYSNMP_MODULE_ID=sensors, fanSensorSpeed=fanSensorSpeed, fanSensorEntry=fanSensorEntry)
