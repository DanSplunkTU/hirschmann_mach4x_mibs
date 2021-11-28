#
# PySNMP MIB module AT-TRIGGER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/awplus/AT-TRIGGER-MIB
# Produced by pysmi-1.1.3 at Sun Nov 28 20:24:49 2021
# On host fv-az77-612 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
modules, = mibBuilder.importSymbols("AT-SMI-MIB", "modules")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, Gauge32, ObjectIdentity, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, iso, Bits, ModuleIdentity, Counter32, MibIdentifier, Integer32, Counter64, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Gauge32", "ObjectIdentity", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "iso", "Bits", "ModuleIdentity", "Counter32", "MibIdentifier", "Integer32", "Counter64", "Unsigned32")
TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString")
trigger = ModuleIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53))
trigger.setRevisions(('2015-01-05 00:00', '2010-09-07 00:00', '2010-06-15 00:15', '2007-11-28 16:00',))
if mibBuilder.loadTexts: trigger.setLastUpdated('201501050000Z')
if mibBuilder.loadTexts: trigger.setOrganization('Allied Telesis, Inc')
triggerTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 0))
triggerTrap = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 0, 1)).setObjects(("AT-TRIGGER-MIB", "triggerLastTriggerActivated"))
if mibBuilder.loadTexts: triggerTrap.setStatus('current')
triggerLastTriggerActivated = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: triggerLastTriggerActivated.setStatus('current')
triggerConfigInfoTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 9), )
if mibBuilder.loadTexts: triggerConfigInfoTable.setStatus('current')
triggerConfigInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 9, 1), ).setIndexNames((0, "AT-TRIGGER-MIB", "triggerNumber"))
if mibBuilder.loadTexts: triggerConfigInfoEntry.setStatus('current')
triggerNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 9, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 250))).setMaxAccess("readonly")
if mibBuilder.loadTexts: triggerNumber.setStatus('current')
triggerName = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 9, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: triggerName.setStatus('current')
triggerTypeDetail = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 9, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: triggerTypeDetail.setStatus('current')
triggerActiveDaysOrDate = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 9, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: triggerActiveDaysOrDate.setStatus('current')
triggerActivateAfter = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 9, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: triggerActivateAfter.setStatus('current')
triggerActivateBefore = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 9, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: triggerActivateBefore.setStatus('current')
triggerActiveStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 9, 1, 7), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: triggerActiveStatus.setStatus('current')
triggerTestMode = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 9, 1, 8), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: triggerTestMode.setStatus('current')
triggerSnmpTrap = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 9, 1, 9), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: triggerSnmpTrap.setStatus('current')
triggerRepeatTimes = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 9, 1, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: triggerRepeatTimes.setStatus('current')
triggerLasttimeModified = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 9, 1, 11), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: triggerLasttimeModified.setStatus('current')
triggerNumberOfActivation = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 9, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: triggerNumberOfActivation.setStatus('current')
triggerLasttimeActivation = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 9, 1, 13), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: triggerLasttimeActivation.setStatus('current')
triggerNumberOfScripts = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 9, 1, 14), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 5))).setMaxAccess("readonly")
if mibBuilder.loadTexts: triggerNumberOfScripts.setStatus('current')
triggerScript1 = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 9, 1, 15), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: triggerScript1.setStatus('current')
triggerScript2 = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 9, 1, 16), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: triggerScript2.setStatus('current')
triggerScript3 = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 9, 1, 17), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: triggerScript3.setStatus('current')
triggerScript4 = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 9, 1, 18), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: triggerScript4.setStatus('current')
triggerScript5 = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 9, 1, 19), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: triggerScript5.setStatus('current')
triggerCounters = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 10))
triggerNumOfActivation = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 10, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: triggerNumOfActivation.setStatus('current')
triggerNumOfActivationToday = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 10, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: triggerNumOfActivationToday.setStatus('current')
triggerNumOfPerodicActivationToday = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 10, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: triggerNumOfPerodicActivationToday.setStatus('current')
triggerNumOfInterfaceActivationToday = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 10, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: triggerNumOfInterfaceActivationToday.setStatus('current')
triggerNumOfResourceActivationToday = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 10, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: triggerNumOfResourceActivationToday.setStatus('current')
triggerNumOfRebootActivationToday = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 10, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: triggerNumOfRebootActivationToday.setStatus('current')
triggerNumOfPingPollActivationToday = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 10, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: triggerNumOfPingPollActivationToday.setStatus('current')
triggerNumOfStackMasterFailActivationToday = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 10, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: triggerNumOfStackMasterFailActivationToday.setStatus('current')
triggerNumOfStackMemberActivationToday = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 10, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: triggerNumOfStackMemberActivationToday.setStatus('current')
triggerNumOfStackXemStkActivationToday = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 10, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: triggerNumOfStackXemStkActivationToday.setStatus('current')
triggerNumOfATMFNodeActivationToday = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 53, 10, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: triggerNumOfATMFNodeActivationToday.setStatus('current')
mibBuilder.exportSymbols("AT-TRIGGER-MIB", triggerScript5=triggerScript5, triggerActiveStatus=triggerActiveStatus, triggerScript4=triggerScript4, triggerCounters=triggerCounters, triggerLasttimeModified=triggerLasttimeModified, triggerName=triggerName, triggerNumOfPingPollActivationToday=triggerNumOfPingPollActivationToday, triggerScript1=triggerScript1, triggerRepeatTimes=triggerRepeatTimes, triggerNumOfRebootActivationToday=triggerNumOfRebootActivationToday, triggerLasttimeActivation=triggerLasttimeActivation, trigger=trigger, triggerNumOfATMFNodeActivationToday=triggerNumOfATMFNodeActivationToday, triggerConfigInfoEntry=triggerConfigInfoEntry, triggerNumOfStackMemberActivationToday=triggerNumOfStackMemberActivationToday, triggerNumOfActivationToday=triggerNumOfActivationToday, triggerNumOfResourceActivationToday=triggerNumOfResourceActivationToday, triggerScript2=triggerScript2, triggerNumberOfScripts=triggerNumberOfScripts, triggerActivateBefore=triggerActivateBefore, triggerTypeDetail=triggerTypeDetail, PYSNMP_MODULE_ID=trigger, triggerNumber=triggerNumber, triggerNumberOfActivation=triggerNumberOfActivation, triggerTrap=triggerTrap, triggerTraps=triggerTraps, triggerNumOfStackMasterFailActivationToday=triggerNumOfStackMasterFailActivationToday, triggerConfigInfoTable=triggerConfigInfoTable, triggerLastTriggerActivated=triggerLastTriggerActivated, triggerScript3=triggerScript3, triggerNumOfPerodicActivationToday=triggerNumOfPerodicActivationToday, triggerNumOfInterfaceActivationToday=triggerNumOfInterfaceActivationToday, triggerActivateAfter=triggerActivateAfter, triggerTestMode=triggerTestMode, triggerActiveDaysOrDate=triggerActiveDaysOrDate, triggerSnmpTrap=triggerSnmpTrap, triggerNumOfStackXemStkActivationToday=triggerNumOfStackXemStkActivationToday, triggerNumOfActivation=triggerNumOfActivation)
