#
# PySNMP MIB module PACKETLOGIC-HW-SFP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/procera/PACKETLOGIC-HW-SFP-MIB
# Produced by pysmi-1.1.3 at Sun Nov 28 20:20:24 2021
# On host fv-az77-612 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
CounterBasedGauge64, = mibBuilder.importSymbols("HCNUM-TC", "CounterBasedGauge64")
hw, = mibBuilder.importSymbols("PACKETLOGIC-HW-MIB", "hw")
packetlogic2, = mibBuilder.importSymbols("PACKETLOGIC-MIB", "packetlogic2")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, Gauge32, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, iso, Unsigned32, Counter32, TimeTicks, IpAddress, Counter64, Bits, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Gauge32", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "iso", "Unsigned32", "Counter32", "TimeTicks", "IpAddress", "Counter64", "Bits", "ModuleIdentity")
DateAndTime, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "DisplayString", "TextualConvention")
sfp = ModuleIdentity((1, 3, 6, 1, 4, 1, 15397, 2, 30, 4))
sfp.setRevisions(('2019-09-12 15:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: sfp.setRevisionsDescriptions((' Latest version at the revision date for version GET VERSION HERE',))
if mibBuilder.loadTexts: sfp.setLastUpdated('201909121500Z')
if mibBuilder.loadTexts: sfp.setOrganization('Procera Networks, Inc.')
if mibBuilder.loadTexts: sfp.setContactInfo('support@proceranetworks.com')
if mibBuilder.loadTexts: sfp.setDescription('MIB For SFP and SFP+ Optical Transceivers')
ports = MibTable((1, 3, 6, 1, 4, 1, 15397, 2, 30, 4, 1), )
if mibBuilder.loadTexts: ports.setStatus('current')
if mibBuilder.loadTexts: ports.setDescription('Conceptual Table')
portEntry = MibTableRow((1, 3, 6, 1, 4, 1, 15397, 2, 30, 4, 1, 1), ).setIndexNames((0, "PACKETLOGIC-HW-SFP-MIB", "portEntryIndex"))
if mibBuilder.loadTexts: portEntry.setStatus('current')
if mibBuilder.loadTexts: portEntry.setDescription('Conceptual Table')
portEntryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 30, 4, 1, 1, 999), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: portEntryIndex.setStatus('current')
if mibBuilder.loadTexts: portEntryIndex.setDescription('Unique Row Index for Conceptual Table')
portName = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 30, 4, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portName.setStatus('current')
if mibBuilder.loadTexts: portName.setDescription('Port Name')
portCompatibility = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 30, 4, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portCompatibility.setStatus('current')
if mibBuilder.loadTexts: portCompatibility.setDescription('Electronic or optical compatibility')
portVendorName = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 30, 4, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portVendorName.setStatus('current')
if mibBuilder.loadTexts: portVendorName.setDescription('SFP vendor name')
portVendorOUI = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 30, 4, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portVendorOUI.setStatus('current')
if mibBuilder.loadTexts: portVendorOUI.setDescription('SFP vendor IEEE company ID')
portVendorPN = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 30, 4, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portVendorPN.setStatus('current')
if mibBuilder.loadTexts: portVendorPN.setDescription('Part number provided by SFP vendor')
portVendorRevisionLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 30, 4, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portVendorRevisionLevel.setStatus('current')
if mibBuilder.loadTexts: portVendorRevisionLevel.setDescription('Revision level for part number provided by vendor')
checksumBaseFields = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 30, 4, 1, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: checksumBaseFields.setStatus('current')
if mibBuilder.loadTexts: checksumBaseFields.setDescription('Check code for Base ID Fields')
portVendorSN = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 30, 4, 1, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portVendorSN.setStatus('current')
if mibBuilder.loadTexts: portVendorSN.setDescription('Serial number provided by vendor')
portVendorDateCode = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 30, 4, 1, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portVendorDateCode.setStatus('current')
if mibBuilder.loadTexts: portVendorDateCode.setDescription('Vendor manufacturing date code')
checksumExtendedFields = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 30, 4, 1, 1, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: checksumExtendedFields.setStatus('current')
if mibBuilder.loadTexts: checksumExtendedFields.setDescription('Check code for the Extended ID Fields')
mibBuilder.exportSymbols("PACKETLOGIC-HW-SFP-MIB", portName=portName, portVendorPN=portVendorPN, portVendorOUI=portVendorOUI, portCompatibility=portCompatibility, sfp=sfp, PYSNMP_MODULE_ID=sfp, checksumExtendedFields=checksumExtendedFields, portEntryIndex=portEntryIndex, portVendorRevisionLevel=portVendorRevisionLevel, checksumBaseFields=checksumBaseFields, portVendorSN=portVendorSN, portVendorDateCode=portVendorDateCode, portVendorName=portVendorName, portEntry=portEntry, ports=ports)
