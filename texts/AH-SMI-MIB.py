#
# PySNMP MIB module AH-SMI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/aerohive/AH-SMI-MIB
# Produced by pysmi-1.1.8 at Mon Feb  7 16:07:01 2022
# On host fv-az42-619 platform Linux version 5.11.0-1028-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, ObjectIdentity, Counter32, ModuleIdentity, IpAddress, TimeTicks, enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Integer32, Counter64, Gauge32, iso, Unsigned32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "ObjectIdentity", "Counter32", "ModuleIdentity", "IpAddress", "TimeTicks", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Integer32", "Counter64", "Gauge32", "iso", "Unsigned32", "MibIdentifier")
DisplayString, MacAddress, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "TextualConvention")
aerohive = ModuleIdentity((1, 3, 6, 1, 4, 1, 26928))
if mibBuilder.loadTexts: aerohive.setLastUpdated('201608310000Z')
if mibBuilder.loadTexts: aerohive.setOrganization('Aerohive Networks, Inc')
if mibBuilder.loadTexts: aerohive.setContactInfo('info@aerohive.com\n                        1011 McCarthy Boulevard\n                        \n                        Milpitas, CA 95035')
if mibBuilder.loadTexts: aerohive.setDescription('This is the MIB module for object type definitions\n\t    that are used throughout the Aerohive Networks enterprise MIBs.')
ahProduct = MibIdentifier((1, 3, 6, 1, 4, 1, 26928, 1))
ahAP = MibIdentifier((1, 3, 6, 1, 4, 1, 26928, 1, 1))
ahAPCommon = MibIdentifier((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1))
ahAPTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1))
ahAPInterface = MibIdentifier((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2))
ahAPMRP = MibIdentifier((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 3))
ahAPIDP = MibIdentifier((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 4))
ahAPHiveAP020_ag = MibIdentifier((1, 3, 6, 1, 4, 1, 26928, 1, 1, 2)).setLabel("ahAPHiveAP020-ag")
ahAPHiveAP028_ag = MibIdentifier((1, 3, 6, 1, 4, 1, 26928, 1, 1, 3)).setLabel("ahAPHiveAP028-ag")
ahAPHiveAP320_n = MibIdentifier((1, 3, 6, 1, 4, 1, 26928, 1, 1, 4)).setLabel("ahAPHiveAP320-n")
ahAPHiveAP340_n = MibIdentifier((1, 3, 6, 1, 4, 1, 26928, 1, 1, 5)).setLabel("ahAPHiveAP340-n")
class AhString(TextualConvention, OctetString):
    description = 'A text string with 32 octets'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class AhNodeID(MacAddress):
    description = 'Mgmt MAC address in hex decimal notation'
    status = 'current'

class AhInterfaceType(TextualConvention, Integer32):
    description = 'Interface type - (PHYSICAL, VIRTUAL)'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("ahPHYSICAL", 0), ("ahVIRTURAL", 1))

class AhInterfaceMode(TextualConvention, Integer32):
    description = 'Interface role types'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("ahNotUsed", 0), ("ahAccess", 1), ("ahBackhaul", 2), ("ahBridge", 3))

class AhMACProtocol(TextualConvention, Integer32):
    description = 'Radio Mode'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("ah11a", 0), ("ah11b", 1), ("ah11g", 2), ("ah11na", 3), ("ah11ng", 4))

mibBuilder.exportSymbols("AH-SMI-MIB", ahAPTrap=ahAPTrap, ahAPHiveAP320_n=ahAPHiveAP320_n, AhInterfaceType=AhInterfaceType, ahProduct=ahProduct, ahAPInterface=ahAPInterface, AhNodeID=AhNodeID, AhMACProtocol=AhMACProtocol, ahAPCommon=ahAPCommon, ahAP=ahAP, AhInterfaceMode=AhInterfaceMode, PYSNMP_MODULE_ID=aerohive, aerohive=aerohive, ahAPIDP=ahAPIDP, AhString=AhString, ahAPMRP=ahAPMRP, ahAPHiveAP028_ag=ahAPHiveAP028_ag, ahAPHiveAP340_n=ahAPHiveAP340_n, ahAPHiveAP020_ag=ahAPHiveAP020_ag)
