#
# PySNMP MIB module RADLAN-MAC-BASE-PRIO (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/radlan/RADLAN-MAC-BASE-PRIO
# Produced by pysmi-1.1.3 at Sun Nov 21 00:45:13 2021
# On host fv-az39-63 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
rnd, = mibBuilder.importSymbols("RADLAN-MIB", "rnd")
RowStatus, = mibBuilder.importSymbols("RADLAN-SNMPv2", "RowStatus")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, TimeTicks, NotificationType, Counter64, Gauge32, ObjectIdentity, MibIdentifier, Bits, ModuleIdentity, Integer32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "TimeTicks", "NotificationType", "Counter64", "Gauge32", "ObjectIdentity", "MibIdentifier", "Bits", "ModuleIdentity", "Integer32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Unsigned32")
MacAddress, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "TextualConvention", "DisplayString")
rlMacBasePrio = MibIdentifier((1, 3, 6, 1, 4, 1, 89, 101))
rlMacBasePrioMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 89, 101, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlMacBasePrioMibVersion.setStatus('current')
rlMacBasePrioSupport = MibScalar((1, 3, 6, 1, 4, 1, 89, 101, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlMacBasePrioSupport.setStatus('current')
rlMacBasePrioForceL3CosEnable = MibScalar((1, 3, 6, 1, 4, 1, 89, 101, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlMacBasePrioForceL3CosEnable.setStatus('current')
rlMacBasePrioForceL3CosTable = MibTable((1, 3, 6, 1, 4, 1, 89, 101, 4), )
if mibBuilder.loadTexts: rlMacBasePrioForceL3CosTable.setStatus('current')
rlMacBasePrioForceL3CosEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 101, 4, 1), ).setIndexNames((0, "RADLAN-MAC-BASE-PRIO", "rlMacBasePrioForceL3CosAddress"), (0, "RADLAN-MAC-BASE-PRIO", "rlMacBasePrioForceL3CosMask"))
if mibBuilder.loadTexts: rlMacBasePrioForceL3CosEntry.setStatus('current')
rlMacBasePrioForceL3CosAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 101, 4, 1, 1), MacAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlMacBasePrioForceL3CosAddress.setStatus('current')
rlMacBasePrioForceL3CosMask = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 101, 4, 1, 2), MacAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlMacBasePrioForceL3CosMask.setStatus('current')
rlMacBasePrioForceL3CosRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 101, 4, 1, 3), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlMacBasePrioForceL3CosRowStatus.setStatus('current')
rlMacBasePrioForceL3CosParamsTable = MibTable((1, 3, 6, 1, 4, 1, 89, 101, 5), )
if mibBuilder.loadTexts: rlMacBasePrioForceL3CosParamsTable.setStatus('current')
rlMacBasePrioForceL3CosParamsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 101, 5, 1), ).setIndexNames((0, "RADLAN-MAC-BASE-PRIO", "rlMacBasePrioForceL3CosParamsEntryIndex"))
if mibBuilder.loadTexts: rlMacBasePrioForceL3CosParamsEntry.setStatus('current')
rlMacBasePrioForceL3CosParamsEntryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 101, 5, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlMacBasePrioForceL3CosParamsEntryIndex.setStatus('current')
rlMacBasePrioForceL3CosParamsEntryTC = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 101, 5, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlMacBasePrioForceL3CosParamsEntryTC.setStatus('current')
rlMacBasePrioForceL3CosParamsEntryUP = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 101, 5, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlMacBasePrioForceL3CosParamsEntryUP.setStatus('current')
rlMacBasePrioForceL3CosParamsEntryDSCP = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 101, 5, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlMacBasePrioForceL3CosParamsEntryDSCP.setStatus('current')
rlMacBasePrioSADATCEnable = MibScalar((1, 3, 6, 1, 4, 1, 89, 101, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlMacBasePrioSADATCEnable.setStatus('current')
rlMacBasePrioSADATCTable = MibTable((1, 3, 6, 1, 4, 1, 89, 101, 7), )
if mibBuilder.loadTexts: rlMacBasePrioSADATCTable.setStatus('current')
rlMacBasePrioSADATCEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 101, 7, 1), ).setIndexNames((0, "RADLAN-MAC-BASE-PRIO", "rlMacBasePrioSADATCAddress"), (0, "RADLAN-MAC-BASE-PRIO", "rlMacBasePrioSADATCMask"))
if mibBuilder.loadTexts: rlMacBasePrioSADATCEntry.setStatus('current')
rlMacBasePrioSADATCAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 101, 7, 1, 1), MacAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlMacBasePrioSADATCAddress.setStatus('current')
rlMacBasePrioSADATCMask = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 101, 7, 1, 2), MacAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlMacBasePrioSADATCMask.setStatus('current')
rlMacBasePrioSADATCPrio = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 101, 7, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlMacBasePrioSADATCPrio.setStatus('current')
rlMacBasePrioSADATCRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 101, 7, 1, 4), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlMacBasePrioSADATCRowStatus.setStatus('current')
mibBuilder.exportSymbols("RADLAN-MAC-BASE-PRIO", rlMacBasePrioForceL3CosEnable=rlMacBasePrioForceL3CosEnable, rlMacBasePrioSADATCEntry=rlMacBasePrioSADATCEntry, rlMacBasePrioForceL3CosParamsEntryTC=rlMacBasePrioForceL3CosParamsEntryTC, rlMacBasePrioMibVersion=rlMacBasePrioMibVersion, rlMacBasePrioForceL3CosRowStatus=rlMacBasePrioForceL3CosRowStatus, rlMacBasePrioForceL3CosTable=rlMacBasePrioForceL3CosTable, rlMacBasePrioSADATCMask=rlMacBasePrioSADATCMask, rlMacBasePrioSADATCPrio=rlMacBasePrioSADATCPrio, rlMacBasePrioForceL3CosMask=rlMacBasePrioForceL3CosMask, rlMacBasePrioSADATCTable=rlMacBasePrioSADATCTable, rlMacBasePrioForceL3CosParamsEntryUP=rlMacBasePrioForceL3CosParamsEntryUP, rlMacBasePrioForceL3CosParamsTable=rlMacBasePrioForceL3CosParamsTable, rlMacBasePrioForceL3CosParamsEntryIndex=rlMacBasePrioForceL3CosParamsEntryIndex, rlMacBasePrioForceL3CosParamsEntry=rlMacBasePrioForceL3CosParamsEntry, rlMacBasePrioSADATCAddress=rlMacBasePrioSADATCAddress, rlMacBasePrioForceL3CosEntry=rlMacBasePrioForceL3CosEntry, rlMacBasePrioForceL3CosAddress=rlMacBasePrioForceL3CosAddress, rlMacBasePrioSADATCEnable=rlMacBasePrioSADATCEnable, rlMacBasePrioSupport=rlMacBasePrioSupport, rlMacBasePrioForceL3CosParamsEntryDSCP=rlMacBasePrioForceL3CosParamsEntryDSCP, rlMacBasePrioSADATCRowStatus=rlMacBasePrioSADATCRowStatus, rlMacBasePrio=rlMacBasePrio)
