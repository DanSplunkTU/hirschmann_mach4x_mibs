#
# PySNMP MIB module Juniper-UNI-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/juniper/Juniper-UNI-SMI
# Produced by pysmi-1.1.3 at Sun Nov 28 20:27:42 2021
# On host fv-az77-612 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, enterprises, Integer32, NotificationType, MibIdentifier, IpAddress, Counter64, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ObjectIdentity, TimeTicks, Counter32, Gauge32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "enterprises", "Integer32", "NotificationType", "MibIdentifier", "IpAddress", "Counter64", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ObjectIdentity", "TimeTicks", "Counter32", "Gauge32", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
juniperUni = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874))
juniperUni.setRevisions(('2003-07-30 19:03', '2002-11-13 20:14', '2001-06-01 21:46', '2000-06-01 14:30', '2000-05-24 04:00', '1999-12-13 19:36', '1999-11-08 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: juniperUni.setRevisionsDescriptions(('Product re-branding: changed UMC to SDX.', 'Replaced Unisphere names with Juniper names.', 'Replaced OBJECT-IDENTITYs with OBJECT IDENTIFIERs.', 'Added usVoiceAdmin and usDataAdmin branchs.', 'Added node for UMC MIB', 'Added REFERENCE clauses to OBJECT-IDENTITY definitions.', 'The initial release of this management informaiton module.',))
if mibBuilder.loadTexts: juniperUni.setLastUpdated('200307301903Z')
if mibBuilder.loadTexts: juniperUni.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: juniperUni.setContactInfo('       Juniper Networks, Inc.\n        Postal: 10 Technology Park Drive\n                Westford, MA  01886-3146\n                USA\n        Tel:    +1 978 589 5800\n        E-mail: mib@Juniper.net')
if mibBuilder.loadTexts: juniperUni.setDescription('The SNMP Management Identifiers (SMI) for the Juniper Networks\n        enterprise.  This is the top-level registry for SNMP managed objects and\n        other SNMP related information modules under the Juniper Networks/\n        Unisphere SNMP management enterprise object identifier.')
juniProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 1))
juniperUniMibs = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 2))
if mibBuilder.loadTexts: juniperUniMibs.setStatus('current')
if mibBuilder.loadTexts: juniperUniMibs.setDescription('This is the root object identifier under which Juniper Networks/\n        Unisphere SNMP managed object (MIB) modules are defined.')
usVoiceMibs = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 1))
juniMibs = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2))
juniperUniExperiment = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 3))
if mibBuilder.loadTexts: juniperUniExperiment.setStatus('current')
if mibBuilder.loadTexts: juniperUniExperiment.setDescription('This object identifier roots experimental MIBs, which are defined as:\n\n         1) IETF work-in-process MIBs which have not been assigned a permanent\n            object identifier by the IANA.\n\n         2) Juniper work-in-process MIBs that have not achieved final production\n            quality or field experience.\n\n        NOTE: Support for MIBs under the juniperUniExperiment subtree is\n              temporary and changes to objects may occur without notice.')
usVoiceExperiment = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 3, 1))
juniExperiment = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 3, 2))
juniperUniAdmin = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4))
if mibBuilder.loadTexts: juniperUniAdmin.setStatus('current')
if mibBuilder.loadTexts: juniperUniAdmin.setDescription('This is reserved for administratively assigned object identifiers, i.e.\n        those not associated with MIB objects.  Examples include items such as\n        chipset or ASIC identifiers.')
usVoiceAdmin = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 4, 1))
juniAdmin = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 4, 2))
juniAgentCapability = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 5))
if mibBuilder.loadTexts: juniAgentCapability.setStatus('current')
if mibBuilder.loadTexts: juniAgentCapability.setDescription("This provides a root object identifier under which AGENT-CAPABILITIES\n        modules are assigned.  Each product's agent's capabilities definitions\n        appear in a collection of separate modules.")
usVoiceAgents = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 1))
juniAgents = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2))
juniNetMgmtProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 6))
if mibBuilder.loadTexts: juniNetMgmtProducts.setStatus('current')
if mibBuilder.loadTexts: juniNetMgmtProducts.setDescription("This provides a root object identifier for the definition of nodes\n        pertaining to Juniper Networks' network management products.  Examples\n        include:\n            SDX - Service Deployment System\n            NMC - Network Management Center\n            NMC-RX - E-series element manager ")
juniSdxMibs = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 6, 1))
mibBuilder.exportSymbols("Juniper-UNI-SMI", juniMibs=juniMibs, juniperUni=juniperUni, usVoiceMibs=usVoiceMibs, juniperUniExperiment=juniperUniExperiment, juniperUniMibs=juniperUniMibs, usVoiceAgents=usVoiceAgents, juniExperiment=juniExperiment, usVoiceExperiment=usVoiceExperiment, juniSdxMibs=juniSdxMibs, juniAgentCapability=juniAgentCapability, PYSNMP_MODULE_ID=juniperUni, juniperUniAdmin=juniperUniAdmin, juniAgents=juniAgents, juniAdmin=juniAdmin, usVoiceAdmin=usVoiceAdmin, juniNetMgmtProducts=juniNetMgmtProducts, juniProducts=juniProducts)
