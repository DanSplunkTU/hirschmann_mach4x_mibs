#
# PySNMP MIB module AT-SETUP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/allied/AT-SETUP-MIB
# Produced by pysmi-1.1.8 at Sun Jan 16 00:31:37 2022
# On host fv-az42-839 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
modules, = mibBuilder.importSymbols("AT-SMI-MIB", "modules")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, Integer32, ObjectIdentity, Unsigned32, IpAddress, NotificationType, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, TimeTicks, Bits, iso, Counter64, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Integer32", "ObjectIdentity", "Unsigned32", "IpAddress", "NotificationType", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "TimeTicks", "Bits", "iso", "Counter64", "Counter32")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
setup = ModuleIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500))
setup.setRevisions(('2014-04-30 00:00', '2013-10-14 00:00', '2012-09-21 00:00', '2010-11-20 00:00', '2010-10-08 00:00', '2010-09-10 00:00', '2010-09-08 00:00', '2010-06-15 00:15', '2010-04-09 00:00', '2008-10-02 00:00', '2008-09-30 00:00', '2008-09-24 00:00', '2008-05-21 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: setup.setRevisionsDescriptions(('Updated decriptions to refer to chassisMappingTable', 'Added new requirement to the objects nextBootLastSetResult and backupLastSetResult,\n                as to check for the existence of a valid release license on the device. If a valid license\n                is not found then these objects will give an appropriate error message.', 'Added chassis switch (e.g. SBx8100) descriptions to stack-related MIB objects', 'Addition of new objects to support system file operations on\n                stacked devices.', 'Minor changes to help messages.', 'Generic syntax tidy up.', 'Added backupConfig object. The nextBootPath and bootcnfgPath objects will\n                now accept a file stored in card:. The nextBootPath object will only accept\n                a file on card if this is supported by the bootloader.', 'MIB revision history dates in descriptions updated.', 'A set to the runCnfgSaveAs object will now be immediately responded before\n                the actual saving operation starts. This prevents the request from being\n                timed out while the saving is still progressing. A new object\n                runCnfgSaveAsStatus is defined which can be polled to obtain the status of\n                the current/previous saving operation.', 'Added support for obtaining GUI applet version information.', 'Add branch serviceConfig.', 'Moved file copy branch to the new AT-FILEv2 MIB.\n                Allowed clearing of currentFirmware, nextBootFirmware and nextBootConfig\n                by setting the path objects with an empty string.', 'Initial revision.',))
if mibBuilder.loadTexts: setup.setLastUpdated('201404300000Z')
if mibBuilder.loadTexts: setup.setOrganization('Allied Telesis, Inc.')
if mibBuilder.loadTexts: setup.setContactInfo('http://www.alliedtelesis.com')
if mibBuilder.loadTexts: setup.setDescription('The AT Setup MIB for managing the software installation and\n                configuration files.')
class SystemFileOperationType(TextualConvention, Integer32):
    description = 'Indicates the current status of an attempt to modify a system\n                file setting.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("idle", 1), ("success", 2), ("failure", 3), ("saving", 4), ("syncing", 5))

restartDevice = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: restartDevice.setStatus('deprecated')
if mibBuilder.loadTexts: restartDevice.setDescription('This object forces a standalone unit or stack of devices to\n                restart immediately when set with a value of 1. For a chassis\n                switch, this object causes the whole chassis to restart\n                immediately. Reading the object will always return zero.\n                \n                NOTE: This object has been replaced by the\n                restartStkMemberDevice object.')
restartStkMemberDevice = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: restartStkMemberDevice.setStatus('current')
if mibBuilder.loadTexts: restartStkMemberDevice.setDescription("This object causes a specified device to restart immediately.\n                The restart is initiated by setting its value to the device's\n                stack member ID. For a chassis switch, it corresponds to the\n                card ID. For VCStack Plus, 1-12 refers to the cards on VCS\n                stack member 1 and 13-24 refers to the cards on VCS stack\n                member 2. Refer to chassisMappingTable for more details.\n                This object causes the specified card to restart immediately.\n                Setting its value to zero will cause all devices in the stack\n                (or a standalone device) to restart. Reading the object will\n                always return zero.")
firmware = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 2))
currentFirmware = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 2, 1))
currSoftVersion = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 2, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: currSoftVersion.setStatus('current')
if mibBuilder.loadTexts: currSoftVersion.setDescription('The major.minor.interim version of the firmware that the device is\n                currently running. Will return 0 if the version cannot be determined.')
currSoftName = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: currSoftName.setStatus('current')
if mibBuilder.loadTexts: currSoftName.setDescription('The name of the firmware that the device is currently running.')
currSoftSaveAs = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 2, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: currSoftSaveAs.setStatus('deprecated')
if mibBuilder.loadTexts: currSoftSaveAs.setDescription("Set with a filename to save the currently running software to\n                the root of flash. Only one save operation can be executed at a\n                time across all SNMP users, and the filename must not contain\n                whitespace characters.\n\n                Immediately upon executing the set action, the actual firmware\n                save operation will be started and continue on the device until\n                it has completed or a failure occurs.\n\n                Subsequent reads of the object will return one of several\n                results:\n\n                saving x            A saving operation is currently in\n                                    progress. Another save cannot be started\n                                    while the object is returning this value.\n\n                x success           The last save operation was successfully\n                                    completed.\n\n                x failure: [error]  The last save operation failed, due to the\n                                    descriptive message attached. The most\n                                    common failure is lack of disk space.\n\n                idle                There is no save operation in progress and\n                                    a new one may be started.\n\n                Upon reading a success or failure message, the message will be\n                cleared and the next read will result in an 'idle' message. A\n                new save operation can now be executed.\n\n                NOTE: This object has been replaced by objects currSoftSaveToFile,\n                currSoftSaveStatus and currSoftLastSaveResult.")
currSoftSaveToFile = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 2, 1, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: currSoftSaveToFile.setStatus('current')
if mibBuilder.loadTexts: currSoftSaveToFile.setDescription("Set with a URL (e.g. 'flash:/filename.rel' or\n                'card:/filename.rel') to save the currently running software to\n                the root of flash or SD card. Only one save operation can be\n                executed at a time across all SNMP users, and an operation may\n                not be started unless the current value of currSoftSaveStatus\n                is 'idle'. The URL must not contain whitespace characters.\n\n                Immediately upon executing the set action, the actual firmware\n                save operation will be started and continue on the device until\n                it has completed or a failure occurs. The current status of the\n                operation can be determined by reading currSoftSaveStatus, and\n                the result of the last completed operation is indicated by\n                currSoftLastSaveResult.\n                \n                When read, this object will return the URL of the last\n                firmware save operation that was attempted.")
currSoftSaveStatus = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 2, 1, 5), SystemFileOperationType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: currSoftSaveStatus.setStatus('current')
if mibBuilder.loadTexts: currSoftSaveStatus.setDescription("Returns the status of any current operation to store the\n                running software to a release file. The following values may\n                be returned:\n\n                1 (idle)                There is no release file save operation\n                                        in progress.\n\n                2 (success)             The last release file save operation\n                                        completed successfully.\n\n                3 (failure)             The last release file save operation\n                                        failed.\n\n                4 (saving)              A release file save operation is\n                                        currently in progress.\n\n                When a read of this object returns a value of 'success' or\n                'failure', it will immediately be reset to 'idle' and a new\n                operation may be initiated if desired. A detailed description\n                of the last completed operation may be determined by reading\n                currSoftLastSaveResult.")
currSoftLastSaveResult = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 2, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: currSoftLastSaveResult.setStatus('current')
if mibBuilder.loadTexts: currSoftLastSaveResult.setDescription('Gives an indication of the result of the last completed SNMP\n                operation to save the running firmware to a release file.')
nextBootFirmware = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 2, 2))
nextBootVersion = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 2, 2, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nextBootVersion.setStatus('current')
if mibBuilder.loadTexts: nextBootVersion.setDescription('The major.minor.interim version of the firmware that the\n                device is currently set to boot from. Will return 0 if the\n                version cannot be determined.')
nextBootPath = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 2, 2, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nextBootPath.setStatus('current')
if mibBuilder.loadTexts: nextBootPath.setDescription("The full path of the release to be used the next time the\n                device restarts. There is no guarantee that the file\n                referenced exists (i.e. it may have been deleted since the boot\n                path was last set).\n\n                Only one set operation can be executed at a time across all\n                SNMP users, and an operation may not be started unless the\n                current value of nextBootSetStatus is 'idle'. The path must not\n                contain whitespace characters.\n\n                Immediately upon setting this object, the system will attempt\n                to set the new boot path, and the process will continue on the\n                device until it has completed or a failure occurs. The current\n                status of the operation can be determined by reading\n                nextBootSetStatus, and the result of the last completed\n                operation is indicated by nextBootLastSetResult.\n\n                This object can be set with an empty string in order to clear\n                the current boot firmware. Otherwise, the path should be of the\n                form 'flash:/filename.rel' or 'card:/filename.rel'.\n\n                There are several requirements that must be met in order to set\n                a boot release file successfully:\n                - The file must exist.\n                - The file must be in the root of flash (on the active master\n                  in a stacked environment) or card.\n                - The file must not be the same as the currently set backup\n                  release.\n                - The file must have a .rel suffix.\n                - The file must be a valid release file.\n                - In a stacked environment, there must be enough disk space\n                  available to store the release file on each stack member.\n                - The device must have a current release license for the\n                  specified release.")
nextBootSetStatus = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 2, 2, 3), SystemFileOperationType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nextBootSetStatus.setStatus('current')
if mibBuilder.loadTexts: nextBootSetStatus.setDescription("Returns the status of any current operation to set the next\n                boot release file. The following values may be returned:\n\n                1 (idle)                There is no boot release setting\n                                        operation in progress.\n\n                2 (success)             The last boot release setting\n                                        operation completed successfully.\n\n                3 (failure)             The last boot release setting\n                                        operation failed.\n\n                5 (syncing)             A boot release setting operation is\n                                        currently in progress and the file is\n                                        being syncronised across the stack or\n                                        system.\n\n                When a read of this object returns a value of 'success' or\n                'failure', it will immediately be reset to 'idle' and a new\n                operation may be initiated if desired. A detailed description\n                of the last completed operation may be determined by reading\n                nextBootLastSetResult.")
nextBootLastSetResult = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 2, 2, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nextBootLastSetResult.setStatus('current')
if mibBuilder.loadTexts: nextBootLastSetResult.setDescription('Gives an indication of the result of the last completed SNMP\n                operation to set the boot release filename.')
backupFirmware = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 2, 3))
backupVersion = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 2, 3, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: backupVersion.setStatus('current')
if mibBuilder.loadTexts: backupVersion.setDescription('The major.minor.interim version of the firmware that the\n                device will boot from as a backup. This will return 0 if the\n                version cannot be determined.')
backupPath = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 2, 3, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: backupPath.setStatus('current')
if mibBuilder.loadTexts: backupPath.setDescription("The full path of the release file to be used as a backup in\n                the event of the main release file failing to boot. There is no\n                guarantee that the file referenced exists (i.e. it may have\n                been deleted since the backup path was last set).\n\n                Only one set operation can be executed at a time across all\n                SNMP users, and an operation may not be started unless the\n                current value of backupSetStatus is 'idle'. The path must not\n                contain whitespace characters.\n\n                Immediately upon setting this object, the system will attempt\n                to set the new backup path, and the process will continue on\n                the device until it has completed or a failure occurs. The\n                current status of the operation can be determined by reading\n                backupSetStatus, and the result of the last completed operation\n                is indicated by backupLastSetResult.\n\n                This object can be set with an empty string in order to clear\n                the current backup firmware. Otherwise, the path should be of\n                the form 'flash:/filename.rel' or 'card:/filename.rel'.\n\n                There are several requirements that must be met in order to set\n                a backup release file successfully:\n                - The file must exist.\n                - The file must be in the root of flash (on the active master\n                  in a stacked environment) or card.\n                - The file must not be the same as the currently set backup\n                  release.\n                - The file must have a .rel suffix.\n                - The file must be a valid release file.\n                - In a stacked environment, there must be enough disk space\n                  available to store the release file on each stack member.\n                - The device must have a current release license for the\n                  specified release.")
backupSetStatus = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 2, 3, 3), SystemFileOperationType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: backupSetStatus.setStatus('current')
if mibBuilder.loadTexts: backupSetStatus.setDescription("Returns the status of any current operation to set the backup\n                boot release file. The following values may be returned:\n\n                1 (idle)                There is no backup boot release setting\n                                        operation in progress.\n\n                2 (success)             The last backup boot release setting\n                                        operation completed successfully.\n\n                3 (failure)             The last backup boot release setting\n                                        operation failed.\n\n                5 (syncing)             A backup boot release setting operation\n                                        is currently in progress and the file\n                                        is being syncronised across the stack\n                                        or system.\n\n                When a read of this object returns a value of 'success' or\n                'failure', it will immediately be reset to 'idle' and a new\n                operation may be initiated if desired. A detailed description\n                of the last completed operation may be determined by reading\n                backupLastSetResult.")
backupLastSetResult = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 2, 3, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: backupLastSetResult.setStatus('current')
if mibBuilder.loadTexts: backupLastSetResult.setDescription('Gives an indication of the result of the last completed SNMP\n                operation to set the backup boot release filename.')
deviceConfiguration = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 3))
runningConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 3, 1))
runCnfgSaveAs = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 3, 1, 1), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: runCnfgSaveAs.setStatus('current')
if mibBuilder.loadTexts: runCnfgSaveAs.setDescription("Set with a URL to save the running configuration to the flash\n                or card filesystem using that filename (e.g.\n                'flash:/myconfig.cfg' or 'card:/myconfig.cfg').\n                \n                Only one set operation can be executed at a time across all\n                SNMP users, and an operation may not be started unless the\n                current value of runCnfgSaveAsStatus is 'idle'. The URL must\n                not contain whitespace characters.\n                \n                Immediately upon setting this object, the system will attempt\n                to save the running configuration, and the process will\n                continue on the device until it has completed or a failure\n                occurs. The current status of the operation can be determined\n                by reading runCnfgSaveAsStatus, and the result of the last\n                completed operation is indicated by runCnfgLastSaveResult.\n            \n                When read, this object will return the URL of the last\n                configuration save operation that was attempted.")
runCnfgSaveAsStatus = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 3, 1, 2), SystemFileOperationType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: runCnfgSaveAsStatus.setStatus('current')
if mibBuilder.loadTexts: runCnfgSaveAsStatus.setDescription("Returns the status of any current operation to save the\n                running configuration. The following values may be returned:\n\n                1 (idle)                There is no config file save operation\n                                        in progress.\n\n                2 (success)             The last config file save operation\n                                        completed successfully.\n\n                3 (failure)             The last config file save operation\n                                        failed.\n\n                4 (saving)              A config file save operation is\n                                        currently in progress.\n\n                When a read of this object returns a value of 'success' or\n                'failure', it will immediately be reset to 'idle' and a new\n                operation may be initiated if desired. A detailed description\n                of the last completed operation may be determined by reading\n                runCnfgLastSaveResult.")
runCnfgLastSaveResult = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 3, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: runCnfgLastSaveResult.setStatus('current')
if mibBuilder.loadTexts: runCnfgLastSaveResult.setDescription('Gives an indication of the result of the last completed SNMP\n                operation to save the running configuration.')
nextBootConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 3, 2))
bootCnfgPath = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 3, 2, 1), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bootCnfgPath.setStatus('current')
if mibBuilder.loadTexts: bootCnfgPath.setDescription("The full path of the configuration file to be used the next\n                time the device restarts. There is no guarantee that the file\n                referenced exists (i.e. it may have been deleted since the\n                configuration path was last set).\n\n                Only one set operation can be executed at a time across all\n                SNMP users, and an operation may not be started unless the\n                current value of bootCnfgSetStatus is 'idle'. The path must not\n                contain whitespace characters.\n\n                Immediately upon setting this object, the system will attempt\n                to set the new configuration path, and the process will\n                continue on the device until it has completed or a failure\n                occurs. The current status of the operation can be determined\n                by reading bootCnfgSetStatus, and the result of the last\n                completed operation is indicated by bootCnfgLastSetResult.\n\n                This object can be set with an empty string in order to clear\n                the current boot configuration. Otherwise, the path should be\n                of the form 'flash:/filename.cfg' or 'card:/filename.cfg'.\n\n                There are several requirements that must be met in order to set\n                a boot configuration file successfully:\n                - The file must exist.\n                - The file must be in the flash (on the active master in a\n                  stacked environment) or card filesystems.\n                - The file must have a .cfg suffix.\n                - In a stacked environment, there must be enough disk space\n                  available to store the configuration file on each stack\n                  member.")
bootCnfgExists = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 3, 2, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bootCnfgExists.setStatus('current')
if mibBuilder.loadTexts: bootCnfgExists.setDescription('This object will return TRUE if the currently defined boot\n                configuration file exists, or FALSE otherwise.')
bootCnfgSetStatus = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 3, 2, 3), SystemFileOperationType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bootCnfgSetStatus.setStatus('current')
if mibBuilder.loadTexts: bootCnfgSetStatus.setDescription("Returns the status of any current operation to set the next\n                boot configuration file. The following values may be returned:\n\n                1 (idle)                There is no boot configuration setting\n                                        operation in progress.\n\n                2 (success)             The last boot configuration setting\n                                        operation completed successfully.\n\n                3 (failure)             The last boot configuration setting\n                                        operation failed.\n\n                5 (syncing)             A boot configuration setting operation\n                                        is currently in progress and the file\n                                        is being syncronised across the stack\n                                        or system.\n\n                When a read of this object returns a value of 'success' or\n                'failure', it will immediately be reset to 'idle' and a new\n                operation may be initiated if desired. A detailed description\n                of the last completed operation may be determined by reading\n                bootCnfgLastSetResult.")
bootCnfgLastSetResult = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 3, 2, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bootCnfgLastSetResult.setStatus('current')
if mibBuilder.loadTexts: bootCnfgLastSetResult.setDescription('Gives an indication of the result of the last completed SNMP\n                operation to set the boot configuration filename.')
defaultConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 3, 3))
dfltCnfgPath = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 3, 3, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dfltCnfgPath.setStatus('current')
if mibBuilder.loadTexts: dfltCnfgPath.setDescription("The full path of the configuration file to be used upon device\n                restart, if no user-defined boot or backup configuration files\n                can be found. There is no guarantee that the file referenced\n                exists (i.e. it may have been deleted).\n\n                This object is not settable - the default configuration file is\n                always 'flash:/default.cfg'")
dfltCnfgExists = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 3, 3, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dfltCnfgExists.setStatus('current')
if mibBuilder.loadTexts: dfltCnfgExists.setDescription('This object will return TRUE if the currently defined default\n                configuration file exists, or FALSE otherwise.')
backupConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 3, 4))
backupCnfgPath = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 3, 4, 1), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: backupCnfgPath.setStatus('current')
if mibBuilder.loadTexts: backupCnfgPath.setDescription("The full path of the backup configuration file to be used the\n                next time the device restarts, if the boot configuration file\n                cannot be accessed. There is no guarantee that the file\n                referenced exists (i.e. it may have been deleted since the\n                backup configuration path was last set).\n\n                Only one set operation can be executed at a time across all\n                SNMP users, and an operation may not be started unless the\n                current value of backupCnfgSetStatus is 'idle'. The path must\n                not contain whitespace characters.\n\n                Immediately upon setting this object, the system will attempt\n                to set the new backup configuration path, and the process will\n                continue on the device until it has completed or a failure\n                occurs. The current status of the operation can be determined\n                by reading backupCnfgSetStatus, and the result of the last\n                completed operation is indicated by backupCnfgLastSetResult.\n\n                This object can be set with an empty string in order to clear\n                the current backup configuration. Otherwise, the path should be\n                of the form 'flash:/filename.cfg' or 'card:/filename.cfg'.\n\n                There are several requirements that must be met in order to set\n                a backup configuration file successfully:\n                - The file must exist.\n                - The file must be in the flash (on the active master in a\n                  stacked environment) or card filesystems.\n                - The file must have a .cfg suffix.\n                - In a stacked environment, there must be enough disk space\n                  available to store the configuration file on each stack\n                  member.")
backupCnfgExists = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 3, 4, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: backupCnfgExists.setStatus('current')
if mibBuilder.loadTexts: backupCnfgExists.setDescription('This object will return TRUE if the currently defined backup\n                configuration file exists, or FALSE otherwise.')
backupCnfgSetStatus = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 3, 4, 3), SystemFileOperationType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: backupCnfgSetStatus.setStatus('current')
if mibBuilder.loadTexts: backupCnfgSetStatus.setDescription("Returns the status of any current operation to set the next\n                backup boot configuration file. The following values may be\n                returned:\n\n                1 (idle)                There is no backup boot configuration\n                                        setting operation in progress.\n\n                2 (success)             The last backup boot configuration\n                                        setting operation completed\n                                        successfully.\n\n                3 (failure)             The last backup boot configuration\n                                        setting operation failed.\n\n                5 (syncing)             A backup boot configuration setting\n                                        operation is currently in progress and\n                                        the file is being syncronised across\n                                        the stack or system.\n\n                When a read of this object returns a value of 'success' or\n                'failure', it will immediately be reset to 'idle' and a new\n                operation may be initiated if desired. A detailed description\n                of the last completed operation may be determined by reading\n                backupCnfgLastSetResult.")
backupCnfgLastSetResult = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 3, 4, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: backupCnfgLastSetResult.setStatus('current')
if mibBuilder.loadTexts: backupCnfgLastSetResult.setDescription('Gives an indication of the result of the last completed SNMP\n                operation to set the backup boot configuration filename.')
serviceConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 5))
srvcTelnetEnable = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 5, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: srvcTelnetEnable.setStatus('current')
if mibBuilder.loadTexts: srvcTelnetEnable.setDescription("This object represents the state of the telnet server of a device.\n\n                A management application can find out the telnet server is either\n                enabled\tor disabled by reading this object.\n\n                To either enable or disable the telnet server, a management\n                application can SET this object with value 'enable(1)' or\n                'disable(2)' respectively.")
srvcSshEnable = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 5, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: srvcSshEnable.setStatus('current')
if mibBuilder.loadTexts: srvcSshEnable.setDescription("This object represents the state of the ssh server of a device.\n\n                A management application can find out the ssh server is either\n                enabled\tor disabled by reading this object.\n\n                To either enable or disable the ssh server, a management\n                application can SET this object with value 'enable(1)' or\n                'disable(2)' respectively.")
guiConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 6))
guiAppletConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 6, 1))
guiAppletSysSwVer = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 6, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: guiAppletSysSwVer.setStatus('current')
if mibBuilder.loadTexts: guiAppletSysSwVer.setDescription("This object represents the system software release that the\n                currently selected GUI applet was designed to run on.\n\n                The system will automatically search for GUI applet files\n                residing in the root directory of flash, and will select the\n                latest available one that is applicable to the currently\n                running system software. This will be the applet that is\n                uploaded to a user's web browser when they initiate use of the\n                GUI.")
guiAppletSwVer = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 6, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: guiAppletSwVer.setStatus('current')
if mibBuilder.loadTexts: guiAppletSwVer.setDescription("This object represents the software version of the currently\n                selected GUI applet.\n\n                The system will automatically search for GUI applet files\n                residing in the root directory of flash, and will select the\n                latest available one that is applicable to the currently\n                running system software. This will be the applet that is\n                uploaded to a user's web browser when they initiate use of the\n                GUI.")
mibBuilder.exportSymbols("AT-SETUP-MIB", setup=setup, SystemFileOperationType=SystemFileOperationType, backupConfig=backupConfig, currSoftSaveAs=currSoftSaveAs, restartStkMemberDevice=restartStkMemberDevice, guiAppletSysSwVer=guiAppletSysSwVer, guiAppletSwVer=guiAppletSwVer, guiAppletConfig=guiAppletConfig, bootCnfgPath=bootCnfgPath, dfltCnfgPath=dfltCnfgPath, nextBootLastSetResult=nextBootLastSetResult, nextBootSetStatus=nextBootSetStatus, srvcSshEnable=srvcSshEnable, bootCnfgExists=bootCnfgExists, currSoftLastSaveResult=currSoftLastSaveResult, PYSNMP_MODULE_ID=setup, backupCnfgPath=backupCnfgPath, backupSetStatus=backupSetStatus, backupCnfgExists=backupCnfgExists, deviceConfiguration=deviceConfiguration, bootCnfgLastSetResult=bootCnfgLastSetResult, guiConfig=guiConfig, defaultConfig=defaultConfig, runCnfgLastSaveResult=runCnfgLastSaveResult, firmware=firmware, serviceConfig=serviceConfig, nextBootConfig=nextBootConfig, bootCnfgSetStatus=bootCnfgSetStatus, backupVersion=backupVersion, runCnfgSaveAs=runCnfgSaveAs, nextBootVersion=nextBootVersion, currSoftSaveToFile=currSoftSaveToFile, currentFirmware=currentFirmware, dfltCnfgExists=dfltCnfgExists, currSoftName=currSoftName, srvcTelnetEnable=srvcTelnetEnable, backupFirmware=backupFirmware, currSoftSaveStatus=currSoftSaveStatus, restartDevice=restartDevice, currSoftVersion=currSoftVersion, backupLastSetResult=backupLastSetResult, runCnfgSaveAsStatus=runCnfgSaveAsStatus, backupCnfgLastSetResult=backupCnfgLastSetResult, nextBootFirmware=nextBootFirmware, backupCnfgSetStatus=backupCnfgSetStatus, backupPath=backupPath, nextBootPath=nextBootPath, runningConfig=runningConfig)
