#
# PySNMP MIB module S5-ROOT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/nortel/S5-ROOT-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 18:14:51 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, TimeTicks, MibIdentifier, Gauge32, ObjectIdentity, Counter64, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Integer32, NotificationType, Counter32, ModuleIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "TimeTicks", "MibIdentifier", "Gauge32", "ObjectIdentity", "Counter64", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Integer32", "NotificationType", "Counter32", "ModuleIdentity", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
series5000, = mibBuilder.importSymbols("SYNOPTICS-ROOT-MIB", "series5000")
s5RootMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 45, 1, 6, 0))
s5RootMib.setRevisions(('2004-07-20 00:00',))
if mibBuilder.loadTexts: s5RootMib.setLastUpdated('200407200000Z')
if mibBuilder.loadTexts: s5RootMib.setOrganization('Nortel Networks')
s5reg = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 1, 6, 1))
s5Traps = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 1, 6, 2))
s5EthTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 1, 6, 2, 1))
s5TokTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 1, 6, 2, 2))
s5FddTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 1, 6, 2, 3))
s5ChaTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 1, 6, 2, 4))
s5ComTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 1, 6, 2, 5))
s5EcellTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 1, 6, 2, 6))
atmTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 1, 6, 2, 7))
remoteLoginTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 1, 6, 2, 8))
stpChangeTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 1, 6, 2, 9))
s5Chassis = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 1, 6, 3))
s5Agent = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 1, 6, 4))
s5Com = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 1, 6, 5))
s5Eth = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 1, 6, 6))
s5Tok = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 1, 6, 7))
s5Fddi = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 1, 6, 8))
s5EnTop = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 1, 6, 9))
s5TrTop = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 1, 6, 10))
s5FdTop = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 1, 6, 11))
s5EnMsTop = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 1, 6, 13))
s5AtmTop = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 1, 6, 14))
s5IfExt = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 1, 6, 15))
bnLogMsg = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 1, 6, 16))
s5Tcs = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 1, 6, 17))
mibBuilder.exportSymbols("S5-ROOT-MIB", bnLogMsg=bnLogMsg, s5EcellTrap=s5EcellTrap, s5ChaTrap=s5ChaTrap, s5reg=s5reg, s5TokTrap=s5TokTrap, remoteLoginTrap=remoteLoginTrap, s5FdTop=s5FdTop, s5ComTrap=s5ComTrap, s5Com=s5Com, s5Traps=s5Traps, stpChangeTrap=stpChangeTrap, s5Tok=s5Tok, s5EnTop=s5EnTop, s5Eth=s5Eth, s5EnMsTop=s5EnMsTop, s5EthTrap=s5EthTrap, s5Tcs=s5Tcs, s5RootMib=s5RootMib, s5Fddi=s5Fddi, atmTraps=atmTraps, PYSNMP_MODULE_ID=s5RootMib, s5AtmTop=s5AtmTop, s5FddTrap=s5FddTrap, s5IfExt=s5IfExt, s5Agent=s5Agent, s5TrTop=s5TrTop, s5Chassis=s5Chassis)
