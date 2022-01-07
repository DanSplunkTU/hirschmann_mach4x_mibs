#
# PySNMP MIB module T11-GS-SERVER-SESSION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/T11-GS-SERVER-SESSION-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:07:39 2022
# On host fv-az36-988 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
fcmSwitchIndex, fcmInstanceIndex = mibBuilder.importSymbols("FC-MGMT-MIB", "fcmSwitchIndex", "fcmInstanceIndex")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
MibIdentifier, ObjectIdentity, ModuleIdentity, iso, Unsigned32, TimeTicks, Gauge32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, mib_2, Bits, NotificationType, IpAddress, Counter64, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "ObjectIdentity", "ModuleIdentity", "iso", "Unsigned32", "TimeTicks", "Gauge32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "mib-2", "Bits", "NotificationType", "IpAddress", "Counter64", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
T11FabricIndex, = mibBuilder.importSymbols("T11-TC-MIB", "T11FabricIndex")
t11GsServerSessionMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 1))
t11GsServerSessionMIB.setRevisions(('2005-10-13 00:00',))
if mibBuilder.loadTexts: t11GsServerSessionMIB.setLastUpdated('200510130000Z')
if mibBuilder.loadTexts: t11GsServerSessionMIB.setOrganization('T11')
t11GssMIBObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 1, 1))
t11GssMIBConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 1, 2))
t11GssMIBNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 1, 0))
t11GssConfiguration = MibIdentifier((1, 3, 6, 1, 2, 1, 1, 1, 1))
t11GssSessionTable = MibTable((1, 3, 6, 1, 2, 1, 1, 1, 1, 1), )
if mibBuilder.loadTexts: t11GssSessionTable.setStatus('current')
t11GssSessionEntry = MibTableRow((1, 3, 6, 1, 2, 1, 1, 1, 1, 1, 1), ).setIndexNames((0, "FC-MGMT-MIB", "fcmInstanceIndex"), (0, "FC-MGMT-MIB", "fcmSwitchIndex"), (0, "T11-GS-SERVER-SESSION-MIB", "t11GssSessionFabricIndex"))
if mibBuilder.loadTexts: t11GssSessionEntry.setStatus('current')
t11GssSessionFabricIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 1, 1, 1, 1, 1, 1), T11FabricIndex())
if mibBuilder.loadTexts: t11GssSessionFabricIndex.setStatus('current')
t11GssSessionOwnerType = MibTableColumn((1, 3, 6, 1, 2, 1, 1, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("gsClient", 2), ("cli", 3), ("snmp", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11GssSessionOwnerType.setStatus('current')
t11GssSessionOwner = MibTableColumn((1, 3, 6, 1, 2, 1, 1, 1, 1, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11GssSessionOwner.setStatus('current')
t11GssSessionControl = MibTableColumn((1, 3, 6, 1, 2, 1, 1, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("commitZoneChanges", 1), ("terminateSession", 2), ("noop", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: t11GssSessionControl.setStatus('current')
t11GssSessionCommitResult = MibTableColumn((1, 3, 6, 1, 2, 1, 1, 1, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("commitSuccessful", 1), ("commitInProgress", 2), ("commitFailed", 3), ("none", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11GssSessionCommitResult.setStatus('current')
t11GssMIBCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 1, 2, 1))
t11GssMIBGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 1, 2, 2))
t11GssMIBCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 1, 2, 1, 1)).setObjects(("T11-GS-SERVER-SESSION-MIB", "t11GssActiveGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    t11GssMIBCompliance = t11GssMIBCompliance.setStatus('current')
t11GssActiveGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 1, 2, 2, 1)).setObjects(("T11-GS-SERVER-SESSION-MIB", "t11GssSessionOwnerType"), ("T11-GS-SERVER-SESSION-MIB", "t11GssSessionOwner"), ("T11-GS-SERVER-SESSION-MIB", "t11GssSessionControl"), ("T11-GS-SERVER-SESSION-MIB", "t11GssSessionCommitResult"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    t11GssActiveGroup = t11GssActiveGroup.setStatus('current')
mibBuilder.exportSymbols("T11-GS-SERVER-SESSION-MIB", t11GssSessionControl=t11GssSessionControl, t11GssMIBCompliance=t11GssMIBCompliance, t11GssSessionTable=t11GssSessionTable, t11GssConfiguration=t11GssConfiguration, t11GssMIBCompliances=t11GssMIBCompliances, t11GssMIBObjects=t11GssMIBObjects, t11GssActiveGroup=t11GssActiveGroup, t11GssMIBNotifications=t11GssMIBNotifications, PYSNMP_MODULE_ID=t11GsServerSessionMIB, t11GssMIBGroups=t11GssMIBGroups, t11GssSessionOwnerType=t11GssSessionOwnerType, t11GssMIBConformance=t11GssMIBConformance, t11GssSessionEntry=t11GssSessionEntry, t11GssSessionCommitResult=t11GssSessionCommitResult, t11GsServerSessionMIB=t11GsServerSessionMIB, t11GssSessionFabricIndex=t11GssSessionFabricIndex, t11GssSessionOwner=t11GssSessionOwner)
