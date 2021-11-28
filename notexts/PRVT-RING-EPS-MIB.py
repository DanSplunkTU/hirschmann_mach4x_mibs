#
# PySNMP MIB module PRVT-RING-EPS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/telco-systems/binos/PRVT-RING-EPS-MIB
# Produced by pysmi-1.1.3 at Sun Nov 28 20:26:40 2021
# On host fv-az77-612 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
Dot1agCfmMepIdOrZero, Dot1agCfmMDLevelOrNone = mibBuilder.importSymbols("IEEE8021-CFM-MIB", "Dot1agCfmMepIdOrZero", "Dot1agCfmMDLevelOrNone")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
switch, = mibBuilder.importSymbols("PRVT-SWITCH-MIB", "switch")
VlanIdOrNone, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanIdOrNone")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
NotificationType, Gauge32, TimeTicks, Integer32, Bits, Counter64, Unsigned32, iso, MibIdentifier, ObjectIdentity, ModuleIdentity, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Gauge32", "TimeTicks", "Integer32", "Bits", "Counter64", "Unsigned32", "iso", "MibIdentifier", "ObjectIdentity", "ModuleIdentity", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress")
TextualConvention, DisplayString, MacAddress, RowStatus, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "MacAddress", "RowStatus", "TruthValue")
prvtRingEpsMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 738, 1, 5, 134))
prvtRingEpsMib.setRevisions(('2013-02-22 00:00', '2011-03-11 00:00', '2010-12-17 00:00', '2010-03-16 00:00', '2010-02-02 00:00', '2009-11-04 00:00',))
if mibBuilder.loadTexts: prvtRingEpsMib.setLastUpdated('201003160000Z')
if mibBuilder.loadTexts: prvtRingEpsMib.setOrganization('BATM Advanced Communication')
prvtRingEpsNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 0))
prvtRingEpsObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1))
prvtRingEpsConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 2))
prvtRingEpsInstances = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 1))
prvtRingEpsVlans = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 2))
prvtRingEpsSubRings = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 3))
class PrvtRingEpsModeType(TextualConvention, Integer32):
    reference = 'G.8032v2 clause 10.1.13'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("rapsMode8032v1", 1), ("rapsMode8032v2", 2))

class PrvtRingEpsStateType(TextualConvention, Integer32):
    reference = 'G.8032v2 clause 10.1.2'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("rapsInit", 0), ("rapsIdle", 1), ("rapsProtection", 2), ("rapsManualSwitch", 3), ("rapsForcedSwitch", 4), ("rapsPending", 5))

class PrvtRingEpsLocalCommandType(TextualConvention, Integer32):
    reference = 'G.8032v2 clause 8'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("rapsLcNoRequest", 0), ("rapsLcExercise", 1), ("rapsLcManualSwitch", 2), ("rapsLcSignalDegrade", 3), ("rapsLcSignalFail", 4), ("rapsLcForcedSwitch", 5), ("rapsLcClear", 6), ("rapsLcLockoutOfProtection", 7))

class PrvtRingEpsRemoteRequestType(TextualConvention, Integer32):
    reference = 'G.8032v2 clause 10.3'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(-1, 0, 7, 11, 13, 14))
    namedValues = NamedValues(("rapsRsNone", -1), ("rapsRsNoRequest", 0), ("rapsRsManualSwitch", 7), ("rapsRsSignalFail", 11), ("rapsRsForcedSwitch", 13), ("rapsRsEvent", 14))

class PrvtRingEpsNodeRoleType(TextualConvention, Integer32):
    reference = 'G.8032v2'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("rapsNrSimpleNode", 0), ("rapsNrRplNeighborNode", 1), ("rapsNrRplOwner", 2))

class PrvtRingEpsRplPortType(TextualConvention, Integer32):
    reference = 'G.8032v2'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("port0", 0), ("port1", 1), ("none", 2))

class PrvtRingEpsDefectType(TextualConvention, Bits):
    reference = 'G.8032v2 10.4'
    status = 'current'
    namedValues = NamedValues(("rapsDprovisioningMismatch", 0))

class PrvtRingEpsPortStatusType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("rapsPsOk", 0), ("rapsPsBlocked", 1), ("rapsPsFailed", 2))

