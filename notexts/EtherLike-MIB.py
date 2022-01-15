#
# PySNMP MIB module EtherLike-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/EtherLike-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 17:49:35 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
InterfaceIndex, ifIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "ifIndex")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
TimeTicks, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, transmission, iso, ObjectIdentity, IpAddress, Counter64, mib_2, Bits, Counter32, NotificationType, Unsigned32, Gauge32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "transmission", "iso", "ObjectIdentity", "IpAddress", "Counter64", "mib-2", "Bits", "Counter32", "NotificationType", "Unsigned32", "Gauge32", "MibIdentifier")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
etherMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 35))
etherMIB.setRevisions(('2003-09-19 00:00', '1999-08-24 04:00', '1998-06-03 21:50', '1994-02-03 04:00',))
if mibBuilder.loadTexts: etherMIB.setLastUpdated('200309190000Z')
if mibBuilder.loadTexts: etherMIB.setOrganization('IETF Ethernet Interfaces and Hub MIB Working Group')
etherMIBObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 35, 1))
dot3 = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7))
dot3StatsTable = MibTable((1, 3, 6, 1, 2, 1, 10, 7, 2), )
if mibBuilder.loadTexts: dot3StatsTable.setStatus('current')
dot3StatsEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 7, 2, 1), ).setIndexNames((0, "EtherLike-MIB", "dot3StatsIndex"))
if mibBuilder.loadTexts: dot3StatsEntry.setStatus('current')
dot3StatsIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3StatsIndex.setStatus('current')
dot3StatsAlignmentErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3StatsAlignmentErrors.setStatus('current')
dot3StatsFCSErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3StatsFCSErrors.setStatus('current')
dot3StatsSingleCollisionFrames = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3StatsSingleCollisionFrames.setStatus('current')
dot3StatsMultipleCollisionFrames = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3StatsMultipleCollisionFrames.setStatus('current')
dot3StatsSQETestErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3StatsSQETestErrors.setStatus('current')
dot3StatsDeferredTransmissions = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3StatsDeferredTransmissions.setStatus('current')
dot3StatsLateCollisions = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3StatsLateCollisions.setStatus('current')
dot3StatsExcessiveCollisions = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3StatsExcessiveCollisions.setStatus('current')
dot3StatsInternalMacTransmitErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3StatsInternalMacTransmitErrors.setStatus('current')
dot3StatsCarrierSenseErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3StatsCarrierSenseErrors.setStatus('current')
dot3StatsFrameTooLongs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3StatsFrameTooLongs.setStatus('current')
dot3StatsInternalMacReceiveErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3StatsInternalMacReceiveErrors.setStatus('current')
dot3StatsEtherChipSet = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 17), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3StatsEtherChipSet.setStatus('deprecated')
dot3StatsSymbolErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3StatsSymbolErrors.setStatus('current')
dot3StatsDuplexStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unknown", 1), ("halfDuplex", 2), ("fullDuplex", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3StatsDuplexStatus.setStatus('current')
dot3StatsRateControlAbility = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 20), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3StatsRateControlAbility.setStatus('current')
dot3StatsRateControlStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 21), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("rateControlOff", 1), ("rateControlOn", 2), ("unknown", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3StatsRateControlStatus.setStatus('current')
dot3CollTable = MibTable((1, 3, 6, 1, 2, 1, 10, 7, 5), )
if mibBuilder.loadTexts: dot3CollTable.setStatus('current')
dot3CollEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 7, 5, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "EtherLike-MIB", "dot3CollCount"))
if mibBuilder.loadTexts: dot3CollEntry.setStatus('current')
dot3CollCount = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 5, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16)))
if mibBuilder.loadTexts: dot3CollCount.setStatus('current')
dot3CollFrequencies = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 5, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3CollFrequencies.setStatus('current')
dot3ControlTable = MibTable((1, 3, 6, 1, 2, 1, 10, 7, 9), )
if mibBuilder.loadTexts: dot3ControlTable.setStatus('current')
dot3ControlEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 7, 9, 1), ).setIndexNames((0, "EtherLike-MIB", "dot3StatsIndex"))
if mibBuilder.loadTexts: dot3ControlEntry.setStatus('current')
dot3ControlFunctionsSupported = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 9, 1, 1), Bits().clone(namedValues=NamedValues(("pause", 0)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3ControlFunctionsSupported.setStatus('current')
dot3ControlInUnknownOpcodes = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 9, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3ControlInUnknownOpcodes.setStatus('current')
dot3HCControlInUnknownOpcodes = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 9, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3HCControlInUnknownOpcodes.setStatus('current')
dot3PauseTable = MibTable((1, 3, 6, 1, 2, 1, 10, 7, 10), )
if mibBuilder.loadTexts: dot3PauseTable.setStatus('current')
dot3PauseEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 7, 10, 1), ).setIndexNames((0, "EtherLike-MIB", "dot3StatsIndex"))
if mibBuilder.loadTexts: dot3PauseEntry.setStatus('current')
dot3PauseAdminMode = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 10, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("disabled", 1), ("enabledXmit", 2), ("enabledRcv", 3), ("enabledXmitAndRcv", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot3PauseAdminMode.setStatus('current')
dot3PauseOperMode = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 10, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("disabled", 1), ("enabledXmit", 2), ("enabledRcv", 3), ("enabledXmitAndRcv", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3PauseOperMode.setStatus('current')
dot3InPauseFrames = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 10, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3InPauseFrames.setStatus('current')
dot3OutPauseFrames = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 10, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3OutPauseFrames.setStatus('current')
dot3HCInPauseFrames = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 10, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3HCInPauseFrames.setStatus('current')
dot3HCOutPauseFrames = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 10, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3HCOutPauseFrames.setStatus('current')
dot3HCStatsTable = MibTable((1, 3, 6, 1, 2, 1, 10, 7, 11), )
if mibBuilder.loadTexts: dot3HCStatsTable.setStatus('current')
dot3HCStatsEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 7, 11, 1), ).setIndexNames((0, "EtherLike-MIB", "dot3StatsIndex"))
if mibBuilder.loadTexts: dot3HCStatsEntry.setStatus('current')
dot3HCStatsAlignmentErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 11, 1, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3HCStatsAlignmentErrors.setStatus('current')
dot3HCStatsFCSErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 11, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3HCStatsFCSErrors.setStatus('current')
dot3HCStatsInternalMacTransmitErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 11, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3HCStatsInternalMacTransmitErrors.setStatus('current')
dot3HCStatsFrameTooLongs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 11, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3HCStatsFrameTooLongs.setStatus('current')
dot3HCStatsInternalMacReceiveErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 11, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3HCStatsInternalMacReceiveErrors.setStatus('current')
dot3HCStatsSymbolErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 11, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3HCStatsSymbolErrors.setStatus('current')
dot3Tests = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7, 6))
dot3Errors = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7, 7))
dot3TestTdr = ObjectIdentity((1, 3, 6, 1, 2, 1, 10, 7, 6, 1))
if mibBuilder.loadTexts: dot3TestTdr.setStatus('deprecated')
dot3TestLoopBack = ObjectIdentity((1, 3, 6, 1, 2, 1, 10, 7, 6, 2))
if mibBuilder.loadTexts: dot3TestLoopBack.setStatus('deprecated')
dot3ErrorInitError = ObjectIdentity((1, 3, 6, 1, 2, 1, 10, 7, 7, 1))
if mibBuilder.loadTexts: dot3ErrorInitError.setStatus('deprecated')
dot3ErrorLoopbackError = ObjectIdentity((1, 3, 6, 1, 2, 1, 10, 7, 7, 2))
if mibBuilder.loadTexts: dot3ErrorLoopbackError.setStatus('deprecated')
etherConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 35, 2))
etherGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 35, 2, 1))
etherCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 35, 2, 2))
etherCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 35, 2, 2, 1)).setObjects(("EtherLike-MIB", "etherStatsGroup"), ("EtherLike-MIB", "etherCollisionTableGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etherCompliance = etherCompliance.setStatus('deprecated')
ether100MbsCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 35, 2, 2, 2)).setObjects(("EtherLike-MIB", "etherStats100MbsGroup"), ("EtherLike-MIB", "etherCollisionTableGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ether100MbsCompliance = ether100MbsCompliance.setStatus('deprecated')
dot3Compliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 35, 2, 2, 3)).setObjects(("EtherLike-MIB", "etherStatsBaseGroup"), ("EtherLike-MIB", "etherDuplexGroup"), ("EtherLike-MIB", "etherStatsLowSpeedGroup"), ("EtherLike-MIB", "etherStatsHighSpeedGroup"), ("EtherLike-MIB", "etherControlGroup"), ("EtherLike-MIB", "etherControlPauseGroup"), ("EtherLike-MIB", "etherCollisionTableGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dot3Compliance = dot3Compliance.setStatus('deprecated')
dot3Compliance2 = ModuleCompliance((1, 3, 6, 1, 2, 1, 35, 2, 2, 4)).setObjects(("EtherLike-MIB", "etherStatsBaseGroup2"), ("EtherLike-MIB", "etherDuplexGroup"), ("EtherLike-MIB", "etherRateControlGroup"), ("EtherLike-MIB", "etherStatsLowSpeedGroup"), ("EtherLike-MIB", "etherStatsHighSpeedGroup"), ("EtherLike-MIB", "etherStatsHalfDuplexGroup"), ("EtherLike-MIB", "etherHCStatsGroup"), ("EtherLike-MIB", "etherControlGroup"), ("EtherLike-MIB", "etherHCControlGroup"), ("EtherLike-MIB", "etherControlPauseGroup"), ("EtherLike-MIB", "etherHCControlPauseGroup"), ("EtherLike-MIB", "etherCollisionTableGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dot3Compliance2 = dot3Compliance2.setStatus('current')
etherStatsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 35, 2, 1, 1)).setObjects(("EtherLike-MIB", "dot3StatsIndex"), ("EtherLike-MIB", "dot3StatsAlignmentErrors"), ("EtherLike-MIB", "dot3StatsFCSErrors"), ("EtherLike-MIB", "dot3StatsSingleCollisionFrames"), ("EtherLike-MIB", "dot3StatsMultipleCollisionFrames"), ("EtherLike-MIB", "dot3StatsSQETestErrors"), ("EtherLike-MIB", "dot3StatsDeferredTransmissions"), ("EtherLike-MIB", "dot3StatsLateCollisions"), ("EtherLike-MIB", "dot3StatsExcessiveCollisions"), ("EtherLike-MIB", "dot3StatsInternalMacTransmitErrors"), ("EtherLike-MIB", "dot3StatsCarrierSenseErrors"), ("EtherLike-MIB", "dot3StatsFrameTooLongs"), ("EtherLike-MIB", "dot3StatsInternalMacReceiveErrors"), ("EtherLike-MIB", "dot3StatsEtherChipSet"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etherStatsGroup = etherStatsGroup.setStatus('deprecated')
etherCollisionTableGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 35, 2, 1, 2)).setObjects(("EtherLike-MIB", "dot3CollFrequencies"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etherCollisionTableGroup = etherCollisionTableGroup.setStatus('current')
etherStats100MbsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 35, 2, 1, 3)).setObjects(("EtherLike-MIB", "dot3StatsIndex"), ("EtherLike-MIB", "dot3StatsAlignmentErrors"), ("EtherLike-MIB", "dot3StatsFCSErrors"), ("EtherLike-MIB", "dot3StatsSingleCollisionFrames"), ("EtherLike-MIB", "dot3StatsMultipleCollisionFrames"), ("EtherLike-MIB", "dot3StatsDeferredTransmissions"), ("EtherLike-MIB", "dot3StatsLateCollisions"), ("EtherLike-MIB", "dot3StatsExcessiveCollisions"), ("EtherLike-MIB", "dot3StatsInternalMacTransmitErrors"), ("EtherLike-MIB", "dot3StatsCarrierSenseErrors"), ("EtherLike-MIB", "dot3StatsFrameTooLongs"), ("EtherLike-MIB", "dot3StatsInternalMacReceiveErrors"), ("EtherLike-MIB", "dot3StatsEtherChipSet"), ("EtherLike-MIB", "dot3StatsSymbolErrors"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etherStats100MbsGroup = etherStats100MbsGroup.setStatus('deprecated')
etherStatsBaseGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 35, 2, 1, 4)).setObjects(("EtherLike-MIB", "dot3StatsIndex"), ("EtherLike-MIB", "dot3StatsAlignmentErrors"), ("EtherLike-MIB", "dot3StatsFCSErrors"), ("EtherLike-MIB", "dot3StatsSingleCollisionFrames"), ("EtherLike-MIB", "dot3StatsMultipleCollisionFrames"), ("EtherLike-MIB", "dot3StatsDeferredTransmissions"), ("EtherLike-MIB", "dot3StatsLateCollisions"), ("EtherLike-MIB", "dot3StatsExcessiveCollisions"), ("EtherLike-MIB", "dot3StatsInternalMacTransmitErrors"), ("EtherLike-MIB", "dot3StatsCarrierSenseErrors"), ("EtherLike-MIB", "dot3StatsFrameTooLongs"), ("EtherLike-MIB", "dot3StatsInternalMacReceiveErrors"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etherStatsBaseGroup = etherStatsBaseGroup.setStatus('deprecated')
etherStatsLowSpeedGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 35, 2, 1, 5)).setObjects(("EtherLike-MIB", "dot3StatsSQETestErrors"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etherStatsLowSpeedGroup = etherStatsLowSpeedGroup.setStatus('current')
etherStatsHighSpeedGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 35, 2, 1, 6)).setObjects(("EtherLike-MIB", "dot3StatsSymbolErrors"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etherStatsHighSpeedGroup = etherStatsHighSpeedGroup.setStatus('current')
etherDuplexGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 35, 2, 1, 7)).setObjects(("EtherLike-MIB", "dot3StatsDuplexStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etherDuplexGroup = etherDuplexGroup.setStatus('current')
etherControlGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 35, 2, 1, 8)).setObjects(("EtherLike-MIB", "dot3ControlFunctionsSupported"), ("EtherLike-MIB", "dot3ControlInUnknownOpcodes"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etherControlGroup = etherControlGroup.setStatus('current')
etherControlPauseGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 35, 2, 1, 9)).setObjects(("EtherLike-MIB", "dot3PauseAdminMode"), ("EtherLike-MIB", "dot3PauseOperMode"), ("EtherLike-MIB", "dot3InPauseFrames"), ("EtherLike-MIB", "dot3OutPauseFrames"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etherControlPauseGroup = etherControlPauseGroup.setStatus('current')
etherStatsBaseGroup2 = ObjectGroup((1, 3, 6, 1, 2, 1, 35, 2, 1, 10)).setObjects(("EtherLike-MIB", "dot3StatsIndex"), ("EtherLike-MIB", "dot3StatsAlignmentErrors"), ("EtherLike-MIB", "dot3StatsFCSErrors"), ("EtherLike-MIB", "dot3StatsInternalMacTransmitErrors"), ("EtherLike-MIB", "dot3StatsFrameTooLongs"), ("EtherLike-MIB", "dot3StatsInternalMacReceiveErrors"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etherStatsBaseGroup2 = etherStatsBaseGroup2.setStatus('current')
etherStatsHalfDuplexGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 35, 2, 1, 11)).setObjects(("EtherLike-MIB", "dot3StatsSingleCollisionFrames"), ("EtherLike-MIB", "dot3StatsMultipleCollisionFrames"), ("EtherLike-MIB", "dot3StatsDeferredTransmissions"), ("EtherLike-MIB", "dot3StatsLateCollisions"), ("EtherLike-MIB", "dot3StatsExcessiveCollisions"), ("EtherLike-MIB", "dot3StatsCarrierSenseErrors"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etherStatsHalfDuplexGroup = etherStatsHalfDuplexGroup.setStatus('current')
etherHCStatsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 35, 2, 1, 12)).setObjects(("EtherLike-MIB", "dot3HCStatsAlignmentErrors"), ("EtherLike-MIB", "dot3HCStatsFCSErrors"), ("EtherLike-MIB", "dot3HCStatsInternalMacTransmitErrors"), ("EtherLike-MIB", "dot3HCStatsFrameTooLongs"), ("EtherLike-MIB", "dot3HCStatsInternalMacReceiveErrors"), ("EtherLike-MIB", "dot3HCStatsSymbolErrors"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etherHCStatsGroup = etherHCStatsGroup.setStatus('current')
etherHCControlGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 35, 2, 1, 13)).setObjects(("EtherLike-MIB", "dot3HCControlInUnknownOpcodes"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etherHCControlGroup = etherHCControlGroup.setStatus('current')
etherHCControlPauseGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 35, 2, 1, 14)).setObjects(("EtherLike-MIB", "dot3HCInPauseFrames"), ("EtherLike-MIB", "dot3HCOutPauseFrames"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etherHCControlPauseGroup = etherHCControlPauseGroup.setStatus('current')
etherRateControlGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 35, 2, 1, 15)).setObjects(("EtherLike-MIB", "dot3StatsRateControlAbility"), ("EtherLike-MIB", "dot3StatsRateControlStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etherRateControlGroup = etherRateControlGroup.setStatus('current')
mibBuilder.exportSymbols("EtherLike-MIB", dot3StatsCarrierSenseErrors=dot3StatsCarrierSenseErrors, dot3PauseAdminMode=dot3PauseAdminMode, dot3StatsTable=dot3StatsTable, etherStatsGroup=etherStatsGroup, dot3StatsFCSErrors=dot3StatsFCSErrors, dot3HCInPauseFrames=dot3HCInPauseFrames, dot3OutPauseFrames=dot3OutPauseFrames, dot3CollTable=dot3CollTable, etherStatsLowSpeedGroup=etherStatsLowSpeedGroup, etherConformance=etherConformance, ether100MbsCompliance=ether100MbsCompliance, etherStatsHalfDuplexGroup=etherStatsHalfDuplexGroup, dot3TestTdr=dot3TestTdr, PYSNMP_MODULE_ID=etherMIB, etherStats100MbsGroup=etherStats100MbsGroup, dot3Errors=dot3Errors, dot3ControlTable=dot3ControlTable, etherStatsHighSpeedGroup=etherStatsHighSpeedGroup, dot3ControlInUnknownOpcodes=dot3ControlInUnknownOpcodes, etherMIBObjects=etherMIBObjects, etherStatsBaseGroup2=etherStatsBaseGroup2, dot3Compliance2=dot3Compliance2, etherMIB=etherMIB, dot3PauseOperMode=dot3PauseOperMode, etherCollisionTableGroup=etherCollisionTableGroup, dot3PauseTable=dot3PauseTable, dot3Tests=dot3Tests, dot3HCControlInUnknownOpcodes=dot3HCControlInUnknownOpcodes, dot3StatsMultipleCollisionFrames=dot3StatsMultipleCollisionFrames, dot3StatsEtherChipSet=dot3StatsEtherChipSet, etherDuplexGroup=etherDuplexGroup, dot3HCStatsSymbolErrors=dot3HCStatsSymbolErrors, etherCompliances=etherCompliances, dot3CollCount=dot3CollCount, dot3InPauseFrames=dot3InPauseFrames, dot3HCStatsFrameTooLongs=dot3HCStatsFrameTooLongs, dot3StatsSingleCollisionFrames=dot3StatsSingleCollisionFrames, dot3HCStatsAlignmentErrors=dot3HCStatsAlignmentErrors, dot3HCStatsEntry=dot3HCStatsEntry, dot3=dot3, dot3StatsIndex=dot3StatsIndex, dot3StatsSymbolErrors=dot3StatsSymbolErrors, dot3ControlEntry=dot3ControlEntry, etherHCControlPauseGroup=etherHCControlPauseGroup, etherHCStatsGroup=etherHCStatsGroup, dot3StatsDeferredTransmissions=dot3StatsDeferredTransmissions, dot3StatsInternalMacReceiveErrors=dot3StatsInternalMacReceiveErrors, dot3ErrorLoopbackError=dot3ErrorLoopbackError, etherControlPauseGroup=etherControlPauseGroup, dot3HCStatsInternalMacTransmitErrors=dot3HCStatsInternalMacTransmitErrors, etherGroups=etherGroups, dot3CollEntry=dot3CollEntry, dot3HCStatsInternalMacReceiveErrors=dot3HCStatsInternalMacReceiveErrors, dot3StatsDuplexStatus=dot3StatsDuplexStatus, dot3HCStatsFCSErrors=dot3HCStatsFCSErrors, etherHCControlGroup=etherHCControlGroup, dot3StatsFrameTooLongs=dot3StatsFrameTooLongs, dot3ControlFunctionsSupported=dot3ControlFunctionsSupported, dot3StatsExcessiveCollisions=dot3StatsExcessiveCollisions, dot3StatsAlignmentErrors=dot3StatsAlignmentErrors, dot3CollFrequencies=dot3CollFrequencies, etherStatsBaseGroup=etherStatsBaseGroup, dot3ErrorInitError=dot3ErrorInitError, dot3StatsLateCollisions=dot3StatsLateCollisions, dot3StatsRateControlStatus=dot3StatsRateControlStatus, dot3HCStatsTable=dot3HCStatsTable, etherCompliance=etherCompliance, etherControlGroup=etherControlGroup, dot3StatsRateControlAbility=dot3StatsRateControlAbility, dot3StatsInternalMacTransmitErrors=dot3StatsInternalMacTransmitErrors, dot3StatsEntry=dot3StatsEntry, dot3StatsSQETestErrors=dot3StatsSQETestErrors, dot3TestLoopBack=dot3TestLoopBack, dot3PauseEntry=dot3PauseEntry, etherRateControlGroup=etherRateControlGroup, dot3Compliance=dot3Compliance, dot3HCOutPauseFrames=dot3HCOutPauseFrames)
