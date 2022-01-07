#
# PySNMP MIB module DISMAN-SCHEDULE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/DISMAN-SCHEDULE-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:07:39 2022
# On host fv-az36-988 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
MibIdentifier, ObjectIdentity, ModuleIdentity, Unsigned32, iso, zeroDotZero, TimeTicks, Gauge32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, mib_2, Bits, NotificationType, IpAddress, Counter64, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "ObjectIdentity", "ModuleIdentity", "Unsigned32", "iso", "zeroDotZero", "TimeTicks", "Gauge32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "mib-2", "Bits", "NotificationType", "IpAddress", "Counter64", "Counter32")
RowStatus, StorageType, DateAndTime, DisplayString, TextualConvention, VariablePointer = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "StorageType", "DateAndTime", "DisplayString", "TextualConvention", "VariablePointer")
schedMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 63))
schedMIB.setRevisions(('2002-01-07 00:00', '1998-11-17 18:00',))
if mibBuilder.loadTexts: schedMIB.setLastUpdated('200201070000Z')
if mibBuilder.loadTexts: schedMIB.setOrganization('IETF Distributed Management Working Group')
schedObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 63, 1))
schedNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 63, 2))
schedConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 63, 3))
class SnmpPduErrorStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18))
    namedValues = NamedValues(("noResponse", -1), ("noError", 0), ("tooBig", 1), ("noSuchName", 2), ("badValue", 3), ("readOnly", 4), ("genErr", 5), ("noAccess", 6), ("wrongType", 7), ("wrongLength", 8), ("wrongEncoding", 9), ("wrongValue", 10), ("noCreation", 11), ("inconsistentValue", 12), ("resourceUnavailable", 13), ("commitFailed", 14), ("undoFailed", 15), ("authorizationError", 16), ("notWritable", 17), ("inconsistentName", 18))

