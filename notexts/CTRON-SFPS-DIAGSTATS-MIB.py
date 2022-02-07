#
# PySNMP MIB module CTRON-SFPS-DIAGSTATS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-SFPS-DIAGSTATS-MIB
# Produced by pysmi-1.1.8 at Mon Feb  7 16:12:01 2022
# On host fv-az42-619 platform Linux version 5.11.0-1028-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
sfpsFloodCounters, sfpsFloodCountersReset, sfpsIsolatedSwitch, sfpsResetNVRAM = mibBuilder.importSymbols("CTRON-SFPS-INCLUDE-MIB", "sfpsFloodCounters", "sfpsFloodCountersReset", "sfpsIsolatedSwitch", "sfpsResetNVRAM")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, Bits, ObjectIdentity, ModuleIdentity, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, MibIdentifier, Counter64, Gauge32, Counter32, IpAddress, TimeTicks, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Bits", "ObjectIdentity", "ModuleIdentity", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "MibIdentifier", "Counter64", "Gauge32", "Counter32", "IpAddress", "TimeTicks", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("CTRON-SFPS-DIAGSTATS-MIB", SfpsAddress=SfpsAddress, sfpsFloodCountersMaxDropsTime=sfpsFloodCountersMaxDropsTime, sfpsFloodCountersTotalRunts=sfpsFloodCountersTotalRunts, sfpsFloodCountersSource=sfpsFloodCountersSource, sfpsFloodCountersLastDropTime=sfpsFloodCountersLastDropTime, sfpsFloodCountersNonNetPort=sfpsFloodCountersNonNetPort, sfpsFloodCountersLastSeqNum=sfpsFloodCountersLastSeqNum, sfpsIsolatedSwitchINBDropped=sfpsIsolatedSwitchINBDropped, sfpsFloodCountersTotalSelfOrig=sfpsFloodCountersTotalSelfOrig, sfpsFloodCountersTotalDropped=sfpsFloodCountersTotalDropped, sfpsFloodCountersResetReset=sfpsFloodCountersResetReset, sfpsIsolatedSwitchResetCounters=sfpsIsolatedSwitchResetCounters, sfpsResetNVRAMOnetoResetNvramAndRestoreIP=sfpsResetNVRAMOnetoResetNvramAndRestoreIP, sfpsResetNVRAMPercentNvramAvailable=sfpsResetNVRAMPercentNvramAvailable, sfpsFloodCountersNumFloods=sfpsFloodCountersNumFloods, sfpsFloodCountersMaxDrops=sfpsFloodCountersMaxDrops, sfpsResetNVRAMTotalNVRAM=sfpsResetNVRAMTotalNVRAM, sfpsResetNVRAMDelayTimer=sfpsResetNVRAMDelayTimer, sfpsFloodCountersNumDrops=sfpsFloodCountersNumDrops, sfpsIsolatedSwitchINBNotSent=sfpsIsolatedSwitchINBNotSent, sfpsIsolatedSwitchIsolatedSwitch=sfpsIsolatedSwitchIsolatedSwitch, sfpsFloodCountersTable=sfpsFloodCountersTable, sfpsFloodCountersEntry=sfpsFloodCountersEntry)
