#
# PySNMP MIB module ENTITY-STATE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/ENTITY-STATE-MIB
# Produced by pysmi-1.1.0 at Mon Nov 15 18:46:22 2021
# On host fv-az77-248 platform Linux version 5.11.0-1020-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
EntityAlarmStatus, EntityOperState, EntityAdminState, EntityStandbyStatus, EntityUsageState = mibBuilder.importSymbols("ENTITY-STATE-TC-MIB", "EntityAlarmStatus", "EntityOperState", "EntityAdminState", "EntityStandbyStatus", "EntityUsageState")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Gauge32, ModuleIdentity, Bits, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, IpAddress, Integer32, Counter32, mib_2, TimeTicks, ObjectIdentity, NotificationType, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "ModuleIdentity", "Bits", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "IpAddress", "Integer32", "Counter32", "mib-2", "TimeTicks", "ObjectIdentity", "NotificationType", "Counter64")
DisplayString, TextualConvention, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "DateAndTime")
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
mibBuilder.exportSymbols("ENTITY-STATE-MIB", entStateCompliances=entStateCompliances, entStateOperDisabled=entStateOperDisabled, entStateGroup=entStateGroup, entStateStandby=entStateStandby, entStateGroups=entStateGroups, entStateUsage=entStateUsage, entStateConformance=entStateConformance, entityStateMIB=entityStateMIB, entStateAlarm=entStateAlarm, PYSNMP_MODULE_ID=entityStateMIB, entStateCompliance=entStateCompliance, entStateNotificationsGroup=entStateNotificationsGroup, entStateObjects=entStateObjects, entStateLastChanged=entStateLastChanged, entStateEntry=entStateEntry, entStateAdmin=entStateAdmin, entStateNotifications=entStateNotifications, entStateOper=entStateOper, entStateOperEnabled=entStateOperEnabled, entStateTable=entStateTable)
