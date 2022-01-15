#
# PySNMP MIB module ONEACCESS-SYS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/oneaccess/ONEACCESS-SYS-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 18:15:12 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
oacMIBModules, oacExpIMSystem = mibBuilder.importSymbols("ONEACCESS-GLOBAL-REG", "oacMIBModules", "oacExpIMSystem")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, iso, IpAddress, Gauge32, ModuleIdentity, MibIdentifier, NotificationType, Unsigned32, Bits, Counter32, ObjectIdentity, TimeTicks, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "iso", "IpAddress", "Gauge32", "ModuleIdentity", "MibIdentifier", "NotificationType", "Unsigned32", "Bits", "Counter32", "ObjectIdentity", "TimeTicks", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
oacSysMIBModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 13191, 1, 100, 671))
oacSysMIBModule.setRevisions(('2014-05-05 00:01', '2011-06-15 00:00', '2010-12-14 00:01', '2010-08-11 10:00', '2010-07-08 10:00',))
if mibBuilder.loadTexts: oacSysMIBModule.setLastUpdated('201405050001Z')
if mibBuilder.loadTexts: oacSysMIBModule.setOrganization(' OneAccess ')
class OASysHwcClass(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("board", 0), ("cpu", 1), ("slot", 2))

class OASysHwcType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("mainboard", 0), ("microprocessor", 1), ("ram", 2), ("flash", 3), ("dsp", 4), ("uplink", 5), ("module", 6))

class OASysCoreType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("controlplane", 0), ("dataforwarding", 1), ("application", 2), ("mixed", 3))

