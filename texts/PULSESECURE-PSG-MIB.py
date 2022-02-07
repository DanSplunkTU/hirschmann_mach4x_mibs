#
# PySNMP MIB module PULSESECURE-PSG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/pulse/PULSESECURE-PSG-MIB
# Produced by pysmi-1.1.8 at Mon Feb  7 16:18:25 2022
# On host fv-az42-619 platform Linux version 5.11.0-1028-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, iso, IpAddress, ModuleIdentity, Gauge32, ObjectIdentity, Counter32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Bits, Integer32, TimeTicks, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "iso", "IpAddress", "ModuleIdentity", "Gauge32", "ObjectIdentity", "Counter32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Bits", "Integer32", "TimeTicks", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
pulsesecure_gateway = ModuleIdentity((1, 3, 6, 1, 4, 1, 12532)).setLabel("pulsesecure-gateway")
pulsesecure_gateway.setRevisions(('2016-07-07 16:10',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: pulsesecure_gateway.setRevisionsDescriptions(('Initial Version',))
if mibBuilder.loadTexts: pulsesecure_gateway.setLastUpdated('201607071610Z')
if mibBuilder.loadTexts: pulsesecure_gateway.setOrganization('Pulse Secure')
if mibBuilder.loadTexts: pulsesecure_gateway.setContactInfo('Internet: https://www.pulsesecure.net')
if mibBuilder.loadTexts: pulsesecure_gateway.setDescription('This file defines the private Pulse Secure MIB extensions.')
logFullPercent = MibScalar((1, 3, 6, 1, 4, 1, 12532, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: logFullPercent.setStatus('current')
if mibBuilder.loadTexts: logFullPercent.setDescription('Percentage of log file full')
signedInWebUsers = MibScalar((1, 3, 6, 1, 4, 1, 12532, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: signedInWebUsers.setStatus('current')
if mibBuilder.loadTexts: signedInWebUsers.setDescription('Number of Signed-In Web Users')
signedInMailUsers = MibScalar((1, 3, 6, 1, 4, 1, 12532, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: signedInMailUsers.setStatus('current')
if mibBuilder.loadTexts: signedInMailUsers.setDescription('Number of Signed-In Mail Users')
blockedIP = MibScalar((1, 3, 6, 1, 4, 1, 12532, 4), IpAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: blockedIP.setStatus('current')
if mibBuilder.loadTexts: blockedIP.setDescription('IP Address that is blocked due to consecutive failed login attempts')
authServerName = MibScalar((1, 3, 6, 1, 4, 1, 12532, 5), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: authServerName.setStatus('current')
if mibBuilder.loadTexts: authServerName.setDescription('Name of an external authentication server')
productName = MibScalar((1, 3, 6, 1, 4, 1, 12532, 6), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: productName.setStatus('current')
if mibBuilder.loadTexts: productName.setDescription('IVE Licensed Product Name')
productVersion = MibScalar((1, 3, 6, 1, 4, 1, 12532, 7), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: productVersion.setStatus('current')
if mibBuilder.loadTexts: productVersion.setDescription('IVE System Software Version')
fileName = MibScalar((1, 3, 6, 1, 4, 1, 12532, 8), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: fileName.setStatus('current')
if mibBuilder.loadTexts: fileName.setDescription('File name')
meetingUserCount = MibScalar((1, 3, 6, 1, 4, 1, 12532, 9), Gauge32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: meetingUserCount.setStatus('current')
if mibBuilder.loadTexts: meetingUserCount.setDescription('the number of concurrent meeting users')
iveCpuUtil = MibScalar((1, 3, 6, 1, 4, 1, 12532, 10), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iveCpuUtil.setStatus('current')
if mibBuilder.loadTexts: iveCpuUtil.setDescription('The CPU Utilization of the IVE system')
iveMemoryUtil = MibScalar((1, 3, 6, 1, 4, 1, 12532, 11), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iveMemoryUtil.setStatus('current')
if mibBuilder.loadTexts: iveMemoryUtil.setDescription('The Memory Utilization of the IVE system')
iveConcurrentUsers = MibScalar((1, 3, 6, 1, 4, 1, 12532, 12), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iveConcurrentUsers.setStatus('current')
if mibBuilder.loadTexts: iveConcurrentUsers.setDescription('The Total number of Concurrent user Licenses used for the IVE Node')
clusterConcurrentUsers = MibScalar((1, 3, 6, 1, 4, 1, 12532, 13), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clusterConcurrentUsers.setStatus('current')
if mibBuilder.loadTexts: clusterConcurrentUsers.setDescription('The Total number of Concurrent user Licenses used for the Cluster')
iveTotalHits = MibScalar((1, 3, 6, 1, 4, 1, 12532, 14), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iveTotalHits.setStatus('current')
if mibBuilder.loadTexts: iveTotalHits.setDescription('The Total number of hits to the IVE since last reboot')
iveFileHits = MibScalar((1, 3, 6, 1, 4, 1, 12532, 15), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iveFileHits.setStatus('current')
if mibBuilder.loadTexts: iveFileHits.setDescription('The Total number of File hits to the IVE since last reboot')
iveWebHits = MibScalar((1, 3, 6, 1, 4, 1, 12532, 16), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iveWebHits.setStatus('current')
if mibBuilder.loadTexts: iveWebHits.setDescription('The Total number of hits via the Web Interface since the last reboot')
iveAppletHits = MibScalar((1, 3, 6, 1, 4, 1, 12532, 17), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iveAppletHits.setStatus('current')
if mibBuilder.loadTexts: iveAppletHits.setDescription('The Total number of applet hits to the IVE  since last reboot')
ivetermHits = MibScalar((1, 3, 6, 1, 4, 1, 12532, 18), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ivetermHits.setStatus('current')
if mibBuilder.loadTexts: ivetermHits.setDescription('The Total number of terminal hits to the IVE since last reboot')
iveSAMHits = MibScalar((1, 3, 6, 1, 4, 1, 12532, 19), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iveSAMHits.setStatus('current')
if mibBuilder.loadTexts: iveSAMHits.setDescription('The Total number of SAM(Secure Application manager)hits of since last\nreboot')
iveNCHits = MibScalar((1, 3, 6, 1, 4, 1, 12532, 20), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iveNCHits.setStatus('current')
if mibBuilder.loadTexts: iveNCHits.setDescription('The Total number of NC(Network Connect) hits of since last reboot')
meetingHits = MibScalar((1, 3, 6, 1, 4, 1, 12532, 21), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: meetingHits.setStatus('current')
if mibBuilder.loadTexts: meetingHits.setDescription('The Total number of Meeting hits of since last reboot')
meetingCount = MibScalar((1, 3, 6, 1, 4, 1, 12532, 22), Gauge32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: meetingCount.setStatus('current')
if mibBuilder.loadTexts: meetingCount.setDescription('the number of concurrent meetings')
logName = MibScalar((1, 3, 6, 1, 4, 1, 12532, 23), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: logName.setStatus('current')
if mibBuilder.loadTexts: logName.setDescription('Name of the log (admin/user/event)')
iveSwapUtil = MibScalar((1, 3, 6, 1, 4, 1, 12532, 24), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iveSwapUtil.setStatus('current')
if mibBuilder.loadTexts: iveSwapUtil.setDescription('The Swap Utilization of the IVE system')
diskFullPercent = MibScalar((1, 3, 6, 1, 4, 1, 12532, 25), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskFullPercent.setStatus('current')
if mibBuilder.loadTexts: diskFullPercent.setDescription('Percentage of disk space full')
blockedIPList = MibTable((1, 3, 6, 1, 4, 1, 12532, 26), ).setMaxAccess("readonly")
if mibBuilder.loadTexts: blockedIPList.setStatus('current')
if mibBuilder.loadTexts: blockedIPList.setDescription('Table of 10 most recently blocked IPs')
ipEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12532, 26, 1), ).setIndexNames((0, "PULSESECURE-PSG-MIB", "ipIndex"))
if mibBuilder.loadTexts: ipEntry.setStatus('current')
if mibBuilder.loadTexts: ipEntry.setDescription('An entry containing a blocked IP')
ipIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 12532, 26, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipIndex.setStatus('current')
if mibBuilder.loadTexts: ipIndex.setDescription('Index for IP Table')
ipValue = MibTableColumn((1, 3, 6, 1, 4, 1, 12532, 26, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipValue.setStatus('current')
if mibBuilder.loadTexts: ipValue.setDescription('Blocked IP Entry')
logID = MibScalar((1, 3, 6, 1, 4, 1, 12532, 27), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: logID.setStatus('current')
if mibBuilder.loadTexts: logID.setDescription('The unique ID of the log message.')
logType = MibScalar((1, 3, 6, 1, 4, 1, 12532, 28), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: logType.setStatus('current')
if mibBuilder.loadTexts: logType.setDescription('String stating whether log message is major or critical.')
logDescription = MibScalar((1, 3, 6, 1, 4, 1, 12532, 29), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: logDescription.setStatus('current')
if mibBuilder.loadTexts: logDescription.setDescription('The actual log message string.')
ivsName = MibScalar((1, 3, 6, 1, 4, 1, 12532, 30), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: ivsName.setStatus('deprecated')
if mibBuilder.loadTexts: ivsName.setDescription('Virtual System name')
ocspResponderURL = MibScalar((1, 3, 6, 1, 4, 1, 12532, 31), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: ocspResponderURL.setStatus('current')
if mibBuilder.loadTexts: ocspResponderURL.setDescription('Name of an OCSP Responder')
fanDescription = MibScalar((1, 3, 6, 1, 4, 1, 12532, 32), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: fanDescription.setStatus('current')
if mibBuilder.loadTexts: fanDescription.setDescription('The status of the fans')
psDescription = MibScalar((1, 3, 6, 1, 4, 1, 12532, 33), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: psDescription.setStatus('current')
if mibBuilder.loadTexts: psDescription.setDescription('The status of the power supplies')
raidDescription = MibScalar((1, 3, 6, 1, 4, 1, 12532, 34), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: raidDescription.setStatus('current')
if mibBuilder.loadTexts: raidDescription.setDescription('The status of the RAID')
clusterName = MibScalar((1, 3, 6, 1, 4, 1, 12532, 35), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: clusterName.setStatus('current')
if mibBuilder.loadTexts: clusterName.setDescription('Cluster Name')
nodeList = MibScalar((1, 3, 6, 1, 4, 1, 12532, 36), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: nodeList.setStatus('current')
if mibBuilder.loadTexts: nodeList.setDescription('List of disabled nodes')
vipType = MibScalar((1, 3, 6, 1, 4, 1, 12532, 37), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: vipType.setStatus('current')
if mibBuilder.loadTexts: vipType.setDescription('Whether the VIP is external or internal')
currentVIP = MibScalar((1, 3, 6, 1, 4, 1, 12532, 38), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: currentVIP.setStatus('current')
if mibBuilder.loadTexts: currentVIP.setDescription('Current value of VIP being changed')
newVIP = MibScalar((1, 3, 6, 1, 4, 1, 12532, 39), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: newVIP.setStatus('current')
if mibBuilder.loadTexts: newVIP.setDescription('New value for the VIp being changed')
nicEvent = MibScalar((1, 3, 6, 1, 4, 1, 12532, 40), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: nicEvent.setStatus('current')
if mibBuilder.loadTexts: nicEvent.setDescription('Type of event that generated a the Trap: admin, external')
nodeName = MibScalar((1, 3, 6, 1, 4, 1, 12532, 41), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: nodeName.setStatus('current')
if mibBuilder.loadTexts: nodeName.setDescription('Node Name')
iveTemperature = MibScalar((1, 3, 6, 1, 4, 1, 12532, 42), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iveTemperature.setStatus('current')
if mibBuilder.loadTexts: iveTemperature.setDescription('The Temperature of MAG application blade. Other platform such as SA\nand IC will return 0')
iveVPNTunnels = MibScalar((1, 3, 6, 1, 4, 1, 12532, 43), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iveVPNTunnels.setStatus('current')
if mibBuilder.loadTexts: iveVPNTunnels.setDescription('The number of concurrent Pulse IPSec and NC users')
iveSSLConnections = MibScalar((1, 3, 6, 1, 4, 1, 12532, 44), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iveSSLConnections.setStatus('current')
if mibBuilder.loadTexts: iveSSLConnections.setDescription('Total number of SSL connection ')
esapVersion = MibScalar((1, 3, 6, 1, 4, 1, 12532, 45), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: esapVersion.setStatus('current')
if mibBuilder.loadTexts: esapVersion.setDescription('Active ESAP Version')
vipChangeReason = MibScalar((1, 3, 6, 1, 4, 1, 12532, 46), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: vipChangeReason.setStatus('current')
if mibBuilder.loadTexts: vipChangeReason.setDescription('Reason for the VIP node change')
processName = MibScalar((1, 3, 6, 1, 4, 1, 12532, 47), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: processName.setStatus('current')
if mibBuilder.loadTexts: processName.setDescription('Process Name')
iveTotalSignedInUsers = MibScalar((1, 3, 6, 1, 4, 1, 12532, 48), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iveTotalSignedInUsers.setStatus('current')
if mibBuilder.loadTexts: iveTotalSignedInUsers.setDescription('The Total number of Users Logged In for the Cluster')
vpnACLSPercentage = MibScalar((1, 3, 6, 1, 4, 1, 12532, 49), Gauge32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: vpnACLSPercentage.setStatus('current')
if mibBuilder.loadTexts: vpnACLSPercentage.setDescription('The percentage of system ACL entries reached')
vpnACLSCount = MibScalar((1, 3, 6, 1, 4, 1, 12532, 50), Gauge32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: vpnACLSCount.setStatus('current')
if mibBuilder.loadTexts: vpnACLSCount.setDescription('The number of system ACL entries reached')
blockedIPv6 = MibScalar((1, 3, 6, 1, 4, 1, 12532, 51), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: blockedIPv6.setStatus('current')
if mibBuilder.loadTexts: blockedIPv6.setDescription('IPv6 Address that is blocked due to consecutive failed login attempts')
iveTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 12532, 251))
iveLogNearlyFull = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 4)).setObjects(("PULSESECURE-PSG-MIB", "logFullPercent"), ("PULSESECURE-PSG-MIB", "logName"))
if mibBuilder.loadTexts: iveLogNearlyFull.setStatus('current')
if mibBuilder.loadTexts: iveLogNearlyFull.setDescription('Log file nearly full')
iveLogFull = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 5)).setObjects(("PULSESECURE-PSG-MIB", "logName"))
if mibBuilder.loadTexts: iveLogFull.setStatus('current')
if mibBuilder.loadTexts: iveLogFull.setDescription('Log file full')
iveMaxConcurrentUsersSignedIn = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 6)).setObjects(("PULSESECURE-PSG-MIB", "iveConcurrentUsers"))
if mibBuilder.loadTexts: iveMaxConcurrentUsersSignedIn.setStatus('current')
if mibBuilder.loadTexts: iveMaxConcurrentUsersSignedIn.setDescription('Maximum number of concurrent users signed in')
iveTooManyFailedLoginAttempts = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 7)).setObjects(("PULSESECURE-PSG-MIB", "blockedIP"))
if mibBuilder.loadTexts: iveTooManyFailedLoginAttempts.setStatus('current')
if mibBuilder.loadTexts: iveTooManyFailedLoginAttempts.setDescription('Too many failed login attempts from IPv4 address')
externalAuthServerUnreachable = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 8)).setObjects(("PULSESECURE-PSG-MIB", "authServerName"))
if mibBuilder.loadTexts: externalAuthServerUnreachable.setStatus('current')
if mibBuilder.loadTexts: externalAuthServerUnreachable.setDescription('External authentication server is not responding')
iveStart = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 9))
if mibBuilder.loadTexts: iveStart.setStatus('current')
if mibBuilder.loadTexts: iveStart.setDescription("IVE startup under administrator's instruction.")
iveShutdown = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 10))
if mibBuilder.loadTexts: iveShutdown.setStatus('current')
if mibBuilder.loadTexts: iveShutdown.setDescription("IVE shutdown under administrator's instruction.")
iveReboot = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 11))
if mibBuilder.loadTexts: iveReboot.setStatus('current')
if mibBuilder.loadTexts: iveReboot.setDescription("IVE reboot under administrator's instruction.")
archiveServerUnreachable = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 12))
if mibBuilder.loadTexts: archiveServerUnreachable.setStatus('current')
if mibBuilder.loadTexts: archiveServerUnreachable.setDescription('Archive server is not responding')
archiveServerLoginFailed = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 13))
if mibBuilder.loadTexts: archiveServerLoginFailed.setStatus('current')
if mibBuilder.loadTexts: archiveServerLoginFailed.setDescription('Could not login into archive server. Verify FTP username and\npassword.')
archiveFileTransferFailed = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 14)).setObjects(("PULSESECURE-PSG-MIB", "fileName"))
if mibBuilder.loadTexts: archiveFileTransferFailed.setStatus('current')
if mibBuilder.loadTexts: archiveFileTransferFailed.setDescription('Could not store file on archive server')
meetingUserLimit = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 15)).setObjects(("PULSESECURE-PSG-MIB", "meetingUserCount"))
if mibBuilder.loadTexts: meetingUserLimit.setStatus('current')
if mibBuilder.loadTexts: meetingUserLimit.setDescription('Concurrent user count over license limit')
iveRestart = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 16))
if mibBuilder.loadTexts: iveRestart.setStatus('current')
if mibBuilder.loadTexts: iveRestart.setDescription("IVE has restarted under administrator's instruction.")
meetingLimit = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 17)).setObjects(("PULSESECURE-PSG-MIB", "meetingCount"))
if mibBuilder.loadTexts: meetingLimit.setStatus('current')
if mibBuilder.loadTexts: meetingLimit.setDescription('Concurrent meeting count over license limit')
iveDiskNearlyFull = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 18)).setObjects(("PULSESECURE-PSG-MIB", "diskFullPercent"))
if mibBuilder.loadTexts: iveDiskNearlyFull.setStatus('current')
if mibBuilder.loadTexts: iveDiskNearlyFull.setDescription('Disk space nearly full')
iveDiskFull = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 19))
if mibBuilder.loadTexts: iveDiskFull.setStatus('current')
if mibBuilder.loadTexts: iveDiskFull.setDescription('Disk space full')
logMessageTrap = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 20)).setObjects(("PULSESECURE-PSG-MIB", "logID"), ("PULSESECURE-PSG-MIB", "logType"), ("PULSESECURE-PSG-MIB", "logDescription"))
if mibBuilder.loadTexts: logMessageTrap.setStatus('current')
if mibBuilder.loadTexts: logMessageTrap.setDescription('The TRAP generated from a log message.')
memUtilNotify = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 21)).setObjects(("PULSESECURE-PSG-MIB", "iveMemoryUtil"))
if mibBuilder.loadTexts: memUtilNotify.setStatus('current')
if mibBuilder.loadTexts: memUtilNotify.setDescription('IVE memory utilization above threshold')
cpuUtilNotify = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 22)).setObjects(("PULSESECURE-PSG-MIB", "iveCpuUtil"))
if mibBuilder.loadTexts: cpuUtilNotify.setStatus('current')
if mibBuilder.loadTexts: cpuUtilNotify.setDescription('IVE CPU utilization above threshold')
swapUtilNotify = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 23)).setObjects(("PULSESECURE-PSG-MIB", "iveSwapUtil"))
if mibBuilder.loadTexts: swapUtilNotify.setStatus('current')
if mibBuilder.loadTexts: swapUtilNotify.setDescription('IVE swap utilization above threshold')
iveMaxConcurrentUsersVirtualSystem = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 24)).setObjects(("PULSESECURE-PSG-MIB", "ivsName"))
if mibBuilder.loadTexts: iveMaxConcurrentUsersVirtualSystem.setStatus('deprecated')
if mibBuilder.loadTexts: iveMaxConcurrentUsersVirtualSystem.setDescription('Maximum number of concurrent Virtual System users signed in')
ocspResponderConnectionFailed = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 25)).setObjects(("PULSESECURE-PSG-MIB", "ocspResponderURL"))
if mibBuilder.loadTexts: ocspResponderConnectionFailed.setStatus('current')
if mibBuilder.loadTexts: ocspResponderConnectionFailed.setDescription('OCSP Responder cannot be connected')
iveFanNotify = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 26)).setObjects(("PULSESECURE-PSG-MIB", "fanDescription"))
if mibBuilder.loadTexts: iveFanNotify.setStatus('current')
if mibBuilder.loadTexts: iveFanNotify.setDescription('The status of the fans has changed')
ivePowerSupplyNotify = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 27)).setObjects(("PULSESECURE-PSG-MIB", "psDescription"))
if mibBuilder.loadTexts: ivePowerSupplyNotify.setStatus('current')
if mibBuilder.loadTexts: ivePowerSupplyNotify.setDescription('The status of the power supplies has changed')
iveRaidNotify = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 28)).setObjects(("PULSESECURE-PSG-MIB", "raidDescription"))
if mibBuilder.loadTexts: iveRaidNotify.setStatus('current')
if mibBuilder.loadTexts: iveRaidNotify.setDescription('The status of the RAID has changed')
iveClusterDisableNodeTrap = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 29)).setObjects(("PULSESECURE-PSG-MIB", "clusterName"), ("PULSESECURE-PSG-MIB", "nodeList"))
if mibBuilder.loadTexts: iveClusterDisableNodeTrap.setStatus('current')
if mibBuilder.loadTexts: iveClusterDisableNodeTrap.setDescription('A Given node(s) in a cluster has(have) been disabled')
iveClusterChangedVIPTrap = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 30)).setObjects(("PULSESECURE-PSG-MIB", "vipType"), ("PULSESECURE-PSG-MIB", "currentVIP"), ("PULSESECURE-PSG-MIB", "newVIP"))
if mibBuilder.loadTexts: iveClusterChangedVIPTrap.setStatus('current')
if mibBuilder.loadTexts: iveClusterChangedVIPTrap.setDescription('A external/internal VIP has changed from its current value to a new\none')
iveNetExternalInterfaceDownTrap = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 31)).setObjects(("PULSESECURE-PSG-MIB", "nicEvent"))
if mibBuilder.loadTexts: iveNetExternalInterfaceDownTrap.setStatus('current')
if mibBuilder.loadTexts: iveNetExternalInterfaceDownTrap.setDescription('The External interface has gone down, reason is in nicEvent')
iveClusterDeleteTrap = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 32)).setObjects(("PULSESECURE-PSG-MIB", "nodeName"))
if mibBuilder.loadTexts: iveClusterDeleteTrap.setStatus('current')
if mibBuilder.loadTexts: iveClusterDeleteTrap.setDescription('Cluster delete inititaed by nodeName')
iveNetInternalInterfaceDownTrap = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 33)).setObjects(("PULSESECURE-PSG-MIB", "nicEvent"))
if mibBuilder.loadTexts: iveNetInternalInterfaceDownTrap.setStatus('current')
if mibBuilder.loadTexts: iveNetInternalInterfaceDownTrap.setDescription('The Internal interface has gone down, reason is in nicEvent')
iveNetManagementInterfaceDownTrap = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 34)).setObjects(("PULSESECURE-PSG-MIB", "nicEvent"))
if mibBuilder.loadTexts: iveNetManagementInterfaceDownTrap.setStatus('current')
if mibBuilder.loadTexts: iveNetManagementInterfaceDownTrap.setDescription('The Management interface has gone down, reason is in nicEvent')
iveTemperatureNotify = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 35)).setObjects(("PULSESECURE-PSG-MIB", "iveTemperature"))
if mibBuilder.loadTexts: iveTemperatureNotify.setStatus('current')
if mibBuilder.loadTexts: iveTemperatureNotify.setDescription('IVE Temperature is above threshold')
iveVIPNodeChanged = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 36)).setObjects(("PULSESECURE-PSG-MIB", "nodeName"), ("PULSESECURE-PSG-MIB", "vipChangeReason"))
if mibBuilder.loadTexts: iveVIPNodeChanged.setStatus('current')
if mibBuilder.loadTexts: iveVIPNodeChanged.setDescription('Notifies that VIP node has changed. \n\t nodeName is the new node which is hosting the VIP.\n\t vipChangeReason specifies the reason for the change.')
iveProcessesNearMaxLimit = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 37)).setObjects(("PULSESECURE-PSG-MIB", "processName"))
if mibBuilder.loadTexts: iveProcessesNearMaxLimit.setStatus('current')
if mibBuilder.loadTexts: iveProcessesNearMaxLimit.setDescription('The count of processes (by processName) is about reach to maximum\nlimit')
iveProcessesReachedMaxLimit = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 38)).setObjects(("PULSESECURE-PSG-MIB", "processName"))
if mibBuilder.loadTexts: iveProcessesReachedMaxLimit.setStatus('current')
if mibBuilder.loadTexts: iveProcessesReachedMaxLimit.setDescription('The count of processes (by processName) has reached to maximum limit')
iveACLsNearMaxLimit = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 39)).setObjects(("PULSESECURE-PSG-MIB", "vpnACLSPercentage"))
if mibBuilder.loadTexts: iveACLsNearMaxLimit.setStatus('current')
if mibBuilder.loadTexts: iveACLsNearMaxLimit.setDescription('The percentage of ACL entries has reached maximum supported limit')
iveACLsCrossedMaxLimit = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 40)).setObjects(("PULSESECURE-PSG-MIB", "vpnACLSCount"))
if mibBuilder.loadTexts: iveACLsCrossedMaxLimit.setStatus('current')
if mibBuilder.loadTexts: iveACLsCrossedMaxLimit.setDescription('The count of ACL entries has crossed maximum supported limit')
iveTooManyFailedLoginAttemptsIPv6 = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 41)).setObjects(("PULSESECURE-PSG-MIB", "blockedIPv6"))
if mibBuilder.loadTexts: iveTooManyFailedLoginAttemptsIPv6.setStatus('current')
if mibBuilder.loadTexts: iveTooManyFailedLoginAttemptsIPv6.setDescription('Too many failed login attempts from IPv6 address')
iveSAProduct = MibIdentifier((1, 3, 6, 1, 4, 1, 12532, 252))
iveICProduct = MibIdentifier((1, 3, 6, 1, 4, 1, 12532, 253))
iveMAGProduct = MibIdentifier((1, 3, 6, 1, 4, 1, 12532, 254))
iveVAProduct = MibIdentifier((1, 3, 6, 1, 4, 1, 12532, 255))
ivePSAProduct = MibIdentifier((1, 3, 6, 1, 4, 1, 12532, 256))
iveProductMAG2600 = MibIdentifier((1, 3, 6, 1, 4, 1, 12532, 254, 1))
iveProductMAG4610 = MibIdentifier((1, 3, 6, 1, 4, 1, 12532, 254, 2))
iveProductSM160 = MibIdentifier((1, 3, 6, 1, 4, 1, 12532, 254, 3))
iveProductSM360 = MibIdentifier((1, 3, 6, 1, 4, 1, 12532, 254, 4))
iveProductVASPE = MibIdentifier((1, 3, 6, 1, 4, 1, 12532, 255, 1))
iveProductVADTE = MibIdentifier((1, 3, 6, 1, 4, 1, 12532, 255, 2))
iveProductPSA300 = MibIdentifier((1, 3, 6, 1, 4, 1, 12532, 256, 1))
iveProductPSA3000 = MibIdentifier((1, 3, 6, 1, 4, 1, 12532, 256, 2))
iveProductPSA5000 = MibIdentifier((1, 3, 6, 1, 4, 1, 12532, 256, 3))
iveProductPSA7000f = MibIdentifier((1, 3, 6, 1, 4, 1, 12532, 256, 4))
iveProductPSA7000c = MibIdentifier((1, 3, 6, 1, 4, 1, 12532, 256, 5))
iveProductPSA10000 = MibIdentifier((1, 3, 6, 1, 4, 1, 12532, 256, 6))
iveMAG2600 = MibIdentifier((1, 3, 6, 1, 4, 1, 12532, 254, 1, 1))
iveMAG4610 = MibIdentifier((1, 3, 6, 1, 4, 1, 12532, 254, 2, 1))
iveMAGSM160 = MibIdentifier((1, 3, 6, 1, 4, 1, 12532, 254, 3, 1))
iveMAGSM360 = MibIdentifier((1, 3, 6, 1, 4, 1, 12532, 254, 4, 1))
iveVASPE = MibIdentifier((1, 3, 6, 1, 4, 1, 12532, 255, 1, 1))
iveVADTE = MibIdentifier((1, 3, 6, 1, 4, 1, 12532, 255, 2, 1))
ivePSA300 = MibIdentifier((1, 3, 6, 1, 4, 1, 12532, 256, 1, 1))
ivePSA3000 = MibIdentifier((1, 3, 6, 1, 4, 1, 12532, 256, 2, 1))
ivePSA5000 = MibIdentifier((1, 3, 6, 1, 4, 1, 12532, 256, 3, 1))
ivePSA7000f = MibIdentifier((1, 3, 6, 1, 4, 1, 12532, 256, 4, 1))
ivePSA7000c = MibIdentifier((1, 3, 6, 1, 4, 1, 12532, 256, 5, 1))
ivePSA10000 = MibIdentifier((1, 3, 6, 1, 4, 1, 12532, 256, 6, 1))
mibBuilder.exportSymbols("PULSESECURE-PSG-MIB", ivsName=ivsName, iveVPNTunnels=iveVPNTunnels, ivePSA7000f=ivePSA7000f, iveTotalSignedInUsers=iveTotalSignedInUsers, swapUtilNotify=swapUtilNotify, ivePSA10000=ivePSA10000, iveFanNotify=iveFanNotify, logType=logType, iveLogFull=iveLogFull, ivePowerSupplyNotify=ivePowerSupplyNotify, productName=productName, iveTooManyFailedLoginAttempts=iveTooManyFailedLoginAttempts, iveSAMHits=iveSAMHits, iveProcessesReachedMaxLimit=iveProcessesReachedMaxLimit, externalAuthServerUnreachable=externalAuthServerUnreachable, iveMemoryUtil=iveMemoryUtil, iveCpuUtil=iveCpuUtil, iveDiskFull=iveDiskFull, iveRaidNotify=iveRaidNotify, iveACLsNearMaxLimit=iveACLsNearMaxLimit, iveSSLConnections=iveSSLConnections, vpnACLSCount=vpnACLSCount, iveProcessesNearMaxLimit=iveProcessesNearMaxLimit, iveProductMAG4610=iveProductMAG4610, iveProductPSA5000=iveProductPSA5000, iveRestart=iveRestart, archiveServerUnreachable=archiveServerUnreachable, ivePSA3000=ivePSA3000, iveProductPSA10000=iveProductPSA10000, pulsesecure_gateway=pulsesecure_gateway, iveProductSM360=iveProductSM360, iveProductPSA7000c=iveProductPSA7000c, clusterConcurrentUsers=clusterConcurrentUsers, fanDescription=fanDescription, blockedIPList=blockedIPList, iveNetExternalInterfaceDownTrap=iveNetExternalInterfaceDownTrap, iveNCHits=iveNCHits, clusterName=clusterName, iveProductVADTE=iveProductVADTE, iveProductPSA3000=iveProductPSA3000, iveFileHits=iveFileHits, meetingUserLimit=meetingUserLimit, ocspResponderConnectionFailed=ocspResponderConnectionFailed, iveProductMAG2600=iveProductMAG2600, iveShutdown=iveShutdown, logFullPercent=logFullPercent, ipValue=ipValue, nodeList=nodeList, currentVIP=currentVIP, signedInWebUsers=signedInWebUsers, ivePSA300=ivePSA300, iveMaxConcurrentUsersVirtualSystem=iveMaxConcurrentUsersVirtualSystem, processName=processName, logMessageTrap=logMessageTrap, iveSwapUtil=iveSwapUtil, iveTemperature=iveTemperature, diskFullPercent=diskFullPercent, iveMAGSM160=iveMAGSM160, meetingCount=meetingCount, iveClusterDeleteTrap=iveClusterDeleteTrap, raidDescription=raidDescription, vipType=vipType, iveMAG2600=iveMAG2600, iveWebHits=iveWebHits, iveMAG4610=iveMAG4610, ivePSA5000=ivePSA5000, ocspResponderURL=ocspResponderURL, iveClusterChangedVIPTrap=iveClusterChangedVIPTrap, iveLogNearlyFull=iveLogNearlyFull, iveProductSM160=iveProductSM160, iveTraps=iveTraps, iveVADTE=iveVADTE, iveVASPE=iveVASPE, PYSNMP_MODULE_ID=pulsesecure_gateway, iveSAProduct=iveSAProduct, iveACLsCrossedMaxLimit=iveACLsCrossedMaxLimit, logName=logName, blockedIP=blockedIP, productVersion=productVersion, ipEntry=ipEntry, iveICProduct=iveICProduct, iveReboot=iveReboot, blockedIPv6=blockedIPv6, esapVersion=esapVersion, meetingLimit=meetingLimit, newVIP=newVIP, ivetermHits=ivetermHits, signedInMailUsers=signedInMailUsers, logDescription=logDescription, ivePSA7000c=ivePSA7000c, iveTotalHits=iveTotalHits, nicEvent=nicEvent, iveVIPNodeChanged=iveVIPNodeChanged, fileName=fileName, ivePSAProduct=ivePSAProduct, ipIndex=ipIndex, iveAppletHits=iveAppletHits, meetingHits=meetingHits, archiveServerLoginFailed=archiveServerLoginFailed, memUtilNotify=memUtilNotify, logID=logID, nodeName=nodeName, iveMAGProduct=iveMAGProduct, vipChangeReason=vipChangeReason, iveMaxConcurrentUsersSignedIn=iveMaxConcurrentUsersSignedIn, cpuUtilNotify=cpuUtilNotify, vpnACLSPercentage=vpnACLSPercentage, meetingUserCount=meetingUserCount, iveDiskNearlyFull=iveDiskNearlyFull, iveConcurrentUsers=iveConcurrentUsers, iveProductPSA7000f=iveProductPSA7000f, psDescription=psDescription, iveTemperatureNotify=iveTemperatureNotify, authServerName=authServerName, iveProductVASPE=iveProductVASPE, iveNetInternalInterfaceDownTrap=iveNetInternalInterfaceDownTrap, iveVAProduct=iveVAProduct, iveMAGSM360=iveMAGSM360, iveNetManagementInterfaceDownTrap=iveNetManagementInterfaceDownTrap, iveClusterDisableNodeTrap=iveClusterDisableNodeTrap, iveProductPSA300=iveProductPSA300, iveStart=iveStart, archiveFileTransferFailed=archiveFileTransferFailed, iveTooManyFailedLoginAttemptsIPv6=iveTooManyFailedLoginAttemptsIPv6)
