#
# PySNMP MIB module OG-SENSOR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/opengear/OG-SENSOR-MIB
# Produced by pysmi-1.1.8 at Mon Feb  7 16:17:33 2022
# On host fv-az42-619 platform Linux version 5.11.0-1028-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ogMgmt, = mibBuilder.importSymbols("OG-SMI-MIB", "ogMgmt")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Integer32, TimeTicks, ObjectIdentity, Bits, Gauge32, ModuleIdentity, Counter32, Unsigned32, iso, MibIdentifier, Counter64, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Integer32", "TimeTicks", "ObjectIdentity", "Bits", "Gauge32", "ModuleIdentity", "Counter32", "Unsigned32", "iso", "MibIdentifier", "Counter64", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ogSensorMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 25049, 10, 13))
ogSensorMib.setRevisions(('2013-08-11 00:00', '2010-03-22 11:27', '2008-11-27 11:40',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ogSensorMib.setRevisionsDescriptions(('Renamed from OPENGEAR-SENSOR-MIB to OG-SENSOR-MIB to\n\t\tfix naming discrepancy.', 'Syntax corrections by Opengear Inc.', 'Initial version.',))
if mibBuilder.loadTexts: ogSensorMib.setLastUpdated('201308110000Z')
if mibBuilder.loadTexts: ogSensorMib.setOrganization('Opengear Inc.')
if mibBuilder.loadTexts: ogSensorMib.setContactInfo('Opengear Inc.\n\t\t 630 West 9560 South,\n\t\t Sandy, UT 84070\n\t\t support@opengear.com')
if mibBuilder.loadTexts: ogSensorMib.setDescription('Opengear SENSOR status MIB')
ogSensorMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 13, 10))
ogsensStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 13, 10, 1))
ogsensStatusTable = MibTable((1, 3, 6, 1, 4, 1, 25049, 10, 13, 10, 1, 3), )
if mibBuilder.loadTexts: ogsensStatusTable.setStatus('current')
if mibBuilder.loadTexts: ogsensStatusTable.setDescription('A table of sensor status events generated by this device.')
ogsensStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25049, 10, 13, 10, 1, 3, 1), ).setIndexNames((0, "OG-SENSOR-MIB", "ogsensStatusIndex"))
if mibBuilder.loadTexts: ogsensStatusEntry.setStatus('current')
if mibBuilder.loadTexts: ogsensStatusEntry.setDescription('A sensor status event that was previously generated by this\n                 device. Each entry is indexed by a message index.')
ogsensStatusIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 10, 13, 10, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: ogsensStatusIndex.setStatus('current')
if mibBuilder.loadTexts: ogsensStatusIndex.setDescription('A monotonically increasing integer for the sole\n                 purpose of indexing messages.  When it reaches the\n                 maximum value the agent flushes the table and wraps\n                 the value back to 1.')
ogsensStatusName = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 10, 13, 10, 1, 3, 1, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogsensStatusName.setStatus('current')
if mibBuilder.loadTexts: ogsensStatusName.setDescription('The name of the device pertaining to the status event')
ogsensStatusDevType = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 10, 13, 10, 1, 3, 1, 11), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogsensStatusDevType.setStatus('current')
if mibBuilder.loadTexts: ogsensStatusDevType.setDescription('The type of device pertaining to the status event')
ogsensStatusType = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 10, 13, 10, 1, 3, 1, 12), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogsensStatusType.setStatus('current')
if mibBuilder.loadTexts: ogsensStatusType.setDescription('The type of sensor pertaining to the status event')
ogsensStatusValue = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 10, 13, 10, 1, 3, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogsensStatusValue.setStatus('current')
if mibBuilder.loadTexts: ogsensStatusValue.setDescription('The value of the sensor pertaining to the status event')
ogSensorMibNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 13, 2))
ogsensMibNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 13, 2, 0))
ogsensEventOccurred = NotificationType((1, 3, 6, 1, 4, 1, 25049, 10, 13, 2, 0, 200)).setObjects(("OG-SENSOR-MIB", "ogsensStatusName"), ("OG-SENSOR-MIB", "ogsensStatusDevType"), ("OG-SENSOR-MIB", "ogsensStatusType"), ("OG-SENSOR-MIB", "ogsensStatusValue"))
if mibBuilder.loadTexts: ogsensEventOccurred.setStatus('current')
if mibBuilder.loadTexts: ogsensEventOccurred.setDescription('The notification sent when a sensor status event occurs')
ogSensorMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 13, 3))
ogSensorMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 13, 3, 1))
ogSensorMibGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 13, 3, 2))
ogSensorMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 25049, 10, 13, 3, 1, 1)).setObjects(("OG-SENSOR-MIB", "ogSensorMibGroup"), ("OG-SENSOR-MIB", "ogsensNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ogSensorMibCompliance = ogSensorMibCompliance.setStatus('current')
if mibBuilder.loadTexts: ogSensorMibCompliance.setDescription('The compliance statement for entities which implement\n                the Opengear sensor MIB.')
ogSensorMibGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 25049, 10, 13, 3, 2, 1)).setObjects(("OG-SENSOR-MIB", "ogsensStatusName"), ("OG-SENSOR-MIB", "ogsensStatusDevType"), ("OG-SENSOR-MIB", "ogsensStatusType"), ("OG-SENSOR-MIB", "ogsensStatusValue"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ogSensorMibGroup = ogSensorMibGroup.setStatus('current')
if mibBuilder.loadTexts: ogSensorMibGroup.setDescription('A collection of objects providing the sensor MIB capability.')
ogsensNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 25049, 10, 13, 3, 2, 2)).setObjects(("OG-SENSOR-MIB", "ogsensEventOccurred"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ogsensNotificationsGroup = ogsensNotificationsGroup.setStatus('current')
if mibBuilder.loadTexts: ogsensNotificationsGroup.setDescription('A collection of notification(s) for sensor system.')
mibBuilder.exportSymbols("OG-SENSOR-MIB", ogsensStatusEntry=ogsensStatusEntry, ogsensStatus=ogsensStatus, ogSensorMibConformance=ogSensorMibConformance, ogsensStatusIndex=ogsensStatusIndex, ogsensStatusName=ogsensStatusName, ogsensMibNotifications=ogsensMibNotifications, ogsensStatusValue=ogsensStatusValue, ogSensorMibCompliances=ogSensorMibCompliances, ogsensStatusType=ogsensStatusType, ogSensorMibGroups=ogSensorMibGroups, ogSensorMibCompliance=ogSensorMibCompliance, PYSNMP_MODULE_ID=ogSensorMib, ogSensorMibNotificationPrefix=ogSensorMibNotificationPrefix, ogSensorMib=ogSensorMib, ogsensStatusTable=ogsensStatusTable, ogSensorMibGroup=ogSensorMibGroup, ogsensNotificationsGroup=ogsensNotificationsGroup, ogsensStatusDevType=ogsensStatusDevType, ogSensorMibObjects=ogSensorMibObjects, ogsensEventOccurred=ogsensEventOccurred)
