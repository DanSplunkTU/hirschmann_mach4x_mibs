#
# PySNMP MIB module BENU-HTTP-SERVER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/benuos/BENU-HTTP-SERVER-MIB
# Produced by pysmi-1.1.8 at Mon Feb  7 16:08:05 2022
# On host fv-az42-619 platform Linux version 5.11.0-1028-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
benuWAG, = mibBuilder.importSymbols("BENU-WAG-MIB", "benuWAG")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, TimeTicks, Integer32, Unsigned32, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Counter64, iso, ModuleIdentity, MibIdentifier, Bits, Gauge32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "TimeTicks", "Integer32", "Unsigned32", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Counter64", "iso", "ModuleIdentity", "MibIdentifier", "Bits", "Gauge32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
benuHttpServerMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 39406, 2, 1, 10))
benuHttpServerMIB.setRevisions(('2015-10-21 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: benuHttpServerMIB.setRevisionsDescriptions(('Initial Version',))
if mibBuilder.loadTexts: benuHttpServerMIB.setLastUpdated('201510210000Z')
if mibBuilder.loadTexts: benuHttpServerMIB.setOrganization('Benu Networks,Inc')
if mibBuilder.loadTexts: benuHttpServerMIB.setContactInfo('Benu Networks,Inc\n                          Corporate Headquarters\n                          300 Concord Road, Suite 110\n                          Billerica, MA 01821 USA\n                          Tel: +1 978-223-4700\n                          Fax: +1 978-362-1908\n                          Email: info@benunets.com')
if mibBuilder.loadTexts: benuHttpServerMIB.setDescription('This MIB module defines management information\n                related to the HTTP server.\n\n                Copyright (C)  2013 by Benu Networks, Inc.\n                All rights reserved.')
bHttpServerObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 39406, 2, 1, 10, 1))
if mibBuilder.loadTexts: bHttpServerObjects.setStatus('current')
if mibBuilder.loadTexts: bHttpServerObjects.setDescription('HTTP server information is defined in this branch.')
bHttpServerLatencyTable = MibTable((1, 3, 6, 1, 4, 1, 39406, 2, 1, 10, 1, 1), )
if mibBuilder.loadTexts: bHttpServerLatencyTable.setStatus('current')
if mibBuilder.loadTexts: bHttpServerLatencyTable.setDescription('Latency information list for HTTP server.')
bHttpServerLatencyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 39406, 2, 1, 10, 1, 1, 1), ).setIndexNames((0, "BENU-HTTP-SERVER-MIB", "bHttpServLatencyStatsInterval"))
if mibBuilder.loadTexts: bHttpServerLatencyEntry.setStatus('current')
if mibBuilder.loadTexts: bHttpServerLatencyEntry.setDescription('A logical row in the bHttpServerLatencyTable.')
bHttpServLatencyStatsInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 10, 1, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: bHttpServLatencyStatsInterval.setStatus('current')
if mibBuilder.loadTexts: bHttpServLatencyStatsInterval.setDescription('The interval during which the measurements were accumulated. The\n       interval index one indicates the latest interval for which statistics\n       accumulation was completed. Older the statistics data, greater the interval\n       index value.\n       In a system supporting a history of n intervals with IntervalCount(1)\n       and IntervalCount(n), the most and least recent intervals respectively, the\n       following applies at the end of an interval:\n       - discard the value of IntervalCount(n)\n       - the value of IntervalCount(i) becomes that of IntervalCount(i+1) for\n         1 <= i < n\n       - the value of IntervalCount(1) becomes that of CurrentCount.')
bHttpServLatencyStatsIntervalDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 10, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bHttpServLatencyStatsIntervalDuration.setStatus('current')
if mibBuilder.loadTexts: bHttpServLatencyStatsIntervalDuration.setDescription('Http server latency stats interval duration.')
bHttpServLatencyTotalPktCount = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 10, 1, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bHttpServLatencyTotalPktCount.setStatus('current')
if mibBuilder.loadTexts: bHttpServLatencyTotalPktCount.setDescription('The count of the total number of packets handled by http server.')
bHttpServLatencyMaxProcessingTime = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 10, 1, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bHttpServLatencyMaxProcessingTime.setStatus('current')
if mibBuilder.loadTexts: bHttpServLatencyMaxProcessingTime.setDescription('Maximum packet processing time handled by http server in micro seconds.')
bHttpServLatencyMinProcessingTime = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 10, 1, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bHttpServLatencyMinProcessingTime.setStatus('current')
if mibBuilder.loadTexts: bHttpServLatencyMinProcessingTime.setDescription('Minimum packet processing time handled by http server in micro seconds.')
bHttpServLatencyAvgProcessingTime = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 10, 1, 1, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bHttpServLatencyAvgProcessingTime.setStatus('current')
if mibBuilder.loadTexts: bHttpServLatencyAvgProcessingTime.setDescription('Average packet processing time handled by http server in micro seconds.')
bHttpServLatencyProcessTimeMorethan1MSPktCount = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 10, 1, 1, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bHttpServLatencyProcessTimeMorethan1MSPktCount.setStatus('current')
if mibBuilder.loadTexts: bHttpServLatencyProcessTimeMorethan1MSPktCount.setDescription('Number of packets took more than 1 milli second processing time handled by http server.')
bHttpServLatencyGetTotalPktCount = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 10, 1, 1, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bHttpServLatencyGetTotalPktCount.setStatus('current')
if mibBuilder.loadTexts: bHttpServLatencyGetTotalPktCount.setDescription('The count of the total number of packets handled by http server GET.')
bHttpServLatencyGetMaxProcessingTime = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 10, 1, 1, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bHttpServLatencyGetMaxProcessingTime.setStatus('current')
if mibBuilder.loadTexts: bHttpServLatencyGetMaxProcessingTime.setDescription('Maximum packet processing time handled by http server in micro seconds - GET.')
bHttpServLatencyGetMinProcessingTime = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 10, 1, 1, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bHttpServLatencyGetMinProcessingTime.setStatus('current')
if mibBuilder.loadTexts: bHttpServLatencyGetMinProcessingTime.setDescription('Minimum packet processing time handled by http server in micro seconds - GET.')
bHttpServLatencyGetAvgProcessingTime = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 10, 1, 1, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bHttpServLatencyGetAvgProcessingTime.setStatus('current')
if mibBuilder.loadTexts: bHttpServLatencyGetAvgProcessingTime.setDescription('Average packet processing time handled by http server in micro seconds - GET.')
bHttpServLatencyGetProcessTimeMorethan1MSPktCount = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 10, 1, 1, 1, 12), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bHttpServLatencyGetProcessTimeMorethan1MSPktCount.setStatus('current')
if mibBuilder.loadTexts: bHttpServLatencyGetProcessTimeMorethan1MSPktCount.setDescription('Number of packets took more than 1 milli second processing time handled by http server - GET.')
bHttpServLatencyPostTotalPktCount = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 10, 1, 1, 1, 13), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bHttpServLatencyPostTotalPktCount.setStatus('current')
if mibBuilder.loadTexts: bHttpServLatencyPostTotalPktCount.setDescription('The count of the total number of packets handled by http server POST.')
bHttpServLatencyPostMaxProcessingTime = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 10, 1, 1, 1, 14), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bHttpServLatencyPostMaxProcessingTime.setStatus('current')
if mibBuilder.loadTexts: bHttpServLatencyPostMaxProcessingTime.setDescription('Maximum packet processing time handled by http server in micro seconds - POST.')
bHttpServLatencyPostMinProcessingTime = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 10, 1, 1, 1, 15), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bHttpServLatencyPostMinProcessingTime.setStatus('current')
if mibBuilder.loadTexts: bHttpServLatencyPostMinProcessingTime.setDescription('Minimum packet processing time handled by http server in micro seconds - POST.')
bHttpServLatencyPostAvgProcessingTime = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 10, 1, 1, 1, 16), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bHttpServLatencyPostAvgProcessingTime.setStatus('current')
if mibBuilder.loadTexts: bHttpServLatencyPostAvgProcessingTime.setDescription('Average packet processing time handled by http server in micro seconds - POST.')
bHttpServLatencyPostProcessTimeMorethan1MSPktCount = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 10, 1, 1, 1, 17), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bHttpServLatencyPostProcessTimeMorethan1MSPktCount.setStatus('current')
if mibBuilder.loadTexts: bHttpServLatencyPostProcessTimeMorethan1MSPktCount.setDescription('Number of packets took more than 1 milli second processing time handled by http server - POST.')
bHttpServLatencyDeleteTotalPktCount = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 10, 1, 1, 1, 18), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bHttpServLatencyDeleteTotalPktCount.setStatus('current')
if mibBuilder.loadTexts: bHttpServLatencyDeleteTotalPktCount.setDescription('The count of the total number of packets handled by http server DELETE.')
bHttpServLatencyDeleteMaxProcessingTime = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 10, 1, 1, 1, 19), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bHttpServLatencyDeleteMaxProcessingTime.setStatus('current')
if mibBuilder.loadTexts: bHttpServLatencyDeleteMaxProcessingTime.setDescription('Maximum packet processing time handled by http server in micro seconds - DELETE.')
bHttpServLatencyDeleteMinProcessingTime = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 10, 1, 1, 1, 20), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bHttpServLatencyDeleteMinProcessingTime.setStatus('current')
if mibBuilder.loadTexts: bHttpServLatencyDeleteMinProcessingTime.setDescription('Minimum packet processing time handled by http server in micro seconds - DELETE.')
bHttpServLatencyDeleteAvgProcessingTime = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 10, 1, 1, 1, 21), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bHttpServLatencyDeleteAvgProcessingTime.setStatus('current')
if mibBuilder.loadTexts: bHttpServLatencyDeleteAvgProcessingTime.setDescription('Average packet processing time handled by http server in micro seconds - DELETE.')
bHttpServLatencyDeleteProcessTimeMorethan1MSPktCount = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 10, 1, 1, 1, 22), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bHttpServLatencyDeleteProcessTimeMorethan1MSPktCount.setStatus('current')
if mibBuilder.loadTexts: bHttpServLatencyDeleteProcessTimeMorethan1MSPktCount.setDescription('Number of packets took more than 1 milli second processing time handled by http server - DELETE.')
mibBuilder.exportSymbols("BENU-HTTP-SERVER-MIB", benuHttpServerMIB=benuHttpServerMIB, bHttpServLatencyGetAvgProcessingTime=bHttpServLatencyGetAvgProcessingTime, bHttpServerObjects=bHttpServerObjects, bHttpServLatencyStatsIntervalDuration=bHttpServLatencyStatsIntervalDuration, bHttpServLatencyPostAvgProcessingTime=bHttpServLatencyPostAvgProcessingTime, bHttpServLatencyProcessTimeMorethan1MSPktCount=bHttpServLatencyProcessTimeMorethan1MSPktCount, bHttpServLatencyDeleteMinProcessingTime=bHttpServLatencyDeleteMinProcessingTime, bHttpServLatencyMinProcessingTime=bHttpServLatencyMinProcessingTime, bHttpServLatencyGetMinProcessingTime=bHttpServLatencyGetMinProcessingTime, bHttpServLatencyPostMaxProcessingTime=bHttpServLatencyPostMaxProcessingTime, bHttpServLatencyGetProcessTimeMorethan1MSPktCount=bHttpServLatencyGetProcessTimeMorethan1MSPktCount, bHttpServerLatencyTable=bHttpServerLatencyTable, PYSNMP_MODULE_ID=benuHttpServerMIB, bHttpServLatencyDeleteMaxProcessingTime=bHttpServLatencyDeleteMaxProcessingTime, bHttpServLatencyDeleteAvgProcessingTime=bHttpServLatencyDeleteAvgProcessingTime, bHttpServLatencyPostMinProcessingTime=bHttpServLatencyPostMinProcessingTime, bHttpServLatencyStatsInterval=bHttpServLatencyStatsInterval, bHttpServerLatencyEntry=bHttpServerLatencyEntry, bHttpServLatencyTotalPktCount=bHttpServLatencyTotalPktCount, bHttpServLatencyGetTotalPktCount=bHttpServLatencyGetTotalPktCount, bHttpServLatencyGetMaxProcessingTime=bHttpServLatencyGetMaxProcessingTime, bHttpServLatencyPostTotalPktCount=bHttpServLatencyPostTotalPktCount, bHttpServLatencyDeleteProcessTimeMorethan1MSPktCount=bHttpServLatencyDeleteProcessTimeMorethan1MSPktCount, bHttpServLatencyPostProcessTimeMorethan1MSPktCount=bHttpServLatencyPostProcessTimeMorethan1MSPktCount, bHttpServLatencyAvgProcessingTime=bHttpServLatencyAvgProcessingTime, bHttpServLatencyMaxProcessingTime=bHttpServLatencyMaxProcessingTime, bHttpServLatencyDeleteTotalPktCount=bHttpServLatencyDeleteTotalPktCount)
