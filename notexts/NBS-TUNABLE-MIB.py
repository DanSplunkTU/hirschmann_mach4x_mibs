#
# PySNMP MIB module NBS-TUNABLE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/mrv/NBS-TUNABLE-MIB
# Produced by pysmi-1.1.8 at Sun Jan 16 00:41:03 2022
# On host fv-az42-839 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
nbs, = mibBuilder.importSymbols("NBS-MIB", "nbs")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, ModuleIdentity, Unsigned32, TimeTicks, Counter64, IpAddress, Bits, Gauge32, Counter32, iso, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "ModuleIdentity", "Unsigned32", "TimeTicks", "Counter64", "IpAddress", "Bits", "Gauge32", "Counter32", "iso", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
nbsTunableMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 629, 203))
if mibBuilder.loadTexts: nbsTunableMib.setLastUpdated('201706280000Z')
if mibBuilder.loadTexts: nbsTunableMib.setOrganization('NBS')
nbsTunableGrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 203, 1))
if mibBuilder.loadTexts: nbsTunableGrp.setStatus('current')
nbsTunableChannelTableSize = MibScalar((1, 3, 6, 1, 4, 1, 629, 203, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsTunableChannelTableSize.setStatus('current')
nbsTunableChannelTable = MibTable((1, 3, 6, 1, 4, 1, 629, 203, 1, 2), )
if mibBuilder.loadTexts: nbsTunableChannelTable.setStatus('current')
nbsTunableChannelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 203, 1, 2, 1), ).setIndexNames((0, "NBS-TUNABLE-MIB", "nbsTunableChannelIfIndex"))
if mibBuilder.loadTexts: nbsTunableChannelEntry.setStatus('current')
nbsTunableChannelIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 203, 1, 2, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsTunableChannelIfIndex.setStatus('current')
nbsTunableChannelFreqStart = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 203, 1, 2, 1, 2), Integer32().clone(190100)).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsTunableChannelFreqStart.setStatus('current')
nbsTunableChannelFreqEnd = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 203, 1, 2, 1, 3), Integer32().clone(197200)).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsTunableChannelFreqEnd.setStatus('current')
nbsTunableChannelFreqStep = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 203, 1, 2, 1, 4), Integer32().clone(100)).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsTunableChannelFreqStep.setStatus('current')
nbsTunableChannelFreqExponent = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 203, 1, 2, 1, 5), Integer32().clone(9)).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsTunableChannelFreqExponent.setStatus('current')
nbsTunableChannelFreqAdmin = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 203, 1, 2, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsTunableChannelFreqAdmin.setStatus('current')
nbsTunableChannelFreqOper = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 203, 1, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsTunableChannelFreqOper.setStatus('current')
nbsTunableChannelFreqDefault = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 203, 1, 2, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsTunableChannelFreqDefault.setStatus('current')
mibBuilder.exportSymbols("NBS-TUNABLE-MIB", nbsTunableChannelTableSize=nbsTunableChannelTableSize, PYSNMP_MODULE_ID=nbsTunableMib, nbsTunableChannelFreqDefault=nbsTunableChannelFreqDefault, nbsTunableMib=nbsTunableMib, nbsTunableChannelIfIndex=nbsTunableChannelIfIndex, nbsTunableChannelFreqOper=nbsTunableChannelFreqOper, nbsTunableChannelFreqStart=nbsTunableChannelFreqStart, nbsTunableGrp=nbsTunableGrp, nbsTunableChannelFreqStep=nbsTunableChannelFreqStep, nbsTunableChannelFreqAdmin=nbsTunableChannelFreqAdmin, nbsTunableChannelTable=nbsTunableChannelTable, nbsTunableChannelFreqExponent=nbsTunableChannelFreqExponent, nbsTunableChannelEntry=nbsTunableChannelEntry, nbsTunableChannelFreqEnd=nbsTunableChannelFreqEnd)
