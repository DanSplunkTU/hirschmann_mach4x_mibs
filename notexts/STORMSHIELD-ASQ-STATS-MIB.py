#
# PySNMP MIB module STORMSHIELD-ASQ-STATS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/stormshield/STORMSHIELD-ASQ-STATS-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:26:42 2022
# On host fv-az135-792 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter64, MibIdentifier, NotificationType, Gauge32, Unsigned32, TimeTicks, IpAddress, Counter32, iso, ModuleIdentity, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter64", "MibIdentifier", "NotificationType", "Gauge32", "Unsigned32", "TimeTicks", "IpAddress", "Counter32", "iso", "ModuleIdentity", "ObjectIdentity")
TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString")
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
mibBuilder.exportSymbols("STORMSHIELD-ASQ-STATS-MIB", snsASQStatsStatefulFlowConflicts=snsASQStatsStatefulFlowConflicts, snsASQStatsStatefulTcpNoNatConnDst=snsASQStatsStatefulTcpNoNatConnDst, snsASQStatsGlobalTimeSinceReset=snsASQStatsGlobalTimeSinceReset, snsASQStatsStatefulHttpTimeoutRst=snsASQStatsStatefulHttpTimeoutRst, snsASQStatsStatefulTcpNatConnSrc=snsASQStatsStatefulTcpNatConnSrc, snsASQStatsStatefulUdpInBytes=snsASQStatsStatefulUdpInBytes, snsASQStatsStatefulSeismoFacts=snsASQStatsStatefulSeismoFacts, snsASQStatsStatefulNatFailures=snsASQStatsStatefulNatFailures, snsASQStatsStatefulFlowFailures=snsASQStatsStatefulFlowFailures, snsASQStatsStatefulUdpPkt=snsASQStatsStatefulUdpPkt, snsASQStatsStatefulPktBlockedSynProxy=snsASQStatsStatefulPktBlockedSynProxy, snsASQStatsStatefulUdpConn=snsASQStatsStatefulUdpConn, snsASQStatsStatefulIcmpOutBytes=snsASQStatsStatefulIcmpOutBytes, snsASQStatsStatefulFilterOverflow=snsASQStatsStatefulFilterOverflow, snsASQStatsStatefulTcpNatConnDst=snsASQStatsStatefulTcpNatConnDst, snsASQStatsStatefulMinorAlarm=snsASQStatsStatefulMinorAlarm, snsASQStatsStatefulUdpNatConnDst=snsASQStatsStatefulUdpNatConnDst, snsASQStatsStateful=snsASQStatsStateful, snsASQStatsStatefulPktBlockedAsync=snsASQStatsStatefulPktBlockedAsync, snsASQStatsStatefulPktAccepted=snsASQStatsStatefulPktAccepted, snsASQStatsStatefulSeismoOverflow=snsASQStatsStatefulSeismoOverflow, snsASQStatsStatefulAlarmOverflow=snsASQStatsStatefulAlarmOverflow, snsASQStatsStatefulOutBytes=snsASQStatsStatefulOutBytes, PYSNMP_MODULE_ID=snsASQStats, snsASQStatsGlobal=snsASQStatsGlobal, snsASQStatsStatefulTcpNoNatConnSrc=snsASQStatsStatefulTcpNoNatConnSrc, snsASQStatsStatefulLogged=snsASQStatsStatefulLogged, snsASQStatsStatefulMajorAlarm=snsASQStatsStatefulMajorAlarm, snsASQStats=snsASQStats, snsASQStatsStatefulPktFragmented=snsASQStatsStatefulPktFragmented, snsASQStatsStatefulUdpNoNatConnDst=snsASQStatsStatefulUdpNoNatConnDst, snsASQStatsStatefulNatUnusable=snsASQStatsStatefulNatUnusable, snsASQStatsStatefulIcmpPkt=snsASQStatsStatefulIcmpPkt, snsASQStatsStatefulPktBlocked=snsASQStatsStatefulPktBlocked, snsASQStatsStatefulIcmpInBytes=snsASQStatsStatefulIcmpInBytes, snsASQStatsStatefulTcpPkt=snsASQStatsStatefulTcpPkt, snsASQStatsStatefulUdpNatConnSrc=snsASQStatsStatefulUdpNatConnSrc, snsASQStatsStatefulTcpEmptyDupAckBlk=snsASQStatsStatefulTcpEmptyDupAckBlk, snsASQStatsStatefulInBytes=snsASQStatsStatefulInBytes, snsASQStatsStatefulTcpInBytes=snsASQStatsStatefulTcpInBytes, snsASQStatsStatefulUdpNoNatConnSrc=snsASQStatsStatefulUdpNoNatConnSrc, snsASQStatsStatefulInterfaceMute=snsASQStatsStatefulInterfaceMute, snsASQStatsStatefulTcpConn=snsASQStatsStatefulTcpConn, snsASQStatsStatefulTcpSmallWindowRst=snsASQStatsStatefulTcpSmallWindowRst, snsASQStatsStatefulUdpOutBytes=snsASQStatsStatefulUdpOutBytes, snsASQStatsStatefulTcpOutBytes=snsASQStatsStatefulTcpOutBytes, snsASQStatsStatefulLogOverflow=snsASQStatsStatefulLogOverflow)
