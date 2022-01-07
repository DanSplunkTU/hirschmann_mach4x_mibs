#
# PySNMP MIB module VRRP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/VRRP-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:07:39 2022
# On host fv-az36-988 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
MibIdentifier, ObjectIdentity, ModuleIdentity, iso, Unsigned32, TimeTicks, Gauge32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, mib_2, Bits, NotificationType, IpAddress, Counter64, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "ObjectIdentity", "ModuleIdentity", "iso", "Unsigned32", "TimeTicks", "Gauge32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "mib-2", "Bits", "NotificationType", "IpAddress", "Counter64", "Counter32")
MacAddress, RowStatus, TimeStamp, TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "RowStatus", "TimeStamp", "TruthValue", "DisplayString", "TextualConvention")
vrrpMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 68))
vrrpMIB.setRevisions(('2000-03-03 00:00',))
if mibBuilder.loadTexts: vrrpMIB.setLastUpdated('200003030000Z')
if mibBuilder.loadTexts: vrrpMIB.setOrganization('IETF VRRP Working Group')
class VrId(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 255)

vrrpOperations = MibIdentifier((1, 3, 6, 1, 2, 1, 68, 1))
vrrpStatistics = MibIdentifier((1, 3, 6, 1, 2, 1, 68, 2))
vrrpConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 68, 3))
vrrpNodeVersion = MibScalar((1, 3, 6, 1, 2, 1, 68, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpNodeVersion.setStatus('current')
vrrpNotificationCntl = MibScalar((1, 3, 6, 1, 2, 1, 68, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vrrpNotificationCntl.setStatus('current')
vrrpOperTable = MibTable((1, 3, 6, 1, 2, 1, 68, 1, 3), )
if mibBuilder.loadTexts: vrrpOperTable.setStatus('current')
vrrpOperEntry = MibTableRow((1, 3, 6, 1, 2, 1, 68, 1, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "VRRP-MIB", "vrrpOperVrId"))
if mibBuilder.loadTexts: vrrpOperEntry.setStatus('current')
vrrpOperVrId = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 1, 3, 1, 1), VrId())
if mibBuilder.loadTexts: vrrpOperVrId.setStatus('current')
vrrpOperVirtualMacAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 1, 3, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpOperVirtualMacAddr.setStatus('current')
vrrpOperState = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("initialize", 1), ("backup", 2), ("master", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpOperState.setStatus('current')
vrrpOperAdminState = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 1, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2))).clone('down')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vrrpOperAdminState.setStatus('current')
vrrpOperPriority = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 1, 3, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)).clone(100)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vrrpOperPriority.setStatus('current')
vrrpOperIpAddrCount = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 1, 3, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpOperIpAddrCount.setStatus('current')
vrrpOperMasterIpAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 1, 3, 1, 7), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpOperMasterIpAddr.setStatus('current')
vrrpOperPrimaryIpAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 1, 3, 1, 8), IpAddress().clone(hexValue="00000000")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vrrpOperPrimaryIpAddr.setStatus('current')
vrrpOperAuthType = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 1, 3, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAuthentication", 1), ("simpleTextPassword", 2), ("ipAuthenticationHeader", 3))).clone('noAuthentication')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vrrpOperAuthType.setStatus('current')
vrrpOperAuthKey = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 1, 3, 1, 10), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vrrpOperAuthKey.setStatus('current')
vrrpOperAdvertisementInterval = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 1, 3, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)).clone(1)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: vrrpOperAdvertisementInterval.setStatus('current')
vrrpOperPreemptMode = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 1, 3, 1, 12), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vrrpOperPreemptMode.setStatus('current')
vrrpOperVirtualRouterUpTime = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 1, 3, 1, 13), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpOperVirtualRouterUpTime.setStatus('current')
vrrpOperProtocol = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 1, 3, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("ip", 1), ("bridge", 2), ("decnet", 3), ("other", 4))).clone('ip')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vrrpOperProtocol.setStatus('current')
vrrpOperRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 1, 3, 1, 15), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vrrpOperRowStatus.setStatus('current')
vrrpAssoIpAddrTable = MibTable((1, 3, 6, 1, 2, 1, 68, 1, 4), )
if mibBuilder.loadTexts: vrrpAssoIpAddrTable.setStatus('current')
vrrpAssoIpAddrEntry = MibTableRow((1, 3, 6, 1, 2, 1, 68, 1, 4, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "VRRP-MIB", "vrrpOperVrId"), (0, "VRRP-MIB", "vrrpAssoIpAddr"))
if mibBuilder.loadTexts: vrrpAssoIpAddrEntry.setStatus('current')
vrrpAssoIpAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 1, 4, 1, 1), IpAddress())
if mibBuilder.loadTexts: vrrpAssoIpAddr.setStatus('current')
vrrpAssoIpAddrRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 1, 4, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vrrpAssoIpAddrRowStatus.setStatus('current')
vrrpRouterChecksumErrors = MibScalar((1, 3, 6, 1, 2, 1, 68, 2, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpRouterChecksumErrors.setStatus('current')
vrrpRouterVersionErrors = MibScalar((1, 3, 6, 1, 2, 1, 68, 2, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpRouterVersionErrors.setStatus('current')
vrrpRouterVrIdErrors = MibScalar((1, 3, 6, 1, 2, 1, 68, 2, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpRouterVrIdErrors.setStatus('current')
vrrpRouterStatsTable = MibTable((1, 3, 6, 1, 2, 1, 68, 2, 4), )
if mibBuilder.loadTexts: vrrpRouterStatsTable.setStatus('current')
vrrpRouterStatsEntry = MibTableRow((1, 3, 6, 1, 2, 1, 68, 2, 4, 1), )
vrrpOperEntry.registerAugmentions(("VRRP-MIB", "vrrpRouterStatsEntry"))
vrrpRouterStatsEntry.setIndexNames(*vrrpOperEntry.getIndexNames())
if mibBuilder.loadTexts: vrrpRouterStatsEntry.setStatus('current')
vrrpStatsBecomeMaster = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 2, 4, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpStatsBecomeMaster.setStatus('current')
vrrpStatsAdvertiseRcvd = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 2, 4, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpStatsAdvertiseRcvd.setStatus('current')
vrrpStatsAdvertiseIntervalErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 2, 4, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpStatsAdvertiseIntervalErrors.setStatus('current')
vrrpStatsAuthFailures = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 2, 4, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpStatsAuthFailures.setStatus('current')
vrrpStatsIpTtlErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 2, 4, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpStatsIpTtlErrors.setStatus('current')
vrrpStatsPriorityZeroPktsRcvd = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 2, 4, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpStatsPriorityZeroPktsRcvd.setStatus('current')
vrrpStatsPriorityZeroPktsSent = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 2, 4, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpStatsPriorityZeroPktsSent.setStatus('current')
vrrpStatsInvalidTypePktsRcvd = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 2, 4, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpStatsInvalidTypePktsRcvd.setStatus('current')
vrrpStatsAddressListErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 2, 4, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpStatsAddressListErrors.setStatus('current')
vrrpStatsInvalidAuthType = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 2, 4, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpStatsInvalidAuthType.setStatus('current')
vrrpStatsAuthTypeMismatch = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 2, 4, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpStatsAuthTypeMismatch.setStatus('current')
vrrpStatsPacketLengthErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 2, 4, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpStatsPacketLengthErrors.setStatus('current')
vrrpNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 68, 0))
vrrpTrapPacketSrc = MibScalar((1, 3, 6, 1, 2, 1, 68, 1, 5), IpAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: vrrpTrapPacketSrc.setStatus('current')
vrrpTrapAuthErrorType = MibScalar((1, 3, 6, 1, 2, 1, 68, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("invalidAuthType", 1), ("authTypeMismatch", 2), ("authFailure", 3)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: vrrpTrapAuthErrorType.setStatus('current')
vrrpTrapNewMaster = NotificationType((1, 3, 6, 1, 2, 1, 68, 0, 1)).setObjects(("VRRP-MIB", "vrrpOperMasterIpAddr"))
if mibBuilder.loadTexts: vrrpTrapNewMaster.setStatus('current')
vrrpTrapAuthFailure = NotificationType((1, 3, 6, 1, 2, 1, 68, 0, 2)).setObjects(("VRRP-MIB", "vrrpTrapPacketSrc"), ("VRRP-MIB", "vrrpTrapAuthErrorType"))
if mibBuilder.loadTexts: vrrpTrapAuthFailure.setStatus('current')
vrrpMIBCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 68, 3, 1))
vrrpMIBGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 68, 3, 2))
vrrpMIBCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 68, 3, 1, 1)).setObjects(("VRRP-MIB", "vrrpOperGroup"), ("VRRP-MIB", "vrrpStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vrrpMIBCompliance = vrrpMIBCompliance.setStatus('current')
vrrpOperGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 68, 3, 2, 1)).setObjects(("VRRP-MIB", "vrrpNodeVersion"), ("VRRP-MIB", "vrrpNotificationCntl"), ("VRRP-MIB", "vrrpOperVirtualMacAddr"), ("VRRP-MIB", "vrrpOperState"), ("VRRP-MIB", "vrrpOperAdminState"), ("VRRP-MIB", "vrrpOperPriority"), ("VRRP-MIB", "vrrpOperIpAddrCount"), ("VRRP-MIB", "vrrpOperMasterIpAddr"), ("VRRP-MIB", "vrrpOperPrimaryIpAddr"), ("VRRP-MIB", "vrrpOperAuthType"), ("VRRP-MIB", "vrrpOperAuthKey"), ("VRRP-MIB", "vrrpOperAdvertisementInterval"), ("VRRP-MIB", "vrrpOperPreemptMode"), ("VRRP-MIB", "vrrpOperVirtualRouterUpTime"), ("VRRP-MIB", "vrrpOperProtocol"), ("VRRP-MIB", "vrrpOperRowStatus"), ("VRRP-MIB", "vrrpAssoIpAddrRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vrrpOperGroup = vrrpOperGroup.setStatus('current')
vrrpStatsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 68, 3, 2, 2)).setObjects(("VRRP-MIB", "vrrpRouterChecksumErrors"), ("VRRP-MIB", "vrrpRouterVersionErrors"), ("VRRP-MIB", "vrrpRouterVrIdErrors"), ("VRRP-MIB", "vrrpStatsBecomeMaster"), ("VRRP-MIB", "vrrpStatsAdvertiseRcvd"), ("VRRP-MIB", "vrrpStatsAdvertiseIntervalErrors"), ("VRRP-MIB", "vrrpStatsAuthFailures"), ("VRRP-MIB", "vrrpStatsIpTtlErrors"), ("VRRP-MIB", "vrrpStatsPriorityZeroPktsRcvd"), ("VRRP-MIB", "vrrpStatsPriorityZeroPktsSent"), ("VRRP-MIB", "vrrpStatsInvalidTypePktsRcvd"), ("VRRP-MIB", "vrrpStatsAddressListErrors"), ("VRRP-MIB", "vrrpStatsInvalidAuthType"), ("VRRP-MIB", "vrrpStatsAuthTypeMismatch"), ("VRRP-MIB", "vrrpStatsPacketLengthErrors"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vrrpStatsGroup = vrrpStatsGroup.setStatus('current')
vrrpTrapGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 68, 3, 2, 3)).setObjects(("VRRP-MIB", "vrrpTrapPacketSrc"), ("VRRP-MIB", "vrrpTrapAuthErrorType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vrrpTrapGroup = vrrpTrapGroup.setStatus('current')
vrrpNotificationGroup = NotificationGroup((1, 3, 6, 1, 2, 1, 68, 3, 2, 4)).setObjects(("VRRP-MIB", "vrrpTrapNewMaster"), ("VRRP-MIB", "vrrpTrapAuthFailure"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vrrpNotificationGroup = vrrpNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("VRRP-MIB", vrrpOperTable=vrrpOperTable, vrrpNotificationGroup=vrrpNotificationGroup, vrrpConformance=vrrpConformance, vrrpStatsAuthTypeMismatch=vrrpStatsAuthTypeMismatch, vrrpOperAdminState=vrrpOperAdminState, vrrpMIB=vrrpMIB, vrrpOperIpAddrCount=vrrpOperIpAddrCount, vrrpOperAdvertisementInterval=vrrpOperAdvertisementInterval, vrrpStatsBecomeMaster=vrrpStatsBecomeMaster, vrrpMIBGroups=vrrpMIBGroups, vrrpStatsAdvertiseIntervalErrors=vrrpStatsAdvertiseIntervalErrors, vrrpStatsIpTtlErrors=vrrpStatsIpTtlErrors, vrrpNotificationCntl=vrrpNotificationCntl, vrrpStatsAdvertiseRcvd=vrrpStatsAdvertiseRcvd, vrrpRouterStatsTable=vrrpRouterStatsTable, vrrpStatsPriorityZeroPktsRcvd=vrrpStatsPriorityZeroPktsRcvd, vrrpOperations=vrrpOperations, vrrpRouterStatsEntry=vrrpRouterStatsEntry, vrrpStatsGroup=vrrpStatsGroup, vrrpRouterChecksumErrors=vrrpRouterChecksumErrors, PYSNMP_MODULE_ID=vrrpMIB, vrrpOperEntry=vrrpOperEntry, vrrpOperAuthKey=vrrpOperAuthKey, vrrpOperState=vrrpOperState, vrrpOperPreemptMode=vrrpOperPreemptMode, vrrpOperPrimaryIpAddr=vrrpOperPrimaryIpAddr, vrrpAssoIpAddrEntry=vrrpAssoIpAddrEntry, vrrpMIBCompliances=vrrpMIBCompliances, vrrpOperAuthType=vrrpOperAuthType, vrrpStatsAuthFailures=vrrpStatsAuthFailures, vrrpTrapPacketSrc=vrrpTrapPacketSrc, vrrpMIBCompliance=vrrpMIBCompliance, vrrpOperPriority=vrrpOperPriority, vrrpOperVirtualRouterUpTime=vrrpOperVirtualRouterUpTime, vrrpAssoIpAddr=vrrpAssoIpAddr, vrrpTrapAuthErrorType=vrrpTrapAuthErrorType, vrrpTrapNewMaster=vrrpTrapNewMaster, vrrpStatsPacketLengthErrors=vrrpStatsPacketLengthErrors, vrrpStatsInvalidAuthType=vrrpStatsInvalidAuthType, vrrpTrapAuthFailure=vrrpTrapAuthFailure, vrrpRouterVrIdErrors=vrrpRouterVrIdErrors, vrrpOperVirtualMacAddr=vrrpOperVirtualMacAddr, vrrpRouterVersionErrors=vrrpRouterVersionErrors, vrrpOperProtocol=vrrpOperProtocol, vrrpOperMasterIpAddr=vrrpOperMasterIpAddr, vrrpAssoIpAddrTable=vrrpAssoIpAddrTable, vrrpOperRowStatus=vrrpOperRowStatus, vrrpNodeVersion=vrrpNodeVersion, vrrpNotifications=vrrpNotifications, vrrpStatistics=vrrpStatistics, vrrpOperGroup=vrrpOperGroup, VrId=VrId, vrrpStatsInvalidTypePktsRcvd=vrrpStatsInvalidTypePktsRcvd, vrrpOperVrId=vrrpOperVrId, vrrpAssoIpAddrRowStatus=vrrpAssoIpAddrRowStatus, vrrpStatsAddressListErrors=vrrpStatsAddressListErrors, vrrpTrapGroup=vrrpTrapGroup, vrrpStatsPriorityZeroPktsSent=vrrpStatsPriorityZeroPktsSent)
