#
# PySNMP MIB module SIAE-SENSOR-TEMP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/siae/SIAE-SENSOR-TEMP-MIB
# Produced by pysmi-1.1.3 at Sun Nov 21 00:48:51 2021
# On host fv-az39-63 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
AlarmStatus, AlarmSeverityCode = mibBuilder.importSymbols("SIAE-ALARM-MIB", "AlarmStatus", "AlarmSeverityCode")
siaeMib, = mibBuilder.importSymbols("SIAE-TREE-MIB", "siaeMib")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Counter32, MibIdentifier, iso, ModuleIdentity, TimeTicks, NotificationType, Gauge32, ObjectIdentity, Unsigned32, Bits, IpAddress, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Counter32", "MibIdentifier", "iso", "ModuleIdentity", "TimeTicks", "NotificationType", "Gauge32", "ObjectIdentity", "Unsigned32", "Bits", "IpAddress", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
sensorTemp = ModuleIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 77))
sensorTemp.setRevisions(('2016-05-03 00:00', '2014-03-31 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: sensorTemp.setRevisionsDescriptions(('MIB version 01.00.01\n             - Added sensorTempMonitorTable and sensorTempMonitorSystemControl\n             - Added DEFVAL clause to sensorTempAlarmThreshold1Severity and\n               sensorTempAlarmThreshold2Severity\n            ', 'Initial version 01.00.00\n            ',))
if mibBuilder.loadTexts: sensorTemp.setLastUpdated('201605030000Z')
if mibBuilder.loadTexts: sensorTemp.setOrganization('SIAE MICROELETTRONICA spa')
if mibBuilder.loadTexts: sensorTemp.setContactInfo('SIAE MICROELETTONICA s.p.a.\n             Via Michelangelo Buonarroti, 21\n             20093 - Cologno Monzese\n             Milano - ITALY\n             Phone :  +39-02-27325-1\n             E-mail: tbd@siaemic.com\n            ')
if mibBuilder.loadTexts: sensorTemp.setDescription('Management information for equipment heat.\n            ')
sensorTempMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 77, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensorTempMibVersion.setStatus('current')
if mibBuilder.loadTexts: sensorTempMibVersion.setDescription('Numerical version of this module.\n             The string version of this MIB have the following format:\n                XX.YY.ZZ\n             so, for example, the value 1 should be interpreted as 00.00.01\n             and the value 10001 should be interpreted as 01.00.01.')
sensorTempTable = MibTable((1, 3, 6, 1, 4, 1, 3373, 1103, 77, 2), )
if mibBuilder.loadTexts: sensorTempTable.setStatus('current')
if mibBuilder.loadTexts: sensorTempTable.setDescription('Table with sensorTemp device entries')
sensorTempEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3373, 1103, 77, 2, 1), ).setIndexNames((0, "SIAE-SENSOR-TEMP-MIB", "sensorTempIndex"))
if mibBuilder.loadTexts: sensorTempEntry.setStatus('current')
if mibBuilder.loadTexts: sensorTempEntry.setDescription('Temperature Sensor entry')
sensorTempIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 77, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensorTempIndex.setStatus('current')
if mibBuilder.loadTexts: sensorTempIndex.setDescription('Temperature Sensor index.\n            ')
sensorTempValue = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 77, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensorTempValue.setStatus('current')
if mibBuilder.loadTexts: sensorTempValue.setDescription('Value of the temperature (in Celsius).\n            ')
sensorTempThreshold1 = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 77, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensorTempThreshold1.setStatus('current')
if mibBuilder.loadTexts: sensorTempThreshold1.setDescription('This object can not be modified. It reports the temperature threshold 1.\n             When sensorTempValue exceeds this value sensorTempStatus1 becomes Active.\n             When threshold has been exceed status returns stand-by only when sensorTempValue\n             goes under sensorTempHysteresis1.\n            ')
sensorTempThreshold2 = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 77, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensorTempThreshold2.setStatus('current')
if mibBuilder.loadTexts: sensorTempThreshold2.setDescription('This object can not be modified. It reports the temperature threshold 2.\n             When sensorTempValue exceeds this value sensorTempStatus2 becomes Active.\n             When threshold has been exceed status returns stand-by only when sensorTempValue\n             goes under sensorTempHysteresis2.  \n            ')
sensorTempHysteresis1 = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 77, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensorTempHysteresis1.setStatus('current')
if mibBuilder.loadTexts: sensorTempHysteresis1.setDescription('This object can not be modified. It reports the temperature hysteresis 1.\n             When sensorTempStatus1 is Active it represents the value under which returns\n             cleared.\n            ')
sensorTempHysteresis2 = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 77, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensorTempHysteresis2.setStatus('current')
if mibBuilder.loadTexts: sensorTempHysteresis2.setDescription('This object can not be modified. It reports the temperature hysteresis 2.\n             When sensorTempStatus1 is Active it represents the value under which returns\n             cleared.  \n            ')
sensorTempStatus1 = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 77, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("cleared", 1), ("alarmed", 2), ("hysteresis", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensorTempStatus1.setStatus('current')
if mibBuilder.loadTexts: sensorTempStatus1.setDescription('This object is used to manage temperature related to sensorTempThreshold1.\n             Values mean:\n             cleared:    sensorTempValue is lower than threshold1\n             active:     sensorTempValue is greater than threshold1\n             hysteresis: sensorTempValue is between threshold1 and hysteresis1 but\n                         previuosly greater than thresold1.\n            ')
sensorTempStatus2 = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 77, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("cleared", 1), ("alarmed", 2), ("hysteresis", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensorTempStatus2.setStatus('current')
if mibBuilder.loadTexts: sensorTempStatus2.setDescription('This object is used to manage temperature related to sensorTempThreshold2.\n             Values mean:\n             cleared:    sensorTempValue is lower than threshold2\n             active:     sensorTempValue is greater than threshold2\n             hysteresis: sensorTempValue is between threshold2 and hysteresis2 but\n                         previuosly greater than thresold2.\n            ')
sensorTempLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 77, 2, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensorTempLabel.setStatus('current')
if mibBuilder.loadTexts: sensorTempLabel.setDescription('A textual string containing information on sensorTemp sensor.\n            ')
sensorTempAlarmThreshold1 = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 77, 3), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensorTempAlarmThreshold1.setStatus('current')
if mibBuilder.loadTexts: sensorTempAlarmThreshold1.setDescription('This object is used to notiy alarm if at least one entry in the\n             sensorTemp table has got sensorTempStatus1 alarmed.')
sensorTempAlarmThreshold2 = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 77, 4), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensorTempAlarmThreshold2.setStatus('current')
if mibBuilder.loadTexts: sensorTempAlarmThreshold2.setDescription('This object is used to notiy alarm if at least one entry in the\n             sensorTemp table has got sensorTempStatus2 alarmed.')
sensorTempAlarmThreshold1Severity = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 77, 5), AlarmSeverityCode().clone('warningTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensorTempAlarmThreshold1Severity.setStatus('current')
if mibBuilder.loadTexts: sensorTempAlarmThreshold1Severity.setDescription('This object is used to change severity of sensorTempAlarmThreshold1.')
sensorTempAlarmThreshold2Severity = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 77, 6), AlarmSeverityCode().clone('criticalTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensorTempAlarmThreshold2Severity.setStatus('current')
if mibBuilder.loadTexts: sensorTempAlarmThreshold2Severity.setDescription('This object is used to change severity of sensorTempAlarmThreshold2.')
sensorTempMonitorTable = MibTable((1, 3, 6, 1, 4, 1, 3373, 1103, 77, 7), )
if mibBuilder.loadTexts: sensorTempMonitorTable.setStatus('current')
if mibBuilder.loadTexts: sensorTempMonitorTable.setDescription('Table with sensorTempMonitor entries')
sensorTempMonitorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3373, 1103, 77, 7, 1), ).setIndexNames((0, "SIAE-SENSOR-TEMP-MIB", "sensorTempIndex"))
if mibBuilder.loadTexts: sensorTempMonitorEntry.setStatus('current')
if mibBuilder.loadTexts: sensorTempMonitorEntry.setDescription('Temperature Sensor Monitor entry')
sensorTempMonitorAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 77, 7, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2))).clone('down')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensorTempMonitorAdminStatus.setStatus('current')
if mibBuilder.loadTexts: sensorTempMonitorAdminStatus.setDescription("The desired state of the temperatuure monitor.\n            \n             When a managed system initializes, all the temperature\n             monitors start with sensorTempMonitorAdminStatus in the\n             down(2) state, it's a default state also. As a result\n             of either explicit management action or per configuration\n             information retained by the managed system,\n             sensorTempMonitorAdminStatus is then changed to the up(1)\n             state (or remains in the down(2) state).\n            ")
sensorTempMonitorOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 77, 7, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensorTempMonitorOperStatus.setStatus('current')
if mibBuilder.loadTexts: sensorTempMonitorOperStatus.setDescription('The current state of the temperatuure monitor. Usually\n             this object report the same value of sensorTempMonitorAdminStatus.\n             When there is some problem related to the temperature sensor,\n             this object shown the down(2) value even if sensorTempMonitorAdminStatus\n             is set to up(1).\n            ')
sensorTempMonitorMinTemp = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 77, 7, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensorTempMonitorMinTemp.setStatus('current')
if mibBuilder.loadTexts: sensorTempMonitorMinTemp.setDescription('The minimum value of the temperature measured in the last actual\n             900 seconds. The value is expressed in degrees Celsius.\n            ')
sensorTempMonitorMaxTemp = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 77, 7, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensorTempMonitorMaxTemp.setStatus('current')
if mibBuilder.loadTexts: sensorTempMonitorMaxTemp.setDescription('The maximum value of the temperature measured in the last actual\n             900 seconds. The value is expressed in degrees Celsius.\n            ')
sensorTempMonitorAverageTemp = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 77, 7, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensorTempMonitorAverageTemp.setStatus('current')
if mibBuilder.loadTexts: sensorTempMonitorAverageTemp.setDescription('The average value of the temperature measured in the last actual\n             900 seconds. The value is expressed in tenth of degrees Celsius.\n            ')
sensorTempMonitorSystemControl = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 77, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("start", 1), ("shutdown", 2))).clone('shutdown')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensorTempMonitorSystemControl.setStatus('current')
if mibBuilder.loadTexts: sensorTempMonitorSystemControl.setDescription("The administrative system control status requested by management\n             for the TEMP-MONITOR feature. The value 'start'(1) indicates that\n             TEMP-MONITOR should be supported in the device on all temperature\n             sensors that have this capability (Those shown in \n             sensorTempMonitorTable). The value shutdown(2) indicates\n             that TEMP-MONITOR should be shutdown in the device on all\n             temperature sensors.\n            ")
mibBuilder.exportSymbols("SIAE-SENSOR-TEMP-MIB", sensorTempMibVersion=sensorTempMibVersion, sensorTempAlarmThreshold1Severity=sensorTempAlarmThreshold1Severity, sensorTempAlarmThreshold2=sensorTempAlarmThreshold2, sensorTempMonitorAverageTemp=sensorTempMonitorAverageTemp, sensorTempLabel=sensorTempLabel, sensorTempValue=sensorTempValue, sensorTempMonitorMaxTemp=sensorTempMonitorMaxTemp, sensorTempMonitorTable=sensorTempMonitorTable, sensorTempThreshold1=sensorTempThreshold1, sensorTempMonitorOperStatus=sensorTempMonitorOperStatus, sensorTempAlarmThreshold1=sensorTempAlarmThreshold1, sensorTempHysteresis2=sensorTempHysteresis2, sensorTempEntry=sensorTempEntry, sensorTempAlarmThreshold2Severity=sensorTempAlarmThreshold2Severity, PYSNMP_MODULE_ID=sensorTemp, sensorTempStatus1=sensorTempStatus1, sensorTempStatus2=sensorTempStatus2, sensorTempMonitorAdminStatus=sensorTempMonitorAdminStatus, sensorTempTable=sensorTempTable, sensorTempMonitorEntry=sensorTempMonitorEntry, sensorTempHysteresis1=sensorTempHysteresis1, sensorTempIndex=sensorTempIndex, sensorTemp=sensorTemp, sensorTempMonitorSystemControl=sensorTempMonitorSystemControl, sensorTempThreshold2=sensorTempThreshold2, sensorTempMonitorMinTemp=sensorTempMonitorMinTemp)
