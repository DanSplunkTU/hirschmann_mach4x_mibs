#
# PySNMP MIB module DHCP-SERVER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/DHCP-SERVER-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:07:39 2022
# On host fv-az36-988 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
MibIdentifier, ObjectIdentity, ModuleIdentity, iso, Unsigned32, TimeTicks, Gauge32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, NotificationType, IpAddress, Counter64, Counter32, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "ObjectIdentity", "ModuleIdentity", "iso", "Unsigned32", "TimeTicks", "Gauge32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "NotificationType", "IpAddress", "Counter64", "Counter32", "enterprises")
RowStatus, DateAndTime, TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DateAndTime", "TruthValue", "DisplayString", "TextualConvention")
lucent = MibIdentifier((1, 3, 6, 1, 4, 1, 1751))
products = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 1))
mibs = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 2))
ipspg = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 1, 48))
ipspgServices = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 1, 48, 1))
ipspgDHCP = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1))
ipspgDNS = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 2))
ipspgTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 1, 48, 2))
dhcpServMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1))
if mibBuilder.loadTexts: dhcpServMib.setLastUpdated('0606220830Z')
if mibBuilder.loadTexts: dhcpServMib.setOrganization('Lucent Technologies')
dhcpServMibTraps = ObjectIdentity((1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 0))
if mibBuilder.loadTexts: dhcpServMibTraps.setStatus('current')
dhcpServMibObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1))
if mibBuilder.loadTexts: dhcpServMibObjects.setStatus('current')
dhcpServSystem = ObjectIdentity((1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 1))
if mibBuilder.loadTexts: dhcpServSystem.setStatus('current')
dhcpServSubnetCounters = ObjectIdentity((1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 2))
if mibBuilder.loadTexts: dhcpServSubnetCounters.setStatus('current')
dhcpServBootpCounters = ObjectIdentity((1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 3))
if mibBuilder.loadTexts: dhcpServBootpCounters.setStatus('current')
dhcpServDhcpCounters = ObjectIdentity((1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 4))
if mibBuilder.loadTexts: dhcpServDhcpCounters.setStatus('current')
dhcpServBootpStatistics = ObjectIdentity((1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 5))
if mibBuilder.loadTexts: dhcpServBootpStatistics.setStatus('current')
dhcpServDhcpStatistics = ObjectIdentity((1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 6))
if mibBuilder.loadTexts: dhcpServDhcpStatistics.setStatus('current')
dhcpServConfiguration = ObjectIdentity((1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 7))
if mibBuilder.loadTexts: dhcpServConfiguration.setStatus('current')
dhcpServFailover = ObjectIdentity((1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 8))
if mibBuilder.loadTexts: dhcpServFailover.setStatus('current')
class DhcpServTimeInterval(TextualConvention, Gauge32):
    status = 'current'

