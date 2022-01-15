#
# PySNMP MIB module COLUBRIS-SYSTEM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/hpmsm/COLUBRIS-SYSTEM-MIB.my
# Produced by pysmi-1.1.8 at Sat Jan 15 18:07:39 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
colubrisMgmtV2, = mibBuilder.importSymbols("COLUBRIS-SMI", "colubrisMgmtV2")
ColubrisNotificationEnable, ColubrisAuthenticationMode, ColubrisProfileIndexOrZero = mibBuilder.importSymbols("COLUBRIS-TC", "ColubrisNotificationEnable", "ColubrisAuthenticationMode", "ColubrisProfileIndexOrZero")
ifOutErrors, ifInErrors, ifOutUcastPkts, ifInUcastPkts = mibBuilder.importSymbols("IF-MIB", "ifOutErrors", "ifInErrors", "ifOutUcastPkts", "ifInUcastPkts")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Integer32, MibIdentifier, ModuleIdentity, IpAddress, TimeTicks, Counter32, Unsigned32, Gauge32, Bits, NotificationType, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibIdentifier", "ModuleIdentity", "IpAddress", "TimeTicks", "Counter32", "Unsigned32", "Gauge32", "Bits", "NotificationType", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ObjectIdentity")
TruthValue, MacAddress, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "MacAddress", "DisplayString", "TextualConvention")
colubrisSystemMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 8744, 5, 6))
if mibBuilder.loadTexts: colubrisSystemMIB.setLastUpdated('200703200000Z')
if mibBuilder.loadTexts: colubrisSystemMIB.setOrganization('Colubris Networks, Inc.')
if mibBuilder.loadTexts: colubrisSystemMIB.setContactInfo('Colubris Networks\n                     Postal: 200 West Street Ste 300\n                             Waltham, Massachusetts 02451-1121\n                             UNITED STATES\n                     Phone:  +1 781 684 0001\n                     Fax:    +1 781 684 0009\n\n                     E-mail: cn-snmp@colubris.com')
if mibBuilder.loadTexts: colubrisSystemMIB.setDescription('Generic system information for Colubris Networks devices.')
colubrisSystemMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 6, 1))
systemInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 6, 1, 1))
systemTime = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 6, 1, 2))
adminAccess = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 6, 1, 3))
heartbeat = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 6, 1, 4))
systemProductName = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 6, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemProductName.setStatus('current')
if mibBuilder.loadTexts: systemProductName.setDescription('Colubris Networks product name for the device.')
systemFirmwareRevision = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 6, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemFirmwareRevision.setStatus('current')
if mibBuilder.loadTexts: systemFirmwareRevision.setDescription('Revision number of the device firmware.')
systemBootRevision = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 6, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemBootRevision.setStatus('current')
if mibBuilder.loadTexts: systemBootRevision.setDescription('Revision number of the device boot loader.')
systemHardwareRevision = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 6, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemHardwareRevision.setStatus('current')
if mibBuilder.loadTexts: systemHardwareRevision.setDescription('Revision number of the system hardware.')
systemSerialNumber = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 6, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemSerialNumber.setStatus('current')
if mibBuilder.loadTexts: systemSerialNumber.setDescription('Device serial number.')
systemConfigurationVersion = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 6, 1, 1, 6), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemConfigurationVersion.setStatus('current')
if mibBuilder.loadTexts: systemConfigurationVersion.setDescription('User-defined string to identify the current device\n                 configuration. This string could be anything in printable\n                 ASCII characters.')
systemUpTime = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 6, 1, 1, 7), Counter32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: systemUpTime.setStatus('current')
if mibBuilder.loadTexts: systemUpTime.setDescription('How long the system has been running since its last restart. \n                 When this counter reaches its maximum value, it wraps\n                 around and starts increasing again from zero.')
systemMacAddress = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 6, 1, 1, 8), MacAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: systemMacAddress.setStatus('current')
if mibBuilder.loadTexts: systemMacAddress.setDescription('MAC address of the device. This information is \n                 only returned in a systemHeartbeatNotification event.')
systemWanPortIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 6, 1, 1, 9), IpAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: systemWanPortIpAddress.setStatus('current')
if mibBuilder.loadTexts: systemWanPortIpAddress.setDescription('IP address of the device WAN port. This information is \n                 only returned in a systemHeartbeatNotification event.')
systemProductFlavor = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 6, 1, 1, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemProductFlavor.setStatus('current')
if mibBuilder.loadTexts: systemProductFlavor.setDescription('The product flavor can extends or alter the\n                 functionality of a Colubris product.')
systemDeviceIdentification = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 6, 1, 1, 11), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemDeviceIdentification.setStatus('current')
if mibBuilder.loadTexts: systemDeviceIdentification.setDescription('Manufacturing Ethernet base MAC address.')
systemTimeUpdateMode = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 6, 1, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("manual", 1), ("sntpUdp", 2), ("tp", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemTimeUpdateMode.setStatus('current')
if mibBuilder.loadTexts: systemTimeUpdateMode.setDescription("Specifies the method and format used to set the system time.\n\n                  'manual': Operator must configures the system time\n                            parameters manually in the GMT zone.\n\n                  'sntpUdp': Look for time servers in the\n                             systemTimeServerTable in order to synchronize\n                             the device system time using SNTP.\n\n                  'tp': Look for time servers in the systemTimeServerTable\n                        in order to synchronize the device system time using\n                        the Time Protocol.")
systemTimeLostWhenRebooting = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 6, 1, 2, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemTimeLostWhenRebooting.setStatus('current')
if mibBuilder.loadTexts: systemTimeLostWhenRebooting.setDescription("Indicates if the system time is lost after rebooting or not.\n                   'true': Indicates that the system time has been lost,\n                   'false': Indicates that the system time has been kept.")
systemTimeDSTOn = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 6, 1, 2, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemTimeDSTOn.setStatus('current')
if mibBuilder.loadTexts: systemTimeDSTOn.setDescription("Specifies if the system time need to be adjusted to compensate\n                 for daylight savings.\n\n                  'true': Adjusts the system time by adding one hour.\n\n                  'false': Keep the current system time.")
systemDate = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 6, 1, 2, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(10, 10)).setFixedLength(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemDate.setStatus('current')
if mibBuilder.loadTexts: systemDate.setDescription("Specifies the current GMT system date when \n                systemTimeUpdateMode attribute is set to 'manual' mode.\n                Reading this attributes will return the current date.\n\n                Specify year (1995-3000), month (01-12), and day (01-31)\n                in the format YYYY/MM/DD. The '/' character is mandatory\n                between the fields.")
systemTimeOfDay = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 6, 1, 2, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemTimeOfDay.setStatus('current')
if mibBuilder.loadTexts: systemTimeOfDay.setDescription("Specifies the current GMT system time when \n                 systemTimeUpdateMode attribute is set to 'manual' mode.\n                 Specify hour (00-24), minutes (00-59), and seconds (00-59)\n                 in the format HH:MM:SS. The ':' character is mandatory \n                 between the fields.")
systemTimeZone = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 6, 1, 2, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemTimeZone.setStatus('current')
if mibBuilder.loadTexts: systemTimeZone.setDescription("Specifies the current system time zone in the \n                 relation to UTC. Specify the direction from UTC (+ or -),\n                 hours from UTC (00-14 or 00-12), and minutes from UTC\n                 (00 or 30) in the format +/-HH:MM.\n\n                 The '+' or '-' character is mandatory at the beginning\n                 of the expression. The ':' character is mandatory between \n                 the time fields.")
systemTimeServerTable = MibTable((1, 3, 6, 1, 4, 1, 8744, 5, 6, 1, 2, 7), )
if mibBuilder.loadTexts: systemTimeServerTable.setStatus('current')
if mibBuilder.loadTexts: systemTimeServerTable.setDescription('A table containing the list of SNTP time servers that can\n                 be used to synchronize the device system time. In tabular\n                 form to allow multiple instances on an agent.')
systemTimeServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8744, 5, 6, 1, 2, 7, 1), ).setIndexNames((0, "COLUBRIS-SYSTEM-MIB", "systemTimeServerIndex"))
if mibBuilder.loadTexts: systemTimeServerEntry.setStatus('current')
if mibBuilder.loadTexts: systemTimeServerEntry.setDescription('A SNTP time server used to get the device time.\n                 systemTimeServerIndex - Uniquely identifies a time server in\n                                         the table.')
systemTimeServerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 6, 1, 2, 7, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 20)))
if mibBuilder.loadTexts: systemTimeServerIndex.setStatus('current')
if mibBuilder.loadTexts: systemTimeServerIndex.setDescription('Index of the time server in the systemTimeServerTable.')
systemTimeServerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 6, 1, 2, 7, 1, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemTimeServerAddress.setStatus('current')
if mibBuilder.loadTexts: systemTimeServerAddress.setDescription('Specifies the DNS name or IP address of the time server to use.\n                 Setting an entry to a null string will delete the entry.')
systemTimeServerNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 6, 1, 2, 8), ColubrisNotificationEnable()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemTimeServerNotificationEnabled.setStatus('current')
if mibBuilder.loadTexts: systemTimeServerNotificationEnabled.setDescription('Specifies if timeServerFailure notifications are generated.')
adminAccessAuthenMode = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 6, 1, 3, 1), ColubrisAuthenticationMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adminAccessAuthenMode.setStatus('current')
if mibBuilder.loadTexts: adminAccessAuthenMode.setDescription('Specifies if administrator authentication is performed\n                 locally or via an AAA server. You must have configured an \n                 AAA profile and the adminAccessAuthenProfileIndex attribute \n                 before you can select a profile or an error will be returned.')
adminAccessAuthenProfileIndex = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 6, 1, 3, 2), ColubrisProfileIndexOrZero()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adminAccessAuthenProfileIndex.setStatus('current')
if mibBuilder.loadTexts: adminAccessAuthenProfileIndex.setDescription("Specifies the AAA profile to be used in order to\n                 authenticate the administrator. This parameter\n                 only applies when the adminAccessAuthenMode\n                 is set to 'profile'. When the special value zero is \n                 specified, no AAA server profile is selected.")
adminAccessMaxLoginAttempts = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 6, 1, 3, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32767))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adminAccessMaxLoginAttempts.setStatus('current')
if mibBuilder.loadTexts: adminAccessMaxLoginAttempts.setDescription('Specifies the number of successive unsuccessful authentications\n                 that must occur to generate an\n                 adminAccessAuthFailureNotification event.')
adminAccessLockOutPeriod = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 6, 1, 3, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 60))).setUnits('minutes').setMaxAccess("readwrite")
if mibBuilder.loadTexts: adminAccessLockOutPeriod.setStatus('current')
if mibBuilder.loadTexts: adminAccessLockOutPeriod.setDescription('Specifies the duration when further login attempts are blocked\n                 after adminAccessMaxLoginAttempts has been reached.\n                 Setting this value to zero disables the lock out\n                 feature.')
adminAccessLoginNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 6, 1, 3, 5), ColubrisNotificationEnable().clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adminAccessLoginNotificationEnabled.setStatus('current')
if mibBuilder.loadTexts: adminAccessLoginNotificationEnabled.setDescription('Specifies if an adminAccessLoginNotification event is generated\n                 after an administrator is successfully authenticated.')
adminAccessAuthFailureNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 6, 1, 3, 6), ColubrisNotificationEnable().clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adminAccessAuthFailureNotificationEnabled.setStatus('current')
if mibBuilder.loadTexts: adminAccessAuthFailureNotificationEnabled.setDescription('Specifies if an adminAccessAuthFailureNotification event is\n                 generated when the number of successive unsuccessful\n                 authentications attempts exceed the value of\n                 adminAccessMaxLoginAttempts.')
adminAccessInfo = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 6, 1, 3, 7), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: adminAccessInfo.setStatus('current')
if mibBuilder.loadTexts: adminAccessInfo.setDescription('Contains various information about the administrator.\n                 This parameter is used in the adminAccessAuthFailureNotification\n                 event to return the administrator status to a management system.')
adminAccessProfileTable = MibTable((1, 3, 6, 1, 4, 1, 8744, 5, 6, 1, 3, 8), )
if mibBuilder.loadTexts: adminAccessProfileTable.setStatus('current')
if mibBuilder.loadTexts: adminAccessProfileTable.setDescription('This table handles the profile of several administrator users.\n                 In tabular form in order to allow multiple instances on an\n                 agent.')
adminAccessProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8744, 5, 6, 1, 3, 8, 1), ).setIndexNames((0, "COLUBRIS-SYSTEM-MIB", "adminAccessProfileIndex"))
if mibBuilder.loadTexts: adminAccessProfileEntry.setStatus('current')
if mibBuilder.loadTexts: adminAccessProfileEntry.setDescription('An administrator profile configured in the administrator\n                 access table.')
adminAccessProfileIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 6, 1, 3, 8, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: adminAccessProfileIndex.setStatus('current')
if mibBuilder.loadTexts: adminAccessProfileIndex.setDescription('Specifies the index of the administrator profile.')
adminAccessUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 6, 1, 3, 8, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 253))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adminAccessUserName.setStatus('current')
if mibBuilder.loadTexts: adminAccessUserName.setDescription('Specifies the user name of the administrator.')
adminAccessAdministrativeRights = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 6, 1, 3, 8, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("readOnly", 1), ("readWrite", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adminAccessAdministrativeRights.setStatus('current')
if mibBuilder.loadTexts: adminAccessAdministrativeRights.setDescription('Specifies the administrative rights of this specific\n                 administrator.')
adminAccessLogoutNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 6, 1, 3, 9), ColubrisNotificationEnable().clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adminAccessLogoutNotificationEnabled.setStatus('current')
if mibBuilder.loadTexts: adminAccessLogoutNotificationEnabled.setDescription('Specifies if an adminAccessLogoutNotification event is generated\n                 after an administrator logs out from the web interface.')
heartbeatPeriod = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 6, 1, 4, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(30, 31536000))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: heartbeatPeriod.setStatus('current')
if mibBuilder.loadTexts: heartbeatPeriod.setDescription('Specifies the delay between 2 heartbeat notifications.\n                 The range of this parameter is 30 seconds to 1 year.')
heartbeatNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 6, 1, 4, 2), ColubrisNotificationEnable().clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: heartbeatNotificationEnabled.setStatus('current')
if mibBuilder.loadTexts: heartbeatNotificationEnabled.setDescription('Specifies if systemHeartbeatNotification events are\n                 generated.')
colubrisSystemMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 6, 2))
colubrisSystemMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 6, 2, 0))
adminAccessAuthFailureNotification = NotificationType((1, 3, 6, 1, 4, 1, 8744, 5, 6, 2, 0, 1)).setObjects(("COLUBRIS-SYSTEM-MIB", "adminAccessInfo"))
if mibBuilder.loadTexts: adminAccessAuthFailureNotification.setStatus('current')
if mibBuilder.loadTexts: adminAccessAuthFailureNotification.setDescription('Sent after an administrator authentication failure.')
adminAccessLoginNotification = NotificationType((1, 3, 6, 1, 4, 1, 8744, 5, 6, 2, 0, 2))
if mibBuilder.loadTexts: adminAccessLoginNotification.setStatus('current')
if mibBuilder.loadTexts: adminAccessLoginNotification.setDescription('Sent after an administrator is successfully authenticated.')
systemColdStart = NotificationType((1, 3, 6, 1, 4, 1, 8744, 5, 6, 2, 0, 3)).setObjects(("COLUBRIS-SYSTEM-MIB", "systemProductName"), ("COLUBRIS-SYSTEM-MIB", "systemFirmwareRevision"), ("COLUBRIS-SYSTEM-MIB", "systemConfigurationVersion"), ("COLUBRIS-SYSTEM-MIB", "systemSerialNumber"))
if mibBuilder.loadTexts: systemColdStart.setStatus('current')
if mibBuilder.loadTexts: systemColdStart.setDescription('Sent at system boot up.')
systemHeartbeatNotification = NotificationType((1, 3, 6, 1, 4, 1, 8744, 5, 6, 2, 0, 4)).setObjects(("COLUBRIS-SYSTEM-MIB", "systemSerialNumber"), ("COLUBRIS-SYSTEM-MIB", "systemMacAddress"), ("COLUBRIS-SYSTEM-MIB", "systemWanPortIpAddress"), ("COLUBRIS-SYSTEM-MIB", "systemUpTime"), ("IF-MIB", "ifOutUcastPkts"), ("IF-MIB", "ifInUcastPkts"), ("IF-MIB", "ifOutErrors"), ("IF-MIB", "ifInErrors"), ("IF-MIB", "ifOutUcastPkts"), ("IF-MIB", "ifInUcastPkts"), ("IF-MIB", "ifOutErrors"), ("IF-MIB", "ifInErrors"), ("IF-MIB", "ifOutUcastPkts"), ("IF-MIB", "ifInUcastPkts"), ("IF-MIB", "ifOutErrors"), ("IF-MIB", "ifInErrors"))
if mibBuilder.loadTexts: systemHeartbeatNotification.setStatus('current')
if mibBuilder.loadTexts: systemHeartbeatNotification.setDescription('Sent every heartbeatPeriod.')
adminAccessLogoutNotification = NotificationType((1, 3, 6, 1, 4, 1, 8744, 5, 6, 2, 0, 5)).setObjects(("COLUBRIS-SYSTEM-MIB", "adminAccessInfo"))
if mibBuilder.loadTexts: adminAccessLogoutNotification.setStatus('current')
if mibBuilder.loadTexts: adminAccessLogoutNotification.setDescription('Sent after an administrator has logout.')
timeServerFailure = NotificationType((1, 3, 6, 1, 4, 1, 8744, 5, 6, 2, 0, 6)).setObjects(("COLUBRIS-SYSTEM-MIB", "systemTimeServerAddress"))
if mibBuilder.loadTexts: timeServerFailure.setStatus('current')
if mibBuilder.loadTexts: timeServerFailure.setDescription('Sent when a time server of the system time table is unreachable.')
colubrisSystemMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 6, 3))
colubrisSystemMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 6, 3, 1))
colubrisSystemMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 6, 3, 2))
colubrisSystemMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 8744, 5, 6, 3, 1, 1)).setObjects(("COLUBRIS-SYSTEM-MIB", "colubrisSystemMIBGroup"), ("COLUBRIS-SYSTEM-MIB", "colubrisSystemNotificationGroup"), ("COLUBRIS-SYSTEM-MIB", "colubrisAdminAccessProfileGroup"), ("COLUBRIS-SYSTEM-MIB", "colubrisAdminAccessNotificationGroup"), ("COLUBRIS-SYSTEM-MIB", "colubrisTimeNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisSystemMIBCompliance = colubrisSystemMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: colubrisSystemMIBCompliance.setDescription('The compliance statement for entities which implement the\n                 Colubris Networks System MIB.')
colubrisSystemMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8744, 5, 6, 3, 2, 1)).setObjects(("COLUBRIS-SYSTEM-MIB", "systemProductName"), ("COLUBRIS-SYSTEM-MIB", "systemFirmwareRevision"), ("COLUBRIS-SYSTEM-MIB", "systemBootRevision"), ("COLUBRIS-SYSTEM-MIB", "systemHardwareRevision"), ("COLUBRIS-SYSTEM-MIB", "systemSerialNumber"), ("COLUBRIS-SYSTEM-MIB", "systemConfigurationVersion"), ("COLUBRIS-SYSTEM-MIB", "systemUpTime"), ("COLUBRIS-SYSTEM-MIB", "systemMacAddress"), ("COLUBRIS-SYSTEM-MIB", "systemWanPortIpAddress"), ("COLUBRIS-SYSTEM-MIB", "systemProductFlavor"), ("COLUBRIS-SYSTEM-MIB", "systemDeviceIdentification"), ("COLUBRIS-SYSTEM-MIB", "systemTimeUpdateMode"), ("COLUBRIS-SYSTEM-MIB", "systemTimeLostWhenRebooting"), ("COLUBRIS-SYSTEM-MIB", "systemTimeDSTOn"), ("COLUBRIS-SYSTEM-MIB", "systemDate"), ("COLUBRIS-SYSTEM-MIB", "systemTimeOfDay"), ("COLUBRIS-SYSTEM-MIB", "systemTimeZone"), ("COLUBRIS-SYSTEM-MIB", "systemTimeServerAddress"), ("COLUBRIS-SYSTEM-MIB", "systemTimeServerNotificationEnabled"), ("COLUBRIS-SYSTEM-MIB", "heartbeatPeriod"), ("COLUBRIS-SYSTEM-MIB", "heartbeatNotificationEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisSystemMIBGroup = colubrisSystemMIBGroup.setStatus('current')
if mibBuilder.loadTexts: colubrisSystemMIBGroup.setDescription('A collection of objects providing the System MIB capability.')
colubrisAdminAccessProfileGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8744, 5, 6, 3, 2, 2)).setObjects(("COLUBRIS-SYSTEM-MIB", "adminAccessAuthenMode"), ("COLUBRIS-SYSTEM-MIB", "adminAccessMaxLoginAttempts"), ("COLUBRIS-SYSTEM-MIB", "adminAccessLockOutPeriod"), ("COLUBRIS-SYSTEM-MIB", "adminAccessLoginNotificationEnabled"), ("COLUBRIS-SYSTEM-MIB", "adminAccessAuthFailureNotificationEnabled"), ("COLUBRIS-SYSTEM-MIB", "adminAccessAuthenProfileIndex"), ("COLUBRIS-SYSTEM-MIB", "adminAccessInfo"), ("COLUBRIS-SYSTEM-MIB", "adminAccessUserName"), ("COLUBRIS-SYSTEM-MIB", "adminAccessAdministrativeRights"), ("COLUBRIS-SYSTEM-MIB", "adminAccessLogoutNotificationEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisAdminAccessProfileGroup = colubrisAdminAccessProfileGroup.setStatus('current')
if mibBuilder.loadTexts: colubrisAdminAccessProfileGroup.setDescription('A collection of objects providing the administrator access\n                 configuration capability.')
colubrisSystemNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 8744, 5, 6, 3, 2, 3)).setObjects(("COLUBRIS-SYSTEM-MIB", "systemColdStart"), ("COLUBRIS-SYSTEM-MIB", "systemHeartbeatNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisSystemNotificationGroup = colubrisSystemNotificationGroup.setStatus('current')
if mibBuilder.loadTexts: colubrisSystemNotificationGroup.setDescription('A collection of supported notifications')
colubrisAdminAccessNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 8744, 5, 6, 3, 2, 4)).setObjects(("COLUBRIS-SYSTEM-MIB", "adminAccessAuthFailureNotification"), ("COLUBRIS-SYSTEM-MIB", "adminAccessLoginNotification"), ("COLUBRIS-SYSTEM-MIB", "adminAccessLogoutNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisAdminAccessNotificationGroup = colubrisAdminAccessNotificationGroup.setStatus('current')
if mibBuilder.loadTexts: colubrisAdminAccessNotificationGroup.setDescription('A collection of supported notifications')
colubrisTimeNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 8744, 5, 6, 3, 2, 5)).setObjects(("COLUBRIS-SYSTEM-MIB", "timeServerFailure"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisTimeNotificationGroup = colubrisTimeNotificationGroup.setStatus('current')
if mibBuilder.loadTexts: colubrisTimeNotificationGroup.setDescription('A collection of supported notifications')
mibBuilder.exportSymbols("COLUBRIS-SYSTEM-MIB", heartbeat=heartbeat, systemProductName=systemProductName, systemTimeZone=systemTimeZone, systemDate=systemDate, adminAccessAuthenProfileIndex=adminAccessAuthenProfileIndex, adminAccessProfileEntry=adminAccessProfileEntry, colubrisSystemMIBNotifications=colubrisSystemMIBNotifications, colubrisSystemMIBNotificationPrefix=colubrisSystemMIBNotificationPrefix, adminAccessAdministrativeRights=adminAccessAdministrativeRights, systemTimeUpdateMode=systemTimeUpdateMode, systemTimeServerTable=systemTimeServerTable, colubrisSystemMIBGroups=colubrisSystemMIBGroups, systemMacAddress=systemMacAddress, systemDeviceIdentification=systemDeviceIdentification, systemBootRevision=systemBootRevision, heartbeatNotificationEnabled=heartbeatNotificationEnabled, adminAccessInfo=adminAccessInfo, adminAccessLockOutPeriod=adminAccessLockOutPeriod, heartbeatPeriod=heartbeatPeriod, systemColdStart=systemColdStart, systemTimeServerEntry=systemTimeServerEntry, systemSerialNumber=systemSerialNumber, PYSNMP_MODULE_ID=colubrisSystemMIB, timeServerFailure=timeServerFailure, colubrisSystemMIB=colubrisSystemMIB, systemTimeOfDay=systemTimeOfDay, colubrisAdminAccessNotificationGroup=colubrisAdminAccessNotificationGroup, adminAccessLoginNotificationEnabled=adminAccessLoginNotificationEnabled, colubrisSystemMIBObjects=colubrisSystemMIBObjects, colubrisAdminAccessProfileGroup=colubrisAdminAccessProfileGroup, adminAccessLogoutNotificationEnabled=adminAccessLogoutNotificationEnabled, colubrisSystemNotificationGroup=colubrisSystemNotificationGroup, adminAccessLogoutNotification=adminAccessLogoutNotification, systemTimeLostWhenRebooting=systemTimeLostWhenRebooting, colubrisTimeNotificationGroup=colubrisTimeNotificationGroup, systemTimeDSTOn=systemTimeDSTOn, systemTimeServerAddress=systemTimeServerAddress, systemHeartbeatNotification=systemHeartbeatNotification, systemFirmwareRevision=systemFirmwareRevision, systemTimeServerNotificationEnabled=systemTimeServerNotificationEnabled, adminAccessMaxLoginAttempts=adminAccessMaxLoginAttempts, adminAccessProfileTable=adminAccessProfileTable, systemInfo=systemInfo, systemUpTime=systemUpTime, colubrisSystemMIBCompliances=colubrisSystemMIBCompliances, adminAccessProfileIndex=adminAccessProfileIndex, colubrisSystemMIBCompliance=colubrisSystemMIBCompliance, systemTimeServerIndex=systemTimeServerIndex, adminAccessAuthFailureNotificationEnabled=adminAccessAuthFailureNotificationEnabled, adminAccess=adminAccess, systemWanPortIpAddress=systemWanPortIpAddress, systemHardwareRevision=systemHardwareRevision, systemConfigurationVersion=systemConfigurationVersion, systemProductFlavor=systemProductFlavor, adminAccessAuthFailureNotification=adminAccessAuthFailureNotification, systemTime=systemTime, adminAccessLoginNotification=adminAccessLoginNotification, adminAccessUserName=adminAccessUserName, colubrisSystemMIBGroup=colubrisSystemMIBGroup, colubrisSystemMIBConformance=colubrisSystemMIBConformance, adminAccessAuthenMode=adminAccessAuthenMode)
