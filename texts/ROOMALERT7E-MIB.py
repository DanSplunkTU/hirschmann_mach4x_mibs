#
# PySNMP MIB module ROOMALERT7E-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/avtech/ROOMALERT7E-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 17:52:35 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, ObjectIdentity, Gauge32, NotificationType, Counter32, Counter64, Integer32, ModuleIdentity, MibIdentifier, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, IpAddress, Bits, enterprises, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "ObjectIdentity", "Gauge32", "NotificationType", "Counter32", "Counter64", "Integer32", "ModuleIdentity", "MibIdentifier", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "IpAddress", "Bits", "enterprises", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
avtech = MibIdentifier((1, 3, 6, 1, 4, 1, 20916))
products = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1))
roomalert7e = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 2))
sensors = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 2, 1))
traps = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 2, 2))
thresholds = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 2, 3))
temperature = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 2, 1, 1))
switch = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 2, 1, 2))
tempreading1c = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tempreading1c.setStatus('mandatory')
if mibBuilder.loadTexts: tempreading1c.setDescription('Temperature Sensor 1 (Celsius)')
tempreading2c = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tempreading2c.setStatus('mandatory')
if mibBuilder.loadTexts: tempreading2c.setDescription('Temperature Sensor 2 (Celsius)')
tempreading3c = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tempreading3c.setStatus('mandatory')
if mibBuilder.loadTexts: tempreading3c.setDescription('Temperature Sensor 3 (Celsius)')
tempreading4c = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tempreading4c.setStatus('mandatory')
if mibBuilder.loadTexts: tempreading4c.setDescription('Temperature Sensor 4 (Celsius)')
tempreading1f = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tempreading1f.setStatus('mandatory')
if mibBuilder.loadTexts: tempreading1f.setDescription('Temperature Sensor 1 (Fahrenheit)')
tempreading2f = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tempreading2f.setStatus('mandatory')
if mibBuilder.loadTexts: tempreading2f.setDescription('Temperature Sensor 2 (Fahrenheit)')
tempreading3f = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 2, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tempreading3f.setStatus('mandatory')
if mibBuilder.loadTexts: tempreading3f.setDescription('Temperature Sensor 3 (Fahrenheit)')
tempreading4f = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 2, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tempreading4f.setStatus('mandatory')
if mibBuilder.loadTexts: tempreading4f.setDescription('Temperature Sensor 4 (Fahrenheit)')
switch1 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 2, 1, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: switch1.setStatus('mandatory')
if mibBuilder.loadTexts: switch1.setDescription('Switch Sensor 1 (0 = OFF, 1 = ON)')
switch2 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 2, 1, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: switch2.setStatus('mandatory')
if mibBuilder.loadTexts: switch2.setDescription('Switch Sensor 2 (0 = OFF, 1 = ON)')
switch3 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 2, 1, 2, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: switch3.setStatus('mandatory')
if mibBuilder.loadTexts: switch3.setDescription('Switch Sensor 3 (0 = OFF, 1 = ON)')
alarmtemp1 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 2, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmtemp1.setStatus('mandatory')
if mibBuilder.loadTexts: alarmtemp1.setDescription('Alarm for temperature 1\n\t\t\t0 = temperature OK\n\t\t\t1 = temperature too high\n\t\t\t2 = temperature too low')
alarmtemp2 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 2, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmtemp2.setStatus('mandatory')
if mibBuilder.loadTexts: alarmtemp2.setDescription('Alarm for temperature 2\n\t\t\t0 = temperature OK\n\t\t\t1 = temperature too high\n\t\t\t2 = temperature too low')
alarmtemp3 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 2, 2, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmtemp3.setStatus('mandatory')
if mibBuilder.loadTexts: alarmtemp3.setDescription('Alarm for temperature 3\n\t\t\t0 = temperature OK\n\t\t\t1 = temperature too high\n\t\t\t2 = temperature too low')
alarmtemp4 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 2, 2, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmtemp4.setStatus('mandatory')
if mibBuilder.loadTexts: alarmtemp4.setDescription('Alarm for temperature 4\n\t\t\t0 = temperature OK\n\t\t\t1 = temperature too high\n\t\t\t2 = temperature too low')
alarmswitch1 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 2, 2, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmswitch1.setStatus('mandatory')
if mibBuilder.loadTexts: alarmswitch1.setDescription('Alarm for switch sensor 1\n\t\t\t0 = Switch Open\n\t\t\t1 = Switch Closed')
alarmswitch2 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 2, 2, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmswitch2.setStatus('mandatory')
if mibBuilder.loadTexts: alarmswitch2.setDescription('Alarm for switch sensor 2\n\t\t\t0 = Switch Open\n\t\t\t1 = Switch Closed')
alarmswitch3 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 2, 2, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmswitch3.setStatus('mandatory')
if mibBuilder.loadTexts: alarmswitch3.setDescription('Alarm for switch sensor 3\n\t\t\t0 = Switch Open\n\t\t\t1 = Switch Closed')
alarmmessage = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 2, 2, 8), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alarmmessage.setStatus('mandatory')
if mibBuilder.loadTexts: alarmmessage.setDescription('Message string to send with trap messages')
upperlimit1 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 2, 3, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: upperlimit1.setStatus('mandatory')
if mibBuilder.loadTexts: upperlimit1.setDescription('High temperature threshold for temperature sensor 1')
lowerlimit1 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 2, 3, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lowerlimit1.setStatus('mandatory')
if mibBuilder.loadTexts: lowerlimit1.setDescription('Low temperature threshold for temperature sensor 1')
upperlimit2 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 2, 3, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: upperlimit2.setStatus('mandatory')
if mibBuilder.loadTexts: upperlimit2.setDescription('High temperature threshold for temperature sensor 2')
lowerlimit2 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 2, 3, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lowerlimit2.setStatus('mandatory')
if mibBuilder.loadTexts: lowerlimit2.setDescription('Low temperature threshold for temperature sensor 2')
upperlimit3 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 2, 3, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: upperlimit3.setStatus('mandatory')
if mibBuilder.loadTexts: upperlimit3.setDescription('High temperature threshold for temperature sensor 3')
lowerlimit3 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 2, 3, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lowerlimit3.setStatus('mandatory')
if mibBuilder.loadTexts: lowerlimit3.setDescription('Low temperature threshold for temperature sensor 3')
upperlimit4 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 2, 3, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: upperlimit4.setStatus('mandatory')
if mibBuilder.loadTexts: upperlimit4.setDescription('High temperature threshold for temperature sensor 4')
lowerlimit4 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 2, 3, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lowerlimit4.setStatus('mandatory')
if mibBuilder.loadTexts: lowerlimit4.setDescription('Low temperature threshold for temperature sensor 4')
alarmstart1_7e = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 2) + (0,1)).setLabel("alarmstart1-7e").setObjects(("ROOMALERT7E-MIB", "alarmmessage"), ("ROOMALERT7E-MIB", "tempreading1c"), ("ROOMALERT7E-MIB", "tempreading1f"))
if mibBuilder.loadTexts: alarmstart1_7e.setDescription('A alarmstart1 trap signifies that the current\n\t\t\ttemperature on sensor 1 is outside the \n\t\t\tdefined high or low threshold.')
room_alert_7e_snmp_trap = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 2) + (0,2)).setLabel("room-alert-7e-snmp-trap").setObjects(("ROOMALERT7E-MIB", "alarmmessage"))
if mibBuilder.loadTexts: room_alert_7e_snmp_trap.setDescription('A room-alert-7e-snmp-trap indicates that an alarm\n\t\t\tcondition has occurred on the sensor inidcated\n\t\t\tby the alarmmessage variable.')
alarmstart2_7e = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 2) + (0,3)).setLabel("alarmstart2-7e").setObjects(("ROOMALERT7E-MIB", "alarmmessage"), ("ROOMALERT7E-MIB", "tempreading2c"), ("ROOMALERT7E-MIB", "tempreading2f"))
if mibBuilder.loadTexts: alarmstart2_7e.setDescription('A alarmstart2 trap signifies that the current\n\t\t\ttemperature on sensor 2 is outside the \n\t\t\tdefined high or low threshold.')
alarmclear2_7e = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 2) + (0,4)).setLabel("alarmclear2-7e").setObjects(("ROOMALERT7E-MIB", "alarmmessage"), ("ROOMALERT7E-MIB", "tempreading2c"), ("ROOMALERT7E-MIB", "tempreading2f"))
if mibBuilder.loadTexts: alarmclear2_7e.setDescription('A alarmclear2 trap signifies that the current\n\t\t\ttemperature on sensor 2 has returned to a \n\t\t\tnormal condition and is within the defined \n\t\t\thigh or low threshold.')
alarmstart3_7e = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 2) + (0,5)).setLabel("alarmstart3-7e").setObjects(("ROOMALERT7E-MIB", "alarmmessage"), ("ROOMALERT7E-MIB", "tempreading3c"), ("ROOMALERT7E-MIB", "tempreading3f"))
if mibBuilder.loadTexts: alarmstart3_7e.setDescription('A alarmstart3 trap signifies that the current\n\t\t\ttemperature on sensor 3 is outside the \n\t\t\tdefined high or low threshold.')
alarmclear3_7e = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 2) + (0,6)).setLabel("alarmclear3-7e").setObjects(("ROOMALERT7E-MIB", "alarmmessage"), ("ROOMALERT7E-MIB", "tempreading3c"), ("ROOMALERT7E-MIB", "tempreading3f"))
if mibBuilder.loadTexts: alarmclear3_7e.setDescription('A alarmclear3 trap signifies that the current\n\t\t\ttemperature on sensor 3 has returned to a \n\t\t\tnormal condition and is within the defined \n\t\t\thigh or low threshold.')
alarmstart4_7e = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 2) + (0,7)).setLabel("alarmstart4-7e").setObjects(("ROOMALERT7E-MIB", "alarmmessage"), ("ROOMALERT7E-MIB", "tempreading4c"), ("ROOMALERT7E-MIB", "tempreading4f"))
if mibBuilder.loadTexts: alarmstart4_7e.setDescription('A alarmstart4 trap signifies that the current\n\t\t\ttemperature on sensor 4 is outside the \n\t\t\tdefined high or low threshold.')
alarmclear4_7e = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 2) + (0,8)).setLabel("alarmclear4-7e").setObjects(("ROOMALERT7E-MIB", "alarmmessage"), ("ROOMALERT7E-MIB", "tempreading4c"), ("ROOMALERT7E-MIB", "tempreading4f"))
if mibBuilder.loadTexts: alarmclear4_7e.setDescription('A alarmclear4 trap signifies that the current\n\t\t\ttemperature on sensor 4 has returned to a \n\t\t\tnormal condition and is within the defined \n\t\t\thigh or low threshold.')
alarmstart5_7e = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 2) + (0,9)).setLabel("alarmstart5-7e").setObjects(("ROOMALERT7E-MIB", "alarmmessage"), ("ROOMALERT7E-MIB", "switch1"), ("ROOMALERT7E-MIB", "switch1"))
if mibBuilder.loadTexts: alarmstart5_7e.setDescription('A alarmstart5 trap signifies that the current\n\t\t\tstatus of switch sensor 1 is outside the \n\t\t\tdefined threshold.')
alarmclear5_7e = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 2) + (0,10)).setLabel("alarmclear5-7e").setObjects(("ROOMALERT7E-MIB", "alarmmessage"), ("ROOMALERT7E-MIB", "switch1"), ("ROOMALERT7E-MIB", "switch1"))
if mibBuilder.loadTexts: alarmclear5_7e.setDescription('A alarmclear5 trap signifies that the current\n\t\t\tstatus of switch sensor 1 is outside the \n\t\t\tdefined threshold.')
alarmstart6_7e = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 2) + (0,11)).setLabel("alarmstart6-7e").setObjects(("ROOMALERT7E-MIB", "alarmmessage"), ("ROOMALERT7E-MIB", "switch2"), ("ROOMALERT7E-MIB", "switch2"))
if mibBuilder.loadTexts: alarmstart6_7e.setDescription('A alarmstart6 trap signifies that the current\n\t\t\tstatus of switch sensor 2 is outside the \n\t\t\tdefined threshold.')
alarmclear6_7e = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 2) + (0,12)).setLabel("alarmclear6-7e").setObjects(("ROOMALERT7E-MIB", "alarmmessage"), ("ROOMALERT7E-MIB", "switch2"), ("ROOMALERT7E-MIB", "switch2"))
if mibBuilder.loadTexts: alarmclear6_7e.setDescription('A alarmclear6 trap signifies that the current\n\t\t\tstatus of switch sensor 2 is outside the \n\t\t\tdefined threshold.')
alarmstart7_7e = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 2) + (0,13)).setLabel("alarmstart7-7e").setObjects(("ROOMALERT7E-MIB", "alarmmessage"), ("ROOMALERT7E-MIB", "switch3"), ("ROOMALERT7E-MIB", "switch3"))
if mibBuilder.loadTexts: alarmstart7_7e.setDescription('A alarmstart7 trap signifies that the current\n\t\t\tstatus of switch sensor 3 is outside the \n\t\t\tdefined threshold.')
alarmclear7_7e = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 2) + (0,14)).setLabel("alarmclear7-7e").setObjects(("ROOMALERT7E-MIB", "alarmmessage"), ("ROOMALERT7E-MIB", "switch3"), ("ROOMALERT7E-MIB", "switch3"))
if mibBuilder.loadTexts: alarmclear7_7e.setDescription('A alarmclear7 trap signifies that the current\n\t\t\tstatus of switch sensor 3 is outside the \n\t\t\tdefined threshold.')
mibBuilder.exportSymbols("ROOMALERT7E-MIB", lowerlimit4=lowerlimit4, alarmstart4_7e=alarmstart4_7e, lowerlimit3=lowerlimit3, tempreading1f=tempreading1f, alarmswitch1=alarmswitch1, alarmstart6_7e=alarmstart6_7e, alarmclear5_7e=alarmclear5_7e, alarmclear4_7e=alarmclear4_7e, products=products, alarmclear2_7e=alarmclear2_7e, tempreading1c=tempreading1c, traps=traps, alarmstart7_7e=alarmstart7_7e, switch=switch, thresholds=thresholds, switch1=switch1, alarmstart1_7e=alarmstart1_7e, tempreading3c=tempreading3c, switch2=switch2, sensors=sensors, room_alert_7e_snmp_trap=room_alert_7e_snmp_trap, roomalert7e=roomalert7e, upperlimit4=upperlimit4, tempreading4f=tempreading4f, alarmclear7_7e=alarmclear7_7e, avtech=avtech, upperlimit3=upperlimit3, lowerlimit1=lowerlimit1, alarmtemp4=alarmtemp4, tempreading4c=tempreading4c, switch3=switch3, tempreading3f=tempreading3f, upperlimit2=upperlimit2, alarmstart2_7e=alarmstart2_7e, alarmstart3_7e=alarmstart3_7e, alarmclear6_7e=alarmclear6_7e, alarmmessage=alarmmessage, alarmtemp3=alarmtemp3, alarmswitch2=alarmswitch2, lowerlimit2=lowerlimit2, alarmswitch3=alarmswitch3, tempreading2c=tempreading2c, tempreading2f=tempreading2f, temperature=temperature, alarmtemp1=alarmtemp1, alarmtemp2=alarmtemp2, alarmstart5_7e=alarmstart5_7e, upperlimit1=upperlimit1, alarmclear3_7e=alarmclear3_7e)
