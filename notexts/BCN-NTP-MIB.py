#
# PySNMP MIB module BCN-NTP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/bluecatnetworks/BCN-NTP-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:11:28 2022
# On host fv-az36-988 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
bcnServices, = mibBuilder.importSymbols("BCN-SMI-MIB", "bcnServices")
BcnAlarmSeverity, = mibBuilder.importSymbols("BCN-TC-MIB", "BcnAlarmSeverity")
InetAddress, InetPortNumber, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetPortNumber", "InetAddressType")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
NotificationType, ObjectIdentity, Bits, Gauge32, Counter32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, iso, IpAddress, TimeTicks, ModuleIdentity, Integer32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "ObjectIdentity", "Bits", "Gauge32", "Counter32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "iso", "IpAddress", "TimeTicks", "ModuleIdentity", "Integer32", "Unsigned32")
TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString")
bcnNtpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 1))
bcnNtpMIB.setRevisions(('2010-12-15 00:00',))
if mibBuilder.loadTexts: bcnNtpMIB.setLastUpdated('201012150000Z')
if mibBuilder.loadTexts: bcnNtpMIB.setOrganization('BlueCat Networks')
bcnNtp = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4))
bcnNtpObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2))
bcnNtpNotification = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 3))
bcnNtpConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 4))
class NTPTimeStamp(TextualConvention, OctetString):
    reference = "D.L. Mills, University of Delaware, 'Network Time Protocol(Version 3)', RFC-1305, March 1992, Section 3.1"
    status = 'current'
    displayHint = '4x.4x'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class NTPLeapIndicator(TextualConvention, Integer32):
    reference = "D.L. Mills, University of Delaware, 'Network Time Protocol(Version 3)', RFC-1305, March 1992, Section 3.2.1"
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("noWarning", 0), ("addSecond", 1), ("subtractSecond", 2), ("alarm", 3))

class NTPRefId(TextualConvention, OctetString):
    reference = "D.L. Mills, University of Delaware, 'Network Time Protocol(Version 3)', RFC-5905, June 2010, Section 7.3"
    status = 'current'
    displayHint = '4x'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

