#
# PySNMP MIB module S5-ROOT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/nortel/S5-ROOT-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 18:14:58 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, ModuleIdentity, Counter32, Integer32, Bits, IpAddress, MibIdentifier, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, NotificationType, iso, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "ModuleIdentity", "Counter32", "Integer32", "Bits", "IpAddress", "MibIdentifier", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "NotificationType", "iso", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
series5000, = mibBuilder.importSymbols("SYNOPTICS-ROOT-MIB", "series5000")
s5RootMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 45, 1, 6, 0))
s5RootMib.setRevisions(('2004-07-20 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: s5RootMib.setRevisionsDescriptions(('Version 118:  Conversion to SMIv2',))
if mibBuilder.loadTexts: s5RootMib.setLastUpdated('200407200000Z')
if mibBuilder.loadTexts: s5RootMib.setOrganization('Nortel Networks')
if mibBuilder.loadTexts: s5RootMib.setContactInfo('Nortel Networks')
if mibBuilder.loadTexts: s5RootMib.setDescription("5000 Root MIB\n\n            Copyright 1993-2004 Nortel Networks, Inc.\n            All rights reserved.\n            This Nortel Networks SNMP Management Information Base Specification\n            (Specification) embodies Nortel Networks' confidential and\n            proprietary intellectual property. Nortel Networks retains all\n            title and ownership in the Specification, including any\n            revisions.\n\n            This Specification is supplied 'AS IS,' and Nortel Networks makes\n            no warranty, either express or implied, as to the use,\n            operation, condition, or performance of the Specification.")
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
mibBuilder.exportSymbols("S5-ROOT-MIB", bnLogMsg=bnLogMsg, s5ChaTrap=s5ChaTrap, s5Com=s5Com, atmTraps=atmTraps, s5RootMib=s5RootMib, s5reg=s5reg, s5AtmTop=s5AtmTop, s5EthTrap=s5EthTrap, s5Tok=s5Tok, s5ComTrap=s5ComTrap, remoteLoginTrap=remoteLoginTrap, s5EnTop=s5EnTop, s5Traps=s5Traps, s5Eth=s5Eth, s5IfExt=s5IfExt, s5FddTrap=s5FddTrap, s5TrTop=s5TrTop, s5EcellTrap=s5EcellTrap, stpChangeTrap=stpChangeTrap, PYSNMP_MODULE_ID=s5RootMib, s5Agent=s5Agent, s5Chassis=s5Chassis, s5Fddi=s5Fddi, s5EnMsTop=s5EnMsTop, s5FdTop=s5FdTop, s5Tcs=s5Tcs, s5TokTrap=s5TokTrap)
