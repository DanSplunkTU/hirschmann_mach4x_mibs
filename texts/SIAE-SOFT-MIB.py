#
# PySNMP MIB module SIAE-SOFT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/siae/SIAE-SOFT-MIB
# Produced by pysmi-1.1.8 at Sun Jan 16 00:44:13 2022
# On host fv-az42-839 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
alarmTrap, = mibBuilder.importSymbols("SIAE-ALARM-MIB", "alarmTrap")
equipIpSnmpAgentAddress, = mibBuilder.importSymbols("SIAE-EQUIP-MIB", "equipIpSnmpAgentAddress")
siaeMib, = mibBuilder.importSymbols("SIAE-TREE-MIB", "siaeMib")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Bits, Gauge32, Unsigned32, ModuleIdentity, IpAddress, iso, Counter32, NotificationType, MibIdentifier, Integer32, Counter64, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Bits", "Gauge32", "Unsigned32", "ModuleIdentity", "IpAddress", "iso", "Counter32", "NotificationType", "MibIdentifier", "Integer32", "Counter64", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
software = ModuleIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 7))
software.setRevisions(('2015-03-23 00:00', '2014-02-03 00:00', '2013-04-16 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: software.setRevisionsDescriptions(('Removed alarmTrapNumber from softwareDownloadStatusTrap\n             and IMPORTS.\n            ', 'Improved description of softwareMibVersion\n            ', 'Initial version 01.00.00\n            ',))
if mibBuilder.loadTexts: software.setLastUpdated('201503230000Z')
if mibBuilder.loadTexts: software.setOrganization('SIAE MICROELETTRONICA spa')
if mibBuilder.loadTexts: software.setContactInfo('SIAE MICROELETTONICA s.p.a.\n             Via Michelangelo Buonarroti, 21\n             20093 - Cologno Monzese\n             Milano - ITALY\n             Phone :  +39-02-27325-1\n             E-mail: help@siaemic.com\n            ')
if mibBuilder.loadTexts: software.setDescription('Maintenance of software releases loaded on SIAE equiment.\n            ')
softwareMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 7, 1), Integer32().clone(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: softwareMibVersion.setStatus('current')
if mibBuilder.loadTexts: softwareMibVersion.setDescription('Numerical version of this module.\n             The string version of this MIB have the following format:\n                XX.YY.ZZ\n             so, for example, the value 1 should be interpreted as 00.00.01\n             and the value 10001 should be interpreted as 01.00.01.')
softwareEquipmentReleaseBench1 = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 7, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: softwareEquipmentReleaseBench1.setStatus('current')
if mibBuilder.loadTexts: softwareEquipmentReleaseBench1.setDescription('ASCII string identifying the equipment release present in Bench1.')
softwareEquipmentReleaseBench1Status = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 7, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notLoaded", 1), ("loaded", 2), ("running", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: softwareEquipmentReleaseBench1Status.setStatus('current')
if mibBuilder.loadTexts: softwareEquipmentReleaseBench1Status.setDescription('Status of the bench 1 software.')
softwareEquipmentReleaseBench2 = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 7, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: softwareEquipmentReleaseBench2.setStatus('current')
if mibBuilder.loadTexts: softwareEquipmentReleaseBench2.setDescription('ASCII string identifying the equipment release present in Bench2.')
softwareEquipmentReleaseBench2Status = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 7, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notLoaded", 1), ("loaded", 2), ("running", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: softwareEquipmentReleaseBench2Status.setStatus('current')
if mibBuilder.loadTexts: softwareEquipmentReleaseBench2Status.setDescription('Status of the bench 2 software.')
softwareIpAddressDwlServer = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 7, 6), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: softwareIpAddressDwlServer.setStatus('current')
if mibBuilder.loadTexts: softwareIpAddressDwlServer.setDescription("Ip address of the SNMP manager connected from which the Software is downloaded,\n             if the leaf softwareRemoteIpAddressDwlServer is set '0.0.0.0'.")
softwareGosipAddressDwlServer = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 7, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: softwareGosipAddressDwlServer.setStatus('current')
if mibBuilder.loadTexts: softwareGosipAddressDwlServer.setDescription('GOSIP address of the remote element from which the Software is downloaded.')
softwareDownloadfile = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 7, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: softwareDownloadfile.setStatus('current')
if mibBuilder.loadTexts: softwareDownloadfile.setDescription('CEM or LOM Directory and name of the descriptor file. The files\n             with the SW code must be present in the same directory.')
softwareActionRequest = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 7, 9), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: softwareActionRequest.setStatus('current')
if mibBuilder.loadTexts: softwareActionRequest.setDescription('This Integer is a bit string  with each bit when set has the following meaning:\n              BIT 0   -    Download  request\n              BIT 1   -    Abort Download  request\n              BIT 2   -    Bench switch   request\n              BIT 4   -    Partial download\n              BIT 5   -    Forced Download\n              BIT 6   -    Implicit Activation\n              BIT 7   -    Delete bench not running\n              BIT 8   -    ODU FW download (whitout activation)\n              BIT 9   -    ODU FW activation\n              BIT 10  -    IDU FPGA download (whitout activation)\n              BIT 11  -    IDU FPGA activation\n             The bit 4...6 enable/disable the different options on download request.')
softwareDownloadStatus = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 7, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("downloading", 1), ("completed", 2), ("interrupted", 3), ("perifDownloading", 4), ("configurationDownloading", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: softwareDownloadStatus.setStatus('current')
if mibBuilder.loadTexts: softwareDownloadStatus.setDescription('Status of SW download operation.')
softwareUnitTable = MibTable((1, 3, 6, 1, 4, 1, 3373, 1103, 7, 11), )
if mibBuilder.loadTexts: softwareUnitTable.setStatus('current')
if mibBuilder.loadTexts: softwareUnitTable.setDescription('Table with Software records concerning units within the equipment.')
softwareUnitRecord = MibTableRow((1, 3, 6, 1, 4, 1, 3373, 1103, 7, 11, 1), ).setIndexNames((0, "SIAE-SOFT-MIB", "softwareUnitId"), (0, "SIAE-SOFT-MIB", "softwareElementId"))
if mibBuilder.loadTexts: softwareUnitRecord.setStatus('current')
if mibBuilder.loadTexts: softwareUnitRecord.setDescription('Software record.')
softwareUnitId = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 7, 11, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: softwareUnitId.setStatus('current')
if mibBuilder.loadTexts: softwareUnitId.setDescription('This object is used as Index of the softwareUnit Table and also identifies\n             the unit in the equipment.')
softwareElementId = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 7, 11, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: softwareElementId.setStatus('current')
if mibBuilder.loadTexts: softwareElementId.setDescription('This object is used as Index of the softwareUnit Table and also identifies\n             the SW programmable element in the specified unit.')
softwareType = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 7, 11, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("s-record", 1), ("image-FPGA", 2), ("volatile", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: softwareType.setStatus('current')
if mibBuilder.loadTexts: softwareType.setDescription('Format type.')
softwareUnitReleaseBench1 = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 7, 11, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: softwareUnitReleaseBench1.setStatus('current')
if mibBuilder.loadTexts: softwareUnitReleaseBench1.setDescription('ASCII string identifying the software release present\n             in the programmable element of specified unit bench 1.')
softwareUnitReleaseBench2 = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 7, 11, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: softwareUnitReleaseBench2.setStatus('current')
if mibBuilder.loadTexts: softwareUnitReleaseBench2.setDescription('ASCII string identifying the software release present\n             in the programmable element of specified unit bench 2.')
softwareUnitActualRelease = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 7, 11, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 33))).setMaxAccess("readonly")
if mibBuilder.loadTexts: softwareUnitActualRelease.setStatus('current')
if mibBuilder.loadTexts: softwareUnitActualRelease.setDescription('ASCII string identifying the software release actually present\n             in the programmable element of specified unit.')
softwareDownloadStatusTrapNotification = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 7, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 34))).clone(namedValues=NamedValues(("trapDisable", 1), ("trapEnable", 2), ("trapEnableWithACK", 34))).clone('trapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: softwareDownloadStatusTrapNotification.setStatus('current')
if mibBuilder.loadTexts: softwareDownloadStatusTrapNotification.setDescription('Enables/disables the trap generation on download status change.')
softwareRemoteIpAddressDwlServer = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 7, 13), IpAddress().clone(hexValue="00")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: softwareRemoteIpAddressDwlServer.setStatus('current')
if mibBuilder.loadTexts: softwareRemoteIpAddressDwlServer.setDescription("Ip address of the remote Server from which the Software is downloaded,\n             different from SNMP manager connected IpAddress.\n             It is used if different from '0.0.0.0'.\n             After each download procedure the leaf is set to '0.0.0.0'.")
softwareDownloadStatusTrap = NotificationType((1, 3, 6, 1, 4, 1, 3373, 1103, 0, 701)).setObjects(("SIAE-EQUIP-MIB", "equipIpSnmpAgentAddress"), ("SIAE-SOFT-MIB", "softwareDownloadStatus"))
if mibBuilder.loadTexts: softwareDownloadStatusTrap.setStatus('current')
if mibBuilder.loadTexts: softwareDownloadStatusTrap.setDescription('This event is generated by ALFOHD-NE when the status of download is changed.\n             The data passed with the event are:\n                1) equipIpSnmpAgentAddress\n                2) softwareDownloadStatus')
mibBuilder.exportSymbols("SIAE-SOFT-MIB", softwareDownloadfile=softwareDownloadfile, softwareElementId=softwareElementId, softwareUnitActualRelease=softwareUnitActualRelease, PYSNMP_MODULE_ID=software, softwareDownloadStatus=softwareDownloadStatus, softwareUnitReleaseBench1=softwareUnitReleaseBench1, softwareEquipmentReleaseBench1Status=softwareEquipmentReleaseBench1Status, softwareEquipmentReleaseBench1=softwareEquipmentReleaseBench1, softwareMibVersion=softwareMibVersion, softwareUnitReleaseBench2=softwareUnitReleaseBench2, softwareUnitTable=softwareUnitTable, software=software, softwareDownloadStatusTrapNotification=softwareDownloadStatusTrapNotification, softwareEquipmentReleaseBench2Status=softwareEquipmentReleaseBench2Status, softwareUnitId=softwareUnitId, softwareGosipAddressDwlServer=softwareGosipAddressDwlServer, softwareIpAddressDwlServer=softwareIpAddressDwlServer, softwareType=softwareType, softwareEquipmentReleaseBench2=softwareEquipmentReleaseBench2, softwareDownloadStatusTrap=softwareDownloadStatusTrap, softwareRemoteIpAddressDwlServer=softwareRemoteIpAddressDwlServer, softwareActionRequest=softwareActionRequest, softwareUnitRecord=softwareUnitRecord)
