#
# PySNMP MIB module ALCATEL-IND1-HA-VLAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/nokia/aos7/ALCATEL-IND1-HA-VLAN-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:32:28 2022
# On host fv-az36-988 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
softentIND1HAVlan, = mibBuilder.importSymbols("ALCATEL-IND1-BASE", "softentIND1HAVlan")
MultiChassisId, = mibBuilder.importSymbols("ALCATEL-IND1-MULTI-CHASSIS-MIB", "MultiChassisId")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
ifIndex, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "ifIndex", "InterfaceIndex")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
iso, ModuleIdentity, Counter32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Gauge32, TimeTicks, MibIdentifier, Integer32, Unsigned32, IpAddress, ObjectIdentity, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "ModuleIdentity", "Counter32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Gauge32", "TimeTicks", "MibIdentifier", "Integer32", "Unsigned32", "IpAddress", "ObjectIdentity", "NotificationType")
RowStatus, TextualConvention, MacAddress, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "MacAddress", "DisplayString")
alcatelIND1HAVlanMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 64, 1))
alcatelIND1HAVlanMIB.setRevisions(('2010-05-13 00:00', '2007-04-03 00:00',))
if mibBuilder.loadTexts: alcatelIND1HAVlanMIB.setLastUpdated('201005130000Z')
if mibBuilder.loadTexts: alcatelIND1HAVlanMIB.setOrganization('Alcatel-Lucent, Enterprise Solutions Division')
alcatelIND1HAVlanMIBNotifications = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 64, 1, 0))
if mibBuilder.loadTexts: alcatelIND1HAVlanMIBNotifications.setStatus('current')
alcatelIND1HAVlanMIBObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 64, 1, 1))
if mibBuilder.loadTexts: alcatelIND1HAVlanMIBObjects.setStatus('current')
alcatelIND1HAVlanMIBConformance = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 64, 1, 2))
if mibBuilder.loadTexts: alcatelIND1HAVlanMIBConformance.setStatus('current')
alcatelIND1HAVlanMIBGroups = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 64, 1, 2, 1))
if mibBuilder.loadTexts: alcatelIND1HAVlanMIBGroups.setStatus('current')
alcatelIND1HAVlanMIBCompliances = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 64, 1, 2, 2))
if mibBuilder.loadTexts: alcatelIND1HAVlanMIBCompliances.setStatus('current')
alaHAVlanCluster = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 64, 1, 1, 1))
alaHAVlanClusterTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 64, 1, 1, 1, 1), )
if mibBuilder.loadTexts: alaHAVlanClusterTable.setStatus('current')
alaHAVlanClusterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 64, 1, 1, 1, 1, 1), ).setIndexNames((0, "ALCATEL-IND1-HA-VLAN-MIB", "alaHAVlanClusterId"))
if mibBuilder.loadTexts: alaHAVlanClusterEntry.setStatus('current')
alaHAVlanClusterId = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 64, 1, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: alaHAVlanClusterId.setStatus('current')
alaHAVlanClusterName = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 64, 1, 1, 1, 1, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaHAVlanClusterName.setStatus('current')
alaHAVlanClusterAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 64, 1, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaHAVlanClusterAdminStatus.setStatus('current')
alaHAVlanClusterOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 64, 1, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaHAVlanClusterOperStatus.setStatus('current')
alaHAVlanClusterOperStatusFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 64, 1, 1, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("invalid", 0), ("novlan", 1), ("vlandown", 2), ("vpanotforwarding", 3), ("ipinterfacedown", 4), ("noigmpmembers", 5), ("nomacaddress", 6), ("nomulticastip", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaHAVlanClusterOperStatusFlag.setStatus('current')
alaHAVlanClusterMode = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 64, 1, 1, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("l2mode", 1), ("l3mode", 2))).clone('l2mode')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaHAVlanClusterMode.setStatus('current')
alaHAVlanClusterVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 64, 1, 1, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4094))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaHAVlanClusterVlan.setStatus('current')
alaHAVlanClusterMacAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 64, 1, 1, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("invalid", 1), ("static", 2), ("dynamic", 3))).clone('invalid')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaHAVlanClusterMacAddressType.setStatus('current')
alaHAVlanClusterMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 64, 1, 1, 1, 1, 1, 9), MacAddress().clone(hexValue="000000000000")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaHAVlanClusterMacAddress.setStatus('current')
alaHAVlanClusterInetAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 64, 1, 1, 1, 1, 1, 10), InetAddressType().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("ipv4", 1))).clone('ipv4')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaHAVlanClusterInetAddressType.setStatus('current')
alaHAVlanClusterInetAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 64, 1, 1, 1, 1, 1, 11), InetAddress().subtype(subtypeSpec=ValueSizeConstraint(0, 4)).clone(hexValue="00000000")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaHAVlanClusterInetAddress.setStatus('current')
alaHAVlanClusterMulticastStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 64, 1, 1, 1, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaHAVlanClusterMulticastStatus.setStatus('current')
alaHAVlanClusterMulticastInetAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 64, 1, 1, 1, 1, 1, 13), InetAddressType().subtype(subtypeSpec=ValueRangeConstraint(1, 1))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaHAVlanClusterMulticastInetAddressType.setStatus('current')
alaHAVlanClusterMulticastInetAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 64, 1, 1, 1, 1, 1, 14), InetAddress().subtype(subtypeSpec=ValueSizeConstraint(0, 4)).clone(hexValue="00000000")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaHAVlanClusterMulticastInetAddress.setStatus('current')
alaHAVlanClusterRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 64, 1, 1, 1, 1, 1, 15), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaHAVlanClusterRowStatus.setStatus('current')
alaHAVlanClusterMcmStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 64, 1, 1, 1, 1, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("inSync", 1), ("outofSync", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaHAVlanClusterMcmStatus.setStatus('deprecated')
alaHAVlanClusterMcmStatusFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 64, 1, 1, 1, 1, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14))).clone(namedValues=NamedValues(("mcdown", 1), ("operationaldown", 2), ("allportmodenotsupported", 3), ("modemismatch", 4), ("vlanmismatch", 5), ("macmismatch", 6), ("ipmismatch", 7), ("arptypemismatch", 8), ("igmpstatusmismatch", 9), ("mcastipmismatch", 10), ("syncinprogress", 11), ("invalidmac", 12), ("nonvipvlannotsupportedinl3mode", 13), ("noflag", 14)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaHAVlanClusterMcmStatusFlag.setStatus('deprecated')
alaHAVlanClusterVflStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 64, 1, 1, 1, 1, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaHAVlanClusterVflStatus.setStatus('deprecated')
alaHAVlanClusterLoopback = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 64, 1, 1, 1, 1, 1, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaHAVlanClusterLoopback.setStatus('current')
alaHAVlanClusterPort = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 64, 1, 1, 2))
alaHAVlanClusterPortTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 64, 1, 1, 2, 1), )
if mibBuilder.loadTexts: alaHAVlanClusterPortTable.setStatus('current')
alaHAVlanClusterPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 64, 1, 1, 2, 1, 1), ).setIndexNames((0, "ALCATEL-IND1-HA-VLAN-MIB", "alaHAVlanClusterId"), (0, "ALCATEL-IND1-HA-VLAN-MIB", "alaHAVlanClusterPortIfIndex"))
if mibBuilder.loadTexts: alaHAVlanClusterPortEntry.setStatus('current')
alaHAVlanClusterPortIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 64, 1, 1, 2, 1, 1, 1), InterfaceIndex()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: alaHAVlanClusterPortIfIndex.setStatus('current')
alaHAVlanClusterPortRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 64, 1, 1, 2, 1, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaHAVlanClusterPortRowStatus.setStatus('current')
alaHAVlanClusterPortType = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 64, 1, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("static", 1), ("dynamic", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaHAVlanClusterPortType.setStatus('current')
alaHAVlanClusterPortValid = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 64, 1, 1, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("valid", 1), ("invalid", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaHAVlanClusterPortValid.setStatus('current')
alaHAVlanClusterPeerMismatch = NotificationType((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 64, 1, 0, 1)).setObjects(("ALCATEL-IND1-HA-VLAN-MIB", "alaHAVlanClusterId"))
if mibBuilder.loadTexts: alaHAVlanClusterPeerMismatch.setStatus('current')
alaHAVlanMCPeerMismatch = NotificationType((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 64, 1, 0, 2)).setObjects(("ALCATEL-IND1-HA-VLAN-MIB", "alaHAVlanClusterId"), ("ALCATEL-IND1-HA-VLAN-MIB", "alaHAVlanMultiChassisId"), ("ALCATEL-IND1-HA-VLAN-MIB", "alaHAVlanClusterPortIfIndex"))
if mibBuilder.loadTexts: alaHAVlanMCPeerMismatch.setStatus('current')
alaHAVlanDynamicMAC = NotificationType((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 64, 1, 0, 3)).setObjects(("ALCATEL-IND1-HA-VLAN-MIB", "alaHAVlanClusterId"), ("ALCATEL-IND1-HA-VLAN-MIB", "alaHAVlanClusterInetAddress"), ("ALCATEL-IND1-HA-VLAN-MIB", "alaHAVlanClusterMacAddress"), ("ALCATEL-IND1-HA-VLAN-MIB", "alaHAVlanClusterPortIfIndex"))
if mibBuilder.loadTexts: alaHAVlanDynamicMAC.setStatus('current')
alaHAVlanNotificationObj = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 64, 1, 1, 3))
alaHAVlanMultiChassisId = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 64, 1, 1, 3, 1), MultiChassisId()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: alaHAVlanMultiChassisId.setStatus('current')
alcatelIND1HAVlanMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 64, 1, 2, 2, 1)).setObjects(("ALCATEL-IND1-HA-VLAN-MIB", "alaHAVlanClusterGroup"), ("ALCATEL-IND1-HA-VLAN-MIB", "alaHAVlanClusterPortGroup"), ("ALCATEL-IND1-HA-VLAN-MIB", "alaHAVlanNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alcatelIND1HAVlanMIBCompliance = alcatelIND1HAVlanMIBCompliance.setStatus('current')
alaHAVlanClusterGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 64, 1, 2, 1, 1)).setObjects(("ALCATEL-IND1-HA-VLAN-MIB", "alaHAVlanClusterId"), ("ALCATEL-IND1-HA-VLAN-MIB", "alaHAVlanClusterName"), ("ALCATEL-IND1-HA-VLAN-MIB", "alaHAVlanClusterAdminStatus"), ("ALCATEL-IND1-HA-VLAN-MIB", "alaHAVlanClusterOperStatus"), ("ALCATEL-IND1-HA-VLAN-MIB", "alaHAVlanClusterOperStatusFlag"), ("ALCATEL-IND1-HA-VLAN-MIB", "alaHAVlanClusterMode"), ("ALCATEL-IND1-HA-VLAN-MIB", "alaHAVlanClusterVlan"), ("ALCATEL-IND1-HA-VLAN-MIB", "alaHAVlanClusterMacAddressType"), ("ALCATEL-IND1-HA-VLAN-MIB", "alaHAVlanClusterMacAddress"), ("ALCATEL-IND1-HA-VLAN-MIB", "alaHAVlanClusterInetAddressType"), ("ALCATEL-IND1-HA-VLAN-MIB", "alaHAVlanClusterInetAddress"), ("ALCATEL-IND1-HA-VLAN-MIB", "alaHAVlanClusterMulticastStatus"), ("ALCATEL-IND1-HA-VLAN-MIB", "alaHAVlanClusterMulticastInetAddressType"), ("ALCATEL-IND1-HA-VLAN-MIB", "alaHAVlanClusterMulticastInetAddress"), ("ALCATEL-IND1-HA-VLAN-MIB", "alaHAVlanClusterRowStatus"), ("ALCATEL-IND1-HA-VLAN-MIB", "alaHAVlanClusterMcmStatus"), ("ALCATEL-IND1-HA-VLAN-MIB", "alaHAVlanClusterMcmStatusFlag"), ("ALCATEL-IND1-HA-VLAN-MIB", "alaHAVlanClusterVflStatus"), ("ALCATEL-IND1-HA-VLAN-MIB", "alaHAVlanClusterLoopback"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaHAVlanClusterGroup = alaHAVlanClusterGroup.setStatus('current')
alaHAVlanClusterPortGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 64, 1, 2, 1, 2)).setObjects(("ALCATEL-IND1-HA-VLAN-MIB", "alaHAVlanClusterPortIfIndex"), ("ALCATEL-IND1-HA-VLAN-MIB", "alaHAVlanClusterPortRowStatus"), ("ALCATEL-IND1-HA-VLAN-MIB", "alaHAVlanClusterPortType"), ("ALCATEL-IND1-HA-VLAN-MIB", "alaHAVlanClusterPortValid"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaHAVlanClusterPortGroup = alaHAVlanClusterPortGroup.setStatus('current')
alaHAVlanNotificationObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 64, 1, 2, 1, 3)).setObjects(("ALCATEL-IND1-HA-VLAN-MIB", "alaHAVlanMultiChassisId"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaHAVlanNotificationObjectGroup = alaHAVlanNotificationObjectGroup.setStatus('current')
alaHAVlanNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 64, 1, 2, 1, 4)).setObjects(("ALCATEL-IND1-HA-VLAN-MIB", "alaHAVlanClusterPeerMismatch"), ("ALCATEL-IND1-HA-VLAN-MIB", "alaHAVlanMCPeerMismatch"), ("ALCATEL-IND1-HA-VLAN-MIB", "alaHAVlanDynamicMAC"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaHAVlanNotificationGroup = alaHAVlanNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("ALCATEL-IND1-HA-VLAN-MIB", alcatelIND1HAVlanMIBCompliances=alcatelIND1HAVlanMIBCompliances, alaHAVlanClusterOperStatus=alaHAVlanClusterOperStatus, alaHAVlanClusterMcmStatusFlag=alaHAVlanClusterMcmStatusFlag, alaHAVlanClusterAdminStatus=alaHAVlanClusterAdminStatus, alaHAVlanClusterPortIfIndex=alaHAVlanClusterPortIfIndex, alaHAVlanClusterOperStatusFlag=alaHAVlanClusterOperStatusFlag, alaHAVlanClusterPort=alaHAVlanClusterPort, alcatelIND1HAVlanMIBObjects=alcatelIND1HAVlanMIBObjects, alaHAVlanMultiChassisId=alaHAVlanMultiChassisId, alaHAVlanClusterEntry=alaHAVlanClusterEntry, alaHAVlanClusterInetAddress=alaHAVlanClusterInetAddress, alaHAVlanClusterRowStatus=alaHAVlanClusterRowStatus, alaHAVlanClusterMulticastStatus=alaHAVlanClusterMulticastStatus, alaHAVlanClusterId=alaHAVlanClusterId, alcatelIND1HAVlanMIBNotifications=alcatelIND1HAVlanMIBNotifications, alaHAVlanClusterVflStatus=alaHAVlanClusterVflStatus, alaHAVlanClusterPortTable=alaHAVlanClusterPortTable, alaHAVlanClusterTable=alaHAVlanClusterTable, alaHAVlanClusterLoopback=alaHAVlanClusterLoopback, alaHAVlanNotificationObjectGroup=alaHAVlanNotificationObjectGroup, alaHAVlanNotificationObj=alaHAVlanNotificationObj, alaHAVlanClusterPortType=alaHAVlanClusterPortType, alaHAVlanClusterMode=alaHAVlanClusterMode, alcatelIND1HAVlanMIBConformance=alcatelIND1HAVlanMIBConformance, alaHAVlanClusterMulticastInetAddress=alaHAVlanClusterMulticastInetAddress, alaHAVlanClusterPortEntry=alaHAVlanClusterPortEntry, alcatelIND1HAVlanMIBCompliance=alcatelIND1HAVlanMIBCompliance, alaHAVlanClusterVlan=alaHAVlanClusterVlan, alaHAVlanClusterPortRowStatus=alaHAVlanClusterPortRowStatus, alaHAVlanNotificationGroup=alaHAVlanNotificationGroup, PYSNMP_MODULE_ID=alcatelIND1HAVlanMIB, alaHAVlanClusterMulticastInetAddressType=alaHAVlanClusterMulticastInetAddressType, alcatelIND1HAVlanMIBGroups=alcatelIND1HAVlanMIBGroups, alaHAVlanClusterGroup=alaHAVlanClusterGroup, alaHAVlanClusterInetAddressType=alaHAVlanClusterInetAddressType, alaHAVlanClusterMacAddressType=alaHAVlanClusterMacAddressType, alaHAVlanMCPeerMismatch=alaHAVlanMCPeerMismatch, alaHAVlanClusterPortGroup=alaHAVlanClusterPortGroup, alaHAVlanClusterMcmStatus=alaHAVlanClusterMcmStatus, alaHAVlanClusterPortValid=alaHAVlanClusterPortValid, alcatelIND1HAVlanMIB=alcatelIND1HAVlanMIB, alaHAVlanCluster=alaHAVlanCluster, alaHAVlanClusterName=alaHAVlanClusterName, alaHAVlanDynamicMAC=alaHAVlanDynamicMAC, alaHAVlanClusterPeerMismatch=alaHAVlanClusterPeerMismatch, alaHAVlanClusterMacAddress=alaHAVlanClusterMacAddress)
