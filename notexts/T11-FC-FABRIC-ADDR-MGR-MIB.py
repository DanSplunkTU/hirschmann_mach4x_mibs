#
# PySNMP MIB module T11-FC-FABRIC-ADDR-MGR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/T11-FC-FABRIC-ADDR-MGR-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:07:39 2022
# On host fv-az36-988 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
FcDomainIdOrZero, FcNameIdOrZero, fcmSwitchIndex, fcmInstanceIndex = mibBuilder.importSymbols("FC-MGMT-MIB", "FcDomainIdOrZero", "FcNameIdOrZero", "fcmSwitchIndex", "fcmInstanceIndex")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
MibIdentifier, ObjectIdentity, ModuleIdentity, Unsigned32, iso, TimeTicks, Gauge32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, mib_2, Bits, NotificationType, IpAddress, Counter64, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "ObjectIdentity", "ModuleIdentity", "Unsigned32", "iso", "TimeTicks", "Gauge32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "mib-2", "Bits", "NotificationType", "IpAddress", "Counter64", "Counter32")
TextualConvention, TruthValue, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "RowStatus", "DisplayString")
T11FabricIndex, = mibBuilder.importSymbols("T11-TC-MIB", "T11FabricIndex")
t11FcFabricAddrMgrMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 137))
t11FcFabricAddrMgrMIB.setRevisions(('2006-03-02 00:00',))
if mibBuilder.loadTexts: t11FcFabricAddrMgrMIB.setLastUpdated('200603020000Z')
if mibBuilder.loadTexts: t11FcFabricAddrMgrMIB.setOrganization('T11')
t11FamNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 137, 0))
t11FamMIBObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 137, 1))
t11FamMIBConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 137, 2))
t11FamConfiguration = MibIdentifier((1, 3, 6, 1, 2, 1, 137, 1, 1))
t11FamInfo = MibIdentifier((1, 3, 6, 1, 2, 1, 137, 1, 2))
t11FamNotifyControl = MibIdentifier((1, 3, 6, 1, 2, 1, 137, 1, 3))
class T11FamDomainPriority(TextualConvention, Unsigned32):
    reference = 'Fibre Channel - Switch Fabric - 3 (FC-SW-3), ANSI INCITS 384-2004, section 6.1.5.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 255)

class T11FamDomainInterfaceRole(TextualConvention, Integer32):
    reference = 'Fibre Channel - Switch Fabric - 3 (FC-SW-3), ANSI INCITS 384-2004, Sections 3.1, 5.7, and Figure 9.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("nonPrincipal", 1), ("principalUpstream", 2), ("principalDownsteam", 3), ("isolated", 4), ("down", 5), ("unknown", 6))

class T11FamState(TextualConvention, Integer32):
    reference = 'Fibre Channel - Switch Fabric - 3 (FC-SW-3), ANSI INCITS 384-2004, Table 86 and Figure 15.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    namedValues = NamedValues(("other", 1), ("starting", 2), ("unconfigured", 3), ("principalSwitchSelection", 4), ("domainIdDistribution", 5), ("buildFabricPhase", 6), ("reconfigureFabricPhase", 7), ("stable", 8), ("stableWithNoEports", 9), ("noDomains", 10), ("disabled", 11), ("unknown", 12))

