#
# PySNMP MIB module EIP-STATS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/efficientip/EIP-STATS-MIB
# Produced by pysmi-1.1.8 at Sun Jan 16 00:36:17 2022
# On host fv-az42-839 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, Counter64, Counter32, ObjectIdentity, Bits, TimeTicks, iso, NotificationType, Gauge32, IpAddress, ModuleIdentity, MibIdentifier, enterprises, NotificationType, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Counter64", "Counter32", "ObjectIdentity", "Bits", "TimeTicks", "iso", "NotificationType", "Gauge32", "IpAddress", "ModuleIdentity", "MibIdentifier", "enterprises", "NotificationType", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention, PhysAddress = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "PhysAddress")
eip = MibIdentifier((1, 3, 6, 1, 4, 1, 2440))
products = MibIdentifier((1, 3, 6, 1, 4, 1, 2440, 1))
eipDns = MibIdentifier((1, 3, 6, 1, 4, 1, 2440, 1, 4))
eipDnsStat = MibIdentifier((1, 3, 6, 1, 4, 1, 2440, 1, 4, 2))
eipDhcp = MibIdentifier((1, 3, 6, 1, 4, 1, 2440, 1, 3))
eipDhcpStat = MibIdentifier((1, 3, 6, 1, 4, 1, 2440, 1, 3, 2))
eipDhcp6 = MibIdentifier((1, 3, 6, 1, 4, 1, 2440, 1, 7))
eipDhcp6Stat = MibIdentifier((1, 3, 6, 1, 4, 1, 2440, 1, 7, 1))
eipDnsStatTable = MibTable((1, 3, 6, 1, 4, 1, 2440, 1, 4, 2, 3), )
if mibBuilder.loadTexts: eipDnsStatTable.setStatus('mandatory')
if mibBuilder.loadTexts: eipDnsStatTable.setDescription('Statistics of DNS queries.')
eipDnsStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2440, 1, 4, 2, 3, 1), ).setIndexNames((0, "EIP-STATS-MIB", "eipDnsStatName"))
if mibBuilder.loadTexts: eipDnsStatEntry.setStatus('mandatory')
if mibBuilder.loadTexts: eipDnsStatEntry.setDescription('Statistics of DNS queries.')
eipDnsStatIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2440, 1, 4, 2, 3, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDnsStatIndex.setStatus('mandatory')
if mibBuilder.loadTexts: eipDnsStatIndex.setDescription('Statistic index')
eipDnsStatName = MibTableColumn((1, 3, 6, 1, 4, 1, 2440, 1, 4, 2, 3, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDnsStatName.setStatus('mandatory')
if mibBuilder.loadTexts: eipDnsStatName.setDescription('Statistic name')
eipDnsStatValue = MibTableColumn((1, 3, 6, 1, 4, 1, 2440, 1, 4, 2, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDnsStatValue.setStatus('mandatory')
if mibBuilder.loadTexts: eipDnsStatValue.setDescription('Statistic value')
eipDhcpStatTable = MibTable((1, 3, 6, 1, 4, 1, 2440, 1, 3, 2, 22), )
if mibBuilder.loadTexts: eipDhcpStatTable.setStatus('mandatory')
if mibBuilder.loadTexts: eipDhcpStatTable.setDescription('Statistics of DHCP queries.')
eipDhcpStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2440, 1, 3, 2, 22, 1), ).setIndexNames((0, "EIP-STATS-MIB", "eipDhcpStatName"))
if mibBuilder.loadTexts: eipDhcpStatEntry.setStatus('mandatory')
if mibBuilder.loadTexts: eipDhcpStatEntry.setDescription('Statistics of DHCP queries.')
eipDhcpStatIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2440, 1, 3, 2, 22, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDhcpStatIndex.setStatus('mandatory')
if mibBuilder.loadTexts: eipDhcpStatIndex.setDescription('Statistic name')
eipDhcpStatName = MibTableColumn((1, 3, 6, 1, 4, 1, 2440, 1, 3, 2, 22, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDhcpStatName.setStatus('mandatory')
if mibBuilder.loadTexts: eipDhcpStatName.setDescription('Statistic name')
eipDhcpStatValue = MibTableColumn((1, 3, 6, 1, 4, 1, 2440, 1, 3, 2, 22, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDhcpStatValue.setStatus('mandatory')
if mibBuilder.loadTexts: eipDhcpStatValue.setDescription('Statistic value')
eipDhcp6StatTable = MibTable((1, 3, 6, 1, 4, 1, 2440, 1, 7, 1, 1), )
if mibBuilder.loadTexts: eipDhcp6StatTable.setStatus('mandatory')
if mibBuilder.loadTexts: eipDhcp6StatTable.setDescription('Statistics of DHCP queries.')
eipDhcp6StatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2440, 1, 7, 1, 1, 1), ).setIndexNames((0, "EIP-STATS-MIB", "eipDhcp6StatName"))
if mibBuilder.loadTexts: eipDhcp6StatEntry.setStatus('mandatory')
if mibBuilder.loadTexts: eipDhcp6StatEntry.setDescription('Statistics of DHCP queries.')
eipDhcp6StatIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2440, 1, 7, 1, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDhcp6StatIndex.setStatus('mandatory')
if mibBuilder.loadTexts: eipDhcp6StatIndex.setDescription('Statistic index')
eipDhcp6StatName = MibTableColumn((1, 3, 6, 1, 4, 1, 2440, 1, 7, 1, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDhcp6StatName.setStatus('mandatory')
if mibBuilder.loadTexts: eipDhcp6StatName.setDescription('Statistic name')
eipDhcp6StatValue = MibTableColumn((1, 3, 6, 1, 4, 1, 2440, 1, 7, 1, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDhcp6StatValue.setStatus('mandatory')
if mibBuilder.loadTexts: eipDhcp6StatValue.setDescription('Statistic value')
mibBuilder.exportSymbols("EIP-STATS-MIB", eipDhcp6=eipDhcp6, eipDhcp6StatTable=eipDhcp6StatTable, eipDhcp6StatEntry=eipDhcp6StatEntry, eipDhcp=eipDhcp, eipDhcpStatName=eipDhcpStatName, eip=eip, eipDhcpStatIndex=eipDhcpStatIndex, eipDhcpStatTable=eipDhcpStatTable, eipDnsStatIndex=eipDnsStatIndex, eipDnsStatName=eipDnsStatName, eipDhcp6StatValue=eipDhcp6StatValue, products=products, eipDhcpStat=eipDhcpStat, eipDhcp6StatIndex=eipDhcp6StatIndex, eipDhcp6StatName=eipDhcp6StatName, eipDnsStat=eipDnsStat, eipDnsStatEntry=eipDnsStatEntry, eipDnsStatTable=eipDnsStatTable, eipDnsStatValue=eipDnsStatValue, eipDhcpStatEntry=eipDhcpStatEntry, eipDhcpStatValue=eipDhcpStatValue, eipDns=eipDns, eipDhcp6Stat=eipDhcp6Stat)
