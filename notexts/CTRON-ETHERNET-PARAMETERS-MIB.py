#
# PySNMP MIB module CTRON-ETHERNET-PARAMETERS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-ETHERNET-PARAMETERS-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:20:21 2022
# On host fv-az36-988 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ctIfPortPortNumber, ctIfPortIfNumber = mibBuilder.importSymbols("CTIF-EXT-MIB", "ctIfPortPortNumber", "ctIfPortIfNumber")
ctEthernetCtlParameters, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctEthernetCtlParameters")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, Gauge32, Counter32, iso, NotificationType, MibIdentifier, TimeTicks, IpAddress, ModuleIdentity, Bits, ObjectIdentity, Unsigned32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Gauge32", "Counter32", "iso", "NotificationType", "MibIdentifier", "TimeTicks", "IpAddress", "ModuleIdentity", "Bits", "ObjectIdentity", "Unsigned32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ctAutoNegCtl = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 4, 2, 1))
ctAutoNegCtlTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 4, 2, 1, 1), )
if mibBuilder.loadTexts: ctAutoNegCtlTable.setStatus('mandatory')
ctAutoNegCtlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 4, 2, 1, 1, 1), ).setIndexNames((0, "CTIF-EXT-MIB", "ctIfPortIfNumber"), (0, "CTIF-EXT-MIB", "ctIfPortPortNumber"))
if mibBuilder.loadTexts: ctAutoNegCtlEntry.setStatus('mandatory')
ctAutoNegAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 4, 2, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctAutoNegAdminStatus.setStatus('mandatory')
ctAutoNegRemoteSignalling = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 4, 2, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("detected", 1), ("notdetected", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctAutoNegRemoteSignalling.setStatus('mandatory')
ctAutoNegAutoConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 4, 2, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("configuring", 2), ("complete", 3), ("disabled", 4), ("paralleldetectfailed", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctAutoNegAutoConfig.setStatus('mandatory')
ctAutoNegLocalTechnologyAbility = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 4, 2, 1, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctAutoNegLocalTechnologyAbility.setStatus('mandatory')
ctAutoNegAdvertisedTechnologyAbility = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 4, 2, 1, 1, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctAutoNegAdvertisedTechnologyAbility.setStatus('mandatory')
ctAutoNegReceivedTechnologyAbility = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 4, 2, 1, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctAutoNegReceivedTechnologyAbility.setStatus('mandatory')
ctFlowControl = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 4, 2, 2))
ctFlowCtlTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 4, 2, 2, 1), )
if mibBuilder.loadTexts: ctFlowCtlTable.setStatus('mandatory')
ctFlowCtlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 4, 2, 2, 1, 1), ).setIndexNames((0, "CTIF-EXT-MIB", "ctIfPortIfNumber"), (0, "CTIF-EXT-MIB", "ctIfPortPortNumber"))
if mibBuilder.loadTexts: ctFlowCtlEntry.setStatus('mandatory')
ctFlowCtlHalfDuplexAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 4, 2, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctFlowCtlHalfDuplexAdminStatus.setStatus('mandatory')
ctFlowCtlHalfDuplexOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 4, 2, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ("notsupported", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFlowCtlHalfDuplexOperStatus.setStatus('mandatory')
ctEtherSupportedPauseModes = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 4, 2, 2, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctEtherSupportedPauseModes.setStatus('mandatory')
ctFlowCtlPauseAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 4, 2, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("symmetric", 1), ("asymmetricRx", 2), ("asymmetricTx", 3), ("disabled", 4), ("autonegotiate", 5))).clone('autonegotiate')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctFlowCtlPauseAdminStatus.setStatus('mandatory')
ctFlowCtlPauseOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 4, 2, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("symmetric", 1), ("asymmetricRx", 2), ("asymmetricTx", 3), ("disabled", 4), ("unknown", 5), ("notsupported", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFlowCtlPauseOperStatus.setStatus('mandatory')
ctFlowCtlPauseTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 4, 2, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFlowCtlPauseTimer.setStatus('mandatory')
ctFlowCtlRxPauseFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 4, 2, 2, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFlowCtlRxPauseFrames.setStatus('mandatory')
ctFlowCtlTxPauseFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 4, 2, 2, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFlowCtlTxPauseFrames.setStatus('mandatory')
ctEtherManualConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 4, 2, 3))
ctEtherManualConfigTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 4, 2, 3, 1), )
if mibBuilder.loadTexts: ctEtherManualConfigTable.setStatus('mandatory')
ctEtherManualConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 4, 2, 3, 1, 1), ).setIndexNames((0, "CTIF-EXT-MIB", "ctIfPortIfNumber"), (0, "CTIF-EXT-MIB", "ctIfPortPortNumber"))
if mibBuilder.loadTexts: ctEtherManualConfigEntry.setStatus('mandatory')
ctEtherSupportedSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 4, 2, 3, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctEtherSupportedSpeed.setStatus('mandatory')
ctEtherSpeedAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 4, 2, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2, 3, 4))).clone(namedValues=NamedValues(("tenmegabit", 2), ("hundredmegabit", 3), ("gigabit", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctEtherSpeedAdminStatus.setStatus('mandatory')
ctEtherSpeedOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 4, 2, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("unknown", 1), ("tenmegabit", 2), ("hundredmegabit", 3), ("gigabit", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctEtherSpeedOperStatus.setStatus('mandatory')
ctEtherSupportedDuplex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 4, 2, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("halfduplex", 1), ("fullduplex", 2), ("halfandfullduplex", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctEtherSupportedDuplex.setStatus('mandatory')
ctEtherDuplexAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 4, 2, 3, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2, 3))).clone(namedValues=NamedValues(("halfduplex", 2), ("fullduplex", 3))).clone('halfduplex')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctEtherDuplexAdminStatus.setStatus('mandatory')
ctEtherDuplexOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 4, 2, 3, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unknown", 1), ("halfduplex", 2), ("fullduplex", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctEtherDuplexOperStatus.setStatus('mandatory')
mibBuilder.exportSymbols("CTRON-ETHERNET-PARAMETERS-MIB", ctEtherDuplexOperStatus=ctEtherDuplexOperStatus, ctFlowControl=ctFlowControl, ctEtherSpeedOperStatus=ctEtherSpeedOperStatus, ctEtherDuplexAdminStatus=ctEtherDuplexAdminStatus, ctEtherSupportedDuplex=ctEtherSupportedDuplex, ctFlowCtlHalfDuplexAdminStatus=ctFlowCtlHalfDuplexAdminStatus, ctAutoNegCtlTable=ctAutoNegCtlTable, ctEtherManualConfigTable=ctEtherManualConfigTable, ctAutoNegCtl=ctAutoNegCtl, ctEtherManualConfig=ctEtherManualConfig, ctEtherSpeedAdminStatus=ctEtherSpeedAdminStatus, ctAutoNegCtlEntry=ctAutoNegCtlEntry, ctFlowCtlPauseTimer=ctFlowCtlPauseTimer, ctEtherManualConfigEntry=ctEtherManualConfigEntry, ctFlowCtlPauseAdminStatus=ctFlowCtlPauseAdminStatus, ctAutoNegAdminStatus=ctAutoNegAdminStatus, ctAutoNegAdvertisedTechnologyAbility=ctAutoNegAdvertisedTechnologyAbility, ctFlowCtlTxPauseFrames=ctFlowCtlTxPauseFrames, ctFlowCtlEntry=ctFlowCtlEntry, ctEtherSupportedPauseModes=ctEtherSupportedPauseModes, ctFlowCtlTable=ctFlowCtlTable, ctFlowCtlPauseOperStatus=ctFlowCtlPauseOperStatus, ctEtherSupportedSpeed=ctEtherSupportedSpeed, ctFlowCtlHalfDuplexOperStatus=ctFlowCtlHalfDuplexOperStatus, ctAutoNegReceivedTechnologyAbility=ctAutoNegReceivedTechnologyAbility, ctFlowCtlRxPauseFrames=ctFlowCtlRxPauseFrames, ctAutoNegLocalTechnologyAbility=ctAutoNegLocalTechnologyAbility, ctAutoNegAutoConfig=ctAutoNegAutoConfig, ctAutoNegRemoteSignalling=ctAutoNegRemoteSignalling)
