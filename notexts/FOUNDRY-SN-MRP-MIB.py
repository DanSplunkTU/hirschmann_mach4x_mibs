#
# PySNMP MIB module FOUNDRY-SN-MRP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/foundry/FOUNDRY-SN-MRP-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:21:34 2022
# On host fv-az36-988 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, Gauge32, NotificationType, ModuleIdentity, TimeTicks, Counter64, ObjectIdentity, Unsigned32, Bits, MibIdentifier, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Gauge32", "NotificationType", "ModuleIdentity", "TimeTicks", "Counter64", "ObjectIdentity", "Unsigned32", "Bits", "MibIdentifier", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
snMetroRing = ModuleIdentity((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 29))
snMetroRing.setRevisions(('2007-05-16 00:00',))
if mibBuilder.loadTexts: snMetroRing.setLastUpdated('200705160000Z')
if mibBuilder.loadTexts: snMetroRing.setOrganization('Foundry Networks, Inc')
snMetroRingGlobalObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 29, 1))
snMetroRingTableObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 29, 2))
snMetroRingTable = MibTable((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 29, 2, 1), )
if mibBuilder.loadTexts: snMetroRingTable.setStatus('current')
snMetroRingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 29, 2, 1, 1), ).setIndexNames((0, "FOUNDRY-SN-MRP-MIB", "snMetroRingVLanId"), (0, "FOUNDRY-SN-MRP-MIB", "snMetroRingId"))
if mibBuilder.loadTexts: snMetroRingEntry.setStatus('current')
snMetroRingVLanId = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 29, 2, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: snMetroRingVLanId.setStatus('current')
snMetroRingId = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 29, 2, 1, 1, 2), Integer32())
if mibBuilder.loadTexts: snMetroRingId.setStatus('current')
snMetroRingConfigState = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 29, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("enabled", 2), ("disabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snMetroRingConfigState.setStatus('current')
snMetroRingRole = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 29, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("master", 2), ("member", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snMetroRingRole.setStatus('current')
snMetroRingHelloTime = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 29, 2, 1, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snMetroRingHelloTime.setStatus('current')
snMetroRingPreforwardingTime = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 29, 2, 1, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snMetroRingPreforwardingTime.setStatus('current')
snMetroRingPort1 = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 29, 2, 1, 1, 7), InterfaceIndex()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snMetroRingPort1.setStatus('current')
snMetroRingPort2 = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 29, 2, 1, 1, 8), InterfaceIndex()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snMetroRingPort2.setStatus('current')
snMetroRingName = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 29, 2, 1, 1, 9), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snMetroRingName.setStatus('current')
snMetroRingRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 29, 2, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("valid", 2), ("delete", 3), ("create", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snMetroRingRowStatus.setStatus('current')
snMetroRingOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 29, 2, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("enabled", 2), ("disabled", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snMetroRingOperState.setStatus('current')
snMetroRingTopoGroupId = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 29, 2, 1, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snMetroRingTopoGroupId.setStatus('current')
snMetroRingRHPTransmitted = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 29, 2, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snMetroRingRHPTransmitted.setStatus('current')
snMetroRingRHPReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 29, 2, 1, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snMetroRingRHPReceived.setStatus('current')
snMetroRingStateChanged = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 29, 2, 1, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snMetroRingStateChanged.setStatus('current')
snMetroRingTCRBPDUReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 29, 2, 1, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snMetroRingTCRBPDUReceived.setStatus('current')
snMetroRingPriPort = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 29, 2, 1, 1, 17), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snMetroRingPriPort.setStatus('current')
snMetroRingSecPort = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 29, 2, 1, 1, 18), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snMetroRingSecPort.setStatus('current')
snMetroRingPriPortState = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 29, 2, 1, 1, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("preforwarding", 2), ("forwarding", 3), ("blocking", 4), ("disabled", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snMetroRingPriPortState.setStatus('current')
snMetroRingSecPortState = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 29, 2, 1, 1, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("preforwarding", 2), ("forwarding", 3), ("blocking", 4), ("disabled", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snMetroRingSecPortState.setStatus('current')
snMetroRingPriPortType = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 29, 2, 1, 1, 21), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("regular", 2), ("tunnel", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snMetroRingPriPortType.setStatus('current')
snMetroRingSecPortType = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 29, 2, 1, 1, 22), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("regular", 2), ("tunnel", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snMetroRingSecPortType.setStatus('current')
snMetroRingPriPortActivePort = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 29, 2, 1, 1, 23), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snMetroRingPriPortActivePort.setStatus('current')
snMetroRingSecPortActivePort = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 29, 2, 1, 1, 24), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snMetroRingSecPortActivePort.setStatus('current')
mibBuilder.exportSymbols("FOUNDRY-SN-MRP-MIB", snMetroRingTopoGroupId=snMetroRingTopoGroupId, snMetroRingTable=snMetroRingTable, snMetroRingRowStatus=snMetroRingRowStatus, snMetroRingStateChanged=snMetroRingStateChanged, snMetroRingId=snMetroRingId, snMetroRingRole=snMetroRingRole, snMetroRingTableObjects=snMetroRingTableObjects, snMetroRingName=snMetroRingName, PYSNMP_MODULE_ID=snMetroRing, snMetroRingPriPort=snMetroRingPriPort, snMetroRingPriPortActivePort=snMetroRingPriPortActivePort, snMetroRingPort2=snMetroRingPort2, snMetroRingOperState=snMetroRingOperState, snMetroRingRHPReceived=snMetroRingRHPReceived, snMetroRingEntry=snMetroRingEntry, snMetroRingPriPortType=snMetroRingPriPortType, snMetroRingPriPortState=snMetroRingPriPortState, snMetroRingConfigState=snMetroRingConfigState, snMetroRingSecPortState=snMetroRingSecPortState, snMetroRingVLanId=snMetroRingVLanId, snMetroRingSecPortType=snMetroRingSecPortType, snMetroRingHelloTime=snMetroRingHelloTime, snMetroRing=snMetroRing, snMetroRingTCRBPDUReceived=snMetroRingTCRBPDUReceived, snMetroRingPort1=snMetroRingPort1, snMetroRingSecPort=snMetroRingSecPort, snMetroRingSecPortActivePort=snMetroRingSecPortActivePort, snMetroRingGlobalObjects=snMetroRingGlobalObjects, snMetroRingPreforwardingTime=snMetroRingPreforwardingTime, snMetroRingRHPTransmitted=snMetroRingRHPTransmitted)
