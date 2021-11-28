#
# PySNMP MIB module SNMP-REPEATER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/SNMP-REPEATER-MIB
# Produced by pysmi-1.1.3 at Sun Nov 28 20:09:00 2021
# On host fv-az77-612 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, ObjectIdentity, iso, NotificationType, Counter64, Gauge32, mib_2, Counter32, MibIdentifier, Bits, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, NotificationType, Unsigned32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "ObjectIdentity", "iso", "NotificationType", "Counter64", "Gauge32", "mib-2", "Counter32", "MibIdentifier", "Bits", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "NotificationType", "Unsigned32", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
snmpDot3RptrMgt = MibIdentifier((1, 3, 6, 1, 2, 1, 22))
class MacAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

rptrBasicPackage = MibIdentifier((1, 3, 6, 1, 2, 1, 22, 1))
rptrMonitorPackage = MibIdentifier((1, 3, 6, 1, 2, 1, 22, 2))
rptrAddrTrackPackage = MibIdentifier((1, 3, 6, 1, 2, 1, 22, 3))
rptrRptrInfo = MibIdentifier((1, 3, 6, 1, 2, 1, 22, 1, 1))
rptrGroupInfo = MibIdentifier((1, 3, 6, 1, 2, 1, 22, 1, 2))
rptrPortInfo = MibIdentifier((1, 3, 6, 1, 2, 1, 22, 1, 3))
rptrMonitorRptrInfo = MibIdentifier((1, 3, 6, 1, 2, 1, 22, 2, 1))
rptrMonitorGroupInfo = MibIdentifier((1, 3, 6, 1, 2, 1, 22, 2, 2))
rptrMonitorPortInfo = MibIdentifier((1, 3, 6, 1, 2, 1, 22, 2, 3))
rptrAddrTrackRptrInfo = MibIdentifier((1, 3, 6, 1, 2, 1, 22, 3, 1))
rptrAddrTrackGroupInfo = MibIdentifier((1, 3, 6, 1, 2, 1, 22, 3, 2))
rptrAddrTrackPortInfo = MibIdentifier((1, 3, 6, 1, 2, 1, 22, 3, 3))
rptrGroupCapacity = MibScalar((1, 3, 6, 1, 2, 1, 22, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rptrGroupCapacity.setStatus('mandatory')
rptrOperStatus = MibScalar((1, 3, 6, 1, 2, 1, 22, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("other", 1), ("ok", 2), ("rptrFailure", 3), ("groupFailure", 4), ("portFailure", 5), ("generalFailure", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rptrOperStatus.setStatus('mandatory')
rptrHealthText = MibScalar((1, 3, 6, 1, 2, 1, 22, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rptrHealthText.setStatus('mandatory')
rptrReset = MibScalar((1, 3, 6, 1, 2, 1, 22, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noReset", 1), ("reset", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rptrReset.setStatus('mandatory')
rptrNonDisruptTest = MibScalar((1, 3, 6, 1, 2, 1, 22, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noSelfTest", 1), ("selfTest", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rptrNonDisruptTest.setStatus('mandatory')
rptrTotalPartitionedPorts = MibScalar((1, 3, 6, 1, 2, 1, 22, 1, 1, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rptrTotalPartitionedPorts.setStatus('mandatory')
rptrGroupTable = MibTable((1, 3, 6, 1, 2, 1, 22, 1, 2, 1), )
if mibBuilder.loadTexts: rptrGroupTable.setStatus('mandatory')
rptrGroupEntry = MibTableRow((1, 3, 6, 1, 2, 1, 22, 1, 2, 1, 1), ).setIndexNames((0, "SNMP-REPEATER-MIB", "rptrGroupIndex"))
if mibBuilder.loadTexts: rptrGroupEntry.setStatus('mandatory')
rptrGroupIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 22, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rptrGroupIndex.setStatus('mandatory')
rptrGroupDescr = MibTableColumn((1, 3, 6, 1, 2, 1, 22, 1, 2, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rptrGroupDescr.setStatus('mandatory')
rptrGroupObjectID = MibTableColumn((1, 3, 6, 1, 2, 1, 22, 1, 2, 1, 1, 3), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rptrGroupObjectID.setStatus('mandatory')
rptrGroupOperStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 22, 1, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("other", 1), ("operational", 2), ("malfunctioning", 3), ("notPresent", 4), ("underTest", 5), ("resetInProgress", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rptrGroupOperStatus.setStatus('mandatory')
rptrGroupLastOperStatusChange = MibTableColumn((1, 3, 6, 1, 2, 1, 22, 1, 2, 1, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rptrGroupLastOperStatusChange.setStatus('mandatory')
rptrGroupPortCapacity = MibTableColumn((1, 3, 6, 1, 2, 1, 22, 1, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rptrGroupPortCapacity.setStatus('mandatory')
rptrPortTable = MibTable((1, 3, 6, 1, 2, 1, 22, 1, 3, 1), )
if mibBuilder.loadTexts: rptrPortTable.setStatus('mandatory')
rptrPortEntry = MibTableRow((1, 3, 6, 1, 2, 1, 22, 1, 3, 1, 1), ).setIndexNames((0, "SNMP-REPEATER-MIB", "rptrPortGroupIndex"), (0, "SNMP-REPEATER-MIB", "rptrPortIndex"))
if mibBuilder.loadTexts: rptrPortEntry.setStatus('mandatory')
rptrPortGroupIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 22, 1, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rptrPortGroupIndex.setStatus('mandatory')
rptrPortIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 22, 1, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rptrPortIndex.setStatus('mandatory')
rptrPortAdminStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 22, 1, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rptrPortAdminStatus.setStatus('mandatory')
rptrPortAutoPartitionState = MibTableColumn((1, 3, 6, 1, 2, 1, 22, 1, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("notAutoPartitioned", 1), ("autoPartitioned", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rptrPortAutoPartitionState.setStatus('mandatory')
rptrPortOperStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 22, 1, 3, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("operational", 1), ("notOperational", 2), ("notPresent", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rptrPortOperStatus.setStatus('mandatory')
rptrMonitorTransmitCollisions = MibScalar((1, 3, 6, 1, 2, 1, 22, 2, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rptrMonitorTransmitCollisions.setStatus('mandatory')
rptrMonitorGroupTable = MibTable((1, 3, 6, 1, 2, 1, 22, 2, 2, 1), )
if mibBuilder.loadTexts: rptrMonitorGroupTable.setStatus('mandatory')
rptrMonitorGroupEntry = MibTableRow((1, 3, 6, 1, 2, 1, 22, 2, 2, 1, 1), ).setIndexNames((0, "SNMP-REPEATER-MIB", "rptrMonitorGroupIndex"))
if mibBuilder.loadTexts: rptrMonitorGroupEntry.setStatus('mandatory')
rptrMonitorGroupIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 22, 2, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rptrMonitorGroupIndex.setStatus('mandatory')
rptrMonitorGroupTotalFrames = MibTableColumn((1, 3, 6, 1, 2, 1, 22, 2, 2, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rptrMonitorGroupTotalFrames.setStatus('mandatory')
rptrMonitorGroupTotalOctets = MibTableColumn((1, 3, 6, 1, 2, 1, 22, 2, 2, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rptrMonitorGroupTotalOctets.setStatus('mandatory')
rptrMonitorGroupTotalErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 22, 2, 2, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rptrMonitorGroupTotalErrors.setStatus('mandatory')
rptrMonitorPortTable = MibTable((1, 3, 6, 1, 2, 1, 22, 2, 3, 1), )
if mibBuilder.loadTexts: rptrMonitorPortTable.setStatus('mandatory')
rptrMonitorPortEntry = MibTableRow((1, 3, 6, 1, 2, 1, 22, 2, 3, 1, 1), ).setIndexNames((0, "SNMP-REPEATER-MIB", "rptrMonitorPortGroupIndex"), (0, "SNMP-REPEATER-MIB", "rptrMonitorPortIndex"))
if mibBuilder.loadTexts: rptrMonitorPortEntry.setStatus('mandatory')
rptrMonitorPortGroupIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 22, 2, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rptrMonitorPortGroupIndex.setStatus('mandatory')
rptrMonitorPortIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 22, 2, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rptrMonitorPortIndex.setStatus('mandatory')
rptrMonitorPortReadableFrames = MibTableColumn((1, 3, 6, 1, 2, 1, 22, 2, 3, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rptrMonitorPortReadableFrames.setStatus('mandatory')
rptrMonitorPortReadableOctets = MibTableColumn((1, 3, 6, 1, 2, 1, 22, 2, 3, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rptrMonitorPortReadableOctets.setStatus('mandatory')
rptrMonitorPortFCSErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 22, 2, 3, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rptrMonitorPortFCSErrors.setStatus('mandatory')
rptrMonitorPortAlignmentErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 22, 2, 3, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rptrMonitorPortAlignmentErrors.setStatus('mandatory')
rptrMonitorPortFrameTooLongs = MibTableColumn((1, 3, 6, 1, 2, 1, 22, 2, 3, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rptrMonitorPortFrameTooLongs.setStatus('mandatory')
rptrMonitorPortShortEvents = MibTableColumn((1, 3, 6, 1, 2, 1, 22, 2, 3, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rptrMonitorPortShortEvents.setStatus('mandatory')
rptrMonitorPortRunts = MibTableColumn((1, 3, 6, 1, 2, 1, 22, 2, 3, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rptrMonitorPortRunts.setStatus('mandatory')
rptrMonitorPortCollisions = MibTableColumn((1, 3, 6, 1, 2, 1, 22, 2, 3, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rptrMonitorPortCollisions.setStatus('mandatory')
rptrMonitorPortLateEvents = MibTableColumn((1, 3, 6, 1, 2, 1, 22, 2, 3, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rptrMonitorPortLateEvents.setStatus('mandatory')
rptrMonitorPortVeryLongEvents = MibTableColumn((1, 3, 6, 1, 2, 1, 22, 2, 3, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rptrMonitorPortVeryLongEvents.setStatus('mandatory')
rptrMonitorPortDataRateMismatches = MibTableColumn((1, 3, 6, 1, 2, 1, 22, 2, 3, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rptrMonitorPortDataRateMismatches.setStatus('mandatory')
rptrMonitorPortAutoPartitions = MibTableColumn((1, 3, 6, 1, 2, 1, 22, 2, 3, 1, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rptrMonitorPortAutoPartitions.setStatus('mandatory')
rptrMonitorPortTotalErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 22, 2, 3, 1, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rptrMonitorPortTotalErrors.setStatus('mandatory')
rptrAddrTrackTable = MibTable((1, 3, 6, 1, 2, 1, 22, 3, 3, 1), )
if mibBuilder.loadTexts: rptrAddrTrackTable.setStatus('mandatory')
rptrAddrTrackEntry = MibTableRow((1, 3, 6, 1, 2, 1, 22, 3, 3, 1, 1), ).setIndexNames((0, "SNMP-REPEATER-MIB", "rptrAddrTrackGroupIndex"), (0, "SNMP-REPEATER-MIB", "rptrAddrTrackPortIndex"))
if mibBuilder.loadTexts: rptrAddrTrackEntry.setStatus('mandatory')
rptrAddrTrackGroupIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 22, 3, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rptrAddrTrackGroupIndex.setStatus('mandatory')
rptrAddrTrackPortIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 22, 3, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rptrAddrTrackPortIndex.setStatus('mandatory')
rptrAddrTrackLastSourceAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 22, 3, 3, 1, 1, 3), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rptrAddrTrackLastSourceAddress.setStatus('deprecated')
rptrAddrTrackSourceAddrChanges = MibTableColumn((1, 3, 6, 1, 2, 1, 22, 3, 3, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rptrAddrTrackSourceAddrChanges.setStatus('mandatory')
rptrAddrTrackNewLastSrcAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 22, 3, 3, 1, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 6))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rptrAddrTrackNewLastSrcAddress.setStatus('mandatory')
rptrHealth = NotificationType((1, 3, 6, 1, 2, 1, 22) + (0,1)).setObjects(("SNMP-REPEATER-MIB", "rptrOperStatus"))
rptrGroupChange = NotificationType((1, 3, 6, 1, 2, 1, 22) + (0,2)).setObjects(("SNMP-REPEATER-MIB", "rptrGroupIndex"))
rptrResetEvent = NotificationType((1, 3, 6, 1, 2, 1, 22) + (0,3)).setObjects(("SNMP-REPEATER-MIB", "rptrOperStatus"))
mibBuilder.exportSymbols("SNMP-REPEATER-MIB", rptrMonitorPortLateEvents=rptrMonitorPortLateEvents, rptrGroupPortCapacity=rptrGroupPortCapacity, rptrMonitorPortAlignmentErrors=rptrMonitorPortAlignmentErrors, rptrOperStatus=rptrOperStatus, rptrGroupOperStatus=rptrGroupOperStatus, rptrMonitorPackage=rptrMonitorPackage, rptrMonitorGroupTotalErrors=rptrMonitorGroupTotalErrors, rptrAddrTrackTable=rptrAddrTrackTable, rptrMonitorPortCollisions=rptrMonitorPortCollisions, rptrBasicPackage=rptrBasicPackage, rptrMonitorPortInfo=rptrMonitorPortInfo, rptrTotalPartitionedPorts=rptrTotalPartitionedPorts, rptrPortIndex=rptrPortIndex, rptrMonitorPortReadableFrames=rptrMonitorPortReadableFrames, rptrMonitorTransmitCollisions=rptrMonitorTransmitCollisions, rptrPortGroupIndex=rptrPortGroupIndex, rptrMonitorPortGroupIndex=rptrMonitorPortGroupIndex, rptrGroupChange=rptrGroupChange, rptrRptrInfo=rptrRptrInfo, rptrPortOperStatus=rptrPortOperStatus, rptrMonitorRptrInfo=rptrMonitorRptrInfo, rptrMonitorGroupEntry=rptrMonitorGroupEntry, rptrPortEntry=rptrPortEntry, rptrPortInfo=rptrPortInfo, rptrMonitorPortTable=rptrMonitorPortTable, rptrHealthText=rptrHealthText, rptrMonitorPortShortEvents=rptrMonitorPortShortEvents, rptrMonitorPortTotalErrors=rptrMonitorPortTotalErrors, MacAddress=MacAddress, rptrResetEvent=rptrResetEvent, rptrPortAutoPartitionState=rptrPortAutoPartitionState, rptrMonitorGroupTotalOctets=rptrMonitorGroupTotalOctets, rptrMonitorPortRunts=rptrMonitorPortRunts, rptrMonitorPortIndex=rptrMonitorPortIndex, rptrAddrTrackEntry=rptrAddrTrackEntry, rptrGroupEntry=rptrGroupEntry, rptrGroupObjectID=rptrGroupObjectID, rptrAddrTrackRptrInfo=rptrAddrTrackRptrInfo, rptrAddrTrackPortIndex=rptrAddrTrackPortIndex, rptrAddrTrackSourceAddrChanges=rptrAddrTrackSourceAddrChanges, rptrMonitorGroupTotalFrames=rptrMonitorGroupTotalFrames, rptrGroupCapacity=rptrGroupCapacity, rptrNonDisruptTest=rptrNonDisruptTest, rptrAddrTrackPackage=rptrAddrTrackPackage, rptrAddrTrackGroupInfo=rptrAddrTrackGroupInfo, rptrGroupDescr=rptrGroupDescr, rptrAddrTrackNewLastSrcAddress=rptrAddrTrackNewLastSrcAddress, rptrMonitorPortFrameTooLongs=rptrMonitorPortFrameTooLongs, rptrHealth=rptrHealth, rptrMonitorGroupTable=rptrMonitorGroupTable, rptrMonitorPortAutoPartitions=rptrMonitorPortAutoPartitions, rptrGroupTable=rptrGroupTable, rptrGroupInfo=rptrGroupInfo, rptrPortTable=rptrPortTable, rptrMonitorGroupIndex=rptrMonitorGroupIndex, rptrGroupIndex=rptrGroupIndex, rptrReset=rptrReset, rptrGroupLastOperStatusChange=rptrGroupLastOperStatusChange, rptrMonitorPortFCSErrors=rptrMonitorPortFCSErrors, rptrAddrTrackGroupIndex=rptrAddrTrackGroupIndex, rptrMonitorPortVeryLongEvents=rptrMonitorPortVeryLongEvents, rptrMonitorPortDataRateMismatches=rptrMonitorPortDataRateMismatches, rptrPortAdminStatus=rptrPortAdminStatus, snmpDot3RptrMgt=snmpDot3RptrMgt, rptrAddrTrackPortInfo=rptrAddrTrackPortInfo, rptrMonitorPortReadableOctets=rptrMonitorPortReadableOctets, rptrMonitorPortEntry=rptrMonitorPortEntry, rptrMonitorGroupInfo=rptrMonitorGroupInfo, rptrAddrTrackLastSourceAddress=rptrAddrTrackLastSourceAddress)
