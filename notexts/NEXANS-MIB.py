#
# PySNMP MIB module NEXANS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/nexans/NEXANS-MIB
# Produced by pysmi-1.1.3 at Sun Nov 28 20:25:24 2021
# On host fv-az77-612 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, MibIdentifier, Counter64, Gauge32, enterprises, Counter32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, ModuleIdentity, Integer32, TimeTicks, Unsigned32, Bits, iso = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "MibIdentifier", "Counter64", "Gauge32", "enterprises", "Counter32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "ModuleIdentity", "Integer32", "TimeTicks", "Unsigned32", "Bits", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
nexansANS = MibIdentifier((1, 3, 6, 1, 4, 1, 266))
products = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1))
bmSwitch = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1, 3))
fiberSwitch100Bm = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1, 3, 1))
copperSwitch100Bm = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1, 3, 2))
fiberSwitch100BmADesk = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1, 3, 3))
copperSwitch100BmADesk = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1, 3, 4))
fiberSwitch100BmA = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1, 3, 5))
copperSwitch100BmA = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1, 3, 6))
fiberSwitch100BmPlus = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1, 3, 7))
copperSwitch100BmPlus = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1, 3, 8))
fiberSwitch100BmPlusDesk = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1, 3, 9))
copperSwitch100BmPlusDesk = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1, 3, 10))
dualSwitch100BmPlusDeskFibFib = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1, 3, 11))
dualSwitch100BmPlusDeskCopCop = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1, 3, 12))
dualSwitch100BmPlusDeskCopFib = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1, 3, 13))
fiberSwitch100BmPlusDeskVersA = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1, 3, 14))
copperSwitch100BmPlusDeskVersA = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1, 3, 15))
fiberSwitchM100Bm = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1, 3, 16))
copperSwitchM100Bm = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1, 3, 17))
fiberSwitch100BmPlusDeskVersC = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1, 3, 18))
copperSwitch100BmPlusDeskVersC = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1, 3, 19))
fiberSwitch1000BmPlus = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1, 3, 20))
dualSwitch1000BmPlusFibFib = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1, 3, 21))
dualSwitch1000BmPlusDeskFibFib = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1, 3, 22))
dualSwitch1000BmPlusCopFib = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1, 3, 23))
dualSwitch1000BmPlusCopCop = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1, 3, 24))
copperSwitch1000BmPlus = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1, 3, 25))
gigaSwitchG541Desk = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1, 3, 27))
gigaSwitchG542SfpDesk = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1, 3, 28))
iSwitch740CopCop = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1, 3, 30))
iSwitch741CopFib = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1, 3, 31))
iSwitch742FibFib = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1, 3, 32))
iSwitch1042FibFib = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1, 3, 33))
iSwitch1043 = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1, 3, 34))
iSwitch742SfpSfp = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1, 3, 35))
iSwitch1043Sfp3Vi = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1, 3, 36))
iGigaSwitch541 = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1, 3, 37))
iGigaSwitch542Sfp2Vi = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1, 3, 38))
iGigaSwitch1604 = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1, 3, 40))
iGigaSwitch1608 = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1, 3, 41))
iGigaSwitch1612 = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1, 3, 42))
gigaSwitchBmFib = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1, 3, 50))
gigaSwitchBmCop = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1, 3, 51))
gigaSwitchV2Fib = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1, 3, 52))
gigaSwitchV2CopFib = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1, 3, 53))
gigaSwitchV2CopCop = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1, 3, 54))
gigaSwitchV2SfpFib = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1, 3, 55))
gigaSwitchV2Cop = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1, 3, 56))
gigaSwitchV3FibTp = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1, 3, 60))
gigaSwitchV3SfpTp = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1, 3, 61))
gigaSwitchV3d2SfpTp = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1, 3, 62))
gigaSwitchV3d2SfpSfp = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1, 3, 63))
gigaSwitchV3d2Fib = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1, 3, 64))
fiberSwitch1000BmV3 = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1, 3, 66))
fiberSwitch100BmV3 = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1, 3, 67))
gigaSwitch641DeskSfpTp = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1, 3, 70))
gigaSwitch642DeskSfpSfp = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1, 3, 71))
mibBuilder.exportSymbols("NEXANS-MIB", copperSwitch100BmPlus=copperSwitch100BmPlus, iSwitch1042FibFib=iSwitch1042FibFib, copperSwitch1000BmPlus=copperSwitch1000BmPlus, dualSwitch100BmPlusDeskFibFib=dualSwitch100BmPlusDeskFibFib, bmSwitch=bmSwitch, gigaSwitchV2SfpFib=gigaSwitchV2SfpFib, iGigaSwitch542Sfp2Vi=iGigaSwitch542Sfp2Vi, gigaSwitch642DeskSfpSfp=gigaSwitch642DeskSfpSfp, gigaSwitchG542SfpDesk=gigaSwitchG542SfpDesk, fiberSwitchM100Bm=fiberSwitchM100Bm, nexansANS=nexansANS, copperSwitch100BmPlusDeskVersC=copperSwitch100BmPlusDeskVersC, copperSwitch100BmA=copperSwitch100BmA, gigaSwitchV2Cop=gigaSwitchV2Cop, fiberSwitch100BmADesk=fiberSwitch100BmADesk, gigaSwitchV2Fib=gigaSwitchV2Fib, gigaSwitch641DeskSfpTp=gigaSwitch641DeskSfpTp, copperSwitch100Bm=copperSwitch100Bm, copperSwitch100BmPlusDesk=copperSwitch100BmPlusDesk, products=products, fiberSwitch1000BmPlus=fiberSwitch1000BmPlus, dualSwitch1000BmPlusDeskFibFib=dualSwitch1000BmPlusDeskFibFib, gigaSwitchBmCop=gigaSwitchBmCop, iSwitch741CopFib=iSwitch741CopFib, fiberSwitch100Bm=fiberSwitch100Bm, gigaSwitchBmFib=gigaSwitchBmFib, gigaSwitchV2CopFib=gigaSwitchV2CopFib, gigaSwitchG541Desk=gigaSwitchG541Desk, copperSwitch100BmADesk=copperSwitch100BmADesk, dualSwitch1000BmPlusFibFib=dualSwitch1000BmPlusFibFib, iGigaSwitch1608=iGigaSwitch1608, dualSwitch1000BmPlusCopFib=dualSwitch1000BmPlusCopFib, copperSwitchM100Bm=copperSwitchM100Bm, iSwitch742FibFib=iSwitch742FibFib, fiberSwitch100BmPlus=fiberSwitch100BmPlus, fiberSwitch100BmPlusDeskVersC=fiberSwitch100BmPlusDeskVersC, fiberSwitch100BmPlusDesk=fiberSwitch100BmPlusDesk, iSwitch1043=iSwitch1043, iSwitch742SfpSfp=iSwitch742SfpSfp, fiberSwitch100BmV3=fiberSwitch100BmV3, gigaSwitchV3d2SfpTp=gigaSwitchV3d2SfpTp, dualSwitch100BmPlusDeskCopFib=dualSwitch100BmPlusDeskCopFib, gigaSwitchV2CopCop=gigaSwitchV2CopCop, gigaSwitchV3d2SfpSfp=gigaSwitchV3d2SfpSfp, dualSwitch1000BmPlusCopCop=dualSwitch1000BmPlusCopCop, iSwitch1043Sfp3Vi=iSwitch1043Sfp3Vi, dualSwitch100BmPlusDeskCopCop=dualSwitch100BmPlusDeskCopCop, iGigaSwitch1612=iGigaSwitch1612, copperSwitch100BmPlusDeskVersA=copperSwitch100BmPlusDeskVersA, gigaSwitchV3FibTp=gigaSwitchV3FibTp, gigaSwitchV3d2Fib=gigaSwitchV3d2Fib, iGigaSwitch1604=iGigaSwitch1604, gigaSwitchV3SfpTp=gigaSwitchV3SfpTp, iSwitch740CopCop=iSwitch740CopCop, fiberSwitch1000BmV3=fiberSwitch1000BmV3, fiberSwitch100BmA=fiberSwitch100BmA, fiberSwitch100BmPlusDeskVersA=fiberSwitch100BmPlusDeskVersA, iGigaSwitch541=iGigaSwitch541)
