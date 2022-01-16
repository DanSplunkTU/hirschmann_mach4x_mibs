#
# PySNMP MIB module F5-BIGIP-WAM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/f5/F5-BIGIP-WAM-MIB
# Produced by pysmi-1.1.8 at Sun Jan 16 00:36:51 2022
# On host fv-az42-839 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
bigipTrafficMgmt, LongDisplayString, bigipCompliances, bigipGroups = mibBuilder.importSymbols("F5-BIGIP-COMMON-MIB", "bigipTrafficMgmt", "LongDisplayString", "bigipCompliances", "bigipGroups")
InetAddressType, InetPortNumber, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetPortNumber", "InetAddress")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
iso, NotificationType, enterprises, Counter64, ObjectIdentity, MibIdentifier, Opaque, ModuleIdentity, Integer32, IpAddress, Counter32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Gauge32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "NotificationType", "enterprises", "Counter64", "ObjectIdentity", "MibIdentifier", "Opaque", "ModuleIdentity", "Integer32", "IpAddress", "Counter32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Gauge32", "Bits")
DisplayString, MacAddress, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "TextualConvention")
bigipWAM = ModuleIdentity((1, 3, 6, 1, 4, 1, 3375, 2, 7))
if mibBuilder.loadTexts: bigipWAM.setLastUpdated('202004092224Z')
if mibBuilder.loadTexts: bigipWAM.setOrganization('F5 Networks, Inc.')
wamAppStat = MibIdentifier((1, 3, 6, 1, 4, 1, 3375, 2, 7, 1))
wamAppStatResetStats = MibScalar((1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wamAppStatResetStats.setStatus('current')
wamAppStatNumber = MibScalar((1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wamAppStatNumber.setStatus('current')
wamAppStatTable = MibTable((1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3), )
if mibBuilder.loadTexts: wamAppStatTable.setStatus('current')
wamAppStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1), ).setIndexNames((0, "F5-BIGIP-WAM-MIB", "wamAppStatName"))
if mibBuilder.loadTexts: wamAppStatEntry.setStatus('current')
wamAppStatName = MibTableColumn((1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 1), LongDisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wamAppStatName.setStatus('obsolete')
wamAppStatVsName = MibTableColumn((1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 2), LongDisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wamAppStatVsName.setStatus('obsolete')
wamAppStatRqstTotal = MibTableColumn((1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wamAppStatRqstTotal.setStatus('obsolete')
wamAppStatProxied = MibTableColumn((1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wamAppStatProxied.setStatus('obsolete')
wamAppStatProxiedBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wamAppStatProxiedBytes.setStatus('obsolete')
wamAppStatProxied1500 = MibTableColumn((1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wamAppStatProxied1500.setStatus('obsolete')
wamAppStatProxied10k = MibTableColumn((1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wamAppStatProxied10k.setStatus('obsolete')
wamAppStatProxied50k = MibTableColumn((1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wamAppStatProxied50k.setStatus('obsolete')
wamAppStatProxied100k = MibTableColumn((1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wamAppStatProxied100k.setStatus('obsolete')
wamAppStatProxied500k = MibTableColumn((1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wamAppStatProxied500k.setStatus('obsolete')
wamAppStatProxied1m = MibTableColumn((1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wamAppStatProxied1m.setStatus('obsolete')
wamAppStatProxied5m = MibTableColumn((1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wamAppStatProxied5m.setStatus('obsolete')
wamAppStatProxiedLarge = MibTableColumn((1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wamAppStatProxiedLarge.setStatus('obsolete')
wamAppStatProxiedNew = MibTableColumn((1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 14), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wamAppStatProxiedNew.setStatus('obsolete')
wamAppStatProxiedExpired = MibTableColumn((1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 15), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wamAppStatProxiedExpired.setStatus('obsolete')
wamAppStatProxiedPerPolicy = MibTableColumn((1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 16), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wamAppStatProxiedPerPolicy.setStatus('obsolete')
wamAppStatProxiedPerIrule = MibTableColumn((1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 17), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wamAppStatProxiedPerIrule.setStatus('obsolete')
wamAppStatProxiedPerInvalidation = MibTableColumn((1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 18), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wamAppStatProxiedPerInvalidation.setStatus('obsolete')
wamAppStatProxiedPerClientRequest = MibTableColumn((1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 19), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wamAppStatProxiedPerClientRequest.setStatus('obsolete')
wamAppStatProxiedBypass = MibTableColumn((1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 20), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wamAppStatProxiedBypass.setStatus('obsolete')
wamAppStatFromCache = MibTableColumn((1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 21), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wamAppStatFromCache.setStatus('obsolete')
wamAppStatFromCacheBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 22), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wamAppStatFromCacheBytes.setStatus('obsolete')
wamAppStatFromCache1500 = MibTableColumn((1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 23), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wamAppStatFromCache1500.setStatus('obsolete')
wamAppStatFromCache10k = MibTableColumn((1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 24), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wamAppStatFromCache10k.setStatus('obsolete')
wamAppStatFromCache50k = MibTableColumn((1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 25), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wamAppStatFromCache50k.setStatus('obsolete')
wamAppStatFromCache100k = MibTableColumn((1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 26), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wamAppStatFromCache100k.setStatus('obsolete')
wamAppStatFromCache500k = MibTableColumn((1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 27), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wamAppStatFromCache500k.setStatus('obsolete')
wamAppStatFromCache1m = MibTableColumn((1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 28), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wamAppStatFromCache1m.setStatus('obsolete')
wamAppStatFromCache5m = MibTableColumn((1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 29), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wamAppStatFromCache5m.setStatus('obsolete')
wamAppStatFromCacheLarge = MibTableColumn((1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 30), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wamAppStatFromCacheLarge.setStatus('obsolete')
wamAppStatOws2xx = MibTableColumn((1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 31), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wamAppStatOws2xx.setStatus('obsolete')
wamAppStatOws3xx = MibTableColumn((1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 32), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wamAppStatOws3xx.setStatus('obsolete')
wamAppStatOws4xx = MibTableColumn((1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 33), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wamAppStatOws4xx.setStatus('obsolete')
wamAppStatOws5xx = MibTableColumn((1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 34), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wamAppStatOws5xx.setStatus('obsolete')
wamAppStatOwsDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 35), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wamAppStatOwsDropped.setStatus('obsolete')
wamAppStatOwsRejected = MibTableColumn((1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 36), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wamAppStatOwsRejected.setStatus('obsolete')
wamAppStatWam2xx = MibTableColumn((1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 37), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wamAppStatWam2xx.setStatus('obsolete')
wamAppStatWam3xx = MibTableColumn((1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 38), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wamAppStatWam3xx.setStatus('obsolete')
wamAppStatWam4xx = MibTableColumn((1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 39), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wamAppStatWam4xx.setStatus('obsolete')
wamAppStatWam5xx = MibTableColumn((1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 40), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wamAppStatWam5xx.setStatus('obsolete')
wamAppStatWam503 = MibTableColumn((1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 41), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wamAppStatWam503.setStatus('obsolete')
wamAppStatWamDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 42), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wamAppStatWamDropped.setStatus('obsolete')
bigipWAMCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 3375, 2, 5, 1, 7)).setObjects(("F5-BIGIP-WAM-MIB", "bigipWAMGroups"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bigipWAMCompliance = bigipWAMCompliance.setStatus('current')
bigipWAMGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 3375, 2, 5, 2, 7))
wamAppStatGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 3375, 2, 5, 2, 7, 1)).setObjects(("F5-BIGIP-WAM-MIB", "wamAppStatResetStats"), ("F5-BIGIP-WAM-MIB", "wamAppStatNumber"), ("F5-BIGIP-WAM-MIB", "wamAppStatName"), ("F5-BIGIP-WAM-MIB", "wamAppStatVsName"), ("F5-BIGIP-WAM-MIB", "wamAppStatRqstTotal"), ("F5-BIGIP-WAM-MIB", "wamAppStatProxied"), ("F5-BIGIP-WAM-MIB", "wamAppStatProxiedBytes"), ("F5-BIGIP-WAM-MIB", "wamAppStatProxied1500"), ("F5-BIGIP-WAM-MIB", "wamAppStatProxied10k"), ("F5-BIGIP-WAM-MIB", "wamAppStatProxied50k"), ("F5-BIGIP-WAM-MIB", "wamAppStatProxied100k"), ("F5-BIGIP-WAM-MIB", "wamAppStatProxied500k"), ("F5-BIGIP-WAM-MIB", "wamAppStatProxied1m"), ("F5-BIGIP-WAM-MIB", "wamAppStatProxied5m"), ("F5-BIGIP-WAM-MIB", "wamAppStatProxiedLarge"), ("F5-BIGIP-WAM-MIB", "wamAppStatProxiedNew"), ("F5-BIGIP-WAM-MIB", "wamAppStatProxiedExpired"), ("F5-BIGIP-WAM-MIB", "wamAppStatProxiedPerPolicy"), ("F5-BIGIP-WAM-MIB", "wamAppStatProxiedPerIrule"), ("F5-BIGIP-WAM-MIB", "wamAppStatProxiedPerInvalidation"), ("F5-BIGIP-WAM-MIB", "wamAppStatProxiedPerClientRequest"), ("F5-BIGIP-WAM-MIB", "wamAppStatProxiedBypass"), ("F5-BIGIP-WAM-MIB", "wamAppStatFromCache"), ("F5-BIGIP-WAM-MIB", "wamAppStatFromCacheBytes"), ("F5-BIGIP-WAM-MIB", "wamAppStatFromCache1500"), ("F5-BIGIP-WAM-MIB", "wamAppStatFromCache10k"), ("F5-BIGIP-WAM-MIB", "wamAppStatFromCache50k"), ("F5-BIGIP-WAM-MIB", "wamAppStatFromCache100k"), ("F5-BIGIP-WAM-MIB", "wamAppStatFromCache500k"), ("F5-BIGIP-WAM-MIB", "wamAppStatFromCache1m"), ("F5-BIGIP-WAM-MIB", "wamAppStatFromCache5m"), ("F5-BIGIP-WAM-MIB", "wamAppStatFromCacheLarge"), ("F5-BIGIP-WAM-MIB", "wamAppStatOws2xx"), ("F5-BIGIP-WAM-MIB", "wamAppStatOws3xx"), ("F5-BIGIP-WAM-MIB", "wamAppStatOws4xx"), ("F5-BIGIP-WAM-MIB", "wamAppStatOws5xx"), ("F5-BIGIP-WAM-MIB", "wamAppStatOwsDropped"), ("F5-BIGIP-WAM-MIB", "wamAppStatOwsRejected"), ("F5-BIGIP-WAM-MIB", "wamAppStatWam2xx"), ("F5-BIGIP-WAM-MIB", "wamAppStatWam3xx"), ("F5-BIGIP-WAM-MIB", "wamAppStatWam4xx"), ("F5-BIGIP-WAM-MIB", "wamAppStatWam5xx"), ("F5-BIGIP-WAM-MIB", "wamAppStatWam503"), ("F5-BIGIP-WAM-MIB", "wamAppStatWamDropped"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    wamAppStatGroup = wamAppStatGroup.setStatus('current')
mibBuilder.exportSymbols("F5-BIGIP-WAM-MIB", wamAppStatWam2xx=wamAppStatWam2xx, wamAppStatProxiedBytes=wamAppStatProxiedBytes, PYSNMP_MODULE_ID=bigipWAM, wamAppStatFromCacheLarge=wamAppStatFromCacheLarge, wamAppStatFromCache100k=wamAppStatFromCache100k, wamAppStatWam3xx=wamAppStatWam3xx, wamAppStatOws5xx=wamAppStatOws5xx, wamAppStat=wamAppStat, wamAppStatProxiedPerClientRequest=wamAppStatProxiedPerClientRequest, wamAppStatProxiedExpired=wamAppStatProxiedExpired, wamAppStatOws4xx=wamAppStatOws4xx, wamAppStatProxied1m=wamAppStatProxied1m, bigipWAMGroups=bigipWAMGroups, wamAppStatFromCache50k=wamAppStatFromCache50k, wamAppStatFromCache1500=wamAppStatFromCache1500, wamAppStatFromCache5m=wamAppStatFromCache5m, wamAppStatNumber=wamAppStatNumber, wamAppStatFromCache500k=wamAppStatFromCache500k, wamAppStatWam5xx=wamAppStatWam5xx, wamAppStatProxied100k=wamAppStatProxied100k, wamAppStatOws3xx=wamAppStatOws3xx, wamAppStatOwsRejected=wamAppStatOwsRejected, wamAppStatProxied10k=wamAppStatProxied10k, bigipWAM=bigipWAM, wamAppStatResetStats=wamAppStatResetStats, wamAppStatGroup=wamAppStatGroup, wamAppStatProxiedNew=wamAppStatProxiedNew, wamAppStatProxied1500=wamAppStatProxied1500, wamAppStatRqstTotal=wamAppStatRqstTotal, wamAppStatWamDropped=wamAppStatWamDropped, wamAppStatProxiedLarge=wamAppStatProxiedLarge, wamAppStatProxiedPerPolicy=wamAppStatProxiedPerPolicy, wamAppStatProxiedPerIrule=wamAppStatProxiedPerIrule, wamAppStatProxiedBypass=wamAppStatProxiedBypass, wamAppStatWam503=wamAppStatWam503, wamAppStatFromCache=wamAppStatFromCache, wamAppStatProxied500k=wamAppStatProxied500k, wamAppStatFromCache10k=wamAppStatFromCache10k, wamAppStatName=wamAppStatName, wamAppStatFromCacheBytes=wamAppStatFromCacheBytes, wamAppStatTable=wamAppStatTable, bigipWAMCompliance=bigipWAMCompliance, wamAppStatFromCache1m=wamAppStatFromCache1m, wamAppStatProxiedPerInvalidation=wamAppStatProxiedPerInvalidation, wamAppStatOwsDropped=wamAppStatOwsDropped, wamAppStatProxied5m=wamAppStatProxied5m, wamAppStatVsName=wamAppStatVsName, wamAppStatProxied=wamAppStatProxied, wamAppStatOws2xx=wamAppStatOws2xx, wamAppStatEntry=wamAppStatEntry, wamAppStatProxied50k=wamAppStatProxied50k, wamAppStatWam4xx=wamAppStatWam4xx)
