#
# PySNMP MIB module ALGPOWER-v2-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/algcom/ALGPOWER-v2
# Produced by pysmi-1.1.8 at Sun Jan 16 00:31:34 2022
# On host fv-az42-839 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, iso, ModuleIdentity, Integer32, ObjectIdentity, Gauge32, IpAddress, enterprises, Counter32, MibIdentifier, TimeTicks, Unsigned32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "iso", "ModuleIdentity", "Integer32", "ObjectIdentity", "Gauge32", "IpAddress", "enterprises", "Counter32", "MibIdentifier", "TimeTicks", "Unsigned32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
algcom = MibIdentifier((1, 3, 6, 1, 4, 1, 49136))
upsObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 49136, 1))
output = MibIdentifier((1, 3, 6, 1, 4, 1, 49136, 1, 1))
battery = MibIdentifier((1, 3, 6, 1, 4, 1, 49136, 1, 2))
input = MibIdentifier((1, 3, 6, 1, 4, 1, 49136, 1, 3))
temperature = MibIdentifier((1, 3, 6, 1, 4, 1, 49136, 1, 4))
watchdog = MibIdentifier((1, 3, 6, 1, 4, 1, 49136, 1, 5))
supply = MibIdentifier((1, 3, 6, 1, 4, 1, 49136, 1, 6))
installation = MibIdentifier((1, 3, 6, 1, 4, 1, 49136, 1, 7))
bat_tst = MibIdentifier((1, 3, 6, 1, 4, 1, 49136, 1, 8)).setLabel("bat-tst")
outputVoltage = MibScalar((1, 3, 6, 1, 4, 1, 49136, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: outputVoltage.setStatus('mandatory')
if mibBuilder.loadTexts: outputVoltage.setDescription('Numeric value of instantaneous output voltage from\n\t\t\tthe source in tenths of a volt. To get the value\n\t\t\tactual in volt should be divided by 10.\n\t\t\t\n\t\t\tExample:\n\t\t\tRead value 241, actual value 24.1V.')
outputCurrent = MibScalar((1, 3, 6, 1, 4, 1, 49136, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: outputCurrent.setStatus('mandatory')
if mibBuilder.loadTexts: outputCurrent.setDescription("Numeric value of current output of converter AC/DC.\n\t\t\tReal value reading in milli ampere.\n\t\t\t\n\t\t\tExample:\n\t\t\tRead value 1087, Actual value 1.087 milli ampere\n\t\t\tor 1.087A.\n\t\t\tIf the output is '0' the AC/DC is off and the output\n\t\t\tfor the equipments is provide from batteries")
oidNotUsed0 = MibScalar((1, 3, 6, 1, 4, 1, 49136, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oidNotUsed0.setStatus('mandatory')
if mibBuilder.loadTexts: oidNotUsed0.setDescription('OID not used.')
oidNotUsed1 = MibScalar((1, 3, 6, 1, 4, 1, 49136, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oidNotUsed1.setStatus('mandatory')
if mibBuilder.loadTexts: oidNotUsed1.setDescription('OID not used.')
batteryVoltage = MibScalar((1, 3, 6, 1, 4, 1, 49136, 1, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: batteryVoltage.setStatus('mandatory')
if mibBuilder.loadTexts: batteryVoltage.setDescription('Numeric value of instantaneous voltage of battery bank.\n\t\tTo get the actual value in volt must be divided by 10.\n\t\t\n\t\tExample:\n\t\tRead value 240, actual value 24.0V.')
batteryCurrent = MibScalar((1, 3, 6, 1, 4, 1, 49136, 1, 2, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: batteryCurrent.setStatus('mandatory')
if mibBuilder.loadTexts: batteryCurrent.setDescription('Numeric value of current in Battery bank. Real\n\t\t\tvalue reading in milli ampere.\n\t\t\tIf the value is negative the Battery bank is provide\n\t\t\tenergy for the output.\n\t\t\tIf the value is positive the Battery bank is under\n\t\t\tcharger \n\t\t\t\n\t\t\tExample:\n\t\t\tRead value -2230, Actual value 2,230 ampere and the\n\t\t\tbattery bank is provide this current.\n\t\t\tRead value 3000, Actual value 3.000 milli ampere and\n\t\t\tthe battery bank is absorve this current.')
chargerStatus = MibScalar((1, 3, 6, 1, 4, 1, 49136, 1, 2, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chargerStatus.setStatus('mandatory')
if mibBuilder.loadTexts: chargerStatus.setDescription('Show the status of battery charger:\n\t\t\t0 - The battery is not connected in DC UPS;\n\t\t\t1 - The battery is voltage incompatible with DC UPS;\n\t\t\t2 - The DC UPS is in nobreak mode;\n\t\t\t3 - The charger of Battery is in Bulk stage;\n\t\t\t4 - The charger of Battery is Absorption stage;\n\t\t\t5 - The charger of Battery is Float stage;\n\t\t\t6 - The Battery will be disconnected in 30s due to\n\t\t\t    low voltage and the DC-UPS output will be\n\t\t\t    turned off.\n\t\t\t7 - The Battery is under test')
alarmOnBattery = MibScalar((1, 3, 6, 1, 4, 1, 49136, 1, 3, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmOnBattery.setStatus('mandatory')
if mibBuilder.loadTexts: alarmOnBattery.setDescription('Shows the operation mode of DC-UPS:\n\n\t\t\t0 - The DC-UPS output is provide by AC energy.\n\t\t\t1 - The DC-UPS output is provide by Battery')
acFail = MibScalar((1, 3, 6, 1, 4, 1, 49136, 1, 3, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acFail.setStatus('mandatory')
if mibBuilder.loadTexts: acFail.setDescription('Alarm that alert about AC outages in the last 10\n\t\t\tminutes:\n\t\t\t\n\t\t\t0 - DC-UPS in normal operation.\n\t\t\t1 - Occur a AC fail in the last 10 minutes.')
batteryCharging = MibScalar((1, 3, 6, 1, 4, 1, 49136, 1, 3, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: batteryCharging.setStatus('mandatory')
if mibBuilder.loadTexts: batteryCharging.setDescription('Show the status of charging Battery:\n\t\t\t\n\t\t\t1 - The battery is on charging.\n\t\t\t0 - The battery is on discharging.')
batteryDischarging = MibScalar((1, 3, 6, 1, 4, 1, 49136, 1, 3, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: batteryDischarging.setStatus('mandatory')
if mibBuilder.loadTexts: batteryDischarging.setDescription('Show the status of discharging Battery:\n\t\t\t\n\t\t\t1 - The battery is on discharging.\n\t\t\t0 - The battery is on charging.')
overheat = MibScalar((1, 3, 6, 1, 4, 1, 49136, 1, 3, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: overheat.setStatus('mandatory')
if mibBuilder.loadTexts: overheat.setDescription('Alarm that alert about overtemperature of DC-UPS\n\t\t\t\n\t\t\t1 - The DC-UPS is in condition of overtemperature.\n\t\t\t0 - The DC-UPS is in normal condition.')
overload = MibScalar((1, 3, 6, 1, 4, 1, 49136, 1, 3, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: overload.setStatus('mandatory')
if mibBuilder.loadTexts: overload.setDescription('Alarm that alert about overload of DC-UPS\n\t\t\t\n\t\t\t1 - The DC-UPS is in condition of overload.\n\t\t\t0 - The DC-UPS is in normal condition.')
fanAfail = MibScalar((1, 3, 6, 1, 4, 1, 49136, 1, 3, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fanAfail.setStatus('mandatory')
if mibBuilder.loadTexts: fanAfail.setDescription('Alarm that alert about fail in internal FAN A\n\t\t\t\n\t\t\t1 - Internal FAN with fail.\n\t\t\t0 - Internal FAN ok')
fanBfail = MibScalar((1, 3, 6, 1, 4, 1, 49136, 1, 3, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fanBfail.setStatus('mandatory')
if mibBuilder.loadTexts: fanBfail.setDescription('Alarm that alert about fail in internal FAN B\n\t\t\t\n\t\t\t1 - Internal FAN with fail.\n\t\t\t0 - Internal FAN ok')
oidNotUsed2 = MibScalar((1, 3, 6, 1, 4, 1, 49136, 1, 3, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oidNotUsed2.setStatus('mandatory')
if mibBuilder.loadTexts: oidNotUsed2.setDescription('OID not used.')
oidNotUsed3 = MibScalar((1, 3, 6, 1, 4, 1, 49136, 1, 3, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oidNotUsed3.setStatus('mandatory')
if mibBuilder.loadTexts: oidNotUsed3.setDescription('OID not used.')
upTime = MibScalar((1, 3, 6, 1, 4, 1, 49136, 1, 3, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: upTime.setStatus('mandatory')
if mibBuilder.loadTexts: upTime.setDescription('System Up time in hours')
innerTemperature = MibScalar((1, 3, 6, 1, 4, 1, 49136, 1, 4, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: innerTemperature.setStatus('mandatory')
if mibBuilder.loadTexts: innerTemperature.setDescription('Show the internal temperature of power supply.\n\t\t\tUses the unit degree Celsius.\n\t\t\t\n\t\t\tExample\n\t\t\tRead value: 25, temperature is 25degC.')
outerTemperature = MibScalar((1, 3, 6, 1, 4, 1, 49136, 1, 4, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: outerTemperature.setStatus('mandatory')
if mibBuilder.loadTexts: outerTemperature.setDescription('Show the temperature of external sensor (cable that\n\t\t\tcomes with power supply).\n\t\t\tUses the unit degree Celsius.\n\t\t\t\n\t\t\tExample\n\t\t\tRead value: 25, temperature is 25degC.')
heatSinkTemperature = MibScalar((1, 3, 6, 1, 4, 1, 49136, 1, 4, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: heatSinkTemperature.setStatus('mandatory')
if mibBuilder.loadTexts: heatSinkTemperature.setDescription('Show the temperature of sensor in the heatsink of\n\t\t\tpower supply use the unit degree Celsius.\n\t\t\t\n\t\t\tExample\n\t\t\tRead value: 25, temperature is 25degC.')
watchdogPing1 = MibScalar((1, 3, 6, 1, 4, 1, 49136, 1, 5, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: watchdogPing1.setStatus('mandatory')
if mibBuilder.loadTexts: watchdogPing1.setDescription('Alarm indicating the action of watchdog 1\n\t\t\tprogrammed in the last 10 minutes. The watchdog\n\t\t\tacts on the output by turning it off when not\n\t\t\treceive response from IP ping command\n\t\t\tconfigured.\n\t\t\t\n\t\t\t1 - The watchdog 1 acted on the output the last 10\n\t\t\t    minutes.\n\t\t\t0 - The Watchdog 1 has not acted in the last 10\n\t\t\t    minutes.')
watchdogPing2 = MibScalar((1, 3, 6, 1, 4, 1, 49136, 1, 5, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: watchdogPing2.setStatus('mandatory')
if mibBuilder.loadTexts: watchdogPing2.setDescription('Alarm indicating the action of watchdog 2\n\t\t\tprogrammed in the last 10 minutes. The watchdog\n\t\t\tacts on the output by turning it off when not\n\t\t\treceive response from IP ping command\n\t\t\tconfigured.\n\t\t\t\n\t\t\t1 - The watchdog 2 acted on the output the last 10\n\t\t\t    minutes.\n\t\t\t0 - The Watchdog 2 has not acted in the last 10\n\t\t\t    minutes.')
watchdogPing3 = MibScalar((1, 3, 6, 1, 4, 1, 49136, 1, 5, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: watchdogPing3.setStatus('mandatory')
if mibBuilder.loadTexts: watchdogPing3.setDescription('Alarm indicating the action of watchdog 3\n\t\t\tprogrammed in the last 10 minutes. The watchdog\n\t\t\tacts on the output by turning it off when not\n\t\t\treceive response from IP ping command\n\t\t\tconfigured.\n\t\t\t\n\t\t\t1 - The watchdog 3 acted on the output the last 10\n\t\t\t    minutes.\n\t\t\t0 - The Watchdog 3 has not acted in the last 10\n\t\t\t    minutes.')
watchdogPing4 = MibScalar((1, 3, 6, 1, 4, 1, 49136, 1, 5, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: watchdogPing4.setStatus('mandatory')
if mibBuilder.loadTexts: watchdogPing4.setDescription('Alarm indicating the action of watchdog 4\n\t\t\tprogrammed in the last 10 minutes. The watchdog\n\t\t\tacts on the output by turning it off when not\n\t\t\treceive response from IP ping command\n\t\t\tconfigured.\n\t\t\t\n\t\t\t1 - The watchdog 4 acted on the output the last 10\n\t\t\t    minutes.\n\t\t\t0 - The Watchdog 4 has not acted in the last 10\n\t\t\t    minutes.')
watchdogPing5 = MibScalar((1, 3, 6, 1, 4, 1, 49136, 1, 5, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: watchdogPing5.setStatus('mandatory')
if mibBuilder.loadTexts: watchdogPing5.setDescription('Alarm indicating the action of watchdog 5\n\t\t\tprogrammed in the last 10 minutes. The watchdog\n\t\t\tacts on the output by turning it off when not\n\t\t\treceive response from IP ping command\n\t\t\tconfigured.\n\t\t\t\n\t\t\t1 - The watchdog 5 acted on the output the last 10\n\t\t\t    minutes.\n\t\t\t0 - The Watchdog 5 has not acted in the last 10\n\t\t\t    minutes.')
watchdogPing6 = MibScalar((1, 3, 6, 1, 4, 1, 49136, 1, 5, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: watchdogPing6.setStatus('mandatory')
if mibBuilder.loadTexts: watchdogPing6.setDescription('Alarm indicating the action of watchdog 6\n\t\t\tprogrammed in the last 10 minutes. The watchdog\n\t\t\tacts on the output by turning it off when not\n\t\t\treceive response from IP ping command\n\t\t\tconfigured.\n\t\t\t\n\t\t\t1 - The watchdog 6 acted on the output the last 10\n\t\t\t    minutes.\n\t\t\t0 - The Watchdog 6 has not acted in the last 10\n\t\t\t    minutes.')
watchdogPing7 = MibScalar((1, 3, 6, 1, 4, 1, 49136, 1, 5, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: watchdogPing7.setStatus('mandatory')
if mibBuilder.loadTexts: watchdogPing7.setDescription('Alarm indicating the action of watchdog 7\n\t\t\tprogrammed in the last 10 minutes. The watchdog\n\t\t\tacts on the output by turning it off when not\n\t\t\treceive response from IP ping command\n\t\t\tconfigured.\n\t\t\t\n\t\t\t1 - The watchdog 7 acted on the output the last 10\n\t\t\t    minutes.\n\t\t\t0 - The Watchdog 7 has not acted in the last 10\n\t\t\t    minutes.')
watchdogPing8 = MibScalar((1, 3, 6, 1, 4, 1, 49136, 1, 5, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: watchdogPing8.setStatus('mandatory')
if mibBuilder.loadTexts: watchdogPing8.setDescription('Alarm indicating the action of watchdog 8\n\t\t\tprogrammed in the last 10 minutes. The watchdog\n\t\t\tacts on the output by turning it off when not\n\t\t\treceive response from IP ping command\n\t\t\tconfigured.\n\t\t\t\n\t\t\t1 - The watchdog 8 acted on the output the last 10\n\t\t\t    minutes.\n\t\t\t0 - The Watchdog 8 has not acted in the last 10\n\t\t\t    minutes.')
watchdogPing9 = MibScalar((1, 3, 6, 1, 4, 1, 49136, 1, 5, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: watchdogPing9.setStatus('mandatory')
if mibBuilder.loadTexts: watchdogPing9.setDescription('Alarm indicating the action of watchdog 9\n\t\t\tprogrammed in the last 10 minutes. The watchdog\n\t\t\tacts on the output by turning it off when not\n\t\t\treceive response from IP ping command\n\t\t\tconfigured.\n\t\t\t\n\t\t\t1 - The watchdog 9 acted on the output the last 10\n\t\t\t    minutes.\n\t\t\t0 - The Watchdog 9 has not acted in the last 10\n\t\t\t    minutes.')
watchdogPing10 = MibScalar((1, 3, 6, 1, 4, 1, 49136, 1, 5, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: watchdogPing10.setStatus('mandatory')
if mibBuilder.loadTexts: watchdogPing10.setDescription('Alarm indicating the action of watchdog 10\n\t\t\tprogrammed in the last 10 minutes. The watchdog\n\t\t\tacts on the output by turning it off when not\n\t\t\treceive response from IP ping command\n\t\t\tconfigured.\n\t\t\t\n\t\t\t1 - The watchdog 10 acted on the output the last 10\n\t\t\t    minutes.\n\t\t\t0 - The Watchdog 10 has not acted in the last 10\n\t\t\t    minutes.')
supplyVoltage = MibScalar((1, 3, 6, 1, 4, 1, 49136, 1, 6, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: supplyVoltage.setStatus('mandatory')
if mibBuilder.loadTexts: supplyVoltage.setDescription('The supply AC voltage decivolt [dV]\n\t\t\tNumeric value of instantaneous input voltage.\n\t\t\tAn optional sensor is required to read this value.\n\t\t\tTo get the actual value in volt it should be\n\t\t\tdivided by 10.\n\t\t\t\n\t\t\tExample:\n\t\t\tRead value 2410, actual value 241 Vac.')
popName = MibScalar((1, 3, 6, 1, 4, 1, 49136, 1, 7, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(30, 30)).setFixedLength(30)).setMaxAccess("readonly")
if mibBuilder.loadTexts: popName.setStatus('mandatory')
if mibBuilder.loadTexts: popName.setDescription('PoP name')
facilityAddr = MibScalar((1, 3, 6, 1, 4, 1, 49136, 1, 7, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(40, 40)).setFixedLength(40)).setMaxAccess("readonly")
if mibBuilder.loadTexts: facilityAddr.setStatus('mandatory')
if mibBuilder.loadTexts: facilityAddr.setDescription('Facility address')
facilityCity = MibScalar((1, 3, 6, 1, 4, 1, 49136, 1, 7, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(30, 30)).setFixedLength(30)).setMaxAccess("readonly")
if mibBuilder.loadTexts: facilityCity.setStatus('mandatory')
if mibBuilder.loadTexts: facilityCity.setDescription('Facility city')
instDate = MibScalar((1, 3, 6, 1, 4, 1, 49136, 1, 7, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(10, 10)).setFixedLength(10)).setMaxAccess("readonly")
if mibBuilder.loadTexts: instDate.setStatus('mandatory')
if mibBuilder.loadTexts: instDate.setDescription('Installation date')
batCapacity = MibScalar((1, 3, 6, 1, 4, 1, 49136, 1, 7, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: batCapacity.setStatus('mandatory')
if mibBuilder.loadTexts: batCapacity.setDescription('Battery capacity')
batBrand = MibScalar((1, 3, 6, 1, 4, 1, 49136, 1, 7, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(30, 30)).setFixedLength(30)).setMaxAccess("readonly")
if mibBuilder.loadTexts: batBrand.setStatus('mandatory')
if mibBuilder.loadTexts: batBrand.setDescription('Battery brand')
batInstDate = MibScalar((1, 3, 6, 1, 4, 1, 49136, 1, 7, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(10, 10)).setFixedLength(10)).setMaxAccess("readonly")
if mibBuilder.loadTexts: batInstDate.setStatus('mandatory')
if mibBuilder.loadTexts: batInstDate.setDescription('Battery installation date')
respPers = MibScalar((1, 3, 6, 1, 4, 1, 49136, 1, 7, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(50, 50)).setFixedLength(50)).setMaxAccess("readonly")
if mibBuilder.loadTexts: respPers.setStatus('mandatory')
if mibBuilder.loadTexts: respPers.setDescription('Responsible person')
btst_date = MibScalar((1, 3, 6, 1, 4, 1, 49136, 1, 8, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(10, 10)).setFixedLength(10)).setLabel("btst-date").setMaxAccess("readonly")
if mibBuilder.loadTexts: btst_date.setStatus('mandatory')
if mibBuilder.loadTexts: btst_date.setDescription('Battery test execution date (dd/mm/yyyy)')
btst_status = MibScalar((1, 3, 6, 1, 4, 1, 49136, 1, 8, 2), Integer32()).setLabel("btst-status").setMaxAccess("readonly")
if mibBuilder.loadTexts: btst_status.setStatus('mandatory')
if mibBuilder.loadTexts: btst_status.setDescription('Battery test status\n\t\t0 - NEVER DONE\n\t\t1 - Passed\n\t\t2 - Running\n\t\t3 - Aborted\n\t\t4 - Failed')
btst_duration = MibScalar((1, 3, 6, 1, 4, 1, 49136, 1, 8, 3), Integer32()).setLabel("btst-duration").setMaxAccess("readonly")
if mibBuilder.loadTexts: btst_duration.setStatus('mandatory')
if mibBuilder.loadTexts: btst_duration.setDescription('Programmed test duration in minutes\n\t\t * 999 - Perform the test until battery is fully discharged')
btst_elapsed = MibScalar((1, 3, 6, 1, 4, 1, 49136, 1, 8, 4), Integer32()).setLabel("btst-elapsed").setMaxAccess("readonly")
if mibBuilder.loadTexts: btst_elapsed.setStatus('mandatory')
if mibBuilder.loadTexts: btst_elapsed.setDescription('Elapsed time in current\\last battery test')
btst_volt_i = MibScalar((1, 3, 6, 1, 4, 1, 49136, 1, 8, 5), Integer32()).setLabel("btst-volt-i").setMaxAccess("readonly")
if mibBuilder.loadTexts: btst_volt_i.setStatus('mandatory')
if mibBuilder.loadTexts: btst_volt_i.setDescription('The battery initial voltage [dV]\n\t\t\tNumeric value of battery voltage when starting the battery test.\n\t\t\t\t\t\t\n\t\t\tExample:\n\t\t\tRead value 241, actual value 24.1 V.')
btst_amp_i = MibScalar((1, 3, 6, 1, 4, 1, 49136, 1, 8, 6), Integer32()).setLabel("btst-amp-i").setMaxAccess("readonly")
if mibBuilder.loadTexts: btst_amp_i.setStatus('mandatory')
if mibBuilder.loadTexts: btst_amp_i.setDescription('The battery initial cuurent [mA]\n\t\t\tNumeric value of battery current when starting the battery test.\n\t\t\t\t\t\t\n\t\t\tExample:\n\t\t\tRead value 1522, actual value 1.55 A.')
btst_volt_f = MibScalar((1, 3, 6, 1, 4, 1, 49136, 1, 8, 7), Integer32()).setLabel("btst-volt-f").setMaxAccess("readonly")
if mibBuilder.loadTexts: btst_volt_f.setStatus('mandatory')
if mibBuilder.loadTexts: btst_volt_f.setDescription('The battery final voltage [dV]\n\t\t\tNumeric value of battery voltage when the battery test is done.\n\t\t\t\t\t\t\n\t\t\tExample:\n\t\t\tRead value 225, actual value 22.5 V.')
btst_amp_f = MibScalar((1, 3, 6, 1, 4, 1, 49136, 1, 8, 8), Integer32()).setLabel("btst-amp-f").setMaxAccess("readonly")
if mibBuilder.loadTexts: btst_amp_f.setStatus('mandatory')
if mibBuilder.loadTexts: btst_amp_f.setDescription('The battery initial cuurent [mA]\n\t\t\tNumeric value of battery current when the battery test is done.\n\t\t\t\t\t\t\n\t\t\tExample:\n\t\t\tRead value 1485, actual value 1.48 A.')
mibBuilder.exportSymbols("ALGPOWER-v2-MIB", acFail=acFail, watchdogPing1=watchdogPing1, facilityCity=facilityCity, chargerStatus=chargerStatus, batteryVoltage=batteryVoltage, oidNotUsed0=oidNotUsed0, oidNotUsed3=oidNotUsed3, bat_tst=bat_tst, outputCurrent=outputCurrent, oidNotUsed1=oidNotUsed1, installation=installation, overload=overload, fanBfail=fanBfail, btst_volt_i=btst_volt_i, btst_date=btst_date, btst_duration=btst_duration, watchdogPing9=watchdogPing9, batInstDate=batInstDate, btst_amp_i=btst_amp_i, watchdogPing8=watchdogPing8, algcom=algcom, fanAfail=fanAfail, respPers=respPers, batteryCharging=batteryCharging, alarmOnBattery=alarmOnBattery, batCapacity=batCapacity, outerTemperature=outerTemperature, watchdogPing3=watchdogPing3, overheat=overheat, upsObjects=upsObjects, oidNotUsed2=oidNotUsed2, watchdogPing2=watchdogPing2, supplyVoltage=supplyVoltage, popName=popName, upTime=upTime, watchdogPing4=watchdogPing4, watchdogPing5=watchdogPing5, batteryDischarging=batteryDischarging, watchdogPing6=watchdogPing6, batBrand=batBrand, facilityAddr=facilityAddr, watchdogPing10=watchdogPing10, outputVoltage=outputVoltage, watchdog=watchdog, output=output, batteryCurrent=batteryCurrent, battery=battery, btst_volt_f=btst_volt_f, btst_amp_f=btst_amp_f, watchdogPing7=watchdogPing7, innerTemperature=innerTemperature, btst_elapsed=btst_elapsed, supply=supply, temperature=temperature, heatSinkTemperature=heatSinkTemperature, input=input, instDate=instDate, btst_status=btst_status)
