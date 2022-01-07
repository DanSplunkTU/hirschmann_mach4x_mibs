#
# PySNMP MIB module VRRP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/VRRP-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:07:50 2022
# On host fv-az36-988 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Bits, Counter64, Unsigned32, mib_2, ModuleIdentity, NotificationType, Counter32, TimeTicks, IpAddress, Integer32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, iso, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter64", "Unsigned32", "mib-2", "ModuleIdentity", "NotificationType", "Counter32", "TimeTicks", "IpAddress", "Integer32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "iso", "Gauge32")
TextualConvention, MacAddress, TruthValue, TimeStamp, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "MacAddress", "TruthValue", "TimeStamp", "RowStatus", "DisplayString")
vrrpMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 68))
vrrpMIB.setRevisions(('2000-03-03 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: vrrpMIB.setRevisionsDescriptions(('Initial version as published in RFC 2787.',))
if mibBuilder.loadTexts: vrrpMIB.setLastUpdated('200003030000Z')
if mibBuilder.loadTexts: vrrpMIB.setOrganization('IETF VRRP Working Group')
if mibBuilder.loadTexts: vrrpMIB.setContactInfo('Brian R. Jewell\n     Postal: Copper Mountain Networks, Inc.\n             2470 Embarcadero Way\n             Palo Alto, California 94303\n     Tel:    +1 650 687 3367\n     E-Mail: bjewell@coppermountain.com')
if mibBuilder.loadTexts: vrrpMIB.setDescription('This MIB describes objects used for managing Virtual Router\n          Redundancy Protocol (VRRP) routers.')
class VrId(TextualConvention, Integer32):
    description = 'A number which, along with an interface index (ifIndex),\n         serves to uniquely identify a virtual router on a given VRRP\n         router. A set of one or more associated addresses is assigned\n         to a VRID.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 255)

vrrpOperations = MibIdentifier((1, 3, 6, 1, 2, 1, 68, 1))
vrrpStatistics = MibIdentifier((1, 3, 6, 1, 2, 1, 68, 2))
vrrpConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 68, 3))
vrrpNodeVersion = MibScalar((1, 3, 6, 1, 2, 1, 68, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpNodeVersion.setStatus('current')
if mibBuilder.loadTexts: vrrpNodeVersion.setDescription('This value identifies the particular version of the VRRP\n         supported by this node.')
vrrpNotificationCntl = MibScalar((1, 3, 6, 1, 2, 1, 68, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vrrpNotificationCntl.setStatus('current')
if mibBuilder.loadTexts: vrrpNotificationCntl.setDescription("Indicates whether the VRRP-enabled router will generate\n         SNMP traps for events defined in this MIB. 'Enabled'\n         results in SNMP traps; 'disabled', no traps are sent.")
vrrpOperTable = MibTable((1, 3, 6, 1, 2, 1, 68, 1, 3), )
if mibBuilder.loadTexts: vrrpOperTable.setStatus('current')
if mibBuilder.loadTexts: vrrpOperTable.setDescription("Operations table for a VRRP router which consists of a\n          sequence (i.e., one or more conceptual rows) of\n          'vrrpOperEntry' items.")
vrrpOperEntry = MibTableRow((1, 3, 6, 1, 2, 1, 68, 1, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "VRRP-MIB", "vrrpOperVrId"))
if mibBuilder.loadTexts: vrrpOperEntry.setStatus('current')
if mibBuilder.loadTexts: vrrpOperEntry.setDescription("An entry in the vrrpOperTable containing the operational\n          characteristics of a virtual router. On a VRRP router,\n          a given virtual router is identified by a combination\n          of the IF index and VRID.\n\n          Rows in the table cannot be modified unless the value\n          of `vrrpOperAdminState' is `disabled' and the\n          `vrrpOperState' has transitioned to `initialize'.")
vrrpOperVrId = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 1, 3, 1, 1), VrId())
if mibBuilder.loadTexts: vrrpOperVrId.setStatus('current')
if mibBuilder.loadTexts: vrrpOperVrId.setDescription('This object contains the Virtual Router Identifier (VRID).')
vrrpOperVirtualMacAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 1, 3, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpOperVirtualMacAddr.setStatus('current')
if mibBuilder.loadTexts: vrrpOperVirtualMacAddr.setDescription("The virtual MAC address of the virtual router. Although this\n         object can be derived from the 'vrrpOperVrId' object, it is\n         defined so that it is easily obtainable by a management\n         application and can be included in VRRP-related SNMP traps.")
vrrpOperState = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("initialize", 1), ("backup", 2), ("master", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpOperState.setStatus('current')
if mibBuilder.loadTexts: vrrpOperState.setDescription("The current state of the virtual router. This object has\n         three defined values:\n\n           - `initialize', which indicates that all the\n             virtual router is waiting for a startup event.\n\n           - `backup', which indicates the virtual router is\n             monitoring the availability of the master router.\n\n           - `master', which indicates that the virtual router\n             is forwarding packets for IP addresses that are\n             associated with this router.\n\n         Setting the `vrrpOperAdminState' object (below) initiates\n         transitions in the value of this object.")
vrrpOperAdminState = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 1, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2))).clone('down')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vrrpOperAdminState.setStatus('current')
if mibBuilder.loadTexts: vrrpOperAdminState.setDescription("This object will enable/disable the virtual router\n         function. Setting the value to `up', will transition\n         the state of the virtual router from `initialize' to `backup'\n         or `master', depending on the value of `vrrpOperPriority'.\n         Setting the value to `down', will transition  the\n         router from `master' or `backup' to `initialize'. State\n         transitions may not be immediate; they sometimes depend on\n         other factors, such as the interface (IF) state.\n\n         The `vrrpOperAdminState' object must be set to `down' prior\n         to modifying the other read-create objects in the conceptual\n         row. The value of the `vrrpOperRowStatus' object (below)\n         must be `active', signifying that the conceptual row\n         is valid (i.e., the objects are correctly set),\n         in order for this object to be set to `up'.")
vrrpOperPriority = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 1, 3, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)).clone(100)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vrrpOperPriority.setStatus('current')
if mibBuilder.loadTexts: vrrpOperPriority.setDescription("This object specifies the priority to be used for the\n         virtual router master election process. Higher values imply\n         higher priority.\n\n         A priority of '0', although not settable, is sent by\n         the master router to indicate that this router has ceased\n         to participate in VRRP and a backup virtual router should\n         transition  to become a new master.\n\n         A priority of 255 is used for the router that owns the\n         associated IP address(es).")
vrrpOperIpAddrCount = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 1, 3, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpOperIpAddrCount.setStatus('current')
if mibBuilder.loadTexts: vrrpOperIpAddrCount.setDescription('The number of IP addresses that are associated with this\n         virtual router. This number is equal to the number of rows\n         in the vrrpAssoIpAddrTable that correspond to a given IF\n         index/VRID pair.')
vrrpOperMasterIpAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 1, 3, 1, 7), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpOperMasterIpAddr.setStatus('current')
if mibBuilder.loadTexts: vrrpOperMasterIpAddr.setDescription("The master router's real (primary) IP address. This is\n         the IP address listed as the source in VRRP advertisement\n         last received by this virtual router.")
vrrpOperPrimaryIpAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 1, 3, 1, 8), IpAddress().clone(hexValue="00000000")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vrrpOperPrimaryIpAddr.setStatus('current')
if mibBuilder.loadTexts: vrrpOperPrimaryIpAddr.setDescription("In the case where there is more than one IP address for\n         a given `ifIndex', this object is used to specify the IP\n         address that will become the `vrrpOperMasterIpAddr', should\n         the virtual router transition from backup to master. If\n         this object is set to 0.0.0.0, the IP address which is\n         numerically lowest will be selected.")
vrrpOperAuthType = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 1, 3, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAuthentication", 1), ("simpleTextPassword", 2), ("ipAuthenticationHeader", 3))).clone('noAuthentication')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vrrpOperAuthType.setStatus('current')
if mibBuilder.loadTexts: vrrpOperAuthType.setDescription('Authentication type used for VRRP protocol exchanges between\n         virtual routers. This value of this object is the same for a\n         given ifIndex.\n\n         New enumerations to this list can only be added via a new\n         RFC on the standards track.')
vrrpOperAuthKey = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 1, 3, 1, 10), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vrrpOperAuthKey.setStatus('current')
if mibBuilder.loadTexts: vrrpOperAuthKey.setDescription("The Authentication Key. This object is set according to\n         the value of the 'vrrpOperAuthType' object\n         ('simpleTextPassword' or 'ipAuthenticationHeader'). If the\n         length of the value is less than 16 octets, the agent will\n         left adjust and zero fill to 16 octets. The value of this\n         object is the same for a given ifIndex.\n\n         When read, vrrpOperAuthKey always returns an Octet String\n         of length zero.")
vrrpOperAdvertisementInterval = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 1, 3, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)).clone(1)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: vrrpOperAdvertisementInterval.setStatus('current')
if mibBuilder.loadTexts: vrrpOperAdvertisementInterval.setDescription('The time interval, in seconds, between sending\n         advertisement messages. Only the master router sends\n         VRRP advertisements.')
vrrpOperPreemptMode = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 1, 3, 1, 12), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vrrpOperPreemptMode.setStatus('current')
if mibBuilder.loadTexts: vrrpOperPreemptMode.setDescription('Controls whether a higher priority virtual router will\n         preempt a lower priority master.')
vrrpOperVirtualRouterUpTime = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 1, 3, 1, 13), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpOperVirtualRouterUpTime.setStatus('current')
if mibBuilder.loadTexts: vrrpOperVirtualRouterUpTime.setDescription("This is the value of the `sysUpTime' object when this\n         virtual router (i.e., the `vrrpOperState') transitioned\n         out of `initialized'.")
vrrpOperProtocol = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 1, 3, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("ip", 1), ("bridge", 2), ("decnet", 3), ("other", 4))).clone('ip')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vrrpOperProtocol.setStatus('current')
if mibBuilder.loadTexts: vrrpOperProtocol.setDescription('The particular protocol being controlled by this Virtual\n         Router.\n\n         New enumerations to this list can only be added via a new\n         RFC on the standards track.')
vrrpOperRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 1, 3, 1, 15), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vrrpOperRowStatus.setStatus('current')
if mibBuilder.loadTexts: vrrpOperRowStatus.setDescription("The row status variable, used in accordance to installation\n         and removal conventions for conceptual rows. The rowstatus of\n         a currently active row in the vrrpOperTable is constrained\n         by the operational state of the corresponding virtual router.\n         When `vrrpOperRowStatus' is set to active(1), no other\n         objects in the conceptual row, with the exception of\n         `vrrpOperAdminState', can be modified. Prior to setting the\n         `vrrpOperRowStatus' object from `active' to a different value,\n         the `vrrpOperAdminState' object must be set to `down' and the\n         `vrrpOperState' object be transitioned to `initialize'.\n\n         To create a row in this table, a manager sets this object\n         to either createAndGo(4) or createAndWait(5). Until instances\n         of all corresponding columns are appropriately configured,\n         the value of the corresponding instance of the `vrrpOperRowStatus'\n         column will be read as notReady(3).\n         In particular, a newly created row cannot be made active(1)\n         until (minimally) the corresponding instance of\n         `vrrpOperVrId' has been set and there is at least one active\n         row in the `vrrpAssoIpAddrTable' defining an associated\n         IP address for the virtual router.")
vrrpAssoIpAddrTable = MibTable((1, 3, 6, 1, 2, 1, 68, 1, 4), )
if mibBuilder.loadTexts: vrrpAssoIpAddrTable.setStatus('current')
if mibBuilder.loadTexts: vrrpAssoIpAddrTable.setDescription('The table of addresses associated with this virtual router.')
vrrpAssoIpAddrEntry = MibTableRow((1, 3, 6, 1, 2, 1, 68, 1, 4, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "VRRP-MIB", "vrrpOperVrId"), (0, "VRRP-MIB", "vrrpAssoIpAddr"))
if mibBuilder.loadTexts: vrrpAssoIpAddrEntry.setStatus('current')
if mibBuilder.loadTexts: vrrpAssoIpAddrEntry.setDescription("An entry in the table contains an IP address that is\n         associated with a virtual router. The number of rows for\n         a given ifIndex and VrId will equal the number of IP\n         addresses associated (e.g., backed up) by the virtual\n         router (equivalent to 'vrrpOperIpAddrCount').\n\n         Rows in the table cannot be modified unless the value\n         of `vrrpOperAdminState' is `disabled' and the\n         `vrrpOperState' has transitioned to `initialize'.")
vrrpAssoIpAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 1, 4, 1, 1), IpAddress())
if mibBuilder.loadTexts: vrrpAssoIpAddr.setStatus('current')
if mibBuilder.loadTexts: vrrpAssoIpAddr.setDescription('The assigned IP addresses that a virtual router is\n         responsible for backing up.')
vrrpAssoIpAddrRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 1, 4, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vrrpAssoIpAddrRowStatus.setStatus('current')
if mibBuilder.loadTexts: vrrpAssoIpAddrRowStatus.setDescription('The row status variable, used according to installation\n         and removal conventions for conceptual rows. Setting this\n         object to active(1) or createAndGo(4) results in the\n         addition of an associated address for a virtual router.\n         Destroying the entry or setting it to notInService(2)\n         removes the associated address from the virtual router.\n         The use of other values is implementation-dependent.')
vrrpRouterChecksumErrors = MibScalar((1, 3, 6, 1, 2, 1, 68, 2, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpRouterChecksumErrors.setStatus('current')
if mibBuilder.loadTexts: vrrpRouterChecksumErrors.setDescription('The total number of VRRP packets received with an invalid\n         VRRP checksum value.')
vrrpRouterVersionErrors = MibScalar((1, 3, 6, 1, 2, 1, 68, 2, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpRouterVersionErrors.setStatus('current')
if mibBuilder.loadTexts: vrrpRouterVersionErrors.setDescription('The total number of VRRP packets received with an unknown\n         or unsupported version number.')
vrrpRouterVrIdErrors = MibScalar((1, 3, 6, 1, 2, 1, 68, 2, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpRouterVrIdErrors.setStatus('current')
if mibBuilder.loadTexts: vrrpRouterVrIdErrors.setDescription('The total number of VRRP packets received with an invalid\n         VRID for this virtual router.')
vrrpRouterStatsTable = MibTable((1, 3, 6, 1, 2, 1, 68, 2, 4), )
if mibBuilder.loadTexts: vrrpRouterStatsTable.setStatus('current')
if mibBuilder.loadTexts: vrrpRouterStatsTable.setDescription('Table of virtual router statistics.')
vrrpRouterStatsEntry = MibTableRow((1, 3, 6, 1, 2, 1, 68, 2, 4, 1), )
vrrpOperEntry.registerAugmentions(("VRRP-MIB", "vrrpRouterStatsEntry"))
vrrpRouterStatsEntry.setIndexNames(*vrrpOperEntry.getIndexNames())
if mibBuilder.loadTexts: vrrpRouterStatsEntry.setStatus('current')
if mibBuilder.loadTexts: vrrpRouterStatsEntry.setDescription('An entry in the table, containing statistics information\n         about a given virtual router.')
vrrpStatsBecomeMaster = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 2, 4, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpStatsBecomeMaster.setStatus('current')
if mibBuilder.loadTexts: vrrpStatsBecomeMaster.setDescription("The total number of times that this virtual router's state\n         has transitioned to MASTER.")
vrrpStatsAdvertiseRcvd = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 2, 4, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpStatsAdvertiseRcvd.setStatus('current')
if mibBuilder.loadTexts: vrrpStatsAdvertiseRcvd.setDescription('The total number of VRRP advertisements received by this\n         virtual router.')
vrrpStatsAdvertiseIntervalErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 2, 4, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpStatsAdvertiseIntervalErrors.setStatus('current')
if mibBuilder.loadTexts: vrrpStatsAdvertiseIntervalErrors.setDescription('The total number of VRRP advertisement packets received\n         for which the advertisement interval is different than the\n         one configured for the local virtual router.')
vrrpStatsAuthFailures = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 2, 4, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpStatsAuthFailures.setStatus('current')
if mibBuilder.loadTexts: vrrpStatsAuthFailures.setDescription('The total number of VRRP packets received that do not pass\n         the authentication check.')
vrrpStatsIpTtlErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 2, 4, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpStatsIpTtlErrors.setStatus('current')
if mibBuilder.loadTexts: vrrpStatsIpTtlErrors.setDescription('The total number of VRRP packets received by the virtual\n         router with IP TTL (Time-To-Live) not equal to 255.')
vrrpStatsPriorityZeroPktsRcvd = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 2, 4, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpStatsPriorityZeroPktsRcvd.setStatus('current')
if mibBuilder.loadTexts: vrrpStatsPriorityZeroPktsRcvd.setDescription("The total number of VRRP packets received by the virtual\n         router with a priority of '0'.")
vrrpStatsPriorityZeroPktsSent = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 2, 4, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpStatsPriorityZeroPktsSent.setStatus('current')
if mibBuilder.loadTexts: vrrpStatsPriorityZeroPktsSent.setDescription("The total number of VRRP packets sent by the virtual router\n         with a priority of '0'.")
vrrpStatsInvalidTypePktsRcvd = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 2, 4, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpStatsInvalidTypePktsRcvd.setStatus('current')
if mibBuilder.loadTexts: vrrpStatsInvalidTypePktsRcvd.setDescription("The number of VRRP packets received by the virtual router\n         with an invalid value in the 'type' field.")
vrrpStatsAddressListErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 2, 4, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpStatsAddressListErrors.setStatus('current')
if mibBuilder.loadTexts: vrrpStatsAddressListErrors.setDescription('The total number of packets received for which the address\n         list does not match the locally configured list for the\n         virtual router.')
vrrpStatsInvalidAuthType = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 2, 4, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpStatsInvalidAuthType.setStatus('current')
if mibBuilder.loadTexts: vrrpStatsInvalidAuthType.setDescription('The total number of packets received with an unknown\n         authentication type.')
vrrpStatsAuthTypeMismatch = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 2, 4, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpStatsAuthTypeMismatch.setStatus('current')
if mibBuilder.loadTexts: vrrpStatsAuthTypeMismatch.setDescription("The total number of packets received with 'Auth Type' not\n         equal to the locally configured authentication method\n         (`vrrpOperAuthType').")
vrrpStatsPacketLengthErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 68, 2, 4, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpStatsPacketLengthErrors.setStatus('current')
if mibBuilder.loadTexts: vrrpStatsPacketLengthErrors.setDescription('The total number of packets received with a packet length\n         less than the length of the VRRP header.')
vrrpNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 68, 0))
vrrpTrapPacketSrc = MibScalar((1, 3, 6, 1, 2, 1, 68, 1, 5), IpAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: vrrpTrapPacketSrc.setStatus('current')
if mibBuilder.loadTexts: vrrpTrapPacketSrc.setDescription('The IP address of an inbound VRRP packet. Used by\n          vrrpTrapAuthFailure trap.')
vrrpTrapAuthErrorType = MibScalar((1, 3, 6, 1, 2, 1, 68, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("invalidAuthType", 1), ("authTypeMismatch", 2), ("authFailure", 3)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: vrrpTrapAuthErrorType.setStatus('current')
if mibBuilder.loadTexts: vrrpTrapAuthErrorType.setDescription('Potential types of configuration conflicts.\n         Used by vrrpAuthFailure trap.')
vrrpTrapNewMaster = NotificationType((1, 3, 6, 1, 2, 1, 68, 0, 1)).setObjects(("VRRP-MIB", "vrrpOperMasterIpAddr"))
if mibBuilder.loadTexts: vrrpTrapNewMaster.setStatus('current')
if mibBuilder.loadTexts: vrrpTrapNewMaster.setDescription("The newMaster trap indicates that the sending agent\n         has transitioned to 'Master' state.")
vrrpTrapAuthFailure = NotificationType((1, 3, 6, 1, 2, 1, 68, 0, 2)).setObjects(("VRRP-MIB", "vrrpTrapPacketSrc"), ("VRRP-MIB", "vrrpTrapAuthErrorType"))
if mibBuilder.loadTexts: vrrpTrapAuthFailure.setStatus('current')
if mibBuilder.loadTexts: vrrpTrapAuthFailure.setDescription("A vrrpAuthFailure trap signifies that a packet has\n         been received from a router whose authentication key\n         or authentication type conflicts with this router's\n         authentication key or authentication type. Implementation\n         of this trap is optional.")
vrrpMIBCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 68, 3, 1))
vrrpMIBGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 68, 3, 2))
vrrpMIBCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 68, 3, 1, 1)).setObjects(("VRRP-MIB", "vrrpOperGroup"), ("VRRP-MIB", "vrrpStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vrrpMIBCompliance = vrrpMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: vrrpMIBCompliance.setDescription('The core compliance statement for all VRRP implementations.')
vrrpOperGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 68, 3, 2, 1)).setObjects(("VRRP-MIB", "vrrpNodeVersion"), ("VRRP-MIB", "vrrpNotificationCntl"), ("VRRP-MIB", "vrrpOperVirtualMacAddr"), ("VRRP-MIB", "vrrpOperState"), ("VRRP-MIB", "vrrpOperAdminState"), ("VRRP-MIB", "vrrpOperPriority"), ("VRRP-MIB", "vrrpOperIpAddrCount"), ("VRRP-MIB", "vrrpOperMasterIpAddr"), ("VRRP-MIB", "vrrpOperPrimaryIpAddr"), ("VRRP-MIB", "vrrpOperAuthType"), ("VRRP-MIB", "vrrpOperAuthKey"), ("VRRP-MIB", "vrrpOperAdvertisementInterval"), ("VRRP-MIB", "vrrpOperPreemptMode"), ("VRRP-MIB", "vrrpOperVirtualRouterUpTime"), ("VRRP-MIB", "vrrpOperProtocol"), ("VRRP-MIB", "vrrpOperRowStatus"), ("VRRP-MIB", "vrrpAssoIpAddrRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vrrpOperGroup = vrrpOperGroup.setStatus('current')
if mibBuilder.loadTexts: vrrpOperGroup.setDescription('Conformance group for VRRP operations.')
vrrpStatsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 68, 3, 2, 2)).setObjects(("VRRP-MIB", "vrrpRouterChecksumErrors"), ("VRRP-MIB", "vrrpRouterVersionErrors"), ("VRRP-MIB", "vrrpRouterVrIdErrors"), ("VRRP-MIB", "vrrpStatsBecomeMaster"), ("VRRP-MIB", "vrrpStatsAdvertiseRcvd"), ("VRRP-MIB", "vrrpStatsAdvertiseIntervalErrors"), ("VRRP-MIB", "vrrpStatsAuthFailures"), ("VRRP-MIB", "vrrpStatsIpTtlErrors"), ("VRRP-MIB", "vrrpStatsPriorityZeroPktsRcvd"), ("VRRP-MIB", "vrrpStatsPriorityZeroPktsSent"), ("VRRP-MIB", "vrrpStatsInvalidTypePktsRcvd"), ("VRRP-MIB", "vrrpStatsAddressListErrors"), ("VRRP-MIB", "vrrpStatsInvalidAuthType"), ("VRRP-MIB", "vrrpStatsAuthTypeMismatch"), ("VRRP-MIB", "vrrpStatsPacketLengthErrors"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vrrpStatsGroup = vrrpStatsGroup.setStatus('current')
if mibBuilder.loadTexts: vrrpStatsGroup.setDescription('Conformance group for VRRP statistics.')
vrrpTrapGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 68, 3, 2, 3)).setObjects(("VRRP-MIB", "vrrpTrapPacketSrc"), ("VRRP-MIB", "vrrpTrapAuthErrorType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vrrpTrapGroup = vrrpTrapGroup.setStatus('current')
if mibBuilder.loadTexts: vrrpTrapGroup.setDescription('Conformance group for objects contained in VRRP notifications.')
vrrpNotificationGroup = NotificationGroup((1, 3, 6, 1, 2, 1, 68, 3, 2, 4)).setObjects(("VRRP-MIB", "vrrpTrapNewMaster"), ("VRRP-MIB", "vrrpTrapAuthFailure"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vrrpNotificationGroup = vrrpNotificationGroup.setStatus('current')
if mibBuilder.loadTexts: vrrpNotificationGroup.setDescription('The VRRP MIB Notification Group.')
mibBuilder.exportSymbols("VRRP-MIB", vrrpOperProtocol=vrrpOperProtocol, vrrpConformance=vrrpConformance, vrrpStatsAdvertiseIntervalErrors=vrrpStatsAdvertiseIntervalErrors, vrrpOperRowStatus=vrrpOperRowStatus, vrrpStatsPriorityZeroPktsSent=vrrpStatsPriorityZeroPktsSent, vrrpOperMasterIpAddr=vrrpOperMasterIpAddr, vrrpAssoIpAddrEntry=vrrpAssoIpAddrEntry, vrrpAssoIpAddr=vrrpAssoIpAddr, vrrpStatsBecomeMaster=vrrpStatsBecomeMaster, vrrpTrapPacketSrc=vrrpTrapPacketSrc, vrrpStatsAddressListErrors=vrrpStatsAddressListErrors, vrrpOperations=vrrpOperations, vrrpOperVrId=vrrpOperVrId, VrId=VrId, vrrpMIBCompliances=vrrpMIBCompliances, vrrpRouterChecksumErrors=vrrpRouterChecksumErrors, vrrpOperGroup=vrrpOperGroup, vrrpStatsAdvertiseRcvd=vrrpStatsAdvertiseRcvd, vrrpOperAuthKey=vrrpOperAuthKey, vrrpMIB=vrrpMIB, vrrpStatsAuthFailures=vrrpStatsAuthFailures, vrrpOperAdvertisementInterval=vrrpOperAdvertisementInterval, vrrpStatsIpTtlErrors=vrrpStatsIpTtlErrors, vrrpStatsPriorityZeroPktsRcvd=vrrpStatsPriorityZeroPktsRcvd, vrrpStatsAuthTypeMismatch=vrrpStatsAuthTypeMismatch, vrrpAssoIpAddrTable=vrrpAssoIpAddrTable, vrrpStatistics=vrrpStatistics, vrrpOperVirtualRouterUpTime=vrrpOperVirtualRouterUpTime, vrrpMIBCompliance=vrrpMIBCompliance, vrrpRouterStatsTable=vrrpRouterStatsTable, vrrpOperPrimaryIpAddr=vrrpOperPrimaryIpAddr, vrrpOperAuthType=vrrpOperAuthType, vrrpOperAdminState=vrrpOperAdminState, vrrpStatsGroup=vrrpStatsGroup, vrrpRouterVrIdErrors=vrrpRouterVrIdErrors, vrrpOperState=vrrpOperState, vrrpOperPriority=vrrpOperPriority, PYSNMP_MODULE_ID=vrrpMIB, vrrpOperIpAddrCount=vrrpOperIpAddrCount, vrrpOperVirtualMacAddr=vrrpOperVirtualMacAddr, vrrpTrapNewMaster=vrrpTrapNewMaster, vrrpStatsInvalidAuthType=vrrpStatsInvalidAuthType, vrrpNotifications=vrrpNotifications, vrrpTrapAuthErrorType=vrrpTrapAuthErrorType, vrrpNodeVersion=vrrpNodeVersion, vrrpRouterStatsEntry=vrrpRouterStatsEntry, vrrpTrapAuthFailure=vrrpTrapAuthFailure, vrrpTrapGroup=vrrpTrapGroup, vrrpNotificationGroup=vrrpNotificationGroup, vrrpRouterVersionErrors=vrrpRouterVersionErrors, vrrpOperTable=vrrpOperTable, vrrpMIBGroups=vrrpMIBGroups, vrrpAssoIpAddrRowStatus=vrrpAssoIpAddrRowStatus, vrrpStatsPacketLengthErrors=vrrpStatsPacketLengthErrors, vrrpStatsInvalidTypePktsRcvd=vrrpStatsInvalidTypePktsRcvd, vrrpOperPreemptMode=vrrpOperPreemptMode, vrrpNotificationCntl=vrrpNotificationCntl, vrrpOperEntry=vrrpOperEntry)
