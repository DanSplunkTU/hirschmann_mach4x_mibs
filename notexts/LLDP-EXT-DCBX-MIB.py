#
# PySNMP MIB module LLDP-EXT-DCBX-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/iee/LLDP-EXT-DCBX-MIB
# Produced by pysmi-1.1.8 at Sun Jan 16 00:30:40 2022
# On host fv-az42-839 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
lldpExtensions, LldpPortNumber = mibBuilder.importSymbols("LLDP-MIB", "lldpExtensions", "LldpPortNumber")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Bits, Integer32, Counter64, iso, Counter32, IpAddress, ObjectIdentity, Unsigned32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, MibIdentifier, NotificationType, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "Counter64", "iso", "Counter32", "IpAddress", "ObjectIdentity", "Unsigned32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "MibIdentifier", "NotificationType", "Gauge32")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
lldpXdcbxMIB = ModuleIdentity((1, 0, 8802, 1, 1, 2, 1, 5, 6945))
if mibBuilder.loadTexts: lldpXdcbxMIB.setLastUpdated('200811200000Z')
if mibBuilder.loadTexts: lldpXdcbxMIB.setOrganization('IEEE ??? Working Group')
class LldpXdcbxPriority(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 7)

class LldpXdcbxPriorityGroup(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15))
    namedValues = NamedValues(("priorityGroupId0", 0), ("priorityGroupId1", 1), ("priorityGroupId2", 2), ("priorityGroupId3", 3), ("priorityGroupId4", 4), ("priorityGroupId5", 5), ("priorityGroupId6", 6), ("priorityGroupId7", 7), ("reserved8", 8), ("reserved9", 9), ("reserved10", 10), ("reserved11", 11), ("reserved12", 12), ("reserved13", 13), ("reserved14", 14), ("noBandwidthLimit", 15))

class LldpXdcbxFeatureType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(2, 3, 4))
    namedValues = NamedValues(("priorityGroup", 2), ("priorityFlowControl", 3), ("applicationProtocol", 4))

class LldpXdcbxFeatureSubType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 255)

class LldpXdcbxVersion(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 255)

class LldpXdcbxTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 7)

class LldpXdcbxPgBw(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 100)

class LldpXdcbxTCPFC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 8)

class LldpXdcbxTCPeer(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 8)

class LldpXdcbxAppProtos(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 15)

class LldpXdcbxSF(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("l2EtherType", 0), ("socketNumber", 1), ("reserved2", 2), ("reserved3", 3))

