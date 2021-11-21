#
# PySNMP MIB module BLUECOAT-SG-PROXY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/bluecoat/BLUECOAT-SG-PROXY-MIB
# Produced by pysmi-1.1.3 at Sun Nov 21 00:39:40 2021
# On host fv-az39-63 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
blueCoatMgmt, = mibBuilder.importSymbols("BLUECOAT-MIB", "blueCoatMgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Counter64, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Integer32, Bits, NotificationType, MibIdentifier, TimeTicks, Gauge32, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Integer32", "Bits", "NotificationType", "MibIdentifier", "TimeTicks", "Gauge32", "Unsigned32", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
bluecoatSGProxyMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 3417, 2, 11))
bluecoatSGProxyMIB.setRevisions(('2011-11-01 03:00', '2007-11-05 03:00', '2007-08-28 03:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: bluecoatSGProxyMIB.setRevisionsDescriptions(('Corrections regarding Capitalization and imports.', 'Minor corrections and reformatting.', 'Initial revision of this MIB.',))
if mibBuilder.loadTexts: bluecoatSGProxyMIB.setLastUpdated('201111010300Z')
if mibBuilder.loadTexts: bluecoatSGProxyMIB.setOrganization('Blue Coat Systems, Inc.')
if mibBuilder.loadTexts: bluecoatSGProxyMIB.setContactInfo('support.services@bluecoat.com\n                         http://www.bluecoat.com')
if mibBuilder.loadTexts: bluecoatSGProxyMIB.setDescription('The BLUECOAT-SG-PROXY-MIB provides system information\n                         and statistics for a BlueCoat SG proxy appliance.')
sgProxyConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 11, 1))
sgProxySystem = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 11, 2))
sgProxyHttp = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3))
sgProxyAdmin = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyAdmin.setStatus('current')
if mibBuilder.loadTexts: sgProxyAdmin.setDescription('The contact responsible for the administration of the\n                         proxy. Usually a name and email address.')
sgProxySoftware = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxySoftware.setStatus('current')
if mibBuilder.loadTexts: sgProxySoftware.setDescription('Name of the proxy sofware.')
sgProxyVersion = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyVersion.setStatus('current')
if mibBuilder.loadTexts: sgProxyVersion.setDescription('Version of the proxy software.')
sgProxySerialNumber = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxySerialNumber.setStatus('current')
if mibBuilder.loadTexts: sgProxySerialNumber.setDescription('Hardware serial number of the proxy appliance.')
sgProxyCpu = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 11, 2, 1))
sgProxyCache = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 11, 2, 2))
sgProxyMemory = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 11, 2, 3))
sgProxyCpuCoreTable = MibTable((1, 3, 6, 1, 4, 1, 3417, 2, 11, 2, 4), )
if mibBuilder.loadTexts: sgProxyCpuCoreTable.setStatus('current')
if mibBuilder.loadTexts: sgProxyCpuCoreTable.setDescription('This table lists the various cpu statistics.')
sgProxyCpuUpTime = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 2, 1, 1), Counter64()).setUnits('Milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyCpuUpTime.setStatus('deprecated')
if mibBuilder.loadTexts: sgProxyCpuUpTime.setDescription('The amount of time the proxy has been running\n                         since boot, in milliseconds. This is no longer functional.\n                         Use sgProxyCpuTable instead.')
sgProxyCpuBusyTime = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 2, 1, 2), Counter64()).setUnits('Milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyCpuBusyTime.setStatus('deprecated')
if mibBuilder.loadTexts: sgProxyCpuBusyTime.setDescription('The amount of busy CPU time since boot,\n                         in milliseconds. This is no longer functional.\n                         Use sgProxyCpuTable instead.')
sgProxyCpuIdleTime = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 2, 1, 3), Counter64()).setUnits('Milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyCpuIdleTime.setStatus('deprecated')
if mibBuilder.loadTexts: sgProxyCpuIdleTime.setDescription('The amount of idle CPU time since boot,\n                         in milliseconds. This is no longer functional.\n                         Use sgProxyCpuTable instead.')
sgProxyCpuUpTimeSinceLastAccess = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 2, 1, 4), Counter64()).setUnits('Milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyCpuUpTimeSinceLastAccess.setStatus('deprecated')
if mibBuilder.loadTexts: sgProxyCpuUpTimeSinceLastAccess.setDescription('The amount of time the proxy has been running since\n                         the last SNMP access to this value, in milliseconds.\n                         This is no longer functional. Use sgProxyCpuTable instead.')
sgProxyCpuBusyTimeSinceLastAccess = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 2, 1, 5), Counter64()).setUnits('Milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyCpuBusyTimeSinceLastAccess.setStatus('deprecated')
if mibBuilder.loadTexts: sgProxyCpuBusyTimeSinceLastAccess.setDescription('The amount of busy CPU time since the last SNMP access\n                         to this value, in milliseconds. This is no longer functional.\n                         Use sgProxyCpuTable instead.')
sgProxyCpuIdleTimeSinceLastAccess = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 2, 1, 6), Counter64()).setUnits('Milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyCpuIdleTimeSinceLastAccess.setStatus('deprecated')
if mibBuilder.loadTexts: sgProxyCpuIdleTimeSinceLastAccess.setDescription('The amount of idle CPU time since the last SNMP access\n                         to this value, in milliseconds. This is no longer functional.\n                         Use sgProxyCpuTable instead.')
sgProxyCpuBusyPerCent = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 2, 1, 7), Gauge32()).setUnits('Percentage').setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyCpuBusyPerCent.setStatus('deprecated')
if mibBuilder.loadTexts: sgProxyCpuBusyPerCent.setDescription('The busy CPU time as a percentage, averaged over\n                         one minute. This is no longer functional.\n                         Use sgProxyCpuTable instead.')
sgProxyCpuIdlePerCent = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 2, 1, 8), Gauge32()).setUnits('Percentage').setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyCpuIdlePerCent.setStatus('deprecated')
if mibBuilder.loadTexts: sgProxyCpuIdlePerCent.setDescription('The idle CPU time as a percentage, averaged over\n                         one minute. This is no longer functional.\n                         Use sgProxyCpuTable instead.')
sgProxyStorage = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 2, 2, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyStorage.setStatus('current')
if mibBuilder.loadTexts: sgProxyStorage.setDescription('The quantity of storage in use by the proxy in bytes.')
sgProxyNumObjects = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 2, 2, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyNumObjects.setStatus('current')
if mibBuilder.loadTexts: sgProxyNumObjects.setDescription('The number of objects currently held by the proxy.')
sgProxyMemAvailable = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 2, 3, 1), Counter64()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyMemAvailable.setStatus('current')
if mibBuilder.loadTexts: sgProxyMemAvailable.setDescription('The total memory available for use by the proxy,\n                         in bytes.')
sgProxyMemCacheUsage = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 2, 3, 2), Counter64()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyMemCacheUsage.setStatus('current')
if mibBuilder.loadTexts: sgProxyMemCacheUsage.setDescription('The memory used by the proxy for object caching,\n                         in bytes.')
sgProxyMemSysUsage = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 2, 3, 3), Counter64()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyMemSysUsage.setStatus('current')
if mibBuilder.loadTexts: sgProxyMemSysUsage.setDescription('The memory used by the proxy for system and support\n                         processes, in bytes.')
sgProxyMemoryPressure = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 2, 3, 4), Gauge32()).setUnits('Percentage').setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyMemoryPressure.setStatus('current')
if mibBuilder.loadTexts: sgProxyMemoryPressure.setDescription('The proportion of memory used in total by the proxy,\n                         as a percentage of the total memory available.')
sgProxyCpuCoreTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3417, 2, 11, 2, 4, 1), ).setIndexNames((0, "BLUECOAT-SG-PROXY-MIB", "sgProxyCpuCoreIndex"))
if mibBuilder.loadTexts: sgProxyCpuCoreTableEntry.setStatus('current')
if mibBuilder.loadTexts: sgProxyCpuCoreTableEntry.setDescription('A cpuTable entry describes the\n                         current cpu statistics.')
sgProxyCpuCoreIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 11, 2, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32)))
if mibBuilder.loadTexts: sgProxyCpuCoreIndex.setStatus('current')
if mibBuilder.loadTexts: sgProxyCpuCoreIndex.setDescription('CPU number.')
sgProxyCpuCoreUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 11, 2, 4, 1, 2), Counter64()).setUnits('Milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyCpuCoreUpTime.setStatus('current')
if mibBuilder.loadTexts: sgProxyCpuCoreUpTime.setDescription('The amount of time the proxy has been running\n                         since boot, in milliseconds.')
sgProxyCpuCoreBusyTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 11, 2, 4, 1, 3), Counter64()).setUnits('Milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyCpuCoreBusyTime.setStatus('current')
if mibBuilder.loadTexts: sgProxyCpuCoreBusyTime.setDescription('The amount of busy CPU time since boot,\n                         in milliseconds.')
sgProxyCpuCoreIdleTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 11, 2, 4, 1, 4), Counter64()).setUnits('Milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyCpuCoreIdleTime.setStatus('current')
if mibBuilder.loadTexts: sgProxyCpuCoreIdleTime.setDescription('The amount of idle CPU time since boot,\n                         in milliseconds.')
sgProxyCpuCoreUpTimeSinceLastAccess = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 11, 2, 4, 1, 5), Counter64()).setUnits('Milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyCpuCoreUpTimeSinceLastAccess.setStatus('current')
if mibBuilder.loadTexts: sgProxyCpuCoreUpTimeSinceLastAccess.setDescription('The amount of time the proxy has been running since\n                         the last SNMP access to this value, in milliseconds.')
sgProxyCpuCoreBusyTimeSinceLastAccess = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 11, 2, 4, 1, 6), Counter64()).setUnits('Milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyCpuCoreBusyTimeSinceLastAccess.setStatus('current')
if mibBuilder.loadTexts: sgProxyCpuCoreBusyTimeSinceLastAccess.setDescription('The amount of busy CPU time since the last SNMP access\n                         to this value, in milliseconds.')
sgProxyCpuCoreIdleTimeSinceLastAccess = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 11, 2, 4, 1, 7), Counter64()).setUnits('Milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyCpuCoreIdleTimeSinceLastAccess.setStatus('current')
if mibBuilder.loadTexts: sgProxyCpuCoreIdleTimeSinceLastAccess.setDescription('The amount of idle CPU time since the last SNMP access\n                         to this value, in milliseconds.')
sgProxyCpuCoreBusyPerCent = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 11, 2, 4, 1, 8), Gauge32()).setUnits('Percentage').setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyCpuCoreBusyPerCent.setStatus('current')
if mibBuilder.loadTexts: sgProxyCpuCoreBusyPerCent.setDescription('The busy CPU time as a percentage, averaged over\n                         one minute.')
sgProxyCpuCoreIdlePerCent = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 11, 2, 4, 1, 9), Gauge32()).setUnits('Percentage').setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyCpuCoreIdlePerCent.setStatus('current')
if mibBuilder.loadTexts: sgProxyCpuCoreIdlePerCent.setDescription('The idle CPU time as a percentage, averaged over\n                         one minute.')
sgProxyHttpPerf = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 1))
sgProxyHttpResponse = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 2))
sgProxyHttpMedian = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 3))
sgProxyHttpClient = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 1, 1))
sgProxyHttpServer = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 1, 2))
sgProxyHttpConnections = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 1, 3))
sgProxyHttpClientRequests = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 1, 1, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyHttpClientRequests.setStatus('current')
if mibBuilder.loadTexts: sgProxyHttpClientRequests.setDescription('The number of HTTP requests received from clients.')
sgProxyHttpClientHits = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 1, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyHttpClientHits.setStatus('current')
if mibBuilder.loadTexts: sgProxyHttpClientHits.setDescription('The number of HTTP hits that the proxy clients\n                         have produced.')
sgProxyHttpClientPartialHits = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 1, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyHttpClientPartialHits.setStatus('current')
if mibBuilder.loadTexts: sgProxyHttpClientPartialHits.setDescription('The number of HTTP partial (near) hits that the proxy\n                         clients have produced.')
sgProxyHttpClientMisses = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 1, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyHttpClientMisses.setStatus('current')
if mibBuilder.loadTexts: sgProxyHttpClientMisses.setDescription('The number of HTTP misses that the proxy clients\n                         have produced.')
sgProxyHttpClientErrors = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 1, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyHttpClientErrors.setStatus('current')
if mibBuilder.loadTexts: sgProxyHttpClientErrors.setDescription('The number of HTTP errors caused by client\n                         connections.')
sgProxyHttpClientRequestRate = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 1, 1, 6), Gauge32()).setUnits('Requests Per Second').setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyHttpClientRequestRate.setStatus('current')
if mibBuilder.loadTexts: sgProxyHttpClientRequestRate.setDescription('The average rate per second of HTTP requests.')
sgProxyHttpClientHitRate = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 1, 1, 7), Gauge32()).setUnits('Percentage').setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyHttpClientHitRate.setStatus('current')
if mibBuilder.loadTexts: sgProxyHttpClientHitRate.setDescription('The percentage HTTP hit rate (by objects).')
sgProxyHttpClientByteHitRate = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 1, 1, 8), Gauge32()).setUnits('Percentage').setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyHttpClientByteHitRate.setStatus('current')
if mibBuilder.loadTexts: sgProxyHttpClientByteHitRate.setDescription('The percentage HTTP hit rate (by requested bytes).\n                         This is the number of bytes returned to the client\n                         for hits, as a fraction of the total bytes.')
sgProxyHttpClientInBytes = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 1, 1, 9), Counter64()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyHttpClientInBytes.setStatus('current')
if mibBuilder.loadTexts: sgProxyHttpClientInBytes.setDescription('The number of bytes received from the clients by\n                         the proxy.')
sgProxyHttpClientOutBytes = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 1, 1, 10), Counter64()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyHttpClientOutBytes.setStatus('current')
if mibBuilder.loadTexts: sgProxyHttpClientOutBytes.setDescription('The number of bytes delivered to clients from\n                         the proxy.')
sgProxyHttpServerRequests = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 1, 2, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyHttpServerRequests.setStatus('current')
if mibBuilder.loadTexts: sgProxyHttpServerRequests.setDescription('The number of HTTP requests that the proxy has\n                         issued.')
sgProxyHttpServerErrors = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 1, 2, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyHttpServerErrors.setStatus('current')
if mibBuilder.loadTexts: sgProxyHttpServerErrors.setDescription('The number of HTTP errors while fetching objects.')
sgProxyHttpServerInBytes = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 1, 2, 3), Counter64()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyHttpServerInBytes.setStatus('current')
if mibBuilder.loadTexts: sgProxyHttpServerInBytes.setDescription('The number of bytes received by the proxy from\n                         remote servers.')
sgProxyHttpServerOutBytes = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 1, 2, 4), Counter64()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyHttpServerOutBytes.setStatus('current')
if mibBuilder.loadTexts: sgProxyHttpServerOutBytes.setDescription('The number of bytes transmitted by the proxy to\n                         remote servers.')
sgProxyHttpClientConnections = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 1, 3, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyHttpClientConnections.setStatus('current')
if mibBuilder.loadTexts: sgProxyHttpClientConnections.setDescription('The total number of HTTP connections with the\n                         proxy clients.')
sgProxyHttpClientConnectionsActive = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 1, 3, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyHttpClientConnectionsActive.setStatus('current')
if mibBuilder.loadTexts: sgProxyHttpClientConnectionsActive.setDescription('The number of active HTTP connections with the\n                         proxy clients.')
sgProxyHttpClientConnectionsIdle = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 1, 3, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyHttpClientConnectionsIdle.setStatus('current')
if mibBuilder.loadTexts: sgProxyHttpClientConnectionsIdle.setDescription('The number of idle HTTP connections with the\n                         proxy clients.')
sgProxyHttpServerConnections = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 1, 3, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyHttpServerConnections.setStatus('current')
if mibBuilder.loadTexts: sgProxyHttpServerConnections.setDescription('The total number of HTTP connections with\n                         remote servers.')
sgProxyHttpServerConnectionsActive = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 1, 3, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyHttpServerConnectionsActive.setStatus('current')
if mibBuilder.loadTexts: sgProxyHttpServerConnectionsActive.setDescription('The number of active HTTP connections with\n                         remote servers.')
sgProxyHttpServerConnectionsIdle = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 1, 3, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyHttpServerConnectionsIdle.setStatus('current')
if mibBuilder.loadTexts: sgProxyHttpServerConnectionsIdle.setDescription('The number of idle HTTP connections with\n                         remote servers.')
sgProxyHttpResponseTime = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 2, 1))
sgProxyHttpResponseFirstByte = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 2, 2))
sgProxyHttpResponseByteRate = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 2, 3))
sgProxyHttpResponseSize = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 2, 4))
sgProxyHttpServiceTimeAll = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 2, 1, 1), Gauge32()).setUnits('Milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyHttpServiceTimeAll.setStatus('current')
if mibBuilder.loadTexts: sgProxyHttpServiceTimeAll.setDescription('The average service time for all HTTP requests,\n                         in milliseconds.')
sgProxyHttpServiceTimeHit = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 2, 1, 2), Gauge32()).setUnits('Milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyHttpServiceTimeHit.setStatus('current')
if mibBuilder.loadTexts: sgProxyHttpServiceTimeHit.setDescription('The average service time for all HTTP hits,\n                         in milliseconds.')
sgProxyHttpServiceTimePartialHit = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 2, 1, 3), Gauge32()).setUnits('Milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyHttpServiceTimePartialHit.setStatus('current')
if mibBuilder.loadTexts: sgProxyHttpServiceTimePartialHit.setDescription('The average service time for all HTTP partial (near)\n                         hits, in milliseconds.')
sgProxyHttpServiceTimeMiss = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 2, 1, 4), Gauge32()).setUnits('Milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyHttpServiceTimeMiss.setStatus('current')
if mibBuilder.loadTexts: sgProxyHttpServiceTimeMiss.setDescription('The average service time for all HTTP misses,\n                         in milliseconds.')
sgProxyHttpTotalFetchTimeAll = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 2, 1, 5), Counter64()).setUnits('Milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyHttpTotalFetchTimeAll.setStatus('current')
if mibBuilder.loadTexts: sgProxyHttpTotalFetchTimeAll.setDescription('The total fetch time for all HTTP responses,\n                         in milliseconds.')
sgProxyHttpTotalFetchTimeHit = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 2, 1, 6), Counter64()).setUnits('Milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyHttpTotalFetchTimeHit.setStatus('current')
if mibBuilder.loadTexts: sgProxyHttpTotalFetchTimeHit.setDescription('The total fetch time for all HTTP hits,\n                         in milliseconds.')
sgProxyHttpTotalFetchTimePartialHit = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 2, 1, 7), Counter64()).setUnits('Milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyHttpTotalFetchTimePartialHit.setStatus('current')
if mibBuilder.loadTexts: sgProxyHttpTotalFetchTimePartialHit.setDescription('The total fetch time for all HTTP partial (near) hits,\n                         in milliseconds.')
sgProxyHttpTotalFetchTimeMiss = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 2, 1, 8), Counter64()).setUnits('Milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyHttpTotalFetchTimeMiss.setStatus('current')
if mibBuilder.loadTexts: sgProxyHttpTotalFetchTimeMiss.setDescription('The total fetch time for all HTTP misses,\n                         in milliseconds.')
sgProxyHttpFirstByteAll = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 2, 2, 1), Gauge32()).setUnits('Milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyHttpFirstByteAll.setStatus('current')
if mibBuilder.loadTexts: sgProxyHttpFirstByteAll.setDescription('The average time to first response byte for all HTTP\n                         requests, in milliseconds.')
sgProxyHttpFirstByteHit = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 2, 2, 2), Gauge32()).setUnits('Milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyHttpFirstByteHit.setStatus('current')
if mibBuilder.loadTexts: sgProxyHttpFirstByteHit.setDescription('The average time to first response byte for all HTTP\n                         hits, in milliseconds.')
sgProxyHttpFirstBytePartialHit = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 2, 2, 3), Gauge32()).setUnits('Milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyHttpFirstBytePartialHit.setStatus('current')
if mibBuilder.loadTexts: sgProxyHttpFirstBytePartialHit.setDescription('The average time to first response byte for all HTTP\n                         partial (near) hits, in milliseconds.')
sgProxyHttpFirstByteMiss = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 2, 2, 4), Gauge32()).setUnits('Milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyHttpFirstByteMiss.setStatus('current')
if mibBuilder.loadTexts: sgProxyHttpFirstByteMiss.setDescription('The average time to first response byte for all HTTP\n                         misses, in milliseconds.')
sgProxyHttpByteRateAll = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 2, 3, 1), Gauge32()).setUnits('Bytes Per Second').setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyHttpByteRateAll.setStatus('current')
if mibBuilder.loadTexts: sgProxyHttpByteRateAll.setDescription('The average byte rate for all HTTP responses, in bytes\n                         per second.')
sgProxyHttpByteRateHit = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 2, 3, 2), Gauge32()).setUnits('Bytes Per Second').setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyHttpByteRateHit.setStatus('current')
if mibBuilder.loadTexts: sgProxyHttpByteRateHit.setDescription('The average byte rate for all HTTP hits, in bytes\n                         per second.')
sgProxyHttpByteRatePartialHit = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 2, 3, 3), Gauge32()).setUnits('Bytes Per Second').setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyHttpByteRatePartialHit.setStatus('current')
if mibBuilder.loadTexts: sgProxyHttpByteRatePartialHit.setDescription('The average byte rate for all HTTP partial hits, in\n                         bytes per second.')
sgProxyHttpByteRateMiss = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 2, 3, 4), Gauge32()).setUnits('Bytes Per Second').setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyHttpByteRateMiss.setStatus('current')
if mibBuilder.loadTexts: sgProxyHttpByteRateMiss.setDescription('The average byte rate for all HTTP misses, in bytes\n                         per second.')
sgProxyHttpResponseSizeAll = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 2, 4, 1), Gauge32()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyHttpResponseSizeAll.setStatus('current')
if mibBuilder.loadTexts: sgProxyHttpResponseSizeAll.setDescription('The average response size for all HTTP responses,\n                         in bytes.')
sgProxyHttpResponseSizeHit = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 2, 4, 2), Gauge32()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyHttpResponseSizeHit.setStatus('current')
if mibBuilder.loadTexts: sgProxyHttpResponseSizeHit.setDescription('The average response size for all HTTP hits,\n                         in bytes.')
sgProxyHttpResponseSizePartialHit = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 2, 4, 3), Gauge32()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyHttpResponseSizePartialHit.setStatus('current')
if mibBuilder.loadTexts: sgProxyHttpResponseSizePartialHit.setDescription('The average response size for all HTTP partial hits,\n                         in bytes.')
sgProxyHttpResponseSizeMiss = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 2, 4, 4), Gauge32()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyHttpResponseSizeMiss.setStatus('current')
if mibBuilder.loadTexts: sgProxyHttpResponseSizeMiss.setDescription('The average response size for all HTTP misses,\n                         in bytes.')
sgProxyHttpMedianServiceTable = MibTable((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 3, 1), )
if mibBuilder.loadTexts: sgProxyHttpMedianServiceTable.setStatus('current')
if mibBuilder.loadTexts: sgProxyHttpMedianServiceTable.setDescription('Table of median HTTP service times.')
sgProxyHttpMedianServiceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 3, 1, 1), ).setIndexNames((0, "BLUECOAT-SG-PROXY-MIB", "sgProxyHttpMedianServiceTime"))
if mibBuilder.loadTexts: sgProxyHttpMedianServiceEntry.setStatus('current')
if mibBuilder.loadTexts: sgProxyHttpMedianServiceEntry.setDescription('Table entry for median HTTP service times.')
sgProxyHttpMedianServiceTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 5, 60))).clone(namedValues=NamedValues(("one", 1), ("five", 5), ("sixty", 60)))).setUnits('Minutes')
if mibBuilder.loadTexts: sgProxyHttpMedianServiceTime.setStatus('current')
if mibBuilder.loadTexts: sgProxyHttpMedianServiceTime.setDescription('The median time used to index the table\n                         sgProxyHttpMedianServiceTable. This release supports\n                         one, five, and sixty minutes.')
sgProxyHttpMedianServiceTimeAll = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 3, 1, 1, 2), Gauge32()).setUnits('Milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyHttpMedianServiceTimeAll.setStatus('current')
if mibBuilder.loadTexts: sgProxyHttpMedianServiceTimeAll.setDescription('The median service time for all HTTP requests,\n                         in milliseconds.')
sgProxyHttpMedianServiceTimeHit = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 3, 1, 1, 3), Gauge32()).setUnits('Milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyHttpMedianServiceTimeHit.setStatus('current')
if mibBuilder.loadTexts: sgProxyHttpMedianServiceTimeHit.setDescription('The median service time for all HTTP hits,\n                         in milliseconds.')
sgProxyHttpMedianServiceTimePartialHit = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 3, 1, 1, 4), Gauge32()).setUnits('Milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyHttpMedianServiceTimePartialHit.setStatus('current')
if mibBuilder.loadTexts: sgProxyHttpMedianServiceTimePartialHit.setDescription('The median service time for all HTTP partial (near)\n                         hits, in milliseconds.')
sgProxyHttpMedianServiceTimeMiss = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 3, 1, 1, 5), Gauge32()).setUnits('Milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyHttpMedianServiceTimeMiss.setStatus('current')
if mibBuilder.loadTexts: sgProxyHttpMedianServiceTimeMiss.setDescription('The median service time for all HTTP misses,\n                         in milliseconds.')
sgProxyDnsMedianServiceTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 3, 1, 1, 6), Gauge32()).setUnits('Milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: sgProxyDnsMedianServiceTime.setStatus('current')
if mibBuilder.loadTexts: sgProxyDnsMedianServiceTime.setDescription('The median DNS service time, in milliseconds.')
mibBuilder.exportSymbols("BLUECOAT-SG-PROXY-MIB", sgProxyCache=sgProxyCache, sgProxyCpuCoreTable=sgProxyCpuCoreTable, sgProxyHttpClientRequestRate=sgProxyHttpClientRequestRate, sgProxyCpuCoreIdleTime=sgProxyCpuCoreIdleTime, sgProxyHttpResponseSizeMiss=sgProxyHttpResponseSizeMiss, sgProxyCpuUpTime=sgProxyCpuUpTime, sgProxyCpuBusyTime=sgProxyCpuBusyTime, sgProxyHttpResponseByteRate=sgProxyHttpResponseByteRate, sgProxyCpuBusyTimeSinceLastAccess=sgProxyCpuBusyTimeSinceLastAccess, sgProxyStorage=sgProxyStorage, sgProxyCpuCoreUpTime=sgProxyCpuCoreUpTime, sgProxyHttpTotalFetchTimeMiss=sgProxyHttpTotalFetchTimeMiss, sgProxyMemAvailable=sgProxyMemAvailable, sgProxyHttpResponseFirstByte=sgProxyHttpResponseFirstByte, sgProxySoftware=sgProxySoftware, sgProxyHttpMedianServiceTimeAll=sgProxyHttpMedianServiceTimeAll, sgProxyHttpServiceTimePartialHit=sgProxyHttpServiceTimePartialHit, sgProxyHttpClientConnections=sgProxyHttpClientConnections, sgProxyAdmin=sgProxyAdmin, sgProxyHttpResponseSizeAll=sgProxyHttpResponseSizeAll, sgProxyHttpClientMisses=sgProxyHttpClientMisses, sgProxyHttpServiceTimeHit=sgProxyHttpServiceTimeHit, sgProxyCpuIdleTime=sgProxyCpuIdleTime, sgProxyHttpClientErrors=sgProxyHttpClientErrors, sgProxyHttpClientConnectionsActive=sgProxyHttpClientConnectionsActive, sgProxyConfig=sgProxyConfig, sgProxyHttpMedianServiceTime=sgProxyHttpMedianServiceTime, sgProxyCpuIdleTimeSinceLastAccess=sgProxyCpuIdleTimeSinceLastAccess, sgProxyHttpServiceTimeMiss=sgProxyHttpServiceTimeMiss, sgProxyHttpResponse=sgProxyHttpResponse, sgProxyHttpClientPartialHits=sgProxyHttpClientPartialHits, sgProxyCpuBusyPerCent=sgProxyCpuBusyPerCent, sgProxyHttpResponseSize=sgProxyHttpResponseSize, sgProxyHttpMedianServiceTimeHit=sgProxyHttpMedianServiceTimeHit, sgProxyHttpMedianServiceTimePartialHit=sgProxyHttpMedianServiceTimePartialHit, sgProxyHttpByteRateMiss=sgProxyHttpByteRateMiss, sgProxyVersion=sgProxyVersion, sgProxyCpuCoreBusyTime=sgProxyCpuCoreBusyTime, sgProxyHttpFirstByteMiss=sgProxyHttpFirstByteMiss, sgProxyHttp=sgProxyHttp, sgProxyHttpPerf=sgProxyHttpPerf, sgProxyHttpClientInBytes=sgProxyHttpClientInBytes, sgProxyCpuCoreUpTimeSinceLastAccess=sgProxyCpuCoreUpTimeSinceLastAccess, sgProxyMemoryPressure=sgProxyMemoryPressure, sgProxyHttpResponseSizePartialHit=sgProxyHttpResponseSizePartialHit, sgProxySerialNumber=sgProxySerialNumber, sgProxyHttpConnections=sgProxyHttpConnections, sgProxyHttpServer=sgProxyHttpServer, bluecoatSGProxyMIB=bluecoatSGProxyMIB, sgProxyHttpServerRequests=sgProxyHttpServerRequests, PYSNMP_MODULE_ID=bluecoatSGProxyMIB, sgProxyMemCacheUsage=sgProxyMemCacheUsage, sgProxyHttpServerConnectionsActive=sgProxyHttpServerConnectionsActive, sgProxyHttpClientRequests=sgProxyHttpClientRequests, sgProxyHttpByteRatePartialHit=sgProxyHttpByteRatePartialHit, sgProxyHttpClient=sgProxyHttpClient, sgProxyCpuCoreTableEntry=sgProxyCpuCoreTableEntry, sgProxyHttpTotalFetchTimePartialHit=sgProxyHttpTotalFetchTimePartialHit, sgProxyHttpMedianServiceTimeMiss=sgProxyHttpMedianServiceTimeMiss, sgProxySystem=sgProxySystem, sgProxyDnsMedianServiceTime=sgProxyDnsMedianServiceTime, sgProxyHttpClientConnectionsIdle=sgProxyHttpClientConnectionsIdle, sgProxyHttpServerConnections=sgProxyHttpServerConnections, sgProxyCpuCoreIndex=sgProxyCpuCoreIndex, sgProxyHttpFirstBytePartialHit=sgProxyHttpFirstBytePartialHit, sgProxyCpu=sgProxyCpu, sgProxyHttpResponseSizeHit=sgProxyHttpResponseSizeHit, sgProxyCpuCoreBusyTimeSinceLastAccess=sgProxyCpuCoreBusyTimeSinceLastAccess, sgProxyHttpServerConnectionsIdle=sgProxyHttpServerConnectionsIdle, sgProxyCpuUpTimeSinceLastAccess=sgProxyCpuUpTimeSinceLastAccess, sgProxyHttpClientHits=sgProxyHttpClientHits, sgProxyCpuCoreIdleTimeSinceLastAccess=sgProxyCpuCoreIdleTimeSinceLastAccess, sgProxyMemSysUsage=sgProxyMemSysUsage, sgProxyHttpTotalFetchTimeHit=sgProxyHttpTotalFetchTimeHit, sgProxyCpuCoreBusyPerCent=sgProxyCpuCoreBusyPerCent, sgProxyHttpClientHitRate=sgProxyHttpClientHitRate, sgProxyHttpServerOutBytes=sgProxyHttpServerOutBytes, sgProxyHttpByteRateHit=sgProxyHttpByteRateHit, sgProxyHttpServiceTimeAll=sgProxyHttpServiceTimeAll, sgProxyHttpResponseTime=sgProxyHttpResponseTime, sgProxyHttpFirstByteAll=sgProxyHttpFirstByteAll, sgProxyCpuCoreIdlePerCent=sgProxyCpuCoreIdlePerCent, sgProxyMemory=sgProxyMemory, sgProxyHttpMedianServiceEntry=sgProxyHttpMedianServiceEntry, sgProxyHttpFirstByteHit=sgProxyHttpFirstByteHit, sgProxyHttpServerInBytes=sgProxyHttpServerInBytes, sgProxyHttpServerErrors=sgProxyHttpServerErrors, sgProxyHttpMedian=sgProxyHttpMedian, sgProxyHttpMedianServiceTable=sgProxyHttpMedianServiceTable, sgProxyHttpClientByteHitRate=sgProxyHttpClientByteHitRate, sgProxyHttpByteRateAll=sgProxyHttpByteRateAll, sgProxyCpuIdlePerCent=sgProxyCpuIdlePerCent, sgProxyHttpTotalFetchTimeAll=sgProxyHttpTotalFetchTimeAll, sgProxyNumObjects=sgProxyNumObjects, sgProxyHttpClientOutBytes=sgProxyHttpClientOutBytes)