class PrvtRingEpsPeerStatusType(TextualConvention, Bits):
    reference = 'ITU-T G.8032v2 clause 10.3'
    status = 'current'
    namedValues = NamedValues(("bRplBlocked", 0), ("bDoNotFlush", 1), ("bBlockedPortReference", 2))

prvtRingEpsInstanceTable = MibTable((1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 1, 1), )
if mibBuilder.loadTexts: prvtRingEpsInstanceTable.setStatus('current')
prvtRingEpsInstanceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 1, 1, 1), ).setIndexNames((0, "PRVT-RING-EPS-MIB", "prvtRingEpsInstanceIndex"))
if mibBuilder.loadTexts: prvtRingEpsInstanceEntry.setStatus('current')
prvtRingEpsInstanceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 10)))
if mibBuilder.loadTexts: prvtRingEpsInstanceIndex.setStatus('current')
prvtRingEpsMode = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 1, 1, 1, 2), PrvtRingEpsModeType().clone('rapsMode8032v2')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRingEpsMode.setStatus('current')
prvtRingEpsNodeRole = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 1, 1, 1, 3), PrvtRingEpsNodeRoleType().clone('rapsNrSimpleNode')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRingEpsNodeRole.setStatus('current')
prvtRingEpsState = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 1, 1, 1, 4), PrvtRingEpsStateType().clone('rapsInit')).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtRingEpsState.setStatus('current')
prvtRingEpsLocalCommand = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 1, 1, 1, 5), PrvtRingEpsLocalCommandType().clone('rapsLcNoRequest')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRingEpsLocalCommand.setStatus('current')
prvtRingEpsControlVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 1, 1, 1, 6), VlanIdOrNone()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRingEpsControlVlan.setStatus('current')
prvtRingEpsPort0Ifindex = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 1, 1, 1, 7), InterfaceIndexOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRingEpsPort0Ifindex.setStatus('current')
prvtRingEpsPort1Ifindex = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 1, 1, 1, 8), InterfaceIndexOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRingEpsPort1Ifindex.setStatus('current')
prvtRingEpsRplPort = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 1, 1, 1, 9), PrvtRingEpsRplPortType().clone('none')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRingEpsRplPort.setStatus('current')
prvtRingEpsManualSwitchPort = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 1, 1, 1, 10), PrvtRingEpsRplPortType().clone('none')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRingEpsManualSwitchPort.setStatus('current')
prvtRingEpsCfmMdLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 1, 1, 1, 11), Dot1agCfmMDLevelOrNone().clone(-1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRingEpsCfmMdLevel.setStatus('current')
prvtRingEpsPort0Mep = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 1, 1, 1, 12), Dot1agCfmMepIdOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRingEpsPort0Mep.setStatus('current')
prvtRingEpsPort1Mep = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 1, 1, 1, 13), Dot1agCfmMepIdOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRingEpsPort1Mep.setStatus('current')
prvtRingEpsRevertive = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 1, 1, 1, 14), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRingEpsRevertive.setStatus('current')
prvtRingEpsNoVirtualChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 1, 1, 1, 15), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRingEpsNoVirtualChannel.setStatus('current')
prvtRingEpsHoldOffTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 1, 1, 1, 16), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 10000))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRingEpsHoldOffTimer.setStatus('current')
prvtRingEpsWaitToRestoreTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 1, 1, 1, 17), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 12)).clone(5)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRingEpsWaitToRestoreTimer.setStatus('current')
prvtRingEpsGuardTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 1, 1, 1, 18), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(10, 2000)).clone(500)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRingEpsGuardTimer.setStatus('current')
prvtRingEpsWaitToBlockTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 1, 1, 1, 19), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(5010, 7000)).clone(5500)).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtRingEpsWaitToBlockTimer.setStatus('current')
prvtRingEpsDefectFop = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 1, 1, 1, 20), PrvtRingEpsDefectType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtRingEpsDefectFop.setStatus('current')
prvtRingEpsPort0Status = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 1, 1, 1, 21), PrvtRingEpsPortStatusType().clone('rapsPsFailed')).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtRingEpsPort0Status.setStatus('current')
prvtRingEpsPort1Status = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 1, 1, 1, 22), PrvtRingEpsPortStatusType().clone('rapsPsFailed')).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtRingEpsPort1Status.setStatus('current')
prvtRingEpsPort0PeerNodeId = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 1, 1, 1, 23), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtRingEpsPort0PeerNodeId.setStatus('current')
prvtRingEpsPort1PeerNodeId = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 1, 1, 1, 24), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtRingEpsPort1PeerNodeId.setStatus('current')
prvtRingEpsPort0PeerCommand = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 1, 1, 1, 25), PrvtRingEpsRemoteRequestType().clone('rapsRsNone')).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtRingEpsPort0PeerCommand.setStatus('current')
prvtRingEpsPort1PeerCommand = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 1, 1, 1, 26), PrvtRingEpsRemoteRequestType().clone('rapsRsNone')).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtRingEpsPort1PeerCommand.setStatus('current')
prvtRingEpsPort0PeerStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 1, 1, 1, 27), PrvtRingEpsPeerStatusType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtRingEpsPort0PeerStatus.setStatus('current')
prvtRingEpsPort1PeerStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 1, 1, 1, 28), PrvtRingEpsPeerStatusType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtRingEpsPort1PeerStatus.setStatus('current')
prvtRingEpsOperationalStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 1, 1, 1, 29), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtRingEpsOperationalStatus.setStatus('current')
prvtRingEpsAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 1, 1, 1, 30), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRingEpsAdminStatus.setStatus('current')
prvtRingEpsRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 1, 1, 1, 31), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRingEpsRowStatus.setStatus('current')
prvtRingEpsForcedSwitchPort = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 1, 1, 1, 32), PrvtRingEpsRplPortType().clone('none')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRingEpsForcedSwitchPort.setStatus('current')
prvtRingEpsInstanceDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 1, 1, 1, 33), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRingEpsInstanceDescription.setStatus('current')
prvtRingEpsRingId = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 1, 1, 1, 34), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRingEpsRingId.setStatus('current')
prvtRingEpsPort0MonitoringMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 1, 1, 1, 35), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ccm", 1), ("link-status", 2))).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtRingEpsPort0MonitoringMethod.setStatus('current')
prvtRingEpsPort1MonitoringMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 1, 1, 1, 36), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ccm", 1), ("link-status", 2))).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtRingEpsPort1MonitoringMethod.setStatus('current')
prvtRingEpsVlanTable = MibTable((1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 2, 1), )
if mibBuilder.loadTexts: prvtRingEpsVlanTable.setStatus('current')
prvtRingEpsVlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 2, 1, 1), ).setIndexNames((0, "PRVT-RING-EPS-MIB", "prvtRingEpsVlanIndex"))
if mibBuilder.loadTexts: prvtRingEpsVlanEntry.setStatus('current')
prvtRingEpsVlanIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 2, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094)))
if mibBuilder.loadTexts: prvtRingEpsVlanIndex.setStatus('current')
prvtRingEpsInstance = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 2, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 10))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRingEpsInstance.setStatus('current')
prvtRingEpsVlanRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 2, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRingEpsVlanRowStatus.setStatus('current')
prvtRingEpsSubRingTable = MibTable((1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 3, 1), )
if mibBuilder.loadTexts: prvtRingEpsSubRingTable.setStatus('current')
prvtRingEpsSubRingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 3, 1, 1), ).setIndexNames((0, "PRVT-RING-EPS-MIB", "prvtRingEpsInstanceIndex"), (0, "PRVT-RING-EPS-MIB", "prvtRingEpsSubRingIndex"))
if mibBuilder.loadTexts: prvtRingEpsSubRingEntry.setStatus('current')
prvtRingEpsSubRingIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 3, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 10)))
if mibBuilder.loadTexts: prvtRingEpsSubRingIndex.setStatus('current')
prvtRingEpsSubRingNodeRole = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 3, 1, 1, 2), PrvtRingEpsNodeRoleType().clone('rapsNrSimpleNode')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRingEpsSubRingNodeRole.setStatus('current')
prvtRingEpsSubRingState = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 3, 1, 1, 3), PrvtRingEpsStateType().clone('rapsInit')).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtRingEpsSubRingState.setStatus('current')
prvtRingEpsSubRingLocalCommand = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 3, 1, 1, 4), PrvtRingEpsLocalCommandType().clone('rapsLcNoRequest')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRingEpsSubRingLocalCommand.setStatus('current')
prvtRingEpsSubRingPortIfindex = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 3, 1, 1, 5), InterfaceIndexOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRingEpsSubRingPortIfindex.setStatus('current')
prvtRingEpsSubRingPortMep = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 3, 1, 1, 6), Dot1agCfmMepIdOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRingEpsSubRingPortMep.setStatus('current')
prvtRingEpsSubRingRplPort = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 3, 1, 1, 7), PrvtRingEpsRplPortType().clone('none')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRingEpsSubRingRplPort.setStatus('current')
prvtRingEpsSubRingVirtualChannelVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 3, 1, 1, 8), VlanIdOrNone()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRingEpsSubRingVirtualChannelVlan.setStatus('current')
prvtRingEpsSubRingRevertive = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 3, 1, 1, 9), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRingEpsSubRingRevertive.setStatus('current')
prvtRingEpsSubRingHoldOffTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 3, 1, 1, 10), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 10000))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRingEpsSubRingHoldOffTimer.setStatus('current')
prvtRingEpsSubRingWaitToRestoreTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 3, 1, 1, 11), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 12)).clone(5)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRingEpsSubRingWaitToRestoreTimer.setStatus('current')
prvtRingEpsSubRingGuardTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 3, 1, 1, 12), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(10, 2000)).clone(500)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRingEpsSubRingGuardTimer.setStatus('current')
prvtRingEpsSubRingWaitToBlockTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 3, 1, 1, 13), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(5010, 7000)).clone(5500)).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtRingEpsSubRingWaitToBlockTimer.setStatus('current')
prvtRingEpsSubRingDefectFop = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 3, 1, 1, 14), PrvtRingEpsDefectType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtRingEpsSubRingDefectFop.setStatus('current')
prvtRingEpsSubRingPortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 3, 1, 1, 15), PrvtRingEpsPortStatusType().clone('rapsPsFailed')).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtRingEpsSubRingPortStatus.setStatus('current')
prvtRingEpsSubRingPortPeerNodeId = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 3, 1, 1, 16), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtRingEpsSubRingPortPeerNodeId.setStatus('current')
prvtRingEpsSubRingPeerCommand = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 3, 1, 1, 17), PrvtRingEpsRemoteRequestType().clone('rapsRsNone')).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtRingEpsSubRingPeerCommand.setStatus('current')
prvtRingEpsSubRingPeerStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 3, 1, 1, 18), PrvtRingEpsPeerStatusType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtRingEpsSubRingPeerStatus.setStatus('current')
prvtRingEpsSubRingVcPeerNodeId = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 3, 1, 1, 19), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtRingEpsSubRingVcPeerNodeId.setStatus('current')
prvtRingEpsSubRingVcPeerCommand = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 3, 1, 1, 20), PrvtRingEpsRemoteRequestType().clone('rapsRsNone')).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtRingEpsSubRingVcPeerCommand.setStatus('current')
prvtRingEpsSubRingVcPeerStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 3, 1, 1, 21), PrvtRingEpsPeerStatusType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtRingEpsSubRingVcPeerStatus.setStatus('current')
prvtRingEpsSubRingPropagateTC = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 3, 1, 1, 22), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRingEpsSubRingPropagateTC.setStatus('current')
prvtRingEpsSubRingOperationalStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 3, 1, 1, 23), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtRingEpsSubRingOperationalStatus.setStatus('current')
prvtRingEpsSubRingAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 3, 1, 1, 24), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRingEpsSubRingAdminStatus.setStatus('current')
prvtRingEpsSubRingRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 3, 1, 1, 25), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRingEpsSubRingRowStatus.setStatus('current')
prvtRingEpsSubRingControlVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 3, 1, 1, 26), VlanIdOrNone()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRingEpsSubRingControlVlan.setStatus('current')
prvtRingEpsSubRingDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 3, 1, 1, 27), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRingEpsSubRingDescription.setStatus('current')
prvtRingEpsSubRingRingId = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 3, 1, 1, 28), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRingEpsSubRingRingId.setStatus('current')
prvtRingEpsSubRingMonitoringMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 3, 1, 1, 29), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ccm", 1), ("link-status", 2))).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtRingEpsSubRingMonitoringMethod.setStatus('current')
prvtRingEpsDefectAlarm = NotificationType((1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 0, 1)).setObjects(("PRVT-RING-EPS-MIB", "prvtRingEpsOperationalStatus"), ("PRVT-RING-EPS-MIB", "prvtRingEpsDefectFop"))
if mibBuilder.loadTexts: prvtRingEpsDefectAlarm.setStatus('current')
prvtRingEpsSwitchoverAlarm = NotificationType((1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 0, 2)).setObjects(("PRVT-RING-EPS-MIB", "prvtRingEpsState"))
if mibBuilder.loadTexts: prvtRingEpsSwitchoverAlarm.setStatus('current')
prvtRingEpsSubRingDefectAlarm = NotificationType((1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 0, 3)).setObjects(("PRVT-RING-EPS-MIB", "prvtRingEpsSubRingOperationalStatus"), ("PRVT-RING-EPS-MIB", "prvtRingEpsSubRingDefectFop"))
if mibBuilder.loadTexts: prvtRingEpsSubRingDefectAlarm.setStatus('current')
prvtRingEpsSubRingSwitchoverAlarm = NotificationType((1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 0, 4)).setObjects(("PRVT-RING-EPS-MIB", "prvtRingEpsSubRingState"))
if mibBuilder.loadTexts: prvtRingEpsSubRingSwitchoverAlarm.setStatus('current')
prvtRingEpsCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 2, 1))
prvtRingEpsGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 2, 2))
prvtRingEpsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 2, 2, 1)).setObjects(("PRVT-RING-EPS-MIB", "prvtRingEpsMode"), ("PRVT-RING-EPS-MIB", "prvtRingEpsNodeRole"), ("PRVT-RING-EPS-MIB", "prvtRingEpsState"), ("PRVT-RING-EPS-MIB", "prvtRingEpsLocalCommand"), ("PRVT-RING-EPS-MIB", "prvtRingEpsControlVlan"), ("PRVT-RING-EPS-MIB", "prvtRingEpsPort0Ifindex"), ("PRVT-RING-EPS-MIB", "prvtRingEpsPort1Ifindex"), ("PRVT-RING-EPS-MIB", "prvtRingEpsRplPort"), ("PRVT-RING-EPS-MIB", "prvtRingEpsManualSwitchPort"), ("PRVT-RING-EPS-MIB", "prvtRingEpsCfmMdLevel"), ("PRVT-RING-EPS-MIB", "prvtRingEpsPort0Mep"), ("PRVT-RING-EPS-MIB", "prvtRingEpsPort1Mep"), ("PRVT-RING-EPS-MIB", "prvtRingEpsRevertive"), ("PRVT-RING-EPS-MIB", "prvtRingEpsNoVirtualChannel"), ("PRVT-RING-EPS-MIB", "prvtRingEpsHoldOffTimer"), ("PRVT-RING-EPS-MIB", "prvtRingEpsWaitToRestoreTimer"), ("PRVT-RING-EPS-MIB", "prvtRingEpsGuardTimer"), ("PRVT-RING-EPS-MIB", "prvtRingEpsWaitToBlockTimer"), ("PRVT-RING-EPS-MIB", "prvtRingEpsDefectFop"), ("PRVT-RING-EPS-MIB", "prvtRingEpsPort0Status"), ("PRVT-RING-EPS-MIB", "prvtRingEpsPort1Status"), ("PRVT-RING-EPS-MIB", "prvtRingEpsPort0PeerNodeId"), ("PRVT-RING-EPS-MIB", "prvtRingEpsPort1PeerNodeId"), ("PRVT-RING-EPS-MIB", "prvtRingEpsPort0PeerCommand"), ("PRVT-RING-EPS-MIB", "prvtRingEpsPort1PeerCommand"), ("PRVT-RING-EPS-MIB", "prvtRingEpsPort0PeerStatus"), ("PRVT-RING-EPS-MIB", "prvtRingEpsPort1PeerStatus"), ("PRVT-RING-EPS-MIB", "prvtRingEpsOperationalStatus"), ("PRVT-RING-EPS-MIB", "prvtRingEpsAdminStatus"), ("PRVT-RING-EPS-MIB", "prvtRingEpsRowStatus"), ("PRVT-RING-EPS-MIB", "prvtRingEpsForcedSwitchPort"), ("PRVT-RING-EPS-MIB", "prvtRingEpsInstanceDescription"), ("PRVT-RING-EPS-MIB", "prvtRingEpsRingId"), ("PRVT-RING-EPS-MIB", "prvtRingEpsPort0MonitoringMethod"), ("PRVT-RING-EPS-MIB", "prvtRingEpsPort1MonitoringMethod"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    prvtRingEpsGroup = prvtRingEpsGroup.setStatus('current')
prvtRingEpsVlanGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 2, 2, 2)).setObjects(("PRVT-RING-EPS-MIB", "prvtRingEpsInstance"), ("PRVT-RING-EPS-MIB", "prvtRingEpsVlanRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    prvtRingEpsVlanGroup = prvtRingEpsVlanGroup.setStatus('current')
prvtRingEpsSubRingGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 2, 2, 3)).setObjects(("PRVT-RING-EPS-MIB", "prvtRingEpsSubRingNodeRole"), ("PRVT-RING-EPS-MIB", "prvtRingEpsSubRingState"), ("PRVT-RING-EPS-MIB", "prvtRingEpsSubRingLocalCommand"), ("PRVT-RING-EPS-MIB", "prvtRingEpsSubRingPortIfindex"), ("PRVT-RING-EPS-MIB", "prvtRingEpsSubRingPortMep"), ("PRVT-RING-EPS-MIB", "prvtRingEpsSubRingRplPort"), ("PRVT-RING-EPS-MIB", "prvtRingEpsSubRingVirtualChannelVlan"), ("PRVT-RING-EPS-MIB", "prvtRingEpsSubRingRevertive"), ("PRVT-RING-EPS-MIB", "prvtRingEpsSubRingHoldOffTimer"), ("PRVT-RING-EPS-MIB", "prvtRingEpsSubRingWaitToRestoreTimer"), ("PRVT-RING-EPS-MIB", "prvtRingEpsSubRingGuardTimer"), ("PRVT-RING-EPS-MIB", "prvtRingEpsSubRingWaitToBlockTimer"), ("PRVT-RING-EPS-MIB", "prvtRingEpsSubRingDefectFop"), ("PRVT-RING-EPS-MIB", "prvtRingEpsSubRingPortStatus"), ("PRVT-RING-EPS-MIB", "prvtRingEpsSubRingPortPeerNodeId"), ("PRVT-RING-EPS-MIB", "prvtRingEpsSubRingPeerCommand"), ("PRVT-RING-EPS-MIB", "prvtRingEpsSubRingPeerStatus"), ("PRVT-RING-EPS-MIB", "prvtRingEpsSubRingVcPeerNodeId"), ("PRVT-RING-EPS-MIB", "prvtRingEpsSubRingVcPeerCommand"), ("PRVT-RING-EPS-MIB", "prvtRingEpsSubRingVcPeerStatus"), ("PRVT-RING-EPS-MIB", "prvtRingEpsSubRingPropagateTC"), ("PRVT-RING-EPS-MIB", "prvtRingEpsSubRingOperationalStatus"), ("PRVT-RING-EPS-MIB", "prvtRingEpsSubRingAdminStatus"), ("PRVT-RING-EPS-MIB", "prvtRingEpsSubRingRowStatus"), ("PRVT-RING-EPS-MIB", "prvtRingEpsSubRingControlVlan"), ("PRVT-RING-EPS-MIB", "prvtRingEpsSubRingDescription"), ("PRVT-RING-EPS-MIB", "prvtRingEpsSubRingRingId"), ("PRVT-RING-EPS-MIB", "prvtRingEpsSubRingMonitoringMethod"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    prvtRingEpsSubRingGroup = prvtRingEpsSubRingGroup.setStatus('current')
prvtRingEpsNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 2, 2, 4)).setObjects(("PRVT-RING-EPS-MIB", "prvtRingEpsSwitchoverAlarm"), ("PRVT-RING-EPS-MIB", "prvtRingEpsDefectAlarm"), ("PRVT-RING-EPS-MIB", "prvtRingEpsSubRingSwitchoverAlarm"), ("PRVT-RING-EPS-MIB", "prvtRingEpsSubRingDefectAlarm"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    prvtRingEpsNotificationsGroup = prvtRingEpsNotificationsGroup.setStatus('current')
prvtRingEpsCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 2, 1, 1)).setObjects(("PRVT-RING-EPS-MIB", "prvtRingEpsGroup"), ("PRVT-RING-EPS-MIB", "prvtRingEpsVlanGroup"), ("PRVT-RING-EPS-MIB", "prvtRingEpsSubRingGroup"), ("PRVT-RING-EPS-MIB", "prvtRingEpsNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    prvtRingEpsCompliance = prvtRingEpsCompliance.setStatus('current')
mibBuilder.exportSymbols("PRVT-RING-EPS-MIB", prvtRingEpsSubRingVcPeerStatus=prvtRingEpsSubRingVcPeerStatus, PrvtRingEpsNodeRoleType=PrvtRingEpsNodeRoleType, prvtRingEpsSubRingPropagateTC=prvtRingEpsSubRingPropagateTC, prvtRingEpsSubRingVcPeerCommand=prvtRingEpsSubRingVcPeerCommand, prvtRingEpsSubRingEntry=prvtRingEpsSubRingEntry, prvtRingEpsSubRingPeerCommand=prvtRingEpsSubRingPeerCommand, prvtRingEpsMode=prvtRingEpsMode, prvtRingEpsSubRingSwitchoverAlarm=prvtRingEpsSubRingSwitchoverAlarm, prvtRingEpsPort1MonitoringMethod=prvtRingEpsPort1MonitoringMethod, prvtRingEpsConformance=prvtRingEpsConformance, prvtRingEpsInstanceEntry=prvtRingEpsInstanceEntry, prvtRingEpsPort0PeerStatus=prvtRingEpsPort0PeerStatus, prvtRingEpsPort0MonitoringMethod=prvtRingEpsPort0MonitoringMethod, prvtRingEpsSubRingAdminStatus=prvtRingEpsSubRingAdminStatus, prvtRingEpsSubRingRevertive=prvtRingEpsSubRingRevertive, prvtRingEpsSubRingLocalCommand=prvtRingEpsSubRingLocalCommand, prvtRingEpsSubRingPortStatus=prvtRingEpsSubRingPortStatus, prvtRingEpsSubRingTable=prvtRingEpsSubRingTable, prvtRingEpsOperationalStatus=prvtRingEpsOperationalStatus, PrvtRingEpsRplPortType=PrvtRingEpsRplPortType, prvtRingEpsNotificationsGroup=prvtRingEpsNotificationsGroup, prvtRingEpsRingId=prvtRingEpsRingId, prvtRingEpsPort0Mep=prvtRingEpsPort0Mep, prvtRingEpsSubRingGuardTimer=prvtRingEpsSubRingGuardTimer, prvtRingEpsGuardTimer=prvtRingEpsGuardTimer, prvtRingEpsVlanRowStatus=prvtRingEpsVlanRowStatus, prvtRingEpsInstanceIndex=prvtRingEpsInstanceIndex, prvtRingEpsInstanceTable=prvtRingEpsInstanceTable, prvtRingEpsPort1PeerCommand=prvtRingEpsPort1PeerCommand, prvtRingEpsGroups=prvtRingEpsGroups, prvtRingEpsWaitToRestoreTimer=prvtRingEpsWaitToRestoreTimer, prvtRingEpsSubRingRplPort=prvtRingEpsSubRingRplPort, PrvtRingEpsPeerStatusType=PrvtRingEpsPeerStatusType, prvtRingEpsSubRingHoldOffTimer=prvtRingEpsSubRingHoldOffTimer, prvtRingEpsDefectAlarm=prvtRingEpsDefectAlarm, prvtRingEpsObjects=prvtRingEpsObjects, prvtRingEpsSubRingDescription=prvtRingEpsSubRingDescription, prvtRingEpsNotifications=prvtRingEpsNotifications, prvtRingEpsCompliance=prvtRingEpsCompliance, prvtRingEpsPort1PeerStatus=prvtRingEpsPort1PeerStatus, prvtRingEpsSubRingRingId=prvtRingEpsSubRingRingId, prvtRingEpsVlanGroup=prvtRingEpsVlanGroup, PrvtRingEpsLocalCommandType=PrvtRingEpsLocalCommandType, prvtRingEpsVlans=prvtRingEpsVlans, prvtRingEpsPort1Mep=prvtRingEpsPort1Mep, prvtRingEpsInstanceDescription=prvtRingEpsInstanceDescription, prvtRingEpsCompliances=prvtRingEpsCompliances, prvtRingEpsVlanEntry=prvtRingEpsVlanEntry, prvtRingEpsAdminStatus=prvtRingEpsAdminStatus, PrvtRingEpsStateType=PrvtRingEpsStateType, prvtRingEpsPort0Ifindex=prvtRingEpsPort0Ifindex, prvtRingEpsState=prvtRingEpsState, prvtRingEpsSubRingPeerStatus=prvtRingEpsSubRingPeerStatus, prvtRingEpsPort1Ifindex=prvtRingEpsPort1Ifindex, prvtRingEpsRowStatus=prvtRingEpsRowStatus, prvtRingEpsSubRingWaitToBlockTimer=prvtRingEpsSubRingWaitToBlockTimer, prvtRingEpsSubRingOperationalStatus=prvtRingEpsSubRingOperationalStatus, prvtRingEpsSubRingRowStatus=prvtRingEpsSubRingRowStatus, PrvtRingEpsModeType=PrvtRingEpsModeType, prvtRingEpsControlVlan=prvtRingEpsControlVlan, prvtRingEpsCfmMdLevel=prvtRingEpsCfmMdLevel, prvtRingEpsSubRingPortMep=prvtRingEpsSubRingPortMep, prvtRingEpsInstance=prvtRingEpsInstance, prvtRingEpsInstances=prvtRingEpsInstances, prvtRingEpsSubRings=prvtRingEpsSubRings, prvtRingEpsSubRingVirtualChannelVlan=prvtRingEpsSubRingVirtualChannelVlan, prvtRingEpsLocalCommand=prvtRingEpsLocalCommand, prvtRingEpsSwitchoverAlarm=prvtRingEpsSwitchoverAlarm, prvtRingEpsSubRingMonitoringMethod=prvtRingEpsSubRingMonitoringMethod, prvtRingEpsPort0PeerCommand=prvtRingEpsPort0PeerCommand, prvtRingEpsMib=prvtRingEpsMib, PrvtRingEpsRemoteRequestType=PrvtRingEpsRemoteRequestType, prvtRingEpsSubRingIndex=prvtRingEpsSubRingIndex, prvtRingEpsPort0PeerNodeId=prvtRingEpsPort0PeerNodeId, prvtRingEpsNoVirtualChannel=prvtRingEpsNoVirtualChannel, prvtRingEpsSubRingControlVlan=prvtRingEpsSubRingControlVlan, prvtRingEpsRevertive=prvtRingEpsRevertive, prvtRingEpsSubRingGroup=prvtRingEpsSubRingGroup, prvtRingEpsSubRingPortPeerNodeId=prvtRingEpsSubRingPortPeerNodeId, PrvtRingEpsDefectType=PrvtRingEpsDefectType, prvtRingEpsRplPort=prvtRingEpsRplPort, prvtRingEpsSubRingPortIfindex=prvtRingEpsSubRingPortIfindex, prvtRingEpsSubRingWaitToRestoreTimer=prvtRingEpsSubRingWaitToRestoreTimer, prvtRingEpsSubRingDefectFop=prvtRingEpsSubRingDefectFop, PYSNMP_MODULE_ID=prvtRingEpsMib, prvtRingEpsSubRingDefectAlarm=prvtRingEpsSubRingDefectAlarm, prvtRingEpsSubRingState=prvtRingEpsSubRingState, prvtRingEpsSubRingVcPeerNodeId=prvtRingEpsSubRingVcPeerNodeId, prvtRingEpsManualSwitchPort=prvtRingEpsManualSwitchPort, prvtRingEpsPort0Status=prvtRingEpsPort0Status, prvtRingEpsVlanIndex=prvtRingEpsVlanIndex, prvtRingEpsSubRingNodeRole=prvtRingEpsSubRingNodeRole, PrvtRingEpsPortStatusType=PrvtRingEpsPortStatusType, prvtRingEpsVlanTable=prvtRingEpsVlanTable, prvtRingEpsNodeRole=prvtRingEpsNodeRole, prvtRingEpsPort1Status=prvtRingEpsPort1Status, prvtRingEpsWaitToBlockTimer=prvtRingEpsWaitToBlockTimer, prvtRingEpsGroup=prvtRingEpsGroup, prvtRingEpsForcedSwitchPort=prvtRingEpsForcedSwitchPort, prvtRingEpsDefectFop=prvtRingEpsDefectFop, prvtRingEpsHoldOffTimer=prvtRingEpsHoldOffTimer, prvtRingEpsPort1PeerNodeId=prvtRingEpsPort1PeerNodeId)
