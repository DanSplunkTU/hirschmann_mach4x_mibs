#
# PySNMP MIB module WISI-GTMODULES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/wisi/WISI-GTMODULES-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 18:21:57 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Gauge32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, IpAddress, Bits, TimeTicks, MibIdentifier, ModuleIdentity, Integer32, Unsigned32, Counter32, NotificationType, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "IpAddress", "Bits", "TimeTicks", "MibIdentifier", "ModuleIdentity", "Integer32", "Unsigned32", "Counter32", "NotificationType", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
gtUnit, = mibBuilder.importSymbols("WISI-TANGRAM-MIB", "gtUnit")
gtModulesMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2))
gtModulesMIB.setRevisions(('2016-09-08 00:00', '2016-06-08 00:00', '2015-06-16 00:00', '2013-07-29 00:00', '2013-06-26 00:00', '2012-10-31 00:00', '2011-12-13 00:00', '2011-09-08 00:00', '2011-04-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: gtModulesMIB.setRevisionsDescriptions(('Added gtModuleReboot to gtModulesTable. Made module power\n\t\ta writeable enumerated value. Updated contact information.', 'Renamed scalar gtModuleSlot to avoid clash with gtModuleTable column.', 'Changes: \tAdded FWIDUploaded to gtModulesTable..', 'Changes: Added module status for N+1 redundancy to table gtModulesTable', 'Changes: Added notifications for N+1 redundancy and module status used in GT11.', 'Changes: Added inputs and outputs list.', 'Changes: Updated MIBs to revision 11 for AixSolve (GT22).', 'Updated representation of versions.', 'Initial version.',))
if mibBuilder.loadTexts: gtModulesMIB.setLastUpdated('201609080000Z')
if mibBuilder.loadTexts: gtModulesMIB.setOrganization('WISI Communications GmbH & Co. KG')
if mibBuilder.loadTexts: gtModulesMIB.setContactInfo('https://wisiconnect.tv/')
if mibBuilder.loadTexts: gtModulesMIB.setDescription('This MIB module represents the modules within a system (rack\n\t\tunit) of a WISI next-generation headend. It provides general\n\t\tmodule information, such as the hardware or firmware ID as well\n\t\tas an unique serial number.')
gtModulesNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 0))
gtModulesObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 1))
gtModulesConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 2))
gtModulesCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 2, 1))
gtModulesGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 2, 2))
gtModulesNotifyPlugin = NotificationType((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 0, 1))
if mibBuilder.loadTexts: gtModulesNotifyPlugin.setStatus('current')
if mibBuilder.loadTexts: gtModulesNotifyPlugin.setDescription('The gtModulesNotifyPlugin notification indicates that\n\t    a new SFM/MFM module has been plugged in the GT01/GN50 rack unit.')
gtModulesNotifyPlugout = NotificationType((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 0, 2))
if mibBuilder.loadTexts: gtModulesNotifyPlugout.setStatus('current')
if mibBuilder.loadTexts: gtModulesNotifyPlugout.setDescription('The gtModulesNotifyPlugout notification indicates that\n\t    an SFM/MFM module has been plugged out of the GT01/GN50 rack unit.')
gtModulesNotifyFailure = NotificationType((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 0, 3))
if mibBuilder.loadTexts: gtModulesNotifyFailure.setStatus('current')
if mibBuilder.loadTexts: gtModulesNotifyFailure.setDescription('The gtModulesNotifyFailure notification indicates that\n\t    GT11 has status failure detected on SFM/MFM module')
gtModulesNotifyRedundancy = NotificationType((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 0, 4))
if mibBuilder.loadTexts: gtModulesNotifyRedundancy.setStatus('current')
if mibBuilder.loadTexts: gtModulesNotifyRedundancy.setDescription('The gtModulesNotifyRedundancy notification indicates that\n\t    GT11 has replaced a faulty SFM/MFM module with reserved SFM/MFM module')
gtModulesNotifyRedundancyClear = NotificationType((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 0, 5))
if mibBuilder.loadTexts: gtModulesNotifyRedundancyClear.setStatus('current')
if mibBuilder.loadTexts: gtModulesNotifyRedundancyClear.setDescription('The gtModulesNotifyRedundancyClear notification indicates that\n\t    GT11 has replaces the SFM/MFM reserve module with a new SFM/MFM master module')
gtModulesNotifyFailureClear = NotificationType((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 0, 6))
if mibBuilder.loadTexts: gtModulesNotifyFailureClear.setStatus('current')
if mibBuilder.loadTexts: gtModulesNotifyFailureClear.setDescription('The gtModulesNotifyFailureClear notification indicates that\n\t    GT11 has status failure cleared detected on SFM/MFM module')
gtThisModuleSlot = MibScalar((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: gtThisModuleSlot.setStatus('current')
if mibBuilder.loadTexts: gtThisModuleSlot.setDescription('The gtThisModuleSlot entity represents the slot where the\n\t\tagent module is plugged in.')
gtNumModules = MibScalar((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: gtNumModules.setStatus('current')
if mibBuilder.loadTexts: gtNumModules.setDescription('The gtNumModules entity represents the number of\n\t\tSFM/MFM modules within the GT01/GN50 rack unit.\n\t\tThe related entries are provided by gtModulesTable.')
gtModulesTable = MibTable((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 1, 3), )
if mibBuilder.loadTexts: gtModulesTable.setStatus('current')
if mibBuilder.loadTexts: gtModulesTable.setDescription('The gtModulesTable table contains a list of all\n\t\tSFM/MFM modules within the GT01/GN50 rack unit.\n\t\tThe number of entries is provided by gtNumModules.')
gtModulesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 1, 3, 1), ).setIndexNames((0, "WISI-GTMODULES-MIB", "gtModule"))
if mibBuilder.loadTexts: gtModulesEntry.setStatus('current')
if mibBuilder.loadTexts: gtModulesEntry.setDescription('The gtModulesEntry table entry represents a\n\t\tSFM/MFM module within the GT01/GN50 rack unit.\n\t\tThe number of entries is provided by gtNumModules.')
gtModule = MibTableColumn((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 1, 3, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 15)))
if mibBuilder.loadTexts: gtModule.setStatus('current')
if mibBuilder.loadTexts: gtModule.setDescription('The gtModule entity represents the numeric index\n\t\tof a SFM/MFM module within the GT01/GN50 rack unit.')
gtModuleName = MibTableColumn((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 1, 3, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gtModuleName.setStatus('current')
if mibBuilder.loadTexts: gtModuleName.setDescription('The gtModule entity represents the symbolic index\n\t\tof a SFM/MFM module within the GT01/GN50 rack unit.')
gtModuleHWID = MibTableColumn((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 1, 3, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gtModuleHWID.setStatus('current')
if mibBuilder.loadTexts: gtModuleHWID.setDescription('The gtModule entity represents the hardware revision\n\t\tof a SFM/MFM module within the GT01/GN50 rack unit.\n\t\tHWID := Major.PCB.BOM.Rework')
gtModuleFWID = MibTableColumn((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 1, 3, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gtModuleFWID.setStatus('current')
if mibBuilder.loadTexts: gtModuleFWID.setDescription('The gtModule entity represents the firmware revision\n\t\tof a SFM/MFM module within the GT01/GN50 rack unit.')
gtModuleSerNo = MibTableColumn((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 1, 3, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gtModuleSerNo.setStatus('current')
if mibBuilder.loadTexts: gtModuleSerNo.setDescription('The gtModule entity represents the unique serial number\n\t\tof a SFM/MFM module within the GT01/GN50 rack unit.\n\t\tSerNo := DDDOPYYMMDDSSSSS, whereby DDD = Device ID,\n\t\tO = OEM code, P = production place, YYMMDD = year-month-day,\n\t\tSSSSS = serial number during a day.')
gtModuleUptime = MibTableColumn((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 1, 3, 1, 6), Counter32()).setUnits('s').setMaxAccess("readonly")
if mibBuilder.loadTexts: gtModuleUptime.setStatus('current')
if mibBuilder.loadTexts: gtModuleUptime.setDescription('The gtModule entity represents the current uptime\n\t\tof a SFM/MFM module within the GT01/GN50 rack unit.')
gtModuleLifetime = MibTableColumn((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 1, 3, 1, 7), Counter32()).setUnits('s').setMaxAccess("readonly")
if mibBuilder.loadTexts: gtModuleLifetime.setStatus('current')
if mibBuilder.loadTexts: gtModuleLifetime.setDescription('The gtModule entity represents the accumulated lifetime\n\t\tof a SFM/MFM module within the GT01/GN50 rack unit.')
gtModulePower = MibTableColumn((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 1, 3, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("off", 0), ("on", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gtModulePower.setStatus('current')
if mibBuilder.loadTexts: gtModulePower.setDescription('The gtModule entity represents the current power state\n\t\tof a SFM/MFM module within the GT01/GN50 rack unit.')
gtModuleMode = MibTableColumn((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 1, 3, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gtModuleMode.setStatus('current')
if mibBuilder.loadTexts: gtModuleMode.setDescription('The gtModule entity represents the current N+1 redundancy mode\n\t\tof a SFM/MFM module within the GT01/GN50 rack unit.')
gtModuleStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 1, 3, 1, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gtModuleStatus.setStatus('current')
if mibBuilder.loadTexts: gtModuleStatus.setDescription('The gtModule entity represents the current status\n\t\tof a SFM/MFM module within the GT01/GN50 rack unit.')
gtModuleSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 1, 3, 1, 11), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: gtModuleSlot.setStatus('deprecated')
if mibBuilder.loadTexts: gtModuleSlot.setDescription('The gtModule entity represents the slot id\n\t\tof a SFM/MFM module within the GT01/GN50 rack unit.')
gtModuleFWIDUploaded = MibTableColumn((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 1, 3, 1, 12), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gtModuleFWIDUploaded.setStatus('current')
if mibBuilder.loadTexts: gtModuleFWIDUploaded.setDescription('The gtModule entity represents the uploaded firmware revision\n\t\tof a SFM/MFM module within the GT01/GN50 rack unit.')
gtModuleReboot = MibTableColumn((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 1, 3, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("running", 0), ("reboot", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gtModuleReboot.setStatus('current')
if mibBuilder.loadTexts: gtModuleReboot.setDescription('The gtModuleReboot entity can be used to reboot an SFM/MFM\n\t\tmodule within the GT01/GN50 rack unit. During normal\n\t\toperations, reading this object will return a value of\n\t\trunning(0) and writing a value of reboot(1) to it will cause\n\t\tthe module to reboot.')
gtNumCapabilities = MibScalar((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: gtNumCapabilities.setStatus('current')
if mibBuilder.loadTexts: gtNumCapabilities.setDescription('The gtNumCapabilities entity represents the number of\n\t\tstreaming capabilites within the GT01/GN50 rack unit.\n\t\tThe related entries are provided by gtModulesTable.')
gtCapabilitiesTable = MibTable((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 1, 5), )
if mibBuilder.loadTexts: gtCapabilitiesTable.setStatus('current')
if mibBuilder.loadTexts: gtCapabilitiesTable.setDescription('The gtCapabilitiesTable table contains a list of all\n\t\tstreaming capabilites within the GT01/GN50 rack unit.\n\t\tThe number of entries is provided by gtNumCapabilities.')
gtCapabilitiesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 1, 5, 1), ).setIndexNames((0, "WISI-GTMODULES-MIB", "gtModule"), (0, "WISI-GTMODULES-MIB", "gtChannel"), (0, "WISI-GTMODULES-MIB", "gtCapability"))
if mibBuilder.loadTexts: gtCapabilitiesEntry.setStatus('current')
if mibBuilder.loadTexts: gtCapabilitiesEntry.setDescription('The gtCapabilitiesEntry table entry represents a\n\t\tstreaming capability within the GT01/GN50 rack unit.\n\t\tThe number of entries is provided by gtNumCapabilities.')
gtChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 1, 5, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4095)))
if mibBuilder.loadTexts: gtChannel.setStatus('current')
if mibBuilder.loadTexts: gtChannel.setDescription('The gtChannel entity represents the numeric index\n\t\tof a streaming capability within the GT01/GN50 rack unit.')
gtCapability = MibTableColumn((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 1, 5, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: gtCapability.setStatus('current')
if mibBuilder.loadTexts: gtCapability.setDescription('The gtCapability entity represents the numeric index\n\t\tof a streaming capability within the GT01/GN50 rack unit.')
gtInputsTable = MibTable((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 1, 7), )
if mibBuilder.loadTexts: gtInputsTable.setStatus('current')
if mibBuilder.loadTexts: gtInputsTable.setDescription('The gtInputsTable table contains a list of all\n\t\tinputs on a SFM/MFM module.')
gtInputsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 1, 7, 1), ).setIndexNames((0, "WISI-GTMODULES-MIB", "gtModule"), (0, "WISI-GTMODULES-MIB", "gtInputsTableIdx"))
if mibBuilder.loadTexts: gtInputsEntry.setStatus('current')
if mibBuilder.loadTexts: gtInputsEntry.setDescription('The gtInputsEntry table entry represents an\n\t\tinput on a SFM/MFM module.')
gtInputsTableIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 1, 7, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 256)))
if mibBuilder.loadTexts: gtInputsTableIdx.setStatus('current')
if mibBuilder.loadTexts: gtInputsTableIdx.setDescription('The gtInputsTableIdx entity represents the numeric index\n\t\tof an input on a SFM/MFM module.')
gtInputChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 1, 7, 1, 2), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gtInputChannel.setStatus('current')
if mibBuilder.loadTexts: gtInputChannel.setDescription('The gtInputChannel referer to the settings table specific\n                to the current type of input on a SFM/MFM module.')
gtInputName = MibTableColumn((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 1, 7, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gtInputName.setStatus('current')
if mibBuilder.loadTexts: gtInputName.setDescription('The gtInputName entity represents the descriptive name\n\t\tof an input on a SFM/MFM module.')
gtOutputsTable = MibTable((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 1, 8), )
if mibBuilder.loadTexts: gtOutputsTable.setStatus('current')
if mibBuilder.loadTexts: gtOutputsTable.setDescription('The gtOutputsTable table contains a list of all\n\t\toutputs on a SFM/MFM module.')
gtOutputsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 1, 8, 1), ).setIndexNames((0, "WISI-GTMODULES-MIB", "gtModule"), (0, "WISI-GTMODULES-MIB", "gtOutputsTableIdx"))
if mibBuilder.loadTexts: gtOutputsEntry.setStatus('current')
if mibBuilder.loadTexts: gtOutputsEntry.setDescription('The gtOutputsEntry table entry represents an\n\t\toutput on a SFM/MFM module.')
gtOutputsTableIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 1, 8, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 256)))
if mibBuilder.loadTexts: gtOutputsTableIdx.setStatus('current')
if mibBuilder.loadTexts: gtOutputsTableIdx.setDescription('The gtOutputsTableIdx entity represents the numeric index\n\t\tof an output on a SFM/MFM module.')
gtOutputChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 1, 8, 1, 2), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gtOutputChannel.setStatus('current')
if mibBuilder.loadTexts: gtOutputChannel.setDescription('The gtOutputChannel referer to the settings table specific\n                to the current type of output on a SFM/MFM module.')
gtOutputName = MibTableColumn((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 1, 8, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gtOutputName.setStatus('current')
if mibBuilder.loadTexts: gtOutputName.setDescription('The gtOutputName entity represents the descriptive name\n\t\tof an output on a SFM/MFM module.')
gtModulesMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 2, 1, 1)).setObjects(("WISI-GTMODULES-MIB", "gtModulesV1Group"), ("WISI-GTMODULES-MIB", "gtModulesSystemGroup"), ("WISI-GTMODULES-MIB", "gtModulesStatsGroup"), ("WISI-GTMODULES-MIB", "gtModulesTrapGroup"), ("WISI-GTMODULES-MIB", "gtModulesSetGroup"), ("WISI-GTMODULES-MIB", "gtModulesBasicNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    gtModulesMIBCompliance = gtModulesMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: gtModulesMIBCompliance.setDescription('The compliance statement for GTMODULESv2 entities\n\t\twhich implement the GTMODULESv2 MIB.')
gtModulesV1Group = ObjectGroup((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 2, 2, 1)).setObjects(("WISI-GTMODULES-MIB", "gtThisModuleSlot"), ("WISI-GTMODULES-MIB", "gtNumModules"), ("WISI-GTMODULES-MIB", "gtModuleName"), ("WISI-GTMODULES-MIB", "gtModuleHWID"), ("WISI-GTMODULES-MIB", "gtModuleFWID"), ("WISI-GTMODULES-MIB", "gtModuleSerNo"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    gtModulesV1Group = gtModulesV1Group.setStatus('current')
if mibBuilder.loadTexts: gtModulesV1Group.setDescription('The gtModulesV1Group group is mandatory only for those\n\t\tGTMODULESv2 entities which also implement GTMODULESv1.')
gtModulesSystemGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 2, 2, 2)).setObjects(("WISI-GTMODULES-MIB", "gtThisModuleSlot"), ("WISI-GTMODULES-MIB", "gtNumModules"), ("WISI-GTMODULES-MIB", "gtModuleName"), ("WISI-GTMODULES-MIB", "gtModuleHWID"), ("WISI-GTMODULES-MIB", "gtModuleFWID"), ("WISI-GTMODULES-MIB", "gtModuleSerNo"), ("WISI-GTMODULES-MIB", "gtCapability"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    gtModulesSystemGroup = gtModulesSystemGroup.setStatus('current')
if mibBuilder.loadTexts: gtModulesSystemGroup.setDescription('The gtModulesSystemGroup group defines GTMODULESv2 entities\n\t\twhich are mandatory.')
gtModulesStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 2, 2, 3)).setObjects(("WISI-GTMODULES-MIB", "gtNumModules"), ("WISI-GTMODULES-MIB", "gtModuleUptime"), ("WISI-GTMODULES-MIB", "gtModuleLifetime"), ("WISI-GTMODULES-MIB", "gtNumCapabilities"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    gtModulesStatsGroup = gtModulesStatsGroup.setStatus('current')
if mibBuilder.loadTexts: gtModulesStatsGroup.setDescription('The gtModulesStatsGroup group defines GTMODULESv2 entities\n\t\twhich provide statistical information.')
gtModulesTrapGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 2, 2, 4))
gtModulesSetGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 2, 2, 5))
gtModulesBasicNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 2, 2, 6)).setObjects(("WISI-GTMODULES-MIB", "gtModulesNotifyPlugin"), ("WISI-GTMODULES-MIB", "gtModulesNotifyPlugout"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    gtModulesBasicNotificationsGroup = gtModulesBasicNotificationsGroup.setStatus('current')
if mibBuilder.loadTexts: gtModulesBasicNotificationsGroup.setDescription('The gtModulesBasicNotificationsGroup group defines\n\t\tGTMODULESv2 notification objects which are mandatory.')
mibBuilder.exportSymbols("WISI-GTMODULES-MIB", gtModulesCompliances=gtModulesCompliances, gtModulesNotifyPlugout=gtModulesNotifyPlugout, gtModulesObjects=gtModulesObjects, gtModuleHWID=gtModuleHWID, gtModuleSlot=gtModuleSlot, gtModulesNotifyFailureClear=gtModulesNotifyFailureClear, gtModulesMIB=gtModulesMIB, gtModulePower=gtModulePower, gtModuleFWIDUploaded=gtModuleFWIDUploaded, gtModuleSerNo=gtModuleSerNo, gtCapability=gtCapability, gtOutputsTableIdx=gtOutputsTableIdx, gtModulesV1Group=gtModulesV1Group, gtModulesSystemGroup=gtModulesSystemGroup, gtModulesBasicNotificationsGroup=gtModulesBasicNotificationsGroup, gtInputsTable=gtInputsTable, gtNumCapabilities=gtNumCapabilities, gtOutputName=gtOutputName, gtThisModuleSlot=gtThisModuleSlot, gtModulesNotifyPlugin=gtModulesNotifyPlugin, gtNumModules=gtNumModules, gtCapabilitiesEntry=gtCapabilitiesEntry, gtModulesEntry=gtModulesEntry, gtModuleMode=gtModuleMode, PYSNMP_MODULE_ID=gtModulesMIB, gtModuleName=gtModuleName, gtOutputsTable=gtOutputsTable, gtModuleUptime=gtModuleUptime, gtOutputChannel=gtOutputChannel, gtInputsTableIdx=gtInputsTableIdx, gtModuleReboot=gtModuleReboot, gtModulesNotifyRedundancy=gtModulesNotifyRedundancy, gtModulesGroups=gtModulesGroups, gtModuleFWID=gtModuleFWID, gtModulesNotifyRedundancyClear=gtModulesNotifyRedundancyClear, gtModulesTrapGroup=gtModulesTrapGroup, gtInputChannel=gtInputChannel, gtOutputsEntry=gtOutputsEntry, gtModulesNotifications=gtModulesNotifications, gtInputsEntry=gtInputsEntry, gtModulesStatsGroup=gtModulesStatsGroup, gtModuleLifetime=gtModuleLifetime, gtModulesSetGroup=gtModulesSetGroup, gtChannel=gtChannel, gtModulesTable=gtModulesTable, gtModule=gtModule, gtCapabilitiesTable=gtCapabilitiesTable, gtModulesConformance=gtModulesConformance, gtModulesMIBCompliance=gtModulesMIBCompliance, gtModuleStatus=gtModuleStatus, gtInputName=gtInputName, gtModulesNotifyFailure=gtModulesNotifyFailure)
