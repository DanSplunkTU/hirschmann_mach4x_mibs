#
# PySNMP MIB module STORMSHIELD-IPSEC-STATS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/stormshield/STORMSHIELD-IPSEC-STATS-MIB
# Produced by pysmi-1.1.8 at Sun Jan 16 00:44:33 2022
# On host fv-az42-839 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, TimeTicks, Integer32, Unsigned32, NotificationType, Counter64, MibIdentifier, Bits, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, iso, ObjectIdentity, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "Integer32", "Unsigned32", "NotificationType", "Counter64", "MibIdentifier", "Bits", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "iso", "ObjectIdentity", "Counter32")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
stormshieldMIB, = mibBuilder.importSymbols("STORMSHIELD-SMI-MIB", "stormshieldMIB")
snsIPSECStats = ModuleIdentity((1, 3, 6, 1, 4, 1, 11256, 1, 13))
snsIPSECStats.setRevisions(('2017-02-20 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: snsIPSECStats.setRevisionsDescriptions(('Initial',))
if mibBuilder.loadTexts: snsIPSECStats.setLastUpdated('201702200000Z')
if mibBuilder.loadTexts: snsIPSECStats.setOrganization('Stormshield')
if mibBuilder.loadTexts: snsIPSECStats.setContactInfo('Customer Support\n\n        22 rue du Gouverneur General Eboue\n        92130 Issy-les-Moulineaux\n        FRANCE\n\n        Tel: +33 (0)9 69 32 96 29\n        E-mail: support@stormshield.eu\n        http://www.stormshield.eu')
if mibBuilder.loadTexts: snsIPSECStats.setDescription('stormshield IPSEC Statistics')
snsIPSECStatsSPD = MibIdentifier((1, 3, 6, 1, 4, 1, 11256, 1, 13, 1))
snsIPSECStatsSAD = MibIdentifier((1, 3, 6, 1, 4, 1, 11256, 1, 13, 2))
snsIPSECStatsSPDIn = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 13, 1, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsIPSECStatsSPDIn.setStatus('current')
if mibBuilder.loadTexts: snsIPSECStatsSPDIn.setDescription('Number of incomming security policies')
snsIPSECStatsSPDOut = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 13, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsIPSECStatsSPDOut.setStatus('current')
if mibBuilder.loadTexts: snsIPSECStatsSPDOut.setDescription('Number of outgoing security policies')
snsIPSECStatsSADLarval = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 13, 2, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsIPSECStatsSADLarval.setStatus('current')
if mibBuilder.loadTexts: snsIPSECStatsSADLarval.setDescription('Number of security associations in establishment')
snsIPSECStatsSADMature = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 13, 2, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsIPSECStatsSADMature.setStatus('current')
if mibBuilder.loadTexts: snsIPSECStatsSADMature.setDescription('Number established security associations')
snsIPSECStatsSADDying = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 13, 2, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsIPSECStatsSADDying.setStatus('current')
if mibBuilder.loadTexts: snsIPSECStatsSADDying.setDescription('Number of security associations in end of life')
snsIPSECStatsSADDead = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 13, 2, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsIPSECStatsSADDead.setStatus('current')
if mibBuilder.loadTexts: snsIPSECStatsSADDead.setDescription('Number of dead security associations')
mibBuilder.exportSymbols("STORMSHIELD-IPSEC-STATS-MIB", snsIPSECStatsSADLarval=snsIPSECStatsSADLarval, snsIPSECStatsSAD=snsIPSECStatsSAD, snsIPSECStatsSADMature=snsIPSECStatsSADMature, snsIPSECStatsSADDying=snsIPSECStatsSADDying, snsIPSECStatsSPDOut=snsIPSECStatsSPDOut, snsIPSECStatsSPD=snsIPSECStatsSPD, snsIPSECStats=snsIPSECStats, PYSNMP_MODULE_ID=snsIPSECStats, snsIPSECStatsSPDIn=snsIPSECStatsSPDIn, snsIPSECStatsSADDead=snsIPSECStatsSADDead)
