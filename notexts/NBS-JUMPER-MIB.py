#
# PySNMP MIB module NBS-JUMPER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/mrv/NBS-JUMPER-MIB
# Produced by pysmi-1.1.3 at Sun Nov 28 20:09:52 2021
# On host fv-az77-612 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
nbs, = mibBuilder.importSymbols("NBS-MIB", "nbs")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, Counter64, ObjectIdentity, Integer32, Counter32, NotificationType, IpAddress, iso, ModuleIdentity, Unsigned32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter64", "ObjectIdentity", "Integer32", "Counter32", "NotificationType", "IpAddress", "iso", "ModuleIdentity", "Unsigned32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
nbsJumperMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 629, 210))
if mibBuilder.loadTexts: nbsJumperMib.setLastUpdated('201209260000Z')
if mibBuilder.loadTexts: nbsJumperMib.setOrganization('NBS')
nbsJumperGrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 210, 1))
if mibBuilder.loadTexts: nbsJumperGrp.setStatus('current')
nbsJumperTableSize = MibScalar((1, 3, 6, 1, 4, 1, 629, 210, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsJumperTableSize.setStatus('current')
nbsJumperTable = MibTable((1, 3, 6, 1, 4, 1, 629, 210, 1, 2), )
if mibBuilder.loadTexts: nbsJumperTable.setStatus('current')
nbsJumperEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 210, 1, 2, 1), ).setIndexNames((0, "NBS-JUMPER-MIB", "nbsJumperIfIndex"), (0, "NBS-JUMPER-MIB", "nbsJumperIndex"))
if mibBuilder.loadTexts: nbsJumperEntry.setStatus('current')
nbsJumperIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 210, 1, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: nbsJumperIfIndex.setStatus('current')
nbsJumperIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 210, 1, 2, 1, 2), Integer32())
if mibBuilder.loadTexts: nbsJumperIndex.setStatus('current')
nbsJumperPosition = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 210, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notSupported", 1), ("off", 2), ("on", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsJumperPosition.setStatus('current')
nbsJumperInterpret = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 210, 1, 2, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 50))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsJumperInterpret.setStatus('current')
nbsJumperSilkScreen = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 210, 1, 2, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 10))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsJumperSilkScreen.setStatus('current')
nbsJumperDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 210, 1, 2, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsJumperDescription.setStatus('current')
mibBuilder.exportSymbols("NBS-JUMPER-MIB", nbsJumperMib=nbsJumperMib, nbsJumperSilkScreen=nbsJumperSilkScreen, nbsJumperTable=nbsJumperTable, nbsJumperIfIndex=nbsJumperIfIndex, nbsJumperIndex=nbsJumperIndex, nbsJumperTableSize=nbsJumperTableSize, nbsJumperEntry=nbsJumperEntry, nbsJumperDescription=nbsJumperDescription, nbsJumperInterpret=nbsJumperInterpret, PYSNMP_MODULE_ID=nbsJumperMib, nbsJumperPosition=nbsJumperPosition, nbsJumperGrp=nbsJumperGrp)
