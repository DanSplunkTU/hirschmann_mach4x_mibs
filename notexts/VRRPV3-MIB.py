#
# PySNMP MIB module VRRPV3-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/VRRPV3-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 15:51:05 2022
# On host fv-az135-792 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Counter64, NotificationType, Unsigned32, Gauge32, ObjectIdentity, Counter32, MibIdentifier, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, mib_2, Bits, IpAddress, iso, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "NotificationType", "Unsigned32", "Gauge32", "ObjectIdentity", "Counter32", "MibIdentifier", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "mib-2", "Bits", "IpAddress", "iso", "Integer32")
TimeInterval, TruthValue, DisplayString, TextualConvention, RowStatus, TimeStamp, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "TimeInterval", "TruthValue", "DisplayString", "TextualConvention", "RowStatus", "TimeStamp", "MacAddress")
vrrpv3MIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 207))
vrrpv3MIB.setRevisions(('2012-02-12 00:00',))
if mibBuilder.loadTexts: vrrpv3MIB.setLastUpdated('201202130000Z')
if mibBuilder.loadTexts: vrrpv3MIB.setOrganization('IETF VRRP Working Group')
class Vrrpv3VrIdTC(TextualConvention, Integer32):
    reference = 'RFC 5798 (Sections 3 and 5.2.3)'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 255)

