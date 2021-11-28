#
# PySNMP MIB module EQLACCESS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/equallogic/EQLACCESS-MIB
# Produced by pysmi-1.1.3 at Sun Nov 28 20:18:03 2021
# On host fv-az77-612 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
eqlGroupId, eqlStorageGroupAdminAccountIndex, UTFString = mibBuilder.importSymbols("EQLGROUP-MIB", "eqlGroupId", "eqlStorageGroupAdminAccountIndex", "UTFString")
eqliscsiVolumeIndex, eqliscsiLocalMemberId, ACLAppliesTo = mibBuilder.importSymbols("EQLVOLUME-MIB", "eqliscsiVolumeIndex", "eqliscsiLocalMemberId", "ACLAppliesTo")
equalLogic, = mibBuilder.importSymbols("EQUALLOGIC-SMI", "equalLogic")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, iso, NotificationType, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Gauge32, Unsigned32, enterprises, TimeTicks, ModuleIdentity, Integer32, ObjectIdentity, Counter64, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "iso", "NotificationType", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Gauge32", "Unsigned32", "enterprises", "TimeTicks", "ModuleIdentity", "Integer32", "ObjectIdentity", "Counter64", "Bits")
RowPointer, DisplayString, RowStatus, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowPointer", "DisplayString", "RowStatus", "TruthValue", "TextualConvention")
eqlAccessModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 12740, 24))
eqlAccessModule.setRevisions(('2012-05-01 00:00',))
if mibBuilder.loadTexts: eqlAccessModule.setLastUpdated('201503171528Z')
if mibBuilder.loadTexts: eqlAccessModule.setOrganization('Dell Inc.')
eqlAccessObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 12740, 24, 1))
eqlAccessNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 12740, 24, 2))
eqlAccessConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 12740, 24, 3))
eqlAccessGroupTable = MibTable((1, 3, 6, 1, 4, 1, 12740, 24, 1, 1), )
if mibBuilder.loadTexts: eqlAccessGroupTable.setStatus('current')
eqlAccessGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12740, 24, 1, 1, 1), ).setIndexNames((0, "EQLACCESS-MIB", "eqlAccessGroupIndex"))
if mibBuilder.loadTexts: eqlAccessGroupEntry.setStatus('current')
eqlAccessGroupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 24, 1, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: eqlAccessGroupIndex.setStatus('current')
eqlAccessGroupRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 24, 1, 1, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlAccessGroupRowStatus.setStatus('current')
eqlAccessGroupUUID = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 24, 1, 1, 1, 3), UTFString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlAccessGroupUUID.setStatus('current')
eqlAccessGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 24, 1, 1, 1, 4), UTFString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlAccessGroupName.setStatus('current')
eqlAccessGroupKeyName = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 24, 1, 1, 1, 5), UTFString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlAccessGroupKeyName.setStatus('current')
eqlAccessGroupDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 24, 1, 1, 1, 6), UTFString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlAccessGroupDescription.setStatus('current')
eqlAccessGroupAdminKey = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 24, 1, 1, 1, 7), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlAccessGroupAdminKey.setStatus('current')
eqlAccessGroupType = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 24, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("access-group", 1), ("access-record", 2))).clone('access-record')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlAccessGroupType.setStatus('current')
eqlAccessGroupPrivacyFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 24, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("public", 1), ("private", 2))).clone('private')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlAccessGroupPrivacyFlag.setStatus('current')
eqlAccessGroupByTypeTable = MibTable((1, 3, 6, 1, 4, 1, 12740, 24, 1, 2), )
if mibBuilder.loadTexts: eqlAccessGroupByTypeTable.setStatus('current')
eqlAccessGroupByTypeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12740, 24, 1, 2, 1), ).setIndexNames((0, "EQLACCESS-MIB", "eqlAccessGroupType"), (0, "EQLACCESS-MIB", "eqlAccessGroupIndex"))
if mibBuilder.loadTexts: eqlAccessGroupByTypeEntry.setStatus('current')
eqlAccessGroupByTypeUUID = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 24, 1, 2, 1, 1), UTFString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlAccessGroupByTypeUUID.setStatus('current')
eqlAccessGroupByTypeName = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 24, 1, 2, 1, 2), UTFString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlAccessGroupByTypeName.setStatus('current')
eqlAccessGroupByTypeDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 24, 1, 2, 1, 3), UTFString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlAccessGroupByTypeDescription.setStatus('current')
eqlAccessGroupByTypeAdminKey = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 24, 1, 2, 1, 4), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlAccessGroupByTypeAdminKey.setStatus('current')
eqlAccessGroupMemberTable = MibTable((1, 3, 6, 1, 4, 1, 12740, 24, 1, 3), )
if mibBuilder.loadTexts: eqlAccessGroupMemberTable.setStatus('current')
eqlAccessGroupMemberEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12740, 24, 1, 3, 1), ).setIndexNames((0, "EQLACCESS-MIB", "eqlAccessGroupIndex"), (0, "EQLACCESS-MIB", "eqlAccessGroupChildIndex"))
if mibBuilder.loadTexts: eqlAccessGroupMemberEntry.setStatus('current')
eqlAccessGroupChildIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 24, 1, 3, 1, 1), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlAccessGroupChildIndex.setStatus('current')
eqlAccessGroupMemberRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 24, 1, 3, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlAccessGroupMemberRowStatus.setStatus('current')
eqlAccessPointTable = MibTable((1, 3, 6, 1, 4, 1, 12740, 24, 1, 4), )
if mibBuilder.loadTexts: eqlAccessPointTable.setStatus('current')
eqlAccessPointEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12740, 24, 1, 4, 1), ).setIndexNames((0, "EQLACCESS-MIB", "eqlAccessGroupIndex"), (0, "EQLACCESS-MIB", "eqlAccessPointIndex"))
if mibBuilder.loadTexts: eqlAccessPointEntry.setStatus('current')
eqlAccessPointIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 24, 1, 4, 1, 1), Unsigned32())
if mibBuilder.loadTexts: eqlAccessPointIndex.setStatus('current')
eqlAccessPointRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 24, 1, 4, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlAccessPointRowStatus.setStatus('current')
eqlAccessPointInitiatorName = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 24, 1, 4, 1, 3), UTFString().subtype(subtypeSpec=ValueSizeConstraint(0, 223))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlAccessPointInitiatorName.setStatus('current')
eqlAccessPointInitiatorCHAPUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 24, 1, 4, 1, 4), UTFString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlAccessPointInitiatorCHAPUserName.setStatus('current')
eqlAccessPointDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 24, 1, 4, 1, 5), UTFString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlAccessPointDescription.setStatus('current')
eqlAccessPointAddrTable = MibTable((1, 3, 6, 1, 4, 1, 12740, 24, 1, 5), )
if mibBuilder.loadTexts: eqlAccessPointAddrTable.setStatus('current')
eqlAccessPointAddrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12740, 24, 1, 5, 1), ).setIndexNames((0, "EQLACCESS-MIB", "eqlAccessGroupIndex"), (0, "EQLACCESS-MIB", "eqlAccessPointIndex"), (0, "EQLACCESS-MIB", "eqlAccessPointAddrIndex"))
if mibBuilder.loadTexts: eqlAccessPointAddrEntry.setStatus('current')
eqlAccessPointAddrIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 24, 1, 5, 1, 1), Unsigned32())
if mibBuilder.loadTexts: eqlAccessPointAddrIndex.setStatus('current')
eqlAccessPointAddrRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 24, 1, 5, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlAccessPointAddrRowStatus.setStatus('current')
eqlAccessPointAddrInitiatorAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 24, 1, 5, 1, 3), InetAddressType().clone('ipv4')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlAccessPointAddrInitiatorAddrType.setStatus('current')
eqlAccessPointAddrInitiatorAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 24, 1, 5, 1, 4), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlAccessPointAddrInitiatorAddr.setStatus('current')
eqlAccessPointAddrInitiatorAddrWildcardType = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 24, 1, 5, 1, 5), InetAddressType().clone('ipv4')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlAccessPointAddrInitiatorAddrWildcardType.setStatus('current')
eqlAccessPointAddrInitiatorAddrWildcard = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 24, 1, 5, 1, 6), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlAccessPointAddrInitiatorAddrWildcard.setStatus('current')
eqlAccessGroupObjectAssocTable = MibTable((1, 3, 6, 1, 4, 1, 12740, 24, 1, 6), )
if mibBuilder.loadTexts: eqlAccessGroupObjectAssocTable.setStatus('current')
eqlAccessGroupObjectAssocEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12740, 24, 1, 6, 1), ).setIndexNames((0, "EQLACCESS-MIB", "eqlAccessGroupIndex"), (0, "EQLACCESS-MIB", "eqlAccessGroupObjectAssocIndex"))
if mibBuilder.loadTexts: eqlAccessGroupObjectAssocEntry.setStatus('current')
eqlAccessGroupObjectAssocIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 24, 1, 6, 1, 1), Unsigned32())
if mibBuilder.loadTexts: eqlAccessGroupObjectAssocIndex.setStatus('current')
eqlAccessGroupObjectAssocRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 24, 1, 6, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlAccessGroupObjectAssocRowStatus.setStatus('current')
eqlAccessGroupObjectAssocOID = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 24, 1, 6, 1, 3), RowPointer()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlAccessGroupObjectAssocOID.setStatus('current')
eqlAccessGroupObjectAssocFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 24, 1, 6, 1, 4), ACLAppliesTo()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlAccessGroupObjectAssocFlag.setStatus('current')
eqlAccessGroupObjectAssocCreator = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 24, 1, 6, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("vCenter", 1), ("gui", 2), ("cli", 3), ("other", 4))).clone('other')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlAccessGroupObjectAssocCreator.setStatus('current')
eqlAccessGroupVolumeAssocTable = MibTable((1, 3, 6, 1, 4, 1, 12740, 24, 1, 7), )
if mibBuilder.loadTexts: eqlAccessGroupVolumeAssocTable.setStatus('current')
eqlAccessGroupVolumeAssocEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12740, 24, 1, 7, 1), ).setIndexNames((0, "EQLACCESS-MIB", "eqlAccessGroupIndex"), (0, "EQLVOLUME-MIB", "eqliscsiLocalMemberId"), (0, "EQLVOLUME-MIB", "eqliscsiVolumeIndex"))
if mibBuilder.loadTexts: eqlAccessGroupVolumeAssocEntry.setStatus('current')
eqlAccessGroupVolumeAssocFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 24, 1, 7, 1, 1), ACLAppliesTo()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlAccessGroupVolumeAssocFlag.setStatus('current')
eqlAccessGroupVolumeAssocObjectIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 24, 1, 7, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlAccessGroupVolumeAssocObjectIndex.setStatus('current')
eqlVolumeAccessGroupAssocTable = MibTable((1, 3, 6, 1, 4, 1, 12740, 24, 1, 8), )
if mibBuilder.loadTexts: eqlVolumeAccessGroupAssocTable.setStatus('current')
eqlVolumeAccessGroupAssocEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12740, 24, 1, 8, 1), ).setIndexNames((0, "EQLVOLUME-MIB", "eqliscsiLocalMemberId"), (0, "EQLVOLUME-MIB", "eqliscsiVolumeIndex"), (0, "EQLACCESS-MIB", "eqlAccessGroupIndex"))
if mibBuilder.loadTexts: eqlVolumeAccessGroupAssocEntry.setStatus('current')
eqlVolumeAccessGroupAssocFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 24, 1, 8, 1, 1), ACLAppliesTo()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlVolumeAccessGroupAssocFlag.setStatus('current')
eqlVolumeAccessGroupAssocObjectIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 24, 1, 8, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlVolumeAccessGroupAssocObjectIndex.setStatus('current')
eqlAccessGroupSharedVolumeAssocTable = MibTable((1, 3, 6, 1, 4, 1, 12740, 24, 1, 9), )
if mibBuilder.loadTexts: eqlAccessGroupSharedVolumeAssocTable.setStatus('current')
eqlAccessGroupSharedVolumeAssocEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12740, 24, 1, 9, 1), ).setIndexNames((0, "EQLACCESS-MIB", "eqlAccessGroupIndex"), (0, "EQLVOLUME-MIB", "eqliscsiLocalMemberId"), (0, "EQLVOLUME-MIB", "eqliscsiVolumeIndex"))
if mibBuilder.loadTexts: eqlAccessGroupSharedVolumeAssocEntry.setStatus('current')
eqlAccessGroupSharedVolumeAssocFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 24, 1, 9, 1, 1), ACLAppliesTo()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlAccessGroupSharedVolumeAssocFlag.setStatus('current')
eqlAccessGroupSharedVolumeAssocObjectIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 24, 1, 9, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlAccessGroupSharedVolumeAssocObjectIndex.setStatus('current')
eqlSharedVolumeAccessGroupAssocTable = MibTable((1, 3, 6, 1, 4, 1, 12740, 24, 1, 10), )
if mibBuilder.loadTexts: eqlSharedVolumeAccessGroupAssocTable.setStatus('current')
eqlSharedVolumeAccessGroupAssocEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12740, 24, 1, 10, 1), ).setIndexNames((0, "EQLVOLUME-MIB", "eqliscsiLocalMemberId"), (0, "EQLVOLUME-MIB", "eqliscsiVolumeIndex"), (0, "EQLACCESS-MIB", "eqlAccessGroupIndex"))
if mibBuilder.loadTexts: eqlSharedVolumeAccessGroupAssocEntry.setStatus('current')
eqlSharedVolumeAccessGroupAssocFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 24, 1, 10, 1, 1), ACLAppliesTo()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlSharedVolumeAccessGroupAssocFlag.setStatus('current')
eqlSharedVolumeAccessGroupAssocObjectIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 24, 1, 10, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlSharedVolumeAccessGroupAssocObjectIndex.setStatus('current')
eqlAdminAccountAccessGroupTable = MibTable((1, 3, 6, 1, 4, 1, 12740, 24, 1, 11), )
if mibBuilder.loadTexts: eqlAdminAccountAccessGroupTable.setStatus('current')
eqlAdminAccountAccessGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12740, 24, 1, 11, 1), ).setIndexNames((0, "EQLGROUP-MIB", "eqlGroupId"), (0, "EQLGROUP-MIB", "eqlStorageGroupAdminAccountIndex"), (0, "EQLACCESS-MIB", "eqlAccessGroupIndex"))
if mibBuilder.loadTexts: eqlAdminAccountAccessGroupEntry.setStatus('current')
eqlAdminAccountAccessGroupRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 24, 1, 11, 1, 1), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlAdminAccountAccessGroupRowStatus.setStatus('current')
eqlAdminAccountAccessGroupAccess = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 24, 1, 11, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("read-only", 1), ("read-write", 2))).clone('read-only')).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlAdminAccountAccessGroupAccess.setStatus('current')
eqlACLCountTable = MibTable((1, 3, 6, 1, 4, 1, 12740, 24, 1, 12), )
if mibBuilder.loadTexts: eqlACLCountTable.setStatus('current')
eqlACLCountEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12740, 24, 1, 12, 1), ).setIndexNames((0, "EQLGROUP-MIB", "eqlGroupId"))
if mibBuilder.loadTexts: eqlACLCountEntry.setStatus('current')
eqlACLCountUserDefined = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 24, 1, 12, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlACLCountUserDefined.setStatus('current')
eqlACLCountMPIO = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 24, 1, 12, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlACLCountMPIO.setStatus('current')
eqlACLCountTotal = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 24, 1, 12, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlACLCountTotal.setStatus('current')
eqlMaxAccessGroupCount = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 24, 1, 12, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlMaxAccessGroupCount.setStatus('current')
eqlMaxAccessRecordCount = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 24, 1, 12, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlMaxAccessRecordCount.setStatus('current')
eqlMaxAccessPointCount = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 24, 1, 12, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlMaxAccessPointCount.setStatus('current')
eqlMaxAccessPointIPAddrCount = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 24, 1, 12, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlMaxAccessPointIPAddrCount.setStatus('current')
eqlMaxAssociationCount = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 24, 1, 12, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlMaxAssociationCount.setStatus('current')
eqlAccessGroupCount = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 24, 1, 12, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlAccessGroupCount.setStatus('current')
eqlAccessRecordCount = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 24, 1, 12, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlAccessRecordCount.setStatus('current')
eqlAccessPointCount = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 24, 1, 12, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlAccessPointCount.setStatus('current')
eqlAccessPointIPAddrCount = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 24, 1, 12, 1, 12), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlAccessPointIPAddrCount.setStatus('current')
eqlAssociationCount = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 24, 1, 12, 1, 13), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlAssociationCount.setStatus('current')
eqlVolumeAccessGroupAssocCountTable = MibTable((1, 3, 6, 1, 4, 1, 12740, 24, 1, 13), )
if mibBuilder.loadTexts: eqlVolumeAccessGroupAssocCountTable.setStatus('current')
eqlVolumeAccessGroupAssocCountEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12740, 24, 1, 13, 1), ).setIndexNames((0, "EQLVOLUME-MIB", "eqliscsiLocalMemberId"), (0, "EQLVOLUME-MIB", "eqliscsiVolumeIndex"))
if mibBuilder.loadTexts: eqlVolumeAccessGroupAssocCountEntry.setStatus('current')
eqlVolumeAccessGroupAssocCount = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 24, 1, 13, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlVolumeAccessGroupAssocCount.setStatus('current')
eqlVolumeAccessRecordAssocCount = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 24, 1, 13, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlVolumeAccessRecordAssocCount.setStatus('current')
mibBuilder.exportSymbols("EQLACCESS-MIB", eqlVolumeAccessGroupAssocCount=eqlVolumeAccessGroupAssocCount, eqlAccessRecordCount=eqlAccessRecordCount, eqlACLCountTable=eqlACLCountTable, eqlAccessGroupByTypeName=eqlAccessGroupByTypeName, eqlAccessGroupByTypeDescription=eqlAccessGroupByTypeDescription, eqlAccessGroupByTypeTable=eqlAccessGroupByTypeTable, eqlAdminAccountAccessGroupRowStatus=eqlAdminAccountAccessGroupRowStatus, eqlMaxAssociationCount=eqlMaxAssociationCount, eqlAdminAccountAccessGroupEntry=eqlAdminAccountAccessGroupEntry, eqlAccessPointAddrInitiatorAddrWildcardType=eqlAccessPointAddrInitiatorAddrWildcardType, eqlSharedVolumeAccessGroupAssocFlag=eqlSharedVolumeAccessGroupAssocFlag, eqlAccessGroupSharedVolumeAssocEntry=eqlAccessGroupSharedVolumeAssocEntry, eqlSharedVolumeAccessGroupAssocObjectIndex=eqlSharedVolumeAccessGroupAssocObjectIndex, eqlAccessGroupMemberEntry=eqlAccessGroupMemberEntry, eqlAccessGroupSharedVolumeAssocTable=eqlAccessGroupSharedVolumeAssocTable, eqlVolumeAccessGroupAssocCountEntry=eqlVolumeAccessGroupAssocCountEntry, PYSNMP_MODULE_ID=eqlAccessModule, eqlAccessGroupByTypeUUID=eqlAccessGroupByTypeUUID, eqlVolumeAccessGroupAssocEntry=eqlVolumeAccessGroupAssocEntry, eqlAccessPointAddrIndex=eqlAccessPointAddrIndex, eqlAccessGroupObjectAssocRowStatus=eqlAccessGroupObjectAssocRowStatus, eqlAccessPointInitiatorCHAPUserName=eqlAccessPointInitiatorCHAPUserName, eqlAccessPointAddrTable=eqlAccessPointAddrTable, eqlAccessPointAddrRowStatus=eqlAccessPointAddrRowStatus, eqlAccessGroupObjectAssocIndex=eqlAccessGroupObjectAssocIndex, eqlVolumeAccessGroupAssocTable=eqlVolumeAccessGroupAssocTable, eqlAccessGroupSharedVolumeAssocObjectIndex=eqlAccessGroupSharedVolumeAssocObjectIndex, eqlAccessGroupCount=eqlAccessGroupCount, eqlAdminAccountAccessGroupAccess=eqlAdminAccountAccessGroupAccess, eqlAccessPointAddrInitiatorAddrWildcard=eqlAccessPointAddrInitiatorAddrWildcard, eqlAccessPointInitiatorName=eqlAccessPointInitiatorName, eqlAdminAccountAccessGroupTable=eqlAdminAccountAccessGroupTable, eqlAccessGroupObjectAssocFlag=eqlAccessGroupObjectAssocFlag, eqlAccessPointEntry=eqlAccessPointEntry, eqlAccessPointCount=eqlAccessPointCount, eqlAccessPointAddrInitiatorAddrType=eqlAccessPointAddrInitiatorAddrType, eqlACLCountEntry=eqlACLCountEntry, eqlACLCountMPIO=eqlACLCountMPIO, eqlAccessGroupPrivacyFlag=eqlAccessGroupPrivacyFlag, eqlAccessObjects=eqlAccessObjects, eqlAssociationCount=eqlAssociationCount, eqlAccessGroupDescription=eqlAccessGroupDescription, eqlAccessPointIndex=eqlAccessPointIndex, eqlAccessGroupAdminKey=eqlAccessGroupAdminKey, eqlAccessPointRowStatus=eqlAccessPointRowStatus, eqlAccessGroupObjectAssocCreator=eqlAccessGroupObjectAssocCreator, eqlAccessGroupName=eqlAccessGroupName, eqlVolumeAccessGroupAssocFlag=eqlVolumeAccessGroupAssocFlag, eqlAccessGroupByTypeEntry=eqlAccessGroupByTypeEntry, eqlMaxAccessPointIPAddrCount=eqlMaxAccessPointIPAddrCount, eqlAccessGroupVolumeAssocFlag=eqlAccessGroupVolumeAssocFlag, eqlAccessGroupObjectAssocOID=eqlAccessGroupObjectAssocOID, eqlAccessGroupVolumeAssocEntry=eqlAccessGroupVolumeAssocEntry, eqlAccessGroupUUID=eqlAccessGroupUUID, eqlACLCountUserDefined=eqlACLCountUserDefined, eqlAccessPointDescription=eqlAccessPointDescription, eqlACLCountTotal=eqlACLCountTotal, eqlAccessGroupRowStatus=eqlAccessGroupRowStatus, eqlSharedVolumeAccessGroupAssocTable=eqlSharedVolumeAccessGroupAssocTable, eqlAccessModule=eqlAccessModule, eqlVolumeAccessGroupAssocCountTable=eqlVolumeAccessGroupAssocCountTable, eqlAccessNotifications=eqlAccessNotifications, eqlAccessConformance=eqlAccessConformance, eqlAccessGroupVolumeAssocTable=eqlAccessGroupVolumeAssocTable, eqlAccessPointAddrEntry=eqlAccessPointAddrEntry, eqlAccessGroupKeyName=eqlAccessGroupKeyName, eqlVolumeAccessGroupAssocObjectIndex=eqlVolumeAccessGroupAssocObjectIndex, eqlAccessPointTable=eqlAccessPointTable, eqlMaxAccessRecordCount=eqlMaxAccessRecordCount, eqlAccessPointIPAddrCount=eqlAccessPointIPAddrCount, eqlAccessGroupByTypeAdminKey=eqlAccessGroupByTypeAdminKey, eqlAccessGroupType=eqlAccessGroupType, eqlSharedVolumeAccessGroupAssocEntry=eqlSharedVolumeAccessGroupAssocEntry, eqlAccessGroupObjectAssocEntry=eqlAccessGroupObjectAssocEntry, eqlAccessGroupChildIndex=eqlAccessGroupChildIndex, eqlAccessGroupIndex=eqlAccessGroupIndex, eqlAccessGroupVolumeAssocObjectIndex=eqlAccessGroupVolumeAssocObjectIndex, eqlAccessGroupMemberTable=eqlAccessGroupMemberTable, eqlAccessGroupMemberRowStatus=eqlAccessGroupMemberRowStatus, eqlAccessGroupTable=eqlAccessGroupTable, eqlMaxAccessPointCount=eqlMaxAccessPointCount, eqlAccessPointAddrInitiatorAddr=eqlAccessPointAddrInitiatorAddr, eqlMaxAccessGroupCount=eqlMaxAccessGroupCount, eqlAccessGroupEntry=eqlAccessGroupEntry, eqlVolumeAccessRecordAssocCount=eqlVolumeAccessRecordAssocCount, eqlAccessGroupObjectAssocTable=eqlAccessGroupObjectAssocTable, eqlAccessGroupSharedVolumeAssocFlag=eqlAccessGroupSharedVolumeAssocFlag)
