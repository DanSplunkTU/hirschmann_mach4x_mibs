#
# PySNMP MIB module UCD-DLMOD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/UCD-DLMOD-MIB
# Produced by pysmi-1.1.0 at Mon Nov 15 18:46:22 2021
# On host fv-az77-248 platform Linux version 5.11.0-1020-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Bits, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, IpAddress, Integer32, Counter32, Counter64, TimeTicks, ObjectIdentity, NotificationType, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Bits", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "IpAddress", "Integer32", "Counter32", "Counter64", "TimeTicks", "ObjectIdentity", "NotificationType", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ucdExperimental, = mibBuilder.importSymbols("UCD-SNMP-MIB", "ucdExperimental")
ucdDlmodMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2021, 13, 14))
ucdDlmodMIB.setRevisions(('2000-01-26 00:00', '1999-12-10 00:00',))
if mibBuilder.loadTexts: ucdDlmodMIB.setLastUpdated('200001260000Z')
if mibBuilder.loadTexts: ucdDlmodMIB.setOrganization('University of California, Davis')
dlmodNextIndex = MibScalar((1, 3, 6, 1, 4, 1, 2021, 13, 14, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dlmodNextIndex.setStatus('current')
dlmodTable = MibTable((1, 3, 6, 1, 4, 1, 2021, 13, 14, 2), )
if mibBuilder.loadTexts: dlmodTable.setStatus('current')
dlmodEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2021, 13, 14, 2, 1), ).setIndexNames((0, "UCD-DLMOD-MIB", "dlmodIndex"))
if mibBuilder.loadTexts: dlmodEntry.setStatus('current')
dlmodIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 14, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: dlmodIndex.setStatus('current')
dlmodName = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 14, 2, 1, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dlmodName.setStatus('current')
dlmodPath = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 14, 2, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dlmodPath.setStatus('current')
dlmodError = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 14, 2, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dlmodError.setStatus('current')
dlmodStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 14, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("loaded", 1), ("unloaded", 2), ("error", 3), ("load", 4), ("unload", 5), ("create", 6), ("delete", 7)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dlmodStatus.setStatus('current')
mibBuilder.exportSymbols("UCD-DLMOD-MIB", dlmodIndex=dlmodIndex, dlmodError=dlmodError, PYSNMP_MODULE_ID=ucdDlmodMIB, ucdDlmodMIB=ucdDlmodMIB, dlmodName=dlmodName, dlmodNextIndex=dlmodNextIndex, dlmodTable=dlmodTable, dlmodPath=dlmodPath, dlmodEntry=dlmodEntry, dlmodStatus=dlmodStatus)
