#
# PySNMP MIB module OG-FAILOVER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/opengear/OG-FAILOVER-MIB
# Produced by pysmi-1.1.3 at Sun Nov 21 00:33:38 2021
# On host fv-az39-63 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ogMgmt, = mibBuilder.importSymbols("OG-SMI-MIB", "ogMgmt")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
TimeTicks, Counter32, Integer32, MibIdentifier, Bits, Gauge32, IpAddress, ObjectIdentity, ModuleIdentity, Unsigned32, NotificationType, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Counter32", "Integer32", "MibIdentifier", "Bits", "Gauge32", "IpAddress", "ObjectIdentity", "ModuleIdentity", "Unsigned32", "NotificationType", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ogFailoverMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 25049, 10, 15))
ogFailoverMib.setRevisions(('2013-08-11 00:00', '2010-03-22 11:27', '2008-11-27 11:40',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ogFailoverMib.setRevisionsDescriptions(('Renamed from OPENGEAR-FAILOVER-MIB to OG-FAILOVER-MIB to\n\t\tfix naming discrepancy.', 'Syntax corrections by Opengear Inc.', 'Initial version.',))
if mibBuilder.loadTexts: ogFailoverMib.setLastUpdated('201308110000Z')
if mibBuilder.loadTexts: ogFailoverMib.setOrganization('Opengear Inc.')
if mibBuilder.loadTexts: ogFailoverMib.setContactInfo('Opengear Inc.\n\t\t630 West 9560 South,\n\t\t Sandy, UT 84070\n\t\t support@opengear.com')
if mibBuilder.loadTexts: ogFailoverMib.setDescription('Opengear network failover MIB')
ogFailoverMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 15, 10))
ogfovrEvent = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 15, 10, 1))
ogfovrEventTable = MibTable((1, 3, 6, 1, 4, 1, 25049, 10, 15, 10, 1, 1), )
if mibBuilder.loadTexts: ogfovrEventTable.setStatus('current')
if mibBuilder.loadTexts: ogfovrEventTable.setDescription('A table of sensor status events generated by this device.')
ogfovrEventEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25049, 10, 15, 10, 1, 1, 1), ).setIndexNames((0, "OG-FAILOVER-MIB", "ogfovrEventIndex"))
if mibBuilder.loadTexts: ogfovrEventEntry.setStatus('current')
if mibBuilder.loadTexts: ogfovrEventEntry.setDescription('A console connection event occuring at this\n                 device. Each entry is indexed by a message index.')
ogfovrEventIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 10, 15, 10, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: ogfovrEventIndex.setStatus('current')
if mibBuilder.loadTexts: ogfovrEventIndex.setDescription('A monotonically increasing integer for the sole\n                 purpose of indexing messages.  When it reaches the\n                 maximum value the agent flushes the table and wraps\n                 the value back to 1.')
ogfovrEventPrimary = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 10, 15, 10, 1, 1, 1, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogfovrEventPrimary.setStatus('current')
if mibBuilder.loadTexts: ogfovrEventPrimary.setDescription('The name of the network interface which failed')
ogfovrEventSecondary = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 10, 15, 10, 1, 1, 1, 11), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogfovrEventSecondary.setStatus('current')
if mibBuilder.loadTexts: ogfovrEventSecondary.setDescription('The name of the network interface which was connected instead')
ogFailoverMibNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 15, 2))
ogfovrMibNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 15, 2, 0))
ogfovrEventOccurred = NotificationType((1, 3, 6, 1, 4, 1, 25049, 10, 15, 2, 0, 200)).setObjects(("OG-FAILOVER-MIB", "ogfovrEventPrimary"), ("OG-FAILOVER-MIB", "ogfovrEventSecondary"))
if mibBuilder.loadTexts: ogfovrEventOccurred.setStatus('current')
if mibBuilder.loadTexts: ogfovrEventOccurred.setDescription('The notification sent when a network failover event occurs')
ogFailoverMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 15, 3))
ogFailoverMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 15, 3, 1))
ogFailoverMibGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 15, 3, 2))
ogFailoverMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 25049, 10, 15, 3, 1, 1)).setObjects(("OG-FAILOVER-MIB", "ogFailoverMibGroup"), ("OG-FAILOVER-MIB", "ogfovrNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ogFailoverMibCompliance = ogFailoverMibCompliance.setStatus('current')
if mibBuilder.loadTexts: ogFailoverMibCompliance.setDescription('The compliance statement for entities which implement\n                the Opengear sensor MIB.')
ogFailoverMibGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 25049, 10, 15, 3, 2, 1)).setObjects(("OG-FAILOVER-MIB", "ogfovrEventPrimary"), ("OG-FAILOVER-MIB", "ogfovrEventSecondary"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ogFailoverMibGroup = ogFailoverMibGroup.setStatus('current')
if mibBuilder.loadTexts: ogFailoverMibGroup.setDescription('A collection of objects providing the sensor MIB capability.')
ogfovrNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 25049, 10, 15, 3, 2, 2)).setObjects(("OG-FAILOVER-MIB", "ogfovrEventOccurred"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ogfovrNotificationsGroup = ogfovrNotificationsGroup.setStatus('current')
if mibBuilder.loadTexts: ogfovrNotificationsGroup.setDescription('A collection of notification(s) for sensor system.')
mibBuilder.exportSymbols("OG-FAILOVER-MIB", ogfovrEventIndex=ogfovrEventIndex, ogFailoverMibObjects=ogFailoverMibObjects, ogFailoverMib=ogFailoverMib, ogFailoverMibGroup=ogFailoverMibGroup, ogfovrEventPrimary=ogfovrEventPrimary, ogfovrEvent=ogfovrEvent, ogfovrEventEntry=ogfovrEventEntry, ogfovrEventSecondary=ogfovrEventSecondary, ogfovrMibNotifications=ogfovrMibNotifications, ogFailoverMibConformance=ogFailoverMibConformance, ogFailoverMibNotificationPrefix=ogFailoverMibNotificationPrefix, ogFailoverMibCompliances=ogFailoverMibCompliances, ogfovrEventTable=ogfovrEventTable, ogFailoverMibGroups=ogFailoverMibGroups, ogFailoverMibCompliance=ogFailoverMibCompliance, ogfovrEventOccurred=ogfovrEventOccurred, ogfovrNotificationsGroup=ogfovrNotificationsGroup, PYSNMP_MODULE_ID=ogFailoverMib)