oacExpIMSysStatistics = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 1))
oacExpIMSysHardwareDescription = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 2))
oacSysMemStatistics = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 1, 1))
oacSysCpuStatistics = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 1, 2))
oacSysSecureCrashlogCount = MibScalar((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 1, 100), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacSysSecureCrashlogCount.setStatus('current')
oacSysStartCaused = MibScalar((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 1, 200), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacSysStartCaused.setStatus('current')
oacSysIMSysMainBoard = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 2, 1))
oacExpIMSysHwComponents = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 2, 2))
oacExpIMSysFactory = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 2, 3))
oacSysIMSysMainIdentifier = MibScalar((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 2, 1, 1), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacSysIMSysMainIdentifier.setStatus('current')
oacSysIMSysMainManufacturedIdentity = MibScalar((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacSysIMSysMainManufacturedIdentity.setStatus('current')
oacSysIMSysMainManufacturedDate = MibScalar((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacSysIMSysMainManufacturedDate.setStatus('current')
oacSysIMSysMainCPU = MibScalar((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 2, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacSysIMSysMainCPU.setStatus('current')
oacSysIMSysMainBSPVersion = MibScalar((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 2, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacSysIMSysMainBSPVersion.setStatus('current')
oacSysIMSysMainBootVersion = MibScalar((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 2, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacSysIMSysMainBootVersion.setStatus('current')
oacSysIMSysMainBootDateCreation = MibScalar((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 2, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacSysIMSysMainBootDateCreation.setStatus('current')
oacSysMemoryFree = MibScalar((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacSysMemoryFree.setStatus('current')
oacSysMemoryAllocated = MibScalar((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacSysMemoryAllocated.setStatus('current')
oacSysMemoryTotal = MibScalar((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacSysMemoryTotal.setStatus('current')
oacSysMemoryUsed = MibScalar((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacSysMemoryUsed.setStatus('current')
oacSysCpuUsed = MibScalar((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 1, 2, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacSysCpuUsed.setStatus('current')
oacSysCpuUsedCoresCount = MibScalar((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 1, 2, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacSysCpuUsedCoresCount.setStatus('current')
oacSysCpuUsedCoresTable = MibTable((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 1, 2, 3), )
if mibBuilder.loadTexts: oacSysCpuUsedCoresTable.setStatus('current')
oacSysCpuUsedCoresEntry = MibTableRow((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 1, 2, 3, 1), ).setIndexNames((0, "ONEACCESS-SYS-MIB", "oacSysCpuUsedIndex"))
if mibBuilder.loadTexts: oacSysCpuUsedCoresEntry.setStatus('current')
oacSysCpuUsedIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 1, 2, 3, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacSysCpuUsedIndex.setStatus('current')
oacSysCpuUsedCoreType = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 1, 2, 3, 1, 2), OASysCoreType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacSysCpuUsedCoreType.setStatus('current')
oacSysCpuUsedValue = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 1, 2, 3, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacSysCpuUsedValue.setStatus('current')
oacSysCpuUsedOneMinuteValue = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 1, 2, 3, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacSysCpuUsedOneMinuteValue.setStatus('current')
oacSysLastRebootCause = MibScalar((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacSysLastRebootCause.setStatus('current')
oacExpIMSysHwComponentsCount = MibScalar((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 2, 2, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacExpIMSysHwComponentsCount.setStatus('current')
oacExpIMSysHwComponentsTable = MibTable((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 2, 2, 2), )
if mibBuilder.loadTexts: oacExpIMSysHwComponentsTable.setStatus('current')
oacExpIMSysHwComponentsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 2, 2, 2, 1), ).setIndexNames((0, "ONEACCESS-SYS-MIB", "oacExpIMSysHwcIndex"))
if mibBuilder.loadTexts: oacExpIMSysHwComponentsEntry.setStatus('current')
oacExpIMSysHwcIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 2, 2, 2, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacExpIMSysHwcIndex.setStatus('current')
oacExpIMSysHwcClass = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 2, 2, 2, 1, 2), OASysHwcClass()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacExpIMSysHwcClass.setStatus('current')
oacExpIMSysHwcType = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 2, 2, 2, 1, 3), OASysHwcType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacExpIMSysHwcType.setStatus('current')
oacExpIMSysHwcDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 2, 2, 2, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacExpIMSysHwcDescription.setStatus('current')
oacExpIMSysHwcSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 2, 2, 2, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacExpIMSysHwcSerialNumber.setStatus('current')
oacExpIMSysHwcManufacturer = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 2, 2, 2, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacExpIMSysHwcManufacturer.setStatus('current')
oacExpIMSysHwcManufacturedDate = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 2, 2, 2, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 10))).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacExpIMSysHwcManufacturedDate.setStatus('current')
oacExpIMSysHwcProductName = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 2, 2, 2, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacExpIMSysHwcProductName.setStatus('current')
oacExpIMSysFactorySupplierID = MibScalar((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 2, 3, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 14))).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacExpIMSysFactorySupplierID.setStatus('current')
oacExpIMSysFactoryProductSalesCode = MibScalar((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 2, 3, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 22))).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacExpIMSysFactoryProductSalesCode.setStatus('current')
oacExpIMSysFactoryHwRevision = MibScalar((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 2, 3, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(2, 7))).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacExpIMSysFactoryHwRevision.setStatus('current')
mibBuilder.exportSymbols("ONEACCESS-SYS-MIB", oacSysIMSysMainBootVersion=oacSysIMSysMainBootVersion, oacExpIMSysHwcIndex=oacExpIMSysHwcIndex, oacExpIMSysFactory=oacExpIMSysFactory, oacSysMemStatistics=oacSysMemStatistics, oacSysCpuUsedValue=oacSysCpuUsedValue, oacExpIMSysHardwareDescription=oacExpIMSysHardwareDescription, oacSysCpuUsedCoreType=oacSysCpuUsedCoreType, oacExpIMSysHwComponentsTable=oacExpIMSysHwComponentsTable, oacSysCpuStatistics=oacSysCpuStatistics, oacSysIMSysMainManufacturedDate=oacSysIMSysMainManufacturedDate, oacExpIMSysHwComponentsCount=oacExpIMSysHwComponentsCount, OASysHwcType=OASysHwcType, oacExpIMSysHwComponentsEntry=oacExpIMSysHwComponentsEntry, oacExpIMSysHwcManufacturedDate=oacExpIMSysHwcManufacturedDate, oacSysCpuUsedCoresEntry=oacSysCpuUsedCoresEntry, oacExpIMSysHwcProductName=oacExpIMSysHwcProductName, oacSysIMSysMainBoard=oacSysIMSysMainBoard, oacSysCpuUsedIndex=oacSysCpuUsedIndex, oacSysIMSysMainBootDateCreation=oacSysIMSysMainBootDateCreation, oacSysMemoryUsed=oacSysMemoryUsed, oacSysCpuUsedOneMinuteValue=oacSysCpuUsedOneMinuteValue, oacExpIMSysHwComponents=oacExpIMSysHwComponents, oacExpIMSysStatistics=oacExpIMSysStatistics, oacExpIMSysFactoryProductSalesCode=oacExpIMSysFactoryProductSalesCode, oacExpIMSysHwcManufacturer=oacExpIMSysHwcManufacturer, oacSysIMSysMainIdentifier=oacSysIMSysMainIdentifier, oacSysIMSysMainCPU=oacSysIMSysMainCPU, oacExpIMSysFactorySupplierID=oacExpIMSysFactorySupplierID, oacSysMemoryTotal=oacSysMemoryTotal, PYSNMP_MODULE_ID=oacSysMIBModule, oacSysCpuUsed=oacSysCpuUsed, oacSysMIBModule=oacSysMIBModule, oacSysLastRebootCause=oacSysLastRebootCause, oacSysCpuUsedCoresTable=oacSysCpuUsedCoresTable, oacSysIMSysMainManufacturedIdentity=oacSysIMSysMainManufacturedIdentity, oacSysMemoryAllocated=oacSysMemoryAllocated, OASysHwcClass=OASysHwcClass, oacExpIMSysHwcClass=oacExpIMSysHwcClass, oacSysStartCaused=oacSysStartCaused, oacSysCpuUsedCoresCount=oacSysCpuUsedCoresCount, oacExpIMSysHwcSerialNumber=oacExpIMSysHwcSerialNumber, oacSysSecureCrashlogCount=oacSysSecureCrashlogCount, oacSysMemoryFree=oacSysMemoryFree, oacExpIMSysHwcType=oacExpIMSysHwcType, oacExpIMSysHwcDescription=oacExpIMSysHwcDescription, oacSysIMSysMainBSPVersion=oacSysIMSysMainBSPVersion, oacExpIMSysFactoryHwRevision=oacExpIMSysFactoryHwRevision, OASysCoreType=OASysCoreType)
