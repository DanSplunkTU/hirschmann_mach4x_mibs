#
# PySNMP MIB module EdgeSwitch-BOXSERVICES-PRIVATE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/edgeswitch/EdgeSwitch-BOXSERVICES-PRIVATE-MIB
# Produced by pysmi-1.1.8 at Mon Feb  7 16:11:34 2022
# On host fv-az42-619 platform Linux version 5.11.0-1028-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
fastPath, = mibBuilder.importSymbols("EdgeSwitch-REF-MIB", "fastPath")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, Counter32, Unsigned32, TimeTicks, ModuleIdentity, Counter64, MibIdentifier, Integer32, Gauge32, IpAddress, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Counter32", "Unsigned32", "TimeTicks", "ModuleIdentity", "Counter64", "MibIdentifier", "Integer32", "Gauge32", "IpAddress", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
fastPathBoxServices = ModuleIdentity((1, 3, 6, 1, 4, 1, 4413, 1, 1, 43))
fastPathBoxServices.setRevisions(('2011-01-26 00:00', '2008-02-22 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: fastPathBoxServices.setRevisionsDescriptions(('Postal address updated.', 'Ubiquiti branding related changes.',))
if mibBuilder.loadTexts: fastPathBoxServices.setLastUpdated('201101260000Z')
if mibBuilder.loadTexts: fastPathBoxServices.setOrganization('Broadcom Inc')
if mibBuilder.loadTexts: fastPathBoxServices.setContactInfo('')
if mibBuilder.loadTexts: fastPathBoxServices.setDescription('The Ubiquiti Private MIB for EdgeSwitch Box Services Feature.')
class BoxsTemperatureStatus(TextualConvention, Integer32):
    description = 'The temperature state'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("low", 0), ("normal", 1), ("warning", 2), ("critical", 3), ("shutdown", 4), ("notpresent", 5), ("notoperational", 6))

boxServicesGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 1, 1, 43, 1))
boxServicesNormalTempRangeMin = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 43, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-100, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: boxServicesNormalTempRangeMin.setStatus('current')
if mibBuilder.loadTexts: boxServicesNormalTempRangeMin.setDescription(' Lower boundary of normal temperature range.')
boxServicesNormalTempRangeMax = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 43, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-100, 100)).clone(45)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: boxServicesNormalTempRangeMax.setStatus('current')
if mibBuilder.loadTexts: boxServicesNormalTempRangeMax.setDescription(' Upper boundary of normal temperature range.')
boxServicesTemperatureTrapEnable = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 43, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: boxServicesTemperatureTrapEnable.setStatus('current')
if mibBuilder.loadTexts: boxServicesTemperatureTrapEnable.setDescription(' Enable or disable temperature change event trap, raised when temperature crosses boundaries of normal range')
boxServicesPSMStateTrapEnable = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 43, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: boxServicesPSMStateTrapEnable.setStatus('current')
if mibBuilder.loadTexts: boxServicesPSMStateTrapEnable.setDescription(' Enable or disable Power Supply Module state change trap.')
boxServicesFanStateTrapEnable = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 43, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: boxServicesFanStateTrapEnable.setStatus('current')
if mibBuilder.loadTexts: boxServicesFanStateTrapEnable.setDescription(' Enable or disable Fan state change trap.')
boxServicesThermalShutdownSensor = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 43, 1, 13), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: boxServicesThermalShutdownSensor.setStatus('current')
if mibBuilder.loadTexts: boxServicesThermalShutdownSensor.setDescription('The number of the sensor which initiated thermal shutdown.')
boxServicesThermalShutdownTemperature = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 43, 1, 14), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: boxServicesThermalShutdownTemperature.setStatus('current')
if mibBuilder.loadTexts: boxServicesThermalShutdownTemperature.setDescription('The temperature of the sensor which initiated thermal shutdown.')
boxServicesFansTable = MibTable((1, 3, 6, 1, 4, 1, 4413, 1, 1, 43, 1, 6), )
if mibBuilder.loadTexts: boxServicesFansTable.setStatus('current')
if mibBuilder.loadTexts: boxServicesFansTable.setDescription('Fan')
boxServicesFansEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4413, 1, 1, 43, 1, 6, 1), ).setIndexNames((0, "EdgeSwitch-BOXSERVICES-PRIVATE-MIB", "boxServicesFanUnitIndex"), (0, "EdgeSwitch-BOXSERVICES-PRIVATE-MIB", "boxServicesFansIndex"))
if mibBuilder.loadTexts: boxServicesFansEntry.setStatus('current')
if mibBuilder.loadTexts: boxServicesFansEntry.setDescription('Box Services Fan Entry')
boxServicesFanUnitIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 43, 1, 6, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: boxServicesFanUnitIndex.setStatus('current')
if mibBuilder.loadTexts: boxServicesFanUnitIndex.setDescription('Unit index for an entry in the Box Services Fan Table')
boxServicesFansIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 43, 1, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: boxServicesFansIndex.setStatus('current')
if mibBuilder.loadTexts: boxServicesFansIndex.setDescription('Unique index of fan table entry')
boxServicesFanItemType = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 43, 1, 6, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("fixed", 1), ("removable", 2), ("fixedAC", 3), ("removableDC", 4), ("fixedDC", 5), ("removableAC", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: boxServicesFanItemType.setStatus('current')
if mibBuilder.loadTexts: boxServicesFanItemType.setDescription('The type of fan')
boxServicesFanItemState = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 43, 1, 6, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("notpresent", 1), ("operational", 2), ("failed", 3), ("powering", 4), ("nopower", 5), ("notpowering", 6), ("incompatible", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: boxServicesFanItemState.setStatus('current')
if mibBuilder.loadTexts: boxServicesFanItemState.setDescription('The status of fan. nopower(4) - This state means the fan is present but no AC is connected.')
boxServicesFanSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 43, 1, 6, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(13, 13)).setFixedLength(13)).setMaxAccess("readonly")
if mibBuilder.loadTexts: boxServicesFanSpeed.setStatus('current')
if mibBuilder.loadTexts: boxServicesFanSpeed.setDescription('The speed of fan')
boxServicesFanDutyLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 43, 1, 6, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(13, 13)).setFixedLength(13)).setMaxAccess("readonly")
if mibBuilder.loadTexts: boxServicesFanDutyLevel.setStatus('current')
if mibBuilder.loadTexts: boxServicesFanDutyLevel.setDescription('The duty level of fan, in percents')
boxServicesPowSuppliesTable = MibTable((1, 3, 6, 1, 4, 1, 4413, 1, 1, 43, 1, 7), )
if mibBuilder.loadTexts: boxServicesPowSuppliesTable.setStatus('current')
if mibBuilder.loadTexts: boxServicesPowSuppliesTable.setDescription('Power supply')
boxServicesPowSuppliesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4413, 1, 1, 43, 1, 7, 1), ).setIndexNames((0, "EdgeSwitch-BOXSERVICES-PRIVATE-MIB", "boxServicesPowerSuppUnitIndex"), (0, "EdgeSwitch-BOXSERVICES-PRIVATE-MIB", "boxServicesPowSupplyIndex"))
if mibBuilder.loadTexts: boxServicesPowSuppliesEntry.setStatus('current')
if mibBuilder.loadTexts: boxServicesPowSuppliesEntry.setDescription('Box Services Power Supply Entry')
boxServicesPowerSuppUnitIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 43, 1, 7, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: boxServicesPowerSuppUnitIndex.setStatus('current')
if mibBuilder.loadTexts: boxServicesPowerSuppUnitIndex.setDescription('Unit index for an entry in the Box Services Power Supply Table')
boxServicesPowSupplyIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 43, 1, 7, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: boxServicesPowSupplyIndex.setStatus('current')
if mibBuilder.loadTexts: boxServicesPowSupplyIndex.setDescription('Unique index of power supply table entry')
boxServicesPowSupplyItemType = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 43, 1, 7, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("fixed", 1), ("removable", 2), ("fixedAC", 3), ("removableDC", 4), ("fixedDC", 5), ("removableAC", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: boxServicesPowSupplyItemType.setStatus('current')
if mibBuilder.loadTexts: boxServicesPowSupplyItemType.setDescription('The type of power supply')
boxServicesPowSupplyItemState = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 43, 1, 7, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("notpresent", 1), ("operational", 2), ("failed", 3), ("powering", 4), ("nopower", 5), ("notpowering", 6), ("incompatible", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: boxServicesPowSupplyItemState.setStatus('current')
if mibBuilder.loadTexts: boxServicesPowSupplyItemState.setDescription('The status of power supply. nopower(5) - This state means the power supply is present but no AC is connected.\n                                                  incompatible(7) - This state is possible on boards capable of pluggable Power supplies')
boxServicesTempSensorsTable = MibTable((1, 3, 6, 1, 4, 1, 4413, 1, 1, 43, 1, 8), )
if mibBuilder.loadTexts: boxServicesTempSensorsTable.setStatus('current')
if mibBuilder.loadTexts: boxServicesTempSensorsTable.setDescription('Temperature sensor')
boxServicesTempSensorsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4413, 1, 1, 43, 1, 8, 1), ).setIndexNames((0, "EdgeSwitch-BOXSERVICES-PRIVATE-MIB", "boxServicesUnitIndex"), (0, "EdgeSwitch-BOXSERVICES-PRIVATE-MIB", "boxServicesTempSensorIndex"))
if mibBuilder.loadTexts: boxServicesTempSensorsEntry.setStatus('current')
if mibBuilder.loadTexts: boxServicesTempSensorsEntry.setDescription('Box Services Temperature Sensor Entry')
boxServicesUnitIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 43, 1, 8, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: boxServicesUnitIndex.setStatus('current')
if mibBuilder.loadTexts: boxServicesUnitIndex.setDescription('Unit index for an entry in the Box Services Temperature Sensor Table')
boxServicesTempSensorIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 43, 1, 8, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: boxServicesTempSensorIndex.setStatus('current')
if mibBuilder.loadTexts: boxServicesTempSensorIndex.setDescription('Unique index of temperature sensor table entry')
boxServicesTempSensorType = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 43, 1, 8, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("fixed", 1), ("removable", 2), ("fixedAC", 3), ("removableDC", 4), ("fixedDC", 5), ("removableAC", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: boxServicesTempSensorType.setStatus('current')
if mibBuilder.loadTexts: boxServicesTempSensorType.setDescription('The type of temperature sensor')
boxServicesTempSensorState = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 43, 1, 8, 1, 4), BoxsTemperatureStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: boxServicesTempSensorState.setStatus('obsolete')
if mibBuilder.loadTexts: boxServicesTempSensorState.setDescription('The state of temperature sensor')
boxServicesTempSensorTemperature = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 43, 1, 8, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: boxServicesTempSensorTemperature.setStatus('current')
if mibBuilder.loadTexts: boxServicesTempSensorTemperature.setDescription('The temperature value reported by sensor')
boxServicesTempUnitTable = MibTable((1, 3, 6, 1, 4, 1, 4413, 1, 1, 43, 1, 15), )
if mibBuilder.loadTexts: boxServicesTempUnitTable.setStatus('current')
if mibBuilder.loadTexts: boxServicesTempUnitTable.setDescription('Temperature status table')
boxServicesTempUnitEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4413, 1, 1, 43, 1, 15, 1), ).setIndexNames((0, "EdgeSwitch-BOXSERVICES-PRIVATE-MIB", "boxServicesTempUnitIndex"))
if mibBuilder.loadTexts: boxServicesTempUnitEntry.setStatus('current')
if mibBuilder.loadTexts: boxServicesTempUnitEntry.setDescription('Box Services Temperature Unit Entry')
boxServicesTempUnitIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 43, 1, 15, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: boxServicesTempUnitIndex.setStatus('current')
if mibBuilder.loadTexts: boxServicesTempUnitIndex.setDescription('Unit index for an entry in the Box Services Temperature Unit Table')
boxServicesTempUnitState = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 43, 1, 15, 1, 2), BoxsTemperatureStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: boxServicesTempUnitState.setStatus('current')
if mibBuilder.loadTexts: boxServicesTempUnitState.setDescription('The temperature state of the unit')
boxServicesTempUnitTemperature = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 43, 1, 15, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: boxServicesTempUnitTemperature.setStatus('current')
if mibBuilder.loadTexts: boxServicesTempUnitTemperature.setDescription('The highest temperature currently reported by any sensor on the unit')
boxServicesNotificationsGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 1, 1, 43, 2))
boxsItemStateChangeEvent = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 43, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("insertion", 1), ("removal", 2), ("becomeoperational", 3), ("failure", 4), ("losepower", 5)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: boxsItemStateChangeEvent.setStatus('current')
if mibBuilder.loadTexts: boxsItemStateChangeEvent.setDescription('This event describes states of the fan or power supply.\n           \n             insertion          - hot-pluggable fan or power supply was inserted\n             removal            - hot-pluggable fan or power supply was removed\n             becomeoperational  - fan or power supply became operational after failure state\n             failure            - fan or power supply failure happened, i.e. it is not able to perform its functions\n             losepower          - a power supply was operational, but the power to it has been disconnected or has failed')
boxsTemperatureChangeEvent = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 43, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("abovethreshold", 1), ("belowthreshold", 2), ("withinnormalrange", 3)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: boxsTemperatureChangeEvent.setStatus('current')
if mibBuilder.loadTexts: boxsTemperatureChangeEvent.setDescription('This event describes change of the temperature. \n           To avoid flipping on boundary conditions, it is allowed to send the trap \n           taking into account some margin around thresholds.\n           \n             abovethreshold     - temperature increased and crossed upper threshold value\n             belowthreshold     - temperature decreased and crossed lower threshold value\n             withinnormalrange  - temperature returned to normal range (between threshold)')
boxsTemperatureStatusCurrentEvent = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 43, 2, 3), BoxsTemperatureStatus()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: boxsTemperatureStatusCurrentEvent.setStatus('current')
if mibBuilder.loadTexts: boxsTemperatureStatusCurrentEvent.setDescription('This event describes the current status of a switch.')
boxsTemperatureStatusPreviousEvent = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 43, 2, 4), BoxsTemperatureStatus()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: boxsTemperatureStatusPreviousEvent.setStatus('current')
if mibBuilder.loadTexts: boxsTemperatureStatusPreviousEvent.setDescription('This event describes the previous status of a switch.')
fastPathBoxServicesTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 1, 1, 43, 0))
boxsFanStateChange = NotificationType((1, 3, 6, 1, 4, 1, 4413, 1, 1, 43, 0, 1)).setObjects(("EdgeSwitch-BOXSERVICES-PRIVATE-MIB", "boxServicesFansIndex"), ("EdgeSwitch-BOXSERVICES-PRIVATE-MIB", "boxsItemStateChangeEvent"))
if mibBuilder.loadTexts: boxsFanStateChange.setStatus('current')
if mibBuilder.loadTexts: boxsFanStateChange.setDescription('Trap is sent when fan state change happens.')
boxsPowSupplyStateChange = NotificationType((1, 3, 6, 1, 4, 1, 4413, 1, 1, 43, 0, 2)).setObjects(("EdgeSwitch-BOXSERVICES-PRIVATE-MIB", "boxServicesPowSupplyIndex"), ("EdgeSwitch-BOXSERVICES-PRIVATE-MIB", "boxsItemStateChangeEvent"))
if mibBuilder.loadTexts: boxsPowSupplyStateChange.setStatus('current')
if mibBuilder.loadTexts: boxsPowSupplyStateChange.setDescription('Trap is sent when power supply state change happens.')
boxsTemperatureChange = NotificationType((1, 3, 6, 1, 4, 1, 4413, 1, 1, 43, 0, 3)).setObjects(("EdgeSwitch-BOXSERVICES-PRIVATE-MIB", "boxServicesTempSensorIndex"), ("EdgeSwitch-BOXSERVICES-PRIVATE-MIB", "boxsTemperatureChangeEvent"))
if mibBuilder.loadTexts: boxsTemperatureChange.setStatus('obsolete')
if mibBuilder.loadTexts: boxsTemperatureChange.setDescription('Trap is sent when temperature is changing and crossing any of the thresholds')
boxsThermalShutdown = NotificationType((1, 3, 6, 1, 4, 1, 4413, 1, 1, 43, 0, 4)).setObjects(("EdgeSwitch-BOXSERVICES-PRIVATE-MIB", "boxServicesThermalShutdownSensor"), ("EdgeSwitch-BOXSERVICES-PRIVATE-MIB", "boxServicesThermalShutdownTemperature"))
if mibBuilder.loadTexts: boxsThermalShutdown.setStatus('current')
if mibBuilder.loadTexts: boxsThermalShutdown.setDescription('Trap is sent when thermal shutdown is initiated.')
boxsTemperatureStateChange = NotificationType((1, 3, 6, 1, 4, 1, 4413, 1, 1, 43, 0, 5)).setObjects(("EdgeSwitch-BOXSERVICES-PRIVATE-MIB", "boxServicesTempUnitIndex"), ("EdgeSwitch-BOXSERVICES-PRIVATE-MIB", "boxsTemperatureStatusCurrentEvent"), ("EdgeSwitch-BOXSERVICES-PRIVATE-MIB", "boxsTemperatureStatusPreviousEvent"))
if mibBuilder.loadTexts: boxsTemperatureStateChange.setStatus('current')
if mibBuilder.loadTexts: boxsTemperatureStateChange.setDescription('Trap is sent when the system temperature crosses a threshold. \n            To avoid rapid flapping between states, a hysteresis may\n            be applied.')
boxsLocatorLedConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 1, 1, 43, 4))
boxsLocatorLedUnit = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 43, 4, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: boxsLocatorLedUnit.setStatus('current')
if mibBuilder.loadTexts: boxsLocatorLedUnit.setDescription("Spesifies unit number where Locator LED should blink on.\n                      This is write-only value. It always returns '0' on request\n                      if the Locator Led feature is supported.")
boxsLocatorLedTime = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 43, 4, 2), Integer32().clone(20)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: boxsLocatorLedTime.setStatus('current')
if mibBuilder.loadTexts: boxsLocatorLedTime.setDescription("Indicates time period in seconds for Locator LED blinking.\n                      The range is from 20 to 3600 seconds.\n                      The dafault value is 20 seconds.\n                      This is write-only value. It always returns '0' on request\n                      if the Locator Led feature is supported.")
boxsLocatorLedEnable = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 43, 4, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: boxsLocatorLedEnable.setStatus('current')
if mibBuilder.loadTexts: boxsLocatorLedEnable.setDescription("Starts the Locator LED blinking.\n                      If boxsLocatorLedUnit has not been set current(manager) unit number will be used.\n                      If boxsLocatorLedTime has not been set default value(20 seconds) will be used.\n                      This is write-only value. It always returns '0' on request\n                      if the Locator Led feature is supported.")
mibBuilder.exportSymbols("EdgeSwitch-BOXSERVICES-PRIVATE-MIB", boxServicesPowSuppliesTable=boxServicesPowSuppliesTable, boxsTemperatureStateChange=boxsTemperatureStateChange, fastPathBoxServices=fastPathBoxServices, boxServicesFanStateTrapEnable=boxServicesFanStateTrapEnable, boxServicesTemperatureTrapEnable=boxServicesTemperatureTrapEnable, boxsTemperatureChange=boxsTemperatureChange, boxServicesPowSupplyItemState=boxServicesPowSupplyItemState, boxServicesTempUnitIndex=boxServicesTempUnitIndex, boxServicesTempUnitTable=boxServicesTempUnitTable, boxsLocatorLedTime=boxsLocatorLedTime, boxsLocatorLedUnit=boxsLocatorLedUnit, boxServicesPowSupplyIndex=boxServicesPowSupplyIndex, boxServicesTempSensorsEntry=boxServicesTempSensorsEntry, boxServicesUnitIndex=boxServicesUnitIndex, boxServicesPSMStateTrapEnable=boxServicesPSMStateTrapEnable, boxServicesPowSuppliesEntry=boxServicesPowSuppliesEntry, boxsLocatorLedEnable=boxsLocatorLedEnable, boxServicesNormalTempRangeMin=boxServicesNormalTempRangeMin, boxServicesPowerSuppUnitIndex=boxServicesPowerSuppUnitIndex, boxServicesTempSensorTemperature=boxServicesTempSensorTemperature, boxServicesTempSensorsTable=boxServicesTempSensorsTable, boxsTemperatureStatusCurrentEvent=boxsTemperatureStatusCurrentEvent, boxServicesFansIndex=boxServicesFansIndex, boxServicesFanDutyLevel=boxServicesFanDutyLevel, boxsTemperatureStatusPreviousEvent=boxsTemperatureStatusPreviousEvent, boxsTemperatureChangeEvent=boxsTemperatureChangeEvent, PYSNMP_MODULE_ID=fastPathBoxServices, fastPathBoxServicesTraps=fastPathBoxServicesTraps, boxServicesFanItemType=boxServicesFanItemType, boxServicesTempUnitState=boxServicesTempUnitState, boxServicesFansTable=boxServicesFansTable, boxServicesGroup=boxServicesGroup, boxServicesPowSupplyItemType=boxServicesPowSupplyItemType, boxServicesTempSensorState=boxServicesTempSensorState, boxServicesFanItemState=boxServicesFanItemState, boxsPowSupplyStateChange=boxsPowSupplyStateChange, boxServicesFanUnitIndex=boxServicesFanUnitIndex, boxServicesTempSensorIndex=boxServicesTempSensorIndex, boxServicesFanSpeed=boxServicesFanSpeed, boxsThermalShutdown=boxsThermalShutdown, BoxsTemperatureStatus=BoxsTemperatureStatus, boxServicesNormalTempRangeMax=boxServicesNormalTempRangeMax, boxServicesTempUnitTemperature=boxServicesTempUnitTemperature, boxServicesTempUnitEntry=boxServicesTempUnitEntry, boxServicesThermalShutdownTemperature=boxServicesThermalShutdownTemperature, boxServicesTempSensorType=boxServicesTempSensorType, boxsFanStateChange=boxsFanStateChange, boxServicesNotificationsGroup=boxServicesNotificationsGroup, boxServicesFansEntry=boxServicesFansEntry, boxsLocatorLedConfigGroup=boxsLocatorLedConfigGroup, boxServicesThermalShutdownSensor=boxServicesThermalShutdownSensor, boxsItemStateChangeEvent=boxsItemStateChangeEvent)
