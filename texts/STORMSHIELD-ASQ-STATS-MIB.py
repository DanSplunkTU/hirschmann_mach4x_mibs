#
# PySNMP MIB module STORMSHIELD-ASQ-STATS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/stormshield/STORMSHIELD-ASQ-STATS-MIB
# Produced by pysmi-1.1.3 at Sun Nov 21 00:37:31 2021
# On host fv-az39-63 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, ModuleIdentity, IpAddress, Gauge32, Counter64, TimeTicks, MibIdentifier, Unsigned32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Bits, iso, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "ModuleIdentity", "IpAddress", "Gauge32", "Counter64", "TimeTicks", "MibIdentifier", "Unsigned32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Bits", "iso", "ObjectIdentity")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
stormshieldMIB, = mibBuilder.importSymbols("STORMSHIELD-SMI-MIB", "stormshieldMIB")
snsASQStats = ModuleIdentity((1, 3, 6, 1, 4, 1, 11256, 1, 12))
snsASQStats.setRevisions(('2017-02-20 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: snsASQStats.setRevisionsDescriptions(('Initial',))
if mibBuilder.loadTexts: snsASQStats.setLastUpdated('201702200000Z')
if mibBuilder.loadTexts: snsASQStats.setOrganization('Stormshield')
if mibBuilder.loadTexts: snsASQStats.setContactInfo('Customer Support\n\n         22 rue du Gouverneur General Eboue\n         92130 Issy-les-Moulineaux\n         FRANCE\n\n         Tel: +33 (0)9 69 32 96 29\n         E-mail: support@stormshield.eu\n         http://www.stormshield.eu')
if mibBuilder.loadTexts: snsASQStats.setDescription('stormshield ASQ Statistics')
snsASQStatsStateful = MibIdentifier((1, 3, 6, 1, 4, 1, 11256, 1, 12, 1))
snsASQStatsGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 11256, 1, 12, 2))
snsASQStatsStatefulPktBlocked = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsASQStatsStatefulPktBlocked.setStatus('current')
if mibBuilder.loadTexts: snsASQStatsStatefulPktBlocked.setDescription('')
snsASQStatsStatefulPktBlockedAsync = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsASQStatsStatefulPktBlockedAsync.setStatus('current')
if mibBuilder.loadTexts: snsASQStatsStatefulPktBlockedAsync.setDescription('')
snsASQStatsStatefulPktBlockedSynProxy = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsASQStatsStatefulPktBlockedSynProxy.setStatus('current')
if mibBuilder.loadTexts: snsASQStatsStatefulPktBlockedSynProxy.setDescription('')
snsASQStatsStatefulPktAccepted = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsASQStatsStatefulPktAccepted.setStatus('current')
if mibBuilder.loadTexts: snsASQStatsStatefulPktAccepted.setDescription('')
snsASQStatsStatefulLogged = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsASQStatsStatefulLogged.setStatus('current')
if mibBuilder.loadTexts: snsASQStatsStatefulLogged.setDescription('')
snsASQStatsStatefulLogOverflow = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsASQStatsStatefulLogOverflow.setStatus('current')
if mibBuilder.loadTexts: snsASQStatsStatefulLogOverflow.setDescription('')
snsASQStatsStatefulFilterOverflow = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsASQStatsStatefulFilterOverflow.setStatus('current')
if mibBuilder.loadTexts: snsASQStatsStatefulFilterOverflow.setDescription('')
snsASQStatsStatefulAlarmOverflow = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsASQStatsStatefulAlarmOverflow.setStatus('current')
if mibBuilder.loadTexts: snsASQStatsStatefulAlarmOverflow.setDescription('')
snsASQStatsStatefulSeismoFacts = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsASQStatsStatefulSeismoFacts.setStatus('current')
if mibBuilder.loadTexts: snsASQStatsStatefulSeismoFacts.setDescription('')
snsASQStatsStatefulSeismoOverflow = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsASQStatsStatefulSeismoOverflow.setStatus('current')
if mibBuilder.loadTexts: snsASQStatsStatefulSeismoOverflow.setDescription('')
snsASQStatsStatefulMinorAlarm = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsASQStatsStatefulMinorAlarm.setStatus('current')
if mibBuilder.loadTexts: snsASQStatsStatefulMinorAlarm.setDescription('')
snsASQStatsStatefulMajorAlarm = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsASQStatsStatefulMajorAlarm.setStatus('current')
if mibBuilder.loadTexts: snsASQStatsStatefulMajorAlarm.setDescription('')
snsASQStatsStatefulPktFragmented = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsASQStatsStatefulPktFragmented.setStatus('current')
if mibBuilder.loadTexts: snsASQStatsStatefulPktFragmented.setDescription('')
snsASQStatsStatefulInBytes = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 14), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsASQStatsStatefulInBytes.setStatus('current')
if mibBuilder.loadTexts: snsASQStatsStatefulInBytes.setDescription('Incoming traffic')
snsASQStatsStatefulOutBytes = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 15), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsASQStatsStatefulOutBytes.setStatus('current')
if mibBuilder.loadTexts: snsASQStatsStatefulOutBytes.setDescription('Outgoing traffic')
snsASQStatsStatefulNatFailures = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 16), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsASQStatsStatefulNatFailures.setStatus('current')
if mibBuilder.loadTexts: snsASQStatsStatefulNatFailures.setDescription('')
snsASQStatsStatefulFlowConflicts = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 17), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsASQStatsStatefulFlowConflicts.setStatus('current')
if mibBuilder.loadTexts: snsASQStatsStatefulFlowConflicts.setDescription('')
snsASQStatsStatefulFlowFailures = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 18), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsASQStatsStatefulFlowFailures.setStatus('current')
if mibBuilder.loadTexts: snsASQStatsStatefulFlowFailures.setDescription('')
snsASQStatsStatefulInterfaceMute = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 19), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsASQStatsStatefulInterfaceMute.setStatus('current')
if mibBuilder.loadTexts: snsASQStatsStatefulInterfaceMute.setDescription('')
snsASQStatsStatefulTcpPkt = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 20), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsASQStatsStatefulTcpPkt.setStatus('current')
if mibBuilder.loadTexts: snsASQStatsStatefulTcpPkt.setDescription('')
snsASQStatsStatefulTcpInBytes = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 21), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsASQStatsStatefulTcpInBytes.setStatus('current')
if mibBuilder.loadTexts: snsASQStatsStatefulTcpInBytes.setDescription('Incoming TCP traffic')
snsASQStatsStatefulTcpOutBytes = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 22), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsASQStatsStatefulTcpOutBytes.setStatus('current')
if mibBuilder.loadTexts: snsASQStatsStatefulTcpOutBytes.setDescription('Outgoing TCP traffic')
snsASQStatsStatefulTcpConn = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 23), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsASQStatsStatefulTcpConn.setStatus('current')
if mibBuilder.loadTexts: snsASQStatsStatefulTcpConn.setDescription('')
snsASQStatsStatefulTcpNatConnSrc = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 24), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsASQStatsStatefulTcpNatConnSrc.setStatus('current')
if mibBuilder.loadTexts: snsASQStatsStatefulTcpNatConnSrc.setDescription('')
snsASQStatsStatefulTcpNatConnDst = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 25), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsASQStatsStatefulTcpNatConnDst.setStatus('current')
if mibBuilder.loadTexts: snsASQStatsStatefulTcpNatConnDst.setDescription('')
snsASQStatsStatefulTcpNoNatConnSrc = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 26), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsASQStatsStatefulTcpNoNatConnSrc.setStatus('current')
if mibBuilder.loadTexts: snsASQStatsStatefulTcpNoNatConnSrc.setDescription('')
snsASQStatsStatefulTcpNoNatConnDst = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 27), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsASQStatsStatefulTcpNoNatConnDst.setStatus('current')
if mibBuilder.loadTexts: snsASQStatsStatefulTcpNoNatConnDst.setDescription('')
snsASQStatsStatefulTcpSmallWindowRst = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 28), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsASQStatsStatefulTcpSmallWindowRst.setStatus('current')
if mibBuilder.loadTexts: snsASQStatsStatefulTcpSmallWindowRst.setDescription('')
snsASQStatsStatefulTcpEmptyDupAckBlk = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 29), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsASQStatsStatefulTcpEmptyDupAckBlk.setStatus('current')
if mibBuilder.loadTexts: snsASQStatsStatefulTcpEmptyDupAckBlk.setDescription('')
snsASQStatsStatefulUdpPkt = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 30), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsASQStatsStatefulUdpPkt.setStatus('current')
if mibBuilder.loadTexts: snsASQStatsStatefulUdpPkt.setDescription('')
snsASQStatsStatefulUdpInBytes = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 31), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsASQStatsStatefulUdpInBytes.setStatus('current')
if mibBuilder.loadTexts: snsASQStatsStatefulUdpInBytes.setDescription('Incoming UDP traffic')
snsASQStatsStatefulUdpOutBytes = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 32), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsASQStatsStatefulUdpOutBytes.setStatus('current')
if mibBuilder.loadTexts: snsASQStatsStatefulUdpOutBytes.setDescription('Outgoing UDP traffic')
snsASQStatsStatefulUdpConn = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 33), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsASQStatsStatefulUdpConn.setStatus('current')
if mibBuilder.loadTexts: snsASQStatsStatefulUdpConn.setDescription('')
snsASQStatsStatefulUdpNatConnSrc = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 34), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsASQStatsStatefulUdpNatConnSrc.setStatus('current')
if mibBuilder.loadTexts: snsASQStatsStatefulUdpNatConnSrc.setDescription('')
snsASQStatsStatefulUdpNatConnDst = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 35), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsASQStatsStatefulUdpNatConnDst.setStatus('current')
if mibBuilder.loadTexts: snsASQStatsStatefulUdpNatConnDst.setDescription('')
snsASQStatsStatefulUdpNoNatConnSrc = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 36), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsASQStatsStatefulUdpNoNatConnSrc.setStatus('current')
if mibBuilder.loadTexts: snsASQStatsStatefulUdpNoNatConnSrc.setDescription('')
snsASQStatsStatefulUdpNoNatConnDst = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 37), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsASQStatsStatefulUdpNoNatConnDst.setStatus('current')
if mibBuilder.loadTexts: snsASQStatsStatefulUdpNoNatConnDst.setDescription('')
snsASQStatsStatefulIcmpPkt = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 38), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsASQStatsStatefulIcmpPkt.setStatus('current')
if mibBuilder.loadTexts: snsASQStatsStatefulIcmpPkt.setDescription('')
snsASQStatsStatefulIcmpInBytes = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 39), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsASQStatsStatefulIcmpInBytes.setStatus('current')
if mibBuilder.loadTexts: snsASQStatsStatefulIcmpInBytes.setDescription('Incoming ICMP traffic')
snsASQStatsStatefulIcmpOutBytes = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 40), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsASQStatsStatefulIcmpOutBytes.setStatus('current')
if mibBuilder.loadTexts: snsASQStatsStatefulIcmpOutBytes.setDescription('Outgoing ICMP traffic')
snsASQStatsStatefulHttpTimeoutRst = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 41), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsASQStatsStatefulHttpTimeoutRst.setStatus('current')
if mibBuilder.loadTexts: snsASQStatsStatefulHttpTimeoutRst.setDescription('')
snsASQStatsStatefulNatUnusable = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 12, 1, 42), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsASQStatsStatefulNatUnusable.setStatus('current')
if mibBuilder.loadTexts: snsASQStatsStatefulNatUnusable.setDescription('')
snsASQStatsGlobalTimeSinceReset = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 12, 2, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsASQStatsGlobalTimeSinceReset.setStatus('current')
if mibBuilder.loadTexts: snsASQStatsGlobalTimeSinceReset.setDescription('Time elapsed since last reset in seconds')
mibBuilder.exportSymbols("STORMSHIELD-ASQ-STATS-MIB", snsASQStatsStatefulUdpOutBytes=snsASQStatsStatefulUdpOutBytes, snsASQStatsStatefulOutBytes=snsASQStatsStatefulOutBytes, snsASQStatsStatefulTcpOutBytes=snsASQStatsStatefulTcpOutBytes, snsASQStatsStatefulPktAccepted=snsASQStatsStatefulPktAccepted, snsASQStatsStatefulFilterOverflow=snsASQStatsStatefulFilterOverflow, snsASQStatsStatefulTcpNatConnSrc=snsASQStatsStatefulTcpNatConnSrc, snsASQStatsStatefulUdpNatConnSrc=snsASQStatsStatefulUdpNatConnSrc, snsASQStatsStatefulNatFailures=snsASQStatsStatefulNatFailures, snsASQStatsStatefulTcpEmptyDupAckBlk=snsASQStatsStatefulTcpEmptyDupAckBlk, snsASQStatsStatefulIcmpInBytes=snsASQStatsStatefulIcmpInBytes, snsASQStatsStatefulUdpNoNatConnSrc=snsASQStatsStatefulUdpNoNatConnSrc, snsASQStatsStatefulTcpNoNatConnDst=snsASQStatsStatefulTcpNoNatConnDst, snsASQStatsStatefulTcpNoNatConnSrc=snsASQStatsStatefulTcpNoNatConnSrc, snsASQStatsStatefulPktFragmented=snsASQStatsStatefulPktFragmented, snsASQStatsStatefulNatUnusable=snsASQStatsStatefulNatUnusable, snsASQStatsStatefulInterfaceMute=snsASQStatsStatefulInterfaceMute, snsASQStatsStatefulInBytes=snsASQStatsStatefulInBytes, snsASQStatsStatefulAlarmOverflow=snsASQStatsStatefulAlarmOverflow, snsASQStatsStatefulSeismoFacts=snsASQStatsStatefulSeismoFacts, snsASQStatsStatefulTcpConn=snsASQStatsStatefulTcpConn, snsASQStatsStatefulIcmpOutBytes=snsASQStatsStatefulIcmpOutBytes, snsASQStatsGlobalTimeSinceReset=snsASQStatsGlobalTimeSinceReset, snsASQStatsStatefulPktBlocked=snsASQStatsStatefulPktBlocked, snsASQStatsStatefulIcmpPkt=snsASQStatsStatefulIcmpPkt, snsASQStatsStatefulFlowFailures=snsASQStatsStatefulFlowFailures, snsASQStatsStatefulPktBlockedAsync=snsASQStatsStatefulPktBlockedAsync, snsASQStatsStatefulSeismoOverflow=snsASQStatsStatefulSeismoOverflow, snsASQStatsGlobal=snsASQStatsGlobal, snsASQStatsStatefulTcpInBytes=snsASQStatsStatefulTcpInBytes, snsASQStatsStatefulUdpPkt=snsASQStatsStatefulUdpPkt, snsASQStatsStatefulUdpNatConnDst=snsASQStatsStatefulUdpNatConnDst, snsASQStatsStatefulTcpNatConnDst=snsASQStatsStatefulTcpNatConnDst, snsASQStatsStatefulTcpPkt=snsASQStatsStatefulTcpPkt, snsASQStatsStatefulMinorAlarm=snsASQStatsStatefulMinorAlarm, snsASQStatsStatefulMajorAlarm=snsASQStatsStatefulMajorAlarm, snsASQStats=snsASQStats, snsASQStatsStatefulLogOverflow=snsASQStatsStatefulLogOverflow, snsASQStatsStatefulUdpInBytes=snsASQStatsStatefulUdpInBytes, snsASQStatsStatefulPktBlockedSynProxy=snsASQStatsStatefulPktBlockedSynProxy, PYSNMP_MODULE_ID=snsASQStats, snsASQStatsStatefulTcpSmallWindowRst=snsASQStatsStatefulTcpSmallWindowRst, snsASQStatsStateful=snsASQStatsStateful, snsASQStatsStatefulUdpNoNatConnDst=snsASQStatsStatefulUdpNoNatConnDst, snsASQStatsStatefulUdpConn=snsASQStatsStatefulUdpConn, snsASQStatsStatefulHttpTimeoutRst=snsASQStatsStatefulHttpTimeoutRst, snsASQStatsStatefulFlowConflicts=snsASQStatsStatefulFlowConflicts, snsASQStatsStatefulLogged=snsASQStatsStatefulLogged)
