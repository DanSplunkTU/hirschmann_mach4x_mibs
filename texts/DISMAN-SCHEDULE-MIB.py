#
# PySNMP MIB module DISMAN-SCHEDULE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/DISMAN-SCHEDULE-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:07:49 2022
# On host fv-az36-988 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Bits, Counter64, Unsigned32, mib_2, zeroDotZero, ModuleIdentity, NotificationType, Counter32, TimeTicks, IpAddress, Integer32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, iso, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter64", "Unsigned32", "mib-2", "zeroDotZero", "ModuleIdentity", "NotificationType", "Counter32", "TimeTicks", "IpAddress", "Integer32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "iso", "Gauge32")
DateAndTime, TextualConvention, VariablePointer, RowStatus, StorageType, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "TextualConvention", "VariablePointer", "RowStatus", "StorageType", "DisplayString")
schedMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 63))
schedMIB.setRevisions(('2002-01-07 00:00', '1998-11-17 18:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: schedMIB.setRevisionsDescriptions(('Revised version, published as RFC 3231.\n\n         This revision introduces a new object type called\n         schedTriggers.  Created new conformance and compliance\n         statements that take care of the new schedTriggers object.\n\n         Several clarifications have been added to remove ambiguities\n         that were discovered and reported by implementors.', 'Initial version, published as RFC 2591.',))
if mibBuilder.loadTexts: schedMIB.setLastUpdated('200201070000Z')
if mibBuilder.loadTexts: schedMIB.setOrganization('IETF Distributed Management Working Group')
if mibBuilder.loadTexts: schedMIB.setContactInfo('WG EMail:  disman@dorothy.bmc.com\n         Subscribe: disman-request@dorothy.bmc.com\n\n         Chair:     Randy Presuhn\n                    BMC Software, Inc.\n         Postal:    Office 1-3141\n                    2141 North First Street\n                    San Jose,  California 95131\n                    USA\n         EMail:     rpresuhn@bmc.com\n         Phone:     +1 408 546-1006\n\n         Editor:    David B. Levi\n                    Nortel Networks\n         Postal:    4401 Great America Parkway\n                    Santa Clara, CA 95052-8185\n                    USA\n         EMail:     dlevi@nortelnetworks.com\n         Phone:     +1 865 686 0432\n\n         Editor:    Juergen Schoenwaelder\n                    TU Braunschweig\n         Postal:    Bueltenweg 74/75\n                    38106 Braunschweig\n                    Germany\n         EMail:     schoenw@ibr.cs.tu-bs.de\n         Phone:     +49 531 391-3283')
if mibBuilder.loadTexts: schedMIB.setDescription('This MIB module defines a MIB which provides mechanisms to\n         schedule SNMP set operations periodically or at specific\n         points in time.')
schedObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 63, 1))
schedNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 63, 2))
schedConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 63, 3))
class SnmpPduErrorStatus(TextualConvention, Integer32):
    description = "This TC enumerates the SNMPv1 and SNMPv2 PDU error status\n         codes as defined in RFC 1157 and RFC 1905.  It also adds a\n         pseudo error status code `noResponse' which indicates a\n         timeout condition."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18))
    namedValues = NamedValues(("noResponse", -1), ("noError", 0), ("tooBig", 1), ("noSuchName", 2), ("badValue", 3), ("readOnly", 4), ("genErr", 5), ("noAccess", 6), ("wrongType", 7), ("wrongLength", 8), ("wrongEncoding", 9), ("wrongValue", 10), ("noCreation", 11), ("inconsistentValue", 12), ("resourceUnavailable", 13), ("commitFailed", 14), ("undoFailed", 15), ("authorizationError", 16), ("notWritable", 17), ("inconsistentName", 18))

