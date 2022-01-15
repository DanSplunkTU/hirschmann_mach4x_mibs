#
# PySNMP MIB module BCN-DHCPV4-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/bluecatnetworks/BCN-DHCPV4-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 17:53:10 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
bcnServices, = mibBuilder.importSymbols("BCN-SMI-MIB", "bcnServices")
BcnAlarmSeverity, = mibBuilder.importSymbols("BCN-TC-MIB", "BcnAlarmSeverity")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Gauge32, Counter32, Counter64, Integer32, Bits, iso, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, MibIdentifier, IpAddress, ObjectIdentity, NotificationType, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Counter32", "Counter64", "Integer32", "Bits", "iso", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "MibIdentifier", "IpAddress", "ObjectIdentity", "NotificationType", "Unsigned32")
TextualConvention, DisplayString, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "MacAddress")
bcnDhcpv4MIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 1))
bcnDhcpv4MIB.setRevisions(('2010-12-08 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: bcnDhcpv4MIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: bcnDhcpv4MIB.setLastUpdated('201012080000Z')
if mibBuilder.loadTexts: bcnDhcpv4MIB.setOrganization('BlueCat Networks')
if mibBuilder.loadTexts: bcnDhcpv4MIB.setContactInfo('BlueCat Networks. Customer Care.\n\n        North America\n        Call: +1.866.491.2228\n        Europe\n        Call: +44.8081.011.306\n        Other\n        Call: +1.416.646.8433\n        \n        Email: support@bluecatnetworks.com')
if mibBuilder.loadTexts: bcnDhcpv4MIB.setDescription('This module provides status as well as statistical information\n        about the DHCPv4 service.')
bcnDhcpv4 = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 1, 1))
bcnDhcpv4Objects = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 2))
bcnDhcpv4Notification = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 3))
bcnDhcpv4Conformance = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 4))
bcnDhcpv4ServiceStatus = ObjectIdentity((1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 2, 1))
if mibBuilder.loadTexts: bcnDhcpv4ServiceStatus.setStatus('current')
if mibBuilder.loadTexts: bcnDhcpv4ServiceStatus.setDescription('General state of the DHCPv4 Service.')
bcnDhcpv4SerOperState = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("running", 1), ("notRunning", 2), ("starting", 3), ("stopping", 4), ("fault", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnDhcpv4SerOperState.setStatus('current')
if mibBuilder.loadTexts: bcnDhcpv4SerOperState.setDescription('Operational state of the Service. The possible states are:\n        running(1)    The service is running normally.\n        notRunning(2) The service is stopped either intentionally (i.e.:\n                      the service is not supposed to run on this node) or\n                      unintentionally (a problem has occurred).\n        starting(3)   The service is in the process of starting, either\n                      for the first time of after an event occurred.\n        stopping(4)   The service is in the process of stopping. Stopping\n                      a service might be necessary after a configuration\n                      change.\n        fault(5)      An error has been detected and the state is undefined.\n        ')
bcnDhcpv4FirstAlertIpAddr = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 2, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnDhcpv4FirstAlertIpAddr.setStatus('current')
if mibBuilder.loadTexts: bcnDhcpv4FirstAlertIpAddr.setDescription('The IP address identifying either subnet or pool for which\n        the available IPs have been exhausted.')
bcnDhcpv4LeaseStatsSuccess = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 2, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnDhcpv4LeaseStatsSuccess.setStatus('current')
if mibBuilder.loadTexts: bcnDhcpv4LeaseStatsSuccess.setDescription('The number of successful DHCPv4 leases issued per second.')
bcnDhcpv4ServiceStatistics = ObjectIdentity((1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 2, 2))
if mibBuilder.loadTexts: bcnDhcpv4ServiceStatistics.setStatus('current')
if mibBuilder.loadTexts: bcnDhcpv4ServiceStatistics.setDescription('General state of the DHCPv4 Service.')
bcnDhcpv4LeaseTable = MibTable((1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 2, 2, 1), )
if mibBuilder.loadTexts: bcnDhcpv4LeaseTable.setStatus('current')
if mibBuilder.loadTexts: bcnDhcpv4LeaseTable.setDescription('Current lease table.')
bcnDhcpv4LeaseEntry = MibTableRow((1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 2, 2, 1, 1), ).setIndexNames((0, "BCN-DHCPV4-MIB", "bcnDhcpv4LeaseIP"))
if mibBuilder.loadTexts: bcnDhcpv4LeaseEntry.setStatus('current')
if mibBuilder.loadTexts: bcnDhcpv4LeaseEntry.setDescription('A logical row in the bcnDhcpv4LeaseTable.')
bcnDhcpv4LeaseIP = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 2, 2, 1, 1, 1), IpAddress())
if mibBuilder.loadTexts: bcnDhcpv4LeaseIP.setStatus('current')
if mibBuilder.loadTexts: bcnDhcpv4LeaseIP.setDescription('IP address of the lease.')
bcnDhcpv4LeaseStartTime = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 2, 2, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnDhcpv4LeaseStartTime.setStatus('current')
if mibBuilder.loadTexts: bcnDhcpv4LeaseStartTime.setDescription('Start time of the lease.')
bcnDhcpv4LeaseEndTime = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 2, 2, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnDhcpv4LeaseEndTime.setStatus('current')
if mibBuilder.loadTexts: bcnDhcpv4LeaseEndTime.setDescription('End time of the lease.')
bcnDhcpv4LeaseTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 2, 2, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnDhcpv4LeaseTimeStamp.setStatus('current')
if mibBuilder.loadTexts: bcnDhcpv4LeaseTimeStamp.setDescription('When failover protocol is being used the timestamp will\n        indicate the time the peer has either been told the lease expires,\n        or the expiry time that the peer has acknowledged.')
bcnDhcpv4LeaseMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 2, 2, 1, 1, 5), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnDhcpv4LeaseMacAddress.setStatus('current')
if mibBuilder.loadTexts: bcnDhcpv4LeaseMacAddress.setDescription('The hardware address (MAC address) of this lease.')
bcnDhcpv4LeaseHostname = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 2, 2, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnDhcpv4LeaseHostname.setStatus('current')
if mibBuilder.loadTexts: bcnDhcpv4LeaseHostname.setDescription('The client hostname of the lease.')
bcnDhcpv4SubnetTable = MibTable((1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 2, 2, 2), )
if mibBuilder.loadTexts: bcnDhcpv4SubnetTable.setStatus('current')
if mibBuilder.loadTexts: bcnDhcpv4SubnetTable.setDescription('Current subnet table.')
bcnDhcpv4SubnetEntry = MibTableRow((1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 2, 2, 2, 1), ).setIndexNames((0, "BCN-DHCPV4-MIB", "bcnDhcpv4SubnetIP"))
if mibBuilder.loadTexts: bcnDhcpv4SubnetEntry.setStatus('current')
if mibBuilder.loadTexts: bcnDhcpv4SubnetEntry.setDescription('A logical row in the bcnDhcpv4SubnetTable.')
bcnDhcpv4SubnetIP = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 2, 2, 2, 1, 1), IpAddress())
if mibBuilder.loadTexts: bcnDhcpv4SubnetIP.setStatus('current')
if mibBuilder.loadTexts: bcnDhcpv4SubnetIP.setDescription('IP address of the subnet.')
bcnDhcpv4SubnetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 2, 2, 2, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnDhcpv4SubnetMask.setStatus('current')
if mibBuilder.loadTexts: bcnDhcpv4SubnetMask.setDescription('IP mask of the subnet.')
bcnDhcpv4SubnetSize = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 2, 2, 2, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnDhcpv4SubnetSize.setStatus('current')
if mibBuilder.loadTexts: bcnDhcpv4SubnetSize.setDescription('Size of the subnet. The size of the subnet is calculated\n      as the sum of the sizes of each pool defined within it. The pools\n      are defined such that the fixed IPs are not contained within them.')
bcnDhcpv4SubnetFreeAddresses = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 2, 2, 2, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnDhcpv4SubnetFreeAddresses.setStatus('current')
if mibBuilder.loadTexts: bcnDhcpv4SubnetFreeAddresses.setDescription('The number of IPs addresses available in this subnet.')
bcnDhcpv4SubnetLowThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 2, 2, 2, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnDhcpv4SubnetLowThreshold.setStatus('current')
if mibBuilder.loadTexts: bcnDhcpv4SubnetLowThreshold.setDescription('Low threshold for available free addresses in this\n        subnet.  If the value for available free addresses in this \n        subnet becomes equal to or less than this value, a \n        bcnDhcpv4SubnetLowNotif event is generated for this subnet.\n        No more bcnDhcpv4SubnetLowNotif events will be generated for\n        this subnet during this execution of the DHCPv4 server until\n        the value for available free addresses has exceeded the value\n        of bcnDhcpv4SubnetHighThreshold.')
bcnDhcpv4SubnetHighThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 2, 2, 2, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnDhcpv4SubnetHighThreshold.setStatus('current')
if mibBuilder.loadTexts: bcnDhcpv4SubnetHighThreshold.setDescription('High threshold for available free addresses in this\n        subnet.  If a bcnDhcpv4SubnetLowNotif event was generated and\n        the value for available free addresses in this subnet has\n        exceeded this value, a bcnDhcpv4SubnetHighNotif event is \n        generated for this subnet.\n        No more bcnDhcpv4SubnetHighNotif events will be generated for\n        this subnet during this execution of the DHCPv4 server until\n        another bcnDhcpv4SubnetLowNotif is generated.')
bcnDhcpv4PoolTable = MibTable((1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 2, 2, 3), )
if mibBuilder.loadTexts: bcnDhcpv4PoolTable.setStatus('current')
if mibBuilder.loadTexts: bcnDhcpv4PoolTable.setDescription('Current pool table.')
bcnDhcpv4PoolEntry = MibTableRow((1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 2, 2, 3, 1), ).setIndexNames((0, "BCN-DHCPV4-MIB", "bcnDhcpv4PoolStartIP"))
if mibBuilder.loadTexts: bcnDhcpv4PoolEntry.setStatus('current')
if mibBuilder.loadTexts: bcnDhcpv4PoolEntry.setDescription('A logical row in the bcnDhcpv4PoolTable.')
bcnDhcpv4PoolStartIP = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 2, 2, 3, 1, 1), IpAddress())
if mibBuilder.loadTexts: bcnDhcpv4PoolStartIP.setStatus('current')
if mibBuilder.loadTexts: bcnDhcpv4PoolStartIP.setDescription('Start IP address of this pool.')
bcnDhcpv4PoolEndIP = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 2, 2, 3, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnDhcpv4PoolEndIP.setStatus('current')
if mibBuilder.loadTexts: bcnDhcpv4PoolEndIP.setDescription('End IP address of this pool.')
bcnDhcpv4PoolSubnetIP = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 2, 2, 3, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnDhcpv4PoolSubnetIP.setStatus('current')
if mibBuilder.loadTexts: bcnDhcpv4PoolSubnetIP.setDescription('Subnet IP address of the pool.')
bcnDhcpv4PoolSize = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 2, 2, 3, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnDhcpv4PoolSize.setStatus('current')
if mibBuilder.loadTexts: bcnDhcpv4PoolSize.setDescription('The size of this pool.')
bcnDhcpv4PoolFreeAddresses = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 2, 2, 3, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnDhcpv4PoolFreeAddresses.setStatus('current')
if mibBuilder.loadTexts: bcnDhcpv4PoolFreeAddresses.setDescription('The number of IPs addresses available in this pool.')
bcnDhcpv4FixedIPTable = MibTable((1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 2, 2, 4), )
if mibBuilder.loadTexts: bcnDhcpv4FixedIPTable.setStatus('current')
if mibBuilder.loadTexts: bcnDhcpv4FixedIPTable.setDescription('List of fixed IP addresses for this DHCPv4 server.')
bcnDhcpv4FixedIPEntry = MibTableRow((1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 2, 2, 4, 1), ).setIndexNames((0, "BCN-DHCPV4-MIB", "bcnDhcpv4FixedIP"))
if mibBuilder.loadTexts: bcnDhcpv4FixedIPEntry.setStatus('current')
if mibBuilder.loadTexts: bcnDhcpv4FixedIPEntry.setDescription('A logical row in the bcnDhcpv4FixedIPTable.')
bcnDhcpv4FixedIP = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 2, 2, 4, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnDhcpv4FixedIP.setStatus('current')
if mibBuilder.loadTexts: bcnDhcpv4FixedIP.setDescription('One of the fixed IP addresses in the DHCPv4\n        configuration.')
bcnDhcpv4NotificationEvents = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 3, 0))
bcnDhcpv4NotificationData = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 3, 1))
bcnDhcpv4AlarmSeverity = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 3, 1, 1), BcnAlarmSeverity()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bcnDhcpv4AlarmSeverity.setStatus('current')
if mibBuilder.loadTexts: bcnDhcpv4AlarmSeverity.setDescription('Severity classification for the alarm.')
bcnDhcpv4AlarmInfo = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 3, 1, 2), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bcnDhcpv4AlarmInfo.setStatus('current')
if mibBuilder.loadTexts: bcnDhcpv4AlarmInfo.setDescription('Descriptive information about the alarm event.')
bcnDhcpv4FailOverState = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 254))).clone(namedValues=NamedValues(("startup", 1), ("normal", 2), ("communicationsInterrupted", 3), ("partnerDown", 4), ("potentialConflict", 5), ("recover", 6), ("paused", 7), ("shutdown", 8), ("recoverDone", 9), ("recoverWait", 254)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bcnDhcpv4FailOverState.setStatus('current')
if mibBuilder.loadTexts: bcnDhcpv4FailOverState.setDescription('The state of DHCPv4 failover.')
bcnDhcpv4SubnetAlertIpAddr = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 3, 1, 4), IpAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bcnDhcpv4SubnetAlertIpAddr.setStatus('current')
if mibBuilder.loadTexts: bcnDhcpv4SubnetAlertIpAddr.setDescription('The IP address identifying a subnet for which the \n        available IPs have been exhausted.')
bcnDhcpv4AlarmNotif = NotificationType((1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 3, 0, 1)).setObjects(("BCN-DHCPV4-MIB", "bcnDhcpv4SerOperState"), ("BCN-DHCPV4-MIB", "bcnDhcpv4AlarmSeverity"), ("BCN-DHCPV4-MIB", "bcnDhcpv4AlarmInfo"))
if mibBuilder.loadTexts: bcnDhcpv4AlarmNotif.setStatus('current')
if mibBuilder.loadTexts: bcnDhcpv4AlarmNotif.setDescription('A bcnDhcpv4AlarmNotif signifies that the DHCPv4 service has\n        transitioned state or a particular event has been detected\n        on the service.')
bcnDhcpv4FailOverNotif = NotificationType((1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 3, 0, 2)).setObjects(("BCN-DHCPV4-MIB", "bcnDhcpv4FailOverState"))
if mibBuilder.loadTexts: bcnDhcpv4FailOverNotif.setStatus('current')
if mibBuilder.loadTexts: bcnDhcpv4FailOverNotif.setDescription('A change of state has been detected on the DHCPv4 failover\n         mechanism.')
bcnDhcpv4SubnetLowNotif = NotificationType((1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 3, 0, 3)).setObjects(("BCN-DHCPV4-MIB", "bcnDhcpv4SubnetAlertIpAddr"), ("BCN-DHCPV4-MIB", "bcnDhcpv4SubnetFreeAddresses"), ("BCN-DHCPV4-MIB", "bcnDhcpv4SubnetLowThreshold"))
if mibBuilder.loadTexts: bcnDhcpv4SubnetLowNotif.setStatus('current')
if mibBuilder.loadTexts: bcnDhcpv4SubnetLowNotif.setDescription('This notification signifies that the number of available IPv4\n        addresses for a particular subnet has fallen below the value\n        of bcnDhcpv4SubnetLowThreshold for that subnet.')
bcnDhcpv4SubnetHighNotif = NotificationType((1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 3, 0, 4)).setObjects(("BCN-DHCPV4-MIB", "bcnDhcpv4SubnetAlertIpAddr"), ("BCN-DHCPV4-MIB", "bcnDhcpv4SubnetFreeAddresses"), ("BCN-DHCPV4-MIB", "bcnDhcpv4SubnetHighThreshold"))
if mibBuilder.loadTexts: bcnDhcpv4SubnetHighNotif.setStatus('current')
if mibBuilder.loadTexts: bcnDhcpv4SubnetHighNotif.setDescription('This notification signifies that the number of available IPv4\n        addresses for a particular subnet has risen above the value\n        of bcnDhcpv4SubnetHighThreshold for that subnet.')
bcnDhcpv4ServiceCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 4, 1))
bcnDhcpv4ServiceGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 4, 2))
bcnDhcpv4ServiceStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 4, 2, 1)).setObjects(("BCN-DHCPV4-MIB", "bcnDhcpv4SerOperState"), ("BCN-DHCPV4-MIB", "bcnDhcpv4FirstAlertIpAddr"), ("BCN-DHCPV4-MIB", "bcnDhcpv4LeaseStatsSuccess"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bcnDhcpv4ServiceStatusGroup = bcnDhcpv4ServiceStatusGroup.setStatus('current')
if mibBuilder.loadTexts: bcnDhcpv4ServiceStatusGroup.setDescription('Status conformance.')
bcnDhcpv4StatisticsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 4, 2, 2)).setObjects(("BCN-DHCPV4-MIB", "bcnDhcpv4LeaseStartTime"), ("BCN-DHCPV4-MIB", "bcnDhcpv4LeaseEndTime"), ("BCN-DHCPV4-MIB", "bcnDhcpv4LeaseTimeStamp"), ("BCN-DHCPV4-MIB", "bcnDhcpv4LeaseMacAddress"), ("BCN-DHCPV4-MIB", "bcnDhcpv4LeaseHostname"), ("BCN-DHCPV4-MIB", "bcnDhcpv4SubnetMask"), ("BCN-DHCPV4-MIB", "bcnDhcpv4SubnetSize"), ("BCN-DHCPV4-MIB", "bcnDhcpv4SubnetFreeAddresses"), ("BCN-DHCPV4-MIB", "bcnDhcpv4SubnetLowThreshold"), ("BCN-DHCPV4-MIB", "bcnDhcpv4SubnetHighThreshold"), ("BCN-DHCPV4-MIB", "bcnDhcpv4PoolSubnetIP"), ("BCN-DHCPV4-MIB", "bcnDhcpv4PoolEndIP"), ("BCN-DHCPV4-MIB", "bcnDhcpv4PoolSize"), ("BCN-DHCPV4-MIB", "bcnDhcpv4PoolFreeAddresses"), ("BCN-DHCPV4-MIB", "bcnDhcpv4FixedIP"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bcnDhcpv4StatisticsGroup = bcnDhcpv4StatisticsGroup.setStatus('current')
if mibBuilder.loadTexts: bcnDhcpv4StatisticsGroup.setDescription('Server statistics conformance.')
bcnDhcpv4NotificationEventGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 4, 2, 3)).setObjects(("BCN-DHCPV4-MIB", "bcnDhcpv4AlarmNotif"), ("BCN-DHCPV4-MIB", "bcnDhcpv4FailOverNotif"), ("BCN-DHCPV4-MIB", "bcnDhcpv4SubnetLowNotif"), ("BCN-DHCPV4-MIB", "bcnDhcpv4SubnetHighNotif"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bcnDhcpv4NotificationEventGroup = bcnDhcpv4NotificationEventGroup.setStatus('current')
if mibBuilder.loadTexts: bcnDhcpv4NotificationEventGroup.setDescription('Server statistics conformance.')
bcnDhcpv4NotificationDataGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 4, 2, 4)).setObjects(("BCN-DHCPV4-MIB", "bcnDhcpv4AlarmSeverity"), ("BCN-DHCPV4-MIB", "bcnDhcpv4AlarmInfo"), ("BCN-DHCPV4-MIB", "bcnDhcpv4FailOverState"), ("BCN-DHCPV4-MIB", "bcnDhcpv4SubnetAlertIpAddr"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bcnDhcpv4NotificationDataGroup = bcnDhcpv4NotificationDataGroup.setStatus('current')
if mibBuilder.loadTexts: bcnDhcpv4NotificationDataGroup.setDescription('Server statistics conformance.')
bcnDhcpv4StatusCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 13315, 3, 1, 1, 4, 1, 1)).setObjects(("BCN-DHCPV4-MIB", "bcnDhcpv4ServiceStatusGroup"), ("BCN-DHCPV4-MIB", "bcnDhcpv4StatisticsGroup"), ("BCN-DHCPV4-MIB", "bcnDhcpv4NotificationEventGroup"), ("BCN-DHCPV4-MIB", "bcnDhcpv4NotificationDataGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bcnDhcpv4StatusCompliance = bcnDhcpv4StatusCompliance.setStatus('current')
if mibBuilder.loadTexts: bcnDhcpv4StatusCompliance.setDescription('Basic conformance')
mibBuilder.exportSymbols("BCN-DHCPV4-MIB", bcnDhcpv4LeaseTimeStamp=bcnDhcpv4LeaseTimeStamp, bcnDhcpv4FixedIP=bcnDhcpv4FixedIP, bcnDhcpv4ServiceStatistics=bcnDhcpv4ServiceStatistics, bcnDhcpv4ServiceGroups=bcnDhcpv4ServiceGroups, bcnDhcpv4PoolEndIP=bcnDhcpv4PoolEndIP, bcnDhcpv4Conformance=bcnDhcpv4Conformance, bcnDhcpv4LeaseStatsSuccess=bcnDhcpv4LeaseStatsSuccess, bcnDhcpv4LeaseTable=bcnDhcpv4LeaseTable, bcnDhcpv4AlarmInfo=bcnDhcpv4AlarmInfo, bcnDhcpv4FailOverState=bcnDhcpv4FailOverState, bcnDhcpv4ServiceStatusGroup=bcnDhcpv4ServiceStatusGroup, bcnDhcpv4SubnetFreeAddresses=bcnDhcpv4SubnetFreeAddresses, bcnDhcpv4StatusCompliance=bcnDhcpv4StatusCompliance, bcnDhcpv4ServiceStatus=bcnDhcpv4ServiceStatus, bcnDhcpv4Objects=bcnDhcpv4Objects, bcnDhcpv4SubnetHighThreshold=bcnDhcpv4SubnetHighThreshold, bcnDhcpv4FailOverNotif=bcnDhcpv4FailOverNotif, bcnDhcpv4LeaseIP=bcnDhcpv4LeaseIP, bcnDhcpv4FirstAlertIpAddr=bcnDhcpv4FirstAlertIpAddr, bcnDhcpv4PoolSubnetIP=bcnDhcpv4PoolSubnetIP, bcnDhcpv4PoolFreeAddresses=bcnDhcpv4PoolFreeAddresses, bcnDhcpv4FixedIPTable=bcnDhcpv4FixedIPTable, PYSNMP_MODULE_ID=bcnDhcpv4MIB, bcnDhcpv4=bcnDhcpv4, bcnDhcpv4SubnetLowNotif=bcnDhcpv4SubnetLowNotif, bcnDhcpv4NotificationEventGroup=bcnDhcpv4NotificationEventGroup, bcnDhcpv4PoolStartIP=bcnDhcpv4PoolStartIP, bcnDhcpv4Notification=bcnDhcpv4Notification, bcnDhcpv4LeaseEndTime=bcnDhcpv4LeaseEndTime, bcnDhcpv4SubnetAlertIpAddr=bcnDhcpv4SubnetAlertIpAddr, bcnDhcpv4StatisticsGroup=bcnDhcpv4StatisticsGroup, bcnDhcpv4LeaseEntry=bcnDhcpv4LeaseEntry, bcnDhcpv4SubnetEntry=bcnDhcpv4SubnetEntry, bcnDhcpv4SerOperState=bcnDhcpv4SerOperState, bcnDhcpv4SubnetIP=bcnDhcpv4SubnetIP, bcnDhcpv4PoolTable=bcnDhcpv4PoolTable, bcnDhcpv4NotificationDataGroup=bcnDhcpv4NotificationDataGroup, bcnDhcpv4NotificationEvents=bcnDhcpv4NotificationEvents, bcnDhcpv4PoolSize=bcnDhcpv4PoolSize, bcnDhcpv4LeaseMacAddress=bcnDhcpv4LeaseMacAddress, bcnDhcpv4AlarmSeverity=bcnDhcpv4AlarmSeverity, bcnDhcpv4SubnetHighNotif=bcnDhcpv4SubnetHighNotif, bcnDhcpv4AlarmNotif=bcnDhcpv4AlarmNotif, bcnDhcpv4PoolEntry=bcnDhcpv4PoolEntry, bcnDhcpv4NotificationData=bcnDhcpv4NotificationData, bcnDhcpv4SubnetLowThreshold=bcnDhcpv4SubnetLowThreshold, bcnDhcpv4LeaseHostname=bcnDhcpv4LeaseHostname, bcnDhcpv4SubnetSize=bcnDhcpv4SubnetSize, bcnDhcpv4SubnetMask=bcnDhcpv4SubnetMask, bcnDhcpv4ServiceCompliances=bcnDhcpv4ServiceCompliances, bcnDhcpv4SubnetTable=bcnDhcpv4SubnetTable, bcnDhcpv4LeaseStartTime=bcnDhcpv4LeaseStartTime, bcnDhcpv4MIB=bcnDhcpv4MIB, bcnDhcpv4FixedIPEntry=bcnDhcpv4FixedIPEntry)
