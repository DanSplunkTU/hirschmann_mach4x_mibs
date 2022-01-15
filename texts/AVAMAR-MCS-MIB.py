#
# PySNMP MIB module AVAMAR-MCS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/avamar/AVAMAR-MCS-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 17:52:24 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, NotificationType, Integer32, Bits, NotificationType, iso, ObjectIdentity, Unsigned32, IpAddress, Gauge32, Counter64, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Counter32, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "NotificationType", "Integer32", "Bits", "NotificationType", "iso", "ObjectIdentity", "Unsigned32", "IpAddress", "Gauge32", "Counter64", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Counter32", "enterprises")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
avamar = MibIdentifier((1, 3, 6, 1, 4, 1, 15597))
software = MibIdentifier((1, 3, 6, 1, 4, 1, 15597, 1))
mcs = MibIdentifier((1, 3, 6, 1, 4, 1, 15597, 1, 1))
event = MibIdentifier((1, 3, 6, 1, 4, 1, 15597, 1, 1, 1))
eventTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 15597, 1, 1, 1, 1))
eventData = MibIdentifier((1, 3, 6, 1, 4, 1, 15597, 1, 1, 1, 2))
burm = MibIdentifier((1, 3, 6, 1, 4, 1, 15597, 1, 1, 2))
burmTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 15597, 1, 1, 2, 1))
burmLastActivityData = MibIdentifier((1, 3, 6, 1, 4, 1, 15597, 1, 1, 2, 2))
burmSchedulerData = MibIdentifier((1, 3, 6, 1, 4, 1, 15597, 1, 1, 2, 3))
dpn = MibIdentifier((1, 3, 6, 1, 4, 1, 15597, 1, 1, 3))
dpnTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 15597, 1, 1, 3, 1))
dpnData = MibIdentifier((1, 3, 6, 1, 4, 1, 15597, 1, 1, 3, 2))
eventTrap = NotificationType((1, 3, 6, 1, 4, 1, 15597, 1, 1, 1, 1) + (0,1)).setObjects(("AVAMAR-MCS-MIB", "eventCode"), ("AVAMAR-MCS-MIB", "eventTimestamp"), ("AVAMAR-MCS-MIB", "eventCategory"), ("AVAMAR-MCS-MIB", "eventType"), ("AVAMAR-MCS-MIB", "eventSummary"), ("AVAMAR-MCS-MIB", "eventHwSource"), ("AVAMAR-MCS-MIB", "eventSwSource"))
if mibBuilder.loadTexts: eventTrap.setDescription('The last event reported by the mcs.')
testEventTrap = NotificationType((1, 3, 6, 1, 4, 1, 15597, 1, 1, 1, 1) + (0,2)).setObjects(("AVAMAR-MCS-MIB", "eventCode"))
if mibBuilder.loadTexts: testEventTrap.setDescription('Test trap for verifying profile.')
eventCode = MibScalar((1, 3, 6, 1, 4, 1, 15597, 1, 1, 1, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventCode.setStatus('mandatory')
if mibBuilder.loadTexts: eventCode.setDescription('Unique code identifying the specific activity,\n                 condition, or status.')
eventTimestamp = MibScalar((1, 3, 6, 1, 4, 1, 15597, 1, 1, 1, 2, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventTimestamp.setStatus('mandatory')
if mibBuilder.loadTexts: eventTimestamp.setDescription('Date event was reported')
eventCategory = MibScalar((1, 3, 6, 1, 4, 1, 15597, 1, 1, 1, 2, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 25))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventCategory.setStatus('mandatory')
if mibBuilder.loadTexts: eventCategory.setDescription('Category of event (SYSTEM, APPLICATION, USER,\n                 SECURITY)')
eventType = MibScalar((1, 3, 6, 1, 4, 1, 15597, 1, 1, 1, 2, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 25))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventType.setStatus('mandatory')
if mibBuilder.loadTexts: eventType.setDescription('Type of event (INTERNAL, ERROR, WARNING, INFORMATION,\n                 DEBUG')
eventSummary = MibScalar((1, 3, 6, 1, 4, 1, 15597, 1, 1, 1, 2, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventSummary.setStatus('mandatory')
if mibBuilder.loadTexts: eventSummary.setDescription('One line summary description of event reported')
eventHwSource = MibScalar((1, 3, 6, 1, 4, 1, 15597, 1, 1, 1, 2, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventHwSource.setStatus('mandatory')
if mibBuilder.loadTexts: eventHwSource.setDescription('System node that reported the event')
eventSwSource = MibScalar((1, 3, 6, 1, 4, 1, 15597, 1, 1, 1, 2, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventSwSource.setStatus('mandatory')
if mibBuilder.loadTexts: eventSwSource.setDescription('System or application module that reported the event')
burmActivityTrap = NotificationType((1, 3, 6, 1, 4, 1, 15597, 1, 1, 2, 1) + (0,1)).setObjects(("AVAMAR-MCS-MIB", "lastActivityClient"), ("AVAMAR-MCS-MIB", "lastActivityDomain"), ("AVAMAR-MCS-MIB", "lastActivityGroup"), ("AVAMAR-MCS-MIB", "lastActivityPlugInName"), ("AVAMAR-MCS-MIB", "lastActivityType"), ("AVAMAR-MCS-MIB", "lastActivityDataset"), ("AVAMAR-MCS-MIB", "lastActivitySchedule"), ("AVAMAR-MCS-MIB", "lastActivityRetentionPolicy"), ("AVAMAR-MCS-MIB", "lastActivityBytesScanned"), ("AVAMAR-MCS-MIB", "lastActivityBytesModifiedSent"), ("AVAMAR-MCS-MIB", "lastActivityStatusCode"), ("AVAMAR-MCS-MIB", "lastActivityErrorCode"), ("AVAMAR-MCS-MIB", "lastActivityBackupLabel"), ("AVAMAR-MCS-MIB", "lastActivityBackupNumber"))
if mibBuilder.loadTexts: burmActivityTrap.setDescription('The last activity reported by the mcs.')
lastActivityClient = MibScalar((1, 3, 6, 1, 4, 1, 15597, 1, 1, 2, 2, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lastActivityClient.setStatus('mandatory')
if mibBuilder.loadTexts: lastActivityClient.setDescription('The client name.')
lastActivityDomain = MibScalar((1, 3, 6, 1, 4, 1, 15597, 1, 1, 2, 2, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lastActivityDomain.setStatus('mandatory')
if mibBuilder.loadTexts: lastActivityDomain.setDescription('The domain of the client is in.')
lastActivityGroup = MibScalar((1, 3, 6, 1, 4, 1, 15597, 1, 1, 2, 2, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lastActivityGroup.setStatus('mandatory')
if mibBuilder.loadTexts: lastActivityGroup.setDescription('The group that this client belongs to.')
lastActivityPlugInName = MibScalar((1, 3, 6, 1, 4, 1, 15597, 1, 1, 2, 2, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lastActivityPlugInName.setStatus('mandatory')
if mibBuilder.loadTexts: lastActivityPlugInName.setDescription('The plug-in this client is using for this activity.')
lastActivityType = MibScalar((1, 3, 6, 1, 4, 1, 15597, 1, 1, 2, 2, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lastActivityType.setStatus('mandatory')
if mibBuilder.loadTexts: lastActivityType.setDescription('The activity type.')
lastActivityDataset = MibScalar((1, 3, 6, 1, 4, 1, 15597, 1, 1, 2, 2, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lastActivityDataset.setStatus('mandatory')
if mibBuilder.loadTexts: lastActivityDataset.setDescription('The dataset this client is using for this activity.')
lastActivitySchedule = MibScalar((1, 3, 6, 1, 4, 1, 15597, 1, 1, 2, 2, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lastActivitySchedule.setStatus('mandatory')
if mibBuilder.loadTexts: lastActivitySchedule.setDescription('The schedule that initiated this activity.')
lastActivityRetentionPolicy = MibScalar((1, 3, 6, 1, 4, 1, 15597, 1, 1, 2, 2, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lastActivityRetentionPolicy.setStatus('mandatory')
if mibBuilder.loadTexts: lastActivityRetentionPolicy.setDescription('The retention policy for the backup resulting from this\n                 activity.')
lastActivityBytesScanned = MibScalar((1, 3, 6, 1, 4, 1, 15597, 1, 1, 2, 2, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 25))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lastActivityBytesScanned.setStatus('mandatory')
if mibBuilder.loadTexts: lastActivityBytesScanned.setDescription('The number of bytes scanned during this activity.')
lastActivityBytesModifiedSent = MibScalar((1, 3, 6, 1, 4, 1, 15597, 1, 1, 2, 2, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 25))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lastActivityBytesModifiedSent.setStatus('mandatory')
if mibBuilder.loadTexts: lastActivityBytesModifiedSent.setDescription('The number of modified bytes sent during a backup.')
lastActivityStatusCode = MibScalar((1, 3, 6, 1, 4, 1, 15597, 1, 1, 2, 2, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lastActivityStatusCode.setStatus('mandatory')
if mibBuilder.loadTexts: lastActivityStatusCode.setDescription('The activity status event code.')
lastActivityErrorCode = MibScalar((1, 3, 6, 1, 4, 1, 15597, 1, 1, 2, 2, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lastActivityErrorCode.setStatus('mandatory')
if mibBuilder.loadTexts: lastActivityErrorCode.setDescription('A failure event code if this activity failed.')
lastActivityBackupLabel = MibScalar((1, 3, 6, 1, 4, 1, 15597, 1, 1, 2, 2, 13), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lastActivityBackupLabel.setStatus('mandatory')
if mibBuilder.loadTexts: lastActivityBackupLabel.setDescription('The backup label for this activity.')
lastActivityBackupNumber = MibScalar((1, 3, 6, 1, 4, 1, 15597, 1, 1, 2, 2, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lastActivityBackupNumber.setStatus('mandatory')
if mibBuilder.loadTexts: lastActivityBackupNumber.setDescription('The backup number for this activity.')
schedulerStatus = MibScalar((1, 3, 6, 1, 4, 1, 15597, 1, 1, 2, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("suspended", 1), ("running", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: schedulerStatus.setStatus('mandatory')
if mibBuilder.loadTexts: schedulerStatus.setDescription('Status of scheduler, either suspended or running.')
serverStatus = MibScalar((1, 3, 6, 1, 4, 1, 15597, 1, 1, 3, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))).clone(namedValues=NamedValues(("unsupported", 1), ("inactive", 2), ("offline", 3), ("suspended", 4), ("adminreadonly", 5), ("adminonly", 6), ("readonly", 7), ("synchronizing", 8), ("admin", 9), ("fullaccess", 10), ("degraded", 11), ("ddrinactive", 12)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: serverStatus.setStatus('mandatory')
if mibBuilder.loadTexts: serverStatus.setDescription('Status of Avamar Server')
activeSessions = MibScalar((1, 3, 6, 1, 4, 1, 15597, 1, 1, 3, 2, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: activeSessions.setStatus('mandatory')
if mibBuilder.loadTexts: activeSessions.setDescription('Number of active avtar sessions')
freeMegabytes = MibScalar((1, 3, 6, 1, 4, 1, 15597, 1, 1, 3, 2, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: freeMegabytes.setStatus('mandatory')
if mibBuilder.loadTexts: freeMegabytes.setDescription('Number of megabytes free on the Avamar Server')
reservedMegabytes = MibScalar((1, 3, 6, 1, 4, 1, 15597, 1, 1, 3, 2, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: reservedMegabytes.setStatus('mandatory')
if mibBuilder.loadTexts: reservedMegabytes.setDescription('Number of megabytes reserved for data storage on the\n                 Avamar Server')
utilization = MibScalar((1, 3, 6, 1, 4, 1, 15597, 1, 1, 3, 2, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: utilization.setStatus('mandatory')
if mibBuilder.loadTexts: utilization.setDescription('Percentage of storage used on the Avamar Server in\n                 tenths of a percent')
protectedMegabytes = MibScalar((1, 3, 6, 1, 4, 1, 15597, 1, 1, 3, 2, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: protectedMegabytes.setStatus('mandatory')
if mibBuilder.loadTexts: protectedMegabytes.setDescription('Number of megabytes of protected data stored on the\n                 Avamar Server')
lastCheckpoint = MibScalar((1, 3, 6, 1, 4, 1, 15597, 1, 1, 3, 2, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lastCheckpoint.setStatus('mandatory')
if mibBuilder.loadTexts: lastCheckpoint.setDescription('The date & time the last checkpoint was taken')
lastValidatedCheckpoint = MibScalar((1, 3, 6, 1, 4, 1, 15597, 1, 1, 3, 2, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lastValidatedCheckpoint.setStatus('mandatory')
if mibBuilder.loadTexts: lastValidatedCheckpoint.setDescription('The date & time of the last checkpoint that has been\n                 validated')
timeSinceLastCheckpoint = MibScalar((1, 3, 6, 1, 4, 1, 15597, 1, 1, 3, 2, 9), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: timeSinceLastCheckpoint.setStatus('mandatory')
if mibBuilder.loadTexts: timeSinceLastCheckpoint.setDescription('The time since the last checkpoint was taken')
timeSinceLastValidatedCheckpoint = MibScalar((1, 3, 6, 1, 4, 1, 15597, 1, 1, 3, 2, 10), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: timeSinceLastValidatedCheckpoint.setStatus('mandatory')
if mibBuilder.loadTexts: timeSinceLastValidatedCheckpoint.setDescription('The time since the last validated checkpoint was taken')
mibBuilder.exportSymbols("AVAMAR-MCS-MIB", avamar=avamar, timeSinceLastCheckpoint=timeSinceLastCheckpoint, timeSinceLastValidatedCheckpoint=timeSinceLastValidatedCheckpoint, lastActivityErrorCode=lastActivityErrorCode, lastActivityBackupNumber=lastActivityBackupNumber, lastActivitySchedule=lastActivitySchedule, utilization=utilization, mcs=mcs, activeSessions=activeSessions, software=software, lastActivityStatusCode=lastActivityStatusCode, lastActivityGroup=lastActivityGroup, eventCode=eventCode, lastActivityBytesModifiedSent=lastActivityBytesModifiedSent, reservedMegabytes=reservedMegabytes, lastActivityDataset=lastActivityDataset, burmSchedulerData=burmSchedulerData, protectedMegabytes=protectedMegabytes, lastActivityBytesScanned=lastActivityBytesScanned, eventTraps=eventTraps, burmActivityTrap=burmActivityTrap, schedulerStatus=schedulerStatus, eventTrap=eventTrap, lastActivityClient=lastActivityClient, lastCheckpoint=lastCheckpoint, lastActivityBackupLabel=lastActivityBackupLabel, dpn=dpn, serverStatus=serverStatus, testEventTrap=testEventTrap, eventType=eventType, eventSwSource=eventSwSource, lastActivityRetentionPolicy=lastActivityRetentionPolicy, freeMegabytes=freeMegabytes, dpnTraps=dpnTraps, eventHwSource=eventHwSource, lastActivityDomain=lastActivityDomain, lastActivityType=lastActivityType, dpnData=dpnData, event=event, burmLastActivityData=burmLastActivityData, burm=burm, eventData=eventData, burmTraps=burmTraps, eventSummary=eventSummary, eventTimestamp=eventTimestamp, lastActivityPlugInName=lastActivityPlugInName, eventCategory=eventCategory, lastValidatedCheckpoint=lastValidatedCheckpoint)
