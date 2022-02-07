#
# PySNMP MIB module OG-PRODUCTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/opengear/OG-PRODUCTS-MIB
# Produced by pysmi-1.1.8 at Mon Feb  7 16:17:33 2022
# On host fv-az42-619 platform Linux version 5.11.0-1028-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ogModules, ogProducts = mibBuilder.importSymbols("OG-SMI-MIB", "ogModules", "ogProducts")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, TimeTicks, Integer32, ObjectIdentity, Bits, Gauge32, ModuleIdentity, Counter32, Unsigned32, iso, MibIdentifier, Counter64, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "TimeTicks", "Integer32", "ObjectIdentity", "Bits", "Gauge32", "ModuleIdentity", "Counter32", "Unsigned32", "iso", "MibIdentifier", "Counter64", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ogProductsMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 25049, 11, 2))
ogProductsMib.setRevisions(('2018-06-15 00:00', '2016-06-27 00:00', '2016-02-10 00:00', '2015-06-02 00:00', '2013-08-11 00:00', '2011-08-15 01:23', '2010-04-15 11:27',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ogProductsMib.setRevisionsDescriptions(('Add Lighthouse 5 target to the MIB.', 'Add CM7196 target to the MIB.', 'Add CM71xx target to the MIB.', 'Add ACM700x target to the MIB.', 'Renamed from OPENGEAR-PRODUCTS-MIB to OG-PRODUCTS-MIB to\n\t\tfix naming discrepancy.', 'Add ACM550x target to the MIB.', 'Initial version.',))
if mibBuilder.loadTexts: ogProductsMib.setLastUpdated('201806150000Z')
if mibBuilder.loadTexts: ogProductsMib.setOrganization('Opengear Inc.')
if mibBuilder.loadTexts: ogProductsMib.setContactInfo('Opengear Inc.\n\t\t 630 West 9560 South,\n\t\t Sandy, UT 84070\n\t\t support@opengear.com')
if mibBuilder.loadTexts: ogProductsMib.setDescription('Opengear Product MIB')
ogCM4001 = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 1, 1))
ogCM4002 = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 1, 2))
ogCM4008 = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 1, 3))
ogCM41xx = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 1, 10))
ogCM71xx = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 1, 11))
ogCM7196 = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 1, 12))
ogSD4001 = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 1, 20))
ogSD4002 = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 1, 21))
ogSD4008 = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 1, 22))
ogSD4001DW = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 1, 23))
ogSD4002DX = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 1, 24))
ogCD = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 1, 30))
ogCMx86 = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 1, 31))
ogCMS61xx = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 1, 40))
ogLighthouse = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 1, 41))
ogLighthouse5 = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 1, 42))
ogIM4004 = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 1, 50))
ogIM42xx = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 1, 60))
ogIM72xx = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 1, 61))
ogKCS61xx = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 1, 70))
ogACM500x = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 1, 80))
ogACM550x = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 1, 81))
ogACM700x = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 1, 90))
ogACM70045 = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 1, 91))
mibBuilder.exportSymbols("OG-PRODUCTS-MIB", ogLighthouse5=ogLighthouse5, ogSD4002=ogSD4002, ogIM4004=ogIM4004, ogACM500x=ogACM500x, ogCM4002=ogCM4002, ogACM700x=ogACM700x, ogSD4001DW=ogSD4001DW, ogSD4008=ogSD4008, ogCM4008=ogCM4008, ogCM4001=ogCM4001, ogCM7196=ogCM7196, ogCD=ogCD, ogCMS61xx=ogCMS61xx, ogKCS61xx=ogKCS61xx, ogIM72xx=ogIM72xx, ogACM70045=ogACM70045, ogCM41xx=ogCM41xx, ogSD4001=ogSD4001, ogLighthouse=ogLighthouse, ogACM550x=ogACM550x, ogSD4002DX=ogSD4002DX, ogProductsMib=ogProductsMib, ogCM71xx=ogCM71xx, PYSNMP_MODULE_ID=ogProductsMib, ogCMx86=ogCMx86, ogIM42xx=ogIM42xx)
