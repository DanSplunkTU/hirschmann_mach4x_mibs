#
# PySNMP MIB module AT-TRIGGER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/allied/AT-TRIGGER-MIB
# Produced by pysmi-1.1.8 at Sun Jan 16 00:31:37 2022
# On host fv-az42-839 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
modules, = mibBuilder.importSymbols("AT-SMI-MIB", "modules")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, Integer32, ObjectIdentity, Unsigned32, IpAddress, NotificationType, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Bits, ModuleIdentity, Counter64, Counter32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Integer32", "ObjectIdentity", "Unsigned32", "IpAddress", "NotificationType", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Bits", "ModuleIdentity", "Counter64", "Counter32", "iso")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
trigger = ModuleIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53))
trigger.setRevisions(('2015-01-05 00:00', '2010-09-07 00:00', '2010-06-15 00:15', '2007-11-28 16:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: trigger.setRevisionsDescriptions(('Add ATMF node trigger MIB', 'Generic syntax tidy up', 'MIB revision history dates in descriptions updated.', 'Added trigger configuration details for AW+',))
if mibBuilder.loadTexts: trigger.setLastUpdated('201501050000Z')
if mibBuilder.loadTexts: trigger.setOrganization('Allied Telesis, Inc')
if mibBuilder.loadTexts: trigger.setContactInfo('http://www.alliedtelesis.com')
if mibBuilder.loadTexts: trigger.setDescription('This MIB file contains definitions of managed objects for the\n                TRIGGER module. ')
triggerTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 0))
triggerTrap = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 0, 1)).setObjects(("AT-TRIGGER-MIB", "triggerLastTriggerActivated"))
if mibBuilder.loadTexts: triggerTrap.setStatus('current')
if mibBuilder.loadTexts: triggerTrap.setDescription('A trigger trap is generated a trigger is activated. The number of the trigger\n                activated is given by the variable triggerLastTriggerActivated.')
triggerLastTriggerActivated = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: triggerLastTriggerActivated.setStatus('current')
if mibBuilder.loadTexts: triggerLastTriggerActivated.setDescription('The trigger number of the most recent trigger activated on this router. This is\n                also the variable sent in the trigger trap below. If no triggers have been activated\n                yet since the last restart of this router, this variable will read as 0.')
triggerConfigInfoTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 9), )
if mibBuilder.loadTexts: triggerConfigInfoTable.setStatus('current')
if mibBuilder.loadTexts: triggerConfigInfoTable.setDescription('The (conceptual) table listing entries of trigger configuration details.')
triggerConfigInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 9, 1), ).setIndexNames((0, "AT-TRIGGER-MIB", "triggerNumber"))
if mibBuilder.loadTexts: triggerConfigInfoEntry.setStatus('current')
if mibBuilder.loadTexts: triggerConfigInfoEntry.setDescription('An entry (conceptual row) in the triggerConfigInfoTable.')
triggerNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 9, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 250))).setMaxAccess("readonly")
if mibBuilder.loadTexts: triggerNumber.setStatus('current')
if mibBuilder.loadTexts: triggerNumber.setDescription('The object represents the ID number of the trigger.')
triggerName = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 9, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: triggerName.setStatus('current')
if mibBuilder.loadTexts: triggerName.setDescription('This object represents the name and description\n                of the trigger.')
triggerTypeDetail = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 9, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: triggerTypeDetail.setStatus('current')
if mibBuilder.loadTexts: triggerTypeDetail.setDescription('This object indicates the trigger type and\n                its activation conditions.')
triggerActiveDaysOrDate = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 9, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: triggerActiveDaysOrDate.setStatus('current')
if mibBuilder.loadTexts: triggerActiveDaysOrDate.setDescription('This objects indicates either the days of a week or the date,\n                on which the trigger is permitted to activate.')
triggerActivateAfter = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 9, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: triggerActivateAfter.setStatus('current')
if mibBuilder.loadTexts: triggerActivateAfter.setDescription('This object indicates the time when the trigger will\n                be activated afterwards.')
triggerActivateBefore = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 9, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: triggerActivateBefore.setStatus('current')
if mibBuilder.loadTexts: triggerActivateBefore.setDescription('This object indicates the time when the trigger will\n                be activated before.')
triggerActiveStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 9, 1, 7), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: triggerActiveStatus.setStatus('current')
if mibBuilder.loadTexts: triggerActiveStatus.setDescription('This object indicates whether or not the trigger is\n                permitted to activate.\n                ')
triggerTestMode = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 9, 1, 8), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: triggerTestMode.setStatus('current')
if mibBuilder.loadTexts: triggerTestMode.setDescription('This object indicates whether or not the trigger is\n                operating in diagnostic mode.\n                ')
triggerSnmpTrap = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 9, 1, 9), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: triggerSnmpTrap.setStatus('current')
if mibBuilder.loadTexts: triggerSnmpTrap.setDescription('This object indicates whether or not a snmp trap will\n                be sent when the trigger is activated.')
triggerRepeatTimes = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 9, 1, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: triggerRepeatTimes.setStatus('current')
if mibBuilder.loadTexts: triggerRepeatTimes.setDescription('This objects indicates whether the trigger repeats\n                an unlimited number of times (continuous) or for a\n                set of times.\n                When the trigger can repeat only a set\n                of times, then the number of times the trigger has\n                been activated is displayed in brackets.')
triggerLasttimeModified = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 9, 1, 11), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: triggerLasttimeModified.setStatus('current')
if mibBuilder.loadTexts: triggerLasttimeModified.setDescription('This object indicates the date and time of the last\n                time that the trigger was modified.')
triggerNumberOfActivation = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 9, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: triggerNumberOfActivation.setStatus('current')
if mibBuilder.loadTexts: triggerNumberOfActivation.setDescription('The objects represents the number of times the trigger\n                has been activated since the last restart of the device.\n                ')
triggerLasttimeActivation = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 9, 1, 13), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: triggerLasttimeActivation.setStatus('current')
if mibBuilder.loadTexts: triggerLasttimeActivation.setDescription('This object indicates the date and time of the last\n                time that the trigger was activated.')
triggerNumberOfScripts = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 9, 1, 14), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 5))).setMaxAccess("readonly")
if mibBuilder.loadTexts: triggerNumberOfScripts.setStatus('current')
if mibBuilder.loadTexts: triggerNumberOfScripts.setDescription('This objects represents the number of scripts that are\n                associated with this trigger.')
triggerScript1 = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 9, 1, 15), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: triggerScript1.setStatus('current')
if mibBuilder.loadTexts: triggerScript1.setDescription('This objects represents the name of the 1st script\n                that is associated with the trigger.\n                ')
triggerScript2 = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 9, 1, 16), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: triggerScript2.setStatus('current')
if mibBuilder.loadTexts: triggerScript2.setDescription('This objects represents the name of the 2nd script\n                that is associated with the trigger.\n                ')
triggerScript3 = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 9, 1, 17), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: triggerScript3.setStatus('current')
if mibBuilder.loadTexts: triggerScript3.setDescription('This objects represents the name of the 3rd script\n                that is associated with the trigger.\n                ')
triggerScript4 = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 9, 1, 18), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: triggerScript4.setStatus('current')
if mibBuilder.loadTexts: triggerScript4.setDescription('This objects represents the name of the 4th script\n                that is associated with the trigger.\n                ')
triggerScript5 = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 9, 1, 19), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: triggerScript5.setStatus('current')
if mibBuilder.loadTexts: triggerScript5.setDescription('This objects represents the name of the 5th script\n                that is associated with the trigger.\n                ')
triggerCounters = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 10))
triggerNumOfActivation = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 10, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: triggerNumOfActivation.setStatus('current')
if mibBuilder.loadTexts: triggerNumOfActivation.setDescription('This objects represents the number of times a trigger\n                has been activated.')
triggerNumOfActivationToday = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 10, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: triggerNumOfActivationToday.setStatus('current')
if mibBuilder.loadTexts: triggerNumOfActivationToday.setDescription('This objects represents the number of times a trigger\n                has been activated today.')
triggerNumOfPerodicActivationToday = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 10, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: triggerNumOfPerodicActivationToday.setStatus('current')
if mibBuilder.loadTexts: triggerNumOfPerodicActivationToday.setDescription('This objects represents the number of times a periodic\n                trigger has been activated today.')
triggerNumOfInterfaceActivationToday = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 10, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: triggerNumOfInterfaceActivationToday.setStatus('current')
if mibBuilder.loadTexts: triggerNumOfInterfaceActivationToday.setDescription('This objects represents the number of times an interface\n                trigger has been activated today.')
triggerNumOfResourceActivationToday = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 10, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: triggerNumOfResourceActivationToday.setStatus('current')
if mibBuilder.loadTexts: triggerNumOfResourceActivationToday.setDescription('This objects represents the number of times a CPU or\n                memory trigger has been activated today.')
triggerNumOfRebootActivationToday = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 10, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: triggerNumOfRebootActivationToday.setStatus('current')
if mibBuilder.loadTexts: triggerNumOfRebootActivationToday.setDescription('This objects represents the number of times a reboot\n                trigger has been activated today.')
triggerNumOfPingPollActivationToday = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 10, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: triggerNumOfPingPollActivationToday.setStatus('current')
if mibBuilder.loadTexts: triggerNumOfPingPollActivationToday.setDescription('This objects represents the number of times a ping-poll\n                trigger has been activated today.')
triggerNumOfStackMasterFailActivationToday = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 10, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: triggerNumOfStackMasterFailActivationToday.setStatus('current')
if mibBuilder.loadTexts: triggerNumOfStackMasterFailActivationToday.setDescription('This objects represents the number of times a stack master\n                fail trigger has been activated today.')
triggerNumOfStackMemberActivationToday = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 10, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: triggerNumOfStackMemberActivationToday.setStatus('current')
if mibBuilder.loadTexts: triggerNumOfStackMemberActivationToday.setDescription('This objects represents the number of times a stack member\n                trigger has been activated today.')
triggerNumOfStackXemStkActivationToday = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 10, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: triggerNumOfStackXemStkActivationToday.setStatus('current')
if mibBuilder.loadTexts: triggerNumOfStackXemStkActivationToday.setDescription('This objects represents the number of times a stack\n                xem-stack trigger has been activated today.')
triggerNumOfATMFNodeActivationToday = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 10, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: triggerNumOfATMFNodeActivationToday.setStatus('current')
if mibBuilder.loadTexts: triggerNumOfATMFNodeActivationToday.setDescription('This objects represents the number of times a ATMF\n                node trigger has been activated today.')
mibBuilder.exportSymbols("AT-TRIGGER-MIB", triggerRepeatTimes=triggerRepeatTimes, triggerScript4=triggerScript4, trigger=trigger, triggerNumOfActivation=triggerNumOfActivation, triggerNumOfATMFNodeActivationToday=triggerNumOfATMFNodeActivationToday, triggerNumberOfActivation=triggerNumberOfActivation, triggerTrap=triggerTrap, triggerNumOfResourceActivationToday=triggerNumOfResourceActivationToday, triggerNumOfRebootActivationToday=triggerNumOfRebootActivationToday, triggerNumOfPerodicActivationToday=triggerNumOfPerodicActivationToday, triggerNumOfStackMasterFailActivationToday=triggerNumOfStackMasterFailActivationToday, triggerScript2=triggerScript2, triggerNumOfStackMemberActivationToday=triggerNumOfStackMemberActivationToday, triggerLasttimeActivation=triggerLasttimeActivation, triggerName=triggerName, triggerConfigInfoTable=triggerConfigInfoTable, PYSNMP_MODULE_ID=trigger, triggerLasttimeModified=triggerLasttimeModified, triggerNumberOfScripts=triggerNumberOfScripts, triggerLastTriggerActivated=triggerLastTriggerActivated, triggerNumOfStackXemStkActivationToday=triggerNumOfStackXemStkActivationToday, triggerTestMode=triggerTestMode, triggerNumOfPingPollActivationToday=triggerNumOfPingPollActivationToday, triggerActiveDaysOrDate=triggerActiveDaysOrDate, triggerNumber=triggerNumber, triggerNumOfActivationToday=triggerNumOfActivationToday, triggerScript1=triggerScript1, triggerNumOfInterfaceActivationToday=triggerNumOfInterfaceActivationToday, triggerCounters=triggerCounters, triggerConfigInfoEntry=triggerConfigInfoEntry, triggerScript5=triggerScript5, triggerTraps=triggerTraps, triggerActivateAfter=triggerActivateAfter, triggerScript3=triggerScript3, triggerTypeDetail=triggerTypeDetail, triggerActiveStatus=triggerActiveStatus, triggerSnmpTrap=triggerSnmpTrap, triggerActivateBefore=triggerActivateBefore)
