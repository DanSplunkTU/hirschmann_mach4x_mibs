#
# PySNMP MIB module CTRON-SSR-CAPACITY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-SSR-CAPACITY-MIB
# Produced by pysmi-1.1.3 at Sun Nov 21 00:45:06 2021
# On host fv-az39-63 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ssrMibs, = mibBuilder.importSymbols("CTRON-SSR-SMI-MIB", "ssrMibs")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, NotificationType, ObjectIdentity, TimeTicks, MibIdentifier, Bits, Integer32, Gauge32, ModuleIdentity, Counter32, Unsigned32, IpAddress, iso = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "NotificationType", "ObjectIdentity", "TimeTicks", "MibIdentifier", "Bits", "Integer32", "Gauge32", "ModuleIdentity", "Counter32", "Unsigned32", "IpAddress", "iso")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
capacityMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 52, 2501, 1, 270))
capacityMIB.setRevisions(('2000-07-15 00:00', '1998-11-05 00:00',))
if mibBuilder.loadTexts: capacityMIB.setLastUpdated('200007150000Z')
if mibBuilder.loadTexts: capacityMIB.setOrganization('Enterasys Networks, Inc.')
class SSRMemoryType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("cpu", 1), ("intFlash", 2), ("pcmcia", 3), ("rmon", 4), ("l2Hardware", 5), ("l3Hardware", 6))

class SSRCapabilityType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("noSupport", 1), ("available", 2), ("enabled", 3), ("disabled", 4))

class SSRStatusType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    namedValues = NamedValues(("ready", 0), ("suspPure", 1), ("suspSleep", 2), ("suspMbox", 3), ("suspQue", 4), ("suspPipe", 5), ("suspSema4", 6), ("suspEvent", 7), ("suspPart", 8), ("suspMem", 9), ("suspDrvr", 10), ("finished", 11), ("terminated", 12))

