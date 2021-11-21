#
# PySNMP MIB module PRVT-LMM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/telco-systems/binox/PRVT-LMM-MIB
# Produced by pysmi-1.1.3 at Sun Nov 21 00:45:53 2021
# On host fv-az39-63 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
switch, = mibBuilder.importSymbols("PRVT-SWITCH-MIB", "switch")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, Counter64, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Gauge32, TimeTicks, IpAddress, NotificationType, Counter32, MibIdentifier, Bits, ModuleIdentity, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Counter64", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Gauge32", "TimeTicks", "IpAddress", "NotificationType", "Counter32", "MibIdentifier", "Bits", "ModuleIdentity", "Integer32")
TextualConvention, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TruthValue")
prvtLmmMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 738, 10, 5, 172))
prvtLmmMIB.setRevisions(('2011-10-11 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: prvtLmmMIB.setRevisionsDescriptions(('Initial release',))
if mibBuilder.loadTexts: prvtLmmMIB.setLastUpdated('201110110000Z')
if mibBuilder.loadTexts: prvtLmmMIB.setOrganization('BATM Advanced Communication')
if mibBuilder.loadTexts: prvtLmmMIB.setContactInfo('BATM/Telco Systems Support team\n         Email:\n         For North America: techsupport@telco.com\n         For North Europe: support@batm.de, info@batm.de\n         For the rest of the world: techsupport@telco.com')
if mibBuilder.loadTexts: prvtLmmMIB.setDescription('Initial version. This MIB will configure laser monitoring')
prvtLmmNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 10, 5, 172, 0))
prvtLmmObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 10, 5, 172, 1))
prvtLmmShutdown = MibScalar((1, 3, 6, 1, 4, 1, 738, 10, 5, 172, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtLmmShutdown.setStatus('current')
if mibBuilder.loadTexts: prvtLmmShutdown.setDescription('Enable/disable laser monitoring')
prvtLmmDebug = MibScalar((1, 3, 6, 1, 4, 1, 738, 10, 5, 172, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtLmmDebug.setStatus('current')
if mibBuilder.loadTexts: prvtLmmDebug.setDescription('Enable/Disable laser monitoring')
prvtLmmPeriod = MibScalar((1, 3, 6, 1, 4, 1, 738, 10, 5, 172, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtLmmPeriod.setStatus('current')
if mibBuilder.loadTexts: prvtLmmPeriod.setDescription('Specify the monitoring interval (sec).')
prvtLmmTrap = MibScalar((1, 3, 6, 1, 4, 1, 738, 10, 5, 172, 1, 4), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtLmmTrap.setStatus('current')
if mibBuilder.loadTexts: prvtLmmTrap.setDescription('Enable/Disable sending SNMP traps when thresholds are crossed')
prvtLmmLog = MibScalar((1, 3, 6, 1, 4, 1, 738, 10, 5, 172, 1, 5), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtLmmLog.setStatus('current')
if mibBuilder.loadTexts: prvtLmmLog.setDescription('Enable/Disable alert notification logging when thresholds are crossed')
prvtLmmLed = MibScalar((1, 3, 6, 1, 4, 1, 738, 10, 5, 172, 1, 6), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtLmmLed.setStatus('current')
if mibBuilder.loadTexts: prvtLmmLed.setDescription('Enable/Disable LED-alert notifications when thresholds are crossed')
prvtLmmTemperatureHighThreshold = MibScalar((1, 3, 6, 1, 4, 1, 738, 10, 5, 172, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-128, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtLmmTemperatureHighThreshold.setStatus('current')
if mibBuilder.loadTexts: prvtLmmTemperatureHighThreshold.setDescription('Specify the low threshold value for global temperature (-128 up to 128).\n         prvtLmmTemperatureHighThreshold must be higher than prvtLmmTemperatureLowThreshold')
prvtLmmTemperatureLowThreshold = MibScalar((1, 3, 6, 1, 4, 1, 738, 10, 5, 172, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-128, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtLmmTemperatureLowThreshold.setStatus('current')
if mibBuilder.loadTexts: prvtLmmTemperatureLowThreshold.setDescription('Specify the low threshold value for global temperature (-128 up to 128).\n         prvtLmmTemperatureHighThreshold must be higher than prvtLmmTemperatureLowThreshold')
prvtLmmRxPowerLowThreshold = MibScalar((1, 3, 6, 1, 4, 1, 738, 10, 5, 172, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-40, 8))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtLmmRxPowerLowThreshold.setStatus('current')
if mibBuilder.loadTexts: prvtLmmRxPowerLowThreshold.setDescription('Specify the low threshold value for global RX-power (-40 up to 8)\n         prvtLmmRxPowerHighThreshold must be higher than prvtLmmRxPowerLowThreshold')
prvtLmmRxPowerHighThreshold = MibScalar((1, 3, 6, 1, 4, 1, 738, 10, 5, 172, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-40, 8))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtLmmRxPowerHighThreshold.setStatus('current')
if mibBuilder.loadTexts: prvtLmmRxPowerHighThreshold.setDescription('Specify the high threshold value for global RX-power (-40 up to 8)\n         prvtLmmRxPowerHighThreshold must be higher than prvtLmmRxPowerLowThreshold')
prvtLmmTxPowerLowThreshold = MibScalar((1, 3, 6, 1, 4, 1, 738, 10, 5, 172, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-40, 8))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtLmmTxPowerLowThreshold.setStatus('current')
if mibBuilder.loadTexts: prvtLmmTxPowerLowThreshold.setDescription('Specify the low threshold value for global RX-power (-40 up to 8)\n         prvtLmmTxPowerHighThreshold must be higher than prvtLmmTxPowerLowThreshold')
prvtLmmTxPowerHighThreshold = MibScalar((1, 3, 6, 1, 4, 1, 738, 10, 5, 172, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-40, 8))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtLmmTxPowerHighThreshold.setStatus('current')
if mibBuilder.loadTexts: prvtLmmTxPowerHighThreshold.setDescription('Specify the high threshold value for global RX-power (-40 up to 8)\n         prvtLmmTxPowerHighThreshold must be higher than prvtLmmTxPowerLowThreshold')
prvtLmmInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 738, 10, 5, 172, 1, 13), )
if mibBuilder.loadTexts: prvtLmmInterfaceTable.setStatus('current')
if mibBuilder.loadTexts: prvtLmmInterfaceTable.setDescription('Lmm configuration per ethernet port')
prvtLmmInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 10, 5, 172, 1, 13, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: prvtLmmInterfaceEntry.setStatus('current')
if mibBuilder.loadTexts: prvtLmmInterfaceEntry.setDescription('The Stack table entry')
prvtLmmInterfaceShutdown = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 172, 1, 13, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtLmmInterfaceShutdown.setStatus('current')
if mibBuilder.loadTexts: prvtLmmInterfaceShutdown.setDescription('Enable/Disable laser monitoring on port')
prvtLmmInterfaceTempLowThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 172, 1, 13, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-128, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtLmmInterfaceTempLowThreshold.setStatus('current')
if mibBuilder.loadTexts: prvtLmmInterfaceTempLowThreshold.setDescription('Specify the low threshold value for port temperature')
prvtLmmInterfaceTempHighThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 172, 1, 13, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-128, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtLmmInterfaceTempHighThreshold.setStatus('current')
if mibBuilder.loadTexts: prvtLmmInterfaceTempHighThreshold.setDescription('Specify the high threshold value for port temperature.\n         Value of prvtLmmInterfaceTempHighThreshold must be greater than \n         prvtLmmInterfaceTempLowThreshold')
prvtLmmInterfaceTempValue = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 172, 1, 13, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtLmmInterfaceTempValue.setStatus('current')
if mibBuilder.loadTexts: prvtLmmInterfaceTempValue.setDescription('Display laser Temperature current value')
prvtLmmInterfaceTempThresholdLo = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 172, 1, 13, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtLmmInterfaceTempThresholdLo.setStatus('current')
if mibBuilder.loadTexts: prvtLmmInterfaceTempThresholdLo.setDescription('The thresholds read from hardware or set by user')
prvtLmmInterfaceTempThresholdHi = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 172, 1, 13, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtLmmInterfaceTempThresholdHi.setStatus('current')
if mibBuilder.loadTexts: prvtLmmInterfaceTempThresholdHi.setDescription('The thresholds read from hardware or set by user')
prvtLmmInterfaceTempTestState = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 172, 1, 13, 1, 7), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtLmmInterfaceTempTestState.setStatus('current')
if mibBuilder.loadTexts: prvtLmmInterfaceTempTestState.setDescription('The state test')
prvtLmmInterfaceRxPowerLowThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 172, 1, 13, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-40, 8))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtLmmInterfaceRxPowerLowThreshold.setStatus('current')
if mibBuilder.loadTexts: prvtLmmInterfaceRxPowerLowThreshold.setDescription('Specify the low threshold value for port RX-power.')
prvtLmmInterfaceRxPowerHighThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 172, 1, 13, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-40, 8))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtLmmInterfaceRxPowerHighThreshold.setStatus('current')
if mibBuilder.loadTexts: prvtLmmInterfaceRxPowerHighThreshold.setDescription('Specify the high threshold value for port RX-power.\n         Value of prvtLmmInterfaceRxPowerHighThreshold must be greater than\n         prvtLmmInterfaceRxPowerLowThreshold')
prvtLmmInterfaceRxPowerValue = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 172, 1, 13, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtLmmInterfaceRxPowerValue.setStatus('current')
if mibBuilder.loadTexts: prvtLmmInterfaceRxPowerValue.setDescription('Display laser Rx Power current value')
prvtLmmInterfaceRxPowerThresholdRxLo = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 172, 1, 13, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtLmmInterfaceRxPowerThresholdRxLo.setStatus('current')
if mibBuilder.loadTexts: prvtLmmInterfaceRxPowerThresholdRxLo.setDescription('The thresholds read from hardware or set by user')
prvtLmmInterfaceRxPowerThresholdRxHi = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 172, 1, 13, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtLmmInterfaceRxPowerThresholdRxHi.setStatus('current')
if mibBuilder.loadTexts: prvtLmmInterfaceRxPowerThresholdRxHi.setDescription('The thresholds read from hardware or set by user')
prvtLmmInterfaceRxPowerTestState = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 172, 1, 13, 1, 13), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtLmmInterfaceRxPowerTestState.setStatus('current')
if mibBuilder.loadTexts: prvtLmmInterfaceRxPowerTestState.setDescription('The state test')
prvtLmmInterfaceTxPowerLowThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 172, 1, 13, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-40, 8))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtLmmInterfaceTxPowerLowThreshold.setStatus('current')
if mibBuilder.loadTexts: prvtLmmInterfaceTxPowerLowThreshold.setDescription('Specify the low threshold value for port TX-power')
prvtLmmInterfaceTxPowerHighThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 172, 1, 13, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-40, 8))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtLmmInterfaceTxPowerHighThreshold.setStatus('current')
if mibBuilder.loadTexts: prvtLmmInterfaceTxPowerHighThreshold.setDescription('Specify the high threshold value for port TX-power\n         Value of prvtLmmInterfaceTxPowerHighThreshold must be greater than\n         prvtLmmInterfaceTxPowerLowThreshold')
prvtLmmInterfaceTxPowerValue = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 172, 1, 13, 1, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtLmmInterfaceTxPowerValue.setStatus('current')
if mibBuilder.loadTexts: prvtLmmInterfaceTxPowerValue.setDescription('Display laser Tx Power current value')
prvtLmmInterfaceTxPowerThresholdTxLo = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 172, 1, 13, 1, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtLmmInterfaceTxPowerThresholdTxLo.setStatus('current')
if mibBuilder.loadTexts: prvtLmmInterfaceTxPowerThresholdTxLo.setDescription('The thresholds read from hardware or set by user')
prvtLmmInterfaceTxPowerThresholdTxHi = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 172, 1, 13, 1, 18), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtLmmInterfaceTxPowerThresholdTxHi.setStatus('current')
if mibBuilder.loadTexts: prvtLmmInterfaceTxPowerThresholdTxHi.setDescription('The thresholds read from hardware or set by user')
prvtLmmInterfaceTxPowerTestState = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 172, 1, 13, 1, 19), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtLmmInterfaceTxPowerTestState.setStatus('current')
if mibBuilder.loadTexts: prvtLmmInterfaceTxPowerTestState.setDescription('The state test')
prvtLmmInterfaceOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 172, 1, 13, 1, 20), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtLmmInterfaceOperStatus.setStatus('current')
if mibBuilder.loadTexts: prvtLmmInterfaceOperStatus.setDescription('Operational status')
prvtLmmTemperatureThresholdCrossed = NotificationType((1, 3, 6, 1, 4, 1, 738, 10, 5, 172, 0, 1)).setObjects(("PRVT-LMM-MIB", "prvtLmmInterfaceTempValue"), ("PRVT-LMM-MIB", "prvtLmmInterfaceTempThresholdHi"), ("PRVT-LMM-MIB", "prvtLmmInterfaceTempThresholdLo"))
if mibBuilder.loadTexts: prvtLmmTemperatureThresholdCrossed.setStatus('current')
if mibBuilder.loadTexts: prvtLmmTemperatureThresholdCrossed.setDescription('The prvtLmmTemperatureThresholdCrossed shall be generated \n         when prvtLmmInterfaceTempValue rises above prvtLmmInterfaceTempThresholdHi\n         or falls below prvtLmmInterfaceTempThresholdLo. Also the \n         notification shall be generated when prvtLmmInterfaceTempValue\n         returns to the normal range between prvtLmmInterfaceTempThresholdHi \n         and prvtLmmInterfaceTempThresholdLo.')
prvtLmmTxPowerThresholdCrossed = NotificationType((1, 3, 6, 1, 4, 1, 738, 10, 5, 172, 0, 2)).setObjects(("PRVT-LMM-MIB", "prvtLmmInterfaceTxPowerValue"), ("PRVT-LMM-MIB", "prvtLmmInterfaceTxPowerThresholdTxHi"), ("PRVT-LMM-MIB", "prvtLmmInterfaceTxPowerThresholdTxLo"))
if mibBuilder.loadTexts: prvtLmmTxPowerThresholdCrossed.setStatus('current')
if mibBuilder.loadTexts: prvtLmmTxPowerThresholdCrossed.setDescription('The prvtLmmTxPowerThresholdCrossed shall be generated \n         when prvtLmmInterfaceTxPowerValue rises above prvtLmmInterfaceTxPowerThresholdTxHi\n         or falls below prvtLmmInterfaceTxPowerThresholdTxLo. Also the \n         notification shall be generated when prvtLmmInterfaceTxPowerValue\n         returns to the normal range between prvtLmmInterfaceTxPowerThresholdTxHi \n         and prvtLmmInterfaceTxPowerThresholdTxLo.')
prvtLmmRxPowerThresholdCrossed = NotificationType((1, 3, 6, 1, 4, 1, 738, 10, 5, 172, 0, 3)).setObjects(("PRVT-LMM-MIB", "prvtLmmInterfaceRxPowerValue"), ("PRVT-LMM-MIB", "prvtLmmInterfaceRxPowerThresholdRxHi"), ("PRVT-LMM-MIB", "prvtLmmInterfaceRxPowerThresholdRxLo"))
if mibBuilder.loadTexts: prvtLmmRxPowerThresholdCrossed.setStatus('current')
if mibBuilder.loadTexts: prvtLmmRxPowerThresholdCrossed.setDescription('The prvtLmmRxPowerThresholdCrossed shall be generated \n         when prvtLmmInterfaceRxPowerValue rises above prvtLmmInterfaceRxPowerThresholdRxHi\n         or falls below prvtLmmInterfaceRxPowerThresholdRxLo. Also the \n         notification shall be generated when prvtLmmInterfaceRxPowerValue\n         returns to the normal range between prvtLmmInterfaceRxPowerThresholdRxHi \n         and prvtLmmInterfaceRxPowerThresholdRxLo.')
mibBuilder.exportSymbols("PRVT-LMM-MIB", prvtLmmInterfaceTempTestState=prvtLmmInterfaceTempTestState, prvtLmmInterfaceRxPowerHighThreshold=prvtLmmInterfaceRxPowerHighThreshold, prvtLmmRxPowerThresholdCrossed=prvtLmmRxPowerThresholdCrossed, prvtLmmLed=prvtLmmLed, prvtLmmShutdown=prvtLmmShutdown, prvtLmmInterfaceRxPowerLowThreshold=prvtLmmInterfaceRxPowerLowThreshold, prvtLmmTemperatureThresholdCrossed=prvtLmmTemperatureThresholdCrossed, prvtLmmInterfaceOperStatus=prvtLmmInterfaceOperStatus, prvtLmmInterfaceTxPowerTestState=prvtLmmInterfaceTxPowerTestState, prvtLmmTemperatureLowThreshold=prvtLmmTemperatureLowThreshold, prvtLmmDebug=prvtLmmDebug, prvtLmmNotifications=prvtLmmNotifications, prvtLmmTxPowerThresholdCrossed=prvtLmmTxPowerThresholdCrossed, prvtLmmPeriod=prvtLmmPeriod, prvtLmmLog=prvtLmmLog, prvtLmmInterfaceEntry=prvtLmmInterfaceEntry, prvtLmmTxPowerLowThreshold=prvtLmmTxPowerLowThreshold, prvtLmmRxPowerHighThreshold=prvtLmmRxPowerHighThreshold, prvtLmmInterfaceRxPowerThresholdRxHi=prvtLmmInterfaceRxPowerThresholdRxHi, prvtLmmInterfaceShutdown=prvtLmmInterfaceShutdown, prvtLmmInterfaceTxPowerThresholdTxHi=prvtLmmInterfaceTxPowerThresholdTxHi, prvtLmmInterfaceTempValue=prvtLmmInterfaceTempValue, prvtLmmInterfaceRxPowerThresholdRxLo=prvtLmmInterfaceRxPowerThresholdRxLo, prvtLmmInterfaceTxPowerThresholdTxLo=prvtLmmInterfaceTxPowerThresholdTxLo, prvtLmmObjects=prvtLmmObjects, prvtLmmTemperatureHighThreshold=prvtLmmTemperatureHighThreshold, prvtLmmInterfaceRxPowerValue=prvtLmmInterfaceRxPowerValue, prvtLmmInterfaceTempLowThreshold=prvtLmmInterfaceTempLowThreshold, prvtLmmInterfaceTempThresholdLo=prvtLmmInterfaceTempThresholdLo, prvtLmmTrap=prvtLmmTrap, prvtLmmInterfaceRxPowerTestState=prvtLmmInterfaceRxPowerTestState, prvtLmmInterfaceTxPowerValue=prvtLmmInterfaceTxPowerValue, prvtLmmMIB=prvtLmmMIB, prvtLmmInterfaceTxPowerHighThreshold=prvtLmmInterfaceTxPowerHighThreshold, prvtLmmRxPowerLowThreshold=prvtLmmRxPowerLowThreshold, prvtLmmInterfaceTable=prvtLmmInterfaceTable, prvtLmmInterfaceTempHighThreshold=prvtLmmInterfaceTempHighThreshold, prvtLmmInterfaceTempThresholdHi=prvtLmmInterfaceTempThresholdHi, prvtLmmTxPowerHighThreshold=prvtLmmTxPowerHighThreshold, prvtLmmInterfaceTxPowerLowThreshold=prvtLmmInterfaceTxPowerLowThreshold, PYSNMP_MODULE_ID=prvtLmmMIB)
