#
# PySNMP MIB module OG-HOST-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/opengear/OG-HOST-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:33:34 2022
# On host fv-az36-988 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
ogMgmt, = mibBuilder.importSymbols("OG-SMI-MIB", "ogMgmt")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Counter64, Gauge32, Unsigned32, NotificationType, Counter32, IpAddress, ObjectIdentity, TimeTicks, MibIdentifier, ModuleIdentity, Bits, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Counter64", "Gauge32", "Unsigned32", "NotificationType", "Counter32", "IpAddress", "ObjectIdentity", "TimeTicks", "MibIdentifier", "ModuleIdentity", "Bits", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ogHostMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 25049, 10, 14))
ogHostMib.setRevisions(('2013-08-11 00:00', '2010-03-22 11:27', '2008-11-27 11:40',))
if mibBuilder.loadTexts: ogHostMib.setLastUpdated('201308110000Z')
if mibBuilder.loadTexts: ogHostMib.setOrganization('Opengear Inc.')
ogHostMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 14, 10))
oghostEvent = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 14, 10, 1))
oghostEventTable = MibTable((1, 3, 6, 1, 4, 1, 25049, 10, 14, 10, 1, 1), )
if mibBuilder.loadTexts: oghostEventTable.setStatus('current')
oghostEventEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25049, 10, 14, 10, 1, 1, 1), ).setIndexNames((0, "OG-HOST-MIB", "oghostEventIndex"))
if mibBuilder.loadTexts: oghostEventEntry.setStatus('current')
oghostEventIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 10, 14, 10, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: oghostEventIndex.setStatus('current')
oghostEventUsername = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 10, 14, 10, 1, 1, 1, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oghostEventUsername.setStatus('current')
oghostEventType = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 10, 14, 10, 1, 1, 1, 11), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oghostEventType.setStatus('current')
oghostEventAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 10, 14, 10, 1, 1, 1, 12), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oghostEventAddress.setStatus('current')
oghostEventDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 10, 14, 10, 1, 1, 1, 13), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oghostEventDescription.setStatus('current')
oghostEventProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 10, 14, 10, 1, 1, 1, 14), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oghostEventProtocol.setStatus('current')
oghostEventPort = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 10, 14, 10, 1, 1, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oghostEventPort.setStatus('current')
ogHostMibNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 14, 2))
oghostMibNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 14, 2, 0))
oghostEventOccurred = NotificationType((1, 3, 6, 1, 4, 1, 25049, 10, 14, 2, 0, 200)).setObjects(("OG-HOST-MIB", "oghostEventUsername"), ("OG-HOST-MIB", "oghostEventType"), ("OG-HOST-MIB", "oghostEventAddress"), ("OG-HOST-MIB", "oghostEventDescription"), ("OG-HOST-MIB", "oghostEventProtocol"), ("OG-HOST-MIB", "oghostEventPort"))
if mibBuilder.loadTexts: oghostEventOccurred.setStatus('current')
ogHostMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 14, 3))
ogHostMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 14, 3, 1))
ogHostMibGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 14, 3, 2))
ogHostMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 25049, 10, 14, 3, 1, 1)).setObjects(("OG-HOST-MIB", "ogHostMibGroup"), ("OG-HOST-MIB", "oghostNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ogHostMibCompliance = ogHostMibCompliance.setStatus('current')
ogHostMibGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 25049, 10, 14, 3, 2, 1)).setObjects(("OG-HOST-MIB", "oghostEventUsername"), ("OG-HOST-MIB", "oghostEventType"), ("OG-HOST-MIB", "oghostEventAddress"), ("OG-HOST-MIB", "oghostEventDescription"), ("OG-HOST-MIB", "oghostEventProtocol"), ("OG-HOST-MIB", "oghostEventPort"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ogHostMibGroup = ogHostMibGroup.setStatus('current')
oghostNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 25049, 10, 14, 3, 2, 2)).setObjects(("OG-HOST-MIB", "oghostEventOccurred"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    oghostNotificationsGroup = oghostNotificationsGroup.setStatus('current')
mibBuilder.exportSymbols("OG-HOST-MIB", oghostEventType=oghostEventType, ogHostMibCompliance=ogHostMibCompliance, ogHostMibGroup=ogHostMibGroup, oghostEventAddress=oghostEventAddress, oghostEventPort=oghostEventPort, oghostMibNotifications=oghostMibNotifications, PYSNMP_MODULE_ID=ogHostMib, ogHostMibNotificationPrefix=ogHostMibNotificationPrefix, oghostNotificationsGroup=oghostNotificationsGroup, oghostEventProtocol=oghostEventProtocol, ogHostMibConformance=ogHostMibConformance, oghostEventTable=oghostEventTable, oghostEventIndex=oghostEventIndex, ogHostMibObjects=ogHostMibObjects, oghostEvent=oghostEvent, ogHostMib=ogHostMib, oghostEventDescription=oghostEventDescription, oghostEventEntry=oghostEventEntry, oghostEventUsername=oghostEventUsername, ogHostMibGroups=ogHostMibGroups, ogHostMibCompliances=ogHostMibCompliances, oghostEventOccurred=oghostEventOccurred)
