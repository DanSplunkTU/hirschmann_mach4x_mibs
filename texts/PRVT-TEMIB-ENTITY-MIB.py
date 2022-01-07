#
# PySNMP MIB module PRVT-TEMIB-ENTITY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/telco-systems/binos/PRVT-TEMIB-ENTITY-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:39:26 2022
# On host fv-az36-988 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
mpls, = mibBuilder.importSymbols("PRVT-CR-LDP-MIB", "mpls")
PrvtLmgrIndex, PrvtLmgrPartnerStatus = mibBuilder.importSymbols("PRVT-LMGR-MIB", "PrvtLmgrIndex", "PrvtLmgrPartnerStatus")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Gauge32, Unsigned32, iso, ModuleIdentity, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, TimeTicks, NotificationType, Counter32, Counter64, MibIdentifier, IpAddress, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Unsigned32", "iso", "ModuleIdentity", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "TimeTicks", "NotificationType", "Counter32", "Counter64", "MibIdentifier", "IpAddress", "Bits")
DisplayString, TruthValue, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention", "RowStatus")
prvtTeMibEntityMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 8))
prvtTeMibEntityMib.setRevisions(('2007-12-06 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: prvtTeMibEntityMib.setRevisionsDescriptions(('Initial.',))
if mibBuilder.loadTexts: prvtTeMibEntityMib.setLastUpdated('200712060000Z')
if mibBuilder.loadTexts: prvtTeMibEntityMib.setOrganization('BATM Advanced Communication')
if mibBuilder.loadTexts: prvtTeMibEntityMib.setContactInfo(' BATM/Telco Systems Support team\n\t\t\t\t\tEmail: \n\t\t\t\tFor North America: techsupport@telco.com\n\t\t\t\tFor North Europe: support@batm.de, info@batm.de\n\t\t\t\tFor the rest of the world: techsupport@telco.com')
if mibBuilder.loadTexts: prvtTeMibEntityMib.setDescription('The MIB module for management of TE-MIB entities.')
prvtTeMibEntityObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 8, 1))
class PrvtTeMibAdminStatus(TextualConvention, Integer32):
    description = 'The desired administrative state of a TE-MIB entity.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("up", 1), ("down", 2))

class PrvtTeMibOperStatus(TextualConvention, Integer32):
    description = 'The current operational state of a TE-MIB entity.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("up", 1), ("down", 2), ("goingUp", 3), ("goingDown", 4), ("actFailed", 5))

class PrvtTeMibEntityIndex(TextualConvention, Unsigned32):
    description = 'The index value identifying a TE-MIB entity.'
    status = 'current'

class PrvtTeMibPartnerStatus(TextualConvention, Integer32):
    description = 'The state of a TE-MIB entity partner.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("initial", 0), ("activating", 1), ("active", 2), ("deactivating", 3), ("failedOver", 4), ("failed", 5), ("unavailable", 6))