chassisCap = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 1))
cpu = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 2))
tasks = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 3))
memory = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 4))
capChassisSlotCount = MibScalar((1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(2, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: capChassisSlotCount.setStatus('current')
capChassisSlotsUsed = MibScalar((1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: capChassisSlotsUsed.setStatus('current')
capChassisSlotsFree = MibScalar((1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: capChassisSlotsFree.setStatus('current')
capChassisCPURedundancy = MibScalar((1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 1, 4), SSRCapabilityType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capChassisCPURedundancy.setStatus('current')
capChassisPSRedundancy = MibScalar((1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 1, 5), SSRCapabilityType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capChassisPSRedundancy.setStatus('current')
capChassisSFRedundancy = MibScalar((1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 1, 6), SSRCapabilityType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capChassisSFRedundancy.setStatus('current')
capCPUTable = MibTable((1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 2, 1), )
if mibBuilder.loadTexts: capCPUTable.setStatus('current')
capCPUEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 2, 1, 1), ).setIndexNames((0, "CTRON-SSR-CAPACITY-MIB", "capCPUModuleIndex"))
if mibBuilder.loadTexts: capCPUEntry.setStatus('current')
capCPUModuleIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295)))
if mibBuilder.loadTexts: capCPUModuleIndex.setStatus('current')
capCPUCurrentUtilization = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: capCPUCurrentUtilization.setStatus('current')
capCPUL3Learned = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 2, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capCPUL3Learned.setStatus('current')
capCPUL3Aged = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 2, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capCPUL3Aged.setStatus('current')
capCPUL2Learned = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 2, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capCPUL2Learned.setStatus('current')
capCPUL2Aged = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 2, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capCPUL2Aged.setStatus('current')
capCPUNIAReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 2, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capCPUNIAReceived.setStatus('current')
capCPUNIATransmitted = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 2, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capCPUNIATransmitted.setStatus('current')
capCPUMinThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 2, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 99))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: capCPUMinThreshold.setStatus('current')
capCPUMaxThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 2, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 99))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: capCPUMaxThreshold.setStatus('current')
capTaskTable = MibTable((1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 3, 1), )
if mibBuilder.loadTexts: capTaskTable.setStatus('current')
capTaskEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 3, 1, 1), ).setIndexNames((0, "CTRON-SSR-CAPACITY-MIB", "capTaskModuleIndex"), (0, "CTRON-SSR-CAPACITY-MIB", "capTaskIndex"))
if mibBuilder.loadTexts: capTaskEntry.setStatus('current')
capTaskModuleIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: capTaskModuleIndex.setStatus('current')
capTaskIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: capTaskIndex.setStatus('current')
capTaskName = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 3, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: capTaskName.setStatus('current')
capTaskShed = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 3, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capTaskShed.setStatus('current')
capTaskStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 3, 1, 1, 5), SSRStatusType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capTaskStatus.setStatus('current')
capTaskUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 3, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: capTaskUsed.setStatus('current')
capMemoryTable = MibTable((1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 4, 1), )
if mibBuilder.loadTexts: capMemoryTable.setStatus('current')
capMemoryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 4, 1, 1), ).setIndexNames((0, "CTRON-SSR-CAPACITY-MIB", "capMemoryType"), (0, "CTRON-SSR-CAPACITY-MIB", "capMemoryIndex"))
if mibBuilder.loadTexts: capMemoryEntry.setStatus('current')
capMemoryType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 4, 1, 1, 1), SSRMemoryType())
if mibBuilder.loadTexts: capMemoryType.setStatus('current')
capMemoryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 4, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: capMemoryIndex.setStatus('current')
capMemoryDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 4, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("readonly")
if mibBuilder.loadTexts: capMemoryDescr.setStatus('current')
capMemorySize = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 4, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: capMemorySize.setStatus('current')
capMemoryFree = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 4, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: capMemoryFree.setStatus('current')
capMemoryUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 4, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: capMemoryUsed.setStatus('current')
capMemoryBlockSize = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 4, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: capMemoryBlockSize.setStatus('current')
capMemoryFailures = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 4, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capMemoryFailures.setStatus('current')
capMemoryRemovable = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 4, 1, 1, 9), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capMemoryRemovable.setStatus('current')
capConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 6))
capCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 6, 1))
capGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 6, 2))
capComplianceV10 = ModuleCompliance((1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 6, 2, 1, 1)).setObjects(("CTRON-SSR-CAPACITY-MIB", "capConfGroupV10"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    capComplianceV10 = capComplianceV10.setStatus('deprecated')
capComplianceV20 = ModuleCompliance((1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 6, 2, 2, 1)).setObjects(("CTRON-SSR-CAPACITY-MIB", "capConfGroupV20"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    capComplianceV20 = capComplianceV20.setStatus('current')
capConfGroupV10 = ObjectGroup((1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 6, 2, 1)).setObjects(("CTRON-SSR-CAPACITY-MIB", "capChassisSlotCount"), ("CTRON-SSR-CAPACITY-MIB", "capChassisSlotsUsed"), ("CTRON-SSR-CAPACITY-MIB", "capChassisSlotsFree"), ("CTRON-SSR-CAPACITY-MIB", "capChassisCPURedundancy"), ("CTRON-SSR-CAPACITY-MIB", "capChassisPSRedundancy"), ("CTRON-SSR-CAPACITY-MIB", "capChassisSFRedundancy"), ("CTRON-SSR-CAPACITY-MIB", "capCPUCurrentUtilization"), ("CTRON-SSR-CAPACITY-MIB", "capCPUL3Learned"), ("CTRON-SSR-CAPACITY-MIB", "capCPUL3Aged"), ("CTRON-SSR-CAPACITY-MIB", "capCPUL2Learned"), ("CTRON-SSR-CAPACITY-MIB", "capCPUL2Aged"), ("CTRON-SSR-CAPACITY-MIB", "capCPUNIAReceived"), ("CTRON-SSR-CAPACITY-MIB", "capCPUNIATransmitted"), ("CTRON-SSR-CAPACITY-MIB", "capTaskName"), ("CTRON-SSR-CAPACITY-MIB", "capTaskShed"), ("CTRON-SSR-CAPACITY-MIB", "capTaskStatus"), ("CTRON-SSR-CAPACITY-MIB", "capTaskUsed"), ("CTRON-SSR-CAPACITY-MIB", "capMemoryDescr"), ("CTRON-SSR-CAPACITY-MIB", "capMemorySize"), ("CTRON-SSR-CAPACITY-MIB", "capMemoryFree"), ("CTRON-SSR-CAPACITY-MIB", "capMemoryUsed"), ("CTRON-SSR-CAPACITY-MIB", "capMemoryBlockSize"), ("CTRON-SSR-CAPACITY-MIB", "capMemoryFailures"), ("CTRON-SSR-CAPACITY-MIB", "capMemoryRemovable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    capConfGroupV10 = capConfGroupV10.setStatus('deprecated')
capConfGroupV20 = ObjectGroup((1, 3, 6, 1, 4, 1, 52, 2501, 1, 270, 6, 2, 2)).setObjects(("CTRON-SSR-CAPACITY-MIB", "capChassisSlotCount"), ("CTRON-SSR-CAPACITY-MIB", "capChassisSlotsUsed"), ("CTRON-SSR-CAPACITY-MIB", "capChassisSlotsFree"), ("CTRON-SSR-CAPACITY-MIB", "capChassisCPURedundancy"), ("CTRON-SSR-CAPACITY-MIB", "capChassisPSRedundancy"), ("CTRON-SSR-CAPACITY-MIB", "capChassisSFRedundancy"), ("CTRON-SSR-CAPACITY-MIB", "capCPUCurrentUtilization"), ("CTRON-SSR-CAPACITY-MIB", "capCPUL3Learned"), ("CTRON-SSR-CAPACITY-MIB", "capCPUL3Aged"), ("CTRON-SSR-CAPACITY-MIB", "capCPUL2Learned"), ("CTRON-SSR-CAPACITY-MIB", "capCPUL2Aged"), ("CTRON-SSR-CAPACITY-MIB", "capCPUNIAReceived"), ("CTRON-SSR-CAPACITY-MIB", "capCPUNIATransmitted"), ("CTRON-SSR-CAPACITY-MIB", "capCPUMinThreshold"), ("CTRON-SSR-CAPACITY-MIB", "capCPUMaxThreshold"), ("CTRON-SSR-CAPACITY-MIB", "capTaskName"), ("CTRON-SSR-CAPACITY-MIB", "capTaskShed"), ("CTRON-SSR-CAPACITY-MIB", "capTaskStatus"), ("CTRON-SSR-CAPACITY-MIB", "capTaskUsed"), ("CTRON-SSR-CAPACITY-MIB", "capMemoryDescr"), ("CTRON-SSR-CAPACITY-MIB", "capMemorySize"), ("CTRON-SSR-CAPACITY-MIB", "capMemoryFree"), ("CTRON-SSR-CAPACITY-MIB", "capMemoryUsed"), ("CTRON-SSR-CAPACITY-MIB", "capMemoryBlockSize"), ("CTRON-SSR-CAPACITY-MIB", "capMemoryFailures"), ("CTRON-SSR-CAPACITY-MIB", "capMemoryRemovable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    capConfGroupV20 = capConfGroupV20.setStatus('current')
mibBuilder.exportSymbols("CTRON-SSR-CAPACITY-MIB", capMemoryFailures=capMemoryFailures, cpu=cpu, capCPUCurrentUtilization=capCPUCurrentUtilization, capCPUMaxThreshold=capCPUMaxThreshold, capCPUL2Aged=capCPUL2Aged, capComplianceV10=capComplianceV10, capMemoryIndex=capMemoryIndex, capCPUL3Learned=capCPUL3Learned, capChassisSlotCount=capChassisSlotCount, capTaskShed=capTaskShed, capMemoryUsed=capMemoryUsed, memory=memory, capTaskTable=capTaskTable, capMemoryDescr=capMemoryDescr, capacityMIB=capacityMIB, capCPUEntry=capCPUEntry, capTaskUsed=capTaskUsed, capTaskModuleIndex=capTaskModuleIndex, capChassisSlotsUsed=capChassisSlotsUsed, capChassisPSRedundancy=capChassisPSRedundancy, capChassisCPURedundancy=capChassisCPURedundancy, SSRStatusType=SSRStatusType, chassisCap=chassisCap, SSRCapabilityType=SSRCapabilityType, PYSNMP_MODULE_ID=capacityMIB, capCPUNIATransmitted=capCPUNIATransmitted, capGroups=capGroups, capTaskIndex=capTaskIndex, capMemoryType=capMemoryType, capCPUNIAReceived=capCPUNIAReceived, capChassisSlotsFree=capChassisSlotsFree, capCPUModuleIndex=capCPUModuleIndex, capComplianceV20=capComplianceV20, capMemorySize=capMemorySize, capMemoryBlockSize=capMemoryBlockSize, SSRMemoryType=SSRMemoryType, capCPUMinThreshold=capCPUMinThreshold, capConfGroupV10=capConfGroupV10, tasks=tasks, capCPUTable=capCPUTable, capMemoryEntry=capMemoryEntry, capChassisSFRedundancy=capChassisSFRedundancy, capTaskStatus=capTaskStatus, capTaskEntry=capTaskEntry, capMemoryFree=capMemoryFree, capCompliances=capCompliances, capCPUL3Aged=capCPUL3Aged, capTaskName=capTaskName, capConfGroupV20=capConfGroupV20, capConformance=capConformance, capCPUL2Learned=capCPUL2Learned, capMemoryRemovable=capMemoryRemovable, capMemoryTable=capMemoryTable)
