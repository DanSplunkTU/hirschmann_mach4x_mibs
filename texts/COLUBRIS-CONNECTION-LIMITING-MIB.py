#
# PySNMP MIB module COLUBRIS-CONNECTION-LIMITING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/hpmsm/COLUBRIS-CONNECTION-LIMITING-MIB.my
# Produced by pysmi-1.1.3 at Sun Nov 21 00:37:18 2021
# On host fv-az39-63 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
colubrisMgmtV2, = mibBuilder.importSymbols("COLUBRIS-SMI", "colubrisMgmtV2")
ColubrisNotificationEnable, = mibBuilder.importSymbols("COLUBRIS-TC", "ColubrisNotificationEnable")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter64, iso, Integer32, TimeTicks, Unsigned32, Bits, NotificationType, Counter32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, IpAddress, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "iso", "Integer32", "TimeTicks", "Unsigned32", "Bits", "NotificationType", "Counter32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "IpAddress", "ModuleIdentity")
DisplayString, TextualConvention, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "MacAddress")
colubrisConnectionLimitingMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 8744, 5, 18))
if mibBuilder.loadTexts: colubrisConnectionLimitingMIB.setLastUpdated('200501210000Z')
if mibBuilder.loadTexts: colubrisConnectionLimitingMIB.setOrganization('Colubris Networks, Inc.')
if mibBuilder.loadTexts: colubrisConnectionLimitingMIB.setContactInfo('Colubris Networks\n                     Postal: 200 West Street Ste 300\n                             Waltham, Massachusetts 02451-1121\n                             UNITED STATES\n                     Phone:  +1 781 684 0001\n                     Fax:    +1 781 684 0009\n\n                     E-mail: cn-snmp@colubris.com')
if mibBuilder.loadTexts: colubrisConnectionLimitingMIB.setDescription('Colubris Networks Connection limiting module.')
colubrisConnectionLimitingMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 18, 1))
connectionLimitingConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 18, 1, 1))
connectionLimitingInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 18, 1, 2))
connectionLimitingMaximumUserConnections = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 18, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(20, 2000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: connectionLimitingMaximumUserConnections.setStatus('current')
if mibBuilder.loadTexts: connectionLimitingMaximumUserConnections.setDescription('Specifies the maximum number of simultaneous connections\n                 allowed for a specific user. If this amount of connections \n                 is reached, no other connections will be allowed\n                 for user and a trap is generated.')
connectionLimitingNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 18, 1, 1, 2), ColubrisNotificationEnable().clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: connectionLimitingNotificationEnabled.setStatus('current')
if mibBuilder.loadTexts: connectionLimitingNotificationEnabled.setDescription('Specifies if connectionLimitingMaximumUserConnectionsReached\n                 notifications are generated.')
connectionLimitingMaximumSystemConnections = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 18, 1, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: connectionLimitingMaximumSystemConnections.setStatus('current')
if mibBuilder.loadTexts: connectionLimitingMaximumSystemConnections.setDescription('Indicates the maximum number of simultaneous connections that\n                 are supported by the device. This is calculated based\n                 on the device type and available memory.')
connectionLimitingUserMACAddress = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 18, 1, 2, 2), MacAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: connectionLimitingUserMACAddress.setStatus('current')
if mibBuilder.loadTexts: connectionLimitingUserMACAddress.setDescription('Specifies the MAC address of the user that has reached the\n                 maximum number of connections.')
connectionLimitingUserIPAddress = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 18, 1, 2, 3), IpAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: connectionLimitingUserIPAddress.setStatus('current')
if mibBuilder.loadTexts: connectionLimitingUserIPAddress.setDescription('Specifies the IP address of the user that has reached the\n                 maximum number of connections.')
colubrisConnectionLimitingMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 18, 2))
colubrisConnectionLimitingMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 18, 2, 0))
connectionLimitingMaximumUserConnectionsReached = NotificationType((1, 3, 6, 1, 4, 1, 8744, 5, 18, 2, 0, 1)).setObjects(("COLUBRIS-CONNECTION-LIMITING-MIB", "connectionLimitingMaximumUserConnections"), ("COLUBRIS-CONNECTION-LIMITING-MIB", "connectionLimitingUserMACAddress"), ("COLUBRIS-CONNECTION-LIMITING-MIB", "connectionLimitingUserIPAddress"))
if mibBuilder.loadTexts: connectionLimitingMaximumUserConnectionsReached.setStatus('current')
if mibBuilder.loadTexts: connectionLimitingMaximumUserConnectionsReached.setDescription('Sent when a user has reached their maximum number of connections.')
colubrisConnectionLimitingMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 18, 3))
colubrisConnectionLimitingMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 18, 3, 1))
colubrisConnectionLimitingMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 18, 3, 2))
colubrisConnectionLimitingMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 8744, 5, 18, 3, 1, 1)).setObjects(("COLUBRIS-CONNECTION-LIMITING-MIB", "colubrisConnectionLimitingConfigMIBGroup"), ("COLUBRIS-CONNECTION-LIMITING-MIB", "colubrisConnectionLimitingInfoMIBGroup"), ("COLUBRIS-CONNECTION-LIMITING-MIB", "colubrisConnectionLimitingNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisConnectionLimitingMIBCompliance = colubrisConnectionLimitingMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: colubrisConnectionLimitingMIBCompliance.setDescription('The compliance statement for entities which implement\n                 the Colubris Networks Tools MIB.')
colubrisConnectionLimitingConfigMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8744, 5, 18, 3, 2, 1)).setObjects(("COLUBRIS-CONNECTION-LIMITING-MIB", "connectionLimitingMaximumUserConnections"), ("COLUBRIS-CONNECTION-LIMITING-MIB", "connectionLimitingNotificationEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisConnectionLimitingConfigMIBGroup = colubrisConnectionLimitingConfigMIBGroup.setStatus('current')
if mibBuilder.loadTexts: colubrisConnectionLimitingConfigMIBGroup.setDescription('A collection of objects providing control over the connection\n                 limiting MIB capability.')
colubrisConnectionLimitingInfoMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8744, 5, 18, 3, 2, 2)).setObjects(("COLUBRIS-CONNECTION-LIMITING-MIB", "connectionLimitingMaximumSystemConnections"), ("COLUBRIS-CONNECTION-LIMITING-MIB", "connectionLimitingUserMACAddress"), ("COLUBRIS-CONNECTION-LIMITING-MIB", "connectionLimitingUserIPAddress"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisConnectionLimitingInfoMIBGroup = colubrisConnectionLimitingInfoMIBGroup.setStatus('current')
if mibBuilder.loadTexts: colubrisConnectionLimitingInfoMIBGroup.setDescription('A collection of objects providing information over the\n                 connection limiting MIB capability.')
colubrisConnectionLimitingNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 8744, 5, 18, 3, 2, 3)).setObjects(("COLUBRIS-CONNECTION-LIMITING-MIB", "connectionLimitingMaximumUserConnectionsReached"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisConnectionLimitingNotificationGroup = colubrisConnectionLimitingNotificationGroup.setStatus('current')
if mibBuilder.loadTexts: colubrisConnectionLimitingNotificationGroup.setDescription('A collection of supported notifications.')
mibBuilder.exportSymbols("COLUBRIS-CONNECTION-LIMITING-MIB", colubrisConnectionLimitingConfigMIBGroup=colubrisConnectionLimitingConfigMIBGroup, connectionLimitingNotificationEnabled=connectionLimitingNotificationEnabled, colubrisConnectionLimitingMIBCompliances=colubrisConnectionLimitingMIBCompliances, colubrisConnectionLimitingNotificationGroup=colubrisConnectionLimitingNotificationGroup, colubrisConnectionLimitingMIBNotificationPrefix=colubrisConnectionLimitingMIBNotificationPrefix, colubrisConnectionLimitingMIB=colubrisConnectionLimitingMIB, connectionLimitingInfo=connectionLimitingInfo, connectionLimitingConfig=connectionLimitingConfig, connectionLimitingMaximumSystemConnections=connectionLimitingMaximumSystemConnections, colubrisConnectionLimitingInfoMIBGroup=colubrisConnectionLimitingInfoMIBGroup, PYSNMP_MODULE_ID=colubrisConnectionLimitingMIB, connectionLimitingMaximumUserConnectionsReached=connectionLimitingMaximumUserConnectionsReached, connectionLimitingUserIPAddress=connectionLimitingUserIPAddress, colubrisConnectionLimitingMIBGroups=colubrisConnectionLimitingMIBGroups, colubrisConnectionLimitingMIBConformance=colubrisConnectionLimitingMIBConformance, colubrisConnectionLimitingMIBNotifications=colubrisConnectionLimitingMIBNotifications, colubrisConnectionLimitingMIBObjects=colubrisConnectionLimitingMIBObjects, colubrisConnectionLimitingMIBCompliance=colubrisConnectionLimitingMIBCompliance, connectionLimitingUserMACAddress=connectionLimitingUserMACAddress, connectionLimitingMaximumUserConnections=connectionLimitingMaximumUserConnections)
