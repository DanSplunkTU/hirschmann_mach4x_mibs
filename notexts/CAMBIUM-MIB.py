#
# PySNMP MIB module CAMBIUM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cambium/cnpilote/CAMBIUM-MIB
# Produced by pysmi-1.1.3 at Sun Nov 21 00:36:16 2021
# On host fv-az39-63 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Integer32, iso, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Bits, MibIdentifier, NotificationType, ModuleIdentity, snmpModules, TimeTicks, Unsigned32, Gauge32, enterprises, IpAddress, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "iso", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Bits", "MibIdentifier", "NotificationType", "ModuleIdentity", "snmpModules", "TimeTicks", "Unsigned32", "Gauge32", "enterprises", "IpAddress", "ObjectIdentity")
TextualConvention, MacAddress, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "MacAddress", "DisplayString")
cnPilotMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 17713, 22))
cnPilotMIB.setRevisions(('2015-09-09 12:38',))
if mibBuilder.loadTexts: cnPilotMIB.setLastUpdated('201509091238Z')
if mibBuilder.loadTexts: cnPilotMIB.setOrganization('Cambium Networks Inc.')
cambium = MibIdentifier((1, 3, 6, 1, 4, 1, 17713))
cambiumStateGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 17713, 22, 1))
cambiumAccessPointTable = MibTable((1, 3, 6, 1, 4, 1, 17713, 22, 1, 1), )
if mibBuilder.loadTexts: cambiumAccessPointTable.setStatus('current')
cambiumAccessPointEntry = MibTableRow((1, 3, 6, 1, 4, 1, 17713, 22, 1, 1, 1), ).setIndexNames((0, "CAMBIUM-MIB", "cambiumAPMACAddress"))
if mibBuilder.loadTexts: cambiumAccessPointEntry.setStatus('current')
cambiumAPMACAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 17713, 22, 1, 1, 1, 1), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cambiumAPMACAddress.setStatus('current')
cambiumAPName = MibTableColumn((1, 3, 6, 1, 4, 1, 17713, 22, 1, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cambiumAPName.setStatus('current')
cambiumAPIPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 17713, 22, 1, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cambiumAPIPAddress.setStatus('current')
cambiumAPSerialNum = MibTableColumn((1, 3, 6, 1, 4, 1, 17713, 22, 1, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cambiumAPSerialNum.setStatus('current')
cambiumAPModel = MibTableColumn((1, 3, 6, 1, 4, 1, 17713, 22, 1, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cambiumAPModel.setStatus('current')
cambiumAPCPUUtilization = MibTableColumn((1, 3, 6, 1, 4, 1, 17713, 22, 1, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cambiumAPCPUUtilization.setStatus('current')
cambiumAPMemoryFree = MibTableColumn((1, 3, 6, 1, 4, 1, 17713, 22, 1, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cambiumAPMemoryFree.setStatus('current')
cambiumAPSWVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 17713, 22, 1, 1, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cambiumAPSWVersion.setStatus('current')
cambiumAPUptime = MibTableColumn((1, 3, 6, 1, 4, 1, 17713, 22, 1, 1, 1, 9), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cambiumAPUptime.setStatus('current')
cambiumAPHWType = MibTableColumn((1, 3, 6, 1, 4, 1, 17713, 22, 1, 1, 1, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cambiumAPHWType.setStatus('current')
cambiumAPRegulatory = MibTableColumn((1, 3, 6, 1, 4, 1, 17713, 22, 1, 1, 1, 11), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cambiumAPRegulatory.setStatus('current')
cambiumAPCnmConstaus = MibTableColumn((1, 3, 6, 1, 4, 1, 17713, 22, 1, 1, 1, 12), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cambiumAPCnmConstaus.setStatus('current')
cambiumAPCnmAccID = MibTableColumn((1, 3, 6, 1, 4, 1, 17713, 22, 1, 1, 1, 13), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cambiumAPCnmAccID.setStatus('current')
cambiumAPTotalClients = MibTableColumn((1, 3, 6, 1, 4, 1, 17713, 22, 1, 1, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cambiumAPTotalClients.setStatus('current')
cambiumAPCheckUpgradeStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 17713, 22, 1, 1, 1, 15), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cambiumAPCheckUpgradeStatus.setStatus('current')
cambiumRadioTable = MibTable((1, 3, 6, 1, 4, 1, 17713, 22, 1, 2), )
if mibBuilder.loadTexts: cambiumRadioTable.setStatus('current')
cambiumRadioEntry = MibTableRow((1, 3, 6, 1, 4, 1, 17713, 22, 1, 2, 1), ).setIndexNames((0, "CAMBIUM-MIB", "cambiumRadioIndex"))
if mibBuilder.loadTexts: cambiumRadioEntry.setStatus('current')
cambiumRadioIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 17713, 22, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cambiumRadioIndex.setStatus('current')
cambiumRadioMACAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 17713, 22, 1, 2, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cambiumRadioMACAddress.setStatus('current')
cambiumRadioBandType = MibTableColumn((1, 3, 6, 1, 4, 1, 17713, 22, 1, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cambiumRadioBandType.setStatus('current')
cambiumRadioWlan = MibTableColumn((1, 3, 6, 1, 4, 1, 17713, 22, 1, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cambiumRadioWlan.setStatus('current')
cambiumRadioNumClients = MibTableColumn((1, 3, 6, 1, 4, 1, 17713, 22, 1, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cambiumRadioNumClients.setStatus('current')
cambiumRadioChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 17713, 22, 1, 2, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cambiumRadioChannel.setStatus('current')
cambiumRadioChannelWidth = MibTableColumn((1, 3, 6, 1, 4, 1, 17713, 22, 1, 2, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cambiumRadioChannelWidth.setStatus('current')
cambiumRadioTransmitPower = MibTableColumn((1, 3, 6, 1, 4, 1, 17713, 22, 1, 2, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cambiumRadioTransmitPower.setStatus('current')
cambiumRadioTotalTxPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 17713, 22, 1, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cambiumRadioTotalTxPackets.setStatus('current')
cambiumRadioTotalRxPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 17713, 22, 1, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cambiumRadioTotalRxPackets.setStatus('current')
cambiumRadioTxDataBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 17713, 22, 1, 2, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cambiumRadioTxDataBytes.setStatus('current')
cambiumRadioRxDataBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 17713, 22, 1, 2, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cambiumRadioRxDataBytes.setStatus('current')
cambiumRadioState = MibTableColumn((1, 3, 6, 1, 4, 1, 17713, 22, 1, 2, 1, 13), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cambiumRadioState.setStatus('current')
cambiumRadioDfsStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 17713, 22, 1, 2, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cambiumRadioDfsStatus.setStatus('current')
cambiumRadioDfsDetect = MibTableColumn((1, 3, 6, 1, 4, 1, 17713, 22, 1, 2, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cambiumRadioDfsDetect.setStatus('current')
cambiumRadioNoiseFloor = MibTableColumn((1, 3, 6, 1, 4, 1, 17713, 22, 1, 2, 1, 16), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cambiumRadioNoiseFloor.setStatus('current')
cambiumRadioInterference = MibTableColumn((1, 3, 6, 1, 4, 1, 17713, 22, 1, 2, 1, 17), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cambiumRadioInterference.setStatus('current')
cambiumRadioAirtime = MibTableColumn((1, 3, 6, 1, 4, 1, 17713, 22, 1, 2, 1, 18), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cambiumRadioAirtime.setStatus('current')
cambiumClientTable = MibTable((1, 3, 6, 1, 4, 1, 17713, 22, 1, 3), )
if mibBuilder.loadTexts: cambiumClientTable.setStatus('current')
cambiumClientEntry = MibTableRow((1, 3, 6, 1, 4, 1, 17713, 22, 1, 3, 1), ).setIndexNames((0, "CAMBIUM-MIB", "cambiumClientMACAddressIndex"))
if mibBuilder.loadTexts: cambiumClientEntry.setStatus('current')
cambiumClientMACAddressIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 17713, 22, 1, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cambiumClientMACAddressIndex.setStatus('current')
cambiumClientMACAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 17713, 22, 1, 3, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cambiumClientMACAddress.setStatus('current')
cambiumClientIPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 17713, 22, 1, 3, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cambiumClientIPAddress.setStatus('current')
cambiumClientName = MibTableColumn((1, 3, 6, 1, 4, 1, 17713, 22, 1, 3, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cambiumClientName.setStatus('current')
cambiumClientSsid = MibTableColumn((1, 3, 6, 1, 4, 1, 17713, 22, 1, 3, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cambiumClientSsid.setStatus('current')
cambiumClientVendorName = MibTableColumn((1, 3, 6, 1, 4, 1, 17713, 22, 1, 3, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cambiumClientVendorName.setStatus('current')
cambiumClientHwmode = MibTableColumn((1, 3, 6, 1, 4, 1, 17713, 22, 1, 3, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cambiumClientHwmode.setStatus('current')
cambiumClientRadioIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 17713, 22, 1, 3, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cambiumClientRadioIndex.setStatus('current')
cambiumClientWlan = MibTableColumn((1, 3, 6, 1, 4, 1, 17713, 22, 1, 3, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cambiumClientWlan.setStatus('current')
cambiumClientVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 17713, 22, 1, 3, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cambiumClientVlan.setStatus('current')
cambiumClientSNR = MibTableColumn((1, 3, 6, 1, 4, 1, 17713, 22, 1, 3, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cambiumClientSNR.setStatus('current')
cambiumClientTxRate = MibTableColumn((1, 3, 6, 1, 4, 1, 17713, 22, 1, 3, 1, 12), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cambiumClientTxRate.setStatus('current')
cambiumClientTotalTxPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 17713, 22, 1, 3, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cambiumClientTotalTxPackets.setStatus('current')
cambiumClientTxDataBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 17713, 22, 1, 3, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cambiumClientTxDataBytes.setStatus('current')
cambiumClientTotalRxPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 17713, 22, 1, 3, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cambiumClientTotalRxPackets.setStatus('current')
cambiumClientRxDataBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 17713, 22, 1, 3, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cambiumClientRxDataBytes.setStatus('current')
cambiumWlanTable = MibTable((1, 3, 6, 1, 4, 1, 17713, 22, 1, 4), )
if mibBuilder.loadTexts: cambiumWlanTable.setStatus('current')
cambiumWlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 17713, 22, 1, 4, 1), ).setIndexNames((0, "CAMBIUM-MIB", "cambiumWlanIndex"))
if mibBuilder.loadTexts: cambiumWlanEntry.setStatus('current')
cambiumWlanIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 17713, 22, 1, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cambiumWlanIndex.setStatus('current')
cambiumWlanSsid = MibTableColumn((1, 3, 6, 1, 4, 1, 17713, 22, 1, 4, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cambiumWlanSsid.setStatus('current')
cambiumWlanBand = MibTableColumn((1, 3, 6, 1, 4, 1, 17713, 22, 1, 4, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cambiumWlanBand.setStatus('current')
cambiumWlanVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 17713, 22, 1, 4, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cambiumWlanVlan.setStatus('current')
cambiumWlanSecurity = MibTableColumn((1, 3, 6, 1, 4, 1, 17713, 22, 1, 4, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cambiumWlanSecurity.setStatus('current')
cambiumWlanGuestAccess = MibTableColumn((1, 3, 6, 1, 4, 1, 17713, 22, 1, 4, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cambiumWlanGuestAccess.setStatus('current')
cambiumWlanNumClients = MibTableColumn((1, 3, 6, 1, 4, 1, 17713, 22, 1, 4, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cambiumWlanNumClients.setStatus('current')
cambiumWlanTotalTxPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 17713, 22, 1, 4, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cambiumWlanTotalTxPackets.setStatus('current')
cambiumWlanTxDataBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 17713, 22, 1, 4, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cambiumWlanTxDataBytes.setStatus('current')
cambiumWlanTotalRxPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 17713, 22, 1, 4, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cambiumWlanTotalRxPackets.setStatus('current')
cambiumWlanRxDataBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 17713, 22, 1, 4, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cambiumWlanRxDataBytes.setStatus('current')
cambiumMeshClientTable = MibTable((1, 3, 6, 1, 4, 1, 17713, 22, 1, 5), )
if mibBuilder.loadTexts: cambiumMeshClientTable.setStatus('current')
cambiumMeshClientEntry = MibTableRow((1, 3, 6, 1, 4, 1, 17713, 22, 1, 5, 1), ).setIndexNames((0, "CAMBIUM-MIB", "cambiumMeshClientMACAddressIndex"))
if mibBuilder.loadTexts: cambiumMeshClientEntry.setStatus('current')
cambiumMeshClientMACAddressIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 17713, 22, 1, 5, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cambiumMeshClientMACAddressIndex.setStatus('current')
cambiumMeshClientMACAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 17713, 22, 1, 5, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cambiumMeshClientMACAddress.setStatus('current')
cambiumMeshClientBaseMACAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 17713, 22, 1, 5, 1, 3), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cambiumMeshClientBaseMACAddress.setStatus('current')
cambiumMeshClientIPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 17713, 22, 1, 5, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cambiumMeshClientIPAddress.setStatus('current')
cambiumMeshClientName = MibTableColumn((1, 3, 6, 1, 4, 1, 17713, 22, 1, 5, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cambiumMeshClientName.setStatus('current')
cambiumMeshClientSsid = MibTableColumn((1, 3, 6, 1, 4, 1, 17713, 22, 1, 5, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cambiumMeshClientSsid.setStatus('current')
cambiumMeshClientRadioBand = MibTableColumn((1, 3, 6, 1, 4, 1, 17713, 22, 1, 5, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cambiumMeshClientRadioBand.setStatus('current')
cambiumMeshClientSNR = MibTableColumn((1, 3, 6, 1, 4, 1, 17713, 22, 1, 5, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cambiumMeshClientSNR.setStatus('current')
cambiumMeshClientRSSI = MibTableColumn((1, 3, 6, 1, 4, 1, 17713, 22, 1, 5, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cambiumMeshClientRSSI.setStatus('current')
cambiumMeshClientStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 17713, 22, 1, 5, 1, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cambiumMeshClientStatus.setStatus('current')
cambiumMeshClientDataRate = MibTableColumn((1, 3, 6, 1, 4, 1, 17713, 22, 1, 5, 1, 11), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cambiumMeshClientDataRate.setStatus('current')
cambiumMeshClientTotalTxPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 17713, 22, 1, 5, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cambiumMeshClientTotalTxPackets.setStatus('current')
cambiumMeshClientTxDataBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 17713, 22, 1, 5, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cambiumMeshClientTxDataBytes.setStatus('current')
cambiumMeshClientTotalRxPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 17713, 22, 1, 5, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cambiumMeshClientTotalRxPackets.setStatus('current')
cambiumMeshClientRxDataBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 17713, 22, 1, 5, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cambiumMeshClientRxDataBytes.setStatus('current')
cambiumAPSetIPAddress = MibScalar((1, 3, 6, 1, 4, 1, 17713, 22, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cambiumAPSetIPAddress.setStatus('current')
cambiumAPReboot = MibScalar((1, 3, 6, 1, 4, 1, 17713, 22, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cambiumAPReboot.setStatus('current')
mibBuilder.exportSymbols("CAMBIUM-MIB", cambiumWlanTotalTxPackets=cambiumWlanTotalTxPackets, cambiumMeshClientMACAddressIndex=cambiumMeshClientMACAddressIndex, cambiumClientName=cambiumClientName, cambiumWlanTable=cambiumWlanTable, cambiumClientSsid=cambiumClientSsid, cambiumRadioEntry=cambiumRadioEntry, cambiumClientHwmode=cambiumClientHwmode, cambiumClientTxRate=cambiumClientTxRate, cambiumAPName=cambiumAPName, cambiumClientSNR=cambiumClientSNR, cambiumMeshClientSNR=cambiumMeshClientSNR, cambiumRadioState=cambiumRadioState, cambiumAPCnmConstaus=cambiumAPCnmConstaus, cambiumWlanGuestAccess=cambiumWlanGuestAccess, cambiumMeshClientMACAddress=cambiumMeshClientMACAddress, PYSNMP_MODULE_ID=cnPilotMIB, cambiumAPModel=cambiumAPModel, cambiumMeshClientRadioBand=cambiumMeshClientRadioBand, cambiumClientIPAddress=cambiumClientIPAddress, cambiumAPCPUUtilization=cambiumAPCPUUtilization, cambiumRadioTotalTxPackets=cambiumRadioTotalTxPackets, cambiumMeshClientIPAddress=cambiumMeshClientIPAddress, cambiumMeshClientTable=cambiumMeshClientTable, cambiumClientTable=cambiumClientTable, cambiumAccessPointEntry=cambiumAccessPointEntry, cambiumAPSetIPAddress=cambiumAPSetIPAddress, cambiumWlanIndex=cambiumWlanIndex, cambiumMeshClientBaseMACAddress=cambiumMeshClientBaseMACAddress, cambiumWlanTxDataBytes=cambiumWlanTxDataBytes, cambiumRadioBandType=cambiumRadioBandType, cambiumAPMACAddress=cambiumAPMACAddress, cambiumRadioTxDataBytes=cambiumRadioTxDataBytes, cambiumMeshClientEntry=cambiumMeshClientEntry, cambiumRadioRxDataBytes=cambiumRadioRxDataBytes, cambiumAPSWVersion=cambiumAPSWVersion, cambiumAPMemoryFree=cambiumAPMemoryFree, cambiumAPCnmAccID=cambiumAPCnmAccID, cambiumAPSerialNum=cambiumAPSerialNum, cambiumClientWlan=cambiumClientWlan, cambiumRadioIndex=cambiumRadioIndex, cambiumAPReboot=cambiumAPReboot, cambiumRadioAirtime=cambiumRadioAirtime, cambiumRadioTransmitPower=cambiumRadioTransmitPower, cambiumClientEntry=cambiumClientEntry, cambiumRadioTotalRxPackets=cambiumRadioTotalRxPackets, cambiumAPUptime=cambiumAPUptime, cambiumClientRadioIndex=cambiumClientRadioIndex, cambiumAccessPointTable=cambiumAccessPointTable, cambiumClientMACAddressIndex=cambiumClientMACAddressIndex, cambiumRadioDfsDetect=cambiumRadioDfsDetect, cambiumRadioInterference=cambiumRadioInterference, cambiumAPRegulatory=cambiumAPRegulatory, cambiumAPHWType=cambiumAPHWType, cambiumRadioNumClients=cambiumRadioNumClients, cambiumMeshClientName=cambiumMeshClientName, cambiumClientVlan=cambiumClientVlan, cambiumMeshClientRSSI=cambiumMeshClientRSSI, cambiumWlanBand=cambiumWlanBand, cambiumWlanTotalRxPackets=cambiumWlanTotalRxPackets, cambiumMeshClientStatus=cambiumMeshClientStatus, cambiumRadioTable=cambiumRadioTable, cambiumRadioChannel=cambiumRadioChannel, cambiumClientMACAddress=cambiumClientMACAddress, cambiumMeshClientSsid=cambiumMeshClientSsid, cambiumWlanVlan=cambiumWlanVlan, cambiumMeshClientTotalRxPackets=cambiumMeshClientTotalRxPackets, cambiumMeshClientTotalTxPackets=cambiumMeshClientTotalTxPackets, cambiumWlanSecurity=cambiumWlanSecurity, cambiumAPIPAddress=cambiumAPIPAddress, cambiumWlanEntry=cambiumWlanEntry, cnPilotMIB=cnPilotMIB, cambiumAPCheckUpgradeStatus=cambiumAPCheckUpgradeStatus, cambiumStateGroup=cambiumStateGroup, cambiumClientTxDataBytes=cambiumClientTxDataBytes, cambiumRadioWlan=cambiumRadioWlan, cambiumRadioNoiseFloor=cambiumRadioNoiseFloor, cambiumClientRxDataBytes=cambiumClientRxDataBytes, cambiumMeshClientRxDataBytes=cambiumMeshClientRxDataBytes, cambium=cambium, cambiumAPTotalClients=cambiumAPTotalClients, cambiumRadioMACAddress=cambiumRadioMACAddress, cambiumClientTotalTxPackets=cambiumClientTotalTxPackets, cambiumWlanRxDataBytes=cambiumWlanRxDataBytes, cambiumMeshClientDataRate=cambiumMeshClientDataRate, cambiumRadioChannelWidth=cambiumRadioChannelWidth, cambiumClientVendorName=cambiumClientVendorName, cambiumMeshClientTxDataBytes=cambiumMeshClientTxDataBytes, cambiumWlanSsid=cambiumWlanSsid, cambiumWlanNumClients=cambiumWlanNumClients, cambiumClientTotalRxPackets=cambiumClientTotalRxPackets, cambiumRadioDfsStatus=cambiumRadioDfsStatus)
