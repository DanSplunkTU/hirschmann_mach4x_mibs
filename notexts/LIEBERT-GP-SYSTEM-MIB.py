#
# PySNMP MIB module LIEBERT-GP-SYSTEM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/liebert/LIEBERT-GP-SYSTEM-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:29:40 2022
# On host fv-az36-988 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
lgpAgentConnectedDeviceCount, lgpAgentDeviceIndex = mibBuilder.importSymbols("LIEBERT-GP-AGENT-MIB", "lgpAgentConnectedDeviceCount", "lgpAgentDeviceIndex")
lgpSystem, liebertSystemModuleReg = mibBuilder.importSymbols("LIEBERT-GP-REGISTRATION-MIB", "lgpSystem", "liebertSystemModuleReg")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
sysUpTime, = mibBuilder.importSymbols("SNMPv2-MIB", "sysUpTime")
TimeTicks, ModuleIdentity, MibIdentifier, Counter32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, iso, IpAddress, Bits, Integer32, Unsigned32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "ModuleIdentity", "MibIdentifier", "Counter32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "iso", "IpAddress", "Bits", "Integer32", "Unsigned32", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
liebertSystemModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 476, 1, 42, 1, 8, 1))
liebertSystemModule.setRevisions(('2008-11-17 00:00', '2008-07-02 00:00', '2008-01-10 00:00', '2007-05-29 00:00', '2006-02-22 00:00',))
if mibBuilder.loadTexts: liebertSystemModule.setLastUpdated('200811170000Z')
if mibBuilder.loadTexts: liebertSystemModule.setOrganization('Liebert Corporation')
lgpSysStatistics = ObjectIdentity((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 1))
if mibBuilder.loadTexts: lgpSysStatistics.setStatus('current')
lgpSysStatus = ObjectIdentity((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 2))
if mibBuilder.loadTexts: lgpSysStatus.setStatus('current')
lgpSysSettings = ObjectIdentity((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 3))
if mibBuilder.loadTexts: lgpSysSettings.setStatus('current')
lgpSysControl = ObjectIdentity((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 4))
if mibBuilder.loadTexts: lgpSysControl.setStatus('current')
lgpSysTime = ObjectIdentity((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 5))
if mibBuilder.loadTexts: lgpSysTime.setStatus('current')
lgpSysMaintenance = ObjectIdentity((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 6))
if mibBuilder.loadTexts: lgpSysMaintenance.setStatus('current')
lgpSysEventDescription = MibScalar((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(255, 255)).setFixedLength(255)).setMaxAccess("readonly")
if mibBuilder.loadTexts: lgpSysEventDescription.setStatus('current')
lgpSysEventNotifications = ObjectIdentity((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 8))
if mibBuilder.loadTexts: lgpSysEventNotifications.setStatus('current')
lgpSysDeviceComponentGroup = ObjectIdentity((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 9))
if mibBuilder.loadTexts: lgpSysDeviceComponentGroup.setStatus('current')
lgpSysDeviceComponentTable = MibTable((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 9, 1), )
if mibBuilder.loadTexts: lgpSysDeviceComponentTable.setStatus('current')
lgpSysDeviceComponentEntry = MibTableRow((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 9, 1, 1), ).setIndexNames((0, "LIEBERT-GP-AGENT-MIB", "lgpAgentDeviceIndex"), (0, "LIEBERT-GP-SYSTEM-MIB", "lgpSysDeviceComponentIndex"))
if mibBuilder.loadTexts: lgpSysDeviceComponentEntry.setStatus('current')
lgpSysDeviceComponentIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 9, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: lgpSysDeviceComponentIndex.setStatus('current')
lgpSysDeviceComponentDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 9, 1, 1, 2), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lgpSysDeviceComponentDescr.setStatus('current')
lgpSysDeviceComponentSerialNum = MibTableColumn((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 9, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(255, 255)).setFixedLength(255)).setMaxAccess("readonly")
if mibBuilder.loadTexts: lgpSysDeviceComponentSerialNum.setStatus('current')
lgpSysDeviceComponentModelNum = MibTableColumn((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 9, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(255, 255)).setFixedLength(255)).setMaxAccess("readonly")
if mibBuilder.loadTexts: lgpSysDeviceComponentModelNum.setStatus('current')
lgpSysDeviceComponentWellknown = ObjectIdentity((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 9, 5))
if mibBuilder.loadTexts: lgpSysDeviceComponentWellknown.setStatus('current')
lgpSysDeviceBatCabinet = ObjectIdentity((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 9, 5, 5))
if mibBuilder.loadTexts: lgpSysDeviceBatCabinet.setStatus('current')
lgpSysDeviceParallelCabinet = ObjectIdentity((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 9, 5, 6))
if mibBuilder.loadTexts: lgpSysDeviceParallelCabinet.setStatus('current')
lgpSysDeviceMaintBypass = ObjectIdentity((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 9, 5, 7))
if mibBuilder.loadTexts: lgpSysDeviceMaintBypass.setStatus('current')
lgpSysNotification = NotificationType((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 8, 1)).setObjects(("SNMPv2-MIB", "sysUpTime"), ("LIEBERT-GP-SYSTEM-MIB", "lgpSysEventDescription"))
if mibBuilder.loadTexts: lgpSysNotification.setStatus('current')
lgpSysNormal = NotificationType((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 8, 2)).setObjects(("SNMPv2-MIB", "sysUpTime"), ("LIEBERT-GP-AGENT-MIB", "lgpAgentConnectedDeviceCount"))
if mibBuilder.loadTexts: lgpSysNormal.setStatus('current')
lgpSysStatisticsRunHrs = MibScalar((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 1, 1), Unsigned32()).setUnits('hours').setMaxAccess("readonly")
if mibBuilder.loadTexts: lgpSysStatisticsRunHrs.setStatus('current')
lgpSysSelfTestResult = MibScalar((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("unknown", 1), ("passed", 2), ("failed", 3), ("inProgress", 4), ("sysFailure", 5), ("inhibited", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lgpSysSelfTestResult.setStatus('current')
lgpSysState = MibScalar((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("normalOperation", 1), ("startUp", 2), ("normalWithWarning", 3), ("normalWithAlarm", 4), ("abnormalOperation", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lgpSysState.setStatus('current')
lgpSysAudibleAlarm = MibScalar((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lgpSysAudibleAlarm.setStatus('current')
lgpSysSelfTest = MibScalar((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 4, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lgpSysSelfTest.setStatus('current')
lgpSysControlOperationOnOff = MibScalar((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 4, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lgpSysControlOperationOnOff.setStatus('current')
lgpSysTimeEpoch = MibScalar((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 5, 1), Unsigned32()).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: lgpSysTimeEpoch.setStatus('current')
lgpSysMaintenanceCapacity = MibScalar((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 6, 1), Unsigned32()).setUnits('percent').setMaxAccess("readonly")
if mibBuilder.loadTexts: lgpSysMaintenanceCapacity.setStatus('current')
lgpSysMaintenanceYear = MibScalar((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 6, 2), Unsigned32()).setUnits('year').setMaxAccess("readonly")
if mibBuilder.loadTexts: lgpSysMaintenanceYear.setStatus('current')
lgpSysMaintenanceMonth = MibScalar((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 6, 3), Unsigned32()).setUnits('month').setMaxAccess("readonly")
if mibBuilder.loadTexts: lgpSysMaintenanceMonth.setStatus('current')
mibBuilder.exportSymbols("LIEBERT-GP-SYSTEM-MIB", lgpSysTimeEpoch=lgpSysTimeEpoch, lgpSysDeviceComponentGroup=lgpSysDeviceComponentGroup, lgpSysDeviceParallelCabinet=lgpSysDeviceParallelCabinet, lgpSysStatus=lgpSysStatus, lgpSysState=lgpSysState, PYSNMP_MODULE_ID=liebertSystemModule, lgpSysDeviceComponentSerialNum=lgpSysDeviceComponentSerialNum, lgpSysAudibleAlarm=lgpSysAudibleAlarm, lgpSysMaintenanceMonth=lgpSysMaintenanceMonth, lgpSysSettings=lgpSysSettings, lgpSysSelfTestResult=lgpSysSelfTestResult, lgpSysTime=lgpSysTime, lgpSysMaintenance=lgpSysMaintenance, lgpSysControlOperationOnOff=lgpSysControlOperationOnOff, lgpSysDeviceComponentEntry=lgpSysDeviceComponentEntry, lgpSysMaintenanceCapacity=lgpSysMaintenanceCapacity, lgpSysMaintenanceYear=lgpSysMaintenanceYear, lgpSysControl=lgpSysControl, lgpSysDeviceComponentModelNum=lgpSysDeviceComponentModelNum, lgpSysDeviceBatCabinet=lgpSysDeviceBatCabinet, lgpSysNormal=lgpSysNormal, lgpSysStatisticsRunHrs=lgpSysStatisticsRunHrs, lgpSysDeviceComponentIndex=lgpSysDeviceComponentIndex, lgpSysDeviceComponentWellknown=lgpSysDeviceComponentWellknown, lgpSysDeviceComponentDescr=lgpSysDeviceComponentDescr, liebertSystemModule=liebertSystemModule, lgpSysDeviceComponentTable=lgpSysDeviceComponentTable, lgpSysStatistics=lgpSysStatistics, lgpSysEventDescription=lgpSysEventDescription, lgpSysEventNotifications=lgpSysEventNotifications, lgpSysSelfTest=lgpSysSelfTest, lgpSysNotification=lgpSysNotification, lgpSysDeviceMaintBypass=lgpSysDeviceMaintBypass)
