#
# PySNMP MIB module STORMSHIELD-ASQ-STATS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/stormshield/STORMSHIELD-ASQ-STATS-MIB
# Produced by pysmi-1.1.8 at Sun Jan 16 00:44:32 2022
# On host fv-az42-839 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, Integer32, Counter32, NotificationType, MibIdentifier, Bits, Counter64, Unsigned32, Gauge32, TimeTicks, ModuleIdentity, IpAddress, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Integer32", "Counter32", "NotificationType", "MibIdentifier", "Bits", "Counter64", "Unsigned32", "Gauge32", "TimeTicks", "ModuleIdentity", "IpAddress", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
stormshieldMIB, = mibBuilder.importSymbols("STORMSHIELD-SMI-MIB", "stormshieldMIB")
snsASQStats = ModuleIdentity((1, 3, 6, 1, 4, 1, 11256, 1, 12))
snsASQStats.setRevisions(('2017-02-20 00:00',))
if mibBuilder.loadTexts: snsASQStats.setLastUpdated('201702200000Z')
if mibBuilder.loadTexts: snsASQStats.setOrganization('Stormshield')
snsASQStatsStateful = MibIdentifier((1, 3, 6, 1, 4, 1, 11256, 1, 12, 1))
snsASQStatsGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 11256, 1, 12, 2))
snsASQStatsStatefulPktBlocked = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsASQStatsStatefulPktBlocked.setStatus('current')
snsASQStatsStatefulPktBlockedAsync = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsASQStatsStatefulPktBlockedAsync.setStatus('current')
snsASQStatsStatefulPktBlockedSynProxy = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsASQStatsStatefulPktBlockedSynProxy.setStatus('current')
snsASQStatsStatefulPktAccepted = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsASQStatsStatefulPktAccepted.setStatus('current')
snsASQStatsStatefulLogged = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsASQStatsStatefulLogged.setStatus('current')
snsASQStatsStatefulLogOverflow = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsASQStatsStatefulLogOverflow.setStatus('current')
snsASQStatsStatefulFilterOverflow = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsASQStatsStatefulFilterOverflow.setStatus('current')
snsASQStatsStatefulAlarmOverflow = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsASQStatsStatefulAlarmOverflow.setStatus('current')
snsASQStatsStatefulSeismoFacts = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsASQStatsStatefulSeismoFacts.setStatus('current')
snsASQStatsStatefulSeismoOverflow = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsASQStatsStatefulSeismoOverflow.setStatus('current')
snsASQStatsStatefulMinorAlarm = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsASQStatsStatefulMinorAlarm.setStatus('current')
snsASQStatsStatefulMajorAlarm = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsASQStatsStatefulMajorAlarm.setStatus('current')
snsASQStatsStatefulPktFragmented = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsASQStatsStatefulPktFragmented.setStatus('current')
snsASQStatsStatefulInBytes = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 14), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsASQStatsStatefulInBytes.setStatus('current')
snsASQStatsStatefulOutBytes = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 15), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsASQStatsStatefulOutBytes.setStatus('current')
snsASQStatsStatefulNatFailures = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 16), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsASQStatsStatefulNatFailures.setStatus('current')
snsASQStatsStatefulFlowConflicts = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 17), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsASQStatsStatefulFlowConflicts.setStatus('current')
snsASQStatsStatefulFlowFailures = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 18), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsASQStatsStatefulFlowFailures.setStatus('current')
snsASQStatsStatefulInterfaceMute = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 19), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsASQStatsStatefulInterfaceMute.setStatus('current')
snsASQStatsStatefulTcpPkt = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 20), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsASQStatsStatefulTcpPkt.setStatus('current')
snsASQStatsStatefulTcpInBytes = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 21), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsASQStatsStatefulTcpInBytes.setStatus('current')
snsASQStatsStatefulTcpOutBytes = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 22), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsASQStatsStatefulTcpOutBytes.setStatus('current')
snsASQStatsStatefulTcpConn = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 23), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsASQStatsStatefulTcpConn.setStatus('current')
snsASQStatsStatefulTcpNatConnSrc = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 24), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsASQStatsStatefulTcpNatConnSrc.setStatus('current')
snsASQStatsStatefulTcpNatConnDst = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 25), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsASQStatsStatefulTcpNatConnDst.setStatus('current')
snsASQStatsStatefulTcpNoNatConnSrc = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 26), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsASQStatsStatefulTcpNoNatConnSrc.setStatus('current')
snsASQStatsStatefulTcpNoNatConnDst = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 27), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsASQStatsStatefulTcpNoNatConnDst.setStatus('current')
snsASQStatsStatefulTcpSmallWindowRst = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 28), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsASQStatsStatefulTcpSmallWindowRst.setStatus('current')
snsASQStatsStatefulTcpEmptyDupAckBlk = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 29), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsASQStatsStatefulTcpEmptyDupAckBlk.setStatus('current')
snsASQStatsStatefulUdpPkt = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 30), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsASQStatsStatefulUdpPkt.setStatus('current')
snsASQStatsStatefulUdpInBytes = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 31), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsASQStatsStatefulUdpInBytes.setStatus('current')
snsASQStatsStatefulUdpOutBytes = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 32), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsASQStatsStatefulUdpOutBytes.setStatus('current')
snsASQStatsStatefulUdpConn = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 33), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsASQStatsStatefulUdpConn.setStatus('current')
snsASQStatsStatefulUdpNatConnSrc = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 34), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsASQStatsStatefulUdpNatConnSrc.setStatus('current')
snsASQStatsStatefulUdpNatConnDst = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 35), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsASQStatsStatefulUdpNatConnDst.setStatus('current')
snsASQStatsStatefulUdpNoNatConnSrc = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 36), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsASQStatsStatefulUdpNoNatConnSrc.setStatus('current')
snsASQStatsStatefulUdpNoNatConnDst = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 37), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsASQStatsStatefulUdpNoNatConnDst.setStatus('current')
snsASQStatsStatefulIcmpPkt = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 38), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsASQStatsStatefulIcmpPkt.setStatus('current')
snsASQStatsStatefulIcmpInBytes = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 39), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsASQStatsStatefulIcmpInBytes.setStatus('current')
snsASQStatsStatefulIcmpOutBytes = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 40), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsASQStatsStatefulIcmpOutBytes.setStatus('current')
snsASQStatsStatefulHttpTimeoutRst = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 41), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsASQStatsStatefulHttpTimeoutRst.setStatus('current')
snsASQStatsStatefulNatUnusable = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 42), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsASQStatsStatefulNatUnusable.setStatus('current')
snsASQStatsGlobalTimeSinceReset = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 12, 2, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsASQStatsGlobalTimeSinceReset.setStatus('current')
mibBuilder.exportSymbols("STORMSHIELD-ASQ-STATS-MIB", snsASQStatsGlobalTimeSinceReset=snsASQStatsGlobalTimeSinceReset, snsASQStatsStatefulIcmpPkt=snsASQStatsStatefulIcmpPkt, snsASQStatsStatefulTcpNoNatConnSrc=snsASQStatsStatefulTcpNoNatConnSrc, snsASQStatsStatefulMajorAlarm=snsASQStatsStatefulMajorAlarm, snsASQStatsStatefulPktBlockedAsync=snsASQStatsStatefulPktBlockedAsync, snsASQStatsStatefulTcpOutBytes=snsASQStatsStatefulTcpOutBytes, snsASQStatsStatefulNatFailures=snsASQStatsStatefulNatFailures, snsASQStatsStatefulAlarmOverflow=snsASQStatsStatefulAlarmOverflow, snsASQStatsStatefulUdpOutBytes=snsASQStatsStatefulUdpOutBytes, snsASQStatsStatefulPktBlocked=snsASQStatsStatefulPktBlocked, snsASQStatsStatefulFilterOverflow=snsASQStatsStatefulFilterOverflow, snsASQStatsStatefulUdpNoNatConnDst=snsASQStatsStatefulUdpNoNatConnDst, snsASQStatsStatefulTcpEmptyDupAckBlk=snsASQStatsStatefulTcpEmptyDupAckBlk, snsASQStatsStatefulLogged=snsASQStatsStatefulLogged, snsASQStatsStatefulMinorAlarm=snsASQStatsStatefulMinorAlarm, snsASQStatsStatefulTcpInBytes=snsASQStatsStatefulTcpInBytes, snsASQStatsStatefulFlowConflicts=snsASQStatsStatefulFlowConflicts, snsASQStatsStatefulIcmpInBytes=snsASQStatsStatefulIcmpInBytes, snsASQStatsStatefulTcpNatConnSrc=snsASQStatsStatefulTcpNatConnSrc, snsASQStatsStatefulUdpNatConnSrc=snsASQStatsStatefulUdpNatConnSrc, snsASQStatsStatefulUdpNatConnDst=snsASQStatsStatefulUdpNatConnDst, snsASQStatsStatefulPktFragmented=snsASQStatsStatefulPktFragmented, snsASQStatsStatefulTcpNoNatConnDst=snsASQStatsStatefulTcpNoNatConnDst, PYSNMP_MODULE_ID=snsASQStats, snsASQStats=snsASQStats, snsASQStatsStatefulUdpInBytes=snsASQStatsStatefulUdpInBytes, snsASQStatsStatefulTcpNatConnDst=snsASQStatsStatefulTcpNatConnDst, snsASQStatsStatefulUdpNoNatConnSrc=snsASQStatsStatefulUdpNoNatConnSrc, snsASQStatsStatefulPktBlockedSynProxy=snsASQStatsStatefulPktBlockedSynProxy, snsASQStatsStatefulUdpConn=snsASQStatsStatefulUdpConn, snsASQStatsStatefulInterfaceMute=snsASQStatsStatefulInterfaceMute, snsASQStatsStatefulHttpTimeoutRst=snsASQStatsStatefulHttpTimeoutRst, snsASQStatsStatefulFlowFailures=snsASQStatsStatefulFlowFailures, snsASQStatsStatefulTcpPkt=snsASQStatsStatefulTcpPkt, snsASQStatsGlobal=snsASQStatsGlobal, snsASQStatsStatefulPktAccepted=snsASQStatsStatefulPktAccepted, snsASQStatsStatefulSeismoFacts=snsASQStatsStatefulSeismoFacts, snsASQStatsStatefulTcpConn=snsASQStatsStatefulTcpConn, snsASQStatsStatefulSeismoOverflow=snsASQStatsStatefulSeismoOverflow, snsASQStatsStatefulLogOverflow=snsASQStatsStatefulLogOverflow, snsASQStatsStatefulIcmpOutBytes=snsASQStatsStatefulIcmpOutBytes, snsASQStatsStatefulTcpSmallWindowRst=snsASQStatsStatefulTcpSmallWindowRst, snsASQStatsStatefulUdpPkt=snsASQStatsStatefulUdpPkt, snsASQStatsStatefulOutBytes=snsASQStatsStatefulOutBytes, snsASQStatsStateful=snsASQStatsStateful, snsASQStatsStatefulInBytes=snsASQStatsStatefulInBytes, snsASQStatsStatefulNatUnusable=snsASQStatsStatefulNatUnusable)
