#
# PySNMP MIB module ADONIS-DNS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/bluecatnetworks/ADONIS-DNS-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 17:53:10 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
appliances, = mibBuilder.importSymbols("BLUECATNETWORKS-MIB", "appliances")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Gauge32, Counter32, Unsigned32, Counter64, Bits, ObjectIdentity, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, MibIdentifier, IpAddress, Integer32, enterprises, NotificationType, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Counter32", "Unsigned32", "Counter64", "Bits", "ObjectIdentity", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "MibIdentifier", "IpAddress", "Integer32", "enterprises", "NotificationType", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
adonis = ModuleIdentity((1, 3, 6, 1, 4, 1, 13315, 100, 101))
if mibBuilder.loadTexts: adonis.setLastUpdated('200810010000Z')
if mibBuilder.loadTexts: adonis.setOrganization('BlueCat Networks Inc.')
if mibBuilder.loadTexts: adonis.setContactInfo('Adonis Technical Support\n\t\t BlueCat Networks Inc.\n\t\t \n\t\t Tel: +1 866 491 2228 (toll free)\n\t\t      +1 416 646 8400 (international) \n\t\t Email: support@bluecatnetworks.com')
if mibBuilder.loadTexts: adonis.setDescription('MIB for the Adonis DNS Server')
adonisObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1))
dns = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 1))
dnsDaemon = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 1, 1))
dnsStats = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 1, 2))
dhcp = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 2))
dhcpDaemon = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 2, 1))
dhcpStats = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 2, 2))
dhcpConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 2, 3))
ha = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 3))
haService = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 3, 1))
commandServer = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 4))
commandServerDaemon = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 4, 1))
lcd = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 5))
lcdDaemon = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 5, 1))
tftp = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 6))
tftpDaemon = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 6, 1))
system = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 7))
systemDaemon = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 7, 1))
adonisTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 100, 101, 2))
trapDNS = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 100, 101, 2, 1))
trapHA = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 100, 101, 2, 2))
trapCommandServer = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 100, 101, 2, 3))
trapDHCP = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 100, 101, 2, 4))
trapReplication = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 100, 101, 2, 5))
trapTFTP = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 100, 101, 2, 6))
trapSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 100, 101, 2, 7))
dnsDaemonRunning = MibScalar((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsDaemonRunning.setStatus('current')
if mibBuilder.loadTexts: dnsDaemonRunning.setDescription('Current running state of the DNS daemon.\n\t\t\t\t 0 - Not Running\n\t\t\t\t 1 - Running')
dnsDaemonNumberOfZones = MibScalar((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 1, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsDaemonNumberOfZones.setStatus('current')
if mibBuilder.loadTexts: dnsDaemonNumberOfZones.setDescription('Number of zones loaded')
dnsDaemonDebugLevel = MibScalar((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 1, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsDaemonDebugLevel.setStatus('current')
if mibBuilder.loadTexts: dnsDaemonDebugLevel.setDescription('Current debug level')
dnsDaemonZoneTransfersInProgress = MibScalar((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 1, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsDaemonZoneTransfersInProgress.setStatus('current')
if mibBuilder.loadTexts: dnsDaemonZoneTransfersInProgress.setDescription('Number of zone transfers currently in progress')
dnsDaemonZoneTransfersDeferred = MibScalar((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 1, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsDaemonZoneTransfersDeferred.setStatus('current')
if mibBuilder.loadTexts: dnsDaemonZoneTransfersDeferred.setDescription('Number of zone transfers currently deferred')
dnsDaemonSOAQueriesInProgress = MibScalar((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 1, 1, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsDaemonSOAQueriesInProgress.setStatus('current')
if mibBuilder.loadTexts: dnsDaemonSOAQueriesInProgress.setDescription('Number of SOA queries in progress')
dnsDaemonQueryLoggingState = MibScalar((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsDaemonQueryLoggingState.setStatus('current')
if mibBuilder.loadTexts: dnsDaemonQueryLoggingState.setDescription('Current running state of query logging.\n\t\t\t\t 0 - Not logging\n\t\t\t\t 1 - Logging')
dnsDaemonZoneTransferFailure = MibScalar((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 1, 1, 8), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsDaemonZoneTransferFailure.setStatus('current')
if mibBuilder.loadTexts: dnsDaemonZoneTransferFailure.setDescription('The last zone transfer failure desciption which includes the time, the zone name, the master address and the explaination')
dnsStatsSuccess = MibScalar((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 1, 2, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsStatsSuccess.setStatus('current')
if mibBuilder.loadTexts: dnsStatsSuccess.setDescription('Number of successful queries made to the server since dns daemon was started')
dnsStatsReferral = MibScalar((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 1, 2, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsStatsReferral.setStatus('current')
if mibBuilder.loadTexts: dnsStatsReferral.setDescription('Number of queries that resulted in referal responses since dns daemon was started')
dnsStatsNXRRSet = MibScalar((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 1, 2, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsStatsNXRRSet.setStatus('current')
if mibBuilder.loadTexts: dnsStatsNXRRSet.setDescription('Number of queries that resulted in non-existent record set since dns daemon was started')
dnsStatsNXDomain = MibScalar((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 1, 2, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsStatsNXDomain.setStatus('current')
if mibBuilder.loadTexts: dnsStatsNXDomain.setDescription('Number of queries that resulted in non-existent domain responses since dns daemon was started')
dnsStatsRecursion = MibScalar((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 1, 2, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsStatsRecursion.setStatus('current')
if mibBuilder.loadTexts: dnsStatsRecursion.setDescription('Number of queries that required the server to perform recursive lookups since dns daemon was started')
dnsStatsFailure = MibScalar((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 1, 2, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsStatsFailure.setStatus('current')
if mibBuilder.loadTexts: dnsStatsFailure.setDescription('Number of failed queries that did not result in non-existent domain or record set since dns daemon was started')
dhcpDaemonRunning = MibScalar((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpDaemonRunning.setStatus('current')
if mibBuilder.loadTexts: dhcpDaemonRunning.setDescription('Current running state of the DHCP daemon.\n\t\t\t\t 0 - Not Running\n\t\t\t\t 1 - Running')
dhcpDaemonSubnetAlert = MibScalar((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 2, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpDaemonSubnetAlert.setStatus('current')
if mibBuilder.loadTexts: dhcpDaemonSubnetAlert.setDescription('The IP address which has to be alerted for.')
dhcpDaemonLeaseStatsSuccess = MibScalar((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpDaemonLeaseStatsSuccess.setStatus('current')
if mibBuilder.loadTexts: dhcpDaemonLeaseStatsSuccess.setDescription('The number of successful DHCP leases issued per second')
dhcpFailOverState = MibScalar((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpFailOverState.setStatus('current')
if mibBuilder.loadTexts: dhcpFailOverState.setDescription('Current state of the DHCP failover.\n\t\t\t\t 1  - startup\n\t\t\t\t 2  - normal\n\t\t\t\t 3  - communications interrupted\n\t\t\t\t 4  - partner down\n\t\t\t\t 5  - potential conflict\n\t\t\t\t 6  - recover\n\t\t\t\t 7  - paused\n\t\t\t\t 8  - shutdown\n\t\t\t\t 9  - recover done\n\t\t\t\t 254 - recover wait')
dhcpLeaseTable = MibTable((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 2, 2, 1), ).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpLeaseTable.setStatus('current')
if mibBuilder.loadTexts: dhcpLeaseTable.setDescription('Current lease table')
dhcpLeaseEntry = MibTableRow((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 2, 2, 1, 1), ).setMaxAccess("readonly").setIndexNames((0, "ADONIS-DNS-MIB", "dhcpIP"))
if mibBuilder.loadTexts: dhcpLeaseEntry.setStatus('current')
if mibBuilder.loadTexts: dhcpLeaseEntry.setDescription('Information about a particular DHCP lease')
dhcpIP = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 2, 2, 1, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpIP.setStatus('current')
if mibBuilder.loadTexts: dhcpIP.setDescription('IP address of the lease')
dhcpLeaseStartTime = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 2, 2, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpLeaseStartTime.setStatus('current')
if mibBuilder.loadTexts: dhcpLeaseStartTime.setDescription('Start time of the lease')
dhcpLeaseEndTime = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 2, 2, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpLeaseEndTime.setStatus('current')
if mibBuilder.loadTexts: dhcpLeaseEndTime.setDescription('End time of the lease')
dhcpLeaseTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 2, 2, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpLeaseTimeStamp.setStatus('current')
if mibBuilder.loadTexts: dhcpLeaseTimeStamp.setDescription('Timestamp of the lease')
dhcpLeaseBindState = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 2, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("free", 0), ("active", 1), ("fixed", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpLeaseBindState.setStatus('current')
if mibBuilder.loadTexts: dhcpLeaseBindState.setDescription('The state of this lease')
dhcpLeaseHardwareAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 2, 2, 1, 1, 6), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpLeaseHardwareAddress.setStatus('current')
if mibBuilder.loadTexts: dhcpLeaseHardwareAddress.setDescription('The hardware address (MAC address) of this lease')
dhcpLeaseHostname = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 2, 2, 1, 1, 7), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpLeaseHostname.setStatus('current')
if mibBuilder.loadTexts: dhcpLeaseHostname.setDescription('The client hostname of this lease')
dhcpSubnetTable = MibTable((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 2, 2, 2), ).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpSubnetTable.setStatus('current')
if mibBuilder.loadTexts: dhcpSubnetTable.setDescription('Current subnet table')
dhcpSubnetEntry = MibTableRow((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 2, 2, 2, 1), ).setMaxAccess("readonly").setIndexNames((0, "ADONIS-DNS-MIB", "dhcpSubnetIP"))
if mibBuilder.loadTexts: dhcpSubnetEntry.setStatus('current')
if mibBuilder.loadTexts: dhcpSubnetEntry.setDescription('Information about a particular DHCP subnet')
dhcpSubnetIP = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 2, 2, 2, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpSubnetIP.setStatus('current')
if mibBuilder.loadTexts: dhcpSubnetIP.setDescription('IP address of the subnet')
dhcpSubnetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 2, 2, 2, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpSubnetMask.setStatus('current')
if mibBuilder.loadTexts: dhcpSubnetMask.setDescription('IP mask of the subnet')
dhcpSubnetSize = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 2, 2, 2, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpSubnetSize.setStatus('current')
if mibBuilder.loadTexts: dhcpSubnetSize.setDescription('size of the subnet')
dhcpSubnetUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 2, 2, 2, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpSubnetUsed.setStatus('current')
if mibBuilder.loadTexts: dhcpSubnetUsed.setDescription('the number of used IPs in the subnet')
dhcpSubnetAlert = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 2, 2, 2, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpSubnetAlert.setStatus('current')
if mibBuilder.loadTexts: dhcpSubnetAlert.setDescription('alert level in the subnet')
dhcpPoolTable = MibTable((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 2, 2, 3), ).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpPoolTable.setStatus('current')
if mibBuilder.loadTexts: dhcpPoolTable.setDescription('Current pool table')
dhcpPoolEntry = MibTableRow((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 2, 2, 3, 1), ).setMaxAccess("readonly").setIndexNames((0, "ADONIS-DNS-MIB", "dhcpPoolStartIP"))
if mibBuilder.loadTexts: dhcpPoolEntry.setStatus('current')
if mibBuilder.loadTexts: dhcpPoolEntry.setDescription('Information about a particular DHCP pool')
dhcpPoolSubnetIP = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 2, 2, 3, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpPoolSubnetIP.setStatus('current')
if mibBuilder.loadTexts: dhcpPoolSubnetIP.setDescription('subnet IP address of the pool')
dhcpPoolStartIP = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 2, 2, 3, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpPoolStartIP.setStatus('current')
if mibBuilder.loadTexts: dhcpPoolStartIP.setDescription('start IP address of the pool')
dhcpPoolEndIP = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 2, 2, 3, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpPoolEndIP.setStatus('current')
if mibBuilder.loadTexts: dhcpPoolEndIP.setDescription('end IP address of the pool')
dhcpPoolSize = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 2, 2, 3, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpPoolSize.setStatus('current')
if mibBuilder.loadTexts: dhcpPoolSize.setDescription('the size of the pool')
dhcpPoolUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 2, 2, 3, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpPoolUsed.setStatus('current')
if mibBuilder.loadTexts: dhcpPoolUsed.setDescription('the number of used IPs in the pool')
dhcpPoolAlert = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 2, 2, 3, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpPoolAlert.setStatus('current')
if mibBuilder.loadTexts: dhcpPoolAlert.setDescription('the alert level of the pool')
dhcpFixedIPTable = MibTable((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 2, 3, 1), ).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpFixedIPTable.setStatus('current')
if mibBuilder.loadTexts: dhcpFixedIPTable.setDescription('Current DHCP subnet tables in configuration')
dhcpFixedIPEntry = MibTableRow((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 2, 3, 1, 1), ).setMaxAccess("readonly").setIndexNames((0, "ADONIS-DNS-MIB", "dhcpFixedIP"))
if mibBuilder.loadTexts: dhcpFixedIPEntry.setStatus('current')
if mibBuilder.loadTexts: dhcpFixedIPEntry.setDescription('Information about a particular DHCP subnet')
dhcpFixedIP = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 2, 3, 1, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpFixedIP.setStatus('current')
if mibBuilder.loadTexts: dhcpFixedIP.setDescription('One of the current fixed IP addresses in the DHCP configuration')
haServiceRunning = MibScalar((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: haServiceRunning.setStatus('current')
if mibBuilder.loadTexts: haServiceRunning.setDescription('Current running state of high availability.\n\t\t\t\t 0 - Not running\n\t\t\t\t 1 - Running')
haServiceNodeType = MibScalar((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: haServiceNodeType.setStatus('current')
if mibBuilder.loadTexts: haServiceNodeType.setDescription('Type of high availability node\n\t\t\t\t 0 - HA not running\n\t\t\t\t 1 - Active Node\n\t\t\t\t 2 - Passive Node')
haReplicationBinding = MibScalar((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: haReplicationBinding.setStatus('current')
if mibBuilder.loadTexts: haReplicationBinding.setDescription('Binding for replicationFailure trap')
commandServerDaemonRunning = MibScalar((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: commandServerDaemonRunning.setStatus('current')
if mibBuilder.loadTexts: commandServerDaemonRunning.setDescription('Current running state of the command server daemon.\n\t\t\t\t 0 - Not running\n\t\t\t\t 1 - Running')
systemState = MibScalar((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 7, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemState.setStatus('current')
if mibBuilder.loadTexts: systemState.setDescription('Current state of system.\n\t\t\t\t 0  - shutdown\n\t\t\t\t 1  - restart\n\t\t\t\t 2  - startup')
tftpDaemonRunning = MibScalar((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tftpDaemonRunning.setStatus('current')
if mibBuilder.loadTexts: tftpDaemonRunning.setDescription('Current running state of the TFTP daemon.\n\t\t\t\t 0 - Not running\n\t\t\t\t 1 - Running\n\t\t\t\t 2 - Restarting')
licenseValid = MibScalar((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: licenseValid.setStatus('current')
if mibBuilder.loadTexts: licenseValid.setDescription('Current virtual machine license status.\n\t\t\t\t 0 - Not valid \n\t\t\t\t 1 - Valid')
licenseExpiry = MibScalar((1, 3, 6, 1, 4, 1, 13315, 100, 101, 1, 5, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: licenseExpiry.setStatus('current')
if mibBuilder.loadTexts: licenseExpiry.setDescription('Expiry time of the license in seconds since the UNIX Epoch')
trapDNSDaemon = NotificationType((1, 3, 6, 1, 4, 1, 13315, 100, 101, 2, 1, 1)).setObjects(("ADONIS-DNS-MIB", "dnsDaemonRunning"), ("ADONIS-DNS-MIB", "dnsDaemonZoneTransferFailure"))
if mibBuilder.loadTexts: trapDNSDaemon.setStatus('current')
if mibBuilder.loadTexts: trapDNSDaemon.setDescription('DNS daemon has stopped running or a zone transfer failed')
trapDHCPDaemon = NotificationType((1, 3, 6, 1, 4, 1, 13315, 100, 101, 2, 4, 1)).setObjects(("ADONIS-DNS-MIB", "dhcpDaemonRunning"), ("ADONIS-DNS-MIB", "dhcpDaemonSubnetAlert"), ("ADONIS-DNS-MIB", "dhcpFailOverState"))
if mibBuilder.loadTexts: trapDHCPDaemon.setStatus('current')
if mibBuilder.loadTexts: trapDHCPDaemon.setDescription('DHCP daemon has stopped running or\n\t\tthe number of assigned IPS in one of the subnets has reached \n\t\tto the alert level or DHCP failover state changes')
trapHAServiceFailOver = NotificationType((1, 3, 6, 1, 4, 1, 13315, 100, 101, 2, 2, 1)).setObjects(("ADONIS-DNS-MIB", "haServiceNodeType"))
if mibBuilder.loadTexts: trapHAServiceFailOver.setStatus('current')
if mibBuilder.loadTexts: trapHAServiceFailOver.setDescription('High availibility service failed over')
trapCommandServerDaemon = NotificationType((1, 3, 6, 1, 4, 1, 13315, 100, 101, 2, 3, 1)).setObjects(("ADONIS-DNS-MIB", "commandServerDaemonRunning"))
if mibBuilder.loadTexts: trapCommandServerDaemon.setStatus('current')
if mibBuilder.loadTexts: trapCommandServerDaemon.setDescription('Command server daemon has stopped running')
trapSystemDaemon = NotificationType((1, 3, 6, 1, 4, 1, 13315, 100, 101, 2, 7, 1)).setObjects(("ADONIS-DNS-MIB", "systemState"))
if mibBuilder.loadTexts: trapSystemDaemon.setStatus('current')
if mibBuilder.loadTexts: trapSystemDaemon.setDescription('System has stopped running')
trapReplicationFailure = NotificationType((1, 3, 6, 1, 4, 1, 13315, 100, 101, 2, 5, 1))
if mibBuilder.loadTexts: trapReplicationFailure.setStatus('current')
if mibBuilder.loadTexts: trapReplicationFailure.setDescription('Replication has failed')
trapTFTPDaemon = NotificationType((1, 3, 6, 1, 4, 1, 13315, 100, 101, 2, 6, 1)).setObjects(("ADONIS-DNS-MIB", "tftpDaemonRunning"))
if mibBuilder.loadTexts: trapTFTPDaemon.setStatus('current')
if mibBuilder.loadTexts: trapTFTPDaemon.setDescription('TFTP daemon has stopped running')
mibBuilder.exportSymbols("ADONIS-DNS-MIB", dnsStatsReferral=dnsStatsReferral, dhcpDaemon=dhcpDaemon, trapCommandServer=trapCommandServer, tftpDaemonRunning=tftpDaemonRunning, dhcpSubnetTable=dhcpSubnetTable, haServiceRunning=haServiceRunning, dhcpDaemonRunning=dhcpDaemonRunning, PYSNMP_MODULE_ID=adonis, dhcpLeaseHardwareAddress=dhcpLeaseHardwareAddress, adonis=adonis, dhcpConfig=dhcpConfig, trapTFTPDaemon=trapTFTPDaemon, trapDHCP=trapDHCP, lcd=lcd, dhcpLeaseEndTime=dhcpLeaseEndTime, haServiceNodeType=haServiceNodeType, dnsStats=dnsStats, haReplicationBinding=haReplicationBinding, trapCommandServerDaemon=trapCommandServerDaemon, dhcpSubnetMask=dhcpSubnetMask, dnsDaemonQueryLoggingState=dnsDaemonQueryLoggingState, tftp=tftp, dhcpPoolStartIP=dhcpPoolStartIP, dhcpFixedIP=dhcpFixedIP, tftpDaemon=tftpDaemon, dhcpSubnetAlert=dhcpSubnetAlert, dhcp=dhcp, dhcpFailOverState=dhcpFailOverState, dnsDaemonZoneTransferFailure=dnsDaemonZoneTransferFailure, dhcpSubnetIP=dhcpSubnetIP, dhcpDaemonSubnetAlert=dhcpDaemonSubnetAlert, dnsDaemon=dnsDaemon, ha=ha, trapTFTP=trapTFTP, systemState=systemState, dnsDaemonDebugLevel=dnsDaemonDebugLevel, dhcpSubnetEntry=dhcpSubnetEntry, dnsDaemonZoneTransfersDeferred=dnsDaemonZoneTransfersDeferred, dnsDaemonNumberOfZones=dnsDaemonNumberOfZones, dhcpPoolSubnetIP=dhcpPoolSubnetIP, dhcpPoolEndIP=dhcpPoolEndIP, dhcpFixedIPEntry=dhcpFixedIPEntry, dhcpLeaseEntry=dhcpLeaseEntry, trapHA=trapHA, dnsStatsNXRRSet=dnsStatsNXRRSet, trapDNS=trapDNS, trapDNSDaemon=trapDNSDaemon, dnsStatsRecursion=dnsStatsRecursion, dhcpDaemonLeaseStatsSuccess=dhcpDaemonLeaseStatsSuccess, dhcpPoolUsed=dhcpPoolUsed, licenseValid=licenseValid, dhcpPoolTable=dhcpPoolTable, adonisObjects=adonisObjects, dhcpPoolEntry=dhcpPoolEntry, dnsStatsFailure=dnsStatsFailure, trapSystem=trapSystem, trapReplication=trapReplication, dhcpSubnetUsed=dhcpSubnetUsed, haService=haService, trapDHCPDaemon=trapDHCPDaemon, dhcpLeaseBindState=dhcpLeaseBindState, commandServer=commandServer, commandServerDaemonRunning=commandServerDaemonRunning, dns=dns, trapSystemDaemon=trapSystemDaemon, systemDaemon=systemDaemon, dhcpFixedIPTable=dhcpFixedIPTable, lcdDaemon=lcdDaemon, dhcpLeaseStartTime=dhcpLeaseStartTime, commandServerDaemon=commandServerDaemon, dnsDaemonSOAQueriesInProgress=dnsDaemonSOAQueriesInProgress, dhcpIP=dhcpIP, licenseExpiry=licenseExpiry, dnsStatsNXDomain=dnsStatsNXDomain, dnsStatsSuccess=dnsStatsSuccess, dhcpLeaseTimeStamp=dhcpLeaseTimeStamp, adonisTraps=adonisTraps, trapHAServiceFailOver=trapHAServiceFailOver, dhcpStats=dhcpStats, dhcpPoolSize=dhcpPoolSize, dhcpPoolAlert=dhcpPoolAlert, dhcpSubnetSize=dhcpSubnetSize, dhcpLeaseHostname=dhcpLeaseHostname, dhcpLeaseTable=dhcpLeaseTable, trapReplicationFailure=trapReplicationFailure, system=system, dnsDaemonZoneTransfersInProgress=dnsDaemonZoneTransfersInProgress, dnsDaemonRunning=dnsDaemonRunning)
