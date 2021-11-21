#
# PySNMP MIB module PRVT-STATISTICS-HISTORY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/telco-systems/binox/PRVT-STATISTICS-HISTORY-MIB
# Produced by pysmi-1.1.3 at Sun Nov 21 00:45:51 2021
# On host fv-az39-63 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
switch, = mibBuilder.importSymbols("PRVT-SWITCH-MIB", "switch")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, ObjectIdentity, Unsigned32, MibIdentifier, Counter64, Gauge32, ModuleIdentity, Integer32, Counter32, NotificationType, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "ObjectIdentity", "Unsigned32", "MibIdentifier", "Counter64", "Gauge32", "ModuleIdentity", "Integer32", "Counter32", "NotificationType", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "IpAddress")
TextualConvention, DisplayString, RowStatus, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "RowStatus", "TruthValue")
prvtStatHistMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 738, 10, 5, 180))
prvtStatHistMIB.setRevisions(('2012-02-20 00:00',))
if mibBuilder.loadTexts: prvtStatHistMIB.setLastUpdated('201202200000Z')
if mibBuilder.loadTexts: prvtStatHistMIB.setOrganization('BATM Advanced Communication')
prvtStatHistObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 10, 5, 180, 1))
prvtStatHistShutdown = MibScalar((1, 3, 6, 1, 4, 1, 738, 10, 5, 180, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtStatHistShutdown.setStatus('current')
prvtStatHistGetInterval = MibScalar((1, 3, 6, 1, 4, 1, 738, 10, 5, 180, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(10, 3600))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtStatHistGetInterval.setStatus('current')
prvtStatHistType = MibScalar((1, 3, 6, 1, 4, 1, 738, 10, 5, 180, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("absolute", 1), ("delta", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtStatHistType.setStatus('current')
prvtStatHistProfileTable = MibTable((1, 3, 6, 1, 4, 1, 738, 10, 5, 180, 1, 4), )
if mibBuilder.loadTexts: prvtStatHistProfileTable.setStatus('current')
prvtStatHistProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 10, 5, 180, 1, 4, 1), ).setIndexNames((0, "PRVT-STATISTICS-HISTORY-MIB", "prvtStatHistProfileName"))
if mibBuilder.loadTexts: prvtStatHistProfileEntry.setStatus('current')
prvtStatHistProfileName = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 180, 1, 4, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 128)))
if mibBuilder.loadTexts: prvtStatHistProfileName.setStatus('current')
prvtStatHistProfileRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 180, 1, 4, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtStatHistProfileRowStatus.setStatus('current')
prvtStatHistProfileXPathTemplate = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 180, 1, 4, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtStatHistProfileXPathTemplate.setStatus('current')
prvtStatHistControlTable = MibTable((1, 3, 6, 1, 4, 1, 738, 10, 5, 180, 1, 5), )
if mibBuilder.loadTexts: prvtStatHistControlTable.setStatus('current')
prvtStatHistControlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 10, 5, 180, 1, 5, 1), ).setIndexNames((0, "PRVT-STATISTICS-HISTORY-MIB", "prvtStatHistControlId"))
if mibBuilder.loadTexts: prvtStatHistControlEntry.setStatus('current')
prvtStatHistControlId = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 180, 1, 5, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 200)))
if mibBuilder.loadTexts: prvtStatHistControlId.setStatus('current')
prvtStatHistControlRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 180, 1, 5, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtStatHistControlRowStatus.setStatus('current')
prvtStatHistControlProfileName = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 180, 1, 5, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtStatHistControlProfileName.setStatus('current')
prvtStatHistControlXPathKey = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 180, 1, 5, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtStatHistControlXPathKey.setStatus('current')
prvtStatHistControlValue = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 180, 1, 5, 1, 5), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtStatHistControlValue.setStatus('current')
prvtStatHistControlFirstDataId = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 180, 1, 5, 1, 6), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtStatHistControlFirstDataId.setStatus('current')
prvtStatHistControlLastDataId = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 180, 1, 5, 1, 7), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtStatHistControlLastDataId.setStatus('current')
prvtStatHistDataTable = MibTable((1, 3, 6, 1, 4, 1, 738, 10, 5, 180, 1, 6), )
if mibBuilder.loadTexts: prvtStatHistDataTable.setStatus('current')
prvtStatHistDataEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 10, 5, 180, 1, 6, 1), ).setIndexNames((0, "PRVT-STATISTICS-HISTORY-MIB", "prvtStatHistControlId"), (0, "PRVT-STATISTICS-HISTORY-MIB", "prvtStatHistDataId"))
if mibBuilder.loadTexts: prvtStatHistDataEntry.setStatus('current')
prvtStatHistDataId = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 180, 1, 6, 1, 1), OctetString())
if mibBuilder.loadTexts: prvtStatHistDataId.setStatus('current')
prvtStatHistDataIntervalStart = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 180, 1, 6, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtStatHistDataIntervalStart.setStatus('current')
prvtStatHistDataIntervalEnd = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 180, 1, 6, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtStatHistDataIntervalEnd.setStatus('current')
prvtStatHistDataProfile = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 180, 1, 6, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtStatHistDataProfile.setStatus('current')
prvtStatHistDataKey = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 180, 1, 6, 1, 5), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtStatHistDataKey.setStatus('current')
prvtStatHistDataValue = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 180, 1, 6, 1, 6), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtStatHistDataValue.setStatus('current')
prvtStatHistDataStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 180, 1, 6, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notAvailable", 1), ("positive", 2), ("negative", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtStatHistDataStatus.setStatus('current')
mibBuilder.exportSymbols("PRVT-STATISTICS-HISTORY-MIB", prvtStatHistControlValue=prvtStatHistControlValue, prvtStatHistControlRowStatus=prvtStatHistControlRowStatus, prvtStatHistDataValue=prvtStatHistDataValue, prvtStatHistDataStatus=prvtStatHistDataStatus, prvtStatHistControlTable=prvtStatHistControlTable, prvtStatHistProfileRowStatus=prvtStatHistProfileRowStatus, prvtStatHistType=prvtStatHistType, prvtStatHistControlId=prvtStatHistControlId, prvtStatHistProfileTable=prvtStatHistProfileTable, prvtStatHistDataIntervalEnd=prvtStatHistDataIntervalEnd, prvtStatHistShutdown=prvtStatHistShutdown, prvtStatHistControlEntry=prvtStatHistControlEntry, prvtStatHistDataTable=prvtStatHistDataTable, prvtStatHistMIB=prvtStatHistMIB, prvtStatHistDataEntry=prvtStatHistDataEntry, prvtStatHistDataId=prvtStatHistDataId, prvtStatHistControlLastDataId=prvtStatHistControlLastDataId, prvtStatHistControlFirstDataId=prvtStatHistControlFirstDataId, prvtStatHistProfileName=prvtStatHistProfileName, prvtStatHistDataIntervalStart=prvtStatHistDataIntervalStart, prvtStatHistObjects=prvtStatHistObjects, prvtStatHistGetInterval=prvtStatHistGetInterval, prvtStatHistProfileEntry=prvtStatHistProfileEntry, prvtStatHistDataKey=prvtStatHistDataKey, prvtStatHistDataProfile=prvtStatHistDataProfile, prvtStatHistControlXPathKey=prvtStatHistControlXPathKey, prvtStatHistProfileXPathTemplate=prvtStatHistProfileXPathTemplate, PYSNMP_MODULE_ID=prvtStatHistMIB, prvtStatHistControlProfileName=prvtStatHistControlProfileName)
