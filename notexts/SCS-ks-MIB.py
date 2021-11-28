#
# PySNMP MIB module SCS-ks-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/carel/SCS-ks-MIB
# Produced by pysmi-1.1.3 at Sun Nov 28 20:19:53 2021
# On host fv-az77-612 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
ifIndex, ifEntry = mibBuilder.importSymbols("IF-MIB", "ifIndex", "ifEntry")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
sysName, sysLocation, sysContact = mibBuilder.importSymbols("SNMPv2-MIB", "sysName", "sysLocation", "sysContact")
Gauge32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, enterprises, NotificationType, iso, Bits, Counter64, TimeTicks, MibIdentifier, Counter32, Integer32, ObjectIdentity, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "enterprises", "NotificationType", "iso", "Bits", "Counter64", "TimeTicks", "MibIdentifier", "Counter32", "Integer32", "ObjectIdentity", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
scs_ks = ModuleIdentity((1, 3, 6, 1, 4, 1, 9839, 1, 1)).setLabel("scs-ks")
scs_ks.setRevisions(('2020-11-05 18:05',))
if mibBuilder.loadTexts: scs_ks.setLastUpdated('202011051805Z')
if mibBuilder.loadTexts: scs_ks.setOrganization('None')
carel = MibIdentifier((1, 3, 6, 1, 4, 1, 9839))
systm = MibIdentifier((1, 3, 6, 1, 4, 1, 9839, 1))
scs = MibIdentifier((1, 3, 6, 1, 4, 1, 9839, 1, 2))
status_evaporator_fan = MibScalar((1, 3, 6, 1, 4, 1, 9839, 1, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("status-evaporator-fan").setUnits('N/A').setMaxAccess("readonly")
if mibBuilder.loadTexts: status_evaporator_fan.setStatus('current')
status_condenser_fan = MibScalar((1, 3, 6, 1, 4, 1, 9839, 1, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("status-condenser-fan").setUnits('N/A').setMaxAccess("readonly")
if mibBuilder.loadTexts: status_condenser_fan.setStatus('current')
status_compressor = MibScalar((1, 3, 6, 1, 4, 1, 9839, 1, 2, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("status-compressor").setUnits('N/A').setMaxAccess("readonly")
if mibBuilder.loadTexts: status_compressor.setStatus('current')
status_heater_thermal_protection = MibScalar((1, 3, 6, 1, 4, 1, 9839, 1, 2, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("status-heater-thermal-protection").setUnits('N/A').setMaxAccess("readonly")
if mibBuilder.loadTexts: status_heater_thermal_protection.setStatus('current')
status_exhaust_air_sensor = MibScalar((1, 3, 6, 1, 4, 1, 9839, 1, 2, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("status-exhaust-air-sensor").setUnits('N/A').setMaxAccess("readonly")
if mibBuilder.loadTexts: status_exhaust_air_sensor.setStatus('current')
status_supply_air_sensor = MibScalar((1, 3, 6, 1, 4, 1, 9839, 1, 2, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("status-supply-air-sensor").setUnits('N/A').setMaxAccess("readonly")
if mibBuilder.loadTexts: status_supply_air_sensor.setStatus('current')
status_outside_sensor = MibScalar((1, 3, 6, 1, 4, 1, 9839, 1, 2, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("status-outside-sensor").setUnits('N/A').setMaxAccess("readonly")
if mibBuilder.loadTexts: status_outside_sensor.setStatus('current')
status_room_temperature_sensor = MibScalar((1, 3, 6, 1, 4, 1, 9839, 1, 2, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("status-room-temperature-sensor").setUnits('N/A').setMaxAccess("readonly")
if mibBuilder.loadTexts: status_room_temperature_sensor.setStatus('current')
status_room_humidity_sensor = MibScalar((1, 3, 6, 1, 4, 1, 9839, 1, 2, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("status-room-humidity-sensor").setUnits('N/A').setMaxAccess("readonly")
if mibBuilder.loadTexts: status_room_humidity_sensor.setStatus('current')
status_min_exhaust_air_temperature = MibScalar((1, 3, 6, 1, 4, 1, 9839, 1, 2, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("status-min-exhaust-air-temperature").setUnits('N/A').setMaxAccess("readonly")
if mibBuilder.loadTexts: status_min_exhaust_air_temperature.setStatus('current')
status_max_exhaust_air_temperature = MibScalar((1, 3, 6, 1, 4, 1, 9839, 1, 2, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("status-max-exhaust-air-temperature").setUnits('N/A').setMaxAccess("readonly")
if mibBuilder.loadTexts: status_max_exhaust_air_temperature.setStatus('current')
status_min_supply_air_temperature = MibScalar((1, 3, 6, 1, 4, 1, 9839, 1, 2, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("status-min-supply-air-temperature").setUnits('N/A').setMaxAccess("readonly")
if mibBuilder.loadTexts: status_min_supply_air_temperature.setStatus('current')
status_water_sensor = MibScalar((1, 3, 6, 1, 4, 1, 9839, 1, 2, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("status-water-sensor").setUnits('N/A').setMaxAccess("readonly")
if mibBuilder.loadTexts: status_water_sensor.setStatus('current')
status_filter_monitoring = MibScalar((1, 3, 6, 1, 4, 1, 9839, 1, 2, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("status-filter-monitoring").setUnits('N/A').setMaxAccess("readonly")
if mibBuilder.loadTexts: status_filter_monitoring.setStatus('current')
exhaust_air_temperature = MibScalar((1, 3, 6, 1, 4, 1, 9839, 1, 2, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-999, 999))).setLabel("exhaust-air-temperature").setUnits('N/A').setMaxAccess("readonly")
if mibBuilder.loadTexts: exhaust_air_temperature.setStatus('current')
supply_air_temperature = MibScalar((1, 3, 6, 1, 4, 1, 9839, 1, 2, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-999, 999))).setLabel("supply-air-temperature").setUnits('N/A').setMaxAccess("readonly")
if mibBuilder.loadTexts: supply_air_temperature.setStatus('current')
outside_air_temperature = MibScalar((1, 3, 6, 1, 4, 1, 9839, 1, 2, 17), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-999, 999))).setLabel("outside-air-temperature").setUnits('N/A').setMaxAccess("readonly")
if mibBuilder.loadTexts: outside_air_temperature.setStatus('current')
room_temperature = MibScalar((1, 3, 6, 1, 4, 1, 9839, 1, 2, 18), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-999, 999))).setLabel("room-temperature").setUnits('N/A').setMaxAccess("readonly")
if mibBuilder.loadTexts: room_temperature.setStatus('current')
room_humidity = MibScalar((1, 3, 6, 1, 4, 1, 9839, 1, 2, 19), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-999, 999))).setLabel("room-humidity").setUnits('N/A').setMaxAccess("readonly")
if mibBuilder.loadTexts: room_humidity.setStatus('current')
status_operational_status = MibScalar((1, 3, 6, 1, 4, 1, 9839, 1, 2, 20), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("status-operational-status").setUnits('N/A').setMaxAccess("readonly")
if mibBuilder.loadTexts: status_operational_status.setStatus('current')
status_collective_fault = MibScalar((1, 3, 6, 1, 4, 1, 9839, 1, 2, 21), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("status-collective-fault").setUnits('N/A').setMaxAccess("readonly")
if mibBuilder.loadTexts: status_collective_fault.setStatus('current')
mibBuilder.exportSymbols("SCS-ks-MIB", exhaust_air_temperature=exhaust_air_temperature, carel=carel, PYSNMP_MODULE_ID=scs_ks, status_supply_air_sensor=status_supply_air_sensor, room_temperature=room_temperature, status_collective_fault=status_collective_fault, status_compressor=status_compressor, scs_ks=scs_ks, outside_air_temperature=outside_air_temperature, status_exhaust_air_sensor=status_exhaust_air_sensor, status_outside_sensor=status_outside_sensor, status_min_supply_air_temperature=status_min_supply_air_temperature, supply_air_temperature=supply_air_temperature, status_room_temperature_sensor=status_room_temperature_sensor, status_operational_status=status_operational_status, room_humidity=room_humidity, status_water_sensor=status_water_sensor, status_room_humidity_sensor=status_room_humidity_sensor, status_evaporator_fan=status_evaporator_fan, status_max_exhaust_air_temperature=status_max_exhaust_air_temperature, scs=scs, status_filter_monitoring=status_filter_monitoring, systm=systm, status_min_exhaust_air_temperature=status_min_exhaust_air_temperature, status_condenser_fan=status_condenser_fan, status_heater_thermal_protection=status_heater_thermal_protection)
