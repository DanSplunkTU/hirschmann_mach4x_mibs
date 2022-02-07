#
# PySNMP MIB module ARRIS-C3-IF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/arris/ARRIS-C3-IF-MIB
# Produced by pysmi-1.1.8 at Mon Feb  7 16:07:37 2022
# On host fv-az42-619 platform Linux version 5.11.0-1028-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
cmtsC3, = mibBuilder.importSymbols("ARRIS-MIB", "cmtsC3")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
ifEntry, = mibBuilder.importSymbols("IF-MIB", "ifEntry")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
TimeTicks, ModuleIdentity, Integer32, NotificationType, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Gauge32, Unsigned32, Counter32, ObjectIdentity, IpAddress, iso, enterprises, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "ModuleIdentity", "Integer32", "NotificationType", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Gauge32", "Unsigned32", "Counter32", "ObjectIdentity", "IpAddress", "iso", "enterprises", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cmtsC3IfMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 12))
if mibBuilder.loadTexts: cmtsC3IfMIB.setLastUpdated('200308200000Z')
if mibBuilder.loadTexts: cmtsC3IfMIB.setOrganization('Arris International')
dcxIfObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 12, 1))
dcxIfTable = MibTable((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 12, 1, 1), )
if mibBuilder.loadTexts: dcxIfTable.setStatus('current')
dcxIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 12, 1, 1, 1), )
ifEntry.registerAugmentions(("ARRIS-C3-IF-MIB", "dcxIfEntry"))
dcxIfEntry.setIndexNames(*ifEntry.getIndexNames())
if mibBuilder.loadTexts: dcxIfEntry.setStatus('current')
dcxIfLoadInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 12, 1, 1, 1, 1), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxIfLoadInterval.setStatus('current')
dcxIfInputBitRate = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 12, 1, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dcxIfInputBitRate.setStatus('current')
dcxIfInputPacketRate = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 12, 1, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dcxIfInputPacketRate.setStatus('current')
dcxIfOutputBitRate = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 12, 1, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dcxIfOutputBitRate.setStatus('current')
dcxIfOutputPacketRate = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 12, 1, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dcxIfOutputPacketRate.setStatus('current')
mibBuilder.exportSymbols("ARRIS-C3-IF-MIB", dcxIfEntry=dcxIfEntry, dcxIfOutputBitRate=dcxIfOutputBitRate, PYSNMP_MODULE_ID=cmtsC3IfMIB, dcxIfTable=dcxIfTable, dcxIfOutputPacketRate=dcxIfOutputPacketRate, dcxIfLoadInterval=dcxIfLoadInterval, dcxIfInputBitRate=dcxIfInputBitRate, dcxIfInputPacketRate=dcxIfInputPacketRate, cmtsC3IfMIB=cmtsC3IfMIB, dcxIfObjects=dcxIfObjects)
