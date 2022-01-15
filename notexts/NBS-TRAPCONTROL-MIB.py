#
# PySNMP MIB module NBS-TRAPCONTROL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/mrv/NBS-TRAPCONTROL-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 18:13:00 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
nbs, = mibBuilder.importSymbols("NBS-MIB", "nbs")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, iso, IpAddress, ObjectIdentity, TimeTicks, Counter32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Counter64, MibIdentifier, Gauge32, Bits, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "iso", "IpAddress", "ObjectIdentity", "TimeTicks", "Counter32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Counter64", "MibIdentifier", "Gauge32", "Bits", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
nbsTrapControlMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 629, 209))
if mibBuilder.loadTexts: nbsTrapControlMib.setLastUpdated('201209260000Z')
if mibBuilder.loadTexts: nbsTrapControlMib.setOrganization('NBS')
nbsTrapListGrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 209, 1))
if mibBuilder.loadTexts: nbsTrapListGrp.setStatus('current')
nbsTrapIfGrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 209, 2))
if mibBuilder.loadTexts: nbsTrapIfGrp.setStatus('current')
nbsTrapListTableSize = MibScalar((1, 3, 6, 1, 4, 1, 629, 209, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsTrapListTableSize.setStatus('current')
nbsTrapListTable = MibTable((1, 3, 6, 1, 4, 1, 629, 209, 1, 2), )
if mibBuilder.loadTexts: nbsTrapListTable.setStatus('current')
nbsTrapListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 209, 1, 2, 1), ).setIndexNames((0, "NBS-TRAPCONTROL-MIB", "nbsTrapListIndex"))
if mibBuilder.loadTexts: nbsTrapListEntry.setStatus('current')
nbsTrapListIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 209, 1, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: nbsTrapListIndex.setStatus('current')
nbsTrapListTrapMib = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 209, 1, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsTrapListTrapMib.setStatus('current')
nbsTrapListTrapName = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 209, 1, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 50))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsTrapListTrapName.setStatus('current')
nbsTrapListTrapDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 209, 1, 2, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsTrapListTrapDescription.setStatus('current')
nbsTrapListTrapOID = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 209, 1, 2, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsTrapListTrapOID.setStatus('current')
nbsTrapIfTableSize = MibScalar((1, 3, 6, 1, 4, 1, 629, 209, 2, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsTrapIfTableSize.setStatus('current')
nbsTrapIfTable = MibTable((1, 3, 6, 1, 4, 1, 629, 209, 2, 2), )
if mibBuilder.loadTexts: nbsTrapIfTable.setStatus('current')
nbsTrapIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 209, 2, 2, 1), ).setIndexNames((0, "NBS-TRAPCONTROL-MIB", "nbsTrapIfIndex"))
if mibBuilder.loadTexts: nbsTrapIfEntry.setStatus('current')
nbsTrapIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 209, 2, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: nbsTrapIfIndex.setStatus('current')
nbsTrapIfTrapsCaps = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 209, 2, 2, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsTrapIfTrapsCaps.setStatus('current')
nbsTrapIfTrapsSelect = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 209, 2, 2, 1, 3), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsTrapIfTrapsSelect.setStatus('current')
mibBuilder.exportSymbols("NBS-TRAPCONTROL-MIB", nbsTrapIfGrp=nbsTrapIfGrp, nbsTrapListTrapMib=nbsTrapListTrapMib, nbsTrapIfTable=nbsTrapIfTable, nbsTrapListGrp=nbsTrapListGrp, nbsTrapControlMib=nbsTrapControlMib, nbsTrapListTable=nbsTrapListTable, nbsTrapListIndex=nbsTrapListIndex, nbsTrapListTrapOID=nbsTrapListTrapOID, nbsTrapIfTableSize=nbsTrapIfTableSize, nbsTrapIfIndex=nbsTrapIfIndex, nbsTrapIfTrapsCaps=nbsTrapIfTrapsCaps, nbsTrapIfTrapsSelect=nbsTrapIfTrapsSelect, nbsTrapListTrapDescription=nbsTrapListTrapDescription, nbsTrapListTrapName=nbsTrapListTrapName, nbsTrapListEntry=nbsTrapListEntry, nbsTrapIfEntry=nbsTrapIfEntry, nbsTrapListTableSize=nbsTrapListTableSize, PYSNMP_MODULE_ID=nbsTrapControlMib)
