#
# PySNMP MIB module RADLAN-rndMng (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/radlan/RADLAN-rndMng
# Produced by pysmi-1.1.8 at Sat Jan 15 18:17:50 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
rnd, = mibBuilder.importSymbols("RADLAN-MIB", "rnd")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, Integer32, Counter64, IpAddress, NotificationType, Counter32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, iso, TimeTicks, Unsigned32, ModuleIdentity, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Integer32", "Counter64", "IpAddress", "NotificationType", "Counter32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "iso", "TimeTicks", "Unsigned32", "ModuleIdentity", "Bits")
TruthValue, DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "RowStatus", "TextualConvention")
DisplayString, = mibBuilder.importSymbols("SNMPv2-TC-v1", "DisplayString")
rndMng = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 1))
rndMng.setRevisions(('2006-06-20 00:00', '2004-06-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rndMng.setRevisionsDescriptions(('Added rlRebootDelay object', 'Initial version of this MIB.',))
if mibBuilder.loadTexts: rndMng.setLastUpdated('200606200000Z')
if mibBuilder.loadTexts: rndMng.setOrganization('Radlan Computer Communications Ltd.')
if mibBuilder.loadTexts: rndMng.setContactInfo('radlan.com')
if mibBuilder.loadTexts: rndMng.setDescription('The private MIB module definition for RND general management MIB.')
rndSysId = MibScalar((1, 3, 6, 1, 4, 1, 89, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rndSysId.setStatus('current')
if mibBuilder.loadTexts: rndSysId.setDescription('Identification of an RND device. The device type for each\n      integer clarifies the sysObjectID in MIB - II.')
rndAction = MibScalar((1, 3, 6, 1, 4, 1, 89, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27))).clone(namedValues=NamedValues(("reset", 1), ("sendNetworkTab", 2), ("deleteNetworkTab", 3), ("sendRoutingTab", 4), ("deleteRoutingTab", 5), ("sendLanTab", 6), ("deleteLanTab", 7), ("deleteArpTab", 8), ("sendArpTab", 9), ("deleteRouteTab", 10), ("sendRouteTab", 11), ("backupSPFRoutingTab", 12), ("backupIPRoutingTab", 13), ("backupNetworkTab", 14), ("backupLanTab", 15), ("backupArpTab", 16), ("backupIPXRipTab", 17), ("backupIPXSAPTab", 18), ("resetStartupCDB", 19), ("eraseStartupCDB", 20), ("deleteZeroHopRoutingAllocTab", 21), ("slipDisconnect", 22), ("deleteDynamicLanTab", 23), ("eraseRunningCDB", 24), ("copyStartupToRunning", 25), ("none", 26), ("resetToFactoryDefaults", 27)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rndAction.setStatus('current')
if mibBuilder.loadTexts: rndAction.setDescription('This variable enables the operator to perform one of the\n      specified actions on the tables maintained by the network device.\n      Send actions require support of proprietery File exchange\n      protocol.')
rndFileName = MibScalar((1, 3, 6, 1, 4, 1, 89, 1, 3), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rndFileName.setStatus('current')
if mibBuilder.loadTexts: rndFileName.setDescription('The name of the file used internally by RND for transferring\n      tables maintained by network devices, using a prorietary File\n      exchange protocol.')
rlSnmpVersionSupported = MibScalar((1, 3, 6, 1, 4, 1, 89, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSnmpVersionSupported.setStatus('current')
if mibBuilder.loadTexts: rlSnmpVersionSupported.setDescription('Indicates the snmp versions that are supported by\n        this device.')
rlSnmpMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 89, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSnmpMibVersion.setStatus('current')
if mibBuilder.loadTexts: rlSnmpMibVersion.setDescription('Indicates the snmp support version that is supported by\n        this device.')
rlCpuUtilEnable = MibScalar((1, 3, 6, 1, 4, 1, 89, 1, 6), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCpuUtilEnable.setStatus('current')
if mibBuilder.loadTexts: rlCpuUtilEnable.setDescription('Enables measurement of the device CPU utilization.\n         In order to get real values for rlCpuUtilDuringLastSecond, rlCpuUtilDuringLastMinute\n         and rlCpuUtilDuringLast5Minutes, the value of this object must be true.')
rlCpuUtilDuringLastSecond = MibScalar((1, 3, 6, 1, 4, 1, 89, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 101))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlCpuUtilDuringLastSecond.setStatus('current')
if mibBuilder.loadTexts: rlCpuUtilDuringLastSecond.setDescription('Percentage of the device CPU utilization during last second.\n         The value 101 is a dummy value, indicating that the CPU utilization was\n         not measured (since measurement is disabled or was disabled during last second).')
rlCpuUtilDuringLastMinute = MibScalar((1, 3, 6, 1, 4, 1, 89, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 101))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlCpuUtilDuringLastMinute.setStatus('current')
if mibBuilder.loadTexts: rlCpuUtilDuringLastMinute.setDescription('Percentage of the device CPU utilization during last minute.\n         The value 101 is a dummy value, indicating that the CPU utilization was\n         not measured (since measurement is disabled or was disabled during last minute).')
rlCpuUtilDuringLast5Minutes = MibScalar((1, 3, 6, 1, 4, 1, 89, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 101))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlCpuUtilDuringLast5Minutes.setStatus('current')
if mibBuilder.loadTexts: rlCpuUtilDuringLast5Minutes.setDescription('Percentage of the device CPU utilization during the last 5 minutes.\n         The value 101 is a dummy value, indicating that the CPU utilization was\n         not measured (since measurement is disabled or was disabled during last 5 minutes).')
rlRebootDelay = MibScalar((1, 3, 6, 1, 4, 1, 89, 1, 10), TimeTicks()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlRebootDelay.setStatus('current')
if mibBuilder.loadTexts: rlRebootDelay.setDescription('Setting the variable will cause the device to reboot rlRebootDelay timeticks\n         from the moment this variable was set.\n         If not set, the variable will return a value of 4294967295.\n         If set to 4294967295, reboot action is cancelled.\n         The maximum delay is set by the host parameter: reboot_delay_max')
mibBuilder.exportSymbols("RADLAN-rndMng", rndSysId=rndSysId, rlCpuUtilDuringLastMinute=rlCpuUtilDuringLastMinute, rlCpuUtilDuringLastSecond=rlCpuUtilDuringLastSecond, rlSnmpMibVersion=rlSnmpMibVersion, rlCpuUtilDuringLast5Minutes=rlCpuUtilDuringLast5Minutes, rlRebootDelay=rlRebootDelay, rlCpuUtilEnable=rlCpuUtilEnable, rndMng=rndMng, rndFileName=rndFileName, PYSNMP_MODULE_ID=rndMng, rndAction=rndAction, rlSnmpVersionSupported=rlSnmpVersionSupported)
