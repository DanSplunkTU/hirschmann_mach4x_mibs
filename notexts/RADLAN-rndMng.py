#
# PySNMP MIB module RADLAN-rndMng (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/radlan/RADLAN-rndMng
# Produced by pysmi-1.1.8 at Sun Jan 16 00:43:10 2022
# On host fv-az42-839 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
rnd, = mibBuilder.importSymbols("RADLAN-MIB", "rnd")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, Bits, Gauge32, iso, Unsigned32, ObjectIdentity, Counter64, Integer32, MibIdentifier, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, IpAddress, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Bits", "Gauge32", "iso", "Unsigned32", "ObjectIdentity", "Counter64", "Integer32", "MibIdentifier", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "IpAddress", "NotificationType")
DisplayString, TruthValue, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention", "RowStatus")
DisplayString, = mibBuilder.importSymbols("SNMPv2-TC-v1", "DisplayString")
rndMng = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 1))
rndMng.setRevisions(('2006-06-20 00:00', '2004-06-01 00:00',))
if mibBuilder.loadTexts: rndMng.setLastUpdated('200606200000Z')
if mibBuilder.loadTexts: rndMng.setOrganization('Radlan Computer Communications Ltd.')
rndSysId = MibScalar((1, 3, 6, 1, 4, 1, 89, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rndSysId.setStatus('current')
rndAction = MibScalar((1, 3, 6, 1, 4, 1, 89, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27))).clone(namedValues=NamedValues(("reset", 1), ("sendNetworkTab", 2), ("deleteNetworkTab", 3), ("sendRoutingTab", 4), ("deleteRoutingTab", 5), ("sendLanTab", 6), ("deleteLanTab", 7), ("deleteArpTab", 8), ("sendArpTab", 9), ("deleteRouteTab", 10), ("sendRouteTab", 11), ("backupSPFRoutingTab", 12), ("backupIPRoutingTab", 13), ("backupNetworkTab", 14), ("backupLanTab", 15), ("backupArpTab", 16), ("backupIPXRipTab", 17), ("backupIPXSAPTab", 18), ("resetStartupCDB", 19), ("eraseStartupCDB", 20), ("deleteZeroHopRoutingAllocTab", 21), ("slipDisconnect", 22), ("deleteDynamicLanTab", 23), ("eraseRunningCDB", 24), ("copyStartupToRunning", 25), ("none", 26), ("resetToFactoryDefaults", 27)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rndAction.setStatus('current')
rndFileName = MibScalar((1, 3, 6, 1, 4, 1, 89, 1, 3), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rndFileName.setStatus('current')
rlSnmpVersionSupported = MibScalar((1, 3, 6, 1, 4, 1, 89, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSnmpVersionSupported.setStatus('current')
rlSnmpMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 89, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSnmpMibVersion.setStatus('current')
rlCpuUtilEnable = MibScalar((1, 3, 6, 1, 4, 1, 89, 1, 6), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCpuUtilEnable.setStatus('current')
rlCpuUtilDuringLastSecond = MibScalar((1, 3, 6, 1, 4, 1, 89, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 101))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlCpuUtilDuringLastSecond.setStatus('current')
rlCpuUtilDuringLastMinute = MibScalar((1, 3, 6, 1, 4, 1, 89, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 101))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlCpuUtilDuringLastMinute.setStatus('current')
rlCpuUtilDuringLast5Minutes = MibScalar((1, 3, 6, 1, 4, 1, 89, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 101))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlCpuUtilDuringLast5Minutes.setStatus('current')
rlRebootDelay = MibScalar((1, 3, 6, 1, 4, 1, 89, 1, 10), TimeTicks()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlRebootDelay.setStatus('current')
mibBuilder.exportSymbols("RADLAN-rndMng", rndAction=rndAction, rndMng=rndMng, rlSnmpVersionSupported=rlSnmpVersionSupported, rlSnmpMibVersion=rlSnmpMibVersion, rlRebootDelay=rlRebootDelay, rlCpuUtilEnable=rlCpuUtilEnable, rlCpuUtilDuringLastSecond=rlCpuUtilDuringLastSecond, rndFileName=rndFileName, PYSNMP_MODULE_ID=rndMng, rndSysId=rndSysId, rlCpuUtilDuringLast5Minutes=rlCpuUtilDuringLast5Minutes, rlCpuUtilDuringLastMinute=rlCpuUtilDuringLastMinute)
