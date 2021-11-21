#
# PySNMP MIB module RADLAN-rndMng (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/eltex/RADLAN-RNDMNG
# Produced by pysmi-1.1.3 at Sun Nov 21 00:26:31 2021
# On host fv-az39-63 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
rnd, = mibBuilder.importSymbols("RADLAN-MIB", "rnd")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, iso, MibIdentifier, NotificationType, TimeTicks, Integer32, IpAddress, Counter64, ObjectIdentity, ModuleIdentity, Counter32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "iso", "MibIdentifier", "NotificationType", "TimeTicks", "Integer32", "IpAddress", "Counter64", "ObjectIdentity", "ModuleIdentity", "Counter32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits")
TruthValue, RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "RowStatus", "TextualConvention", "DisplayString")
rndMng = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 1))
rndMng.setRevisions(('2012-12-04 00:00', '2012-04-04 00:00', '2009-02-24 00:00', '2007-10-24 00:00', '2006-06-20 00:00', '2004-06-01 00:00',))
if mibBuilder.loadTexts: rndMng.setLastUpdated('201212040000Z')
if mibBuilder.loadTexts: rndMng.setOrganization('Radlan Computer Communications Ltd.')
rndSysId = MibScalar((1, 3, 6, 1, 4, 1, 89, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rndSysId.setStatus('current')
rndAction = MibScalar((1, 3, 6, 1, 4, 1, 89, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27))).clone(namedValues=NamedValues(("reset", 1), ("sendNetworkTab", 2), ("deleteNetworkTab", 3), ("sendRoutingTab", 4), ("deleteRoutingTab", 5), ("sendLanTab", 6), ("deleteLanTab", 7), ("deleteArpTab", 8), ("sendArpTab", 9), ("deleteRouteTab", 10), ("sendRouteTab", 11), ("backupSPFRoutingTab", 12), ("backupIPRoutingTab", 13), ("backupNetworkTab", 14), ("backupLanTab", 15), ("backupArpTab", 16), ("backupIPXRipTab", 17), ("backupIPXSAPTab", 18), ("resetStartupCDB", 19), ("eraseStartupCDB", 20), ("deleteZeroHopRoutingAllocTab", 21), ("slipDisconnect", 22), ("deleteDynamicLanTab", 23), ("eraseRunningCDB", 24), ("copyStartupToRunning", 25), ("none", 26), ("resetToFactoryDefaults", 27)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rndAction.setStatus('current')
rndFileName = MibScalar((1, 3, 6, 1, 4, 1, 89, 1, 3), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rndFileName.setStatus('current')
rlSnmpVersionSupported = MibScalar((1, 3, 6, 1, 4, 1, 89, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSnmpVersionSupported.setStatus('current')
rlSnmpMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 89, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSnmpMibVersion.setStatus('current')
rlCpuUtilEnable = MibScalar((1, 3, 6, 1, 4, 1, 89, 1, 6), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCpuUtilEnable.setStatus('current')
rlCpuUtilDuringLastSecond = MibScalar((1, 3, 6, 1, 4, 1, 89, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 101))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlCpuUtilDuringLastSecond.setStatus('current')
rlCpuUtilDuringLastMinute = MibScalar((1, 3, 6, 1, 4, 1, 89, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 101))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlCpuUtilDuringLastMinute.setStatus('current')
rlCpuUtilDuringLast5Minutes = MibScalar((1, 3, 6, 1, 4, 1, 89, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 101))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlCpuUtilDuringLast5Minutes.setStatus('current')
rlRebootDelay = MibScalar((1, 3, 6, 1, 4, 1, 89, 1, 10), TimeTicks()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlRebootDelay.setStatus('current')
rlGroupManagement = MibIdentifier((1, 3, 6, 1, 4, 1, 89, 1, 11))
rlGroupMngQuery = MibScalar((1, 3, 6, 1, 4, 1, 89, 1, 11, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("query", 1), ("idle", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlGroupMngQuery.setStatus('current')
rlGroupMngQueryPeriod = MibScalar((1, 3, 6, 1, 4, 1, 89, 1, 11, 2), Integer32()).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlGroupMngQueryPeriod.setStatus('current')
rlGroupMngLastUpdate = MibScalar((1, 3, 6, 1, 4, 1, 89, 1, 11, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlGroupMngLastUpdate.setStatus('current')
rlGroupMngDevicesTable = MibTable((1, 3, 6, 1, 4, 1, 89, 1, 11, 4), )
if mibBuilder.loadTexts: rlGroupMngDevicesTable.setStatus('current')
rlGroupMngDeviceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 1, 11, 4, 1), ).setIndexNames((0, "RADLAN-rndMng", "rlGroupMngDeviceIdType"), (0, "RADLAN-rndMng", "rlGroupMngDeviceId"), (0, "RADLAN-rndMng", "rlGroupMngSubdevice"))
if mibBuilder.loadTexts: rlGroupMngDeviceEntry.setStatus('current')
rlGroupMngDeviceIdType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 1, 11, 4, 1, 1), InetAddressType())
if mibBuilder.loadTexts: rlGroupMngDeviceIdType.setStatus('current')
rlGroupMngDeviceId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 1, 11, 4, 1, 2), InetAddress())
if mibBuilder.loadTexts: rlGroupMngDeviceId.setStatus('current')
rlGroupMngSubdevice = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 1, 11, 4, 1, 3), Integer32())
if mibBuilder.loadTexts: rlGroupMngSubdevice.setStatus('current')
rlGroupMngDeviceDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 1, 11, 4, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlGroupMngDeviceDescription.setStatus('current')
rlGroupMngGroupMngEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 1, 11, 4, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlGroupMngGroupMngEnabled.setStatus('current')
rlGroupMngGroupLLDPDeviceId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 1, 11, 4, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlGroupMngGroupLLDPDeviceId.setStatus('current')
rlGroupMngDeviceVendor = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 1, 11, 4, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlGroupMngDeviceVendor.setStatus('current')
rlGroupMngDeviceAdvertisedCachingTime = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 1, 11, 4, 1, 8), Integer32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: rlGroupMngDeviceAdvertisedCachingTime.setStatus('current')
rlGroupMngDeviceLocationURL = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 1, 11, 4, 1, 9), DisplayString()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: rlGroupMngDeviceLocationURL.setStatus('current')
rlGroupMngDeviceLastSeen = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 1, 11, 4, 1, 10), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlGroupMngDeviceLastSeen.setStatus('current')
rlRunningCDBequalToStartupCDB = MibScalar((1, 3, 6, 1, 4, 1, 89, 1, 13), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlRunningCDBequalToStartupCDB.setStatus('current')
rlClearMib = MibScalar((1, 3, 6, 1, 4, 1, 89, 1, 14), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlClearMib.setStatus('current')
rlScheduledReload = MibScalar((1, 3, 6, 1, 4, 1, 89, 1, 15), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 10))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlScheduledReload.setStatus('current')
rlScheduledReloadPendingDate = MibScalar((1, 3, 6, 1, 4, 1, 89, 1, 16), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 24))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlScheduledReloadPendingDate.setStatus('current')
rlScheduledReloadApprovedDate = MibScalar((1, 3, 6, 1, 4, 1, 89, 1, 17), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 24))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlScheduledReloadApprovedDate.setStatus('current')
rlScheduledReloadCommit = MibScalar((1, 3, 6, 1, 4, 1, 89, 1, 18), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlScheduledReloadCommit.setStatus('current')
rlSysNameTable = MibTable((1, 3, 6, 1, 4, 1, 89, 1, 19), )
if mibBuilder.loadTexts: rlSysNameTable.setStatus('current')
rlSysNameEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 1, 19, 1), ).setIndexNames((0, "RADLAN-rndMng", "rlSysNameSource"), (0, "RADLAN-rndMng", "rlSysNameIfIndex"))
if mibBuilder.loadTexts: rlSysNameEntry.setStatus('current')
rlSysNameSource = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 1, 19, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("dhcpv6", 1), ("dhcpv4", 2), ("static", 3))).clone('static'))
if mibBuilder.loadTexts: rlSysNameSource.setStatus('current')
rlSysNameIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 1, 19, 1, 2), InterfaceIndex().clone(1))
if mibBuilder.loadTexts: rlSysNameIfIndex.setStatus('current')
rlSysNameName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 1, 19, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlSysNameName.setStatus('current')
rlSysNameRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 1, 19, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlSysNameRowStatus.setStatus('current')
rlErrdisableLinkFlappingCause = MibScalar((1, 3, 6, 1, 4, 1, 89, 1, 20), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlErrdisableLinkFlappingCause.setStatus('current')
mibBuilder.exportSymbols("RADLAN-rndMng", rlSysNameName=rlSysNameName, rlClearMib=rlClearMib, rlErrdisableLinkFlappingCause=rlErrdisableLinkFlappingCause, rlSysNameIfIndex=rlSysNameIfIndex, rlGroupMngDeviceVendor=rlGroupMngDeviceVendor, rndAction=rndAction, rndMng=rndMng, rlCpuUtilEnable=rlCpuUtilEnable, rndSysId=rndSysId, rlGroupMngDeviceLastSeen=rlGroupMngDeviceLastSeen, rlCpuUtilDuringLastMinute=rlCpuUtilDuringLastMinute, rlGroupMngLastUpdate=rlGroupMngLastUpdate, rlSysNameEntry=rlSysNameEntry, rlRebootDelay=rlRebootDelay, rlGroupMngGroupMngEnabled=rlGroupMngGroupMngEnabled, rlGroupMngDeviceEntry=rlGroupMngDeviceEntry, rlGroupMngSubdevice=rlGroupMngSubdevice, rlSnmpMibVersion=rlSnmpMibVersion, rlGroupMngQuery=rlGroupMngQuery, rlGroupMngGroupLLDPDeviceId=rlGroupMngGroupLLDPDeviceId, rlGroupManagement=rlGroupManagement, rlSysNameRowStatus=rlSysNameRowStatus, rlSnmpVersionSupported=rlSnmpVersionSupported, rlGroupMngDeviceDescription=rlGroupMngDeviceDescription, rlSysNameSource=rlSysNameSource, rlGroupMngDeviceLocationURL=rlGroupMngDeviceLocationURL, rlCpuUtilDuringLast5Minutes=rlCpuUtilDuringLast5Minutes, rndFileName=rndFileName, rlScheduledReloadCommit=rlScheduledReloadCommit, rlSysNameTable=rlSysNameTable, rlScheduledReloadPendingDate=rlScheduledReloadPendingDate, rlGroupMngDeviceId=rlGroupMngDeviceId, rlGroupMngDeviceIdType=rlGroupMngDeviceIdType, rlCpuUtilDuringLastSecond=rlCpuUtilDuringLastSecond, rlGroupMngDeviceAdvertisedCachingTime=rlGroupMngDeviceAdvertisedCachingTime, rlScheduledReloadApprovedDate=rlScheduledReloadApprovedDate, rlRunningCDBequalToStartupCDB=rlRunningCDBequalToStartupCDB, rlScheduledReload=rlScheduledReload, rlGroupMngDevicesTable=rlGroupMngDevicesTable, PYSNMP_MODULE_ID=rndMng, rlGroupMngQueryPeriod=rlGroupMngQueryPeriod)
