#
# PySNMP MIB module BTI8xx-SFP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/bti/BTI8xx-SFP-MIB
# Produced by pysmi-1.1.3 at Sun Nov 21 00:29:56 2021
# On host fv-az39-63 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
mainSystem, = mibBuilder.importSymbols("BTI8xx-TC-MIB", "mainSystem")
ifIndex, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "ifIndex", "InterfaceIndex")
PerfTotalCount, PerfIntervalCount, PerfCurrentCount = mibBuilder.importSymbols("PerfHist-TC-MIB", "PerfTotalCount", "PerfIntervalCount", "PerfCurrentCount")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Bits, ModuleIdentity, TimeTicks, Counter64, MibIdentifier, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, NotificationType, IpAddress, Gauge32, Integer32, Counter32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "ModuleIdentity", "TimeTicks", "Counter64", "MibIdentifier", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "NotificationType", "IpAddress", "Gauge32", "Integer32", "Counter32", "iso")
MacAddress, RowStatus, TruthValue, DateAndTime, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "RowStatus", "TruthValue", "DateAndTime", "TextualConvention", "DisplayString")
sfp = ModuleIdentity((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 6))
sfp.setRevisions(('2015-11-20 12:00', '2013-12-27 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: sfp.setRevisionsDescriptions(("\n            *1. Change the MAX-ACCESS(for silvercreek tool).\n              'not-accessible' -> 'read-only'\n                -sfpInfoIndex\n                -sfpInventoryIndex\n                -sfpDiagnosticIndex\n                -sfpStatusIndex\n\n            *2. Change the Syntax(for silver creek tool).\n              2.1. DisplayString -> OCTET STRING\n                sfpInfoLocation\n                sfpInfoSerialNumber\n                sfpInfoProductCode\n                sfpInventoryLocation\n                sfpInventoryType\n                sfpInventoryPecCode\n                sfpInventoryCLEI\n                sfpDiagnosticLocation\n                sfpDiagnosticCalibration\n                sfpDiagnosticTemperature\n                sfpDiagnosticVoltageV\n                sfpDiagnosticTxBiasMA\n                sfpDiagnosticTxPowerDbm\n                sfpDiagnosticRxPowerDbm\n                sfpStatusLocation\n                sfpStatusRxStatus\n                sfpStatusTxStatus\n\n              2.2. Delete the syntax value range\n                sfpInfoDistanceFiber1\n                sfpInfoDistanceFiber2\n                sfpInfoDistanceCopper\n\n            *3. MIB code sorting.\n            ", 'Initial version of MIB.',))
if mibBuilder.loadTexts: sfp.setLastUpdated('201511201200Z')
if mibBuilder.loadTexts: sfp.setOrganization('Actus Networks Ltd.')
if mibBuilder.loadTexts: sfp.setContactInfo('\n    Support:  +82-2-26535666\n    R&D:      +82-2-26535666\n    Fax:      +82-2-26534662\n    Email:    ymkim@actusnetworks.com\n    ')
if mibBuilder.loadTexts: sfp.setDescription('This is a top-level MIB for Actus whose purpose is to lay out\n    the top-level objects in the OID hierarchy from which\n    BTI8xx MIB OIDs descend.')
sfpInfoTable = MibTable((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 6, 1), )
if mibBuilder.loadTexts: sfpInfoTable.setStatus('current')
if mibBuilder.loadTexts: sfpInfoTable.setDescription('Table that contains sfp port information/configuration.')
sfpInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 6, 1, 1), ).setIndexNames((0, "BTI8xx-SFP-MIB", "sfpInfoIndex"))
if mibBuilder.loadTexts: sfpInfoEntry.setStatus('current')
if mibBuilder.loadTexts: sfpInfoEntry.setDescription('A list of information for each context.')
sfpInfoIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 6, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 12))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpInfoIndex.setStatus('current')
if mibBuilder.loadTexts: sfpInfoIndex.setDescription('The index of sfpInfoTable.')
sfpInfoLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 6, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpInfoLocation.setStatus('current')
if mibBuilder.loadTexts: sfpInfoLocation.setDescription('The Location of the sfp.')
sfpInfoSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 6, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpInfoSerialNumber.setStatus('current')
if mibBuilder.loadTexts: sfpInfoSerialNumber.setDescription('The Serial Number of the sfp.')
sfpInfoProductCode = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 6, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpInfoProductCode.setStatus('current')
if mibBuilder.loadTexts: sfpInfoProductCode.setDescription('The Product Code of the sfp.')
sfpInfoWigth = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 6, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpInfoWigth.setStatus('current')
if mibBuilder.loadTexts: sfpInfoWigth.setDescription('The Wigth(nm) of the sfp.')
sfpInfoDistanceFiber1 = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 6, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpInfoDistanceFiber1.setStatus('current')
if mibBuilder.loadTexts: sfpInfoDistanceFiber1.setDescription('The Distance Fiber1(m) of the sfp.')
sfpInfoDistanceFiber2 = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 6, 1, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpInfoDistanceFiber2.setStatus('current')
if mibBuilder.loadTexts: sfpInfoDistanceFiber2.setDescription('The Distance Fiber2(m) of the sfp.')
sfpInfoDistanceCopper = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 6, 1, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpInfoDistanceCopper.setStatus('current')
if mibBuilder.loadTexts: sfpInfoDistanceCopper.setDescription('The Distance meter - length type of the sfp.')
sfpInventoryTable = MibTable((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 6, 2), )
if mibBuilder.loadTexts: sfpInventoryTable.setStatus('current')
if mibBuilder.loadTexts: sfpInventoryTable.setDescription('Table that contains sfp port information/configuration.')
sfpInventoryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 6, 2, 1), ).setIndexNames((0, "BTI8xx-SFP-MIB", "sfpInventoryIndex"))
if mibBuilder.loadTexts: sfpInventoryEntry.setStatus('current')
if mibBuilder.loadTexts: sfpInventoryEntry.setDescription('A list of information for each context.')
sfpInventoryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 6, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 12))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpInventoryIndex.setStatus('current')
if mibBuilder.loadTexts: sfpInventoryIndex.setDescription('The index of sfpInventoryTable.')
sfpInventoryLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 6, 2, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpInventoryLocation.setStatus('current')
if mibBuilder.loadTexts: sfpInventoryLocation.setDescription('The Location of the sfp.')
sfpInventoryType = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 6, 2, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpInventoryType.setStatus('current')
if mibBuilder.loadTexts: sfpInventoryType.setDescription('The Type of the sfp Inventory.')
sfpInventoryPecCode = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 6, 2, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpInventoryPecCode.setStatus('current')
if mibBuilder.loadTexts: sfpInventoryPecCode.setDescription('The Product Equipment Code form-factory pluggable inventory item.')
sfpInventoryCLEI = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 6, 2, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpInventoryCLEI.setStatus('current')
if mibBuilder.loadTexts: sfpInventoryCLEI.setDescription('The Product Equipment Code form-factory pluggable inventory item.')
sfpInventoryStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 6, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("supported", 1), ("notSupported", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpInventoryStatus.setStatus('current')
if mibBuilder.loadTexts: sfpInventoryStatus.setDescription('The Status of the sfp Inventory.')
sfpInventoryEqStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 6, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("equipped", 1), ("unEquipped", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpInventoryEqStatus.setStatus('current')
if mibBuilder.loadTexts: sfpInventoryEqStatus.setDescription('The Eq. Status of the sfp Inventory.')
sfpDiagnosticTable = MibTable((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 6, 3), )
if mibBuilder.loadTexts: sfpDiagnosticTable.setStatus('current')
if mibBuilder.loadTexts: sfpDiagnosticTable.setDescription('Table that contains sfp port information/configuration.')
sfpDiagnosticEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 6, 3, 1), ).setIndexNames((0, "BTI8xx-SFP-MIB", "sfpDiagnosticIndex"))
if mibBuilder.loadTexts: sfpDiagnosticEntry.setStatus('current')
if mibBuilder.loadTexts: sfpDiagnosticEntry.setDescription('A list of information for each context.')
sfpDiagnosticIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 6, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 12))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpDiagnosticIndex.setStatus('current')
if mibBuilder.loadTexts: sfpDiagnosticIndex.setDescription('The index of sfpDiagnosticTable. ')
sfpDiagnosticLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 6, 3, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpDiagnosticLocation.setStatus('current')
if mibBuilder.loadTexts: sfpDiagnosticLocation.setDescription('The Location of the sfp Diagnostic.')
sfpDiagnosticCalibration = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 6, 3, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpDiagnosticCalibration.setStatus('current')
if mibBuilder.loadTexts: sfpDiagnosticCalibration.setDescription('The Calibration of the sfp Diagnostic.')
sfpDiagnosticTemperature = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 6, 3, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 24))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpDiagnosticTemperature.setStatus('current')
if mibBuilder.loadTexts: sfpDiagnosticTemperature.setDescription('The Temperature Celsius of the sfp Diagnostic.')
sfpDiagnosticVoltageV = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 6, 3, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 24))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpDiagnosticVoltageV.setStatus('current')
if mibBuilder.loadTexts: sfpDiagnosticVoltageV.setDescription('The Voltage V of the sfp Diagnostic.')
sfpDiagnosticTxBiasMA = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 6, 3, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 24))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpDiagnosticTxBiasMA.setStatus('current')
if mibBuilder.loadTexts: sfpDiagnosticTxBiasMA.setDescription('The Tx Bias mA of the sfp Diagnostic.')
sfpDiagnosticTxPowerDbm = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 6, 3, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 24))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpDiagnosticTxPowerDbm.setStatus('current')
if mibBuilder.loadTexts: sfpDiagnosticTxPowerDbm.setDescription('The Tx Power Dbm of the sfp Diagnostic.')
sfpDiagnosticRxPowerDbm = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 6, 3, 1, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 24))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpDiagnosticRxPowerDbm.setStatus('current')
if mibBuilder.loadTexts: sfpDiagnosticRxPowerDbm.setDescription('The Rx Power Dbm of the sfp Diagnostic.')
sfpStatusTable = MibTable((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 6, 4), )
if mibBuilder.loadTexts: sfpStatusTable.setStatus('current')
if mibBuilder.loadTexts: sfpStatusTable.setDescription('Table that contains sfp port information/configuration.')
sfpStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 6, 4, 1), ).setIndexNames((0, "BTI8xx-SFP-MIB", "sfpStatusIndex"))
if mibBuilder.loadTexts: sfpStatusEntry.setStatus('current')
if mibBuilder.loadTexts: sfpStatusEntry.setDescription('A list of information for each context.')
sfpStatusIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 6, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 12))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpStatusIndex.setStatus('current')
if mibBuilder.loadTexts: sfpStatusIndex.setDescription('The index of sfpStatusTable. ')
sfpStatusLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 6, 4, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpStatusLocation.setStatus('current')
if mibBuilder.loadTexts: sfpStatusLocation.setDescription('The Location of the sfp Status.')
sfpStatusEqStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 6, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("equipped", 1), ("unEquipped", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpStatusEqStatus.setStatus('current')
if mibBuilder.loadTexts: sfpStatusEqStatus.setDescription('The Equipped of the sfp Status.')
sfpStatusRxStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 6, 4, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpStatusRxStatus.setStatus('current')
if mibBuilder.loadTexts: sfpStatusRxStatus.setDescription('The Rx Status of the sfp Status.')
sfpStatusTxStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 6, 4, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpStatusTxStatus.setStatus('current')
if mibBuilder.loadTexts: sfpStatusTxStatus.setDescription('The Tx Status of the sfp Status.')
mibBuilder.exportSymbols("BTI8xx-SFP-MIB", sfpStatusLocation=sfpStatusLocation, sfpInfoDistanceFiber2=sfpInfoDistanceFiber2, sfpStatusRxStatus=sfpStatusRxStatus, sfpInventoryEqStatus=sfpInventoryEqStatus, sfpDiagnosticTemperature=sfpDiagnosticTemperature, sfp=sfp, sfpInfoSerialNumber=sfpInfoSerialNumber, sfpInfoIndex=sfpInfoIndex, sfpStatusTable=sfpStatusTable, sfpDiagnosticLocation=sfpDiagnosticLocation, sfpDiagnosticRxPowerDbm=sfpDiagnosticRxPowerDbm, sfpStatusEqStatus=sfpStatusEqStatus, sfpStatusTxStatus=sfpStatusTxStatus, sfpInfoDistanceCopper=sfpInfoDistanceCopper, sfpStatusIndex=sfpStatusIndex, sfpDiagnosticCalibration=sfpDiagnosticCalibration, sfpInfoDistanceFiber1=sfpInfoDistanceFiber1, sfpInfoEntry=sfpInfoEntry, sfpInventoryStatus=sfpInventoryStatus, sfpDiagnosticTxBiasMA=sfpDiagnosticTxBiasMA, sfpInventoryPecCode=sfpInventoryPecCode, sfpInfoProductCode=sfpInfoProductCode, sfpInfoLocation=sfpInfoLocation, sfpInventoryEntry=sfpInventoryEntry, sfpDiagnosticTable=sfpDiagnosticTable, sfpInfoTable=sfpInfoTable, sfpDiagnosticIndex=sfpDiagnosticIndex, sfpInventoryType=sfpInventoryType, sfpDiagnosticTxPowerDbm=sfpDiagnosticTxPowerDbm, sfpStatusEntry=sfpStatusEntry, sfpInfoWigth=sfpInfoWigth, sfpDiagnosticVoltageV=sfpDiagnosticVoltageV, sfpInventoryIndex=sfpInventoryIndex, sfpInventoryCLEI=sfpInventoryCLEI, PYSNMP_MODULE_ID=sfp, sfpDiagnosticEntry=sfpDiagnosticEntry, sfpInventoryTable=sfpInventoryTable, sfpInventoryLocation=sfpInventoryLocation)