schedLocalTime = MibScalar((1, 3, 6, 1, 2, 1, 63, 1, 1), DateAndTime().subtype(subtypeSpec=ValueSizeConstraint(11, 11)).setFixedLength(11)).setMaxAccess("readonly")
if mibBuilder.loadTexts: schedLocalTime.setStatus('current')
if mibBuilder.loadTexts: schedLocalTime.setDescription('The local time used by the scheduler.  Schedules which\n         refer to calendar time will use the local time indicated\n         by this object.  An implementation MUST return all 11 bytes\n         of the DateAndTime textual-convention so that a manager\n         may retrieve the offset from GMT time.')
schedTable = MibTable((1, 3, 6, 1, 2, 1, 63, 1, 2), )
if mibBuilder.loadTexts: schedTable.setStatus('current')
if mibBuilder.loadTexts: schedTable.setDescription('This table defines scheduled actions triggered by\n         SNMP set operations.')
schedEntry = MibTableRow((1, 3, 6, 1, 2, 1, 63, 1, 2, 1), ).setIndexNames((0, "DISMAN-SCHEDULE-MIB", "schedOwner"), (0, "DISMAN-SCHEDULE-MIB", "schedName"))
if mibBuilder.loadTexts: schedEntry.setStatus('current')
if mibBuilder.loadTexts: schedEntry.setDescription('An entry describing a particular scheduled action.\n\n         Unless noted otherwise, writable objects of this row\n         can be modified independent of the current value of\n         schedRowStatus, schedAdminStatus and schedOperStatus.\n         In particular, it is legal to modify schedInterval\n         and the objects in the schedCalendarGroup when\n         schedRowStatus is active and schedAdminStatus and\n         schedOperStatus are both enabled.')
schedOwner = MibTableColumn((1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32)))
if mibBuilder.loadTexts: schedOwner.setStatus('current')
if mibBuilder.loadTexts: schedOwner.setDescription('The owner of this scheduling entry.  The exact semantics of\n         this string are subject to the security policy defined by\n\n         the security administrator.')
schedName = MibTableColumn((1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: schedName.setStatus('current')
if mibBuilder.loadTexts: schedName.setDescription('The locally-unique, administratively assigned name for this\n         scheduling entry.  This object allows a schedOwner to have\n         multiple entries in the schedTable.')
schedDescr = MibTableColumn((1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 3), SnmpAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: schedDescr.setStatus('current')
if mibBuilder.loadTexts: schedDescr.setDescription('The human readable description of the purpose of this\n         scheduling entry.')
schedInterval = MibTableColumn((1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 4), Unsigned32()).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: schedInterval.setStatus('current')
if mibBuilder.loadTexts: schedInterval.setDescription('The number of seconds between two action invocations of\n         a periodic scheduler.  Implementations must guarantee\n         that action invocations will not occur before at least\n         schedInterval seconds have passed.\n\n         The scheduler must ignore all periodic schedules that\n         have a schedInterval value of 0.  A periodic schedule\n         with a scheduling interval of 0 seconds will therefore\n         never invoke an action.\n\n         Implementations may be forced to delay invocations in the\n         face of local constraints.  A scheduled management function\n         should therefore not rely on the accuracy provided by the\n         scheduler implementation.\n\n         Note that implementations which maintain a list of pending\n         activations must re-calculate them when this object is\n         changed.')
schedWeekDay = MibTableColumn((1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 5), Bits().clone(namedValues=NamedValues(("sunday", 0), ("monday", 1), ("tuesday", 2), ("wednesday", 3), ("thursday", 4), ("friday", 5), ("saturday", 6)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: schedWeekDay.setStatus('current')
if mibBuilder.loadTexts: schedWeekDay.setDescription('The set of weekdays on which the scheduled action should\n         take place.  Setting multiple bits will include several\n         weekdays in the set of possible weekdays for this schedule.\n         Setting all bits will cause the scheduler to ignore the\n         weekday.\n\n         Note that implementations which maintain a list of pending\n         activations must re-calculate them when this object is\n         changed.')
schedMonth = MibTableColumn((1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 6), Bits().clone(namedValues=NamedValues(("january", 0), ("february", 1), ("march", 2), ("april", 3), ("may", 4), ("june", 5), ("july", 6), ("august", 7), ("september", 8), ("october", 9), ("november", 10), ("december", 11)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: schedMonth.setStatus('current')
if mibBuilder.loadTexts: schedMonth.setDescription('The set of months during which the scheduled action should\n         take place.  Setting multiple bits will include several\n         months in the set of possible months for this schedule.\n\n         Setting all bits will cause the scheduler to ignore the\n         month.\n\n         Note that implementations which maintain a list of pending\n         activations must re-calculate them when this object is\n         changed.')
schedDay = MibTableColumn((1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 7), Bits().clone(namedValues=NamedValues(("d1", 0), ("d2", 1), ("d3", 2), ("d4", 3), ("d5", 4), ("d6", 5), ("d7", 6), ("d8", 7), ("d9", 8), ("d10", 9), ("d11", 10), ("d12", 11), ("d13", 12), ("d14", 13), ("d15", 14), ("d16", 15), ("d17", 16), ("d18", 17), ("d19", 18), ("d20", 19), ("d21", 20), ("d22", 21), ("d23", 22), ("d24", 23), ("d25", 24), ("d26", 25), ("d27", 26), ("d28", 27), ("d29", 28), ("d30", 29), ("d31", 30), ("r1", 31), ("r2", 32), ("r3", 33), ("r4", 34), ("r5", 35), ("r6", 36), ("r7", 37), ("r8", 38), ("r9", 39), ("r10", 40), ("r11", 41), ("r12", 42), ("r13", 43), ("r14", 44), ("r15", 45), ("r16", 46), ("r17", 47), ("r18", 48), ("r19", 49), ("r20", 50), ("r21", 51), ("r22", 52), ("r23", 53), ("r24", 54), ("r25", 55), ("r26", 56), ("r27", 57), ("r28", 58), ("r29", 59), ("r30", 60), ("r31", 61)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: schedDay.setStatus('current')
if mibBuilder.loadTexts: schedDay.setDescription("The set of days in a month on which a scheduled action\n         should take place.  There are two sets of bits one can\n         use to define the day within a month:\n\n         Enumerations starting with the letter 'd' indicate a\n         day in a month relative to the first day of a month.\n         The first day of the month can therefore be specified\n         by setting the bit d1(0) and d31(30) means the last\n         day of a month with 31 days.\n\n         Enumerations starting with the letter 'r' indicate a\n         day in a month in reverse order, relative to the last\n         day of a month.  The last day in the month can therefore\n         be specified by setting the bit r1(31) and r31(61) means\n         the first day of a month with 31 days.\n\n         Setting multiple bits will include several days in the set\n         of possible days for this schedule.  Setting all bits will\n         cause the scheduler to ignore the day within a month.\n\n         Setting all bits starting with the letter 'd' or the\n         letter 'r' will also cause the scheduler to ignore the\n         day within a month.\n\n         Note that implementations which maintain a list of pending\n         activations must re-calculate them when this object is\n         changed.")
schedHour = MibTableColumn((1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 8), Bits().clone(namedValues=NamedValues(("h0", 0), ("h1", 1), ("h2", 2), ("h3", 3), ("h4", 4), ("h5", 5), ("h6", 6), ("h7", 7), ("h8", 8), ("h9", 9), ("h10", 10), ("h11", 11), ("h12", 12), ("h13", 13), ("h14", 14), ("h15", 15), ("h16", 16), ("h17", 17), ("h18", 18), ("h19", 19), ("h20", 20), ("h21", 21), ("h22", 22), ("h23", 23)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: schedHour.setStatus('current')
if mibBuilder.loadTexts: schedHour.setDescription('The set of hours within a day during which the scheduled\n         action should take place.\n\n         Note that implementations which maintain a list of pending\n         activations must re-calculate them when this object is\n         changed.')
schedMinute = MibTableColumn((1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 9), Bits().clone(namedValues=NamedValues(("m0", 0), ("m1", 1), ("m2", 2), ("m3", 3), ("m4", 4), ("m5", 5), ("m6", 6), ("m7", 7), ("m8", 8), ("m9", 9), ("m10", 10), ("m11", 11), ("m12", 12), ("m13", 13), ("m14", 14), ("m15", 15), ("m16", 16), ("m17", 17), ("m18", 18), ("m19", 19), ("m20", 20), ("m21", 21), ("m22", 22), ("m23", 23), ("m24", 24), ("m25", 25), ("m26", 26), ("m27", 27), ("m28", 28), ("m29", 29), ("m30", 30), ("m31", 31), ("m32", 32), ("m33", 33), ("m34", 34), ("m35", 35), ("m36", 36), ("m37", 37), ("m38", 38), ("m39", 39), ("m40", 40), ("m41", 41), ("m42", 42), ("m43", 43), ("m44", 44), ("m45", 45), ("m46", 46), ("m47", 47), ("m48", 48), ("m49", 49), ("m50", 50), ("m51", 51), ("m52", 52), ("m53", 53), ("m54", 54), ("m55", 55), ("m56", 56), ("m57", 57), ("m58", 58), ("m59", 59)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: schedMinute.setStatus('current')
if mibBuilder.loadTexts: schedMinute.setDescription('The set of minutes within an hour when the scheduled action\n         should take place.\n\n         Note that implementations which maintain a list of pending\n         activations must re-calculate them when this object is\n         changed.')
schedContextName = MibTableColumn((1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 10), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: schedContextName.setStatus('current')
if mibBuilder.loadTexts: schedContextName.setDescription('The context which contains the local MIB variable pointed\n         to by schedVariable.')
schedVariable = MibTableColumn((1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 11), VariablePointer().clone((0, 0))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: schedVariable.setStatus('current')
if mibBuilder.loadTexts: schedVariable.setDescription('An object identifier pointing to a local MIB variable\n         which resolves to an ASN.1 primitive type of INTEGER.')
schedValue = MibTableColumn((1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 12), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: schedValue.setStatus('current')
if mibBuilder.loadTexts: schedValue.setDescription('The value which is written to the MIB object pointed to by\n         schedVariable when the scheduler invokes an action.  The\n         implementation shall enforce the use of access control\n         rules when performing the set operation on schedVariable.\n         This is accomplished by calling the isAccessAllowed abstract\n         service interface as defined in RFC 2571.\n\n         Note that an implementation may choose to issue an SNMP Set\n         message to the SNMP engine and leave the access control\n         decision to the normal message processing procedure.')
schedType = MibTableColumn((1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("periodic", 1), ("calendar", 2), ("oneshot", 3))).clone('periodic')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: schedType.setStatus('current')
if mibBuilder.loadTexts: schedType.setDescription("The type of this schedule.  The value periodic(1) indicates\n         that this entry specifies a periodic schedule.  A periodic\n         schedule is defined by the value of schedInterval.  The\n         values of schedWeekDay, schedMonth, schedDay, schedHour\n         and schedMinute are ignored.\n\n         The value calendar(2) indicates that this entry describes a\n         calendar schedule.  A calendar schedule is defined by the\n         values of schedWeekDay, schedMonth, schedDay, schedHour and\n         schedMinute.  The value of schedInterval is ignored.  A\n         calendar schedule will trigger on all local times that\n         satisfy the bits set in schedWeekDay, schedMonth, schedDay,\n         schedHour and schedMinute.\n\n         The value oneshot(3) indicates that this entry describes a\n         one-shot schedule.  A one-shot schedule is similar to a\n         calendar schedule with the additional feature that it\n         disables itself by changing in the `finished'\n         schedOperStatus once the schedule triggers an action.\n\n         Note that implementations which maintain a list of pending\n         activations must re-calculate them when this object is\n         changed.")
schedAdminStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: schedAdminStatus.setStatus('current')
if mibBuilder.loadTexts: schedAdminStatus.setDescription('The desired state of the schedule.')
schedOperStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ("finished", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: schedOperStatus.setStatus('current')
if mibBuilder.loadTexts: schedOperStatus.setDescription('The current operational state of this schedule.  The state\n         enabled(1) indicates this entry is active and that the\n         scheduler will invoke actions at appropriate times.  The\n         disabled(2) state indicates that this entry is currently\n         inactive and ignored by the scheduler.  The finished(3)\n         state indicates that the schedule has ended.  Schedules\n         in the finished(3) state are ignored by the scheduler.\n         A one-shot schedule enters the finished(3) state when it\n         deactivates itself.\n\n         Note that the operational state must not be enabled(1)\n         when the schedRowStatus is not active.')
schedFailures = MibTableColumn((1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: schedFailures.setStatus('current')
if mibBuilder.loadTexts: schedFailures.setDescription('This variable counts the number of failures while invoking\n         the scheduled action.  This counter at most increments once\n         for a triggered action.')
schedLastFailure = MibTableColumn((1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 17), SnmpPduErrorStatus().clone('noError')).setMaxAccess("readonly")
if mibBuilder.loadTexts: schedLastFailure.setStatus('current')
if mibBuilder.loadTexts: schedLastFailure.setDescription('The most recent error that occurred during the invocation of\n         a scheduled action.  The value noError(0) is returned\n         if no errors have occurred yet.')
schedLastFailed = MibTableColumn((1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 18), DateAndTime().clone(hexValue="0000000000000000")).setMaxAccess("readonly")
if mibBuilder.loadTexts: schedLastFailed.setStatus('current')
if mibBuilder.loadTexts: schedLastFailed.setDescription("The date and time when the most recent failure occurred.\n\n         The value '0000000000000000'H is returned if no failure\n         occurred since the last re-initialization of the scheduler.")
schedStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 19), StorageType().clone('volatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: schedStorageType.setStatus('current')
if mibBuilder.loadTexts: schedStorageType.setDescription("This object defines whether this scheduled action is kept\n         in volatile storage and lost upon reboot or if this row is\n         backed up by non-volatile or permanent storage.\n\n         Conceptual rows having the value `permanent' must allow\n         write access to the columnar objects schedDescr,\n         schedInterval, schedContextName, schedVariable, schedValue,\n         and schedAdminStatus.  If an implementation supports the\n         schedCalendarGroup, write access must be also allowed to\n         the columnar objects schedWeekDay, schedMonth, schedDay,\n         schedHour, schedMinute.")
schedRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 20), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: schedRowStatus.setStatus('current')
if mibBuilder.loadTexts: schedRowStatus.setDescription('The status of this scheduled action.  A control that allows\n         entries to be added and removed from this table.\n\n         Note that the operational state must change to enabled\n         when the administrative state is enabled and the row\n         status changes to active(1).\n\n         Attempts to destroy(6) a row or to set a row\n         notInService(2) while the operational state is enabled\n         result in inconsistentValue errors.\n\n         The value of this object has no effect on whether other\n         objects in this conceptual row can be modified.')
schedTriggers = MibTableColumn((1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: schedTriggers.setStatus('current')
if mibBuilder.loadTexts: schedTriggers.setDescription('This variable counts the number of attempts (either\n         successful or failed) to invoke the scheduled action.')
schedTraps = MibIdentifier((1, 3, 6, 1, 2, 1, 63, 2, 0))
schedActionFailure = NotificationType((1, 3, 6, 1, 2, 1, 63, 2, 0, 1)).setObjects(("DISMAN-SCHEDULE-MIB", "schedLastFailure"), ("DISMAN-SCHEDULE-MIB", "schedLastFailed"))
if mibBuilder.loadTexts: schedActionFailure.setStatus('current')
if mibBuilder.loadTexts: schedActionFailure.setDescription('This notification is generated whenever the invocation of a\n         scheduled action fails.')
schedCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 63, 3, 1))
schedGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 63, 3, 2))
schedCompliance2 = ModuleCompliance((1, 3, 6, 1, 2, 1, 63, 3, 1, 2)).setObjects(("DISMAN-SCHEDULE-MIB", "schedGroup2"), ("DISMAN-SCHEDULE-MIB", "schedNotificationsGroup"), ("DISMAN-SCHEDULE-MIB", "schedCalendarGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    schedCompliance2 = schedCompliance2.setStatus('current')
if mibBuilder.loadTexts: schedCompliance2.setDescription('The compliance statement for SNMP entities which implement\n         the scheduling MIB.')
schedGroup2 = ObjectGroup((1, 3, 6, 1, 2, 1, 63, 3, 2, 4)).setObjects(("DISMAN-SCHEDULE-MIB", "schedDescr"), ("DISMAN-SCHEDULE-MIB", "schedInterval"), ("DISMAN-SCHEDULE-MIB", "schedContextName"), ("DISMAN-SCHEDULE-MIB", "schedVariable"), ("DISMAN-SCHEDULE-MIB", "schedValue"), ("DISMAN-SCHEDULE-MIB", "schedType"), ("DISMAN-SCHEDULE-MIB", "schedAdminStatus"), ("DISMAN-SCHEDULE-MIB", "schedOperStatus"), ("DISMAN-SCHEDULE-MIB", "schedFailures"), ("DISMAN-SCHEDULE-MIB", "schedLastFailure"), ("DISMAN-SCHEDULE-MIB", "schedLastFailed"), ("DISMAN-SCHEDULE-MIB", "schedStorageType"), ("DISMAN-SCHEDULE-MIB", "schedRowStatus"), ("DISMAN-SCHEDULE-MIB", "schedTriggers"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    schedGroup2 = schedGroup2.setStatus('current')
if mibBuilder.loadTexts: schedGroup2.setDescription('A collection of objects providing scheduling capabilities.')
schedCalendarGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 63, 3, 2, 2)).setObjects(("DISMAN-SCHEDULE-MIB", "schedLocalTime"), ("DISMAN-SCHEDULE-MIB", "schedWeekDay"), ("DISMAN-SCHEDULE-MIB", "schedMonth"), ("DISMAN-SCHEDULE-MIB", "schedDay"), ("DISMAN-SCHEDULE-MIB", "schedHour"), ("DISMAN-SCHEDULE-MIB", "schedMinute"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    schedCalendarGroup = schedCalendarGroup.setStatus('current')
if mibBuilder.loadTexts: schedCalendarGroup.setDescription('A collection of objects providing calendar based schedules.')
schedNotificationsGroup = NotificationGroup((1, 3, 6, 1, 2, 1, 63, 3, 2, 3)).setObjects(("DISMAN-SCHEDULE-MIB", "schedActionFailure"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    schedNotificationsGroup = schedNotificationsGroup.setStatus('current')
if mibBuilder.loadTexts: schedNotificationsGroup.setDescription('The notifications emitted by the scheduler.')
schedCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 63, 3, 1, 1)).setObjects(("DISMAN-SCHEDULE-MIB", "schedGroup"), ("DISMAN-SCHEDULE-MIB", "schedNotificationsGroup"), ("DISMAN-SCHEDULE-MIB", "schedCalendarGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    schedCompliance = schedCompliance.setStatus('deprecated')
if mibBuilder.loadTexts: schedCompliance.setDescription('The compliance statement for SNMP entities which implement\n         the scheduling MIB.')
schedGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 63, 3, 2, 1)).setObjects(("DISMAN-SCHEDULE-MIB", "schedDescr"), ("DISMAN-SCHEDULE-MIB", "schedInterval"), ("DISMAN-SCHEDULE-MIB", "schedContextName"), ("DISMAN-SCHEDULE-MIB", "schedVariable"), ("DISMAN-SCHEDULE-MIB", "schedValue"), ("DISMAN-SCHEDULE-MIB", "schedType"), ("DISMAN-SCHEDULE-MIB", "schedAdminStatus"), ("DISMAN-SCHEDULE-MIB", "schedOperStatus"), ("DISMAN-SCHEDULE-MIB", "schedFailures"), ("DISMAN-SCHEDULE-MIB", "schedLastFailure"), ("DISMAN-SCHEDULE-MIB", "schedLastFailed"), ("DISMAN-SCHEDULE-MIB", "schedStorageType"), ("DISMAN-SCHEDULE-MIB", "schedRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    schedGroup = schedGroup.setStatus('deprecated')
if mibBuilder.loadTexts: schedGroup.setDescription('A collection of objects providing scheduling capabilities.')
mibBuilder.exportSymbols("DISMAN-SCHEDULE-MIB", schedOwner=schedOwner, schedType=schedType, schedTraps=schedTraps, schedLocalTime=schedLocalTime, schedMIB=schedMIB, schedGroups=schedGroups, schedWeekDay=schedWeekDay, schedActionFailure=schedActionFailure, schedGroup=schedGroup, schedCompliance=schedCompliance, schedGroup2=schedGroup2, schedFailures=schedFailures, schedNotifications=schedNotifications, schedNotificationsGroup=schedNotificationsGroup, schedRowStatus=schedRowStatus, PYSNMP_MODULE_ID=schedMIB, schedTriggers=schedTriggers, schedEntry=schedEntry, schedStorageType=schedStorageType, schedVariable=schedVariable, SnmpPduErrorStatus=SnmpPduErrorStatus, schedLastFailure=schedLastFailure, schedObjects=schedObjects, schedTable=schedTable, schedCompliance2=schedCompliance2, schedContextName=schedContextName, schedCompliances=schedCompliances, schedConformance=schedConformance, schedDescr=schedDescr, schedAdminStatus=schedAdminStatus, schedMonth=schedMonth, schedMinute=schedMinute, schedValue=schedValue, schedHour=schedHour, schedName=schedName, schedInterval=schedInterval, schedDay=schedDay, schedCalendarGroup=schedCalendarGroup, schedOperStatus=schedOperStatus, schedLastFailed=schedLastFailed)
