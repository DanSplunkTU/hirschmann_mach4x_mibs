#
# PySNMP MIB module ELTEX-LTP8X-STANDALONE (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/eltex/ELTEX-LTP8X-STANDALONE
# Produced by pysmi-1.1.8 at Fri Jan  7 16:20:01 2022
# On host fv-az36-988 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
ltp8x, = mibBuilder.importSymbols("ELTEX-LTP8X", "ltp8x")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Integer32, Bits, MibIdentifier, TimeTicks, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, NotificationType, Counter64, Counter32, ObjectIdentity, Unsigned32, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Bits", "MibIdentifier", "TimeTicks", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "NotificationType", "Counter64", "Counter32", "ObjectIdentity", "Unsigned32", "ModuleIdentity", "Gauge32")
RowStatus, DisplayString, TextualConvention, TimeInterval, TimeStamp, MacAddress, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention", "TimeInterval", "TimeStamp", "MacAddress", "TruthValue")
ltp8xStandalone = ModuleIdentity((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1))
ltp8xStandalone.setRevisions(('2010-07-21 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ltp8xStandalone.setRevisionsDescriptions(('First revision',))
if mibBuilder.loadTexts: ltp8xStandalone.setLastUpdated('201007210000Z')
if mibBuilder.loadTexts: ltp8xStandalone.setOrganization('Eltex Co')
if mibBuilder.loadTexts: ltp8xStandalone.setContactInfo('eltex@gcom.ru')
if mibBuilder.loadTexts: ltp8xStandalone.setDescription('LTP8X-INSIDE MIB')
ltp8xSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 1))
ltp8xHostName = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ltp8xHostName.setStatus('current')
if mibBuilder.loadTexts: ltp8xHostName.setDescription(' ')
ltp8xIPAddress = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ltp8xIPAddress.setStatus('current')
if mibBuilder.loadTexts: ltp8xIPAddress.setDescription(' ')
ltp8xNetMask = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ltp8xNetMask.setStatus('current')
if mibBuilder.loadTexts: ltp8xNetMask.setDescription(' ')
ltp8xGateway = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ltp8xGateway.setStatus('current')
if mibBuilder.loadTexts: ltp8xGateway.setDescription(' ')
ltp8xVLAN = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ltp8xVLAN.setStatus('current')
if mibBuilder.loadTexts: ltp8xVLAN.setDescription(' ')
ltp8xFirmwareRevision = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ltp8xFirmwareRevision.setStatus('current')
if mibBuilder.loadTexts: ltp8xFirmwareRevision.setDescription(' ')
ltp8xSystemUptime = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ltp8xSystemUptime.setStatus('current')
if mibBuilder.loadTexts: ltp8xSystemUptime.setDescription('Uptime value in seconds')
ltp8xSystemHardwareRevision = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ltp8xSystemHardwareRevision.setStatus('current')
if mibBuilder.loadTexts: ltp8xSystemHardwareRevision.setDescription('')
ltp8xSystemMacAddress = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ltp8xSystemMacAddress.setStatus('current')
if mibBuilder.loadTexts: ltp8xSystemMacAddress.setDescription('')
ltp8xSystemDeviceName = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 1, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ltp8xSystemDeviceName.setStatus('current')
if mibBuilder.loadTexts: ltp8xSystemDeviceName.setDescription('')
ltp8xServicesControlTable = MibTable((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 2), )
if mibBuilder.loadTexts: ltp8xServicesControlTable.setStatus('current')
if mibBuilder.loadTexts: ltp8xServicesControlTable.setDescription(' ')
ltp8xServicesControlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 2, 1), ).setIndexNames((0, "ELTEX-LTP8X-STANDALONE", "ltp8xServicesControlIndex"))
if mibBuilder.loadTexts: ltp8xServicesControlEntry.setStatus('current')
if mibBuilder.loadTexts: ltp8xServicesControlEntry.setDescription('')
ltp8xServicesControlIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: ltp8xServicesControlIndex.setStatus('current')
if mibBuilder.loadTexts: ltp8xServicesControlIndex.setDescription('')
ltp8xServicesControlName = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ltp8xServicesControlName.setStatus('current')
if mibBuilder.loadTexts: ltp8xServicesControlName.setDescription('')
ltp8xServicesControlEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 2, 1, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ltp8xServicesControlEnabled.setStatus('current')
if mibBuilder.loadTexts: ltp8xServicesControlEnabled.setDescription('')
ltp8xBoardStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 10))
ltp8xDiskFreeSpace = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 10, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ltp8xDiskFreeSpace.setStatus('current')
if mibBuilder.loadTexts: ltp8xDiskFreeSpace.setDescription('Ammount of free disk space in kB.')
ltp8xRAMFree = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 10, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ltp8xRAMFree.setStatus('current')
if mibBuilder.loadTexts: ltp8xRAMFree.setDescription(' ')
ltp8xCPULoadAverage1Minute = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 10, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ltp8xCPULoadAverage1Minute.setStatus('current')
if mibBuilder.loadTexts: ltp8xCPULoadAverage1Minute.setDescription(' ')
ltp8xCPULoadAverage5Minutes = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 10, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ltp8xCPULoadAverage5Minutes.setStatus('current')
if mibBuilder.loadTexts: ltp8xCPULoadAverage5Minutes.setDescription(' ')
ltp8xCPULoadAverage15Minutes = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 10, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ltp8xCPULoadAverage15Minutes.setStatus('current')
if mibBuilder.loadTexts: ltp8xCPULoadAverage15Minutes.setDescription(' ')
ltp8xFan0Active = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 10, 6), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ltp8xFan0Active.setStatus('current')
if mibBuilder.loadTexts: ltp8xFan0Active.setDescription(' ')
ltp8xFan0RPM = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 10, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ltp8xFan0RPM.setStatus('current')
if mibBuilder.loadTexts: ltp8xFan0RPM.setDescription('Rotations per minute')
ltp8xFan1Active = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 10, 8), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ltp8xFan1Active.setStatus('current')
if mibBuilder.loadTexts: ltp8xFan1Active.setDescription(' ')
ltp8xFan1RPM = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 10, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ltp8xFan1RPM.setStatus('current')
if mibBuilder.loadTexts: ltp8xFan1RPM.setDescription('Rotations per minute')
ltp8xSensor1Temperature = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 10, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ltp8xSensor1Temperature.setStatus('current')
if mibBuilder.loadTexts: ltp8xSensor1Temperature.setDescription(' ')
ltp8xSensor2Temperature = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 10, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ltp8xSensor2Temperature.setStatus('current')
if mibBuilder.loadTexts: ltp8xSensor2Temperature.setDescription(' ')
ltp8xSensor1TemperatureExt = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 10, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(65535))).clone(namedValues=NamedValues(("notValid", 65535)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ltp8xSensor1TemperatureExt.setStatus('current')
if mibBuilder.loadTexts: ltp8xSensor1TemperatureExt.setDescription(' ')
ltp8xSensor2TemperatureExt = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 10, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(65535))).clone(namedValues=NamedValues(("notValid", 65535)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ltp8xSensor2TemperatureExt.setStatus('current')
if mibBuilder.loadTexts: ltp8xSensor2TemperatureExt.setDescription(' ')
ltp8xFanMinRPM = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 10, 20), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ltp8xFanMinRPM.setStatus('current')
if mibBuilder.loadTexts: ltp8xFanMinRPM.setDescription(' ')
ltp8xFanMaxRPM = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 10, 21), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ltp8xFanMaxRPM.setStatus('current')
if mibBuilder.loadTexts: ltp8xFanMaxRPM.setDescription(' ')
ltp8xUsers = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 11))
ltp8xUsersTable = MibTable((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 11, 1), )
if mibBuilder.loadTexts: ltp8xUsersTable.setStatus('current')
if mibBuilder.loadTexts: ltp8xUsersTable.setDescription(' ')
ltp8xUsersEntry = MibTableRow((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 11, 1, 1), ).setIndexNames((0, "ELTEX-LTP8X-STANDALONE", "ltp8xUsersName"))
if mibBuilder.loadTexts: ltp8xUsersEntry.setStatus('current')
if mibBuilder.loadTexts: ltp8xUsersEntry.setDescription('')
ltp8xUsersName = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 11, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ltp8xUsersName.setStatus('current')
if mibBuilder.loadTexts: ltp8xUsersName.setDescription('')
ltp8xUsersGroups = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 11, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(4, 4)).setFixedLength(4)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ltp8xUsersGroups.setStatus('current')
if mibBuilder.loadTexts: ltp8xUsersGroups.setDescription('')
ltp8xUsersOldPassword = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 11, 1, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ltp8xUsersOldPassword.setStatus('current')
if mibBuilder.loadTexts: ltp8xUsersOldPassword.setDescription('')
ltp8xUsersNewPassword = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 11, 1, 1, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ltp8xUsersNewPassword.setStatus('current')
if mibBuilder.loadTexts: ltp8xUsersNewPassword.setDescription('')
ltp8xUsersRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 11, 1, 1, 5), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ltp8xUsersRowStatus.setStatus('current')
if mibBuilder.loadTexts: ltp8xUsersRowStatus.setDescription('')
ltp8xUsersPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 11, 1, 1, 6), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ltp8xUsersPriority.setStatus('current')
if mibBuilder.loadTexts: ltp8xUsersPriority.setDescription('')
ltp8xUsersGroupsTable = MibTable((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 11, 2), )
if mibBuilder.loadTexts: ltp8xUsersGroupsTable.setStatus('current')
if mibBuilder.loadTexts: ltp8xUsersGroupsTable.setDescription(' ')
ltp8xUsersGroupsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 11, 2, 1), ).setIndexNames((0, "ELTEX-LTP8X-STANDALONE", "ltp8xUsersGroupsID"))
if mibBuilder.loadTexts: ltp8xUsersGroupsEntry.setStatus('current')
if mibBuilder.loadTexts: ltp8xUsersGroupsEntry.setDescription('')
ltp8xUsersGroupsID = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 11, 2, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ltp8xUsersGroupsID.setStatus('current')
if mibBuilder.loadTexts: ltp8xUsersGroupsID.setDescription('')
ltp8xUsersGroupsName = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 11, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ltp8xUsersGroupsName.setStatus('current')
if mibBuilder.loadTexts: ltp8xUsersGroupsName.setDescription('')
ltp8xPrivilegesNamesTable = MibTable((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 11, 3), )
if mibBuilder.loadTexts: ltp8xPrivilegesNamesTable.setStatus('current')
if mibBuilder.loadTexts: ltp8xPrivilegesNamesTable.setDescription('')
ltp8xPrivilegesNamesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 11, 3, 1), ).setIndexNames((0, "ELTEX-LTP8X-STANDALONE", "ltp8xPrivilegesNamesIndex"))
if mibBuilder.loadTexts: ltp8xPrivilegesNamesEntry.setStatus('current')
if mibBuilder.loadTexts: ltp8xPrivilegesNamesEntry.setDescription('')
ltp8xPrivilegesNamesIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 11, 3, 1, 1), Unsigned32())
if mibBuilder.loadTexts: ltp8xPrivilegesNamesIndex.setStatus('current')
if mibBuilder.loadTexts: ltp8xPrivilegesNamesIndex.setDescription(' ')
ltp8xPrivilegesNamesName = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 11, 3, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ltp8xPrivilegesNamesName.setStatus('current')
if mibBuilder.loadTexts: ltp8xPrivilegesNamesName.setDescription('')
ltp8xPrivilegesLevelsTable = MibTable((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 11, 4), )
if mibBuilder.loadTexts: ltp8xPrivilegesLevelsTable.setStatus('current')
if mibBuilder.loadTexts: ltp8xPrivilegesLevelsTable.setDescription('')
ltp8xPrivilegesLevelsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 11, 4, 1), ).setIndexNames((0, "ELTEX-LTP8X-STANDALONE", "ltp8xPrivilegesLevelsLevel"))
if mibBuilder.loadTexts: ltp8xPrivilegesLevelsEntry.setStatus('current')
if mibBuilder.loadTexts: ltp8xPrivilegesLevelsEntry.setDescription('')
ltp8xPrivilegesLevelsLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 11, 4, 1, 1), Unsigned32())
if mibBuilder.loadTexts: ltp8xPrivilegesLevelsLevel.setStatus('current')
if mibBuilder.loadTexts: ltp8xPrivilegesLevelsLevel.setDescription(' ')
ltp8xPrivilegesLevelsAllowed = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 11, 4, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(4, 4)).setFixedLength(4)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ltp8xPrivilegesLevelsAllowed.setStatus('current')
if mibBuilder.loadTexts: ltp8xPrivilegesLevelsAllowed.setDescription('')
ltp8xLogSubmodulesTable = MibTable((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 12), )
if mibBuilder.loadTexts: ltp8xLogSubmodulesTable.setStatus('current')
if mibBuilder.loadTexts: ltp8xLogSubmodulesTable.setDescription(' ')
ltp8xLogSubmodulesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 12, 1), ).setIndexNames((0, "ELTEX-LTP8X-STANDALONE", "ltp8xLogSubmodulesID"))
if mibBuilder.loadTexts: ltp8xLogSubmodulesEntry.setStatus('current')
if mibBuilder.loadTexts: ltp8xLogSubmodulesEntry.setDescription('')
ltp8xLogSubmodulesID = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 12, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)))
if mibBuilder.loadTexts: ltp8xLogSubmodulesID.setStatus('current')
if mibBuilder.loadTexts: ltp8xLogSubmodulesID.setDescription('')
ltp8xLogSubmodulesName = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 12, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ltp8xLogSubmodulesName.setStatus('current')
if mibBuilder.loadTexts: ltp8xLogSubmodulesName.setDescription('')
ltp8xLogSubmodulesLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 12, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("emergency", 0), ("alert", 1), ("critical", 2), ("error", 3), ("warning", 4), ("notice", 5), ("info", 6), ("debug", 7), ("none", 8)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ltp8xLogSubmodulesLevel.setStatus('current')
if mibBuilder.loadTexts: ltp8xLogSubmodulesLevel.setDescription('')
ltp8xLogSubmodulesDestination = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 12, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("syslog", 0), ("console", 1), ("telnet", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ltp8xLogSubmodulesDestination.setStatus('current')
if mibBuilder.loadTexts: ltp8xLogSubmodulesDestination.setDescription('')
ltp8xLogSubmodulesShowProgName = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 12, 1, 5), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ltp8xLogSubmodulesShowProgName.setStatus('current')
if mibBuilder.loadTexts: ltp8xLogSubmodulesShowProgName.setDescription('Controls if process name will appear in log.')
ltp8xLogSubmodulesShowSubmoduleName = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 12, 1, 6), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ltp8xLogSubmodulesShowSubmoduleName.setStatus('current')
if mibBuilder.loadTexts: ltp8xLogSubmodulesShowSubmoduleName.setDescription('Controls if submodule name will appear in log.')
ltp8xLogSubmodulesShowLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 12, 1, 7), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ltp8xLogSubmodulesShowLevel.setStatus('current')
if mibBuilder.loadTexts: ltp8xLogSubmodulesShowLevel.setDescription('Controls if log message level will appear in log.')
ltp8xLogSubmodulesShowTime = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 12, 1, 8), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ltp8xLogSubmodulesShowTime.setStatus('current')
if mibBuilder.loadTexts: ltp8xLogSubmodulesShowTime.setDescription('Controls if log message time will appear in log.')
ltp8xActivationAuthModeTable = MibTable((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 13), )
if mibBuilder.loadTexts: ltp8xActivationAuthModeTable.setStatus('current')
if mibBuilder.loadTexts: ltp8xActivationAuthModeTable.setDescription(' ')
ltp8xActivationAuthModeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 13, 1), ).setIndexNames((0, "ELTEX-LTP8X-STANDALONE", "ltp8xActivationAuthModeChannel"))
if mibBuilder.loadTexts: ltp8xActivationAuthModeEntry.setStatus('current')
if mibBuilder.loadTexts: ltp8xActivationAuthModeEntry.setDescription('')
ltp8xActivationAuthModeChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 13, 1, 1), Unsigned32())
if mibBuilder.loadTexts: ltp8xActivationAuthModeChannel.setStatus('current')
if mibBuilder.loadTexts: ltp8xActivationAuthModeChannel.setDescription('')
ltp8xActivationAuthModeHostControlledLumpedSN = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 13, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ltp8xActivationAuthModeHostControlledLumpedSN.setStatus('current')
if mibBuilder.loadTexts: ltp8xActivationAuthModeHostControlledLumpedSN.setDescription('')
ltp8xLoggingDestinationsTable = MibTable((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 14), )
if mibBuilder.loadTexts: ltp8xLoggingDestinationsTable.setStatus('current')
if mibBuilder.loadTexts: ltp8xLoggingDestinationsTable.setDescription(' ')
ltp8xLoggingDestinationsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 14, 1), ).setIndexNames((0, "ELTEX-LTP8X-STANDALONE", "ltp8xLoggingDestinationsId"))
if mibBuilder.loadTexts: ltp8xLoggingDestinationsEntry.setStatus('current')
if mibBuilder.loadTexts: ltp8xLoggingDestinationsEntry.setDescription('')
ltp8xLoggingDestinationsId = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 14, 1, 1), Unsigned32())
if mibBuilder.loadTexts: ltp8xLoggingDestinationsId.setStatus('current')
if mibBuilder.loadTexts: ltp8xLoggingDestinationsId.setDescription('')
ltp8xLoggingDestinationsName = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 14, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ltp8xLoggingDestinationsName.setStatus('current')
if mibBuilder.loadTexts: ltp8xLoggingDestinationsName.setDescription('')
ltp8xLoggingDestinationsLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 14, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("emergency", 0), ("alert", 1), ("critical", 2), ("error", 3), ("warning", 4), ("notice", 5), ("info", 6), ("debug", 7), ("none", 8)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ltp8xLoggingDestinationsLevel.setStatus('current')
if mibBuilder.loadTexts: ltp8xLoggingDestinationsLevel.setDescription('')
ltp8xInterfaceStatusTable = MibTable((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 15), )
if mibBuilder.loadTexts: ltp8xInterfaceStatusTable.setStatus('current')
if mibBuilder.loadTexts: ltp8xInterfaceStatusTable.setDescription(' ')
ltp8xInterfaceStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 15, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: ltp8xInterfaceStatusEntry.setStatus('current')
if mibBuilder.loadTexts: ltp8xInterfaceStatusEntry.setDescription('')
ltp8xInterfaceStatusError = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 15, 1, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ltp8xInterfaceStatusError.setStatus('current')
if mibBuilder.loadTexts: ltp8xInterfaceStatusError.setDescription('If true - all other fields should be ignored')
ltp8xInterfaceStatusDuplex = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 15, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("halfDuplex", 0), ("fullDuplex", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ltp8xInterfaceStatusDuplex.setStatus('current')
if mibBuilder.loadTexts: ltp8xInterfaceStatusDuplex.setDescription('')
ltp8xInterfaceStatusFlowControlEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 15, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ltp8xInterfaceStatusFlowControlEnabled.setStatus('current')
if mibBuilder.loadTexts: ltp8xInterfaceStatusFlowControlEnabled.setDescription('')
ltp8xFanControl = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 16))
ltp8xFanSpeed = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 16, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(-1))).clone(namedValues=NamedValues(("auto", -1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ltp8xFanSpeed.setStatus('current')
if mibBuilder.loadTexts: ltp8xFanSpeed.setDescription('Set fixed/auto fan speed. In percent, or auto')
ltp8xFanMinSpeed = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 16, 2), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ltp8xFanMinSpeed.setStatus('current')
if mibBuilder.loadTexts: ltp8xFanMinSpeed.setDescription("Fan's rotation speed low limit (in percent)")
ltp8xPowerSupplyTable = MibTable((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 17), )
if mibBuilder.loadTexts: ltp8xPowerSupplyTable.setStatus('current')
if mibBuilder.loadTexts: ltp8xPowerSupplyTable.setDescription(' ')
ltp8xPowerSupplyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 17, 1), ).setIndexNames((0, "ELTEX-LTP8X-STANDALONE", "ltp8xPowerSupplyModuleId"))
if mibBuilder.loadTexts: ltp8xPowerSupplyEntry.setStatus('current')
if mibBuilder.loadTexts: ltp8xPowerSupplyEntry.setDescription('')
ltp8xPowerSupplyModuleId = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 17, 1, 1), Unsigned32())
if mibBuilder.loadTexts: ltp8xPowerSupplyModuleId.setStatus('current')
if mibBuilder.loadTexts: ltp8xPowerSupplyModuleId.setDescription('')
ltp8xPowerSupplyModulePresent = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 17, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ltp8xPowerSupplyModulePresent.setStatus('current')
if mibBuilder.loadTexts: ltp8xPowerSupplyModulePresent.setDescription('')
ltp8xPowerSupplyModuleName = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 17, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ltp8xPowerSupplyModuleName.setStatus('current')
if mibBuilder.loadTexts: ltp8xPowerSupplyModuleName.setDescription('')
ltp8xPowerSupplyModuleType = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 17, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("directCurrent", 0), ("alternateCurrent", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ltp8xPowerSupplyModuleType.setStatus('current')
if mibBuilder.loadTexts: ltp8xPowerSupplyModuleType.setDescription('')
ltp8xPowerSupplyModuleIntact = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 17, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ltp8xPowerSupplyModuleIntact.setStatus('current')
if mibBuilder.loadTexts: ltp8xPowerSupplyModuleIntact.setDescription('')
ltp8xLicense = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 18))
ltp8xLicenseInstalled = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 18, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ltp8xLicenseInstalled.setStatus('current')
if mibBuilder.loadTexts: ltp8xLicenseInstalled.setDescription('')
ltp8xLicenseValid = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 18, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ltp8xLicenseValid.setStatus('current')
if mibBuilder.loadTexts: ltp8xLicenseValid.setDescription('')
ltp8xLicenseVersion = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 18, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("version1v0", 0), ("version1v1", 1), ("version1v2", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ltp8xLicenseVersion.setStatus('current')
if mibBuilder.loadTexts: ltp8xLicenseVersion.setDescription('')
ltp8xLicenseBoardSN = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 18, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ltp8xLicenseBoardSN.setStatus('current')
if mibBuilder.loadTexts: ltp8xLicenseBoardSN.setDescription('')
ltp8xLicenseVendor = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 18, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ltp8xLicenseVendor.setStatus('current')
if mibBuilder.loadTexts: ltp8xLicenseVendor.setDescription('')
ltp8xLicenseONTCount = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 18, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2147483647, -1))).clone(namedValues=NamedValues(("unlimited", 2147483647), ("notAvailable", -1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ltp8xLicenseONTCount.setStatus('current')
if mibBuilder.loadTexts: ltp8xLicenseONTCount.setDescription('')
ltp8xLicenseActiveONTCount = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 18, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(-1))).clone(namedValues=NamedValues(("notAvailable", -1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ltp8xLicenseActiveONTCount.setStatus('current')
if mibBuilder.loadTexts: ltp8xLicenseActiveONTCount.setDescription('')
ltp8xLogSize = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 20), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ltp8xLogSize.setStatus('current')
if mibBuilder.loadTexts: ltp8xLogSize.setDescription(' ')
ltp8xExternalFirmwareIP = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 21), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ltp8xExternalFirmwareIP.setStatus('current')
if mibBuilder.loadTexts: ltp8xExternalFirmwareIP.setDescription('Address of server that contains ONT firmwares.')
ltp8xExternalFirmwarePort = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 22), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ltp8xExternalFirmwarePort.setStatus('current')
if mibBuilder.loadTexts: ltp8xExternalFirmwarePort.setDescription('Port of server that contains ONT firmwares.')
ltp8xNTPDaylightSaving = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 25), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ltp8xNTPDaylightSaving.setStatus('current')
if mibBuilder.loadTexts: ltp8xNTPDaylightSaving.setDescription(' ')
ltp8xONTFwAutoUpdateEnabled = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 26), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ltp8xONTFwAutoUpdateEnabled.setStatus('current')
if mibBuilder.loadTexts: ltp8xONTFwAutoUpdateEnabled.setDescription(' ')
ltp8xConfigChangeCounter = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 40), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ltp8xConfigChangeCounter.setStatus('current')
if mibBuilder.loadTexts: ltp8xConfigChangeCounter.setDescription(' ')
ltp8xRereadConfig = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 49), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ltp8xRereadConfig.setStatus('current')
if mibBuilder.loadTexts: ltp8xRereadConfig.setDescription(' ')
ltp8xSaveConfig = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 50), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ltp8xSaveConfig.setStatus('current')
if mibBuilder.loadTexts: ltp8xSaveConfig.setDescription(' ')
ltp8xRebootTimeout = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 51), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ltp8xRebootTimeout.setStatus('current')
if mibBuilder.loadTexts: ltp8xRebootTimeout.setDescription(' ')
mibBuilder.exportSymbols("ELTEX-LTP8X-STANDALONE", ltp8xActivationAuthModeTable=ltp8xActivationAuthModeTable, ltp8xLogSubmodulesEntry=ltp8xLogSubmodulesEntry, ltp8xLicense=ltp8xLicense, ltp8xFan0RPM=ltp8xFan0RPM, ltp8xLicenseONTCount=ltp8xLicenseONTCount, ltp8xExternalFirmwareIP=ltp8xExternalFirmwareIP, ltp8xPowerSupplyModuleType=ltp8xPowerSupplyModuleType, ltp8xSaveConfig=ltp8xSaveConfig, ltp8xUsersGroups=ltp8xUsersGroups, ltp8xONTFwAutoUpdateEnabled=ltp8xONTFwAutoUpdateEnabled, ltp8xBoardStatus=ltp8xBoardStatus, ltp8xFan0Active=ltp8xFan0Active, ltp8xServicesControlEntry=ltp8xServicesControlEntry, ltp8xPowerSupplyModulePresent=ltp8xPowerSupplyModulePresent, ltp8xCPULoadAverage1Minute=ltp8xCPULoadAverage1Minute, ltp8xFanMinRPM=ltp8xFanMinRPM, ltp8xLogSubmodulesShowLevel=ltp8xLogSubmodulesShowLevel, ltp8xLogSubmodulesShowTime=ltp8xLogSubmodulesShowTime, ltp8xPowerSupplyModuleId=ltp8xPowerSupplyModuleId, ltp8xPrivilegesLevelsTable=ltp8xPrivilegesLevelsTable, ltp8xLogSubmodulesShowProgName=ltp8xLogSubmodulesShowProgName, ltp8xServicesControlTable=ltp8xServicesControlTable, ltp8xSensor2TemperatureExt=ltp8xSensor2TemperatureExt, ltp8xInterfaceStatusDuplex=ltp8xInterfaceStatusDuplex, ltp8xLogSubmodulesTable=ltp8xLogSubmodulesTable, ltp8xUsersGroupsTable=ltp8xUsersGroupsTable, ltp8xPrivilegesNamesEntry=ltp8xPrivilegesNamesEntry, ltp8xVLAN=ltp8xVLAN, ltp8xLicenseValid=ltp8xLicenseValid, ltp8xCPULoadAverage5Minutes=ltp8xCPULoadAverage5Minutes, ltp8xLicenseBoardSN=ltp8xLicenseBoardSN, ltp8xLogSubmodulesName=ltp8xLogSubmodulesName, ltp8xInterfaceStatusEntry=ltp8xInterfaceStatusEntry, ltp8xUsersGroupsEntry=ltp8xUsersGroupsEntry, ltp8xPrivilegesLevelsEntry=ltp8xPrivilegesLevelsEntry, ltp8xSensor2Temperature=ltp8xSensor2Temperature, ltp8xLicenseVersion=ltp8xLicenseVersion, ltp8xLogSubmodulesLevel=ltp8xLogSubmodulesLevel, ltp8xLogSubmodulesDestination=ltp8xLogSubmodulesDestination, ltp8xPrivilegesNamesName=ltp8xPrivilegesNamesName, ltp8xPowerSupplyModuleName=ltp8xPowerSupplyModuleName, PYSNMP_MODULE_ID=ltp8xStandalone, ltp8xFanMinSpeed=ltp8xFanMinSpeed, ltp8xSensor1Temperature=ltp8xSensor1Temperature, ltp8xUsersName=ltp8xUsersName, ltp8xUsersGroupsID=ltp8xUsersGroupsID, ltp8xPrivilegesNamesIndex=ltp8xPrivilegesNamesIndex, ltp8xLicenseActiveONTCount=ltp8xLicenseActiveONTCount, ltp8xLicenseVendor=ltp8xLicenseVendor, ltp8xLogSubmodulesShowSubmoduleName=ltp8xLogSubmodulesShowSubmoduleName, ltp8xLoggingDestinationsTable=ltp8xLoggingDestinationsTable, ltp8xInterfaceStatusFlowControlEnabled=ltp8xInterfaceStatusFlowControlEnabled, ltp8xRAMFree=ltp8xRAMFree, ltp8xUsers=ltp8xUsers, ltp8xSystemDeviceName=ltp8xSystemDeviceName, ltp8xFirmwareRevision=ltp8xFirmwareRevision, ltp8xInterfaceStatusTable=ltp8xInterfaceStatusTable, ltp8xPrivilegesNamesTable=ltp8xPrivilegesNamesTable, ltp8xActivationAuthModeChannel=ltp8xActivationAuthModeChannel, ltp8xGateway=ltp8xGateway, ltp8xPowerSupplyEntry=ltp8xPowerSupplyEntry, ltp8xFanMaxRPM=ltp8xFanMaxRPM, ltp8xFanSpeed=ltp8xFanSpeed, ltp8xRebootTimeout=ltp8xRebootTimeout, ltp8xUsersNewPassword=ltp8xUsersNewPassword, ltp8xInterfaceStatusError=ltp8xInterfaceStatusError, ltp8xUsersEntry=ltp8xUsersEntry, ltp8xUsersPriority=ltp8xUsersPriority, ltp8xCPULoadAverage15Minutes=ltp8xCPULoadAverage15Minutes, ltp8xHostName=ltp8xHostName, ltp8xLoggingDestinationsEntry=ltp8xLoggingDestinationsEntry, ltp8xServicesControlEnabled=ltp8xServicesControlEnabled, ltp8xFan1Active=ltp8xFan1Active, ltp8xUsersRowStatus=ltp8xUsersRowStatus, ltp8xRereadConfig=ltp8xRereadConfig, ltp8xUsersTable=ltp8xUsersTable, ltp8xServicesControlIndex=ltp8xServicesControlIndex, ltp8xPrivilegesLevelsLevel=ltp8xPrivilegesLevelsLevel, ltp8xUsersGroupsName=ltp8xUsersGroupsName, ltp8xNetMask=ltp8xNetMask, ltp8xSystem=ltp8xSystem, ltp8xPrivilegesLevelsAllowed=ltp8xPrivilegesLevelsAllowed, ltp8xActivationAuthModeEntry=ltp8xActivationAuthModeEntry, ltp8xConfigChangeCounter=ltp8xConfigChangeCounter, ltp8xLoggingDestinationsName=ltp8xLoggingDestinationsName, ltp8xSystemHardwareRevision=ltp8xSystemHardwareRevision, ltp8xDiskFreeSpace=ltp8xDiskFreeSpace, ltp8xPowerSupplyTable=ltp8xPowerSupplyTable, ltp8xLogSubmodulesID=ltp8xLogSubmodulesID, ltp8xPowerSupplyModuleIntact=ltp8xPowerSupplyModuleIntact, ltp8xActivationAuthModeHostControlledLumpedSN=ltp8xActivationAuthModeHostControlledLumpedSN, ltp8xLoggingDestinationsId=ltp8xLoggingDestinationsId, ltp8xLicenseInstalled=ltp8xLicenseInstalled, ltp8xExternalFirmwarePort=ltp8xExternalFirmwarePort, ltp8xServicesControlName=ltp8xServicesControlName, ltp8xStandalone=ltp8xStandalone, ltp8xUsersOldPassword=ltp8xUsersOldPassword, ltp8xSystemUptime=ltp8xSystemUptime, ltp8xFan1RPM=ltp8xFan1RPM, ltp8xSystemMacAddress=ltp8xSystemMacAddress, ltp8xFanControl=ltp8xFanControl, ltp8xLogSize=ltp8xLogSize, ltp8xIPAddress=ltp8xIPAddress, ltp8xNTPDaylightSaving=ltp8xNTPDaylightSaving, ltp8xLoggingDestinationsLevel=ltp8xLoggingDestinationsLevel, ltp8xSensor1TemperatureExt=ltp8xSensor1TemperatureExt)
