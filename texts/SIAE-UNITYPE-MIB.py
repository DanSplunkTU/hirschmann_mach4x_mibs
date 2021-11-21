#
# PySNMP MIB module SIAE-UNITYPE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/siae/SIAE-UNITYPE-MIB
# Produced by pysmi-1.1.3 at Sun Nov 21 00:48:51 2021
# On host fv-az39-63 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
siaeMib, = mibBuilder.importSymbols("SIAE-TREE-MIB", "siaeMib")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, MibIdentifier, iso, ModuleIdentity, TimeTicks, ObjectIdentity, NotificationType, Gauge32, Unsigned32, Bits, IpAddress, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "MibIdentifier", "iso", "ModuleIdentity", "TimeTicks", "ObjectIdentity", "NotificationType", "Gauge32", "Unsigned32", "Bits", "IpAddress", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
unitTypeMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 506))
unitTypeMib.setRevisions(('2016-10-14 00:00', '2016-07-19 00:00', '2016-04-05 00:00', '2015-03-04 00:00', '2014-12-01 00:00', '2014-03-19 00:00', '2014-02-07 00:00', '2013-04-16 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: unitTypeMib.setRevisionsDescriptions((' Added unitTypeALFOplus1(229),\n              unitTypeAGS20ARI2E(260), unitTypeAGS20ARI2ETDM2(261),\n              unitTypeAGS20ARI2ETDM3(262),\n              unitTypeAGS20ARI2EXG(263), unitTypeAGS20ARI2ETDM2XG(264),\n              unitTypeAGS20ARI2ETDM3XG(265).\n              Modified unitTypeALFO80HDx(280)\n            ', ' Added unitTypeALFO80HDx(270)\n            ', ' Added unitTypeAGS20ARI2XG(250), unitTypeAGS20ARI2TDM2XG(251),\n              unitTypeAGS20ARI2TDM3XG(252), unitTypeAGS20ARI4XG(253),\n              unitTypeAGS20ARI4TDM2XG(254) and unitTypeAGS20ARI4TDM3XG(255)\n            ', ' Added unitTypeAGS20ARI1DP(223) and unitTypeAGS20ARI1TDM2DP(224)\n              and unitTypeAGS20ARI1TDM3DP(225)\n            ', ' Added unitTypeAGS20ODU(231)\n            ', ' Added unitTypeAGS20CORE(222)\n            ', '- Removed types unitTypeCore, unitTypeAri1, unitTypeAri2 and\n               unitTypeDri2\n             - Added types unitTypeODU and unitTypeAGS20\n            ', 'Initial version 01.00.00\n            ',))
if mibBuilder.loadTexts: unitTypeMib.setLastUpdated('201607190000Z')
if mibBuilder.loadTexts: unitTypeMib.setOrganization('SIAE MICROELETTRONICA spa')
if mibBuilder.loadTexts: unitTypeMib.setContactInfo('SIAE MICROELETTONICA s.p.a.\n             Via Michelangelo Buonarroti, 21\n             20093 - Cologno Monzese\n             Milano - ITALY\n             Phone :  +39-02-27325-1\n             E-mail: help@siaemic.com\n            ')
if mibBuilder.loadTexts: unitTypeMib.setDescription('Types of SIAE equipment units.\n            ')
unitType = MibIdentifier((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3))
unitTypeUnequipped = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 1))
if mibBuilder.loadTexts: unitTypeUnequipped.setStatus('current')
if mibBuilder.loadTexts: unitTypeUnequipped.setDescription('Unequipped unit')
if mibBuilder.loadTexts: unitTypeUnequipped.setReference('None')
unitTypeODU = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 5))
if mibBuilder.loadTexts: unitTypeODU.setStatus('current')
if mibBuilder.loadTexts: unitTypeODU.setDescription('Out Door Unit')
if mibBuilder.loadTexts: unitTypeODU.setReference('None')
unitTypeALFO80HD = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 200))
if mibBuilder.loadTexts: unitTypeALFO80HD.setStatus('current')
if mibBuilder.loadTexts: unitTypeALFO80HD.setDescription('ALFO 80GHz HD')
if mibBuilder.loadTexts: unitTypeALFO80HD.setReference('None')
unitTypeALFO80HDelectrical = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 201))
if mibBuilder.loadTexts: unitTypeALFO80HDelectrical.setStatus('current')
if mibBuilder.loadTexts: unitTypeALFO80HDelectrical.setDescription('ALFO 80GHz HD (electrical ethernet inferface)')
if mibBuilder.loadTexts: unitTypeALFO80HDelectrical.setReference('None')
unitTypeALFO80HDelectricalOptical = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 202))
if mibBuilder.loadTexts: unitTypeALFO80HDelectricalOptical.setStatus('current')
if mibBuilder.loadTexts: unitTypeALFO80HDelectricalOptical.setDescription('ALFO 80GHz HD (electrical and optical ethernet inferface)')
if mibBuilder.loadTexts: unitTypeALFO80HDelectricalOptical.setReference('None')
unitTypeALFO80HDoptical = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 203))
if mibBuilder.loadTexts: unitTypeALFO80HDoptical.setStatus('current')
if mibBuilder.loadTexts: unitTypeALFO80HDoptical.setDescription('ALFO 80GHz HD (optical ethernet inferface)')
if mibBuilder.loadTexts: unitTypeALFO80HDoptical.setReference('None')
unitTypeAGS20ARI1 = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 210))
if mibBuilder.loadTexts: unitTypeAGS20ARI1.setStatus('current')
if mibBuilder.loadTexts: unitTypeAGS20ARI1.setDescription('AGS-20 ARI1')
if mibBuilder.loadTexts: unitTypeAGS20ARI1.setReference('None')
unitTypeAGS20ARI2 = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 211))
if mibBuilder.loadTexts: unitTypeAGS20ARI2.setStatus('current')
if mibBuilder.loadTexts: unitTypeAGS20ARI2.setDescription('AGS-20 ARI-2')
if mibBuilder.loadTexts: unitTypeAGS20ARI2.setReference('None')
unitTypeAGS20ARI4 = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 212))
if mibBuilder.loadTexts: unitTypeAGS20ARI4.setStatus('current')
if mibBuilder.loadTexts: unitTypeAGS20ARI4.setDescription('AGS-20 ARI-4')
if mibBuilder.loadTexts: unitTypeAGS20ARI4.setReference('None')
unitTypeAGS20DRI4 = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 213))
if mibBuilder.loadTexts: unitTypeAGS20DRI4.setStatus('current')
if mibBuilder.loadTexts: unitTypeAGS20DRI4.setDescription('AGS-20 DRI-4')
if mibBuilder.loadTexts: unitTypeAGS20DRI4.setReference('None')
unitTypeAGS20ARI1TDM2 = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 214))
if mibBuilder.loadTexts: unitTypeAGS20ARI1TDM2.setStatus('current')
if mibBuilder.loadTexts: unitTypeAGS20ARI1TDM2.setDescription('AGS-20 ARI-1 TDM-2')
if mibBuilder.loadTexts: unitTypeAGS20ARI1TDM2.setReference('None')
unitTypeAGS20ARI1TDM3 = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 215))
if mibBuilder.loadTexts: unitTypeAGS20ARI1TDM3.setStatus('current')
if mibBuilder.loadTexts: unitTypeAGS20ARI1TDM3.setDescription('AGS-20 ARI-1 TDM-3')
if mibBuilder.loadTexts: unitTypeAGS20ARI1TDM3.setReference('None')
unitTypeAGS20ARI2TDM2 = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 216))
if mibBuilder.loadTexts: unitTypeAGS20ARI2TDM2.setStatus('current')
if mibBuilder.loadTexts: unitTypeAGS20ARI2TDM2.setDescription('AGS-20 ARI-2 TDM-2')
if mibBuilder.loadTexts: unitTypeAGS20ARI2TDM2.setReference('None')
unitTypeAGS20ARI2TDM3 = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 217))
if mibBuilder.loadTexts: unitTypeAGS20ARI2TDM3.setStatus('current')
if mibBuilder.loadTexts: unitTypeAGS20ARI2TDM3.setDescription('AGS-20 ARI-2 TDM-3')
if mibBuilder.loadTexts: unitTypeAGS20ARI2TDM3.setReference('None')
unitTypeAGS20ARI4TDM2 = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 218))
if mibBuilder.loadTexts: unitTypeAGS20ARI4TDM2.setStatus('current')
if mibBuilder.loadTexts: unitTypeAGS20ARI4TDM2.setDescription('AGS-20 ARI-4 TDM-2')
if mibBuilder.loadTexts: unitTypeAGS20ARI4TDM2.setReference('None')
unitTypeAGS20ARI4TDM3 = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 219))
if mibBuilder.loadTexts: unitTypeAGS20ARI4TDM3.setStatus('current')
if mibBuilder.loadTexts: unitTypeAGS20ARI4TDM3.setDescription('AGS-20 ARI-4 TDM-3')
if mibBuilder.loadTexts: unitTypeAGS20ARI4TDM3.setReference('None')
unitTypeAGS20DRI4TDM2 = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 220))
if mibBuilder.loadTexts: unitTypeAGS20DRI4TDM2.setStatus('current')
if mibBuilder.loadTexts: unitTypeAGS20DRI4TDM2.setDescription('AGS-20 DRI-4 TDM-2')
if mibBuilder.loadTexts: unitTypeAGS20DRI4TDM2.setReference('None')
unitTypeAGS20DRI4TDM3 = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 221))
if mibBuilder.loadTexts: unitTypeAGS20DRI4TDM3.setStatus('current')
if mibBuilder.loadTexts: unitTypeAGS20DRI4TDM3.setDescription('AGS-20 DRI-4 TDM-3')
if mibBuilder.loadTexts: unitTypeAGS20DRI4TDM3.setReference('None')
unitTypeAGS20CORE = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 222))
if mibBuilder.loadTexts: unitTypeAGS20CORE.setStatus('current')
if mibBuilder.loadTexts: unitTypeAGS20CORE.setDescription('AGS-20 CORE')
if mibBuilder.loadTexts: unitTypeAGS20CORE.setReference('None')
unitTypeAGS20ARI1DP = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 223))
if mibBuilder.loadTexts: unitTypeAGS20ARI1DP.setStatus('current')
if mibBuilder.loadTexts: unitTypeAGS20ARI1DP.setDescription('AGS-20 ARI1 Dual Power')
if mibBuilder.loadTexts: unitTypeAGS20ARI1DP.setReference('None')
unitTypeAGS20ARI1TDM2DP = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 224))
if mibBuilder.loadTexts: unitTypeAGS20ARI1TDM2DP.setStatus('current')
if mibBuilder.loadTexts: unitTypeAGS20ARI1TDM2DP.setDescription('AGS-20 ARI-1 TDM-2 Dual Power')
if mibBuilder.loadTexts: unitTypeAGS20ARI1TDM2DP.setReference('None')
unitTypeAGS20ARI1TDM3DP = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 225))
if mibBuilder.loadTexts: unitTypeAGS20ARI1TDM3DP.setStatus('current')
if mibBuilder.loadTexts: unitTypeAGS20ARI1TDM3DP.setDescription('AGS-20 ARI-1 TDM-3 Dual Power')
if mibBuilder.loadTexts: unitTypeAGS20ARI1TDM3DP.setReference('None')
unitTypeALFOplus1 = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 229))
if mibBuilder.loadTexts: unitTypeALFOplus1.setStatus('current')
if mibBuilder.loadTexts: unitTypeALFOplus1.setDescription('ALFOplus1')
if mibBuilder.loadTexts: unitTypeALFOplus1.setReference('None')
unitTypeALFOplus2 = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 230))
if mibBuilder.loadTexts: unitTypeALFOplus2.setStatus('current')
if mibBuilder.loadTexts: unitTypeALFOplus2.setDescription('ALFOplus2')
if mibBuilder.loadTexts: unitTypeALFOplus2.setReference('None')
unitTypeAGS20ODU = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 231))
if mibBuilder.loadTexts: unitTypeAGS20ODU.setStatus('current')
if mibBuilder.loadTexts: unitTypeAGS20ODU.setDescription('AGS-20 ODU')
if mibBuilder.loadTexts: unitTypeAGS20ODU.setReference('None')
unitTypeAGS20ARI1TDM2LC = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 240))
if mibBuilder.loadTexts: unitTypeAGS20ARI1TDM2LC.setStatus('current')
if mibBuilder.loadTexts: unitTypeAGS20ARI1TDM2LC.setDescription('AGS-20 ARI-1 TDM-2 Low Cost')
if mibBuilder.loadTexts: unitTypeAGS20ARI1TDM2LC.setReference('None')
unitTypeAGS20ARI2XG = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 250))
if mibBuilder.loadTexts: unitTypeAGS20ARI2XG.setStatus('current')
if mibBuilder.loadTexts: unitTypeAGS20ARI2XG.setDescription('AGS-20 ARI-2 with 10G ports')
if mibBuilder.loadTexts: unitTypeAGS20ARI2XG.setReference('None')
unitTypeAGS20ARI2TDM2XG = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 251))
if mibBuilder.loadTexts: unitTypeAGS20ARI2TDM2XG.setStatus('current')
if mibBuilder.loadTexts: unitTypeAGS20ARI2TDM2XG.setDescription('AGS-20 ARI-2 TDM-2 with 10G ports')
if mibBuilder.loadTexts: unitTypeAGS20ARI2TDM2XG.setReference('None')
unitTypeAGS20ARI2TDM3XG = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 252))
if mibBuilder.loadTexts: unitTypeAGS20ARI2TDM3XG.setStatus('current')
if mibBuilder.loadTexts: unitTypeAGS20ARI2TDM3XG.setDescription('AGS-20 ARI-2 TDM-3 with 10G ports')
if mibBuilder.loadTexts: unitTypeAGS20ARI2TDM3XG.setReference('None')
unitTypeAGS20ARI4XG = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 253))
if mibBuilder.loadTexts: unitTypeAGS20ARI4XG.setStatus('current')
if mibBuilder.loadTexts: unitTypeAGS20ARI4XG.setDescription('AGS-20 ARI-4 with 10G ports')
if mibBuilder.loadTexts: unitTypeAGS20ARI4XG.setReference('None')
unitTypeAGS20ARI4TDM2XG = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 254))
if mibBuilder.loadTexts: unitTypeAGS20ARI4TDM2XG.setStatus('current')
if mibBuilder.loadTexts: unitTypeAGS20ARI4TDM2XG.setDescription('AGS-20 ARI-4 TDM-2 with 10G ports')
if mibBuilder.loadTexts: unitTypeAGS20ARI4TDM2XG.setReference('None')
unitTypeAGS20ARI4TDM3XG = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 255))
if mibBuilder.loadTexts: unitTypeAGS20ARI4TDM3XG.setStatus('current')
if mibBuilder.loadTexts: unitTypeAGS20ARI4TDM3XG.setDescription('AGS-20 ARI-4 TDM-3 with 10G ports')
if mibBuilder.loadTexts: unitTypeAGS20ARI4TDM3XG.setReference('None')
unitTypeAGS20ARI2E = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 260))
if mibBuilder.loadTexts: unitTypeAGS20ARI2E.setStatus('current')
if mibBuilder.loadTexts: unitTypeAGS20ARI2E.setDescription('AGS-20 ARI-2 Enhanced')
if mibBuilder.loadTexts: unitTypeAGS20ARI2E.setReference('None')
unitTypeAGS20ARI2ETDM2 = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 261))
if mibBuilder.loadTexts: unitTypeAGS20ARI2ETDM2.setStatus('current')
if mibBuilder.loadTexts: unitTypeAGS20ARI2ETDM2.setDescription('AGS-20 ARI-2 Enhanced TDM-2')
if mibBuilder.loadTexts: unitTypeAGS20ARI2ETDM2.setReference('None')
unitTypeAGS20ARI2ETDM3 = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 262))
if mibBuilder.loadTexts: unitTypeAGS20ARI2ETDM3.setStatus('current')
if mibBuilder.loadTexts: unitTypeAGS20ARI2ETDM3.setDescription('AGS-20 ARI-2 Enhanced TDM-3')
if mibBuilder.loadTexts: unitTypeAGS20ARI2ETDM3.setReference('None')
unitTypeAGS20ARI2EXG = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 263))
if mibBuilder.loadTexts: unitTypeAGS20ARI2EXG.setStatus('current')
if mibBuilder.loadTexts: unitTypeAGS20ARI2EXG.setDescription('AGS-20 ARI-2 Enhanced with 10G ports')
if mibBuilder.loadTexts: unitTypeAGS20ARI2EXG.setReference('None')
unitTypeAGS20ARI2ETDM2XG = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 264))
if mibBuilder.loadTexts: unitTypeAGS20ARI2ETDM2XG.setStatus('current')
if mibBuilder.loadTexts: unitTypeAGS20ARI2ETDM2XG.setDescription('AGS-20 ARI-2 Enhanced TDM-2 with 10G ports')
if mibBuilder.loadTexts: unitTypeAGS20ARI2ETDM2XG.setReference('None')
unitTypeAGS20ARI2ETDM3XG = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 265))
if mibBuilder.loadTexts: unitTypeAGS20ARI2ETDM3XG.setStatus('current')
if mibBuilder.loadTexts: unitTypeAGS20ARI2ETDM3XG.setDescription('AGS-20 ARI-2 Enhanced TDM-3 with 10G ports')
if mibBuilder.loadTexts: unitTypeAGS20ARI2ETDM3XG.setReference('None')
unitTypeALFO80HDx = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 280))
if mibBuilder.loadTexts: unitTypeALFO80HDx.setStatus('current')
if mibBuilder.loadTexts: unitTypeALFO80HDx.setDescription('ALFO 80GHz HD with 10G ports')
if mibBuilder.loadTexts: unitTypeALFO80HDx.setReference('None')
mibBuilder.exportSymbols("SIAE-UNITYPE-MIB", unitTypeALFOplus1=unitTypeALFOplus1, unitTypeAGS20DRI4=unitTypeAGS20DRI4, unitTypeAGS20ARI4XG=unitTypeAGS20ARI4XG, unitTypeAGS20ARI2EXG=unitTypeAGS20ARI2EXG, unitTypeMib=unitTypeMib, unitTypeAGS20ARI2E=unitTypeAGS20ARI2E, unitTypeAGS20DRI4TDM3=unitTypeAGS20DRI4TDM3, unitTypeAGS20ARI2ETDM3=unitTypeAGS20ARI2ETDM3, unitTypeAGS20ARI2TDM2=unitTypeAGS20ARI2TDM2, unitTypeALFO80HDelectrical=unitTypeALFO80HDelectrical, unitTypeAGS20ARI2ETDM2XG=unitTypeAGS20ARI2ETDM2XG, unitTypeALFO80HD=unitTypeALFO80HD, unitTypeAGS20DRI4TDM2=unitTypeAGS20DRI4TDM2, unitTypeAGS20ARI1TDM3=unitTypeAGS20ARI1TDM3, unitTypeAGS20ARI2ETDM2=unitTypeAGS20ARI2ETDM2, unitTypeAGS20ARI1TDM2DP=unitTypeAGS20ARI1TDM2DP, unitTypeAGS20ARI4TDM3=unitTypeAGS20ARI4TDM3, unitTypeAGS20CORE=unitTypeAGS20CORE, unitTypeAGS20ARI1TDM3DP=unitTypeAGS20ARI1TDM3DP, unitTypeAGS20ARI2TDM2XG=unitTypeAGS20ARI2TDM2XG, unitTypeALFOplus2=unitTypeALFOplus2, unitTypeALFO80HDx=unitTypeALFO80HDx, unitTypeAGS20ARI4TDM3XG=unitTypeAGS20ARI4TDM3XG, unitTypeAGS20ARI2ETDM3XG=unitTypeAGS20ARI2ETDM3XG, unitTypeAGS20ARI1TDM2LC=unitTypeAGS20ARI1TDM2LC, unitTypeAGS20ARI2=unitTypeAGS20ARI2, unitTypeAGS20ARI2TDM3=unitTypeAGS20ARI2TDM3, unitTypeALFO80HDelectricalOptical=unitTypeALFO80HDelectricalOptical, unitTypeAGS20ARI2TDM3XG=unitTypeAGS20ARI2TDM3XG, unitTypeODU=unitTypeODU, unitTypeALFO80HDoptical=unitTypeALFO80HDoptical, unitTypeAGS20ARI4=unitTypeAGS20ARI4, unitTypeAGS20ARI1DP=unitTypeAGS20ARI1DP, unitType=unitType, unitTypeAGS20ARI4TDM2XG=unitTypeAGS20ARI4TDM2XG, PYSNMP_MODULE_ID=unitTypeMib, unitTypeAGS20ODU=unitTypeAGS20ODU, unitTypeAGS20ARI4TDM2=unitTypeAGS20ARI4TDM2, unitTypeUnequipped=unitTypeUnequipped, unitTypeAGS20ARI1TDM2=unitTypeAGS20ARI1TDM2, unitTypeAGS20ARI2XG=unitTypeAGS20ARI2XG, unitTypeAGS20ARI1=unitTypeAGS20ARI1)
