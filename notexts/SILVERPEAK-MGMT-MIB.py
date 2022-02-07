#
# PySNMP MIB module SILVERPEAK-MGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/silverpeak/SILVERPEAK-MGMT-MIB
# Produced by pysmi-1.1.8 at Mon Feb  7 16:19:36 2022
# On host fv-az42-619 platform Linux version 5.11.0-1028-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
silverpeakNotifications, silverpeakMgmt = mibBuilder.importSymbols("SILVERPEAK-SMI", "silverpeakNotifications", "silverpeakMgmt")
SilverpeakAlarmSeverity, SilverpeakSeqNum, SilverpeakYesNo = mibBuilder.importSymbols("SILVERPEAK-TC", "SilverpeakAlarmSeverity", "SilverpeakSeqNum", "SilverpeakYesNo")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
ModuleIdentity, ObjectIdentity, Gauge32, Unsigned32, iso, MibIdentifier, Counter32, IpAddress, Bits, NotificationType, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "ObjectIdentity", "Gauge32", "Unsigned32", "iso", "MibIdentifier", "Counter32", "IpAddress", "Bits", "NotificationType", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
silverpeakMgmtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 23867, 3, 1))
if mibBuilder.loadTexts: silverpeakMgmtMIB.setLastUpdated('201201060000Z')
if mibBuilder.loadTexts: silverpeakMgmtMIB.setOrganization('Silver Peak Systems, Inc.')
silverpeakMgmtMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 23867, 3, 1, 1))
silverpeakMgmtMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 23867, 4, 1))
silverpeakMgmtMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 23867, 3, 1, 2))
silverpeakMgmtMIBScalars = MibIdentifier((1, 3, 6, 1, 4, 1, 23867, 3, 1, 1, 1))
spsSystemVersion = MibScalar((1, 3, 6, 1, 4, 1, 23867, 3, 1, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: spsSystemVersion.setStatus('current')
spsProductModel = MibScalar((1, 3, 6, 1, 4, 1, 23867, 3, 1, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: spsProductModel.setStatus('current')
spsOperStatus = MibScalar((1, 3, 6, 1, 4, 1, 23867, 3, 1, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: spsOperStatus.setStatus('current')
spsActiveAlarmCount = MibScalar((1, 3, 6, 1, 4, 1, 23867, 3, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: spsActiveAlarmCount.setStatus('current')
spsSystemUptime = MibScalar((1, 3, 6, 1, 4, 1, 23867, 3, 1, 1, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: spsSystemUptime.setStatus('current')
spsSystemSerial = MibScalar((1, 3, 6, 1, 4, 1, 23867, 3, 1, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: spsSystemSerial.setStatus('current')
silverpeakMgmtMIBTables = MibIdentifier((1, 3, 6, 1, 4, 1, 23867, 3, 1, 1, 2))
spsActiveAlarmTable = MibTable((1, 3, 6, 1, 4, 1, 23867, 3, 1, 1, 2, 1), )
if mibBuilder.loadTexts: spsActiveAlarmTable.setStatus('current')
activeAlarmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 23867, 3, 1, 1, 2, 1, 1), ).setIndexNames((0, "SILVERPEAK-MGMT-MIB", "spsActiveAlarmIndex"))
if mibBuilder.loadTexts: activeAlarmEntry.setStatus('current')
spsActiveAlarmIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 23867, 3, 1, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: spsActiveAlarmIndex.setStatus('current')
spsActiveAlarmSeqNum = MibTableColumn((1, 3, 6, 1, 4, 1, 23867, 3, 1, 1, 2, 1, 1, 2), SilverpeakSeqNum()).setMaxAccess("readonly")
if mibBuilder.loadTexts: spsActiveAlarmSeqNum.setStatus('current')
spsActiveAlarmSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 23867, 3, 1, 1, 2, 1, 1, 3), SilverpeakAlarmSeverity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: spsActiveAlarmSeverity.setStatus('current')
spsActiveAlarmName = MibTableColumn((1, 3, 6, 1, 4, 1, 23867, 3, 1, 1, 2, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: spsActiveAlarmName.setStatus('current')
spsActiveAlarmDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 23867, 3, 1, 1, 2, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: spsActiveAlarmDescr.setStatus('current')
spsActiveAlarmSource = MibTableColumn((1, 3, 6, 1, 4, 1, 23867, 3, 1, 1, 2, 1, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: spsActiveAlarmSource.setStatus('current')
spsActiveAlarmType = MibTableColumn((1, 3, 6, 1, 4, 1, 23867, 3, 1, 1, 2, 1, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: spsActiveAlarmType.setStatus('current')
spsActiveAlarmAcked = MibTableColumn((1, 3, 6, 1, 4, 1, 23867, 3, 1, 1, 2, 1, 1, 8), SilverpeakYesNo()).setMaxAccess("readonly")
if mibBuilder.loadTexts: spsActiveAlarmAcked.setStatus('current')
spsActiveAlarmActive = MibTableColumn((1, 3, 6, 1, 4, 1, 23867, 3, 1, 1, 2, 1, 1, 9), SilverpeakYesNo()).setMaxAccess("readonly")
if mibBuilder.loadTexts: spsActiveAlarmActive.setStatus('current')
spsActiveAlarmClearable = MibTableColumn((1, 3, 6, 1, 4, 1, 23867, 3, 1, 1, 2, 1, 1, 10), SilverpeakYesNo()).setMaxAccess("readonly")
if mibBuilder.loadTexts: spsActiveAlarmClearable.setStatus('current')
spsActiveAlarmLogTime = MibTableColumn((1, 3, 6, 1, 4, 1, 23867, 3, 1, 1, 2, 1, 1, 11), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: spsActiveAlarmLogTime.setStatus('current')
spsActiveAlarmServiceAffect = MibTableColumn((1, 3, 6, 1, 4, 1, 23867, 3, 1, 1, 2, 1, 1, 12), SilverpeakYesNo()).setMaxAccess("readonly")
if mibBuilder.loadTexts: spsActiveAlarmServiceAffect.setStatus('current')
spsActiveAlarmTypeId = MibTableColumn((1, 3, 6, 1, 4, 1, 23867, 3, 1, 1, 2, 1, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: spsActiveAlarmTypeId.setStatus('current')
spsNotifyAlarm = NotificationType((1, 3, 6, 1, 4, 1, 23867, 4, 1, 1)).setObjects(("SILVERPEAK-MGMT-MIB", "spsActiveAlarmSource"), ("SILVERPEAK-MGMT-MIB", "spsActiveAlarmSeverity"), ("SILVERPEAK-MGMT-MIB", "spsActiveAlarmDescr"))
if mibBuilder.loadTexts: spsNotifyAlarm.setStatus('current')
silverpeakMgmtMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 23867, 3, 1, 2, 1))
silverpeakMgmtMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 23867, 3, 1, 2, 2))
silverpeakMgmtCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 23867, 3, 1, 2, 1, 1)).setObjects(("SILVERPEAK-MGMT-MIB", "silverpeakMgmtGroup"), ("SILVERPEAK-MGMT-MIB", "silverpeakMgmtNotifyGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    silverpeakMgmtCompliance = silverpeakMgmtCompliance.setStatus('current')
silverpeakMgmtGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 23867, 3, 1, 2, 2, 1)).setObjects(("SILVERPEAK-MGMT-MIB", "spsSystemVersion"), ("SILVERPEAK-MGMT-MIB", "spsProductModel"), ("SILVERPEAK-MGMT-MIB", "spsOperStatus"), ("SILVERPEAK-MGMT-MIB", "spsActiveAlarmSeqNum"), ("SILVERPEAK-MGMT-MIB", "spsActiveAlarmSeverity"), ("SILVERPEAK-MGMT-MIB", "spsActiveAlarmName"), ("SILVERPEAK-MGMT-MIB", "spsActiveAlarmDescr"), ("SILVERPEAK-MGMT-MIB", "spsActiveAlarmSource"), ("SILVERPEAK-MGMT-MIB", "spsActiveAlarmType"), ("SILVERPEAK-MGMT-MIB", "spsActiveAlarmAcked"), ("SILVERPEAK-MGMT-MIB", "spsActiveAlarmActive"), ("SILVERPEAK-MGMT-MIB", "spsActiveAlarmClearable"), ("SILVERPEAK-MGMT-MIB", "spsActiveAlarmLogTime"), ("SILVERPEAK-MGMT-MIB", "spsActiveAlarmServiceAffect"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    silverpeakMgmtGroup = silverpeakMgmtGroup.setStatus('current')
silverpeakMgmtNotifyGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 23867, 3, 1, 2, 2, 3)).setObjects(("SILVERPEAK-MGMT-MIB", "spsNotifyAlarm"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    silverpeakMgmtNotifyGroup = silverpeakMgmtNotifyGroup.setStatus('current')
mibBuilder.exportSymbols("SILVERPEAK-MGMT-MIB", silverpeakMgmtMIB=silverpeakMgmtMIB, spsActiveAlarmIndex=spsActiveAlarmIndex, spsActiveAlarmType=spsActiveAlarmType, spsActiveAlarmClearable=spsActiveAlarmClearable, silverpeakMgmtMIBCompliances=silverpeakMgmtMIBCompliances, silverpeakMgmtGroup=silverpeakMgmtGroup, activeAlarmEntry=activeAlarmEntry, silverpeakMgmtMIBNotifications=silverpeakMgmtMIBNotifications, silverpeakMgmtMIBGroups=silverpeakMgmtMIBGroups, silverpeakMgmtCompliance=silverpeakMgmtCompliance, spsNotifyAlarm=spsNotifyAlarm, spsOperStatus=spsOperStatus, spsActiveAlarmSource=spsActiveAlarmSource, spsSystemVersion=spsSystemVersion, silverpeakMgmtMIBConformance=silverpeakMgmtMIBConformance, silverpeakMgmtMIBScalars=silverpeakMgmtMIBScalars, PYSNMP_MODULE_ID=silverpeakMgmtMIB, spsActiveAlarmCount=spsActiveAlarmCount, spsActiveAlarmLogTime=spsActiveAlarmLogTime, spsActiveAlarmName=spsActiveAlarmName, silverpeakMgmtMIBObjects=silverpeakMgmtMIBObjects, spsActiveAlarmDescr=spsActiveAlarmDescr, spsActiveAlarmSeverity=spsActiveAlarmSeverity, silverpeakMgmtMIBTables=silverpeakMgmtMIBTables, spsProductModel=spsProductModel, spsSystemSerial=spsSystemSerial, spsActiveAlarmAcked=spsActiveAlarmAcked, silverpeakMgmtNotifyGroup=silverpeakMgmtNotifyGroup, spsActiveAlarmSeqNum=spsActiveAlarmSeqNum, spsActiveAlarmTypeId=spsActiveAlarmTypeId, spsActiveAlarmServiceAffect=spsActiveAlarmServiceAffect, spsActiveAlarmActive=spsActiveAlarmActive, spsActiveAlarmTable=spsActiveAlarmTable, spsSystemUptime=spsSystemUptime)
