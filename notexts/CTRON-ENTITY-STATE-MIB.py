#
# PySNMP MIB module CTRON-ENTITY-STATE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-ENTITY-STATE-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 18:01:45 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
EntityAdminState, EntityUsageState, EntityStandbyStatus, EntityAlarmStatus, EntityOperState = mibBuilder.importSymbols("CTRON-ENTITY-STATE-TC-MIB", "EntityAdminState", "EntityUsageState", "EntityStandbyStatus", "EntityAlarmStatus", "EntityOperState")
ctEntityStateMib, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctEntityStateMib")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
ObjectIdentity, ModuleIdentity, Gauge32, MibIdentifier, TimeTicks, Unsigned32, Integer32, Bits, Counter32, Counter64, NotificationType, IpAddress, iso, mib_2, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "ModuleIdentity", "Gauge32", "MibIdentifier", "TimeTicks", "Unsigned32", "Integer32", "Bits", "Counter32", "Counter64", "NotificationType", "IpAddress", "iso", "mib-2", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DateAndTime, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "DisplayString", "TextualConvention")
ctEntityStateMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 52, 4, 2, 31, 1))
ctEntityStateMIB.setRevisions(('2005-01-23 00:00',))
if mibBuilder.loadTexts: ctEntityStateMIB.setLastUpdated('200501230000Z')
if mibBuilder.loadTexts: ctEntityStateMIB.setOrganization('IETF Entity MIB Working Group')
ctEntStateObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 31, 1, 1))
ctEntStateTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 31, 1, 1, 1), )
if mibBuilder.loadTexts: ctEntStateTable.setStatus('current')
ctEntStateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 31, 1, 1, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: ctEntStateEntry.setStatus('current')
ctEntStateLastChanged = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 31, 1, 1, 1, 1, 1), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctEntStateLastChanged.setStatus('current')
ctEntStateAdmin = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 31, 1, 1, 1, 1, 2), EntityAdminState()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctEntStateAdmin.setStatus('current')
ctEntStateOper = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 31, 1, 1, 1, 1, 3), EntityOperState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctEntStateOper.setStatus('current')
ctEntStateUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 31, 1, 1, 1, 1, 4), EntityUsageState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctEntStateUsage.setStatus('current')
ctEntStateAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 31, 1, 1, 1, 1, 5), EntityAlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctEntStateAlarm.setStatus('current')
ctEntStateStandby = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 31, 1, 1, 1, 1, 6), EntityStandbyStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctEntStateStandby.setStatus('current')
ctEntStateNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 31, 1, 0))
ctEntStateOperEnabled = NotificationType((1, 3, 6, 1, 4, 1, 52, 4, 2, 31, 1, 0, 1)).setObjects(("CTRON-ENTITY-STATE-MIB", "ctEntStateAdmin"), ("CTRON-ENTITY-STATE-MIB", "ctEntStateAlarm"))
if mibBuilder.loadTexts: ctEntStateOperEnabled.setStatus('current')
ctEntStateOperDisabled = NotificationType((1, 3, 6, 1, 4, 1, 52, 4, 2, 31, 1, 0, 2)).setObjects(("CTRON-ENTITY-STATE-MIB", "ctEntStateAdmin"), ("CTRON-ENTITY-STATE-MIB", "ctEntStateAlarm"))
if mibBuilder.loadTexts: ctEntStateOperDisabled.setStatus('current')
ctEntStateConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 31, 1, 2))
ctEntStateCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 31, 1, 2, 1))
ctEntStateCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 52, 4, 2, 31, 1, 2, 1, 1)).setObjects(("CTRON-ENTITY-STATE-MIB", "ctEntStateGroup"), ("CTRON-ENTITY-STATE-MIB", "ctEntStateNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ctEntStateCompliance = ctEntStateCompliance.setStatus('current')
ctEntStateGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 31, 1, 2, 2))
ctEntStateGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 52, 4, 2, 31, 1, 2, 2, 1)).setObjects(("CTRON-ENTITY-STATE-MIB", "ctEntStateLastChanged"), ("CTRON-ENTITY-STATE-MIB", "ctEntStateAdmin"), ("CTRON-ENTITY-STATE-MIB", "ctEntStateOper"), ("CTRON-ENTITY-STATE-MIB", "ctEntStateUsage"), ("CTRON-ENTITY-STATE-MIB", "ctEntStateAlarm"), ("CTRON-ENTITY-STATE-MIB", "ctEntStateStandby"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ctEntStateGroup = ctEntStateGroup.setStatus('current')
ctEntStateNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 52, 4, 2, 31, 1, 2, 2, 2)).setObjects(("CTRON-ENTITY-STATE-MIB", "ctEntStateOperEnabled"), ("CTRON-ENTITY-STATE-MIB", "ctEntStateOperDisabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ctEntStateNotificationsGroup = ctEntStateNotificationsGroup.setStatus('current')
mibBuilder.exportSymbols("CTRON-ENTITY-STATE-MIB", ctEntStateAlarm=ctEntStateAlarm, ctEntStateConformance=ctEntStateConformance, ctEntStateLastChanged=ctEntStateLastChanged, ctEntStateOper=ctEntStateOper, ctEntStateGroups=ctEntStateGroups, ctEntStateGroup=ctEntStateGroup, ctEntStateOperEnabled=ctEntStateOperEnabled, ctEntStateOperDisabled=ctEntStateOperDisabled, ctEntStateObjects=ctEntStateObjects, ctEntityStateMIB=ctEntityStateMIB, ctEntStateStandby=ctEntStateStandby, ctEntStateTable=ctEntStateTable, ctEntStateCompliance=ctEntStateCompliance, PYSNMP_MODULE_ID=ctEntityStateMIB, ctEntStateCompliances=ctEntStateCompliances, ctEntStateUsage=ctEntStateUsage, ctEntStateNotificationsGroup=ctEntStateNotificationsGroup, ctEntStateAdmin=ctEntStateAdmin, ctEntStateEntry=ctEntStateEntry, ctEntStateNotifications=ctEntStateNotifications)
