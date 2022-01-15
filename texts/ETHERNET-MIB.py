#
# PySNMP MIB module ETHERNET-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/exalt/ETHERNET-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 18:02:17 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
remEthAlarms, locEthAlarms, interface = mibBuilder.importSymbols("ExaltComProducts", "remEthAlarms", "locEthAlarms", "interface")
EnableStatusT, AlarmLevelT, EthernetMgmtTypeT = mibBuilder.importSymbols("ExaltComm", "EnableStatusT", "AlarmLevelT", "EthernetMgmtTypeT")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
IpAddress, Integer32, MibIdentifier, ModuleIdentity, TimeTicks, Bits, Unsigned32, ObjectIdentity, Counter64, iso, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Integer32", "MibIdentifier", "ModuleIdentity", "TimeTicks", "Bits", "Unsigned32", "ObjectIdentity", "Counter64", "iso", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class EthernetFunctionT(TextualConvention, Integer32):
    description = 'The  ethernet port function status '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("traffic", 0), ("mgmt", 1), ("trafficmgmt", 2))

class EthernetModeT(TextualConvention, Integer32):
    description = 'The Ethernet port operation modes '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("full1000", 0), ("half1000", 1), ("full100", 2), ("half100", 3), ("full10", 4), ("half10", 5), ("auto", 6))

class EthRateLimitTypeT(TextualConvention, Integer32):
    description = 'The ethernet rate limit type in KBPS (or) MBPS.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("kbps", 0), ("mbps", 1))

class EthRateLimitValueT(TextualConvention, Integer32):
    description = 'The ethernet rate limit, if the rate limit is enabled,\n                             the value is applied on to the port.\n                             eg., rate in KBPS (64..1792, stepsize 64)\n                                  rate in MBPS (2..100, stepsize 1) and (104..1000, stepsize 8)'
    status = 'current'

