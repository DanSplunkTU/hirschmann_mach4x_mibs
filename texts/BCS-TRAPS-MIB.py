#
# PySNMP MIB module BCS-TRAPS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/arris/BCS-TRAPS-MIB
# Produced by pysmi-1.1.8 at Sun Jan 16 00:31:56 2022
# On host fv-az42-839 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
bcs, = mibBuilder.importSymbols("BCS-IDENT-MIB", "bcs")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, Counter64, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, TimeTicks, iso, Bits, Counter32, NotificationType, ObjectIdentity, IpAddress, MibIdentifier, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Counter64", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "TimeTicks", "iso", "Bits", "Counter32", "NotificationType", "ObjectIdentity", "IpAddress", "MibIdentifier", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
bcsTraps = ModuleIdentity((1, 3, 6, 1, 4, 1, 1166, 7, 3))
if mibBuilder.loadTexts: bcsTraps.setLastUpdated('200603280000Z')
if mibBuilder.loadTexts: bcsTraps.setOrganization('Motorola Connected Home Solutions')
if mibBuilder.loadTexts: bcsTraps.setContactInfo('Motorola Technical Response Center\n                      Inside USA     1-888-944-HELP (1-888-944-4357)\n                      Outside USA    1-215-323-0044\n                      TRC Hours:\n                      Monday through Friday 8am - 7pm Eastern Standard Time\n                      Saturdays            10am - 5pm Eastern Standard Time')
if mibBuilder.loadTexts: bcsTraps.setDescription('The MIB module for the bcs common trap objects.')
bcsTrapElements = MibIdentifier((1, 3, 6, 1, 4, 1, 1166, 7, 3, 1))
bcsTrapControl = MibIdentifier((1, 3, 6, 1, 4, 1, 1166, 7, 3, 2))
class ConfigChangeState(TextualConvention, Integer32):
    description = 'Represents the current state of a configuration change'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("staged", 1), ("applied", 2), ("saved", 3))

class ConfigChangeAction(TextualConvention, Integer32):
    description = 'Represents the action required to instantiate configuration change.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("waitingRetune", 1), ("waitingSave", 2), ("waitingReboot", 3))