schedLocalTime = MibScalar((1, 3, 6, 1, 2, 1, 63, 1, 1), DateAndTime().subtype(subtypeSpec=ValueSizeConstraint(11, 11)).setFixedLength(11)).setMaxAccess("readonly")
if mibBuilder.loadTexts: schedLocalTime.setStatus('current')
schedTable = MibTable((1, 3, 6, 1, 2, 1, 63, 1, 2), )
if mibBuilder.loadTexts: schedTable.setStatus('current')
schedEntry = MibTableRow((1, 3, 6, 1, 2, 1, 63, 1, 2, 1), ).setIndexNames((0, "DISMAN-SCHEDULE-MIB", "schedOwner"), (0, "DISMAN-SCHEDULE-MIB", "schedName"))
if mibBuilder.loadTexts: schedEntry.setStatus('current')
schedOwner = MibTableColumn((1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32)))
if mibBuilder.loadTexts: schedOwner.setStatus('current')
schedName = MibTableColumn((1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: schedName.setStatus('current')
schedDescr = MibTableColumn((1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 3), SnmpAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: schedDescr.setStatus('current')
schedInterval = MibTableColumn((1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 4), Unsigned32()).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: schedInterval.setStatus('current')
schedWeekDay = MibTableColumn((1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 5), Bits().clone(namedValues=NamedValues(("sunday", 0), ("monday", 1), ("tuesday", 2), ("wednesday", 3), ("thursday", 4), ("friday", 5), ("saturday", 6)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: schedWeekDay.setStatus('current')
schedMonth = MibTableColumn((1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 6), Bits().clone(namedValues=NamedValues(("january", 0), ("february", 1), ("march", 2), ("april", 3), ("may", 4), ("june", 5), ("july", 6), ("august", 7), ("september", 8), ("october", 9), ("november", 10), ("december", 11)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: schedMonth.setStatus('current')
schedDay = MibTableColumn((1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 7), Bits().clone(namedValues=NamedValues(("d1", 0), ("d2", 1), ("d3", 2), ("d4", 3), ("d5", 4), ("d6", 5), ("d7", 6), ("d8", 7), ("d9", 8), ("d10", 9), ("d11", 10), ("d12", 11), ("d13", 12), ("d14", 13), ("d15", 14), ("d16", 15), ("d17", 16), ("d18", 17), ("d19", 18), ("d20", 19), ("d21", 20), ("d22", 21), ("d23", 22), ("d24", 23), ("d25", 24), ("d26", 25), ("d27", 26), ("d28", 27), ("d29", 28), ("d30", 29), ("d31", 30), ("r1", 31), ("r2", 32), ("r3", 33), ("r4", 34), ("r5", 35), ("r6", 36), ("r7", 37), ("r8", 38), ("r9", 39), ("r10", 40), ("r11", 41), ("r12", 42), ("r13", 43), ("r14", 44), ("r15", 45), ("r16", 46), ("r17", 47), ("r18", 48), ("r19", 49), ("r20", 50), ("r21", 51), ("r22", 52), ("r23", 53), ("r24", 54), ("r25", 55), ("r26", 56), ("r27", 57), ("r28", 58), ("r29", 59), ("r30", 60), ("r31", 61)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: schedDay.setStatus('current')
schedHour = MibTableColumn((1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 8), Bits().clone(namedValues=NamedValues(("h0", 0), ("h1", 1), ("h2", 2), ("h3", 3), ("h4", 4), ("h5", 5), ("h6", 6), ("h7", 7), ("h8", 8), ("h9", 9), ("h10", 10), ("h11", 11), ("h12", 12), ("h13", 13), ("h14", 14), ("h15", 15), ("h16", 16), ("h17", 17), ("h18", 18), ("h19", 19), ("h20", 20), ("h21", 21), ("h22", 22), ("h23", 23)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: schedHour.setStatus('current')
schedMinute = MibTableColumn((1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 9), Bits().clone(namedValues=NamedValues(("m0", 0), ("m1", 1), ("m2", 2), ("m3", 3), ("m4", 4), ("m5", 5), ("m6", 6), ("m7", 7), ("m8", 8), ("m9", 9), ("m10", 10), ("m11", 11), ("m12", 12), ("m13", 13), ("m14", 14), ("m15", 15), ("m16", 16), ("m17", 17), ("m18", 18), ("m19", 19), ("m20", 20), ("m21", 21), ("m22", 22), ("m23", 23), ("m24", 24), ("m25", 25), ("m26", 26), ("m27", 27), ("m28", 28), ("m29", 29), ("m30", 30), ("m31", 31), ("m32", 32), ("m33", 33), ("m34", 34), ("m35", 35), ("m36", 36), ("m37", 37), ("m38", 38), ("m39", 39), ("m40", 40), ("m41", 41), ("m42", 42), ("m43", 43), ("m44", 44), ("m45", 45), ("m46", 46), ("m47", 47), ("m48", 48), ("m49", 49), ("m50", 50), ("m51", 51), ("m52", 52), ("m53", 53), ("m54", 54), ("m55", 55), ("m56", 56), ("m57", 57), ("m58", 58), ("m59", 59)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: schedMinute.setStatus('current')
schedContextName = MibTableColumn((1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 10), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: schedContextName.setStatus('current')
schedVariable = MibTableColumn((1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 11), VariablePointer().clone((0, 0))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: schedVariable.setStatus('current')
schedValue = MibTableColumn((1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 12), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: schedValue.setStatus('current')
schedType = MibTableColumn((1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("periodic", 1), ("calendar", 2), ("oneshot", 3))).clone('periodic')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: schedType.setStatus('current')
schedAdminStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: schedAdminStatus.setStatus('current')
schedOperStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ("finished", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: schedOperStatus.setStatus('current')
schedFailures = MibTableColumn((1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: schedFailures.setStatus('current')
schedLastFailure = MibTableColumn((1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 17), SnmpPduErrorStatus().clone('noError')).setMaxAccess("readonly")
if mibBuilder.loadTexts: schedLastFailure.setStatus('current')
schedLastFailed = MibTableColumn((1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 18), DateAndTime().clone(hexValue="0000000000000000")).setMaxAccess("readonly")
if mibBuilder.loadTexts: schedLastFailed.setStatus('current')
schedStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 19), StorageType().clone('volatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: schedStorageType.setStatus('current')
schedRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 20), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: schedRowStatus.setStatus('current')
schedTriggers = MibTableColumn((1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: schedTriggers.setStatus('current')
schedTraps = MibIdentifier((1, 3, 6, 1, 2, 1, 63, 2, 0))
schedActionFailure = NotificationType((1, 3, 6, 1, 2, 1, 63, 2, 0, 1)).setObjects(("DISMAN-SCHEDULE-MIB", "schedLastFailure"), ("DISMAN-SCHEDULE-MIB", "schedLastFailed"))
if mibBuilder.loadTexts: schedActionFailure.setStatus('current')
schedCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 63, 3, 1))
schedGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 63, 3, 2))
schedCompliance2 = ModuleCompliance((1, 3, 6, 1, 2, 1, 63, 3, 1, 2)).setObjects(("DISMAN-SCHEDULE-MIB", "schedGroup2"), ("DISMAN-SCHEDULE-MIB", "schedNotificationsGroup"), ("DISMAN-SCHEDULE-MIB", "schedCalendarGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    schedCompliance2 = schedCompliance2.setStatus('current')
schedGroup2 = ObjectGroup((1, 3, 6, 1, 2, 1, 63, 3, 2, 4)).setObjects(("DISMAN-SCHEDULE-MIB", "schedDescr"), ("DISMAN-SCHEDULE-MIB", "schedInterval"), ("DISMAN-SCHEDULE-MIB", "schedContextName"), ("DISMAN-SCHEDULE-MIB", "schedVariable"), ("DISMAN-SCHEDULE-MIB", "schedValue"), ("DISMAN-SCHEDULE-MIB", "schedType"), ("DISMAN-SCHEDULE-MIB", "schedAdminStatus"), ("DISMAN-SCHEDULE-MIB", "schedOperStatus"), ("DISMAN-SCHEDULE-MIB", "schedFailures"), ("DISMAN-SCHEDULE-MIB", "schedLastFailure"), ("DISMAN-SCHEDULE-MIB", "schedLastFailed"), ("DISMAN-SCHEDULE-MIB", "schedStorageType"), ("DISMAN-SCHEDULE-MIB", "schedRowStatus"), ("DISMAN-SCHEDULE-MIB", "schedTriggers"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    schedGroup2 = schedGroup2.setStatus('current')
schedCalendarGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 63, 3, 2, 2)).setObjects(("DISMAN-SCHEDULE-MIB", "schedLocalTime"), ("DISMAN-SCHEDULE-MIB", "schedWeekDay"), ("DISMAN-SCHEDULE-MIB", "schedMonth"), ("DISMAN-SCHEDULE-MIB", "schedDay"), ("DISMAN-SCHEDULE-MIB", "schedHour"), ("DISMAN-SCHEDULE-MIB", "schedMinute"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    schedCalendarGroup = schedCalendarGroup.setStatus('current')
schedNotificationsGroup = NotificationGroup((1, 3, 6, 1, 2, 1, 63, 3, 2, 3)).setObjects(("DISMAN-SCHEDULE-MIB", "schedActionFailure"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    schedNotificationsGroup = schedNotificationsGroup.setStatus('current')
schedCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 63, 3, 1, 1)).setObjects(("DISMAN-SCHEDULE-MIB", "schedGroup"), ("DISMAN-SCHEDULE-MIB", "schedNotificationsGroup"), ("DISMAN-SCHEDULE-MIB", "schedCalendarGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    schedCompliance = schedCompliance.setStatus('deprecated')
schedGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 63, 3, 2, 1)).setObjects(("DISMAN-SCHEDULE-MIB", "schedDescr"), ("DISMAN-SCHEDULE-MIB", "schedInterval"), ("DISMAN-SCHEDULE-MIB", "schedContextName"), ("DISMAN-SCHEDULE-MIB", "schedVariable"), ("DISMAN-SCHEDULE-MIB", "schedValue"), ("DISMAN-SCHEDULE-MIB", "schedType"), ("DISMAN-SCHEDULE-MIB", "schedAdminStatus"), ("DISMAN-SCHEDULE-MIB", "schedOperStatus"), ("DISMAN-SCHEDULE-MIB", "schedFailures"), ("DISMAN-SCHEDULE-MIB", "schedLastFailure"), ("DISMAN-SCHEDULE-MIB", "schedLastFailed"), ("DISMAN-SCHEDULE-MIB", "schedStorageType"), ("DISMAN-SCHEDULE-MIB", "schedRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    schedGroup = schedGroup.setStatus('deprecated')
mibBuilder.exportSymbols("DISMAN-SCHEDULE-MIB", schedTable=schedTable, schedConformance=schedConformance, schedMinute=schedMinute, schedEntry=schedEntry, schedAdminStatus=schedAdminStatus, schedOwner=schedOwner, schedWeekDay=schedWeekDay, schedTriggers=schedTriggers, schedHour=schedHour, schedContextName=schedContextName, schedStorageType=schedStorageType, schedNotificationsGroup=schedNotificationsGroup, schedGroup=schedGroup, SnmpPduErrorStatus=SnmpPduErrorStatus, schedCompliance2=schedCompliance2, schedGroups=schedGroups, PYSNMP_MODULE_ID=schedMIB, schedOperStatus=schedOperStatus, schedCompliances=schedCompliances, schedActionFailure=schedActionFailure, schedLastFailed=schedLastFailed, schedDescr=schedDescr, schedName=schedName, schedCalendarGroup=schedCalendarGroup, schedMIB=schedMIB, schedGroup2=schedGroup2, schedRowStatus=schedRowStatus, schedInterval=schedInterval, schedFailures=schedFailures, schedCompliance=schedCompliance, schedObjects=schedObjects, schedLastFailure=schedLastFailure, schedType=schedType, schedDay=schedDay, schedValue=schedValue, schedMonth=schedMonth, schedNotifications=schedNotifications, schedTraps=schedTraps, schedLocalTime=schedLocalTime, schedVariable=schedVariable)
