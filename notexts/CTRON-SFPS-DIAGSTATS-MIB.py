#
# PySNMP MIB module CTRON-SFPS-DIAGSTATS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-SFPS-DIAGSTATS-MIB
# Produced by pysmi-1.1.8 at Sun Jan 16 00:36:31 2022
# On host fv-az42-839 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
sfpsIsolatedSwitch, sfpsFloodCounters, sfpsResetNVRAM, sfpsFloodCountersReset = mibBuilder.importSymbols("CTRON-SFPS-INCLUDE-MIB", "sfpsIsolatedSwitch", "sfpsFloodCounters", "sfpsResetNVRAM", "sfpsFloodCountersReset")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, ObjectIdentity, MibIdentifier, iso, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Bits, Counter64, ModuleIdentity, NotificationType, Counter32, Gauge32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "ObjectIdentity", "MibIdentifier", "iso", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Bits", "Counter64", "ModuleIdentity", "NotificationType", "Counter32", "Gauge32", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class SfpsAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

sfpsFloodCountersTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 2, 1, 1), )
if mibBuilder.loadTexts: sfpsFloodCountersTable.setStatus('mandatory')
sfpsFloodCountersEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 2, 1, 1, 1), ).setIndexNames((0, "CTRON-SFPS-DIAGSTATS-MIB", "sfpsFloodCountersSource"))
if mibBuilder.loadTexts: sfpsFloodCountersEntry.setStatus('mandatory')
sfpsFloodCountersSource = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 2, 1, 1, 1, 1), SfpsAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsFloodCountersSource.setStatus('mandatory')
sfpsFloodCountersNumFloods = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 2, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsFloodCountersNumFloods.setStatus('mandatory')
sfpsFloodCountersLastSeqNum = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 2, 1, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsFloodCountersLastSeqNum.setStatus('mandatory')
sfpsFloodCountersNumDrops = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 2, 1, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsFloodCountersNumDrops.setStatus('mandatory')
sfpsFloodCountersLastDropTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 2, 1, 1, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsFloodCountersLastDropTime.setStatus('mandatory')
sfpsFloodCountersMaxDrops = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 2, 1, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsFloodCountersMaxDrops.setStatus('mandatory')
sfpsFloodCountersMaxDropsTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 2, 1, 1, 1, 7), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsFloodCountersMaxDropsTime.setStatus('mandatory')
sfpsFloodCountersResetReset = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 2, 2, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsFloodCountersResetReset.setStatus('mandatory')
sfpsFloodCountersTotalDropped = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 2, 2, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsFloodCountersTotalDropped.setStatus('mandatory')
sfpsFloodCountersTotalRunts = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 2, 2, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsFloodCountersTotalRunts.setStatus('mandatory')
sfpsFloodCountersTotalSelfOrig = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 2, 2, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsFloodCountersTotalSelfOrig.setStatus('mandatory')
sfpsFloodCountersNonNetPort = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 2, 2, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsFloodCountersNonNetPort.setStatus('mandatory')
sfpsIsolatedSwitchIsolatedSwitch = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 2, 5, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("yes", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsIsolatedSwitchIsolatedSwitch.setStatus('mandatory')
sfpsIsolatedSwitchResetCounters = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 2, 5, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsIsolatedSwitchResetCounters.setStatus('mandatory')
sfpsIsolatedSwitchINBDropped = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 2, 5, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsIsolatedSwitchINBDropped.setStatus('mandatory')
sfpsIsolatedSwitchINBNotSent = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 2, 5, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsIsolatedSwitchINBNotSent.setStatus('mandatory')
sfpsResetNVRAMPercentNvramAvailable = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 3, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsResetNVRAMPercentNvramAvailable.setStatus('mandatory')
sfpsResetNVRAMTotalNVRAM = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 3, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsResetNVRAMTotalNVRAM.setStatus('mandatory')
sfpsResetNVRAMOnetoResetNvramAndRestoreIP = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 3, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsResetNVRAMOnetoResetNvramAndRestoreIP.setStatus('mandatory')
sfpsResetNVRAMDelayTimer = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 3, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsResetNVRAMDelayTimer.setStatus('mandatory')
mibBuilder.exportSymbols("CTRON-SFPS-DIAGSTATS-MIB", sfpsResetNVRAMDelayTimer=sfpsResetNVRAMDelayTimer, sfpsFloodCountersNonNetPort=sfpsFloodCountersNonNetPort, sfpsIsolatedSwitchIsolatedSwitch=sfpsIsolatedSwitchIsolatedSwitch, sfpsFloodCountersTable=sfpsFloodCountersTable, sfpsFloodCountersLastDropTime=sfpsFloodCountersLastDropTime, sfpsFloodCountersTotalDropped=sfpsFloodCountersTotalDropped, sfpsResetNVRAMPercentNvramAvailable=sfpsResetNVRAMPercentNvramAvailable, sfpsFloodCountersResetReset=sfpsFloodCountersResetReset, SfpsAddress=SfpsAddress, sfpsResetNVRAMTotalNVRAM=sfpsResetNVRAMTotalNVRAM, sfpsResetNVRAMOnetoResetNvramAndRestoreIP=sfpsResetNVRAMOnetoResetNvramAndRestoreIP, sfpsFloodCountersNumDrops=sfpsFloodCountersNumDrops, sfpsFloodCountersMaxDropsTime=sfpsFloodCountersMaxDropsTime, sfpsFloodCountersTotalSelfOrig=sfpsFloodCountersTotalSelfOrig, sfpsFloodCountersTotalRunts=sfpsFloodCountersTotalRunts, sfpsFloodCountersLastSeqNum=sfpsFloodCountersLastSeqNum, sfpsIsolatedSwitchResetCounters=sfpsIsolatedSwitchResetCounters, sfpsIsolatedSwitchINBDropped=sfpsIsolatedSwitchINBDropped, sfpsFloodCountersMaxDrops=sfpsFloodCountersMaxDrops, sfpsFloodCountersEntry=sfpsFloodCountersEntry, sfpsFloodCountersNumFloods=sfpsFloodCountersNumFloods, sfpsIsolatedSwitchINBNotSent=sfpsIsolatedSwitchINBNotSent, sfpsFloodCountersSource=sfpsFloodCountersSource)
