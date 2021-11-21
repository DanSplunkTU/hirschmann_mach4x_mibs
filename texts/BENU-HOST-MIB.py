#
# PySNMP MIB module BENU-HOST-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/benuos/BENU-HOST-MIB
# Produced by pysmi-1.1.3 at Sun Nov 21 00:50:41 2021
# On host fv-az39-63 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
benuPlatform, = mibBuilder.importSymbols("BENU-PLATFORM-MIB", "benuPlatform")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, Gauge32, Integer32, ModuleIdentity, ObjectIdentity, IpAddress, NotificationType, Bits, iso, MibIdentifier, Counter64, Counter32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Gauge32", "Integer32", "ModuleIdentity", "ObjectIdentity", "IpAddress", "NotificationType", "Bits", "iso", "MibIdentifier", "Counter64", "Counter32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
bHostMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 39406, 1, 5))
bHostMIB.setRevisions(('2015-11-03 00:00', '2015-04-28 00:00', '2015-04-27 00:00', '2015-01-05 00:00', '2015-01-04 00:00', '2014-12-17 00:00', '2014-09-22 00:00', '2014-03-21 00:00', '2013-05-27 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: bHostMIB.setRevisionsDescriptions(('Changed bSysTotalMem, bSysMemUsed and bSysMemFree from CounterBasedGauge64 to Unsigned32', 'Improved the use of 64 Bit Gauge by replacing Unsigned64 with CounterBasedGauge64', 'Updated the description of bSWTaskRunStateTime', 'Updated notification assignments to comply with standards (RFC 2578).', 'Updated MIB file with change in MAX-ACCESS level for notification objects.', 'updated MIB file with change in bHostNotifObjects', 'Changed bSWTaskRunStateTime from Unsigned32 to TimeTicks', 'Trap definitions are changed', 'Initial Version',))
if mibBuilder.loadTexts: bHostMIB.setLastUpdated('201511030000Z')
if mibBuilder.loadTexts: bHostMIB.setOrganization('Benu Networks')
if mibBuilder.loadTexts: bHostMIB.setContactInfo('Benu Networks Inc,\n      300 Concord Road,\n      Billerca MA 01821\n      Email: support@benunets.com')
if mibBuilder.loadTexts: bHostMIB.setDescription('This mib module defines statistics for software \n        running entities.\n        Copyright (C) 2001, 2008 by Benu Networks, Inc.\n        All rights reserved.')
bHostMIBObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 39406, 1, 5, 1))
if mibBuilder.loadTexts: bHostMIBObjects.setStatus('current')
if mibBuilder.loadTexts: bHostMIBObjects.setDescription('MIB objects for Host related  statistics are defined in this branch.')
bHostNotifObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 39406, 1, 5, 0))
if mibBuilder.loadTexts: bHostNotifObjects.setStatus('current')
if mibBuilder.loadTexts: bHostNotifObjects.setDescription('Notifications of Host related statistics are defined in this branch.')
bHostNotifVariables = ObjectIdentity((1, 3, 6, 1, 4, 1, 39406, 1, 5, 2))
if mibBuilder.loadTexts: bHostNotifVariables.setStatus('current')
if mibBuilder.loadTexts: bHostNotifVariables.setDescription('MIB objects for Host notifications are defined in this branch.')
bSWTaskInfoTable = MibTable((1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 1), )
if mibBuilder.loadTexts: bSWTaskInfoTable.setStatus('current')
if mibBuilder.loadTexts: bSWTaskInfoTable.setDescription('The (conceptual) table of running software\n        performance metrics.')
bSWTaskInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 1, 1), ).setIndexNames((0, "BENU-HOST-MIB", "bSWTaskIndex"))
if mibBuilder.loadTexts: bSWTaskInfoEntry.setStatus('current')
if mibBuilder.loadTexts: bSWTaskInfoEntry.setDescription('A (conceptual) entry containing software performance\n        metrics. ')
bSWTaskIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: bSWTaskIndex.setStatus('current')
if mibBuilder.loadTexts: bSWTaskIndex.setDescription('Index of the software task entry in the table.')
bSWTaskName = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bSWTaskName.setStatus('current')
if mibBuilder.loadTexts: bSWTaskName.setDescription('The name  of the running software task.')
bSWTaskProcessID = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bSWTaskProcessID.setStatus('current')
if mibBuilder.loadTexts: bSWTaskProcessID.setDescription('Indicates Process ID.')
bSWTaskLoadIntervalDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bSWTaskLoadIntervalDuration.setStatus('current')
if mibBuilder.loadTexts: bSWTaskLoadIntervalDuration.setDescription('Load interval duration in seconds.')
bSWTaskRunStateTime = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 1, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bSWTaskRunStateTime.setStatus('current')
if mibBuilder.loadTexts: bSWTaskRunStateTime.setDescription('The amount of  CPU time used by the process since it is started.\n        Value will be in hundredths of a second')
bSWTaskCPUUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 1, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bSWTaskCPUUsage.setStatus('current')
if mibBuilder.loadTexts: bSWTaskCPUUsage.setDescription('CPU usage of the task in the last 1 sec interval duration.\n        The task share of the elapsed time as a percentage of total CPU \n        time is recorded for one second.\n        Unit is percentage. Range is from 0 to maxcore*100 ')
bSWTaskAvgCPUUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 1, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bSWTaskAvgCPUUsage.setStatus('current')
if mibBuilder.loadTexts: bSWTaskAvgCPUUsage.setDescription('Average  CPU usage of the task in the last load interval duration.\n        The task share of the elapsed time as a percentage of total CPU \n        time is recorded for every one second.These one second samples are\n        averaged over a period of load interval.After every one second, older\n        one sec sample will be discarded and new sample will be added to the \n        set . After addition of a new sample value , average over one second\n        samples in a interval  will be done. \n        Unit is percentage. Range is from 0 to maxcore*100 ')
bSWTaskMaxCPUUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 1, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bSWTaskMaxCPUUsage.setStatus('current')
if mibBuilder.loadTexts: bSWTaskMaxCPUUsage.setDescription('Maximum  CPU usage of the task in the last load interval duration.\n        The task share of the elapsed time as a percentage of total CPU \n        time is recorded for every one second. The maximum of these one \n        second samples is calculated over a period of load interval duration. \n        This counter enable to detect the spikes in cpu usage .\n        After every one second, older one sec sample will be discarded and \n        new sample will be added to the set . After addition of new sample \n        value , maximum value over one second intervals in a interval \n        duration will be calculated . \n        Unit is percentage. Range is from 0 to maxcore*100 ')
bSWTaskCodeSegmentSize = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 1, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bSWTaskCodeSegmentSize.setStatus('current')
if mibBuilder.loadTexts: bSWTaskCodeSegmentSize.setDescription('Code segment size of the process.\n        Units kilo-bytes')
bSWTaskDataSegmentSize = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 1, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bSWTaskDataSegmentSize.setStatus('current')
if mibBuilder.loadTexts: bSWTaskDataSegmentSize.setDescription('Data segment  size of the process.\n        Units kilo-bytes')
bSWTaskResidentPhyMem = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 1, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bSWTaskResidentPhyMem.setStatus('current')
if mibBuilder.loadTexts: bSWTaskResidentPhyMem.setDescription('The non-swapped physical memory a task has used.\n        Units kilo-bytes')
bSWTaskVirtMemUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 1, 1, 12), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bSWTaskVirtMemUsage.setStatus('current')
if mibBuilder.loadTexts: bSWTaskVirtMemUsage.setDescription('The  total  amount  of virtual memory used by the task.\n        Units kilo-bytes')
bSWTaskSharedMem = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 1, 1, 13), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bSWTaskSharedMem.setStatus('current')
if mibBuilder.loadTexts: bSWTaskSharedMem.setDescription('The amount of shared memory used by a task. \n        Units kilo-bytes')
bSWTaskVirtMemPeakUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 1, 1, 14), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bSWTaskVirtMemPeakUsage.setStatus('current')
if mibBuilder.loadTexts: bSWTaskVirtMemPeakUsage.setDescription('The peak usage of total  amount  of virtual memory used \n\tby the task.\n        Units kilo-bytes')
bSWTaskAvgCPUUsageHighThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 1, 1, 15), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bSWTaskAvgCPUUsageHighThreshold.setStatus('current')
if mibBuilder.loadTexts: bSWTaskAvgCPUUsageHighThreshold.setDescription('The high threshold for average cpu utilization of a task  \n        in a load interval.  If a bSWTaskAvgCPUUsageLow event has\n        been generated ( or  no bSWTaskAvgCPUUsageHigh was\n        generated previously ) for this task, and the value for\n        average cpu utilization  has exceeded the value of\n        bSWTaskAvgCPUUsageHighThreshold, then a\n        bSWTaskAvgCPUUsageHigh event will be generated.  No more\n        bSWTaskAvgCPUUsageHigh events will be generated for this\n        task  until the value for average cpu utilization becomes equal to \n        or less than the value of bSWTaskAvgCPUUsageLowThreshold.\n         Unit is percentage. Range is from 0 to bSWTaskCPUUsageLimit ')
bSWTaskAvgCPUUsageLowThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 1, 1, 16), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bSWTaskAvgCPUUsageLowThreshold.setStatus('current')
if mibBuilder.loadTexts: bSWTaskAvgCPUUsageLowThreshold.setDescription('The low threshold for avaerage cpu utilization of a task  \n        in a load interval.  If a bSWTaskAvgCPUUsageHigh event has\n        been generated ( or  no bSWTaskAvgCPUUsageLow was\n        generated previously ) for this task, and the value for\n        average cpu utilization  has fallen below the value of\n        bSWTaskAvgCPUUsageLowThreshold, then a\n        bSWTaskAvgCPUUsageLow event will be generated.  No more\n        bSWTaskAvgCPUUsageLow events will be generated for this\n        task  until the value for average cpu utilization exceeds  \n        the value of bSWTaskAvgCPUUsageHighThreshold.\n        Unit is percentage. Range is from 0 to bSWTaskAvgCPUUsageHighThreshold ')
bSWTaskCPUUsageLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 1, 1, 17), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bSWTaskCPUUsageLimit.setStatus('current')
if mibBuilder.loadTexts: bSWTaskCPUUsageLimit.setDescription('The limit on cpu usage of the process.When cpu usage of a \n         process reaches this limit , process would be killed and \n         bSWTaskDied notification will be sent. The reason in this \n         notification would be cpuUsageLimitReached .\n         Unit is percentage. Range is from 0 to maxcore*100 ')
bSWTaskRestartLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 1, 1, 18), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bSWTaskRestartLimit.setStatus('current')
if mibBuilder.loadTexts: bSWTaskRestartLimit.setDescription('The limit on restart of the process.When bSWTaskRestartCount\n         of a process reaches this limit , process would not be restarted\n         and bSWTaskRestartLimitReached notification will be  sent')
bSWTaskRestartability = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 1, 1, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("yes", 1), ("no", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bSWTaskRestartability.setStatus('current')
if mibBuilder.loadTexts: bSWTaskRestartability.setDescription('This indicates whether a process is enabled or not for \n        restart. If enabled the process in context respawns after\n        it has crashed/stopped.')
bSWTaskRestartCount = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 1, 1, 20), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bSWTaskRestartCount.setStatus('current')
if mibBuilder.loadTexts: bSWTaskRestartCount.setDescription('This indicates the number of times the process has\n        respawned/restarted.')
bSysTotalMem = MibScalar((1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bSysTotalMem.setStatus('current')
if mibBuilder.loadTexts: bSysTotalMem.setDescription('Total Usable RAM, kilobytes')
bSysMemUsed = MibScalar((1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bSysMemUsed.setStatus('current')
if mibBuilder.loadTexts: bSysMemUsed.setDescription('The amount of physical RAM, in kilobytes, used by the system.')
bSysMemFree = MibScalar((1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bSysMemFree.setStatus('current')
if mibBuilder.loadTexts: bSysMemFree.setDescription('The amount of physical RAM, in kilobytes, left unused by the system.')
bSysTotalCPUUtilAvailable = MibScalar((1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bSysTotalCPUUtilAvailable.setStatus('current')
if mibBuilder.loadTexts: bSysTotalCPUUtilAvailable.setDescription('The total CPU utilization available across all CPU cores.\n         The value is maxcores * 100 percentage.')
bSysAvgCPUUtil15Sec = MibScalar((1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bSysAvgCPUUtil15Sec.setStatus('current')
if mibBuilder.loadTexts: bSysAvgCPUUtil15Sec.setDescription('The average CPU utilization across all CPU cores\n         in the last 15 seconds.\n         This value is updated for every bCPUMonInterval seconds.\n         Units is percentage . Range is from 0 to  100 .')
bSysAvgCPUUtil1Min = MibScalar((1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bSysAvgCPUUtil1Min.setStatus('current')
if mibBuilder.loadTexts: bSysAvgCPUUtil1Min.setDescription('The average CPU utilization across all CPU cores\n         in the last one minute.\n         This value is updated for every bCPUMonInterval seconds.\n         Units is percentage . Range is from 0 to  100 .')
bSysAvgCPUUtil5Min = MibScalar((1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bSysAvgCPUUtil5Min.setStatus('current')
if mibBuilder.loadTexts: bSysAvgCPUUtil5Min.setDescription('The average CPU utilization across all CPU cores\n         in the last five minutes.\n         This value is updated for every bCPUMonInterval seconds.\n         Units is percentage . Range is from 0 to  100 .')
bCPUMonInterval = MibScalar((1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 9), Unsigned32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: bCPUMonInterval.setStatus('current')
if mibBuilder.loadTexts: bCPUMonInterval.setDescription('CPU usage sampling interval. The value of this\n        object in seconds indicates the how often the \n        CPU utilization is calculated and monitored across all cores.\n        This value for this will be configured by the CLI.')
bSWTaskDiedReason = MibScalar((1, 3, 6, 1, 4, 1, 39406, 1, 5, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("cpuUsageLimitReached", 1), ("unKnown", 2)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bSWTaskDiedReason.setStatus('current')
if mibBuilder.loadTexts: bSWTaskDiedReason.setDescription('This indicates the reason for process kill')
bSWProcessName = MibScalar((1, 3, 6, 1, 4, 1, 39406, 1, 5, 2, 2), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bSWProcessName.setStatus('current')
if mibBuilder.loadTexts: bSWProcessName.setDescription('The name  of the running software task.')
bSWProcessID = MibScalar((1, 3, 6, 1, 4, 1, 39406, 1, 5, 2, 3), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bSWProcessID.setStatus('current')
if mibBuilder.loadTexts: bSWProcessID.setDescription('Indicates Process ID.')
bSWProcessAvgCPUUsageLowThreshold = MibScalar((1, 3, 6, 1, 4, 1, 39406, 1, 5, 2, 4), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bSWProcessAvgCPUUsageLowThreshold.setStatus('current')
if mibBuilder.loadTexts: bSWProcessAvgCPUUsageLowThreshold.setDescription('The low threshold for avaerage cpu utilization of a task\n        in a load interval.  If a bSWTaskAvgCPUUsageHigh event has\n        been generated ( or  no bSWTaskAvgCPUUsageLow was\n        generated previously ) for this task, and the value for\n        average cpu utilization  has fallen below the value of\n        bSWTaskAvgCPUUsageLowThreshold, then a\n        bSWTaskAvgCPUUsageLow event will be generated.  No more\n        bSWTaskAvgCPUUsageLow events will be generated for this\n        task  until the value for average cpu utilization exceeds\n        the value of bSWTaskAvgCPUUsageHighThreshold.\n        Unit is percentage. Range is from 0 to bSWTaskAvgCPUUsageHighThreshold ')
bSWProcessAvgCPUUsageHighThreshold = MibScalar((1, 3, 6, 1, 4, 1, 39406, 1, 5, 2, 5), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bSWProcessAvgCPUUsageHighThreshold.setStatus('current')
if mibBuilder.loadTexts: bSWProcessAvgCPUUsageHighThreshold.setDescription('The high threshold for average cpu utilization of a task\n        in a load interval.  If a bSWTaskAvgCPUUsageLow event has\n        been generated ( or  no bSWTaskAvgCPUUsageHigh was\n        generated previously ) for this task, and the value for\n        average cpu utilization  has exceeded the value of\n        bSWTaskAvgCPUUsageHighThreshold, then a\n        bSWTaskAvgCPUUsageHigh event will be generated.  No more\n        bSWTaskAvgCPUUsageHigh events will be generated for this\n        task  until the value for average cpu utilization becomes equal to\n        or less than the value of bSWTaskAvgCPUUsageLowThreshold.\n         Unit is percentage. Range is from 0 to bSWTaskCPUUsageLimit ')
bSWTaskAvgCPUUsageLow = NotificationType((1, 3, 6, 1, 4, 1, 39406, 1, 5, 0, 1)).setObjects(("BENU-HOST-MIB", "bSWProcessName"), ("BENU-HOST-MIB", "bSWProcessID"), ("BENU-HOST-MIB", "bSWProcessAvgCPUUsageLowThreshold"))
if mibBuilder.loadTexts: bSWTaskAvgCPUUsageLow.setStatus('current')
if mibBuilder.loadTexts: bSWTaskAvgCPUUsageLow.setDescription('This notification signifies that the average cpu utilization\n        in a load interval is cleared , meaning that it\n        has fallen below the  value of bSWTaskAvgCPUUsageLowThreshold\n        for that task bSWTaskName.')
bSWTaskAvgCPUUsageHigh = NotificationType((1, 3, 6, 1, 4, 1, 39406, 1, 5, 0, 2)).setObjects(("BENU-HOST-MIB", "bSWProcessName"), ("BENU-HOST-MIB", "bSWProcessID"), ("BENU-HOST-MIB", "bSWProcessAvgCPUUsageHighThreshold"))
if mibBuilder.loadTexts: bSWTaskAvgCPUUsageHigh.setStatus('current')
if mibBuilder.loadTexts: bSWTaskAvgCPUUsageHigh.setDescription('This notification signifies that the average cpu utilization\n        in a load interval has risen above the  value of \n        bSWTaskAvgCPUUsageHighThreshold for that task bSWTaskName.')
bSWTaskDied = NotificationType((1, 3, 6, 1, 4, 1, 39406, 1, 5, 0, 3)).setObjects(("BENU-HOST-MIB", "bSWProcessName"), ("BENU-HOST-MIB", "bSWProcessID"), ("BENU-HOST-MIB", "bSWTaskDiedReason"))
if mibBuilder.loadTexts: bSWTaskDied.setStatus('current')
if mibBuilder.loadTexts: bSWTaskDied.setDescription('This notification signifies that the process has died.\n         This notification will also be sent if the process \n\t manager kills a process because of reaching cpu usage limit\n         or process crashed/terminated')
bSWTaskRestartLimitReached = NotificationType((1, 3, 6, 1, 4, 1, 39406, 1, 5, 0, 4)).setObjects(("BENU-HOST-MIB", "bSWProcessName"), ("BENU-HOST-MIB", "bSWProcessID"))
if mibBuilder.loadTexts: bSWTaskRestartLimitReached.setStatus('current')
if mibBuilder.loadTexts: bSWTaskRestartLimitReached.setDescription('This notification signifies that the process has reached maximum\n         restarts and all the attempts to restart the process has failed.')
mibBuilder.exportSymbols("BENU-HOST-MIB", bSWTaskRestartLimitReached=bSWTaskRestartLimitReached, bHostMIBObjects=bHostMIBObjects, bSWTaskAvgCPUUsageHigh=bSWTaskAvgCPUUsageHigh, bSWTaskInfoEntry=bSWTaskInfoEntry, bSysMemUsed=bSysMemUsed, bSWTaskDataSegmentSize=bSWTaskDataSegmentSize, bSWTaskProcessID=bSWTaskProcessID, bHostMIB=bHostMIB, PYSNMP_MODULE_ID=bHostMIB, bSWTaskAvgCPUUsageLow=bSWTaskAvgCPUUsageLow, bSWTaskIndex=bSWTaskIndex, bSysAvgCPUUtil1Min=bSysAvgCPUUtil1Min, bSWProcessName=bSWProcessName, bSWTaskLoadIntervalDuration=bSWTaskLoadIntervalDuration, bHostNotifObjects=bHostNotifObjects, bSWTaskRestartability=bSWTaskRestartability, bSWTaskName=bSWTaskName, bSWTaskCPUUsageLimit=bSWTaskCPUUsageLimit, bSysMemFree=bSysMemFree, bSWTaskAvgCPUUsageHighThreshold=bSWTaskAvgCPUUsageHighThreshold, bCPUMonInterval=bCPUMonInterval, bSWTaskCodeSegmentSize=bSWTaskCodeSegmentSize, bSysAvgCPUUtil15Sec=bSysAvgCPUUtil15Sec, bSysAvgCPUUtil5Min=bSysAvgCPUUtil5Min, bSWTaskDiedReason=bSWTaskDiedReason, bSWProcessID=bSWProcessID, bSWTaskRunStateTime=bSWTaskRunStateTime, bSWTaskRestartLimit=bSWTaskRestartLimit, bSysTotalMem=bSysTotalMem, bSWProcessAvgCPUUsageHighThreshold=bSWProcessAvgCPUUsageHighThreshold, bSWTaskInfoTable=bSWTaskInfoTable, bSWTaskVirtMemPeakUsage=bSWTaskVirtMemPeakUsage, bSWTaskResidentPhyMem=bSWTaskResidentPhyMem, bSWTaskSharedMem=bSWTaskSharedMem, bSWTaskCPUUsage=bSWTaskCPUUsage, bSWProcessAvgCPUUsageLowThreshold=bSWProcessAvgCPUUsageLowThreshold, bSWTaskAvgCPUUsage=bSWTaskAvgCPUUsage, bSWTaskDied=bSWTaskDied, bSWTaskVirtMemUsage=bSWTaskVirtMemUsage, bSWTaskAvgCPUUsageLowThreshold=bSWTaskAvgCPUUsageLowThreshold, bSWTaskRestartCount=bSWTaskRestartCount, bSysTotalCPUUtilAvailable=bSysTotalCPUUtilAvailable, bHostNotifVariables=bHostNotifVariables, bSWTaskMaxCPUUsage=bSWTaskMaxCPUUsage)
