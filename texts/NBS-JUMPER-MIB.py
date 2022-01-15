#
# PySNMP MIB module NBS-JUMPER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/mrv/NBS-JUMPER-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 18:13:01 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
nbs, = mibBuilder.importSymbols("NBS-MIB", "nbs")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, NotificationType, Integer32, Counter64, Bits, Counter32, IpAddress, TimeTicks, ModuleIdentity, MibIdentifier, iso, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "NotificationType", "Integer32", "Counter64", "Bits", "Counter32", "IpAddress", "TimeTicks", "ModuleIdentity", "MibIdentifier", "iso", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
nbsJumperMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 629, 210))
if mibBuilder.loadTexts: nbsJumperMib.setLastUpdated('201209260000Z')
if mibBuilder.loadTexts: nbsJumperMib.setOrganization('NBS')
if mibBuilder.loadTexts: nbsJumperMib.setContactInfo('For technical support, please contact your service channel')
if mibBuilder.loadTexts: nbsJumperMib.setDescription("MIB for reporting configuration of module's dipswitches and jumpers")
nbsJumperGrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 210, 1))
if mibBuilder.loadTexts: nbsJumperGrp.setStatus('current')
if mibBuilder.loadTexts: nbsJumperGrp.setDescription('Jumper and dipswitch information')
nbsJumperTableSize = MibScalar((1, 3, 6, 1, 4, 1, 629, 210, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsJumperTableSize.setStatus('current')
if mibBuilder.loadTexts: nbsJumperTableSize.setDescription('The number of entries in nbsJumperTable.')
nbsJumperTable = MibTable((1, 3, 6, 1, 4, 1, 629, 210, 1, 2), )
if mibBuilder.loadTexts: nbsJumperTable.setStatus('current')
if mibBuilder.loadTexts: nbsJumperTable.setDescription('All Jumper and dipswitch information')
nbsJumperEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 210, 1, 2, 1), ).setIndexNames((0, "NBS-JUMPER-MIB", "nbsJumperIfIndex"), (0, "NBS-JUMPER-MIB", "nbsJumperIndex"))
if mibBuilder.loadTexts: nbsJumperEntry.setStatus('current')
if mibBuilder.loadTexts: nbsJumperEntry.setDescription('Individual Jumper and dipswitch information')
nbsJumperIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 210, 1, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: nbsJumperIfIndex.setStatus('current')
if mibBuilder.loadTexts: nbsJumperIfIndex.setDescription('Unique identifier of this module in format css000 where\n           c is nbsCmmcChassisIndex and ss is nbsCmmcSlotIndex of\n           this board.')
nbsJumperIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 210, 1, 2, 1, 2), Integer32())
if mibBuilder.loadTexts: nbsJumperIndex.setStatus('current')
if mibBuilder.loadTexts: nbsJumperIndex.setDescription('Unique index of the jumper or dipswitch.  Index starts at 1.')
nbsJumperPosition = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 210, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notSupported", 1), ("off", 2), ("on", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsJumperPosition.setStatus('current')
if mibBuilder.loadTexts: nbsJumperPosition.setDescription('Actual/current position of this jumper or dipswitch.  For\n                 jumpers, on(3) indicates the pin pair is connected, off(2)\n                 means the jumper pair is unconnected.')
nbsJumperInterpret = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 210, 1, 2, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 50))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsJumperInterpret.setStatus('current')
if mibBuilder.loadTexts: nbsJumperInterpret.setDescription('Textual interpretation of the current\n                 nbsJumperPosition - what being on(3) or off(2)\n                 means for this feature.')
nbsJumperSilkScreen = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 210, 1, 2, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 10))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsJumperSilkScreen.setStatus('current')
if mibBuilder.loadTexts: nbsJumperSilkScreen.setDescription('The J number for this jumper, or SW block plus switch\n                 number for this dipswitch, as etched into the circuit\n                 board or dipswitch block.')
nbsJumperDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 210, 1, 2, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsJumperDescription.setStatus('current')
if mibBuilder.loadTexts: nbsJumperDescription.setDescription('Role of this jumper, feature it represents.')
mibBuilder.exportSymbols("NBS-JUMPER-MIB", PYSNMP_MODULE_ID=nbsJumperMib, nbsJumperTableSize=nbsJumperTableSize, nbsJumperEntry=nbsJumperEntry, nbsJumperDescription=nbsJumperDescription, nbsJumperTable=nbsJumperTable, nbsJumperIfIndex=nbsJumperIfIndex, nbsJumperSilkScreen=nbsJumperSilkScreen, nbsJumperPosition=nbsJumperPosition, nbsJumperInterpret=nbsJumperInterpret, nbsJumperGrp=nbsJumperGrp, nbsJumperIndex=nbsJumperIndex, nbsJumperMib=nbsJumperMib)
