#
# PySNMP MIB module NBS-ROADM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/mrv/NBS-ROADM-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:30:34 2022
# On host fv-az36-988 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
InterfaceIndex, ifAlias = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "ifAlias")
nbs, NbsTcMHz, NbsTcStagingCommit, NbsTcMilliDb = mibBuilder.importSymbols("NBS-MIB", "nbs", "NbsTcMHz", "NbsTcStagingCommit", "NbsTcMilliDb")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, Unsigned32, ModuleIdentity, TimeTicks, ObjectIdentity, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Gauge32, Integer32, IpAddress, MibIdentifier, NotificationType, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Unsigned32", "ModuleIdentity", "TimeTicks", "ObjectIdentity", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Gauge32", "Integer32", "IpAddress", "MibIdentifier", "NotificationType", "Counter64")
TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString")
nbsRoadmMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 629, 235))
if mibBuilder.loadTexts: nbsRoadmMib.setLastUpdated('201504300000Z')
if mibBuilder.loadTexts: nbsRoadmMib.setOrganization('NBS')
nbsRoadmCommonGrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 235, 10))
if mibBuilder.loadTexts: nbsRoadmCommonGrp.setStatus('current')
nbsRoadmFlexgridGrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 235, 20))
if mibBuilder.loadTexts: nbsRoadmFlexgridGrp.setStatus('current')
nbsRoadmStagingGrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 235, 30))
if mibBuilder.loadTexts: nbsRoadmStagingGrp.setStatus('current')
nbsRoadmCommittedGrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 235, 31))
if mibBuilder.loadTexts: nbsRoadmCommittedGrp.setStatus('current')
nbsRoadmRedundantGrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 235, 32))
if mibBuilder.loadTexts: nbsRoadmRedundantGrp.setStatus('current')
nbsRoadmTraps = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 235, 100))
if mibBuilder.loadTexts: nbsRoadmTraps.setStatus('current')
nbsRoadmEvent = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 235, 100, 0))
if mibBuilder.loadTexts: nbsRoadmEvent.setStatus('current')
nbsRoadmCommonTableSize = MibScalar((1, 3, 6, 1, 4, 1, 629, 235, 10, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsRoadmCommonTableSize.setStatus('current')
nbsRoadmCommonTable = MibTable((1, 3, 6, 1, 4, 1, 629, 235, 10, 2), )
if mibBuilder.loadTexts: nbsRoadmCommonTable.setStatus('current')
nbsRoadmCommonEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 235, 10, 2, 1), ).setIndexNames((0, "NBS-ROADM-MIB", "nbsRoadmCommonIfIndex"))
if mibBuilder.loadTexts: nbsRoadmCommonEntry.setStatus('current')
nbsRoadmCommonIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 235, 10, 2, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsRoadmCommonIfIndex.setStatus('current')
nbsRoadmCommonStagingQuickCfg = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 235, 10, 2, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("notSupported", 1), ("supported", 2), ("std100Ghz", 3), ("std50Ghz", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsRoadmCommonStagingQuickCfg.setStatus('current')
nbsRoadmCommonStagingAddCaps = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 235, 10, 2, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("notSupported", 1), ("capable", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsRoadmCommonStagingAddCaps.setStatus('current')
nbsRoadmCommonStagingDropCaps = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 235, 10, 2, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("notSupported", 1), ("capable", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsRoadmCommonStagingDropCaps.setStatus('current')
nbsRoadmCommonStagingCommit = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 235, 10, 2, 1, 20), NbsTcStagingCommit()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsRoadmCommonStagingCommit.setStatus('current')
nbsRoadmCommonCommittedGridType = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 235, 10, 2, 1, 30), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("notSupported", 1), ("reserved", 2), ("customized", 3), ("std100Ghz", 4), ("std50Ghz", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsRoadmCommonCommittedGridType.setStatus('current')
nbsRoadmCommonCommittedChannels = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 235, 10, 2, 1, 40), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsRoadmCommonCommittedChannels.setStatus('current')
nbsRoadmFlexgridTableSize = MibScalar((1, 3, 6, 1, 4, 1, 629, 235, 20, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsRoadmFlexgridTableSize.setStatus('current')
nbsRoadmFlexgridTable = MibTable((1, 3, 6, 1, 4, 1, 629, 235, 20, 2), )
if mibBuilder.loadTexts: nbsRoadmFlexgridTable.setStatus('current')
nbsRoadmFlexgridEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 235, 20, 2, 1), ).setIndexNames((0, "NBS-ROADM-MIB", "nbsRoadmFlexgridIfIndex"))
if mibBuilder.loadTexts: nbsRoadmFlexgridEntry.setStatus('current')
nbsRoadmFlexgridIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 235, 20, 2, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsRoadmFlexgridIfIndex.setStatus('current')
nbsRoadmFlexgridCenterlineMin = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 235, 20, 2, 1, 21), NbsTcMHz().clone(190100000)).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsRoadmFlexgridCenterlineMin.setStatus('current')
nbsRoadmFlexgridCenterlineMax = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 235, 20, 2, 1, 22), NbsTcMHz().clone(197250000)).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsRoadmFlexgridCenterlineMax.setStatus('current')
nbsRoadmFlexgridCenterlineIncr = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 235, 20, 2, 1, 23), NbsTcMHz().clone(12500)).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsRoadmFlexgridCenterlineIncr.setStatus('current')
nbsRoadmFlexgridBandwidthMin = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 235, 20, 2, 1, 31), NbsTcMHz().clone(25000)).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsRoadmFlexgridBandwidthMin.setStatus('current')
nbsRoadmFlexgridBandwidthMax = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 235, 20, 2, 1, 32), NbsTcMHz().clone(25000)).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsRoadmFlexgridBandwidthMax.setStatus('current')
nbsRoadmFlexgridBandwidthIncr = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 235, 20, 2, 1, 33), NbsTcMHz().clone(25000)).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsRoadmFlexgridBandwidthIncr.setStatus('current')
nbsRoadmStagingTableSize = MibScalar((1, 3, 6, 1, 4, 1, 629, 235, 30, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsRoadmStagingTableSize.setStatus('current')
nbsRoadmStagingTable = MibTable((1, 3, 6, 1, 4, 1, 629, 235, 30, 2), )
if mibBuilder.loadTexts: nbsRoadmStagingTable.setStatus('current')
nbsRoadmStagingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 235, 30, 2, 1), ).setIndexNames((0, "NBS-ROADM-MIB", "nbsRoadmStagingIfIndex"), (0, "NBS-ROADM-MIB", "nbsRoadmStagingCenterline"))
if mibBuilder.loadTexts: nbsRoadmStagingEntry.setStatus('current')
nbsRoadmStagingIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 235, 30, 2, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsRoadmStagingIfIndex.setStatus('current')
nbsRoadmStagingCenterline = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 235, 30, 2, 1, 2), NbsTcMHz()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsRoadmStagingCenterline.setStatus('current')
nbsRoadmStagingBandwidth = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 235, 30, 2, 1, 10), NbsTcMHz().clone(100000)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nbsRoadmStagingBandwidth.setStatus('current')
nbsRoadmStagingChannelName = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 235, 30, 2, 1, 30), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nbsRoadmStagingChannelName.setStatus('current')
nbsRoadmStagingAddPort = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 235, 30, 2, 1, 41), InterfaceIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nbsRoadmStagingAddPort.setStatus('current')
nbsRoadmStagingDropPort = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 235, 30, 2, 1, 42), InterfaceIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nbsRoadmStagingDropPort.setStatus('current')
nbsRoadmStagingSecondaryPort = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 235, 30, 2, 1, 43), InterfaceIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nbsRoadmStagingSecondaryPort.setStatus('current')
nbsRoadmStagingSecondAttenu = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 235, 30, 2, 1, 44), NbsTcMilliDb().clone(-1000000)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nbsRoadmStagingSecondAttenu.setStatus('current')
nbsRoadmStagingAddAttenu = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 235, 30, 2, 1, 51), NbsTcMilliDb().clone(-1000000)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nbsRoadmStagingAddAttenu.setStatus('current')
nbsRoadmStagingDropAttenu = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 235, 30, 2, 1, 52), NbsTcMilliDb().clone(-1000000)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nbsRoadmStagingDropAttenu.setStatus('current')
nbsRoadmStagingItuName = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 235, 30, 2, 1, 53), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsRoadmStagingItuName.setStatus('current')
nbsRoadmStagingRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 235, 30, 2, 1, 99), RowStatus().clone('active')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nbsRoadmStagingRowStatus.setStatus('current')
nbsRoadmCommittedTableSize = MibScalar((1, 3, 6, 1, 4, 1, 629, 235, 31, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsRoadmCommittedTableSize.setStatus('current')
nbsRoadmCommittedTable = MibTable((1, 3, 6, 1, 4, 1, 629, 235, 31, 2), )
if mibBuilder.loadTexts: nbsRoadmCommittedTable.setStatus('current')
nbsRoadmCommittedEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 235, 31, 2, 1), ).setIndexNames((0, "NBS-ROADM-MIB", "nbsRoadmCommittedIfIndex"), (0, "NBS-ROADM-MIB", "nbsRoadmCommittedCenterline"))
if mibBuilder.loadTexts: nbsRoadmCommittedEntry.setStatus('current')
nbsRoadmCommittedIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 235, 31, 2, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsRoadmCommittedIfIndex.setStatus('current')
nbsRoadmCommittedCenterline = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 235, 31, 2, 1, 2), NbsTcMHz()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsRoadmCommittedCenterline.setStatus('current')
nbsRoadmCommittedBandwidth = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 235, 31, 2, 1, 10), NbsTcMHz().clone(100000)).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsRoadmCommittedBandwidth.setStatus('current')
nbsRoadmCommittedChannelName = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 235, 31, 2, 1, 30), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsRoadmCommittedChannelName.setStatus('current')
nbsRoadmCommittedAddPort = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 235, 31, 2, 1, 41), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsRoadmCommittedAddPort.setStatus('current')
nbsRoadmCommittedDropPort = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 235, 31, 2, 1, 42), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsRoadmCommittedDropPort.setStatus('current')
nbsRoadmCommittedSecondaryPort = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 235, 31, 2, 1, 43), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsRoadmCommittedSecondaryPort.setStatus('current')
nbsRoadmCommittedSecondAttenu = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 235, 31, 2, 1, 44), NbsTcMilliDb()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsRoadmCommittedSecondAttenu.setStatus('current')
nbsRoadmCommittedAddAttenu = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 235, 31, 2, 1, 51), NbsTcMilliDb()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsRoadmCommittedAddAttenu.setStatus('current')
nbsRoadmCommittedDropAttenu = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 235, 31, 2, 1, 52), NbsTcMilliDb()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsRoadmCommittedDropAttenu.setStatus('current')
nbsRoadmCommittedItuName = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 235, 31, 2, 1, 60), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsRoadmCommittedItuName.setStatus('current')
nbsRoadmRedundantTableSize = MibScalar((1, 3, 6, 1, 4, 1, 629, 235, 32, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsRoadmRedundantTableSize.setStatus('current')
nbsRoadmRedundantTable = MibTable((1, 3, 6, 1, 4, 1, 629, 235, 32, 2), )
if mibBuilder.loadTexts: nbsRoadmRedundantTable.setStatus('current')
nbsRoadmRedundantEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 235, 32, 2, 1), ).setIndexNames((0, "NBS-ROADM-MIB", "nbsRoadmRedundantIfIndex"), (0, "NBS-ROADM-MIB", "nbsRoadmRedundantCenterline"))
if mibBuilder.loadTexts: nbsRoadmRedundantEntry.setStatus('current')
nbsRoadmRedundantIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 235, 32, 2, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsRoadmRedundantIfIndex.setStatus('current')
nbsRoadmRedundantCenterline = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 235, 32, 2, 1, 2), NbsTcMHz()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsRoadmRedundantCenterline.setStatus('current')
nbsRoadmRedundantItuName = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 235, 32, 2, 1, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsRoadmRedundantItuName.setStatus('current')
nbsRoadmRedundantChannelName = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 235, 32, 2, 1, 20), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsRoadmRedundantChannelName.setStatus('current')
nbsRoadmRedundantMapPort = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 235, 32, 2, 1, 29), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsRoadmRedundantMapPort.setStatus('current')
nbsRoadmRedundantSecondaryPort = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 235, 32, 2, 1, 30), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsRoadmRedundantSecondaryPort.setStatus('current')
nbsRoadmRedundantCurPort = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 235, 32, 2, 1, 40), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsRoadmRedundantCurPort.setStatus('current')
nbsRoadmRedundantCurAttenu = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 235, 32, 2, 1, 41), NbsTcMilliDb()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsRoadmRedundantCurAttenu.setStatus('current')
nbsRoadmRedundantCurState = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 235, 32, 2, 1, 50), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("switching", 1), ("active", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsRoadmRedundantCurState.setStatus('current')
nbsRoadmEventStageAreaCommitted = NotificationType((1, 3, 6, 1, 4, 1, 629, 235, 100, 0, 10)).setObjects(("NBS-ROADM-MIB", "nbsRoadmCommonIfIndex"), ("IF-MIB", "ifAlias"), ("NBS-ROADM-MIB", "nbsRoadmCommonCommittedGridType"), ("NBS-ROADM-MIB", "nbsRoadmCommonCommittedChannels"))
if mibBuilder.loadTexts: nbsRoadmEventStageAreaCommitted.setStatus('current')
nbsRoadmEventRedundancyTriggered = NotificationType((1, 3, 6, 1, 4, 1, 629, 235, 100, 0, 20)).setObjects(("NBS-ROADM-MIB", "nbsRoadmRedundantIfIndex"), ("NBS-ROADM-MIB", "nbsRoadmRedundantCenterline"))
if mibBuilder.loadTexts: nbsRoadmEventRedundancyTriggered.setStatus('current')
mibBuilder.exportSymbols("NBS-ROADM-MIB", nbsRoadmStagingDropPort=nbsRoadmStagingDropPort, PYSNMP_MODULE_ID=nbsRoadmMib, nbsRoadmCommonTableSize=nbsRoadmCommonTableSize, nbsRoadmFlexgridTable=nbsRoadmFlexgridTable, nbsRoadmFlexgridCenterlineMin=nbsRoadmFlexgridCenterlineMin, nbsRoadmFlexgridBandwidthIncr=nbsRoadmFlexgridBandwidthIncr, nbsRoadmStagingTable=nbsRoadmStagingTable, nbsRoadmStagingEntry=nbsRoadmStagingEntry, nbsRoadmCommittedDropPort=nbsRoadmCommittedDropPort, nbsRoadmCommittedCenterline=nbsRoadmCommittedCenterline, nbsRoadmRedundantCenterline=nbsRoadmRedundantCenterline, nbsRoadmRedundantTableSize=nbsRoadmRedundantTableSize, nbsRoadmTraps=nbsRoadmTraps, nbsRoadmCommittedSecondaryPort=nbsRoadmCommittedSecondaryPort, nbsRoadmCommittedBandwidth=nbsRoadmCommittedBandwidth, nbsRoadmFlexgridTableSize=nbsRoadmFlexgridTableSize, nbsRoadmRedundantCurState=nbsRoadmRedundantCurState, nbsRoadmCommonGrp=nbsRoadmCommonGrp, nbsRoadmStagingChannelName=nbsRoadmStagingChannelName, nbsRoadmCommonStagingQuickCfg=nbsRoadmCommonStagingQuickCfg, nbsRoadmMib=nbsRoadmMib, nbsRoadmCommonCommittedGridType=nbsRoadmCommonCommittedGridType, nbsRoadmFlexgridCenterlineMax=nbsRoadmFlexgridCenterlineMax, nbsRoadmFlexgridEntry=nbsRoadmFlexgridEntry, nbsRoadmFlexgridBandwidthMax=nbsRoadmFlexgridBandwidthMax, nbsRoadmStagingAddPort=nbsRoadmStagingAddPort, nbsRoadmStagingItuName=nbsRoadmStagingItuName, nbsRoadmCommittedAddAttenu=nbsRoadmCommittedAddAttenu, nbsRoadmEventStageAreaCommitted=nbsRoadmEventStageAreaCommitted, nbsRoadmCommittedChannelName=nbsRoadmCommittedChannelName, nbsRoadmStagingBandwidth=nbsRoadmStagingBandwidth, nbsRoadmCommittedIfIndex=nbsRoadmCommittedIfIndex, nbsRoadmRedundantTable=nbsRoadmRedundantTable, nbsRoadmCommonEntry=nbsRoadmCommonEntry, nbsRoadmStagingRowStatus=nbsRoadmStagingRowStatus, nbsRoadmCommittedGrp=nbsRoadmCommittedGrp, nbsRoadmRedundantCurPort=nbsRoadmRedundantCurPort, nbsRoadmStagingDropAttenu=nbsRoadmStagingDropAttenu, nbsRoadmEvent=nbsRoadmEvent, nbsRoadmFlexgridBandwidthMin=nbsRoadmFlexgridBandwidthMin, nbsRoadmCommonCommittedChannels=nbsRoadmCommonCommittedChannels, nbsRoadmStagingCenterline=nbsRoadmStagingCenterline, nbsRoadmStagingAddAttenu=nbsRoadmStagingAddAttenu, nbsRoadmCommittedAddPort=nbsRoadmCommittedAddPort, nbsRoadmRedundantItuName=nbsRoadmRedundantItuName, nbsRoadmRedundantMapPort=nbsRoadmRedundantMapPort, nbsRoadmCommittedTableSize=nbsRoadmCommittedTableSize, nbsRoadmFlexgridCenterlineIncr=nbsRoadmFlexgridCenterlineIncr, nbsRoadmRedundantCurAttenu=nbsRoadmRedundantCurAttenu, nbsRoadmRedundantGrp=nbsRoadmRedundantGrp, nbsRoadmCommittedSecondAttenu=nbsRoadmCommittedSecondAttenu, nbsRoadmCommittedDropAttenu=nbsRoadmCommittedDropAttenu, nbsRoadmRedundantChannelName=nbsRoadmRedundantChannelName, nbsRoadmStagingGrp=nbsRoadmStagingGrp, nbsRoadmCommonStagingCommit=nbsRoadmCommonStagingCommit, nbsRoadmRedundantEntry=nbsRoadmRedundantEntry, nbsRoadmCommittedEntry=nbsRoadmCommittedEntry, nbsRoadmCommonStagingDropCaps=nbsRoadmCommonStagingDropCaps, nbsRoadmCommonTable=nbsRoadmCommonTable, nbsRoadmFlexgridGrp=nbsRoadmFlexgridGrp, nbsRoadmFlexgridIfIndex=nbsRoadmFlexgridIfIndex, nbsRoadmEventRedundancyTriggered=nbsRoadmEventRedundancyTriggered, nbsRoadmCommittedTable=nbsRoadmCommittedTable, nbsRoadmRedundantSecondaryPort=nbsRoadmRedundantSecondaryPort, nbsRoadmCommonStagingAddCaps=nbsRoadmCommonStagingAddCaps, nbsRoadmStagingTableSize=nbsRoadmStagingTableSize, nbsRoadmCommittedItuName=nbsRoadmCommittedItuName, nbsRoadmRedundantIfIndex=nbsRoadmRedundantIfIndex, nbsRoadmStagingIfIndex=nbsRoadmStagingIfIndex, nbsRoadmCommonIfIndex=nbsRoadmCommonIfIndex, nbsRoadmStagingSecondAttenu=nbsRoadmStagingSecondAttenu, nbsRoadmStagingSecondaryPort=nbsRoadmStagingSecondaryPort)
