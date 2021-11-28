#
# PySNMP MIB module JUNIPER-WX-GLOBAL-REG (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/juniper/JUNIPER-WX-MIB
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
jnxWxGlobalRegModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 8239, 1, 1, 1))
jnxWxGlobalRegModule.setRevisions(('2007-11-17 10:00', '2007-11-17 10:00', '2007-11-14 01:30', '2006-06-08 18:00', '2005-05-09 10:12', '2004-03-15 14:00', '2003-06-26 20:00', '2001-07-29 22:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: jnxWxGlobalRegModule.setRevisionsDescriptions(('\n\t\t\tAdd wxc1800, wxc2600, wxc3400 product OID', '\n\t\t\tChange ISM200 product identity to jnxIsm200Wxc', '\n\t\t\tAdd ISM200 product OID.', '\n\t\t\tUpdate contact and MIB with Juniper information\n\t\t\tAdd wxc590 and wx60 product OID.', '\n\t\t\tAdded wxc250 product OID.', '\n\t\t\tAdd wx100 product OID.', '\n\t\t\tAdd wx80 product OID.', '\n\t\t\tRev 1.0\n\t\t\tInitial version of MIB module JUNIPER-WX-GLOBAL-REG.',))
if mibBuilder.loadTexts: jnxWxGlobalRegModule.setLastUpdated('200107292200Z')
if mibBuilder.loadTexts: jnxWxGlobalRegModule.setOrganization('Juniper Networks, Inc')
if mibBuilder.loadTexts: jnxWxGlobalRegModule.setContactInfo('\n\t\t\t\t\tCustomer Support\n\t\t\t\t\tJuniper Networks, Inc.\n\t\t\t\t\t1194 North Mathilda Avenue\n\t\t\t\t\tSunnyvale, CA  94089\n\n\t\t\t\t\t+1 888-314-JTAC\n\t\t\t\t\tsupport@juniper.net')
if mibBuilder.loadTexts: jnxWxGlobalRegModule.setDescription("\n\t\t\tA MIB module containing top-level OID definitions\n\t\t\tfor various sub-trees for Juniper Networks' enterprise MIB modules.")
juniperWxRoot = ObjectIdentity((1, 3, 6, 1, 4, 1, 8239))
if mibBuilder.loadTexts: juniperWxRoot.setStatus('current')
if mibBuilder.loadTexts: juniperWxRoot.setDescription('\n\t\t\tThe root of the OID sub-tree assigned to Juniper Networks assigned by\n\t\t\tthe Internet Assigned Numbers Authority (IANA).')
jnxWxReg = ObjectIdentity((1, 3, 6, 1, 4, 1, 8239, 1))
if mibBuilder.loadTexts: jnxWxReg.setStatus('current')
if mibBuilder.loadTexts: jnxWxReg.setDescription('\n\t\t\tSub-tree for registrations - identification of modules and logical and\n\t\t\tphysical components.')
jnxWxModules = ObjectIdentity((1, 3, 6, 1, 4, 1, 8239, 1, 1))
if mibBuilder.loadTexts: jnxWxModules.setStatus('current')
if mibBuilder.loadTexts: jnxWxModules.setDescription('\n\t\t\tSub-tree for module registrations.')
jnxWxMibs = ObjectIdentity((1, 3, 6, 1, 4, 1, 8239, 2))
if mibBuilder.loadTexts: jnxWxMibs.setStatus('current')
if mibBuilder.loadTexts: jnxWxMibs.setDescription('\n\t\t\tSub-tree for all WX object and event definitions.')
jnxWxCaps = ObjectIdentity((1, 3, 6, 1, 4, 1, 8239, 3))
if mibBuilder.loadTexts: jnxWxCaps.setStatus('current')
if mibBuilder.loadTexts: jnxWxCaps.setDescription('\n\t\t\tSub-tree for agent profiles.')
jnxWxReqs = ObjectIdentity((1, 3, 6, 1, 4, 1, 8239, 4))
if mibBuilder.loadTexts: jnxWxReqs.setStatus('current')
if mibBuilder.loadTexts: jnxWxReqs.setDescription('\n\t\t\tSub-tree for management application requirements.')
jnxWxExpr = ObjectIdentity((1, 3, 6, 1, 4, 1, 8239, 5))
if mibBuilder.loadTexts: jnxWxExpr.setStatus('current')
if mibBuilder.loadTexts: jnxWxExpr.setDescription('\n\t\t\tSub-tree for experimental definitions.')
jnxWxCommonMib = ObjectIdentity((1, 3, 6, 1, 4, 1, 8239, 2, 1))
if mibBuilder.loadTexts: jnxWxCommonMib.setStatus('current')
if mibBuilder.loadTexts: jnxWxCommonMib.setDescription('\n\t\t\tSub-tree for common WX object and event definitions.\n\t\t\tThese would be implemented by all WX products.')
jnxWxSpecificMib = ObjectIdentity((1, 3, 6, 1, 4, 1, 8239, 2, 2))
if mibBuilder.loadTexts: jnxWxSpecificMib.setStatus('current')
if mibBuilder.loadTexts: jnxWxSpecificMib.setDescription('\n\t\t\tSub-tree for specific WX object and event definitions.')
jnxWxProduct = ObjectIdentity((1, 3, 6, 1, 4, 1, 8239, 1, 2))
if mibBuilder.loadTexts: jnxWxProduct.setStatus('current')
if mibBuilder.loadTexts: jnxWxProduct.setDescription('\n\t\t\tThe WAN Acceleration product family.')
jnxWxProductWx50 = ObjectIdentity((1, 3, 6, 1, 4, 1, 8239, 1, 2, 1))
if mibBuilder.loadTexts: jnxWxProductWx50.setStatus('current')
if mibBuilder.loadTexts: jnxWxProductWx50.setDescription('\n\t\t\t\tWAN Acceleration Model 50')
jnxWxProductWx55 = ObjectIdentity((1, 3, 6, 1, 4, 1, 8239, 1, 2, 2))
if mibBuilder.loadTexts: jnxWxProductWx55.setStatus('current')
if mibBuilder.loadTexts: jnxWxProductWx55.setDescription('\n\t\t\t\tWAN Acceleration Model 55')
jnxWxProductWx20 = ObjectIdentity((1, 3, 6, 1, 4, 1, 8239, 1, 2, 3))
if mibBuilder.loadTexts: jnxWxProductWx20.setStatus('current')
if mibBuilder.loadTexts: jnxWxProductWx20.setDescription('\n\t\t\t\tWAN Acceleration Model 20')
jnxWxProductWx80 = ObjectIdentity((1, 3, 6, 1, 4, 1, 8239, 1, 2, 4))
if mibBuilder.loadTexts: jnxWxProductWx80.setStatus('current')
if mibBuilder.loadTexts: jnxWxProductWx80.setDescription('\n\t\t\t\tWAN Acceleration Model 80')
jnxWxProductWx100 = ObjectIdentity((1, 3, 6, 1, 4, 1, 8239, 1, 2, 5))
if mibBuilder.loadTexts: jnxWxProductWx100.setStatus('current')
if mibBuilder.loadTexts: jnxWxProductWx100.setDescription('\n\t\t\t\tWAN Acceleration Model 100')
jnxWxProductWxc500 = ObjectIdentity((1, 3, 6, 1, 4, 1, 8239, 1, 2, 6))
if mibBuilder.loadTexts: jnxWxProductWxc500.setStatus('current')
if mibBuilder.loadTexts: jnxWxProductWxc500.setDescription('\n\t\t\t\tSequence Caching Model 500')
jnxWxProductWx15 = ObjectIdentity((1, 3, 6, 1, 4, 1, 8239, 1, 2, 7))
if mibBuilder.loadTexts: jnxWxProductWx15.setStatus('current')
if mibBuilder.loadTexts: jnxWxProductWx15.setDescription('\n\t\t\t\tWAN Acceleration Model 15')
jnxWxProductWxc250 = ObjectIdentity((1, 3, 6, 1, 4, 1, 8239, 1, 2, 8))
if mibBuilder.loadTexts: jnxWxProductWxc250.setStatus('current')
if mibBuilder.loadTexts: jnxWxProductWxc250.setDescription('\n\t\t\t\tSequence Caching Model 250')
jnxWxProductWx60 = ObjectIdentity((1, 3, 6, 1, 4, 1, 8239, 1, 2, 9))
if mibBuilder.loadTexts: jnxWxProductWx60.setStatus('current')
if mibBuilder.loadTexts: jnxWxProductWx60.setDescription('\n\t\t\t\tWAN Acceleration Model 60')
jnxWxProductWxc590 = ObjectIdentity((1, 3, 6, 1, 4, 1, 8239, 1, 2, 10))
if mibBuilder.loadTexts: jnxWxProductWxc590.setStatus('current')
if mibBuilder.loadTexts: jnxWxProductWxc590.setDescription('\n\t\t\t\tSequence Caching Model 590')
jnxWxProductIsm200Wxc = ObjectIdentity((1, 3, 6, 1, 4, 1, 8239, 1, 2, 11))
if mibBuilder.loadTexts: jnxWxProductIsm200Wxc.setStatus('current')
if mibBuilder.loadTexts: jnxWxProductIsm200Wxc.setDescription('\n\t\t\t\tWAN Acceleration Model ISM200')
jnxWxProductWxc1800 = ObjectIdentity((1, 3, 6, 1, 4, 1, 8239, 1, 2, 12))
if mibBuilder.loadTexts: jnxWxProductWxc1800.setStatus('current')
if mibBuilder.loadTexts: jnxWxProductWxc1800.setDescription('\n\t\t\t\tWAN Acceleration Model 1800')
jnxWxProductWxc2600 = ObjectIdentity((1, 3, 6, 1, 4, 1, 8239, 1, 2, 13))
if mibBuilder.loadTexts: jnxWxProductWxc2600.setStatus('current')
if mibBuilder.loadTexts: jnxWxProductWxc2600.setDescription('\n\t\t\t\tWAN Acceleration Model 2600')
jnxWxProductWxc3400 = ObjectIdentity((1, 3, 6, 1, 4, 1, 8239, 1, 2, 14))
if mibBuilder.loadTexts: jnxWxProductWxc3400.setStatus('current')
if mibBuilder.loadTexts: jnxWxProductWxc3400.setDescription('\n\t\t\t\tWAN Acceleration Model 3400')
mibBuilder.exportSymbols("JUNIPER-WX-GLOBAL-REG", juniperWxRoot=juniperWxRoot, jnxWxProductWx80=jnxWxProductWx80, jnxWxProductWx20=jnxWxProductWx20, jnxWxProductWxc2600=jnxWxProductWxc2600, jnxWxProductIsm200Wxc=jnxWxProductIsm200Wxc, jnxWxSpecificMib=jnxWxSpecificMib, jnxWxProductWx15=jnxWxProductWx15, jnxWxProductWxc250=jnxWxProductWxc250, jnxWxProductWxc3400=jnxWxProductWxc3400, PYSNMP_MODULE_ID=jnxWxGlobalRegModule, jnxWxReqs=jnxWxReqs, jnxWxProductWxc590=jnxWxProductWxc590, jnxWxProductWx100=jnxWxProductWx100, jnxWxMibs=jnxWxMibs, jnxWxCommonMib=jnxWxCommonMib, jnxWxGlobalRegModule=jnxWxGlobalRegModule, jnxWxProductWxc1800=jnxWxProductWxc1800, jnxWxProductWx50=jnxWxProductWx50, jnxWxCaps=jnxWxCaps, jnxWxExpr=jnxWxExpr, jnxWxProductWxc500=jnxWxProductWxc500, jnxWxProductWx60=jnxWxProductWx60, jnxWxReg=jnxWxReg, jnxWxModules=jnxWxModules, jnxWxProduct=jnxWxProduct, jnxWxProductWx55=jnxWxProductWx55)
