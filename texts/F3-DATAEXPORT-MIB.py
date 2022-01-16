#
# PySNMP MIB module F3-DATAEXPORT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/adva/F3-DATAEXPORT-MIB
# Produced by pysmi-1.1.8 at Sun Jan 16 00:31:31 2022
# On host fv-az42-839 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
fsp150cm, = mibBuilder.importSymbols("ADVA-MIB", "fsp150cm")
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
IpVersion, PerfCounter64 = mibBuilder.importSymbols("CM-COMMON-MIB", "IpVersion", "PerfCounter64")
Ipv6Address, = mibBuilder.importSymbols("IPV6-TC", "Ipv6Address")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
TimeTicks, Counter32, Bits, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Unsigned32, MibIdentifier, Integer32, NotificationType, ModuleIdentity, iso, Counter64, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Counter32", "Bits", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Unsigned32", "MibIdentifier", "Integer32", "NotificationType", "ModuleIdentity", "iso", "Counter64", "ObjectIdentity")
StorageType, RowStatus, DisplayString, TextualConvention, VariablePointer = mibBuilder.importSymbols("SNMPv2-TC", "StorageType", "RowStatus", "DisplayString", "TextualConvention", "VariablePointer")
f3DataExportMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2544, 1, 12, 30))
f3DataExportMIB.setRevisions(('2013-10-31 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: f3DataExportMIB.setRevisionsDescriptions(('\n         Notes from release 201312090000Z,\n         (1) Added new object: f3DataExportClearStatsAction\n         Notes from release 201310310000Z,\n         (1) MIB version ready for release FSP150CC 6.1.CC.',))
if mibBuilder.loadTexts: f3DataExportMIB.setLastUpdated('201310310000Z')
if mibBuilder.loadTexts: f3DataExportMIB.setOrganization('ADVA Optical Networking')
if mibBuilder.loadTexts: f3DataExportMIB.setContactInfo('        Marek Romaniuk\n                     ADVA Optical Networking, Inc.\n                Tel: +48 58 7716 414\n             E-mail: mromaniuk@advaoptical.com\n             Postal: ul. Slaska 35/37\n                     81-310 Gdynia, Poland')
if mibBuilder.loadTexts: f3DataExportMIB.setDescription('This module defines the Data Export MIB definitions \n             used by the F3 (FSP150CM/CC) product lines.\n             Copyright (C) ADVA Optical Networking.')
f3DataExportConfigObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 30, 1))
f3DataExportCounterObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 30, 2))
f3DataExportActionObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 30, 3))
f3DataExportConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 30, 4))
class DataExportType(TextualConvention, Bits):
    description = 'Data Export Types.'
    status = 'current'
    namedValues = NamedValues(("esal3pm", 1), ("twamppm", 2), ("flowbyteratepm", 3))

