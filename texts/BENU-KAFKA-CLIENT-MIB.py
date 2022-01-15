#
# PySNMP MIB module BENU-KAFKA-CLIENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/benuos/BENU-KAFKA-CLIENT-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 17:52:56 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
benuWAG, = mibBuilder.importSymbols("BENU-WAG-MIB", "benuWAG")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, Gauge32, ObjectIdentity, ModuleIdentity, Unsigned32, MibIdentifier, NotificationType, IpAddress, iso, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, TimeTicks, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Gauge32", "ObjectIdentity", "ModuleIdentity", "Unsigned32", "MibIdentifier", "NotificationType", "IpAddress", "iso", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "TimeTicks", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
benuKafkaClientMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 39406, 2, 1, 12))
benuKafkaClientMIB.setRevisions(('2015-10-21 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: benuKafkaClientMIB.setRevisionsDescriptions(('Initial Version',))
if mibBuilder.loadTexts: benuKafkaClientMIB.setLastUpdated('201510210000Z')
if mibBuilder.loadTexts: benuKafkaClientMIB.setOrganization('Benu Networks,Inc')
if mibBuilder.loadTexts: benuKafkaClientMIB.setContactInfo('Benu Networks,Inc\n                          Corporate Headquarters\n                          300 Concord Road, Suite 110\n                          Billerica, MA 01821 USA\n                          Tel: +1 978-223-4700\n                          Fax: +1 978-362-1908\n                          Email: info@benunets.com')
if mibBuilder.loadTexts: benuKafkaClientMIB.setDescription('This MIB module defines management information\n                related to the KAFKA client.\n\n                Copyright (C)  2013 by Benu Networks, Inc.\n                All rights reserved.')
bKafkaClientObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 39406, 2, 1, 12, 1))
if mibBuilder.loadTexts: bKafkaClientObjects.setStatus('current')
if mibBuilder.loadTexts: bKafkaClientObjects.setDescription('KAFKA client information is defined in this branch.')
bKafkaClientLatencyTable = MibTable((1, 3, 6, 1, 4, 1, 39406, 2, 1, 12, 1, 1), )
if mibBuilder.loadTexts: bKafkaClientLatencyTable.setStatus('current')
if mibBuilder.loadTexts: bKafkaClientLatencyTable.setDescription('Latency information list for KAFKA client.')
bKafkaClientLatencyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 39406, 2, 1, 12, 1, 1, 1), ).setIndexNames((0, "BENU-KAFKA-CLIENT-MIB", "bKafkaClientLatencyStatsInterval"))
if mibBuilder.loadTexts: bKafkaClientLatencyEntry.setStatus('current')
if mibBuilder.loadTexts: bKafkaClientLatencyEntry.setDescription('A logical row in the bKafkaClientLatencyTable.')
bKafkaClientLatencyStatsInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 12, 1, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: bKafkaClientLatencyStatsInterval.setStatus('current')
if mibBuilder.loadTexts: bKafkaClientLatencyStatsInterval.setDescription('The interval during which the measurements were accumulated. The\n       interval index one indicates the latest interval for which statistics\n       accumulation was completed. Older the statistics data, greater the interval\n       index value.\n       In a system supporting a history of n intervals with IntervalCount(1)\n       and IntervalCount(n), the most and least recent intervals respectively, the\n       following applies at the end of an interval:\n       - discard the value of IntervalCount(n)\n       - the value of IntervalCount(i) becomes that of IntervalCount(i+1) for\n         1 <= i < n\n       - the value of IntervalCount(1) becomes that of CurrentCount.')
bKafkaClientLatencyStatsIntervalDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 12, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bKafkaClientLatencyStatsIntervalDuration.setStatus('current')
if mibBuilder.loadTexts: bKafkaClientLatencyStatsIntervalDuration.setDescription('Kafka client latency stats interval duration.')
bKafkaClientLatencyTotalPktCount = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 12, 1, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bKafkaClientLatencyTotalPktCount.setStatus('current')
if mibBuilder.loadTexts: bKafkaClientLatencyTotalPktCount.setDescription('The count of total number of packets handled by Kafka client.')
bKafkaClientLatencyMaxProcessingTime = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 12, 1, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bKafkaClientLatencyMaxProcessingTime.setStatus('current')
if mibBuilder.loadTexts: bKafkaClientLatencyMaxProcessingTime.setDescription('Maximum packet processing time handled by Kafka client in micro seconds.')
bKafkaClientLatencyMinProcessingTime = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 12, 1, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bKafkaClientLatencyMinProcessingTime.setStatus('current')
if mibBuilder.loadTexts: bKafkaClientLatencyMinProcessingTime.setDescription('Minimum packet processing time handled by Kafka client in micro seconds.')
bKafkaClientLatencyAvgProcessingTime = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 12, 1, 1, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bKafkaClientLatencyAvgProcessingTime.setStatus('current')
if mibBuilder.loadTexts: bKafkaClientLatencyAvgProcessingTime.setDescription('Average packet processing time handled by Kafka client in micro seconds.')
bKafkaClientLatencyProcessTimeMorethan1MSPktCount = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 12, 1, 1, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bKafkaClientLatencyProcessTimeMorethan1MSPktCount.setStatus('current')
if mibBuilder.loadTexts: bKafkaClientLatencyProcessTimeMorethan1MSPktCount.setDescription('Number of packets took more than 1 milli second processing time handled by Kafka client.')
mibBuilder.exportSymbols("BENU-KAFKA-CLIENT-MIB", bKafkaClientLatencyStatsInterval=bKafkaClientLatencyStatsInterval, bKafkaClientLatencyMinProcessingTime=bKafkaClientLatencyMinProcessingTime, bKafkaClientObjects=bKafkaClientObjects, bKafkaClientLatencyMaxProcessingTime=bKafkaClientLatencyMaxProcessingTime, bKafkaClientLatencyProcessTimeMorethan1MSPktCount=bKafkaClientLatencyProcessTimeMorethan1MSPktCount, benuKafkaClientMIB=benuKafkaClientMIB, bKafkaClientLatencyTable=bKafkaClientLatencyTable, bKafkaClientLatencyTotalPktCount=bKafkaClientLatencyTotalPktCount, bKafkaClientLatencyStatsIntervalDuration=bKafkaClientLatencyStatsIntervalDuration, PYSNMP_MODULE_ID=benuKafkaClientMIB, bKafkaClientLatencyEntry=bKafkaClientLatencyEntry, bKafkaClientLatencyAvgProcessingTime=bKafkaClientLatencyAvgProcessingTime)
