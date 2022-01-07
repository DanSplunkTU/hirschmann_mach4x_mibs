#
# PySNMP MIB module ALCATEL-IND1-AUTO-FABRIC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/nokia/aos7/ALCATEL-IND1-AUTO-FABRIC-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:32:28 2022
# On host fv-az36-988 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
softentIND1AutoFabric, = mibBuilder.importSymbols("ALCATEL-IND1-BASE", "softentIND1AutoFabric")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
iso, ModuleIdentity, Counter32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Gauge32, TimeTicks, MibIdentifier, Integer32, Unsigned32, IpAddress, ObjectIdentity, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "ModuleIdentity", "Counter32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Gauge32", "TimeTicks", "MibIdentifier", "Integer32", "Unsigned32", "IpAddress", "ObjectIdentity", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
alcatelIND1AUTOFABRICMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 75, 1))
alcatelIND1AUTOFABRICMIB.setRevisions(('2012-11-25 00:00',))
if mibBuilder.loadTexts: alcatelIND1AUTOFABRICMIB.setLastUpdated('201211260000Z')
if mibBuilder.loadTexts: alcatelIND1AUTOFABRICMIB.setOrganization('Alcatel - Architects Of An Internet World')
alcatelIND1AUTOFABRICMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 75, 1, 0))
alcatelIND1AUTOFABRICMIBObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 75, 1, 1))
if mibBuilder.loadTexts: alcatelIND1AUTOFABRICMIBObjects.setStatus('current')
alcatelIND1AUTOFABRICMIBConformance = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 75, 1, 2))
if mibBuilder.loadTexts: alcatelIND1AUTOFABRICMIBConformance.setStatus('current')
alcatelIND1AUTOFABRICMIBGroups = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 75, 1, 2, 1))
if mibBuilder.loadTexts: alcatelIND1AUTOFABRICMIBGroups.setStatus('current')
alcatelIND1AUTOFABRICMIBCompliances = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 75, 1, 2, 2))
if mibBuilder.loadTexts: alcatelIND1AUTOFABRICMIBCompliances.setStatus('current')
alaAutoFabricGlobalStatus = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 75, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaAutoFabricGlobalStatus.setStatus('current')
alaAutoFabricGlobalDiscovery = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 75, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("default", 1), ("restart", 2))).clone('default')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaAutoFabricGlobalDiscovery.setStatus('current')
alaAutoFabricGlobalLACPProtocolStatus = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 75, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaAutoFabricGlobalLACPProtocolStatus.setStatus('current')
alaAutoFabricGlobalSPBProtocolStatus = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 75, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaAutoFabricGlobalSPBProtocolStatus.setStatus('current')
alaAutoFabricGlobalMVRPProtocolStatus = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 75, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaAutoFabricGlobalMVRPProtocolStatus.setStatus('current')
alaAutoFabricGlobalConfigSaveTimer = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 75, 1, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(60, 3600)).clone(300)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaAutoFabricGlobalConfigSaveTimer.setStatus('current')
alaAutoFabricGlobalConfigSaveTimerStatus = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 75, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaAutoFabricGlobalConfigSaveTimerStatus.setStatus('current')
alaAutoFabricGlobalDiscoveryTimer = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 75, 1, 1, 8), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 3600))).setUnits('Minutes').setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaAutoFabricGlobalDiscoveryTimer.setStatus('current')
alaAutoFabricRemoveGlobalConfig = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 75, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("default", 1), ("removeGlobalConfig", 2))).clone('default')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaAutoFabricRemoveGlobalConfig.setStatus('deprecated')
alaAutoFabricGlobalOSPFv2ProtocolStatus = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 75, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaAutoFabricGlobalOSPFv2ProtocolStatus.setStatus('current')
alaAutoFabricGlobalOSPFv3ProtocolStatus = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 75, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaAutoFabricGlobalOSPFv3ProtocolStatus.setStatus('current')
alaAutoFabricGlobalISISProtocolStatus = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 75, 1, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaAutoFabricGlobalISISProtocolStatus.setStatus('current')
alaAutoFabricSPBDefaultProfile = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 75, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("singleService", 1), ("autoVlan", 2))).clone('autoVlan')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaAutoFabricSPBDefaultProfile.setStatus('current')
alaAutoFabricLBDProtocolStatus = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 75, 1, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaAutoFabricLBDProtocolStatus.setStatus('current')
alaAutoFabricRemoveVCReload = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 75, 1, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("default", 1), ("removeVCReload", 2))).clone('default')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaAutoFabricRemoveVCReload.setStatus('current')
alaAutoFabricPortConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 75, 1, 1, 9))
alaAutoFabricPortConfigTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 75, 1, 1, 9, 1), )
if mibBuilder.loadTexts: alaAutoFabricPortConfigTable.setStatus('current')
alaAutoFabricPortConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 75, 1, 1, 9, 1, 1), ).setIndexNames((0, "ALCATEL-IND1-AUTO-FABRIC-MIB", "alaAutoFabricPortConfigIfIndex"))
if mibBuilder.loadTexts: alaAutoFabricPortConfigEntry.setStatus('current')
alaAutoFabricPortConfigIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 75, 1, 1, 9, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: alaAutoFabricPortConfigIfIndex.setStatus('current')
alaAutoFabricPortConfigStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 75, 1, 1, 9, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaAutoFabricPortConfigStatus.setStatus('current')
alaAutoFabricPortLACPProtocolStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 75, 1, 1, 9, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaAutoFabricPortLACPProtocolStatus.setStatus('current')
alaAutoFabricPortSPBProtocolStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 75, 1, 1, 9, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaAutoFabricPortSPBProtocolStatus.setStatus('current')
alaAutoFabricPortMVRPProtocolStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 75, 1, 1, 9, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaAutoFabricPortMVRPProtocolStatus.setStatus('current')
alaAutoFabricPortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 75, 1, 1, 9, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("disabled", 1), ("pending", 2), ("complete", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaAutoFabricPortStatus.setStatus('current')
alaAutoFabricPortSPBDefaultProfile = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 75, 1, 1, 9, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("singleService", 1), ("autoVlan", 2))).clone('autoVlan')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaAutoFabricPortSPBDefaultProfile.setStatus('current')
alaAutoFabricTrapsObj = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 75, 1, 1, 16))
alaAutoFabricSTPMode = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 75, 1, 1, 16, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("flatMode", 1), ("perVlan", 2)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: alaAutoFabricSTPMode.setStatus('current')
alaAutoFabricSTPModeChangeAlert = NotificationType((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 75, 1, 0, 1)).setObjects(("ALCATEL-IND1-AUTO-FABRIC-MIB", "alaAutoFabricSTPMode"))
if mibBuilder.loadTexts: alaAutoFabricSTPModeChangeAlert.setStatus('current')
alcatelIND1AUTOFABRICMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 75, 1, 2, 2, 1)).setObjects(("ALCATEL-IND1-AUTO-FABRIC-MIB", "alaAutoFabricBaseGroup"), ("ALCATEL-IND1-AUTO-FABRIC-MIB", "alaAutoFabricPortConfigGroup"), ("ALCATEL-IND1-AUTO-FABRIC-MIB", "alaAutoFabricNotificationGroup"), ("ALCATEL-IND1-AUTO-FABRIC-MIB", "alaAutoFabricTrapsObjGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alcatelIND1AUTOFABRICMIBCompliance = alcatelIND1AUTOFABRICMIBCompliance.setStatus('current')
alaAutoFabricBaseGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 75, 1, 2, 1, 1)).setObjects(("ALCATEL-IND1-AUTO-FABRIC-MIB", "alaAutoFabricGlobalStatus"), ("ALCATEL-IND1-AUTO-FABRIC-MIB", "alaAutoFabricGlobalDiscovery"), ("ALCATEL-IND1-AUTO-FABRIC-MIB", "alaAutoFabricGlobalLACPProtocolStatus"), ("ALCATEL-IND1-AUTO-FABRIC-MIB", "alaAutoFabricGlobalSPBProtocolStatus"), ("ALCATEL-IND1-AUTO-FABRIC-MIB", "alaAutoFabricGlobalMVRPProtocolStatus"), ("ALCATEL-IND1-AUTO-FABRIC-MIB", "alaAutoFabricGlobalConfigSaveTimer"), ("ALCATEL-IND1-AUTO-FABRIC-MIB", "alaAutoFabricGlobalConfigSaveTimerStatus"), ("ALCATEL-IND1-AUTO-FABRIC-MIB", "alaAutoFabricGlobalDiscoveryTimer"), ("ALCATEL-IND1-AUTO-FABRIC-MIB", "alaAutoFabricRemoveGlobalConfig"), ("ALCATEL-IND1-AUTO-FABRIC-MIB", "alaAutoFabricGlobalOSPFv2ProtocolStatus"), ("ALCATEL-IND1-AUTO-FABRIC-MIB", "alaAutoFabricGlobalOSPFv3ProtocolStatus"), ("ALCATEL-IND1-AUTO-FABRIC-MIB", "alaAutoFabricGlobalISISProtocolStatus"), ("ALCATEL-IND1-AUTO-FABRIC-MIB", "alaAutoFabricSPBDefaultProfile"), ("ALCATEL-IND1-AUTO-FABRIC-MIB", "alaAutoFabricLBDProtocolStatus"), ("ALCATEL-IND1-AUTO-FABRIC-MIB", "alaAutoFabricRemoveVCReload"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaAutoFabricBaseGroup = alaAutoFabricBaseGroup.setStatus('current')
alaAutoFabricPortConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 75, 1, 2, 1, 2)).setObjects(("ALCATEL-IND1-AUTO-FABRIC-MIB", "alaAutoFabricPortConfigStatus"), ("ALCATEL-IND1-AUTO-FABRIC-MIB", "alaAutoFabricPortLACPProtocolStatus"), ("ALCATEL-IND1-AUTO-FABRIC-MIB", "alaAutoFabricPortSPBProtocolStatus"), ("ALCATEL-IND1-AUTO-FABRIC-MIB", "alaAutoFabricPortMVRPProtocolStatus"), ("ALCATEL-IND1-AUTO-FABRIC-MIB", "alaAutoFabricPortStatus"), ("ALCATEL-IND1-AUTO-FABRIC-MIB", "alaAutoFabricPortSPBDefaultProfile"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaAutoFabricPortConfigGroup = alaAutoFabricPortConfigGroup.setStatus('current')
alaAutoFabricNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 75, 1, 2, 1, 3)).setObjects(("ALCATEL-IND1-AUTO-FABRIC-MIB", "alaAutoFabricSTPModeChangeAlert"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaAutoFabricNotificationGroup = alaAutoFabricNotificationGroup.setStatus('current')
alaAutoFabricTrapsObjGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 75, 1, 2, 1, 4)).setObjects(("ALCATEL-IND1-AUTO-FABRIC-MIB", "alaAutoFabricSTPMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaAutoFabricTrapsObjGroup = alaAutoFabricTrapsObjGroup.setStatus('current')
mibBuilder.exportSymbols("ALCATEL-IND1-AUTO-FABRIC-MIB", alaAutoFabricRemoveGlobalConfig=alaAutoFabricRemoveGlobalConfig, alaAutoFabricSTPMode=alaAutoFabricSTPMode, alaAutoFabricPortStatus=alaAutoFabricPortStatus, alaAutoFabricGlobalOSPFv3ProtocolStatus=alaAutoFabricGlobalOSPFv3ProtocolStatus, alaAutoFabricPortSPBProtocolStatus=alaAutoFabricPortSPBProtocolStatus, alaAutoFabricPortMVRPProtocolStatus=alaAutoFabricPortMVRPProtocolStatus, alaAutoFabricGlobalOSPFv2ProtocolStatus=alaAutoFabricGlobalOSPFv2ProtocolStatus, alaAutoFabricNotificationGroup=alaAutoFabricNotificationGroup, alaAutoFabricPortConfigTable=alaAutoFabricPortConfigTable, alcatelIND1AUTOFABRICMIB=alcatelIND1AUTOFABRICMIB, alaAutoFabricBaseGroup=alaAutoFabricBaseGroup, PYSNMP_MODULE_ID=alcatelIND1AUTOFABRICMIB, alaAutoFabricPortConfigStatus=alaAutoFabricPortConfigStatus, alaAutoFabricTrapsObj=alaAutoFabricTrapsObj, alcatelIND1AUTOFABRICMIBCompliances=alcatelIND1AUTOFABRICMIBCompliances, alcatelIND1AUTOFABRICMIBConformance=alcatelIND1AUTOFABRICMIBConformance, alaAutoFabricSPBDefaultProfile=alaAutoFabricSPBDefaultProfile, alaAutoFabricGlobalConfigSaveTimerStatus=alaAutoFabricGlobalConfigSaveTimerStatus, alaAutoFabricPortConfigIfIndex=alaAutoFabricPortConfigIfIndex, alaAutoFabricSTPModeChangeAlert=alaAutoFabricSTPModeChangeAlert, alaAutoFabricGlobalDiscovery=alaAutoFabricGlobalDiscovery, alcatelIND1AUTOFABRICMIBNotifications=alcatelIND1AUTOFABRICMIBNotifications, alcatelIND1AUTOFABRICMIBGroups=alcatelIND1AUTOFABRICMIBGroups, alaAutoFabricPortLACPProtocolStatus=alaAutoFabricPortLACPProtocolStatus, alaAutoFabricGlobalMVRPProtocolStatus=alaAutoFabricGlobalMVRPProtocolStatus, alaAutoFabricGlobalConfigSaveTimer=alaAutoFabricGlobalConfigSaveTimer, alaAutoFabricRemoveVCReload=alaAutoFabricRemoveVCReload, alaAutoFabricPortConfig=alaAutoFabricPortConfig, alaAutoFabricLBDProtocolStatus=alaAutoFabricLBDProtocolStatus, alaAutoFabricPortConfigEntry=alaAutoFabricPortConfigEntry, alcatelIND1AUTOFABRICMIBObjects=alcatelIND1AUTOFABRICMIBObjects, alaAutoFabricGlobalSPBProtocolStatus=alaAutoFabricGlobalSPBProtocolStatus, alaAutoFabricPortConfigGroup=alaAutoFabricPortConfigGroup, alaAutoFabricGlobalStatus=alaAutoFabricGlobalStatus, alaAutoFabricGlobalISISProtocolStatus=alaAutoFabricGlobalISISProtocolStatus, alaAutoFabricTrapsObjGroup=alaAutoFabricTrapsObjGroup, alaAutoFabricGlobalDiscoveryTimer=alaAutoFabricGlobalDiscoveryTimer, alcatelIND1AUTOFABRICMIBCompliance=alcatelIND1AUTOFABRICMIBCompliance, alaAutoFabricGlobalLACPProtocolStatus=alaAutoFabricGlobalLACPProtocolStatus, alaAutoFabricPortSPBDefaultProfile=alaAutoFabricPortSPBDefaultProfile)
