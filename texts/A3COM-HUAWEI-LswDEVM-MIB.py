#
# PySNMP MIB module A3COM-HUAWEI-LswDEVM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/3com/A3COM-HUAWEI-LswDEVM-MIB
# Produced by pysmi-1.1.8 at Mon Feb  7 16:06:47 2022
# On host fv-az42-619 platform Linux version 5.11.0-1028-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
hwLswFrameIndex, hwLswSlotIndex = mibBuilder.importSymbols("A3COM-HUAWEI-DEVICE-MIB", "hwLswFrameIndex", "hwLswSlotIndex")
lswCommon, huaweiUtility = mibBuilder.importSymbols("A3COM-HUAWEI-OID-MIB", "lswCommon", "huaweiUtility")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Unsigned32, ObjectIdentity, NotificationType, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Counter64, IpAddress, ModuleIdentity, Gauge32, Integer32, iso, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Unsigned32", "ObjectIdentity", "NotificationType", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Counter64", "IpAddress", "ModuleIdentity", "Gauge32", "Integer32", "iso", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hwLswdevMMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 9))
hwLswdevMMib.setRevisions(('2001-06-29 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hwLswdevMMib.setRevisionsDescriptions(('',))
if mibBuilder.loadTexts: hwLswdevMMib.setLastUpdated('201111260000Z')
if mibBuilder.loadTexts: hwLswdevMMib.setOrganization('')
if mibBuilder.loadTexts: hwLswdevMMib.setContactInfo('')
if mibBuilder.loadTexts: hwLswdevMMib.setDescription('')
hwDevice = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 1))
hwCpuTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 1, 1), )
if mibBuilder.loadTexts: hwCpuTable.setStatus('current')
if mibBuilder.loadTexts: hwCpuTable.setDescription('A table of CPU statistics.')
hwCpuEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 1, 1, 1), ).setIndexNames((0, "A3COM-HUAWEI-LswDEVM-MIB", "hwCpuIndex"))
if mibBuilder.loadTexts: hwCpuEntry.setStatus('current')
if mibBuilder.loadTexts: hwCpuEntry.setDescription('The Entries of hwCpuTable.')
hwCpuIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 1, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: hwCpuIndex.setStatus('current')
if mibBuilder.loadTexts: hwCpuIndex.setDescription('Index of hwCpuTable. This integer is a  uniq number to\n             identify the CPU(s). We recommand two Number Plans in this\n             paper, Logical Number or Phisical Number. For the first\n             case, hwCpuIndex is a integer, range from 1 to the Maximum\n             number, for example 1,2,3,4,5 ..., where 1 represents\n             the first CPU, 2 represents the second CPU, etc.  For the\n             second case hwCpuIndex represents physical card position\n             (Shelf Number, Frame Number, Slot Number, SubSlotNumber)\n             where the CPU residing, for example, 0x01020304 represent\n             the CPU on the 4th subslot of the 3th slot of the 2nd frame\n             of the 1st Shelf. In the condition of multiple CPU system\n             where CPU group coordinately  process on one board, we see\n             the CPUs as one CPU')
hwCpuCostRate = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 1, 1, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwCpuCostRate.setStatus('current')
if mibBuilder.loadTexts: hwCpuCostRate.setDescription('The overall CPU busy percentage in the last 5 second period. ')
hwCpuCostRatePer1Min = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 1, 1, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwCpuCostRatePer1Min.setStatus('current')
if mibBuilder.loadTexts: hwCpuCostRatePer1Min.setDescription('The overall CPU cost percentage in the last 1 minute period. ')
hwCpuCostRatePer5Min = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 1, 1, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwCpuCostRatePer5Min.setStatus('current')
if mibBuilder.loadTexts: hwCpuCostRatePer5Min.setDescription('The overall CPU cost percentage in the last 5 minutes period. ')
hwMem = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 1, 2))
hwMemTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 1, 2, 1), )
if mibBuilder.loadTexts: hwMemTable.setStatus('current')
if mibBuilder.loadTexts: hwMemTable.setDescription('This table contains memory information.  ')
hwMemEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 1, 2, 1, 1), ).setIndexNames((0, "A3COM-HUAWEI-LswDEVM-MIB", "hwMemModuleIndex"))
if mibBuilder.loadTexts: hwMemEntry.setStatus('current')
if mibBuilder.loadTexts: hwMemEntry.setDescription('The Entries of hwMemTable')
hwMemModuleIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 1, 2, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: hwMemModuleIndex.setStatus('current')
if mibBuilder.loadTexts: hwMemModuleIndex.setDescription('Index of hwMemTable. This integer is a  uniq number to\n             identify the memory module. We recommand two Number Plans\n             in this paper, Logical Number or Phisical Number. For the\n             first case, hwMemModuleIndex is a integer, range from 1 to\n             the Maximum number, for example 1,2,3,4,5 ..., where 1\n             represents the first memory module, 2 represents the second\n             memory module, etc.  For the second case hwMemModuleIndex\n             represents physical card position (Shelf Number, Frame Number,\n             Slot Number, SubSlotNumber) where the memory module residing,\n             for example, 0x01020304 represent the memory module on the 4th\n             subslot of the 3th slot of the 2nd frame of the 1st Shelf. ')
hwMemSize = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 1, 2, 1, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwMemSize.setStatus('current')
if mibBuilder.loadTexts: hwMemSize.setDescription('Indicates the total size of the memory module\n            which is on the managed object.')
hwMemFree = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 1, 2, 1, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwMemFree.setStatus('current')
if mibBuilder.loadTexts: hwMemFree.setDescription('Indicates the free size of the memory')
hwMemRawSliceUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 1, 2, 1, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwMemRawSliceUsed.setStatus('current')
if mibBuilder.loadTexts: hwMemRawSliceUsed.setDescription('Indicates the used size of the raw slice memory')
hwMemLgFree = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 1, 2, 1, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwMemLgFree.setStatus('current')
if mibBuilder.loadTexts: hwMemLgFree.setDescription('The largest free size of the contiguous area in the memory.\n           The unit is byte.')
hwMemFail = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 1, 2, 1, 1, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwMemFail.setStatus('current')
if mibBuilder.loadTexts: hwMemFail.setDescription('The times of memory allocation failures')
hwMemFailNoMem = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 1, 2, 1, 1, 7), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwMemFailNoMem.setStatus('current')
if mibBuilder.loadTexts: hwMemFailNoMem.setDescription('The times of memory allocation failures due to no free memory.')
hwBufTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 1, 2, 2), )
if mibBuilder.loadTexts: hwBufTable.setStatus('current')
if mibBuilder.loadTexts: hwBufTable.setDescription('This table contains buffer information.  ')
hwBufEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 1, 2, 2, 1), ).setIndexNames((0, "A3COM-HUAWEI-LswDEVM-MIB", "hwBufModuleIndex"), (0, "A3COM-HUAWEI-LswDEVM-MIB", "hwBufSize"))
if mibBuilder.loadTexts: hwBufEntry.setStatus('current')
if mibBuilder.loadTexts: hwBufEntry.setDescription('The Entries of hwBufferTable')
hwBufModuleIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 1, 2, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: hwBufModuleIndex.setStatus('current')
if mibBuilder.loadTexts: hwBufModuleIndex.setDescription('Index of hwBufferTable. This integer is a  uniq number to\n             identify the buffer module. We recommand two Number Plans\n             in this paper, Logical Number or Phisical Number. For the\n             first case, hwBufferModuleIndex is a integer, range from 1 to\n             the Maximum number, for example 1,2,3,4,5 ..., where 1\n             represents the first buffer module, 2 represents the second\n             buffer module, etc.  For the second case hwBufferModuleIndex\n             represents physical card position (Shelf Number, Frame Number,\n             Slot Number, SubSlotNumber) where the buffer module residing,\n             for example, 0x01020304 represent the buffer module on the 4th\n             subslot of the 3th slot of the 2nd frame of the 1st Shelf. ')
hwBufSize = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 1, 2, 2, 1, 2), Integer32())
if mibBuilder.loadTexts: hwBufSize.setStatus('current')
if mibBuilder.loadTexts: hwBufSize.setDescription('The size of buffer,unit is byte.')
hwBufCurrentTotal = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 1, 2, 2, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwBufCurrentTotal.setStatus('current')
if mibBuilder.loadTexts: hwBufCurrentTotal.setDescription('The total number of buffer currently.')
hwBufCurrentUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 1, 2, 2, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwBufCurrentUsed.setStatus('current')
if mibBuilder.loadTexts: hwBufCurrentUsed.setDescription('The number of used buffer currently.')
hwFlh = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 1, 3))
hwFlhTotalSize = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 1, 3, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwFlhTotalSize.setStatus('current')
if mibBuilder.loadTexts: hwFlhTotalSize.setDescription("The flash memory's total size, in kilobyte")
hwFlhTotalFree = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 1, 3, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwFlhTotalFree.setStatus('current')
if mibBuilder.loadTexts: hwFlhTotalFree.setDescription('The free space in internal flash memory, in kilobyte')
hwFlhLastDelTime = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 1, 3, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwFlhLastDelTime.setStatus('current')
if mibBuilder.loadTexts: hwFlhLastDelTime.setDescription('The time since system up of the lastest deleting operation of\n            flash memory.The value of Zero indicates there is no erasing operation\n            since system up')
hwFlhDelState = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 1, 3, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("executing", 1), ("ok", 2), ("error", 3), ("readOnly", 4), ("failtoopen", 5), ("blockMallocFail", 6), ("noneDelOperationSinceStart", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwFlhDelState.setStatus('current')
if mibBuilder.loadTexts: hwFlhDelState.setDescription('The state indicates the result of current or\n            lastest flash memory deleting operation')
hwFlhState = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 6, 1, 3, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("busy", 1), ("free", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwFlhState.setStatus('current')
if mibBuilder.loadTexts: hwFlhState.setDescription('Busy indicates the flash memory is unavailable due to others may be using it,\n            and free indicates the flash memory is available now')
hwLswdevMMibObject = ObjectIdentity((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 9, 1))
if mibBuilder.loadTexts: hwLswdevMMibObject.setStatus('current')
if mibBuilder.loadTexts: hwLswdevMMibObject.setDescription('Description.')
hwdevMFanStatusTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 9, 1, 1), )
if mibBuilder.loadTexts: hwdevMFanStatusTable.setStatus('current')
if mibBuilder.loadTexts: hwdevMFanStatusTable.setDescription(' Fan status description table ')
hwdevMFanStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 9, 1, 1, 1), ).setIndexNames((0, "A3COM-HUAWEI-LswDEVM-MIB", "hwDevMFanNum"))
if mibBuilder.loadTexts: hwdevMFanStatusEntry.setStatus('current')
if mibBuilder.loadTexts: hwdevMFanStatusEntry.setDescription(' Fan status description table entry ')
hwDevMFanNum = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 9, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwDevMFanNum.setStatus('current')
if mibBuilder.loadTexts: hwDevMFanNum.setDescription(' Fan number ')
hwDevMFanStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 9, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("active", 1), ("deactive", 2), ("not-install", 3), ("unsupport", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwDevMFanStatus.setStatus('current')
if mibBuilder.loadTexts: hwDevMFanStatus.setDescription(' Fan status: active (1), deactive (2) not installed (3) and unsupported (4)')
hwdevMPowerStatusTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 9, 1, 2), )
if mibBuilder.loadTexts: hwdevMPowerStatusTable.setStatus('current')
if mibBuilder.loadTexts: hwdevMPowerStatusTable.setDescription(' Power status description table  ')
hwdevMPowerStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 9, 1, 2, 1), ).setIndexNames((0, "A3COM-HUAWEI-LswDEVM-MIB", "hwDevMPowerNum"))
if mibBuilder.loadTexts: hwdevMPowerStatusEntry.setStatus('current')
if mibBuilder.loadTexts: hwdevMPowerStatusEntry.setDescription(' Power status description table entry   ')
hwDevMPowerNum = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 9, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwDevMPowerNum.setStatus('current')
if mibBuilder.loadTexts: hwDevMPowerNum.setDescription('Power number ')
hwDevMPowerStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 9, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("active", 1), ("deactive", 2), ("not-install", 3), ("unsupport", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwDevMPowerStatus.setStatus('current')
if mibBuilder.loadTexts: hwDevMPowerStatus.setDescription(' Power status: active (1), deactive (2) not installed (3) and unsupported    ')
hwdevMSlotEnvironmentTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 9, 1, 3), )
if mibBuilder.loadTexts: hwdevMSlotEnvironmentTable.setStatus('current')
if mibBuilder.loadTexts: hwdevMSlotEnvironmentTable.setDescription(' environment description table  ')
hwdevMSlotEnvironmentEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 9, 1, 3, 1), ).setIndexNames((0, "A3COM-HUAWEI-DEVICE-MIB", "hwLswFrameIndex"), (0, "A3COM-HUAWEI-DEVICE-MIB", "hwLswSlotIndex"), (0, "A3COM-HUAWEI-LswDEVM-MIB", "hwdevMSlotEnvironmentType"))
if mibBuilder.loadTexts: hwdevMSlotEnvironmentEntry.setStatus('current')
if mibBuilder.loadTexts: hwdevMSlotEnvironmentEntry.setDescription(' environment description table entry   ')
hwdevMSlotEnvironmentType = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 9, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("temperature", 1), ("humidity", 2), ("fog", 3))))
if mibBuilder.loadTexts: hwdevMSlotEnvironmentType.setStatus('current')
if mibBuilder.loadTexts: hwdevMSlotEnvironmentType.setDescription('Environment type ')
hwDevMSlotEnvironmentStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 9, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("normal", 1), ("upper", 2), ("lower", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwDevMSlotEnvironmentStatus.setStatus('current')
if mibBuilder.loadTexts: hwDevMSlotEnvironmentStatus.setDescription(' Environment status')
hwDevMSlotEnvironmentValue = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 9, 1, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwDevMSlotEnvironmentValue.setStatus('current')
if mibBuilder.loadTexts: hwDevMSlotEnvironmentValue.setDescription(' Environment value')
hwDevMSlotEnvironmentUpperLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 9, 1, 3, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwDevMSlotEnvironmentUpperLimit.setStatus('current')
if mibBuilder.loadTexts: hwDevMSlotEnvironmentUpperLimit.setDescription('Environment upper limit ')
hwDevMSlotEnvironmentLowerLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 9, 1, 3, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwDevMSlotEnvironmentLowerLimit.setStatus('current')
if mibBuilder.loadTexts: hwDevMSlotEnvironmentLowerLimit.setDescription(' Environment Lower limit')
hwLinkUpDownTrapEnable = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 9, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("enableBoth", 1), ("disableBoth", 2), ("enableLinkUpTrapOnly", 3), ("enableLinkDownTrapOnly", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwLinkUpDownTrapEnable.setStatus('current')
if mibBuilder.loadTexts: hwLinkUpDownTrapEnable.setDescription('Enable/Disable linkUp/linkDown traps of the device, determining whether\n         to enable linkUp/linkDown traps with that of the interface.\n         When the value is enableBoth(1), the linkUp/linkDown traps are both\n         enabled.\n         When the value is disableBoth(2), the linkUp/linkDown traps are both\n         disabled.\n         When the value is enableLinkUpTrapOnly(3), the linkUp traps is enabled\n         and the linkDown traps is disabled.\n         When the value is enableLinkDownTrapOnly(4), the linkUp traps is\n         disabled and the linkDown traps is enabled. ')
hwdot1qTpFdbLearnStatus = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 9, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwdot1qTpFdbLearnStatus.setStatus('current')
if mibBuilder.loadTexts: hwdot1qTpFdbLearnStatus.setDescription(' Enable/Disable the address learning.')
hwCfmWriteFlash = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 9, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("write", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwCfmWriteFlash.setStatus('current')
if mibBuilder.loadTexts: hwCfmWriteFlash.setDescription(' Write the current effective configuration into the Flash memory.\n                      This object does not support read operation.')
hwCfmEraseFlash = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 9, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("erase", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwCfmEraseFlash.setStatus('current')
if mibBuilder.loadTexts: hwCfmEraseFlash.setDescription(' Delete the configuration from the Flash memory.\n                      This object does not support read operation.')
hwDevMFirstTrapTime = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 9, 1, 13), TimeTicks()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hwDevMFirstTrapTime.setStatus('current')
if mibBuilder.loadTexts: hwDevMFirstTrapTime.setDescription('Represents the first trap time.')
mibBuilder.exportSymbols("A3COM-HUAWEI-LswDEVM-MIB", hwCpuCostRate=hwCpuCostRate, hwMemTable=hwMemTable, hwFlhTotalSize=hwFlhTotalSize, hwDevMSlotEnvironmentStatus=hwDevMSlotEnvironmentStatus, hwCpuTable=hwCpuTable, hwDevMFirstTrapTime=hwDevMFirstTrapTime, hwDevMPowerNum=hwDevMPowerNum, hwCfmWriteFlash=hwCfmWriteFlash, hwLswdevMMib=hwLswdevMMib, hwCpuCostRatePer1Min=hwCpuCostRatePer1Min, hwDevMFanStatus=hwDevMFanStatus, hwBufCurrentUsed=hwBufCurrentUsed, hwdevMSlotEnvironmentTable=hwdevMSlotEnvironmentTable, hwFlhTotalFree=hwFlhTotalFree, hwDevMSlotEnvironmentValue=hwDevMSlotEnvironmentValue, hwFlhLastDelTime=hwFlhLastDelTime, hwBufModuleIndex=hwBufModuleIndex, hwMemModuleIndex=hwMemModuleIndex, hwMemFree=hwMemFree, hwDevMFanNum=hwDevMFanNum, hwBufEntry=hwBufEntry, hwDevMPowerStatus=hwDevMPowerStatus, hwMemSize=hwMemSize, hwMemLgFree=hwMemLgFree, hwMem=hwMem, hwdot1qTpFdbLearnStatus=hwdot1qTpFdbLearnStatus, hwBufSize=hwBufSize, hwBufTable=hwBufTable, hwBufCurrentTotal=hwBufCurrentTotal, hwFlhDelState=hwFlhDelState, hwLinkUpDownTrapEnable=hwLinkUpDownTrapEnable, hwFlh=hwFlh, hwFlhState=hwFlhState, hwMemFailNoMem=hwMemFailNoMem, hwdevMFanStatusTable=hwdevMFanStatusTable, PYSNMP_MODULE_ID=hwLswdevMMib, hwCpuIndex=hwCpuIndex, hwDevMSlotEnvironmentLowerLimit=hwDevMSlotEnvironmentLowerLimit, hwDevMSlotEnvironmentUpperLimit=hwDevMSlotEnvironmentUpperLimit, hwCpuEntry=hwCpuEntry, hwdevMPowerStatusEntry=hwdevMPowerStatusEntry, hwCpuCostRatePer5Min=hwCpuCostRatePer5Min, hwCfmEraseFlash=hwCfmEraseFlash, hwMemEntry=hwMemEntry, hwdevMSlotEnvironmentType=hwdevMSlotEnvironmentType, hwDevice=hwDevice, hwdevMSlotEnvironmentEntry=hwdevMSlotEnvironmentEntry, hwLswdevMMibObject=hwLswdevMMibObject, hwdevMFanStatusEntry=hwdevMFanStatusEntry, hwMemFail=hwMemFail, hwdevMPowerStatusTable=hwdevMPowerStatusTable, hwMemRawSliceUsed=hwMemRawSliceUsed)
