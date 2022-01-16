#
# PySNMP MIB module ADTRAN-AOSFILESYSTEM (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/adtran/ADTRAN-AOSFILESYSTEM
# Produced by pysmi-1.1.8 at Sun Jan 16 00:31:13 2022
# On host fv-az42-839 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
adGenAOSCommon, adGenAOSConformance = mibBuilder.importSymbols("ADTRAN-AOS", "adGenAOSCommon", "adGenAOSConformance")
adIdentity, = mibBuilder.importSymbols("ADTRAN-MIB", "adIdentity")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Gauge32, ObjectIdentity, Counter64, MibIdentifier, IpAddress, iso, Unsigned32, ModuleIdentity, Counter32, Bits, NotificationType, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "ObjectIdentity", "Counter64", "MibIdentifier", "IpAddress", "iso", "Unsigned32", "ModuleIdentity", "Counter32", "Bits", "NotificationType", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks")
TDomain, RowStatus, DisplayString, TAddress, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TDomain", "RowStatus", "DisplayString", "TAddress", "TextualConvention")
adGenAOSFileSystemMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 664, 6, 10000, 53, 1, 6))
adGenAOSFileSystemMib.setRevisions(('2005-05-18 00:00',))
if mibBuilder.loadTexts: adGenAOSFileSystemMib.setLastUpdated('200505180000Z')
if mibBuilder.loadTexts: adGenAOSFileSystemMib.setOrganization('ADTRAN, Inc.')
adGenAOSFileSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 6))
adAOSFileSystemRecordTable = MibTable((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 6, 1), )
if mibBuilder.loadTexts: adAOSFileSystemRecordTable.setStatus('current')
adAOSFileSystemRecordEntry = MibTableRow((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 6, 1, 1), ).setIndexNames((0, "ADTRAN-AOSFILESYSTEM", "adAOSFileSystemRecordID"))
if mibBuilder.loadTexts: adAOSFileSystemRecordEntry.setStatus('current')
adAOSFileSystemRecordID = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 6, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adAOSFileSystemRecordID.setStatus('current')
adAOSFileSystemRecordSystem = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 6, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adAOSFileSystemRecordSystem.setStatus('current')
adAOSFileSystemRecordType = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 6, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("file", 1), ("directory", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adAOSFileSystemRecordType.setStatus('current')
adAOSFileSystemRecordPath = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 6, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adAOSFileSystemRecordPath.setStatus('current')
adAOSFileSystemRecordName = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 6, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adAOSFileSystemRecordName.setStatus('current')
adAOSFileSystemRecordSize = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 6, 1, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adAOSFileSystemRecordSize.setStatus('current')
adAOSFileSystemRecordStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 6, 1, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: adAOSFileSystemRecordStatus.setStatus('current')
adAOSFileSystemTable = MibTable((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 6, 2), )
if mibBuilder.loadTexts: adAOSFileSystemTable.setStatus('current')
adAOSFileSystemEntry = MibTableRow((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 6, 2, 1), ).setIndexNames((0, "ADTRAN-AOSFILESYSTEM", "adAOSFileSystemID"))
if mibBuilder.loadTexts: adAOSFileSystemEntry.setStatus('current')
adAOSFileSystemID = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 6, 2, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adAOSFileSystemID.setStatus('current')
adAOSFileSystemType = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 6, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adAOSFileSystemType.setStatus('current')
adAOSFileSystemTotalSize = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 6, 2, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adAOSFileSystemTotalSize.setStatus('current')
adAOSFileSystemFreeSize = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 6, 2, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adAOSFileSystemFreeSize.setStatus('current')
adGenAOSFileSystemConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 5))
adAOSFileSystemCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 5, 1))
adAOSFileSystemRecordGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 5, 2))
adAOSFileSystemGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 5, 3))
adAOSFileSystemCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 5, 1, 1)).setObjects(("ADTRAN-AOSFILESYSTEM", "adGenAOSFileSystemRecordGroup"), ("ADTRAN-AOSFILESYSTEM", "adGenAOSFileSystemGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adAOSFileSystemCompliance = adAOSFileSystemCompliance.setStatus('current')
adGenAOSFileSystemRecordGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 5, 2, 1)).setObjects(("ADTRAN-AOSFILESYSTEM", "adAOSFileSystemRecordID"), ("ADTRAN-AOSFILESYSTEM", "adAOSFileSystemRecordSystem"), ("ADTRAN-AOSFILESYSTEM", "adAOSFileSystemRecordType"), ("ADTRAN-AOSFILESYSTEM", "adAOSFileSystemRecordPath"), ("ADTRAN-AOSFILESYSTEM", "adAOSFileSystemRecordName"), ("ADTRAN-AOSFILESYSTEM", "adAOSFileSystemRecordSize"), ("ADTRAN-AOSFILESYSTEM", "adAOSFileSystemRecordStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAOSFileSystemRecordGroup = adGenAOSFileSystemRecordGroup.setStatus('current')
adGenAOSFileSystemGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 5, 3, 1)).setObjects(("ADTRAN-AOSFILESYSTEM", "adAOSFileSystemID"), ("ADTRAN-AOSFILESYSTEM", "adAOSFileSystemType"), ("ADTRAN-AOSFILESYSTEM", "adAOSFileSystemTotalSize"), ("ADTRAN-AOSFILESYSTEM", "adAOSFileSystemFreeSize"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAOSFileSystemGroup = adGenAOSFileSystemGroup.setStatus('current')
mibBuilder.exportSymbols("ADTRAN-AOSFILESYSTEM", adAOSFileSystemRecordTable=adAOSFileSystemRecordTable, adAOSFileSystemRecordSize=adAOSFileSystemRecordSize, adAOSFileSystemRecordName=adAOSFileSystemRecordName, adAOSFileSystemRecordGroups=adAOSFileSystemRecordGroups, adAOSFileSystemRecordID=adAOSFileSystemRecordID, adGenAOSFileSystemConformance=adGenAOSFileSystemConformance, adAOSFileSystemRecordEntry=adAOSFileSystemRecordEntry, adGenAOSFileSystemMib=adGenAOSFileSystemMib, adAOSFileSystemRecordSystem=adAOSFileSystemRecordSystem, adAOSFileSystemEntry=adAOSFileSystemEntry, adAOSFileSystemCompliance=adAOSFileSystemCompliance, adAOSFileSystemTotalSize=adAOSFileSystemTotalSize, adGenAOSFileSystemRecordGroup=adGenAOSFileSystemRecordGroup, adAOSFileSystemRecordPath=adAOSFileSystemRecordPath, adAOSFileSystemRecordType=adAOSFileSystemRecordType, adGenAOSFileSystemGroup=adGenAOSFileSystemGroup, PYSNMP_MODULE_ID=adGenAOSFileSystemMib, adAOSFileSystemType=adAOSFileSystemType, adAOSFileSystemTable=adAOSFileSystemTable, adAOSFileSystemGroups=adAOSFileSystemGroups, adAOSFileSystemRecordStatus=adAOSFileSystemRecordStatus, adGenAOSFileSystem=adGenAOSFileSystem, adAOSFileSystemFreeSize=adAOSFileSystemFreeSize, adAOSFileSystemCompliances=adAOSFileSystemCompliances, adAOSFileSystemID=adAOSFileSystemID)
