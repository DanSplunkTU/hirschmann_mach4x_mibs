#
# PySNMP MIB module CTRON-BDG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-BDG-MIB
# Produced by pysmi-1.1.3 at Sun Nov 21 00:45:06 2021
# On host fv-az39-63 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
bridge, layerMgmt = mibBuilder.importSymbols("IRM-OIDS", "bridge", "layerMgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, NotificationType, ObjectIdentity, TimeTicks, MibIdentifier, Bits, Integer32, Gauge32, ModuleIdentity, Counter32, Unsigned32, IpAddress, iso = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "NotificationType", "ObjectIdentity", "TimeTicks", "MibIdentifier", "Bits", "Integer32", "Gauge32", "ModuleIdentity", "Counter32", "Unsigned32", "IpAddress", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
bridgeRev1 = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 3, 1))
bdgdevice = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 1))
bdgPort = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 2))
filterDB = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3))
trapTypes = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 4))
bdgTables = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 5))
acqDB = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 1))
permDB = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 2))
specialDB = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 3))
acqStats = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 1, 1))
acqOptions = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 1, 2))
permStats = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 2, 1))
permOptions = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 2, 2))
specStats = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 3, 1))
specFilters = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 3, 2))
bdgdeviceDisableBdg = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disableBridge", 0), ("enableBridge", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bdgdeviceDisableBdg.setStatus('mandatory')
bdgdeviceRestoreSettings = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0))).clone(namedValues=NamedValues(("restoreSettings", 0)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bdgdeviceRestoreSettings.setStatus('mandatory')
bdgdeviceBdgName = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 1, 4), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bdgdeviceBdgName.setStatus('mandatory')
bdgdeviceNumPorts = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdgdeviceNumPorts.setStatus('mandatory')
bdgdeviceType = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 1, 6), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdgdeviceType.setStatus('mandatory')
bdgdeviceVersion = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 1, 7), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdgdeviceVersion.setStatus('mandatory')
bdgdeviceLocation = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 1, 8), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bdgdeviceLocation.setStatus('mandatory')
bdgdeviceStatus = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 1, 9), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdgdeviceStatus.setStatus('mandatory')
bdgdeviceRestartBdg = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0))).clone(namedValues=NamedValues(("restartBridge", 0)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bdgdeviceRestartBdg.setStatus('mandatory')
bdgdeviceFrFwd = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdgdeviceFrFwd.setStatus('mandatory')
bdgdeviceFrRx = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdgdeviceFrRx.setStatus('mandatory')
bdgdeviceFrFlt = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdgdeviceFrFlt.setStatus('mandatory')
bdgdeviceErr = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdgdeviceErr.setStatus('mandatory')
bdgdeviceSwitchSetting = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 1, 15), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdgdeviceSwitchSetting.setStatus('mandatory')
bdgdeviceNumRestarts = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdgdeviceNumRestarts.setStatus('mandatory')
bdgdeviceTypeFiltering = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("ieee8021", 0), ("specialDB", 1), ("both", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bdgdeviceTypeFiltering.setStatus('mandatory')
bdgdeviceSTAProtocol = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("ieee8021", 0), ("dec", 1), ("none", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bdgdeviceSTAProtocol.setStatus('mandatory')
bdgdeviceBridgeID = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 1, 19), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdgdeviceBridgeID.setStatus('mandatory')
bdgdeviceTopChgCnt = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdgdeviceTopChgCnt.setStatus('mandatory')
bdgdeviceRootCost = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 1, 21), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdgdeviceRootCost.setStatus('mandatory')
bdgdeviceRootPort = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 1, 22), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdgdeviceRootPort.setStatus('mandatory')
bdgdeviceHelloTime = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 1, 23), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdgdeviceHelloTime.setStatus('mandatory')
bdgdeviceBdgMaxAge = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 1, 24), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bdgdeviceBdgMaxAge.setStatus('mandatory')
bdgdeviceBdgFwdDly = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 1, 25), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bdgdeviceBdgFwdDly.setStatus('mandatory')
bdgdeviceTimeTopChg = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 1, 26), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdgdeviceTimeTopChg.setStatus('mandatory')
bdgdeviceTopChg = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 1, 27), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("noTopologyChangeInProgress", 0), ("topologyChangeInProgress", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdgdeviceTopChg.setStatus('mandatory')
bdgdeviceDesigRoot = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 1, 28), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdgdeviceDesigRoot.setStatus('mandatory')
bdgdeviceMaxAge = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 1, 29), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdgdeviceMaxAge.setStatus('mandatory')
bdgdeviceHoldTime = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 1, 30), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdgdeviceHoldTime.setStatus('mandatory')
bdgdeviceFwdDly = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 1, 31), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdgdeviceFwdDly.setStatus('mandatory')
bdgdeviceBdgHello = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 1, 32), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bdgdeviceBdgHello.setStatus('mandatory')
bdgdeviceBdgPriority = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 1, 33), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bdgdeviceBdgPriority.setStatus('mandatory')
bdgdeviceResetCounts = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 1, 34), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0))).clone(namedValues=NamedValues(("resetCounts", 0)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bdgdeviceResetCounts.setStatus('mandatory')
bdgdeviceUptime = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 1, 35), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdgdeviceUptime.setStatus('mandatory')
bdgdeviceTrapType = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 1, 36), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdgdeviceTrapType.setStatus('mandatory')
bdgPortAddress = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 2, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdgPortAddress.setStatus('mandatory')
bdgPortName = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 2, 2), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bdgPortName.setStatus('mandatory')
bdgPortType = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 2, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdgPortType.setStatus('mandatory')
bdgPortStatus = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 2, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdgPortStatus.setStatus('mandatory')
bdgPortNetName = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 2, 5), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bdgPortNetName.setStatus('mandatory')
bdgPortFrRx = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 2, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdgPortFrRx.setStatus('mandatory')
bdgPortDisInb = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 2, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdgPortDisInb.setStatus('mandatory')
bdgPortFwdOutb = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 2, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdgPortFwdOutb.setStatus('mandatory')
bdgPortDisLOB = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 2, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdgPortDisLOB.setStatus('mandatory')
bdgPortDisTDE = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 2, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdgPortDisTDE.setStatus('mandatory')
bdgPortDisErr = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 2, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdgPortDisErr.setStatus('mandatory')
bdgPortColl = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 2, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdgPortColl.setStatus('mandatory')
bdgPortTxAbrt = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 2, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdgPortTxAbrt.setStatus('mandatory')
bdgPortOowColl = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 2, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdgPortOowColl.setStatus('mandatory')
bdgPortCRCErr = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 2, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdgPortCRCErr.setStatus('mandatory')
bdgPortFrAlErr = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 2, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdgPortFrAlErr.setStatus('mandatory')
bdgPortPriority = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 2, 17), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bdgPortPriority.setStatus('mandatory')
bdgPortState = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 2, 18), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdgPortState.setStatus('mandatory')
bdgPortPathCost = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 2, 19), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bdgPortPathCost.setStatus('mandatory')
bdgPortDesigCost = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 2, 20), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdgPortDesigCost.setStatus('mandatory')
bdgPortDesigBrdg = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 2, 21), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdgPortDesigBrdg.setStatus('mandatory')
bdgPortDesigPort = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 2, 22), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdgPortDesigPort.setStatus('mandatory')
bdgPortTopChgAck = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 2, 23), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("noTopologyChangeIsOccurring", 0), ("topologyChangeIsOccurring", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdgPortTopChgAck.setStatus('mandatory')
bdgPortDesigRoot = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 2, 24), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdgPortDesigRoot.setStatus('mandatory')
bdgPortRuntPackets = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 2, 25), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdgPortRuntPackets.setStatus('mandatory')
bdgPortOversizePackets = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 2, 26), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdgPortOversizePackets.setStatus('mandatory')
bdgPortFrFilt = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 2, 27), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdgPortFrFilt.setStatus('mandatory')
acqTotalEntries = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acqTotalEntries.setStatus('mandatory')
acqMaxEntries = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acqMaxEntries.setStatus('mandatory')
acqStaticEntries = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acqStaticEntries.setStatus('mandatory')
acqStaticAgeTime = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acqStaticAgeTime.setStatus('mandatory')
acqDynEntries = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acqDynEntries.setStatus('mandatory')
acqDynAgeTime = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 1, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acqDynAgeTime.setStatus('mandatory')
acqEraseDatabase = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0))).clone(namedValues=NamedValues(("eraseAcquiredDatabase", 0)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acqEraseDatabase.setStatus('mandatory')
acqCreate00 = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 1, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0))).clone(namedValues=NamedValues(("createAcquiredEntryFilterPort1FilterPort2", 0)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acqCreate00.setStatus('mandatory')
acqCreate20 = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 1, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0))).clone(namedValues=NamedValues(("createAcquiredEntryForwardPort1FilterPort2", 0)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acqCreate20.setStatus('mandatory')
acqCreate01 = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 1, 2, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0))).clone(namedValues=NamedValues(("createAcquiredEntryFilterPort1ForwardPort2", 0)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acqCreate01.setStatus('mandatory')
acqCreate21 = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 1, 2, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0))).clone(namedValues=NamedValues(("createAcquiredEntryForwardPort1ForwardPort2", 0)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acqCreate21.setStatus('mandatory')
acqDelete = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 1, 2, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0))).clone(namedValues=NamedValues(("deleteAcquiredEntry", 0)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acqDelete.setStatus('mandatory')
acqDispType = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 1, 2, 6), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acqDispType.setStatus('mandatory')
acqDispOutp1 = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 1, 2, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 2))).clone(namedValues=NamedValues(("filter", 0), ("relay", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acqDispOutp1.setStatus('mandatory')
acqDispOutp2 = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 1, 2, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("filter", 0), ("relay", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acqDispOutp2.setStatus('mandatory')
acqSrcAddress = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 1, 2, 9), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acqSrcAddress.setStatus('mandatory')
permMaxEntries = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: permMaxEntries.setStatus('mandatory')
permCurrEntries = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: permCurrEntries.setStatus('mandatory')
permEraseDatabase = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0))).clone(namedValues=NamedValues(("erasePermanentDatabase", 0)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: permEraseDatabase.setStatus('mandatory')
permCreate00 = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 2, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0))).clone(namedValues=NamedValues(("createPermanentEntryFilterPort1FilterPort2", 0)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: permCreate00.setStatus('mandatory')
permCreate20 = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 2, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0))).clone(namedValues=NamedValues(("createPermanentEntryForwardPort1FilterPort2", 0)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: permCreate20.setStatus('mandatory')
permCreate01 = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 2, 2, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0))).clone(namedValues=NamedValues(("createPermanentEntryFilterPort1ForwardPort2", 0)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: permCreate01.setStatus('mandatory')
permCreate21 = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 2, 2, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0))).clone(namedValues=NamedValues(("createPermanentEntryForwardPort1ForwardPort2", 0)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: permCreate21.setStatus('mandatory')
permDelete = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 2, 2, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0))).clone(namedValues=NamedValues(("deletePermanentEntry", 0)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: permDelete.setStatus('mandatory')
permDispType = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 2, 2, 6), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: permDispType.setStatus('mandatory')
permDispOutp1 = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 2, 2, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 2))).clone(namedValues=NamedValues(("filter", 0), ("relay", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: permDispOutp1.setStatus('mandatory')
permDispOutp2 = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 2, 2, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("filter", 0), ("relay", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: permDispOutp2.setStatus('mandatory')
permSrcAddress = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 2, 2, 9), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: permSrcAddress.setStatus('mandatory')
specNumEntries = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: specNumEntries.setStatus('mandatory')
specMaxEntries = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: specMaxEntries.setStatus('mandatory')
specNextFilterNum = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: specNextFilterNum.setStatus('mandatory')
specEnable = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 3, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disableFilter", 0), ("enableFilter", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: specEnable.setStatus('mandatory')
specPort1 = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 3, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 2))).clone(namedValues=NamedValues(("filter", 0), ("relay", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: specPort1.setStatus('mandatory')
specPort2 = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 3, 2, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("filter", 0), ("relay", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: specPort2.setStatus('mandatory')
specDestAddress = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 3, 2, 4), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: specDestAddress.setStatus('mandatory')
specSrcAddress = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 3, 2, 5), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: specSrcAddress.setStatus('mandatory')
specType = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 3, 2, 6), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: specType.setStatus('mandatory')
specDataField = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 3, 2, 7), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: specDataField.setStatus('mandatory')
specDeleteFilter = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 3, 2, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0))).clone(namedValues=NamedValues(("deleteFilter", 0)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: specDeleteFilter.setStatus('mandatory')
lmcommon = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 2, 1))
mAC = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 2, 2))
ieee8023 = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 2, 2, 1))
pcIF = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 2, 2, 1, 1))
pcIfRev = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 2, 2, 1, 1, 1))
pcDeviceName = MibScalar((1, 3, 6, 1, 4, 1, 52, 2, 2, 1, 1, 1, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pcDeviceName.setStatus('mandatory')
pcBoardType = MibScalar((1, 3, 6, 1, 4, 1, 52, 2, 2, 1, 1, 1, 2), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pcBoardType.setStatus('mandatory')
pcOwnerName = MibScalar((1, 3, 6, 1, 4, 1, 52, 2, 2, 1, 1, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pcOwnerName.setStatus('mandatory')
pcLocation = MibScalar((1, 3, 6, 1, 4, 1, 52, 2, 2, 1, 1, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pcLocation.setStatus('mandatory')
pcMMACAddr = MibScalar((1, 3, 6, 1, 4, 1, 52, 2, 2, 1, 1, 1, 5), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pcMMACAddr.setStatus('mandatory')
pcMMACBoard = MibScalar((1, 3, 6, 1, 4, 1, 52, 2, 2, 1, 1, 1, 6), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pcMMACBoard.setStatus('mandatory')
pcMMACPort = MibScalar((1, 3, 6, 1, 4, 1, 52, 2, 2, 1, 1, 1, 7), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pcMMACPort.setStatus('mandatory')
pcApplication = MibScalar((1, 3, 6, 1, 4, 1, 52, 2, 2, 1, 1, 1, 8), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pcApplication.setStatus('mandatory')
pcDriverRev = MibScalar((1, 3, 6, 1, 4, 1, 52, 2, 2, 1, 1, 1, 9), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pcDriverRev.setStatus('mandatory')
pcOnboardMemory = MibScalar((1, 3, 6, 1, 4, 1, 52, 2, 2, 1, 1, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pcOnboardMemory.setStatus('mandatory')
pcComment = MibScalar((1, 3, 6, 1, 4, 1, 52, 2, 2, 1, 1, 1, 11), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pcComment.setStatus('mandatory')
pcMACAddr = MibScalar((1, 3, 6, 1, 4, 1, 52, 2, 2, 1, 1, 1, 12), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pcMACAddr.setStatus('mandatory')
pcFramesXmit = MibScalar((1, 3, 6, 1, 4, 1, 52, 2, 2, 1, 1, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pcFramesXmit.setStatus('mandatory')
pcBytesXmit = MibScalar((1, 3, 6, 1, 4, 1, 52, 2, 2, 1, 1, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pcBytesXmit.setStatus('mandatory')
pcMcastXmit = MibScalar((1, 3, 6, 1, 4, 1, 52, 2, 2, 1, 1, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pcMcastXmit.setStatus('mandatory')
pcBcastXmit = MibScalar((1, 3, 6, 1, 4, 1, 52, 2, 2, 1, 1, 1, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pcBcastXmit.setStatus('mandatory')
pcDeferXmit = MibScalar((1, 3, 6, 1, 4, 1, 52, 2, 2, 1, 1, 1, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pcDeferXmit.setStatus('mandatory')
pcSglColl = MibScalar((1, 3, 6, 1, 4, 1, 52, 2, 2, 1, 1, 1, 18), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pcSglColl.setStatus('mandatory')
pcMultiColl = MibScalar((1, 3, 6, 1, 4, 1, 52, 2, 2, 1, 1, 1, 19), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pcMultiColl.setStatus('mandatory')
pcTotXmitErrs = MibScalar((1, 3, 6, 1, 4, 1, 52, 2, 2, 1, 1, 1, 20), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pcTotXmitErrs.setStatus('mandatory')
pcLateColls = MibScalar((1, 3, 6, 1, 4, 1, 52, 2, 2, 1, 1, 1, 21), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pcLateColls.setStatus('mandatory')
pcXcessColls = MibScalar((1, 3, 6, 1, 4, 1, 52, 2, 2, 1, 1, 1, 22), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pcXcessColls.setStatus('mandatory')
pcCarrErr = MibScalar((1, 3, 6, 1, 4, 1, 52, 2, 2, 1, 1, 1, 23), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pcCarrErr.setStatus('mandatory')
pcFramesRec = MibScalar((1, 3, 6, 1, 4, 1, 52, 2, 2, 1, 1, 1, 24), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pcFramesRec.setStatus('mandatory')
pcBytesRec = MibScalar((1, 3, 6, 1, 4, 1, 52, 2, 2, 1, 1, 1, 25), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pcBytesRec.setStatus('mandatory')
pcMcastRec = MibScalar((1, 3, 6, 1, 4, 1, 52, 2, 2, 1, 1, 1, 26), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pcMcastRec.setStatus('mandatory')
pcBcastRec = MibScalar((1, 3, 6, 1, 4, 1, 52, 2, 2, 1, 1, 1, 27), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pcBcastRec.setStatus('mandatory')
pcTotRecErrs = MibScalar((1, 3, 6, 1, 4, 1, 52, 2, 2, 1, 1, 1, 28), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pcTotRecErrs.setStatus('mandatory')
pcTooLong = MibScalar((1, 3, 6, 1, 4, 1, 52, 2, 2, 1, 1, 1, 29), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pcTooLong.setStatus('mandatory')
pcTooShort = MibScalar((1, 3, 6, 1, 4, 1, 52, 2, 2, 1, 1, 1, 30), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pcTooShort.setStatus('mandatory')
pcAlignErrs = MibScalar((1, 3, 6, 1, 4, 1, 52, 2, 2, 1, 1, 1, 31), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pcAlignErrs.setStatus('mandatory')
pcCRCErrs = MibScalar((1, 3, 6, 1, 4, 1, 52, 2, 2, 1, 1, 1, 32), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pcCRCErrs.setStatus('mandatory')
pcLenErrs = MibScalar((1, 3, 6, 1, 4, 1, 52, 2, 2, 1, 1, 1, 33), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pcLenErrs.setStatus('mandatory')
pcIntRecErr = MibScalar((1, 3, 6, 1, 4, 1, 52, 2, 2, 1, 1, 1, 34), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pcIntRecErr.setStatus('mandatory')
pcSqeErr = MibScalar((1, 3, 6, 1, 4, 1, 52, 2, 2, 1, 1, 1, 35), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pcSqeErr.setStatus('mandatory')
mibBuilder.exportSymbols("CTRON-BDG-MIB", pcDeviceName=pcDeviceName, pcBytesRec=pcBytesRec, bdgPortDesigPort=bdgPortDesigPort, acqCreate21=acqCreate21, bdgdeviceTopChg=bdgdeviceTopChg, bdgdeviceBdgName=bdgdeviceBdgName, bdgdeviceErr=bdgdeviceErr, bdgdeviceRootCost=bdgdeviceRootCost, pcOnboardMemory=pcOnboardMemory, acqStaticAgeTime=acqStaticAgeTime, permSrcAddress=permSrcAddress, specSrcAddress=specSrcAddress, pcMMACBoard=pcMMACBoard, pcMcastRec=pcMcastRec, pcSqeErr=pcSqeErr, bdgdeviceDesigRoot=bdgdeviceDesigRoot, bdgdeviceUptime=bdgdeviceUptime, bdgdeviceSTAProtocol=bdgdeviceSTAProtocol, bdgdeviceTypeFiltering=bdgdeviceTypeFiltering, permCreate01=permCreate01, pcCRCErrs=pcCRCErrs, pcIfRev=pcIfRev, pcCarrErr=pcCarrErr, bdgdeviceRestoreSettings=bdgdeviceRestoreSettings, permCreate00=permCreate00, bdgPortCRCErr=bdgPortCRCErr, bdgdeviceSwitchSetting=bdgdeviceSwitchSetting, bdgdeviceFwdDly=bdgdeviceFwdDly, pcMcastXmit=pcMcastXmit, acqCreate01=acqCreate01, bdgPortColl=bdgPortColl, bdgPortStatus=bdgPortStatus, acqDispOutp1=acqDispOutp1, acqDynAgeTime=acqDynAgeTime, bdgPortFrRx=bdgPortFrRx, bdgdeviceBdgPriority=bdgdeviceBdgPriority, bdgdeviceBdgFwdDly=bdgdeviceBdgFwdDly, specFilters=specFilters, pcDeferXmit=pcDeferXmit, pcBytesXmit=pcBytesXmit, bdgPortDesigRoot=bdgPortDesigRoot, pcFramesXmit=pcFramesXmit, filterDB=filterDB, pcSglColl=pcSglColl, pcAlignErrs=pcAlignErrs, bdgdeviceType=bdgdeviceType, bdgdeviceDisableBdg=bdgdeviceDisableBdg, acqOptions=acqOptions, specNumEntries=specNumEntries, acqDispOutp2=acqDispOutp2, acqDB=acqDB, acqStaticEntries=acqStaticEntries, bdgdeviceBdgMaxAge=bdgdeviceBdgMaxAge, bdgdeviceRootPort=bdgdeviceRootPort, specDestAddress=specDestAddress, permEraseDatabase=permEraseDatabase, permDispOutp1=permDispOutp1, bdgPortType=bdgPortType, pcMMACAddr=pcMMACAddr, pcTotRecErrs=pcTotRecErrs, pcBcastRec=pcBcastRec, bdgdeviceBridgeID=bdgdeviceBridgeID, bdgPortTopChgAck=bdgPortTopChgAck, bdgPortDisLOB=bdgPortDisLOB, bdgPortAddress=bdgPortAddress, bdgPortFrAlErr=bdgPortFrAlErr, acqDynEntries=acqDynEntries, permDB=permDB, specialDB=specialDB, bdgPortRuntPackets=bdgPortRuntPackets, bdgPortFwdOutb=bdgPortFwdOutb, specStats=specStats, specDataField=specDataField, bdgPortPathCost=bdgPortPathCost, pcXcessColls=pcXcessColls, bdgdeviceFrRx=bdgdeviceFrRx, bdgdeviceMaxAge=bdgdeviceMaxAge, bdgdeviceHelloTime=bdgdeviceHelloTime, pcFramesRec=pcFramesRec, bdgPortDisErr=bdgPortDisErr, acqTotalEntries=acqTotalEntries, pcOwnerName=pcOwnerName, pcDriverRev=pcDriverRev, bdgdeviceNumPorts=bdgdeviceNumPorts, bdgdeviceVersion=bdgdeviceVersion, mAC=mAC, bdgPortDesigCost=bdgPortDesigCost, lmcommon=lmcommon, bdgdeviceHoldTime=bdgdeviceHoldTime, bdgdeviceResetCounts=bdgdeviceResetCounts, bdgdevice=bdgdevice, acqCreate00=acqCreate00, acqMaxEntries=acqMaxEntries, bdgdeviceBdgHello=bdgdeviceBdgHello, bridgeRev1=bridgeRev1, acqCreate20=acqCreate20, permCreate21=permCreate21, specPort1=specPort1, pcComment=pcComment, acqStats=acqStats, pcBoardType=pcBoardType, bdgPortName=bdgPortName, bdgdeviceTimeTopChg=bdgdeviceTimeTopChg, bdgPortDesigBrdg=bdgPortDesigBrdg, pcIF=pcIF, bdgdeviceFrFwd=bdgdeviceFrFwd, pcMACAddr=pcMACAddr, trapTypes=trapTypes, bdgdeviceTrapType=bdgdeviceTrapType, specDeleteFilter=specDeleteFilter, permMaxEntries=permMaxEntries, specEnable=specEnable, permCurrEntries=permCurrEntries, pcLocation=pcLocation, bdgPortState=bdgPortState, bdgPortFrFilt=bdgPortFrFilt, bdgdeviceFrFlt=bdgdeviceFrFlt, specType=specType, specMaxEntries=specMaxEntries, permOptions=permOptions, bdgPortDisInb=bdgPortDisInb, pcTotXmitErrs=pcTotXmitErrs, pcMultiColl=pcMultiColl, pcApplication=pcApplication, permDelete=permDelete, pcBcastXmit=pcBcastXmit, bdgdeviceLocation=bdgdeviceLocation, acqDispType=acqDispType, pcLateColls=pcLateColls, bdgTables=bdgTables, bdgPortOversizePackets=bdgPortOversizePackets, permCreate20=permCreate20, bdgPortNetName=bdgPortNetName, acqDelete=acqDelete, permDispOutp2=permDispOutp2, acqSrcAddress=acqSrcAddress, bdgPortTxAbrt=bdgPortTxAbrt, bdgdeviceNumRestarts=bdgdeviceNumRestarts, bdgdeviceRestartBdg=bdgdeviceRestartBdg, ieee8023=ieee8023, bdgPort=bdgPort, specPort2=specPort2, pcLenErrs=pcLenErrs, pcIntRecErr=pcIntRecErr, pcTooLong=pcTooLong, specNextFilterNum=specNextFilterNum, pcMMACPort=pcMMACPort, bdgPortOowColl=bdgPortOowColl, permDispType=permDispType, bdgdeviceTopChgCnt=bdgdeviceTopChgCnt, pcTooShort=pcTooShort, permStats=permStats, bdgdeviceStatus=bdgdeviceStatus, bdgPortDisTDE=bdgPortDisTDE, acqEraseDatabase=acqEraseDatabase, bdgPortPriority=bdgPortPriority)
