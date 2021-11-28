#
# PySNMP MIB module PRVT-SYS-MON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/telco-systems/binos/PRVT-SYS-MON-MIB
# Produced by pysmi-1.1.3 at Sun Nov 28 20:26:43 2021
# On host fv-az77-612 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
reportsL2IfaceSlot, prvt_products, reportsL2IfacePort, reportsIfJackIndex, reportsL2IfaceUnit = mibBuilder.importSymbols("PRVT-SWITCH-MIB", "reportsL2IfaceSlot", "prvt-products", "reportsL2IfacePort", "reportsIfJackIndex", "reportsL2IfaceUnit")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Counter32, Counter64, Bits, IpAddress, MibIdentifier, Gauge32, ObjectIdentity, Unsigned32, ModuleIdentity, TimeTicks, Integer32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Counter32", "Counter64", "Bits", "IpAddress", "MibIdentifier", "Gauge32", "ObjectIdentity", "Unsigned32", "ModuleIdentity", "TimeTicks", "Integer32", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
prvtSysMonMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 738, 1, 111, 3))
prvtSysMonMib.setRevisions(('2007-12-27 00:00', '2005-02-16 00:00', '2003-11-18 00:00', '2003-05-13 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: prvtSysMonMib.setRevisionsDescriptions(('Added laser management', 'Fixed spelling errors and changed the contact info.', 'Add new notifications portsCRCErrExceeded, portsRuntsExceeded, \n\tportsOverSizeExceeded and support vars for them.\n\tChange the MAX-ACCESS for all \n\tsysMonValues to accessible-for-notify', 'Initial version.',))
if mibBuilder.loadTexts: prvtSysMonMib.setLastUpdated('200712270000Z')
if mibBuilder.loadTexts: prvtSysMonMib.setOrganization('BATM Advanced Communication')
if mibBuilder.loadTexts: prvtSysMonMib.setContactInfo(' BATM/Telco Systems Support team\n\t\t\t\tEmail: \n\t\t\t\tFor North America: techsupport@telco.com\n\t\t\t\tFor North Europe: support@batm.de, info@batm.de\n\t\t\t\tFor the rest of the world: techsupport@telco.com')
if mibBuilder.loadTexts: prvtSysMonMib.setDescription('Information for system resources')
software = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 111))
class EnableStatus(TextualConvention, Integer32):
    description = 'enable(1), disable(2)'
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
if mibBuilder.loadTexts: cpuUtilizationThreshold.setDescription('High limit in percent of normal CPU utilization')
ramBytesFreeThreshold = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ramBytesFreeThreshold.setStatus('current')
if mibBuilder.loadTexts: ramBytesFreeThreshold.setDescription('Low limit in bytes free in the system memory')
portErrorsThreshold = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portErrorsThreshold.setStatus('current')
if mibBuilder.loadTexts: portErrorsThreshold.setDescription('High limit in percent of communication errors on port')
portsBroadcastThreshold = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portsBroadcastThreshold.setStatus('current')
if mibBuilder.loadTexts: portsBroadcastThreshold.setDescription('High limit in percent of exceeding broadcast-limit on port')
portsCRCErrThreshold = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portsCRCErrThreshold.setStatus('current')
if mibBuilder.loadTexts: portsCRCErrThreshold.setDescription('High limit in percent of exceeding CRC error on port')
portsRuntsThreshold = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portsRuntsThreshold.setStatus('current')
if mibBuilder.loadTexts: portsRuntsThreshold.setDescription('High limit in percent of exceeding runts on port')
portsOverSizeThreshold = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portsOverSizeThreshold.setStatus('current')
if mibBuilder.loadTexts: portsOverSizeThreshold.setDescription('High limit in percent of exceeding over-size on port')
laserPortThresholdTable = MibTable((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 1, 8), )
if mibBuilder.loadTexts: laserPortThresholdTable.setStatus('current')
if mibBuilder.loadTexts: laserPortThresholdTable.setDescription('Defines thresholds for each port in the device')
laserPortThresholdEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 1, 8, 1), ).setIndexNames((0, "PRVT-SWITCH-MIB", "reportsL2IfaceUnit"), (0, "PRVT-SWITCH-MIB", "reportsL2IfaceSlot"), (0, "PRVT-SWITCH-MIB", "reportsL2IfacePort"), (0, "PRVT-SWITCH-MIB", "reportsIfJackIndex"))
if mibBuilder.loadTexts: laserPortThresholdEntry.setStatus('current')
if mibBuilder.loadTexts: laserPortThresholdEntry.setDescription('')
laserTemperatureHighThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 1, 8, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: laserTemperatureHighThreshold.setStatus('current')
if mibBuilder.loadTexts: laserTemperatureHighThreshold.setDescription('Configures high temperature threshold. The range is -128 to 128. The accuracy is 1C.')
laserTemperatureLowThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 1, 8, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: laserTemperatureLowThreshold.setStatus('current')
if mibBuilder.loadTexts: laserTemperatureLowThreshold.setDescription('Configures low temperature threshold. The range is -128 to 128. The accuracy is 1C.')
laserTxPowerHighThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 1, 8, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: laserTxPowerHighThreshold.setStatus('current')
if mibBuilder.loadTexts: laserTxPowerHighThreshold.setDescription('Configures Tx power high threshold. The range is -40 to 8.')
laserTxPowerLowThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 1, 8, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: laserTxPowerLowThreshold.setStatus('current')
if mibBuilder.loadTexts: laserTxPowerLowThreshold.setDescription('Configures Tx power low threshold. The range is -40 to 8.')
laserRxPowerHighThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 1, 8, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: laserRxPowerHighThreshold.setStatus('current')
if mibBuilder.loadTexts: laserRxPowerHighThreshold.setDescription('Configures Rx power high threshold. The range is -40 to 8.')
laserRxPowerLowThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 1, 8, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: laserRxPowerLowThreshold.setStatus('current')
if mibBuilder.loadTexts: laserRxPowerLowThreshold.setDescription('Configures Rx power low threshold. The range is -40 to 8.')
monCpuUtilization = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: monCpuUtilization.setStatus('current')
if mibBuilder.loadTexts: monCpuUtilization.setDescription('The current level in percent of CPU utilization')
monRamBytesFree = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 2, 2), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: monRamBytesFree.setStatus('current')
if mibBuilder.loadTexts: monRamBytesFree.setDescription('The number of bytes currently free in the system memory')
monPortsTable = MibTable((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 2, 3), )
if mibBuilder.loadTexts: monPortsTable.setStatus('current')
if mibBuilder.loadTexts: monPortsTable.setDescription('Defines the ports monitor Table for providing, via SNMP, the\n             last sampled parameters by the periodic monitor')
monPortsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 2, 3, 1), ).setIndexNames((0, "PRVT-SWITCH-MIB", "reportsL2IfaceUnit"), (0, "PRVT-SWITCH-MIB", "reportsL2IfaceSlot"), (0, "PRVT-SWITCH-MIB", "reportsL2IfacePort"))
if mibBuilder.loadTexts: monPortsEntry.setStatus('current')
if mibBuilder.loadTexts: monPortsEntry.setDescription('Defines an entry in the monPortsTable. The entries are indexed by\n            the physical location of the port in the device.')
monPortErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 2, 3, 1, 1), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: monPortErrors.setStatus('current')
if mibBuilder.loadTexts: monPortErrors.setDescription('The percentages of errors on the port that generated the notification.')
monPortBroadcast = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 2, 3, 1, 2), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: monPortBroadcast.setStatus('current')
if mibBuilder.loadTexts: monPortBroadcast.setDescription('The percentages of packets exceeding broadcast-limit on the port that generated the notification.')
monPortCRCErr = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 2, 3, 1, 3), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: monPortCRCErr.setStatus('current')
if mibBuilder.loadTexts: monPortCRCErr.setDescription('The percentage of CRC errors on the port that generated the notification.')
monPortRunts = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 2, 3, 1, 4), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: monPortRunts.setStatus('current')
if mibBuilder.loadTexts: monPortRunts.setDescription('The percentage of runt packets on the port that generated the notification.')
monPortOverSize = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 2, 3, 1, 5), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: monPortOverSize.setStatus('current')
if mibBuilder.loadTexts: monPortOverSize.setDescription('The percentage of over-size packets on the port that generated the notification.')
laserPortValueTable = MibTable((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 2, 4), )
if mibBuilder.loadTexts: laserPortValueTable.setStatus('current')
if mibBuilder.loadTexts: laserPortValueTable.setDescription('This table displays the current laser-related values for each port in the device.')
laserPortValueEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 2, 4, 1), ).setIndexNames((0, "PRVT-SWITCH-MIB", "reportsL2IfaceUnit"), (0, "PRVT-SWITCH-MIB", "reportsL2IfaceSlot"), (0, "PRVT-SWITCH-MIB", "reportsL2IfacePort"), (0, "PRVT-SWITCH-MIB", "reportsIfJackIndex"))
if mibBuilder.loadTexts: laserPortValueEntry.setStatus('current')
if mibBuilder.loadTexts: laserPortValueEntry.setDescription('')
sfpStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 2, 4, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("lm-supported", 1), ("lm-not-supported", 2), ("extracted", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpStatus.setStatus('current')
if mibBuilder.loadTexts: sfpStatus.setDescription('If value of this field is not supported, then \n\tthe values of other fields are not relevant. \n\tThe value is supported only if SFP compliant \n\twith SFF-8472 is inserted.')
laserTemperature = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 2, 4, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: laserTemperature.setStatus('current')
if mibBuilder.loadTexts: laserTemperature.setDescription('Represents module temperature.\n\tThe range is -128 to 128. The accuracy is 1C.')
laserTxPower = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 2, 4, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: laserTxPower.setStatus('current')
if mibBuilder.loadTexts: laserTxPower.setDescription('Represents Tx power. The range is -40 to 8.')
laserRxPower = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 2, 4, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: laserRxPower.setStatus('current')
if mibBuilder.loadTexts: laserRxPower.setDescription('Represents Rx power. The range is -40 to 8.')
cpuUtilizationExceeded = NotificationType((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 0, 1)).setObjects(("PRVT-SYS-MON-MIB", "monCpuUtilization"), ("PRVT-SYS-MON-MIB", "cpuUtilizationThreshold"))
if mibBuilder.loadTexts: cpuUtilizationExceeded.setStatus('current')
if mibBuilder.loadTexts: cpuUtilizationExceeded.setDescription('The cpuUtilizationExceeded notification indicates that the sending\n\t\t\t agent sense that the CPU utilization has passed the\n\t\t\t program threshold.')
ramFreeSpaceExceeded = NotificationType((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 0, 2)).setObjects(("PRVT-SYS-MON-MIB", "monRamBytesFree"), ("PRVT-SYS-MON-MIB", "ramBytesFreeThreshold"))
if mibBuilder.loadTexts: ramFreeSpaceExceeded.setStatus('current')
if mibBuilder.loadTexts: ramFreeSpaceExceeded.setDescription('The ramFreeSpaceExceeded notification indicates that the sending\n             agent sense that the system memory utilization has passed the\n             program threshold.')
portErrorsExceeded = NotificationType((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 0, 3)).setObjects(("PRVT-SYS-MON-MIB", "monPortErrors"), ("PRVT-SYS-MON-MIB", "portErrorsThreshold"))
if mibBuilder.loadTexts: portErrorsExceeded.setStatus('current')
if mibBuilder.loadTexts: portErrorsExceeded.setDescription('The portErrorsExceeded notification indicates that the sending\n             agent sense that the level of errors on the port\n             has passed the program threshold.')
portsBroadcastExceeded = NotificationType((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 0, 4)).setObjects(("PRVT-SYS-MON-MIB", "monPortBroadcast"), ("PRVT-SYS-MON-MIB", "portsBroadcastThreshold"))
if mibBuilder.loadTexts: portsBroadcastExceeded.setStatus('current')
if mibBuilder.loadTexts: portsBroadcastExceeded.setDescription('The portsBroadcastExceeded notification indicates that the sending\n             agent sense that the level of broadcast-limit has passed the\n             program threshold.')
portsCRCErrExceeded = NotificationType((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 0, 5)).setObjects(("PRVT-SYS-MON-MIB", "monPortCRCErr"), ("PRVT-SYS-MON-MIB", "portsCRCErrThreshold"))
if mibBuilder.loadTexts: portsCRCErrExceeded.setStatus('current')
if mibBuilder.loadTexts: portsCRCErrExceeded.setDescription('The portsCRCErrExceeded notification indicates that the sending\n             agent sense that the level of CRC error has passed the\n             program threshold.')
portsRuntsExceeded = NotificationType((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 0, 6)).setObjects(("PRVT-SYS-MON-MIB", "monPortRunts"), ("PRVT-SYS-MON-MIB", "portsRuntsThreshold"))
if mibBuilder.loadTexts: portsRuntsExceeded.setStatus('current')
if mibBuilder.loadTexts: portsRuntsExceeded.setDescription('The portsRuntsExceeded notification indicates that the sending\n            agent sense that the level of runts has passed the\n            program threshold.')
portsOverSizeExceeded = NotificationType((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 0, 7)).setObjects(("PRVT-SYS-MON-MIB", "monPortOverSize"), ("PRVT-SYS-MON-MIB", "portsOverSizeThreshold"))
if mibBuilder.loadTexts: portsOverSizeExceeded.setStatus('current')
if mibBuilder.loadTexts: portsOverSizeExceeded.setDescription('The portsOverSizeExceeded notification indicates that the sending\n            agent sense that the level of oversize has passed the\n            program threshold.')
laserTemperatureThresholdCrossed = NotificationType((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 0, 8)).setObjects(("PRVT-SYS-MON-MIB", "laserTemperature"), ("PRVT-SYS-MON-MIB", "laserTemperatureHighThreshold"), ("PRVT-SYS-MON-MIB", "laserTemperatureLowThreshold"))
if mibBuilder.loadTexts: laserTemperatureThresholdCrossed.setStatus('current')
if mibBuilder.loadTexts: laserTemperatureThresholdCrossed.setDescription('The laserTemperatureThresholdCrossed shall be generated \n\t\t\t\t\twhen laserTemperature rises above laserHighTemperatureThreshold \n\t\t\t\t\tor falls below laserTemperatureLowThreshold. Also the \n\t\t\t\t\tnotification shall be generated when laserTemperature\n\t\t\t\t \treturns to the normal range between laserHighTemperatureThreshold \n\t\t\t\t\tand laserTemperatureLowThreshold.')
laserTxPowerThresholdCrossed = NotificationType((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 0, 9)).setObjects(("PRVT-SYS-MON-MIB", "laserTxPower"), ("PRVT-SYS-MON-MIB", "laserTxPowerHighThreshold"), ("PRVT-SYS-MON-MIB", "laserTxPowerLowThreshold"))
if mibBuilder.loadTexts: laserTxPowerThresholdCrossed.setStatus('current')
if mibBuilder.loadTexts: laserTxPowerThresholdCrossed.setDescription('The laserTxPowerThresholdCrossed shall be generated\n\t\t\t\t\t\t\twhen laserTxPower rises above laserHighTxPowerThreshold\n\t\t\t\t\t\t\tor falls below laserTxPowerLowThreshold. Also the \n\t\t\t\t\t\t\tnotification shall be generated when laserTxPower \n\t\t\t\t\t\t\treturns to the normal range between \n\t\t\t\t\t\t\tlaserHighTxPowerThreshold and laserTxPowerLowThreshold.')
laserRxPowerThresholdCrossed = NotificationType((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 0, 10)).setObjects(("PRVT-SYS-MON-MIB", "laserRxPower"), ("PRVT-SYS-MON-MIB", "laserRxPowerHighThreshold"), ("PRVT-SYS-MON-MIB", "laserRxPowerLowThreshold"))
if mibBuilder.loadTexts: laserRxPowerThresholdCrossed.setStatus('current')
if mibBuilder.loadTexts: laserRxPowerThresholdCrossed.setDescription('The laserRxPowerThresholdCrossed shall be generated \n\t\t\t\t\t\t\twhen laserRxPower rises above laserHighRxPowerThreshold \n\t\t\t\t\t\t\tor falls below laserRxPowerLowThreshold. Also the \n\t\t\t\t\t\t\tnotification shall be generated when laserRxPower \n\t\t\t\t\t\t\treturns to the normal range between \n\t\t\t\t\t\t\tlaserHighRxPowerThreshold and laserRxPowerLowThreshold.')
sfpMonStatusChanged = NotificationType((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 0, 11)).setObjects(("PRVT-SYS-MON-MIB", "sfpMonStatus"))
if mibBuilder.loadTexts: sfpMonStatusChanged.setStatus('current')
if mibBuilder.loadTexts: sfpMonStatusChanged.setDescription('This trap will be send only if the SFP is inserted or extracted')
sfpPortManTable = MibTable((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 2, 5), )
if mibBuilder.loadTexts: sfpPortManTable.setStatus('current')
if mibBuilder.loadTexts: sfpPortManTable.setDescription('This table  will be responsible for managing SFPs.')
sfpPortManEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 2, 5, 1), ).setIndexNames((0, "PRVT-SWITCH-MIB", "reportsL2IfaceUnit"), (0, "PRVT-SWITCH-MIB", "reportsL2IfaceSlot"), (0, "PRVT-SWITCH-MIB", "reportsL2IfacePort"), (0, "PRVT-SWITCH-MIB", "reportsIfJackIndex"))
if mibBuilder.loadTexts: sfpPortManEntry.setStatus('current')
if mibBuilder.loadTexts: sfpPortManEntry.setDescription('')
sfpMonStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 2, 5, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("sfpInserted", 1), ("sfpExtracted", 2), ("sfpUnknown", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpMonStatus.setStatus('current')
if mibBuilder.loadTexts: sfpMonStatus.setDescription('This object gives information is SFP is inserted or not in the port.')
sfpVendor = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 2, 5, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 9)).clone(hexValue="")).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpVendor.setStatus('current')
if mibBuilder.loadTexts: sfpVendor.setDescription('This object gives SFP vendor name.')
sfpPN = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 2, 5, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 9)).clone(hexValue="")).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpPN.setStatus('current')
if mibBuilder.loadTexts: sfpPN.setDescription('This object gives SFP vendor name.')
sfpRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 2, 5, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 9)).clone(hexValue="")).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpRevision.setStatus('current')
if mibBuilder.loadTexts: sfpRevision.setDescription('This object gives SFP vendor revision.')
sfpLenght = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 2, 5, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 9)).clone(hexValue="")).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpLenght.setStatus('current')
if mibBuilder.loadTexts: sfpLenght.setDescription('This object gives information regarding link length.')
sfpConnector = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 2, 5, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 9)).clone(hexValue="")).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpConnector.setStatus('current')
if mibBuilder.loadTexts: sfpConnector.setDescription('This object gives SFP connector type.')
sysMonConfigTable = MibTable((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 3, 1), )
if mibBuilder.loadTexts: sysMonConfigTable.setStatus('current')
if mibBuilder.loadTexts: sysMonConfigTable.setDescription('This table configures periodic monitoring parameters.')
sysMonConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 3, 1, 1), ).setIndexNames((0, "PRVT-SYS-MON-MIB", "sysMonIndicator"))
if mibBuilder.loadTexts: sysMonConfigEntry.setStatus('current')
if mibBuilder.loadTexts: sysMonConfigEntry.setDescription('')
sysMonIndicator = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("cpu-usage", 1), ("ram-usage", 2), ("power-supply", 3), ("onboard-power", 4), ("fan", 5), ("temperature", 6), ("laser", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysMonIndicator.setStatus('current')
if mibBuilder.loadTexts: sysMonIndicator.setDescription('Enumeration.')
sysMonEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 3, 1, 1, 2), EnableStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysMonEnable.setStatus('current')
if mibBuilder.loadTexts: sysMonEnable.setDescription('Enabled/disabled')
sysMonPeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 3, 1, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysMonPeriod.setStatus('current')
if mibBuilder.loadTexts: sysMonPeriod.setDescription('Configure monitoring period in seconds.')
sysMonTrap = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 3, 1, 1, 4), EnableStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysMonTrap.setStatus('current')
if mibBuilder.loadTexts: sysMonTrap.setDescription('Enabled/disabled')
sysMonLog = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 3, 1, 1, 5), EnableStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysMonLog.setStatus('current')
if mibBuilder.loadTexts: sysMonLog.setDescription('Enabled/disabled')
sysMonLed = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 3, 1, 1, 6), EnableStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysMonLed.setStatus('current')
if mibBuilder.loadTexts: sysMonLed.setDescription('Enabled/disabled')
sysMonDefaults = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 3, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("noop", 0), ("reset", 1))).clone('noop')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysMonDefaults.setStatus('current')
if mibBuilder.loadTexts: sysMonDefaults.setDescription('If set to 1, resets all configurations to defaults.')
sysMonMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 2, 2))
sysMonNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 2, 2, 3)).setObjects(("PRVT-SYS-MON-MIB", "cpuUtilizationExceeded"), ("PRVT-SYS-MON-MIB", "ramFreeSpaceExceeded"), ("PRVT-SYS-MON-MIB", "portErrorsExceeded"), ("PRVT-SYS-MON-MIB", "portsBroadcastExceeded"), ("PRVT-SYS-MON-MIB", "portsCRCErrExceeded"), ("PRVT-SYS-MON-MIB", "portsRuntsExceeded"), ("PRVT-SYS-MON-MIB", "portsOverSizeExceeded"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sysMonNotificationGroup = sysMonNotificationGroup.setStatus('current')
if mibBuilder.loadTexts: sysMonNotificationGroup.setDescription('Private Notification Group.')
mibBuilder.exportSymbols("PRVT-SYS-MON-MIB", ramFreeSpaceExceeded=ramFreeSpaceExceeded, portsRuntsExceeded=portsRuntsExceeded, EnableStatus=EnableStatus, laserRxPowerLowThreshold=laserRxPowerLowThreshold, laserTemperatureHighThreshold=laserTemperatureHighThreshold, portsCRCErrExceeded=portsCRCErrExceeded, sysMonConfig=sysMonConfig, laserTemperatureLowThreshold=laserTemperatureLowThreshold, sysMonConfigTable=sysMonConfigTable, sysMonTrap=sysMonTrap, sfpStatus=sfpStatus, monCpuUtilization=monCpuUtilization, sysMonEnable=sysMonEnable, sysMonNotificationGroup=sysMonNotificationGroup, laserRxPowerThresholdCrossed=laserRxPowerThresholdCrossed, monPortBroadcast=monPortBroadcast, sfpVendor=sfpVendor, laserTxPower=laserTxPower, prvtSysMonMib=prvtSysMonMib, laserRxPower=laserRxPower, monPortsTable=monPortsTable, sysMonLed=sysMonLed, portsCRCErrThreshold=portsCRCErrThreshold, sfpPN=sfpPN, PYSNMP_MODULE_ID=prvtSysMonMib, prvtSysMonConformance=prvtSysMonConformance, portsOverSizeThreshold=portsOverSizeThreshold, sysMonValues=sysMonValues, sfpConnector=sfpConnector, sysMonConfigEntry=sysMonConfigEntry, sfpMonStatusChanged=sfpMonStatusChanged, monPortOverSize=monPortOverSize, sysMonMIBGroups=sysMonMIBGroups, laserPortThresholdTable=laserPortThresholdTable, monPortRunts=monPortRunts, portsBroadcastExceeded=portsBroadcastExceeded, sysMonPeriod=sysMonPeriod, laserPortThresholdEntry=laserPortThresholdEntry, sfpRevision=sfpRevision, laserTxPowerThresholdCrossed=laserTxPowerThresholdCrossed, sysMonThreshold=sysMonThreshold, portsBroadcastThreshold=portsBroadcastThreshold, laserPortValueEntry=laserPortValueEntry, portsRuntsThreshold=portsRuntsThreshold, portErrorsThreshold=portErrorsThreshold, monPortErrors=monPortErrors, monRamBytesFree=monRamBytesFree, ramBytesFreeThreshold=ramBytesFreeThreshold, cpuUtilizationExceeded=cpuUtilizationExceeded, laserRxPowerHighThreshold=laserRxPowerHighThreshold, monPortsEntry=monPortsEntry, laserPortValueTable=laserPortValueTable, laserTxPowerLowThreshold=laserTxPowerLowThreshold, laserTemperatureThresholdCrossed=laserTemperatureThresholdCrossed, sfpMonStatus=sfpMonStatus, sysMonLog=sysMonLog, sysMonDefaults=sysMonDefaults, sysMonIndicator=sysMonIndicator, portsOverSizeExceeded=portsOverSizeExceeded, sfpPortManTable=sfpPortManTable, monPortCRCErr=monPortCRCErr, software=software, laserTemperature=laserTemperature, portErrorsExceeded=portErrorsExceeded, sfpPortManEntry=sfpPortManEntry, sfpLenght=sfpLenght, prvtSysMonObjects=prvtSysMonObjects, laserTxPowerHighThreshold=laserTxPowerHighThreshold, cpuUtilizationThreshold=cpuUtilizationThreshold, prvtSysMonNotifications=prvtSysMonNotifications)
