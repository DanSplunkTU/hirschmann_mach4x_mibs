#
# PySNMP MIB module PACKETLOGIC-TRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/procera/PACKETLOGIC-TRAP-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:35:03 2022
# On host fv-az36-988 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
CounterBasedGauge64, = mibBuilder.importSymbols("HCNUM-TC", "CounterBasedGauge64")
packetlogic2, = mibBuilder.importSymbols("PACKETLOGIC-MIB", "packetlogic2")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, MibIdentifier, Integer32, Bits, ObjectIdentity, TimeTicks, IpAddress, Gauge32, NotificationType, ModuleIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "MibIdentifier", "Integer32", "Bits", "ObjectIdentity", "TimeTicks", "IpAddress", "Gauge32", "NotificationType", "ModuleIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Counter32")
DateAndTime, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "TextualConvention", "DisplayString")
pl2Trap = ModuleIdentity((1, 3, 6, 1, 4, 1, 15397, 2, 8))
pl2Trap.setRevisions(('2019-09-12 15:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: pl2Trap.setRevisionsDescriptions((' Latest version at the revision date for version GET VERSION HERE',))
if mibBuilder.loadTexts: pl2Trap.setLastUpdated('201909121500Z')
if mibBuilder.loadTexts: pl2Trap.setOrganization('Procera Networks, Inc.')
if mibBuilder.loadTexts: pl2Trap.setContactInfo('support@proceranetworks.com')
if mibBuilder.loadTexts: pl2Trap.setDescription('MIB for PacketLogic2 traps')
pl2Traps = MibIdentifier((1, 3, 6, 1, 4, 1, 15397, 2, 8, 0))
pl2TrapVals = MibIdentifier((1, 3, 6, 1, 4, 1, 15397, 2, 8, 1))
pl2ChannelTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 15397, 2, 8, 2))
pl2ChannelTrapVals = MibIdentifier((1, 3, 6, 1, 4, 1, 15397, 2, 8, 3))
pl2StorageTrapVals = MibIdentifier((1, 3, 6, 1, 4, 1, 15397, 2, 8, 4))
pl2ContentLogicTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 15397, 2, 8, 5))
pl2ContentLogicHourlyUpdateTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 15397, 2, 8, 5, 1))
pl2ContentLogicCategoriesLoadingTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 15397, 2, 8, 5, 2))
pl2ContentLogicDatabaseUpdateTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 15397, 2, 8, 5, 3))
pl2ContentLogicDatabaseLoadingTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 15397, 2, 8, 5, 4))
pl2ContentLogicTrapVals = MibIdentifier((1, 3, 6, 1, 4, 1, 15397, 2, 8, 6))
pl2TrapMessage = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 8, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pl2TrapMessage.setStatus('current')
if mibBuilder.loadTexts: pl2TrapMessage.setDescription('Message describing trap.')
pl2TrapOid = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 8, 1, 2), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pl2TrapOid.setStatus('current')
if mibBuilder.loadTexts: pl2TrapOid.setDescription('OID Causing trap.')
pl2TrapValue = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 8, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pl2TrapValue.setStatus('current')
if mibBuilder.loadTexts: pl2TrapValue.setDescription('Current value of item causing trap.')
pl2TrapThreshold = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 8, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pl2TrapThreshold.setStatus('current')
if mibBuilder.loadTexts: pl2TrapThreshold.setDescription('Threshold of item causing trap.')
pl2TrapValue64 = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 8, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pl2TrapValue64.setStatus('current')
if mibBuilder.loadTexts: pl2TrapValue64.setDescription('Current value of item causing trap.')
pl2TrapThreshold64 = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 8, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pl2TrapThreshold64.setStatus('current')
if mibBuilder.loadTexts: pl2TrapThreshold64.setDescription('Threshold of item causing trap.')
channelIndex = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 8, 3, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelIndex.setStatus('current')
if mibBuilder.loadTexts: channelIndex.setDescription('Index of the channel.')
channelDescr = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 8, 3, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelDescr.setStatus('current')
if mibBuilder.loadTexts: channelDescr.setDescription('A description of the channel.')
channelPort = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 8, 3, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("external", 0), ("internal", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelPort.setStatus('current')
if mibBuilder.loadTexts: channelPort.setDescription('The port of the channel.')
prevState = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 8, 3, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("auto", 0), ("hd-10", 1), ("fd-10", 2), ("hd-100", 3), ("fd-100", 4), ("fd-1000", 5), ("fd-10000", 6), ("fd-40000", 7), ("fd-100000", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: prevState.setStatus('current')
if mibBuilder.loadTexts: prevState.setDescription('This is the state the channel was in before it changed.')
newState = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 8, 3, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("auto", 0), ("hd-10", 1), ("fd-10", 2), ("hd-100", 3), ("fd-100", 4), ("fd-1000", 5), ("fd-10000", 6), ("fd-40000", 7), ("fd-100000", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: newState.setStatus('current')
if mibBuilder.loadTexts: newState.setDescription('This is the new state of the channel.')
pl2ContentLogicDatabase = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 8, 6, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pl2ContentLogicDatabase.setStatus('current')
if mibBuilder.loadTexts: pl2ContentLogicDatabase.setDescription('Name of the database.')
pl2ContentLogicReason = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 8, 6, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pl2ContentLogicReason.setStatus('current')
if mibBuilder.loadTexts: pl2ContentLogicReason.setDescription('Reason for the failed event.')
pl2TrapGenericMsg = NotificationType((1, 3, 6, 1, 4, 1, 15397, 2, 8, 0, 1)).setObjects(("PACKETLOGIC-TRAP-MIB", "pl2TrapMessage"))
if mibBuilder.loadTexts: pl2TrapGenericMsg.setStatus('current')
if mibBuilder.loadTexts: pl2TrapGenericMsg.setDescription('Used for generic or undefined alerts. A message briefly explains the alert.')
pl2TrapGeneric = NotificationType((1, 3, 6, 1, 4, 1, 15397, 2, 8, 0, 2))
if mibBuilder.loadTexts: pl2TrapGeneric.setStatus('current')
if mibBuilder.loadTexts: pl2TrapGeneric.setDescription('Used for generic or undefined alerts without message. Should be avoided.')
pl2TrapSystemStatsAlert = NotificationType((1, 3, 6, 1, 4, 1, 15397, 2, 8, 0, 3)).setObjects(("PACKETLOGIC-TRAP-MIB", "pl2TrapThreshold"), ("PACKETLOGIC-TRAP-MIB", "pl2TrapMessage"), ("PACKETLOGIC-TRAP-MIB", "pl2TrapValue"), ("PACKETLOGIC-TRAP-MIB", "pl2TrapOid"))
if mibBuilder.loadTexts: pl2TrapSystemStatsAlert.setStatus('current')
if mibBuilder.loadTexts: pl2TrapSystemStatsAlert.setDescription('An Alert Threshold defined in SystemStats (System Diagnostics) was reached. This trap is used for items with 32 bit values.')
pl2TrapSystemStatsAlert64 = NotificationType((1, 3, 6, 1, 4, 1, 15397, 2, 8, 0, 4)).setObjects(("PACKETLOGIC-TRAP-MIB", "pl2TrapThreshold64"), ("PACKETLOGIC-TRAP-MIB", "pl2TrapMessage"), ("PACKETLOGIC-TRAP-MIB", "pl2TrapValue64"), ("PACKETLOGIC-TRAP-MIB", "pl2TrapOid"))
if mibBuilder.loadTexts: pl2TrapSystemStatsAlert64.setStatus('current')
if mibBuilder.loadTexts: pl2TrapSystemStatsAlert64.setDescription('An Alert Threshold defined in SystemStats (System Diagnostics) was reached. This trap is used for items with 64 bit values.')
pl2TrapSystemStatsAlertClear = NotificationType((1, 3, 6, 1, 4, 1, 15397, 2, 8, 0, 5)).setObjects(("PACKETLOGIC-TRAP-MIB", "pl2TrapOid"))
if mibBuilder.loadTexts: pl2TrapSystemStatsAlertClear.setStatus('current')
if mibBuilder.loadTexts: pl2TrapSystemStatsAlertClear.setDescription('An Alert Threshold defined in SystemStats (System Diagnostics) is now clear.')
pl2ChannelStateChanged = NotificationType((1, 3, 6, 1, 4, 1, 15397, 2, 8, 2, 1)).setObjects(("PACKETLOGIC-TRAP-MIB", "channelIndex"), ("PACKETLOGIC-TRAP-MIB", "channelDescr"), ("PACKETLOGIC-TRAP-MIB", "channelPort"), ("PACKETLOGIC-TRAP-MIB", "newState"), ("PACKETLOGIC-TRAP-MIB", "prevState"))
if mibBuilder.loadTexts: pl2ChannelStateChanged.setStatus('current')
if mibBuilder.loadTexts: pl2ChannelStateChanged.setDescription('Channel state changed')
pl2StorageGenericTrap = NotificationType((1, 3, 6, 1, 4, 1, 15397, 2, 8, 4, 1)).setObjects(("PACKETLOGIC-TRAP-MIB", "pl2TrapMessage"))
if mibBuilder.loadTexts: pl2StorageGenericTrap.setStatus('current')
if mibBuilder.loadTexts: pl2StorageGenericTrap.setDescription('Generic or undefined alerts from the storage devices.')
pl2StorageBattery = NotificationType((1, 3, 6, 1, 4, 1, 15397, 2, 8, 4, 2)).setObjects(("PACKETLOGIC-TRAP-MIB", "pl2TrapMessage"))
if mibBuilder.loadTexts: pl2StorageBattery.setStatus('current')
if mibBuilder.loadTexts: pl2StorageBattery.setDescription('Alerts regarding batteries in storage devices.')
pl2StoragePowerSupply = NotificationType((1, 3, 6, 1, 4, 1, 15397, 2, 8, 4, 3)).setObjects(("PACKETLOGIC-TRAP-MIB", "pl2TrapMessage"))
if mibBuilder.loadTexts: pl2StoragePowerSupply.setStatus('current')
if mibBuilder.loadTexts: pl2StoragePowerSupply.setDescription('Alerts for power supplies in storage devices.')
pl2StoragePhysicalDisk = NotificationType((1, 3, 6, 1, 4, 1, 15397, 2, 8, 4, 4)).setObjects(("PACKETLOGIC-TRAP-MIB", "pl2TrapMessage"))
if mibBuilder.loadTexts: pl2StoragePhysicalDisk.setStatus('current')
if mibBuilder.loadTexts: pl2StoragePhysicalDisk.setDescription('Alerts for physical disks in storage devices.')
pl2StorageVirtualDisk = NotificationType((1, 3, 6, 1, 4, 1, 15397, 2, 8, 4, 5)).setObjects(("PACKETLOGIC-TRAP-MIB", "pl2TrapMessage"))
if mibBuilder.loadTexts: pl2StorageVirtualDisk.setStatus('current')
if mibBuilder.loadTexts: pl2StorageVirtualDisk.setDescription('Alerts for virtual disks in storage devices.')
pl2ContentLogicHourlyUpdateStarted = NotificationType((1, 3, 6, 1, 4, 1, 15397, 2, 8, 5, 1, 1))
if mibBuilder.loadTexts: pl2ContentLogicHourlyUpdateStarted.setStatus('current')
if mibBuilder.loadTexts: pl2ContentLogicHourlyUpdateStarted.setDescription('A trap for notifying that ContentLogic has started an hourly update.')
pl2ContentLogicHourlyUpdateCompleted = NotificationType((1, 3, 6, 1, 4, 1, 15397, 2, 8, 5, 1, 2))
if mibBuilder.loadTexts: pl2ContentLogicHourlyUpdateCompleted.setStatus('current')
if mibBuilder.loadTexts: pl2ContentLogicHourlyUpdateCompleted.setDescription('A trap for notifying that ContentLogic has completed an hourly update.')
pl2ContentLogicHourlyUpdateFailed = NotificationType((1, 3, 6, 1, 4, 1, 15397, 2, 8, 5, 1, 3)).setObjects(("PACKETLOGIC-TRAP-MIB", "pl2ContentLogicReason"))
if mibBuilder.loadTexts: pl2ContentLogicHourlyUpdateFailed.setStatus('current')
if mibBuilder.loadTexts: pl2ContentLogicHourlyUpdateFailed.setDescription('A trap for notifying that ContentLogic has failed an hourly update.')
pl2ContentLogicCategoriesLoadingStarted = NotificationType((1, 3, 6, 1, 4, 1, 15397, 2, 8, 5, 2, 1)).setObjects(("PACKETLOGIC-TRAP-MIB", "pl2ContentLogicDatabase"))
if mibBuilder.loadTexts: pl2ContentLogicCategoriesLoadingStarted.setStatus('current')
if mibBuilder.loadTexts: pl2ContentLogicCategoriesLoadingStarted.setDescription('A trap for notifying that ContentLogic has started to load categories.')
pl2ContentLogicCategoriesLoadingCompleted = NotificationType((1, 3, 6, 1, 4, 1, 15397, 2, 8, 5, 2, 2)).setObjects(("PACKETLOGIC-TRAP-MIB", "pl2ContentLogicDatabase"))
if mibBuilder.loadTexts: pl2ContentLogicCategoriesLoadingCompleted.setStatus('current')
if mibBuilder.loadTexts: pl2ContentLogicCategoriesLoadingCompleted.setDescription('A trap for notifying that ContentLogic has completed loading categories.')
pl2ContentLogicCategoriesLoadingFailed = NotificationType((1, 3, 6, 1, 4, 1, 15397, 2, 8, 5, 2, 3)).setObjects(("PACKETLOGIC-TRAP-MIB", "pl2ContentLogicDatabase"), ("PACKETLOGIC-TRAP-MIB", "pl2ContentLogicReason"))
if mibBuilder.loadTexts: pl2ContentLogicCategoriesLoadingFailed.setStatus('current')
if mibBuilder.loadTexts: pl2ContentLogicCategoriesLoadingFailed.setDescription('A trap for notifying that ContentLogic has failed to load categories.')
pl2ContentLogicDatabaseUpdateStarted = NotificationType((1, 3, 6, 1, 4, 1, 15397, 2, 8, 5, 3, 1)).setObjects(("PACKETLOGIC-TRAP-MIB", "pl2ContentLogicDatabase"))
if mibBuilder.loadTexts: pl2ContentLogicDatabaseUpdateStarted.setStatus('current')
if mibBuilder.loadTexts: pl2ContentLogicDatabaseUpdateStarted.setDescription('A trap for notifying that ContentLogic has started to update a database.')
pl2ContentLogicDatabaseUpdateCompleted = NotificationType((1, 3, 6, 1, 4, 1, 15397, 2, 8, 5, 3, 2)).setObjects(("PACKETLOGIC-TRAP-MIB", "pl2ContentLogicDatabase"))
if mibBuilder.loadTexts: pl2ContentLogicDatabaseUpdateCompleted.setStatus('current')
if mibBuilder.loadTexts: pl2ContentLogicDatabaseUpdateCompleted.setDescription('A trap for notifying that ContentLogic has completed updating a database.')
pl2ContentLogicDatabaseUpdateFailed = NotificationType((1, 3, 6, 1, 4, 1, 15397, 2, 8, 5, 3, 3)).setObjects(("PACKETLOGIC-TRAP-MIB", "pl2ContentLogicDatabase"), ("PACKETLOGIC-TRAP-MIB", "pl2ContentLogicReason"))
if mibBuilder.loadTexts: pl2ContentLogicDatabaseUpdateFailed.setStatus('current')
if mibBuilder.loadTexts: pl2ContentLogicDatabaseUpdateFailed.setDescription('A trap for notifying that ContentLogic has failed to update a database.')
pl2ContentLogicDatabaseLoadingStarted = NotificationType((1, 3, 6, 1, 4, 1, 15397, 2, 8, 5, 4, 1)).setObjects(("PACKETLOGIC-TRAP-MIB", "pl2ContentLogicDatabase"))
if mibBuilder.loadTexts: pl2ContentLogicDatabaseLoadingStarted.setStatus('current')
if mibBuilder.loadTexts: pl2ContentLogicDatabaseLoadingStarted.setDescription('A trap for notifying that ContentLogic has started to load a database.')
pl2ContentLogicDatabaseLoadingCompleted = NotificationType((1, 3, 6, 1, 4, 1, 15397, 2, 8, 5, 4, 2)).setObjects(("PACKETLOGIC-TRAP-MIB", "pl2ContentLogicDatabase"))
if mibBuilder.loadTexts: pl2ContentLogicDatabaseLoadingCompleted.setStatus('current')
if mibBuilder.loadTexts: pl2ContentLogicDatabaseLoadingCompleted.setDescription('A trap for notifying that ContentLogic has completed loading a database.')
pl2ContentLogicDatabaseLoadingFailed = NotificationType((1, 3, 6, 1, 4, 1, 15397, 2, 8, 5, 4, 3)).setObjects(("PACKETLOGIC-TRAP-MIB", "pl2ContentLogicDatabase"), ("PACKETLOGIC-TRAP-MIB", "pl2ContentLogicReason"))
if mibBuilder.loadTexts: pl2ContentLogicDatabaseLoadingFailed.setStatus('current')
if mibBuilder.loadTexts: pl2ContentLogicDatabaseLoadingFailed.setDescription('A trap for notifying that ContentLogic has failed to load a database.')
mibBuilder.exportSymbols("PACKETLOGIC-TRAP-MIB", pl2TrapSystemStatsAlert=pl2TrapSystemStatsAlert, pl2TrapVals=pl2TrapVals, pl2StoragePhysicalDisk=pl2StoragePhysicalDisk, pl2ContentLogicTrapVals=pl2ContentLogicTrapVals, pl2ContentLogicHourlyUpdateCompleted=pl2ContentLogicHourlyUpdateCompleted, pl2ContentLogicDatabaseLoadingTraps=pl2ContentLogicDatabaseLoadingTraps, channelDescr=channelDescr, pl2Traps=pl2Traps, pl2TrapOid=pl2TrapOid, channelPort=channelPort, pl2ContentLogicCategoriesLoadingCompleted=pl2ContentLogicCategoriesLoadingCompleted, pl2ContentLogicDatabase=pl2ContentLogicDatabase, pl2TrapSystemStatsAlert64=pl2TrapSystemStatsAlert64, pl2ChannelTrapVals=pl2ChannelTrapVals, pl2ContentLogicDatabaseUpdateCompleted=pl2ContentLogicDatabaseUpdateCompleted, pl2Trap=pl2Trap, pl2TrapGeneric=pl2TrapGeneric, newState=newState, pl2StorageGenericTrap=pl2StorageGenericTrap, pl2ContentLogicDatabaseLoadingStarted=pl2ContentLogicDatabaseLoadingStarted, pl2ContentLogicDatabaseUpdateTraps=pl2ContentLogicDatabaseUpdateTraps, pl2StorageVirtualDisk=pl2StorageVirtualDisk, pl2ContentLogicDatabaseLoadingFailed=pl2ContentLogicDatabaseLoadingFailed, pl2ContentLogicTraps=pl2ContentLogicTraps, pl2TrapThreshold64=pl2TrapThreshold64, channelIndex=channelIndex, prevState=prevState, pl2StorageTrapVals=pl2StorageTrapVals, pl2ContentLogicHourlyUpdateFailed=pl2ContentLogicHourlyUpdateFailed, pl2StorageBattery=pl2StorageBattery, PYSNMP_MODULE_ID=pl2Trap, pl2ContentLogicCategoriesLoadingStarted=pl2ContentLogicCategoriesLoadingStarted, pl2ContentLogicCategoriesLoadingTraps=pl2ContentLogicCategoriesLoadingTraps, pl2ContentLogicHourlyUpdateTraps=pl2ContentLogicHourlyUpdateTraps, pl2TrapValue=pl2TrapValue, pl2TrapValue64=pl2TrapValue64, pl2ContentLogicReason=pl2ContentLogicReason, pl2ChannelStateChanged=pl2ChannelStateChanged, pl2TrapMessage=pl2TrapMessage, pl2TrapThreshold=pl2TrapThreshold, pl2StoragePowerSupply=pl2StoragePowerSupply, pl2ContentLogicCategoriesLoadingFailed=pl2ContentLogicCategoriesLoadingFailed, pl2ContentLogicDatabaseLoadingCompleted=pl2ContentLogicDatabaseLoadingCompleted, pl2TrapSystemStatsAlertClear=pl2TrapSystemStatsAlertClear, pl2ChannelTraps=pl2ChannelTraps, pl2ContentLogicDatabaseUpdateFailed=pl2ContentLogicDatabaseUpdateFailed, pl2ContentLogicDatabaseUpdateStarted=pl2ContentLogicDatabaseUpdateStarted, pl2ContentLogicHourlyUpdateStarted=pl2ContentLogicHourlyUpdateStarted, pl2TrapGenericMsg=pl2TrapGenericMsg)
