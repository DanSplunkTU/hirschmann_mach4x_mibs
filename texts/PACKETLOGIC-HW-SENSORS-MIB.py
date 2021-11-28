#
# PySNMP MIB module PACKETLOGIC-HW-SENSORS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/procera/PACKETLOGIC-HW-SENSORS-MIB
# Produced by pysmi-1.1.3 at Sun Nov 28 20:20:22 2021
# On host fv-az77-612 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
CounterBasedGauge64, = mibBuilder.importSymbols("HCNUM-TC", "CounterBasedGauge64")
hw, = mibBuilder.importSymbols("PACKETLOGIC-HW-MIB", "hw")
packetlogic2, = mibBuilder.importSymbols("PACKETLOGIC-MIB", "packetlogic2")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, Gauge32, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, iso, Unsigned32, Counter32, TimeTicks, IpAddress, Counter64, Bits, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Gauge32", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "iso", "Unsigned32", "Counter32", "TimeTicks", "IpAddress", "Counter64", "Bits", "ModuleIdentity")
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
mibBuilder.exportSymbols("PACKETLOGIC-HW-SENSORS-MIB", tempSensorEntry=tempSensorEntry, fanSensorEntryIndex=fanSensorEntryIndex, tempSensorStatus=tempSensorStatus, tempSensorEntryIndex=tempSensorEntryIndex, tempSensorUnit=tempSensorUnit, tempSensorId=tempSensorId, PYSNMP_MODULE_ID=sensors, tempSensorReading=tempSensorReading, fanSensorUnit=fanSensorUnit, fanSensorEntry=fanSensorEntry, fanSensorStatus=fanSensorStatus, fanSensorId=fanSensorId, tempSensors=tempSensors, sensors=sensors, fanSensors=fanSensors, fanSensorSpeed=fanSensorSpeed)