prvtMplsTeMibEntityTable = MibTable((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 8, 1, 1), )
if mibBuilder.loadTexts: prvtMplsTeMibEntityTable.setStatus('current')
if mibBuilder.loadTexts: prvtMplsTeMibEntityTable.setDescription('The table of TE-MIB entities.')
prvtMplsTeMibEntityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 8, 1, 1, 1), ).setIndexNames((0, "PRVT-TEMIB-ENTITY-MIB", "prvtMplsTeMibEntityIndex"))
if mibBuilder.loadTexts: prvtMplsTeMibEntityEntry.setStatus('current')
if mibBuilder.loadTexts: prvtMplsTeMibEntityEntry.setDescription('Each entry represents a TE-MIB entity.')
prvtMplsTeMibEntityIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 8, 1, 1, 1, 1), PrvtTeMibEntityIndex())
if mibBuilder.loadTexts: prvtMplsTeMibEntityIndex.setStatus('current')
if mibBuilder.loadTexts: prvtMplsTeMibEntityIndex.setDescription('The index of this TE-MIB entity table entry.  This is the\n           HAF entity index passed on the entity create parameters.')
prvtMplsTeMibEntityAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 8, 1, 1, 1, 2), PrvtTeMibAdminStatus().clone('up')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtMplsTeMibEntityAdminStatus.setStatus('current')
if mibBuilder.loadTexts: prvtMplsTeMibEntityAdminStatus.setDescription("The desired administrative state of the TE-MIB entity.\n           When prvtMplsTeMibEntityRowStatus is 'active' and\n           prvtMplsTeMibEntityAdminStatus is 'up' the TE-MIB entity is active\n           and only these two fields can be modified.")
prvtMplsTeMibEntityOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 8, 1, 1, 1, 3), PrvtTeMibOperStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtMplsTeMibEntityOperStatus.setStatus('current')
if mibBuilder.loadTexts: prvtMplsTeMibEntityOperStatus.setDescription('The current operational state of the TE-MIB entity.')
prvtMplsTeMibEntityRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 8, 1, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtMplsTeMibEntityRowStatus.setStatus('current')
if mibBuilder.loadTexts: prvtMplsTeMibEntityRowStatus.setDescription("The row status for the TE-MIB entity table entry, used to create\n           and destroy TE-MIB entities.\n           When prvtMplsTeMibEntityRowStatus is 'active' and\n           prvtMplsTeMibEntityAdminStatus is 'up' the TE-MIB entity is active\n           and only these two fields can be modified.")
prvtMplsTeMibTunnelRetryInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 8, 1, 1, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(3000)).setUnits('milliseconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtMplsTeMibTunnelRetryInterval.setStatus('current')
if mibBuilder.loadTexts: prvtMplsTeMibTunnelRetryInterval.setDescription('The persistent tunnel retry interval.\n           This is the interval between the first failure of a persistent\n           tunnel and the first attempt to re-establish the tunnel.\n           A value of 0 indicates retrying is not supported.\n           A management agent may preempt a retry by resetting\n           mplsTunnelAdminStatus for the tunnel in question.')
prvtMplsTeMibTunnelRetryDecayRate = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 8, 1, 1, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100)).clone(50)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtMplsTeMibTunnelRetryDecayRate.setStatus('current')
if mibBuilder.loadTexts: prvtMplsTeMibTunnelRetryDecayRate.setDescription('The persistent tunnel decay rate.  This is a percentage.\n           Thus a value of 10 increases the retry interval by ten per cent\n           of the previous value.  A value of 0 indicates a constant\n           retry rate.')
prvtMplsTeMibTunnelRetryMax = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 8, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 255)).clone(10)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtMplsTeMibTunnelRetryMax.setStatus('current')
if mibBuilder.loadTexts: prvtMplsTeMibTunnelRetryMax.setDescription("The maximum number of retry attempts that will be made before a\n           persistent tunnel is deemed inoperable.  Once in this state,\n           a management agent should set mplsTunnelAdminStatus to 'up' to\n           attempt to reestablish the tunnel.\n           A value of -1 indicates infinite retry, so a persistent tunnel\n           will continue to be retried until it is successfully\n           established.")
prvtMplsTeMibTnnlBufPoolSize = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 8, 1, 1, 1, 8), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)).clone(8)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtMplsTeMibTnnlBufPoolSize.setStatus('current')
if mibBuilder.loadTexts: prvtMplsTeMibTnnlBufPoolSize.setDescription('The maximum number of buffers available for tunnel management\n           messages.  This is used to limit the number of tunnel management\n           messages to avoid buffer shortage conditions.')
prvtMplsTeMibLsrIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 8, 1, 1, 1, 9), PrvtLmgrIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtMplsTeMibLsrIndex.setStatus('current')
if mibBuilder.loadTexts: prvtMplsTeMibLsrIndex.setDescription('The index of the PRVT-LMGR product instance which this TE-MIB is to\n           join to as its LDB interface provider. If this value is not\n           specified, or the value of this object is 0, TE-MIB will use the\n           prvtMplsTeMibEntityIndex value as the Lsr index when joining on the\n           LDB interface.')
prvtMplsTeMibLdbStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 8, 1, 1, 1, 10), PrvtTeMibPartnerStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtMplsTeMibLdbStatus.setStatus('current')
if mibBuilder.loadTexts: prvtMplsTeMibLdbStatus.setDescription('Diagnostic Field providing information about the status\n         of the Label Database Interface user as seen by the\n\t TE-MIB entity.')
prvtMplsTeMibLraStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 8, 1, 1, 1, 11), PrvtLmgrPartnerStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtMplsTeMibLraStatus.setStatus('current')
if mibBuilder.loadTexts: prvtMplsTeMibLraStatus.setDescription('Diagnostic Field providing information about the status\n         of the LRAPI user as seen by the TE-MIB entity.')
prvtMplsTeMibLdiStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 8, 1, 1, 1, 12), PrvtTeMibPartnerStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtMplsTeMibLdiStatus.setStatus('current')
if mibBuilder.loadTexts: prvtMplsTeMibLdiStatus.setDescription('A diagnostic value which reports the state of the LDI\n         join.')
prvtMplsTeMibRsvpEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 8, 1, 1, 1, 13), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtMplsTeMibRsvpEnable.setStatus('current')
if mibBuilder.loadTexts: prvtMplsTeMibRsvpEnable.setDescription('A boolean indicating whether the PRVT-TE-MIB should expect\n         a join from PRVT-RSVP across the LRAPI.  This indicates\n         whether RSVP-TE LSP tunnels are supported or not.')
prvtMplsTeMibCrldpEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 8, 1, 1, 1, 14), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtMplsTeMibCrldpEnable.setStatus('current')
if mibBuilder.loadTexts: prvtMplsTeMibCrldpEnable.setDescription('A boolean indicating whether the PRVT-TE-MIB should join\n         to PRVT-CR-LDP or not across the LDI, and therefore support\n         CR-LDP LSP tunnels or not.')
prvtMplsTeMibCrldpIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 8, 1, 1, 1, 15), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtMplsTeMibCrldpIndex.setStatus('current')
if mibBuilder.loadTexts: prvtMplsTeMibCrldpIndex.setDescription('The index of the PRVT-MPLS product instance which this\n         TE-MIB is to join to as its LDI interface provider.  If\n         this value is not specified, or the value of this object\n         is 0, TE-MIB will use the prvtMplsTeMibEntityIndex value as\n         the CR-LDP product index when joining on the LDI\n         interface.')
prvtMplsTeMibUseRsvpResvConf = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 8, 1, 1, 1, 16), Bits().clone(namedValues=NamedValues(("useResvConfForUNI", 0), ("useResvConfForGMPLS", 1)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtMplsTeMibUseRsvpResvConf.setStatus('current')
if mibBuilder.loadTexts: prvtMplsTeMibUseRsvpResvConf.setDescription('Flags field indicating whether a RESV_CONFIRM object\n         should be included in RSVP Resv messages.  The possible\n         bit values are as follows.\n\n         - useResvConfForUNI: RESV_CONFIRM objects should be\n           inserted into all UNI Resv messages.\n         - useResvConfForGMPLS: RESV_CONFIRM objects should be\n           inserted into all standard GMPLS Resv messages.')
prvtMplsTeMibAllowGracefulDeletion = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 8, 1, 1, 1, 17), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtMplsTeMibAllowGracefulDeletion.setStatus('current')
if mibBuilder.loadTexts: prvtMplsTeMibAllowGracefulDeletion.setDescription('A boolean indicating whether the TE-MIB should allow\n         tunnels to be deleted using the graceful deletion\n         procedure.')
prvtMplsTeMibShowTransitTunnels = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 8, 1, 1, 1, 18), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtMplsTeMibShowTransitTunnels.setStatus('current')
if mibBuilder.loadTexts: prvtMplsTeMibShowTransitTunnels.setDescription('A flag to indicate whether RSVP should inform TE-MIB about\n          LSPs for which this node is transit.')
prvtMplsTeMibSupportCHopTable = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 8, 1, 1, 1, 19), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtMplsTeMibSupportCHopTable.setStatus('current')
if mibBuilder.loadTexts: prvtMplsTeMibSupportCHopTable.setDescription('A flag to indicate whether TE-MIB should support the\n          mplsTunnelCHopTable.')
prvtMplsTeMibNhrIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 8, 1, 1, 1, 20), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtMplsTeMibNhrIndex.setStatus('current')
if mibBuilder.loadTexts: prvtMplsTeMibNhrIndex.setDescription('The index of the PRVT-MPLS product instance which this\n            TE-MIB is to join to as its NHR interface provider.  If\n            this value is not specified, or the value of this object\n            is 0, TE-MIB will use the prvtMplsTeMibEntityIndex value as\n            the LSR index when joining on the NHR interface.')
prvtMplsTeMibNhrBufPoolSize = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 8, 1, 1, 1, 21), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)).clone(8)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtMplsTeMibNhrBufPoolSize.setStatus('current')
if mibBuilder.loadTexts: prvtMplsTeMibNhrBufPoolSize.setDescription('The maximum number of buffers available for Next Hop\n            Routing Interface messages.  This is used to limit the\n            number of tunnel management messages to avoid buffer\n            shortage conditions.')
prvtMplsTeMibNhrStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 8, 1, 1, 1, 22), PrvtTeMibPartnerStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtMplsTeMibNhrStatus.setStatus('current')
if mibBuilder.loadTexts: prvtMplsTeMibNhrStatus.setDescription('A diagnostic value which reports the state of the NHR\n        join.')
prvtMplsTeMibExtPrtSuppAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 8, 1, 1, 1, 23), PrvtTeMibAdminStatus().clone('down')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtMplsTeMibExtPrtSuppAdminStatus.setStatus('current')
if mibBuilder.loadTexts: prvtMplsTeMibExtPrtSuppAdminStatus.setDescription('The desired operational state of support for the extended\n         PROTECTION object defined in\n         draft-lang-ccamp-gmpls-recovery-e2e-signaling.')
prvtMplsTeMibRsvpIpv6AdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 8, 1, 1, 1, 24), PrvtTeMibAdminStatus().clone('down')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtMplsTeMibRsvpIpv6AdminStatus.setStatus('current')
if mibBuilder.loadTexts: prvtMplsTeMibRsvpIpv6AdminStatus.setDescription('Specifies whether the local node supports IPv6 LSPs.\n\n         Setting this to UP means that this node supports IPv6 LSPs\n         being set up to, from and through this node.\n\n         Setting this to DOWN means that IPv6 LSPs are NOT\n         supported by this node.  Existing IPv6 LSPs for which this\n         node is the ingress are torn down.\n\n         This field can be modified while TE-MIB is oper_status UP\n         or DOWN.\n\n         The value of this field MUST match the value of the\n         dcRsvpProductIpv6AdminStatus field in the\n         dcRsvpProductTable.')
prvtMplsTeMibRsvpIpv6OperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 8, 1, 1, 1, 25), PrvtTeMibOperStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtMplsTeMibRsvpIpv6OperStatus.setStatus('current')
if mibBuilder.loadTexts: prvtMplsTeMibRsvpIpv6OperStatus.setDescription('The current operational status for IPv6 support.  When\n         this is UP IPv6 LSPs can be set up from this node.  When\n         this is DOWN there will be no active IPv6 LSPs.')
prvtMplsTeMibDynFacilityBypass = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 8, 1, 1, 1, 26), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtMplsTeMibDynFacilityBypass.setStatus('current')
if mibBuilder.loadTexts: prvtMplsTeMibDynFacilityBypass.setDescription('This object gives the user ability to globally enable/disable \n         automatically creation of bypass tunnels for all LSPs. Bypass \n         tunnels will be created on FRR tunnel request automatically.\n         The default value is true. The creation of Dynamic bypass tunnels \n         is enabled')
prvtTeMibEntityConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 8, 2))
prvtTeMibEntityCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 8, 2, 1))
prvtTeMibEntityGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 8, 2, 2))
prvtTeMibEntityMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 8, 2, 1, 1)).setObjects(("PRVT-TEMIB-ENTITY-MIB", "mplsTeMibMandatoryGroup"), ("PRVT-TEMIB-ENTITY-MIB", "mplsTeMibOptionalGroup"), ("PRVT-TEMIB-ENTITY-MIB", "mplsTeMibCrldpGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    prvtTeMibEntityMibCompliance = prvtTeMibEntityMibCompliance.setStatus('current')
if mibBuilder.loadTexts: prvtTeMibEntityMibCompliance.setDescription('The compliance statement for the PRVT-TEMIB product.')
mplsTeMibMandatoryGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 8, 2, 2, 2)).setObjects(("PRVT-TEMIB-ENTITY-MIB", "prvtMplsTeMibEntityRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mplsTeMibMandatoryGroup = mplsTeMibMandatoryGroup.setStatus('current')
if mibBuilder.loadTexts: mplsTeMibMandatoryGroup.setDescription('Mandatory Objects.')
mplsTeMibOptionalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 8, 2, 2, 3)).setObjects(("PRVT-TEMIB-ENTITY-MIB", "prvtMplsTeMibEntityAdminStatus"), ("PRVT-TEMIB-ENTITY-MIB", "prvtMplsTeMibEntityOperStatus"), ("PRVT-TEMIB-ENTITY-MIB", "prvtMplsTeMibTunnelRetryInterval"), ("PRVT-TEMIB-ENTITY-MIB", "prvtMplsTeMibTunnelRetryDecayRate"), ("PRVT-TEMIB-ENTITY-MIB", "prvtMplsTeMibTunnelRetryMax"), ("PRVT-TEMIB-ENTITY-MIB", "prvtMplsTeMibTnnlBufPoolSize"), ("PRVT-TEMIB-ENTITY-MIB", "prvtMplsTeMibLsrIndex"), ("PRVT-TEMIB-ENTITY-MIB", "prvtMplsTeMibLdbStatus"), ("PRVT-TEMIB-ENTITY-MIB", "prvtMplsTeMibLraStatus"), ("PRVT-TEMIB-ENTITY-MIB", "prvtMplsTeMibRsvpEnable"), ("PRVT-TEMIB-ENTITY-MIB", "prvtMplsTeMibUseRsvpResvConf"), ("PRVT-TEMIB-ENTITY-MIB", "prvtMplsTeMibAllowGracefulDeletion"), ("PRVT-TEMIB-ENTITY-MIB", "prvtMplsTeMibShowTransitTunnels"), ("PRVT-TEMIB-ENTITY-MIB", "prvtMplsTeMibSupportCHopTable"), ("PRVT-TEMIB-ENTITY-MIB", "prvtMplsTeMibNhrIndex"), ("PRVT-TEMIB-ENTITY-MIB", "prvtMplsTeMibNhrBufPoolSize"), ("PRVT-TEMIB-ENTITY-MIB", "prvtMplsTeMibNhrStatus"), ("PRVT-TEMIB-ENTITY-MIB", "prvtMplsTeMibExtPrtSuppAdminStatus"), ("PRVT-TEMIB-ENTITY-MIB", "prvtMplsTeMibRsvpIpv6AdminStatus"), ("PRVT-TEMIB-ENTITY-MIB", "prvtMplsTeMibRsvpIpv6OperStatus"), ("PRVT-TEMIB-ENTITY-MIB", "prvtMplsTeMibDynFacilityBypass"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mplsTeMibOptionalGroup = mplsTeMibOptionalGroup.setStatus('current')
if mibBuilder.loadTexts: mplsTeMibOptionalGroup.setDescription('Optional Objects.')
mplsTeMibCrldpGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 8, 2, 2, 4)).setObjects(("PRVT-TEMIB-ENTITY-MIB", "prvtMplsTeMibLdiStatus"), ("PRVT-TEMIB-ENTITY-MIB", "prvtMplsTeMibCrldpEnable"), ("PRVT-TEMIB-ENTITY-MIB", "prvtMplsTeMibCrldpIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mplsTeMibCrldpGroup = mplsTeMibCrldpGroup.setStatus('current')
if mibBuilder.loadTexts: mplsTeMibCrldpGroup.setDescription('Group of objects relating to CR-LDP')
mibBuilder.exportSymbols("PRVT-TEMIB-ENTITY-MIB", prvtMplsTeMibEntityTable=prvtMplsTeMibEntityTable, prvtMplsTeMibTunnelRetryInterval=prvtMplsTeMibTunnelRetryInterval, PrvtTeMibPartnerStatus=PrvtTeMibPartnerStatus, PYSNMP_MODULE_ID=prvtTeMibEntityMib, prvtMplsTeMibEntityRowStatus=prvtMplsTeMibEntityRowStatus, prvtMplsTeMibLdbStatus=prvtMplsTeMibLdbStatus, mplsTeMibMandatoryGroup=mplsTeMibMandatoryGroup, PrvtTeMibAdminStatus=PrvtTeMibAdminStatus, prvtTeMibEntityGroups=prvtTeMibEntityGroups, prvtMplsTeMibNhrStatus=prvtMplsTeMibNhrStatus, PrvtTeMibOperStatus=PrvtTeMibOperStatus, prvtTeMibEntityMib=prvtTeMibEntityMib, prvtMplsTeMibTunnelRetryMax=prvtMplsTeMibTunnelRetryMax, prvtMplsTeMibTunnelRetryDecayRate=prvtMplsTeMibTunnelRetryDecayRate, prvtMplsTeMibEntityOperStatus=prvtMplsTeMibEntityOperStatus, prvtMplsTeMibCrldpIndex=prvtMplsTeMibCrldpIndex, prvtMplsTeMibExtPrtSuppAdminStatus=prvtMplsTeMibExtPrtSuppAdminStatus, prvtTeMibEntityObjects=prvtTeMibEntityObjects, mplsTeMibCrldpGroup=mplsTeMibCrldpGroup, prvtMplsTeMibNhrBufPoolSize=prvtMplsTeMibNhrBufPoolSize, prvtTeMibEntityConformance=prvtTeMibEntityConformance, prvtTeMibEntityMibCompliance=prvtTeMibEntityMibCompliance, prvtMplsTeMibNhrIndex=prvtMplsTeMibNhrIndex, prvtMplsTeMibEntityAdminStatus=prvtMplsTeMibEntityAdminStatus, prvtMplsTeMibShowTransitTunnels=prvtMplsTeMibShowTransitTunnels, prvtMplsTeMibTnnlBufPoolSize=prvtMplsTeMibTnnlBufPoolSize, prvtMplsTeMibRsvpIpv6OperStatus=prvtMplsTeMibRsvpIpv6OperStatus, prvtMplsTeMibRsvpIpv6AdminStatus=prvtMplsTeMibRsvpIpv6AdminStatus, prvtMplsTeMibCrldpEnable=prvtMplsTeMibCrldpEnable, prvtMplsTeMibLraStatus=prvtMplsTeMibLraStatus, prvtTeMibEntityCompliances=prvtTeMibEntityCompliances, mplsTeMibOptionalGroup=mplsTeMibOptionalGroup, prvtMplsTeMibUseRsvpResvConf=prvtMplsTeMibUseRsvpResvConf, prvtMplsTeMibSupportCHopTable=prvtMplsTeMibSupportCHopTable, prvtMplsTeMibDynFacilityBypass=prvtMplsTeMibDynFacilityBypass, prvtMplsTeMibLsrIndex=prvtMplsTeMibLsrIndex, prvtMplsTeMibLdiStatus=prvtMplsTeMibLdiStatus, prvtMplsTeMibEntityEntry=prvtMplsTeMibEntityEntry, prvtMplsTeMibEntityIndex=prvtMplsTeMibEntityIndex, PrvtTeMibEntityIndex=PrvtTeMibEntityIndex, prvtMplsTeMibRsvpEnable=prvtMplsTeMibRsvpEnable, prvtMplsTeMibAllowGracefulDeletion=prvtMplsTeMibAllowGracefulDeletion)
