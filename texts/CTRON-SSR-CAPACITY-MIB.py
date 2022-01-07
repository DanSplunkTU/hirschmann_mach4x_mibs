#
# PySNMP MIB module CTRON-SSR-CAPACITY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-SSR-CAPACITY-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:20:26 2022
# On host fv-az36-988 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
ssrMibs, = mibBuilder.importSymbols("CTRON-SSR-SMI-MIB", "ssrMibs")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
iso, Counter64, TimeTicks, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, IpAddress, Counter32, NotificationType, ModuleIdentity, Gauge32, Integer32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Counter64", "TimeTicks", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "IpAddress", "Counter32", "NotificationType", "ModuleIdentity", "Gauge32", "Integer32", "Bits")
TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString")
capacityMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 52, 2501, 1, 270))
capacityMIB.setRevisions(('2000-07-15 00:00', '1998-11-05 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: capacityMIB.setRevisionsDescriptions(('Update contact information, Change object name chassis\n         to chassisCap due to collsion with chassis in ctron-mib-names.txt.\n         SSR enterprise mibs apply to the Riverstone RS product line and\n         Enterasys SSR.', 'Revision 1.0 Initial MIB revision.',))
if mibBuilder.loadTexts: capacityMIB.setLastUpdated('200007150000Z')
if mibBuilder.loadTexts: capacityMIB.setOrganization('Enterasys Networks, Inc.')
if mibBuilder.loadTexts: capacityMIB.setContactInfo('Enterasys Networks\n     35 Industrial Way, P.O. Box 5005\n     Rochester, NH 03867-0505\n     (603) 332-9400\n     support@enterasys.com\n     http://www.enterasys.com')
if mibBuilder.loadTexts: capacityMIB.setDescription('This module defines a schema to access RS system resource \n      capacity statistics.')
class SSRMemoryType(TextualConvention, Integer32):
    description = 'A unique value, greater than zero, for each non-volatile memory\n        device supported by the SSR series of products.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("cpu", 1), ("intFlash", 2), ("pcmcia", 3), ("rmon", 4), ("l2Hardware", 5), ("l3Hardware", 6))

class SSRCapabilityType(TextualConvention, Integer32):
    description = 'A unique value, greater than zero, for the different \n         capabilities of the SSR chassis.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("noSupport", 1), ("available", 2), ("enabled", 3), ("disabled", 4))

class SSRStatusType(TextualConvention, Integer32):
    description = 'A unique value, greater than zero, for each possible state\n        a task on the SSR can be in.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    namedValues = NamedValues(("ready", 0), ("suspPure", 1), ("suspSleep", 2), ("suspMbox", 3), ("suspQue", 4), ("suspPipe", 5), ("suspSema4", 6), ("suspEvent", 7), ("suspPart", 8), ("suspMem", 9), ("suspDrvr", 10), ("finished", 11), ("terminated", 12))

chassisCap = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 1))
cpu = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 2))
tasks = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 3))
memory = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 4))
capChassisSlotCount = MibScalar((1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(2, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: capChassisSlotCount.setStatus('current')
if mibBuilder.loadTexts: capChassisSlotCount.setDescription('The maximum number of slots in the chassis, including the\n                slot for the CPU module.')
capChassisSlotsUsed = MibScalar((1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: capChassisSlotsUsed.setStatus('current')
if mibBuilder.loadTexts: capChassisSlotsUsed.setDescription('The number of slots used in the chassis.  This number \n                includes the slot used for the CPU module, if any.')
capChassisSlotsFree = MibScalar((1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: capChassisSlotsFree.setStatus('current')
if mibBuilder.loadTexts: capChassisSlotsFree.setDescription('The number of free slots in the chassis.  This includes\n                all of the available slots not used by the CPU or redundant\n                CPU card.')
capChassisCPURedundancy = MibScalar((1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 1, 4), SSRCapabilityType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capChassisCPURedundancy.setStatus('current')
if mibBuilder.loadTexts: capChassisCPURedundancy.setDescription('The chassis CPU redundancy capability of the SSR.  This\n                will be one of the following values:\n                  noSupport(1)   -- feature not supported\n                  available(2)   -- feature not in use\n                  enabled(3)     -- feature in use and enabled\n                  disabled(4)    -- feature in use and disabled\n               ')
capChassisPSRedundancy = MibScalar((1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 1, 5), SSRCapabilityType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capChassisPSRedundancy.setStatus('current')
if mibBuilder.loadTexts: capChassisPSRedundancy.setDescription('The chassis Power Supply redundancy capability of the SSR.  \n                This will be one of the following values:\n                  noSupport(1)   -- feature not supported\n                  available(2)   -- feature not in use\n                  enabled(3)     -- feature in use and enabled\n                  disabled(4)    -- feature in use and disabled\n               ')
capChassisSFRedundancy = MibScalar((1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 1, 6), SSRCapabilityType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capChassisSFRedundancy.setStatus('current')
if mibBuilder.loadTexts: capChassisSFRedundancy.setDescription('The chassis Switching Fabric redundancy capability of the SSR. \n                This will be one of the following values:\n                  noSupport(1)   -- feature not supported\n                  available(2)   -- feature not in use\n                  enabled(3)     -- feature in use and enabled\n                  disabled(4)    -- feature in use and disabled\n               ')
capCPUTable = MibTable((1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 2, 1), )
if mibBuilder.loadTexts: capCPUTable.setStatus('current')
if mibBuilder.loadTexts: capCPUTable.setDescription('Summary of CPU statistics.  It is assumed that there is only \n         one CPU per line card.')
capCPUEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 2, 1, 1), ).setIndexNames((0, "CTRON-SSR-CAPACITY-MIB", "capCPUModuleIndex"))
if mibBuilder.loadTexts: capCPUEntry.setStatus('current')
if mibBuilder.loadTexts: capCPUEntry.setDescription('An entry containing CPU statistics information.')
capCPUModuleIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295)))
if mibBuilder.loadTexts: capCPUModuleIndex.setStatus('current')
if mibBuilder.loadTexts: capCPUModuleIndex.setDescription('The Slot index in which the current CPU is residing.')
capCPUCurrentUtilization = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: capCPUCurrentUtilization.setStatus('current')
if mibBuilder.loadTexts: capCPUCurrentUtilization.setDescription('The CPU utilization expressed as an integer percentage.\n                This is calculated over the last 5 seconds at a 0.1 second\n                interval as a simple average.')
capCPUL3Learned = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 2, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capCPUL3Learned.setStatus('current')
if mibBuilder.loadTexts: capCPUL3Learned.setDescription('The total number of new layer 3 flows the CPU has processed and\n                programmed into the Layer 3 hardware flow tables. \n\n                Layer 3 flows are packets for IP or IPX protocols that will\n                be routed from one subnet to another. Bridged flows or IP and\n                IPX flows that originate and terminate in the same subnet\n                are accounted for by capCPUL2Learned object.')
capCPUL3Aged = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 2, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capCPUL3Aged.setStatus('current')
if mibBuilder.loadTexts: capCPUL3Aged.setDescription('The total number of Layer 3flows that have been\n                removed from the layer 3 hardware flow tables across \n                all modules by the Layer 3 aging task. This number may\n                increase quickly if routing protocols are not stable. Removal\n                or insertion of routes into the forwarding table will cause\n                premature aging of flows. Flows are normally aged/removed \n                from the hardware when there are no more packets being sent\n                for a defined time period.  \n                This counter is cumulative from the time the system started.')
capCPUL2Learned = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 2, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capCPUL2Learned.setStatus('current')
if mibBuilder.loadTexts: capCPUL2Learned.setDescription('The number of L2 flows or addresses learned. \n                The intended result here is to see how many stations \n                attempt to establish switched communication through the SSR.')
capCPUL2Aged = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 2, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capCPUL2Aged.setStatus('current')
if mibBuilder.loadTexts: capCPUL2Aged.setDescription('The total number of L2 addresses or flows aged out.  Hosts\n                that end switched communication through the SSR are aged out\n                every 15 seconds.')
capCPUNIAReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 2, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capCPUNIAReceived.setStatus('current')
if mibBuilder.loadTexts: capCPUNIAReceived.setDescription('The total number of packets received by the NIA chip.\n                This is useful in gauging how many packets are forwarded\n                to the CPU for processing.')
capCPUNIATransmitted = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 2, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capCPUNIATransmitted.setStatus('current')
if mibBuilder.loadTexts: capCPUNIATransmitted.setDescription('The total number of packets transmitted by the NIA chip. \n                This is useful in seeing how much the CPU is communicating\n                directory with management stations and other routers.')
capCPUMinThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 2, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 99))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: capCPUMinThreshold.setStatus('current')
if mibBuilder.loadTexts: capCPUMinThreshold.setDescription('The CPU utilization expressed as an integer percentage.\n                This value represents the threshold minimum value for\n                capCPUCurrentUtilization that is used to reset the\n                threshold testing for generation of the\n                envCPUThresholdTrap. This value is equal to 0 by\n                default. When this value or the value of\n                capCPUMaxThreshold is equal to 0, no envCPUThresholdTrap\n                will be generated.')
capCPUMaxThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 2, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 99))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: capCPUMaxThreshold.setStatus('current')
if mibBuilder.loadTexts: capCPUMaxThreshold.setDescription('The CPU utilization expressed as an integer percentage.\n                This value represents the threshold maximum for\n                capCPUCurrentUtilization which causes generation of the\n                envCPUThresholdTrap. Another trap is not generated until\n                the capCPUCurrentUtilization value has dropped below\n                capCPUMinThreshold. When this value or the value of\n                capCPUMinThreshold is equal to 0, no envCPUThresholdTrap\n                will be generated.')
capTaskTable = MibTable((1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 3, 1), )
if mibBuilder.loadTexts: capTaskTable.setStatus('current')
if mibBuilder.loadTexts: capTaskTable.setDescription('A summary of the tasks running on a CPU enabled module in \n         the chassis.')
capTaskEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 3, 1, 1), ).setIndexNames((0, "CTRON-SSR-CAPACITY-MIB", "capTaskModuleIndex"), (0, "CTRON-SSR-CAPACITY-MIB", "capTaskIndex"))
if mibBuilder.loadTexts: capTaskEntry.setStatus('current')
if mibBuilder.loadTexts: capTaskEntry.setDescription('An entry containing information on a task running on a CPU enabled\n         module in the chassis including the memory consumption and current\n         status.')
capTaskModuleIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: capTaskModuleIndex.setStatus('current')
if mibBuilder.loadTexts: capTaskModuleIndex.setDescription('The module index on which the task is running.')
capTaskIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: capTaskIndex.setStatus('current')
if mibBuilder.loadTexts: capTaskIndex.setDescription('A unique index assigned to a task instance.  This index is\n                unique to the task for the time SSR is booted.  If the task\n                is terminated, the index will not be reused for another task\n                that might become active in the system.')
capTaskName = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 3, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: capTaskName.setStatus('current')
if mibBuilder.loadTexts: capTaskName.setDescription('The encrypted name assigned to this task.  This is unique \n                for each different type of task, but there may be multiple \n                instances of the same task running in the system.')
capTaskShed = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 3, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capTaskShed.setStatus('current')
if mibBuilder.loadTexts: capTaskShed.setDescription('The number of times this task has been scheduled to run.  \n                This is a cumulative count from the time the SSR was started.')
capTaskStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 3, 1, 1, 5), SSRStatusType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capTaskStatus.setStatus('current')
if mibBuilder.loadTexts: capTaskStatus.setDescription('The current status of this task.')
capTaskUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 3, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: capTaskUsed.setStatus('current')
if mibBuilder.loadTexts: capTaskUsed.setDescription('The size of the memory consumed by this task.  This can be \n                used to monitor any excess memory use by a particular task \n                and is expressed in bytes.')
capMemoryTable = MibTable((1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 4, 1), )
if mibBuilder.loadTexts: capMemoryTable.setStatus('current')
if mibBuilder.loadTexts: capMemoryTable.setDescription('A summary of the non-volatile storage devices in the SSR.')
capMemoryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 4, 1, 1), ).setIndexNames((0, "CTRON-SSR-CAPACITY-MIB", "capMemoryType"), (0, "CTRON-SSR-CAPACITY-MIB", "capMemoryIndex"))
if mibBuilder.loadTexts: capMemoryEntry.setStatus('current')
if mibBuilder.loadTexts: capMemoryEntry.setDescription('An entry containing information on a non-volatile memory device\n         in the SSR.')
capMemoryType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 4, 1, 1, 1), SSRMemoryType())
if mibBuilder.loadTexts: capMemoryType.setStatus('current')
if mibBuilder.loadTexts: capMemoryType.setDescription('A type of storage device from the enumerated memory types.')
capMemoryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 4, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: capMemoryIndex.setStatus('current')
if mibBuilder.loadTexts: capMemoryIndex.setDescription('An index or enumeration for the entries of a particular \n                memory type.  This index corresponds to:\n                   -- Interface index for L2Hardware Type\n                   -- Module index for L3Hardware Type\n                   -- Enumeration for everything else.')
capMemoryDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 4, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("readonly")
if mibBuilder.loadTexts: capMemoryDescr.setStatus('current')
if mibBuilder.loadTexts: capMemoryDescr.setDescription('The description of the memory device.')
capMemorySize = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 4, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: capMemorySize.setStatus('current')
if mibBuilder.loadTexts: capMemorySize.setDescription('Memory device total memory capacity expressed in blocks.')
capMemoryFree = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 4, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: capMemoryFree.setStatus('current')
if mibBuilder.loadTexts: capMemoryFree.setDescription('Memory device free memory in blocks.  This will include any\n         unused memory between used memory blocks and is calculated by\n         subtracting the memory used from the size of the memory device.')
capMemoryUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 4, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: capMemoryUsed.setStatus('current')
if mibBuilder.loadTexts: capMemoryUsed.setDescription('Size of used memory on the memory device.  This includes the blocks\n         of memory that are only partially used and is expressed in blocks.')
capMemoryBlockSize = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 4, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: capMemoryBlockSize.setStatus('current')
if mibBuilder.loadTexts: capMemoryBlockSize.setDescription('Size of the memory blocks on the memory device.  This is the \n         minimum block size of memory returned when memory is requested \n         and is expressed in bytes.')
capMemoryFailures = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 4, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capMemoryFailures.setStatus('current')
if mibBuilder.loadTexts: capMemoryFailures.setDescription('The number of times a memory allocation in this memory device has\n         failed.  In the case of L2Hardware and L3Hardware types it expresses\n         the number of times a Full Hash Bucket condition has been met.')
capMemoryRemovable = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 4, 1, 1, 9), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capMemoryRemovable.setStatus('current')
if mibBuilder.loadTexts: capMemoryRemovable.setDescription('Indicates if the memory type is removable.')
capConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 6))
capCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 6, 1))
capGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 6, 2))
capComplianceV10 = ModuleCompliance((1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 6, 2, 1, 1)).setObjects(("CTRON-SSR-CAPACITY-MIB", "capConfGroupV10"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    capComplianceV10 = capComplianceV10.setStatus('deprecated')
if mibBuilder.loadTexts: capComplianceV10.setDescription('The compliance statement for the SSR-CAPACITY-MIB.')
capComplianceV20 = ModuleCompliance((1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 6, 2, 2, 1)).setObjects(("CTRON-SSR-CAPACITY-MIB", "capConfGroupV20"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    capComplianceV20 = capComplianceV20.setStatus('current')
if mibBuilder.loadTexts: capComplianceV20.setDescription('The compliance statement for the SSR-CAPACITY-MIB.')
capConfGroupV10 = ObjectGroup((1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 6, 2, 1)).setObjects(("CTRON-SSR-CAPACITY-MIB", "capChassisSlotCount"), ("CTRON-SSR-CAPACITY-MIB", "capChassisSlotsUsed"), ("CTRON-SSR-CAPACITY-MIB", "capChassisSlotsFree"), ("CTRON-SSR-CAPACITY-MIB", "capChassisCPURedundancy"), ("CTRON-SSR-CAPACITY-MIB", "capChassisPSRedundancy"), ("CTRON-SSR-CAPACITY-MIB", "capChassisSFRedundancy"), ("CTRON-SSR-CAPACITY-MIB", "capCPUCurrentUtilization"), ("CTRON-SSR-CAPACITY-MIB", "capCPUL3Learned"), ("CTRON-SSR-CAPACITY-MIB", "capCPUL3Aged"), ("CTRON-SSR-CAPACITY-MIB", "capCPUL2Learned"), ("CTRON-SSR-CAPACITY-MIB", "capCPUL2Aged"), ("CTRON-SSR-CAPACITY-MIB", "capCPUNIAReceived"), ("CTRON-SSR-CAPACITY-MIB", "capCPUNIATransmitted"), ("CTRON-SSR-CAPACITY-MIB", "capTaskName"), ("CTRON-SSR-CAPACITY-MIB", "capTaskShed"), ("CTRON-SSR-CAPACITY-MIB", "capTaskStatus"), ("CTRON-SSR-CAPACITY-MIB", "capTaskUsed"), ("CTRON-SSR-CAPACITY-MIB", "capMemoryDescr"), ("CTRON-SSR-CAPACITY-MIB", "capMemorySize"), ("CTRON-SSR-CAPACITY-MIB", "capMemoryFree"), ("CTRON-SSR-CAPACITY-MIB", "capMemoryUsed"), ("CTRON-SSR-CAPACITY-MIB", "capMemoryBlockSize"), ("CTRON-SSR-CAPACITY-MIB", "capMemoryFailures"), ("CTRON-SSR-CAPACITY-MIB", "capMemoryRemovable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    capConfGroupV10 = capConfGroupV10.setStatus('deprecated')
if mibBuilder.loadTexts: capConfGroupV10.setDescription('A set of managed objects that make up version 1.0 of the SSR capacity mib.')
capConfGroupV20 = ObjectGroup((1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 6, 2, 2)).setObjects(("CTRON-SSR-CAPACITY-MIB", "capChassisSlotCount"), ("CTRON-SSR-CAPACITY-MIB", "capChassisSlotsUsed"), ("CTRON-SSR-CAPACITY-MIB", "capChassisSlotsFree"), ("CTRON-SSR-CAPACITY-MIB", "capChassisCPURedundancy"), ("CTRON-SSR-CAPACITY-MIB", "capChassisPSRedundancy"), ("CTRON-SSR-CAPACITY-MIB", "capChassisSFRedundancy"), ("CTRON-SSR-CAPACITY-MIB", "capCPUCurrentUtilization"), ("CTRON-SSR-CAPACITY-MIB", "capCPUL3Learned"), ("CTRON-SSR-CAPACITY-MIB", "capCPUL3Aged"), ("CTRON-SSR-CAPACITY-MIB", "capCPUL2Learned"), ("CTRON-SSR-CAPACITY-MIB", "capCPUL2Aged"), ("CTRON-SSR-CAPACITY-MIB", "capCPUNIAReceived"), ("CTRON-SSR-CAPACITY-MIB", "capCPUNIATransmitted"), ("CTRON-SSR-CAPACITY-MIB", "capCPUMinThreshold"), ("CTRON-SSR-CAPACITY-MIB", "capCPUMaxThreshold"), ("CTRON-SSR-CAPACITY-MIB", "capTaskName"), ("CTRON-SSR-CAPACITY-MIB", "capTaskShed"), ("CTRON-SSR-CAPACITY-MIB", "capTaskStatus"), ("CTRON-SSR-CAPACITY-MIB", "capTaskUsed"), ("CTRON-SSR-CAPACITY-MIB", "capMemoryDescr"), ("CTRON-SSR-CAPACITY-MIB", "capMemorySize"), ("CTRON-SSR-CAPACITY-MIB", "capMemoryFree"), ("CTRON-SSR-CAPACITY-MIB", "capMemoryUsed"), ("CTRON-SSR-CAPACITY-MIB", "capMemoryBlockSize"), ("CTRON-SSR-CAPACITY-MIB", "capMemoryFailures"), ("CTRON-SSR-CAPACITY-MIB", "capMemoryRemovable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    capConfGroupV20 = capConfGroupV20.setStatus('current')
if mibBuilder.loadTexts: capConfGroupV20.setDescription('A set of managed objects that make up version 2.0 of the SSR capacity mib.')
mibBuilder.exportSymbols("CTRON-SSR-CAPACITY-MIB", capTaskUsed=capTaskUsed, capCPUEntry=capCPUEntry, memory=memory, capCPUCurrentUtilization=capCPUCurrentUtilization, capCPUMaxThreshold=capCPUMaxThreshold, capChassisSlotsUsed=capChassisSlotsUsed, capTaskTable=capTaskTable, capTaskModuleIndex=capTaskModuleIndex, capCPUL2Aged=capCPUL2Aged, SSRCapabilityType=SSRCapabilityType, capConformance=capConformance, capComplianceV20=capComplianceV20, capCompliances=capCompliances, capMemoryDescr=capMemoryDescr, capCPUL3Aged=capCPUL3Aged, capMemoryFree=capMemoryFree, capCPUMinThreshold=capCPUMinThreshold, capacityMIB=capacityMIB, capMemoryTable=capMemoryTable, capTaskShed=capTaskShed, capCPUNIATransmitted=capCPUNIATransmitted, capMemoryEntry=capMemoryEntry, capTaskIndex=capTaskIndex, capMemoryFailures=capMemoryFailures, cpu=cpu, SSRStatusType=SSRStatusType, capCPUModuleIndex=capCPUModuleIndex, chassisCap=chassisCap, capChassisSlotsFree=capChassisSlotsFree, capMemorySize=capMemorySize, capConfGroupV20=capConfGroupV20, capMemoryUsed=capMemoryUsed, capMemoryIndex=capMemoryIndex, capGroups=capGroups, capTaskStatus=capTaskStatus, capMemoryRemovable=capMemoryRemovable, PYSNMP_MODULE_ID=capacityMIB, tasks=tasks, capComplianceV10=capComplianceV10, capTaskName=capTaskName, capCPUNIAReceived=capCPUNIAReceived, capCPUL3Learned=capCPUL3Learned, capCPUTable=capCPUTable, capChassisSFRedundancy=capChassisSFRedundancy, capTaskEntry=capTaskEntry, capMemoryType=capMemoryType, capMemoryBlockSize=capMemoryBlockSize, capChassisSlotCount=capChassisSlotCount, capConfGroupV10=capConfGroupV10, SSRMemoryType=SSRMemoryType, capCPUL2Learned=capCPUL2Learned, capChassisPSRedundancy=capChassisPSRedundancy, capChassisCPURedundancy=capChassisCPURedundancy)
