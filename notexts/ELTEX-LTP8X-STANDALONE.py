#
# PySNMP MIB module ELTEX-LTP8X-STANDALONE (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/eltex/ELTEX-LTP8X-STANDALONE
# Produced by pysmi-1.1.8 at Fri Jan  7 16:19:58 2022
# On host fv-az36-988 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ltp8x, = mibBuilder.importSymbols("ELTEX-LTP8X", "ltp8x")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, ObjectIdentity, Counter32, iso, MibIdentifier, Unsigned32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, IpAddress, Integer32, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "ObjectIdentity", "Counter32", "iso", "MibIdentifier", "Unsigned32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "IpAddress", "Integer32", "TimeTicks", "Counter64", "Gauge32")
RowStatus, MacAddress, TimeStamp, TruthValue, TimeInterval, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "MacAddress", "TimeStamp", "TruthValue", "TimeInterval", "TextualConvention", "DisplayString")
ltp8xStandalone = ModuleIdentity((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1))
ltp8xStandalone.setRevisions(('2010-07-21 00:00',))
if mibBuilder.loadTexts: ltp8xStandalone.setLastUpdated('201007210000Z')
if mibBuilder.loadTexts: ltp8xStandalone.setOrganization('Eltex Co')
ltp8xSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 1))
ltp8xHostName = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ltp8xHostName.setStatus('current')
ltp8xIPAddress = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ltp8xIPAddress.setStatus('current')
ltp8xNetMask = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ltp8xNetMask.setStatus('current')
ltp8xGateway = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ltp8xGateway.setStatus('current')
ltp8xVLAN = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ltp8xVLAN.setStatus('current')
ltp8xFirmwareRevision = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ltp8xFirmwareRevision.setStatus('current')
ltp8xSystemUptime = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ltp8xSystemUptime.setStatus('current')
ltp8xSystemHardwareRevision = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ltp8xSystemHardwareRevision.setStatus('current')
ltp8xSystemMacAddress = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ltp8xSystemMacAddress.setStatus('current')
ltp8xSystemDeviceName = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 1, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ltp8xSystemDeviceName.setStatus('current')
ltp8xServicesControlTable = MibTable((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 2), )
if mibBuilder.loadTexts: ltp8xServicesControlTable.setStatus('current')
ltp8xServicesControlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 2, 1), ).setIndexNames((0, "ELTEX-LTP8X-STANDALONE", "ltp8xServicesControlIndex"))
if mibBuilder.loadTexts: ltp8xServicesControlEntry.setStatus('current')
ltp8xServicesControlIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: ltp8xServicesControlIndex.setStatus('current')
ltp8xServicesControlName = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ltp8xServicesControlName.setStatus('current')
ltp8xServicesControlEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 2, 1, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ltp8xServicesControlEnabled.setStatus('current')
ltp8xBoardStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 10))
ltp8xDiskFreeSpace = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 10, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ltp8xDiskFreeSpace.setStatus('current')
ltp8xRAMFree = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 10, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ltp8xRAMFree.setStatus('current')
ltp8xCPULoadAverage1Minute = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 10, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ltp8xCPULoadAverage1Minute.setStatus('current')
ltp8xCPULoadAverage5Minutes = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 10, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ltp8xCPULoadAverage5Minutes.setStatus('current')
ltp8xCPULoadAverage15Minutes = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 10, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ltp8xCPULoadAverage15Minutes.setStatus('current')
ltp8xFan0Active = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 10, 6), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ltp8xFan0Active.setStatus('current')
ltp8xFan0RPM = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 10, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ltp8xFan0RPM.setStatus('current')
ltp8xFan1Active = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 10, 8), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ltp8xFan1Active.setStatus('current')
ltp8xFan1RPM = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 10, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ltp8xFan1RPM.setStatus('current')
ltp8xSensor1Temperature = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 10, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ltp8xSensor1Temperature.setStatus('current')
ltp8xSensor2Temperature = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 10, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ltp8xSensor2Temperature.setStatus('current')
ltp8xSensor1TemperatureExt = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 10, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(65535))).clone(namedValues=NamedValues(("notValid", 65535)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ltp8xSensor1TemperatureExt.setStatus('current')
ltp8xSensor2TemperatureExt = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 10, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(65535))).clone(namedValues=NamedValues(("notValid", 65535)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ltp8xSensor2TemperatureExt.setStatus('current')
ltp8xFanMinRPM = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 10, 20), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ltp8xFanMinRPM.setStatus('current')
ltp8xFanMaxRPM = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 10, 21), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ltp8xFanMaxRPM.setStatus('current')
ltp8xUsers = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 11))
ltp8xUsersTable = MibTable((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 11, 1), )
if mibBuilder.loadTexts: ltp8xUsersTable.setStatus('current')
ltp8xUsersEntry = MibTableRow((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 11, 1, 1), ).setIndexNames((0, "ELTEX-LTP8X-STANDALONE", "ltp8xUsersName"))
if mibBuilder.loadTexts: ltp8xUsersEntry.setStatus('current')
ltp8xUsersName = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 11, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ltp8xUsersName.setStatus('current')
ltp8xUsersGroups = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 11, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(4, 4)).setFixedLength(4)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ltp8xUsersGroups.setStatus('current')
ltp8xUsersOldPassword = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 11, 1, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ltp8xUsersOldPassword.setStatus('current')
ltp8xUsersNewPassword = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 11, 1, 1, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ltp8xUsersNewPassword.setStatus('current')
ltp8xUsersRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 11, 1, 1, 5), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ltp8xUsersRowStatus.setStatus('current')
ltp8xUsersPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 11, 1, 1, 6), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ltp8xUsersPriority.setStatus('current')
ltp8xUsersGroupsTable = MibTable((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 11, 2), )
if mibBuilder.loadTexts: ltp8xUsersGroupsTable.setStatus('current')
ltp8xUsersGroupsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 11, 2, 1), ).setIndexNames((0, "ELTEX-LTP8X-STANDALONE", "ltp8xUsersGroupsID"))
if mibBuilder.loadTexts: ltp8xUsersGroupsEntry.setStatus('current')
ltp8xUsersGroupsID = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 11, 2, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ltp8xUsersGroupsID.setStatus('current')
ltp8xUsersGroupsName = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 11, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ltp8xUsersGroupsName.setStatus('current')
ltp8xPrivilegesNamesTable = MibTable((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 11, 3), )
if mibBuilder.loadTexts: ltp8xPrivilegesNamesTable.setStatus('current')
ltp8xPrivilegesNamesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 11, 3, 1), ).setIndexNames((0, "ELTEX-LTP8X-STANDALONE", "ltp8xPrivilegesNamesIndex"))
if mibBuilder.loadTexts: ltp8xPrivilegesNamesEntry.setStatus('current')
ltp8xPrivilegesNamesIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 11, 3, 1, 1), Unsigned32())
if mibBuilder.loadTexts: ltp8xPrivilegesNamesIndex.setStatus('current')
ltp8xPrivilegesNamesName = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 11, 3, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ltp8xPrivilegesNamesName.setStatus('current')
ltp8xPrivilegesLevelsTable = MibTable((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 11, 4), )
if mibBuilder.loadTexts: ltp8xPrivilegesLevelsTable.setStatus('current')
ltp8xPrivilegesLevelsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 11, 4, 1), ).setIndexNames((0, "ELTEX-LTP8X-STANDALONE", "ltp8xPrivilegesLevelsLevel"))
if mibBuilder.loadTexts: ltp8xPrivilegesLevelsEntry.setStatus('current')
ltp8xPrivilegesLevelsLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 11, 4, 1, 1), Unsigned32())
if mibBuilder.loadTexts: ltp8xPrivilegesLevelsLevel.setStatus('current')
ltp8xPrivilegesLevelsAllowed = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 11, 4, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(4, 4)).setFixedLength(4)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ltp8xPrivilegesLevelsAllowed.setStatus('current')
ltp8xLogSubmodulesTable = MibTable((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 12), )
if mibBuilder.loadTexts: ltp8xLogSubmodulesTable.setStatus('current')
ltp8xLogSubmodulesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 12, 1), ).setIndexNames((0, "ELTEX-LTP8X-STANDALONE", "ltp8xLogSubmodulesID"))
if mibBuilder.loadTexts: ltp8xLogSubmodulesEntry.setStatus('current')
ltp8xLogSubmodulesID = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 12, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)))
if mibBuilder.loadTexts: ltp8xLogSubmodulesID.setStatus('current')
ltp8xLogSubmodulesName = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 12, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ltp8xLogSubmodulesName.setStatus('current')
ltp8xLogSubmodulesLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 12, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("emergency", 0), ("alert", 1), ("critical", 2), ("error", 3), ("warning", 4), ("notice", 5), ("info", 6), ("debug", 7), ("none", 8)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ltp8xLogSubmodulesLevel.setStatus('current')
ltp8xLogSubmodulesDestination = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 12, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("syslog", 0), ("console", 1), ("telnet", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ltp8xLogSubmodulesDestination.setStatus('current')
ltp8xLogSubmodulesShowProgName = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 12, 1, 5), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ltp8xLogSubmodulesShowProgName.setStatus('current')
ltp8xLogSubmodulesShowSubmoduleName = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 12, 1, 6), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ltp8xLogSubmodulesShowSubmoduleName.setStatus('current')
ltp8xLogSubmodulesShowLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 12, 1, 7), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ltp8xLogSubmodulesShowLevel.setStatus('current')
ltp8xLogSubmodulesShowTime = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 12, 1, 8), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ltp8xLogSubmodulesShowTime.setStatus('current')
ltp8xActivationAuthModeTable = MibTable((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 13), )
if mibBuilder.loadTexts: ltp8xActivationAuthModeTable.setStatus('current')
ltp8xActivationAuthModeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 13, 1), ).setIndexNames((0, "ELTEX-LTP8X-STANDALONE", "ltp8xActivationAuthModeChannel"))
if mibBuilder.loadTexts: ltp8xActivationAuthModeEntry.setStatus('current')
ltp8xActivationAuthModeChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 13, 1, 1), Unsigned32())
if mibBuilder.loadTexts: ltp8xActivationAuthModeChannel.setStatus('current')
ltp8xActivationAuthModeHostControlledLumpedSN = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 13, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ltp8xActivationAuthModeHostControlledLumpedSN.setStatus('current')
ltp8xLoggingDestinationsTable = MibTable((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 14), )
if mibBuilder.loadTexts: ltp8xLoggingDestinationsTable.setStatus('current')
ltp8xLoggingDestinationsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 14, 1), ).setIndexNames((0, "ELTEX-LTP8X-STANDALONE", "ltp8xLoggingDestinationsId"))
if mibBuilder.loadTexts: ltp8xLoggingDestinationsEntry.setStatus('current')
ltp8xLoggingDestinationsId = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 14, 1, 1), Unsigned32())
if mibBuilder.loadTexts: ltp8xLoggingDestinationsId.setStatus('current')
ltp8xLoggingDestinationsName = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 14, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ltp8xLoggingDestinationsName.setStatus('current')
ltp8xLoggingDestinationsLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 14, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("emergency", 0), ("alert", 1), ("critical", 2), ("error", 3), ("warning", 4), ("notice", 5), ("info", 6), ("debug", 7), ("none", 8)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ltp8xLoggingDestinationsLevel.setStatus('current')
ltp8xInterfaceStatusTable = MibTable((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 15), )
if mibBuilder.loadTexts: ltp8xInterfaceStatusTable.setStatus('current')
ltp8xInterfaceStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 15, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: ltp8xInterfaceStatusEntry.setStatus('current')
ltp8xInterfaceStatusError = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 15, 1, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ltp8xInterfaceStatusError.setStatus('current')
ltp8xInterfaceStatusDuplex = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 15, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("halfDuplex", 0), ("fullDuplex", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ltp8xInterfaceStatusDuplex.setStatus('current')
ltp8xInterfaceStatusFlowControlEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 15, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ltp8xInterfaceStatusFlowControlEnabled.setStatus('current')
ltp8xFanControl = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 16))
ltp8xFanSpeed = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 16, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(-1))).clone(namedValues=NamedValues(("auto", -1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ltp8xFanSpeed.setStatus('current')
ltp8xFanMinSpeed = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 16, 2), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ltp8xFanMinSpeed.setStatus('current')
ltp8xPowerSupplyTable = MibTable((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 17), )
if mibBuilder.loadTexts: ltp8xPowerSupplyTable.setStatus('current')
ltp8xPowerSupplyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 17, 1), ).setIndexNames((0, "ELTEX-LTP8X-STANDALONE", "ltp8xPowerSupplyModuleId"))
if mibBuilder.loadTexts: ltp8xPowerSupplyEntry.setStatus('current')
ltp8xPowerSupplyModuleId = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 17, 1, 1), Unsigned32())
if mibBuilder.loadTexts: ltp8xPowerSupplyModuleId.setStatus('current')
ltp8xPowerSupplyModulePresent = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 17, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ltp8xPowerSupplyModulePresent.setStatus('current')
ltp8xPowerSupplyModuleName = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 17, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ltp8xPowerSupplyModuleName.setStatus('current')
ltp8xPowerSupplyModuleType = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 17, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("directCurrent", 0), ("alternateCurrent", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ltp8xPowerSupplyModuleType.setStatus('current')
ltp8xPowerSupplyModuleIntact = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 17, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ltp8xPowerSupplyModuleIntact.setStatus('current')
ltp8xLicense = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 18))
ltp8xLicenseInstalled = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 18, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ltp8xLicenseInstalled.setStatus('current')
ltp8xLicenseValid = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 18, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ltp8xLicenseValid.setStatus('current')
ltp8xLicenseVersion = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 18, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("version1v0", 0), ("version1v1", 1), ("version1v2", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ltp8xLicenseVersion.setStatus('current')
ltp8xLicenseBoardSN = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 18, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ltp8xLicenseBoardSN.setStatus('current')
ltp8xLicenseVendor = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 18, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ltp8xLicenseVendor.setStatus('current')
ltp8xLicenseONTCount = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 18, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2147483647, -1))).clone(namedValues=NamedValues(("unlimited", 2147483647), ("notAvailable", -1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ltp8xLicenseONTCount.setStatus('current')
ltp8xLicenseActiveONTCount = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 18, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(-1))).clone(namedValues=NamedValues(("notAvailable", -1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ltp8xLicenseActiveONTCount.setStatus('current')
ltp8xLogSize = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 20), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ltp8xLogSize.setStatus('current')
ltp8xExternalFirmwareIP = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 21), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ltp8xExternalFirmwareIP.setStatus('current')
ltp8xExternalFirmwarePort = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 22), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ltp8xExternalFirmwarePort.setStatus('current')
ltp8xNTPDaylightSaving = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 25), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ltp8xNTPDaylightSaving.setStatus('current')
ltp8xONTFwAutoUpdateEnabled = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 26), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ltp8xONTFwAutoUpdateEnabled.setStatus('current')
ltp8xConfigChangeCounter = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 40), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ltp8xConfigChangeCounter.setStatus('current')
ltp8xRereadConfig = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 49), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ltp8xRereadConfig.setStatus('current')
ltp8xSaveConfig = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 50), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ltp8xSaveConfig.setStatus('current')
ltp8xRebootTimeout = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 22, 1, 51), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ltp8xRebootTimeout.setStatus('current')
mibBuilder.exportSymbols("ELTEX-LTP8X-STANDALONE", ltp8xSystemUptime=ltp8xSystemUptime, ltp8xUsersGroupsTable=ltp8xUsersGroupsTable, ltp8xLicenseBoardSN=ltp8xLicenseBoardSN, ltp8xPowerSupplyModuleId=ltp8xPowerSupplyModuleId, ltp8xStandalone=ltp8xStandalone, ltp8xLicenseValid=ltp8xLicenseValid, ltp8xFanMaxRPM=ltp8xFanMaxRPM, ltp8xServicesControlTable=ltp8xServicesControlTable, ltp8xPrivilegesLevelsTable=ltp8xPrivilegesLevelsTable, ltp8xSensor2Temperature=ltp8xSensor2Temperature, ltp8xSaveConfig=ltp8xSaveConfig, ltp8xPrivilegesLevelsLevel=ltp8xPrivilegesLevelsLevel, ltp8xServicesControlEntry=ltp8xServicesControlEntry, ltp8xInterfaceStatusTable=ltp8xInterfaceStatusTable, ltp8xServicesControlName=ltp8xServicesControlName, ltp8xLicenseInstalled=ltp8xLicenseInstalled, ltp8xPowerSupplyTable=ltp8xPowerSupplyTable, ltp8xGateway=ltp8xGateway, ltp8xLogSubmodulesLevel=ltp8xLogSubmodulesLevel, ltp8xLogSubmodulesShowSubmoduleName=ltp8xLogSubmodulesShowSubmoduleName, ltp8xLicenseVendor=ltp8xLicenseVendor, ltp8xPrivilegesNamesName=ltp8xPrivilegesNamesName, ltp8xSystemHardwareRevision=ltp8xSystemHardwareRevision, ltp8xFanSpeed=ltp8xFanSpeed, ltp8xSystemMacAddress=ltp8xSystemMacAddress, ltp8xUsersEntry=ltp8xUsersEntry, ltp8xPowerSupplyModulePresent=ltp8xPowerSupplyModulePresent, ltp8xFanControl=ltp8xFanControl, ltp8xUsersOldPassword=ltp8xUsersOldPassword, ltp8xSensor1TemperatureExt=ltp8xSensor1TemperatureExt, ltp8xLogSubmodulesShowLevel=ltp8xLogSubmodulesShowLevel, ltp8xRAMFree=ltp8xRAMFree, ltp8xActivationAuthModeHostControlledLumpedSN=ltp8xActivationAuthModeHostControlledLumpedSN, ltp8xInterfaceStatusFlowControlEnabled=ltp8xInterfaceStatusFlowControlEnabled, ltp8xUsersName=ltp8xUsersName, ltp8xLogSubmodulesName=ltp8xLogSubmodulesName, ltp8xServicesControlIndex=ltp8xServicesControlIndex, ltp8xFan0Active=ltp8xFan0Active, ltp8xLicense=ltp8xLicense, ltp8xFan0RPM=ltp8xFan0RPM, ltp8xSystemDeviceName=ltp8xSystemDeviceName, ltp8xConfigChangeCounter=ltp8xConfigChangeCounter, ltp8xUsersNewPassword=ltp8xUsersNewPassword, ltp8xUsersGroupsEntry=ltp8xUsersGroupsEntry, ltp8xPowerSupplyModuleIntact=ltp8xPowerSupplyModuleIntact, ltp8xLoggingDestinationsId=ltp8xLoggingDestinationsId, ltp8xLoggingDestinationsEntry=ltp8xLoggingDestinationsEntry, ltp8xLoggingDestinationsLevel=ltp8xLoggingDestinationsLevel, ltp8xCPULoadAverage1Minute=ltp8xCPULoadAverage1Minute, ltp8xUsers=ltp8xUsers, ltp8xRebootTimeout=ltp8xRebootTimeout, ltp8xFan1RPM=ltp8xFan1RPM, ltp8xUsersTable=ltp8xUsersTable, ltp8xSensor2TemperatureExt=ltp8xSensor2TemperatureExt, ltp8xFanMinRPM=ltp8xFanMinRPM, ltp8xLoggingDestinationsTable=ltp8xLoggingDestinationsTable, ltp8xLicenseVersion=ltp8xLicenseVersion, ltp8xPrivilegesLevelsEntry=ltp8xPrivilegesLevelsEntry, ltp8xLogSubmodulesShowTime=ltp8xLogSubmodulesShowTime, ltp8xLogSubmodulesID=ltp8xLogSubmodulesID, ltp8xCPULoadAverage5Minutes=ltp8xCPULoadAverage5Minutes, ltp8xExternalFirmwareIP=ltp8xExternalFirmwareIP, ltp8xServicesControlEnabled=ltp8xServicesControlEnabled, ltp8xPrivilegesLevelsAllowed=ltp8xPrivilegesLevelsAllowed, ltp8xLogSubmodulesEntry=ltp8xLogSubmodulesEntry, ltp8xInterfaceStatusEntry=ltp8xInterfaceStatusEntry, ltp8xLogSubmodulesShowProgName=ltp8xLogSubmodulesShowProgName, ltp8xIPAddress=ltp8xIPAddress, ltp8xONTFwAutoUpdateEnabled=ltp8xONTFwAutoUpdateEnabled, ltp8xUsersGroups=ltp8xUsersGroups, ltp8xDiskFreeSpace=ltp8xDiskFreeSpace, ltp8xPrivilegesNamesTable=ltp8xPrivilegesNamesTable, ltp8xLogSize=ltp8xLogSize, ltp8xLogSubmodulesTable=ltp8xLogSubmodulesTable, ltp8xExternalFirmwarePort=ltp8xExternalFirmwarePort, ltp8xCPULoadAverage15Minutes=ltp8xCPULoadAverage15Minutes, ltp8xFanMinSpeed=ltp8xFanMinSpeed, ltp8xLicenseONTCount=ltp8xLicenseONTCount, ltp8xUsersGroupsName=ltp8xUsersGroupsName, ltp8xFan1Active=ltp8xFan1Active, ltp8xPrivilegesNamesEntry=ltp8xPrivilegesNamesEntry, ltp8xHostName=ltp8xHostName, ltp8xFirmwareRevision=ltp8xFirmwareRevision, ltp8xSystem=ltp8xSystem, ltp8xRereadConfig=ltp8xRereadConfig, ltp8xInterfaceStatusError=ltp8xInterfaceStatusError, ltp8xBoardStatus=ltp8xBoardStatus, ltp8xActivationAuthModeEntry=ltp8xActivationAuthModeEntry, ltp8xLicenseActiveONTCount=ltp8xLicenseActiveONTCount, ltp8xUsersPriority=ltp8xUsersPriority, ltp8xPowerSupplyModuleType=ltp8xPowerSupplyModuleType, ltp8xActivationAuthModeChannel=ltp8xActivationAuthModeChannel, ltp8xLogSubmodulesDestination=ltp8xLogSubmodulesDestination, ltp8xSensor1Temperature=ltp8xSensor1Temperature, ltp8xPowerSupplyEntry=ltp8xPowerSupplyEntry, ltp8xNetMask=ltp8xNetMask, ltp8xInterfaceStatusDuplex=ltp8xInterfaceStatusDuplex, ltp8xUsersGroupsID=ltp8xUsersGroupsID, PYSNMP_MODULE_ID=ltp8xStandalone, ltp8xPowerSupplyModuleName=ltp8xPowerSupplyModuleName, ltp8xActivationAuthModeTable=ltp8xActivationAuthModeTable, ltp8xUsersRowStatus=ltp8xUsersRowStatus, ltp8xLoggingDestinationsName=ltp8xLoggingDestinationsName, ltp8xVLAN=ltp8xVLAN, ltp8xNTPDaylightSaving=ltp8xNTPDaylightSaving, ltp8xPrivilegesNamesIndex=ltp8xPrivilegesNamesIndex)
