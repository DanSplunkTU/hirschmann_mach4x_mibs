#
# PySNMP MIB module TAIT-COMMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/tait/TAIT-COMMON-MIB
# Produced by pysmi-1.1.8 at Sun Jan 16 00:44:38 2022
# On host fv-az42-839 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Counter32, TimeTicks, ObjectIdentity, Unsigned32, NotificationType, iso, ModuleIdentity, enterprises, Gauge32, IpAddress, Bits, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Counter32", "TimeTicks", "ObjectIdentity", "Unsigned32", "NotificationType", "iso", "ModuleIdentity", "enterprises", "Gauge32", "IpAddress", "Bits", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
taitCommonRegModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 3570, 1, 1, 1))
taitCommonRegModule.setRevisions(('2012-02-20 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: taitCommonRegModule.setRevisionsDescriptions(('Update with new identity.',))
if mibBuilder.loadTexts: taitCommonRegModule.setLastUpdated('201202201200Z')
if mibBuilder.loadTexts: taitCommonRegModule.setOrganization('www.taitradio.com')
if mibBuilder.loadTexts: taitCommonRegModule.setContactInfo('postal: Tait International Limited\n                   558 Wairakei Road\n                   PO Box 1645\n                   Christchurch\n                   New Zealand\n\n           phone:  +64 3358 3399\n           email:  support@taitradio.com')
if mibBuilder.loadTexts: taitCommonRegModule.setDescription('The Tait Communication registration module.')
tait = ObjectIdentity((1, 3, 6, 1, 4, 1, 3570))
if mibBuilder.loadTexts: tait.setStatus('current')
if mibBuilder.loadTexts: tait.setDescription('The root of the sub-tree for Tait Communications.')
taitRegistrations = ObjectIdentity((1, 3, 6, 1, 4, 1, 3570, 1))
if mibBuilder.loadTexts: taitRegistrations.setStatus('current')
if mibBuilder.loadTexts: taitRegistrations.setDescription('Sub-tree for registrations, which includes modules.')
taitModules = ObjectIdentity((1, 3, 6, 1, 4, 1, 3570, 1, 1))
if mibBuilder.loadTexts: taitModules.setStatus('current')
if mibBuilder.loadTexts: taitModules.setDescription('Sub-tree for module registrations. It contains the textual context files.')
taitGeneric = ObjectIdentity((1, 3, 6, 1, 4, 1, 3570, 2))
if mibBuilder.loadTexts: taitGeneric.setStatus('current')
if mibBuilder.loadTexts: taitGeneric.setDescription('Sub-tree for common objects and events for products.')
taitProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 3570, 3))
if mibBuilder.loadTexts: taitProducts.setStatus('current')
if mibBuilder.loadTexts: taitProducts.setDescription('Sub-tree for product-specific objects and events.')
mibBuilder.exportSymbols("TAIT-COMMON-MIB", PYSNMP_MODULE_ID=taitCommonRegModule, taitRegistrations=taitRegistrations, taitProducts=taitProducts, taitModules=taitModules, tait=tait, taitGeneric=taitGeneric, taitCommonRegModule=taitCommonRegModule)