trapIdentifier = MibScalar((1, 3, 6, 1, 4, 1, 1166, 7, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)).clone(2147483647)).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapIdentifier.setStatus('current')
if mibBuilder.loadTexts: trapIdentifier.setDescription('This object identifies the specific notification issued by the\n         network element.')
trapSequenceId = MibScalar((1, 3, 6, 1, 4, 1, 1166, 7, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapSequenceId.setStatus('current')
if mibBuilder.loadTexts: trapSequenceId.setDescription('This object identifies the specific notification issued by the\n\t  network element.')
trapNetworkElemModelNumber = MibScalar((1, 3, 6, 1, 4, 1, 1166, 7, 3, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapNetworkElemModelNumber.setStatus('current')
if mibBuilder.loadTexts: trapNetworkElemModelNumber.setDescription('The value of this object is the model number of\n         the network element.  Combination of Model # and Serial # is used as the unique\n         identifier of the NE.')
trapNetworkElemSerialNum = MibScalar((1, 3, 6, 1, 4, 1, 1166, 7, 3, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapNetworkElemSerialNum.setStatus('current')
if mibBuilder.loadTexts: trapNetworkElemSerialNum.setDescription('The value of this object is the serial number of\n         the network element. Combination of Model # and Serial # is used as the unique\n         identifier of the NE.')
trapPerceivedSeverity = MibScalar((1, 3, 6, 1, 4, 1, 1166, 7, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("cleared", 1), ("indeterminate", 2), ("warning", 3), ("minor", 4), ("major", 5), ("critical", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapPerceivedSeverity.setStatus('current')
if mibBuilder.loadTexts: trapPerceivedSeverity.setDescription('This parameter defines five severity levels, which provide \n        an indication of how it is perceived that the capability \n        of the managed object has been affected. The other level\n        is not a severity level, but indicates that an alarm has been\n        cleared, and thus is no longer in alarm state.  Note that this \n        field has no meaning for configuration change traps.          ')
trapNetworkElemOperState = MibScalar((1, 3, 6, 1, 4, 1, 1166, 7, 3, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapNetworkElemOperState.setStatus('current')
if mibBuilder.loadTexts: trapNetworkElemOperState.setDescription('The current Operational State of the Network Element\n           which generated the trap.')
trapNetworkElemAlarmStatus = MibScalar((1, 3, 6, 1, 4, 1, 1166, 7, 3, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("idle", 1), ("indeterminate", 2), ("warning", 3), ("minor", 4), ("major", 5), ("critical", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapNetworkElemAlarmStatus.setStatus('current')
if mibBuilder.loadTexts: trapNetworkElemAlarmStatus.setDescription('The current Alarm Status of the Network Element\n          Alarm Status is always equal to the highest severity\n          level of all outstanding alarms in this NE.')
trapNetworkElemAdminState = MibScalar((1, 3, 6, 1, 4, 1, 1166, 7, 3, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("locked", 1), ("unlocked", 2), ("shuttingDown", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapNetworkElemAdminState.setStatus('current')
if mibBuilder.loadTexts: trapNetworkElemAdminState.setDescription('The current Adminsitrative state of the network element.')
trapNetworkElemAvailStatus = MibScalar((1, 3, 6, 1, 4, 1, 1166, 7, 3, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("inTest", 1), ("failed", 2), ("powerOff", 3), ("offLine", 4), ("offDuty", 5), ("dependency", 6), ("degraded", 7), ("notInstalled", 8), ("logFull", 9), ("available", 10)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapNetworkElemAvailStatus.setStatus('current')
if mibBuilder.loadTexts: trapNetworkElemAvailStatus.setDescription('The current Operational state of the network elment\n          is defined in ISO/IEC 10164-2.')
trapText = MibScalar((1, 3, 6, 1, 4, 1, 1166, 7, 3, 1, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapText.setStatus('current')
if mibBuilder.loadTexts: trapText.setDescription('This  variable contains an optional trap text.')
trapNETrapLastTrapTimeStamp = MibScalar((1, 3, 6, 1, 4, 1, 1166, 7, 3, 1, 11), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapNETrapLastTrapTimeStamp.setStatus('current')
if mibBuilder.loadTexts: trapNETrapLastTrapTimeStamp.setDescription('This OBJECT IDENTIFIER is used to hold time, in hundreths of a second since the\n          network management portion of the system was last re-initialized.')
trapChangedObjectId = MibScalar((1, 3, 6, 1, 4, 1, 1166, 7, 3, 1, 12), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapChangedObjectId.setStatus('current')
if mibBuilder.loadTexts: trapChangedObjectId.setDescription('This  variable identifies the object that\n \t has generated the trap.')
trapAdditionalInfoInteger1 = MibScalar((1, 3, 6, 1, 4, 1, 1166, 7, 3, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)).clone(2147483647)).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapAdditionalInfoInteger1.setStatus('current')
if mibBuilder.loadTexts: trapAdditionalInfoInteger1.setDescription('This 32 bit integer is used to hold specific information about \n         the trap.')
trapAdditionalInfoInteger2 = MibScalar((1, 3, 6, 1, 4, 1, 1166, 7, 3, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)).clone(2147483647)).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapAdditionalInfoInteger2.setStatus('current')
if mibBuilder.loadTexts: trapAdditionalInfoInteger2.setDescription('This 32 bit integer is used to hold specific information about \n         the trap.           ')
trapAdditionalInfoInteger3 = MibScalar((1, 3, 6, 1, 4, 1, 1166, 7, 3, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)).clone(2147483647)).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapAdditionalInfoInteger3.setStatus('current')
if mibBuilder.loadTexts: trapAdditionalInfoInteger3.setDescription('This 32 bit integer is used to hold specific information about \n         the trap.            ')
trapChangedValueDisplayString = MibScalar((1, 3, 6, 1, 4, 1, 1166, 7, 3, 1, 16), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapChangedValueDisplayString.setStatus('current')
if mibBuilder.loadTexts: trapChangedValueDisplayString.setDescription('This DisplayString is used to hold specific information about\n         the trap.')
trapChangedValueOID = MibScalar((1, 3, 6, 1, 4, 1, 1166, 7, 3, 1, 17), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapChangedValueOID.setStatus('current')
if mibBuilder.loadTexts: trapChangedValueOID.setDescription('This OBJECT IDENTIFIER is used to hold specific information about \n        the trap.')
trapChangedValueIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 1166, 7, 3, 1, 18), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapChangedValueIpAddress.setStatus('current')
if mibBuilder.loadTexts: trapChangedValueIpAddress.setDescription('This OBJECT IDENTIFIER is used to hold specific information about \n        the trap.')
trapChangedValueInteger = MibScalar((1, 3, 6, 1, 4, 1, 1166, 7, 3, 1, 19), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)).clone(2147483647)).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapChangedValueInteger.setStatus('current')
if mibBuilder.loadTexts: trapChangedValueInteger.setDescription('This 32 bit integer is used to hold specific information about \n         the trap.          ')
numberOfTrapReceivers = MibScalar((1, 3, 6, 1, 4, 1, 1166, 7, 3, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: numberOfTrapReceivers.setStatus('current')
if mibBuilder.loadTexts: numberOfTrapReceivers.setDescription('The number of managers to send traps to.\n         This number can not exceed 4')
trapReceiversTable = MibTable((1, 3, 6, 1, 4, 1, 1166, 7, 3, 2, 2), )
if mibBuilder.loadTexts: trapReceiversTable.setStatus('current')
if mibBuilder.loadTexts: trapReceiversTable.setDescription('A list of managers to send traps to.  The number of\n        entries is given by the value of NumTrapReceivers.\n        Maximum number of Trap Receivers is four.')
trapReceiversEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1166, 7, 3, 2, 2, 1), ).setIndexNames((0, "BCS-TRAPS-MIB", "trapReceiversTableIndex"))
if mibBuilder.loadTexts: trapReceiversEntry.setStatus('current')
if mibBuilder.loadTexts: trapReceiversEntry.setDescription('The list of managers to send traps.')
trapReceiversTableIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 7, 3, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4)))
if mibBuilder.loadTexts: trapReceiversTableIndex.setStatus('current')
if mibBuilder.loadTexts: trapReceiversTableIndex.setDescription('The index to a trap receiver entry.')
trapReceiverAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 7, 3, 2, 2, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trapReceiverAddr.setStatus('current')
if mibBuilder.loadTexts: trapReceiverAddr.setDescription("The IP address of the manager to send a trap to.\n          NOTE: Changing TrapReceiverAddr FROM default value to\n          anything else is equivalent of 'creating' of a new entry.\n          Changing trapReceiverAddr TO default value will result\n          in deletion of that entry.")
trapReceiverCommunityString = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 7, 3, 2, 2, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trapReceiverCommunityString.setStatus('current')
if mibBuilder.loadTexts: trapReceiverCommunityString.setDescription('The community name to use in the trap when\n         sent to the manager.')
trapToBeSendQueueSize = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 7, 3, 2, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(50, 1000)).clone(50)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trapToBeSendQueueSize.setStatus('current')
if mibBuilder.loadTexts: trapToBeSendQueueSize.setDescription('The agent maintains 2 queues: TrapsToBeSendQueue and TrapsSentQueue.\n         The SNMP agent can receive a burst of traps which need to be sent\n         to the network manager.  The SNMP agent will put them in\n         TrapsToBeSendQueue and from there hi will send traps to the\n         a manager at throttling rate.  The traps will be kept in sequence\n         by the time at which they came in ')
trapSentQueueSize = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 7, 3, 2, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(50, 300)).clone(50)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trapSentQueueSize.setStatus('current')
if mibBuilder.loadTexts: trapSentQueueSize.setDescription("The agent maintains 2 queues: TrapsToBeSendQueue and TrapsSentQueue.\n         The SNMP agent maintains Trap History (TrapsSentQueue) by saving last 'X'\n         sent traps.")
trapThrottlingRate = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 7, 3, 2, 2, 1, 6), Integer32().clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trapThrottlingRate.setStatus('current')
if mibBuilder.loadTexts: trapThrottlingRate.setDescription('The number of traps agent can send to a particular manager\n         (trapReceiver) per second. ')
trapLastSent = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 7, 3, 2, 2, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)).clone(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapLastSent.setStatus('current')
if mibBuilder.loadTexts: trapLastSent.setDescription('This variable contains the last trapSequenceId (sequence number) \n         agent sent to this manager.  Upon startup agent will send\n         cold-start trap and set value of TrapLastSent to 1.')
trapReceiversEntryOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 7, 3, 2, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trapReceiversEntryOperState.setStatus('current')
if mibBuilder.loadTexts: trapReceiversEntryOperState.setDescription('The current Operational State of this entry\n         in trapReceivers Table ')
trapResendRequest = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 7, 3, 2, 2, 1, 9), Integer32().clone(2147483647)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trapResendRequest.setStatus('current')
if mibBuilder.loadTexts: trapResendRequest.setDescription('The manager may write this object when the indicated trap \n         (indicated via trapIdentifier) should be resent.  It is not \n         intended to be read by the manager, but is read-write for\n         compatability with older SNMP compilers.')
numberOfDiscriminators = MibScalar((1, 3, 6, 1, 4, 1, 1166, 7, 3, 2, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)).clone(2147483647)).setMaxAccess("readonly")
if mibBuilder.loadTexts: numberOfDiscriminators.setStatus('current')
if mibBuilder.loadTexts: numberOfDiscriminators.setDescription("The number of EFDs (filters) agent has in it's database.\n          This number can not exceed 20 ")
trapDiscrimTable = MibTable((1, 3, 6, 1, 4, 1, 1166, 7, 3, 2, 4), )
if mibBuilder.loadTexts: trapDiscrimTable.setStatus('current')
if mibBuilder.loadTexts: trapDiscrimTable.setDescription('A list of EFDs (trap filters).  Before forwarding trap to\n          a trapReceiver (manager) agent filters all traps acording\n          to all EFDs defined for this manager.')
trapDiscrimEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1166, 7, 3, 2, 4, 1), ).setIndexNames((0, "BCS-TRAPS-MIB", "trapDiscrimTableIndex"))
if mibBuilder.loadTexts: trapDiscrimEntry.setStatus('current')
if mibBuilder.loadTexts: trapDiscrimEntry.setDescription('The list of discriminators (trap filters.)')
trapDiscrimTableIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 7, 3, 2, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 20)))
if mibBuilder.loadTexts: trapDiscrimTableIndex.setStatus('current')
if mibBuilder.loadTexts: trapDiscrimTableIndex.setDescription('The index to a trap discriminator entry.')
trapDiscrimReceiverAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 7, 3, 2, 4, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trapDiscrimReceiverAddr.setStatus('current')
if mibBuilder.loadTexts: trapDiscrimReceiverAddr.setDescription("The IP address of the manager this Discrim belongs to.\n          It should be equal to TrapReceiverAddr.\n          NOTE: Changing trapDiscrimReceiverAddr FROM default value to\n          anything else is equivalent of 'creating' of a new entry.\n          Changing trapReceiverAddr TO default value will result\n          in deletion of that entry.")
trapDiscrimAvailabilityStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 7, 3, 2, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(5, 10))).clone(namedValues=NamedValues(("offDuty", 5), ("available", 10)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapDiscrimAvailabilityStatus.setStatus('current')
if mibBuilder.loadTexts: trapDiscrimAvailabilityStatus.setDescription('This object reflects the current Availability status of the\n         Discrim (based on ISO/IEC 10164-2).')
trapDiscrimWeeklyMask = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 7, 3, 2, 4, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trapDiscrimWeeklyMask.setStatus('current')
if mibBuilder.loadTexts: trapDiscrimWeeklyMask.setDescription("This object represents weekly scedule for corresponding\n         Discrim.  The WeeklyMask consists of 7 numeric \n         characters (1 for each day of the week).  Each numeric\n         character can take a value of either '1' - enabled or \n         '2' - disabled.  For example, with WeeklyMask='1122221',\n         an agent will apply corresponding Discriminator only on\n         Mondays, Tuesdays and Sundays.\n         Any characters other than '1' and '2' will be ignored.")
trapDiscrimDailyStartTime = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 7, 3, 2, 4, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1439))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trapDiscrimDailyStartTime.setStatus('current')
if mibBuilder.loadTexts: trapDiscrimDailyStartTime.setDescription('This object represents daily start time for corresponding\n         Discrim.  The StartTime is expressed as an offset\n         (in minutes) from 2400 hours military time.  For example,\n         StartTime=70 represents start time of 1:10 AM.')
trapDiscrimDailyStopTime = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 7, 3, 2, 4, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1439))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trapDiscrimDailyStopTime.setStatus('current')
if mibBuilder.loadTexts: trapDiscrimDailyStopTime.setDescription('This object represents daily stop time for corresponding\n        Discrim.  The StopTime is expressed as an offset\n        (in minutes) from 2400 hours military time.  For example,\n        StopTime=70 represents stop time of 1:10 AM.')
trapSeverityDiscrim = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 7, 3, 2, 4, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("indeterminate", 2), ("warning", 3), ("minor", 4), ("major", 5), ("critical", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trapSeverityDiscrim.setStatus('current')
if mibBuilder.loadTexts: trapSeverityDiscrim.setDescription('The severity threshold of traps to be send to the manager.\n         Only traps of equal or greater severity than\n         this value are sent to the manager.')
trapDiscrimOperationalState = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 7, 3, 2, 4, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trapDiscrimOperationalState.setStatus('current')
if mibBuilder.loadTexts: trapDiscrimOperationalState.setDescription('The current Operational State of the Discriminator. ')
trapDiscrimConfigChangeCntl = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 7, 3, 2, 4, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2))).clone('on')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trapDiscrimConfigChangeCntl.setStatus('current')
if mibBuilder.loadTexts: trapDiscrimConfigChangeCntl.setDescription('This variable turns reporting of configuration changes \n         on or off. ')
mibBuilder.exportSymbols("BCS-TRAPS-MIB", trapDiscrimTableIndex=trapDiscrimTableIndex, trapDiscrimWeeklyMask=trapDiscrimWeeklyMask, trapNetworkElemAdminState=trapNetworkElemAdminState, trapIdentifier=trapIdentifier, trapReceiversEntryOperState=trapReceiversEntryOperState, trapDiscrimOperationalState=trapDiscrimOperationalState, trapToBeSendQueueSize=trapToBeSendQueueSize, trapNetworkElemAvailStatus=trapNetworkElemAvailStatus, trapDiscrimDailyStartTime=trapDiscrimDailyStartTime, trapNETrapLastTrapTimeStamp=trapNETrapLastTrapTimeStamp, trapChangedValueInteger=trapChangedValueInteger, trapChangedObjectId=trapChangedObjectId, trapChangedValueDisplayString=trapChangedValueDisplayString, trapDiscrimAvailabilityStatus=trapDiscrimAvailabilityStatus, trapNetworkElemOperState=trapNetworkElemOperState, trapThrottlingRate=trapThrottlingRate, PYSNMP_MODULE_ID=bcsTraps, trapPerceivedSeverity=trapPerceivedSeverity, trapReceiverCommunityString=trapReceiverCommunityString, trapNetworkElemModelNumber=trapNetworkElemModelNumber, trapChangedValueOID=trapChangedValueOID, trapSentQueueSize=trapSentQueueSize, trapDiscrimEntry=trapDiscrimEntry, trapNetworkElemAlarmStatus=trapNetworkElemAlarmStatus, bcsTrapControl=bcsTrapControl, trapLastSent=trapLastSent, trapDiscrimTable=trapDiscrimTable, trapSeverityDiscrim=trapSeverityDiscrim, trapReceiversTableIndex=trapReceiversTableIndex, trapReceiversEntry=trapReceiversEntry, trapResendRequest=trapResendRequest, trapAdditionalInfoInteger3=trapAdditionalInfoInteger3, trapReceiversTable=trapReceiversTable, ConfigChangeState=ConfigChangeState, numberOfDiscriminators=numberOfDiscriminators, ConfigChangeAction=ConfigChangeAction, trapChangedValueIpAddress=trapChangedValueIpAddress, trapDiscrimReceiverAddr=trapDiscrimReceiverAddr, trapDiscrimDailyStopTime=trapDiscrimDailyStopTime, trapDiscrimConfigChangeCntl=trapDiscrimConfigChangeCntl, trapNetworkElemSerialNum=trapNetworkElemSerialNum, trapAdditionalInfoInteger2=trapAdditionalInfoInteger2, bcsTraps=bcsTraps, trapReceiverAddr=trapReceiverAddr, numberOfTrapReceivers=numberOfTrapReceivers, bcsTrapElements=bcsTrapElements, trapSequenceId=trapSequenceId, trapText=trapText, trapAdditionalInfoInteger1=trapAdditionalInfoInteger1)
