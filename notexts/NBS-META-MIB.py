#
# PySNMP MIB module NBS-META-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/mrv/NBS-META-MIB
# Produced by pysmi-1.1.3 at Sun Nov 21 00:26:48 2021
# On host fv-az39-63 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
nbs, = mibBuilder.importSymbols("NBS-MIB", "nbs")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Counter32, ModuleIdentity, TimeTicks, NotificationType, MibIdentifier, Gauge32, Counter64, Bits, iso, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Counter32", "ModuleIdentity", "TimeTicks", "NotificationType", "MibIdentifier", "Gauge32", "Counter64", "Bits", "iso", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
nbsMetaMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 629, 205))
if mibBuilder.loadTexts: nbsMetaMib.setLastUpdated('201209260000Z')
if mibBuilder.loadTexts: nbsMetaMib.setOrganization('NBS')
nbsMetaMibGrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 205, 1))
if mibBuilder.loadTexts: nbsMetaMibGrp.setStatus('current')
nbsMetaMibFeatureTableSize = MibScalar((1, 3, 6, 1, 4, 1, 629, 205, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsMetaMibFeatureTableSize.setStatus('current')
nbsMetaMibFeatureTable = MibTable((1, 3, 6, 1, 4, 1, 629, 205, 1, 2), )
if mibBuilder.loadTexts: nbsMetaMibFeatureTable.setStatus('current')
nbsMetaMibFeatureEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 205, 1, 2, 1), ).setIndexNames((0, "NBS-META-MIB", "nbsMetaMibFeatureID"))
if mibBuilder.loadTexts: nbsMetaMibFeatureEntry.setStatus('current')
nbsMetaMibFeatureID = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 205, 1, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: nbsMetaMibFeatureID.setStatus('current')
nbsMetaMibFeatureFamily = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 205, 1, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsMetaMibFeatureFamily.setStatus('current')
nbsMetaMibFeatureName = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 205, 1, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsMetaMibFeatureName.setStatus('current')
nbsMetaMibFeatureDesc = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 205, 1, 2, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsMetaMibFeatureDesc.setStatus('current')
nbsMetaMibFeatureUnits = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 205, 1, 2, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsMetaMibFeatureUnits.setStatus('current')
nbsMetaMibFeatureType = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 205, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("enum", 1), ("string", 2), ("integer", 3), ("float", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsMetaMibFeatureType.setStatus('current')
nbsMetaMibVariableTableSize = MibScalar((1, 3, 6, 1, 4, 1, 629, 205, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsMetaMibVariableTableSize.setStatus('current')
nbsMetaMibVariableTable = MibTable((1, 3, 6, 1, 4, 1, 629, 205, 1, 4), )
if mibBuilder.loadTexts: nbsMetaMibVariableTable.setStatus('current')
nbsMetaMibVariableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 205, 1, 4, 1), ).setIndexNames((0, "NBS-META-MIB", "nbsMetaMibVariableIfIndex"), (0, "NBS-META-MIB", "nbsMetaMibVariableID"))
if mibBuilder.loadTexts: nbsMetaMibVariableEntry.setStatus('current')
nbsMetaMibVariableIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 205, 1, 4, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: nbsMetaMibVariableIfIndex.setStatus('current')
nbsMetaMibVariableID = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 205, 1, 4, 1, 2), Integer32())
if mibBuilder.loadTexts: nbsMetaMibVariableID.setStatus('current')
nbsMetaMibVariableCaps = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 205, 1, 4, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsMetaMibVariableCaps.setStatus('current')
nbsMetaMibVariableDefault = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 205, 1, 4, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsMetaMibVariableDefault.setStatus('current')
nbsMetaMibVariableJumper = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 205, 1, 4, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsMetaMibVariableJumper.setStatus('current')
nbsMetaMibVariableOper = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 205, 1, 4, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsMetaMibVariableOper.setStatus('current')
nbsMetaMibVariableAdmin = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 205, 1, 4, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsMetaMibVariableAdmin.setStatus('current')
nbsMetaMibVariableStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 205, 1, 4, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsMetaMibVariableStatus.setStatus('current')
mibBuilder.exportSymbols("NBS-META-MIB", nbsMetaMibVariableStatus=nbsMetaMibVariableStatus, nbsMetaMibFeatureDesc=nbsMetaMibFeatureDesc, nbsMetaMibVariableID=nbsMetaMibVariableID, nbsMetaMibVariableTableSize=nbsMetaMibVariableTableSize, nbsMetaMibVariableEntry=nbsMetaMibVariableEntry, nbsMetaMibFeatureTableSize=nbsMetaMibFeatureTableSize, PYSNMP_MODULE_ID=nbsMetaMib, nbsMetaMibVariableJumper=nbsMetaMibVariableJumper, nbsMetaMibFeatureEntry=nbsMetaMibFeatureEntry, nbsMetaMib=nbsMetaMib, nbsMetaMibFeatureType=nbsMetaMibFeatureType, nbsMetaMibVariableTable=nbsMetaMibVariableTable, nbsMetaMibFeatureTable=nbsMetaMibFeatureTable, nbsMetaMibVariableIfIndex=nbsMetaMibVariableIfIndex, nbsMetaMibFeatureID=nbsMetaMibFeatureID, nbsMetaMibFeatureFamily=nbsMetaMibFeatureFamily, nbsMetaMibFeatureUnits=nbsMetaMibFeatureUnits, nbsMetaMibVariableCaps=nbsMetaMibVariableCaps, nbsMetaMibVariableDefault=nbsMetaMibVariableDefault, nbsMetaMibFeatureName=nbsMetaMibFeatureName, nbsMetaMibVariableAdmin=nbsMetaMibVariableAdmin, nbsMetaMibVariableOper=nbsMetaMibVariableOper, nbsMetaMibGrp=nbsMetaMibGrp)
