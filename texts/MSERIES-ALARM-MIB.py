#
# PySNMP MIB module MSERIES-ALARM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/smartoptics/MSERIES-ALARM-MIB
# Produced by pysmi-1.1.3 at Sun Nov 21 00:40:22 2021
# On host fv-az39-63 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
mseries, = mibBuilder.importSymbols("MSERIES-MIB", "mseries")
AlarmNotificationType, AlarmPerceivedSeverity, PortType, UnitType, AlarmProbableCause = mibBuilder.importSymbols("MSERIES-TC", "AlarmNotificationType", "AlarmPerceivedSeverity", "PortType", "UnitType", "AlarmProbableCause")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Integer32, ObjectIdentity, NotificationType, Counter32, iso, TimeTicks, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Bits, Counter64, MibIdentifier, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "ObjectIdentity", "NotificationType", "Counter32", "iso", "TimeTicks", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Bits", "Counter64", "MibIdentifier", "IpAddress")
DisplayString, TextualConvention, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "DateAndTime")
smartAlarm = ModuleIdentity((1, 3, 6, 1, 4, 1, 30826, 1, 1))
smartAlarm.setRevisions(('2014-02-12 14:15', '2013-10-15 13:41', '2011-12-05 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: smartAlarm.setRevisionsDescriptions(('Added alarmLogList and smartAlarmMIBConformance.', 'Added alarmHostName, alarmPortName and alarmPortType to AlarmEntry.\n                                 Added alarmHostName, alarmPortName and alarmPortType to\n                                 alarmNotificationCleared, alarmNotificationWarning,\n                                 alarmNotificationMinor, alarmNotificationMajor,\n                                 and alarmNotificationCritical.\n\n                                 Also alarmPort reports different numbers against before\n                                 (changed from SmartOS v2.1). 1-10 means Line ports\n                                 and 11 and above means Client port.\n\n                                 Descriptions are also updated.', 'Initial revision.\n\n                                 Added notifications.',))
if mibBuilder.loadTexts: smartAlarm.setLastUpdated('201402121415Z')
if mibBuilder.loadTexts: smartAlarm.setOrganization('SmartOptics')
if mibBuilder.loadTexts: smartAlarm.setContactInfo('http://www.smartoptics.com')
if mibBuilder.loadTexts: smartAlarm.setDescription('This is the enterprise specific Alarm MIB for SmartOptics M-Series')
alarmGeneral = MibIdentifier((1, 3, 6, 1, 4, 1, 30826, 1, 1, 1))
alarmActiveList = MibIdentifier((1, 3, 6, 1, 4, 1, 30826, 1, 1, 2))
alarmLogList = MibIdentifier((1, 3, 6, 1, 4, 1, 30826, 1, 1, 3))
alarmNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 30826, 1, 1, 4))
smartAlarmMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 30826, 1, 1, 5))
smartAlarmGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 30826, 1, 1, 5, 1))
smartAlarmCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 30826, 1, 1, 5, 2))
smartAlarmGeneralLastSeqNumber = MibScalar((1, 3, 6, 1, 4, 1, 30826, 1, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: smartAlarmGeneralLastSeqNumber.setStatus('current')
if mibBuilder.loadTexts: smartAlarmGeneralLastSeqNumber.setDescription('The sequence number of the last sent notification.')
smartAlarmGeneralHighestSeverity = MibScalar((1, 3, 6, 1, 4, 1, 30826, 1, 1, 1, 2), AlarmPerceivedSeverity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: smartAlarmGeneralHighestSeverity.setStatus('current')
if mibBuilder.loadTexts: smartAlarmGeneralHighestSeverity.setDescription('The current highest severity of the active alarms.')
smartAlarmGeneralNumberActiveList = MibScalar((1, 3, 6, 1, 4, 1, 30826, 1, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: smartAlarmGeneralNumberActiveList.setStatus('current')
if mibBuilder.loadTexts: smartAlarmGeneralNumberActiveList.setDescription('The number of active alarms in the alarmActiveList.')
smartAlarmGeneralNumberLogList = MibScalar((1, 3, 6, 1, 4, 1, 30826, 1, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: smartAlarmGeneralNumberLogList.setStatus('current')
if mibBuilder.loadTexts: smartAlarmGeneralNumberLogList.setDescription('The number of alarms in the alarmLogList.')
alarmActiveTable = MibTable((1, 3, 6, 1, 4, 1, 30826, 1, 1, 2, 1), )
if mibBuilder.loadTexts: alarmActiveTable.setStatus('current')
if mibBuilder.loadTexts: alarmActiveTable.setDescription('The active alarm list.')
alarmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30826, 1, 1, 2, 1, 1), ).setIndexNames((0, "MSERIES-ALARM-MIB", "alarmIndex"))
if mibBuilder.loadTexts: alarmEntry.setStatus('current')
if mibBuilder.loadTexts: alarmEntry.setDescription('An entry in the active alarm list.')
alarmIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 30826, 1, 1, 2, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmIndex.setStatus('current')
if mibBuilder.loadTexts: alarmIndex.setDescription('An unique index assigned to each alarm.')
alarmUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 30826, 1, 1, 2, 1, 1, 2), UnitType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmUnit.setStatus('current')
if mibBuilder.loadTexts: alarmUnit.setDescription('The alarming unit associated with this alarm.\n        undefined(0), nmb(1), psu1(2), psu2(3), fan(4), system&#40;5&#41;,\n        slaveNmb(6), slavePsu1(7), slavePsu2(8), slaveFan(9).')
alarmPort = MibTableColumn((1, 3, 6, 1, 4, 1, 30826, 1, 1, 2, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmPort.setStatus('current')
if mibBuilder.loadTexts: alarmPort.setDescription('The alarming port associated with this alarm.\n        1-10 is Line Ports. 11 and higher is Client ports. For non port alarms this value is 0.')
alarmText = MibTableColumn((1, 3, 6, 1, 4, 1, 30826, 1, 1, 2, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmText.setStatus('current')
if mibBuilder.loadTexts: alarmText.setDescription('The additional text for the alarm.')
alarmSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 30826, 1, 1, 2, 1, 1, 5), AlarmPerceivedSeverity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmSeverity.setStatus('current')
if mibBuilder.loadTexts: alarmSeverity.setDescription('The severity of the alarm as defined in\n        ITU-T X.733.')
alarmActivationTime = MibTableColumn((1, 3, 6, 1, 4, 1, 30826, 1, 1, 2, 1, 1, 6), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmActivationTime.setStatus('current')
if mibBuilder.loadTexts: alarmActivationTime.setDescription('The time when the alarm was created.')
alarmCeaseTime = MibTableColumn((1, 3, 6, 1, 4, 1, 30826, 1, 1, 2, 1, 1, 7), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmCeaseTime.setStatus('current')
if mibBuilder.loadTexts: alarmCeaseTime.setDescription('The time when the alarm was ceased.')
alarmSeqNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 30826, 1, 1, 2, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmSeqNumber.setStatus('current')
if mibBuilder.loadTexts: alarmSeqNumber.setDescription('The last sequence number used when issuing\n        a notification for this alarm.')
alarmHostName = MibTableColumn((1, 3, 6, 1, 4, 1, 30826, 1, 1, 2, 1, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmHostName.setStatus('current')
if mibBuilder.loadTexts: alarmHostName.setDescription('The hostname.')
alarmPortName = MibTableColumn((1, 3, 6, 1, 4, 1, 30826, 1, 1, 2, 1, 1, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmPortName.setStatus('current')
if mibBuilder.loadTexts: alarmPortName.setDescription('The Port Name.')
alarmPortType = MibTableColumn((1, 3, 6, 1, 4, 1, 30826, 1, 1, 2, 1, 1, 11), PortType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmPortType.setStatus('current')
if mibBuilder.loadTexts: alarmPortType.setDescription('The Port Type. undefined(0), rx(1), tx(2), biDi(3).')
alarmType = MibTableColumn((1, 3, 6, 1, 4, 1, 30826, 1, 1, 2, 1, 1, 12), AlarmNotificationType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmType.setStatus('current')
if mibBuilder.loadTexts: alarmType.setDescription('The type of alarm as defined in ITU-T X.733\n         undefined (0),\n         other (1),\n         communicationsAlarm (2),\n         qualityOfServiceAlarm (3),\n         processingErrorAlarm (4),\n         equipmentAlarm (5),\n         environmental (6),\n         integrityViolation (7),\n         operationalViolation (8),\n         physicalViolation(9),\n         securityServiceOrMechanismViloation (10),\n         timeDomainViolation (11)')
alarmCause = MibTableColumn((1, 3, 6, 1, 4, 1, 30826, 1, 1, 2, 1, 1, 13), AlarmProbableCause()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmCause.setStatus('current')
if mibBuilder.loadTexts: alarmCause.setDescription('The alarm probable cause as defined in ITU-T X.733.\n        undefined (0)\n        adapterError (1)                       -- Equipment\n        applicationSubsystemFailure (2)        -- Processing\n        bandwidthReduced (3)                   -- Quality of service\n        callEstablishmentError (4)             -- Communications\n        communicationsProtocolError (5)        -- Communications\n        communicationsSubsystemFailure (6)     -- Communications\n        configurationOrCustomizationError (7)  -- Processing\n        congestion (8)                         -- Quality of service\n        corruptData (9)                        -- Processing\n        cpuCyclesLimitExceeded (10)            -- Processing\n        dTEdCEInterfaceError (11)              -- Communications\n        datasetOrModemError (12)               -- Equipment\n        degradedSignal (13)                    -- Communications\n        enclosureDoorOpen (14)                 -- Environmental\n        equipmentMalfunction (15)              -- Equipment\n        excessiveVibration (16)                -- Environmental\n        fileError (17)                         -- Processing\n        fireDetected (18)                      -- Environmental\n        floodDetected (19)                     -- Environmental\n        framingError (20)                      -- Communications\n        heatingOrVentilationOrCoolingSystemProblem (21) -- Environmental\n        humidityUnacceptable (22)              -- Environmental\n        inputDeviceError (23)                  -- Equipment\n        inputOutputDeviceError (24)            -- Equipment\n        lANError (25)                          -- Communications\n        leakDetected (26)                      -- Environmental\n        localNodeTransmissionError (27)        -- Communications\n        lossOfFrame (28)                       -- Communications\n        lossOfSignal (29)                      -- Communications\n        materialSupplyExhausted (30)           -- Environmental\n        multiplexerProblem (31)                -- Equipment\n        outOfMemory (32)                       -- Processing\n        outputDeviceError (33)                 -- Equipment\n        performanceDegraded (34)               -- Quality of service\n        powerProblem (35)                      -- Equipment\n        pressureUnacceptable (36)              -- Environmental\n        processorProblem (37)                  -- Equipment\n        pumpFailure (38)                       -- Environmental\n        queueSizeExceeded (39)                 -- Quality of service\n        receiveFailure (40)                    -- Equipment\n        receiverFailure (41)                   -- Equipment\n        remoteNodeTransmissionError (42)       -- Communications\n        resourceAtOrNearingCapacity (43)       -- Quality of service\n        responseTimeExcessive (44)             -- Quality of service\n        retransmissionRateExcessive (45)       -- Quality of service\n        softwareProgramError (46)              -- Processing\n        softwareError (47)                     -- Processing\n        softwareProgramAbnormallyTerminated (48) -- Processing\n        storageCapacityProblem (49)            -- Processing\n        temperatureUnacceptable (50)           -- Environmental\n        thresholdCrossed (51)                  -- Quality of service\n        timingProblem (52)                     -- Equipment\n        toxicLeakDetected (53)                 -- Environmental\n        transmitFailure (54)                   -- Equipment\n        transmitterFailure (55)                -- Equipment\n        underlyingResourceUnavailable (56)     -- Processing\n        versionMismatch (57)                   -- Processing')
alarmPortAlias = MibTableColumn((1, 3, 6, 1, 4, 1, 30826, 1, 1, 2, 1, 1, 14), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmPortAlias.setStatus('current')
if mibBuilder.loadTexts: alarmPortAlias.setDescription('The Port Alias.')
alarmLogTable = MibTable((1, 3, 6, 1, 4, 1, 30826, 1, 1, 3, 1), )
if mibBuilder.loadTexts: alarmLogTable.setStatus('current')
if mibBuilder.loadTexts: alarmLogTable.setDescription('The active alarm list.')
alarmLogEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30826, 1, 1, 3, 1, 1), ).setIndexNames((0, "MSERIES-ALARM-MIB", "alarmLogIndex"))
if mibBuilder.loadTexts: alarmLogEntry.setStatus('current')
if mibBuilder.loadTexts: alarmLogEntry.setDescription('An entry in the alarm log table.')
alarmLogIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 30826, 1, 1, 3, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmLogIndex.setStatus('current')
if mibBuilder.loadTexts: alarmLogIndex.setDescription('An unique index assigned to each alarm.')
alarmLogUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 30826, 1, 1, 3, 1, 1, 2), UnitType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmLogUnit.setStatus('current')
if mibBuilder.loadTexts: alarmLogUnit.setDescription('The alarming unit associated with this alarm.\n        undefined(0), nmb(1), psu1(2), psu2(3), fan(4), system&#40;5&#41;,\n        slaveNmb(6), slavePsu1(7), slavePsu2(8), slaveFan(9).')
alarmLogPort = MibTableColumn((1, 3, 6, 1, 4, 1, 30826, 1, 1, 3, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmLogPort.setStatus('current')
if mibBuilder.loadTexts: alarmLogPort.setDescription('The alarming port associated with this alarm.\n        1-10 is Line Ports. 11 and higher is Client ports. For non port alarms this value is 0.')
alarmLogText = MibTableColumn((1, 3, 6, 1, 4, 1, 30826, 1, 1, 3, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmLogText.setStatus('current')
if mibBuilder.loadTexts: alarmLogText.setDescription('The additional text for the alarm.')
alarmLogSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 30826, 1, 1, 3, 1, 1, 5), AlarmPerceivedSeverity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmLogSeverity.setStatus('current')
if mibBuilder.loadTexts: alarmLogSeverity.setDescription('The severity of the alarm as defined in\n        ITU-T X.733.')
alarmLogActivationTime = MibTableColumn((1, 3, 6, 1, 4, 1, 30826, 1, 1, 3, 1, 1, 6), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmLogActivationTime.setStatus('current')
if mibBuilder.loadTexts: alarmLogActivationTime.setDescription('The time when the alarm was created.')
alarmLogCeaseTime = MibTableColumn((1, 3, 6, 1, 4, 1, 30826, 1, 1, 3, 1, 1, 7), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmLogCeaseTime.setStatus('current')
if mibBuilder.loadTexts: alarmLogCeaseTime.setDescription('The time when the alarm was ceased.')
alarmLogSeqNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 30826, 1, 1, 3, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmLogSeqNumber.setStatus('current')
if mibBuilder.loadTexts: alarmLogSeqNumber.setDescription('The last sequence number used when issuing\n        a notification for this alarm.')
alarmLogHostName = MibTableColumn((1, 3, 6, 1, 4, 1, 30826, 1, 1, 3, 1, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmLogHostName.setStatus('current')
if mibBuilder.loadTexts: alarmLogHostName.setDescription('The hostname.')
alarmLogPortName = MibTableColumn((1, 3, 6, 1, 4, 1, 30826, 1, 1, 3, 1, 1, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmLogPortName.setStatus('current')
if mibBuilder.loadTexts: alarmLogPortName.setDescription('The Port Name.')
alarmLogPortType = MibTableColumn((1, 3, 6, 1, 4, 1, 30826, 1, 1, 3, 1, 1, 11), PortType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmLogPortType.setStatus('current')
if mibBuilder.loadTexts: alarmLogPortType.setDescription('The Port Direction. rx(1), tx(2), biDi(3).')
alarmLogType = MibTableColumn((1, 3, 6, 1, 4, 1, 30826, 1, 1, 3, 1, 1, 12), AlarmNotificationType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmLogType.setStatus('current')
if mibBuilder.loadTexts: alarmLogType.setDescription('The type of alarm as defined in ITU-T X.733\n         undefined (0),\n         other (1),\n         communicationsAlarm (2),\n         qualityOfServiceAlarm (3),\n         processingErrorAlarm (4),\n         equipmentAlarm (5),\n         environmental (6),\n         integrityViolation (7),\n         operationalViolation (8),\n         physicalViolation(9),\n         securityServiceOrMechanismViloation (10),\n         timeDomainViolation (11)')
alarmLogCause = MibTableColumn((1, 3, 6, 1, 4, 1, 30826, 1, 1, 3, 1, 1, 13), AlarmProbableCause()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmLogCause.setStatus('current')
if mibBuilder.loadTexts: alarmLogCause.setDescription('The alarm probable cause as defined in ITU-T X.733.\n        undefined (0)\n        adapterError (1)                       -- Equipment\n        applicationSubsystemFailure (2)        -- Processing\n        bandwidthReduced (3)                   -- Quality of service\n        callEstablishmentError (4)             -- Communications\n        communicationsProtocolError (5)        -- Communications\n        communicationsSubsystemFailure (6)     -- Communications\n        configurationOrCustomizationError (7)  -- Processing\n        congestion (8)                         -- Quality of service\n        corruptData (9)                        -- Processing\n        cpuCyclesLimitExceeded (10)            -- Processing\n        dTEdCEInterfaceError (11)              -- Communications\n        datasetOrModemError (12)               -- Equipment\n        degradedSignal (13)                    -- Communications\n        enclosureDoorOpen (14)                 -- Environmental\n        equipmentMalfunction (15)              -- Equipment\n        excessiveVibration (16)                -- Environmental\n        fileError (17)                         -- Processing\n        fireDetected (18)                      -- Environmental\n        floodDetected (19)                     -- Environmental\n        framingError (20)                      -- Communications\n        heatingOrVentilationOrCoolingSystemProblem (21) -- Environmental\n        humidityUnacceptable (22)              -- Environmental\n        inputDeviceError (23)                  -- Equipment\n        inputOutputDeviceError (24)            -- Equipment\n        lANError (25)                          -- Communications\n        leakDetected (26)                      -- Environmental\n        localNodeTransmissionError (27)        -- Communications\n        lossOfFrame (28)                       -- Communications\n        lossOfSignal (29)                      -- Communications\n        materialSupplyExhausted (30)           -- Environmental\n        multiplexerProblem (31)                -- Equipment\n        outOfMemory (32)                       -- Processing\n        outputDeviceError (33)                 -- Equipment\n        performanceDegraded (34)               -- Quality of service\n        powerProblem (35)                      -- Equipment\n        pressureUnacceptable (36)              -- Environmental\n        processorProblem (37)                  -- Equipment\n        pumpFailure (38)                       -- Environmental\n        queueSizeExceeded (39)                 -- Quality of service\n        receiveFailure (40)                    -- Equipment\n        receiverFailure (41)                   -- Equipment\n        remoteNodeTransmissionError (42)       -- Communications\n        resourceAtOrNearingCapacity (43)       -- Quality of service\n        responseTimeExcessive (44)             -- Quality of service\n        retransmissionRateExcessive (45)       -- Quality of service\n        softwareProgramError (46)              -- Processing\n        softwareError (47)                     -- Processing\n        softwareProgramAbnormallyTerminated (48) -- Processing\n        storageCapacityProblem (49)            -- Processing\n        temperatureUnacceptable (50)           -- Environmental\n        thresholdCrossed (51)                  -- Quality of service\n        timingProblem (52)                     -- Equipment\n        toxicLeakDetected (53)                 -- Environmental\n        transmitFailure (54)                   -- Equipment\n        transmitterFailure (55)                -- Equipment\n        underlyingResourceUnavailable (56)     -- Processing\n        versionMismatch (57)                   -- Processing')
alarmNotifyPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 30826, 1, 1, 4, 0))
alarmNotificationCleared = NotificationType((1, 3, 6, 1, 4, 1, 30826, 1, 1, 4, 0, 1)).setObjects(("MSERIES-ALARM-MIB", "alarmIndex"), ("MSERIES-ALARM-MIB", "alarmUnit"), ("MSERIES-ALARM-MIB", "alarmPort"), ("MSERIES-ALARM-MIB", "alarmText"), ("MSERIES-ALARM-MIB", "alarmSeverity"), ("MSERIES-ALARM-MIB", "alarmActivationTime"), ("MSERIES-ALARM-MIB", "alarmCeaseTime"), ("MSERIES-ALARM-MIB", "alarmSeqNumber"), ("MSERIES-ALARM-MIB", "alarmHostName"), ("MSERIES-ALARM-MIB", "alarmPortName"), ("MSERIES-ALARM-MIB", "alarmPortType"), ("MSERIES-ALARM-MIB", "alarmPortAlias"))
if mibBuilder.loadTexts: alarmNotificationCleared.setStatus('current')
if mibBuilder.loadTexts: alarmNotificationCleared.setDescription('Sent when an alarm is cleared.')
alarmNotificationWarning = NotificationType((1, 3, 6, 1, 4, 1, 30826, 1, 1, 4, 0, 2)).setObjects(("MSERIES-ALARM-MIB", "alarmIndex"), ("MSERIES-ALARM-MIB", "alarmUnit"), ("MSERIES-ALARM-MIB", "alarmPort"), ("MSERIES-ALARM-MIB", "alarmText"), ("MSERIES-ALARM-MIB", "alarmSeverity"), ("MSERIES-ALARM-MIB", "alarmActivationTime"), ("MSERIES-ALARM-MIB", "alarmCeaseTime"), ("MSERIES-ALARM-MIB", "alarmSeqNumber"), ("MSERIES-ALARM-MIB", "alarmHostName"), ("MSERIES-ALARM-MIB", "alarmPortName"), ("MSERIES-ALARM-MIB", "alarmPortType"), ("MSERIES-ALARM-MIB", "alarmPortAlias"))
if mibBuilder.loadTexts: alarmNotificationWarning.setStatus('current')
if mibBuilder.loadTexts: alarmNotificationWarning.setDescription('Sent when an alarm with warning severity is activated.')
alarmNotificationMinor = NotificationType((1, 3, 6, 1, 4, 1, 30826, 1, 1, 4, 0, 3)).setObjects(("MSERIES-ALARM-MIB", "alarmIndex"), ("MSERIES-ALARM-MIB", "alarmUnit"), ("MSERIES-ALARM-MIB", "alarmPort"), ("MSERIES-ALARM-MIB", "alarmText"), ("MSERIES-ALARM-MIB", "alarmSeverity"), ("MSERIES-ALARM-MIB", "alarmActivationTime"), ("MSERIES-ALARM-MIB", "alarmCeaseTime"), ("MSERIES-ALARM-MIB", "alarmSeqNumber"), ("MSERIES-ALARM-MIB", "alarmHostName"), ("MSERIES-ALARM-MIB", "alarmPortName"), ("MSERIES-ALARM-MIB", "alarmPortType"), ("MSERIES-ALARM-MIB", "alarmPortAlias"))
if mibBuilder.loadTexts: alarmNotificationMinor.setStatus('current')
if mibBuilder.loadTexts: alarmNotificationMinor.setDescription('Sent when an alarm with minor severity is activated.')
alarmNotificationMajor = NotificationType((1, 3, 6, 1, 4, 1, 30826, 1, 1, 4, 0, 4)).setObjects(("MSERIES-ALARM-MIB", "alarmIndex"), ("MSERIES-ALARM-MIB", "alarmUnit"), ("MSERIES-ALARM-MIB", "alarmPort"), ("MSERIES-ALARM-MIB", "alarmText"), ("MSERIES-ALARM-MIB", "alarmSeverity"), ("MSERIES-ALARM-MIB", "alarmActivationTime"), ("MSERIES-ALARM-MIB", "alarmCeaseTime"), ("MSERIES-ALARM-MIB", "alarmSeqNumber"), ("MSERIES-ALARM-MIB", "alarmHostName"), ("MSERIES-ALARM-MIB", "alarmPortName"), ("MSERIES-ALARM-MIB", "alarmPortType"), ("MSERIES-ALARM-MIB", "alarmPortAlias"))
if mibBuilder.loadTexts: alarmNotificationMajor.setStatus('current')
if mibBuilder.loadTexts: alarmNotificationMajor.setDescription('Sent when an alarm with major severity is activated..')
alarmNotificationCritical = NotificationType((1, 3, 6, 1, 4, 1, 30826, 1, 1, 4, 0, 5)).setObjects(("MSERIES-ALARM-MIB", "alarmIndex"), ("MSERIES-ALARM-MIB", "alarmUnit"), ("MSERIES-ALARM-MIB", "alarmPort"), ("MSERIES-ALARM-MIB", "alarmText"), ("MSERIES-ALARM-MIB", "alarmSeverity"), ("MSERIES-ALARM-MIB", "alarmActivationTime"), ("MSERIES-ALARM-MIB", "alarmCeaseTime"), ("MSERIES-ALARM-MIB", "alarmSeqNumber"), ("MSERIES-ALARM-MIB", "alarmHostName"), ("MSERIES-ALARM-MIB", "alarmPortName"), ("MSERIES-ALARM-MIB", "alarmPortType"), ("MSERIES-ALARM-MIB", "alarmPortAlias"))
if mibBuilder.loadTexts: alarmNotificationCritical.setStatus('current')
if mibBuilder.loadTexts: alarmNotificationCritical.setDescription('Sent when an alarm with critical severity is activated.')
smartAlarmGeneralGroupV1 = ObjectGroup((1, 3, 6, 1, 4, 1, 30826, 1, 1, 5, 1, 1)).setObjects(("MSERIES-ALARM-MIB", "smartAlarmGeneralLastSeqNumber"), ("MSERIES-ALARM-MIB", "smartAlarmGeneralHighestSeverity"), ("MSERIES-ALARM-MIB", "smartAlarmGeneralNumberActiveList"), ("MSERIES-ALARM-MIB", "smartAlarmGeneralNumberLogList"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    smartAlarmGeneralGroupV1 = smartAlarmGeneralGroupV1.setStatus('current')
if mibBuilder.loadTexts: smartAlarmGeneralGroupV1.setDescription('The general alarm objects V1.')
smartAlarmNotificationGroupV1 = NotificationGroup((1, 3, 6, 1, 4, 1, 30826, 1, 1, 5, 1, 2)).setObjects(("MSERIES-ALARM-MIB", "alarmNotificationCleared"), ("MSERIES-ALARM-MIB", "alarmNotificationCritical"), ("MSERIES-ALARM-MIB", "alarmNotificationMajor"), ("MSERIES-ALARM-MIB", "alarmNotificationMinor"), ("MSERIES-ALARM-MIB", "alarmNotificationWarning"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    smartAlarmNotificationGroupV1 = smartAlarmNotificationGroupV1.setStatus('current')
if mibBuilder.loadTexts: smartAlarmNotificationGroupV1.setDescription('The alarm notifications V1.')
smartAlarmActiveTableGroupV1 = ObjectGroup((1, 3, 6, 1, 4, 1, 30826, 1, 1, 5, 1, 3)).setObjects(("MSERIES-ALARM-MIB", "alarmIndex"), ("MSERIES-ALARM-MIB", "alarmUnit"), ("MSERIES-ALARM-MIB", "alarmPort"), ("MSERIES-ALARM-MIB", "alarmText"), ("MSERIES-ALARM-MIB", "alarmSeverity"), ("MSERIES-ALARM-MIB", "alarmActivationTime"), ("MSERIES-ALARM-MIB", "alarmCeaseTime"), ("MSERIES-ALARM-MIB", "alarmSeqNumber"), ("MSERIES-ALARM-MIB", "alarmHostName"), ("MSERIES-ALARM-MIB", "alarmPortName"), ("MSERIES-ALARM-MIB", "alarmPortType"), ("MSERIES-ALARM-MIB", "alarmType"), ("MSERIES-ALARM-MIB", "alarmCause"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    smartAlarmActiveTableGroupV1 = smartAlarmActiveTableGroupV1.setStatus('current')
if mibBuilder.loadTexts: smartAlarmActiveTableGroupV1.setDescription('The active alarm table objects V1.')
smartAlarmLogTableGroupV1 = ObjectGroup((1, 3, 6, 1, 4, 1, 30826, 1, 1, 5, 1, 4)).setObjects(("MSERIES-ALARM-MIB", "alarmLogIndex"), ("MSERIES-ALARM-MIB", "alarmLogUnit"), ("MSERIES-ALARM-MIB", "alarmLogPort"), ("MSERIES-ALARM-MIB", "alarmLogText"), ("MSERIES-ALARM-MIB", "alarmLogSeverity"), ("MSERIES-ALARM-MIB", "alarmLogActivationTime"), ("MSERIES-ALARM-MIB", "alarmLogCeaseTime"), ("MSERIES-ALARM-MIB", "alarmLogSeqNumber"), ("MSERIES-ALARM-MIB", "alarmLogHostName"), ("MSERIES-ALARM-MIB", "alarmLogPortName"), ("MSERIES-ALARM-MIB", "alarmLogPortType"), ("MSERIES-ALARM-MIB", "alarmLogType"), ("MSERIES-ALARM-MIB", "alarmLogCause"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    smartAlarmLogTableGroupV1 = smartAlarmLogTableGroupV1.setStatus('current')
if mibBuilder.loadTexts: smartAlarmLogTableGroupV1.setDescription('The alarm log table objects V1.')
smartAlarmBasicComplV1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 30826, 1, 1, 5, 2, 1)).setObjects(("MSERIES-ALARM-MIB", "smartAlarmGeneralGroupV1"), ("MSERIES-ALARM-MIB", "smartAlarmNotificationGroupV1"), ("MSERIES-ALARM-MIB", "smartAlarmActiveTableGroupV1"), ("MSERIES-ALARM-MIB", "smartAlarmLogTableGroupV1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    smartAlarmBasicComplV1 = smartAlarmBasicComplV1.setStatus('current')
if mibBuilder.loadTexts: smartAlarmBasicComplV1.setDescription('Basic implementation requirements for the alarm MIB V1.')
mibBuilder.exportSymbols("MSERIES-ALARM-MIB", smartAlarmGeneralNumberLogList=smartAlarmGeneralNumberLogList, alarmLogUnit=alarmLogUnit, alarmSeqNumber=alarmSeqNumber, alarmLogCeaseTime=alarmLogCeaseTime, alarmActiveTable=alarmActiveTable, alarmLogPort=alarmLogPort, alarmCause=alarmCause, smartAlarmGeneralHighestSeverity=smartAlarmGeneralHighestSeverity, alarmGeneral=alarmGeneral, alarmLogPortName=alarmLogPortName, alarmPortName=alarmPortName, alarmNotificationWarning=alarmNotificationWarning, alarmNotificationCritical=alarmNotificationCritical, smartAlarmGroups=smartAlarmGroups, smartAlarmCompliances=smartAlarmCompliances, alarmSeverity=alarmSeverity, smartAlarmNotificationGroupV1=smartAlarmNotificationGroupV1, alarmCeaseTime=alarmCeaseTime, alarmNotifyPrefix=alarmNotifyPrefix, alarmLogSeverity=alarmLogSeverity, alarmNotificationMinor=alarmNotificationMinor, alarmLogText=alarmLogText, PYSNMP_MODULE_ID=smartAlarm, alarmLogTable=alarmLogTable, alarmIndex=alarmIndex, alarmLogActivationTime=alarmLogActivationTime, alarmUnit=alarmUnit, alarmPortAlias=alarmPortAlias, alarmText=alarmText, smartAlarmLogTableGroupV1=smartAlarmLogTableGroupV1, smartAlarm=smartAlarm, smartAlarmGeneralLastSeqNumber=smartAlarmGeneralLastSeqNumber, alarmNotificationCleared=alarmNotificationCleared, alarmNotifications=alarmNotifications, alarmEntry=alarmEntry, alarmLogEntry=alarmLogEntry, alarmType=alarmType, smartAlarmMIBConformance=smartAlarmMIBConformance, alarmPort=alarmPort, alarmLogSeqNumber=alarmLogSeqNumber, alarmLogHostName=alarmLogHostName, alarmLogIndex=alarmLogIndex, alarmPortType=alarmPortType, alarmLogPortType=alarmLogPortType, alarmLogCause=alarmLogCause, smartAlarmBasicComplV1=smartAlarmBasicComplV1, alarmHostName=alarmHostName, smartAlarmGeneralNumberActiveList=smartAlarmGeneralNumberActiveList, smartAlarmActiveTableGroupV1=smartAlarmActiveTableGroupV1, smartAlarmGeneralGroupV1=smartAlarmGeneralGroupV1, alarmLogType=alarmLogType, alarmActivationTime=alarmActivationTime, alarmNotificationMajor=alarmNotificationMajor, alarmLogList=alarmLogList, alarmActiveList=alarmActiveList)
