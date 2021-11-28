#
# PySNMP MIB module STORMSHIELD-HA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/stormshield/STORMSHIELD-HA-MIB
# Produced by pysmi-1.1.3 at Sun Nov 28 20:18:48 2021
# On host fv-az77-612 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Integer32, TimeTicks, ObjectIdentity, iso, IpAddress, ModuleIdentity, Bits, Unsigned32, Counter32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Integer32", "TimeTicks", "ObjectIdentity", "iso", "IpAddress", "ModuleIdentity", "Bits", "Unsigned32", "Counter32", "Counter64")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
stormshieldMIB, = mibBuilder.importSymbols("STORMSHIELD-SMI-MIB", "stormshieldMIB")
snsHA = ModuleIdentity((1, 3, 6, 1, 4, 1, 11256, 1, 11))
snsHA.setRevisions(('2017-02-20 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: snsHA.setRevisionsDescriptions(('Initial',))
if mibBuilder.loadTexts: snsHA.setLastUpdated('201702200000Z')
if mibBuilder.loadTexts: snsHA.setOrganization('Stormshield')
if mibBuilder.loadTexts: snsHA.setContactInfo('Customer Support\n\n         22 rue du Gouverneur General Eboue\n         92130 Issy-les-Moulineaux\n         FRANCE\n\n         Tel: +33 (0)9 69 32 96 29\n         E-mail: support@stormshield.eu\n         http://www.stormshield.eu')
if mibBuilder.loadTexts: snsHA.setDescription('stormshield HA cluster')
snsNbNode = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 11, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsNbNode.setStatus('current')
if mibBuilder.loadTexts: snsNbNode.setDescription('Number of firewalls in the HA cluster')
snsNbDeadNode = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 11, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsNbDeadNode.setStatus('current')
if mibBuilder.loadTexts: snsNbDeadNode.setDescription('Number of firewalls registered in the HA cluster but not replying')
snsNbActiveNode = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 11, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsNbActiveNode.setStatus('current')
if mibBuilder.loadTexts: snsNbActiveNode.setDescription('Number of active firewalls')
snsNbHALinks = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 11, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsNbHALinks.setStatus('current')
if mibBuilder.loadTexts: snsNbHALinks.setDescription('Number of ethernet links used for HA communication')
snsNbFaultyHALinks = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 11, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsNbFaultyHALinks.setStatus('current')
if mibBuilder.loadTexts: snsNbFaultyHALinks.setDescription('Number of faulty HA links')
snsNodeTable = MibTable((1, 3, 6, 1, 4, 1, 11256, 1, 11, 7), )
if mibBuilder.loadTexts: snsNodeTable.setStatus('current')
if mibBuilder.loadTexts: snsNodeTable.setDescription('Firewalls part of the HA cluster')
snsNode = MibTableRow((1, 3, 6, 1, 4, 1, 11256, 1, 11, 7, 1), ).setIndexNames((0, "STORMSHIELD-HA-MIB", "snsNodeIndex"))
if mibBuilder.loadTexts: snsNode.setStatus('current')
if mibBuilder.loadTexts: snsNode.setDescription('HA node')
snsNodeIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 11, 7, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2)))
if mibBuilder.loadTexts: snsNodeIndex.setStatus('current')
if mibBuilder.loadTexts: snsNodeIndex.setDescription('Index of each line in table')
snsFwSerial = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 11, 7, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsFwSerial.setStatus('current')
if mibBuilder.loadTexts: snsFwSerial.setDescription('Firewall serial')
snsOnline = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 11, 7, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsOnline.setStatus('current')
if mibBuilder.loadTexts: snsOnline.setDescription('Firewall is online')
snsModel = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 11, 7, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsModel.setStatus('current')
if mibBuilder.loadTexts: snsModel.setDescription('Firewall model')
snsVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 11, 7, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsVersion.setStatus('current')
if mibBuilder.loadTexts: snsVersion.setDescription('Firewall firmware version')
snsHALicence = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 11, 7, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsHALicence.setStatus('current')
if mibBuilder.loadTexts: snsHALicence.setDescription('HA Licence')
snsHAQuality = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 11, 7, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsHAQuality.setStatus('current')
if mibBuilder.loadTexts: snsHAQuality.setDescription('HA Quality')
snsHAPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 11, 7, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsHAPriority.setStatus('current')
if mibBuilder.loadTexts: snsHAPriority.setDescription('HA Priority')
snsHAStatusForced = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 11, 7, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsHAStatusForced.setStatus('current')
if mibBuilder.loadTexts: snsHAStatusForced.setDescription('HA status forced (-2 : Unknown forced status,\n         -1 : No peer found, 0 : No forced status,\n         1 : Forced active, 2 : Forced passive)')
snsHAActive = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 11, 7, 1, 10), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsHAActive.setStatus('current')
if mibBuilder.loadTexts: snsHAActive.setDescription('Is the firewall active ?')
snsUptime = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 11, 7, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsUptime.setStatus('current')
if mibBuilder.loadTexts: snsUptime.setDescription('Firewall uptime')
snsHASyncStatus = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 11, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsHASyncStatus.setStatus('current')
if mibBuilder.loadTexts: snsHASyncStatus.setDescription('Firewall configuration synchronization status ?\n         (1: Synced, 0: Not synced, -1: Unknown / Error)')
snsHAFwAdminRevison = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 11, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsHAFwAdminRevison.setStatus('current')
if mibBuilder.loadTexts: snsHAFwAdminRevison.setDescription('Firewall Admin Revision')
snsNodePowerSupplyTable = MibTable((1, 3, 6, 1, 4, 1, 11256, 1, 11, 10), )
if mibBuilder.loadTexts: snsNodePowerSupplyTable.setStatus('current')
if mibBuilder.loadTexts: snsNodePowerSupplyTable.setDescription('Power supply status of Firewalls')
snsNodePowerSupplyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11256, 1, 11, 10, 1), ).setIndexNames((0, "STORMSHIELD-HA-MIB", "snsNodeIndex"), (0, "STORMSHIELD-HA-MIB", "snsNodePowerSupplyIndex"))
if mibBuilder.loadTexts: snsNodePowerSupplyEntry.setStatus('current')
if mibBuilder.loadTexts: snsNodePowerSupplyEntry.setDescription('Power supply information')
snsNodePowerSupplyIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 11, 10, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)))
if mibBuilder.loadTexts: snsNodePowerSupplyIndex.setStatus('current')
if mibBuilder.loadTexts: snsNodePowerSupplyIndex.setDescription('Index of each line in table')
snsNodePowerSupplyPowered = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 11, 10, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsNodePowerSupplyPowered.setStatus('current')
if mibBuilder.loadTexts: snsNodePowerSupplyPowered.setDescription('Power supply is powered by electricity ?')
snsNodeDiskTable = MibTable((1, 3, 6, 1, 4, 1, 11256, 1, 11, 11), )
if mibBuilder.loadTexts: snsNodeDiskTable.setStatus('current')
if mibBuilder.loadTexts: snsNodeDiskTable.setDescription('Disks status of Firewalls')
snsNodeDiskEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11256, 1, 11, 11, 1), ).setIndexNames((0, "STORMSHIELD-HA-MIB", "snsNodeIndex"), (0, "STORMSHIELD-HA-MIB", "snsNodeDiskIndex"))
if mibBuilder.loadTexts: snsNodeDiskEntry.setStatus('current')
if mibBuilder.loadTexts: snsNodeDiskEntry.setDescription('Disk information')
snsNodeDiskIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 11, 11, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)))
if mibBuilder.loadTexts: snsNodeDiskIndex.setStatus('current')
if mibBuilder.loadTexts: snsNodeDiskIndex.setDescription('Index of each disk in table')
snsNodeDiskName = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 11, 11, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsNodeDiskName.setStatus('current')
if mibBuilder.loadTexts: snsNodeDiskName.setDescription('Mount point name')
snsNodeDiskSmartResult = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 11, 11, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsNodeDiskSmartResult.setStatus('current')
if mibBuilder.loadTexts: snsNodeDiskSmartResult.setDescription('Result of the smart infos tests')
snsNodeDiskIsRaid = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 11, 11, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsNodeDiskIsRaid.setStatus('current')
if mibBuilder.loadTexts: snsNodeDiskIsRaid.setDescription('Is the disk a member of a RAID array')
snsNodeDiskRaidStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 11, 11, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsNodeDiskRaidStatus.setStatus('current')
if mibBuilder.loadTexts: snsNodeDiskRaidStatus.setDescription('RAID Status')
snsNodeDiskPosition = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 11, 11, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsNodeDiskPosition.setStatus('current')
if mibBuilder.loadTexts: snsNodeDiskPosition.setDescription('Disk Position')
snsNodeCpuTable = MibTable((1, 3, 6, 1, 4, 1, 11256, 1, 11, 12), )
if mibBuilder.loadTexts: snsNodeCpuTable.setStatus('current')
if mibBuilder.loadTexts: snsNodeCpuTable.setDescription('Cpus status of Firewalls')
snsNodeCpuEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11256, 1, 11, 12, 1), ).setIndexNames((0, "STORMSHIELD-HA-MIB", "snsNodeIndex"), (0, "STORMSHIELD-HA-MIB", "snsNodeCpuIndex"))
if mibBuilder.loadTexts: snsNodeCpuEntry.setStatus('current')
if mibBuilder.loadTexts: snsNodeCpuEntry.setDescription('CPU information')
snsNodeCpuIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 11, 12, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)))
if mibBuilder.loadTexts: snsNodeCpuIndex.setStatus('current')
if mibBuilder.loadTexts: snsNodeCpuIndex.setDescription('Index of each cpu in table')
snsNodeCpuTemp = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 11, 12, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsNodeCpuTemp.setStatus('current')
if mibBuilder.loadTexts: snsNodeCpuTemp.setDescription('Temperature in Celsius degree')
mibBuilder.exportSymbols("STORMSHIELD-HA-MIB", snsHAStatusForced=snsHAStatusForced, snsHALicence=snsHALicence, snsNodeCpuTable=snsNodeCpuTable, snsNodeCpuEntry=snsNodeCpuEntry, snsNodeCpuTemp=snsNodeCpuTemp, snsNbHALinks=snsNbHALinks, snsNodeDiskEntry=snsNodeDiskEntry, snsHAFwAdminRevison=snsHAFwAdminRevison, snsNbNode=snsNbNode, snsUptime=snsUptime, snsVersion=snsVersion, snsNbDeadNode=snsNbDeadNode, snsNodeDiskRaidStatus=snsNodeDiskRaidStatus, snsNodePowerSupplyTable=snsNodePowerSupplyTable, snsFwSerial=snsFwSerial, snsHAPriority=snsHAPriority, snsHASyncStatus=snsHASyncStatus, snsNbFaultyHALinks=snsNbFaultyHALinks, snsNbActiveNode=snsNbActiveNode, snsHA=snsHA, snsNodePowerSupplyIndex=snsNodePowerSupplyIndex, snsNodeCpuIndex=snsNodeCpuIndex, snsNodeDiskTable=snsNodeDiskTable, snsNodeTable=snsNodeTable, snsHAActive=snsHAActive, snsNodeDiskIsRaid=snsNodeDiskIsRaid, snsNodeDiskPosition=snsNodeDiskPosition, snsHAQuality=snsHAQuality, snsOnline=snsOnline, PYSNMP_MODULE_ID=snsHA, snsNodeIndex=snsNodeIndex, snsNodePowerSupplyEntry=snsNodePowerSupplyEntry, snsNodeDiskIndex=snsNodeDiskIndex, snsNodePowerSupplyPowered=snsNodePowerSupplyPowered, snsNodeDiskName=snsNodeDiskName, snsNode=snsNode, snsModel=snsModel, snsNodeDiskSmartResult=snsNodeDiskSmartResult)
