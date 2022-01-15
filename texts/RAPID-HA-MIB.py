#
# PySNMP MIB module RAPID-HA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/nortel/RAPID-HA-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 18:14:58 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
rapidstream, = mibBuilder.importSymbols("RAPID-MIB", "rapidstream")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, ModuleIdentity, IpAddress, Integer32, Bits, Counter32, MibIdentifier, enterprises, Unsigned32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, NotificationType, iso, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "ModuleIdentity", "IpAddress", "Integer32", "Bits", "Counter32", "MibIdentifier", "enterprises", "Unsigned32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "NotificationType", "iso", "Gauge32")
DateAndTime, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "DisplayString", "TextualConvention")
rsInfoModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 4355, 6))
rsInfoModule.setRevisions(('2002-11-01 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rsInfoModule.setRevisionsDescriptions(('Initial revision.',))
if mibBuilder.loadTexts: rsInfoModule.setLastUpdated('0211011200Z')
if mibBuilder.loadTexts: rsInfoModule.setOrganization('WatchGuard Technologies, Inc.')
if mibBuilder.loadTexts: rsInfoModule.setContactInfo('   Ella Yu\n                      WatchGuard Technologies, Inc.\n                      1841 Zanker Road\n                      San Jose, CA 95112\n                      USA\n\n                      408-519-4888\n                      ella.yu@watchguard.com ')
if mibBuilder.loadTexts: rsInfoModule.setDescription('The MIB module describes general information\n             of RapidStream system.  Mainly, the information \n             obtained from this MIB is used by rsInfoSystemMIB,\n             rsClientMIB, rsSystemStatisticsMIB, rsIpsecTunnelMIB,\n             rsHAMIB.')
rsHAMIB = ObjectIdentity((1, 3, 6, 1, 4, 1, 4355, 6, 6))
if mibBuilder.loadTexts: rsHAMIB.setStatus('current')
if mibBuilder.loadTexts: rsHAMIB.setDescription('This is the base object identifier for all HA related\n             branches.')
rsHALocal = ObjectIdentity((1, 3, 6, 1, 4, 1, 4355, 6, 6, 1))
if mibBuilder.loadTexts: rsHALocal.setStatus('current')
if mibBuilder.loadTexts: rsHALocal.setDescription('This is the base object identifier for all objects which are\n            belong to local appliance.')
rsHAPeer = ObjectIdentity((1, 3, 6, 1, 4, 1, 4355, 6, 6, 2))
if mibBuilder.loadTexts: rsHAPeer.setStatus('current')
if mibBuilder.loadTexts: rsHAPeer.setDescription('This is the base object identifier for all objects which are\n            belong to peer appliance.')
rsHAStatus = MibScalar((1, 3, 6, 1, 4, 1, 4355, 6, 6, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))).clone(namedValues=NamedValues(("disabled", 0), ("unknown", 1), ("as-primary-active", 2), ("as-secondary-active", 3), ("aa-primary-ative", 4), ("aa-secondary-active", 5), ("aa-primary-takeover", 6), ("aa-secondary-takeover", 7), ("standby", 8), ("admin", 9), ("failed", 10), ("unavailable", 11)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsHAStatus.setStatus('current')
if mibBuilder.loadTexts: rsHAStatus.setDescription("Indicates current status of local appliance. \n             disabled:               The local appliance of HA system is not enabled. \n             unknown:                The local appliance of HA system is in initialization\n             as-primary-active:      The local appliance that is the primary appliance of \n                                     HA/AS system is in active mode. This status is also called \n                                     MASTER in some systems.\n             as-secondary-active:    The local appliance that is the secondary appliance of \n                                     HA/AS system is in active mode. This status is also called\n                                     BACKUP in some systems.\n             aa-primary-ative:       The local appliance that is the primary appliance of \n                                     HA/AA system is in active mode.\n             aa-secondary-active:    The local appliance that is the secondary appliance of \n                                     HA/AA system is in active mode.\n             aa-primary-takeover:    The local appliance that is the primary appliance of \n                                     HA/AA system has taken over the peer's duty.\n             aa-secondary-takeover:  The local appliance of the secondary appliance of \n                                     HA/AA system has taken over the peer's duty.\n             standby:                The local appliance of HA/AS system is in standby mode.\n             admin:                  The local appliance of HA system detects an mismatched\n                                     configuration and waits for system administrator to reslove\n                                     the conflict.\n             failed:                 The local appliance of the HA system is down due to forced failover\n                                     or other reasons.\n             unavailable:            It's reported when local appliance of HA system is unabled \n                                     to get status information.\n            ")
rsHAPeerStatus = MibScalar((1, 3, 6, 1, 4, 1, 4355, 6, 6, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("unavailable", 0), ("active", 1), ("standby", 2), ("admin", 3), ("failed", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsHAPeerStatus.setStatus('current')
if mibBuilder.loadTexts: rsHAPeerStatus.setDescription("Indicates current status of peer appliance.\n             unavailable:    It's reported when peer appliance of HA system is unabled\n                             to get status information. \n             active:         The peer applicance of HA system is in active mode.\n             standby:        The peer applicance of HA system is in standby mode.\n             admin:          The peer applicance of HA system dectects an mismatched\n                             configuration and waits for system administrator to reslove the conflict. \n             failed:         The peer appliance of HA system is down due to forced failover or other reasons.\n            ")
rsHALastDBSyncTime = MibScalar((1, 3, 6, 1, 4, 1, 4355, 6, 6, 1, 3), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsHALastDBSyncTime.setStatus('current')
if mibBuilder.loadTexts: rsHALastDBSyncTime.setDescription('The last DB synchronized time of local appliance.')
rsHAError = MibScalar((1, 3, 6, 1, 4, 1, 4355, 6, 6, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14))).clone(namedValues=NamedValues(("no-error", 0), ("mismatched-ha-id", 1), ("mismatched-software", 2), ("mismatched-database", 3), ("mismatched-hardware", 4), ("forced-fail", 5), ("invalid-ha-role", 6), ("link-down", 7), ("lost-mia-heartbeat", 8), ("mia-not-responding", 9), ("admin-command-failed", 10), ("detect-ha-error", 11), ("unavailable", 12), ("hotsync-failed", 13), ("config-sync-failed", 14)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsHAError.setStatus('current')
if mibBuilder.loadTexts: rsHAError.setDescription('Reports the current error that occurred in local appliance .')
rsHAPeerError = MibScalar((1, 3, 6, 1, 4, 1, 4355, 6, 6, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14))).clone(namedValues=NamedValues(("no-error", 0), ("mismatched-ha-id", 1), ("mismatched-software", 2), ("mismatched-database", 3), ("mismatched-hardware", 4), ("forced-fail", 5), ("invalid-ha-role", 6), ("link-down", 7), ("lost-mia-heartbeat", 8), ("mia-not-responding", 9), ("admin-command-failed", 10), ("detect-ha-error", 11), ("unavailable", 12), ("hotsync-failed", 13), ("config-sync-failed", 14)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsHAPeerError.setStatus('current')
if mibBuilder.loadTexts: rsHAPeerError.setDescription('Reports the current error that occurred in peer appliance.')
rsHAPeerSerialNumber = MibScalar((1, 3, 6, 1, 4, 1, 4355, 6, 6, 2, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsHAPeerSerialNumber.setStatus('current')
if mibBuilder.loadTexts: rsHAPeerSerialNumber.setDescription('The serial number of peer appliance.')
rsHAPeerLastDBSyncTime = MibScalar((1, 3, 6, 1, 4, 1, 4355, 6, 6, 2, 2), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsHAPeerLastDBSyncTime.setStatus('current')
if mibBuilder.loadTexts: rsHAPeerLastDBSyncTime.setDescription('The last DB synchronized time of peer appliance.')
rsHAPeerDevice = ObjectIdentity((1, 3, 6, 1, 4, 1, 4355, 6, 6, 2, 3))
if mibBuilder.loadTexts: rsHAPeerDevice.setStatus('current')
if mibBuilder.loadTexts: rsHAPeerDevice.setDescription('This is the base object for parameters and configuration\n           data of devices in this entity.')
rsHAPeerCounters = ObjectIdentity((1, 3, 6, 1, 4, 1, 4355, 6, 6, 2, 4))
if mibBuilder.loadTexts: rsHAPeerCounters.setStatus('current')
if mibBuilder.loadTexts: rsHAPeerCounters.setDescription('This is the base object for parameters and configuration\n           data of devices in this entity.')
rsHAPeerIfNumber = MibScalar((1, 3, 6, 1, 4, 1, 4355, 6, 6, 2, 3, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsHAPeerIfNumber.setStatus('current')
if mibBuilder.loadTexts: rsHAPeerIfNumber.setDescription('The number of RapidCard installed in this entity.')
rsHAPeerIfTable = MibTable((1, 3, 6, 1, 4, 1, 4355, 6, 6, 2, 3, 2), )
if mibBuilder.loadTexts: rsHAPeerIfTable.setStatus('current')
if mibBuilder.loadTexts: rsHAPeerIfTable.setDescription('A list of RapidCard entries.  The number of\n           entries is given by the value of rsHAPeerDeviceNumber.')
rsHAPeerIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4355, 6, 6, 2, 3, 2, 1), ).setIndexNames((0, "RAPID-HA-MIB", "rsHAPeerIfIndex"))
if mibBuilder.loadTexts: rsHAPeerIfEntry.setStatus('current')
if mibBuilder.loadTexts: rsHAPeerIfEntry.setDescription('A RapidCard entry containing objects for a\n           particular RapidCard.')
rsHAPeerIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4355, 6, 6, 2, 3, 2, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsHAPeerIfIndex.setStatus('current')
if mibBuilder.loadTexts: rsHAPeerIfIndex.setDescription('The unique value for each interface.')
rsHAPeerIfIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 4355, 6, 6, 2, 3, 2, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsHAPeerIfIpAddr.setStatus('current')
if mibBuilder.loadTexts: rsHAPeerIfIpAddr.setDescription('The ip address of the interface.')
rsHAPeerIfLinkStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4355, 6, 6, 2, 3, 2, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("down", 0), ("up", 1), ("other", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsHAPeerIfLinkStatus.setStatus('current')
if mibBuilder.loadTexts: rsHAPeerIfLinkStatus.setDescription('The current state of the interface.')
rsHAPeerSystemCpuUtil = MibScalar((1, 3, 6, 1, 4, 1, 4355, 6, 6, 2, 4, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsHAPeerSystemCpuUtil.setStatus('current')
if mibBuilder.loadTexts: rsHAPeerSystemCpuUtil.setDescription('The CPU utilization of the peer system in last 5 \n            seconds.')
rsHAPeerSystemTotalSendBytes = MibScalar((1, 3, 6, 1, 4, 1, 4355, 6, 6, 2, 4, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsHAPeerSystemTotalSendBytes.setStatus('current')
if mibBuilder.loadTexts: rsHAPeerSystemTotalSendBytes.setDescription('The total number of bytes sent since peer system \n            is up.')
rsHAPeerSystemTotalRecvBytes = MibScalar((1, 3, 6, 1, 4, 1, 4355, 6, 6, 2, 4, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsHAPeerSystemTotalRecvBytes.setStatus('current')
if mibBuilder.loadTexts: rsHAPeerSystemTotalRecvBytes.setDescription('The total number of bytes received since peer system \n            is up.')
rsHAPeerSystemTotalSendPackets = MibScalar((1, 3, 6, 1, 4, 1, 4355, 6, 6, 2, 4, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsHAPeerSystemTotalSendPackets.setStatus('current')
if mibBuilder.loadTexts: rsHAPeerSystemTotalSendPackets.setDescription('The total number of packets sent since peer system is \n            up.')
rsHAPeerSystemTotalRecvPackets = MibScalar((1, 3, 6, 1, 4, 1, 4355, 6, 6, 2, 4, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsHAPeerSystemTotalRecvPackets.setStatus('current')
if mibBuilder.loadTexts: rsHAPeerSystemTotalRecvPackets.setDescription('The total number of packets received since peer \n            system is up.')
rsHAPeerSystemStreamReqTotal = MibScalar((1, 3, 6, 1, 4, 1, 4355, 6, 6, 2, 4, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsHAPeerSystemStreamReqTotal.setStatus('current')
if mibBuilder.loadTexts: rsHAPeerSystemStreamReqTotal.setDescription('The total number of the connection requests since \n            system is up.')
rsHAPeerSystemStreamReqDrop = MibScalar((1, 3, 6, 1, 4, 1, 4355, 6, 6, 2, 4, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsHAPeerSystemStreamReqDrop.setStatus('current')
if mibBuilder.loadTexts: rsHAPeerSystemStreamReqDrop.setDescription('The total number of the connection requests being \n            dropped since system is up.')
rsHAPeerSystemCurrIpsecTunnels = MibScalar((1, 3, 6, 1, 4, 1, 4355, 6, 6, 2, 4, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsHAPeerSystemCurrIpsecTunnels.setStatus('current')
if mibBuilder.loadTexts: rsHAPeerSystemCurrIpsecTunnels.setDescription('The number of ipsec tunnels in the peer system \n            currently.')
rsHAPeerSystemCpuUtil1 = MibScalar((1, 3, 6, 1, 4, 1, 4355, 6, 6, 2, 4, 9), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsHAPeerSystemCpuUtil1.setStatus('current')
if mibBuilder.loadTexts: rsHAPeerSystemCpuUtil1.setDescription('The CPU utilization of the peer system in last 1 \n            minute.')
rsHAPeerSystemCpuUtil5 = MibScalar((1, 3, 6, 1, 4, 1, 4355, 6, 6, 2, 4, 10), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsHAPeerSystemCpuUtil5.setStatus('current')
if mibBuilder.loadTexts: rsHAPeerSystemCpuUtil5.setDescription('The CPU utilization of the peer system in last 5 \n            minutes.')
rsHAPeerSystemCpuUtil15 = MibScalar((1, 3, 6, 1, 4, 1, 4355, 6, 6, 2, 4, 11), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsHAPeerSystemCpuUtil15.setStatus('current')
if mibBuilder.loadTexts: rsHAPeerSystemCpuUtil15.setDescription('The CPU utilization of the peer system in last 15 \n            minutes.')
mibBuilder.exportSymbols("RAPID-HA-MIB", rsHAPeerIfLinkStatus=rsHAPeerIfLinkStatus, rsHAPeerSystemTotalSendBytes=rsHAPeerSystemTotalSendBytes, rsHAPeerSystemTotalSendPackets=rsHAPeerSystemTotalSendPackets, rsHAPeerSerialNumber=rsHAPeerSerialNumber, rsHAPeerIfEntry=rsHAPeerIfEntry, rsHAPeerError=rsHAPeerError, PYSNMP_MODULE_ID=rsInfoModule, rsHAMIB=rsHAMIB, rsHAPeerIfTable=rsHAPeerIfTable, rsHAPeerSystemCpuUtil=rsHAPeerSystemCpuUtil, rsHAPeerIfIpAddr=rsHAPeerIfIpAddr, rsHAPeerSystemTotalRecvBytes=rsHAPeerSystemTotalRecvBytes, rsHAPeerSystemCpuUtil15=rsHAPeerSystemCpuUtil15, rsHALocal=rsHALocal, rsHAStatus=rsHAStatus, rsHAPeerSystemCurrIpsecTunnels=rsHAPeerSystemCurrIpsecTunnels, rsHAPeerSystemStreamReqDrop=rsHAPeerSystemStreamReqDrop, rsHAPeerDevice=rsHAPeerDevice, rsHAPeerSystemCpuUtil5=rsHAPeerSystemCpuUtil5, rsHAError=rsHAError, rsInfoModule=rsInfoModule, rsHAPeerCounters=rsHAPeerCounters, rsHAPeerSystemCpuUtil1=rsHAPeerSystemCpuUtil1, rsHALastDBSyncTime=rsHALastDBSyncTime, rsHAPeerSystemTotalRecvPackets=rsHAPeerSystemTotalRecvPackets, rsHAPeerStatus=rsHAPeerStatus, rsHAPeer=rsHAPeer, rsHAPeerIfIndex=rsHAPeerIfIndex, rsHAPeerLastDBSyncTime=rsHAPeerLastDBSyncTime, rsHAPeerSystemStreamReqTotal=rsHAPeerSystemStreamReqTotal, rsHAPeerIfNumber=rsHAPeerIfNumber)