vrrpv3Notifications = MibIdentifier((1, 3, 6, 1, 2, 1, 207, 0))
vrrpv3Objects = MibIdentifier((1, 3, 6, 1, 2, 1, 207, 1))
vrrpv3Conformance = MibIdentifier((1, 3, 6, 1, 2, 1, 207, 2))
vrrpv3Operations = MibIdentifier((1, 3, 6, 1, 2, 1, 207, 1, 1))
vrrpv3Statistics = MibIdentifier((1, 3, 6, 1, 2, 1, 207, 1, 2))
vrrpv3OperationsTable = MibTable((1, 3, 6, 1, 2, 1, 207, 1, 1, 1), )
if mibBuilder.loadTexts: vrrpv3OperationsTable.setStatus('current')
vrrpv3OperationsEntry = MibTableRow((1, 3, 6, 1, 2, 1, 207, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "VRRPV3-MIB", "vrrpv3OperationsVrId"), (0, "VRRPV3-MIB", "vrrpv3OperationsInetAddrType"))
if mibBuilder.loadTexts: vrrpv3OperationsEntry.setStatus('current')
vrrpv3OperationsVrId = MibTableColumn((1, 3, 6, 1, 2, 1, 207, 1, 1, 1, 1, 1), Vrrpv3VrIdTC())
if mibBuilder.loadTexts: vrrpv3OperationsVrId.setStatus('current')
vrrpv3OperationsInetAddrType = MibTableColumn((1, 3, 6, 1, 2, 1, 207, 1, 1, 1, 1, 2), InetAddressType())
if mibBuilder.loadTexts: vrrpv3OperationsInetAddrType.setStatus('current')
vrrpv3OperationsMasterIpAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 207, 1, 1, 1, 1, 3), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpv3OperationsMasterIpAddr.setStatus('current')
vrrpv3OperationsPrimaryIpAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 207, 1, 1, 1, 1, 4), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vrrpv3OperationsPrimaryIpAddr.setStatus('current')
vrrpv3OperationsVirtualMacAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 207, 1, 1, 1, 1, 5), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpv3OperationsVirtualMacAddr.setStatus('current')
vrrpv3OperationsStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 207, 1, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("initialize", 1), ("backup", 2), ("master", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpv3OperationsStatus.setStatus('current')
vrrpv3OperationsPriority = MibTableColumn((1, 3, 6, 1, 2, 1, 207, 1, 1, 1, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)).clone(100)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vrrpv3OperationsPriority.setStatus('current')
vrrpv3OperationsAddrCount = MibTableColumn((1, 3, 6, 1, 2, 1, 207, 1, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpv3OperationsAddrCount.setStatus('current')
vrrpv3OperationsAdvInterval = MibTableColumn((1, 3, 6, 1, 2, 1, 207, 1, 1, 1, 1, 9), TimeInterval().subtype(subtypeSpec=ValueRangeConstraint(1, 4095)).clone(100)).setUnits('centiseconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: vrrpv3OperationsAdvInterval.setStatus('current')
vrrpv3OperationsPreemptMode = MibTableColumn((1, 3, 6, 1, 2, 1, 207, 1, 1, 1, 1, 10), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vrrpv3OperationsPreemptMode.setStatus('current')
vrrpv3OperationsAcceptMode = MibTableColumn((1, 3, 6, 1, 2, 1, 207, 1, 1, 1, 1, 11), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vrrpv3OperationsAcceptMode.setStatus('current')
vrrpv3OperationsUpTime = MibTableColumn((1, 3, 6, 1, 2, 1, 207, 1, 1, 1, 1, 12), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpv3OperationsUpTime.setStatus('current')
vrrpv3OperationsRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 207, 1, 1, 1, 1, 13), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vrrpv3OperationsRowStatus.setStatus('current')
vrrpv3AssociatedIpAddrTable = MibTable((1, 3, 6, 1, 2, 1, 207, 1, 1, 2), )
if mibBuilder.loadTexts: vrrpv3AssociatedIpAddrTable.setStatus('current')
vrrpv3AssociatedIpAddrEntry = MibTableRow((1, 3, 6, 1, 2, 1, 207, 1, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "VRRPV3-MIB", "vrrpv3OperationsVrId"), (0, "VRRPV3-MIB", "vrrpv3OperationsInetAddrType"), (0, "VRRPV3-MIB", "vrrpv3AssociatedIpAddrAddress"))
if mibBuilder.loadTexts: vrrpv3AssociatedIpAddrEntry.setStatus('current')
vrrpv3AssociatedIpAddrAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 207, 1, 1, 2, 1, 1), InetAddress().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(4, 4), ValueSizeConstraint(16, 16), )))
if mibBuilder.loadTexts: vrrpv3AssociatedIpAddrAddress.setStatus('current')
vrrpv3AssociatedIpAddrRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 207, 1, 1, 2, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vrrpv3AssociatedIpAddrRowStatus.setStatus('current')
vrrpv3RouterChecksumErrors = MibScalar((1, 3, 6, 1, 2, 1, 207, 1, 2, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpv3RouterChecksumErrors.setStatus('current')
vrrpv3RouterVersionErrors = MibScalar((1, 3, 6, 1, 2, 1, 207, 1, 2, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpv3RouterVersionErrors.setStatus('current')
vrrpv3RouterVrIdErrors = MibScalar((1, 3, 6, 1, 2, 1, 207, 1, 2, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpv3RouterVrIdErrors.setStatus('current')
vrrpv3GlobalStatisticsDiscontinuityTime = MibScalar((1, 3, 6, 1, 2, 1, 207, 1, 2, 4), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpv3GlobalStatisticsDiscontinuityTime.setStatus('current')
vrrpv3StatisticsTable = MibTable((1, 3, 6, 1, 2, 1, 207, 1, 2, 5), )
if mibBuilder.loadTexts: vrrpv3StatisticsTable.setStatus('current')
vrrpv3StatisticsEntry = MibTableRow((1, 3, 6, 1, 2, 1, 207, 1, 2, 5, 1), )
vrrpv3OperationsEntry.registerAugmentions(("VRRPV3-MIB", "vrrpv3StatisticsEntry"))
vrrpv3StatisticsEntry.setIndexNames(*vrrpv3OperationsEntry.getIndexNames())
if mibBuilder.loadTexts: vrrpv3StatisticsEntry.setStatus('current')
vrrpv3StatisticsMasterTransitions = MibTableColumn((1, 3, 6, 1, 2, 1, 207, 1, 2, 5, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpv3StatisticsMasterTransitions.setStatus('current')
vrrpv3StatisticsNewMasterReason = MibTableColumn((1, 3, 6, 1, 2, 1, 207, 1, 2, 5, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("notMaster", 0), ("priority", 1), ("preempted", 2), ("masterNoResponse", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpv3StatisticsNewMasterReason.setStatus('current')
vrrpv3StatisticsRcvdAdvertisements = MibTableColumn((1, 3, 6, 1, 2, 1, 207, 1, 2, 5, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpv3StatisticsRcvdAdvertisements.setStatus('current')
vrrpv3StatisticsAdvIntervalErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 207, 1, 2, 5, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpv3StatisticsAdvIntervalErrors.setStatus('current')
vrrpv3StatisticsIpTtlErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 207, 1, 2, 5, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpv3StatisticsIpTtlErrors.setStatus('current')
vrrpv3StatisticsProtoErrReason = MibTableColumn((1, 3, 6, 1, 2, 1, 207, 1, 2, 5, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("noError", 0), ("ipTtlError", 1), ("versionError", 2), ("checksumError", 3), ("vrIdError", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpv3StatisticsProtoErrReason.setStatus('current')
vrrpv3StatisticsRcvdPriZeroPackets = MibTableColumn((1, 3, 6, 1, 2, 1, 207, 1, 2, 5, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpv3StatisticsRcvdPriZeroPackets.setStatus('current')
vrrpv3StatisticsSentPriZeroPackets = MibTableColumn((1, 3, 6, 1, 2, 1, 207, 1, 2, 5, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpv3StatisticsSentPriZeroPackets.setStatus('current')
vrrpv3StatisticsRcvdInvalidTypePackets = MibTableColumn((1, 3, 6, 1, 2, 1, 207, 1, 2, 5, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpv3StatisticsRcvdInvalidTypePackets.setStatus('current')
vrrpv3StatisticsAddressListErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 207, 1, 2, 5, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpv3StatisticsAddressListErrors.setStatus('current')
vrrpv3StatisticsPacketLengthErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 207, 1, 2, 5, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpv3StatisticsPacketLengthErrors.setStatus('current')
vrrpv3StatisticsRowDiscontinuityTime = MibTableColumn((1, 3, 6, 1, 2, 1, 207, 1, 2, 5, 1, 12), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpv3StatisticsRowDiscontinuityTime.setStatus('current')
vrrpv3StatisticsRefreshRate = MibTableColumn((1, 3, 6, 1, 2, 1, 207, 1, 2, 5, 1, 13), Unsigned32()).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpv3StatisticsRefreshRate.setStatus('current')
vrrpv3NewMaster = NotificationType((1, 3, 6, 1, 2, 1, 207, 0, 1)).setObjects(("VRRPV3-MIB", "vrrpv3OperationsMasterIpAddr"), ("VRRPV3-MIB", "vrrpv3StatisticsNewMasterReason"))
if mibBuilder.loadTexts: vrrpv3NewMaster.setStatus('current')
vrrpv3ProtoError = NotificationType((1, 3, 6, 1, 2, 1, 207, 0, 2)).setObjects(("VRRPV3-MIB", "vrrpv3StatisticsProtoErrReason"))
if mibBuilder.loadTexts: vrrpv3ProtoError.setStatus('current')
vrrpv3Compliances = MibIdentifier((1, 3, 6, 1, 2, 1, 207, 2, 1))
vrrpv3Groups = MibIdentifier((1, 3, 6, 1, 2, 1, 207, 2, 2))
vrrpv3FullCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 207, 2, 1, 1)).setObjects(("VRRPV3-MIB", "vrrpv3OperationsGroup"), ("VRRPV3-MIB", "vrrpv3StatisticsGroup"), ("VRRPV3-MIB", "vrrpv3InfoGroup"), ("VRRPV3-MIB", "vrrpv3NotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vrrpv3FullCompliance = vrrpv3FullCompliance.setStatus('current')
vrrpv3ReadOnlyCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 207, 2, 1, 2)).setObjects(("VRRPV3-MIB", "vrrpv3OperationsGroup"), ("VRRPV3-MIB", "vrrpv3StatisticsGroup"), ("VRRPV3-MIB", "vrrpv3StatisticsDiscontinuityGroup"), ("VRRPV3-MIB", "vrrpv3InfoGroup"), ("VRRPV3-MIB", "vrrpv3NotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vrrpv3ReadOnlyCompliance = vrrpv3ReadOnlyCompliance.setStatus('current')
vrrpv3OperationsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 207, 2, 2, 1)).setObjects(("VRRPV3-MIB", "vrrpv3OperationsVirtualMacAddr"), ("VRRPV3-MIB", "vrrpv3OperationsStatus"), ("VRRPV3-MIB", "vrrpv3OperationsPriority"), ("VRRPV3-MIB", "vrrpv3OperationsMasterIpAddr"), ("VRRPV3-MIB", "vrrpv3OperationsAdvInterval"), ("VRRPV3-MIB", "vrrpv3OperationsPreemptMode"), ("VRRPV3-MIB", "vrrpv3OperationsAcceptMode"), ("VRRPV3-MIB", "vrrpv3OperationsUpTime"), ("VRRPV3-MIB", "vrrpv3OperationsRowStatus"), ("VRRPV3-MIB", "vrrpv3OperationsAddrCount"), ("VRRPV3-MIB", "vrrpv3OperationsPrimaryIpAddr"), ("VRRPV3-MIB", "vrrpv3AssociatedIpAddrRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vrrpv3OperationsGroup = vrrpv3OperationsGroup.setStatus('current')
vrrpv3StatisticsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 207, 2, 2, 2)).setObjects(("VRRPV3-MIB", "vrrpv3RouterChecksumErrors"), ("VRRPV3-MIB", "vrrpv3RouterVersionErrors"), ("VRRPV3-MIB", "vrrpv3RouterVrIdErrors"), ("VRRPV3-MIB", "vrrpv3StatisticsMasterTransitions"), ("VRRPV3-MIB", "vrrpv3StatisticsNewMasterReason"), ("VRRPV3-MIB", "vrrpv3StatisticsRcvdAdvertisements"), ("VRRPV3-MIB", "vrrpv3StatisticsAdvIntervalErrors"), ("VRRPV3-MIB", "vrrpv3StatisticsRcvdPriZeroPackets"), ("VRRPV3-MIB", "vrrpv3StatisticsSentPriZeroPackets"), ("VRRPV3-MIB", "vrrpv3StatisticsRcvdInvalidTypePackets"), ("VRRPV3-MIB", "vrrpv3StatisticsIpTtlErrors"), ("VRRPV3-MIB", "vrrpv3StatisticsProtoErrReason"), ("VRRPV3-MIB", "vrrpv3StatisticsAddressListErrors"), ("VRRPV3-MIB", "vrrpv3StatisticsPacketLengthErrors"), ("VRRPV3-MIB", "vrrpv3StatisticsRowDiscontinuityTime"), ("VRRPV3-MIB", "vrrpv3StatisticsRefreshRate"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vrrpv3StatisticsGroup = vrrpv3StatisticsGroup.setStatus('current')
vrrpv3StatisticsDiscontinuityGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 207, 2, 2, 3)).setObjects(("VRRPV3-MIB", "vrrpv3GlobalStatisticsDiscontinuityTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vrrpv3StatisticsDiscontinuityGroup = vrrpv3StatisticsDiscontinuityGroup.setStatus('current')
vrrpv3InfoGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 207, 2, 2, 4)).setObjects(("VRRPV3-MIB", "vrrpv3StatisticsProtoErrReason"), ("VRRPV3-MIB", "vrrpv3StatisticsNewMasterReason"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vrrpv3InfoGroup = vrrpv3InfoGroup.setStatus('current')
vrrpv3NotificationsGroup = NotificationGroup((1, 3, 6, 1, 2, 1, 207, 2, 2, 5)).setObjects(("VRRPV3-MIB", "vrrpv3NewMaster"), ("VRRPV3-MIB", "vrrpv3ProtoError"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vrrpv3NotificationsGroup = vrrpv3NotificationsGroup.setStatus('current')
mibBuilder.exportSymbols("VRRPV3-MIB", vrrpv3Groups=vrrpv3Groups, vrrpv3OperationsTable=vrrpv3OperationsTable, vrrpv3Conformance=vrrpv3Conformance, vrrpv3OperationsEntry=vrrpv3OperationsEntry, vrrpv3AssociatedIpAddrRowStatus=vrrpv3AssociatedIpAddrRowStatus, Vrrpv3VrIdTC=Vrrpv3VrIdTC, vrrpv3StatisticsRefreshRate=vrrpv3StatisticsRefreshRate, vrrpv3OperationsVrId=vrrpv3OperationsVrId, vrrpv3StatisticsProtoErrReason=vrrpv3StatisticsProtoErrReason, vrrpv3StatisticsDiscontinuityGroup=vrrpv3StatisticsDiscontinuityGroup, vrrpv3StatisticsEntry=vrrpv3StatisticsEntry, vrrpv3OperationsPriority=vrrpv3OperationsPriority, vrrpv3RouterVrIdErrors=vrrpv3RouterVrIdErrors, vrrpv3Objects=vrrpv3Objects, vrrpv3Notifications=vrrpv3Notifications, vrrpv3OperationsUpTime=vrrpv3OperationsUpTime, vrrpv3NotificationsGroup=vrrpv3NotificationsGroup, vrrpv3OperationsAddrCount=vrrpv3OperationsAddrCount, vrrpv3StatisticsSentPriZeroPackets=vrrpv3StatisticsSentPriZeroPackets, vrrpv3StatisticsNewMasterReason=vrrpv3StatisticsNewMasterReason, vrrpv3AssociatedIpAddrAddress=vrrpv3AssociatedIpAddrAddress, vrrpv3FullCompliance=vrrpv3FullCompliance, vrrpv3AssociatedIpAddrTable=vrrpv3AssociatedIpAddrTable, vrrpv3StatisticsMasterTransitions=vrrpv3StatisticsMasterTransitions, vrrpv3StatisticsRcvdAdvertisements=vrrpv3StatisticsRcvdAdvertisements, vrrpv3OperationsPreemptMode=vrrpv3OperationsPreemptMode, vrrpv3OperationsStatus=vrrpv3OperationsStatus, vrrpv3Operations=vrrpv3Operations, vrrpv3OperationsPrimaryIpAddr=vrrpv3OperationsPrimaryIpAddr, vrrpv3StatisticsIpTtlErrors=vrrpv3StatisticsIpTtlErrors, vrrpv3NewMaster=vrrpv3NewMaster, vrrpv3StatisticsPacketLengthErrors=vrrpv3StatisticsPacketLengthErrors, vrrpv3Statistics=vrrpv3Statistics, vrrpv3OperationsAdvInterval=vrrpv3OperationsAdvInterval, vrrpv3OperationsGroup=vrrpv3OperationsGroup, vrrpv3RouterVersionErrors=vrrpv3RouterVersionErrors, PYSNMP_MODULE_ID=vrrpv3MIB, vrrpv3AssociatedIpAddrEntry=vrrpv3AssociatedIpAddrEntry, vrrpv3ProtoError=vrrpv3ProtoError, vrrpv3OperationsAcceptMode=vrrpv3OperationsAcceptMode, vrrpv3StatisticsAdvIntervalErrors=vrrpv3StatisticsAdvIntervalErrors, vrrpv3StatisticsGroup=vrrpv3StatisticsGroup, vrrpv3StatisticsTable=vrrpv3StatisticsTable, vrrpv3OperationsVirtualMacAddr=vrrpv3OperationsVirtualMacAddr, vrrpv3OperationsInetAddrType=vrrpv3OperationsInetAddrType, vrrpv3StatisticsRcvdInvalidTypePackets=vrrpv3StatisticsRcvdInvalidTypePackets, vrrpv3RouterChecksumErrors=vrrpv3RouterChecksumErrors, vrrpv3GlobalStatisticsDiscontinuityTime=vrrpv3GlobalStatisticsDiscontinuityTime, vrrpv3StatisticsAddressListErrors=vrrpv3StatisticsAddressListErrors, vrrpv3InfoGroup=vrrpv3InfoGroup, vrrpv3ReadOnlyCompliance=vrrpv3ReadOnlyCompliance, vrrpv3MIB=vrrpv3MIB, vrrpv3StatisticsRcvdPriZeroPackets=vrrpv3StatisticsRcvdPriZeroPackets, vrrpv3OperationsRowStatus=vrrpv3OperationsRowStatus, vrrpv3Compliances=vrrpv3Compliances, vrrpv3StatisticsRowDiscontinuityTime=vrrpv3StatisticsRowDiscontinuityTime, vrrpv3OperationsMasterIpAddr=vrrpv3OperationsMasterIpAddr)
