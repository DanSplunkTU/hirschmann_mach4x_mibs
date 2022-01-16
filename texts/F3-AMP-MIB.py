#
# PySNMP MIB module F3-AMP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/adva/F3-AMP-MIB
# Produced by pysmi-1.1.8 at Sun Jan 16 00:31:31 2022
# On host fv-az42-839 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
fsp150cm, = mibBuilder.importSymbols("ADVA-MIB", "fsp150cm")
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
VlanId, = mibBuilder.importSymbols("CM-COMMON-MIB", "VlanId")
IpManagementTunnelType, IpManagementTunnelEncapsulationType, IpSourceAddrType = mibBuilder.importSymbols("CM-IP-MIB", "IpManagementTunnelType", "IpManagementTunnelEncapsulationType", "IpSourceAddrType")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
TimeTicks, Counter32, Bits, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Gauge32, MibIdentifier, Integer32, NotificationType, ModuleIdentity, iso, Counter64, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Counter32", "Bits", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Gauge32", "MibIdentifier", "Integer32", "NotificationType", "ModuleIdentity", "iso", "Counter64", "ObjectIdentity")
StorageType, RowStatus, TruthValue, DateAndTime, DisplayString, TextualConvention, VariablePointer = mibBuilder.importSymbols("SNMPv2-TC", "StorageType", "RowStatus", "TruthValue", "DateAndTime", "DisplayString", "TextualConvention", "VariablePointer")
f3AMPMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24))
f3AMPMIB.setRevisions(('2012-09-30 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: f3AMPMIB.setRevisionsDescriptions(('\n         Notes from release 201209300000Z,\n         (1)MIB version ready for release FSP150CC 5.6CC.',))
if mibBuilder.loadTexts: f3AMPMIB.setLastUpdated('201209310000Z')
if mibBuilder.loadTexts: f3AMPMIB.setOrganization('ADVA Optical Networking')
if mibBuilder.loadTexts: f3AMPMIB.setContactInfo('        Jakub Zalewski\n                     ADVA Optical Networking, Inc.\n                Tel: +48 58 7716 411\n             E-mail: jzalewski@advaoptical.com\n             Postal: ul. Slaska 35/37\n                     81-310 Gdynia, Poland')
if mibBuilder.loadTexts: f3AMPMIB.setDescription('This module defines the Automatic Management Provisioning MIB definitions\n             used by the F3 (FSP150CM/CC) product lines.  \n             Copyright (C) ADVA Optical Networking.')
class AMPRole(TextualConvention, Integer32):
    description = 'Defines client or server role.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("client", 1), ("server", 2))

class AMPStatus(TextualConvention, Integer32):
    description = 'Defines AMP Status.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("notAvailable", 1), ("disabled", 2), ("associatingActive", 3), ("associatingPassive", 4), ("associated", 5), ("noPeer", 6))

class AMPConfigStatus(TextualConvention, Integer32):
    description = 'Defines AMP Configuration Status.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("none", 1), ("provision", 2), ("noPeer", 3), ("request", 4), ("configSuccess", 5), ("configFail", 6), ("timeout", 7))

class AMPProtocol(TextualConvention, Integer32):
    description = 'Defines protocol over which AMP messages are sent.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1))
    namedValues = NamedValues(("efmOam", 1))

class AMPConfigAction(TextualConvention, Integer32):
    description = 'Defines Actions available for f3AmpConfig object'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("noAction", 1), ("clearStats", 2))

f3AmpConfigObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 1))
f3AmpStatsObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 2))
f3AmpConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 3))
f3AmpConfigTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 1, 1), )
if mibBuilder.loadTexts: f3AmpConfigTable.setStatus('current')
if mibBuilder.loadTexts: f3AmpConfigTable.setDescription('A list of entries corresponding to Automatic Management Provisioning\n             configuration instance for configuration purposes.')
f3AmpConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 1, 1, 1), ).setIndexNames((0, "F3-AMP-MIB", "f3AmpConfigIndex"))
if mibBuilder.loadTexts: f3AmpConfigEntry.setStatus('current')
if mibBuilder.loadTexts: f3AmpConfigEntry.setDescription('A conceptual row in the f3AmpConfigTable.')
f3AmpConfigIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)))
if mibBuilder.loadTexts: f3AmpConfigIndex.setStatus('current')
if mibBuilder.loadTexts: f3AmpConfigIndex.setDescription('An integer index value used to uniquely identify\n             this AMP Config within the System.')
f3AmpConfigRole = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 1, 1, 1, 2), AMPRole()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3AmpConfigRole.setStatus('current')
if mibBuilder.loadTexts: f3AmpConfigRole.setDescription('Configures AMP instance to be either Client or Server.')
f3AmpConfigProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 1, 1, 1, 3), AMPProtocol()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3AmpConfigProtocol.setStatus('current')
if mibBuilder.loadTexts: f3AmpConfigProtocol.setDescription('Configures protocol over which AMP message will be transported.')
f3AmpConfigEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 1, 1, 1, 4), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3AmpConfigEnabled.setStatus('current')
if mibBuilder.loadTexts: f3AmpConfigEnabled.setDescription('Enables or Disables AMP on a Port.')
f3AmpConfigPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 1, 1, 1, 5), VariablePointer()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3AmpConfigPort.setStatus('current')
if mibBuilder.loadTexts: f3AmpConfigPort.setDescription('Port on which AMP Server or Client will operate. This port will \n          transmit/receive AMP messages. The AMP can operate on Access Ports and\n          Network Port and f3AmpConfigPort shall point to either cmEthernetAccPortIndex \n          or cmEthernetNetPortIndex.')
f3AmpConfigStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 1, 1, 1, 6), AMPStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3AmpConfigStatus.setStatus('current')
if mibBuilder.loadTexts: f3AmpConfigStatus.setDescription('The Status of AMP.')
f3AmpConfigRemSysName = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 1, 1, 1, 7), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3AmpConfigRemSysName.setStatus('current')
if mibBuilder.loadTexts: f3AmpConfigRemSysName.setDescription("When f3AmpConfigRole is 'server' this object specifies sysName which is sent\n          in a AMP message to be configfured on a AMP Client device.\n          When f3AmpConfigRole is 'client' this object is read-only and shows the sysName\n          value which was received from the AMP Server.")
f3AmpConfigRemSysIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 1, 1, 1, 8), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3AmpConfigRemSysIpAddr.setStatus('current')
if mibBuilder.loadTexts: f3AmpConfigRemSysIpAddr.setDescription("When f3AmpConfigRole is 'server' this object specifies System IP address \n          which is sent in a AMP message to be configfured on a AMP Client device.\n          When f3AmpConfigRole is 'client' this object is read-only and shows the \n          System IP address value which was received from the AMP Server.")
f3AmpConfigRemSysIpMask = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 1, 1, 1, 9), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3AmpConfigRemSysIpMask.setStatus('current')
if mibBuilder.loadTexts: f3AmpConfigRemSysIpMask.setDescription("When f3AmpConfigRole is 'server' this object specifies System IP mask \n          which is sent in a AMP message to be configfured on a AMP Client device.\n          When f3AmpConfigRole is 'client' this object is read-only and shows the \n          System IP mask value which was received from the AMP Server.")
f3AmpConfigRemSysDefGateway = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 1, 1, 1, 10), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3AmpConfigRemSysDefGateway.setStatus('current')
if mibBuilder.loadTexts: f3AmpConfigRemSysDefGateway.setDescription("When f3AmpConfigRole is 'server' this object specifies System Default Gateway \n          which is sent in a AMP message to be configfured on a AMP Client device.\n          When f3AmpConfigRole is 'client' this object is read-only and shows the \n          System Default Gateway value which was received from the AMP Server.")
f3AmpConfigRemSysSNMPV1IfName = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 1, 1, 1, 11), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3AmpConfigRemSysSNMPV1IfName.setStatus('current')
if mibBuilder.loadTexts: f3AmpConfigRemSysSNMPV1IfName.setDescription("When f3AmpConfigRole is 'server' this object specifies \n          System SNMPV1 Interface Name which is sent\n          in a AMP message to be configfured on a AMP Client device.\n          When f3AmpConfigRole is 'client' this object shows the \n          System SNMPV1 Interface Name value which was received from the AMP Server.")
f3AmpConfigRemSysSrcIpAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 1, 1, 1, 12), IpSourceAddrType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3AmpConfigRemSysSrcIpAddrType.setStatus('current')
if mibBuilder.loadTexts: f3AmpConfigRemSysSrcIpAddrType.setDescription("When f3AmpConfigRole is 'server' this object specifies System Source IP Address \n          type which is sent in an AMP message to be configfured on an AMP Client device.\n          When f3AmpConfigRole is 'client' this object is read-only and shows the \n          System Source IP Address Type value which was received from the AMP Server.")
f3AmpConfigRemSysSrcIpAddrIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 1, 1, 1, 13), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3AmpConfigRemSysSrcIpAddrIfName.setStatus('current')
if mibBuilder.loadTexts: f3AmpConfigRemSysSrcIpAddrIfName.setDescription("When f3AmpConfigRole is 'server' this object specifies System Source IP\n          Interface name sent in an AMP message to be configured on an AMP Client device.\n          When f3AmpConfigRole is 'client' this object shows the  SystemSource IP Interface \n          value which was received from the AMP Server.")
f3AmpConfigRemTunnelIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 1, 1, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3AmpConfigRemTunnelIndex.setStatus('current')
if mibBuilder.loadTexts: f3AmpConfigRemTunnelIndex.setDescription("When f3AmpConfigRole is 'server' this object specifies \n          index of a Management Tunnel which is sent\n          in an AMP message to be configfured on an AMP Client device.\n          When f3AmpConfigRole is 'client' this object is read-only and shows the \n          index of a Management Tunnel which was received from the AMP Server.")
f3AmpConfigRemTunnelName = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 1, 1, 1, 15), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3AmpConfigRemTunnelName.setStatus('current')
if mibBuilder.loadTexts: f3AmpConfigRemTunnelName.setDescription("When f3AmpConfigRole is 'server' this object specifies \n          a Management Tunnel name which is sent\n          in an AMP message to be configfured on an AMP Client device.\n          When f3AmpConfigRole is 'client' this object is read-only and shows the \n          Management Tunnel name which was received from the AMP Server.")
f3AmpConfigRemTunnelType = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 1, 1, 1, 16), IpManagementTunnelType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3AmpConfigRemTunnelType.setStatus('current')
if mibBuilder.loadTexts: f3AmpConfigRemTunnelType.setDescription("When f3AmpConfigRole is 'server' this object specifies \n          a Management Tunnel type value which is sent\n          in an AMP message to be configfured on an AMP Client device.\n          When f3AmpConfigRole is 'client' this object is read-only and shows the \n          Management Tunnel type value which was received from the AMP Server.")
f3AmpConfigRemTunnelIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 1, 1, 1, 17), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3AmpConfigRemTunnelIpAddr.setStatus('current')
if mibBuilder.loadTexts: f3AmpConfigRemTunnelIpAddr.setDescription("When f3AmpConfigRole is 'server' this object specifies \n          IP Address of a Management Tunnel which is sent\n          in an AMP message to be configfured on an AMP Client device.\n          When f3AmpConfigRole is 'client' this object is read-only and shows the \n          IP Address of a Management Tunnel which was received from the AMP Server.")
f3AmpConfigRemTunnelIpMask = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 1, 1, 1, 18), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3AmpConfigRemTunnelIpMask.setStatus('current')
if mibBuilder.loadTexts: f3AmpConfigRemTunnelIpMask.setDescription("When f3AmpConfigRole is 'server' this object specifies \n          IP Mask of a Management Tunnel which is sent\n          in an AMP message to be configfured on an AMP Client device.\n          When f3AmpConfigRole is 'client' this object is read-only and shows the \n          IP Mask of a Management Tunnel which was received from the AMP Server.")
f3AmpConfigRemTunnelVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 1, 1, 1, 19), VlanId()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3AmpConfigRemTunnelVlanId.setStatus('current')
if mibBuilder.loadTexts: f3AmpConfigRemTunnelVlanId.setDescription("When f3AmpConfigRole is 'server' this object specifies \n          VlanId of a Management Tunnel which is sent\n          in an AMP message to be configfured on an AMP Client device.\n          When f3AmpConfigRole is 'client' this object is read-only and shows the \n          VlanId of a Management Tunnel which was received from the AMP Server.")
f3AmpConfigRemTunnelSVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 1, 1, 1, 20), VlanId()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3AmpConfigRemTunnelSVlanId.setStatus('current')
if mibBuilder.loadTexts: f3AmpConfigRemTunnelSVlanId.setDescription("When f3AmpConfigRole is 'server' this object specifies \n          S-TAG VlanId of a Management Tunnel which is sent\n          in an AMP message to be configfured on an AMP Client device.\n          When f3AmpConfigRole is 'client' this object is read-only and shows the \n          S-TAG VlanId of a Management Tunnel which was received from the AMP Server.")
f3AmpConfigRemTunnelSVlanIdEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 1, 1, 1, 21), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3AmpConfigRemTunnelSVlanIdEnabled.setStatus('current')
if mibBuilder.loadTexts: f3AmpConfigRemTunnelSVlanIdEnabled.setDescription("When f3AmpConfigRole is 'server' this object specifies \n          a Management Tunnel S-TAG VlanId Enable value which is sent\n          in an AMP message to be configfured on an AMP Client device.\n          When f3AmpConfigRole is 'client' this object is read-only and shows the \n          a Management Tunnel S-TAG VlanId Enabled value which was received \n          from the AMP Server.")
f3AmpConfigRemTunnelRip2PktsEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 1, 1, 1, 22), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3AmpConfigRemTunnelRip2PktsEnabled.setStatus('current')
if mibBuilder.loadTexts: f3AmpConfigRemTunnelRip2PktsEnabled.setDescription("When f3AmpConfigRole is 'server' this object specifies \n          a Management Tunnel RIP2 Packates Enabled value which is sent\n          in an AMP message to be configfured on an AMP Client device.\n          When f3AmpConfigRole is 'client' this object is read-only and shows the \n          a Management Tunnel RIP2 Packates Enabled value which was received \n          from the AMP Server.")
f3AmpConfigRemTunnelCOS = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 1, 1, 1, 23), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3AmpConfigRemTunnelCOS.setStatus('current')
if mibBuilder.loadTexts: f3AmpConfigRemTunnelCOS.setDescription("When f3AmpConfigRole is 'server' this object specifies \n          COS of a Management Tunnel which is sent\n          in an AMP message to be configfured on an AMP Client device.\n          When f3AmpConfigRole is 'client' this object is read-only and shows the \n          COS of a Management Tunnel which was received from the AMP Server.")
f3AmpConfigRemTunnelCIR = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 1, 1, 1, 24), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3AmpConfigRemTunnelCIR.setStatus('current')
if mibBuilder.loadTexts: f3AmpConfigRemTunnelCIR.setDescription("When f3AmpConfigRole is 'server' this object specifies \n          CIR of a Management Tunnel which is sent\n          in an AMP message to be configfured on an AMP Client device.\n          When f3AmpConfigRole is 'client' this object is read-only and shows the \n          CIR of a Management Tunnel which was received from the AMP Server.")
f3AmpConfigRemTunnelEIR = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 1, 1, 1, 25), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3AmpConfigRemTunnelEIR.setStatus('current')
if mibBuilder.loadTexts: f3AmpConfigRemTunnelEIR.setDescription("When f3AmpConfigRole is 'server' this object specifies \n          EIR of a Management Tunnel which is sent\n          in an AMP message to be configfured on an AMP Client device.\n          When f3AmpConfigRole is 'client' this object is read-only and shows the \n          EIR of a Management Tunnel which was received from the AMP Server.")
f3AmpConfigRemTunnelBufferSize = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 1, 1, 1, 26), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3AmpConfigRemTunnelBufferSize.setStatus('current')
if mibBuilder.loadTexts: f3AmpConfigRemTunnelBufferSize.setDescription("When f3AmpConfigRole is 'server' this object specifies \n          Buffer Size of a Management Tunnel which is sent\n          in an AMP message to be configfured on an AMP Client device.\n          When f3AmpConfigRole is 'client' this object is read-only and shows the \n          Buffer Size of a Management Tunnel which was received from the AMP Server.")
f3AmpConfigRemTunnelEncapType = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 1, 1, 1, 27), IpManagementTunnelEncapsulationType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3AmpConfigRemTunnelEncapType.setStatus('current')
if mibBuilder.loadTexts: f3AmpConfigRemTunnelEncapType.setDescription("When f3AmpConfigRole is 'server' this object specifies \n          Encapsulation Type of a Management Tunnel which is sent\n          in an AMP message to be configfured on an AMP Client device.\n          When f3AmpConfigRole is 'client' this object is read-only and shows the \n          Encapsulation Type of a Management Tunnel which was received from \n          the AMP Server.")
f3AmpConfigRemTunnelMtu = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 1, 1, 1, 28), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3AmpConfigRemTunnelMtu.setStatus('current')
if mibBuilder.loadTexts: f3AmpConfigRemTunnelMtu.setDescription("When f3AmpConfigRole is 'server' this object specifies \n          MTU of a Management Tunnel which is sent\n          in an AMP message to be configfured on an AMP Client device.\n          When f3AmpConfigRole is 'client' this object is read-only and shows the \n          MTU of a Management Tunnel which was received from the AMP Server.")
f3AmpConfigAction = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 1, 1, 1, 29), AMPConfigAction()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3AmpConfigAction.setStatus('current')
if mibBuilder.loadTexts: f3AmpConfigAction.setDescription('This object may be used to initiate user action on this AMP Config instance.')
f3AmpConfigStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 1, 1, 1, 30), StorageType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3AmpConfigStorageType.setStatus('current')
if mibBuilder.loadTexts: f3AmpConfigStorageType.setDescription('The type of storage configured for this entry.')
f3AmpConfigRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 1, 1, 1, 31), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3AmpConfigRowStatus.setStatus('current')
if mibBuilder.loadTexts: f3AmpConfigRowStatus.setDescription('The status of this row.  An entry MUST NOT exist in the \n            active state unless all objects in the entry have an \n            appropriate value, as described\n            in the description clause for each writable object.\n\n            The values of f3AmpConfigRowStatus supported are\n            createAndGo(4) and destroy(6).  All mandatory attributes\n            must be specified in a single SNMP SET request with\n            neRowStatus value as createAndGo(4).\n            Upon successful row creation, this object has a\n            value of active(1).\n\n            The f3AmpConfigRowStatus object may be modified if\n            the associated instance of this object is equal to active(1).')
f3AmpStatsTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 2, 1), )
if mibBuilder.loadTexts: f3AmpStatsTable.setStatus('current')
if mibBuilder.loadTexts: f3AmpStatsTable.setDescription('A list of entries corresponding to Automatic Management Provisioning\n             Statistics')
f3AmpStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 2, 1, 1), ).setIndexNames((0, "F3-AMP-MIB", "f3AmpConfigIndex"))
if mibBuilder.loadTexts: f3AmpStatsEntry.setStatus('current')
if mibBuilder.loadTexts: f3AmpStatsEntry.setDescription('A conceptual row in the f3AmpStatsTable.')
f3AmpStatsProvDataTx = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 2, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3AmpStatsProvDataTx.setStatus('current')
if mibBuilder.loadTexts: f3AmpStatsProvDataTx.setDescription('The number of Provisioning Data messages sent by AMP Server.')
f3AmpStatsProvDataRx = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 2, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3AmpStatsProvDataRx.setStatus('current')
if mibBuilder.loadTexts: f3AmpStatsProvDataRx.setDescription('The number of Provisioning Data messages received by AMP Client.')
f3AmpStatsProvRequestTx = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 2, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3AmpStatsProvRequestTx.setStatus('current')
if mibBuilder.loadTexts: f3AmpStatsProvRequestTx.setDescription('The number of Provisioning Request messages sent by AMP Client.')
f3AmpStatsProvRequestRx = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 2, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3AmpStatsProvRequestRx.setStatus('current')
if mibBuilder.loadTexts: f3AmpStatsProvRequestRx.setDescription('The number of Provisioning Request received sent by AMP Server.')
f3AmpStatsConfigSuccessTx = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 2, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3AmpStatsConfigSuccessTx.setStatus('current')
if mibBuilder.loadTexts: f3AmpStatsConfigSuccessTx.setDescription('The number of Configuration Success messages sent sent by AMP Client.')
f3AmpStatsConfigSuccessRx = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 2, 1, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3AmpStatsConfigSuccessRx.setStatus('current')
if mibBuilder.loadTexts: f3AmpStatsConfigSuccessRx.setDescription('The number of Configuration Success messages received by AMP Server.')
f3AmpStatsConfigFailTx = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 2, 1, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3AmpStatsConfigFailTx.setStatus('current')
if mibBuilder.loadTexts: f3AmpStatsConfigFailTx.setDescription('The number of Configuration Success messages received by AMP Client.')
f3AmpStatsConfigFailRx = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 2, 1, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3AmpStatsConfigFailRx.setStatus('current')
if mibBuilder.loadTexts: f3AmpStatsConfigFailRx.setDescription('The number of Configuration Success messages received by AMP Server.')
f3AmpStatsSpuriousMessageRx = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 2, 1, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3AmpStatsSpuriousMessageRx.setStatus('current')
if mibBuilder.loadTexts: f3AmpStatsSpuriousMessageRx.setDescription('The number of Spurious messages received by AMP Client or Server')
f3AmpStatsTimeoutRx = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 2, 1, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3AmpStatsTimeoutRx.setStatus('current')
if mibBuilder.loadTexts: f3AmpStatsTimeoutRx.setDescription('The number of messages which were not received within the time out value.\n           AMP Client can time out while waiting for Prov Data message. \n           AMP Server can time out while waiting for Config Fail or Config Success\n           message.')
f3AmpStatsLastRxStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 2, 1, 1, 11), AMPConfigStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3AmpStatsLastRxStatus.setStatus('current')
if mibBuilder.loadTexts: f3AmpStatsLastRxStatus.setDescription('Last received Configuration Status.')
f3AmpStatsRxTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 2, 1, 1, 12), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3AmpStatsRxTimeStamp.setStatus('current')
if mibBuilder.loadTexts: f3AmpStatsRxTimeStamp.setDescription('Time of last received Configuration Status.')
f3AmpStatsLastTxStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 2, 1, 1, 13), AMPConfigStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3AmpStatsLastTxStatus.setStatus('current')
if mibBuilder.loadTexts: f3AmpStatsLastTxStatus.setDescription('Last sent Configuration Status.')
f3AmpStatsTxTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 2, 1, 1, 14), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3AmpStatsTxTimeStamp.setStatus('current')
if mibBuilder.loadTexts: f3AmpStatsTxTimeStamp.setDescription('Time of last sent Configuration Status.')
f3AmpCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 3, 1))
f3AmpGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 3, 2))
f3AmpCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 3, 1, 1)).setObjects(("F3-AMP-MIB", "f3AmpConfigGroup"), ("F3-AMP-MIB", "f3AmpStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3AmpCompliance = f3AmpCompliance.setStatus('current')
if mibBuilder.loadTexts: f3AmpCompliance.setDescription('Describes the requirements for conformance to the F3-AMP-MIB compilance.')
f3AmpConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 3, 2, 1)).setObjects(("F3-AMP-MIB", "f3AmpConfigRole"), ("F3-AMP-MIB", "f3AmpConfigProtocol"), ("F3-AMP-MIB", "f3AmpConfigEnabled"), ("F3-AMP-MIB", "f3AmpConfigPort"), ("F3-AMP-MIB", "f3AmpConfigStatus"), ("F3-AMP-MIB", "f3AmpConfigRemSysName"), ("F3-AMP-MIB", "f3AmpConfigRemSysIpAddr"), ("F3-AMP-MIB", "f3AmpConfigRemSysIpMask"), ("F3-AMP-MIB", "f3AmpConfigRemSysDefGateway"), ("F3-AMP-MIB", "f3AmpConfigRemSysSNMPV1IfName"), ("F3-AMP-MIB", "f3AmpConfigRemSysSrcIpAddrType"), ("F3-AMP-MIB", "f3AmpConfigRemSysSrcIpAddrIfName"), ("F3-AMP-MIB", "f3AmpConfigRemTunnelIndex"), ("F3-AMP-MIB", "f3AmpConfigRemTunnelName"), ("F3-AMP-MIB", "f3AmpConfigRemTunnelType"), ("F3-AMP-MIB", "f3AmpConfigRemTunnelIpAddr"), ("F3-AMP-MIB", "f3AmpConfigRemTunnelIpMask"), ("F3-AMP-MIB", "f3AmpConfigRemTunnelVlanId"), ("F3-AMP-MIB", "f3AmpConfigRemTunnelSVlanId"), ("F3-AMP-MIB", "f3AmpConfigRemTunnelSVlanIdEnabled"), ("F3-AMP-MIB", "f3AmpConfigRemTunnelRip2PktsEnabled"), ("F3-AMP-MIB", "f3AmpConfigRemTunnelCOS"), ("F3-AMP-MIB", "f3AmpConfigRemTunnelCIR"), ("F3-AMP-MIB", "f3AmpConfigRemTunnelEIR"), ("F3-AMP-MIB", "f3AmpConfigRemTunnelBufferSize"), ("F3-AMP-MIB", "f3AmpConfigRemTunnelEncapType"), ("F3-AMP-MIB", "f3AmpConfigRemTunnelMtu"), ("F3-AMP-MIB", "f3AmpConfigAction"), ("F3-AMP-MIB", "f3AmpConfigStorageType"), ("F3-AMP-MIB", "f3AmpConfigRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3AmpConfigGroup = f3AmpConfigGroup.setStatus('current')
if mibBuilder.loadTexts: f3AmpConfigGroup.setDescription('A collection of objects used to manage the AMP Configuration.')
f3AmpStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 3, 2, 2)).setObjects(("F3-AMP-MIB", "f3AmpStatsProvDataTx"), ("F3-AMP-MIB", "f3AmpStatsProvDataRx"), ("F3-AMP-MIB", "f3AmpStatsProvRequestTx"), ("F3-AMP-MIB", "f3AmpStatsProvRequestRx"), ("F3-AMP-MIB", "f3AmpStatsConfigSuccessTx"), ("F3-AMP-MIB", "f3AmpStatsConfigSuccessRx"), ("F3-AMP-MIB", "f3AmpStatsConfigFailTx"), ("F3-AMP-MIB", "f3AmpStatsConfigFailRx"), ("F3-AMP-MIB", "f3AmpStatsSpuriousMessageRx"), ("F3-AMP-MIB", "f3AmpStatsTimeoutRx"), ("F3-AMP-MIB", "f3AmpStatsLastRxStatus"), ("F3-AMP-MIB", "f3AmpStatsRxTimeStamp"), ("F3-AMP-MIB", "f3AmpStatsLastTxStatus"), ("F3-AMP-MIB", "f3AmpStatsTxTimeStamp"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3AmpStatsGroup = f3AmpStatsGroup.setStatus('current')
if mibBuilder.loadTexts: f3AmpStatsGroup.setDescription('A collection of objects used to manage the AMP Statistics.')
mibBuilder.exportSymbols("F3-AMP-MIB", f3AmpConfigRemSysSrcIpAddrIfName=f3AmpConfigRemSysSrcIpAddrIfName, f3AmpConfigRowStatus=f3AmpConfigRowStatus, f3AmpConfigRole=f3AmpConfigRole, f3AmpCompliances=f3AmpCompliances, f3AmpConfigRemTunnelEIR=f3AmpConfigRemTunnelEIR, f3AmpConfigRemTunnelBufferSize=f3AmpConfigRemTunnelBufferSize, f3AmpConfigAction=f3AmpConfigAction, f3AmpConfigRemTunnelName=f3AmpConfigRemTunnelName, f3AmpConfigIndex=f3AmpConfigIndex, f3AmpConfigRemTunnelMtu=f3AmpConfigRemTunnelMtu, f3AmpStatsProvDataTx=f3AmpStatsProvDataTx, f3AmpStatsProvRequestTx=f3AmpStatsProvRequestTx, f3AmpConfigRemTunnelRip2PktsEnabled=f3AmpConfigRemTunnelRip2PktsEnabled, f3AmpConfigTable=f3AmpConfigTable, f3AmpConfigEntry=f3AmpConfigEntry, f3AmpStatsConfigSuccessTx=f3AmpStatsConfigSuccessTx, f3AmpConfigStorageType=f3AmpConfigStorageType, f3AmpStatsConfigFailRx=f3AmpStatsConfigFailRx, f3AmpConfigRemTunnelIpMask=f3AmpConfigRemTunnelIpMask, f3AmpStatsTimeoutRx=f3AmpStatsTimeoutRx, f3AmpConfigPort=f3AmpConfigPort, f3AmpStatsGroup=f3AmpStatsGroup, f3AmpConfigRemTunnelType=f3AmpConfigRemTunnelType, f3AmpStatsObjects=f3AmpStatsObjects, f3AmpStatsEntry=f3AmpStatsEntry, PYSNMP_MODULE_ID=f3AMPMIB, f3AmpConfigRemSysSNMPV1IfName=f3AmpConfigRemSysSNMPV1IfName, f3AmpStatsTxTimeStamp=f3AmpStatsTxTimeStamp, f3AmpStatsConfigSuccessRx=f3AmpStatsConfigSuccessRx, f3AmpConfigProtocol=f3AmpConfigProtocol, f3AmpConformance=f3AmpConformance, AMPProtocol=AMPProtocol, f3AmpConfigEnabled=f3AmpConfigEnabled, f3AmpConfigRemTunnelIpAddr=f3AmpConfigRemTunnelIpAddr, f3AmpConfigRemTunnelSVlanIdEnabled=f3AmpConfigRemTunnelSVlanIdEnabled, f3AmpStatsTable=f3AmpStatsTable, f3AmpStatsConfigFailTx=f3AmpStatsConfigFailTx, AMPConfigAction=AMPConfigAction, f3AmpConfigRemSysDefGateway=f3AmpConfigRemSysDefGateway, f3AmpStatsProvRequestRx=f3AmpStatsProvRequestRx, f3AmpCompliance=f3AmpCompliance, AMPRole=AMPRole, f3AmpStatsProvDataRx=f3AmpStatsProvDataRx, f3AmpConfigRemSysSrcIpAddrType=f3AmpConfigRemSysSrcIpAddrType, f3AmpConfigRemTunnelCIR=f3AmpConfigRemTunnelCIR, f3AmpStatsSpuriousMessageRx=f3AmpStatsSpuriousMessageRx, f3AmpStatsLastTxStatus=f3AmpStatsLastTxStatus, f3AmpGroups=f3AmpGroups, f3AmpStatsLastRxStatus=f3AmpStatsLastRxStatus, f3AmpConfigGroup=f3AmpConfigGroup, f3AmpConfigRemTunnelIndex=f3AmpConfigRemTunnelIndex, f3AMPMIB=f3AMPMIB, f3AmpConfigRemTunnelSVlanId=f3AmpConfigRemTunnelSVlanId, f3AmpConfigRemSysIpMask=f3AmpConfigRemSysIpMask, f3AmpConfigRemSysIpAddr=f3AmpConfigRemSysIpAddr, f3AmpConfigStatus=f3AmpConfigStatus, f3AmpConfigRemTunnelVlanId=f3AmpConfigRemTunnelVlanId, f3AmpConfigRemTunnelEncapType=f3AmpConfigRemTunnelEncapType, f3AmpConfigObjects=f3AmpConfigObjects, AMPConfigStatus=AMPConfigStatus, f3AmpConfigRemTunnelCOS=f3AmpConfigRemTunnelCOS, f3AmpConfigRemSysName=f3AmpConfigRemSysName, AMPStatus=AMPStatus, f3AmpStatsRxTimeStamp=f3AmpStatsRxTimeStamp)