lldpXdcbxNotifications = MibIdentifier((1, 0, 8802, 1, 1, 2, 1, 5, 6945, 0))
lldpXdcbxObjects = MibIdentifier((1, 0, 8802, 1, 1, 2, 1, 5, 6945, 1))
lldpXdcbxFeatures = MibIdentifier((1, 0, 8802, 1, 1, 2, 1, 5, 6945, 2))
lldpXdcbxPortTable = MibTable((1, 0, 8802, 1, 1, 2, 1, 5, 6945, 1, 1), )
if mibBuilder.loadTexts: lldpXdcbxPortTable.setStatus('current')
lldpXdcbxPortEntry = MibTableRow((1, 0, 8802, 1, 1, 2, 1, 5, 6945, 1, 1, 1), ).setIndexNames((0, "LLDP-EXT-DCBX-MIB", "lldpXdcbxPortNumber"))
if mibBuilder.loadTexts: lldpXdcbxPortEntry.setStatus('current')
lldpXdcbxPortNumber = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 6945, 1, 1, 1, 1), LldpPortNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXdcbxPortNumber.setStatus('current')
lldpXdcbxPortEnable = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 6945, 1, 1, 1, 2), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lldpXdcbxPortEnable.setStatus('current')
lldpXdcbxPortVersionOper = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 6945, 1, 1, 1, 3), LldpXdcbxVersion()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXdcbxPortVersionOper.setStatus('current')
lldpXdcbxPortVersionMax = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 6945, 1, 1, 1, 4), LldpXdcbxVersion()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXdcbxPortVersionMax.setStatus('current')
lldpXdcbxPortSeqNo = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 6945, 1, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXdcbxPortSeqNo.setStatus('current')
lldpXdcbxPortAckNo = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 6945, 1, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXdcbxPortAckNo.setStatus('current')
lldpXdcbxFeatTable = MibTable((1, 0, 8802, 1, 1, 2, 1, 5, 6945, 2, 1), )
if mibBuilder.loadTexts: lldpXdcbxFeatTable.setStatus('current')
lldpXdcbxFeatEntry = MibTableRow((1, 0, 8802, 1, 1, 2, 1, 5, 6945, 2, 1, 1), ).setIndexNames((0, "LLDP-EXT-DCBX-MIB", "lldpXdcbxPortNumber"), (0, "LLDP-EXT-DCBX-MIB", "lldpXdcbxFeatType"), (0, "LLDP-EXT-DCBX-MIB", "lldpXdcbxFeatSubType"))
if mibBuilder.loadTexts: lldpXdcbxFeatEntry.setStatus('current')
lldpXdcbxFeatType = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 6945, 2, 1, 1, 1), LldpXdcbxFeatureType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lldpXdcbxFeatType.setStatus('current')
lldpXdcbxFeatSubType = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 6945, 2, 1, 1, 2), LldpXdcbxFeatureSubType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lldpXdcbxFeatSubType.setStatus('current')
lldpXdcbxFeatVersionOper = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 6945, 2, 1, 1, 3), LldpXdcbxVersion()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXdcbxFeatVersionOper.setStatus('current')
lldpXdcbxFeatVersionMax = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 6945, 2, 1, 1, 4), LldpXdcbxVersion()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXdcbxFeatVersionMax.setStatus('current')
lldpXdcbxFeatEnable = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 6945, 2, 1, 1, 5), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lldpXdcbxFeatEnable.setStatus('current')
lldpXdcbxFeatWilling = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 6945, 2, 1, 1, 6), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lldpXdcbxFeatWilling.setStatus('current')
lldpXdcbxFeatError = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 6945, 2, 1, 1, 7), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXdcbxFeatError.setStatus('current')
lldpXdcbxFeatAdvertise = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 6945, 2, 1, 1, 8), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lldpXdcbxFeatAdvertise.setStatus('current')
lldpXdcbxFeatOperMode = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 6945, 2, 1, 1, 9), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXdcbxFeatOperMode.setStatus('current')
lldpXdcbxFeatSyncd = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 6945, 2, 1, 1, 10), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXdcbxFeatSyncd.setStatus('current')
lldpXdcbxFeatSeqNo = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 6945, 2, 1, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXdcbxFeatSeqNo.setStatus('current')
lldpXdcbxFeatPeerWilling = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 6945, 2, 1, 1, 12), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXdcbxFeatPeerWilling.setStatus('current')
lldpXdcbxFeatLocalParameterChange = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 6945, 2, 1, 1, 13), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXdcbxFeatLocalParameterChange.setStatus('current')
lldpXdcbxFeatPeerEnable = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 6945, 2, 1, 1, 14), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXdcbxFeatPeerEnable.setStatus('current')
lldpXdcbxFeatPeerError = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 6945, 2, 1, 1, 15), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXdcbxFeatPeerError.setStatus('current')
lldpXdcbxFeatPeerAdvertise = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 6945, 2, 1, 1, 16), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lldpXdcbxFeatPeerAdvertise.setStatus('current')
lldpXdcbxFeatPeerTC = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 6945, 2, 1, 1, 17), LldpXdcbxTCPeer()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXdcbxFeatPeerTC.setStatus('current')
lldpXdcbxFeatPg = MibIdentifier((1, 0, 8802, 1, 1, 2, 1, 5, 6945, 2, 2))
lldpXdcbxFeatPgNumTCsSupported = MibScalar((1, 0, 8802, 1, 1, 2, 1, 5, 6945, 2, 2, 1), LldpXdcbxTC()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lldpXdcbxFeatPgNumTCsSupported.setStatus('current')
lldpXdcbxFeatPgPrioAllocTable = MibTable((1, 0, 8802, 1, 1, 2, 1, 5, 6945, 2, 2, 2), )
if mibBuilder.loadTexts: lldpXdcbxFeatPgPrioAllocTable.setStatus('current')
lldpXdcbxFeatPgPrioAllocEntry = MibTableRow((1, 0, 8802, 1, 1, 2, 1, 5, 6945, 2, 2, 2, 1), ).setIndexNames((0, "LLDP-EXT-DCBX-MIB", "lldpXdcbxPortNumber"), (0, "LLDP-EXT-DCBX-MIB", "lldpXdcbxFeatPgPrioAllocPrioId"))
if mibBuilder.loadTexts: lldpXdcbxFeatPgPrioAllocEntry.setStatus('current')
lldpXdcbxFeatPgPrioAllocPrioId = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 6945, 2, 2, 2, 1, 1), LldpXdcbxPriority()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lldpXdcbxFeatPgPrioAllocPrioId.setStatus('current')
lldpXdcbxFeatPgPrioAllocPgIdDesired = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 6945, 2, 2, 2, 1, 2), LldpXdcbxPriorityGroup()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lldpXdcbxFeatPgPrioAllocPgIdDesired.setStatus('current')
lldpXdcbxFeatPgPrioAllocPgIdOper = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 6945, 2, 2, 2, 1, 3), LldpXdcbxPriorityGroup()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXdcbxFeatPgPrioAllocPgIdOper.setStatus('current')
lldpXdcbxFeatPgPrioAllocPgIdPeer = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 6945, 2, 2, 2, 1, 4), LldpXdcbxPriorityGroup()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXdcbxFeatPgPrioAllocPgIdPeer.setStatus('current')
lldpXdcbxFeatPgBwAllocTable = MibTable((1, 0, 8802, 1, 1, 2, 1, 5, 6945, 2, 2, 3), )
if mibBuilder.loadTexts: lldpXdcbxFeatPgBwAllocTable.setStatus('current')
lldpXdcbxFeatPgBwAllocEntry = MibTableRow((1, 0, 8802, 1, 1, 2, 1, 5, 6945, 2, 2, 3, 1), ).setIndexNames((0, "LLDP-EXT-DCBX-MIB", "lldpXdcbxPortNumber"), (0, "LLDP-EXT-DCBX-MIB", "lldpXdcbxFeatPgBwAllocPgId"))
if mibBuilder.loadTexts: lldpXdcbxFeatPgBwAllocEntry.setStatus('current')
lldpXdcbxFeatPgBwAllocPgId = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 6945, 2, 2, 3, 1, 1), LldpXdcbxPriorityGroup()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lldpXdcbxFeatPgBwAllocPgId.setStatus('current')
lldpXdcbxFeatPgBwAllocBwDesired = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 6945, 2, 2, 3, 1, 2), LldpXdcbxPgBw()).setUnits('percent').setMaxAccess("readwrite")
if mibBuilder.loadTexts: lldpXdcbxFeatPgBwAllocBwDesired.setStatus('current')
lldpXdcbxFeatPgBwAllocBwOper = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 6945, 2, 2, 3, 1, 3), LldpXdcbxPgBw()).setUnits('percent').setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXdcbxFeatPgBwAllocBwOper.setStatus('current')
lldpXdcbxFeatPgBwAllocBwPeer = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 6945, 2, 2, 3, 1, 4), LldpXdcbxPgBw()).setUnits('percent').setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXdcbxFeatPgBwAllocBwPeer.setStatus('current')
lldpXdcbxFeatPfc = MibIdentifier((1, 0, 8802, 1, 1, 2, 1, 5, 6945, 2, 3))
lldpXdcbxFeatPfcNumTCPFCSupported = MibScalar((1, 0, 8802, 1, 1, 2, 1, 5, 6945, 2, 3, 1), LldpXdcbxTCPFC()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lldpXdcbxFeatPfcNumTCPFCSupported.setStatus('current')
lldpXdcbxFeatPfcTable = MibTable((1, 0, 8802, 1, 1, 2, 1, 5, 6945, 2, 3, 2), )
if mibBuilder.loadTexts: lldpXdcbxFeatPfcTable.setStatus('current')
lldpXdcbxFeatPfcEntry = MibTableRow((1, 0, 8802, 1, 1, 2, 1, 5, 6945, 2, 3, 2, 1), ).setIndexNames((0, "LLDP-EXT-DCBX-MIB", "lldpXdcbxPortNumber"), (0, "LLDP-EXT-DCBX-MIB", "lldpXdcbxFeatPfcPriority"))
if mibBuilder.loadTexts: lldpXdcbxFeatPfcEntry.setStatus('current')
lldpXdcbxFeatPfcPriority = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 6945, 2, 3, 2, 1, 1), LldpXdcbxPriority()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lldpXdcbxFeatPfcPriority.setStatus('current')
lldpXdcbxFeatPfcEnableDesired = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 6945, 2, 3, 2, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lldpXdcbxFeatPfcEnableDesired.setStatus('current')
lldpXdcbxFeatPfcEnableOper = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 6945, 2, 3, 2, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXdcbxFeatPfcEnableOper.setStatus('current')
lldpXdcbxFeatPfcEnablePeer = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 6945, 2, 3, 2, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXdcbxFeatPfcEnablePeer.setStatus('current')
lldpXdcbxFeatAppProto = MibIdentifier((1, 0, 8802, 1, 1, 2, 1, 5, 6945, 2, 4))
lldpXdcbxFeatAppProtoTable = MibTable((1, 0, 8802, 1, 1, 2, 1, 5, 6945, 2, 4, 1), )
if mibBuilder.loadTexts: lldpXdcbxFeatAppProtoTable.setStatus('current')
lldpXdcbxFeatAppProtoEntry = MibTableRow((1, 0, 8802, 1, 1, 2, 1, 5, 6945, 2, 4, 1, 1), ).setIndexNames((0, "LLDP-EXT-DCBX-MIB", "lldpXdcbxPortNumber"), (0, "LLDP-EXT-DCBX-MIB", "lldpXdcbxFeatAppProtoIndex"))
if mibBuilder.loadTexts: lldpXdcbxFeatAppProtoEntry.setStatus('current')
lldpXdcbxFeatAppProtoIndex = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 6945, 2, 4, 1, 1, 1), LldpXdcbxAppProtos()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lldpXdcbxFeatAppProtoIndex.setStatus('current')
lldpXdcbxFeatAppProtoSF = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 6945, 2, 4, 1, 1, 2), LldpXdcbxSF()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lldpXdcbxFeatAppProtoSF.setStatus('current')
lldpXdcbxFeatAppProtoOUI = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 6945, 2, 4, 1, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lldpXdcbxFeatAppProtoOUI.setStatus('current')
lldpXdcbxFeatAppProtoId = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 6945, 2, 4, 1, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lldpXdcbxFeatAppProtoId.setStatus('current')
lldpXdcbxFeatAppProtoPrioTable = MibTable((1, 0, 8802, 1, 1, 2, 1, 5, 6945, 2, 4, 2), )
if mibBuilder.loadTexts: lldpXdcbxFeatAppProtoPrioTable.setStatus('current')
lldpXdcbxFeatAppProtoPrioEntry = MibTableRow((1, 0, 8802, 1, 1, 2, 1, 5, 6945, 2, 4, 2, 1), ).setIndexNames((0, "LLDP-EXT-DCBX-MIB", "lldpXdcbxPortNumber"), (0, "LLDP-EXT-DCBX-MIB", "lldpXdcbxFeatAppProtoIndex"), (0, "LLDP-EXT-DCBX-MIB", "lldpXdcbxFeatAppProtoPriority"))
if mibBuilder.loadTexts: lldpXdcbxFeatAppProtoPrioEntry.setStatus('current')
lldpXdcbxFeatAppProtoPriority = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 6945, 2, 4, 2, 1, 1), LldpXdcbxPriority()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lldpXdcbxFeatAppProtoPriority.setStatus('current')
lldpXdcbxFeatAppProtoEnableDesired = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 6945, 2, 4, 2, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lldpXdcbxFeatAppProtoEnableDesired.setStatus('current')
lldpXdcbxFeatAppProtoEnableOper = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 6945, 2, 4, 2, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXdcbxFeatAppProtoEnableOper.setStatus('current')
lldpXdcbxFeatAppProtoEnablePeer = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 6945, 2, 4, 2, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXdcbxFeatAppProtoEnablePeer.setStatus('current')
lldpXdcbxMiscControlError = NotificationType((1, 0, 8802, 1, 1, 2, 1, 5, 6945, 0, 1)).setObjects(("LLDP-EXT-DCBX-MIB", "lldpXdcbxPortNumber"))
if mibBuilder.loadTexts: lldpXdcbxMiscControlError.setStatus('current')
lldpXdcbxMiscFeatureError = NotificationType((1, 0, 8802, 1, 1, 2, 1, 5, 6945, 0, 2)).setObjects(("LLDP-EXT-DCBX-MIB", "lldpXdcbxFeatError"))
if mibBuilder.loadTexts: lldpXdcbxMiscFeatureError.setStatus('current')
lldpXdcbxMultiplePeers = NotificationType((1, 0, 8802, 1, 1, 2, 1, 5, 6945, 0, 3)).setObjects(("LLDP-EXT-DCBX-MIB", "lldpXdcbxPortNumber"))
if mibBuilder.loadTexts: lldpXdcbxMultiplePeers.setStatus('current')
lldpXdcbxLldpTxDisabled = NotificationType((1, 0, 8802, 1, 1, 2, 1, 5, 6945, 0, 4)).setObjects(("LLDP-EXT-DCBX-MIB", "lldpXdcbxPortNumber"))
if mibBuilder.loadTexts: lldpXdcbxLldpTxDisabled.setStatus('current')
lldpXdcbxLldpRxDisabled = NotificationType((1, 0, 8802, 1, 1, 2, 1, 5, 6945, 0, 5)).setObjects(("LLDP-EXT-DCBX-MIB", "lldpXdcbxPortNumber"))
if mibBuilder.loadTexts: lldpXdcbxLldpRxDisabled.setStatus('current')
lldpXdcbxDupControlTlv = NotificationType((1, 0, 8802, 1, 1, 2, 1, 5, 6945, 0, 6)).setObjects(("LLDP-EXT-DCBX-MIB", "lldpXdcbxPortNumber"))
if mibBuilder.loadTexts: lldpXdcbxDupControlTlv.setStatus('current')
lldpXdcbxDupFeatureTlv = NotificationType((1, 0, 8802, 1, 1, 2, 1, 5, 6945, 0, 7)).setObjects(("LLDP-EXT-DCBX-MIB", "lldpXdcbxFeatType"))
if mibBuilder.loadTexts: lldpXdcbxDupFeatureTlv.setStatus('current')
lldpXdcbxPeerNoFeat = NotificationType((1, 0, 8802, 1, 1, 2, 1, 5, 6945, 0, 8)).setObjects(("LLDP-EXT-DCBX-MIB", "lldpXdcbxFeatType"))
if mibBuilder.loadTexts: lldpXdcbxPeerNoFeat.setStatus('current')
lldpXdcbxPeerNoResp = NotificationType((1, 0, 8802, 1, 1, 2, 1, 5, 6945, 0, 9)).setObjects(("LLDP-EXT-DCBX-MIB", "lldpXdcbxPortNumber"))
if mibBuilder.loadTexts: lldpXdcbxPeerNoResp.setStatus('current')
lldpXdcbxPeerConfigMismatch = NotificationType((1, 0, 8802, 1, 1, 2, 1, 5, 6945, 0, 10)).setObjects(("LLDP-EXT-DCBX-MIB", "lldpXdcbxPortNumber"))
if mibBuilder.loadTexts: lldpXdcbxPeerConfigMismatch.setStatus('current')
mibBuilder.exportSymbols("LLDP-EXT-DCBX-MIB", lldpXdcbxDupControlTlv=lldpXdcbxDupControlTlv, lldpXdcbxFeatType=lldpXdcbxFeatType, lldpXdcbxFeatPfcEnableDesired=lldpXdcbxFeatPfcEnableDesired, lldpXdcbxObjects=lldpXdcbxObjects, lldpXdcbxFeatPeerAdvertise=lldpXdcbxFeatPeerAdvertise, lldpXdcbxMultiplePeers=lldpXdcbxMultiplePeers, lldpXdcbxFeatVersionMax=lldpXdcbxFeatVersionMax, lldpXdcbxFeatPgBwAllocBwPeer=lldpXdcbxFeatPgBwAllocBwPeer, lldpXdcbxFeatPgPrioAllocPgIdPeer=lldpXdcbxFeatPgPrioAllocPgIdPeer, lldpXdcbxFeatPgPrioAllocPgIdOper=lldpXdcbxFeatPgPrioAllocPgIdOper, LldpXdcbxTCPeer=LldpXdcbxTCPeer, LldpXdcbxPgBw=LldpXdcbxPgBw, lldpXdcbxFeatAppProtoTable=lldpXdcbxFeatAppProtoTable, lldpXdcbxFeatEntry=lldpXdcbxFeatEntry, lldpXdcbxFeatPgBwAllocBwDesired=lldpXdcbxFeatPgBwAllocBwDesired, lldpXdcbxFeatAppProtoPrioTable=lldpXdcbxFeatAppProtoPrioTable, LldpXdcbxFeatureType=LldpXdcbxFeatureType, lldpXdcbxFeatPgPrioAllocEntry=lldpXdcbxFeatPgPrioAllocEntry, lldpXdcbxFeatAppProtoEnableDesired=lldpXdcbxFeatAppProtoEnableDesired, lldpXdcbxMiscControlError=lldpXdcbxMiscControlError, lldpXdcbxFeatPgPrioAllocPrioId=lldpXdcbxFeatPgPrioAllocPrioId, LldpXdcbxFeatureSubType=LldpXdcbxFeatureSubType, lldpXdcbxFeatSubType=lldpXdcbxFeatSubType, lldpXdcbxPortSeqNo=lldpXdcbxPortSeqNo, LldpXdcbxTC=LldpXdcbxTC, lldpXdcbxFeatPfcPriority=lldpXdcbxFeatPfcPriority, LldpXdcbxVersion=LldpXdcbxVersion, lldpXdcbxFeatPgPrioAllocTable=lldpXdcbxFeatPgPrioAllocTable, lldpXdcbxFeatAppProtoEnablePeer=lldpXdcbxFeatAppProtoEnablePeer, lldpXdcbxFeatAppProtoPrioEntry=lldpXdcbxFeatAppProtoPrioEntry, lldpXdcbxPortTable=lldpXdcbxPortTable, LldpXdcbxTCPFC=LldpXdcbxTCPFC, lldpXdcbxFeatPeerEnable=lldpXdcbxFeatPeerEnable, lldpXdcbxFeatPfcNumTCPFCSupported=lldpXdcbxFeatPfcNumTCPFCSupported, lldpXdcbxFeatAppProtoOUI=lldpXdcbxFeatAppProtoOUI, lldpXdcbxFeatSeqNo=lldpXdcbxFeatSeqNo, lldpXdcbxFeatAppProtoEnableOper=lldpXdcbxFeatAppProtoEnableOper, lldpXdcbxFeatPfcEntry=lldpXdcbxFeatPfcEntry, lldpXdcbxNotifications=lldpXdcbxNotifications, lldpXdcbxPortVersionMax=lldpXdcbxPortVersionMax, lldpXdcbxFeatPgBwAllocTable=lldpXdcbxFeatPgBwAllocTable, LldpXdcbxPriorityGroup=LldpXdcbxPriorityGroup, lldpXdcbxPortNumber=lldpXdcbxPortNumber, lldpXdcbxFeatPgBwAllocBwOper=lldpXdcbxFeatPgBwAllocBwOper, LldpXdcbxSF=LldpXdcbxSF, lldpXdcbxFeatPgBwAllocEntry=lldpXdcbxFeatPgBwAllocEntry, lldpXdcbxFeatures=lldpXdcbxFeatures, lldpXdcbxFeatAdvertise=lldpXdcbxFeatAdvertise, lldpXdcbxFeatOperMode=lldpXdcbxFeatOperMode, lldpXdcbxPeerNoResp=lldpXdcbxPeerNoResp, lldpXdcbxFeatLocalParameterChange=lldpXdcbxFeatLocalParameterChange, lldpXdcbxFeatPgPrioAllocPgIdDesired=lldpXdcbxFeatPgPrioAllocPgIdDesired, lldpXdcbxFeatWilling=lldpXdcbxFeatWilling, lldpXdcbxFeatEnable=lldpXdcbxFeatEnable, lldpXdcbxFeatAppProtoPriority=lldpXdcbxFeatAppProtoPriority, lldpXdcbxPeerConfigMismatch=lldpXdcbxPeerConfigMismatch, lldpXdcbxMiscFeatureError=lldpXdcbxMiscFeatureError, lldpXdcbxFeatPgBwAllocPgId=lldpXdcbxFeatPgBwAllocPgId, lldpXdcbxFeatPfc=lldpXdcbxFeatPfc, lldpXdcbxPortEntry=lldpXdcbxPortEntry, lldpXdcbxFeatAppProtoEntry=lldpXdcbxFeatAppProtoEntry, LldpXdcbxPriority=LldpXdcbxPriority, lldpXdcbxPortVersionOper=lldpXdcbxPortVersionOper, lldpXdcbxPeerNoFeat=lldpXdcbxPeerNoFeat, lldpXdcbxFeatPeerError=lldpXdcbxFeatPeerError, lldpXdcbxFeatAppProtoSF=lldpXdcbxFeatAppProtoSF, lldpXdcbxFeatPg=lldpXdcbxFeatPg, lldpXdcbxFeatVersionOper=lldpXdcbxFeatVersionOper, lldpXdcbxFeatAppProtoIndex=lldpXdcbxFeatAppProtoIndex, lldpXdcbxFeatError=lldpXdcbxFeatError, lldpXdcbxPortEnable=lldpXdcbxPortEnable, lldpXdcbxLldpTxDisabled=lldpXdcbxLldpTxDisabled, lldpXdcbxFeatPfcEnablePeer=lldpXdcbxFeatPfcEnablePeer, lldpXdcbxFeatPeerWilling=lldpXdcbxFeatPeerWilling, lldpXdcbxFeatSyncd=lldpXdcbxFeatSyncd, lldpXdcbxFeatPfcTable=lldpXdcbxFeatPfcTable, lldpXdcbxFeatPfcEnableOper=lldpXdcbxFeatPfcEnableOper, LldpXdcbxAppProtos=LldpXdcbxAppProtos, lldpXdcbxFeatAppProto=lldpXdcbxFeatAppProto, lldpXdcbxPortAckNo=lldpXdcbxPortAckNo, PYSNMP_MODULE_ID=lldpXdcbxMIB, lldpXdcbxFeatTable=lldpXdcbxFeatTable, lldpXdcbxFeatPeerTC=lldpXdcbxFeatPeerTC, lldpXdcbxFeatPgNumTCsSupported=lldpXdcbxFeatPgNumTCsSupported, lldpXdcbxFeatAppProtoId=lldpXdcbxFeatAppProtoId, lldpXdcbxLldpRxDisabled=lldpXdcbxLldpRxDisabled, lldpXdcbxDupFeatureTlv=lldpXdcbxDupFeatureTlv, lldpXdcbxMIB=lldpXdcbxMIB)