f3DataExportTypes = MibScalar((1, 3, 6, 1, 4, 1, 2544, 1, 12, 30, 1, 1), DataExportType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3DataExportTypes.setStatus('current')
if mibBuilder.loadTexts: f3DataExportTypes.setDescription(' This object provides ability to set data export types.')
f3DataExportReportInterval = MibScalar((1, 3, 6, 1, 4, 1, 2544, 1, 12, 30, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 60))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3DataExportReportInterval.setStatus('current')
if mibBuilder.loadTexts: f3DataExportReportInterval.setDescription(' This object provides ability to set interval value (in seconds).')
f3DataExportIpVersion = MibScalar((1, 3, 6, 1, 4, 1, 2544, 1, 12, 30, 1, 3), IpVersion()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3DataExportIpVersion.setStatus('current')
if mibBuilder.loadTexts: f3DataExportIpVersion.setDescription(' This object provides ability to set version of IP protocol.')
f3DataExportServerIpv4Addr = MibScalar((1, 3, 6, 1, 4, 1, 2544, 1, 12, 30, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3DataExportServerIpv4Addr.setStatus('current')
if mibBuilder.loadTexts: f3DataExportServerIpv4Addr.setDescription(' This object provides ability to set IPv4 FTP server address.')
f3DataExportServerIpv6Addr = MibScalar((1, 3, 6, 1, 4, 1, 2544, 1, 12, 30, 1, 5), Ipv6Address()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3DataExportServerIpv6Addr.setStatus('current')
if mibBuilder.loadTexts: f3DataExportServerIpv6Addr.setDescription(' This object provides ability to set IPv6 FTP server address.')
f3DataExportUserName = MibScalar((1, 3, 6, 1, 4, 1, 2544, 1, 12, 30, 1, 6), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3DataExportUserName.setStatus('current')
if mibBuilder.loadTexts: f3DataExportUserName.setDescription(' This object provides ability to set transfer protocol user login.')
f3DataExportPassword = MibScalar((1, 3, 6, 1, 4, 1, 2544, 1, 12, 30, 1, 7), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3DataExportPassword.setStatus('current')
if mibBuilder.loadTexts: f3DataExportPassword.setDescription(' This object provides ability to set transfer protocol user password. \n           Reading this object will return an empty string if the password \n           has not been set or ***** if the password has been set.')
f3DataExportPath = MibScalar((1, 3, 6, 1, 4, 1, 2544, 1, 12, 30, 1, 8), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3DataExportPath.setStatus('current')
if mibBuilder.loadTexts: f3DataExportPath.setDescription(' This object provides ability to set remote path to place file.')
f3DataExportConfigObjectTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 1, 12, 30, 1, 9), )
if mibBuilder.loadTexts: f3DataExportConfigObjectTable.setStatus('current')
if mibBuilder.loadTexts: f3DataExportConfigObjectTable.setDescription('This table allows configuration of the object which need export data.')
f3DataExportConfigObjectEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 1, 12, 30, 1, 9, 1), ).setIndexNames((0, "F3-DATAEXPORT-MIB", "f3DataExportConfigObjectEntity"))
if mibBuilder.loadTexts: f3DataExportConfigObjectEntry.setStatus('current')
if mibBuilder.loadTexts: f3DataExportConfigObjectEntry.setDescription('A conceptual row in the f3DataExportConfigObjectTable.')
f3DataExportConfigObjectEntity = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 30, 1, 9, 1, 1), VariablePointer())
if mibBuilder.loadTexts: f3DataExportConfigObjectEntity.setStatus('current')
if mibBuilder.loadTexts: f3DataExportConfigObjectEntity.setDescription('The object value need export data.')
f3DataExportConfigObjectStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 30, 1, 9, 1, 2), StorageType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3DataExportConfigObjectStorageType.setStatus('current')
if mibBuilder.loadTexts: f3DataExportConfigObjectStorageType.setDescription('The type of storage configured for this entry.')
f3DataExportConfigObjectRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 30, 1, 9, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3DataExportConfigObjectRowStatus.setStatus('current')
if mibBuilder.loadTexts: f3DataExportConfigObjectRowStatus.setDescription('The status of this row.\n          \tAn entry MUST NOT exist in the active state unless all\n          \tobjects in the entry have an appropriate value, as described\n          \tin the description clause for each writable object.\n \t\n          \tThe values of f3DataExportConfigObjectRowStatus supported are\n          \tcreateAndGo(4) and destroy(6).  All mandatory attributes\n          \tmust be specified in a single SNMP SET request with\n          \tf3DataExportConfigObjectRowStatus value as createAndGo(4).\n          \tUpon successful row creation, this object has a\n          \tvalue of active(1).\n \t\n          \tThe f3DataExportConfigObjectRowStatus object may be modified if\n          \tthe associated instance of this object is equal to active(1).')
f3DataExportServerXferPass = MibScalar((1, 3, 6, 1, 4, 1, 2544, 1, 12, 30, 2, 1), PerfCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3DataExportServerXferPass.setStatus('current')
if mibBuilder.loadTexts: f3DataExportServerXferPass.setDescription(' Counter for successful PM export')
f3DataExportServerXferFail = MibScalar((1, 3, 6, 1, 4, 1, 2544, 1, 12, 30, 2, 2), PerfCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3DataExportServerXferFail.setStatus('current')
if mibBuilder.loadTexts: f3DataExportServerXferFail.setDescription(' Counter for failure PM export.')
f3DataExportClearStatsAction = MibScalar((1, 3, 6, 1, 4, 1, 2544, 1, 12, 30, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("not-applicable", 0), ("clear", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3DataExportClearStatsAction.setStatus('current')
if mibBuilder.loadTexts: f3DataExportClearStatsAction.setDescription('Initiates a data export action. \n             This object is write only.\n             Supported actions are:\n             clear(1) - Clear Data Export Stats.')
f3DataExportCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 30, 4, 1))
f3DataExportGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 30, 4, 2))
f3DataExportCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2544, 1, 12, 30, 4, 1, 1)).setObjects(("F3-DATAEXPORT-MIB", "f3DataExportConfigGroup"), ("F3-DATAEXPORT-MIB", "f3DataExportCounterGroup"), ("F3-DATAEXPORT-MIB", "f3DataExportActionGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3DataExportCompliance = f3DataExportCompliance.setStatus('current')
if mibBuilder.loadTexts: f3DataExportCompliance.setDescription('Describes the requirements for conformance to the F3-DATAEXPORT-MIB compilance.')
f3DataExportConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2544, 1, 12, 30, 4, 2, 1)).setObjects(("F3-DATAEXPORT-MIB", "f3DataExportTypes"), ("F3-DATAEXPORT-MIB", "f3DataExportReportInterval"), ("F3-DATAEXPORT-MIB", "f3DataExportIpVersion"), ("F3-DATAEXPORT-MIB", "f3DataExportServerIpv4Addr"), ("F3-DATAEXPORT-MIB", "f3DataExportServerIpv6Addr"), ("F3-DATAEXPORT-MIB", "f3DataExportUserName"), ("F3-DATAEXPORT-MIB", "f3DataExportPassword"), ("F3-DATAEXPORT-MIB", "f3DataExportPath"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3DataExportConfigGroup = f3DataExportConfigGroup.setStatus('current')
if mibBuilder.loadTexts: f3DataExportConfigGroup.setDescription('A collection of objects used to manage the Data Export.')
f3DataExportCounterGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2544, 1, 12, 30, 4, 2, 2)).setObjects(("F3-DATAEXPORT-MIB", "f3DataExportServerXferPass"), ("F3-DATAEXPORT-MIB", "f3DataExportServerXferFail"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3DataExportCounterGroup = f3DataExportCounterGroup.setStatus('current')
if mibBuilder.loadTexts: f3DataExportCounterGroup.setDescription('A collection of Data Export counter objects.')
f3DataExportActionGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2544, 1, 12, 30, 4, 2, 3)).setObjects(("F3-DATAEXPORT-MIB", "f3DataExportClearStatsAction"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3DataExportActionGroup = f3DataExportActionGroup.setStatus('current')
if mibBuilder.loadTexts: f3DataExportActionGroup.setDescription('A collection of Data Export action objects.')
mibBuilder.exportSymbols("F3-DATAEXPORT-MIB", f3DataExportActionObjects=f3DataExportActionObjects, f3DataExportServerXferPass=f3DataExportServerXferPass, f3DataExportConfigObjects=f3DataExportConfigObjects, f3DataExportConfigObjectEntity=f3DataExportConfigObjectEntity, f3DataExportConfigObjectRowStatus=f3DataExportConfigObjectRowStatus, f3DataExportIpVersion=f3DataExportIpVersion, f3DataExportPassword=f3DataExportPassword, f3DataExportActionGroup=f3DataExportActionGroup, f3DataExportServerIpv4Addr=f3DataExportServerIpv4Addr, f3DataExportGroups=f3DataExportGroups, f3DataExportMIB=f3DataExportMIB, f3DataExportServerIpv6Addr=f3DataExportServerIpv6Addr, DataExportType=DataExportType, f3DataExportTypes=f3DataExportTypes, f3DataExportConfigGroup=f3DataExportConfigGroup, f3DataExportCompliances=f3DataExportCompliances, f3DataExportServerXferFail=f3DataExportServerXferFail, f3DataExportConfigObjectStorageType=f3DataExportConfigObjectStorageType, f3DataExportConformance=f3DataExportConformance, f3DataExportCompliance=f3DataExportCompliance, f3DataExportCounterGroup=f3DataExportCounterGroup, f3DataExportCounterObjects=f3DataExportCounterObjects, f3DataExportClearStatsAction=f3DataExportClearStatsAction, f3DataExportReportInterval=f3DataExportReportInterval, f3DataExportUserName=f3DataExportUserName, PYSNMP_MODULE_ID=f3DataExportMIB, f3DataExportPath=f3DataExportPath, f3DataExportConfigObjectTable=f3DataExportConfigObjectTable, f3DataExportConfigObjectEntry=f3DataExportConfigObjectEntry)