dhcpServSystemDescr = MibScalar((1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpServSystemDescr.setStatus('current')
dhcpServSystemStatus = MibScalar((1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("starting", 0), ("running", 1), ("stopping", 2), ("stopped", 3), ("reload", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpServSystemStatus.setStatus('current')
dhcpServSystemUpTime = MibScalar((1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpServSystemUpTime.setStatus('current')
dhcpServSystemResetTime = MibScalar((1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpServSystemResetTime.setStatus('current')
dhcpServCountUsedSubnets = MibScalar((1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpServCountUsedSubnets.setStatus('current')
dhcpServCountUnusedSubnets = MibScalar((1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 2, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpServCountUnusedSubnets.setStatus('current')
dhcpServCountFullSubnets = MibScalar((1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 2, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpServCountFullSubnets.setStatus('current')
dhcpServBootpCountRequests = MibScalar((1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 3, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpServBootpCountRequests.setStatus('current')
dhcpServBootpCountInvalids = MibScalar((1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 3, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpServBootpCountInvalids.setStatus('current')
dhcpServBootpCountReplies = MibScalar((1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 3, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpServBootpCountReplies.setStatus('current')
dhcpServBootpCountDroppedUnknownClients = MibScalar((1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 3, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpServBootpCountDroppedUnknownClients.setStatus('current')
dhcpServBootpCountDroppedNotServingSubnet = MibScalar((1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 3, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpServBootpCountDroppedNotServingSubnet.setStatus('current')
dhcpServDhcpCountDiscovers = MibScalar((1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 4, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpServDhcpCountDiscovers.setStatus('current')
dhcpServDhcpCountRequests = MibScalar((1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 4, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpServDhcpCountRequests.setStatus('current')
dhcpServDhcpCountReleases = MibScalar((1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 4, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpServDhcpCountReleases.setStatus('current')
dhcpServDhcpCountDeclines = MibScalar((1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 4, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpServDhcpCountDeclines.setStatus('current')
dhcpServDhcpCountInforms = MibScalar((1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 4, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpServDhcpCountInforms.setStatus('current')
dhcpServDhcpCountInvalids = MibScalar((1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 4, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpServDhcpCountInvalids.setStatus('current')
dhcpServDhcpCountOffers = MibScalar((1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 4, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpServDhcpCountOffers.setStatus('current')
dhcpServDhcpCountAcks = MibScalar((1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 4, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpServDhcpCountAcks.setStatus('current')
dhcpServDhcpCountNacks = MibScalar((1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 4, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpServDhcpCountNacks.setStatus('current')
dhcpServDhcpCountDroppedUnknownClient = MibScalar((1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 4, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpServDhcpCountDroppedUnknownClient.setStatus('current')
dhcpServDhcpCountDroppedNotServingSubnet = MibScalar((1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 4, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpServDhcpCountDroppedNotServingSubnet.setStatus('current')
dhcpServBootpStatMinArrivalInterval = MibScalar((1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 5, 1), DhcpServTimeInterval()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpServBootpStatMinArrivalInterval.setStatus('current')
dhcpServBootpStatMaxArrivalInterval = MibScalar((1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 5, 2), DhcpServTimeInterval()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpServBootpStatMaxArrivalInterval.setStatus('current')
dhcpServBootpStatLastArrivalTime = MibScalar((1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 5, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpServBootpStatLastArrivalTime.setStatus('current')
dhcpServBootpStatMinResponseTime = MibScalar((1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 5, 4), DhcpServTimeInterval()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpServBootpStatMinResponseTime.setStatus('current')
dhcpServBootpStatMaxResponseTime = MibScalar((1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 5, 5), DhcpServTimeInterval()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpServBootpStatMaxResponseTime.setStatus('current')
dhcpServBootpStatSumResponseTime = MibScalar((1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 5, 6), DhcpServTimeInterval()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpServBootpStatSumResponseTime.setStatus('current')
dhcpServDhcpStatMinArrivalInterval = MibScalar((1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 6, 1), DhcpServTimeInterval()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpServDhcpStatMinArrivalInterval.setStatus('current')
dhcpServDhcpStatMaxArrivalInterval = MibScalar((1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 6, 2), DhcpServTimeInterval()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpServDhcpStatMaxArrivalInterval.setStatus('current')
dhcpServDhcpStatLastArrivalTime = MibScalar((1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 6, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpServDhcpStatLastArrivalTime.setStatus('current')
dhcpServDhcpStatMinResponseTime = MibScalar((1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 6, 4), DhcpServTimeInterval()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpServDhcpStatMinResponseTime.setStatus('current')
dhcpServDhcpStatMaxResponseTime = MibScalar((1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 6, 5), DhcpServTimeInterval()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpServDhcpStatMaxResponseTime.setStatus('current')
dhcpServDhcpStatSumResponseTime = MibScalar((1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 6, 6), DhcpServTimeInterval()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpServDhcpStatSumResponseTime.setStatus('current')
dhcpServRangeTable = MibTable((1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 7, 2), )
if mibBuilder.loadTexts: dhcpServRangeTable.setStatus('current')
dhcpServRangeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 7, 2, 1), ).setIndexNames((0, "DHCP-SERVER-MIB", "dhcpServRangeSubnetAddr"), (0, "DHCP-SERVER-MIB", "dhcpServRangeStart"))
if mibBuilder.loadTexts: dhcpServRangeEntry.setStatus('current')
dhcpServRangeSubnetAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 7, 2, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpServRangeSubnetAddr.setStatus('current')
dhcpServRangeSubnetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 7, 2, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpServRangeSubnetMask.setStatus('current')
dhcpServRangeStart = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 7, 2, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpServRangeStart.setStatus('current')
dhcpServRangeEnd = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 7, 2, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpServRangeEnd.setStatus('current')
dhcpServRangeInUse = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 7, 2, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpServRangeInUse.setStatus('current')
dhcpServRangeOutstandingOffers = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 7, 2, 1, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpServRangeOutstandingOffers.setStatus('current')
dhcpServRangeUnavailable = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 7, 2, 1, 7), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpServRangeUnavailable.setStatus('current')
dhcpServRangeType = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 7, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("manBootp", 1), ("autoBootp", 2), ("manDhcp", 3), ("autoDhcp", 4), ("dynamicDhcp", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpServRangeType.setStatus('current')
dhcpServRangeUnused = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 7, 2, 1, 9), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpServRangeUnused.setStatus('current')
dhcpServFailoverTable = MibTable((1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 8, 1), )
if mibBuilder.loadTexts: dhcpServFailoverTable.setStatus('current')
dhcpServFailoverEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 8, 1, 1), ).setIndexNames((0, "DHCP-SERVER-MIB", "dhcpServFailoverPartnerAddr"))
if mibBuilder.loadTexts: dhcpServFailoverEntry.setStatus('current')
dhcpServFailoverPartnerAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 8, 1, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpServFailoverPartnerAddr.setStatus('current')
dhcpServFailoverPartnerType = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 8, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("primary", 1), ("failover", 2), ("unconfigured", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpServFailoverPartnerType.setStatus('current')
dhcpServFailoverPartnerStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 8, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("unknown", 0), ("syncing", 1), ("active", 2), ("inactive", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpServFailoverPartnerStatus.setStatus('current')
dhcpServFailoverPartnerPolltime = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 8, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpServFailoverPartnerPolltime.setStatus('current')
ipspgDhcpTrapTable = MibTable((1, 3, 6, 1, 4, 1, 1751, 1, 48, 2, 1), )
if mibBuilder.loadTexts: ipspgDhcpTrapTable.setStatus('current')
ipspgDhcpTrapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1751, 1, 48, 2, 1, 1), ).setIndexNames((0, "DHCP-SERVER-MIB", "ipspgDhcpTrIndex"))
if mibBuilder.loadTexts: ipspgDhcpTrapEntry.setStatus('current')
ipspgDhcpTrIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 1, 48, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipspgDhcpTrIndex.setStatus('current')
ipspgDhcpTrSequence = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 1, 48, 2, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipspgDhcpTrSequence.setStatus('current')
ipspgDhcpTrId = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 1, 48, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 3))).clone(namedValues=NamedValues(("monitor", 1), ("analyzer", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipspgDhcpTrId.setStatus('current')
ipspgDhcpTrText = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 1, 48, 2, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipspgDhcpTrText.setStatus('current')
ipspgDhcpTrPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 1, 48, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("inform", 1), ("warning", 2), ("minor", 3), ("major", 4), ("critical", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipspgDhcpTrPriority.setStatus('current')
ipspgDhcpTrClass = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 1, 48, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipspgDhcpTrClass.setStatus('current')
ipspgDhcpTrType = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 1, 48, 2, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipspgDhcpTrType.setStatus('current')
ipspgDhcpTrTime = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 1, 48, 2, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipspgDhcpTrTime.setStatus('current')
ipspgDhcpTrSuspect = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 1, 48, 2, 1, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipspgDhcpTrSuspect.setStatus('current')
ipspgDhcpTrDiagId = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 1, 48, 2, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipspgDhcpTrDiagId.setStatus('current')
dhcpServerStarted = NotificationType((1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 0, 1)).setObjects(("DHCP-SERVER-MIB", "ipspgDhcpTrSequence"), ("DHCP-SERVER-MIB", "ipspgDhcpTrId"), ("DHCP-SERVER-MIB", "ipspgDhcpTrText"), ("DHCP-SERVER-MIB", "ipspgDhcpTrPriority"), ("DHCP-SERVER-MIB", "ipspgDhcpTrClass"), ("DHCP-SERVER-MIB", "ipspgDhcpTrType"), ("DHCP-SERVER-MIB", "ipspgDhcpTrTime"), ("DHCP-SERVER-MIB", "ipspgDhcpTrSuspect"), ("DHCP-SERVER-MIB", "ipspgDhcpTrDiagId"))
if mibBuilder.loadTexts: dhcpServerStarted.setStatus('current')
dhcpServerStopped = NotificationType((1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 0, 2)).setObjects(("DHCP-SERVER-MIB", "ipspgDhcpTrSequence"), ("DHCP-SERVER-MIB", "ipspgDhcpTrId"), ("DHCP-SERVER-MIB", "ipspgDhcpTrText"), ("DHCP-SERVER-MIB", "ipspgDhcpTrPriority"), ("DHCP-SERVER-MIB", "ipspgDhcpTrClass"), ("DHCP-SERVER-MIB", "ipspgDhcpTrType"), ("DHCP-SERVER-MIB", "ipspgDhcpTrTime"), ("DHCP-SERVER-MIB", "ipspgDhcpTrSuspect"), ("DHCP-SERVER-MIB", "ipspgDhcpTrDiagId"))
if mibBuilder.loadTexts: dhcpServerStopped.setStatus('current')
dhcpServerReload = NotificationType((1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 0, 3)).setObjects(("DHCP-SERVER-MIB", "ipspgDhcpTrSequence"), ("DHCP-SERVER-MIB", "ipspgDhcpTrId"), ("DHCP-SERVER-MIB", "ipspgDhcpTrText"), ("DHCP-SERVER-MIB", "ipspgDhcpTrPriority"), ("DHCP-SERVER-MIB", "ipspgDhcpTrClass"), ("DHCP-SERVER-MIB", "ipspgDhcpTrType"), ("DHCP-SERVER-MIB", "ipspgDhcpTrTime"), ("DHCP-SERVER-MIB", "ipspgDhcpTrSuspect"), ("DHCP-SERVER-MIB", "ipspgDhcpTrDiagId"))
if mibBuilder.loadTexts: dhcpServerReload.setStatus('current')
dhcpServerSubnetDepleted = NotificationType((1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 0, 4)).setObjects(("DHCP-SERVER-MIB", "ipspgDhcpTrSequence"), ("DHCP-SERVER-MIB", "ipspgDhcpTrId"), ("DHCP-SERVER-MIB", "ipspgDhcpTrText"), ("DHCP-SERVER-MIB", "ipspgDhcpTrPriority"), ("DHCP-SERVER-MIB", "ipspgDhcpTrClass"), ("DHCP-SERVER-MIB", "ipspgDhcpTrType"), ("DHCP-SERVER-MIB", "ipspgDhcpTrTime"), ("DHCP-SERVER-MIB", "ipspgDhcpTrSuspect"), ("DHCP-SERVER-MIB", "ipspgDhcpTrDiagId"))
if mibBuilder.loadTexts: dhcpServerSubnetDepleted.setStatus('current')
dhcpServerBadPacket = NotificationType((1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 0, 5)).setObjects(("DHCP-SERVER-MIB", "ipspgDhcpTrSequence"), ("DHCP-SERVER-MIB", "ipspgDhcpTrId"), ("DHCP-SERVER-MIB", "ipspgDhcpTrText"), ("DHCP-SERVER-MIB", "ipspgDhcpTrPriority"), ("DHCP-SERVER-MIB", "ipspgDhcpTrClass"), ("DHCP-SERVER-MIB", "ipspgDhcpTrType"), ("DHCP-SERVER-MIB", "ipspgDhcpTrTime"), ("DHCP-SERVER-MIB", "ipspgDhcpTrSuspect"), ("DHCP-SERVER-MIB", "ipspgDhcpTrDiagId"))
if mibBuilder.loadTexts: dhcpServerBadPacket.setStatus('current')
dhcpServerFailoverActive = NotificationType((1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 0, 6)).setObjects(("DHCP-SERVER-MIB", "ipspgDhcpTrSequence"), ("DHCP-SERVER-MIB", "ipspgDhcpTrId"), ("DHCP-SERVER-MIB", "ipspgDhcpTrText"), ("DHCP-SERVER-MIB", "ipspgDhcpTrPriority"), ("DHCP-SERVER-MIB", "ipspgDhcpTrClass"), ("DHCP-SERVER-MIB", "ipspgDhcpTrType"), ("DHCP-SERVER-MIB", "ipspgDhcpTrTime"), ("DHCP-SERVER-MIB", "ipspgDhcpTrSuspect"), ("DHCP-SERVER-MIB", "ipspgDhcpTrDiagId"))
if mibBuilder.loadTexts: dhcpServerFailoverActive.setStatus('current')
dhcpServerFailoverReturnedControl = NotificationType((1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 0, 7)).setObjects(("DHCP-SERVER-MIB", "ipspgDhcpTrSequence"), ("DHCP-SERVER-MIB", "ipspgDhcpTrId"), ("DHCP-SERVER-MIB", "ipspgDhcpTrText"), ("DHCP-SERVER-MIB", "ipspgDhcpTrPriority"), ("DHCP-SERVER-MIB", "ipspgDhcpTrClass"), ("DHCP-SERVER-MIB", "ipspgDhcpTrType"), ("DHCP-SERVER-MIB", "ipspgDhcpTrTime"), ("DHCP-SERVER-MIB", "ipspgDhcpTrSuspect"), ("DHCP-SERVER-MIB", "ipspgDhcpTrDiagId"))
if mibBuilder.loadTexts: dhcpServerFailoverReturnedControl.setStatus('current')
dhcpServerSubnetThresholdExceeded = NotificationType((1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 0, 8)).setObjects(("DHCP-SERVER-MIB", "ipspgDhcpTrSequence"), ("DHCP-SERVER-MIB", "ipspgDhcpTrId"), ("DHCP-SERVER-MIB", "ipspgDhcpTrText"), ("DHCP-SERVER-MIB", "ipspgDhcpTrPriority"), ("DHCP-SERVER-MIB", "ipspgDhcpTrClass"), ("DHCP-SERVER-MIB", "ipspgDhcpTrType"), ("DHCP-SERVER-MIB", "ipspgDhcpTrTime"), ("DHCP-SERVER-MIB", "ipspgDhcpTrSuspect"), ("DHCP-SERVER-MIB", "ipspgDhcpTrDiagId"))
if mibBuilder.loadTexts: dhcpServerSubnetThresholdExceeded.setStatus('current')
dhcpServerSubnetThresholdDescent = NotificationType((1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 0, 9)).setObjects(("DHCP-SERVER-MIB", "ipspgDhcpTrSequence"), ("DHCP-SERVER-MIB", "ipspgDhcpTrId"), ("DHCP-SERVER-MIB", "ipspgDhcpTrText"), ("DHCP-SERVER-MIB", "ipspgDhcpTrPriority"), ("DHCP-SERVER-MIB", "ipspgDhcpTrClass"), ("DHCP-SERVER-MIB", "ipspgDhcpTrType"), ("DHCP-SERVER-MIB", "ipspgDhcpTrTime"), ("DHCP-SERVER-MIB", "ipspgDhcpTrSuspect"), ("DHCP-SERVER-MIB", "ipspgDhcpTrDiagId"))
if mibBuilder.loadTexts: dhcpServerSubnetThresholdDescent.setStatus('current')
dhcpServerDropUnknownClient = NotificationType((1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 0, 10)).setObjects(("DHCP-SERVER-MIB", "ipspgDhcpTrSequence"), ("DHCP-SERVER-MIB", "ipspgDhcpTrId"), ("DHCP-SERVER-MIB", "ipspgDhcpTrText"), ("DHCP-SERVER-MIB", "ipspgDhcpTrPriority"), ("DHCP-SERVER-MIB", "ipspgDhcpTrClass"), ("DHCP-SERVER-MIB", "ipspgDhcpTrType"), ("DHCP-SERVER-MIB", "ipspgDhcpTrTime"), ("DHCP-SERVER-MIB", "ipspgDhcpTrSuspect"), ("DHCP-SERVER-MIB", "ipspgDhcpTrDiagId"))
if mibBuilder.loadTexts: dhcpServerDropUnknownClient.setStatus('current')
dhcpServerPingResponseReceived = NotificationType((1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 0, 11)).setObjects(("DHCP-SERVER-MIB", "ipspgDhcpTrSequence"), ("DHCP-SERVER-MIB", "ipspgDhcpTrId"), ("DHCP-SERVER-MIB", "ipspgDhcpTrText"), ("DHCP-SERVER-MIB", "ipspgDhcpTrPriority"), ("DHCP-SERVER-MIB", "ipspgDhcpTrClass"), ("DHCP-SERVER-MIB", "ipspgDhcpTrType"), ("DHCP-SERVER-MIB", "ipspgDhcpTrTime"), ("DHCP-SERVER-MIB", "ipspgDhcpTrSuspect"), ("DHCP-SERVER-MIB", "ipspgDhcpTrDiagId"))
if mibBuilder.loadTexts: dhcpServerPingResponseReceived.setStatus('current')
mibBuilder.exportSymbols("DHCP-SERVER-MIB", dhcpServDhcpCounters=dhcpServDhcpCounters, PYSNMP_MODULE_ID=dhcpServMib, dhcpServerFailoverActive=dhcpServerFailoverActive, dhcpServerSubnetThresholdExceeded=dhcpServerSubnetThresholdExceeded, dhcpServDhcpCountInforms=dhcpServDhcpCountInforms, dhcpServDhcpCountNacks=dhcpServDhcpCountNacks, dhcpServBootpStatMaxResponseTime=dhcpServBootpStatMaxResponseTime, dhcpServCountFullSubnets=dhcpServCountFullSubnets, dhcpServDhcpStatMinArrivalInterval=dhcpServDhcpStatMinArrivalInterval, ipspgServices=ipspgServices, mibs=mibs, ipspgDhcpTrText=ipspgDhcpTrText, ipspgDhcpTrDiagId=ipspgDhcpTrDiagId, dhcpServDhcpCountOffers=dhcpServDhcpCountOffers, dhcpServMibObjects=dhcpServMibObjects, ipspgDhcpTrSequence=ipspgDhcpTrSequence, dhcpServFailoverPartnerAddr=dhcpServFailoverPartnerAddr, dhcpServerStarted=dhcpServerStarted, ipspgDhcpTrTime=ipspgDhcpTrTime, dhcpServBootpStatistics=dhcpServBootpStatistics, dhcpServSubnetCounters=dhcpServSubnetCounters, dhcpServBootpStatMinArrivalInterval=dhcpServBootpStatMinArrivalInterval, DhcpServTimeInterval=DhcpServTimeInterval, lucent=lucent, dhcpServerReload=dhcpServerReload, dhcpServDhcpCountDroppedUnknownClient=dhcpServDhcpCountDroppedUnknownClient, dhcpServDhcpCountReleases=dhcpServDhcpCountReleases, dhcpServSystemResetTime=dhcpServSystemResetTime, ipspg=ipspg, dhcpServerDropUnknownClient=dhcpServerDropUnknownClient, dhcpServConfiguration=dhcpServConfiguration, dhcpServDhcpStatistics=dhcpServDhcpStatistics, dhcpServSystemStatus=dhcpServSystemStatus, dhcpServDhcpCountRequests=dhcpServDhcpCountRequests, dhcpServBootpCountDroppedUnknownClients=dhcpServBootpCountDroppedUnknownClients, dhcpServDhcpCountDroppedNotServingSubnet=dhcpServDhcpCountDroppedNotServingSubnet, dhcpServFailoverPartnerType=dhcpServFailoverPartnerType, dhcpServFailoverPartnerStatus=dhcpServFailoverPartnerStatus, dhcpServSystemUpTime=dhcpServSystemUpTime, dhcpServRangeType=dhcpServRangeType, dhcpServDhcpCountDiscovers=dhcpServDhcpCountDiscovers, dhcpServCountUnusedSubnets=dhcpServCountUnusedSubnets, dhcpServBootpCountDroppedNotServingSubnet=dhcpServBootpCountDroppedNotServingSubnet, ipspgDHCP=ipspgDHCP, dhcpServerFailoverReturnedControl=dhcpServerFailoverReturnedControl, dhcpServFailoverTable=dhcpServFailoverTable, dhcpServRangeUnavailable=dhcpServRangeUnavailable, dhcpServBootpStatMinResponseTime=dhcpServBootpStatMinResponseTime, dhcpServDhcpStatSumResponseTime=dhcpServDhcpStatSumResponseTime, dhcpServDhcpCountInvalids=dhcpServDhcpCountInvalids, dhcpServDhcpStatMaxArrivalInterval=dhcpServDhcpStatMaxArrivalInterval, dhcpServDhcpStatLastArrivalTime=dhcpServDhcpStatLastArrivalTime, dhcpServCountUsedSubnets=dhcpServCountUsedSubnets, dhcpServBootpCounters=dhcpServBootpCounters, dhcpServRangeUnused=dhcpServRangeUnused, dhcpServBootpCountRequests=dhcpServBootpCountRequests, dhcpServRangeTable=dhcpServRangeTable, ipspgDhcpTrapEntry=ipspgDhcpTrapEntry, ipspgDhcpTrType=ipspgDhcpTrType, dhcpServMib=dhcpServMib, dhcpServDhcpStatMinResponseTime=dhcpServDhcpStatMinResponseTime, products=products, dhcpServBootpCountReplies=dhcpServBootpCountReplies, dhcpServSystemDescr=dhcpServSystemDescr, ipspgDhcpTrIndex=ipspgDhcpTrIndex, dhcpServerSubnetDepleted=dhcpServerSubnetDepleted, dhcpServBootpCountInvalids=dhcpServBootpCountInvalids, dhcpServFailoverEntry=dhcpServFailoverEntry, dhcpServerStopped=dhcpServerStopped, dhcpServerSubnetThresholdDescent=dhcpServerSubnetThresholdDescent, ipspgDNS=ipspgDNS, dhcpServerPingResponseReceived=dhcpServerPingResponseReceived, dhcpServFailover=dhcpServFailover, dhcpServDhcpCountDeclines=dhcpServDhcpCountDeclines, dhcpServSystem=dhcpServSystem, dhcpServRangeStart=dhcpServRangeStart, dhcpServRangeSubnetAddr=dhcpServRangeSubnetAddr, dhcpServRangeInUse=dhcpServRangeInUse, ipspgDhcpTrapTable=ipspgDhcpTrapTable, ipspgTrap=ipspgTrap, dhcpServDhcpStatMaxResponseTime=dhcpServDhcpStatMaxResponseTime, dhcpServMibTraps=dhcpServMibTraps, ipspgDhcpTrSuspect=ipspgDhcpTrSuspect, dhcpServBootpStatSumResponseTime=dhcpServBootpStatSumResponseTime, dhcpServBootpStatLastArrivalTime=dhcpServBootpStatLastArrivalTime, dhcpServRangeEnd=dhcpServRangeEnd, dhcpServRangeEntry=dhcpServRangeEntry, ipspgDhcpTrId=ipspgDhcpTrId, ipspgDhcpTrClass=ipspgDhcpTrClass, dhcpServFailoverPartnerPolltime=dhcpServFailoverPartnerPolltime, dhcpServRangeSubnetMask=dhcpServRangeSubnetMask, ipspgDhcpTrPriority=ipspgDhcpTrPriority, dhcpServerBadPacket=dhcpServerBadPacket, dhcpServDhcpCountAcks=dhcpServDhcpCountAcks, dhcpServRangeOutstandingOffers=dhcpServRangeOutstandingOffers, dhcpServBootpStatMaxArrivalInterval=dhcpServBootpStatMaxArrivalInterval)
