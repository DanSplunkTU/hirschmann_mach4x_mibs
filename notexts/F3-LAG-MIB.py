#
# PySNMP MIB module F3-LAG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/adva/F3-LAG-MIB
# Produced by pysmi-1.1.8 at Sun Jan 16 00:31:21 2022
# On host fv-az42-839 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
fsp150cm, = mibBuilder.importSymbols("ADVA-MIB", "fsp150cm")
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
CmPmBinAction, = mibBuilder.importSymbols("CM-COMMON-MIB", "CmPmBinAction")
slotIndex, shelfIndex, neIndex = mibBuilder.importSymbols("CM-ENTITY-MIB", "slotIndex", "shelfIndex", "neIndex")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
ObjectIdentity, Integer32, TimeTicks, Counter64, MibIdentifier, Bits, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, IpAddress, Counter32, Unsigned32, ModuleIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Integer32", "TimeTicks", "Counter64", "MibIdentifier", "Bits", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "IpAddress", "Counter32", "Unsigned32", "ModuleIdentity", "iso")
RowStatus, DateAndTime, TruthValue, DisplayString, TextualConvention, StorageType, VariablePointer = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DateAndTime", "TruthValue", "DisplayString", "TextualConvention", "StorageType", "VariablePointer")
f3LagMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2544, 1, 12, 14))
f3LagMIB.setRevisions(('2016-04-06 00:00',))
if mibBuilder.loadTexts: f3LagMIB.setLastUpdated('201604060000Z')
if mibBuilder.loadTexts: f3LagMIB.setOrganization('ADVA Optical Networking')
f3LagObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 14, 1))
f3LagConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 14, 2))
class AggMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("active-standby", 1), ("loadsharing", 2))

class AggPortState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("active", 1), ("standby", 2))

class LagFrameDistributionAlgorithmType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("activeStandby", 1), ("srcdstMacHash", 2), ("serviceAssignment", 3))

class LinkAssignMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("auto", 1), ("provisionedLinkList", 2))

