#
# PySNMP MIB module BENU-IPPOOL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/benuos/BENU-IPPOOL-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:11:15 2022
# On host fv-az36-988 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
benuWAG, = mibBuilder.importSymbols("BENU-WAG-MIB", "benuWAG")
InetAddressType, InetPortNumber, InetAddressIPv4, InetAddress, InetAddressIPv6 = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetPortNumber", "InetAddressIPv4", "InetAddress", "InetAddressIPv6")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
mib_2, IpAddress, Counter32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, ModuleIdentity, Bits, Gauge32, TimeTicks, MibIdentifier, ObjectIdentity, iso, Unsigned32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "mib-2", "IpAddress", "Counter32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "ModuleIdentity", "Bits", "Gauge32", "TimeTicks", "MibIdentifier", "ObjectIdentity", "iso", "Unsigned32", "Integer32")
TextualConvention, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TruthValue")
benuIPPoolMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5))
benuIPPoolMIB.setRevisions(('2015-08-11 00:00', '2015-01-05 00:00', '2013-10-21 00:00',))
if mibBuilder.loadTexts: benuIPPoolMIB.setLastUpdated('201508110000Z')
if mibBuilder.loadTexts: benuIPPoolMIB.setOrganization('Benu Networks,Inc')
bIPPoolNotifications = ObjectIdentity((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 0))
if mibBuilder.loadTexts: bIPPoolNotifications.setStatus('current')
bIPv4PoolMIBObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1))
if mibBuilder.loadTexts: bIPv4PoolMIBObjects.setStatus('current')
bIPv4PoolNotifObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 2))
if mibBuilder.loadTexts: bIPv4PoolNotifObjects.setStatus('current')
bIPv6PoolMIBObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 3))
if mibBuilder.loadTexts: bIPv6PoolMIBObjects.setStatus('current')
bIPv6PoolNotifObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 4))
if mibBuilder.loadTexts: bIPv6PoolNotifObjects.setStatus('current')
bIPPoolTable = MibTable((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 1), )
if mibBuilder.loadTexts: bIPPoolTable.setStatus('current')
bIPPoolEntry = MibTableRow((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 1, 1), ).setIndexNames((0, "BENU-IPPOOL-MIB", "bIPPoolStatsInterval"), (0, "BENU-IPPOOL-MIB", "bIPPoolIndex"))
if mibBuilder.loadTexts: bIPPoolEntry.setStatus('current')
bIPPoolStatsInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: bIPPoolStatsInterval.setStatus('current')
bIPPoolIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 1, 1, 2), Integer32())
if mibBuilder.loadTexts: bIPPoolIndex.setStatus('current')
bIPPoolIntervalDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPoolIntervalDuration.setStatus('current')
bIPPoolName = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPoolName.setStatus('current')
bIPPoolStartAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 1, 1, 5), InetAddressIPv4()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPoolStartAddress.setStatus('current')
bIPPoolEndAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 1, 1, 6), InetAddressIPv4()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPoolEndAddress.setStatus('current')
bIPPoolTotalAddresses = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 1, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPoolTotalAddresses.setStatus('current')
bIPPoolReservedAddresses = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 1, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPoolReservedAddresses.setStatus('current')
bIPPoolPeakFreeAddresses = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 1, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPoolPeakFreeAddresses.setStatus('current')
bIPPoolPeakUsedAddresses = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 1, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPoolPeakUsedAddresses.setStatus('current')
bIPPoolUsedAddrLowThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 1, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPoolUsedAddrLowThreshold.setStatus('current')
bIPPoolUsedAddrHighThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 1, 1, 12), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPoolUsedAddrHighThreshold.setStatus('current')
bIPPoolGrpName = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 1, 1, 13), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPoolGrpName.setStatus('current')
bIPPoolGroupTable = MibTable((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 2), )
if mibBuilder.loadTexts: bIPPoolGroupTable.setStatus('current')
bIPPoolGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 2, 1), ).setIndexNames((0, "BENU-IPPOOL-MIB", "bIPPoolGroupStatsInterval"), (0, "BENU-IPPOOL-MIB", "bIPPoolGroupIndex"))
if mibBuilder.loadTexts: bIPPoolGroupEntry.setStatus('current')
bIPPoolGroupStatsInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: bIPPoolGroupStatsInterval.setStatus('current')
bIPPoolGroupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 2, 1, 2), Integer32())
if mibBuilder.loadTexts: bIPPoolGroupIndex.setStatus('current')
bIPPoolGroupIntervalDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPoolGroupIntervalDuration.setStatus('current')
bIPPoolGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 2, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPoolGroupName.setStatus('current')
bIPPoolGroupTotalAddresses = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 2, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPoolGroupTotalAddresses.setStatus('current')
bIPPoolGroupReservedAddresses = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 2, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPoolGroupReservedAddresses.setStatus('current')
bIPPoolGroupPeakFreeAddresses = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 2, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPoolGroupPeakFreeAddresses.setStatus('current')
bIPPoolGroupPeakUsedAddresses = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 2, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPoolGroupPeakUsedAddresses.setStatus('current')
bIPPoolGlobalTable = MibTable((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 3), )
if mibBuilder.loadTexts: bIPPoolGlobalTable.setStatus('current')
bIPPoolGlobalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 3, 1), ).setIndexNames((0, "BENU-IPPOOL-MIB", "bIPPoolGlobalStatsInterval"), (0, "BENU-IPPOOL-MIB", "bIPPoolClientIndex"))
if mibBuilder.loadTexts: bIPPoolGlobalEntry.setStatus('current')
bIPPoolGlobalStatsInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 3, 1, 1), Integer32())
if mibBuilder.loadTexts: bIPPoolGlobalStatsInterval.setStatus('current')
bIPPoolClientIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 3, 1, 2), Integer32())
if mibBuilder.loadTexts: bIPPoolClientIndex.setStatus('current')
bIPPoolClientName = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 3, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPoolClientName.setStatus('current')
bIPPoolGlobalAllocReq = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 3, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPoolGlobalAllocReq.setStatus('current')
bIPPoolGlobalAllocReqSucc = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 3, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPoolGlobalAllocReqSucc.setStatus('current')
bIPPoolGlobalAllocReqUnSucc = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 3, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPoolGlobalAllocReqUnSucc.setStatus('current')
bIPPoolGlobalDupAllocReq = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 3, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPoolGlobalDupAllocReq.setStatus('current')
bIPPoolGlobalStaticAllocReq = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 3, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPoolGlobalStaticAllocReq.setStatus('current')
bIPPoolGlobalAllocResponses = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 3, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPoolGlobalAllocResponses.setStatus('current')
bIPPoolGlobalDeAllocReq = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 3, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPoolGlobalDeAllocReq.setStatus('current')
bIPPoolGlobalDeAllocReqSucc = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 3, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPoolGlobalDeAllocReqSucc.setStatus('current')
bIPPoolGlobalDeAllocReqUnSucc = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 3, 1, 12), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPoolGlobalDeAllocReqUnSucc.setStatus('current')
bIPPoolGlobalInvalidReq = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 3, 1, 13), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPoolGlobalInvalidReq.setStatus('current')
bIPPoolGlobalNotAvailCount = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 3, 1, 14), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPoolGlobalNotAvailCount.setStatus('current')
bIPPoolGlobalPoolExhaustedCount = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 3, 1, 15), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPoolGlobalPoolExhaustedCount.setStatus('current')
bIPPoolGlobalGroupExhaustedCount = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 3, 1, 16), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPoolGlobalGroupExhaustedCount.setStatus('current')
bIPPoolGlobalInvalidPoolNameCount = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 3, 1, 17), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPoolGlobalInvalidPoolNameCount.setStatus('current')
bIPPoolGlobalInvalidGroupNameCount = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 3, 1, 18), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPoolGlobalInvalidGroupNameCount.setStatus('current')
bIPPoolGlobalInvalidIPAddrCount = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 3, 1, 19), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPoolGlobalInvalidIPAddrCount.setStatus('current')
bIPPoolGlobalHashInsertFail = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 3, 1, 20), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPoolGlobalHashInsertFail.setStatus('current')
bIPPoolGlobalHashDeleteFail = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 3, 1, 21), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPoolGlobalHashDeleteFail.setStatus('current')
bIPPoolGlobalRequestedAllocatedMismacth = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 3, 1, 22), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPoolGlobalRequestedAllocatedMismacth.setStatus('current')
bIPPoolGlobalRequestedIPNotFree = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 3, 1, 23), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPoolGlobalRequestedIPNotFree.setStatus('current')
bIPPoolGlobalGenErrCount = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 3, 1, 24), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPoolGlobalGenErrCount.setStatus('current')
bIPPoolGlobalAddrRelDueToIntAdd = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 3, 1, 25), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPoolGlobalAddrRelDueToIntAdd.setStatus('current')
bIPPoolGlobalGroupDeAllocReq = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 3, 1, 26), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPoolGlobalGroupDeAllocReq.setStatus('current')
bIPPoolGlobalGroupDeAllocReqSucc = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 3, 1, 27), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPoolGlobalGroupDeAllocReqSucc.setStatus('current')
bIPPoolGlobalGroupDeAllocReqUnSucc = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 3, 1, 28), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPoolGlobalGroupDeAllocReqUnSucc.setStatus('current')
bIPPoolTotalPoolCreatedEvents = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 3, 1, 29), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPoolTotalPoolCreatedEvents.setStatus('current')
bIPPoolTotalPoolDeletedEvents = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 3, 1, 30), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPoolTotalPoolDeletedEvents.setStatus('current')
bIPPoolGlobalIntervalDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 1, 3, 1, 31), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPoolGlobalIntervalDuration.setStatus('current')
bIPPoolUsedAddrLow = NotificationType((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 0, 1)).setObjects(("BENU-IPPOOL-MIB", "bIPPoolName"), ("BENU-IPPOOL-MIB", "bIPPoolTotalAddresses"), ("BENU-IPPOOL-MIB", "bIPPoolUsedAddrLowThreshold"))
if mibBuilder.loadTexts: bIPPoolUsedAddrLow.setStatus('current')
bIPPoolUsedAddrHigh = NotificationType((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 0, 2)).setObjects(("BENU-IPPOOL-MIB", "bIPPoolName"), ("BENU-IPPOOL-MIB", "bIPPoolTotalAddresses"), ("BENU-IPPOOL-MIB", "bIPPoolUsedAddrHighThreshold"))
if mibBuilder.loadTexts: bIPPoolUsedAddrHigh.setStatus('current')
bIPPoolAddrExhausted = NotificationType((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 0, 5)).setObjects(("BENU-IPPOOL-MIB", "bIPPoolName"), ("BENU-IPPOOL-MIB", "bIPPoolTotalAddresses"))
if mibBuilder.loadTexts: bIPPoolAddrExhausted.setStatus('current')
bIPv6PoolTable = MibTable((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 3, 1), )
if mibBuilder.loadTexts: bIPv6PoolTable.setStatus('current')
bIPv6PoolEntry = MibTableRow((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 3, 1, 1), ).setIndexNames((0, "BENU-IPPOOL-MIB", "bIPv6PoolStatsInterval"), (0, "BENU-IPPOOL-MIB", "bIPv6PoolIndex"))
if mibBuilder.loadTexts: bIPv6PoolEntry.setStatus('current')
bIPv6PoolStatsInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 3, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: bIPv6PoolStatsInterval.setStatus('current')
bIPv6PoolIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 3, 1, 1, 2), Integer32())
if mibBuilder.loadTexts: bIPv6PoolIndex.setStatus('current')
bIPv6PoolIntervalDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 3, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPv6PoolIntervalDuration.setStatus('current')
bIPv6PoolName = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 3, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPv6PoolName.setStatus('current')
bIPv6PoolStartPrefix = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 3, 1, 1, 5), InetAddressIPv6()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPv6PoolStartPrefix.setStatus('current')
bIPv6PoolEndPrefix = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 3, 1, 1, 6), InetAddressIPv6()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPv6PoolEndPrefix.setStatus('current')
bIPv6PoolTotalPrefixes = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 3, 1, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPv6PoolTotalPrefixes.setStatus('current')
bIPv6PoolReservedPrefixes = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 3, 1, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPv6PoolReservedPrefixes.setStatus('current')
bIPv6PoolPeakFreePrefixes = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 3, 1, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPv6PoolPeakFreePrefixes.setStatus('current')
bIPv6PoolPeakUsedPrefixes = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 3, 1, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPv6PoolPeakUsedPrefixes.setStatus('current')
bIPv6PoolUsedPrefixLowThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 3, 1, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPv6PoolUsedPrefixLowThreshold.setStatus('current')
bIPv6PoolUsedPrefixHighThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 3, 1, 1, 12), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPv6PoolUsedPrefixHighThreshold.setStatus('current')
bIPv6PoolGrpName = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 3, 1, 1, 13), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPv6PoolGrpName.setStatus('current')
bIPv6PoolGroupTable = MibTable((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 3, 2), )
if mibBuilder.loadTexts: bIPv6PoolGroupTable.setStatus('current')
bIPv6PoolGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 3, 2, 1), ).setIndexNames((0, "BENU-IPPOOL-MIB", "bIPv6PoolGroupStatsInterval"), (0, "BENU-IPPOOL-MIB", "bIPv6PoolGroupIndex"))
if mibBuilder.loadTexts: bIPv6PoolGroupEntry.setStatus('current')
bIPv6PoolGroupStatsInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 3, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: bIPv6PoolGroupStatsInterval.setStatus('current')
bIPv6PoolGroupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 3, 2, 1, 2), Integer32())
if mibBuilder.loadTexts: bIPv6PoolGroupIndex.setStatus('current')
bIPv6PoolGroupIntervalDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 3, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPv6PoolGroupIntervalDuration.setStatus('current')
bIPv6PoolGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 3, 2, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPv6PoolGroupName.setStatus('current')
bIPv6PoolGroupTotalPrefixes = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 3, 2, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPv6PoolGroupTotalPrefixes.setStatus('current')
bIPv6PoolGroupReservedPrefixes = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 3, 2, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPv6PoolGroupReservedPrefixes.setStatus('current')
bIPv6PoolGroupPeakFreePrefixes = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 3, 2, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPv6PoolGroupPeakFreePrefixes.setStatus('current')
bIPv6PoolGroupPeakUsedPrefixes = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 3, 2, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPv6PoolGroupPeakUsedPrefixes.setStatus('current')
bIPv6PoolGlobalTable = MibTable((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 3, 3), )
if mibBuilder.loadTexts: bIPv6PoolGlobalTable.setStatus('current')
bIPv6PoolGlobalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 3, 3, 1), ).setIndexNames((0, "BENU-IPPOOL-MIB", "bIPv6PoolGlobalStatsInterval"), (0, "BENU-IPPOOL-MIB", "bIPv6PoolClientIndex"))
if mibBuilder.loadTexts: bIPv6PoolGlobalEntry.setStatus('current')
bIPv6PoolGlobalStatsInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 3, 3, 1, 1), Integer32())
if mibBuilder.loadTexts: bIPv6PoolGlobalStatsInterval.setStatus('current')
bIPv6PoolClientIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 3, 3, 1, 2), Integer32())
if mibBuilder.loadTexts: bIPv6PoolClientIndex.setStatus('current')
bIPv6PoolClientName = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 3, 3, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPv6PoolClientName.setStatus('current')
bIPv6PoolGlobalAllocReq = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 3, 3, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPv6PoolGlobalAllocReq.setStatus('current')
bIPv6PoolGlobalAllocReqSucc = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 3, 3, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPv6PoolGlobalAllocReqSucc.setStatus('current')
bIPv6PoolGlobalAllocReqUnSucc = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 3, 3, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPv6PoolGlobalAllocReqUnSucc.setStatus('current')
bIPv6PoolGlobalDupAllocReq = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 3, 3, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPv6PoolGlobalDupAllocReq.setStatus('current')
bIPv6PoolGlobalStaticAllocReq = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 3, 3, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPv6PoolGlobalStaticAllocReq.setStatus('current')
bIPv6PoolGlobalAllocResponses = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 3, 3, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPv6PoolGlobalAllocResponses.setStatus('current')
bIPv6PoolGlobalDeAllocReq = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 3, 3, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPv6PoolGlobalDeAllocReq.setStatus('current')
bIPv6PoolGlobalDeAllocReqSucc = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 3, 3, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPv6PoolGlobalDeAllocReqSucc.setStatus('current')
bIPv6PoolGlobalDeAllocReqUnSucc = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 3, 3, 1, 12), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPv6PoolGlobalDeAllocReqUnSucc.setStatus('current')
bIPv6PoolGlobalInvalidReq = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 3, 3, 1, 13), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPv6PoolGlobalInvalidReq.setStatus('current')
bIPv6PoolGlobalNotAvailCount = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 3, 3, 1, 14), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPv6PoolGlobalNotAvailCount.setStatus('current')
bIPv6PoolGlobalPoolExhaustedCount = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 3, 3, 1, 15), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPv6PoolGlobalPoolExhaustedCount.setStatus('current')
bIPv6PoolGlobalGroupExhaustedCount = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 3, 3, 1, 16), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPv6PoolGlobalGroupExhaustedCount.setStatus('current')
bIPv6PoolGlobalInvalidPoolNameCount = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 3, 3, 1, 17), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPv6PoolGlobalInvalidPoolNameCount.setStatus('current')
bIPv6PoolGlobalInvalidGroupNameCount = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 3, 3, 1, 18), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPv6PoolGlobalInvalidGroupNameCount.setStatus('current')
bIPv6PoolGlobalInvalidIPAddrCount = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 3, 3, 1, 19), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPv6PoolGlobalInvalidIPAddrCount.setStatus('current')
bIPv6PoolGlobalHashInsertFail = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 3, 3, 1, 20), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPv6PoolGlobalHashInsertFail.setStatus('current')
bIPv6PoolGlobalHashDeleteFail = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 3, 3, 1, 21), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPv6PoolGlobalHashDeleteFail.setStatus('current')
bIPv6PoolGlobalRequestedAllocatedMismacth = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 3, 3, 1, 22), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPv6PoolGlobalRequestedAllocatedMismacth.setStatus('current')
bIPv6PoolGlobalRequestedIPNotFree = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 3, 3, 1, 23), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPv6PoolGlobalRequestedIPNotFree.setStatus('current')
bIPv6PoolGlobalGenErrCount = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 3, 3, 1, 24), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPv6PoolGlobalGenErrCount.setStatus('current')
bIPv6PoolGlobalPrefixRelDueToIntAdd = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 3, 3, 1, 25), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPv6PoolGlobalPrefixRelDueToIntAdd.setStatus('current')
bIPv6PoolTotalPoolCreatedEvents = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 3, 3, 1, 26), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPv6PoolTotalPoolCreatedEvents.setStatus('current')
bIPv6PoolTotalPoolDeletedEvents = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 3, 3, 1, 27), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPv6PoolTotalPoolDeletedEvents.setStatus('current')
bIPv6PoolGlobalIntervalDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 3, 3, 1, 28), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPv6PoolGlobalIntervalDuration.setStatus('current')
bIPv6PoolUsedPrefixLow = NotificationType((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 0, 3)).setObjects(("BENU-IPPOOL-MIB", "bIPv6PoolName"), ("BENU-IPPOOL-MIB", "bIPv6PoolTotalPrefixes"), ("BENU-IPPOOL-MIB", "bIPv6PoolUsedPrefixLowThreshold"))
if mibBuilder.loadTexts: bIPv6PoolUsedPrefixLow.setStatus('current')
bIPv6PoolUsedPrefixHigh = NotificationType((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 0, 4)).setObjects(("BENU-IPPOOL-MIB", "bIPv6PoolName"), ("BENU-IPPOOL-MIB", "bIPv6PoolTotalPrefixes"), ("BENU-IPPOOL-MIB", "bIPv6PoolUsedPrefixHighThreshold"))
if mibBuilder.loadTexts: bIPv6PoolUsedPrefixHigh.setStatus('current')
bIPv6PoolPrefixExhausted = NotificationType((1, 3, 6, 1, 4, 1, 39406, 2, 1, 5, 0, 6)).setObjects(("BENU-IPPOOL-MIB", "bIPv6PoolName"), ("BENU-IPPOOL-MIB", "bIPv6PoolTotalPrefixes"))
if mibBuilder.loadTexts: bIPv6PoolPrefixExhausted.setStatus('current')
mibBuilder.exportSymbols("BENU-IPPOOL-MIB", bIPPoolTotalPoolDeletedEvents=bIPPoolTotalPoolDeletedEvents, bIPv6PoolGlobalDeAllocReq=bIPv6PoolGlobalDeAllocReq, bIPPoolGlobalStatsInterval=bIPPoolGlobalStatsInterval, bIPPoolUsedAddrHighThreshold=bIPPoolUsedAddrHighThreshold, bIPPoolGlobalDeAllocReqSucc=bIPPoolGlobalDeAllocReqSucc, bIPv6PoolGroupPeakFreePrefixes=bIPv6PoolGroupPeakFreePrefixes, bIPPoolUsedAddrLow=bIPPoolUsedAddrLow, bIPPoolGlobalIntervalDuration=bIPPoolGlobalIntervalDuration, bIPPoolTotalPoolCreatedEvents=bIPPoolTotalPoolCreatedEvents, bIPv6PoolGlobalIntervalDuration=bIPv6PoolGlobalIntervalDuration, bIPv6PoolGlobalAllocResponses=bIPv6PoolGlobalAllocResponses, bIPv6PoolTotalPoolCreatedEvents=bIPv6PoolTotalPoolCreatedEvents, bIPv6PoolTable=bIPv6PoolTable, bIPv6PoolGroupName=bIPv6PoolGroupName, bIPv6PoolGlobalAllocReqSucc=bIPv6PoolGlobalAllocReqSucc, bIPv6PoolGlobalRequestedIPNotFree=bIPv6PoolGlobalRequestedIPNotFree, bIPPoolGroupReservedAddresses=bIPPoolGroupReservedAddresses, bIPPoolGroupName=bIPPoolGroupName, bIPPoolGlobalGroupExhaustedCount=bIPPoolGlobalGroupExhaustedCount, bIPPoolGlobalAllocReqSucc=bIPPoolGlobalAllocReqSucc, bIPv6PoolGlobalGroupExhaustedCount=bIPv6PoolGlobalGroupExhaustedCount, bIPPoolEndAddress=bIPPoolEndAddress, bIPv6PoolTotalPrefixes=bIPv6PoolTotalPrefixes, bIPPoolClientIndex=bIPPoolClientIndex, bIPv6PoolGlobalDeAllocReqSucc=bIPv6PoolGlobalDeAllocReqSucc, bIPPoolTotalAddresses=bIPPoolTotalAddresses, bIPv6PoolTotalPoolDeletedEvents=bIPv6PoolTotalPoolDeletedEvents, bIPPoolClientName=bIPPoolClientName, bIPv6PoolGlobalInvalidPoolNameCount=bIPv6PoolGlobalInvalidPoolNameCount, bIPPoolGroupPeakUsedAddresses=bIPPoolGroupPeakUsedAddresses, bIPPoolUsedAddrHigh=bIPPoolUsedAddrHigh, bIPPoolGlobalInvalidPoolNameCount=bIPPoolGlobalInvalidPoolNameCount, bIPv6PoolMIBObjects=bIPv6PoolMIBObjects, bIPv6PoolGlobalPrefixRelDueToIntAdd=bIPv6PoolGlobalPrefixRelDueToIntAdd, bIPv6PoolGlobalInvalidReq=bIPv6PoolGlobalInvalidReq, bIPPoolIndex=bIPPoolIndex, bIPv6PoolStatsInterval=bIPv6PoolStatsInterval, bIPPoolGroupIndex=bIPPoolGroupIndex, bIPv6PoolGlobalStatsInterval=bIPv6PoolGlobalStatsInterval, bIPv6PoolPeakFreePrefixes=bIPv6PoolPeakFreePrefixes, bIPv6PoolGroupReservedPrefixes=bIPv6PoolGroupReservedPrefixes, bIPv6PoolGlobalHashDeleteFail=bIPv6PoolGlobalHashDeleteFail, bIPv6PoolGlobalStaticAllocReq=bIPv6PoolGlobalStaticAllocReq, bIPPoolGlobalInvalidGroupNameCount=bIPPoolGlobalInvalidGroupNameCount, bIPv6PoolPeakUsedPrefixes=bIPv6PoolPeakUsedPrefixes, bIPPoolReservedAddresses=bIPPoolReservedAddresses, bIPv6PoolStartPrefix=bIPv6PoolStartPrefix, bIPPoolUsedAddrLowThreshold=bIPPoolUsedAddrLowThreshold, bIPPoolTable=bIPPoolTable, bIPv6PoolGlobalTable=bIPv6PoolGlobalTable, bIPPoolGroupStatsInterval=bIPPoolGroupStatsInterval, bIPPoolGlobalGroupDeAllocReq=bIPPoolGlobalGroupDeAllocReq, benuIPPoolMIB=benuIPPoolMIB, bIPPoolGlobalGroupDeAllocReqSucc=bIPPoolGlobalGroupDeAllocReqSucc, bIPv6PoolUsedPrefixLow=bIPv6PoolUsedPrefixLow, bIPv6PoolIntervalDuration=bIPv6PoolIntervalDuration, bIPPoolGlobalTable=bIPPoolGlobalTable, bIPPoolGlobalNotAvailCount=bIPPoolGlobalNotAvailCount, bIPv6PoolNotifObjects=bIPv6PoolNotifObjects, bIPv6PoolGroupTotalPrefixes=bIPv6PoolGroupTotalPrefixes, bIPv6PoolClientName=bIPv6PoolClientName, bIPv6PoolGroupPeakUsedPrefixes=bIPv6PoolGroupPeakUsedPrefixes, bIPv6PoolEndPrefix=bIPv6PoolEndPrefix, bIPPoolGrpName=bIPPoolGrpName, bIPPoolGroupTable=bIPPoolGroupTable, bIPPoolGlobalAllocResponses=bIPPoolGlobalAllocResponses, bIPv6PoolGlobalRequestedAllocatedMismacth=bIPv6PoolGlobalRequestedAllocatedMismacth, bIPPoolStartAddress=bIPPoolStartAddress, bIPv6PoolGlobalPoolExhaustedCount=bIPv6PoolGlobalPoolExhaustedCount, bIPPoolGlobalRequestedIPNotFree=bIPPoolGlobalRequestedIPNotFree, bIPv6PoolReservedPrefixes=bIPv6PoolReservedPrefixes, bIPv6PoolIndex=bIPv6PoolIndex, bIPv6PoolGroupEntry=bIPv6PoolGroupEntry, bIPPoolIntervalDuration=bIPPoolIntervalDuration, bIPPoolName=bIPPoolName, bIPPoolGlobalEntry=bIPPoolGlobalEntry, bIPv6PoolUsedPrefixHigh=bIPv6PoolUsedPrefixHigh, bIPPoolAddrExhausted=bIPPoolAddrExhausted, bIPv4PoolMIBObjects=bIPv4PoolMIBObjects, bIPv6PoolPrefixExhausted=bIPv6PoolPrefixExhausted, bIPPoolNotifications=bIPPoolNotifications, bIPv6PoolGlobalEntry=bIPv6PoolGlobalEntry, bIPv4PoolNotifObjects=bIPv4PoolNotifObjects, bIPv6PoolGlobalHashInsertFail=bIPv6PoolGlobalHashInsertFail, bIPPoolGlobalGenErrCount=bIPPoolGlobalGenErrCount, bIPv6PoolGlobalInvalidGroupNameCount=bIPv6PoolGlobalInvalidGroupNameCount, bIPPoolGroupTotalAddresses=bIPPoolGroupTotalAddresses, bIPv6PoolGlobalDupAllocReq=bIPv6PoolGlobalDupAllocReq, bIPPoolGlobalDeAllocReq=bIPPoolGlobalDeAllocReq, bIPv6PoolGroupIntervalDuration=bIPv6PoolGroupIntervalDuration, bIPv6PoolEntry=bIPv6PoolEntry, bIPPoolGlobalAllocReqUnSucc=bIPPoolGlobalAllocReqUnSucc, bIPPoolGlobalInvalidReq=bIPPoolGlobalInvalidReq, bIPv6PoolGlobalAllocReq=bIPv6PoolGlobalAllocReq, bIPv6PoolName=bIPv6PoolName, bIPPoolPeakUsedAddresses=bIPPoolPeakUsedAddresses, bIPv6PoolUsedPrefixHighThreshold=bIPv6PoolUsedPrefixHighThreshold, bIPv6PoolGroupStatsInterval=bIPv6PoolGroupStatsInterval, bIPv6PoolClientIndex=bIPv6PoolClientIndex, bIPPoolGroupPeakFreeAddresses=bIPPoolGroupPeakFreeAddresses, bIPPoolGroupEntry=bIPPoolGroupEntry, bIPPoolGlobalStaticAllocReq=bIPPoolGlobalStaticAllocReq, bIPPoolPeakFreeAddresses=bIPPoolPeakFreeAddresses, bIPPoolEntry=bIPPoolEntry, bIPv6PoolGlobalInvalidIPAddrCount=bIPv6PoolGlobalInvalidIPAddrCount, bIPPoolGlobalInvalidIPAddrCount=bIPPoolGlobalInvalidIPAddrCount, bIPPoolGroupIntervalDuration=bIPPoolGroupIntervalDuration, bIPPoolGlobalPoolExhaustedCount=bIPPoolGlobalPoolExhaustedCount, bIPv6PoolGlobalGenErrCount=bIPv6PoolGlobalGenErrCount, bIPPoolGlobalGroupDeAllocReqUnSucc=bIPPoolGlobalGroupDeAllocReqUnSucc, bIPPoolGlobalAllocReq=bIPPoolGlobalAllocReq, bIPPoolGlobalRequestedAllocatedMismacth=bIPPoolGlobalRequestedAllocatedMismacth, bIPv6PoolGlobalNotAvailCount=bIPv6PoolGlobalNotAvailCount, bIPPoolGlobalHashDeleteFail=bIPPoolGlobalHashDeleteFail, bIPPoolGlobalDupAllocReq=bIPPoolGlobalDupAllocReq, PYSNMP_MODULE_ID=benuIPPoolMIB, bIPPoolGlobalDeAllocReqUnSucc=bIPPoolGlobalDeAllocReqUnSucc, bIPv6PoolGroupTable=bIPv6PoolGroupTable, bIPv6PoolGrpName=bIPv6PoolGrpName, bIPv6PoolUsedPrefixLowThreshold=bIPv6PoolUsedPrefixLowThreshold, bIPPoolGlobalHashInsertFail=bIPPoolGlobalHashInsertFail, bIPv6PoolGlobalDeAllocReqUnSucc=bIPv6PoolGlobalDeAllocReqUnSucc, bIPPoolStatsInterval=bIPPoolStatsInterval, bIPv6PoolGroupIndex=bIPv6PoolGroupIndex, bIPv6PoolGlobalAllocReqUnSucc=bIPv6PoolGlobalAllocReqUnSucc, bIPPoolGlobalAddrRelDueToIntAdd=bIPPoolGlobalAddrRelDueToIntAdd)
