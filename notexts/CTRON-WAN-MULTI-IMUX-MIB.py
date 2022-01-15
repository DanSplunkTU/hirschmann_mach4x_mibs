#
# PySNMP MIB module CTRON-WAN-MULTI-IMUX-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-WAN-MULTI-IMUX-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 18:01:45 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
ctWanServices, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctWanServices")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, Gauge32, ModuleIdentity, MibIdentifier, TimeTicks, Unsigned32, Integer32, Bits, Counter32, Counter64, NotificationType, IpAddress, iso, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Gauge32", "ModuleIdentity", "MibIdentifier", "TimeTicks", "Unsigned32", "Integer32", "Bits", "Counter32", "Counter64", "NotificationType", "IpAddress", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ctWanMultiMux = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 2))
ctWANMMuxGeneralGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 2, 1))
ctWANMMuxMaxNum = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctWANMMuxMaxNum.setStatus('mandatory')
ctWanMMuxTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 2, 2), )
if mibBuilder.loadTexts: ctWanMMuxTable.setStatus('mandatory')
ctWanMMuxEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 2, 2, 1), ).setIndexNames((0, "CTRON-WAN-MULTI-IMUX-MIB", "ctWanMMuxId"))
if mibBuilder.loadTexts: ctWanMMuxEntry.setStatus('mandatory')
ctWanMMuxId = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctWanMMuxId.setStatus('mandatory')
ctWanMMuxIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctWanMMuxIfIndex.setStatus('mandatory')
ctWanMMuxMaxNumGroups = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 2, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctWanMMuxMaxNumGroups.setStatus('mandatory')
ctWanMMuxAdmin = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 2, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctWanMMuxAdmin.setStatus('mandatory')
ctWanMMuxGroupTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 2, 3), )
if mibBuilder.loadTexts: ctWanMMuxGroupTable.setStatus('mandatory')
ctWanMMuxGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 2, 3, 1), ).setIndexNames((0, "CTRON-WAN-MULTI-IMUX-MIB", "ctWanMMuxGroupMMuxId"), (0, "CTRON-WAN-MULTI-IMUX-MIB", "ctWanMMuxGroupId"))
if mibBuilder.loadTexts: ctWanMMuxGroupEntry.setStatus('mandatory')
ctWanMMuxGroupMMuxId = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 2, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctWanMMuxGroupMMuxId.setStatus('mandatory')
ctWanMMuxGroupId = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 2, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctWanMMuxGroupId.setStatus('mandatory')
ctWanMMuxGroupAdmin = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 2, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctWanMMuxGroupAdmin.setStatus('mandatory')
ctWanMMuxGroupNumChannels = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 2, 3, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctWanMMuxGroupNumChannels.setStatus('mandatory')
ctWanMMuxGroupAddChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 2, 3, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctWanMMuxGroupAddChannel.setStatus('mandatory')
ctWanMMuxGroupDelChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 2, 3, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctWanMMuxGroupDelChannel.setStatus('mandatory')
ctWanMMuxChannelTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 2, 4), )
if mibBuilder.loadTexts: ctWanMMuxChannelTable.setStatus('mandatory')
ctWanMMuxChannelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 2, 4, 1), ).setIndexNames((0, "CTRON-WAN-MULTI-IMUX-MIB", "ctWanMMuxChannelMMuxId"), (0, "CTRON-WAN-MULTI-IMUX-MIB", "ctWanMMuxChannelGroupId"), (0, "CTRON-WAN-MULTI-IMUX-MIB", "ctWanMMuxChannelId"))
if mibBuilder.loadTexts: ctWanMMuxChannelEntry.setStatus('mandatory')
ctWanMMuxChannelMMuxId = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 2, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctWanMMuxChannelMMuxId.setStatus('mandatory')
ctWanMMuxChannelGroupId = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 2, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctWanMMuxChannelGroupId.setStatus('mandatory')
ctWanMMuxChannelId = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 2, 4, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctWanMMuxChannelId.setStatus('mandatory')
ctWanMMuxChannelIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 2, 4, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctWanMMuxChannelIfIndex.setStatus('mandatory')
ctWanMMuxChannelPhysNum = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 2, 4, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctWanMMuxChannelPhysNum.setStatus('mandatory')
ctWanMMuxChannelBwAvail = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 2, 4, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctWanMMuxChannelBwAvail.setStatus('mandatory')
ctWanMMuxChannelByteCount = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 2, 4, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctWanMMuxChannelByteCount.setStatus('mandatory')
ctWanMMuxChannelStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 2, 4, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("inactive", 1), ("active", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctWanMMuxChannelStatus.setStatus('mandatory')
mibBuilder.exportSymbols("CTRON-WAN-MULTI-IMUX-MIB", ctWanMMuxChannelBwAvail=ctWanMMuxChannelBwAvail, ctWanMMuxIfIndex=ctWanMMuxIfIndex, ctWanMMuxGroupMMuxId=ctWanMMuxGroupMMuxId, ctWanMMuxChannelId=ctWanMMuxChannelId, ctWanMMuxGroupNumChannels=ctWanMMuxGroupNumChannels, ctWanMMuxChannelIfIndex=ctWanMMuxChannelIfIndex, ctWanMMuxGroupAdmin=ctWanMMuxGroupAdmin, ctWanMMuxId=ctWanMMuxId, ctWanMMuxChannelPhysNum=ctWanMMuxChannelPhysNum, ctWanMMuxChannelStatus=ctWanMMuxChannelStatus, ctWanMMuxChannelByteCount=ctWanMMuxChannelByteCount, ctWanMMuxChannelMMuxId=ctWanMMuxChannelMMuxId, ctWanMMuxEntry=ctWanMMuxEntry, ctWanMultiMux=ctWanMultiMux, ctWanMMuxGroupEntry=ctWanMMuxGroupEntry, ctWanMMuxChannelTable=ctWanMMuxChannelTable, ctWANMMuxGeneralGroup=ctWANMMuxGeneralGroup, ctWanMMuxGroupAddChannel=ctWanMMuxGroupAddChannel, ctWanMMuxGroupTable=ctWanMMuxGroupTable, ctWanMMuxGroupDelChannel=ctWanMMuxGroupDelChannel, ctWanMMuxTable=ctWanMMuxTable, ctWanMMuxChannelGroupId=ctWanMMuxChannelGroupId, ctWanMMuxAdmin=ctWanMMuxAdmin, ctWanMMuxChannelEntry=ctWanMMuxChannelEntry, ctWanMMuxMaxNumGroups=ctWanMMuxMaxNumGroups, ctWanMMuxGroupId=ctWanMMuxGroupId, ctWANMMuxMaxNum=ctWANMMuxMaxNum)