f3LagTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 1, 12, 14, 1, 1), )
if mibBuilder.loadTexts: f3LagTable.setStatus('current')
f3LagEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 1, 12, 14, 1, 1, 1), ).setIndexNames((0, "CM-ENTITY-MIB", "neIndex"), (0, "F3-LAG-MIB", "f3LagIndex"))
if mibBuilder.loadTexts: f3LagEntry.setStatus('current')
f3LagIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 14, 1, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: f3LagIndex.setStatus('current')
f3LagIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 14, 1, 1, 1, 2), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3LagIfIndex.setStatus('current')
f3LagName = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 14, 1, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3LagName.setStatus('current')
f3LagProtocols = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 14, 1, 1, 1, 4), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3LagProtocols.setStatus('current')
f3LagLacpControl = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 14, 1, 1, 1, 5), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3LagLacpControl.setStatus('current')
f3LagMode = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 14, 1, 1, 1, 6), AggMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3LagMode.setStatus('current')
f3LagCcmDefectsDetectionEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 14, 1, 1, 1, 7), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3LagCcmDefectsDetectionEnabled.setStatus('current')
f3LagStatsAction = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 14, 1, 1, 1, 8), CmPmBinAction()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3LagStatsAction.setStatus('current')
f3LagStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 14, 1, 1, 1, 9), StorageType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3LagStorageType.setStatus('current')
f3LagRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 14, 1, 1, 1, 10), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3LagRowStatus.setStatus('current')
f3LagIgnorePartnerColMaxDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 14, 1, 1, 1, 11), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3LagIgnorePartnerColMaxDelay.setStatus('current')
f3LagFrameDistAlgorithm = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 14, 1, 1, 1, 12), LagFrameDistributionAlgorithmType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3LagFrameDistAlgorithm.setStatus('current')
f3LagDiscardWrongConversation = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 14, 1, 1, 1, 13), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3LagDiscardWrongConversation.setStatus('current')
f3LagStatsTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 1, 12, 14, 1, 2), )
if mibBuilder.loadTexts: f3LagStatsTable.setStatus('current')
f3LagStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 1, 12, 14, 1, 2, 1), ).setIndexNames((0, "CM-ENTITY-MIB", "neIndex"), (0, "F3-LAG-MIB", "f3LagIndex"), (0, "F3-LAG-MIB", "f3LagStatsIndex"))
if mibBuilder.loadTexts: f3LagStatsEntry.setStatus('current')
f3LagStatsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 14, 1, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: f3LagStatsIndex.setStatus('current')
f3LagStatsOctetsTxOK = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 14, 1, 2, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3LagStatsOctetsTxOK.setStatus('current')
f3LagStatsOctetsRxOK = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 14, 1, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3LagStatsOctetsRxOK.setStatus('current')
f3LagStatsFramesTxOK = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 14, 1, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3LagStatsFramesTxOK.setStatus('current')
f3LagStatsFramesRxOK = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 14, 1, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3LagStatsFramesRxOK.setStatus('current')
f3LagStatsMulticastFramesTxOK = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 14, 1, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3LagStatsMulticastFramesTxOK.setStatus('current')
f3LagStatsMulticastFramesRxOK = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 14, 1, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3LagStatsMulticastFramesRxOK.setStatus('current')
f3LagStatsBroadcastFramesTxOK = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 14, 1, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3LagStatsBroadcastFramesTxOK.setStatus('current')
f3LagStatsBroadcastFramesRxOK = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 14, 1, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3LagStatsBroadcastFramesRxOK.setStatus('current')
f3LagStatsFramesWithTxErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 14, 1, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3LagStatsFramesWithTxErrors.setStatus('current')
f3LagStatsFramesWithRxErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 14, 1, 2, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3LagStatsFramesWithRxErrors.setStatus('current')
f3LagStatsUnknownProtocolFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 14, 1, 2, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3LagStatsUnknownProtocolFrames.setStatus('current')
f3LagPortTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 1, 12, 14, 1, 3), )
if mibBuilder.loadTexts: f3LagPortTable.setStatus('current')
f3LagPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 1, 12, 14, 1, 3, 1), ).setIndexNames((0, "CM-ENTITY-MIB", "neIndex"), (0, "F3-LAG-MIB", "f3LagIndex"), (0, "F3-LAG-MIB", "f3LagPortIndex"))
if mibBuilder.loadTexts: f3LagPortEntry.setStatus('current')
f3LagPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 14, 1, 3, 1, 1), Integer32())
if mibBuilder.loadTexts: f3LagPortIndex.setStatus('current')
f3LagPortMember = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 14, 1, 3, 1, 2), VariablePointer()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3LagPortMember.setStatus('current')
f3LagPortLacpForceOutOfSync = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 14, 1, 3, 1, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3LagPortLacpForceOutOfSync.setStatus('current')
f3LagPortState = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 14, 1, 3, 1, 4), AggPortState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3LagPortState.setStatus('current')
f3LagPortStatsAction = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 14, 1, 3, 1, 5), CmPmBinAction()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3LagPortStatsAction.setStatus('current')
f3LagPortStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 14, 1, 3, 1, 6), StorageType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3LagPortStorageType.setStatus('current')
f3LagPortRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 14, 1, 3, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3LagPortRowStatus.setStatus('current')
f3LagServiceMapTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 1, 12, 14, 1, 4), )
if mibBuilder.loadTexts: f3LagServiceMapTable.setStatus('current')
f3LagServiceMapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 1, 12, 14, 1, 4, 1), ).setIndexNames((0, "CM-ENTITY-MIB", "neIndex"), (0, "F3-LAG-MIB", "f3LagIndex"), (0, "F3-LAG-MIB", "f3LagServiceMapIndex"))
if mibBuilder.loadTexts: f3LagServiceMapEntry.setStatus('current')
f3LagServiceMapIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 14, 1, 4, 1, 1), Integer32())
if mibBuilder.loadTexts: f3LagServiceMapIndex.setStatus('current')
f3LagServiceMapServiceObj = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 14, 1, 4, 1, 2), VariablePointer()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3LagServiceMapServiceObj.setStatus('current')
f3LagServiceMapLinkAssignMode = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 14, 1, 4, 1, 3), LinkAssignMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3LagServiceMapLinkAssignMode.setStatus('current')
f3LagServiceMapStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 14, 1, 4, 1, 4), StorageType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3LagServiceMapStorageType.setStatus('current')
f3LagServiceMapRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 14, 1, 4, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3LagServiceMapRowStatus.setStatus('current')
f3LagServiceMapMemberLinkList = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 14, 1, 4, 1, 6), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3LagServiceMapMemberLinkList.setStatus('current')
f3LagServiceMapCurrentMemberLink = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 14, 1, 4, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3LagServiceMapCurrentMemberLink.setStatus('current')
f3LagCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 14, 2, 1))
f3LagGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 14, 2, 2))
f3LagCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2544, 1, 12, 14, 2, 1, 1)).setObjects(("F3-LAG-MIB", "f3LagObjectGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3LagCompliance = f3LagCompliance.setStatus('current')
f3LagObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2544, 1, 12, 14, 2, 2, 1)).setObjects(("F3-LAG-MIB", "f3LagIndex"), ("F3-LAG-MIB", "f3LagIfIndex"), ("F3-LAG-MIB", "f3LagName"), ("F3-LAG-MIB", "f3LagProtocols"), ("F3-LAG-MIB", "f3LagLacpControl"), ("F3-LAG-MIB", "f3LagMode"), ("F3-LAG-MIB", "f3LagCcmDefectsDetectionEnabled"), ("F3-LAG-MIB", "f3LagStatsAction"), ("F3-LAG-MIB", "f3LagStorageType"), ("F3-LAG-MIB", "f3LagRowStatus"), ("F3-LAG-MIB", "f3LagIgnorePartnerColMaxDelay"), ("F3-LAG-MIB", "f3LagFrameDistAlgorithm"), ("F3-LAG-MIB", "f3LagDiscardWrongConversation"), ("F3-LAG-MIB", "f3LagStatsIndex"), ("F3-LAG-MIB", "f3LagStatsOctetsTxOK"), ("F3-LAG-MIB", "f3LagStatsOctetsRxOK"), ("F3-LAG-MIB", "f3LagStatsFramesTxOK"), ("F3-LAG-MIB", "f3LagStatsFramesRxOK"), ("F3-LAG-MIB", "f3LagStatsMulticastFramesTxOK"), ("F3-LAG-MIB", "f3LagStatsMulticastFramesRxOK"), ("F3-LAG-MIB", "f3LagStatsBroadcastFramesTxOK"), ("F3-LAG-MIB", "f3LagStatsBroadcastFramesRxOK"), ("F3-LAG-MIB", "f3LagStatsFramesWithTxErrors"), ("F3-LAG-MIB", "f3LagStatsFramesWithRxErrors"), ("F3-LAG-MIB", "f3LagStatsUnknownProtocolFrames"), ("F3-LAG-MIB", "f3LagPortIndex"), ("F3-LAG-MIB", "f3LagPortMember"), ("F3-LAG-MIB", "f3LagPortLacpForceOutOfSync"), ("F3-LAG-MIB", "f3LagPortState"), ("F3-LAG-MIB", "f3LagPortStatsAction"), ("F3-LAG-MIB", "f3LagPortStorageType"), ("F3-LAG-MIB", "f3LagPortRowStatus"), ("F3-LAG-MIB", "f3LagServiceMapIndex"), ("F3-LAG-MIB", "f3LagServiceMapServiceObj"), ("F3-LAG-MIB", "f3LagServiceMapLinkAssignMode"), ("F3-LAG-MIB", "f3LagServiceMapStorageType"), ("F3-LAG-MIB", "f3LagServiceMapRowStatus"), ("F3-LAG-MIB", "f3LagServiceMapMemberLinkList"), ("F3-LAG-MIB", "f3LagServiceMapCurrentMemberLink"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3LagObjectGroup = f3LagObjectGroup.setStatus('current')
mibBuilder.exportSymbols("F3-LAG-MIB", f3LagStatsMulticastFramesRxOK=f3LagStatsMulticastFramesRxOK, f3LagName=f3LagName, f3LagStatsEntry=f3LagStatsEntry, f3LagStorageType=f3LagStorageType, f3LagMode=f3LagMode, f3LagStatsBroadcastFramesTxOK=f3LagStatsBroadcastFramesTxOK, f3LagServiceMapTable=f3LagServiceMapTable, f3LagServiceMapStorageType=f3LagServiceMapStorageType, f3LagProtocols=f3LagProtocols, f3LagStatsFramesWithTxErrors=f3LagStatsFramesWithTxErrors, f3LagServiceMapRowStatus=f3LagServiceMapRowStatus, f3LagStatsAction=f3LagStatsAction, f3LagRowStatus=f3LagRowStatus, f3LagStatsBroadcastFramesRxOK=f3LagStatsBroadcastFramesRxOK, f3LagLacpControl=f3LagLacpControl, LinkAssignMode=LinkAssignMode, f3LagPortStatsAction=f3LagPortStatsAction, f3LagGroups=f3LagGroups, f3LagCompliances=f3LagCompliances, f3LagStatsOctetsTxOK=f3LagStatsOctetsTxOK, f3LagObjects=f3LagObjects, LagFrameDistributionAlgorithmType=LagFrameDistributionAlgorithmType, f3LagIfIndex=f3LagIfIndex, f3LagServiceMapEntry=f3LagServiceMapEntry, f3LagPortMember=f3LagPortMember, AggMode=AggMode, PYSNMP_MODULE_ID=f3LagMIB, f3LagPortIndex=f3LagPortIndex, f3LagMIB=f3LagMIB, f3LagStatsTable=f3LagStatsTable, f3LagServiceMapIndex=f3LagServiceMapIndex, f3LagStatsFramesRxOK=f3LagStatsFramesRxOK, f3LagEntry=f3LagEntry, f3LagDiscardWrongConversation=f3LagDiscardWrongConversation, f3LagPortLacpForceOutOfSync=f3LagPortLacpForceOutOfSync, AggPortState=AggPortState, f3LagTable=f3LagTable, f3LagConformance=f3LagConformance, f3LagCompliance=f3LagCompliance, f3LagCcmDefectsDetectionEnabled=f3LagCcmDefectsDetectionEnabled, f3LagStatsFramesWithRxErrors=f3LagStatsFramesWithRxErrors, f3LagPortState=f3LagPortState, f3LagStatsOctetsRxOK=f3LagStatsOctetsRxOK, f3LagIgnorePartnerColMaxDelay=f3LagIgnorePartnerColMaxDelay, f3LagStatsFramesTxOK=f3LagStatsFramesTxOK, f3LagPortTable=f3LagPortTable, f3LagPortEntry=f3LagPortEntry, f3LagIndex=f3LagIndex, f3LagPortStorageType=f3LagPortStorageType, f3LagServiceMapMemberLinkList=f3LagServiceMapMemberLinkList, f3LagServiceMapCurrentMemberLink=f3LagServiceMapCurrentMemberLink, f3LagFrameDistAlgorithm=f3LagFrameDistAlgorithm, f3LagStatsUnknownProtocolFrames=f3LagStatsUnknownProtocolFrames, f3LagServiceMapServiceObj=f3LagServiceMapServiceObj, f3LagServiceMapLinkAssignMode=f3LagServiceMapLinkAssignMode, f3LagStatsMulticastFramesTxOK=f3LagStatsMulticastFramesTxOK, f3LagObjectGroup=f3LagObjectGroup, f3LagStatsIndex=f3LagStatsIndex, f3LagPortRowStatus=f3LagPortRowStatus)
