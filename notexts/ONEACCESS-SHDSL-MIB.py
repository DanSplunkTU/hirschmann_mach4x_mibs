#
# PySNMP MIB module ONEACCESS-SHDSL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/oneaccess/ONEACCESS-SHDSL-MIB
# Produced by pysmi-1.1.3 at Sun Nov 28 20:30:58 2021
# On host fv-az77-612 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
hdsl2ShdslSpanConfProfileEntry, hdsl2ShdslSpanStatusEntry, hdsl2ShdslEndpointCurrEntry = mibBuilder.importSymbols("HDSL2-SHDSL-LINE-MIB", "hdsl2ShdslSpanConfProfileEntry", "hdsl2ShdslSpanStatusEntry", "hdsl2ShdslEndpointCurrEntry")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
oacExpIMSystem, = mibBuilder.importSymbols("ONEACCESS-GLOBAL-REG", "oacExpIMSystem")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, IpAddress, Counter64, Bits, ObjectIdentity, Counter32, TimeTicks, Unsigned32, Gauge32, iso, ModuleIdentity, Integer32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "IpAddress", "Counter64", "Bits", "ObjectIdentity", "Counter32", "TimeTicks", "Unsigned32", "Gauge32", "iso", "ModuleIdentity", "Integer32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
oacSHDSLMIBModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3))
oacSHDSLMIBModule.setRevisions(('2011-06-15 00:00', '2010-08-20 00:01', '2010-07-30 00:01', '2010-07-08 00:01',))
if mibBuilder.loadTexts: oacSHDSLMIBModule.setLastUpdated('201106150000Z')
if mibBuilder.loadTexts: oacSHDSLMIBModule.setOrganization(' OneAccess ')
oacSHDSLObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1))
oacSHDSLSpanStatusTable = MibTable((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 2), )
if mibBuilder.loadTexts: oacSHDSLSpanStatusTable.setStatus('current')
oacSHDSLSpanStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 2, 1), )
hdsl2ShdslSpanStatusEntry.registerAugmentions(("ONEACCESS-SHDSL-MIB", "oacSHDSLSpanStatusEntry"))
oacSHDSLSpanStatusEntry.setIndexNames(*hdsl2ShdslSpanStatusEntry.getIndexNames())
if mibBuilder.loadTexts: oacSHDSLSpanStatusEntry.setStatus('current')
oacSHDSLSpanStatusUpDown = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 2, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacSHDSLSpanStatusUpDown.setStatus('current')
oacSHDSLSpanStatusCurrStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 2, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(30, 30)).setFixedLength(30)).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacSHDSLSpanStatusCurrStatus.setStatus('current')
oacSHDSLSpanStatusCurrShowtimeStart = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacSHDSLSpanStatusCurrShowtimeStart.setStatus('current')
oacSHDSLSpanStatusCurrCellDelin = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacSHDSLSpanStatusCurrCellDelin.setStatus('current')
oacSHDSLSpanStatusCurrCRCanomalies = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacSHDSLSpanStatusCurrCRCanomalies.setStatus('current')
oacSHDSLSpanStatusCurrHECErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacSHDSLSpanStatusCurrHECErrors.setStatus('current')
oacSHDSLSpanStatusCurrRxCells = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacSHDSLSpanStatusCurrRxCells.setStatus('current')
oacSHDSLSpanStatusCurrTxCells = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacSHDSLSpanStatusCurrTxCells.setStatus('current')
oacSHDSLSpanStatusCurrRxDrops = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacSHDSLSpanStatusCurrRxDrops.setStatus('current')
oacSHDSLSpanStatusCurrES = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacSHDSLSpanStatusCurrES.setStatus('current')
oacSHDSLSpanStatusCurrSES = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 2, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacSHDSLSpanStatusCurrSES.setStatus('current')
oacSHDSLSpanStatusCurrLOSWS = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 2, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacSHDSLSpanStatusCurrLOSWS.setStatus('current')
oacSHDSLSpanStatusCurrUAS = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 2, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacSHDSLSpanStatusCurrUAS.setStatus('current')
oacSHDSLSpanStatusCurrConstellation = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 2, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2, 3))).clone(namedValues=NamedValues(("tcPam16", 2), ("tcPam32", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacSHDSLSpanStatusCurrConstellation.setStatus('current')
oacSHDSLEndpointCurrTable = MibTable((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 5), )
if mibBuilder.loadTexts: oacSHDSLEndpointCurrTable.setStatus('current')
oacSHDSLEndpointCurrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 5, 1), )
hdsl2ShdslEndpointCurrEntry.registerAugmentions(("ONEACCESS-SHDSL-MIB", "oacSHDSLEndpointCurrEntry"))
oacSHDSLEndpointCurrEntry.setIndexNames(*hdsl2ShdslEndpointCurrEntry.getIndexNames())
if mibBuilder.loadTexts: oacSHDSLEndpointCurrEntry.setStatus('current')
oacSHDSLEndpointCurrAtn = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1270, 1280))).setUnits('dB/10').setMaxAccess("readonly")
if mibBuilder.loadTexts: oacSHDSLEndpointCurrAtn.setStatus('current')
oacSHDSLEndpointCurrSnrMgn = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 5, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1270, 1280))).setUnits('dB/10').setMaxAccess("readonly")
if mibBuilder.loadTexts: oacSHDSLEndpointCurrSnrMgn.setStatus('current')
oacSHDSLEndpointCurrTxPwr = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 5, 1, 3), Integer32()).setUnits('dB/10').setMaxAccess("readonly")
if mibBuilder.loadTexts: oacSHDSLEndpointCurrTxPwr.setStatus('current')
oacSHDSLEndpointCurrRxGain = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 5, 1, 4), Integer32()).setUnits('dB/10').setMaxAccess("readonly")
if mibBuilder.loadTexts: oacSHDSLEndpointCurrRxGain.setStatus('current')
oacSHDSLEndpointCurrMaxAttainableLineRate = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 5, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacSHDSLEndpointCurrMaxAttainableLineRate.setStatus('current')
oacSHDSLEndpointCurrCommands = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 5, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacSHDSLEndpointCurrCommands.setStatus('current')
oacSHDSLEndpointCurrResponses = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 5, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacSHDSLEndpointCurrResponses.setStatus('current')
oacSHDSLEndpointCurrdiscardedCommands = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 5, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacSHDSLEndpointCurrdiscardedCommands.setStatus('current')
oacSHDSLEndpointCurrerroredCommands = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 5, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacSHDSLEndpointCurrerroredCommands.setStatus('current')
oacSHDSLEndpointCurrReceivedFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 5, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacSHDSLEndpointCurrReceivedFrames.setStatus('current')
oacSHDSLEndpointCurrBadTransparency = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 5, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacSHDSLEndpointCurrBadTransparency.setStatus('current')
oacSHDSLEndpointCurrBadFCS = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 5, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacSHDSLEndpointCurrBadFCS.setStatus('current')
oacSHDSLEndpointCurrEOCStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 5, 1, 13), OctetString().subtype(subtypeSpec=ValueSizeConstraint(50, 50)).setFixedLength(50)).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacSHDSLEndpointCurrEOCStatus.setStatus('current')
oacSHDSLEndpointCurrretrainTable = MibTable((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 7), )
if mibBuilder.loadTexts: oacSHDSLEndpointCurrretrainTable.setStatus('current')
oacSHDSLEndpointCurrretrainEntry = MibTableRow((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 7, 1), )
hdsl2ShdslEndpointCurrEntry.registerAugmentions(("ONEACCESS-SHDSL-MIB", "oacSHDSLEndpointCurrretrainEntry"))
oacSHDSLEndpointCurrretrainEntry.setIndexNames(*hdsl2ShdslEndpointCurrEntry.getIndexNames())
if mibBuilder.loadTexts: oacSHDSLEndpointCurrretrainEntry.setStatus('current')
oacSHDSLEndpointCurrretrainSQPAIR = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 7, 1, 1), Integer32()).setUnits('SQPAIR').setMaxAccess("readonly")
if mibBuilder.loadTexts: oacSHDSLEndpointCurrretrainSQPAIR.setStatus('current')
oacSHDSLEndpointCurrretrainSQLINE = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 7, 1, 2), Integer32()).setUnits('SQLINE').setMaxAccess("readonly")
if mibBuilder.loadTexts: oacSHDSLEndpointCurrretrainSQLINE.setStatus('current')
oacSHDSLEndpointCurrretrainCRCPAIR = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 7, 1, 3), Integer32()).setUnits('CRCPAIR').setMaxAccess("readonly")
if mibBuilder.loadTexts: oacSHDSLEndpointCurrretrainCRCPAIR.setStatus('current')
oacSHDSLEndpointCurrretrainCRCLINE = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 7, 1, 4), Integer32()).setUnits('CRCLINE').setMaxAccess("readonly")
if mibBuilder.loadTexts: oacSHDSLEndpointCurrretrainCRCLINE.setStatus('current')
oacSHDSLEndpointCurrretrainFsyncPAIR = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 7, 1, 5), Integer32()).setUnits('FsyncPAIR').setMaxAccess("readonly")
if mibBuilder.loadTexts: oacSHDSLEndpointCurrretrainFsyncPAIR.setStatus('current')
oacSHDSLEndpointCurrretrainFsyncLINE = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 7, 1, 6), Integer32()).setUnits('FsyncLINE').setMaxAccess("readonly")
if mibBuilder.loadTexts: oacSHDSLEndpointCurrretrainFsyncLINE.setStatus('current')
oacSHDSLEndpointCurrretrainFSyncSQPAIR = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 7, 1, 7), Integer32()).setUnits('FSync&SQPAIR').setMaxAccess("readonly")
if mibBuilder.loadTexts: oacSHDSLEndpointCurrretrainFSyncSQPAIR.setStatus('current')
oacSHDSLEndpointCurrretrainFSyncSQLINE = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 7, 1, 8), Integer32()).setUnits('FSync&SQLINE').setMaxAccess("readonly")
if mibBuilder.loadTexts: oacSHDSLEndpointCurrretrainFSyncSQLINE.setStatus('current')
oacSHDSLTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 2))
oacSHDSLTrapPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 2, 0))
oacSHDSLHardDownTrap = NotificationType((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 2, 0, 1))
if mibBuilder.loadTexts: oacSHDSLHardDownTrap.setStatus('current')
oacSHDSLSpanConfProfileTable = MibTable((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 10), )
if mibBuilder.loadTexts: oacSHDSLSpanConfProfileTable.setStatus('current')
oacSHDSLSpanConfProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 10, 1), )
hdsl2ShdslSpanConfProfileEntry.registerAugmentions(("ONEACCESS-SHDSL-MIB", "oacSHDSLSpanConfProfileEntry"))
oacSHDSLSpanConfProfileEntry.setIndexNames(*hdsl2ShdslSpanConfProfileEntry.getIndexNames())
if mibBuilder.loadTexts: oacSHDSLSpanConfProfileEntry.setStatus('current')
oacSHDSLSpanConfProfileConstellation = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 10, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("auto", 1), ("tcPam16", 2), ("tcPam32", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacSHDSLSpanConfProfileConstellation.setStatus('current')
oacSHDSLSpanConfProfileAutoConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 10, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacSHDSLSpanConfProfileAutoConfig.setStatus('current')
oacSHDSLSpanConfProfileCaplist = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 10, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("newstyle", 1), ("oldstyle", 2), ("auto", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacSHDSLSpanConfProfileCaplist.setStatus('current')
oacSHDSLSpanConfProfileEfmAggregation = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 10, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("disabled", 1), ("auto", 2), ("negotiated", 3), ("static", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacSHDSLSpanConfProfileEfmAggregation.setStatus('current')
oacSHDSLSpanConfProfileCrcCheck = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 10, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 30))).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacSHDSLSpanConfProfileCrcCheck.setStatus('current')
oacSHDSLSpanConfProfileMeansqCheck = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 10, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 30))).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacSHDSLSpanConfProfileMeansqCheck.setStatus('current')
oacSHDSLSpanConfProfileMeansqThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 10, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2, 10))).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacSHDSLSpanConfProfileMeansqThreshold.setStatus('current')
oacSHDSLSpanConfProfileLineProbing = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 10, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("adaptive", 1), ("normal", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacSHDSLSpanConfProfileLineProbing.setStatus('current')
oacSHDSLSpanConfProfileEocManagement = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 10, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oacSHDSLSpanConfProfileEocManagement.setStatus('current')
oacSHDSLSpanConfProfileEocStatusPollDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 10, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 29))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: oacSHDSLSpanConfProfileEocStatusPollDelay.setStatus('current')
oacSHDSLSpanConfProfileEocStatusPollInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3, 3, 1, 10, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(30, 30), ValueRangeConstraint(60, 60), ValueRangeConstraint(90, 90), ValueRangeConstraint(120, 120), )).clone(30)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: oacSHDSLSpanConfProfileEocStatusPollInterval.setStatus('current')
mibBuilder.exportSymbols("ONEACCESS-SHDSL-MIB", oacSHDSLSpanStatusCurrSES=oacSHDSLSpanStatusCurrSES, oacSHDSLSpanConfProfileMeansqCheck=oacSHDSLSpanConfProfileMeansqCheck, oacSHDSLEndpointCurrEOCStatus=oacSHDSLEndpointCurrEOCStatus, oacSHDSLEndpointCurrretrainSQLINE=oacSHDSLEndpointCurrretrainSQLINE, oacSHDSLSpanStatusCurrShowtimeStart=oacSHDSLSpanStatusCurrShowtimeStart, oacSHDSLEndpointCurrBadFCS=oacSHDSLEndpointCurrBadFCS, oacSHDSLSpanStatusCurrUAS=oacSHDSLSpanStatusCurrUAS, oacSHDSLSpanStatusCurrES=oacSHDSLSpanStatusCurrES, oacSHDSLSpanStatusCurrRxCells=oacSHDSLSpanStatusCurrRxCells, oacSHDSLSpanConfProfileMeansqThreshold=oacSHDSLSpanConfProfileMeansqThreshold, oacSHDSLTrapPrefix=oacSHDSLTrapPrefix, oacSHDSLEndpointCurrretrainTable=oacSHDSLEndpointCurrretrainTable, oacSHDSLSpanStatusCurrHECErrors=oacSHDSLSpanStatusCurrHECErrors, oacSHDSLEndpointCurrretrainFsyncPAIR=oacSHDSLEndpointCurrretrainFsyncPAIR, oacSHDSLSpanStatusCurrConstellation=oacSHDSLSpanStatusCurrConstellation, oacSHDSLSpanConfProfileEocStatusPollDelay=oacSHDSLSpanConfProfileEocStatusPollDelay, oacSHDSLSpanConfProfileEocStatusPollInterval=oacSHDSLSpanConfProfileEocStatusPollInterval, oacSHDSLEndpointCurrCommands=oacSHDSLEndpointCurrCommands, oacSHDSLEndpointCurrretrainFsyncLINE=oacSHDSLEndpointCurrretrainFsyncLINE, oacSHDSLEndpointCurrTable=oacSHDSLEndpointCurrTable, oacSHDSLSpanStatusEntry=oacSHDSLSpanStatusEntry, oacSHDSLSpanConfProfileEocManagement=oacSHDSLSpanConfProfileEocManagement, oacSHDSLEndpointCurrEntry=oacSHDSLEndpointCurrEntry, oacSHDSLEndpointCurrResponses=oacSHDSLEndpointCurrResponses, oacSHDSLSpanStatusCurrCellDelin=oacSHDSLSpanStatusCurrCellDelin, oacSHDSLEndpointCurrBadTransparency=oacSHDSLEndpointCurrBadTransparency, oacSHDSLSpanConfProfileEfmAggregation=oacSHDSLSpanConfProfileEfmAggregation, oacSHDSLEndpointCurrretrainFSyncSQLINE=oacSHDSLEndpointCurrretrainFSyncSQLINE, oacSHDSLEndpointCurrRxGain=oacSHDSLEndpointCurrRxGain, oacSHDSLSpanStatusUpDown=oacSHDSLSpanStatusUpDown, PYSNMP_MODULE_ID=oacSHDSLMIBModule, oacSHDSLHardDownTrap=oacSHDSLHardDownTrap, oacSHDSLSpanConfProfileLineProbing=oacSHDSLSpanConfProfileLineProbing, oacSHDSLEndpointCurrretrainEntry=oacSHDSLEndpointCurrretrainEntry, oacSHDSLEndpointCurrTxPwr=oacSHDSLEndpointCurrTxPwr, oacSHDSLEndpointCurrdiscardedCommands=oacSHDSLEndpointCurrdiscardedCommands, oacSHDSLTraps=oacSHDSLTraps, oacSHDSLEndpointCurrReceivedFrames=oacSHDSLEndpointCurrReceivedFrames, oacSHDSLSpanConfProfileEntry=oacSHDSLSpanConfProfileEntry, oacSHDSLObjects=oacSHDSLObjects, oacSHDSLEndpointCurrerroredCommands=oacSHDSLEndpointCurrerroredCommands, oacSHDSLSpanStatusCurrRxDrops=oacSHDSLSpanStatusCurrRxDrops, oacSHDSLSpanConfProfileCaplist=oacSHDSLSpanConfProfileCaplist, oacSHDSLEndpointCurrretrainSQPAIR=oacSHDSLEndpointCurrretrainSQPAIR, oacSHDSLSpanConfProfileTable=oacSHDSLSpanConfProfileTable, oacSHDSLSpanStatusCurrCRCanomalies=oacSHDSLSpanStatusCurrCRCanomalies, oacSHDSLEndpointCurrretrainCRCPAIR=oacSHDSLEndpointCurrretrainCRCPAIR, oacSHDSLEndpointCurrMaxAttainableLineRate=oacSHDSLEndpointCurrMaxAttainableLineRate, oacSHDSLEndpointCurrAtn=oacSHDSLEndpointCurrAtn, oacSHDSLEndpointCurrretrainCRCLINE=oacSHDSLEndpointCurrretrainCRCLINE, oacSHDSLSpanConfProfileCrcCheck=oacSHDSLSpanConfProfileCrcCheck, oacSHDSLSpanStatusCurrTxCells=oacSHDSLSpanStatusCurrTxCells, oacSHDSLSpanConfProfileConstellation=oacSHDSLSpanConfProfileConstellation, oacSHDSLSpanStatusCurrLOSWS=oacSHDSLSpanStatusCurrLOSWS, oacSHDSLEndpointCurrSnrMgn=oacSHDSLEndpointCurrSnrMgn, oacSHDSLSpanStatusCurrStatus=oacSHDSLSpanStatusCurrStatus, oacSHDSLMIBModule=oacSHDSLMIBModule, oacSHDSLEndpointCurrretrainFSyncSQPAIR=oacSHDSLEndpointCurrretrainFSyncSQPAIR, oacSHDSLSpanConfProfileAutoConfig=oacSHDSLSpanConfProfileAutoConfig, oacSHDSLSpanStatusTable=oacSHDSLSpanStatusTable)
