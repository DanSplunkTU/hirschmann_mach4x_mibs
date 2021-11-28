#
# PySNMP MIB module SYNOLOGY-RAID-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/synology/SYNOLOGY-RAID-MIB
# Produced by pysmi-1.1.3 at Sun Nov 28 20:10:08 2021
# On host fv-az77-612 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Integer32, Bits, Gauge32, TimeTicks, Counter64, ObjectIdentity, Unsigned32, IpAddress, Counter32, iso, NotificationType, MibIdentifier, enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Bits", "Gauge32", "TimeTicks", "Counter64", "ObjectIdentity", "Unsigned32", "IpAddress", "Counter32", "iso", "NotificationType", "MibIdentifier", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
synoRaid = ModuleIdentity((1, 3, 6, 1, 4, 1, 6574, 3))
synoRaid.setRevisions(('2013-09-11 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: synoRaid.setRevisionsDescriptions(('Second draft.',))
if mibBuilder.loadTexts: synoRaid.setLastUpdated('201309110000Z')
if mibBuilder.loadTexts: synoRaid.setOrganization('www.synology.com')
if mibBuilder.loadTexts: synoRaid.setContactInfo('postal:   Jay Pan\n          email:    jaypan@synology.com')
if mibBuilder.loadTexts: synoRaid.setDescription('Characteristics of the raid information')
synology = MibIdentifier((1, 3, 6, 1, 4, 1, 6574))
raidTable = MibTable((1, 3, 6, 1, 4, 1, 6574, 3, 1), )
if mibBuilder.loadTexts: raidTable.setStatus('current')
if mibBuilder.loadTexts: raidTable.setDescription('Synology raid table')
raidEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6574, 3, 1, 1), ).setIndexNames((0, "SYNOLOGY-RAID-MIB", "raidIndex"))
if mibBuilder.loadTexts: raidEntry.setStatus('current')
if mibBuilder.loadTexts: raidEntry.setDescription('For all raid entry')
raidIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: raidIndex.setStatus('current')
if mibBuilder.loadTexts: raidIndex.setDescription('The index of raid table')
raidName = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 3, 1, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: raidName.setStatus('current')
if mibBuilder.loadTexts: raidName.setDescription('Synology raid name\n\t The name of each raid will be showed here.\n\t')
raidStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 12))).setMaxAccess("readonly")
if mibBuilder.loadTexts: raidStatus.setStatus('current')
if mibBuilder.loadTexts: raidStatus.setDescription('Synology Raid status\n\t Each meanings of status represented describe below.\n\t Normal(1): The raid functions normally.\n \t Degrade(11): Degrade happens when a tolerable failure of disk(s) occurs.\n \t Crashed(12): Raid has crashed and just uses for read-only operation.\n\t \n\t ** 2018/6/15 add **\n\t DataScrubbing(13): Raid status is DATASCRUBBING\n\t RaidDeploying(14) : Deploying Single volume on pool\n\t RaidUnDeploying(15): Undeploying Single volume on pool\n\t RaidMountCache(16): Mounting SSD cache\n\t RaidUnmountCache(17): Unmounting SSD cache\n\t RaidExpandingUnfinishedSHR(18): Continue expand SHR if interrupted\n\t RaidConvertSHRToPool(19): Converting Single volume on SHR to mutiple volume on SHR\n\t RaidMigrateSHR1ToSHR2(20): Migrating SHR1 to SHR2\n\t RaidUnknownStatus(21): Unknown raid status\n\t ** END **\n\n\t Note:\n\t Other status will be showed when creating or deleting raids, including below status, Repairing(2), Migrating(3), Expanding(4), Deleting(5), Creating(6), RaidSyncing(7), RaidParityChecking(8), RaidAssembling(9) and Canceling(10).\n\t')
raidFreeSize = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 3, 1, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: raidFreeSize.setStatus('current')
if mibBuilder.loadTexts: raidFreeSize.setDescription('Synology raid freesize\n\t Free space in bytes.\n\t')
raidTotalSize = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 3, 1, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: raidTotalSize.setStatus('current')
if mibBuilder.loadTexts: raidTotalSize.setDescription('Synology raid totalsize\n\t Total space in bytes.\n\t')
raidConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6574, 3, 2))
raidCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6574, 3, 2, 1))
raidGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6574, 3, 2, 2))
raidCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6574, 3, 2, 1, 1)).setObjects(("SYNOLOGY-RAID-MIB", "raidGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    raidCompliance = raidCompliance.setStatus('current')
if mibBuilder.loadTexts: raidCompliance.setDescription('The compliance statement for synoRaid entities which\n            implement the SYNOLOGY RAID MIB.')
raidGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6574, 3, 2, 2, 1)).setObjects(("SYNOLOGY-RAID-MIB", "raidName"), ("SYNOLOGY-RAID-MIB", "raidStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    raidGroup = raidGroup.setStatus('current')
if mibBuilder.loadTexts: raidGroup.setDescription('A collection of objects providing basic instrumentation and\n            control of an synology raid entity.')
mibBuilder.exportSymbols("SYNOLOGY-RAID-MIB", PYSNMP_MODULE_ID=synoRaid, raidStatus=raidStatus, raidFreeSize=raidFreeSize, raidGroup=raidGroup, raidEntry=raidEntry, synoRaid=synoRaid, raidName=raidName, synology=synology, raidCompliances=raidCompliances, raidIndex=raidIndex, raidTable=raidTable, raidConformance=raidConformance, raidGroups=raidGroups, raidTotalSize=raidTotalSize, raidCompliance=raidCompliance)
