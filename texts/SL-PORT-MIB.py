#
# PySNMP MIB module SL-PORT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/packetlight/SL-PORT-MIB
# Produced by pysmi-1.1.3 at Sun Nov 21 00:47:38 2021
# On host fv-az39-63 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
slMain, = mibBuilder.importSymbols("SL-MAIN-MIB", "slMain")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Gauge32, ObjectIdentity, TimeTicks, Counter32, Integer32, NotificationType, iso, Unsigned32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, IpAddress, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Gauge32", "ObjectIdentity", "TimeTicks", "Counter32", "Integer32", "NotificationType", "iso", "Unsigned32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "IpAddress", "Counter64")
RowStatus, TextualConvention, TimeStamp, DateAndTime, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "TimeStamp", "DateAndTime", "DisplayString", "TruthValue")
slPort = ModuleIdentity((1, 3, 6, 1, 4, 1, 4515, 1, 3, 14))
if mibBuilder.loadTexts: slPort.setLastUpdated('200101180000Z')
if mibBuilder.loadTexts: slPort.setOrganization('PacketLight Networks Ltd.')
if mibBuilder.loadTexts: slPort.setContactInfo('Omri_Viner@PacketLight.com')
if mibBuilder.loadTexts: slPort.setDescription('This MIB module describes the Leds.')
class LedColor(TextualConvention, Integer32):
    description = 'The LED color.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("off", 1), ("red", 2), ("yellow", 3), ("green", 4))

class LedMode(TextualConvention, Integer32):
    description = 'The LED mode.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("stable", 1), ("fastBlinking", 2), ("slowBlinking", 3))

slPortConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 3, 14, 1))
slPortNotification = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 3, 14, 2))
slPortConfigTable = MibTable((1, 3, 6, 1, 4, 1, 4515, 1, 3, 14, 1, 1), )
if mibBuilder.loadTexts: slPortConfigTable.setStatus('current')
if mibBuilder.loadTexts: slPortConfigTable.setDescription('This table describe the state of the LEDs.')
slPortConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4515, 1, 3, 14, 1, 1, 1), ).setIndexNames((0, "SL-PORT-MIB", "slPortConfigIndex"))
if mibBuilder.loadTexts: slPortConfigEntry.setStatus('current')
if mibBuilder.loadTexts: slPortConfigEntry.setDescription('An entry in the table correspond to a port of the node.')
slPortConfigIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 14, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slPortConfigIndex.setStatus('current')
if mibBuilder.loadTexts: slPortConfigIndex.setDescription('The Slot Index of the LED. The Slot number for\n        the Shelf led is 0.')
slPortConfigLedColor = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 14, 1, 1, 1, 2), LedColor()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slPortConfigLedColor.setStatus('current')
if mibBuilder.loadTexts: slPortConfigLedColor.setDescription('The LED color of the port.')
slPortConfigLedMode = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 14, 1, 1, 1, 3), LedMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slPortConfigLedMode.setStatus('current')
if mibBuilder.loadTexts: slPortConfigLedMode.setDescription('The LED mode of the port.')
slPortConfigChangeType = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 14, 1, 1, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slPortConfigChangeType.setStatus('current')
if mibBuilder.loadTexts: slPortConfigChangeType.setDescription('This object is used to change the type of the port.\n        The type value is one of the IANA types.\n        Changing port type should remove all the information related to this port.\n        Such as, ifTable entry, PM info, GFP and VCG entries, current alarms, ...')
slPortConfigAlarmMask = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 14, 1, 1, 1, 5), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slPortConfigAlarmMask.setStatus('current')
if mibBuilder.loadTexts: slPortConfigAlarmMask.setDescription('This object is used to mask the alarms of the port.')
slPortConfigLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 14, 1, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slPortConfigLabel.setStatus('current')
if mibBuilder.loadTexts: slPortConfigLabel.setDescription('This object is the shadow of ifAlias. When the ifAlias\n        of the primary interface of this port is changed, \n        the value of this object should be changed to the same value.')
slPortConfigLastChange = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 14, 1, 2), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slPortConfigLastChange.setStatus('current')
if mibBuilder.loadTexts: slPortConfigLastChange.setDescription('The value of sysUpTime at last time a slPortConfigTable table\n         was changed.')
slPortConfigChanged = NotificationType((1, 3, 6, 1, 4, 1, 4515, 1, 3, 14, 2, 1)).setObjects(("SL-PORT-MIB", "slPortConfigIndex"), ("SL-PORT-MIB", "slPortConfigLedColor"), ("SL-PORT-MIB", "slPortConfigLedMode"), ("SL-PORT-MIB", "slPortConfigChangeType"), ("SL-PORT-MIB", "slPortConfigAlarmMask"), ("SL-PORT-MIB", "slPortConfigLabel"))
if mibBuilder.loadTexts: slPortConfigChanged.setStatus('current')
if mibBuilder.loadTexts: slPortConfigChanged.setDescription('An slPortConfigChanged notification is sent\n\t\twhen the state of one of the port is changed.')
slPortConfigChangedType = NotificationType((1, 3, 6, 1, 4, 1, 4515, 1, 3, 14, 2, 2)).setObjects(("SL-PORT-MIB", "slPortConfigIndex"), ("SL-PORT-MIB", "slPortConfigChangeType"))
if mibBuilder.loadTexts: slPortConfigChangedType.setStatus('current')
if mibBuilder.loadTexts: slPortConfigChangedType.setDescription('An slPortConfigChangedType notification is sent\n\t\twhen the type of one of a port is changed.')
slPortConfigChangedMask = NotificationType((1, 3, 6, 1, 4, 1, 4515, 1, 3, 14, 2, 3)).setObjects(("SL-PORT-MIB", "slPortConfigIndex"), ("SL-PORT-MIB", "slPortConfigAlarmMask"))
if mibBuilder.loadTexts: slPortConfigChangedMask.setStatus('current')
if mibBuilder.loadTexts: slPortConfigChangedMask.setDescription('An slPortConfigChangedMask notification is sent\n\t\twhen the mask of one of the port is changed.')
slPortConfigChangedLabel = NotificationType((1, 3, 6, 1, 4, 1, 4515, 1, 3, 14, 2, 4)).setObjects(("SL-PORT-MIB", "slPortConfigIndex"), ("SL-PORT-MIB", "slPortConfigLabel"))
if mibBuilder.loadTexts: slPortConfigChangedLabel.setStatus('current')
if mibBuilder.loadTexts: slPortConfigChangedLabel.setDescription('An slPortConfigChangedLabel notification is sent when the \n\t\tcorresponding object slPortConfigLabel is changed.')
slPortConfigChangedApsEnabled = NotificationType((1, 3, 6, 1, 4, 1, 4515, 1, 3, 14, 2, 5)).setObjects(("SL-PORT-MIB", "slPortConfigIndex"))
if mibBuilder.loadTexts: slPortConfigChangedApsEnabled.setStatus('current')
if mibBuilder.loadTexts: slPortConfigChangedApsEnabled.setDescription('An slPortConfigChangedLabel notification is sent when the \n\t\tcorresponding object slPortConfigApsEnable is changed.')
mibBuilder.exportSymbols("SL-PORT-MIB", slPortConfigLedColor=slPortConfigLedColor, slPortConfigTable=slPortConfigTable, slPortConfigAlarmMask=slPortConfigAlarmMask, slPortConfigEntry=slPortConfigEntry, PYSNMP_MODULE_ID=slPort, slPortNotification=slPortNotification, slPortConfigLabel=slPortConfigLabel, slPortConfigChangedMask=slPortConfigChangedMask, LedMode=LedMode, slPort=slPort, LedColor=LedColor, slPortConfig=slPortConfig, slPortConfigChangedLabel=slPortConfigChangedLabel, slPortConfigChanged=slPortConfigChanged, slPortConfigLedMode=slPortConfigLedMode, slPortConfigLastChange=slPortConfigLastChange, slPortConfigIndex=slPortConfigIndex, slPortConfigChangedApsEnabled=slPortConfigChangedApsEnabled, slPortConfigChangeType=slPortConfigChangeType, slPortConfigChangedType=slPortConfigChangedType)