t11FamTable = MibTable((1, 3, 6, 1, 2, 1, 137, 1, 1, 1), )
if mibBuilder.loadTexts: t11FamTable.setStatus('current')
t11FamEntry = MibTableRow((1, 3, 6, 1, 2, 1, 137, 1, 1, 1, 1), ).setIndexNames((0, "FC-MGMT-MIB", "fcmInstanceIndex"), (0, "FC-MGMT-MIB", "fcmSwitchIndex"), (0, "T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamFabricIndex"))
if mibBuilder.loadTexts: t11FamEntry.setStatus('current')
t11FamFabricIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 137, 1, 1, 1, 1, 1), T11FabricIndex())
if mibBuilder.loadTexts: t11FamFabricIndex.setStatus('current')
t11FamConfigDomainId = MibTableColumn((1, 3, 6, 1, 2, 1, 137, 1, 1, 1, 1, 2), FcDomainIdOrZero()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: t11FamConfigDomainId.setStatus('current')
t11FamConfigDomainIdType = MibTableColumn((1, 3, 6, 1, 2, 1, 137, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("preferred", 1), ("insistent", 2), ("static", 3))).clone('preferred')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: t11FamConfigDomainIdType.setStatus('current')
t11FamAutoReconfigure = MibTableColumn((1, 3, 6, 1, 2, 1, 137, 1, 1, 1, 1, 4), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: t11FamAutoReconfigure.setStatus('current')
t11FamContiguousAllocation = MibTableColumn((1, 3, 6, 1, 2, 1, 137, 1, 1, 1, 1, 5), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: t11FamContiguousAllocation.setStatus('current')
t11FamPriority = MibTableColumn((1, 3, 6, 1, 2, 1, 137, 1, 1, 1, 1, 6), T11FamDomainPriority()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: t11FamPriority.setStatus('current')
t11FamPrincipalSwitchWwn = MibTableColumn((1, 3, 6, 1, 2, 1, 137, 1, 1, 1, 1, 7), FcNameIdOrZero().clone(hexValue="")).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FamPrincipalSwitchWwn.setStatus('current')
t11FamLocalSwitchWwn = MibTableColumn((1, 3, 6, 1, 2, 1, 137, 1, 1, 1, 1, 8), FcNameIdOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FamLocalSwitchWwn.setStatus('current')
t11FamAssignedAreaIdList = MibTableColumn((1, 3, 6, 1, 2, 1, 137, 1, 1, 1, 1, 9), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FamAssignedAreaIdList.setStatus('current')
t11FamGrantedFcIds = MibTableColumn((1, 3, 6, 1, 2, 1, 137, 1, 1, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FamGrantedFcIds.setStatus('current')
t11FamRecoveredFcIds = MibTableColumn((1, 3, 6, 1, 2, 1, 137, 1, 1, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FamRecoveredFcIds.setStatus('current')
t11FamFreeFcIds = MibTableColumn((1, 3, 6, 1, 2, 1, 137, 1, 1, 1, 1, 12), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FamFreeFcIds.setStatus('current')
t11FamAssignedFcIds = MibTableColumn((1, 3, 6, 1, 2, 1, 137, 1, 1, 1, 1, 13), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FamAssignedFcIds.setStatus('current')
t11FamAvailableFcIds = MibTableColumn((1, 3, 6, 1, 2, 1, 137, 1, 1, 1, 1, 14), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FamAvailableFcIds.setStatus('current')
t11FamRunningPriority = MibTableColumn((1, 3, 6, 1, 2, 1, 137, 1, 1, 1, 1, 15), T11FamDomainPriority()).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FamRunningPriority.setStatus('current')
t11FamPrincSwRunningPriority = MibTableColumn((1, 3, 6, 1, 2, 1, 137, 1, 1, 1, 1, 16), T11FamDomainPriority()).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FamPrincSwRunningPriority.setStatus('current')
t11FamState = MibTableColumn((1, 3, 6, 1, 2, 1, 137, 1, 1, 1, 1, 17), T11FamState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FamState.setStatus('current')
t11FamLocalPrincipalSwitchSlctns = MibTableColumn((1, 3, 6, 1, 2, 1, 137, 1, 1, 1, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FamLocalPrincipalSwitchSlctns.setStatus('current')
t11FamPrincipalSwitchSelections = MibTableColumn((1, 3, 6, 1, 2, 1, 137, 1, 1, 1, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FamPrincipalSwitchSelections.setStatus('current')
t11FamBuildFabrics = MibTableColumn((1, 3, 6, 1, 2, 1, 137, 1, 1, 1, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FamBuildFabrics.setStatus('current')
t11FamFabricReconfigures = MibTableColumn((1, 3, 6, 1, 2, 1, 137, 1, 1, 1, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FamFabricReconfigures.setStatus('current')
t11FamDomainId = MibTableColumn((1, 3, 6, 1, 2, 1, 137, 1, 1, 1, 1, 22), FcDomainIdOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FamDomainId.setStatus('current')
t11FamSticky = MibTableColumn((1, 3, 6, 1, 2, 1, 137, 1, 1, 1, 1, 23), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FamSticky.setStatus('current')
t11FamRestart = MibTableColumn((1, 3, 6, 1, 2, 1, 137, 1, 1, 1, 1, 24), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("nonDisruptive", 1), ("disruptive", 2), ("noOp", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: t11FamRestart.setStatus('current')
t11FamRcFabricNotifyEnable = MibTableColumn((1, 3, 6, 1, 2, 1, 137, 1, 1, 1, 1, 25), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: t11FamRcFabricNotifyEnable.setStatus('current')
t11FamEnable = MibTableColumn((1, 3, 6, 1, 2, 1, 137, 1, 1, 1, 1, 26), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: t11FamEnable.setStatus('current')
t11FamFabricName = MibTableColumn((1, 3, 6, 1, 2, 1, 137, 1, 1, 1, 1, 27), FcNameIdOrZero()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: t11FamFabricName.setStatus('current')
t11FamIfTable = MibTable((1, 3, 6, 1, 2, 1, 137, 1, 1, 2), )
if mibBuilder.loadTexts: t11FamIfTable.setStatus('current')
t11FamIfEntry = MibTableRow((1, 3, 6, 1, 2, 1, 137, 1, 1, 2, 1), ).setIndexNames((0, "FC-MGMT-MIB", "fcmInstanceIndex"), (0, "FC-MGMT-MIB", "fcmSwitchIndex"), (0, "T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamFabricIndex"), (0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: t11FamIfEntry.setStatus('current')
t11FamIfRcfReject = MibTableColumn((1, 3, 6, 1, 2, 1, 137, 1, 1, 2, 1, 1), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: t11FamIfRcfReject.setStatus('current')
t11FamIfRole = MibTableColumn((1, 3, 6, 1, 2, 1, 137, 1, 1, 2, 1, 2), T11FamDomainInterfaceRole()).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FamIfRole.setStatus('current')
t11FamIfRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 137, 1, 1, 2, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: t11FamIfRowStatus.setStatus('current')
t11FamAreaTable = MibTable((1, 3, 6, 1, 2, 1, 137, 1, 2, 1), )
if mibBuilder.loadTexts: t11FamAreaTable.setStatus('current')
t11FamAreaEntry = MibTableRow((1, 3, 6, 1, 2, 1, 137, 1, 2, 1, 1), ).setIndexNames((0, "FC-MGMT-MIB", "fcmInstanceIndex"), (0, "FC-MGMT-MIB", "fcmSwitchIndex"), (0, "T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamFabricIndex"), (0, "T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamAreaAreaId"))
if mibBuilder.loadTexts: t11FamAreaEntry.setStatus('current')
t11FamAreaAreaId = MibTableColumn((1, 3, 6, 1, 2, 1, 137, 1, 2, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)))
if mibBuilder.loadTexts: t11FamAreaAreaId.setStatus('current')
t11FamAreaAssignedPortIdList = MibTableColumn((1, 3, 6, 1, 2, 1, 137, 1, 2, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FamAreaAssignedPortIdList.setStatus('current')
t11FamDatabaseTable = MibTable((1, 3, 6, 1, 2, 1, 137, 1, 2, 2), )
if mibBuilder.loadTexts: t11FamDatabaseTable.setStatus('current')
t11FamDatabaseEntry = MibTableRow((1, 3, 6, 1, 2, 1, 137, 1, 2, 2, 1), ).setIndexNames((0, "FC-MGMT-MIB", "fcmInstanceIndex"), (0, "FC-MGMT-MIB", "fcmSwitchIndex"), (0, "T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamFabricIndex"), (0, "T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamDatabaseDomainId"))
if mibBuilder.loadTexts: t11FamDatabaseEntry.setStatus('current')
t11FamDatabaseDomainId = MibTableColumn((1, 3, 6, 1, 2, 1, 137, 1, 2, 2, 1, 1), FcDomainIdOrZero().subtype(subtypeSpec=ValueRangeConstraint(1, 239)))
if mibBuilder.loadTexts: t11FamDatabaseDomainId.setStatus('current')
t11FamDatabaseSwitchWwn = MibTableColumn((1, 3, 6, 1, 2, 1, 137, 1, 2, 2, 1, 2), FcNameIdOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FamDatabaseSwitchWwn.setStatus('current')
t11FamMaxFcIdCacheSize = MibScalar((1, 3, 6, 1, 2, 1, 137, 1, 2, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FamMaxFcIdCacheSize.setStatus('current')
t11FamFcIdCacheTable = MibTable((1, 3, 6, 1, 2, 1, 137, 1, 2, 4), )
if mibBuilder.loadTexts: t11FamFcIdCacheTable.setStatus('current')
t11FamFcIdCacheEntry = MibTableRow((1, 3, 6, 1, 2, 1, 137, 1, 2, 4, 1), ).setIndexNames((0, "FC-MGMT-MIB", "fcmInstanceIndex"), (0, "FC-MGMT-MIB", "fcmSwitchIndex"), (0, "T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamFabricIndex"), (0, "T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamFcIdCacheWwn"))
if mibBuilder.loadTexts: t11FamFcIdCacheEntry.setStatus('current')
t11FamFcIdCacheWwn = MibTableColumn((1, 3, 6, 1, 2, 1, 137, 1, 2, 4, 1, 1), FcNameIdOrZero())
if mibBuilder.loadTexts: t11FamFcIdCacheWwn.setStatus('current')
t11FamFcIdCacheAreaIdPortId = MibTableColumn((1, 3, 6, 1, 2, 1, 137, 1, 2, 4, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FamFcIdCacheAreaIdPortId.setStatus('current')
t11FamFcIdCachePortIds = MibTableColumn((1, 3, 6, 1, 2, 1, 137, 1, 2, 4, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FamFcIdCachePortIds.setStatus('current')
t11FamNotifyFabricIndex = MibScalar((1, 3, 6, 1, 2, 1, 137, 1, 3, 1), T11FabricIndex()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: t11FamNotifyFabricIndex.setStatus('current')
t11FamDomainIdNotAssignedNotify = NotificationType((1, 3, 6, 1, 2, 1, 137, 0, 1)).setObjects(("T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamLocalSwitchWwn"), ("T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamNotifyFabricIndex"))
if mibBuilder.loadTexts: t11FamDomainIdNotAssignedNotify.setStatus('current')
t11FamNewPrincipalSwitchNotify = NotificationType((1, 3, 6, 1, 2, 1, 137, 0, 2)).setObjects(("T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamLocalSwitchWwn"), ("T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamNotifyFabricIndex"))
if mibBuilder.loadTexts: t11FamNewPrincipalSwitchNotify.setStatus('current')
t11FamFabricChangeNotify = NotificationType((1, 3, 6, 1, 2, 1, 137, 0, 3)).setObjects(("T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamLocalSwitchWwn"), ("T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamNotifyFabricIndex"))
if mibBuilder.loadTexts: t11FamFabricChangeNotify.setStatus('current')
t11FamMIBCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 137, 2, 1))
t11FamMIBGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 137, 2, 2))
t11FamMIBCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 137, 2, 1, 1)).setObjects(("T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamGroup"), ("T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamDatabaseGroup"), ("T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamAreaGroup"), ("T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    t11FamMIBCompliance = t11FamMIBCompliance.setStatus('current')
t11FamGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 137, 2, 2, 1)).setObjects(("T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamConfigDomainId"), ("T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamConfigDomainIdType"), ("T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamAutoReconfigure"), ("T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamContiguousAllocation"), ("T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamPriority"), ("T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamPrincipalSwitchWwn"), ("T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamLocalSwitchWwn"), ("T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamAssignedAreaIdList"), ("T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamGrantedFcIds"), ("T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamRecoveredFcIds"), ("T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamFreeFcIds"), ("T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamAssignedFcIds"), ("T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamAvailableFcIds"), ("T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamRunningPriority"), ("T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamPrincSwRunningPriority"), ("T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamState"), ("T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamLocalPrincipalSwitchSlctns"), ("T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamPrincipalSwitchSelections"), ("T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamBuildFabrics"), ("T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamFabricReconfigures"), ("T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamDomainId"), ("T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamSticky"), ("T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamRestart"), ("T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamRcFabricNotifyEnable"), ("T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamEnable"), ("T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamFabricName"), ("T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamIfRcfReject"), ("T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamIfRole"), ("T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamIfRowStatus"), ("T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamNotifyFabricIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    t11FamGroup = t11FamGroup.setStatus('current')
t11FamCommandGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 137, 2, 2, 2)).setObjects(("T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamRestart"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    t11FamCommandGroup = t11FamCommandGroup.setStatus('current')
t11FamDatabaseGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 137, 2, 2, 3)).setObjects(("T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamDatabaseSwitchWwn"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    t11FamDatabaseGroup = t11FamDatabaseGroup.setStatus('current')
t11FamAreaGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 137, 2, 2, 4)).setObjects(("T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamAreaAssignedPortIdList"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    t11FamAreaGroup = t11FamAreaGroup.setStatus('current')
t11FamCacheGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 137, 2, 2, 5)).setObjects(("T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamMaxFcIdCacheSize"), ("T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamFcIdCacheAreaIdPortId"), ("T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamFcIdCachePortIds"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    t11FamCacheGroup = t11FamCacheGroup.setStatus('current')
t11FamNotificationGroup = NotificationGroup((1, 3, 6, 1, 2, 1, 137, 2, 2, 6)).setObjects(("T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamDomainIdNotAssignedNotify"), ("T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamNewPrincipalSwitchNotify"), ("T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamFabricChangeNotify"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    t11FamNotificationGroup = t11FamNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("T11-FC-FABRIC-ADDR-MGR-MIB", PYSNMP_MODULE_ID=t11FcFabricAddrMgrMIB, t11FamDatabaseEntry=t11FamDatabaseEntry, t11FamFabricReconfigures=t11FamFabricReconfigures, t11FamMaxFcIdCacheSize=t11FamMaxFcIdCacheSize, t11FamEntry=t11FamEntry, t11FamCacheGroup=t11FamCacheGroup, t11FamGroup=t11FamGroup, t11FamNotifyControl=t11FamNotifyControl, t11FamDomainId=t11FamDomainId, t11FamAreaEntry=t11FamAreaEntry, t11FamGrantedFcIds=t11FamGrantedFcIds, t11FamRcFabricNotifyEnable=t11FamRcFabricNotifyEnable, t11FamFabricName=t11FamFabricName, t11FamSticky=t11FamSticky, t11FamInfo=t11FamInfo, t11FamIfRcfReject=t11FamIfRcfReject, t11FamAreaAssignedPortIdList=t11FamAreaAssignedPortIdList, t11FamFcIdCachePortIds=t11FamFcIdCachePortIds, t11FamNotifyFabricIndex=t11FamNotifyFabricIndex, t11FamDomainIdNotAssignedNotify=t11FamDomainIdNotAssignedNotify, t11FamNotificationGroup=t11FamNotificationGroup, t11FamIfEntry=t11FamIfEntry, t11FamDatabaseTable=t11FamDatabaseTable, t11FamDatabaseSwitchWwn=t11FamDatabaseSwitchWwn, t11FamFabricIndex=t11FamFabricIndex, t11FamContiguousAllocation=t11FamContiguousAllocation, t11FamMIBObjects=t11FamMIBObjects, t11FamAssignedAreaIdList=t11FamAssignedAreaIdList, t11FamAreaTable=t11FamAreaTable, t11FamMIBCompliances=t11FamMIBCompliances, t11FamFabricChangeNotify=t11FamFabricChangeNotify, t11FamRestart=t11FamRestart, t11FamConfiguration=t11FamConfiguration, t11FamFcIdCacheWwn=t11FamFcIdCacheWwn, t11FcFabricAddrMgrMIB=t11FcFabricAddrMgrMIB, t11FamEnable=t11FamEnable, t11FamRecoveredFcIds=t11FamRecoveredFcIds, t11FamMIBCompliance=t11FamMIBCompliance, t11FamPriority=t11FamPriority, t11FamMIBConformance=t11FamMIBConformance, t11FamAutoReconfigure=t11FamAutoReconfigure, t11FamState=t11FamState, t11FamBuildFabrics=t11FamBuildFabrics, t11FamAreaAreaId=t11FamAreaAreaId, t11FamConfigDomainId=t11FamConfigDomainId, t11FamTable=t11FamTable, t11FamAvailableFcIds=t11FamAvailableFcIds, t11FamRunningPriority=t11FamRunningPriority, t11FamIfRole=t11FamIfRole, t11FamConfigDomainIdType=t11FamConfigDomainIdType, t11FamLocalSwitchWwn=t11FamLocalSwitchWwn, t11FamDatabaseDomainId=t11FamDatabaseDomainId, t11FamFcIdCacheEntry=t11FamFcIdCacheEntry, t11FamDatabaseGroup=t11FamDatabaseGroup, t11FamNotifications=t11FamNotifications, T11FamDomainPriority=T11FamDomainPriority, t11FamAreaGroup=t11FamAreaGroup, t11FamPrincipalSwitchSelections=t11FamPrincipalSwitchSelections, t11FamAssignedFcIds=t11FamAssignedFcIds, t11FamFcIdCacheTable=t11FamFcIdCacheTable, t11FamFcIdCacheAreaIdPortId=t11FamFcIdCacheAreaIdPortId, t11FamFreeFcIds=t11FamFreeFcIds, t11FamLocalPrincipalSwitchSlctns=t11FamLocalPrincipalSwitchSlctns, t11FamIfRowStatus=t11FamIfRowStatus, T11FamDomainInterfaceRole=T11FamDomainInterfaceRole, t11FamPrincipalSwitchWwn=t11FamPrincipalSwitchWwn, t11FamIfTable=t11FamIfTable, t11FamCommandGroup=t11FamCommandGroup, T11FamState=T11FamState, t11FamPrincSwRunningPriority=t11FamPrincSwRunningPriority, t11FamMIBGroups=t11FamMIBGroups, t11FamNewPrincipalSwitchNotify=t11FamNewPrincipalSwitchNotify)
