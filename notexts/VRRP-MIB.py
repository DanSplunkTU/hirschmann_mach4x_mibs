#
# PySNMP MIB module VRRP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/output/asn1/VRRP-MIB
# Produced by pysmi-1.1.8 at Sun Jan 16 00:41:36 2022
# On host fv-az42-839 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, TimeTicks, Counter32, Unsigned32, MibIdentifier, iso, ObjectIdentity, Bits, Gauge32, Integer32, IpAddress, ModuleIdentity, mib_2, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "TimeTicks", "Counter32", "Unsigned32", "MibIdentifier", "iso", "ObjectIdentity", "Bits", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "mib-2", "Counter64")
MacAddress, TimeInterval, TruthValue, StorageType, TimeStamp, TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "TimeInterval", "TruthValue", "StorageType", "TimeStamp", "TextualConvention", "RowStatus", "DisplayString")
vrrpMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 68))
vrrpMIB.setRevisions(('2006-12-13 00:00', '2000-03-03 00:00',))
if mibBuilder.loadTexts: vrrpMIB.setLastUpdated('200612130000Z')
if mibBuilder.loadTexts: vrrpMIB.setOrganization('IETF VRRP Working Group')
class VrId(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 255)

vrrpOperations = MibIdentifier((1, 3, 6, 1, 2, 1, 68, 1))
vrrpStatistics = MibIdentifier((1, 3, 6, 1, 2, 1, 68, 2))
vrrpConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 68, 3))
vrrpNodeVersion = MibScalar((1, 3, 6, 1, 2, 1, 68, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpNodeVersion.setStatus('deprecated')
vrrpNotificationCntl = MibScalar((1, 3, 6, 1, 2, 1, 68, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vrrpNotificationCntl.setStatus('current')
vrrpOperationsTable = MibTable((1, 3, 6, 1, 2, 1, 68, 1, 7), )
if mibBuilder.loadTexts: vrrpOperationsTable.setStatus('current')
vrrpOperationsEntry = MibTableRow((1, 3, 6, 1, 2, 1, 68, 1, 7, 1), ).setIndexNames((0, "VRRP-MIB", "vrrpOperationsInetAddrType"), (0, "VRRP-MIB", "vrrpOperationsVrId"), (0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: vrrpOperationsEntry.setStatus('current')
vrrpOperationsInetAddrType = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 1, 7, 1, 1), InetAddressType())
if mibBuilder.loadTexts: vrrpOperationsInetAddrType.setStatus('current')
vrrpOperationsVrId = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 1, 7, 1, 2), VrId())
if mibBuilder.loadTexts: vrrpOperationsVrId.setStatus('current')
vrrpOperationsVirtualMacAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 1, 7, 1, 3), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpOperationsVirtualMacAddr.setStatus('current')
vrrpOperationsState = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 1, 7, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("initialize", 1), ("backup", 2), ("master", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpOperationsState.setStatus('current')
vrrpOperationsPriority = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 1, 7, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)).clone(100)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vrrpOperationsPriority.setStatus('current')
vrrpOperationsAddrCount = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 1, 7, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpOperationsAddrCount.setStatus('current')
vrrpOperationsMasterIpAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 1, 7, 1, 7), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpOperationsMasterIpAddr.setStatus('current')
vrrpOperationsPrimaryIpAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 1, 7, 1, 8), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vrrpOperationsPrimaryIpAddr.setStatus('current')
vrrpOperationsAdvInterval = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 1, 7, 1, 9), TimeInterval().subtype(subtypeSpec=ValueRangeConstraint(1, 4096)).clone(100)).setUnits('centiseconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: vrrpOperationsAdvInterval.setStatus('current')
vrrpOperationsPreemptMode = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 1, 7, 1, 10), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vrrpOperationsPreemptMode.setStatus('current')
vrrpOperationsAcceptMode = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 1, 7, 1, 11), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vrrpOperationsAcceptMode.setStatus('current')
vrrpOperationsUpTime = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 1, 7, 1, 12), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpOperationsUpTime.setStatus('current')
vrrpOperationsStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 1, 7, 1, 13), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vrrpOperationsStorageType.setStatus('current')
vrrpOperationsRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 1, 7, 1, 14), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vrrpOperationsRowStatus.setStatus('current')
vrrpAssociatedIpAddrTable = MibTable((1, 3, 6, 1, 2, 1, 68, 1, 8), )
if mibBuilder.loadTexts: vrrpAssociatedIpAddrTable.setStatus('current')
vrrpAssociatedIpAddrEntry = MibTableRow((1, 3, 6, 1, 2, 1, 68, 1, 8, 1), ).setIndexNames((0, "VRRP-MIB", "vrrpOperationsInetAddrType"), (0, "VRRP-MIB", "vrrpOperationsVrId"), (0, "IF-MIB", "ifIndex"), (0, "VRRP-MIB", "vrrpAssociatedIpAddr"))
if mibBuilder.loadTexts: vrrpAssociatedIpAddrEntry.setStatus('current')
vrrpAssociatedIpAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 1, 8, 1, 1), InetAddress().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(4, 4), ValueSizeConstraint(16, 16), )))
if mibBuilder.loadTexts: vrrpAssociatedIpAddr.setStatus('current')
vrrpAssociatedStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 1, 8, 1, 2), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vrrpAssociatedStorageType.setStatus('current')
vrrpAssociatedIpAddrRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 1, 8, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vrrpAssociatedIpAddrRowStatus.setStatus('current')
vrrpRouterChecksumErrors = MibScalar((1, 3, 6, 1, 2, 1, 68, 2, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpRouterChecksumErrors.setStatus('current')
vrrpRouterVersionErrors = MibScalar((1, 3, 6, 1, 2, 1, 68, 2, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpRouterVersionErrors.setStatus('current')
vrrpRouterVrIdErrors = MibScalar((1, 3, 6, 1, 2, 1, 68, 2, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpRouterVrIdErrors.setStatus('current')
vrrpRouterStatisticsTable = MibTable((1, 3, 6, 1, 2, 1, 68, 2, 5), )
if mibBuilder.loadTexts: vrrpRouterStatisticsTable.setStatus('current')
vrrpRouterStatisticsEntry = MibTableRow((1, 3, 6, 1, 2, 1, 68, 2, 5, 1), )
vrrpOperationsEntry.registerAugmentions(("VRRP-MIB", "vrrpRouterStatisticsEntry"))
vrrpRouterStatisticsEntry.setIndexNames(*vrrpOperationsEntry.getIndexNames())
if mibBuilder.loadTexts: vrrpRouterStatisticsEntry.setStatus('current')
vrrpStatisticsMasterTransitions = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 2, 5, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpStatisticsMasterTransitions.setStatus('current')
vrrpStatisticsRcvdAdvertisements = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 2, 5, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpStatisticsRcvdAdvertisements.setStatus('current')
vrrpStatisticsAdvIntervalErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 2, 5, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpStatisticsAdvIntervalErrors.setStatus('current')
vrrpStatisticsIpTtlErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 2, 5, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpStatisticsIpTtlErrors.setStatus('current')
vrrpStatisticsRcvdPriZeroPackets = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 2, 5, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpStatisticsRcvdPriZeroPackets.setStatus('current')
vrrpStatisticsSentPriZeroPackets = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 2, 5, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpStatisticsSentPriZeroPackets.setStatus('current')
vrrpStatisticsRcvdInvalidTypePkts = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 2, 5, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpStatisticsRcvdInvalidTypePkts.setStatus('current')
vrrpStatisticsAddressListErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 2, 5, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpStatisticsAddressListErrors.setStatus('current')
vrrpStatisticsPacketLengthErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 2, 5, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpStatisticsPacketLengthErrors.setStatus('current')
vrrpStatisticsRcvdInvalidAuthentications = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 2, 5, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpStatisticsRcvdInvalidAuthentications.setStatus('current')
vrrpStatisticsDiscontinuityTime = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 2, 5, 1, 11), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpStatisticsDiscontinuityTime.setStatus('current')
vrrpStatisticsRefreshRate = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 2, 5, 1, 12), Unsigned32()).setUnits('milli-seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpStatisticsRefreshRate.setStatus('current')
vrrpNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 68, 0))
vrrpNewMasterReason = MibScalar((1, 3, 6, 1, 2, 1, 68, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("notmaster", 0), ("priority", 1), ("preempted", 2), ("masterNoResponse", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpNewMasterReason.setStatus('current')
vrrpTrapProtoErrReason = MibScalar((1, 3, 6, 1, 2, 1, 68, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("hopLimitError", 0), ("versionError", 1), ("checksumError", 2), ("vridError", 3)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: vrrpTrapProtoErrReason.setStatus('current')
vrrpTrapNewMaster = NotificationType((1, 3, 6, 1, 2, 1, 68, 0, 1)).setObjects(("VRRP-MIB", "vrrpOperationsMasterIpAddr"), ("VRRP-MIB", "vrrpNewMasterReason"))
if mibBuilder.loadTexts: vrrpTrapNewMaster.setStatus('current')
vrrpTrapProtoError = NotificationType((1, 3, 6, 1, 2, 1, 68, 0, 3)).setObjects(("VRRP-MIB", "vrrpTrapProtoErrReason"))
if mibBuilder.loadTexts: vrrpTrapProtoError.setStatus('current')
vrrpOperTable = MibTable((1, 3, 6, 1, 2, 1, 68, 1, 3), )
if mibBuilder.loadTexts: vrrpOperTable.setStatus('deprecated')
vrrpOperEntry = MibTableRow((1, 3, 6, 1, 2, 1, 68, 1, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "VRRP-MIB", "vrrpOperVrId"))
if mibBuilder.loadTexts: vrrpOperEntry.setStatus('deprecated')
vrrpOperVrId = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 1, 3, 1, 1), VrId())
if mibBuilder.loadTexts: vrrpOperVrId.setStatus('deprecated')
vrrpOperVirtualMacAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 1, 3, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpOperVirtualMacAddr.setStatus('deprecated')
vrrpOperState = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("initialize", 1), ("backup", 2), ("master", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpOperState.setStatus('deprecated')
vrrpOperAdminState = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 1, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2))).clone('down')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vrrpOperAdminState.setStatus('deprecated')
vrrpOperPriority = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 1, 3, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)).clone(100)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vrrpOperPriority.setStatus('deprecated')
vrrpOperIpAddrCount = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 1, 3, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpOperIpAddrCount.setStatus('deprecated')
vrrpOperMasterIpAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 1, 3, 1, 7), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpOperMasterIpAddr.setStatus('deprecated')
vrrpOperPrimaryIpAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 1, 3, 1, 8), IpAddress().clone(hexValue="00000000")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vrrpOperPrimaryIpAddr.setStatus('deprecated')
vrrpOperAuthType = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 1, 3, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAuthentication", 1), ("simpleTextPassword", 2), ("ipAuthenticationHeader", 3))).clone('noAuthentication')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vrrpOperAuthType.setStatus('deprecated')
vrrpOperAuthKey = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 1, 3, 1, 10), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vrrpOperAuthKey.setStatus('deprecated')
vrrpOperAdvertisementInterval = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 1, 3, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)).clone(1)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: vrrpOperAdvertisementInterval.setStatus('deprecated')
vrrpOperPreemptMode = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 1, 3, 1, 12), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vrrpOperPreemptMode.setStatus('deprecated')
vrrpOperVirtualRouterUpTime = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 1, 3, 1, 13), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpOperVirtualRouterUpTime.setStatus('deprecated')
vrrpOperProtocol = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 1, 3, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("ip", 1), ("bridge", 2), ("decnet", 3), ("other", 4))).clone('ip')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vrrpOperProtocol.setStatus('deprecated')
vrrpOperRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 1, 3, 1, 15), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vrrpOperRowStatus.setStatus('deprecated')
vrrpAssoIpAddrTable = MibTable((1, 3, 6, 1, 2, 1, 68, 1, 4), )
if mibBuilder.loadTexts: vrrpAssoIpAddrTable.setStatus('deprecated')
vrrpAssoIpAddrEntry = MibTableRow((1, 3, 6, 1, 2, 1, 68, 1, 4, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "VRRP-MIB", "vrrpOperVrId"), (0, "VRRP-MIB", "vrrpAssoIpAddr"))
if mibBuilder.loadTexts: vrrpAssoIpAddrEntry.setStatus('deprecated')
vrrpAssoIpAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 1, 4, 1, 1), IpAddress())
if mibBuilder.loadTexts: vrrpAssoIpAddr.setStatus('deprecated')
vrrpAssoIpAddrRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 1, 4, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vrrpAssoIpAddrRowStatus.setStatus('deprecated')
vrrpRouterStatsTable = MibTable((1, 3, 6, 1, 2, 1, 68, 2, 4), )
if mibBuilder.loadTexts: vrrpRouterStatsTable.setStatus('deprecated')
vrrpRouterStatsEntry = MibTableRow((1, 3, 6, 1, 2, 1, 68, 2, 4, 1), )
vrrpOperEntry.registerAugmentions(("VRRP-MIB", "vrrpRouterStatsEntry"))
vrrpRouterStatsEntry.setIndexNames(*vrrpOperEntry.getIndexNames())
if mibBuilder.loadTexts: vrrpRouterStatsEntry.setStatus('deprecated')
vrrpStatsBecomeMaster = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 2, 4, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpStatsBecomeMaster.setStatus('deprecated')
vrrpStatsAdvertiseRcvd = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 2, 4, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpStatsAdvertiseRcvd.setStatus('deprecated')
vrrpStatsAdvertiseIntervalErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 2, 4, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpStatsAdvertiseIntervalErrors.setStatus('deprecated')
vrrpStatsAuthFailures = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 2, 4, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpStatsAuthFailures.setStatus('deprecated')
vrrpStatsIpTtlErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 2, 4, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpStatsIpTtlErrors.setStatus('deprecated')
vrrpStatsPriorityZeroPktsRcvd = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 2, 4, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpStatsPriorityZeroPktsRcvd.setStatus('deprecated')
vrrpStatsPriorityZeroPktsSent = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 2, 4, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpStatsPriorityZeroPktsSent.setStatus('deprecated')
vrrpStatsInvalidTypePktsRcvd = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 2, 4, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpStatsInvalidTypePktsRcvd.setStatus('deprecated')
vrrpStatsAddressListErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 2, 4, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpStatsAddressListErrors.setStatus('deprecated')
vrrpStatsInvalidAuthType = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 2, 4, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpStatsInvalidAuthType.setStatus('deprecated')
vrrpStatsAuthTypeMismatch = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 2, 4, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpStatsAuthTypeMismatch.setStatus('deprecated')
vrrpStatsPacketLengthErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 2, 4, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpStatsPacketLengthErrors.setStatus('deprecated')
vrrpTrapPacketSrc = MibScalar((1, 3, 6, 1, 2, 1, 68, 1, 5), IpAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: vrrpTrapPacketSrc.setStatus('deprecated')
vrrpTrapAuthErrorType = MibScalar((1, 3, 6, 1, 2, 1, 68, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("invalidAuthType", 1), ("authTypeMismatch", 2), ("authFailure", 3)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: vrrpTrapAuthErrorType.setStatus('deprecated')
vrrpTrapAuthFailure = NotificationType((1, 3, 6, 1, 2, 1, 68, 0, 2)).setObjects(("VRRP-MIB", "vrrpTrapPacketSrc"), ("VRRP-MIB", "vrrpTrapAuthErrorType"))
if mibBuilder.loadTexts: vrrpTrapAuthFailure.setStatus('deprecated')
vrrpMIBCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 68, 3, 1))
vrrpMIBGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 68, 3, 2))
vrrpMIBCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 68, 3, 1, 1)).setObjects(("VRRP-MIB", "vrrpOperGroup"), ("VRRP-MIB", "vrrpStatsGroup"), ("VRRP-MIB", "vrrpTrapGroup"), ("VRRP-MIB", "vrrpNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vrrpMIBCompliance = vrrpMIBCompliance.setStatus('deprecated')
vrrpModuleFullCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 68, 3, 1, 2)).setObjects(("VRRP-MIB", "vrrpOperationsGroup"), ("VRRP-MIB", "vrrpStatisticsGroup"), ("VRRP-MIB", "vrrpTrapInfoGroup"), ("VRRP-MIB", "vrrpNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vrrpModuleFullCompliance = vrrpModuleFullCompliance.setStatus('current')
vrrpModuleReadOnlyCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 68, 3, 1, 3)).setObjects(("VRRP-MIB", "vrrpOperationsGroup"), ("VRRP-MIB", "vrrpStatisticsGroup"), ("VRRP-MIB", "vrrpTrapInfoGroup"), ("VRRP-MIB", "vrrpNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vrrpModuleReadOnlyCompliance = vrrpModuleReadOnlyCompliance.setStatus('current')
vrrpOperGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 68, 3, 2, 1)).setObjects(("VRRP-MIB", "vrrpNodeVersion"), ("VRRP-MIB", "vrrpNotificationCntl"), ("VRRP-MIB", "vrrpOperVirtualMacAddr"), ("VRRP-MIB", "vrrpOperState"), ("VRRP-MIB", "vrrpOperAdminState"), ("VRRP-MIB", "vrrpOperPriority"), ("VRRP-MIB", "vrrpOperIpAddrCount"), ("VRRP-MIB", "vrrpOperMasterIpAddr"), ("VRRP-MIB", "vrrpOperPrimaryIpAddr"), ("VRRP-MIB", "vrrpOperAuthType"), ("VRRP-MIB", "vrrpOperAuthKey"), ("VRRP-MIB", "vrrpOperAdvertisementInterval"), ("VRRP-MIB", "vrrpOperPreemptMode"), ("VRRP-MIB", "vrrpOperVirtualRouterUpTime"), ("VRRP-MIB", "vrrpOperProtocol"), ("VRRP-MIB", "vrrpOperRowStatus"), ("VRRP-MIB", "vrrpAssoIpAddrRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vrrpOperGroup = vrrpOperGroup.setStatus('deprecated')
vrrpStatsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 68, 3, 2, 2)).setObjects(("VRRP-MIB", "vrrpRouterChecksumErrors"), ("VRRP-MIB", "vrrpRouterVersionErrors"), ("VRRP-MIB", "vrrpRouterVrIdErrors"), ("VRRP-MIB", "vrrpStatsBecomeMaster"), ("VRRP-MIB", "vrrpStatsAdvertiseRcvd"), ("VRRP-MIB", "vrrpStatsAdvertiseIntervalErrors"), ("VRRP-MIB", "vrrpStatsAuthFailures"), ("VRRP-MIB", "vrrpStatsIpTtlErrors"), ("VRRP-MIB", "vrrpStatsPriorityZeroPktsRcvd"), ("VRRP-MIB", "vrrpStatsPriorityZeroPktsSent"), ("VRRP-MIB", "vrrpStatsInvalidTypePktsRcvd"), ("VRRP-MIB", "vrrpStatsAddressListErrors"), ("VRRP-MIB", "vrrpStatsInvalidAuthType"), ("VRRP-MIB", "vrrpStatsAuthTypeMismatch"), ("VRRP-MIB", "vrrpStatsPacketLengthErrors"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vrrpStatsGroup = vrrpStatsGroup.setStatus('deprecated')
vrrpTrapGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 68, 3, 2, 3)).setObjects(("VRRP-MIB", "vrrpTrapPacketSrc"), ("VRRP-MIB", "vrrpTrapAuthErrorType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vrrpTrapGroup = vrrpTrapGroup.setStatus('deprecated')
vrrpNotificationGroup = NotificationGroup((1, 3, 6, 1, 2, 1, 68, 3, 2, 4)).setObjects(("VRRP-MIB", "vrrpTrapNewMaster"), ("VRRP-MIB", "vrrpTrapAuthFailure"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vrrpNotificationGroup = vrrpNotificationGroup.setStatus('deprecated')
vrrpOperationsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 68, 3, 2, 5)).setObjects(("VRRP-MIB", "vrrpNotificationCntl"), ("VRRP-MIB", "vrrpOperationsVirtualMacAddr"), ("VRRP-MIB", "vrrpOperationsState"), ("VRRP-MIB", "vrrpOperationsPriority"), ("VRRP-MIB", "vrrpOperationsMasterIpAddr"), ("VRRP-MIB", "vrrpOperationsAdvInterval"), ("VRRP-MIB", "vrrpOperationsPreemptMode"), ("VRRP-MIB", "vrrpOperationsAcceptMode"), ("VRRP-MIB", "vrrpOperationsUpTime"), ("VRRP-MIB", "vrrpOperationsStorageType"), ("VRRP-MIB", "vrrpOperationsRowStatus"), ("VRRP-MIB", "vrrpOperationsAddrCount"), ("VRRP-MIB", "vrrpOperationsPrimaryIpAddr"), ("VRRP-MIB", "vrrpAssociatedStorageType"), ("VRRP-MIB", "vrrpAssociatedIpAddrRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vrrpOperationsGroup = vrrpOperationsGroup.setStatus('current')
vrrpStatisticsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 68, 3, 2, 6)).setObjects(("VRRP-MIB", "vrrpRouterChecksumErrors"), ("VRRP-MIB", "vrrpRouterVersionErrors"), ("VRRP-MIB", "vrrpRouterVrIdErrors"), ("VRRP-MIB", "vrrpStatisticsMasterTransitions"), ("VRRP-MIB", "vrrpStatisticsRcvdAdvertisements"), ("VRRP-MIB", "vrrpStatisticsAdvIntervalErrors"), ("VRRP-MIB", "vrrpStatisticsRcvdPriZeroPackets"), ("VRRP-MIB", "vrrpStatisticsSentPriZeroPackets"), ("VRRP-MIB", "vrrpStatisticsRcvdInvalidTypePkts"), ("VRRP-MIB", "vrrpStatisticsIpTtlErrors"), ("VRRP-MIB", "vrrpStatisticsAddressListErrors"), ("VRRP-MIB", "vrrpStatisticsPacketLengthErrors"), ("VRRP-MIB", "vrrpStatisticsRcvdInvalidAuthentications"), ("VRRP-MIB", "vrrpStatisticsDiscontinuityTime"), ("VRRP-MIB", "vrrpStatisticsRefreshRate"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vrrpStatisticsGroup = vrrpStatisticsGroup.setStatus('current')
vrrpTrapInfoGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 68, 3, 2, 7)).setObjects(("VRRP-MIB", "vrrpNewMasterReason"), ("VRRP-MIB", "vrrpTrapProtoErrReason"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vrrpTrapInfoGroup = vrrpTrapInfoGroup.setStatus('current')
vrrpNotificationsGroup = NotificationGroup((1, 3, 6, 1, 2, 1, 68, 3, 2, 8)).setObjects(("VRRP-MIB", "vrrpTrapNewMaster"), ("VRRP-MIB", "vrrpTrapProtoError"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vrrpNotificationsGroup = vrrpNotificationsGroup.setStatus('current')
mibBuilder.exportSymbols("VRRP-MIB", vrrpOperationsState=vrrpOperationsState, vrrpRouterVersionErrors=vrrpRouterVersionErrors, vrrpOperationsEntry=vrrpOperationsEntry, vrrpTrapNewMaster=vrrpTrapNewMaster, vrrpOperVrId=vrrpOperVrId, vrrpNotifications=vrrpNotifications, vrrpMIB=vrrpMIB, vrrpNewMasterReason=vrrpNewMasterReason, vrrpAssociatedStorageType=vrrpAssociatedStorageType, vrrpOperationsGroup=vrrpOperationsGroup, vrrpOperationsAcceptMode=vrrpOperationsAcceptMode, vrrpRouterVrIdErrors=vrrpRouterVrIdErrors, vrrpStatsInvalidTypePktsRcvd=vrrpStatsInvalidTypePktsRcvd, vrrpTrapAuthErrorType=vrrpTrapAuthErrorType, vrrpAssoIpAddrEntry=vrrpAssoIpAddrEntry, vrrpAssociatedIpAddrEntry=vrrpAssociatedIpAddrEntry, vrrpStatsBecomeMaster=vrrpStatsBecomeMaster, vrrpOperationsPrimaryIpAddr=vrrpOperationsPrimaryIpAddr, vrrpTrapInfoGroup=vrrpTrapInfoGroup, vrrpOperAuthType=vrrpOperAuthType, vrrpModuleFullCompliance=vrrpModuleFullCompliance, vrrpNotificationGroup=vrrpNotificationGroup, vrrpStatsAdvertiseRcvd=vrrpStatsAdvertiseRcvd, vrrpOperationsInetAddrType=vrrpOperationsInetAddrType, vrrpOperPrimaryIpAddr=vrrpOperPrimaryIpAddr, vrrpOperGroup=vrrpOperGroup, vrrpStatsIpTtlErrors=vrrpStatsIpTtlErrors, vrrpRouterStatisticsEntry=vrrpRouterStatisticsEntry, vrrpNodeVersion=vrrpNodeVersion, vrrpOperationsMasterIpAddr=vrrpOperationsMasterIpAddr, vrrpOperPreemptMode=vrrpOperPreemptMode, vrrpStatsPacketLengthErrors=vrrpStatsPacketLengthErrors, vrrpOperationsStorageType=vrrpOperationsStorageType, vrrpOperations=vrrpOperations, vrrpRouterStatsEntry=vrrpRouterStatsEntry, vrrpStatisticsPacketLengthErrors=vrrpStatisticsPacketLengthErrors, vrrpConformance=vrrpConformance, vrrpStatisticsRcvdInvalidAuthentications=vrrpStatisticsRcvdInvalidAuthentications, vrrpStatistics=vrrpStatistics, VrId=VrId, vrrpStatisticsDiscontinuityTime=vrrpStatisticsDiscontinuityTime, vrrpOperationsAdvInterval=vrrpOperationsAdvInterval, vrrpStatsPriorityZeroPktsRcvd=vrrpStatsPriorityZeroPktsRcvd, vrrpTrapGroup=vrrpTrapGroup, vrrpStatisticsAdvIntervalErrors=vrrpStatisticsAdvIntervalErrors, vrrpStatsPriorityZeroPktsSent=vrrpStatsPriorityZeroPktsSent, vrrpOperationsTable=vrrpOperationsTable, vrrpOperIpAddrCount=vrrpOperIpAddrCount, vrrpStatsAuthTypeMismatch=vrrpStatsAuthTypeMismatch, vrrpOperProtocol=vrrpOperProtocol, vrrpOperationsUpTime=vrrpOperationsUpTime, vrrpAssociatedIpAddrRowStatus=vrrpAssociatedIpAddrRowStatus, vrrpOperationsVirtualMacAddr=vrrpOperationsVirtualMacAddr, vrrpTrapPacketSrc=vrrpTrapPacketSrc, vrrpStatisticsRcvdAdvertisements=vrrpStatisticsRcvdAdvertisements, vrrpStatisticsMasterTransitions=vrrpStatisticsMasterTransitions, vrrpStatisticsRcvdInvalidTypePkts=vrrpStatisticsRcvdInvalidTypePkts, vrrpStatisticsGroup=vrrpStatisticsGroup, vrrpAssociatedIpAddrTable=vrrpAssociatedIpAddrTable, vrrpOperationsRowStatus=vrrpOperationsRowStatus, vrrpStatsAdvertiseIntervalErrors=vrrpStatsAdvertiseIntervalErrors, vrrpModuleReadOnlyCompliance=vrrpModuleReadOnlyCompliance, vrrpStatisticsRefreshRate=vrrpStatisticsRefreshRate, vrrpStatisticsAddressListErrors=vrrpStatisticsAddressListErrors, vrrpStatisticsRcvdPriZeroPackets=vrrpStatisticsRcvdPriZeroPackets, vrrpStatsAddressListErrors=vrrpStatsAddressListErrors, vrrpOperAdminState=vrrpOperAdminState, vrrpTrapProtoError=vrrpTrapProtoError, vrrpTrapAuthFailure=vrrpTrapAuthFailure, vrrpOperEntry=vrrpOperEntry, vrrpAssoIpAddrRowStatus=vrrpAssoIpAddrRowStatus, vrrpMIBCompliances=vrrpMIBCompliances, vrrpNotificationCntl=vrrpNotificationCntl, vrrpAssoIpAddr=vrrpAssoIpAddr, vrrpAssociatedIpAddr=vrrpAssociatedIpAddr, vrrpOperTable=vrrpOperTable, vrrpStatsAuthFailures=vrrpStatsAuthFailures, vrrpOperRowStatus=vrrpOperRowStatus, vrrpStatisticsIpTtlErrors=vrrpStatisticsIpTtlErrors, PYSNMP_MODULE_ID=vrrpMIB, vrrpMIBCompliance=vrrpMIBCompliance, vrrpOperationsPriority=vrrpOperationsPriority, vrrpOperMasterIpAddr=vrrpOperMasterIpAddr, vrrpOperVirtualRouterUpTime=vrrpOperVirtualRouterUpTime, vrrpStatisticsSentPriZeroPackets=vrrpStatisticsSentPriZeroPackets, vrrpOperAuthKey=vrrpOperAuthKey, vrrpStatsInvalidAuthType=vrrpStatsInvalidAuthType, vrrpOperationsAddrCount=vrrpOperationsAddrCount, vrrpOperationsPreemptMode=vrrpOperationsPreemptMode, vrrpOperPriority=vrrpOperPriority, vrrpOperVirtualMacAddr=vrrpOperVirtualMacAddr, vrrpAssoIpAddrTable=vrrpAssoIpAddrTable, vrrpRouterChecksumErrors=vrrpRouterChecksumErrors, vrrpTrapProtoErrReason=vrrpTrapProtoErrReason, vrrpNotificationsGroup=vrrpNotificationsGroup, vrrpOperState=vrrpOperState, vrrpRouterStatsTable=vrrpRouterStatsTable, vrrpRouterStatisticsTable=vrrpRouterStatisticsTable, vrrpMIBGroups=vrrpMIBGroups, vrrpStatsGroup=vrrpStatsGroup, vrrpOperAdvertisementInterval=vrrpOperAdvertisementInterval, vrrpOperationsVrId=vrrpOperationsVrId)
