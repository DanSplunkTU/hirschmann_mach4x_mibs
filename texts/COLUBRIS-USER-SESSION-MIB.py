#
# PySNMP MIB module COLUBRIS-USER-SESSION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/hpmsm/COLUBRIS-USER-SESSION-MIB.my
# Produced by pysmi-1.1.8 at Fri Jan  7 16:25:17 2022
# On host fv-az36-988 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
colubrisMgmtV2, = mibBuilder.importSymbols("COLUBRIS-SMI", "colubrisMgmtV2")
ColubrisSSIDOrNone, = mibBuilder.importSymbols("COLUBRIS-TC", "ColubrisSSIDOrNone")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Unsigned32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, NotificationType, Bits, IpAddress, iso, Integer32, MibIdentifier, ObjectIdentity, ModuleIdentity, TimeTicks, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "NotificationType", "Bits", "IpAddress", "iso", "Integer32", "MibIdentifier", "ObjectIdentity", "ModuleIdentity", "TimeTicks", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
colubrisUserSessionMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 8744, 5, 36))
if mibBuilder.loadTexts: colubrisUserSessionMIB.setLastUpdated('200703050000Z')
if mibBuilder.loadTexts: colubrisUserSessionMIB.setOrganization('Colubris Networks, Inc.')
if mibBuilder.loadTexts: colubrisUserSessionMIB.setContactInfo('Colubris Networks\n                     Postal: 200 West Street Ste 300\n                             Waltham, Massachusetts 02451-1121\n                             UNITED STATES\n                     Phone:  +1 781 684 0001\n                     Fax:    +1 781 684 0009\n\n                     E-mail: cn-snmp@colubris.com')
if mibBuilder.loadTexts: colubrisUserSessionMIB.setDescription('Colubris Networks User Session MIB.')
colubrisUserSessionMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 36, 1))
coUserSessionInfoGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 36, 1, 1))
coUserSessionStGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 36, 1, 2))
coUserSessACUserMaxCount = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 36, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coUserSessACUserMaxCount.setStatus('current')
if mibBuilder.loadTexts: coUserSessACUserMaxCount.setDescription('Indicates the maximum number of concurrent\n                 authenticated AC users.')
coUserSessNonACUserMaxCount = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 36, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coUserSessNonACUserMaxCount.setStatus('current')
if mibBuilder.loadTexts: coUserSessNonACUserMaxCount.setDescription('Indicates the maximum number of concurrent\n                 authenticated non AC users.')
coUserSessACUserCount = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 36, 1, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coUserSessACUserCount.setStatus('current')
if mibBuilder.loadTexts: coUserSessACUserCount.setDescription('Indicates the number of currently authenticated AC users.')
coUserSessNonACUserCount = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 36, 1, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coUserSessNonACUserCount.setStatus('current')
if mibBuilder.loadTexts: coUserSessNonACUserCount.setDescription('Indicates the number of currently authenticated non AC users.')
coUserSessionTable = MibTable((1, 3, 6, 1, 4, 1, 8744, 5, 36, 1, 2, 1), )
if mibBuilder.loadTexts: coUserSessionTable.setStatus('current')
if mibBuilder.loadTexts: coUserSessionTable.setDescription('A table containing specific information for users authenticated\n                 (AC and non-AC) by the authentication system.')
coUserSessionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8744, 5, 36, 1, 2, 1, 1), ).setIndexNames((0, "COLUBRIS-USER-SESSION-MIB", "coUserSessIndex"))
if mibBuilder.loadTexts: coUserSessionEntry.setStatus('current')
if mibBuilder.loadTexts: coUserSessionEntry.setDescription('Information about a particular user that has been authenticated\n                 by the authentication system.\n                 coUserSessIndex - Uniquely identifies a user in the table.')
coUserSessIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 36, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: coUserSessIndex.setStatus('current')
if mibBuilder.loadTexts: coUserSessIndex.setDescription('Index of a user in the coUserSessionTable.')
coUserSessUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 36, 1, 2, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 252))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coUserSessUserName.setStatus('current')
if mibBuilder.loadTexts: coUserSessUserName.setDescription("Indicates the user's name.")
coUserSessClientIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 36, 1, 2, 1, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coUserSessClientIpAddress.setStatus('current')
if mibBuilder.loadTexts: coUserSessClientIpAddress.setDescription("Indicates the user's IP address.")
coUserSessSessionDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 36, 1, 2, 1, 1, 4), Counter32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: coUserSessSessionDuration.setStatus('current')
if mibBuilder.loadTexts: coUserSessSessionDuration.setDescription("Indicates how long the user's session has been active.\n                 When this counter reaches its maximum value, it wraps\n                 around and starts increasing again from zero.")
coUserSessIdleTime = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 36, 1, 2, 1, 1, 5), Counter32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: coUserSessIdleTime.setStatus('current')
if mibBuilder.loadTexts: coUserSessIdleTime.setDescription("Indicates for how long the user's session has been idle.\n                 When this counter reaches its maximum value, it wraps\n                 around and starts increasing again from zero.")
coUserSessMAPGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 36, 1, 2, 1, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coUserSessMAPGroupName.setStatus('current')
if mibBuilder.loadTexts: coUserSessMAPGroupName.setDescription("Indicates the user's MultiService Access Point Group\n                 Name.")
coUserSessVSCName = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 36, 1, 2, 1, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coUserSessVSCName.setStatus('current')
if mibBuilder.loadTexts: coUserSessVSCName.setDescription("Indicates the user's Virtual Service Community Name.")
coUserSessSSID = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 36, 1, 2, 1, 1, 8), ColubrisSSIDOrNone()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coUserSessSSID.setStatus('current')
if mibBuilder.loadTexts: coUserSessSSID.setDescription("Indicates the user's Access Point SSID (ONLY when\n                 Location-aware is enabled and properly configured).\n                 If this information is not available, a zero-Length\n                 string is returned.")
coUserSessVLAN = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 36, 1, 2, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4094))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coUserSessVLAN.setStatus('current')
if mibBuilder.loadTexts: coUserSessVLAN.setDescription('Specifies the VLAN currently assigned to the user.')
coUserSessPHYType = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 36, 1, 2, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("unknown", 0), ("ieee802dot11a", 1), ("ieee802dot11b", 2), ("ieee802dot11g", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coUserSessPHYType.setStatus('current')
if mibBuilder.loadTexts: coUserSessPHYType.setDescription("Specifies the user's radio type.")
coUserSessAuthType = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 36, 1, 2, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ac", 1), ("nonAc", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coUserSessAuthType.setStatus('current')
if mibBuilder.loadTexts: coUserSessAuthType.setDescription("User's authentication type.")
coUserSessCalledStationID = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 36, 1, 2, 1, 1, 12), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 252))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coUserSessCalledStationID.setStatus('current')
if mibBuilder.loadTexts: coUserSessCalledStationID.setDescription("Indicates the user's called station ID.")
coUserSessCallingStationID = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 36, 1, 2, 1, 1, 13), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 252))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coUserSessCallingStationID.setStatus('current')
if mibBuilder.loadTexts: coUserSessCallingStationID.setDescription("Indicates the user's calling station ID.")
coUserSessRADIUSServerProfileName = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 36, 1, 2, 1, 1, 14), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 40))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coUserSessRADIUSServerProfileName.setStatus('current')
if mibBuilder.loadTexts: coUserSessRADIUSServerProfileName.setDescription('Indicates the RADIUS server profile name used to\n                 authenticate the user.')
coUserSessRADIUSServerIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 36, 1, 2, 1, 1, 15), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coUserSessRADIUSServerIpAddress.setStatus('current')
if mibBuilder.loadTexts: coUserSessRADIUSServerIpAddress.setDescription('Indicates the RADIUS server IP address used to\n                 authenticate the user.')
coUserSessBytesSent = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 36, 1, 2, 1, 1, 16), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coUserSessBytesSent.setStatus('current')
if mibBuilder.loadTexts: coUserSessBytesSent.setDescription('Indicates the total number of bytes sent by the user.\n                 When this counter reaches its maximum value, it wraps\n                 around and starts increasing again from zero.')
coUserSessBytesReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 36, 1, 2, 1, 1, 17), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coUserSessBytesReceived.setStatus('current')
if mibBuilder.loadTexts: coUserSessBytesReceived.setDescription('Indicates the total number of bytes received by the user.\n                 When this counter reaches its maximum value, it wraps\n                 around and starts increasing again from zero.')
coUserSessPacketsSent = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 36, 1, 2, 1, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coUserSessPacketsSent.setStatus('current')
if mibBuilder.loadTexts: coUserSessPacketsSent.setDescription('Indicates the total number of IP packets sent by the user.\n                 When this counter reaches its maximum value, it wraps\n                 around and starts increasing again from zero.')
coUserSessPacketsReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 36, 1, 2, 1, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coUserSessPacketsReceived.setStatus('current')
if mibBuilder.loadTexts: coUserSessPacketsReceived.setDescription('Indicates the total number of IP packets received by the user.\n                 When this counter reaches its maximum value, it wraps\n                 around and starts increasing again from zero.')
userSessionMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 36, 2))
userSessionMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 36, 2, 0))
colubrisUserSessionMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 36, 3))
colubrisUserSessionMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 36, 3, 1))
colubrisUserSessionMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 36, 3, 2))
colubrisUserSessionMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 8744, 5, 36, 3, 1, 1)).setObjects(("COLUBRIS-USER-SESSION-MIB", "colubrisUserSessionInfoMIBGroup"), ("COLUBRIS-USER-SESSION-MIB", "colubrisUserSessionStMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisUserSessionMIBCompliance = colubrisUserSessionMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: colubrisUserSessionMIBCompliance.setDescription('The compliance statement for entities which implement\n                 the Colubris User Session MIB.')
colubrisUserSessionInfoMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8744, 5, 36, 3, 2, 1)).setObjects(("COLUBRIS-USER-SESSION-MIB", "coUserSessACUserMaxCount"), ("COLUBRIS-USER-SESSION-MIB", "coUserSessNonACUserMaxCount"), ("COLUBRIS-USER-SESSION-MIB", "coUserSessACUserCount"), ("COLUBRIS-USER-SESSION-MIB", "coUserSessNonACUserCount"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisUserSessionInfoMIBGroup = colubrisUserSessionInfoMIBGroup.setStatus('current')
if mibBuilder.loadTexts: colubrisUserSessionInfoMIBGroup.setDescription('A collection of objects providing global information\n                 for the User Session MIB.')
colubrisUserSessionStMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8744, 5, 36, 3, 2, 2)).setObjects(("COLUBRIS-USER-SESSION-MIB", "coUserSessUserName"), ("COLUBRIS-USER-SESSION-MIB", "coUserSessClientIpAddress"), ("COLUBRIS-USER-SESSION-MIB", "coUserSessSessionDuration"), ("COLUBRIS-USER-SESSION-MIB", "coUserSessIdleTime"), ("COLUBRIS-USER-SESSION-MIB", "coUserSessMAPGroupName"), ("COLUBRIS-USER-SESSION-MIB", "coUserSessVSCName"), ("COLUBRIS-USER-SESSION-MIB", "coUserSessSSID"), ("COLUBRIS-USER-SESSION-MIB", "coUserSessVLAN"), ("COLUBRIS-USER-SESSION-MIB", "coUserSessPHYType"), ("COLUBRIS-USER-SESSION-MIB", "coUserSessAuthType"), ("COLUBRIS-USER-SESSION-MIB", "coUserSessCalledStationID"), ("COLUBRIS-USER-SESSION-MIB", "coUserSessCallingStationID"), ("COLUBRIS-USER-SESSION-MIB", "coUserSessRADIUSServerProfileName"), ("COLUBRIS-USER-SESSION-MIB", "coUserSessRADIUSServerIpAddress"), ("COLUBRIS-USER-SESSION-MIB", "coUserSessBytesSent"), ("COLUBRIS-USER-SESSION-MIB", "coUserSessBytesReceived"), ("COLUBRIS-USER-SESSION-MIB", "coUserSessPacketsSent"), ("COLUBRIS-USER-SESSION-MIB", "coUserSessPacketsReceived"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisUserSessionStMIBGroup = colubrisUserSessionStMIBGroup.setStatus('current')
if mibBuilder.loadTexts: colubrisUserSessionStMIBGroup.setDescription('A collection of objects providing the user session MIB\n                 capability.')
mibBuilder.exportSymbols("COLUBRIS-USER-SESSION-MIB", coUserSessBytesReceived=coUserSessBytesReceived, coUserSessACUserMaxCount=coUserSessACUserMaxCount, coUserSessSessionDuration=coUserSessSessionDuration, coUserSessCalledStationID=coUserSessCalledStationID, coUserSessBytesSent=coUserSessBytesSent, coUserSessNonACUserCount=coUserSessNonACUserCount, colubrisUserSessionMIBGroups=colubrisUserSessionMIBGroups, coUserSessionInfoGroup=coUserSessionInfoGroup, coUserSessVSCName=coUserSessVSCName, coUserSessAuthType=coUserSessAuthType, coUserSessPacketsReceived=coUserSessPacketsReceived, colubrisUserSessionMIB=colubrisUserSessionMIB, colubrisUserSessionMIBObjects=colubrisUserSessionMIBObjects, coUserSessClientIpAddress=coUserSessClientIpAddress, userSessionMIBNotificationPrefix=userSessionMIBNotificationPrefix, userSessionMIBNotifications=userSessionMIBNotifications, coUserSessUserName=coUserSessUserName, coUserSessMAPGroupName=coUserSessMAPGroupName, coUserSessPHYType=coUserSessPHYType, coUserSessCallingStationID=coUserSessCallingStationID, coUserSessPacketsSent=coUserSessPacketsSent, colubrisUserSessionInfoMIBGroup=colubrisUserSessionInfoMIBGroup, coUserSessRADIUSServerIpAddress=coUserSessRADIUSServerIpAddress, coUserSessIndex=coUserSessIndex, coUserSessionStGroup=coUserSessionStGroup, PYSNMP_MODULE_ID=colubrisUserSessionMIB, colubrisUserSessionMIBCompliance=colubrisUserSessionMIBCompliance, coUserSessionEntry=coUserSessionEntry, colubrisUserSessionStMIBGroup=colubrisUserSessionStMIBGroup, coUserSessSSID=coUserSessSSID, coUserSessACUserCount=coUserSessACUserCount, coUserSessIdleTime=coUserSessIdleTime, coUserSessRADIUSServerProfileName=coUserSessRADIUSServerProfileName, colubrisUserSessionMIBConformance=colubrisUserSessionMIBConformance, coUserSessionTable=coUserSessionTable, coUserSessVLAN=coUserSessVLAN, coUserSessNonACUserMaxCount=coUserSessNonACUserMaxCount, colubrisUserSessionMIBCompliances=colubrisUserSessionMIBCompliances)
