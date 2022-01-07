#
# PySNMP MIB module CTRON-SFPS-PORT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-SFPS-PORT-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:05:38 2022
# On host fv-az135-792 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
sfpsPortAttributeAPI, sfpsPortConfig, sfpsPortAttributeTable, sfpsPortStats = mibBuilder.importSymbols("CTRON-SFPS-INCLUDE-MIB", "sfpsPortAttributeAPI", "sfpsPortConfig", "sfpsPortAttributeTable", "sfpsPortStats")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Gauge32, Bits, Integer32, MibIdentifier, TimeTicks, Unsigned32, ModuleIdentity, Counter32, ObjectIdentity, NotificationType, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Gauge32", "Bits", "Integer32", "MibIdentifier", "TimeTicks", "Unsigned32", "ModuleIdentity", "Counter32", "ObjectIdentity", "NotificationType", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class SfpsSwitchPort(Integer32):
    pass

class HexInteger(Integer32):
    pass

sfpsInPortConfigTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 1), )
if mibBuilder.loadTexts: sfpsInPortConfigTable.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsInPortConfigTable.setDescription('This table contains the configuration information of each\n                 configured inbound SFPS switch port.  If SFPS is not\n                 configured on a port, than an entry will not exist.')
sfpsInPortConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 1, 1), ).setIndexNames((0, "CTRON-SFPS-PORT-MIB", "sfpsInPortConfigPort"))
if mibBuilder.loadTexts: sfpsInPortConfigEntry.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsInPortConfigEntry.setDescription('Each entry specifies the SFPS configuration for the SFPS\n                inbound switch port for which the entry exists.')
sfpsInPortConfigPort = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 1, 1, 1), SfpsSwitchPort()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsInPortConfigPort.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsInPortConfigPort.setDescription('The primary index to the SFPS in port table.  This identifies\n                the inbound SFPS switch port for which the entry exists.')
sfpsInPortConfigAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3), ("loopback", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsInPortConfigAdminStatus.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsInPortConfigAdminStatus.setDescription('Sets the administrative state of the SFPS inbound switch port\n                 for which the entry exists.')
sfpsInPortConfigOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3), ("pending-disable", 4), ("pending-enable", 5), ("invalid-config", 6), ("testing", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsInPortConfigOperStatus.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsInPortConfigOperStatus.setDescription('Indicates the current operating condition of the SFPS\n                 on the inbound switch port for which this entry exists.')
sfpsInPortConfigOperTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 1, 1, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsInPortConfigOperTime.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsInPortConfigOperTime.setDescription('Indicates the elapsed time, in hundredths of a second,\n                 that sfpsInPortOperStatus has been in its current\n                 operational state on the SFPS inbound switch port for which\n                 this entry exists.')
sfpsInPortConfigType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20))).clone(namedValues=NamedValues(("other", 1), ("access-port", 2), ("network-port", 3), ("host-mgmt-port", 4), ("host-ctl-port", 5), ("unknown", 6), ("going-to-access", 7), ("hybrid-port", 8), ("stand-by", 9), ("network-only", 10), ("accessOnly", 11), ("raPrimary", 12), ("uplink", 13), ("fclStandby", 14), ("loopStandby", 15), ("raStandby", 16), ("flood", 17), ("uplinkFlood", 18), ("downlinkFlood", 19), ("unknown-ra-standby", 20)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsInPortConfigType.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsInPortConfigType.setDescription('Sets the type of port access attribute for the inbound SFPS\n                 port for which the entry exists.  Access ports allow single\n                 user or shared access and perform statisics and control;\n                 network ports are equivalent to trunk ports with no access\n                 control; host management port indicates the (virtual) port\n                 to which the (internal) management agent is attached; host\n                 control port indicates the port to redirect non-management\n                 packets.')
sfpsInPortConfigReservedBW = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 1, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsInPortConfigReservedBW.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsInPortConfigReservedBW.setDescription('Sets the amount of Bandwidth that is reserved for the inbound\n                 SFPS port for which this entry exists.  This bandwidth is\n                 set aside for this port and may be given to another port if\n                 unused.')
sfpsInPortConfigAllocBW = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsInPortConfigAllocBW.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsInPortConfigAllocBW.setDescription('Sets the amount of Bandwidth that is allocated for\n                 the inbound SFPS port for which this entry exists.\n                 This bandwidth may be less than the reserved\n                 bandwidth.')
sfpsInPortConfigQoS = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 1, 1, 8), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsInPortConfigQoS.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsInPortConfigQoS.setDescription('Sets the desired QoS service class for the inbound\n                 SFPS port for which this entry exists.')
sfpsInPortConfigQSize = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsInPortConfigQSize.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsInPortConfigQSize.setDescription('Indicates the maximum inbound queue size for this port.\n                 Size is indicated in packets (packet descriptors).')
sfpsInPortConfigQLen = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 1, 1, 10), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsInPortConfigQLen.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsInPortConfigQLen.setDescription('Indicates the actual inbound queue size for this port.\n                 Size is indicated in packets (packet descriptors).  This\n                 is a transient value that reflects the current depth of\n                 queue.')
sfpsInPortConfigSwitchId = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 1, 1, 11), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsInPortConfigSwitchId.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsInPortConfigSwitchId.setDescription('This entry is the id of the port.')
sfpsInPortConfigMediaType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14))).clone(namedValues=NamedValues(("ethernet", 1), ("fddi", 2), ("atm-lec", 3), ("token-ring", 4), ("wan", 5), ("inb", 6), ("hcp", 7), ("hdp", 8), ("atm-svc", 9), ("atm-pvc", 10), ("unknown", 11), ("atm-forum-lec", 12), ("atm-forum-pvc", 13), ("atm-forum-svc", 14)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsInPortConfigMediaType.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsInPortConfigMediaType.setDescription('')
sfpsInPortConfigFrontPanelPort = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 1, 1, 13), SfpsSwitchPort()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsInPortConfigFrontPanelPort.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsInPortConfigFrontPanelPort.setDescription('This represents the front panel physical port number')
sfpsInPortConfigLinkStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("linkUp", 2), ("linkDown", 3), ("link-N-A", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsInPortConfigLinkStatus.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsInPortConfigLinkStatus.setDescription('The link status of this port.')
sfpsInPortConfigLinkStateAge = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 1, 1, 15), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsInPortConfigLinkStateAge.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsInPortConfigLinkStateAge.setDescription('Number of time ticks that link has been in this state.')
sfpsInPortConfigRouterPort = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 1, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("router-port", 2), ("no-router", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsInPortConfigRouterPort.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsInPortConfigRouterPort.setDescription('Specifies whether this port is a router port.')
sfpsInPortConfigSlotNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 1, 1, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsInPortConfigSlotNumber.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsInPortConfigSlotNumber.setDescription('Slot number in the chassis.')
sfpsInPortConfigMib2PortId = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 1, 1, 18), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsInPortConfigMib2PortId.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsInPortConfigMib2PortId.setDescription('Mib2 Port id')
sfpsInPortConfigTopoAgent = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 1, 1, 19), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsInPortConfigTopoAgent.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsInPortConfigTopoAgent.setDescription('Topology Agent')
sfpsInPortConfigLayer3Learning = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 1, 1, 22), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("enabled", 2), ("disabled", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsInPortConfigLayer3Learning.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsInPortConfigLayer3Learning.setDescription('Topology Agent')
sfpsOutPortConfigTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 2), )
if mibBuilder.loadTexts: sfpsOutPortConfigTable.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsOutPortConfigTable.setDescription('This table contains the configuration information of each\n                 configured outbound SFPS switch port.  If SFPS is not\n                 configured on a port, than an entry will not exist.')
sfpsOutPortConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 2, 1), ).setIndexNames((0, "CTRON-SFPS-PORT-MIB", "sfpsOutPortConfigPort"))
if mibBuilder.loadTexts: sfpsOutPortConfigEntry.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsOutPortConfigEntry.setDescription('Each entry specifies the SFPS configuration for the SFPS\n                outbound switch port for which the entry exists.')
sfpsOutPortConfigPort = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 2, 1, 1), SfpsSwitchPort()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsOutPortConfigPort.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsOutPortConfigPort.setDescription('The primary index to the SFPS in port table.  This identifies\n                the outbound SFPS switch port for which the entry exists.')
sfpsOutPortConfigAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3), ("loopback", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsOutPortConfigAdminStatus.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsOutPortConfigAdminStatus.setDescription('Sets the administrative state of the SFPS outbound switch port\n                 for which the entry exists.')
sfpsOutPortConfigOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3), ("pending-disable", 4), ("pending-enable", 5), ("invalid-config", 6), ("testing", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsOutPortConfigOperStatus.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsOutPortConfigOperStatus.setDescription('Indicates the current operating condition of the SFPS\n                 on the outbound switch port for which this entry exists.')
sfpsOutPortConfigOperTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 2, 1, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsOutPortConfigOperTime.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsOutPortConfigOperTime.setDescription('Indicates the elapsed time, in hundredths of a second,\n                 that sfpsOutPortOperStatus has been in its current\n                 operational state on the SFPS outbound switch port for which\n                 this entry exists.')
sfpsOutPortConfigType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20))).clone(namedValues=NamedValues(("other", 1), ("access-port", 2), ("network-port", 3), ("host-mgmt-port", 4), ("host-ctl-port", 5), ("unknown", 6), ("going-to-access", 7), ("hybrid-port", 8), ("stand-by", 9), ("network-only", 10), ("accessOnly", 11), ("raPrimary", 12), ("standbyFCLConflict", 13), ("standbyLoopedPort", 14), ("standbyVersionConflict", 15), ("standbyRANonPrimary", 16), ("flood", 17), ("uplinkFlood", 18), ("downlinkFlood", 19), ("unknown-ra-standby", 20)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsOutPortConfigType.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsOutPortConfigType.setDescription('Sets the type of port access attribute for the outbound SFPS\n                 port for which the entry exists.  Access ports allow single\n                 user or shared access and perform statisics and control;\n                 network ports are equivalent to trunk ports with no access\n                 control; host management port indicates the (virtual) port\n                 to which the (internal) management agent is attached; host\n                 control port indicates the port to redirect non-management\n                 packets.')
sfpsOutPortConfigReservedBW = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 2, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsOutPortConfigReservedBW.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsOutPortConfigReservedBW.setDescription('Sets the amount of Bandwidth that is reserved for the outbound\n                 SFPS port for which this entry exists.  This bandwidth is\n                 set aside for this port and may be given to another port if\n                 unused.')
sfpsOutPortConfigAllocBW = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsOutPortConfigAllocBW.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsOutPortConfigAllocBW.setDescription('Sets the amount of Bandwidth that is allocated for\n                 the outbound  SFPS port for which this entry exists.\n                 This bandwidth may be less than the reserved\n                 bandwidth.')
sfpsOutPortConfigQoS = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 2, 1, 8), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsOutPortConfigQoS.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsOutPortConfigQoS.setDescription('Sets the desired QoS service class for the outbound\n                 SFPS port for which this entry exists.')
sfpsOutPortConfigQSize = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 2, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsOutPortConfigQSize.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsOutPortConfigQSize.setDescription('Indicates the maximum outbound queue size for this port.\n                 Size is indicated in packets (packet descriptors).')
sfpsOutPortConfigQLen = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 2, 1, 10), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsOutPortConfigQLen.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsOutPortConfigQLen.setDescription('Indicates the actual outbound queue size for this port.\n                 Size is indicated in packets (packet descriptors).  This\n                 is a transient value that reflects the current depth of\n                 queue.')
sfpsOutPortConfigSwitchId = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 2, 1, 11), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsOutPortConfigSwitchId.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsOutPortConfigSwitchId.setDescription('This entry is id of the port.')
sfpsOutPortConfigMediaType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 2, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14))).clone(namedValues=NamedValues(("ethernet", 1), ("fddi", 2), ("atm-lec", 3), ("token-ring", 4), ("wan", 5), ("inb", 6), ("hcp", 7), ("hdp", 8), ("atm-encap", 9), ("atm-pvc", 10), ("unknown", 11), ("atm-forum-lec", 12), ("atm-forum-pvc", 13), ("atm-forum-svc", 14)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsOutPortConfigMediaType.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsOutPortConfigMediaType.setDescription('')
sfpsOutPortConfigFrontPanelPort = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 2, 1, 13), SfpsSwitchPort()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsOutPortConfigFrontPanelPort.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsOutPortConfigFrontPanelPort.setDescription('')
sfpsOutPortConfigLinkStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 2, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("linkUp", 2), ("linkDown", 3), ("linkNA", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsOutPortConfigLinkStatus.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsOutPortConfigLinkStatus.setDescription('The link status of this port.')
sfpsOutPortConfigLinkStateAge = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 2, 1, 15), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsOutPortConfigLinkStateAge.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsOutPortConfigLinkStateAge.setDescription('Number of time ticks that link has been in this state.')
sfpsOutPortConfigRouterPort = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 2, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("router-port", 2), ("no-router", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsOutPortConfigRouterPort.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsOutPortConfigRouterPort.setDescription('Specifies whether this port is a router port.')
sfpsOutPortConfigSlotNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 2, 1, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsOutPortConfigSlotNumber.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsOutPortConfigSlotNumber.setDescription('Slot number in the chassis.')
sfpsOutPortConfigMib2PortId = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 2, 1, 18), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsOutPortConfigMib2PortId.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsOutPortConfigMib2PortId.setDescription('Mib2 Port id')
sfpsInPortStatsTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 2, 1), )
if mibBuilder.loadTexts: sfpsInPortStatsTable.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsInPortStatsTable.setDescription('This table contains the packet and byte counters for each\n                 inbound SFPS switch port.')
sfpsInPortStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 2, 1, 1), ).setIndexNames((0, "CTRON-SFPS-PORT-MIB", "sfpsInPortStatsPort"))
if mibBuilder.loadTexts: sfpsInPortStatsEntry.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsInPortStatsEntry.setDescription('Specifies the SFPS packet and byte counters for the\n                 inbound SFPS switch port for which this entry exists.')
sfpsInPortStatsPort = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 2, 1, 1, 1), SfpsSwitchPort()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsInPortStatsPort.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsInPortStatsPort.setDescription('The primary index to the SFPS port table.  This identifies\n                the SFPS inbound switch port for which the entry exists.')
sfpsInPortStatsAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsInPortStatsAdminStatus.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsInPortStatsAdminStatus.setDescription('Sets the administrative state of the SFPS packet and byte\n                 counters on the inbound SFPS switch port for which this entry\n                 exists.')
sfpsInPortStatsReset = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("other", 1), ("reset", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsInPortStatsReset.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsInPortStatsReset.setDescription('Resets the SFPS packet and byte counters on the inbound SFPS\n                switch port for which this entry exists.')
sfpsInPortStatsOperTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 2, 1, 1, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsInPortStatsOperTime.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsInPortStatsOperTime.setDescription('Indicates the amount of time (# of time ticks) that the\n                port-specific SFPS packet and byte counters have been\n                active on the inbound SFPS switch port for which this entry\n                exists.')
sfpsInPortStatsPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 2, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsInPortStatsPkts.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsInPortStatsPkts.setDescription('Indicates the total number of SFPS packets that have been\n                 received, during sfpsInPortStatsOpertime, on the inbound\n                 SFPS switch port for which this entry exists.')
sfpsInPortStatsDiscardPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 2, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsInPortStatsDiscardPkts.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsInPortStatsDiscardPkts.setDescription('Indicates the total number of SFPS packets that have been\n                 discarded (dropped), during sfpsInPortStatsOpertime, on the\n                 inbound SFPS switch port for which this entry exists')
sfpsInPortStatsBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 2, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsInPortStatsBytes.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsInPortStatsBytes.setDescription('Indicates the total number of SFPS bytes that have been\n                received, during sfpsInPortStatsOperTime, on the inbound\n                SFPS switch port for which the entry exists.')
sfpsInPortStatsDiscardBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 2, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsInPortStatsDiscardBytes.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsInPortStatsDiscardBytes.setDescription('Indicates the total number of bytes in the SFPS packets\n                that have been discarded (dropped), during\n                sfpsInPortStatsOperTime, on the inbound SFPS switch port for\n                which the entry exists.')
sfpsInPortStatsQOverflows = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 2, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsInPortStatsQOverflows.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsInPortStatsQOverflows.setDescription('Indicates the total number of queue overflow conditions\n                 have been experienced for the inbound SFPS switch port\n                 for which the entry exists.')
sfpsInPortStatsLinkUps = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 2, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsInPortStatsLinkUps.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsInPortStatsLinkUps.setDescription('The number of link ups that this port has seen.')
sfpsInPortStatsLinkDowns = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 2, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsInPortStatsLinkDowns.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsInPortStatsLinkDowns.setDescription('The number of link downs that this port has seen.')
sfpsOutPortStatsTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 2, 2), )
if mibBuilder.loadTexts: sfpsOutPortStatsTable.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsOutPortStatsTable.setDescription('This table contains the packet and byte counters for each\n                 outbound SFPS switch port.')
sfpsOutPortStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 2, 2, 1), ).setIndexNames((0, "CTRON-SFPS-PORT-MIB", "sfpsOutPortStatsPort"))
if mibBuilder.loadTexts: sfpsOutPortStatsEntry.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsOutPortStatsEntry.setDescription('Specifies the SFPS packet and byte counters for the\n                 outbound SFPS switch port for which this entry exists.')
sfpsOutPortStatsPort = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 2, 2, 1, 1), SfpsSwitchPort()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsOutPortStatsPort.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsOutPortStatsPort.setDescription('The primary index to the SFPS port table.  This identifies\n                the SFPS outbound switch port for which the entry exists.')
sfpsOutPortStatsAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsOutPortStatsAdminStatus.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsOutPortStatsAdminStatus.setDescription('Sets the administrative state of the SFPS packet and byte\n                 counters on the outbound SFPS switch port for which this entry\n                 exists.')
sfpsOutPortStatsReset = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("other", 1), ("reset", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsOutPortStatsReset.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsOutPortStatsReset.setDescription('Resets the SFPS packet and byte counters on the outbound SFPS\n                switch port for which this entry exists.')
sfpsOutPortStatsOperTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 2, 2, 1, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsOutPortStatsOperTime.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsOutPortStatsOperTime.setDescription('Indicates the amount of time (# of time ticks) that the\n                port-specific SFPS packet and byte counters have been\n                active on the outbound SFPS switch port for which this entry\n                exists.')
sfpsOutPortStatsPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 2, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsOutPortStatsPkts.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsOutPortStatsPkts.setDescription('Indicates the total number of SFPS packets that have been\n                 received, during sfpsOutPortStatsOpertime, on the outbound\n                 SFPS switch port for which this entry exists.')
sfpsOutPortStatsDiscardPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 2, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsOutPortStatsDiscardPkts.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsOutPortStatsDiscardPkts.setDescription('Indicates the total number of SFPS packets that have been\n                 discarded (dropped), during sfpsOutPortStatsOpertime, on the\n                 outbound SFPS switch port for which this entry exists')
sfpsOutPortStatsBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 2, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsOutPortStatsBytes.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsOutPortStatsBytes.setDescription('Indicates the total number of SFPS bytes that have been\n                received, during sfpsOutPortStatsOperTime, on the outbound\n                SFPS switch port for which the entry exists.')
sfpsOutPortStatsDiscardBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 2, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsOutPortStatsDiscardBytes.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsOutPortStatsDiscardBytes.setDescription('Indicates the total number of bytes in the SFPS packets\n                that have been discarded (dropped), during\n                sfpsOutPortStatsOperTime, on the outbound SFPS switch port for\n                which the entry exists.')
sfpsOutPortStatsQOverflows = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 2, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsOutPortStatsQOverflows.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsOutPortStatsQOverflows.setDescription('Indicates the total number of queue overflow conditions\n                 have been experienced for the outbound SFPS switch port\n                 for which the entry exists.')
sfpsOutPortStatsLinkUps = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 2, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsOutPortStatsLinkUps.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsOutPortStatsLinkUps.setDescription('The number of link ups that this port has seen.')
sfpsOutPortStatsLinkDowns = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 2, 2, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsOutPortStatsLinkDowns.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsOutPortStatsLinkDowns.setDescription('The number of link downs that this port has seen.')
sfpsPortAttributePort = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 9, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsPortAttributePort.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsPortAttributePort.setDescription('')
sfpsPortAttributeAttributes = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 9, 1, 2), HexInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsPortAttributeAttributes.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsPortAttributeAttributes.setDescription('')
sfpsPortAttributeLearnSelfArp = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 9, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2, 1))).clone(namedValues=NamedValues(("off", 2), ("on", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsPortAttributeLearnSelfArp.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsPortAttributeLearnSelfArp.setDescription('')
sfpsPortAttributeAPIVerb = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 9, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("resetAll", 2), ("resetPort", 3), ("enablePortAttr", 4), ("disablePortAttr", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsPortAttributeAPIVerb.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsPortAttributeAPIVerb.setDescription('')
sfpsPortAttributeAPIPort = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 9, 2, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsPortAttributeAPIPort.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsPortAttributeAPIPort.setDescription('')
sfpsPortAttributeAPIAttribute = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 9, 2, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2, 1))).clone(namedValues=NamedValues(("none", 2), ("learnSelfArp", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsPortAttributeAPIAttribute.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsPortAttributeAPIAttribute.setDescription('')
mibBuilder.exportSymbols("CTRON-SFPS-PORT-MIB", sfpsInPortConfigLinkStatus=sfpsInPortConfigLinkStatus, sfpsOutPortStatsOperTime=sfpsOutPortStatsOperTime, sfpsOutPortConfigType=sfpsOutPortConfigType, sfpsOutPortConfigRouterPort=sfpsOutPortConfigRouterPort, sfpsOutPortConfigOperTime=sfpsOutPortConfigOperTime, sfpsOutPortConfigLinkStateAge=sfpsOutPortConfigLinkStateAge, sfpsInPortStatsDiscardBytes=sfpsInPortStatsDiscardBytes, sfpsInPortStatsTable=sfpsInPortStatsTable, sfpsOutPortConfigLinkStatus=sfpsOutPortConfigLinkStatus, sfpsOutPortStatsAdminStatus=sfpsOutPortStatsAdminStatus, sfpsInPortConfigTable=sfpsInPortConfigTable, sfpsOutPortConfigOperStatus=sfpsOutPortConfigOperStatus, sfpsOutPortStatsQOverflows=sfpsOutPortStatsQOverflows, sfpsInPortConfigMediaType=sfpsInPortConfigMediaType, sfpsInPortConfigSlotNumber=sfpsInPortConfigSlotNumber, sfpsOutPortStatsPkts=sfpsOutPortStatsPkts, sfpsPortAttributeAPIVerb=sfpsPortAttributeAPIVerb, sfpsOutPortConfigReservedBW=sfpsOutPortConfigReservedBW, sfpsOutPortConfigQoS=sfpsOutPortConfigQoS, sfpsOutPortConfigPort=sfpsOutPortConfigPort, sfpsOutPortStatsTable=sfpsOutPortStatsTable, sfpsOutPortConfigFrontPanelPort=sfpsOutPortConfigFrontPanelPort, sfpsOutPortConfigSwitchId=sfpsOutPortConfigSwitchId, sfpsInPortConfigAdminStatus=sfpsInPortConfigAdminStatus, sfpsInPortConfigAllocBW=sfpsInPortConfigAllocBW, sfpsOutPortStatsDiscardPkts=sfpsOutPortStatsDiscardPkts, sfpsPortAttributePort=sfpsPortAttributePort, sfpsOutPortConfigSlotNumber=sfpsOutPortConfigSlotNumber, sfpsInPortStatsEntry=sfpsInPortStatsEntry, sfpsInPortStatsQOverflows=sfpsInPortStatsQOverflows, sfpsPortAttributeLearnSelfArp=sfpsPortAttributeLearnSelfArp, sfpsOutPortStatsDiscardBytes=sfpsOutPortStatsDiscardBytes, sfpsInPortConfigQLen=sfpsInPortConfigQLen, sfpsInPortConfigOperTime=sfpsInPortConfigOperTime, sfpsInPortStatsOperTime=sfpsInPortStatsOperTime, sfpsInPortStatsLinkUps=sfpsInPortStatsLinkUps, sfpsInPortConfigReservedBW=sfpsInPortConfigReservedBW, sfpsInPortConfigPort=sfpsInPortConfigPort, sfpsOutPortConfigQSize=sfpsOutPortConfigQSize, sfpsPortAttributeAttributes=sfpsPortAttributeAttributes, sfpsOutPortStatsPort=sfpsOutPortStatsPort, sfpsInPortConfigType=sfpsInPortConfigType, sfpsInPortConfigMib2PortId=sfpsInPortConfigMib2PortId, sfpsOutPortConfigEntry=sfpsOutPortConfigEntry, sfpsInPortConfigQSize=sfpsInPortConfigQSize, sfpsInPortStatsAdminStatus=sfpsInPortStatsAdminStatus, sfpsInPortStatsReset=sfpsInPortStatsReset, sfpsInPortStatsDiscardPkts=sfpsInPortStatsDiscardPkts, sfpsInPortStatsPort=sfpsInPortStatsPort, sfpsInPortConfigFrontPanelPort=sfpsInPortConfigFrontPanelPort, sfpsOutPortStatsLinkUps=sfpsOutPortStatsLinkUps, sfpsOutPortStatsBytes=sfpsOutPortStatsBytes, sfpsInPortConfigLinkStateAge=sfpsInPortConfigLinkStateAge, sfpsInPortConfigTopoAgent=sfpsInPortConfigTopoAgent, sfpsInPortConfigSwitchId=sfpsInPortConfigSwitchId, sfpsOutPortConfigAllocBW=sfpsOutPortConfigAllocBW, sfpsPortAttributeAPIPort=sfpsPortAttributeAPIPort, sfpsInPortConfigQoS=sfpsInPortConfigQoS, sfpsOutPortConfigTable=sfpsOutPortConfigTable, sfpsOutPortConfigQLen=sfpsOutPortConfigQLen, sfpsOutPortStatsLinkDowns=sfpsOutPortStatsLinkDowns, sfpsOutPortConfigMediaType=sfpsOutPortConfigMediaType, sfpsOutPortConfigAdminStatus=sfpsOutPortConfigAdminStatus, sfpsOutPortConfigMib2PortId=sfpsOutPortConfigMib2PortId, sfpsInPortStatsLinkDowns=sfpsInPortStatsLinkDowns, sfpsInPortConfigEntry=sfpsInPortConfigEntry, sfpsInPortStatsBytes=sfpsInPortStatsBytes, sfpsOutPortStatsEntry=sfpsOutPortStatsEntry, sfpsPortAttributeAPIAttribute=sfpsPortAttributeAPIAttribute, HexInteger=HexInteger, sfpsInPortConfigLayer3Learning=sfpsInPortConfigLayer3Learning, sfpsInPortConfigRouterPort=sfpsInPortConfigRouterPort, sfpsInPortStatsPkts=sfpsInPortStatsPkts, SfpsSwitchPort=SfpsSwitchPort, sfpsInPortConfigOperStatus=sfpsInPortConfigOperStatus, sfpsOutPortStatsReset=sfpsOutPortStatsReset)
