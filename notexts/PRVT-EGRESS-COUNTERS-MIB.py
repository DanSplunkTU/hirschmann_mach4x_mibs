#
# PySNMP MIB module PRVT-EGRESS-COUNTERS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/telco-systems/binos/PRVT-EGRESS-COUNTERS-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:39:22 2022
# On host fv-az36-988 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
ifIndex, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "ifIndex", "InterfaceIndex")
switch, = mibBuilder.importSymbols("PRVT-SWITCH-MIB", "switch")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Bits, NotificationType, Integer32, Counter32, TimeTicks, ObjectIdentity, Gauge32, ModuleIdentity, Counter64, IpAddress, MibIdentifier, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "NotificationType", "Integer32", "Counter32", "TimeTicks", "ObjectIdentity", "Gauge32", "ModuleIdentity", "Counter64", "IpAddress", "MibIdentifier", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso")
RowStatus, TextualConvention, TimeStamp, DisplayString, StorageType, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "TimeStamp", "DisplayString", "StorageType", "TruthValue")
prvtEgressCounterMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 738, 1, 5, 160))
prvtEgressCounterMib.setRevisions(('2010-05-21 00:00',))
if mibBuilder.loadTexts: prvtEgressCounterMib.setLastUpdated('201005210000Z')
if mibBuilder.loadTexts: prvtEgressCounterMib.setOrganization('BATM Advanced Communication')
prvtEgressCntNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 160, 0))
prvtEgressCntObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 160, 1))
prvtEgressCntConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 160, 2))
prvtEgressCntCounterSetTable = MibTable((1, 3, 6, 1, 4, 1, 738, 1, 5, 160, 1, 1), )
if mibBuilder.loadTexts: prvtEgressCntCounterSetTable.setStatus('current')
prvtEgressCntCounterSetEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 1, 5, 160, 1, 1, 1), ).setIndexNames((0, "PRVT-EGRESS-COUNTERS-MIB", "prvtEgressCntCounterSetID"))
if mibBuilder.loadTexts: prvtEgressCntCounterSetEntry.setStatus('current')
prvtEgressCntCounterSetID = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 160, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2)))
if mibBuilder.loadTexts: prvtEgressCntCounterSetID.setStatus('current')
prvtEgressCntAllPriorities = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 160, 1, 1, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtEgressCntAllPriorities.setStatus('current')
prvtEgressCntPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 160, 1, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtEgressCntPriority.setStatus('current')
prvtEgressCntAllDropLevels = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 160, 1, 1, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtEgressCntAllDropLevels.setStatus('current')
prvtEgressCntDropLevelMode = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 160, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("green", 1), ("yellow", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtEgressCntDropLevelMode.setStatus('current')
prvtEgressCntAllVlans = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 160, 1, 1, 1, 6), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtEgressCntAllVlans.setStatus('current')
prvtEgressCntVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 160, 1, 1, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtEgressCntVlan.setStatus('current')
prvtEgressCntAllInterfaces = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 160, 1, 1, 1, 8), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtEgressCntAllInterfaces.setStatus('current')
prvtEgressCntInterfaces = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 160, 1, 1, 1, 9), InterfaceIndex()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtEgressCntInterfaces.setStatus('current')
prvtEgressCntPort = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 160, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("none", 0), ("set", 1))).clone('none')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtEgressCntPort.setStatus('current')
prvtEgressCntClearCounterSet = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 160, 1, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("none", 0), ("clear", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtEgressCntClearCounterSet.setStatus('current')
prvtEgressCntCounterSetRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 160, 1, 1, 1, 12), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtEgressCntCounterSetRowStatus.setStatus('current')
prvtEgressCntCountersTable = MibTable((1, 3, 6, 1, 4, 1, 738, 1, 5, 160, 1, 2), )
if mibBuilder.loadTexts: prvtEgressCntCountersTable.setStatus('current')
prvtEgressCntCountersEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 1, 5, 160, 1, 2, 1), ).setIndexNames((0, "PRVT-EGRESS-COUNTERS-MIB", "prvtEgressCntCounterSetID"))
if mibBuilder.loadTexts: prvtEgressCntCountersEntry.setStatus('current')
prvtEgressCntOutBcFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 160, 1, 2, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtEgressCntOutBcFrames.setStatus('current')
prvtEgressCntOutNUcFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 160, 1, 2, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtEgressCntOutNUcFrames.setStatus('current')
prvtEgressCntOutUcFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 160, 1, 2, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtEgressCntOutUcFrames.setStatus('current')
prvtEgressCntEgrFilterDisc = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 160, 1, 2, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtEgressCntEgrFilterDisc.setStatus('current')
prvtEgressCntTxqFilterDisc = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 160, 1, 2, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtEgressCntTxqFilterDisc.setStatus('current')
prvtEgressCntOutCtrlFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 160, 1, 2, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtEgressCntOutCtrlFrames.setStatus('current')
prvtEgressCntEgrFrwFilterDisc = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 160, 1, 2, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtEgressCntEgrFrwFilterDisc.setStatus('current')
prvtEgressCntClearCounters = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 160, 1, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("none", 0), ("clear", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtEgressCntClearCounters.setStatus('current')
prvtEgressCntQosCountersTable = MibTable((1, 3, 6, 1, 4, 1, 738, 1, 5, 160, 1, 3), )
if mibBuilder.loadTexts: prvtEgressCntQosCountersTable.setStatus('current')
prvtEgressCntQosCountersEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 1, 5, 160, 1, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: prvtEgressCntQosCountersEntry.setStatus('current')
prvtEgressCntQosYellowPacketCounters = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 160, 1, 3, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtEgressCntQosYellowPacketCounters.setStatus('current')
prvtEgressCntQosRedPacketCounters = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 160, 1, 3, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtEgressCntQosRedPacketCounters.setStatus('current')
prvtEgressCntQosMaximumRateReached = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 160, 1, 3, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtEgressCntQosMaximumRateReached.setStatus('current')
prvtEgressCntCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 160, 2, 1))
prvtEgressCntGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 160, 2, 2))
prvtEgressCntCounterSetGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 738, 1, 5, 160, 2, 2, 1)).setObjects(("PRVT-EGRESS-COUNTERS-MIB", "prvtEgressCntAllPriorities"), ("PRVT-EGRESS-COUNTERS-MIB", "prvtEgressCntPriority"), ("PRVT-EGRESS-COUNTERS-MIB", "prvtEgressCntAllDropLevels"), ("PRVT-EGRESS-COUNTERS-MIB", "prvtEgressCntDropLevelMode"), ("PRVT-EGRESS-COUNTERS-MIB", "prvtEgressCntAllVlans"), ("PRVT-EGRESS-COUNTERS-MIB", "prvtEgressCntVlan"), ("PRVT-EGRESS-COUNTERS-MIB", "prvtEgressCntAllInterfaces"), ("PRVT-EGRESS-COUNTERS-MIB", "prvtEgressCntInterfaces"), ("PRVT-EGRESS-COUNTERS-MIB", "prvtEgressCntPort"), ("PRVT-EGRESS-COUNTERS-MIB", "prvtEgressCntClearCounterSet"), ("PRVT-EGRESS-COUNTERS-MIB", "prvtEgressCntCounterSetRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    prvtEgressCntCounterSetGroup = prvtEgressCntCounterSetGroup.setStatus('current')
prvtEgressCntCountersGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 738, 1, 5, 160, 2, 2, 2)).setObjects(("PRVT-EGRESS-COUNTERS-MIB", "prvtEgressCntOutBcFrames"), ("PRVT-EGRESS-COUNTERS-MIB", "prvtEgressCntOutNUcFrames"), ("PRVT-EGRESS-COUNTERS-MIB", "prvtEgressCntOutUcFrames"), ("PRVT-EGRESS-COUNTERS-MIB", "prvtEgressCntEgrFilterDisc"), ("PRVT-EGRESS-COUNTERS-MIB", "prvtEgressCntTxqFilterDisc"), ("PRVT-EGRESS-COUNTERS-MIB", "prvtEgressCntOutCtrlFrames"), ("PRVT-EGRESS-COUNTERS-MIB", "prvtEgressCntEgrFrwFilterDisc"), ("PRVT-EGRESS-COUNTERS-MIB", "prvtEgressCntClearCounters"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    prvtEgressCntCountersGroup = prvtEgressCntCountersGroup.setStatus('current')
prvtEgressCntQosCountersGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 738, 1, 5, 160, 2, 2, 3)).setObjects(("PRVT-EGRESS-COUNTERS-MIB", "prvtEgressCntQosYellowPacketCounters"), ("PRVT-EGRESS-COUNTERS-MIB", "prvtEgressCntQosRedPacketCounters"), ("PRVT-EGRESS-COUNTERS-MIB", "prvtEgressCntQosMaximumRateReached"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    prvtEgressCntQosCountersGroup = prvtEgressCntQosCountersGroup.setStatus('current')
prvtEgressCntCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 738, 1, 5, 160, 2, 1, 1)).setObjects(("PRVT-EGRESS-COUNTERS-MIB", "prvtEgressCntCounterSetGroup"), ("PRVT-EGRESS-COUNTERS-MIB", "prvtEgressCntCountersGroup"), ("PRVT-EGRESS-COUNTERS-MIB", "prvtEgressCntQosCountersGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    prvtEgressCntCompliance = prvtEgressCntCompliance.setStatus('current')
mibBuilder.exportSymbols("PRVT-EGRESS-COUNTERS-MIB", prvtEgressCounterMib=prvtEgressCounterMib, prvtEgressCntCounterSetEntry=prvtEgressCntCounterSetEntry, PYSNMP_MODULE_ID=prvtEgressCounterMib, prvtEgressCntGroups=prvtEgressCntGroups, prvtEgressCntAllVlans=prvtEgressCntAllVlans, prvtEgressCntQosYellowPacketCounters=prvtEgressCntQosYellowPacketCounters, prvtEgressCntPriority=prvtEgressCntPriority, prvtEgressCntEgrFilterDisc=prvtEgressCntEgrFilterDisc, prvtEgressCntDropLevelMode=prvtEgressCntDropLevelMode, prvtEgressCntInterfaces=prvtEgressCntInterfaces, prvtEgressCntCounterSetRowStatus=prvtEgressCntCounterSetRowStatus, prvtEgressCntCompliances=prvtEgressCntCompliances, prvtEgressCntConformance=prvtEgressCntConformance, prvtEgressCntOutBcFrames=prvtEgressCntOutBcFrames, prvtEgressCntEgrFrwFilterDisc=prvtEgressCntEgrFrwFilterDisc, prvtEgressCntAllInterfaces=prvtEgressCntAllInterfaces, prvtEgressCntAllPriorities=prvtEgressCntAllPriorities, prvtEgressCntVlan=prvtEgressCntVlan, prvtEgressCntPort=prvtEgressCntPort, prvtEgressCntCountersEntry=prvtEgressCntCountersEntry, prvtEgressCntCountersTable=prvtEgressCntCountersTable, prvtEgressCntQosCountersTable=prvtEgressCntQosCountersTable, prvtEgressCntQosMaximumRateReached=prvtEgressCntQosMaximumRateReached, prvtEgressCntNotifications=prvtEgressCntNotifications, prvtEgressCntOutNUcFrames=prvtEgressCntOutNUcFrames, prvtEgressCntCounterSetID=prvtEgressCntCounterSetID, prvtEgressCntCompliance=prvtEgressCntCompliance, prvtEgressCntOutUcFrames=prvtEgressCntOutUcFrames, prvtEgressCntOutCtrlFrames=prvtEgressCntOutCtrlFrames, prvtEgressCntCountersGroup=prvtEgressCntCountersGroup, prvtEgressCntQosRedPacketCounters=prvtEgressCntQosRedPacketCounters, prvtEgressCntAllDropLevels=prvtEgressCntAllDropLevels, prvtEgressCntObjects=prvtEgressCntObjects, prvtEgressCntCounterSetGroup=prvtEgressCntCounterSetGroup, prvtEgressCntTxqFilterDisc=prvtEgressCntTxqFilterDisc, prvtEgressCntClearCounters=prvtEgressCntClearCounters, prvtEgressCntCounterSetTable=prvtEgressCntCounterSetTable, prvtEgressCntQosCountersGroup=prvtEgressCntQosCountersGroup, prvtEgressCntQosCountersEntry=prvtEgressCntQosCountersEntry, prvtEgressCntClearCounterSet=prvtEgressCntClearCounterSet)
