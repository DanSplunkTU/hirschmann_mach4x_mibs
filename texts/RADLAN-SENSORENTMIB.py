#
# PySNMP MIB module RADLAN-SENSORENTMIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/radlan/RADLAN-SENSORENTMIB
# Produced by pysmi-1.1.8 at Sat Jan 15 18:17:50 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
entityPhysicalGroup, entPhysicalIndex = mibBuilder.importSymbols("ENTITY-MIB", "entityPhysicalGroup", "entPhysicalIndex")
entPhySensorEntry, EntitySensorValue = mibBuilder.importSymbols("ENTITY-SENSOR-MIB", "entPhySensorEntry", "EntitySensorValue")
rlEnv, = mibBuilder.importSymbols("RADLAN-HWENVIROMENT", "rlEnv")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
MibIdentifier, Integer32, Counter64, IpAddress, NotificationType, mib_2, Counter32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, iso, TimeTicks, Unsigned32, ModuleIdentity, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Integer32", "Counter64", "IpAddress", "NotificationType", "mib-2", "Counter32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "iso", "TimeTicks", "Unsigned32", "ModuleIdentity", "Bits")
TimeStamp, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TimeStamp", "DisplayString", "TextualConvention")
rlSensor = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 83, 4))
rlSensor.setRevisions(('2003-09-21 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rlSensor.setRevisionsDescriptions(('ADDED this MODULE-IDENTITY clause.',))
if mibBuilder.loadTexts: rlSensor.setLastUpdated('200309210000Z')
if mibBuilder.loadTexts: rlSensor.setOrganization('Radlan Computer Communications Ltd.')
if mibBuilder.loadTexts: rlSensor.setContactInfo('radlan.com')
if mibBuilder.loadTexts: rlSensor.setDescription('The private MIB module definition for sensors in Radlan devices.')
rlEntPhySensorTable = MibTable((1, 3, 6, 1, 4, 1, 89, 83, 3), )
if mibBuilder.loadTexts: rlEntPhySensorTable.setStatus('current')
if mibBuilder.loadTexts: rlEntPhySensorTable.setDescription('The addition to the table of sensors maintained by the environmental\n                monitor.')
rlEntPhySensorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 83, 3, 1), )
entPhySensorEntry.registerAugmentions(("RADLAN-SENSORENTMIB", "rlEntPhySensorEntry"))
rlEntPhySensorEntry.setIndexNames(*entPhySensorEntry.getIndexNames())
if mibBuilder.loadTexts: rlEntPhySensorEntry.setStatus('current')
if mibBuilder.loadTexts: rlEntPhySensorEntry.setDescription('An additon to the entry in the sensor table, representing the\n                maximum/minimum values for the sensor associated.')
rlEnvPhySensorMinValue = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 83, 3, 1, 1), EntitySensorValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlEnvPhySensorMinValue.setStatus('current')
if mibBuilder.loadTexts: rlEnvPhySensorMinValue.setDescription('Minimum value for the Sensor being instrumented.')
rlEnvPhySensorMaxValue = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 83, 3, 1, 2), EntitySensorValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlEnvPhySensorMaxValue.setStatus('current')
if mibBuilder.loadTexts: rlEnvPhySensorMaxValue.setDescription('Maximum value for the Sensor being instrumented.')
rlEnvPhySensorTestValue = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 83, 3, 1, 3), EntitySensorValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlEnvPhySensorTestValue.setStatus('current')
if mibBuilder.loadTexts: rlEnvPhySensorTestValue.setDescription('Test/reference value for the Sensor being instrumented.')
mibBuilder.exportSymbols("RADLAN-SENSORENTMIB", rlEnvPhySensorTestValue=rlEnvPhySensorTestValue, rlEntPhySensorEntry=rlEntPhySensorEntry, rlEntPhySensorTable=rlEntPhySensorTable, PYSNMP_MODULE_ID=rlSensor, rlEnvPhySensorMinValue=rlEnvPhySensorMinValue, rlSensor=rlSensor, rlEnvPhySensorMaxValue=rlEnvPhySensorMaxValue)
