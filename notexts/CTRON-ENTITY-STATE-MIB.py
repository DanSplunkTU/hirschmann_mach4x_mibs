#
# PySNMP MIB module CTRON-ENTITY-STATE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-ENTITY-STATE-MIB
# Produced by pysmi-1.1.8 at Mon Feb  7 16:12:01 2022
# On host fv-az42-619 platform Linux version 5.11.0-1028-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
EntityStandbyStatus, EntityAlarmStatus, EntityUsageState, EntityOperState, EntityAdminState = mibBuilder.importSymbols("CTRON-ENTITY-STATE-TC-MIB", "EntityStandbyStatus", "EntityAlarmStatus", "EntityUsageState", "EntityOperState", "EntityAdminState")
ctEntityStateMib, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctEntityStateMib")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Integer32, TimeTicks, Unsigned32, Bits, ObjectIdentity, ModuleIdentity, NotificationType, iso, MibIdentifier, Counter64, Gauge32, Counter32, IpAddress, mib_2, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "TimeTicks", "Unsigned32", "Bits", "ObjectIdentity", "ModuleIdentity", "NotificationType", "iso", "MibIdentifier", "Counter64", "Gauge32", "Counter32", "IpAddress", "mib-2", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "DateAndTime")
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
mibBuilder.exportSymbols("CTRON-ENTITY-STATE-MIB", PYSNMP_MODULE_ID=ctEntityStateMIB, ctEntStateAlarm=ctEntStateAlarm, ctEntStateGroups=ctEntStateGroups, ctEntStateCompliance=ctEntStateCompliance, ctEntStateConformance=ctEntStateConformance, ctEntStateCompliances=ctEntStateCompliances, ctEntStateNotifications=ctEntStateNotifications, ctEntStateAdmin=ctEntStateAdmin, ctEntStateOperDisabled=ctEntStateOperDisabled, ctEntStateEntry=ctEntStateEntry, ctEntStateOperEnabled=ctEntStateOperEnabled, ctEntStateNotificationsGroup=ctEntStateNotificationsGroup, ctEntStateGroup=ctEntStateGroup, ctEntStateTable=ctEntStateTable, ctEntStateStandby=ctEntStateStandby, ctEntStateObjects=ctEntStateObjects, ctEntityStateMIB=ctEntityStateMIB, ctEntStateLastChanged=ctEntStateLastChanged, ctEntStateOper=ctEntStateOper, ctEntStateUsage=ctEntStateUsage)
