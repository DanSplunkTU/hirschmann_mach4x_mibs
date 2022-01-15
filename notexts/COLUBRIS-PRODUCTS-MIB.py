#
# PySNMP MIB module COLUBRIS-PRODUCTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/hpmsm/COLUBRIS-PRODUCTS-MIB.my
# Produced by pysmi-1.1.8 at Sat Jan 15 18:07:38 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
colubrisProducts, colubrisModules = mibBuilder.importSymbols("COLUBRIS-SMI", "colubrisProducts", "colubrisModules")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, Bits, Counter32, Unsigned32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, iso, MibIdentifier, TimeTicks, Gauge32, Counter64, NotificationType, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Bits", "Counter32", "Unsigned32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "iso", "MibIdentifier", "TimeTicks", "Gauge32", "Counter64", "NotificationType", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
colubrisProductsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 8744, 4, 2))
if mibBuilder.loadTexts: colubrisProductsMIB.setLastUpdated('200709060000Z')
if mibBuilder.loadTexts: colubrisProductsMIB.setOrganization('Colubris Networks, Inc.')
colubrisCN1000 = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 1))
colubrisCN1000HEREUARE = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 2))
colubrisCN1050 = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 3))
colubrisCN1054 = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 4))
colubrisCN3000 = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 5))
colubrisCN100HEREUARE = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 6))
colubrisCN100TRAVELNET = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 7))
colubrisCN300 = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 8))
colubrisCN1150 = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 9))
colubrisCN3100 = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 10))
colubrisCN1000LIGHT = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 11))
colubrisCN3500 = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 12))
colubrisCN310 = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 13))
colubrisCN1500 = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 14))
colubrisCN1550 = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 15))
colubrisCN3200 = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 16))
colubrisCN1200 = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 17))
colubrisCN1250 = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 18))
colubrisCN320SE = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 19))
colubrisCN320 = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 20))
colubrisCN1220 = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 21))
colubrisCN200 = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 22))
colubrisCN3300 = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 23))
colubrisCN330 = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 24))
colubrisMSC5200 = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 25))
colubrisWCB200 = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 26))
colubrisMSC5500 = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 27))
colubrisMAP625 = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 28))
colubrisMAP630 = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 29))
colubrisMAP330SENSOR = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 32))
colubris1300 = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 33))
colubris1500 = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 34))
colubrisMSC5100 = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 35))
colubrisMSM410 = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 41))
mibBuilder.exportSymbols("COLUBRIS-PRODUCTS-MIB", colubrisCN3300=colubrisCN3300, colubris1300=colubris1300, colubrisCN3200=colubrisCN3200, colubrisCN1050=colubrisCN1050, colubrisCN3000=colubrisCN3000, colubrisMAP330SENSOR=colubrisMAP330SENSOR, colubrisCN330=colubrisCN330, colubrisMSC5500=colubrisMSC5500, colubrisCN1054=colubrisCN1054, colubrisCN1550=colubrisCN1550, colubrisCN320SE=colubrisCN320SE, colubrisWCB200=colubrisWCB200, colubrisMSC5100=colubrisMSC5100, colubrisCN200=colubrisCN200, colubrisMSM410=colubrisMSM410, colubrisMSC5200=colubrisMSC5200, colubrisCN1150=colubrisCN1150, colubrisCN100TRAVELNET=colubrisCN100TRAVELNET, colubrisMAP625=colubrisMAP625, colubrisCN3100=colubrisCN3100, colubrisCN1250=colubrisCN1250, colubrisCN320=colubrisCN320, colubrisCN300=colubrisCN300, colubrisProductsMIB=colubrisProductsMIB, colubris1500=colubris1500, colubrisCN100HEREUARE=colubrisCN100HEREUARE, colubrisCN3500=colubrisCN3500, PYSNMP_MODULE_ID=colubrisProductsMIB, colubrisMAP630=colubrisMAP630, colubrisCN1000=colubrisCN1000, colubrisCN310=colubrisCN310, colubrisCN1200=colubrisCN1200, colubrisCN1000LIGHT=colubrisCN1000LIGHT, colubrisCN1000HEREUARE=colubrisCN1000HEREUARE, colubrisCN1220=colubrisCN1220, colubrisCN1500=colubrisCN1500)
