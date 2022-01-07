#
# PySNMP MIB module BCN-HA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/bluecatnetworks/BCN-HA-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:11:28 2022
# On host fv-az36-988 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
bcnServices, = mibBuilder.importSymbols("BCN-SMI-MIB", "bcnServices")
BcnAlarmSeverity, = mibBuilder.importSymbols("BCN-TC-MIB", "BcnAlarmSeverity")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
NotificationType, ObjectIdentity, Bits, Gauge32, Counter32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, iso, IpAddress, TimeTicks, ModuleIdentity, Integer32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "ObjectIdentity", "Bits", "Gauge32", "Counter32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "iso", "IpAddress", "TimeTicks", "ModuleIdentity", "Integer32", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
bcnHaMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 13315, 3, 1, 5, 1))
bcnHaMIB.setRevisions(('2010-12-15 00:00',))
if mibBuilder.loadTexts: bcnHaMIB.setLastUpdated('201012150000Z')
if mibBuilder.loadTexts: bcnHaMIB.setOrganization('BlueCat Networks')
bcnHa = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 1, 5))
bcnHaObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 1, 5, 2))
bcnHaNotification = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 1, 5, 3))
bcnHaConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 1, 5, 4))
bcnHaServiceStatus = ObjectIdentity((1, 3, 6, 1, 4, 1, 13315, 3, 1, 5, 2, 1))
if mibBuilder.loadTexts: bcnHaServiceStatus.setStatus('current')
bcnHaSerOperState = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 1, 5, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("standalone", 1), ("active", 2), ("passive", 3), ("stopped", 4), ("stopping", 5), ("becomingActive", 6), ("becomingPassive", 7), ("fault", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnHaSerOperState.setStatus('current')
bcnHaSerReplicationState = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 1, 5, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notConfigured", 1), ("replicating", 2), ("synchronized", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnHaSerReplicationState.setStatus('current')
bcnHaSerAddressTable = MibTable((1, 3, 6, 1, 4, 1, 13315, 3, 1, 5, 2, 1, 3), )
if mibBuilder.loadTexts: bcnHaSerAddressTable.setStatus('current')
bcnHaSerAddressEntry = MibTableRow((1, 3, 6, 1, 4, 1, 13315, 3, 1, 5, 2, 1, 3, 1), ).setIndexNames((0, "BCN-HA-MIB", "bcnHaSerAddrTableIndex"))
if mibBuilder.loadTexts: bcnHaSerAddressEntry.setStatus('current')
bcnHaSerAddrTableIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 5, 2, 1, 3, 1, 1), Unsigned32())
if mibBuilder.loadTexts: bcnHaSerAddrTableIndex.setStatus('current')
bcnHaSerVirtualAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 5, 2, 1, 3, 1, 2), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnHaSerVirtualAddressType.setStatus('current')
bcnHaSerVirtualAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 5, 2, 1, 3, 1, 3), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnHaSerVirtualAddress.setStatus('current')
bcnHaSerPhysicalAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 5, 2, 1, 3, 1, 4), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnHaSerPhysicalAddressType.setStatus('current')
bcnHaSerPhysicalAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 5, 2, 1, 3, 1, 5), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnHaSerPhysicalAddress.setStatus('current')
bcnHaSerPeerAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 5, 2, 1, 3, 1, 6), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnHaSerPeerAddressType.setStatus('current')
bcnHaSerPeerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 5, 2, 1, 3, 1, 7), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnHaSerPeerAddress.setStatus('current')
bcnHaNotificationEvents = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 1, 5, 3, 0))
bcnHaNotificationData = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 1, 5, 3, 1))
bcnHaAlarmSeverity = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 1, 5, 3, 1, 1), BcnAlarmSeverity()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bcnHaAlarmSeverity.setStatus('current')
bcnHaAlarmInfo = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 1, 5, 3, 1, 2), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bcnHaAlarmInfo.setStatus('current')
bcnHaAlarmNotif = NotificationType((1, 3, 6, 1, 4, 1, 13315, 3, 1, 5, 3, 0, 1)).setObjects(("BCN-HA-MIB", "bcnHaSerOperState"), ("BCN-HA-MIB", "bcnHaAlarmSeverity"), ("BCN-HA-MIB", "bcnHaAlarmInfo"))
if mibBuilder.loadTexts: bcnHaAlarmNotif.setStatus('current')
bcnHaServiceCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 1, 5, 4, 1))
bcnHaServiceGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 1, 5, 4, 2))
bcnHaServiceStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 13315, 3, 1, 5, 4, 2, 1)).setObjects(("BCN-HA-MIB", "bcnHaSerOperState"), ("BCN-HA-MIB", "bcnHaSerReplicationState"), ("BCN-HA-MIB", "bcnHaSerVirtualAddressType"), ("BCN-HA-MIB", "bcnHaSerVirtualAddress"), ("BCN-HA-MIB", "bcnHaSerPhysicalAddressType"), ("BCN-HA-MIB", "bcnHaSerPhysicalAddress"), ("BCN-HA-MIB", "bcnHaSerPeerAddressType"), ("BCN-HA-MIB", "bcnHaSerPeerAddress"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bcnHaServiceStatusGroup = bcnHaServiceStatusGroup.setStatus('current')
bcnHaNotificationEventGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 13315, 3, 1, 5, 4, 2, 2)).setObjects(("BCN-HA-MIB", "bcnHaAlarmNotif"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bcnHaNotificationEventGroup = bcnHaNotificationEventGroup.setStatus('current')
bcnHaNotificationDataGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 13315, 3, 1, 5, 4, 2, 3)).setObjects(("BCN-HA-MIB", "bcnHaAlarmSeverity"), ("BCN-HA-MIB", "bcnHaAlarmInfo"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bcnHaNotificationDataGroup = bcnHaNotificationDataGroup.setStatus('current')
bcnHaStatusCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 13315, 3, 1, 5, 4, 1, 1)).setObjects(("BCN-HA-MIB", "bcnHaServiceStatusGroup"), ("BCN-HA-MIB", "bcnHaNotificationEventGroup"), ("BCN-HA-MIB", "bcnHaNotificationDataGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bcnHaStatusCompliance = bcnHaStatusCompliance.setStatus('current')
mibBuilder.exportSymbols("BCN-HA-MIB", bcnHaSerOperState=bcnHaSerOperState, bcnHaNotificationEvents=bcnHaNotificationEvents, PYSNMP_MODULE_ID=bcnHaMIB, bcnHaServiceStatusGroup=bcnHaServiceStatusGroup, bcnHaSerVirtualAddressType=bcnHaSerVirtualAddressType, bcnHaServiceStatus=bcnHaServiceStatus, bcnHaSerVirtualAddress=bcnHaSerVirtualAddress, bcnHaAlarmSeverity=bcnHaAlarmSeverity, bcnHaNotification=bcnHaNotification, bcnHaNotificationData=bcnHaNotificationData, bcnHaSerReplicationState=bcnHaSerReplicationState, bcnHaConformance=bcnHaConformance, bcnHaServiceCompliances=bcnHaServiceCompliances, bcnHaSerPhysicalAddress=bcnHaSerPhysicalAddress, bcnHaNotificationDataGroup=bcnHaNotificationDataGroup, bcnHaMIB=bcnHaMIB, bcnHaSerPeerAddress=bcnHaSerPeerAddress, bcnHaServiceGroups=bcnHaServiceGroups, bcnHaStatusCompliance=bcnHaStatusCompliance, bcnHaAlarmNotif=bcnHaAlarmNotif, bcnHaSerAddrTableIndex=bcnHaSerAddrTableIndex, bcnHaSerPeerAddressType=bcnHaSerPeerAddressType, bcnHa=bcnHa, bcnHaSerPhysicalAddressType=bcnHaSerPhysicalAddressType, bcnHaAlarmInfo=bcnHaAlarmInfo, bcnHaNotificationEventGroup=bcnHaNotificationEventGroup, bcnHaObjects=bcnHaObjects, bcnHaSerAddressTable=bcnHaSerAddressTable, bcnHaSerAddressEntry=bcnHaSerAddressEntry)
