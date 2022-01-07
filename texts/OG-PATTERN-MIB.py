#
# PySNMP MIB module OG-PATTERN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/opengear/OG-PATTERN-MIB
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
ogPatternMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 25049, 10, 12))
ogPatternMib.setRevisions(('2013-08-11 00:00', '2010-03-22 11:27', '2008-11-27 11:40',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ogPatternMib.setRevisionsDescriptions(('Renamed from OPENGEAR-PATTERN-MIB to OG-PATTERN-MIB to\n\t\tfix naming discrepancy.', 'Syntax corrections by Opengear Inc.', 'Initial version.',))
if mibBuilder.loadTexts: ogPatternMib.setLastUpdated('201308110000Z')
if mibBuilder.loadTexts: ogPatternMib.setOrganization('Opengear Inc.')
if mibBuilder.loadTexts: ogPatternMib.setContactInfo('Opengear Inc.\n\t\t 630 West 9560 South,\n\t\t Sandy, UT 84070\n\t\t support@opengear.com')
if mibBuilder.loadTexts: ogPatternMib.setDescription('Opengear console pattern matching MIB')
ogPatternMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 12, 10))
ogpatnEvent = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 12, 10, 1))
ogpatnEventTable = MibTable((1, 3, 6, 1, 4, 1, 25049, 10, 12, 10, 1, 1), )
if mibBuilder.loadTexts: ogpatnEventTable.setStatus('current')
if mibBuilder.loadTexts: ogpatnEventTable.setDescription('A table of sensor status events generated by this device.')
ogpatnEventEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25049, 10, 12, 10, 1, 1, 1), ).setIndexNames((0, "OG-PATTERN-MIB", "ogpatnEventIndex"))
if mibBuilder.loadTexts: ogpatnEventEntry.setStatus('current')
if mibBuilder.loadTexts: ogpatnEventEntry.setDescription('A console connection event occuring at this\n                 device. Each entry is indexed by a message index.')
ogpatnEventIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 10, 12, 10, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: ogpatnEventIndex.setStatus('current')
if mibBuilder.loadTexts: ogpatnEventIndex.setDescription('A monotonically increasing integer for the sole\n                 purpose of indexing messages.  When it reaches the\n                 maximum value the agent flushes the table and wraps\n                 the value back to 1.')
ogpatnEventDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 10, 12, 10, 1, 1, 1, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogpatnEventDescription.setStatus('current')
if mibBuilder.loadTexts: ogpatnEventDescription.setDescription('A description of the matches purpose')
ogpatnEventText = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 10, 12, 10, 1, 1, 1, 11), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogpatnEventText.setStatus('current')
if mibBuilder.loadTexts: ogpatnEventText.setDescription('The full text which matched the pattern')
ogpatnEventPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 10, 12, 10, 1, 1, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogpatnEventPortNumber.setStatus('current')
if mibBuilder.loadTexts: ogpatnEventPortNumber.setDescription('Serial port number on which the pattern matched')
ogpatnEventPortLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 10, 12, 10, 1, 1, 1, 13), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogpatnEventPortLabel.setStatus('current')
if mibBuilder.loadTexts: ogpatnEventPortLabel.setDescription('The label for the serial port where pattern matched occurred')
ogPatternMibNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 12, 2))
ogpatnMibNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 12, 2, 0))
ogpatnEventOccurred = NotificationType((1, 3, 6, 1, 4, 1, 25049, 10, 12, 2, 0, 200)).setObjects(("OG-PATTERN-MIB", "ogpatnEventDescription"), ("OG-PATTERN-MIB", "ogpatnEventText"), ("OG-PATTERN-MIB", "ogpatnEventPortNumber"), ("OG-PATTERN-MIB", "ogpatnEventPortLabel"))
if mibBuilder.loadTexts: ogpatnEventOccurred.setStatus('current')
if mibBuilder.loadTexts: ogpatnEventOccurred.setDescription('An alert sent when a pre-defined pattern was\n\t\tmatched text in a consoles serial character stream')
ogPatternMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 12, 3))
ogPatternMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 12, 3, 1))
ogPatternMibGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 12, 3, 2))
ogPatternMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 25049, 10, 12, 3, 1, 1)).setObjects(("OG-PATTERN-MIB", "ogPatternMibGroup"), ("OG-PATTERN-MIB", "ogpatnNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ogPatternMibCompliance = ogPatternMibCompliance.setStatus('current')
if mibBuilder.loadTexts: ogPatternMibCompliance.setDescription('The compliance statement for entities which implement\n                the Opengear Pattern MIB.')
ogPatternMibGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 25049, 10, 12, 3, 2, 1)).setObjects(("OG-PATTERN-MIB", "ogpatnEventDescription"), ("OG-PATTERN-MIB", "ogpatnEventText"), ("OG-PATTERN-MIB", "ogpatnEventPortNumber"), ("OG-PATTERN-MIB", "ogpatnEventPortLabel"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ogPatternMibGroup = ogPatternMibGroup.setStatus('current')
if mibBuilder.loadTexts: ogPatternMibGroup.setDescription('A collection of objects providing the sensor MIB capability.')
ogpatnNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 25049, 10, 12, 3, 2, 2)).setObjects(("OG-PATTERN-MIB", "ogpatnEventOccurred"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ogpatnNotificationsGroup = ogpatnNotificationsGroup.setStatus('current')
if mibBuilder.loadTexts: ogpatnNotificationsGroup.setDescription('A collection of notification(s) for sensor system.')
mibBuilder.exportSymbols("OG-PATTERN-MIB", ogpatnEventEntry=ogpatnEventEntry, ogPatternMibGroup=ogPatternMibGroup, ogpatnNotificationsGroup=ogpatnNotificationsGroup, ogPatternMibConformance=ogPatternMibConformance, ogpatnEventIndex=ogpatnEventIndex, ogPatternMibCompliance=ogPatternMibCompliance, ogpatnEventTable=ogpatnEventTable, PYSNMP_MODULE_ID=ogPatternMib, ogpatnEventOccurred=ogpatnEventOccurred, ogpatnEventText=ogpatnEventText, ogPatternMibNotificationPrefix=ogPatternMibNotificationPrefix, ogPatternMib=ogPatternMib, ogpatnEvent=ogpatnEvent, ogpatnEventPortLabel=ogpatnEventPortLabel, ogPatternMibCompliances=ogPatternMibCompliances, ogPatternMibGroups=ogPatternMibGroups, ogPatternMibObjects=ogPatternMibObjects, ogpatnMibNotifications=ogpatnMibNotifications, ogpatnEventPortNumber=ogpatnEventPortNumber, ogpatnEventDescription=ogpatnEventDescription)
