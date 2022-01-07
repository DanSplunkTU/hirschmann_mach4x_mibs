#
# PySNMP MIB module OG-UPS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/opengear/OG-UPS-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:21:34 2022
# On host fv-az135-792 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ogMgmt, = mibBuilder.importSymbols("OG-SMI-MIB", "ogMgmt")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
iso, NotificationType, ObjectIdentity, TimeTicks, MibIdentifier, Unsigned32, Integer32, Gauge32, Counter32, Counter64, IpAddress, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "NotificationType", "ObjectIdentity", "TimeTicks", "MibIdentifier", "Unsigned32", "Integer32", "Gauge32", "Counter32", "Counter64", "IpAddress", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ogNetUpsMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 25049, 10, 16))
ogNetUpsMib.setRevisions(('2013-08-11 00:00', '2010-03-22 11:27', '2008-06-13 11:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ogNetUpsMib.setRevisionsDescriptions(('Renamed from OPENGEAR-UPS-MIB to OG-UPS-MIB to\nfix naming discrepancy.', 'Syntax corrections by Opengear Inc.', 'Initial version.',))
if mibBuilder.loadTexts: ogNetUpsMib.setLastUpdated('201308110000Z')
if mibBuilder.loadTexts: ogNetUpsMib.setOrganization('Opengear Inc.')
if mibBuilder.loadTexts: ogNetUpsMib.setContactInfo('Opengear Inc.\n630 West 9560 South,\nSandy, UT 84070\nsupport@opengear.com')
if mibBuilder.loadTexts: ogNetUpsMib.setDescription('Opengear UPS status MIB')
ogNetUpsMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 16, 10))
ognupsEvent = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 16, 10, 1))
ognupsEventTable = MibTable((1, 3, 6, 1, 4, 1, 25049, 10, 16, 10, 1, 1), )
if mibBuilder.loadTexts: ognupsEventTable.setStatus('current')
if mibBuilder.loadTexts: ognupsEventTable.setDescription('A table of serial signal events generated by this device.')
ognupsEventEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25049, 10, 16, 10, 1, 1, 1), ).setIndexNames((0, "OG-UPS-MIB", "ognupsEventIndex"))
if mibBuilder.loadTexts: ognupsEventEntry.setStatus('current')
if mibBuilder.loadTexts: ognupsEventEntry.setDescription('A console connection event occuring at this\n                 device. Each entry is indexed by a message index.')
ognupsEventIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 10, 16, 10, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: ognupsEventIndex.setStatus('current')
if mibBuilder.loadTexts: ognupsEventIndex.setDescription('A monotonically increasing integer for the sole\n                 purpose of indexing messages.  When it reaches the\n                 maximum value the agent flushes the table and wraps\n                 the value back to 1.')
ognupsEventName = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 10, 16, 10, 1, 1, 1, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ognupsEventName.setStatus('current')
if mibBuilder.loadTexts: ognupsEventName.setDescription('The name of the UPS pertaining to the status event')
ognupsEventType = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 10, 16, 10, 1, 1, 1, 11), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ognupsEventType.setStatus('current')
if mibBuilder.loadTexts: ognupsEventType.setDescription('The type of status event')
ogNetUpsMibNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 16, 2))
ognupsMibNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 16, 2, 0))
ognupsEventOccurred = NotificationType((1, 3, 6, 1, 4, 1, 25049, 10, 16, 2, 0, 200)).setObjects(("OG-UPS-MIB", "ognupsEventName"), ("OG-UPS-MIB", "ognupsEventType"))
if mibBuilder.loadTexts: ognupsEventOccurred.setStatus('current')
if mibBuilder.loadTexts: ognupsEventOccurred.setDescription('The notification sent when a UPS status event occurs')
ogNetUpsMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 16, 3))
ogNetUpsMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 16, 3, 1))
ogNetUpsMibGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 16, 3, 2))
ogNetUpsMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 25049, 10, 16, 3, 1, 1)).setObjects(("OG-UPS-MIB", "ogNetUpsMibGroup"), ("OG-UPS-MIB", "ognupsNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ogNetUpsMibCompliance = ogNetUpsMibCompliance.setStatus('current')
if mibBuilder.loadTexts: ogNetUpsMibCompliance.setDescription('The compliance statement for entities which implement\n                the Opengear UPS MIB.')
ogNetUpsMibGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 25049, 10, 16, 3, 2, 1)).setObjects(("OG-UPS-MIB", "ognupsEventName"), ("OG-UPS-MIB", "ognupsEventType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ogNetUpsMibGroup = ogNetUpsMibGroup.setStatus('current')
if mibBuilder.loadTexts: ogNetUpsMibGroup.setDescription('A collection of objects providing the sensor MIB capability.')
ognupsNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 25049, 10, 16, 3, 2, 2)).setObjects(("OG-UPS-MIB", "ognupsEventOccurred"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ognupsNotificationsGroup = ognupsNotificationsGroup.setStatus('current')
if mibBuilder.loadTexts: ognupsNotificationsGroup.setDescription('A collection of notification(s) for sensor system.')
mibBuilder.exportSymbols("OG-UPS-MIB", ogNetUpsMibCompliances=ogNetUpsMibCompliances, ogNetUpsMibGroups=ogNetUpsMibGroups, ognupsNotificationsGroup=ognupsNotificationsGroup, ogNetUpsMib=ogNetUpsMib, ogNetUpsMibGroup=ogNetUpsMibGroup, ogNetUpsMibObjects=ogNetUpsMibObjects, ognupsEventEntry=ognupsEventEntry, ognupsEventIndex=ognupsEventIndex, ogNetUpsMibCompliance=ogNetUpsMibCompliance, PYSNMP_MODULE_ID=ogNetUpsMib, ognupsEventName=ognupsEventName, ognupsMibNotifications=ognupsMibNotifications, ognupsEventTable=ognupsEventTable, ogNetUpsMibNotificationPrefix=ogNetUpsMibNotificationPrefix, ogNetUpsMibConformance=ogNetUpsMibConformance, ognupsEventType=ognupsEventType, ognupsEvent=ognupsEvent, ognupsEventOccurred=ognupsEventOccurred)
