#
# PySNMP MIB module BENU-HOST-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/benuos/BENU-HOST-MIB
# Produced by pysmi-1.1.8 at Sun Jan 16 00:32:19 2022
# On host fv-az42-839 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
benuPlatform, = mibBuilder.importSymbols("BENU-PLATFORM-MIB", "benuPlatform")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, iso, Integer32, Gauge32, MibIdentifier, Bits, TimeTicks, IpAddress, ObjectIdentity, NotificationType, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "iso", "Integer32", "Gauge32", "MibIdentifier", "Bits", "TimeTicks", "IpAddress", "ObjectIdentity", "NotificationType", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
bHostMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 39406, 1, 5))
bHostMIB.setRevisions(('2015-11-03 00:00', '2015-04-28 00:00', '2015-04-27 00:00', '2015-01-05 00:00', '2015-01-04 00:00', '2014-12-17 00:00', '2014-09-22 00:00', '2014-03-21 00:00', '2013-05-27 00:00',))
if mibBuilder.loadTexts: bHostMIB.setLastUpdated('201511030000Z')
if mibBuilder.loadTexts: bHostMIB.setOrganization('Benu Networks')
bHostMIBObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 39406, 1, 5, 1))
if mibBuilder.loadTexts: bHostMIBObjects.setStatus('current')
bHostNotifObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 39406, 1, 5, 0))
if mibBuilder.loadTexts: bHostNotifObjects.setStatus('current')
bHostNotifVariables = ObjectIdentity((1, 3, 6, 1, 4, 1, 39406, 1, 5, 2))
if mibBuilder.loadTexts: bHostNotifVariables.setStatus('current')
bSWTaskInfoTable = MibTable((1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 1), )
if mibBuilder.loadTexts: bSWTaskInfoTable.setStatus('current')
bSWTaskInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 1, 1), ).setIndexNames((0, "BENU-HOST-MIB", "bSWTaskIndex"))
if mibBuilder.loadTexts: bSWTaskInfoEntry.setStatus('current')
bSWTaskIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: bSWTaskIndex.setStatus('current')
bSWTaskName = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bSWTaskName.setStatus('current')
bSWTaskProcessID = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bSWTaskProcessID.setStatus('current')
bSWTaskLoadIntervalDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bSWTaskLoadIntervalDuration.setStatus('current')
bSWTaskRunStateTime = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 1, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bSWTaskRunStateTime.setStatus('current')
bSWTaskCPUUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 1, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bSWTaskCPUUsage.setStatus('current')
bSWTaskAvgCPUUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 1, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bSWTaskAvgCPUUsage.setStatus('current')
bSWTaskMaxCPUUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 1, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bSWTaskMaxCPUUsage.setStatus('current')
bSWTaskCodeSegmentSize = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 1, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bSWTaskCodeSegmentSize.setStatus('current')
bSWTaskDataSegmentSize = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 1, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bSWTaskDataSegmentSize.setStatus('current')
bSWTaskResidentPhyMem = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 1, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bSWTaskResidentPhyMem.setStatus('current')
bSWTaskVirtMemUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 1, 1, 12), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bSWTaskVirtMemUsage.setStatus('current')
bSWTaskSharedMem = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 1, 1, 13), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bSWTaskSharedMem.setStatus('current')
bSWTaskVirtMemPeakUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 1, 1, 14), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bSWTaskVirtMemPeakUsage.setStatus('current')
bSWTaskAvgCPUUsageHighThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 1, 1, 15), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bSWTaskAvgCPUUsageHighThreshold.setStatus('current')
bSWTaskAvgCPUUsageLowThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 1, 1, 16), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bSWTaskAvgCPUUsageLowThreshold.setStatus('current')
bSWTaskCPUUsageLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 1, 1, 17), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bSWTaskCPUUsageLimit.setStatus('current')
bSWTaskRestartLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 1, 1, 18), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bSWTaskRestartLimit.setStatus('current')
bSWTaskRestartability = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 1, 1, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("yes", 1), ("no", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bSWTaskRestartability.setStatus('current')
bSWTaskRestartCount = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 1, 1, 20), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bSWTaskRestartCount.setStatus('current')
bSysTotalMem = MibScalar((1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bSysTotalMem.setStatus('current')
bSysMemUsed = MibScalar((1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bSysMemUsed.setStatus('current')
bSysMemFree = MibScalar((1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bSysMemFree.setStatus('current')
bSysTotalCPUUtilAvailable = MibScalar((1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bSysTotalCPUUtilAvailable.setStatus('current')
bSysAvgCPUUtil15Sec = MibScalar((1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bSysAvgCPUUtil15Sec.setStatus('current')
bSysAvgCPUUtil1Min = MibScalar((1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bSysAvgCPUUtil1Min.setStatus('current')
bSysAvgCPUUtil5Min = MibScalar((1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bSysAvgCPUUtil5Min.setStatus('current')
bCPUMonInterval = MibScalar((1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 9), Unsigned32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: bCPUMonInterval.setStatus('current')
bSWTaskDiedReason = MibScalar((1, 3, 6, 1, 4, 1, 39406, 1, 5, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("cpuUsageLimitReached", 1), ("unKnown", 2)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bSWTaskDiedReason.setStatus('current')
bSWProcessName = MibScalar((1, 3, 6, 1, 4, 1, 39406, 1, 5, 2, 2), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bSWProcessName.setStatus('current')
bSWProcessID = MibScalar((1, 3, 6, 1, 4, 1, 39406, 1, 5, 2, 3), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bSWProcessID.setStatus('current')
bSWProcessAvgCPUUsageLowThreshold = MibScalar((1, 3, 6, 1, 4, 1, 39406, 1, 5, 2, 4), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bSWProcessAvgCPUUsageLowThreshold.setStatus('current')
bSWProcessAvgCPUUsageHighThreshold = MibScalar((1, 3, 6, 1, 4, 1, 39406, 1, 5, 2, 5), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bSWProcessAvgCPUUsageHighThreshold.setStatus('current')
bSWTaskAvgCPUUsageLow = NotificationType((1, 3, 6, 1, 4, 1, 39406, 1, 5, 0, 1)).setObjects(("BENU-HOST-MIB", "bSWProcessName"), ("BENU-HOST-MIB", "bSWProcessID"), ("BENU-HOST-MIB", "bSWProcessAvgCPUUsageLowThreshold"))
if mibBuilder.loadTexts: bSWTaskAvgCPUUsageLow.setStatus('current')
bSWTaskAvgCPUUsageHigh = NotificationType((1, 3, 6, 1, 4, 1, 39406, 1, 5, 0, 2)).setObjects(("BENU-HOST-MIB", "bSWProcessName"), ("BENU-HOST-MIB", "bSWProcessID"), ("BENU-HOST-MIB", "bSWProcessAvgCPUUsageHighThreshold"))
if mibBuilder.loadTexts: bSWTaskAvgCPUUsageHigh.setStatus('current')
bSWTaskDied = NotificationType((1, 3, 6, 1, 4, 1, 39406, 1, 5, 0, 3)).setObjects(("BENU-HOST-MIB", "bSWProcessName"), ("BENU-HOST-MIB", "bSWProcessID"), ("BENU-HOST-MIB", "bSWTaskDiedReason"))
if mibBuilder.loadTexts: bSWTaskDied.setStatus('current')
bSWTaskRestartLimitReached = NotificationType((1, 3, 6, 1, 4, 1, 39406, 1, 5, 0, 4)).setObjects(("BENU-HOST-MIB", "bSWProcessName"), ("BENU-HOST-MIB", "bSWProcessID"))
if mibBuilder.loadTexts: bSWTaskRestartLimitReached.setStatus('current')
mibBuilder.exportSymbols("BENU-HOST-MIB", bSWTaskRunStateTime=bSWTaskRunStateTime, bSWTaskAvgCPUUsageLowThreshold=bSWTaskAvgCPUUsageLowThreshold, bHostMIBObjects=bHostMIBObjects, bHostMIB=bHostMIB, bSWTaskInfoTable=bSWTaskInfoTable, bSWTaskVirtMemUsage=bSWTaskVirtMemUsage, bSWProcessAvgCPUUsageLowThreshold=bSWProcessAvgCPUUsageLowThreshold, bSWProcessName=bSWProcessName, bSWTaskAvgCPUUsageLow=bSWTaskAvgCPUUsageLow, bSWTaskRestartLimitReached=bSWTaskRestartLimitReached, bSysTotalCPUUtilAvailable=bSysTotalCPUUtilAvailable, bCPUMonInterval=bCPUMonInterval, bSWTaskAvgCPUUsageHighThreshold=bSWTaskAvgCPUUsageHighThreshold, bHostNotifObjects=bHostNotifObjects, bSWTaskLoadIntervalDuration=bSWTaskLoadIntervalDuration, bSWTaskVirtMemPeakUsage=bSWTaskVirtMemPeakUsage, bSysAvgCPUUtil15Sec=bSysAvgCPUUtil15Sec, bSWTaskCodeSegmentSize=bSWTaskCodeSegmentSize, bSWTaskMaxCPUUsage=bSWTaskMaxCPUUsage, bSWTaskCPUUsageLimit=bSWTaskCPUUsageLimit, bSysMemUsed=bSysMemUsed, bSWTaskProcessID=bSWTaskProcessID, bSWTaskResidentPhyMem=bSWTaskResidentPhyMem, bSWTaskName=bSWTaskName, bSysMemFree=bSysMemFree, bHostNotifVariables=bHostNotifVariables, bSWTaskIndex=bSWTaskIndex, bSWTaskAvgCPUUsage=bSWTaskAvgCPUUsage, bSWProcessID=bSWProcessID, bSysAvgCPUUtil5Min=bSysAvgCPUUtil5Min, bSWTaskDied=bSWTaskDied, bSWTaskRestartCount=bSWTaskRestartCount, PYSNMP_MODULE_ID=bHostMIB, bSWTaskRestartability=bSWTaskRestartability, bSWTaskRestartLimit=bSWTaskRestartLimit, bSWTaskDiedReason=bSWTaskDiedReason, bSWProcessAvgCPUUsageHighThreshold=bSWProcessAvgCPUUsageHighThreshold, bSysTotalMem=bSysTotalMem, bSWTaskAvgCPUUsageHigh=bSWTaskAvgCPUUsageHigh, bSWTaskCPUUsage=bSWTaskCPUUsage, bSWTaskInfoEntry=bSWTaskInfoEntry, bSWTaskSharedMem=bSWTaskSharedMem, bSWTaskDataSegmentSize=bSWTaskDataSegmentSize, bSysAvgCPUUtil1Min=bSysAvgCPUUtil1Min)
