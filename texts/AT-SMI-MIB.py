#
# PySNMP MIB module AT-SMI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/allied/AT-SMI-MIB
# Produced by pysmi-1.1.8 at Mon Feb  7 16:07:19 2022
# On host fv-az42-619 platform Linux version 5.11.0-1028-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, TimeTicks, Counter32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ModuleIdentity, Unsigned32, IpAddress, iso, ObjectIdentity, NotificationType, Bits, Counter64, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "TimeTicks", "Counter32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ModuleIdentity", "Unsigned32", "IpAddress", "iso", "ObjectIdentity", "NotificationType", "Bits", "Counter64", "enterprises")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
alliedTelesis = ModuleIdentity((1, 3, 6, 1, 4, 1, 207))
alliedTelesis.setRevisions(('2014-09-30 00:00', '2010-06-15 00:15', '2008-02-28 00:00', '2006-06-14 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: alliedTelesis.setRevisionsDescriptions(('Merged object IDs from ATKK-WLAN-SMI-MIB for Wireless Products.', 'MIB revision history dates in descriptions updated.', 'Standardized the file head.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: alliedTelesis.setLastUpdated('201409300000Z')
if mibBuilder.loadTexts: alliedTelesis.setOrganization('Allied Telesis, Inc.')
if mibBuilder.loadTexts: alliedTelesis.setContactInfo('  http://www.alliedtelesis.com')
if mibBuilder.loadTexts: alliedTelesis.setDescription('The Structure of Management Information for Allied Telesis enterprise.')
class DisplayStringUnsized(TextualConvention, OctetString):
    reference = 'DisplayString'
    description = 'Represents textual information taken from the NVT ASCII\n                character set. It is a variation of DisplayString which\n                is defined in RFC 2579.'
    status = 'current'
    displayHint = '255a'

products = ObjectIdentity((1, 3, 6, 1, 4, 1, 207, 1))
if mibBuilder.loadTexts: products.setStatus('current')
if mibBuilder.loadTexts: products.setDescription('products is the root OBJECT IDENTIFIER. Beneath it there are subtree\n                bridgeRouter and routerSwitch, which are is defined in AT-PRODUCTS-MIB.')
wirelesslan = ObjectIdentity((1, 3, 6, 1, 4, 1, 207, 1, 13))
if mibBuilder.loadTexts: wirelesslan.setStatus('current')
if mibBuilder.loadTexts: wirelesslan.setDescription('subtree beneath which wireless lan product MIB object ids are assigned.')
mibObject = ObjectIdentity((1, 3, 6, 1, 4, 1, 207, 8))
if mibBuilder.loadTexts: mibObject.setStatus('current')
if mibBuilder.loadTexts: mibObject.setDescription('mibObject is the root OBJECT IDENTIFIER from which brouterMib and\n                wirelessLanmMIB are built.')
brouterMib = ObjectIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4))
if mibBuilder.loadTexts: brouterMib.setStatus('current')
if mibBuilder.loadTexts: brouterMib.setDescription('subtree beneath which atRouter object ids are assigned.')
wirelessLanmMIB = ObjectIdentity((1, 3, 6, 1, 4, 1, 207, 8, 42))
if mibBuilder.loadTexts: wirelessLanmMIB.setStatus('current')
if mibBuilder.loadTexts: wirelessLanmMIB.setDescription('subtree beneath which object ids for wlanAccess and uwc are assigned.')
atUWC = ObjectIdentity((1, 3, 6, 1, 4, 1, 207, 8, 42, 8))
if mibBuilder.loadTexts: atUWC.setStatus('current')
if mibBuilder.loadTexts: atUWC.setDescription('subtree beneath which wlanSwitch object ids are assigned.')
atRouter = ObjectIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4))
if mibBuilder.loadTexts: atRouter.setStatus('current')
if mibBuilder.loadTexts: atRouter.setDescription('subtree beneath which various groups of object id are assigned.')
objects = ObjectIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1))
if mibBuilder.loadTexts: objects.setStatus('current')
if mibBuilder.loadTexts: objects.setDescription('subtree beneath which object ids for boards and chips are assigned.')
traps = ObjectIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 2))
if mibBuilder.loadTexts: traps.setStatus('current')
if mibBuilder.loadTexts: traps.setDescription('subtree beneath which un-sorted trap ids are assigned.')
sysinfo = ObjectIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3))
if mibBuilder.loadTexts: sysinfo.setStatus('current')
if mibBuilder.loadTexts: sysinfo.setDescription('subtree beneath which system inforamtion ids are assigned.')
modules = ObjectIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4))
if mibBuilder.loadTexts: modules.setStatus('current')
if mibBuilder.loadTexts: modules.setDescription('subtree beneath which software module ids are assigned.')
arInterfaces = ObjectIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 5))
if mibBuilder.loadTexts: arInterfaces.setStatus('current')
if mibBuilder.loadTexts: arInterfaces.setDescription('subtree beneath which interface ids are assigned.')
protocols = ObjectIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 6))
if mibBuilder.loadTexts: protocols.setStatus('current')
if mibBuilder.loadTexts: protocols.setDescription('subtree beneath which protocol ids are assigned.')
atAgents = ObjectIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 7))
if mibBuilder.loadTexts: atAgents.setStatus('current')
if mibBuilder.loadTexts: atAgents.setDescription('subtree beneath which variation from standards defined.')
mibBuilder.exportSymbols("AT-SMI-MIB", protocols=protocols, objects=objects, alliedTelesis=alliedTelesis, brouterMib=brouterMib, arInterfaces=arInterfaces, wirelesslan=wirelesslan, traps=traps, atUWC=atUWC, products=products, DisplayStringUnsized=DisplayStringUnsized, modules=modules, atAgents=atAgents, atRouter=atRouter, sysinfo=sysinfo, wirelessLanmMIB=wirelessLanmMIB, mibObject=mibObject, PYSNMP_MODULE_ID=alliedTelesis)
