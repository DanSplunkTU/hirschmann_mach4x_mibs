#
# PySNMP MIB module CTRON-TX-QUEUE-ARBITRATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-TX-QUEUE-ARBITRATION-MIB
# Produced by pysmi-1.1.8 at Mon Feb  7 16:12:01 2022
# On host fv-az42-619 platform Linux version 5.11.0-1028-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
ctTxQArb, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctTxQArb")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, Bits, ObjectIdentity, ModuleIdentity, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, MibIdentifier, Counter64, Gauge32, Counter32, IpAddress, TimeTicks, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Bits", "ObjectIdentity", "ModuleIdentity", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "MibIdentifier", "Counter64", "Gauge32", "Counter32", "IpAddress", "TimeTicks", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ctTxQArbConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 12, 1))
ctTxQBufferConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 12, 2))
ctTxQPortGroupMapTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 12, 1, 1), )
if mibBuilder.loadTexts: ctTxQPortGroupMapTable.setStatus('mandatory')
ctTxQPortGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 12, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: ctTxQPortGroupEntry.setStatus('mandatory')
ctTxQPortGroup = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 12, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctTxQPortGroup.setStatus('mandatory')
ctTxQArbTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 12, 1, 2), )
if mibBuilder.loadTexts: ctTxQArbTable.setStatus('mandatory')
ctTxQArbEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 12, 1, 2, 1), ).setIndexNames((0, "CTRON-TX-QUEUE-ARBITRATION-MIB", "ctTxQPortGroup"))
if mibBuilder.loadTexts: ctTxQArbEntry.setStatus('mandatory')
ctTxQArbNumQueues = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 12, 1, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctTxQArbNumQueues.setStatus('mandatory')
ctTxQArbNumSlices = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 12, 1, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctTxQArbNumSlices.setStatus('mandatory')
ctTxQArbSetting = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 12, 1, 2, 1, 4), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTxQArbSetting.setStatus('mandatory')
ctTxQBufferOptimizeEnable = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 12, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTxQBufferOptimizeEnable.setStatus('optional')
mibBuilder.exportSymbols("CTRON-TX-QUEUE-ARBITRATION-MIB", ctTxQArbNumQueues=ctTxQArbNumQueues, ctTxQPortGroupMapTable=ctTxQPortGroupMapTable, ctTxQBufferOptimizeEnable=ctTxQBufferOptimizeEnable, ctTxQArbTable=ctTxQArbTable, ctTxQArbEntry=ctTxQArbEntry, ctTxQArbNumSlices=ctTxQArbNumSlices, ctTxQPortGroupEntry=ctTxQPortGroupEntry, ctTxQArbConfig=ctTxQArbConfig, ctTxQArbSetting=ctTxQArbSetting, ctTxQBufferConfig=ctTxQBufferConfig, ctTxQPortGroup=ctTxQPortGroup)
