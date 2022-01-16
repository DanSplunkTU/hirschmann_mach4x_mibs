#
# PySNMP MIB module BENU-KAFKA-CLIENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/benuos/BENU-KAFKA-CLIENT-MIB
# Produced by pysmi-1.1.8 at Sun Jan 16 00:32:19 2022
# On host fv-az42-839 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
benuWAG, = mibBuilder.importSymbols("BENU-WAG-MIB", "benuWAG")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, iso, Integer32, Gauge32, MibIdentifier, Bits, TimeTicks, IpAddress, ObjectIdentity, NotificationType, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "iso", "Integer32", "Gauge32", "MibIdentifier", "Bits", "TimeTicks", "IpAddress", "ObjectIdentity", "NotificationType", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
benuKafkaClientMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 39406, 2, 1, 12))
benuKafkaClientMIB.setRevisions(('2015-10-21 00:00',))
if mibBuilder.loadTexts: benuKafkaClientMIB.setLastUpdated('201510210000Z')
if mibBuilder.loadTexts: benuKafkaClientMIB.setOrganization('Benu Networks,Inc')
bKafkaClientObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 39406, 2, 1, 12, 1))
if mibBuilder.loadTexts: bKafkaClientObjects.setStatus('current')
bKafkaClientLatencyTable = MibTable((1, 3, 6, 1, 4, 1, 39406, 2, 1, 12, 1, 1), )
if mibBuilder.loadTexts: bKafkaClientLatencyTable.setStatus('current')
bKafkaClientLatencyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 39406, 2, 1, 12, 1, 1, 1), ).setIndexNames((0, "BENU-KAFKA-CLIENT-MIB", "bKafkaClientLatencyStatsInterval"))
if mibBuilder.loadTexts: bKafkaClientLatencyEntry.setStatus('current')
bKafkaClientLatencyStatsInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 12, 1, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: bKafkaClientLatencyStatsInterval.setStatus('current')
bKafkaClientLatencyStatsIntervalDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 12, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bKafkaClientLatencyStatsIntervalDuration.setStatus('current')
bKafkaClientLatencyTotalPktCount = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 12, 1, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bKafkaClientLatencyTotalPktCount.setStatus('current')
bKafkaClientLatencyMaxProcessingTime = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 12, 1, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bKafkaClientLatencyMaxProcessingTime.setStatus('current')
bKafkaClientLatencyMinProcessingTime = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 12, 1, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bKafkaClientLatencyMinProcessingTime.setStatus('current')
bKafkaClientLatencyAvgProcessingTime = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 12, 1, 1, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bKafkaClientLatencyAvgProcessingTime.setStatus('current')
bKafkaClientLatencyProcessTimeMorethan1MSPktCount = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 12, 1, 1, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bKafkaClientLatencyProcessTimeMorethan1MSPktCount.setStatus('current')
mibBuilder.exportSymbols("BENU-KAFKA-CLIENT-MIB", bKafkaClientLatencyTotalPktCount=bKafkaClientLatencyTotalPktCount, PYSNMP_MODULE_ID=benuKafkaClientMIB, bKafkaClientObjects=bKafkaClientObjects, bKafkaClientLatencyTable=bKafkaClientLatencyTable, bKafkaClientLatencyStatsIntervalDuration=bKafkaClientLatencyStatsIntervalDuration, bKafkaClientLatencyMaxProcessingTime=bKafkaClientLatencyMaxProcessingTime, bKafkaClientLatencyEntry=bKafkaClientLatencyEntry, bKafkaClientLatencyAvgProcessingTime=bKafkaClientLatencyAvgProcessingTime, bKafkaClientLatencyMinProcessingTime=bKafkaClientLatencyMinProcessingTime, benuKafkaClientMIB=benuKafkaClientMIB, bKafkaClientLatencyProcessTimeMorethan1MSPktCount=bKafkaClientLatencyProcessTimeMorethan1MSPktCount, bKafkaClientLatencyStatsInterval=bKafkaClientLatencyStatsInterval)
