#
# PySNMP MIB module VIPRINET-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/viprinet/VIPRINET-MIB
# Produced by pysmi-1.1.3 at Sun Nov 21 00:46:24 2021
# On host fv-az39-63 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Counter64, Integer32, ModuleIdentity, Counter32, iso, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, enterprises, Bits, MibIdentifier, Unsigned32, NotificationType, IpAddress, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Integer32", "ModuleIdentity", "Counter32", "iso", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "enterprises", "Bits", "MibIdentifier", "Unsigned32", "NotificationType", "IpAddress", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
viprinet = ModuleIdentity((1, 3, 6, 1, 4, 1, 35424))
viprinet.setRevisions(('2015-09-28 16:20',))
if mibBuilder.loadTexts: viprinet.setLastUpdated('201509281620Z')
if mibBuilder.loadTexts: viprinet.setOrganization('Viprinet')
vpnRouter = MibIdentifier((1, 3, 6, 1, 4, 1, 35424, 1))
vpnRouterInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 35424, 1, 1))
vpnRouterHealth = MibIdentifier((1, 3, 6, 1, 4, 1, 35424, 1, 2))
vpnRouterFans = MibIdentifier((1, 3, 6, 1, 4, 1, 35424, 1, 3))
vpnRouterInterfaces = MibIdentifier((1, 3, 6, 1, 4, 1, 35424, 1, 4))
vpnRouterTunnels = MibIdentifier((1, 3, 6, 1, 4, 1, 35424, 1, 5))
vpnRouterTunnelChannels = MibIdentifier((1, 3, 6, 1, 4, 1, 35424, 1, 6))
vpnRouterName = MibScalar((1, 3, 6, 1, 4, 1, 35424, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(64, 64)).setFixedLength(64)).setMaxAccess("readonly")
if mibBuilder.loadTexts: vpnRouterName.setStatus('current')
vpnRouterSerial = MibScalar((1, 3, 6, 1, 4, 1, 35424, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(19, 19)).setFixedLength(19)).setMaxAccess("readonly")
if mibBuilder.loadTexts: vpnRouterSerial.setStatus('current')
vpnRouterModel = MibScalar((1, 3, 6, 1, 4, 1, 35424, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readonly")
if mibBuilder.loadTexts: vpnRouterModel.setStatus('current')
vpnRouterFirmware = MibScalar((1, 3, 6, 1, 4, 1, 35424, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(22, 22)).setFixedLength(22)).setMaxAccess("readonly")
if mibBuilder.loadTexts: vpnRouterFirmware.setStatus('current')
vpnRouterMode = MibScalar((1, 3, 6, 1, 4, 1, 35424, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 3))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vpnRouterMode.setStatus('current')
vpnRouteruptime = MibScalar((1, 3, 6, 1, 4, 1, 35424, 1, 1, 6), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vpnRouteruptime.setStatus('current')
vpnRouterFirmwareStatus = MibScalar((1, 3, 6, 1, 4, 1, 35424, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vpnRouterFirmwareStatus.setStatus('current')
vpnRouterCPULoad = MibScalar((1, 3, 6, 1, 4, 1, 35424, 1, 2, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(3, 3)).setFixedLength(3)).setMaxAccess("readonly")
if mibBuilder.loadTexts: vpnRouterCPULoad.setStatus('current')
vpnRouterMemoryUsage = MibScalar((1, 3, 6, 1, 4, 1, 35424, 1, 2, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vpnRouterMemoryUsage.setStatus('current')
vpnRouterSystemTemperature = MibScalar((1, 3, 6, 1, 4, 1, 35424, 1, 2, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vpnRouterSystemTemperature.setStatus('current')
vpnRouterCPUTemperature = MibScalar((1, 3, 6, 1, 4, 1, 35424, 1, 2, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vpnRouterCPUTemperature.setStatus('current')
vpnRouterPowerSupplyFailure = MibScalar((1, 3, 6, 1, 4, 1, 35424, 1, 2, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vpnRouterPowerSupplyFailure.setStatus('current')
vpnRouterFanCount = MibScalar((1, 3, 6, 1, 4, 1, 35424, 1, 3, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vpnRouterFanCount.setStatus('current')
vpnRouterFanTable = MibTable((1, 3, 6, 1, 4, 1, 35424, 1, 3, 2), )
if mibBuilder.loadTexts: vpnRouterFanTable.setStatus('current')
vpnRouterFanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 35424, 1, 3, 2, 1), ).setIndexNames((0, "VIPRINET-MIB", "vpnRouterFanIndex"))
if mibBuilder.loadTexts: vpnRouterFanEntry.setStatus('current')
vpnRouterFanIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 35424, 1, 3, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: vpnRouterFanIndex.setStatus('current')
vpnRouterFanAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 35424, 1, 3, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vpnRouterFanAdminStatus.setStatus('current')
vpnRouterFanOperativeStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 35424, 1, 3, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vpnRouterFanOperativeStatus.setStatus('current')
vpnRouterFanRPM = MibTableColumn((1, 3, 6, 1, 4, 1, 35424, 1, 3, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vpnRouterFanRPM.setStatus('current')
vpnRouterInterfaceCount = MibScalar((1, 3, 6, 1, 4, 1, 35424, 1, 4, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vpnRouterInterfaceCount.setStatus('current')
vpnRouterInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 35424, 1, 4, 2), )
if mibBuilder.loadTexts: vpnRouterInterfaceTable.setStatus('current')
vpnRouterInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 35424, 1, 4, 2, 1), ).setIndexNames((0, "VIPRINET-MIB", "vpnRouterInterfaceIndex"))
if mibBuilder.loadTexts: vpnRouterInterfaceEntry.setStatus('current')
vpnRouterInterfaceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 35424, 1, 4, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: vpnRouterInterfaceIndex.setStatus('current')
vpnRouterInterfaceName = MibTableColumn((1, 3, 6, 1, 4, 1, 35424, 1, 4, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vpnRouterInterfaceName.setStatus('current')
vpnRouterInterfaceAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 35424, 1, 4, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vpnRouterInterfaceAdminStatus.setStatus('current')
vpnRouterInterfaceOperativeStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 35424, 1, 4, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 3))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vpnRouterInterfaceOperativeStatus.setStatus('current')
vpnRouterInterfaceBandwidthToWan = MibTableColumn((1, 3, 6, 1, 4, 1, 35424, 1, 4, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vpnRouterInterfaceBandwidthToWan.setStatus('current')
vpnRouterInterfaceBandwidthFromWan = MibTableColumn((1, 3, 6, 1, 4, 1, 35424, 1, 4, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vpnRouterInterfaceBandwidthFromWan.setStatus('current')
vpnRouterInterfaceTrafficUp = MibTableColumn((1, 3, 6, 1, 4, 1, 35424, 1, 4, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vpnRouterInterfaceTrafficUp.setStatus('current')
vpnRouterInterfaceTrafficDown = MibTableColumn((1, 3, 6, 1, 4, 1, 35424, 1, 4, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vpnRouterInterfaceTrafficDown.setStatus('current')
vpnRouterInterfaceSignalStrength = MibTableColumn((1, 3, 6, 1, 4, 1, 35424, 1, 4, 2, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vpnRouterInterfaceSignalStrength.setStatus('current')
vpnRouterInterfaceServiceType = MibTableColumn((1, 3, 6, 1, 4, 1, 35424, 1, 4, 2, 1, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vpnRouterInterfaceServiceType.setStatus('current')
vpnRouterInterfaceServiceStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 35424, 1, 4, 2, 1, 11), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vpnRouterInterfaceServiceStatus.setStatus('current')
vpnRouterInterfaceRoaming = MibTableColumn((1, 3, 6, 1, 4, 1, 35424, 1, 4, 2, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vpnRouterInterfaceRoaming.setStatus('current')
vpnRouterInterfaceNetworkName = MibTableColumn((1, 3, 6, 1, 4, 1, 35424, 1, 4, 2, 1, 13), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vpnRouterInterfaceNetworkName.setStatus('current')
vpnRouterInterfaceBandInfo = MibTableColumn((1, 3, 6, 1, 4, 1, 35424, 1, 4, 2, 1, 14), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vpnRouterInterfaceBandInfo.setStatus('current')
vpnRouterInterfaceIMSI = MibTableColumn((1, 3, 6, 1, 4, 1, 35424, 1, 4, 2, 1, 15), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vpnRouterInterfaceIMSI.setStatus('current')
vpnRouterInterfaceIMEI = MibTableColumn((1, 3, 6, 1, 4, 1, 35424, 1, 4, 2, 1, 16), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vpnRouterInterfaceIMEI.setStatus('current')
vpnRouterInterfacePINStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 35424, 1, 4, 2, 1, 17), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vpnRouterInterfacePINStatus.setStatus('current')
vpnRouterInterfaceRFBand = MibTableColumn((1, 3, 6, 1, 4, 1, 35424, 1, 4, 2, 1, 18), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vpnRouterInterfaceRFBand.setStatus('current')
vpnRouterInterfaceRFChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 35424, 1, 4, 2, 1, 19), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vpnRouterInterfaceRFChannel.setStatus('current')
vpnRouterInterfaceSyncrateUpstream = MibTableColumn((1, 3, 6, 1, 4, 1, 35424, 1, 4, 2, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vpnRouterInterfaceSyncrateUpstream.setStatus('current')
vpnRouterInterfaceSyncrateDownstream = MibTableColumn((1, 3, 6, 1, 4, 1, 35424, 1, 4, 2, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vpnRouterInterfaceSyncrateDownstream.setStatus('current')
vpnRouterTunnelCount = MibScalar((1, 3, 6, 1, 4, 1, 35424, 1, 5, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vpnRouterTunnelCount.setStatus('current')
vpnRouterTunnelTable = MibTable((1, 3, 6, 1, 4, 1, 35424, 1, 5, 2), )
if mibBuilder.loadTexts: vpnRouterTunnelTable.setStatus('current')
vpnRouterTunnelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 35424, 1, 5, 2, 1), ).setIndexNames((0, "VIPRINET-MIB", "vpnRouterTunnelIndex"))
if mibBuilder.loadTexts: vpnRouterTunnelEntry.setStatus('current')
vpnRouterTunnelIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 35424, 1, 5, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: vpnRouterTunnelIndex.setStatus('current')
vpnRouterTunnelName = MibTableColumn((1, 3, 6, 1, 4, 1, 35424, 1, 5, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vpnRouterTunnelName.setStatus('current')
vpnRouterTunnelAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 35424, 1, 5, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vpnRouterTunnelAdminStatus.setStatus('current')
vpnRouterTunnelOperativeStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 35424, 1, 5, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vpnRouterTunnelOperativeStatus.setStatus('current')
vpnRouterTunnelCumulatedBandwidthToWan = MibTableColumn((1, 3, 6, 1, 4, 1, 35424, 1, 5, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vpnRouterTunnelCumulatedBandwidthToWan.setStatus('current')
vpnRouterTunnelCumulatedBandwidthFromWan = MibTableColumn((1, 3, 6, 1, 4, 1, 35424, 1, 5, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vpnRouterTunnelCumulatedBandwidthFromWan.setStatus('current')
vpnRouterTunnelCurrentCumulatedBandwidthToWan = MibTableColumn((1, 3, 6, 1, 4, 1, 35424, 1, 5, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vpnRouterTunnelCurrentCumulatedBandwidthToWan.setStatus('current')
vpnRouterTunnelCurrentCumulatedBandwidthFromWan = MibTableColumn((1, 3, 6, 1, 4, 1, 35424, 1, 5, 2, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vpnRouterTunnelCurrentCumulatedBandwidthFromWan.setStatus('current')
vpnRouterTunnelTrafficUp = MibTableColumn((1, 3, 6, 1, 4, 1, 35424, 1, 5, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vpnRouterTunnelTrafficUp.setStatus('current')
vpnRouterTunnelTrafficDown = MibTableColumn((1, 3, 6, 1, 4, 1, 35424, 1, 5, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vpnRouterTunnelTrafficDown.setStatus('current')
vpnRouterTunnelRemoteRouterSerial = MibTableColumn((1, 3, 6, 1, 4, 1, 35424, 1, 5, 2, 1, 11), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vpnRouterTunnelRemoteRouterSerial.setStatus('current')
vpnRouterTunnelChannelCount = MibScalar((1, 3, 6, 1, 4, 1, 35424, 1, 6, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vpnRouterTunnelChannelCount.setStatus('current')
vpnRouterTunnelChannelTable = MibTable((1, 3, 6, 1, 4, 1, 35424, 1, 6, 2), )
if mibBuilder.loadTexts: vpnRouterTunnelChannelTable.setStatus('current')
vpnRouterTunnelChannelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 35424, 1, 6, 2, 1), ).setIndexNames((0, "VIPRINET-MIB", "vpnRouterTunnelChannelIndex"))
if mibBuilder.loadTexts: vpnRouterTunnelChannelEntry.setStatus('current')
vpnRouterTunnelChannelIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 35424, 1, 6, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: vpnRouterTunnelChannelIndex.setStatus('current')
vpnRouterTunnelChannelName = MibTableColumn((1, 3, 6, 1, 4, 1, 35424, 1, 6, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vpnRouterTunnelChannelName.setStatus('current')
vpnRouterTunnelChannelAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 35424, 1, 6, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vpnRouterTunnelChannelAdminStatus.setStatus('current')
vpnRouterTunnelChannelOperativeStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 35424, 1, 6, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vpnRouterTunnelChannelOperativeStatus.setStatus('current')
vpnRouterTunnelChannelMaxBandwidthToWan = MibTableColumn((1, 3, 6, 1, 4, 1, 35424, 1, 6, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vpnRouterTunnelChannelMaxBandwidthToWan.setStatus('current')
vpnRouterTunnelChannelMaxBandwidthFromWan = MibTableColumn((1, 3, 6, 1, 4, 1, 35424, 1, 6, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vpnRouterTunnelChannelMaxBandwidthFromWan.setStatus('current')
vpnRouterTunnelChannelCurrentBandwidthToWan = MibTableColumn((1, 3, 6, 1, 4, 1, 35424, 1, 6, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vpnRouterTunnelChannelCurrentBandwidthToWan.setStatus('current')
vpnRouterTunnelChannelCurrentBandwidthFromWan = MibTableColumn((1, 3, 6, 1, 4, 1, 35424, 1, 6, 2, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vpnRouterTunnelChannelCurrentBandwidthFromWan.setStatus('current')
vpnRouterTunnelChannelTrafficUp = MibTableColumn((1, 3, 6, 1, 4, 1, 35424, 1, 6, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vpnRouterTunnelChannelTrafficUp.setStatus('current')
vpnRouterTunnelChannelTrafficDown = MibTableColumn((1, 3, 6, 1, 4, 1, 35424, 1, 6, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vpnRouterTunnelChannelTrafficDown.setStatus('current')
vpnRouterTunnelChannelReferencedTunnel = MibTableColumn((1, 3, 6, 1, 4, 1, 35424, 1, 6, 2, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vpnRouterTunnelChannelReferencedTunnel.setStatus('current')
vpnRouterTunnelChannelIsBackup = MibTableColumn((1, 3, 6, 1, 4, 1, 35424, 1, 6, 2, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vpnRouterTunnelChannelIsBackup.setStatus('current')
vpnRouterTunnelChannelModuleSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 35424, 1, 6, 2, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 6))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vpnRouterTunnelChannelModuleSlot.setStatus('current')
vpnRouterTunnelChannelPacketLoss = MibTableColumn((1, 3, 6, 1, 4, 1, 35424, 1, 6, 2, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vpnRouterTunnelChannelPacketLoss.setStatus('current')
vpnRouterTunnelChannelLinkStability = MibTableColumn((1, 3, 6, 1, 4, 1, 35424, 1, 6, 2, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vpnRouterTunnelChannelLinkStability.setStatus('current')
vpnRouterConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 35424, 1, 7))
vpnRouterGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 35424, 1, 7, 1))
vpnRouterCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 35424, 1, 7, 2))
vpnRouterReadOnlyCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 35424, 1, 7, 2, 1)).setObjects(("VIPRINET-MIB", "vpnRouterObjects"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vpnRouterReadOnlyCompliance = vpnRouterReadOnlyCompliance.setStatus('current')
vpnRouterObjects = ObjectGroup((1, 3, 6, 1, 4, 1, 35424, 1, 7, 1, 1)).setObjects(("VIPRINET-MIB", "vpnRouterTunnelChannelName"), ("VIPRINET-MIB", "vpnRouterTunnelChannelAdminStatus"), ("VIPRINET-MIB", "vpnRouterTunnelChannelOperativeStatus"), ("VIPRINET-MIB", "vpnRouterTunnelChannelMaxBandwidthToWan"), ("VIPRINET-MIB", "vpnRouterTunnelChannelMaxBandwidthFromWan"), ("VIPRINET-MIB", "vpnRouterTunnelChannelCurrentBandwidthToWan"), ("VIPRINET-MIB", "vpnRouterTunnelChannelCurrentBandwidthFromWan"), ("VIPRINET-MIB", "vpnRouterTunnelChannelTrafficUp"), ("VIPRINET-MIB", "vpnRouterTunnelChannelTrafficDown"), ("VIPRINET-MIB", "vpnRouterTunnelChannelReferencedTunnel"), ("VIPRINET-MIB", "vpnRouterTunnelChannelIsBackup"), ("VIPRINET-MIB", "vpnRouterTunnelChannelModuleSlot"), ("VIPRINET-MIB", "vpnRouterTunnelChannelPacketLoss"), ("VIPRINET-MIB", "vpnRouterTunnelChannelLinkStability"), ("VIPRINET-MIB", "vpnRouterTunnelName"), ("VIPRINET-MIB", "vpnRouterTunnelAdminStatus"), ("VIPRINET-MIB", "vpnRouterTunnelOperativeStatus"), ("VIPRINET-MIB", "vpnRouterTunnelCumulatedBandwidthToWan"), ("VIPRINET-MIB", "vpnRouterTunnelCumulatedBandwidthFromWan"), ("VIPRINET-MIB", "vpnRouterTunnelCurrentCumulatedBandwidthToWan"), ("VIPRINET-MIB", "vpnRouterTunnelCurrentCumulatedBandwidthFromWan"), ("VIPRINET-MIB", "vpnRouterTunnelTrafficUp"), ("VIPRINET-MIB", "vpnRouterTunnelTrafficDown"), ("VIPRINET-MIB", "vpnRouterTunnelRemoteRouterSerial"), ("VIPRINET-MIB", "vpnRouterInterfaceName"), ("VIPRINET-MIB", "vpnRouterInterfaceAdminStatus"), ("VIPRINET-MIB", "vpnRouterInterfaceOperativeStatus"), ("VIPRINET-MIB", "vpnRouterInterfaceBandwidthToWan"), ("VIPRINET-MIB", "vpnRouterInterfaceBandwidthFromWan"), ("VIPRINET-MIB", "vpnRouterInterfaceTrafficUp"), ("VIPRINET-MIB", "vpnRouterInterfaceTrafficDown"), ("VIPRINET-MIB", "vpnRouterFanAdminStatus"), ("VIPRINET-MIB", "vpnRouterFanOperativeStatus"), ("VIPRINET-MIB", "vpnRouterFanRPM"), ("VIPRINET-MIB", "vpnRouterName"), ("VIPRINET-MIB", "vpnRouterSerial"), ("VIPRINET-MIB", "vpnRouterModel"), ("VIPRINET-MIB", "vpnRouterFirmware"), ("VIPRINET-MIB", "vpnRouterMode"), ("VIPRINET-MIB", "vpnRouteruptime"), ("VIPRINET-MIB", "vpnRouterFirmwareStatus"), ("VIPRINET-MIB", "vpnRouterCPULoad"), ("VIPRINET-MIB", "vpnRouterMemoryUsage"), ("VIPRINET-MIB", "vpnRouterSystemTemperature"), ("VIPRINET-MIB", "vpnRouterCPUTemperature"), ("VIPRINET-MIB", "vpnRouterPowerSupplyFailure"), ("VIPRINET-MIB", "vpnRouterFanCount"), ("VIPRINET-MIB", "vpnRouterInterfaceCount"), ("VIPRINET-MIB", "vpnRouterTunnelCount"), ("VIPRINET-MIB", "vpnRouterTunnelChannelCount"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vpnRouterObjects = vpnRouterObjects.setStatus('current')
mibBuilder.exportSymbols("VIPRINET-MIB", vpnRouterTunnelChannelCount=vpnRouterTunnelChannelCount, vpnRouterInterfaceTrafficDown=vpnRouterInterfaceTrafficDown, vpnRouterModel=vpnRouterModel, vpnRouterInterfaceRFChannel=vpnRouterInterfaceRFChannel, vpnRouterInterfaceRFBand=vpnRouterInterfaceRFBand, vpnRouterTunnelName=vpnRouterTunnelName, vpnRouterTunnelChannelEntry=vpnRouterTunnelChannelEntry, vpnRouterInterfaceEntry=vpnRouterInterfaceEntry, vpnRouterTunnelChannelTrafficUp=vpnRouterTunnelChannelTrafficUp, vpnRouterTunnelChannelIndex=vpnRouterTunnelChannelIndex, vpnRouterInterfaceSignalStrength=vpnRouterInterfaceSignalStrength, vpnRouterTunnelRemoteRouterSerial=vpnRouterTunnelRemoteRouterSerial, PYSNMP_MODULE_ID=viprinet, vpnRouterTunnelChannelCurrentBandwidthFromWan=vpnRouterTunnelChannelCurrentBandwidthFromWan, vpnRouterFirmware=vpnRouterFirmware, vpnRouterMode=vpnRouterMode, vpnRouterTunnelCurrentCumulatedBandwidthToWan=vpnRouterTunnelCurrentCumulatedBandwidthToWan, vpnRouterTunnelChannelPacketLoss=vpnRouterTunnelChannelPacketLoss, vpnRouterCompliances=vpnRouterCompliances, vpnRouterInterfaceBandInfo=vpnRouterInterfaceBandInfo, vpnRouterInterfaceOperativeStatus=vpnRouterInterfaceOperativeStatus, vpnRouterInterfaceIndex=vpnRouterInterfaceIndex, vpnRouteruptime=vpnRouteruptime, vpnRouterInterfaceBandwidthToWan=vpnRouterInterfaceBandwidthToWan, vpnRouterFanOperativeStatus=vpnRouterFanOperativeStatus, vpnRouterTunnelChannelMaxBandwidthFromWan=vpnRouterTunnelChannelMaxBandwidthFromWan, vpnRouterInterfaceTrafficUp=vpnRouterInterfaceTrafficUp, vpnRouterTunnelTrafficUp=vpnRouterTunnelTrafficUp, vpnRouterTunnelCount=vpnRouterTunnelCount, vpnRouterReadOnlyCompliance=vpnRouterReadOnlyCompliance, vpnRouterFanAdminStatus=vpnRouterFanAdminStatus, vpnRouterTunnelChannels=vpnRouterTunnelChannels, vpnRouterInterfaceCount=vpnRouterInterfaceCount, vpnRouterFans=vpnRouterFans, vpnRouterInterfaceIMSI=vpnRouterInterfaceIMSI, vpnRouterInterfaceName=vpnRouterInterfaceName, vpnRouterFirmwareStatus=vpnRouterFirmwareStatus, vpnRouterFanCount=vpnRouterFanCount, vpnRouterInterfaceSyncrateDownstream=vpnRouterInterfaceSyncrateDownstream, vpnRouterTunnelCumulatedBandwidthFromWan=vpnRouterTunnelCumulatedBandwidthFromWan, vpnRouterFanEntry=vpnRouterFanEntry, vpnRouterSystemTemperature=vpnRouterSystemTemperature, vpnRouterTunnelChannelCurrentBandwidthToWan=vpnRouterTunnelChannelCurrentBandwidthToWan, vpnRouterCPULoad=vpnRouterCPULoad, vpnRouter=vpnRouter, vpnRouterTunnelChannelName=vpnRouterTunnelChannelName, vpnRouterTunnelChannelTrafficDown=vpnRouterTunnelChannelTrafficDown, vpnRouterCPUTemperature=vpnRouterCPUTemperature, vpnRouterHealth=vpnRouterHealth, vpnRouterInterfaceServiceType=vpnRouterInterfaceServiceType, vpnRouterTunnelChannelAdminStatus=vpnRouterTunnelChannelAdminStatus, vpnRouterObjects=vpnRouterObjects, viprinet=viprinet, vpnRouterFanRPM=vpnRouterFanRPM, vpnRouterTunnelAdminStatus=vpnRouterTunnelAdminStatus, vpnRouterPowerSupplyFailure=vpnRouterPowerSupplyFailure, vpnRouterInterfaceIMEI=vpnRouterInterfaceIMEI, vpnRouterTunnelEntry=vpnRouterTunnelEntry, vpnRouterName=vpnRouterName, vpnRouterMemoryUsage=vpnRouterMemoryUsage, vpnRouterTunnels=vpnRouterTunnels, vpnRouterTunnelChannelTable=vpnRouterTunnelChannelTable, vpnRouterTunnelTable=vpnRouterTunnelTable, vpnRouterInterfaceBandwidthFromWan=vpnRouterInterfaceBandwidthFromWan, vpnRouterInterfaceNetworkName=vpnRouterInterfaceNetworkName, vpnRouterTunnelCumulatedBandwidthToWan=vpnRouterTunnelCumulatedBandwidthToWan, vpnRouterGroups=vpnRouterGroups, vpnRouterTunnelTrafficDown=vpnRouterTunnelTrafficDown, vpnRouterInfo=vpnRouterInfo, vpnRouterInterfaceAdminStatus=vpnRouterInterfaceAdminStatus, vpnRouterTunnelCurrentCumulatedBandwidthFromWan=vpnRouterTunnelCurrentCumulatedBandwidthFromWan, vpnRouterFanTable=vpnRouterFanTable, vpnRouterInterfacePINStatus=vpnRouterInterfacePINStatus, vpnRouterTunnelChannelModuleSlot=vpnRouterTunnelChannelModuleSlot, vpnRouterTunnelChannelReferencedTunnel=vpnRouterTunnelChannelReferencedTunnel, vpnRouterInterfaceTable=vpnRouterInterfaceTable, vpnRouterSerial=vpnRouterSerial, vpnRouterConformance=vpnRouterConformance, vpnRouterInterfaceSyncrateUpstream=vpnRouterInterfaceSyncrateUpstream, vpnRouterTunnelChannelLinkStability=vpnRouterTunnelChannelLinkStability, vpnRouterFanIndex=vpnRouterFanIndex, vpnRouterTunnelOperativeStatus=vpnRouterTunnelOperativeStatus, vpnRouterTunnelChannelOperativeStatus=vpnRouterTunnelChannelOperativeStatus, vpnRouterInterfaceRoaming=vpnRouterInterfaceRoaming, vpnRouterTunnelChannelMaxBandwidthToWan=vpnRouterTunnelChannelMaxBandwidthToWan, vpnRouterTunnelIndex=vpnRouterTunnelIndex, vpnRouterTunnelChannelIsBackup=vpnRouterTunnelChannelIsBackup, vpnRouterInterfaces=vpnRouterInterfaces, vpnRouterInterfaceServiceStatus=vpnRouterInterfaceServiceStatus)
