#
# PySNMP MIB module COLUBRIS-DEVICE-EVENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/hpmsm/COLUBRIS-DEVICE-EVENT-MIB.my
# Produced by pysmi-1.1.8 at Mon Feb  7 16:13:23 2022
# On host fv-az42-619 platform Linux version 5.11.0-1028-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
coDevDisIndex, = mibBuilder.importSymbols("COLUBRIS-DEVICE-MIB", "coDevDisIndex")
colubrisMgmtV2, = mibBuilder.importSymbols("COLUBRIS-SMI", "colubrisMgmtV2")
ColubrisSSIDOrNone, ColubrisNotificationEnable = mibBuilder.importSymbols("COLUBRIS-TC", "ColubrisSSIDOrNone", "ColubrisNotificationEnable")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Counter32, ModuleIdentity, Counter64, NotificationType, ObjectIdentity, iso, IpAddress, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, TimeTicks, Integer32, MibIdentifier, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "ModuleIdentity", "Counter64", "NotificationType", "ObjectIdentity", "iso", "IpAddress", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "TimeTicks", "Integer32", "MibIdentifier", "Unsigned32")
MacAddress, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "DisplayString", "TextualConvention")
colubrisDeviceEventMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 8744, 5, 26))
if mibBuilder.loadTexts: colubrisDeviceEventMIB.setLastUpdated('200607050000Z')
if mibBuilder.loadTexts: colubrisDeviceEventMIB.setOrganization('Colubris Networks, Inc.')
if mibBuilder.loadTexts: colubrisDeviceEventMIB.setContactInfo('Colubris Networks\n                     Postal: 200 West Street Ste 300\n                             Waltham, Massachusetts 02451-1121\n                             UNITED STATES\n                     Phone:  +1 781 684 0001\n                     Fax:    +1 781 684 0009\n\n                     E-mail: cn-snmp@colubris.com')
if mibBuilder.loadTexts: colubrisDeviceEventMIB.setDescription('Colubris Device Event MIB.')
colubrisDeviceEventMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 26, 1))
coDeviceEventConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 26, 1, 1))
coDeviceEventInfoGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 26, 1, 2))
coDevEvSuccessfulAssociationNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 26, 1, 1, 1), ColubrisNotificationEnable().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: coDevEvSuccessfulAssociationNotificationEnabled.setStatus('current')
if mibBuilder.loadTexts: coDevEvSuccessfulAssociationNotificationEnabled.setDescription('Specifies if coDeviceEventSuccessfulAssociation notifications\n                 are generated.')
coDevEvAssociationFailureNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 26, 1, 1, 2), ColubrisNotificationEnable().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: coDevEvAssociationFailureNotificationEnabled.setStatus('current')
if mibBuilder.loadTexts: coDevEvAssociationFailureNotificationEnabled.setDescription('Specifies if coDeviceEventAssociationFailure notifications\n                 are generated.')
coDevEvSuccessfulReAssociationNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 26, 1, 1, 3), ColubrisNotificationEnable().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: coDevEvSuccessfulReAssociationNotificationEnabled.setStatus('current')
if mibBuilder.loadTexts: coDevEvSuccessfulReAssociationNotificationEnabled.setDescription('Specifies if coDeviceEventSuccessfulReAssociation\n                 notifications are generated.')
coDevEvReAssociationFailureNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 26, 1, 1, 4), ColubrisNotificationEnable().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: coDevEvReAssociationFailureNotificationEnabled.setStatus('current')
if mibBuilder.loadTexts: coDevEvReAssociationFailureNotificationEnabled.setDescription('Specifies if coDeviceEventReAssociationFailure notifications\n                 are generated.')
coDevEvSuccessfulAuthenticationNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 26, 1, 1, 5), ColubrisNotificationEnable().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: coDevEvSuccessfulAuthenticationNotificationEnabled.setStatus('current')
if mibBuilder.loadTexts: coDevEvSuccessfulAuthenticationNotificationEnabled.setDescription('Specifies if coDeviceEventSuccessfulAuthentication\n                 notifications are generated.')
coDevEvAuthenticationFailureNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 26, 1, 1, 6), ColubrisNotificationEnable().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: coDevEvAuthenticationFailureNotificationEnabled.setStatus('current')
if mibBuilder.loadTexts: coDevEvAuthenticationFailureNotificationEnabled.setDescription('Specifies if coDeviceEventAuthenticationFailure\n                 notifications are generated.')
coDevEvSuccessfulDisAssociationNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 26, 1, 1, 7), ColubrisNotificationEnable().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: coDevEvSuccessfulDisAssociationNotificationEnabled.setStatus('current')
if mibBuilder.loadTexts: coDevEvSuccessfulDisAssociationNotificationEnabled.setDescription('Specifies if coDeviceEventSuccessfulDisAssociation notifications\n                 are generated.')
coDevEvDisAssociationFailureNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 26, 1, 1, 8), ColubrisNotificationEnable().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: coDevEvDisAssociationFailureNotificationEnabled.setStatus('current')
if mibBuilder.loadTexts: coDevEvDisAssociationFailureNotificationEnabled.setDescription('Specifies if coDeviceEventDisAssociationFailure notifications\n                 are generated.')
coDevEvSuccessfulDeAuthenticationNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 26, 1, 1, 9), ColubrisNotificationEnable().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: coDevEvSuccessfulDeAuthenticationNotificationEnabled.setStatus('current')
if mibBuilder.loadTexts: coDevEvSuccessfulDeAuthenticationNotificationEnabled.setDescription('Specifies if coDeviceEventSuccessfulDeAuthentication\n                 notifications are generated.')
coDevEvDeAuthenticationFailureNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 26, 1, 1, 10), ColubrisNotificationEnable().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: coDevEvDeAuthenticationFailureNotificationEnabled.setStatus('current')
if mibBuilder.loadTexts: coDevEvDeAuthenticationFailureNotificationEnabled.setDescription('Specifies if coDeviceEventDeAuthenticationFailure\n                 notifications are generated.')
coDeviceEventTable = MibTable((1, 3, 6, 1, 4, 1, 8744, 5, 26, 1, 2, 1), )
if mibBuilder.loadTexts: coDeviceEventTable.setStatus('current')
if mibBuilder.loadTexts: coDeviceEventTable.setDescription('The list of devices available in the Event system.')
coDeviceEventEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8744, 5, 26, 1, 2, 1, 1), ).setIndexNames((0, "COLUBRIS-DEVICE-MIB", "coDevDisIndex"), (0, "COLUBRIS-DEVICE-EVENT-MIB", "coDevEvIndex"))
if mibBuilder.loadTexts: coDeviceEventEntry.setStatus('current')
if mibBuilder.loadTexts: coDeviceEventEntry.setDescription('An entry in the coDeviceEventTable.\n                 coDevDisIndex - Uniquely identify a device in the\n                                 MultiService Access Controller.\n                 coDevEvIndex - Uniquely identify a device in the\n                                Event system.')
coDevEvIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 26, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: coDevEvIndex.setStatus('current')
if mibBuilder.loadTexts: coDevEvIndex.setDescription('Specifies the index associated to a device in the\n                 Event system.')
coDevEvMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 26, 1, 2, 1, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevEvMacAddress.setStatus('current')
if mibBuilder.loadTexts: coDevEvMacAddress.setDescription("MAC address of the device's generating the events.")
coDeviceEventDetailTable = MibTable((1, 3, 6, 1, 4, 1, 8744, 5, 26, 1, 2, 2), )
if mibBuilder.loadTexts: coDeviceEventDetailTable.setStatus('current')
if mibBuilder.loadTexts: coDeviceEventDetailTable.setDescription('The Event for each devices.')
coDeviceEventDetailEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8744, 5, 26, 1, 2, 2, 1), ).setIndexNames((0, "COLUBRIS-DEVICE-MIB", "coDevDisIndex"), (0, "COLUBRIS-DEVICE-EVENT-MIB", "coDevEvIndex"), (0, "COLUBRIS-DEVICE-EVENT-MIB", "coDevEvLogIndex"))
if mibBuilder.loadTexts: coDeviceEventDetailEntry.setStatus('current')
if mibBuilder.loadTexts: coDeviceEventDetailEntry.setDescription('An entry in the coDeviceEventDetailTable.\n                 coDevDisIndex - Uniquely identifies a device on the\n                                 MultiService Access Controller.\n                 coDevEvIndex - Uniquely identifies a device on the\n                                Event system.\n                 coDevEvLogIndex - Uniquely identifies a log for a\n                                   specific device in the Event\n                                   system. ')
coDevEvLogIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 26, 1, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: coDevEvLogIndex.setStatus('current')
if mibBuilder.loadTexts: coDevEvLogIndex.setDescription('Uniquely identifies a log for a specific device in the\n                 Event system.')
coDevEvDetMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 26, 1, 2, 2, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevEvDetMacAddress.setStatus('current')
if mibBuilder.loadTexts: coDevEvDetMacAddress.setDescription('MAC address of the device generating the events.')
coDevEvTime = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 26, 1, 2, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevEvTime.setStatus('current')
if mibBuilder.loadTexts: coDevEvTime.setDescription('Date and time of the event.')
coDevEvSSID = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 26, 1, 2, 2, 1, 4), ColubrisSSIDOrNone()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevEvSSID.setStatus('current')
if mibBuilder.loadTexts: coDevEvSSID.setDescription('The SSID used by the wireless device.')
coDevEvRadioIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 26, 1, 2, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevEvRadioIndex.setStatus('current')
if mibBuilder.loadTexts: coDevEvRadioIndex.setDescription('Radio index where the wireless device is connected.')
coDevEvDuplicateCount = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 26, 1, 2, 2, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevEvDuplicateCount.setStatus('current')
if mibBuilder.loadTexts: coDevEvDuplicateCount.setDescription('Number of times this event is repeated.')
coDevEvCategory = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 26, 1, 2, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("wireless", 1), ("ieee802dot1x", 2), ("wpa", 3), ("macAuthentication", 4), ("dhcpServer", 5), ("pptpL2tp", 6), ("ipSec", 7), ("unknown", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevEvCategory.setStatus('current')
if mibBuilder.loadTexts: coDevEvCategory.setDescription('The module that sent the message.')
coDevEvOperation = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 26, 1, 2, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("association", 1), ("authentication", 2), ("authorization", 3), ("encryption", 4), ("addressAllocation", 5), ("vpnAuthentication", 6), ("vpnAddressAllocation", 7), ("unknown", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevEvOperation.setStatus('current')
if mibBuilder.loadTexts: coDevEvOperation.setDescription('The action that has occured.')
coDevEvStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 26, 1, 2, 2, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevEvStatus.setStatus('current')
if mibBuilder.loadTexts: coDevEvStatus.setDescription('The status itself.')
coDevEvOptionalData = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 26, 1, 2, 2, 1, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevEvOptionalData.setStatus('current')
if mibBuilder.loadTexts: coDevEvOptionalData.setDescription('Additional data that may be supplied (reason codes,\n                 etc).')
colubrisDeviceEventMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 26, 2))
colubrisDeviceEventMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 26, 2, 0))
coDeviceEventSuccessfulAssociation = NotificationType((1, 3, 6, 1, 4, 1, 8744, 5, 26, 2, 0, 1)).setObjects(("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvMacAddress"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvSSID"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvStatus"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvOptionalData"))
if mibBuilder.loadTexts: coDeviceEventSuccessfulAssociation.setStatus('current')
if mibBuilder.loadTexts: coDeviceEventSuccessfulAssociation.setDescription('Sent when a client station is successfully associated with the AP.')
coDeviceEventAssociationFailure = NotificationType((1, 3, 6, 1, 4, 1, 8744, 5, 26, 2, 0, 2)).setObjects(("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvMacAddress"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvSSID"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvStatus"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvOptionalData"))
if mibBuilder.loadTexts: coDeviceEventAssociationFailure.setStatus('current')
if mibBuilder.loadTexts: coDeviceEventAssociationFailure.setDescription('Sent when a client station has failed to associate with the AP.')
coDeviceEventSuccessfulReAssociation = NotificationType((1, 3, 6, 1, 4, 1, 8744, 5, 26, 2, 0, 3)).setObjects(("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvMacAddress"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvSSID"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvStatus"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvOptionalData"))
if mibBuilder.loadTexts: coDeviceEventSuccessfulReAssociation.setStatus('current')
if mibBuilder.loadTexts: coDeviceEventSuccessfulReAssociation.setDescription('Sent when a client station is successfully reassociated with the AP.')
coDeviceEventReAssociationFailure = NotificationType((1, 3, 6, 1, 4, 1, 8744, 5, 26, 2, 0, 4)).setObjects(("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvMacAddress"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvSSID"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvStatus"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvOptionalData"))
if mibBuilder.loadTexts: coDeviceEventReAssociationFailure.setStatus('current')
if mibBuilder.loadTexts: coDeviceEventReAssociationFailure.setDescription('Sent when a client station has failed to reassociate with the AP.')
coDeviceEventSuccessfulAuthentication = NotificationType((1, 3, 6, 1, 4, 1, 8744, 5, 26, 2, 0, 5)).setObjects(("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvMacAddress"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvSSID"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvStatus"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvOptionalData"))
if mibBuilder.loadTexts: coDeviceEventSuccessfulAuthentication.setStatus('current')
if mibBuilder.loadTexts: coDeviceEventSuccessfulAuthentication.setDescription('Sent when a client station is successfully authenticated.')
coDeviceEventAuthenticationFailure = NotificationType((1, 3, 6, 1, 4, 1, 8744, 5, 26, 2, 0, 6)).setObjects(("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvMacAddress"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvSSID"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvStatus"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvOptionalData"))
if mibBuilder.loadTexts: coDeviceEventAuthenticationFailure.setStatus('current')
if mibBuilder.loadTexts: coDeviceEventAuthenticationFailure.setDescription('Sent when a client station has failed to authenticate.')
coDeviceEventSuccessfulDisAssociation = NotificationType((1, 3, 6, 1, 4, 1, 8744, 5, 26, 2, 0, 7)).setObjects(("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvMacAddress"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvSSID"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvStatus"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvOptionalData"))
if mibBuilder.loadTexts: coDeviceEventSuccessfulDisAssociation.setStatus('current')
if mibBuilder.loadTexts: coDeviceEventSuccessfulDisAssociation.setDescription('Sent when a client station is successfully disassociated from the AP.')
coDeviceEventDisAssociationFailure = NotificationType((1, 3, 6, 1, 4, 1, 8744, 5, 26, 2, 0, 8)).setObjects(("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvMacAddress"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvSSID"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvStatus"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvOptionalData"))
if mibBuilder.loadTexts: coDeviceEventDisAssociationFailure.setStatus('current')
if mibBuilder.loadTexts: coDeviceEventDisAssociationFailure.setDescription('Sent when a client station has failed to disassociate from the AP.')
coDeviceEventSuccessfulDeAuthentication = NotificationType((1, 3, 6, 1, 4, 1, 8744, 5, 26, 2, 0, 9)).setObjects(("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvMacAddress"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvSSID"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvStatus"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvOptionalData"))
if mibBuilder.loadTexts: coDeviceEventSuccessfulDeAuthentication.setStatus('current')
if mibBuilder.loadTexts: coDeviceEventSuccessfulDeAuthentication.setDescription('Sent when a client station is successfully deauthenticated.')
coDeviceEventDeAuthenticationFailure = NotificationType((1, 3, 6, 1, 4, 1, 8744, 5, 26, 2, 0, 10)).setObjects(("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvMacAddress"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvSSID"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvStatus"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvOptionalData"))
if mibBuilder.loadTexts: coDeviceEventDeAuthenticationFailure.setStatus('current')
if mibBuilder.loadTexts: coDeviceEventDeAuthenticationFailure.setDescription('Sent when a client station has failed to deauthenticate.')
colubrisDeviceEventMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 26, 3))
colubrisDeviceEventMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 26, 3, 1))
colubrisDeviceEventMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 26, 3, 2))
colubrisDeviceEventMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 8744, 5, 26, 3, 1, 1)).setObjects(("COLUBRIS-DEVICE-EVENT-MIB", "colubrisDeviceEventConfigMIBGroup"), ("COLUBRIS-DEVICE-EVENT-MIB", "colubrisDeviceEventInfoMIBGroup"), ("COLUBRIS-DEVICE-EVENT-MIB", "colubrisDeviceEventNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisDeviceEventMIBCompliance = colubrisDeviceEventMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: colubrisDeviceEventMIBCompliance.setDescription('The compliance statement for the Event Log MIB.')
colubrisDeviceEventConfigMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8744, 5, 26, 3, 2, 1)).setObjects(("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvSuccessfulAssociationNotificationEnabled"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvAssociationFailureNotificationEnabled"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvSuccessfulReAssociationNotificationEnabled"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvReAssociationFailureNotificationEnabled"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvSuccessfulAuthenticationNotificationEnabled"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvAuthenticationFailureNotificationEnabled"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvSuccessfulDisAssociationNotificationEnabled"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvDisAssociationFailureNotificationEnabled"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvSuccessfulDeAuthenticationNotificationEnabled"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvDeAuthenticationFailureNotificationEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisDeviceEventConfigMIBGroup = colubrisDeviceEventConfigMIBGroup.setStatus('current')
if mibBuilder.loadTexts: colubrisDeviceEventConfigMIBGroup.setDescription('A collection of objects for Device Event configuration.')
colubrisDeviceEventInfoMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8744, 5, 26, 3, 2, 2)).setObjects(("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvMacAddress"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvDetMacAddress"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvTime"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvSSID"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvRadioIndex"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvDuplicateCount"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvCategory"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvOperation"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvStatus"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvOptionalData"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisDeviceEventInfoMIBGroup = colubrisDeviceEventInfoMIBGroup.setStatus('current')
if mibBuilder.loadTexts: colubrisDeviceEventInfoMIBGroup.setDescription('A collection of objects for Device Event status.')
colubrisDeviceEventNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 8744, 5, 26, 3, 2, 3)).setObjects(("COLUBRIS-DEVICE-EVENT-MIB", "coDeviceEventSuccessfulAssociation"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDeviceEventAssociationFailure"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDeviceEventSuccessfulReAssociation"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDeviceEventReAssociationFailure"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDeviceEventSuccessfulAuthentication"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDeviceEventAuthenticationFailure"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDeviceEventSuccessfulDisAssociation"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDeviceEventDisAssociationFailure"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDeviceEventSuccessfulDeAuthentication"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDeviceEventDeAuthenticationFailure"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisDeviceEventNotificationGroup = colubrisDeviceEventNotificationGroup.setStatus('current')
if mibBuilder.loadTexts: colubrisDeviceEventNotificationGroup.setDescription('A collection of supported Device Event\n                 notifications.')
mibBuilder.exportSymbols("COLUBRIS-DEVICE-EVENT-MIB", PYSNMP_MODULE_ID=colubrisDeviceEventMIB, coDeviceEventDetailEntry=coDeviceEventDetailEntry, colubrisDeviceEventMIBCompliances=colubrisDeviceEventMIBCompliances, coDeviceEventInfoGroup=coDeviceEventInfoGroup, coDevEvMacAddress=coDevEvMacAddress, coDevEvReAssociationFailureNotificationEnabled=coDevEvReAssociationFailureNotificationEnabled, coDevEvAssociationFailureNotificationEnabled=coDevEvAssociationFailureNotificationEnabled, coDevEvSuccessfulDisAssociationNotificationEnabled=coDevEvSuccessfulDisAssociationNotificationEnabled, coDeviceEventConfigGroup=coDeviceEventConfigGroup, coDeviceEventDeAuthenticationFailure=coDeviceEventDeAuthenticationFailure, coDevEvDetMacAddress=coDevEvDetMacAddress, coDevEvStatus=coDevEvStatus, coDeviceEventReAssociationFailure=coDeviceEventReAssociationFailure, coDevEvSSID=coDevEvSSID, coDeviceEventAssociationFailure=coDeviceEventAssociationFailure, coDeviceEventDetailTable=coDeviceEventDetailTable, coDevEvSuccessfulAssociationNotificationEnabled=coDevEvSuccessfulAssociationNotificationEnabled, coDevEvLogIndex=coDevEvLogIndex, colubrisDeviceEventMIBObjects=colubrisDeviceEventMIBObjects, coDevEvDeAuthenticationFailureNotificationEnabled=coDevEvDeAuthenticationFailureNotificationEnabled, coDevEvRadioIndex=coDevEvRadioIndex, coDevEvDuplicateCount=coDevEvDuplicateCount, coDeviceEventTable=coDeviceEventTable, coDevEvOperation=coDevEvOperation, coDevEvDisAssociationFailureNotificationEnabled=coDevEvDisAssociationFailureNotificationEnabled, colubrisDeviceEventMIBNotifications=colubrisDeviceEventMIBNotifications, coDeviceEventSuccessfulDisAssociation=coDeviceEventSuccessfulDisAssociation, coDeviceEventSuccessfulAssociation=coDeviceEventSuccessfulAssociation, colubrisDeviceEventMIBConformance=colubrisDeviceEventMIBConformance, coDeviceEventSuccessfulDeAuthentication=coDeviceEventSuccessfulDeAuthentication, coDeviceEventAuthenticationFailure=coDeviceEventAuthenticationFailure, coDevEvSuccessfulAuthenticationNotificationEnabled=coDevEvSuccessfulAuthenticationNotificationEnabled, colubrisDeviceEventMIB=colubrisDeviceEventMIB, coDeviceEventSuccessfulAuthentication=coDeviceEventSuccessfulAuthentication, coDevEvSuccessfulDeAuthenticationNotificationEnabled=coDevEvSuccessfulDeAuthenticationNotificationEnabled, coDevEvAuthenticationFailureNotificationEnabled=coDevEvAuthenticationFailureNotificationEnabled, colubrisDeviceEventConfigMIBGroup=colubrisDeviceEventConfigMIBGroup, coDevEvCategory=coDevEvCategory, colubrisDeviceEventNotificationGroup=colubrisDeviceEventNotificationGroup, colubrisDeviceEventMIBNotificationPrefix=colubrisDeviceEventMIBNotificationPrefix, coDevEvIndex=coDevEvIndex, coDeviceEventSuccessfulReAssociation=coDeviceEventSuccessfulReAssociation, colubrisDeviceEventMIBGroups=colubrisDeviceEventMIBGroups, coDevEvSuccessfulReAssociationNotificationEnabled=coDevEvSuccessfulReAssociationNotificationEnabled, coDeviceEventEntry=coDeviceEventEntry, colubrisDeviceEventInfoMIBGroup=colubrisDeviceEventInfoMIBGroup, coDevEvTime=coDevEvTime, colubrisDeviceEventMIBCompliance=colubrisDeviceEventMIBCompliance, coDevEvOptionalData=coDevEvOptionalData, coDeviceEventDisAssociationFailure=coDeviceEventDisAssociationFailure)
