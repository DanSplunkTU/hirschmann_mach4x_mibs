#
# PySNMP MIB module PRVT-SYS-MON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/telco-systems/binos/PRVT-SYS-MON-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:26:57 2022
# On host fv-az135-792 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
reportsIfJackIndex, reportsL2IfaceUnit, prvt_products, reportsL2IfaceSlot, reportsL2IfacePort = mibBuilder.importSymbols("PRVT-SWITCH-MIB", "reportsIfJackIndex", "reportsL2IfaceUnit", "prvt-products", "reportsL2IfaceSlot", "reportsL2IfacePort")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, Integer32, Bits, Counter64, MibIdentifier, TimeTicks, NotificationType, Counter32, IpAddress, Unsigned32, ObjectIdentity, Gauge32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Integer32", "Bits", "Counter64", "MibIdentifier", "TimeTicks", "NotificationType", "Counter32", "IpAddress", "Unsigned32", "ObjectIdentity", "Gauge32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
prvtSysMonMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 738, 1, 111, 3))
prvtSysMonMib.setRevisions(('2007-12-27 00:00', '2005-02-16 00:00', '2003-11-18 00:00', '2003-05-13 00:00',))
if mibBuilder.loadTexts: prvtSysMonMib.setLastUpdated('200712270000Z')
if mibBuilder.loadTexts: prvtSysMonMib.setOrganization('BATM Advanced Communication')
software = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 111))
class EnableStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enable", 1), ("disable", 2))

prvtSysMonNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 0))
prvtSysMonObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1))
prvtSysMonConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 2))
sysMonThreshold = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 1))
sysMonValues = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 2))
sysMonConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 3))
cpuUtilizationThreshold = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpuUtilizationThreshold.setStatus('current')
ramBytesFreeThreshold = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ramBytesFreeThreshold.setStatus('current')
portErrorsThreshold = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portErrorsThreshold.setStatus('current')
portsBroadcastThreshold = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portsBroadcastThreshold.setStatus('current')
portsCRCErrThreshold = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portsCRCErrThreshold.setStatus('current')
portsRuntsThreshold = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portsRuntsThreshold.setStatus('current')
portsOverSizeThreshold = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portsOverSizeThreshold.setStatus('current')
laserPortThresholdTable = MibTable((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 1, 8), )
if mibBuilder.loadTexts: laserPortThresholdTable.setStatus('current')
laserPortThresholdEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 1, 8, 1), ).setIndexNames((0, "PRVT-SWITCH-MIB", "reportsL2IfaceUnit"), (0, "PRVT-SWITCH-MIB", "reportsL2IfaceSlot"), (0, "PRVT-SWITCH-MIB", "reportsL2IfacePort"), (0, "PRVT-SWITCH-MIB", "reportsIfJackIndex"))
if mibBuilder.loadTexts: laserPortThresholdEntry.setStatus('current')
laserTemperatureHighThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 1, 8, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: laserTemperatureHighThreshold.setStatus('current')
laserTemperatureLowThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 1, 8, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: laserTemperatureLowThreshold.setStatus('current')
laserTxPowerHighThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 1, 8, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: laserTxPowerHighThreshold.setStatus('current')
laserTxPowerLowThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 1, 8, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: laserTxPowerLowThreshold.setStatus('current')
laserRxPowerHighThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 1, 8, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: laserRxPowerHighThreshold.setStatus('current')
laserRxPowerLowThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 1, 8, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: laserRxPowerLowThreshold.setStatus('current')
monCpuUtilization = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: monCpuUtilization.setStatus('current')
monRamBytesFree = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 2, 2), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: monRamBytesFree.setStatus('current')
monPortsTable = MibTable((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 2, 3), )
if mibBuilder.loadTexts: monPortsTable.setStatus('current')
monPortsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 2, 3, 1), ).setIndexNames((0, "PRVT-SWITCH-MIB", "reportsL2IfaceUnit"), (0, "PRVT-SWITCH-MIB", "reportsL2IfaceSlot"), (0, "PRVT-SWITCH-MIB", "reportsL2IfacePort"))
if mibBuilder.loadTexts: monPortsEntry.setStatus('current')
monPortErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 2, 3, 1, 1), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: monPortErrors.setStatus('current')
monPortBroadcast = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 2, 3, 1, 2), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: monPortBroadcast.setStatus('current')
monPortCRCErr = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 2, 3, 1, 3), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: monPortCRCErr.setStatus('current')
monPortRunts = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 2, 3, 1, 4), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: monPortRunts.setStatus('current')
monPortOverSize = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 2, 3, 1, 5), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: monPortOverSize.setStatus('current')
laserPortValueTable = MibTable((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 2, 4), )
if mibBuilder.loadTexts: laserPortValueTable.setStatus('current')
laserPortValueEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 2, 4, 1), ).setIndexNames((0, "PRVT-SWITCH-MIB", "reportsL2IfaceUnit"), (0, "PRVT-SWITCH-MIB", "reportsL2IfaceSlot"), (0, "PRVT-SWITCH-MIB", "reportsL2IfacePort"), (0, "PRVT-SWITCH-MIB", "reportsIfJackIndex"))
if mibBuilder.loadTexts: laserPortValueEntry.setStatus('current')
sfpStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 2, 4, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("lm-supported", 1), ("lm-not-supported", 2), ("extracted", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpStatus.setStatus('current')
laserTemperature = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 2, 4, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: laserTemperature.setStatus('current')
laserTxPower = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 2, 4, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: laserTxPower.setStatus('current')
laserRxPower = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 2, 4, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: laserRxPower.setStatus('current')
cpuUtilizationExceeded = NotificationType((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 0, 1)).setObjects(("PRVT-SYS-MON-MIB", "monCpuUtilization"), ("PRVT-SYS-MON-MIB", "cpuUtilizationThreshold"))
if mibBuilder.loadTexts: cpuUtilizationExceeded.setStatus('current')
ramFreeSpaceExceeded = NotificationType((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 0, 2)).setObjects(("PRVT-SYS-MON-MIB", "monRamBytesFree"), ("PRVT-SYS-MON-MIB", "ramBytesFreeThreshold"))
if mibBuilder.loadTexts: ramFreeSpaceExceeded.setStatus('current')
portErrorsExceeded = NotificationType((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 0, 3)).setObjects(("PRVT-SYS-MON-MIB", "monPortErrors"), ("PRVT-SYS-MON-MIB", "portErrorsThreshold"))
if mibBuilder.loadTexts: portErrorsExceeded.setStatus('current')
portsBroadcastExceeded = NotificationType((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 0, 4)).setObjects(("PRVT-SYS-MON-MIB", "monPortBroadcast"), ("PRVT-SYS-MON-MIB", "portsBroadcastThreshold"))
if mibBuilder.loadTexts: portsBroadcastExceeded.setStatus('current')
portsCRCErrExceeded = NotificationType((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 0, 5)).setObjects(("PRVT-SYS-MON-MIB", "monPortCRCErr"), ("PRVT-SYS-MON-MIB", "portsCRCErrThreshold"))
if mibBuilder.loadTexts: portsCRCErrExceeded.setStatus('current')
portsRuntsExceeded = NotificationType((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 0, 6)).setObjects(("PRVT-SYS-MON-MIB", "monPortRunts"), ("PRVT-SYS-MON-MIB", "portsRuntsThreshold"))
if mibBuilder.loadTexts: portsRuntsExceeded.setStatus('current')
portsOverSizeExceeded = NotificationType((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 0, 7)).setObjects(("PRVT-SYS-MON-MIB", "monPortOverSize"), ("PRVT-SYS-MON-MIB", "portsOverSizeThreshold"))
if mibBuilder.loadTexts: portsOverSizeExceeded.setStatus('current')
laserTemperatureThresholdCrossed = NotificationType((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 0, 8)).setObjects(("PRVT-SYS-MON-MIB", "laserTemperature"), ("PRVT-SYS-MON-MIB", "laserTemperatureHighThreshold"), ("PRVT-SYS-MON-MIB", "laserTemperatureLowThreshold"))
if mibBuilder.loadTexts: laserTemperatureThresholdCrossed.setStatus('current')
laserTxPowerThresholdCrossed = NotificationType((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 0, 9)).setObjects(("PRVT-SYS-MON-MIB", "laserTxPower"), ("PRVT-SYS-MON-MIB", "laserTxPowerHighThreshold"), ("PRVT-SYS-MON-MIB", "laserTxPowerLowThreshold"))
if mibBuilder.loadTexts: laserTxPowerThresholdCrossed.setStatus('current')
laserRxPowerThresholdCrossed = NotificationType((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 0, 10)).setObjects(("PRVT-SYS-MON-MIB", "laserRxPower"), ("PRVT-SYS-MON-MIB", "laserRxPowerHighThreshold"), ("PRVT-SYS-MON-MIB", "laserRxPowerLowThreshold"))
if mibBuilder.loadTexts: laserRxPowerThresholdCrossed.setStatus('current')
sfpMonStatusChanged = NotificationType((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 0, 11)).setObjects(("PRVT-SYS-MON-MIB", "sfpMonStatus"))
if mibBuilder.loadTexts: sfpMonStatusChanged.setStatus('current')
sfpPortManTable = MibTable((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 2, 5), )
if mibBuilder.loadTexts: sfpPortManTable.setStatus('current')
sfpPortManEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 2, 5, 1), ).setIndexNames((0, "PRVT-SWITCH-MIB", "reportsL2IfaceUnit"), (0, "PRVT-SWITCH-MIB", "reportsL2IfaceSlot"), (0, "PRVT-SWITCH-MIB", "reportsL2IfacePort"), (0, "PRVT-SWITCH-MIB", "reportsIfJackIndex"))
if mibBuilder.loadTexts: sfpPortManEntry.setStatus('current')
sfpMonStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 2, 5, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("sfpInserted", 1), ("sfpExtracted", 2), ("sfpUnknown", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpMonStatus.setStatus('current')
sfpVendor = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 2, 5, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 9)).clone(hexValue="")).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpVendor.setStatus('current')
sfpPN = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 2, 5, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 9)).clone(hexValue="")).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpPN.setStatus('current')
sfpRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 2, 5, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 9)).clone(hexValue="")).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpRevision.setStatus('current')
sfpLenght = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 2, 5, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 9)).clone(hexValue="")).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpLenght.setStatus('current')
sfpConnector = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 2, 5, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 9)).clone(hexValue="")).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpConnector.setStatus('current')
sysMonConfigTable = MibTable((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 3, 1), )
if mibBuilder.loadTexts: sysMonConfigTable.setStatus('current')
sysMonConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 3, 1, 1), ).setIndexNames((0, "PRVT-SYS-MON-MIB", "sysMonIndicator"))
if mibBuilder.loadTexts: sysMonConfigEntry.setStatus('current')
sysMonIndicator = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("cpu-usage", 1), ("ram-usage", 2), ("power-supply", 3), ("onboard-power", 4), ("fan", 5), ("temperature", 6), ("laser", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysMonIndicator.setStatus('current')
sysMonEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 3, 1, 1, 2), EnableStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysMonEnable.setStatus('current')
sysMonPeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 3, 1, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysMonPeriod.setStatus('current')
sysMonTrap = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 3, 1, 1, 4), EnableStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysMonTrap.setStatus('current')
sysMonLog = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 3, 1, 1, 5), EnableStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysMonLog.setStatus('current')
sysMonLed = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 3, 1, 1, 6), EnableStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysMonLed.setStatus('current')
sysMonDefaults = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 3, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("noop", 0), ("reset", 1))).clone('noop')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysMonDefaults.setStatus('current')
sysMonMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 2, 2))
sysMonNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 2, 2, 3)).setObjects(("PRVT-SYS-MON-MIB", "cpuUtilizationExceeded"), ("PRVT-SYS-MON-MIB", "ramFreeSpaceExceeded"), ("PRVT-SYS-MON-MIB", "portErrorsExceeded"), ("PRVT-SYS-MON-MIB", "portsBroadcastExceeded"), ("PRVT-SYS-MON-MIB", "portsCRCErrExceeded"), ("PRVT-SYS-MON-MIB", "portsRuntsExceeded"), ("PRVT-SYS-MON-MIB", "portsOverSizeExceeded"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sysMonNotificationGroup = sysMonNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("PRVT-SYS-MON-MIB", sysMonPeriod=sysMonPeriod, prvtSysMonObjects=prvtSysMonObjects, sysMonDefaults=sysMonDefaults, portsRuntsThreshold=portsRuntsThreshold, monRamBytesFree=monRamBytesFree, laserPortValueTable=laserPortValueTable, portsCRCErrExceeded=portsCRCErrExceeded, sysMonNotificationGroup=sysMonNotificationGroup, software=software, sysMonTrap=sysMonTrap, sfpPortManTable=sfpPortManTable, portsBroadcastThreshold=portsBroadcastThreshold, cpuUtilizationExceeded=cpuUtilizationExceeded, sfpPN=sfpPN, sysMonConfig=sysMonConfig, sysMonLed=sysMonLed, prvtSysMonConformance=prvtSysMonConformance, portsRuntsExceeded=portsRuntsExceeded, sysMonConfigTable=sysMonConfigTable, monPortBroadcast=monPortBroadcast, sfpStatus=sfpStatus, prvtSysMonNotifications=prvtSysMonNotifications, PYSNMP_MODULE_ID=prvtSysMonMib, laserTemperatureThresholdCrossed=laserTemperatureThresholdCrossed, sfpMonStatusChanged=sfpMonStatusChanged, ramBytesFreeThreshold=ramBytesFreeThreshold, sysMonIndicator=sysMonIndicator, ramFreeSpaceExceeded=ramFreeSpaceExceeded, sfpPortManEntry=sfpPortManEntry, laserRxPowerLowThreshold=laserRxPowerLowThreshold, portsBroadcastExceeded=portsBroadcastExceeded, monCpuUtilization=monCpuUtilization, portsCRCErrThreshold=portsCRCErrThreshold, laserTemperatureHighThreshold=laserTemperatureHighThreshold, laserTemperature=laserTemperature, sysMonConfigEntry=sysMonConfigEntry, monPortOverSize=monPortOverSize, laserPortValueEntry=laserPortValueEntry, sysMonValues=sysMonValues, laserTxPowerLowThreshold=laserTxPowerLowThreshold, sfpRevision=sfpRevision, monPortRunts=monPortRunts, sysMonThreshold=sysMonThreshold, portErrorsExceeded=portErrorsExceeded, sfpConnector=sfpConnector, sysMonEnable=sysMonEnable, sysMonMIBGroups=sysMonMIBGroups, cpuUtilizationThreshold=cpuUtilizationThreshold, laserPortThresholdEntry=laserPortThresholdEntry, sysMonLog=sysMonLog, portErrorsThreshold=portErrorsThreshold, laserRxPower=laserRxPower, sfpMonStatus=sfpMonStatus, portsOverSizeThreshold=portsOverSizeThreshold, laserTemperatureLowThreshold=laserTemperatureLowThreshold, laserTxPowerHighThreshold=laserTxPowerHighThreshold, laserTxPower=laserTxPower, portsOverSizeExceeded=portsOverSizeExceeded, monPortsTable=monPortsTable, laserRxPowerThresholdCrossed=laserRxPowerThresholdCrossed, laserTxPowerThresholdCrossed=laserTxPowerThresholdCrossed, laserRxPowerHighThreshold=laserRxPowerHighThreshold, monPortErrors=monPortErrors, sfpLenght=sfpLenght, sfpVendor=sfpVendor, prvtSysMonMib=prvtSysMonMib, EnableStatus=EnableStatus, monPortsEntry=monPortsEntry, laserPortThresholdTable=laserPortThresholdTable, monPortCRCErr=monPortCRCErr)
