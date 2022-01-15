#
# PySNMP MIB module AT-PRODUCT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/allied/AT-PRODUCT-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 17:51:17 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
alliedTelesis, = mibBuilder.importSymbols("AT-SMI-MIB", "alliedTelesis")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, NotificationType, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Counter64, Bits, Gauge32, ModuleIdentity, ObjectIdentity, TimeTicks, Counter32, MibIdentifier, iso = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "NotificationType", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Counter64", "Bits", "Gauge32", "ModuleIdentity", "ObjectIdentity", "TimeTicks", "Counter32", "MibIdentifier", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
products = ModuleIdentity((1, 3, 6, 1, 4, 1, 207, 1))
products.setRevisions(('2017-10-19 00:00', '2017-03-31 00:00', '2017-02-01 00:00', '2017-01-18 00:00', '2016-10-03 00:00', '2016-07-25 00:00', '2016-05-06 00:00', '2016-01-08 00:00', '2015-11-10 00:00', '2015-08-05 00:00', '2015-07-27 00:00', '2015-07-22 00:00', '2015-05-06 00:00', '2015-04-03 00:00', '2014-11-19 00:00', '2014-11-18 00:00', '2014-10-22 00:00', '2014-09-23 00:00', '2014-08-28 00:00', '2014-08-20 00:00', '2014-07-30 00:00', '2014-06-09 00:00', '2014-06-03 00:00', '2014-05-16 00:00', '2013-08-01 00:00', '2013-07-09 00:00', '2013-04-02 00:00', '2012-03-22 00:00', '2011-12-18 05:00', '2011-09-15 00:00', '2011-09-14 00:00', '2011-09-05 00:00', '2011-04-04 00:00', '2010-10-12 00:00', '2010-09-20 00:00', '2010-09-07 00:00', '2010-08-19 00:00', '2010-07-22 00:00', '2010-06-15 00:15', '2009-05-19 00:00', '2009-05-15 00:00', '2008-03-06 13:00', '2007-11-15 00:00', '2007-03-21 00:00', '2007-02-07 00:00', '2006-06-14 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: products.setRevisionsDescriptions(('Rename atx55018XSPQ to atx55018XSPQm.', "Remove '_' in the MIB object names to comply with ASN.1.\n                Remove '-' to comply with SMIv2 standard.\n                Some mib object names are slightly changed to make it more readable.", 'Added GS970 products.', 'Added GS970PS products.', 'Added x550 products.', 'Added AT-SBX81XLEM as standalone product.', 'Added AT-GS900M Next Generation.', 'Added AT-FS980M products.', 'Added new SwitchBlade x908G2/3 products', 'Added AT-XS900MX products.', 'Added SecureHUB products.', 'Add Virtual Appliance (VAA).', 'Added AT-AR2050V.', 'Change the product name from x230-10GPT to x350-10GPT.', 'Add IE300 product family.', 'Added AT-AR3050S and AT-AR4050S.', 'Renaming Ix510 to IE510 and moving to Industrial Switch subtree.', 'Added AT-GS924MX, AT-GS924MPX, AT-GS948MX and AT-GS948MPX.', 'Added x510L products.', 'Renaming IE500 Family to IE200.', 'Added x510-28GTX-R and x510-52GTX-R product.', 'Added x510DP-28GTX product.', 'Added x510_28GSX/DC and Ix510_28GSX products. Added IE500 Family.', 'Added dc2552xs product', 'Changed x950 to x930, added x230 and x310 products', 'Added x510DP and IX5 products.', 'Added x950 products.', 'Added x510 product.', 'Added at-SBx81CFC400 and at-SBx81CFC960 products.', 'Added AT-SBx8106 product.', 'Added AT-SBx8112 product.', 'Added systemOID 196, 197 and 198', 'Added Rapier 48x product', 'Add swhub tree and systemOID 181 and 182', 'Add Rapier24ib product', 'Generic syntax tidy up', 'Added bridgeRouter 81 at_AR560SRouter.', 'Renamed at_x600_24TsPoE_220W_PSU to at_x600_24TsPoEPlus to reflect usage.', 'MIB revision history dates in descriptions updated.', 'Added systemOID 93, 94, 95, 96, 97, 98, 99, 100 and 101', ' Added systemOID 91,92. ', ' Added systemOID 69,70,75,76,77. ', 'Changed systemOID 67 from AT-8824R to 8724SL-V2.', 'Added systemOID for x900-48FS.', 'Added systemOID for AT-8824R.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: products.setLastUpdated('201710190000Z')
if mibBuilder.loadTexts: products.setOrganization('Allied Telesis, Inc.')
if mibBuilder.loadTexts: products.setContactInfo('  http://www.alliedtelesis.com')
if mibBuilder.loadTexts: products.setDescription('This file defines the identities of Allied Telesis products.\n                OID products is the root OBJECT IDENTIFIER. Beneath it there are subtrees\n                bridgeRouter, routerSwitch and swhub, which are defined in AT-SMI-MIB.')
bridgeRouter = ObjectIdentity((1, 3, 6, 1, 4, 1, 207, 1, 1))
if mibBuilder.loadTexts: bridgeRouter.setStatus('current')
if mibBuilder.loadTexts: bridgeRouter.setDescription('subtree beneath which brige product MIB object ids are assigned.')
centreComAR300Router = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 1, 8))
centreComAR720Router = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 1, 11))
centreComAR300LRouter = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 1, 12))
centreComAR310Router = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 1, 13))
centreComAR300LURouter = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 1, 14))
centreComAR300URouter = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 1, 15))
centreComAR310URouter = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 1, 16))
centreComAR350Router = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 1, 17))
centreComAR370Router = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 1, 18))
centreComAR330Router = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 1, 19))
centreComAR395Router = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 1, 20))
centreComAR390Router = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 1, 21))
centreComAR370URouter = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 1, 22))
centreComAR740Router = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 1, 23))
centreComAR140SRouter = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 1, 24))
centreComAR140URouter = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 1, 25))
centreComAR320Router = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 1, 26))
centreComAR130SRouter = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 1, 27))
centreComAR130URouter = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 1, 28))
centreComAR160Router = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 1, 29))
atAR740RouterDC = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 1, 43))
centreComAR120Router = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 1, 44))
atAR410Router = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 1, 47))
atAR725Router = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 1, 48))
atAR745Router = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 1, 49))
atAR410v2Router = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 1, 50))
atAR410v3Router = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 1, 51))
atAR725RouterDC = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 1, 52))
atAR745RouterDC = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 1, 53))
atAR450Router = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 1, 54))
atAR450DualRouter = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 1, 55))
atAR440Router = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 1, 59))
atAR441Router = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 1, 60))
atAR442Router = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 1, 61))
atAR443Router = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 1, 62))
atAR444Router = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 1, 63))
atAR420Router = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 1, 64))
atAR415SRouter = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 1, 71))
atAR415SRouterDC = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 1, 72))
atAR550Router = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 1, 73))
atAR551Router = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 1, 74))
atAR552Router = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 1, 75))
atAR550SRouterDP = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 1, 76))
atAR570Router = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 1, 78))
atAR770Router = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 1, 79))
atAR750SRouterDP = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 1, 80))
atAR560SRouter = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 1, 81))
atAR3050SRouter = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 1, 82))
atAR4050SRouter = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 1, 85))
atAR2050VRouter = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 1, 88))
atAR2010VRouter = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 1, 89))
routerSwitch = ObjectIdentity((1, 3, 6, 1, 4, 1, 207, 1, 14))
if mibBuilder.loadTexts: routerSwitch.setStatus('current')
if mibBuilder.loadTexts: routerSwitch.setDescription('subtree beneath which router and switch product MIB object ids are assigned.')
atRapier24 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 1))
atRapier16fSC = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 2))
atRapier16fVF = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 3))
atRapier16fMT = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 4))
atRapier48 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 5))
atRapier8t8fSC = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 6))
atRapier8t8fSCi = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 7))
atRapier8t8fMT = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 8))
atRapier8t8fMTi = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 9))
atRapier8fSC = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 10))
atRapier8fSCi = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 11))
atRapier8fMT = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 12))
atRapier8fMTi = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 13))
atRapier16fMTi = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 14))
atRapierG6 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 15))
atRapierG6SX = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 16))
atRapierG6LX = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 17))
atRapierG6MT = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 18))
atRapier16fSCi = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 19))
atRapier24i = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 20))
atRapier48i = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 21))
atSwitchblade4AC = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 22))
atSwitchblade4DC = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 23))
atSwitchblade8AC = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 24))
atSwitchblade8DC = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 25))
at9816GF = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 26))
at9812TF = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 27))
at9816GB = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 28))
at9812T = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 29))
at8724XL = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 30))
at8748XL = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 31))
at8724XLDC = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 32))
at8748XLDC = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 33))
at9816GbDC = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 34))
at9812tDC = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 35))
at8824 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 36))
at8848 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 37))
at8824DC = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 38))
at8848DC = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 39))
at8624XL80 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 41))
at8724XL80 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 42))
at8748XL80 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 43))
at8948EX = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 44))
at8948i = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 45))
at8624T2M = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 46))
atRapier24iDcNEBS = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 47))
at8724XLDcNEBS = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 48))
at9924T = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 49))
at9924SP = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 50))
at9924T4SP = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 51))
at9924TEMC = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 53))
at8724MLB = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 55))
at8624POE = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 56))
at9924Ts = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 57))
at86482SP = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 58))
at9924Ti = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 59))
at9924SPi = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 60))
at9924Tsi = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 61))
at9924SPsi = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 62))
at8948iN = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 63))
at9924TsiN = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 64))
atRapier48w = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 65))
at8724SlV2 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 67))
x90048FS = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 68))
atSwitchBladex908 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 69))
atx90012XTS = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 70))
atRapier48wb = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 71))
atRapier48wAC = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 72))
atRapier48wbAC = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 73))
atx90024XT = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 75))
atx90024XS = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 76))
atx90024XtN = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 77))
atx60024Ts = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 80))
atx60024TsXP = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 81))
atx60048Ts = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 82))
atx60048TsXP = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 83))
atRapier24ibNEBS = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 84))
atRapier24ibDcNEBS = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 85))
atSBx8112 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 86))
atSBx81CFC400 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 87))
atSBx81CFC960 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 88))
atx60024TsPoE = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 91))
atx60024TsPoEPlus = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 92))
x61048TsXPOEPlus = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 93))
x61048TsPOEPlus = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 94))
x61024TsXPOEPlus = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 95))
x61024TsPOEPlus = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 96))
x61048TsX = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 97))
x61048Ts = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 98))
x61024TsX = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 99))
x61024Ts = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 100))
x61024SPX = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 101))
atRP48xDC = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 105))
atx51028GTX = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 109))
atx51028GPX = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 110))
atx51028GSX = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 111))
atx51052GTX = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 112))
atx51052GPX = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 113))
atSBx8106 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 114))
atx510DP52GTX = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 116))
atIX528GPX = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 117))
atx93028GTX = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 118))
atx93028GPX = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 119))
atx93028GSX = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 120))
atx93052GTX = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 121))
atx93052GPX = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 122))
atdc2552xs = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 123))
atx51028GSXDC = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 124))
atx510DP28GTX = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 126))
atx510L28GT = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 127))
atx510L52GT = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 128))
atx510L28GP = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 129))
atx510L52GP = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 130))
atx51028GTXR = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 131))
atx51052GTXR = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 132))
atSH51028GTX = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 133))
atSH51052GTX = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 134))
atSH51028GPX = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 135))
atSH51052GPX = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 136))
atsbx908g2 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 137))
atsbx908g3 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 138))
atx55018XTQ = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 139))
atx55018XSQ = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 140))
atx55018XSPQm = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 141))
atSBx81XLEM = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 14, 142))
swhub = ObjectIdentity((1, 3, 6, 1, 4, 1, 207, 1, 4))
if mibBuilder.loadTexts: swhub.setStatus('current')
if mibBuilder.loadTexts: swhub.setDescription('subtree beneath which Layer2 switch product MIB object ids are assigned.')
atx200GE52T = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 4, 181))
atx200GE28T = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 4, 182))
atx2109GT = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 4, 196))
atx21016GT = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 4, 197))
atx21024GT = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 4, 198))
atx31026FT = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 4, 216))
atx31050FT = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 4, 217))
atx31026FP = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 4, 218))
atx31050FP = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 4, 219))
atx31026GT = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 4, 220))
atx31050GT = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 4, 221))
atx31026GP = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 4, 222))
atx31050GP = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 4, 223))
atx23010GT = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 4, 224))
atx23018GT = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 4, 225))
atx23028GT = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 4, 226))
atx23052GT = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 4, 227))
atx23010GP = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 4, 228))
atx23018GP = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 4, 229))
atx23028GP = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 4, 230))
atx23052GP = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 4, 231))
atx35010GPT = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 4, 232))
atGS924MX = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 4, 253))
atGS924MPX = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 4, 254))
atGS948MX = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 4, 255))
atGS948MPX = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 4, 256))
atXS916MXT = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 4, 257))
atXS916MXS = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 4, 258))
atXS916MXP = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 4, 259))
atSH23010GP = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 4, 260))
atSH23018GP = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 4, 261))
atSH23028GP = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 4, 262))
atSH2109GT = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 4, 263))
atSH21016GT = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 4, 264))
atSH21024GT = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 4, 265))
atSH31026FT = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 4, 266))
atSH31050FT = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 4, 267))
atSH31026FP = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 4, 268))
atSH31050FP = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 4, 269))
atSH23010GT = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 4, 270))
atSH23018GT = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 4, 271))
atSH23028GT = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 4, 272))
atFS980M9 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 4, 274))
atFS980M9PS = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 4, 275))
atFS980M18 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 4, 276))
atFS980M18PS = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 4, 277))
atFS980M28 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 4, 278))
atFS980M28PS = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 4, 279))
atFS980M52 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 4, 280))
atFS980M52PS = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 4, 281))
atGS910M = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 4, 282))
atGS910MP = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 4, 283))
atGS918M = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 4, 284))
atGS918MP = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 4, 285))
atGS928M = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 4, 286))
atGS928MP = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 4, 287))
atGS952M = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 4, 288))
atGS952MP = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 4, 289))
atGS970M28PS = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 4, 312))
atGS970M18PS = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 4, 313))
atGS970M10PS = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 4, 314))
atGS970M28 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 4, 315))
atGS970M18 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 4, 316))
atGS970M10 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 4, 317))
industrialSwitch = ObjectIdentity((1, 3, 6, 1, 4, 1, 207, 1, 24))
if mibBuilder.loadTexts: industrialSwitch.setStatus('current')
if mibBuilder.loadTexts: industrialSwitch.setDescription('subtree beneath which industrial switch product MIB object ids are assigned.')
atIE2006GT = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 24, 1))
atIE2006GP = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 24, 2))
atIE2006GPW = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 24, 3))
atIE2006FT = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 24, 6))
atIE2006FP = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 24, 7))
atIE30012GT = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 24, 8))
atIE30012GP = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 24, 9))
atIE30012GS = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 24, 10))
atIE30020GST = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 24, 11))
atIE51028GSX = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 24, 12))
virtualApp = ObjectIdentity((1, 3, 6, 1, 4, 1, 207, 1, 26))
if mibBuilder.loadTexts: virtualApp.setStatus('current')
if mibBuilder.loadTexts: virtualApp.setDescription('subtree beneath which virtual appliance MIB object ids are assigned.')
atVAA = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 26, 1))
mibBuilder.exportSymbols("AT-PRODUCT-MIB", atx23052GP=atx23052GP, at8948iN=at8948iN, centreComAR120Router=centreComAR120Router, atx510DP28GTX=atx510DP28GTX, atIE30020GST=atIE30020GST, atAR443Router=atAR443Router, at8948i=at8948i, atRapier16fMTi=atRapier16fMTi, atRapier24ibDcNEBS=atRapier24ibDcNEBS, atSH23028GT=atSH23028GT, atRapier8fMTi=atRapier8fMTi, atXS916MXT=atXS916MXT, atGS918M=atGS918M, atAR3050SRouter=atAR3050SRouter, atAR550Router=atAR550Router, x61048TsXPOEPlus=x61048TsXPOEPlus, atGS918MP=atGS918MP, atGS970M28PS=atGS970M28PS, atGS970M28=atGS970M28, atFS980M9=atFS980M9, atx93052GTX=atx93052GTX, atx60024TsXP=atx60024TsXP, at8724XLDC=at8724XLDC, x61048TsX=x61048TsX, at8724XL=at8724XL, atRapier24=atRapier24, x90048FS=x90048FS, atFS980M9PS=atFS980M9PS, atSH31050FT=atSH31050FT, atx93028GPX=atx93028GPX, atx55018XSQ=atx55018XSQ, at8624XL80=at8624XL80, atx51052GPX=atx51052GPX, atx60024TsPoEPlus=atx60024TsPoEPlus, atx55018XTQ=atx55018XTQ, at9924SPsi=at9924SPsi, atx51028GPX=atx51028GPX, atSH31050FP=atSH31050FP, atIE30012GS=atIE30012GS, atx23018GT=atx23018GT, atSH51028GPX=atSH51028GPX, atGS948MX=atGS948MX, atFS980M28=atFS980M28, atSwitchblade4DC=atSwitchblade4DC, atx60048TsXP=atx60048TsXP, centreComAR350Router=centreComAR350Router, atSwitchblade8AC=atSwitchblade8AC, atSwitchBladex908=atSwitchBladex908, atIE2006GPW=atIE2006GPW, atx51052GTXR=atx51052GTXR, atGS910MP=atGS910MP, atx21016GT=atx21016GT, at9924TsiN=at9924TsiN, x61024Ts=x61024Ts, atRapier8fMT=atRapier8fMT, atRapier8t8fSCi=atRapier8t8fSCi, atIE51028GSX=atIE51028GSX, atAR415SRouter=atAR415SRouter, atx93052GPX=atx93052GPX, at8724XLDcNEBS=at8724XLDcNEBS, atx31026GT=atx31026GT, atSH23010GT=atSH23010GT, centreComAR300URouter=centreComAR300URouter, swhub=swhub, atRapier8fSCi=atRapier8fSCi, centreComAR130SRouter=centreComAR130SRouter, at9924SP=at9924SP, atSH51052GPX=atSH51052GPX, atx21024GT=atx21024GT, PYSNMP_MODULE_ID=products, atRapier48wAC=atRapier48wAC, centreComAR330Router=centreComAR330Router, atGS970M18=atGS970M18, atAR2010VRouter=atAR2010VRouter, atSH51052GTX=atSH51052GTX, atx31050FT=atx31050FT, at8848=at8848, at86482SP=at86482SP, atx31026FP=atx31026FP, centreComAR300Router=centreComAR300Router, atRapier48wb=atRapier48wb, atRapier24ibNEBS=atRapier24ibNEBS, atx510L52GP=atx510L52GP, atIE2006GP=atIE2006GP, atVAA=atVAA, atAR552Router=atAR552Router, at9924SPi=at9924SPi, atx93028GTX=atx93028GTX, atx51028GSXDC=atx51028GSXDC, atAR441Router=atAR441Router, atAR440Router=atAR440Router, atRapier8t8fSC=atRapier8t8fSC, at9816GB=at9816GB, atRapier16fSC=atRapier16fSC, at8748XL=at8748XL, at8824=at8824, atGS924MX=atGS924MX, atSH23028GP=atSH23028GP, atIX528GPX=atIX528GPX, atIE30012GP=atIE30012GP, at9924Ti=at9924Ti, at8624T2M=at8624T2M, atx51052GTX=atx51052GTX, centreComAR140URouter=centreComAR140URouter, atRapier16fVF=atRapier16fVF, at8724MLB=at8724MLB, atAR750SRouterDP=atAR750SRouterDP, at8724SlV2=at8724SlV2, atFS980M18PS=atFS980M18PS, atAR770Router=atAR770Router, atIE2006FP=atIE2006FP, atx60048Ts=atx60048Ts, x61048TsPOEPlus=x61048TsPOEPlus, bridgeRouter=bridgeRouter, atAR550SRouterDP=atAR550SRouterDP, centreComAR370URouter=centreComAR370URouter, atRapier48=atRapier48, at9812T=at9812T, atAR420Router=atAR420Router, atx60024Ts=atx60024Ts, atx23052GT=atx23052GT, atAR560SRouter=atAR560SRouter, atx23010GT=atx23010GT, centreComAR130URouter=centreComAR130URouter, centreComAR160Router=centreComAR160Router, atAR442Router=atAR442Router, atXS916MXS=atXS916MXS, at8848DC=at8848DC, x61024TsXPOEPlus=x61024TsXPOEPlus, atx31050FP=atx31050FP, atSBx8106=atSBx8106, atGS924MPX=atGS924MPX, atx200GE28T=atx200GE28T, atRapier48wbAC=atRapier48wbAC, atsbx908g2=atsbx908g2, atAR570Router=atAR570Router, atGS952MP=atGS952MP, atGS970M10=atGS970M10, atx23028GP=atx23028GP, atAR410v3Router=atAR410v3Router, atIE30012GT=atIE30012GT, atAR444Router=atAR444Router, at8824DC=at8824DC, x61024TsPOEPlus=x61024TsPOEPlus, atSH21016GT=atSH21016GT, centreComAR720Router=centreComAR720Router, atSH31026FT=atSH31026FT, atSH51028GTX=atSH51028GTX, atIE2006GT=atIE2006GT, atRapier24i=atRapier24i, atSH31026FP=atSH31026FP, atRapier16fMT=atRapier16fMT, at9812tDC=at9812tDC, atSwitchblade4AC=atSwitchblade4AC, atx93028GSX=atx93028GSX, at9924T4SP=at9924T4SP, atRapier8t8fMT=atRapier8t8fMT, at9924TEMC=at9924TEMC, atx90012XTS=atx90012XTS, centreComAR300LRouter=centreComAR300LRouter, atIE2006FT=atIE2006FT, atsbx908g3=atsbx908g3, atx60024TsPoE=atx60024TsPoE, atdc2552xs=atdc2552xs, atSH2109GT=atSH2109GT, centreComAR310Router=centreComAR310Router, atx510L28GT=atx510L28GT, virtualApp=virtualApp, atRapier8fSC=atRapier8fSC, atx510L28GP=atx510L28GP, atGS928MP=atGS928MP, atx23010GP=atx23010GP, at9816GbDC=at9816GbDC, atx2109GT=atx2109GT, atFS980M18=atFS980M18, atRapierG6=atRapierG6, atx23018GP=atx23018GP, atSBx81XLEM=atSBx81XLEM, atx31050GP=atx31050GP, atAR745RouterDC=atAR745RouterDC, atGS948MPX=atGS948MPX, atx55018XSPQm=atx55018XSPQm, atXS916MXP=atXS916MXP, atGS910M=atGS910M, at9924Ts=at9924Ts, atGS952M=atGS952M, atx35010GPT=atx35010GPT, at9816GF=at9816GF, atAR551Router=atAR551Router, atx510L52GT=atx510L52GT, atx31026FT=atx31026FT, atGS970M18PS=atGS970M18PS, atRapier16fSCi=atRapier16fSCi, at9812TF=at9812TF, atFS980M52PS=atFS980M52PS, centreComAR395Router=centreComAR395Router, at8624POE=at8624POE, atx23028GT=atx23028GT, atGS970M10PS=atGS970M10PS, atx51028GTX=atx51028GTX, atRP48xDC=atRP48xDC, at9924Tsi=at9924Tsi, atAR4050SRouter=atAR4050SRouter, atAR410v2Router=atAR410v2Router, at8948EX=at8948EX, centreComAR740Router=centreComAR740Router, atSH23018GT=atSH23018GT, industrialSwitch=industrialSwitch, atx510DP52GTX=atx510DP52GTX, atRapier8t8fMTi=atRapier8t8fMTi, x61048Ts=x61048Ts, atFS980M52=atFS980M52, at8748XLDC=at8748XLDC, centreComAR320Router=centreComAR320Router, atx200GE52T=atx200GE52T, centreComAR310URouter=centreComAR310URouter, atAR415SRouterDC=atAR415SRouterDC, centreComAR140SRouter=centreComAR140SRouter, atRapierG6SX=atRapierG6SX, x61024SPX=x61024SPX, atAR725RouterDC=atAR725RouterDC, atSBx81CFC960=atSBx81CFC960, atSBx81CFC400=atSBx81CFC400, atSH23010GP=atSH23010GP, at9924T=at9924T, atx31026GP=atx31026GP, atSH23018GP=atSH23018GP, atFS980M28PS=atFS980M28PS, centreComAR390Router=centreComAR390Router, routerSwitch=routerSwitch, x61024TsX=x61024TsX, atAR740RouterDC=atAR740RouterDC, products=products, atSwitchblade8DC=atSwitchblade8DC, atRapier48i=atRapier48i, atx31050GT=atx31050GT, atRapierG6MT=atRapierG6MT, atx90024XtN=atx90024XtN, atAR410Router=atAR410Router, atRapier24iDcNEBS=atRapier24iDcNEBS, at8724XL80=at8724XL80, atRapier48w=atRapier48w, at8748XL80=at8748XL80, atx90024XS=atx90024XS, centreComAR300LURouter=centreComAR300LURouter, centreComAR370Router=centreComAR370Router, atAR725Router=atAR725Router, atAR450Router=atAR450Router, atx90024XT=atx90024XT, atSBx8112=atSBx8112, atx51028GSX=atx51028GSX, atGS928M=atGS928M, atAR745Router=atAR745Router, atx51028GTXR=atx51028GTXR)
mibBuilder.exportSymbols("AT-PRODUCT-MIB", atAR450DualRouter=atAR450DualRouter, atSH21024GT=atSH21024GT, atAR2050VRouter=atAR2050VRouter, atRapierG6LX=atRapierG6LX)