ethernet = ObjectIdentity((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 2, 1))
if mibBuilder.loadTexts: ethernet.setStatus('current')
if mibBuilder.loadTexts: ethernet.setDescription('Ethernet interfaces.')
ethernetNumChannels = MibScalar((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 2, 1, 3), Gauge32()).setUnits('channels').setMaxAccess("readonly")
if mibBuilder.loadTexts: ethernetNumChannels.setStatus('current')
if mibBuilder.loadTexts: ethernetNumChannels.setDescription('The maximum number of available ethernet channels. ')
ethernetInterfaces = MibTable((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 2, 1, 4), )
if mibBuilder.loadTexts: ethernetInterfaces.setStatus('current')
if mibBuilder.loadTexts: ethernetInterfaces.setDescription('Attributes for ethernet ports.')
ethernetInterface = MibTableRow((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 2, 1, 4, 1), ).setIndexNames((0, "ETHERNET-MIB", "function"), (0, "ETHERNET-MIB", "mode"), (0, "ETHERNET-MIB", "alarm"), (0, "ETHERNET-MIB", "mute"), (0, "ETHERNET-MIB", "dhcp"), (0, "ETHERNET-MIB", "rateConfig"), (0, "ETHERNET-MIB", "rateType"), (0, "ETHERNET-MIB", "rateLimit"))
if mibBuilder.loadTexts: ethernetInterface.setStatus('current')
if mibBuilder.loadTexts: ethernetInterface.setDescription('An entry in the Ethernet table.')
function = MibTableColumn((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 2, 1, 4, 1, 1), EthernetFunctionT()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: function.setStatus('current')
if mibBuilder.loadTexts: function.setDescription('Ethernet port function. ')
mode = MibTableColumn((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 2, 1, 4, 1, 2), EthernetModeT()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mode.setStatus('current')
if mibBuilder.loadTexts: mode.setDescription('Ethernet mode . ')
alarm = MibTableColumn((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 2, 1, 4, 1, 3), EnableStatusT()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alarm.setStatus('current')
if mibBuilder.loadTexts: alarm.setDescription('Ethernet port alarm. ')
mute = MibTableColumn((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 2, 1, 4, 1, 4), EnableStatusT()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mute.setStatus('current')
if mibBuilder.loadTexts: mute.setDescription("Ethernet can be muted, when there is a system/ethernet alarm.\n                             When MHS is enabled, the ethernet mute is termed as 'Auto', \n                             setting a value as 2, when MHS disabled, the value is restored ")
rateConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 2, 1, 4, 1, 5), EnableStatusT()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rateConfig.setStatus('current')
if mibBuilder.loadTexts: rateConfig.setDescription('Ethernet rate limit status, default is disabled ')
rateType = MibTableColumn((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 2, 1, 4, 1, 6), EthRateLimitTypeT()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rateType.setStatus('current')
if mibBuilder.loadTexts: rateType.setDescription('Ethernet rate limit type, default is KBPS ')
rateLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 2, 1, 4, 1, 7), EthRateLimitValueT()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rateLimit.setStatus('current')
if mibBuilder.loadTexts: rateLimit.setDescription('Ethernet rate limit type default is 64KBPS')
dhcp = MibTableColumn((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 2, 1, 4, 1, 8), EnableStatusT()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dhcp.setStatus('current')
if mibBuilder.loadTexts: dhcp.setDescription('DHCP (Enable/Disable) on port. ')
ethernetLearning = MibScalar((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 2, 1, 5), EnableStatusT()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ethernetLearning.setStatus('current')
if mibBuilder.loadTexts: ethernetLearning.setDescription('Etherner Learning (Enable/Disable) on the switch ')
ethernetMgmt = MibScalar((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 2, 1, 6), EthernetMgmtTypeT()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ethernetMgmt.setStatus('current')
if mibBuilder.loadTexts: ethernetMgmt.setDescription('Etherner Management Type (Inband/Out-of-Band/Port-to-Port/Legacy) for the switch ')
ethernetFlowControl = MibScalar((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 2, 1, 7), EnableStatusT()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ethernetFlowControl.setStatus('current')
if mibBuilder.loadTexts: ethernetFlowControl.setDescription('Etherner Flow Control (Disable/Enable) on the switch ')
commitEthernetSettings = MibScalar((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 2, 1, 1000), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(4, 200))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: commitEthernetSettings.setStatus('current')
if mibBuilder.loadTexts: commitEthernetSettings.setDescription('The Commit ethernet command. ')
locETHAlarms = MibTable((1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 2, 3, 2, 1), )
if mibBuilder.loadTexts: locETHAlarms.setStatus('current')
if mibBuilder.loadTexts: locETHAlarms.setDescription('The Local Ethernet Interface Alarms.')
locEthAlarmsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 2, 3, 2, 1, 1), ).setIndexNames((0, "ETHERNET-MIB", "locEthAlarm"))
if mibBuilder.loadTexts: locEthAlarmsEntry.setStatus('current')
if mibBuilder.loadTexts: locEthAlarmsEntry.setDescription('Ethernet Alarms table Entry.')
locEthAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 2, 3, 2, 1, 1, 1), AlarmLevelT()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locEthAlarm.setStatus('current')
if mibBuilder.loadTexts: locEthAlarm.setDescription('The Alarms state for the Local Ethernet Channel.\n                            ')
remETHAlarms = MibTable((1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 2, 4, 2, 1), )
if mibBuilder.loadTexts: remETHAlarms.setStatus('current')
if mibBuilder.loadTexts: remETHAlarms.setDescription('The Local Ethernet Interface Alarms.')
remEthAlarmsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 2, 4, 2, 1, 1), ).setIndexNames((0, "ETHERNET-MIB", "remEthAlarm"))
if mibBuilder.loadTexts: remEthAlarmsEntry.setStatus('current')
if mibBuilder.loadTexts: remEthAlarmsEntry.setDescription('Ethernet Alarms table Entry.')
remEthAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 2, 4, 2, 1, 1, 1), AlarmLevelT()).setMaxAccess("readonly")
if mibBuilder.loadTexts: remEthAlarm.setStatus('current')
if mibBuilder.loadTexts: remEthAlarm.setDescription('The Alarms state for the Remote Ethernet Channel.\n                            ')
mibBuilder.exportSymbols("ETHERNET-MIB", EthRateLimitValueT=EthRateLimitValueT, ethernetNumChannels=ethernetNumChannels, ethernetInterfaces=ethernetInterfaces, function=function, locEthAlarmsEntry=locEthAlarmsEntry, mode=mode, ethernetInterface=ethernetInterface, alarm=alarm, locEthAlarm=locEthAlarm, ethernet=ethernet, rateType=rateType, rateLimit=rateLimit, EthRateLimitTypeT=EthRateLimitTypeT, commitEthernetSettings=commitEthernetSettings, remEthAlarm=remEthAlarm, remETHAlarms=remETHAlarms, mute=mute, ethernetMgmt=ethernetMgmt, remEthAlarmsEntry=remEthAlarmsEntry, locETHAlarms=locETHAlarms, ethernetFlowControl=ethernetFlowControl, EthernetModeT=EthernetModeT, dhcp=dhcp, ethernetLearning=ethernetLearning, EthernetFunctionT=EthernetFunctionT, rateConfig=rateConfig)
