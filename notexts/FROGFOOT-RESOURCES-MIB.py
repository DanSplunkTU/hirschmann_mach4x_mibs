#
# PySNMP MIB module FROGFOOT-RESOURCES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/FROGFOOT-RESOURCES-MIB
# Produced by pysmi-1.1.3 at Sun Nov 28 20:09:00 2021
# On host fv-az77-612 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, ObjectIdentity, iso, Counter64, Gauge32, MibIdentifier, enterprises, Counter32, Bits, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, NotificationType, Unsigned32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "ObjectIdentity", "iso", "Counter64", "Gauge32", "MibIdentifier", "enterprises", "Counter32", "Bits", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "NotificationType", "Unsigned32", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
resources = ModuleIdentity((1, 3, 6, 1, 4, 1, 10002, 1, 1, 1))
if mibBuilder.loadTexts: resources.setLastUpdated('200407170000Z')
if mibBuilder.loadTexts: resources.setOrganization('Frogfoot Networks')
frogfoot = MibIdentifier((1, 3, 6, 1, 4, 1, 10002))
servers = MibIdentifier((1, 3, 6, 1, 4, 1, 10002, 1))
system = MibIdentifier((1, 3, 6, 1, 4, 1, 10002, 1, 1))
memory = MibIdentifier((1, 3, 6, 1, 4, 1, 10002, 1, 1, 1, 1))
swap = MibIdentifier((1, 3, 6, 1, 4, 1, 10002, 1, 1, 1, 2))
storage = MibIdentifier((1, 3, 6, 1, 4, 1, 10002, 1, 1, 1, 3))
load = MibIdentifier((1, 3, 6, 1, 4, 1, 10002, 1, 1, 1, 4))
resMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 10002, 1, 1, 1, 31))
resMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 10002, 1, 1, 1, 31, 1))
resConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 10002, 1, 1, 1, 31, 2))
resGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 10002, 1, 1, 1, 31, 2, 1))
resCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 10002, 1, 1, 1, 31, 2, 2))
class TableIndex(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

memTotal = MibScalar((1, 3, 6, 1, 4, 1, 10002, 1, 1, 1, 1, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: memTotal.setStatus('current')
memFree = MibScalar((1, 3, 6, 1, 4, 1, 10002, 1, 1, 1, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: memFree.setStatus('current')
memBuffer = MibScalar((1, 3, 6, 1, 4, 1, 10002, 1, 1, 1, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: memBuffer.setStatus('current')
memCache = MibScalar((1, 3, 6, 1, 4, 1, 10002, 1, 1, 1, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: memCache.setStatus('current')
swapTotal = MibScalar((1, 3, 6, 1, 4, 1, 10002, 1, 1, 1, 2, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swapTotal.setStatus('current')
swapFree = MibScalar((1, 3, 6, 1, 4, 1, 10002, 1, 1, 1, 2, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swapFree.setStatus('current')
diskNumber = MibScalar((1, 3, 6, 1, 4, 1, 10002, 1, 1, 1, 3, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskNumber.setStatus('current')
diskTable = MibTable((1, 3, 6, 1, 4, 1, 10002, 1, 1, 1, 3, 2), )
if mibBuilder.loadTexts: diskTable.setStatus('current')
diskEntry = MibTableRow((1, 3, 6, 1, 4, 1, 10002, 1, 1, 1, 3, 2, 1), ).setIndexNames((0, "FROGFOOT-RESOURCES-MIB", "diskIndex"))
if mibBuilder.loadTexts: diskEntry.setStatus('current')
diskIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 10002, 1, 1, 1, 3, 2, 1, 1), TableIndex())
if mibBuilder.loadTexts: diskIndex.setStatus('current')
diskDev = MibTableColumn((1, 3, 6, 1, 4, 1, 10002, 1, 1, 1, 3, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskDev.setStatus('current')
diskDir = MibTableColumn((1, 3, 6, 1, 4, 1, 10002, 1, 1, 1, 3, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskDir.setStatus('current')
diskFSType = MibTableColumn((1, 3, 6, 1, 4, 1, 10002, 1, 1, 1, 3, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24))).clone(namedValues=NamedValues(("unknown", 0), ("adfs", 1), ("affs", 2), ("coda", 3), ("cramfs", 4), ("ext2", 5), ("hpfs", 6), ("iso9660", 7), ("jffs2", 8), ("jfs", 9), ("minix", 10), ("msdos", 11), ("ncpfs", 12), ("nfs", 13), ("ntfs", 14), ("qnx4", 15), ("reiserfs", 16), ("romfs", 17), ("smbfs", 18), ("sysv", 19), ("tmpfs", 20), ("udf", 21), ("ufs", 22), ("vxfs", 23), ("xfs", 24)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskFSType.setStatus('current')
diskTotal = MibTableColumn((1, 3, 6, 1, 4, 1, 10002, 1, 1, 1, 3, 2, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskTotal.setStatus('current')
diskFree = MibTableColumn((1, 3, 6, 1, 4, 1, 10002, 1, 1, 1, 3, 2, 1, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskFree.setStatus('current')
loadNumber = MibScalar((1, 3, 6, 1, 4, 1, 10002, 1, 1, 1, 4, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: loadNumber.setStatus('current')
loadTable = MibTable((1, 3, 6, 1, 4, 1, 10002, 1, 1, 1, 4, 2), )
if mibBuilder.loadTexts: loadTable.setStatus('current')
loadEntry = MibTableRow((1, 3, 6, 1, 4, 1, 10002, 1, 1, 1, 4, 2, 1), ).setIndexNames((0, "FROGFOOT-RESOURCES-MIB", "loadIndex"))
if mibBuilder.loadTexts: loadEntry.setStatus('current')
loadIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 10002, 1, 1, 1, 4, 2, 1, 1), TableIndex())
if mibBuilder.loadTexts: loadIndex.setStatus('current')
loadDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 10002, 1, 1, 1, 4, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: loadDescr.setStatus('current')
loadValue = MibTableColumn((1, 3, 6, 1, 4, 1, 10002, 1, 1, 1, 4, 2, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: loadValue.setStatus('current')
resCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 10002, 1, 1, 1, 31, 2, 2, 1)).setObjects(("FROGFOOT-RESOURCES-MIB", "resMemGroup"), ("FROGFOOT-RESOURCES-MIB", "resSwapGroup"), ("FROGFOOT-RESOURCES-MIB", "resDiskGroup"), ("FROGFOOT-RESOURCES-MIB", "resLoadGroup"), ("FROGFOOT-RESOURCES-MIB", "resMemGroup"), ("FROGFOOT-RESOURCES-MIB", "resSwapGroup"), ("FROGFOOT-RESOURCES-MIB", "resDiskGroup"), ("FROGFOOT-RESOURCES-MIB", "resLoadGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    resCompliance = resCompliance.setStatus('current')
resMemGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 10002, 1, 1, 1, 31, 2, 1, 1)).setObjects(("FROGFOOT-RESOURCES-MIB", "memTotal"), ("FROGFOOT-RESOURCES-MIB", "memFree"), ("FROGFOOT-RESOURCES-MIB", "memBuffer"), ("FROGFOOT-RESOURCES-MIB", "memCache"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    resMemGroup = resMemGroup.setStatus('current')
resSwapGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 10002, 1, 1, 1, 31, 2, 1, 2)).setObjects(("FROGFOOT-RESOURCES-MIB", "swapTotal"), ("FROGFOOT-RESOURCES-MIB", "swapFree"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    resSwapGroup = resSwapGroup.setStatus('current')
resDiskGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 10002, 1, 1, 1, 31, 2, 1, 3)).setObjects(("FROGFOOT-RESOURCES-MIB", "diskNumber"), ("FROGFOOT-RESOURCES-MIB", "diskDev"), ("FROGFOOT-RESOURCES-MIB", "diskDir"), ("FROGFOOT-RESOURCES-MIB", "diskFSType"), ("FROGFOOT-RESOURCES-MIB", "diskTotal"), ("FROGFOOT-RESOURCES-MIB", "diskFree"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    resDiskGroup = resDiskGroup.setStatus('current')
resLoadGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 10002, 1, 1, 1, 31, 2, 1, 4)).setObjects(("FROGFOOT-RESOURCES-MIB", "loadNumber"), ("FROGFOOT-RESOURCES-MIB", "loadDescr"), ("FROGFOOT-RESOURCES-MIB", "loadValue"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    resLoadGroup = resLoadGroup.setStatus('current')
mibBuilder.exportSymbols("FROGFOOT-RESOURCES-MIB", resources=resources, loadTable=loadTable, diskIndex=diskIndex, resCompliances=resCompliances, diskTotal=diskTotal, diskNumber=diskNumber, memBuffer=memBuffer, resMIB=resMIB, load=load, diskFree=diskFree, resCompliance=resCompliance, resMIBObjects=resMIBObjects, storage=storage, memTotal=memTotal, memory=memory, diskTable=diskTable, resGroups=resGroups, loadValue=loadValue, resLoadGroup=resLoadGroup, swapFree=swapFree, PYSNMP_MODULE_ID=resources, loadNumber=loadNumber, diskDev=diskDev, resConformance=resConformance, memCache=memCache, diskEntry=diskEntry, system=system, swapTotal=swapTotal, swap=swap, loadIndex=loadIndex, loadDescr=loadDescr, memFree=memFree, diskFSType=diskFSType, resMemGroup=resMemGroup, resSwapGroup=resSwapGroup, frogfoot=frogfoot, diskDir=diskDir, resDiskGroup=resDiskGroup, TableIndex=TableIndex, servers=servers, loadEntry=loadEntry)
