#
# PySNMP MIB module CTINB2-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTINB2-MIB
# Produced by pysmi-1.1.3 at Sun Nov 28 20:25:16 2021
# On host fv-az77-612 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
ctINBinfo2, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctINBinfo2")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Bits, ObjectIdentity, Counter32, NotificationType, Unsigned32, Integer32, iso, TimeTicks, Counter64, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Bits", "ObjectIdentity", "Counter32", "NotificationType", "Unsigned32", "Integer32", "iso", "TimeTicks", "Counter64", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ctInbUtil = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 2, 1))
ctInbUtilInterval = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 2, 1, 1), Integer32().clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctInbUtilInterval.setStatus('mandatory')
ctInbUtilTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 2, 1, 2), )
if mibBuilder.loadTexts: ctInbUtilTable.setStatus('mandatory')
ctInbUtilEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 2, 1, 2, 1), ).setIndexNames((0, "CTINB2-MIB", "ctInbUtilSrcSlot"), (0, "CTINB2-MIB", "ctInbUtilDestSlot"))
if mibBuilder.loadTexts: ctInbUtilEntry.setStatus('mandatory')
ctInbUtilSrcSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 2, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctInbUtilSrcSlot.setStatus('mandatory')
ctInbUtilDestSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 2, 1, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctInbUtilDestSlot.setStatus('mandatory')
ctInbUtilHiByteCountA = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 2, 1, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctInbUtilHiByteCountA.setStatus('mandatory')
ctInbUtilLoByteCountA = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 2, 1, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctInbUtilLoByteCountA.setStatus('mandatory')
ctInbUtilHiByteCountB = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 2, 1, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctInbUtilHiByteCountB.setStatus('mandatory')
ctInbUtilLoByteCountB = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 2, 1, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctInbUtilLoByteCountB.setStatus('mandatory')
ctInbUtilAbsoluteA = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 2, 1, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctInbUtilAbsoluteA.setStatus('mandatory')
ctInbUtilAbsoluteB = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 2, 1, 2, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctInbUtilAbsoluteB.setStatus('mandatory')
ctInbUtilAbsoluteTotal = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 2, 1, 2, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctInbUtilAbsoluteTotal.setStatus('mandatory')
mibBuilder.exportSymbols("CTINB2-MIB", ctInbUtilDestSlot=ctInbUtilDestSlot, ctInbUtilSrcSlot=ctInbUtilSrcSlot, ctInbUtilInterval=ctInbUtilInterval, ctInbUtilHiByteCountA=ctInbUtilHiByteCountA, ctInbUtilHiByteCountB=ctInbUtilHiByteCountB, ctInbUtilAbsoluteB=ctInbUtilAbsoluteB, ctInbUtilEntry=ctInbUtilEntry, ctInbUtil=ctInbUtil, ctInbUtilTable=ctInbUtilTable, ctInbUtilAbsoluteTotal=ctInbUtilAbsoluteTotal, ctInbUtilLoByteCountA=ctInbUtilLoByteCountA, ctInbUtilLoByteCountB=ctInbUtilLoByteCountB, ctInbUtilAbsoluteA=ctInbUtilAbsoluteA)
