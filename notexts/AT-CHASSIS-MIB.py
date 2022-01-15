#
# PySNMP MIB module AT-CHASSIS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/allied/AT-CHASSIS-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 17:51:15 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
sysinfo, = mibBuilder.importSymbols("AT-SMI-MIB", "sysinfo")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, Integer32, Bits, MibIdentifier, Counter64, Unsigned32, iso, ObjectIdentity, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, ModuleIdentity, IpAddress, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Integer32", "Bits", "MibIdentifier", "Counter64", "Unsigned32", "iso", "ObjectIdentity", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "ModuleIdentity", "IpAddress", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
chassis = ModuleIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 23))
chassis.setRevisions(('2014-06-09 00:00', '2014-05-26 00:00', '2014-04-16 00:00', '2012-05-15 00:00', '2011-09-26 00:00',))
if mibBuilder.loadTexts: chassis.setLastUpdated('201406090000Z')
if mibBuilder.loadTexts: chassis.setOrganization('Allied Telesis, Inc.')
chassisNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 23, 0))
chassisCardRoleChangeNotify = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 23, 0, 1)).setObjects(("AT-CHASSIS-MIB", "slotNumber"), ("AT-CHASSIS-MIB", "chassisRole"))
if mibBuilder.loadTexts: chassisCardRoleChangeNotify.setStatus('current')
chassisCardJoinNotify = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 23, 0, 2)).setObjects(("AT-CHASSIS-MIB", "slotNumber"))
if mibBuilder.loadTexts: chassisCardJoinNotify.setStatus('current')
chassisCardLeaveNotify = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 23, 0, 3)).setObjects(("AT-CHASSIS-MIB", "slotNumber"))
if mibBuilder.loadTexts: chassisCardLeaveNotify.setStatus('current')
slotNumber = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 23, 0, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 12))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: slotNumber.setStatus('current')
chassisRole = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 23, 0, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("leaving", 1), ("discovering", 2), ("synchronizing", 3), ("standbyMember", 4), ("pendingMaster", 5), ("disabledMaster", 6), ("activeMaster", 7)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: chassisRole.setStatus('current')
chassisCardTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 23, 1), )
if mibBuilder.loadTexts: chassisCardTable.setStatus('current')
chassisCardEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 23, 1, 1), ).setIndexNames((0, "AT-CHASSIS-MIB", "chassisCardSlot"))
if mibBuilder.loadTexts: chassisCardEntry.setStatus('current')
chassisCardSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 23, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 24))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisCardSlot.setStatus('current')
chassisCardBoardOID = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 23, 1, 1, 2), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisCardBoardOID.setStatus('current')
chassisCardName = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 23, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisCardName.setStatus('current')
chassisCardState = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 23, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))).clone(namedValues=NamedValues(("unknown", 1), ("configuring", 2), ("syncing", 3), ("online", 4), ("syncingFirmware", 5), ("joining", 6), ("incompatibleSW", 7), ("disabled", 8), ("initializing", 9), ("booting", 10), ("unsupportedHW", 11), ("provisioned", 12)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisCardState.setStatus('current')
chassisCardControllerState = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 23, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unknown", 1), ("active", 2), ("standby", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisCardControllerState.setStatus('current')
chassiCardSwVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 23, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassiCardSwVersion.setStatus('current')
chassisMappingTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 23, 2), )
if mibBuilder.loadTexts: chassisMappingTable.setStatus('current')
chassisMappingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 23, 2, 1), ).setIndexNames((0, "AT-CHASSIS-MIB", "chassisNodeId"))
if mibBuilder.loadTexts: chassisMappingEntry.setStatus('current')
chassisNodeId = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 23, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 24))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisNodeId.setStatus('current')
chassisVCSMemberId = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 23, 2, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisVCSMemberId.setStatus('current')
chassisSlotNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 23, 2, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 12))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisSlotNumber.setStatus('current')
chassisNodeDisplayString = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 23, 2, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisNodeDisplayString.setStatus('current')
chassisNodeStateString = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 23, 2, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisNodeStateString.setStatus('current')
mibBuilder.exportSymbols("AT-CHASSIS-MIB", chassisCardName=chassisCardName, chassisCardBoardOID=chassisCardBoardOID, chassisNotifications=chassisNotifications, chassisCardEntry=chassisCardEntry, chassisCardSlot=chassisCardSlot, slotNumber=slotNumber, chassisCardControllerState=chassisCardControllerState, chassisMappingTable=chassisMappingTable, chassisCardRoleChangeNotify=chassisCardRoleChangeNotify, chassisVCSMemberId=chassisVCSMemberId, chassisSlotNumber=chassisSlotNumber, chassisNodeStateString=chassisNodeStateString, chassisCardTable=chassisCardTable, chassis=chassis, chassisCardJoinNotify=chassisCardJoinNotify, chassisNodeDisplayString=chassisNodeDisplayString, chassiCardSwVersion=chassiCardSwVersion, chassisMappingEntry=chassisMappingEntry, PYSNMP_MODULE_ID=chassis, chassisCardState=chassisCardState, chassisCardLeaveNotify=chassisCardLeaveNotify, chassisNodeId=chassisNodeId, chassisRole=chassisRole)