bcnNtpServiceStatus = ObjectIdentity((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 1))
if mibBuilder.loadTexts: bcnNtpServiceStatus.setStatus('current')
bcnNtpSerOperState = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("running", 1), ("notRunning", 2), ("starting", 3), ("stopping", 4), ("fault", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnNtpSerOperState.setStatus('current')
bcnNtpSystem = ObjectIdentity((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 2))
if mibBuilder.loadTexts: bcnNtpSystem.setStatus('current')
bcnNtpSysLeap = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 2, 1), NTPLeapIndicator()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnNtpSysLeap.setStatus('current')
bcnNtpSysStratum = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnNtpSysStratum.setStatus('current')
bcnNtpSysPrecision = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 2, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnNtpSysPrecision.setStatus('current')
bcnNtpSysRootDelay = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 2, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnNtpSysRootDelay.setStatus('current')
bcnNtpSysRootDispersion = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 2, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnNtpSysRootDispersion.setStatus('current')
bcnNtpSysRefId = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 2, 6), NTPRefId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnNtpSysRefId.setStatus('current')
bcnNtpSysRefTime = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 2, 7), NTPTimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnNtpSysRefTime.setStatus('current')
bcnNtpSysPoll = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 2, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnNtpSysPoll.setStatus('current')
bcnNtpSysPeer = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 2, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnNtpSysPeer.setStatus('current')
bcnNtpSysFreq = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 2, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnNtpSysFreq.setStatus('current')
bcnNtpSysClock = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 2, 11), NTPTimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnNtpSysClock.setStatus('current')
bcnNtpSysSystem = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 2, 12), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnNtpSysSystem.setStatus('current')
bcnNtpSysProcessor = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 2, 13), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnNtpSysProcessor.setStatus('current')
bcnNtpSysJitter = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 2, 14), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnNtpSysJitter.setStatus('current')
bcnNtpPeers = ObjectIdentity((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 3))
if mibBuilder.loadTexts: bcnNtpPeers.setStatus('current')
bcnNtpPeersVarTable = MibTable((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 3, 1), )
if mibBuilder.loadTexts: bcnNtpPeersVarTable.setStatus('current')
bcnNtpPeersVarEntry = MibTableRow((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 3, 1, 1), ).setIndexNames((0, "BCN-NTP-MIB", "bcnNtpPeersAssocId"))
if mibBuilder.loadTexts: bcnNtpPeersVarEntry.setStatus('current')
bcnNtpPeersAssocId = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 3, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: bcnNtpPeersAssocId.setStatus('current')
bcnNtpPeersConfigured = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 3, 1, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnNtpPeersConfigured.setStatus('current')
bcnNtpPeersPeerAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 3, 1, 1, 3), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnNtpPeersPeerAddressType.setStatus('current')
bcnNtpPeersPeerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 3, 1, 1, 4), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnNtpPeersPeerAddress.setStatus('current')
bcnNtpPeersPeerPort = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 3, 1, 1, 5), InetPortNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnNtpPeersPeerPort.setStatus('current')
bcnNtpPeersHostAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 3, 1, 1, 6), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnNtpPeersHostAddressType.setStatus('current')
bcnNtpPeersHostAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 3, 1, 1, 7), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnNtpPeersHostAddress.setStatus('current')
bcnNtpPeersHostPort = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 3, 1, 1, 8), InetPortNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnNtpPeersHostPort.setStatus('current')
bcnNtpPeersLeap = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 3, 1, 1, 9), NTPLeapIndicator()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnNtpPeersLeap.setStatus('current')
bcnNtpPeersMode = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 3, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("unspecified", 0), ("symmetricActive", 1), ("symmetricPassive", 2), ("client", 3), ("server", 4), ("broadcast", 5), ("reservedControl", 6), ("reservedPrivate", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnNtpPeersMode.setStatus('current')
bcnNtpPeersStratum = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 3, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnNtpPeersStratum.setStatus('current')
bcnNtpPeersPeerPoll = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 3, 1, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnNtpPeersPeerPoll.setStatus('current')
bcnNtpPeersHostPoll = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 3, 1, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnNtpPeersHostPoll.setStatus('current')
bcnNtpPeersPrecision = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 3, 1, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnNtpPeersPrecision.setStatus('current')
bcnNtpPeersRootDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 3, 1, 1, 15), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnNtpPeersRootDelay.setStatus('current')
bcnNtpPeersRootDispersion = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 3, 1, 1, 16), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnNtpPeersRootDispersion.setStatus('current')
bcnNtpPeersRefId = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 3, 1, 1, 17), NTPRefId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnNtpPeersRefId.setStatus('current')
bcnNtpPeersRefTime = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 3, 1, 1, 18), NTPTimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnNtpPeersRefTime.setStatus('current')
bcnNtpPeersOrgTime = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 3, 1, 1, 19), NTPTimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnNtpPeersOrgTime.setStatus('current')
bcnNtpPeersReceiveTime = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 3, 1, 1, 20), NTPTimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnNtpPeersReceiveTime.setStatus('current')
bcnNtpPeersTransmitTime = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 3, 1, 1, 21), NTPTimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnNtpPeersTransmitTime.setStatus('current')
bcnNtpPeersReach = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 3, 1, 1, 22), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnNtpPeersReach.setStatus('current')
bcnNtpPeersOffset = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 3, 1, 1, 23), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnNtpPeersOffset.setStatus('current')
bcnNtpPeersDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 3, 1, 1, 24), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnNtpPeersDelay.setStatus('current')
bcnNtpPeersDispersion = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 3, 1, 1, 25), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnNtpPeersDispersion.setStatus('current')
bcnNtpPeersJitter = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 2, 3, 1, 1, 26), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnNtpPeersJitter.setStatus('current')
bcnNtpNotificationEvents = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 3, 0))
bcnNtpNotificationData = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 3, 1))
bcnNtpAlarmSeverity = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 3, 1, 1), BcnAlarmSeverity()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bcnNtpAlarmSeverity.setStatus('current')
bcnNtpAlarmInfo = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 3, 1, 2), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bcnNtpAlarmInfo.setStatus('current')
bcnNtpAlarmNotif = NotificationType((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 3, 0, 1)).setObjects(("BCN-NTP-MIB", "bcnNtpSerOperState"), ("BCN-NTP-MIB", "bcnNtpAlarmSeverity"), ("BCN-NTP-MIB", "bcnNtpAlarmInfo"))
if mibBuilder.loadTexts: bcnNtpAlarmNotif.setStatus('current')
bcnNtpServiceCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 4, 1))
bcnNtpServiceGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 4, 2))
bcnNtpServiceStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 4, 2, 1)).setObjects(("BCN-NTP-MIB", "bcnNtpSerOperState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bcnNtpServiceStatusGroup = bcnNtpServiceStatusGroup.setStatus('current')
bcnNtpSystemGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 4, 2, 2)).setObjects(("BCN-NTP-MIB", "bcnNtpSysLeap"), ("BCN-NTP-MIB", "bcnNtpSysStratum"), ("BCN-NTP-MIB", "bcnNtpSysPrecision"), ("BCN-NTP-MIB", "bcnNtpSysRootDelay"), ("BCN-NTP-MIB", "bcnNtpSysRootDispersion"), ("BCN-NTP-MIB", "bcnNtpSysRefId"), ("BCN-NTP-MIB", "bcnNtpSysRefTime"), ("BCN-NTP-MIB", "bcnNtpSysPoll"), ("BCN-NTP-MIB", "bcnNtpSysPeer"), ("BCN-NTP-MIB", "bcnNtpSysFreq"), ("BCN-NTP-MIB", "bcnNtpSysClock"), ("BCN-NTP-MIB", "bcnNtpSysSystem"), ("BCN-NTP-MIB", "bcnNtpSysProcessor"), ("BCN-NTP-MIB", "bcnNtpSysJitter"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bcnNtpSystemGroup = bcnNtpSystemGroup.setStatus('current')
bcnNtpPeersGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 4, 2, 3)).setObjects(("BCN-NTP-MIB", "bcnNtpPeersConfigured"), ("BCN-NTP-MIB", "bcnNtpPeersPeerAddressType"), ("BCN-NTP-MIB", "bcnNtpPeersPeerAddress"), ("BCN-NTP-MIB", "bcnNtpPeersPeerPort"), ("BCN-NTP-MIB", "bcnNtpPeersHostAddressType"), ("BCN-NTP-MIB", "bcnNtpPeersHostAddress"), ("BCN-NTP-MIB", "bcnNtpPeersHostPort"), ("BCN-NTP-MIB", "bcnNtpPeersLeap"), ("BCN-NTP-MIB", "bcnNtpPeersMode"), ("BCN-NTP-MIB", "bcnNtpPeersStratum"), ("BCN-NTP-MIB", "bcnNtpPeersPeerPoll"), ("BCN-NTP-MIB", "bcnNtpPeersHostPoll"), ("BCN-NTP-MIB", "bcnNtpPeersPrecision"), ("BCN-NTP-MIB", "bcnNtpPeersRootDelay"), ("BCN-NTP-MIB", "bcnNtpPeersRootDispersion"), ("BCN-NTP-MIB", "bcnNtpPeersRefId"), ("BCN-NTP-MIB", "bcnNtpPeersRefTime"), ("BCN-NTP-MIB", "bcnNtpPeersOrgTime"), ("BCN-NTP-MIB", "bcnNtpPeersReceiveTime"), ("BCN-NTP-MIB", "bcnNtpPeersTransmitTime"), ("BCN-NTP-MIB", "bcnNtpPeersReach"), ("BCN-NTP-MIB", "bcnNtpPeersOffset"), ("BCN-NTP-MIB", "bcnNtpPeersDelay"), ("BCN-NTP-MIB", "bcnNtpPeersDispersion"), ("BCN-NTP-MIB", "bcnNtpPeersJitter"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bcnNtpPeersGroup = bcnNtpPeersGroup.setStatus('current')
bcnNtpNotificationEventGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 4, 2, 4)).setObjects(("BCN-NTP-MIB", "bcnNtpAlarmNotif"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bcnNtpNotificationEventGroup = bcnNtpNotificationEventGroup.setStatus('current')
bcnNtpNotificationDataGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 4, 2, 5)).setObjects(("BCN-NTP-MIB", "bcnNtpAlarmSeverity"), ("BCN-NTP-MIB", "bcnNtpAlarmInfo"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bcnNtpNotificationDataGroup = bcnNtpNotificationDataGroup.setStatus('current')
bcnNtpStatusCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 13315, 3, 1, 4, 4, 1, 1)).setObjects(("BCN-NTP-MIB", "bcnNtpServiceStatusGroup"), ("BCN-NTP-MIB", "bcnNtpSystemGroup"), ("BCN-NTP-MIB", "bcnNtpPeersGroup"), ("BCN-NTP-MIB", "bcnNtpNotificationEventGroup"), ("BCN-NTP-MIB", "bcnNtpNotificationDataGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bcnNtpStatusCompliance = bcnNtpStatusCompliance.setStatus('current')
mibBuilder.exportSymbols("BCN-NTP-MIB", bcnNtpPeersHostPoll=bcnNtpPeersHostPoll, bcnNtpServiceGroups=bcnNtpServiceGroups, PYSNMP_MODULE_ID=bcnNtpMIB, bcnNtpPeersDelay=bcnNtpPeersDelay, bcnNtpPeersHostAddress=bcnNtpPeersHostAddress, bcnNtpAlarmNotif=bcnNtpAlarmNotif, NTPTimeStamp=NTPTimeStamp, bcnNtpConformance=bcnNtpConformance, bcnNtpSysPrecision=bcnNtpSysPrecision, bcnNtpPeersTransmitTime=bcnNtpPeersTransmitTime, bcnNtpPeersMode=bcnNtpPeersMode, bcnNtpPeersVarEntry=bcnNtpPeersVarEntry, bcnNtpSystem=bcnNtpSystem, bcnNtpPeersPeerPoll=bcnNtpPeersPeerPoll, bcnNtpPeersRefId=bcnNtpPeersRefId, bcnNtpPeersHostPort=bcnNtpPeersHostPort, bcnNtpSysPoll=bcnNtpSysPoll, bcnNtpAlarmInfo=bcnNtpAlarmInfo, bcnNtpServiceStatus=bcnNtpServiceStatus, bcnNtpSysRefTime=bcnNtpSysRefTime, bcnNtpPeersOrgTime=bcnNtpPeersOrgTime, bcnNtpMIB=bcnNtpMIB, bcnNtp=bcnNtp, bcnNtpPeersLeap=bcnNtpPeersLeap, bcnNtpPeersDispersion=bcnNtpPeersDispersion, bcnNtpPeersJitter=bcnNtpPeersJitter, bcnNtpNotificationEvents=bcnNtpNotificationEvents, bcnNtpSysSystem=bcnNtpSysSystem, bcnNtpNotificationData=bcnNtpNotificationData, bcnNtpSystemGroup=bcnNtpSystemGroup, NTPRefId=NTPRefId, bcnNtpNotificationDataGroup=bcnNtpNotificationDataGroup, bcnNtpPeersPrecision=bcnNtpPeersPrecision, bcnNtpNotificationEventGroup=bcnNtpNotificationEventGroup, bcnNtpPeersRefTime=bcnNtpPeersRefTime, bcnNtpSysLeap=bcnNtpSysLeap, bcnNtpPeersPeerAddress=bcnNtpPeersPeerAddress, bcnNtpPeersReach=bcnNtpPeersReach, bcnNtpPeersConfigured=bcnNtpPeersConfigured, bcnNtpPeersStratum=bcnNtpPeersStratum, bcnNtpPeersPeerPort=bcnNtpPeersPeerPort, bcnNtpSysJitter=bcnNtpSysJitter, bcnNtpSysStratum=bcnNtpSysStratum, bcnNtpSysRefId=bcnNtpSysRefId, bcnNtpStatusCompliance=bcnNtpStatusCompliance, bcnNtpSysRootDispersion=bcnNtpSysRootDispersion, bcnNtpNotification=bcnNtpNotification, bcnNtpPeersRootDelay=bcnNtpPeersRootDelay, bcnNtpServiceCompliances=bcnNtpServiceCompliances, bcnNtpPeers=bcnNtpPeers, bcnNtpSysClock=bcnNtpSysClock, bcnNtpObjects=bcnNtpObjects, NTPLeapIndicator=NTPLeapIndicator, bcnNtpPeersOffset=bcnNtpPeersOffset, bcnNtpPeersReceiveTime=bcnNtpPeersReceiveTime, bcnNtpServiceStatusGroup=bcnNtpServiceStatusGroup, bcnNtpSysPeer=bcnNtpSysPeer, bcnNtpPeersRootDispersion=bcnNtpPeersRootDispersion, bcnNtpSysRootDelay=bcnNtpSysRootDelay, bcnNtpPeersAssocId=bcnNtpPeersAssocId, bcnNtpPeersHostAddressType=bcnNtpPeersHostAddressType, bcnNtpAlarmSeverity=bcnNtpAlarmSeverity, bcnNtpPeersPeerAddressType=bcnNtpPeersPeerAddressType, bcnNtpPeersGroup=bcnNtpPeersGroup, bcnNtpSerOperState=bcnNtpSerOperState, bcnNtpSysProcessor=bcnNtpSysProcessor, bcnNtpPeersVarTable=bcnNtpPeersVarTable, bcnNtpSysFreq=bcnNtpSysFreq)
