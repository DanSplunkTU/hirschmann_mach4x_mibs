#
# PySNMP MIB module NBS-OPTIC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/mrv/NBS-OPTIC-MIB
# Produced by pysmi-1.1.8 at Mon Feb  7 16:16:28 2022
# On host fv-az42-619 platform Linux version 5.11.0-1028-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
nbs, = mibBuilder.importSymbols("NBS-MIB", "nbs")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, Counter32, TimeTicks, IpAddress, Counter64, NotificationType, ObjectIdentity, Unsigned32, iso, Bits, Integer32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Counter32", "TimeTicks", "IpAddress", "Counter64", "NotificationType", "ObjectIdentity", "Unsigned32", "iso", "Bits", "Integer32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
nbsOpticMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 629, 213))
if mibBuilder.loadTexts: nbsOpticMib.setLastUpdated('201209260000Z')
if mibBuilder.loadTexts: nbsOpticMib.setOrganization('NBS')
nbsOpticPortGrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 213, 1))
if mibBuilder.loadTexts: nbsOpticPortGrp.setStatus('current')
nbsOpticPortTableSize = MibScalar((1, 3, 6, 1, 4, 1, 629, 213, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsOpticPortTableSize.setStatus('current')
nbsOpticPortTable = MibTable((1, 3, 6, 1, 4, 1, 629, 213, 1, 2), )
if mibBuilder.loadTexts: nbsOpticPortTable.setStatus('current')
nbsOpticPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 213, 1, 2, 1), ).setIndexNames((0, "NBS-OPTIC-MIB", "nbsOpticPortNdx"))
if mibBuilder.loadTexts: nbsOpticPortEntry.setStatus('current')
nbsOpticPortNdx = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 213, 1, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: nbsOpticPortNdx.setStatus('current')
nbsOpticPortTxStatusAdmin = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 213, 1, 2, 1, 21), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notSupported", 1), ("outOfService", 2), ("inService", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsOpticPortTxStatusAdmin.setStatus('current')
nbsOpticPortTxStatusOper = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 213, 1, 2, 1, 22), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notSupported", 1), ("outOfService", 2), ("inService", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsOpticPortTxStatusOper.setStatus('current')
nbsOpticPortRxStatusAdmin = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 213, 1, 2, 1, 31), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notSupported", 1), ("outOfService", 2), ("inService", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsOpticPortRxStatusAdmin.setStatus('current')
nbsOpticPortRxStatusOper = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 213, 1, 2, 1, 32), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notSupported", 1), ("outOfService", 2), ("inService", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsOpticPortRxStatusOper.setStatus('current')
nbsOpticPortConnector = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 213, 1, 2, 1, 41), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsOpticPortConnector.setStatus('current')
nbsOpticPortPolish = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 213, 1, 2, 1, 42), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("notSupported", 1), ("pc", 2), ("upc", 3), ("apc", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsOpticPortPolish.setStatus('current')
nbsOpticPortFiberMode = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 213, 1, 2, 1, 51), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("notSupported", 1), ("reserved2", 2), ("reserved3", 3), ("singleMode", 4), ("multiMode", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsOpticPortFiberMode.setStatus('current')
mibBuilder.exportSymbols("NBS-OPTIC-MIB", nbsOpticPortRxStatusOper=nbsOpticPortRxStatusOper, nbsOpticPortRxStatusAdmin=nbsOpticPortRxStatusAdmin, nbsOpticPortTableSize=nbsOpticPortTableSize, nbsOpticPortEntry=nbsOpticPortEntry, nbsOpticPortNdx=nbsOpticPortNdx, nbsOpticPortGrp=nbsOpticPortGrp, PYSNMP_MODULE_ID=nbsOpticMib, nbsOpticMib=nbsOpticMib, nbsOpticPortTxStatusOper=nbsOpticPortTxStatusOper, nbsOpticPortPolish=nbsOpticPortPolish, nbsOpticPortTable=nbsOpticPortTable, nbsOpticPortTxStatusAdmin=nbsOpticPortTxStatusAdmin, nbsOpticPortFiberMode=nbsOpticPortFiberMode, nbsOpticPortConnector=nbsOpticPortConnector)
