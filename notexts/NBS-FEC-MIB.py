#
# PySNMP MIB module NBS-FEC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/mrv/NBS-FEC-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:30:34 2022
# On host fv-az36-988 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
nbs, = mibBuilder.importSymbols("NBS-MIB", "nbs")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, Unsigned32, ModuleIdentity, TimeTicks, ObjectIdentity, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Gauge32, Integer32, IpAddress, MibIdentifier, NotificationType, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Unsigned32", "ModuleIdentity", "TimeTicks", "ObjectIdentity", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Gauge32", "Integer32", "IpAddress", "MibIdentifier", "NotificationType", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
nbsFecMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 629, 232))
if mibBuilder.loadTexts: nbsFecMib.setLastUpdated('201504290000Z')
if mibBuilder.loadTexts: nbsFecMib.setOrganization('NBS')
class NbsFecCode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15))
    namedValues = NamedValues(("notSupported", 0), ("noFec", 1), ("zero", 2), ("gfec", 3), ("ufec7", 4), ("ufec10", 5), ("ufec25", 6), ("hgfec7", 7), ("sdfec0", 8), ("sdfec1", 9), ("sdfec2", 10), ("sdfec3", 11), ("g975i4", 12), ("g975i7", 13), ("xfec7", 14), ("sdfec15", 15))

nbsFecCfgGrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 232, 1))
if mibBuilder.loadTexts: nbsFecCfgGrp.setStatus('current')
nbsFecCfgTable = MibTable((1, 3, 6, 1, 4, 1, 629, 232, 1, 1), )
if mibBuilder.loadTexts: nbsFecCfgTable.setStatus('current')
nbsFecCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 232, 1, 1, 1), ).setIndexNames((0, "NBS-FEC-MIB", "nbsFecCfgIfIndex"))
if mibBuilder.loadTexts: nbsFecCfgEntry.setStatus('current')
nbsFecCfgIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 232, 1, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: nbsFecCfgIfIndex.setStatus('current')
nbsFecCfgCodeCaps = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 232, 1, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(3, 3)).setFixedLength(3)).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsFecCfgCodeCaps.setStatus('current')
nbsFecCfgCodeAdmin = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 232, 1, 1, 1, 3), NbsFecCode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsFecCfgCodeAdmin.setStatus('current')
nbsFecCfgCodeOper = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 232, 1, 1, 1, 4), NbsFecCode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsFecCfgCodeOper.setStatus('current')
mibBuilder.exportSymbols("NBS-FEC-MIB", nbsFecCfgEntry=nbsFecCfgEntry, nbsFecCfgTable=nbsFecCfgTable, PYSNMP_MODULE_ID=nbsFecMib, NbsFecCode=NbsFecCode, nbsFecCfgGrp=nbsFecCfgGrp, nbsFecCfgIfIndex=nbsFecCfgIfIndex, nbsFecCfgCodeCaps=nbsFecCfgCodeCaps, nbsFecCfgCodeOper=nbsFecCfgCodeOper, nbsFecCfgCodeAdmin=nbsFecCfgCodeAdmin, nbsFecMib=nbsFecMib)
