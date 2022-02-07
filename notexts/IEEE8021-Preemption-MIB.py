#
# PySNMP MIB module IEEE8021-Preemption-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/iee/IEEE8021-Preemption-MIB
# Produced by pysmi-1.1.8 at Mon Feb  7 16:06:21 2022
# On host fv-az42-619 platform Linux version 5.11.0-1028-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
ieee8021BridgeBaseComponentId, ieee8021BridgeBasePort = mibBuilder.importSymbols("IEEE8021-BRIDGE-MIB", "ieee8021BridgeBaseComponentId", "ieee8021BridgeBasePort")
IEEE8021PriorityValue, ieee802dot1mibs = mibBuilder.importSymbols("IEEE8021-TC-MIB", "IEEE8021PriorityValue", "ieee802dot1mibs")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
TimeTicks, MibIdentifier, NotificationType, Unsigned32, IpAddress, Integer32, ModuleIdentity, Counter64, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Counter32, Gauge32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "MibIdentifier", "NotificationType", "Unsigned32", "IpAddress", "Integer32", "ModuleIdentity", "Counter64", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Counter32", "Gauge32", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ieee8021PreemptionMib = ModuleIdentity((1, 3, 111, 2, 802, 1, 1, 29))
ieee8021PreemptionMib.setRevisions(('2018-06-21 00:00', '2016-08-15 00:00',))
if mibBuilder.loadTexts: ieee8021PreemptionMib.setLastUpdated('201806210000Z')
if mibBuilder.loadTexts: ieee8021PreemptionMib.setOrganization('IEEE 802.1 Working Group')
ieee8021PreemptionNotifications = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 29, 0))
ieee8021PreemptionObjects = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 29, 1))
ieee8021PreemptionConformance = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 29, 2))
ieee8021PreemptionParameters = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 29, 1, 1))
ieee8021PreemptionParameterTable = MibTable((1, 3, 111, 2, 802, 1, 1, 29, 1, 1, 1), )
if mibBuilder.loadTexts: ieee8021PreemptionParameterTable.setStatus('current')
ieee8021PreemptionParameterEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 29, 1, 1, 1, 1), ).setIndexNames((0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBaseComponentId"), (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePort"), (0, "IEEE8021-Preemption-MIB", "ieee8021PreemptionPriority"))
if mibBuilder.loadTexts: ieee8021PreemptionParameterEntry.setStatus('current')
ieee8021PreemptionPriority = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 29, 1, 1, 1, 1, 1), IEEE8021PriorityValue())
if mibBuilder.loadTexts: ieee8021PreemptionPriority.setStatus('current')
ieee8021FramePreemptionAdminStatus = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 29, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("express", 1), ("preemptible", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021FramePreemptionAdminStatus.setStatus('current')
ieee8021PreemptionConfigTable = MibTable((1, 3, 111, 2, 802, 1, 1, 29, 1, 1, 2), )
if mibBuilder.loadTexts: ieee8021PreemptionConfigTable.setStatus('current')
ieee8021PreemptionConfigEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 29, 1, 1, 2, 1), ).setIndexNames((0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBaseComponentId"), (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePort"))
if mibBuilder.loadTexts: ieee8021PreemptionConfigEntry.setStatus('current')
ieee8021FramePreemptionHoldAdvance = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 29, 1, 1, 2, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021FramePreemptionHoldAdvance.setStatus('current')
ieee8021FramePreemptionReleaseAdvance = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 29, 1, 1, 2, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021FramePreemptionReleaseAdvance.setStatus('current')
ieee8021FramePreemptionActive = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 29, 1, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("idle", 1), ("active", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021FramePreemptionActive.setStatus('current')
ieee8021FramePreemptionHoldRequest = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 29, 1, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("hold", 1), ("release", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021FramePreemptionHoldRequest.setStatus('current')
ieee8021PreemptionCompliances = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 29, 2, 1))
ieee8021PreemptionGroups = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 29, 2, 2))
ieee8021PreemptionGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 29, 2, 2, 1)).setObjects(("IEEE8021-Preemption-MIB", "ieee8021FramePreemptionAdminStatus"), ("IEEE8021-Preemption-MIB", "ieee8021FramePreemptionHoldAdvance"), ("IEEE8021-Preemption-MIB", "ieee8021FramePreemptionReleaseAdvance"), ("IEEE8021-Preemption-MIB", "ieee8021FramePreemptionActive"), ("IEEE8021-Preemption-MIB", "ieee8021FramePreemptionHoldRequest"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021PreemptionGroup = ieee8021PreemptionGroup.setStatus('current')
ieee8021PreemptionCompliance = ModuleCompliance((1, 3, 111, 2, 802, 1, 1, 29, 2, 1, 1)).setObjects(("IEEE8021-Preemption-MIB", "ieee8021PreemptionGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021PreemptionCompliance = ieee8021PreemptionCompliance.setStatus('current')
mibBuilder.exportSymbols("IEEE8021-Preemption-MIB", ieee8021PreemptionParameterEntry=ieee8021PreemptionParameterEntry, ieee8021PreemptionParameters=ieee8021PreemptionParameters, ieee8021FramePreemptionHoldRequest=ieee8021FramePreemptionHoldRequest, PYSNMP_MODULE_ID=ieee8021PreemptionMib, ieee8021FramePreemptionReleaseAdvance=ieee8021FramePreemptionReleaseAdvance, ieee8021PreemptionMib=ieee8021PreemptionMib, ieee8021FramePreemptionAdminStatus=ieee8021FramePreemptionAdminStatus, ieee8021PreemptionPriority=ieee8021PreemptionPriority, ieee8021FramePreemptionActive=ieee8021FramePreemptionActive, ieee8021FramePreemptionHoldAdvance=ieee8021FramePreemptionHoldAdvance, ieee8021PreemptionGroups=ieee8021PreemptionGroups, ieee8021PreemptionParameterTable=ieee8021PreemptionParameterTable, ieee8021PreemptionCompliance=ieee8021PreemptionCompliance, ieee8021PreemptionNotifications=ieee8021PreemptionNotifications, ieee8021PreemptionConfigEntry=ieee8021PreemptionConfigEntry, ieee8021PreemptionObjects=ieee8021PreemptionObjects, ieee8021PreemptionGroup=ieee8021PreemptionGroup, ieee8021PreemptionCompliances=ieee8021PreemptionCompliances, ieee8021PreemptionConformance=ieee8021PreemptionConformance, ieee8021PreemptionConfigTable=ieee8021PreemptionConfigTable)
