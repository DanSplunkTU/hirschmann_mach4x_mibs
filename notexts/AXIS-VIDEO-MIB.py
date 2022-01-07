#
# PySNMP MIB module AXIS-VIDEO-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/axis/AXIS-VIDEO-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 15:55:01 2022
# On host fv-az135-792 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
products, axis = mibBuilder.importSymbols("AXIS-ROOT-MIB", "products", "axis")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ModuleIdentity, Gauge32, Bits, Unsigned32, iso, ObjectIdentity, NotificationType, Integer32, Counter64, Counter32, IpAddress, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ModuleIdentity", "Gauge32", "Bits", "Unsigned32", "iso", "ObjectIdentity", "NotificationType", "Integer32", "Counter64", "Counter32", "IpAddress", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
video = ModuleIdentity((1, 3, 6, 1, 4, 1, 368, 4))
video.setRevisions(('2016-09-23 12:18', '2012-12-12 12:02',))
if mibBuilder.loadTexts: video.setLastUpdated('201609231218Z')
if mibBuilder.loadTexts: video.setOrganization('Axis Communications AB')
videoBased = MibIdentifier((1, 3, 6, 1, 4, 1, 368, 1, 1))
videoObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 368, 4, 1))
powerSupplyTable = MibTable((1, 3, 6, 1, 4, 1, 368, 4, 1, 1), )
if mibBuilder.loadTexts: powerSupplyTable.setStatus('current')
powerSupplyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 368, 4, 1, 1, 1), ).setIndexNames((0, "AXIS-VIDEO-MIB", "powerSupplyType"), (0, "AXIS-VIDEO-MIB", "powerSupplyId"))
if mibBuilder.loadTexts: powerSupplyEntry.setStatus('current')
powerSupplyType = MibTableColumn((1, 3, 6, 1, 4, 1, 368, 4, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("common", 1), ("internal", 2), ("external", 3))))
if mibBuilder.loadTexts: powerSupplyType.setStatus('current')
powerSupplyId = MibTableColumn((1, 3, 6, 1, 4, 1, 368, 4, 1, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 128)))
if mibBuilder.loadTexts: powerSupplyId.setStatus('current')
powerSupplyStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 368, 4, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ok", 1), ("failure", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: powerSupplyStatus.setStatus('current')
fanTable = MibTable((1, 3, 6, 1, 4, 1, 368, 4, 1, 2), )
if mibBuilder.loadTexts: fanTable.setStatus('current')
fanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 368, 4, 1, 2, 1), ).setIndexNames((0, "AXIS-VIDEO-MIB", "fanType"), (0, "AXIS-VIDEO-MIB", "fanId"))
if mibBuilder.loadTexts: fanEntry.setStatus('current')
fanType = MibTableColumn((1, 3, 6, 1, 4, 1, 368, 4, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("common", 1), ("housing", 2), ("rack", 3), ("cpu", 4))))
if mibBuilder.loadTexts: fanType.setStatus('current')
fanId = MibTableColumn((1, 3, 6, 1, 4, 1, 368, 4, 1, 2, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 128)))
if mibBuilder.loadTexts: fanId.setStatus('current')
fanStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 368, 4, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ok", 1), ("failure", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fanStatus.setStatus('current')
tempSensorTable = MibTable((1, 3, 6, 1, 4, 1, 368, 4, 1, 3), )
if mibBuilder.loadTexts: tempSensorTable.setStatus('current')
tempSensorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 368, 4, 1, 3, 1), ).setIndexNames((0, "AXIS-VIDEO-MIB", "tempSensorType"), (0, "AXIS-VIDEO-MIB", "tempSensorId"))
if mibBuilder.loadTexts: tempSensorEntry.setStatus('current')
tempSensorType = MibTableColumn((1, 3, 6, 1, 4, 1, 368, 4, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("common", 1), ("housing", 2), ("rack", 3), ("cpu", 4))))
if mibBuilder.loadTexts: tempSensorType.setStatus('current')
tempSensorId = MibTableColumn((1, 3, 6, 1, 4, 1, 368, 4, 1, 3, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 128)))
if mibBuilder.loadTexts: tempSensorId.setStatus('current')
tempSensorStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 368, 4, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ok", 1), ("failure", 2), ("outOfBoundary", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tempSensorStatus.setStatus('current')
tempSensorValue = MibTableColumn((1, 3, 6, 1, 4, 1, 368, 4, 1, 3, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-176, 150))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tempSensorValue.setStatus('current')
videoChannelTable = MibTable((1, 3, 6, 1, 4, 1, 368, 4, 1, 4), )
if mibBuilder.loadTexts: videoChannelTable.setStatus('current')
videoChannelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 368, 4, 1, 4, 1), ).setIndexNames((0, "AXIS-VIDEO-MIB", "videoChannelId"))
if mibBuilder.loadTexts: videoChannelEntry.setStatus('current')
videoChannelId = MibTableColumn((1, 3, 6, 1, 4, 1, 368, 4, 1, 4, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 8192)))
if mibBuilder.loadTexts: videoChannelId.setStatus('current')
videoSignalStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 368, 4, 1, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("signalOk", 1), ("noSignal", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: videoSignalStatus.setStatus('current')
audioChannelTable = MibTable((1, 3, 6, 1, 4, 1, 368, 4, 1, 5), )
if mibBuilder.loadTexts: audioChannelTable.setStatus('current')
audioChannelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 368, 4, 1, 5, 1), ).setIndexNames((0, "AXIS-VIDEO-MIB", "audioChannelId"))
if mibBuilder.loadTexts: audioChannelEntry.setStatus('current')
audioChannelId = MibTableColumn((1, 3, 6, 1, 4, 1, 368, 4, 1, 5, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 8192)))
if mibBuilder.loadTexts: audioChannelId.setStatus('current')
audioSignalStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 368, 4, 1, 5, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("signalOk", 1), ("noSignal", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: audioSignalStatus.setStatus('current')
casingTable = MibTable((1, 3, 6, 1, 4, 1, 368, 4, 1, 6), )
if mibBuilder.loadTexts: casingTable.setStatus('current')
casingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 368, 4, 1, 6, 1), ).setIndexNames((0, "AXIS-VIDEO-MIB", "casingId"))
if mibBuilder.loadTexts: casingEntry.setStatus('current')
casingId = MibTableColumn((1, 3, 6, 1, 4, 1, 368, 4, 1, 6, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 32)))
if mibBuilder.loadTexts: casingId.setStatus('current')
casingName = MibTableColumn((1, 3, 6, 1, 4, 1, 368, 4, 1, 6, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: casingName.setStatus('current')
casingStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 368, 4, 1, 6, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("closed", 1), ("open", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: casingStatus.setStatus('current')
storageTable = MibTable((1, 3, 6, 1, 4, 1, 368, 4, 1, 8), )
if mibBuilder.loadTexts: storageTable.setStatus('current')
storageEntry = MibTableRow((1, 3, 6, 1, 4, 1, 368, 4, 1, 8, 1), ).setIndexNames((0, "AXIS-VIDEO-MIB", "storageId"))
if mibBuilder.loadTexts: storageEntry.setStatus('current')
storageId = MibTableColumn((1, 3, 6, 1, 4, 1, 368, 4, 1, 8, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 128)))
if mibBuilder.loadTexts: storageId.setStatus('current')
storageName = MibTableColumn((1, 3, 6, 1, 4, 1, 368, 4, 1, 8, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: storageName.setStatus('current')
storageDisruptionDetected = MibTableColumn((1, 3, 6, 1, 4, 1, 368, 4, 1, 8, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: storageDisruptionDetected.setStatus('current')
videoNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 368, 4, 2))
videoNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 368, 4, 2, 0))
alarmID = MibScalar((1, 3, 6, 1, 4, 1, 368, 4, 2, 1), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: alarmID.setStatus('current')
alarmName = MibScalar((1, 3, 6, 1, 4, 1, 368, 4, 2, 2), SnmpAdminString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: alarmName.setStatus('current')
alarmText = MibScalar((1, 3, 6, 1, 4, 1, 368, 4, 2, 3), SnmpAdminString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: alarmText.setStatus('current')
videoConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 368, 4, 3))
videoGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 368, 4, 3, 1))
videoCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 368, 4, 3, 2))
alarmNew = NotificationType((1, 3, 6, 1, 4, 1, 368, 4, 2, 0, 1)).setObjects(("AXIS-VIDEO-MIB", "alarmID"), ("AXIS-VIDEO-MIB", "alarmName"), ("AXIS-VIDEO-MIB", "alarmText"))
if mibBuilder.loadTexts: alarmNew.setStatus('current')
alarmCleared = NotificationType((1, 3, 6, 1, 4, 1, 368, 4, 2, 0, 2)).setObjects(("AXIS-VIDEO-MIB", "alarmID"), ("AXIS-VIDEO-MIB", "alarmName"), ("AXIS-VIDEO-MIB", "alarmText"))
if mibBuilder.loadTexts: alarmCleared.setStatus('current')
alarmSingle = NotificationType((1, 3, 6, 1, 4, 1, 368, 4, 2, 0, 3)).setObjects(("AXIS-VIDEO-MIB", "alarmID"), ("AXIS-VIDEO-MIB", "alarmName"), ("AXIS-VIDEO-MIB", "alarmText"))
if mibBuilder.loadTexts: alarmSingle.setStatus('current')
videoObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 368, 4, 3, 1, 1)).setObjects(("AXIS-VIDEO-MIB", "powerSupplyStatus"), ("AXIS-VIDEO-MIB", "fanStatus"), ("AXIS-VIDEO-MIB", "tempSensorStatus"), ("AXIS-VIDEO-MIB", "tempSensorValue"), ("AXIS-VIDEO-MIB", "videoSignalStatus"), ("AXIS-VIDEO-MIB", "audioSignalStatus"), ("AXIS-VIDEO-MIB", "casingName"), ("AXIS-VIDEO-MIB", "casingStatus"), ("AXIS-VIDEO-MIB", "storageDisruptionDetected"), ("AXIS-VIDEO-MIB", "storageName"), ("AXIS-VIDEO-MIB", "alarmID"), ("AXIS-VIDEO-MIB", "alarmName"), ("AXIS-VIDEO-MIB", "alarmText"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    videoObjectGroup = videoObjectGroup.setStatus('obsolete')
videoNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 368, 4, 3, 1, 2)).setObjects(("AXIS-VIDEO-MIB", "alarmNew"), ("AXIS-VIDEO-MIB", "alarmCleared"), ("AXIS-VIDEO-MIB", "alarmSingle"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    videoNotificationGroup = videoNotificationGroup.setStatus('current')
tempSensorGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 368, 4, 3, 1, 3)).setObjects(("AXIS-VIDEO-MIB", "tempSensorStatus"), ("AXIS-VIDEO-MIB", "tempSensorValue"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tempSensorGroup = tempSensorGroup.setStatus('current')
casingGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 368, 4, 3, 1, 4)).setObjects(("AXIS-VIDEO-MIB", "casingName"), ("AXIS-VIDEO-MIB", "casingStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    casingGroup = casingGroup.setStatus('current')
storageGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 368, 4, 3, 1, 5)).setObjects(("AXIS-VIDEO-MIB", "storageDisruptionDetected"), ("AXIS-VIDEO-MIB", "storageName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    storageGroup = storageGroup.setStatus('current')
videoComplianceRev2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 368, 4, 3, 2, 2)).setObjects(("AXIS-VIDEO-MIB", "videoNotificationGroup"), ("AXIS-VIDEO-MIB", "powerSupplyStatus"), ("AXIS-VIDEO-MIB", "fanStatus"), ("AXIS-VIDEO-MIB", "tempSensorGroup"), ("AXIS-VIDEO-MIB", "videoSignalStatus"), ("AXIS-VIDEO-MIB", "audioSignalStatus"), ("AXIS-VIDEO-MIB", "casingGroup"), ("AXIS-VIDEO-MIB", "storageGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    videoComplianceRev2 = videoComplianceRev2.setStatus('current')
videoCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 368, 4, 3, 2, 1)).setObjects(("AXIS-VIDEO-MIB", "videoObjectGroup"), ("AXIS-VIDEO-MIB", "videoNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    videoCompliance = videoCompliance.setStatus('obsolete')
mibBuilder.exportSymbols("AXIS-VIDEO-MIB", videoGroups=videoGroups, tempSensorGroup=tempSensorGroup, videoConformance=videoConformance, fanType=fanType, casingTable=casingTable, casingId=casingId, videoCompliances=videoCompliances, video=video, PYSNMP_MODULE_ID=video, audioChannelEntry=audioChannelEntry, tempSensorStatus=tempSensorStatus, videoComplianceRev2=videoComplianceRev2, videoNotificationGroup=videoNotificationGroup, powerSupplyTable=powerSupplyTable, tempSensorValue=tempSensorValue, videoSignalStatus=videoSignalStatus, fanStatus=fanStatus, audioChannelTable=audioChannelTable, fanId=fanId, casingEntry=casingEntry, storageTable=storageTable, alarmText=alarmText, powerSupplyType=powerSupplyType, casingName=casingName, videoNotifications=videoNotifications, videoCompliance=videoCompliance, videoObjects=videoObjects, alarmNew=alarmNew, tempSensorId=tempSensorId, videoChannelId=videoChannelId, powerSupplyStatus=powerSupplyStatus, videoObjectGroup=videoObjectGroup, storageGroup=storageGroup, powerSupplyId=powerSupplyId, audioSignalStatus=audioSignalStatus, alarmSingle=alarmSingle, casingGroup=casingGroup, videoChannelEntry=videoChannelEntry, audioChannelId=audioChannelId, videoNotificationPrefix=videoNotificationPrefix, casingStatus=casingStatus, storageDisruptionDetected=storageDisruptionDetected, videoBased=videoBased, videoChannelTable=videoChannelTable, tempSensorEntry=tempSensorEntry, alarmCleared=alarmCleared, storageName=storageName, storageEntry=storageEntry, fanEntry=fanEntry, tempSensorType=tempSensorType, alarmName=alarmName, tempSensorTable=tempSensorTable, storageId=storageId, powerSupplyEntry=powerSupplyEntry, alarmID=alarmID, fanTable=fanTable)
