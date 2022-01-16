#
# PySNMP MIB module RC-VRF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/nortel/RC-VRF-MIB
# Produced by pysmi-1.1.8 at Sun Jan 16 00:41:51 2022
# On host fv-az42-839 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
EnableValue, rcVrf, IdList = mibBuilder.importSymbols("RAPID-CITY", "EnableValue", "rcVrf", "IdList")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
iso, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Counter64, Counter32, mib_2, Gauge32, ObjectIdentity, Unsigned32, IpAddress, Integer32, Bits, MibIdentifier, ModuleIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Counter64", "Counter32", "mib-2", "Gauge32", "ObjectIdentity", "Unsigned32", "IpAddress", "Integer32", "Bits", "MibIdentifier", "ModuleIdentity", "TimeTicks")
RowStatus, TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TruthValue", "DisplayString", "TextualConvention")
rcVrfMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 2272, 1, 203, 1))
rcVrfMib.setRevisions(('2008-09-09 00:00', '2008-05-18 00:00', '2008-05-16 00:00', '2008-05-13 00:00', '2008-05-09 00:00', '2008-05-08 00:00', '2008-04-28 00:00', '2008-03-13 00:00', '2007-12-18 00:00', '2007-05-03 00:00', '2007-01-24 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rcVrfMib.setRevisionsDescriptions(('Version 11: added values isis(3) and pim(4) to VrfRpTriggerBitCode.', 'Version 10: corrected the enum values for rcVrfIpVpnSvcLblAllocOpt.', 'Version 9: Updated default value for rcVrfRpTrigger and removed vrrp bit from VrfRpTriggerBitCode.', 'Version 8: Updated default value for rcVrfRpTrigger.', 'Version 7: Fixed smilint errors.', 'Version 6: Removed embedded control characters\n                               (was causing compile errors).', 'Version 5: Fixed smilint issues.', "Version 4: Changed module name to 'RC-VRF-MIB'\nfrom 'RC-VIRTUAL-ROUTING-MIB'.", 'Version 3: Changed syntax of rcVrfIpVpnStatus from TruthValue to EnableValue', 'Version 2: Add rcVrfIpVpnTableSize, rcVrfIpVpnTable.', 'Version 1: Initial version',))
if mibBuilder.loadTexts: rcVrfMib.setLastUpdated('200809090000Z')
if mibBuilder.loadTexts: rcVrfMib.setOrganization('Nortel Networks')
if mibBuilder.loadTexts: rcVrfMib.setContactInfo('Alka Malik\n             Postal:  Nortel Networks, Inc. \n                      600 Technology Park\n                      Billerica, MA 01821\n              email:  alka@nortel.com\n                     ')
if mibBuilder.loadTexts: rcVrfMib.setDescription('The MIB module is the definition of the managed\n                      objects for the Virtual Router.')
class VrfIdentifier(TextualConvention, Unsigned32):
    description = "Virtual Router Identifier.\n             VRFID 0 is reserved for the Administrative VRF\n             and cannot be used to create VRF's.\n            "
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class VPNId(TextualConvention, OctetString):
    reference = "Fox, B. and Gleeson, B., 'Virtual Private Networks\n             Identifier', RFC 2685, September 1999."
    description = 'The purpose of a VPN-ID is to uniquely identify a VPN.\n             The Global VPN Identifier format is:\n             3 octet VPN Authority, Organizationally Unique Identifier\n             followed by 4 octet VPN index identifying VPN according\n             to OUI'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(7, 7)
    fixedLength = 7

class VrfRpTriggerBitCode(TextualConvention, Bits):
    description = 'This object represents Routing Protocol (RP)\n             Triggers on a Virtual Router.  The BITS\n             represent an Action-code that specifies the\n             action on the Routing Protocols.\n\n             The actions are:  initiate or shutdown.\n\n             When encoding the RP using the BITS construct,\n             the value is encoded as an OCTET STRING where\n             the first bit (bit 0) is the highest bit of the\n             octet.\n\n             Bits 0-3 may be specified in any combination to\n             allow multiple Routing Protocols to be acted on\n             simultaneously or individually.\n            '
    status = 'current'
    namedValues = NamedValues(("rip", 0), ("ospf", 1), ("bgp", 2), ("isis", 3), ("pim", 4))

rcVrfNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2272, 1, 203, 1, 0))
rcVrfObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2272, 1, 203, 1, 1))
rcVrfNotificationObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2272, 1, 203, 1, 2))
rcVrfConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 2272, 1, 203, 1, 1, 1))
rcVrfConfigScalars = MibIdentifier((1, 3, 6, 1, 4, 1, 2272, 1, 203, 1, 1, 1, 1))
rcVrfConfigNextAvailableVrfId = MibScalar((1, 3, 6, 1, 4, 1, 2272, 1, 203, 1, 1, 1, 1, 1), VrfIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rcVrfConfigNextAvailableVrfId.setStatus('current')
if mibBuilder.loadTexts: rcVrfConfigNextAvailableVrfId.setDescription('The next available Virtual Router Id (index).\n            This object provides a hint for the rcVrfId value\n            to use when administratively creating a new\n            rcVrfConfigEntry.\n\n            A GET of this object returns the next available rcVrfId\n            value to be used to create an entry in the associated\n            rcVrfConfigTable; or zero, if no valid rcVrfId\n            value is available. A value of zero(0) indicates that\n            it is not possible to create a new rcVrfConfigEntry.\n            This object also returns a value of zero when it is the\n            lexicographic successor of a varbind presented in an\n            SNMP GETNEXT or GETBULK request, for which circumstance\n            it is assumed that ifIndex allocation is unintended.\n\n            Successive GETs will typically return different\n            values, thus avoiding collisions among cooperating\n            management clients seeking to create table entries\n            simultaneously.\n\n            Unless specified otherwise by its MAX-ACCESS and\n            DESCRIPTION clauses, an object of this type is read-only,\n            and a SET of such an object returns a notWritable error.')
rcVrfConfigTable = MibTable((1, 3, 6, 1, 4, 1, 2272, 1, 203, 1, 1, 1, 2), )
if mibBuilder.loadTexts: rcVrfConfigTable.setStatus('current')
if mibBuilder.loadTexts: rcVrfConfigTable.setDescription('This table is for creating the new Virtual Routers.')
rcVrfConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2272, 1, 203, 1, 1, 1, 2, 1), ).setIndexNames((0, "RC-VRF-MIB", "rcVrfId"))
if mibBuilder.loadTexts: rcVrfConfigEntry.setStatus('current')
if mibBuilder.loadTexts: rcVrfConfigEntry.setDescription('The entries in this table can be added/deleted\n            using the rcVrfRowStatus.')
rcVrfId = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 203, 1, 1, 1, 2, 1, 1), VrfIdentifier())
if mibBuilder.loadTexts: rcVrfId.setStatus('current')
if mibBuilder.loadTexts: rcVrfId.setDescription('The unique id of this virtual router instance. A Virtual\n             Router cannot not be created with rcVrfId = 0.\n             VRFID 0 is reserved for the Administrative VRF.\n            ')
rcVrfRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 203, 1, 1, 1, 2, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rcVrfRowStatus.setStatus('current')
if mibBuilder.loadTexts: rcVrfRowStatus.setDescription("The status column has three defined values:\n\n            - `active', which indicates that the conceptual row is\n            available for use by the managed device;\n            - `createAndGo', which is supplied by a management\n            station wishing to create a new instance of a\n            conceptual row and to have its status automatically set\n            to active, making it available for use by the managed\n            device;\n\n            - `destroy', which is supplied by a management station\n            wishing to delete all of the instances associated with\n            an existing conceptual row.")
rcVrfName = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 203, 1, 1, 1, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rcVrfName.setStatus('current')
if mibBuilder.loadTexts: rcVrfName.setDescription('The Name of the Virtual Router.')
rcVrfContextName = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 203, 1, 1, 1, 2, 1, 4), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rcVrfContextName.setStatus('current')
if mibBuilder.loadTexts: rcVrfContextName.setDescription("The SNMPv2 Community String or SNMPv3 contextName\n            denotes the VRF 'context' and is used to logically\n            separate the MIB module management.")
rcVrfTrapEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 203, 1, 1, 1, 2, 1, 5), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rcVrfTrapEnable.setStatus('current')
if mibBuilder.loadTexts: rcVrfTrapEnable.setDescription('This objects is used to enable the generation\n            of the VrfUp and VrfDown traps.\n                true(1)     - VRF Traps Enabled\n                false(2)    - VRF Traps Disabled')
rcVrfMaxRoutes = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 203, 1, 1, 1, 2, 1, 6), Unsigned32().clone(10000)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rcVrfMaxRoutes.setStatus('current')
if mibBuilder.loadTexts: rcVrfMaxRoutes.setDescription('This object specifies the maximum number of routes that\n            this VRF can support. The default value is 10000.')
rcVrfAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 203, 1, 1, 1, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("testing", 3), ("unknown", 4))).clone('down')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rcVrfAdminStatus.setStatus('current')
if mibBuilder.loadTexts: rcVrfAdminStatus.setDescription('The administrative state of the Virtual Router.')
rcVrfVpnId = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 203, 1, 1, 1, 2, 1, 8), VPNId()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rcVrfVpnId.setStatus('current')
if mibBuilder.loadTexts: rcVrfVpnId.setDescription('The Virtual Private Network Identifier of the Virtual\n             Router.')
rcVrfRpTrigger = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 203, 1, 1, 1, 2, 1, 9), VrfRpTriggerBitCode().clone(namedValues=NamedValues(("rip", 0), ("ospf", 1)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rcVrfRpTrigger.setStatus('current')
if mibBuilder.loadTexts: rcVrfRpTrigger.setDescription("This object represents Routing Protocol (RP)\n             Triggers on a Virtual Router and it meant to\n             be used to initiate or shutdown routing\n             protocols on a VRF.  Multiple RPs can be acted\n             on simultaneously.  Also, individual RPs can\n             be brought up in steps, which should not\n             affect the RPs that were running. The BITS\n             represent an Action-code that specifies what\n             action is to be performed for the RPs.\n             The actions are:  initiate(1) or shutdown(0).\n\n             The running status of an RP shall be available\n             in the VRF stats table's rcVrfRpStatus, which has\n             a similar format, but represents the status.\n\n             Bits 0-3 may be specified in any combination.\n             Individual routing protocols may be enabled\n             and disabled independently.  Protocols are\n             enabled by setting the respective BIT and are\n             disabled by resetting the BIT.\n\n             So, for example, to enable RIP and BGP protocols\n             the rcVrfRpTrigger bits 0 and 2 need to be set, and\n             as encoded as 10100000.\n             All zeros should be interpreted as all protocols\n             disable.\n            ")
rcVrfMaxRoutesTrapEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 203, 1, 1, 1, 2, 1, 10), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rcVrfMaxRoutesTrapEnable.setStatus('current')
if mibBuilder.loadTexts: rcVrfMaxRoutesTrapEnable.setDescription('This objects is used to enable the generation\n             of the VRF Max Routes Exceeded traps.\n                true(1)     - VRF Max Routes Exceeded Traps Enabled\n                false(2)    - VRF Max Routes Exceeded Traps Disabled')
rcVrfStat = MibIdentifier((1, 3, 6, 1, 4, 1, 2272, 1, 203, 1, 1, 2))
rcVrfStatScalars = MibIdentifier((1, 3, 6, 1, 4, 1, 2272, 1, 203, 1, 1, 2, 1))
rcVrfConfiguredVRFs = MibScalar((1, 3, 6, 1, 4, 1, 2272, 1, 203, 1, 1, 2, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rcVrfConfiguredVRFs.setStatus('current')
if mibBuilder.loadTexts: rcVrfConfiguredVRFs.setDescription('The number of VRFs configured on this network element.')
rcVrfActiveVRFs = MibScalar((1, 3, 6, 1, 4, 1, 2272, 1, 203, 1, 1, 2, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rcVrfActiveVRFs.setStatus('current')
if mibBuilder.loadTexts: rcVrfActiveVRFs.setDescription('The number of VRFs that are active on the network element.\n            These are VRFs for which the\n            rcVrfStatOperStatus  = up(1)')
rcVrfStatTable = MibTable((1, 3, 6, 1, 4, 1, 2272, 1, 203, 1, 1, 2, 2), )
if mibBuilder.loadTexts: rcVrfStatTable.setStatus('current')
if mibBuilder.loadTexts: rcVrfStatTable.setDescription('This table contains statistics for the Virtual Router.')
rcVrfStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2272, 1, 203, 1, 1, 2, 2, 1), ).setIndexNames((0, "RC-VRF-MIB", "rcVrfId"))
if mibBuilder.loadTexts: rcVrfStatEntry.setStatus('current')
if mibBuilder.loadTexts: rcVrfStatEntry.setDescription('Entries in this table are per rcVrfId.')
rcVrfStatRouteEntries = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 203, 1, 1, 2, 2, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rcVrfStatRouteEntries.setStatus('current')
if mibBuilder.loadTexts: rcVrfStatRouteEntries.setDescription('Total number of routes for this VRF.')
rcVrfStatFIBEntries = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 203, 1, 1, 2, 2, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rcVrfStatFIBEntries.setStatus('current')
if mibBuilder.loadTexts: rcVrfStatFIBEntries.setDescription('Total number of FIB Entries for this VRF.')
rcVrfStatUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 203, 1, 1, 2, 2, 1, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rcVrfStatUpTime.setStatus('current')
if mibBuilder.loadTexts: rcVrfStatUpTime.setDescription('The time in (in hundredths of a second) since\n            this VRF entry has been operational.')
rcVrfOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 203, 1, 1, 2, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("unknown", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rcVrfOperStatus.setStatus('current')
if mibBuilder.loadTexts: rcVrfOperStatus.setDescription('The operational status of the Virtual Router.')
rcVrfRpStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 203, 1, 1, 2, 2, 1, 5), VrfRpTriggerBitCode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rcVrfRpStatus.setStatus('current')
if mibBuilder.loadTexts: rcVrfRpStatus.setDescription('This object represents the status of Routing\n             Protocols on this VRF corresponding to the list\n             of RP specified in rcVrfRpTrigger.\n\n             The BITS represent an Action-code that specifies\n             the status of the RPs.\n             The status are:  initiated (1) or shutdown (0).\n             Initiated status is indicated when the respective\n             BIT value is 1 and indicates shutdown when the\n             respective BIT value is 0.\n\n             Bits 0-3 may appear in any combination to\n             indicate that RPs may be enabled and disabled\n             independently or that multiple RP are acted on\n             simultaneously.\n            ')
rcVrfRouterAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 203, 1, 1, 2, 2, 1, 6), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rcVrfRouterAddressType.setStatus('current')
if mibBuilder.loadTexts: rcVrfRouterAddressType.setDescription('Router Address Type of this VRF.')
rcVrfRouterAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 203, 1, 1, 2, 2, 1, 7), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rcVrfRouterAddress.setStatus('current')
if mibBuilder.loadTexts: rcVrfRouterAddress.setDescription('Router Address of this VRF.  It is derived from one of the\n            interfaces. If loopback interface is present, the loopback\n            interface address can be used. However, loopback interface\n            is optional.')
rcVrfIpVpnTableSize = MibScalar((1, 3, 6, 1, 4, 1, 2272, 1, 203, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rcVrfIpVpnTableSize.setStatus('current')
if mibBuilder.loadTexts: rcVrfIpVpnTableSize.setDescription('Size of Vrf IpVpn Table')
rcVrfIpVpnTable = MibTable((1, 3, 6, 1, 4, 1, 2272, 1, 203, 1, 1, 4), )
if mibBuilder.loadTexts: rcVrfIpVpnTable.setStatus('current')
if mibBuilder.loadTexts: rcVrfIpVpnTable.setDescription('Table required to configure vpn under ip.')
rcVrfIpVpnTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2272, 1, 203, 1, 1, 4, 1), ).setIndexNames((0, "RC-VRF-MIB", "rcVrfIpVpnVrfId"))
if mibBuilder.loadTexts: rcVrfIpVpnTableEntry.setStatus('current')
if mibBuilder.loadTexts: rcVrfIpVpnTableEntry.setDescription('Entries in this table are per rcVrfId.')
rcVrfIpVpnVrfId = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 203, 1, 1, 4, 1, 1), VrfIdentifier())
if mibBuilder.loadTexts: rcVrfIpVpnVrfId.setStatus('current')
if mibBuilder.loadTexts: rcVrfIpVpnVrfId.setDescription('The VrfId serves as the Index for the rcIpVpnVrfTable and\n                   also for the rcIpVpnRouteDistinguisherTable. It allows to\n                   connect to the vrf table to obtain other attributes like the\n                   vrf name, rcVrfMaxRoutesTrapEnable etc.')
rcVrfIpVpnStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 203, 1, 1, 4, 1, 2), EnableValue().clone('disable')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rcVrfIpVpnStatus.setStatus('current')
if mibBuilder.loadTexts: rcVrfIpVpnStatus.setDescription('The status of IpVpn.')
rcVrfIpVpnImportRTList = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 203, 1, 1, 4, 1, 3), IdList()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rcVrfIpVpnImportRTList.setStatus('current')
if mibBuilder.loadTexts: rcVrfIpVpnImportRTList.setDescription('The Import RT list is a list of all the route-targets\n                   attached to a particular vrf behaving in the import mode.')
rcVrfIpVpnExportRTList = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 203, 1, 1, 4, 1, 4), IdList()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rcVrfIpVpnExportRTList.setStatus('current')
if mibBuilder.loadTexts: rcVrfIpVpnExportRTList.setDescription('The Export RT list is a list of all the route-targets\n                   attached to a particular vrf in the export mode.')
rcVrfIpVpnSvcLblAllocOpt = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 203, 1, 1, 4, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("perVrfperNexthop", 1), ("perVrf", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rcVrfIpVpnSvcLblAllocOpt.setStatus('current')
if mibBuilder.loadTexts: rcVrfIpVpnSvcLblAllocOpt.setDescription('The service label allocation option for the ipvpn')
rcVrfIpVpnRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 203, 1, 1, 4, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rcVrfIpVpnRowStatus.setStatus('current')
if mibBuilder.loadTexts: rcVrfIpVpnRowStatus.setDescription('RowStatus for the Vpn Entry.')
mibBuilder.exportSymbols("RC-VRF-MIB", rcVrfId=rcVrfId, rcVrfConfigNextAvailableVrfId=rcVrfConfigNextAvailableVrfId, rcVrfIpVpnTable=rcVrfIpVpnTable, rcVrfMaxRoutes=rcVrfMaxRoutes, rcVrfStatRouteEntries=rcVrfStatRouteEntries, VrfIdentifier=VrfIdentifier, rcVrfConfiguredVRFs=rcVrfConfiguredVRFs, rcVrfIpVpnImportRTList=rcVrfIpVpnImportRTList, rcVrfName=rcVrfName, rcVrfRpStatus=rcVrfRpStatus, rcVrfConfigScalars=rcVrfConfigScalars, rcVrfRpTrigger=rcVrfRpTrigger, rcVrfTrapEnable=rcVrfTrapEnable, rcVrfNotificationObjects=rcVrfNotificationObjects, rcVrfConfigTable=rcVrfConfigTable, rcVrfConfig=rcVrfConfig, rcVrfStat=rcVrfStat, rcVrfIpVpnExportRTList=rcVrfIpVpnExportRTList, PYSNMP_MODULE_ID=rcVrfMib, rcVrfIpVpnRowStatus=rcVrfIpVpnRowStatus, VrfRpTriggerBitCode=VrfRpTriggerBitCode, rcVrfIpVpnSvcLblAllocOpt=rcVrfIpVpnSvcLblAllocOpt, rcVrfRouterAddressType=rcVrfRouterAddressType, rcVrfOperStatus=rcVrfOperStatus, rcVrfStatUpTime=rcVrfStatUpTime, rcVrfRowStatus=rcVrfRowStatus, rcVrfStatScalars=rcVrfStatScalars, rcVrfRouterAddress=rcVrfRouterAddress, rcVrfNotifications=rcVrfNotifications, rcVrfStatFIBEntries=rcVrfStatFIBEntries, rcVrfConfigEntry=rcVrfConfigEntry, rcVrfIpVpnStatus=rcVrfIpVpnStatus, rcVrfActiveVRFs=rcVrfActiveVRFs, rcVrfStatEntry=rcVrfStatEntry, VPNId=VPNId, rcVrfIpVpnTableSize=rcVrfIpVpnTableSize, rcVrfMib=rcVrfMib, rcVrfObjects=rcVrfObjects, rcVrfIpVpnTableEntry=rcVrfIpVpnTableEntry, rcVrfIpVpnVrfId=rcVrfIpVpnVrfId, rcVrfVpnId=rcVrfVpnId, rcVrfStatTable=rcVrfStatTable, rcVrfAdminStatus=rcVrfAdminStatus, rcVrfMaxRoutesTrapEnable=rcVrfMaxRoutesTrapEnable, rcVrfContextName=rcVrfContextName)
