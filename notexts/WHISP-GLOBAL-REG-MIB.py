#
# PySNMP MIB module WHISP-GLOBAL-REG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cambium/WHISP-GLOBAL-REG-MIB
# Produced by pysmi-1.1.8 at Mon Feb  7 16:08:18 2022
# On host fv-az42-619 platform Linux version 5.11.0-1028-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, Gauge32, MibIdentifier, TimeTicks, IpAddress, iso, Bits, Counter64, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, ModuleIdentity, Counter32, enterprises, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Gauge32", "MibIdentifier", "TimeTicks", "IpAddress", "iso", "Bits", "Counter64", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "ModuleIdentity", "Counter32", "enterprises", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
whispGlobalRegModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 161, 19, 1, 1, 1))
if mibBuilder.loadTexts: whispGlobalRegModule.setLastUpdated('200304100000Z')
if mibBuilder.loadTexts: whispGlobalRegModule.setOrganization('Motorola')
mot = MibIdentifier((1, 3, 6, 1, 4, 1, 161))
whispRoot = MibIdentifier((1, 3, 6, 1, 4, 1, 161, 19))
whispReg = MibIdentifier((1, 3, 6, 1, 4, 1, 161, 19, 1))
whispGeneric = MibIdentifier((1, 3, 6, 1, 4, 1, 161, 19, 2))
whispProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 161, 19, 3))
whispAps = MibIdentifier((1, 3, 6, 1, 4, 1, 161, 19, 3, 1))
whispSm = MibIdentifier((1, 3, 6, 1, 4, 1, 161, 19, 3, 2))
whispBox = MibIdentifier((1, 3, 6, 1, 4, 1, 161, 19, 3, 3))
whispCMM = MibIdentifier((1, 3, 6, 1, 4, 1, 161, 19, 3, 4))
whispPlv = MibIdentifier((1, 3, 6, 1, 4, 1, 161, 19, 3, 5))
whispCMM4 = MibIdentifier((1, 3, 6, 1, 4, 1, 161, 19, 3, 6))
whispPlvModem = MibIdentifier((1, 3, 6, 1, 4, 1, 161, 19, 3, 7))
whispPlvGateway = MibIdentifier((1, 3, 6, 1, 4, 1, 161, 19, 3, 8))
whispPlvRepeater = MibIdentifier((1, 3, 6, 1, 4, 1, 161, 19, 3, 9))
whispPlvBridge = MibIdentifier((1, 3, 6, 1, 4, 1, 161, 19, 3, 10))
whispModules = MibIdentifier((1, 3, 6, 1, 4, 1, 161, 19, 1, 1))
canopySnmpAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 161, 19, 250))
ucos = MibIdentifier((1, 3, 6, 1, 4, 1, 161, 19, 250, 256))
prizmSnmpAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 161, 19, 1250))
prizm = MibIdentifier((1, 3, 6, 1, 4, 1, 161, 19, 1000))
mibBuilder.exportSymbols("WHISP-GLOBAL-REG-MIB", whispPlvBridge=whispPlvBridge, whispProducts=whispProducts, prizmSnmpAgent=prizmSnmpAgent, ucos=ucos, whispAps=whispAps, whispPlvModem=whispPlvModem, whispReg=whispReg, whispPlvRepeater=whispPlvRepeater, PYSNMP_MODULE_ID=whispGlobalRegModule, whispModules=whispModules, whispGlobalRegModule=whispGlobalRegModule, canopySnmpAgent=canopySnmpAgent, whispSm=whispSm, whispCMM4=whispCMM4, whispPlv=whispPlv, whispBox=whispBox, whispGeneric=whispGeneric, whispRoot=whispRoot, whispPlvGateway=whispPlvGateway, prizm=prizm, mot=mot, whispCMM=whispCMM)
