#
# PySNMP MIB module ENTITY-STATE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/output/asn1/ENTITY-STATE-MIB
# Produced by pysmi-1.1.8 at Mon Feb  7 16:07:33 2022
# On host fv-az42-619 platform Linux version 5.11.0-1028-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
EntityAlarmStatus, EntityOperState, EntityUsageState, EntityAdminState, EntityStandbyStatus = mibBuilder.importSymbols("ENTITY-STATE-TC-MIB", "EntityAlarmStatus", "EntityOperState", "EntityUsageState", "EntityAdminState", "EntityStandbyStatus")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
iso, Gauge32, IpAddress, ObjectIdentity, NotificationType, Unsigned32, Counter64, mib_2, MibIdentifier, TimeTicks, Integer32, Bits, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Gauge32", "IpAddress", "ObjectIdentity", "NotificationType", "Unsigned32", "Counter64", "mib-2", "MibIdentifier", "TimeTicks", "Integer32", "Bits", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32")
DateAndTime, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "TextualConvention", "DisplayString")
entityStateMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 131))
entityStateMIB.setRevisions(('2005-11-22 00:00',))
if mibBuilder.loadTexts: entityStateMIB.setLastUpdated('200511220000Z')
if mibBuilder.loadTexts: entityStateMIB.setOrganization('IETF Entity MIB Working Group')
entStateObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 131, 1))
entStateTable = MibTable((1, 3, 6, 1, 2, 1, 131, 1, 1), )
if mibBuilder.loadTexts: entStateTable.setStatus('current')
entStateEntry = MibTableRow((1, 3, 6, 1, 2, 1, 131, 1, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: entStateEntry.setStatus('current')
entStateLastChanged = MibTableColumn((1, 3, 6, 1, 2, 1, 131, 1, 1, 1, 1), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entStateLastChanged.setStatus('current')
entStateAdmin = MibTableColumn((1, 3, 6, 1, 2, 1, 131, 1, 1, 1, 2), EntityAdminState()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: entStateAdmin.setStatus('current')
entStateOper = MibTableColumn((1, 3, 6, 1, 2, 1, 131, 1, 1, 1, 3), EntityOperState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entStateOper.setStatus('current')
entStateUsage = MibTableColumn((1, 3, 6, 1, 2, 1, 131, 1, 1, 1, 4), EntityUsageState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entStateUsage.setStatus('current')
entStateAlarm = MibTableColumn((1, 3, 6, 1, 2, 1, 131, 1, 1, 1, 5), EntityAlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entStateAlarm.setStatus('current')
entStateStandby = MibTableColumn((1, 3, 6, 1, 2, 1, 131, 1, 1, 1, 6), EntityStandbyStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entStateStandby.setStatus('current')
entStateNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 131, 0))
entStateOperEnabled = NotificationType((1, 3, 6, 1, 2, 1, 131, 0, 1)).setObjects(("ENTITY-STATE-MIB", "entStateAdmin"), ("ENTITY-STATE-MIB", "entStateAlarm"))
if mibBuilder.loadTexts: entStateOperEnabled.setStatus('current')
entStateOperDisabled = NotificationType((1, 3, 6, 1, 2, 1, 131, 0, 2)).setObjects(("ENTITY-STATE-MIB", "entStateAdmin"), ("ENTITY-STATE-MIB", "entStateAlarm"))
if mibBuilder.loadTexts: entStateOperDisabled.setStatus('current')
entStateConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 131, 2))
entStateCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 131, 2, 1))
entStateCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 131, 2, 1, 1)).setObjects(("ENTITY-STATE-MIB", "entStateGroup"), ("ENTITY-STATE-MIB", "entStateNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    entStateCompliance = entStateCompliance.setStatus('current')
entStateGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 131, 2, 2))
entStateGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 131, 2, 2, 1)).setObjects(("ENTITY-STATE-MIB", "entStateLastChanged"), ("ENTITY-STATE-MIB", "entStateAdmin"), ("ENTITY-STATE-MIB", "entStateOper"), ("ENTITY-STATE-MIB", "entStateUsage"), ("ENTITY-STATE-MIB", "entStateAlarm"), ("ENTITY-STATE-MIB", "entStateStandby"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    entStateGroup = entStateGroup.setStatus('current')
entStateNotificationsGroup = NotificationGroup((1, 3, 6, 1, 2, 1, 131, 2, 2, 2)).setObjects(("ENTITY-STATE-MIB", "entStateOperEnabled"), ("ENTITY-STATE-MIB", "entStateOperDisabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    entStateNotificationsGroup = entStateNotificationsGroup.setStatus('current')
mibBuilder.exportSymbols("ENTITY-STATE-MIB", entStateAlarm=entStateAlarm, entStateOper=entStateOper, entStateNotifications=entStateNotifications, entStateObjects=entStateObjects, entStateNotificationsGroup=entStateNotificationsGroup, entStateConformance=entStateConformance, entStateAdmin=entStateAdmin, entStateEntry=entStateEntry, entStateLastChanged=entStateLastChanged, entStateUsage=entStateUsage, PYSNMP_MODULE_ID=entityStateMIB, entStateOperDisabled=entStateOperDisabled, entStateGroups=entStateGroups, entStateOperEnabled=entStateOperEnabled, entStateCompliances=entStateCompliances, entStateGroup=entStateGroup, entStateTable=entStateTable, entityStateMIB=entityStateMIB, entStateCompliance=entStateCompliance, entStateStandby=entStateStandby)
