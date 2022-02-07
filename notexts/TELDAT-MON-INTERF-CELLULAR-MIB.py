#
# PySNMP MIB module TELDAT-MON-INTERF-CELLULAR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/teldat/TELDAT-MON-INTERF-CELLULAR-MIB
# Produced by pysmi-1.1.8 at Mon Feb  7 16:20:02 2022
# On host fv-az42-619 platform Linux version 5.11.0-1028-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, iso, TimeTicks, IpAddress, Counter64, NotificationType, Unsigned32, MibIdentifier, Counter32, Gauge32, Bits, Integer32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "iso", "TimeTicks", "IpAddress", "Counter64", "NotificationType", "Unsigned32", "MibIdentifier", "Counter32", "Gauge32", "Bits", "Integer32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
telProdNpMonInterfRouter, = mibBuilder.importSymbols("TELDAT-SW-STRUCTURE-MIB", "telProdNpMonInterfRouter")
telProdNpMonInterfCellular = MibIdentifier((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18))
teldatCellularInfoInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 1), )
if mibBuilder.loadTexts: teldatCellularInfoInterfaceTable.setStatus('mandatory')
teldatCellularInfoInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 1, 1), ).setIndexNames((0, "TELDAT-MON-INTERF-CELLULAR-MIB", "teldatCellularInfoInterfaceIndex"))
if mibBuilder.loadTexts: teldatCellularInfoInterfaceEntry.setStatus('mandatory')
teldatCellularInfoInterfaceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularInfoInterfaceIndex.setStatus('mandatory')
teldatCellularInfoInterfaceModuleManufacturer = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularInfoInterfaceModuleManufacturer.setStatus('mandatory')
teldatCellularInfoInterfaceModuleModel = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularInfoInterfaceModuleModel.setStatus('mandatory')
teldatCellularInfoInterfaceModuleFirmware = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularInfoInterfaceModuleFirmware.setStatus('mandatory')
teldatCellularInfoInterfaceModuleIMEI = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularInfoInterfaceModuleIMEI.setStatus('mandatory')
teldatCellularInfoInterfaceModuleIMSI = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularInfoInterfaceModuleIMSI.setStatus('mandatory')
teldatCellularInfoInterfaceSIMId = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 1, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularInfoInterfaceSIMId.setStatus('mandatory')
teldatCellularInfoInterfaceSIMIcc = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 1, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularInfoInterfaceSIMIcc.setStatus('mandatory')
teldatCellularStatObject = MibIdentifier((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3))
teldatCellularStateInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 1), )
if mibBuilder.loadTexts: teldatCellularStateInterfaceTable.setStatus('mandatory')
teldatCellularStateInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 1, 1), ).setIndexNames((0, "TELDAT-MON-INTERF-CELLULAR-MIB", "teldatCellularStateInterfaceIndex"))
if mibBuilder.loadTexts: teldatCellularStateInterfaceEntry.setStatus('mandatory')
teldatCellularStateInterfaceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularStateInterfaceIndex.setStatus('mandatory')
teldatCellularStateInterfaceState = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularStateInterfaceState.setStatus('mandatory')
teldatCellularStateInterfaceDropPing = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 1, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularStateInterfaceDropPing.setStatus('mandatory')
teldatCellularStateInterfaceDropTrace = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 1, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularStateInterfaceDropTrace.setStatus('mandatory')
teldatCellularStateInterfaceDropTraffic = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 1, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularStateInterfaceDropTraffic.setStatus('mandatory')
teldatCellularStateInterfaceTConnTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 1, 1, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularStateInterfaceTConnTime.setStatus('mandatory')
teldatCellularStateInterfaceCConnTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 1, 1, 7), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularStateInterfaceCConnTime.setStatus('mandatory')
teldatCellularStateInterfaceCurDial = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 1, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularStateInterfaceCurDial.setStatus('mandatory')
teldatCellularStateInterfaceNCall = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 1, 1, 9), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularStateInterfaceNCall.setStatus('mandatory')
teldatCellularStateInterfaceDestination = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 1, 1, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularStateInterfaceDestination.setStatus('mandatory')
teldatCellularStateInterfaceTime2Sp = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 1, 1, 11), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularStateInterfaceTime2Sp.setStatus('mandatory')
teldatCellularStateMobileTable = MibTable((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 2), )
if mibBuilder.loadTexts: teldatCellularStateMobileTable.setStatus('mandatory')
teldatCellularStateMobileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 2, 1), ).setIndexNames((0, "TELDAT-MON-INTERF-CELLULAR-MIB", "teldatCellularStateMobileIndex"))
if mibBuilder.loadTexts: teldatCellularStateMobileEntry.setStatus('mandatory')
teldatCellularStateMobileIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularStateMobileIndex.setStatus('mandatory')
teldatCellularStateMobileRegistrationState = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("searching", 0), ("home-network", 1), ("attaching", 2), ("denied", 3), ("unknown", 4), ("roaming", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularStateMobileRegistrationState.setStatus('mandatory')
teldatCellularStateMobilePublicLandMobileNtwCode = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularStateMobilePublicLandMobileNtwCode.setStatus('mandatory')
teldatCellularStateMobileCellLocationAreaCode = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 2, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularStateMobileCellLocationAreaCode.setStatus('mandatory')
teldatCellularStateMobileCellId = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 2, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularStateMobileCellId.setStatus('mandatory')
teldatCellularStateMobileRadioTechnology = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 2, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularStateMobileRadioTechnology.setStatus('mandatory')
teldatCellularStateMobileRadioBand = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 2, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularStateMobileRadioBand.setStatus('mandatory')
teldatCellularStateMobileRxSignalCodePwr = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 2, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularStateMobileRxSignalCodePwr.setStatus('mandatory')
teldatCellularStateMobileEnergyChipByPwrdnsty = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 2, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularStateMobileEnergyChipByPwrdnsty.setStatus('mandatory')
teldatCellularStateMobileSignalQuality = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 2, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularStateMobileSignalQuality.setStatus('mandatory')
teldatCellularStateMobileTemperature = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 2, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularStateMobileTemperature.setStatus('mandatory')
teldatCellularStateMobileRxPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 2, 1, 12), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularStateMobileRxPackets.setStatus('mandatory')
teldatCellularStateMobileRxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 2, 1, 13), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularStateMobileRxBytes.setStatus('mandatory')
teldatCellularStateMobileTxPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 2, 1, 14), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularStateMobileTxPackets.setStatus('mandatory')
teldatCellularStateMobileTxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 2, 1, 15), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularStateMobileTxBytes.setStatus('mandatory')
teldatCellularStateMobileRxBpsLast1s = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 2, 1, 16), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularStateMobileRxBpsLast1s.setStatus('mandatory')
teldatCellularStateMobileTxBpsLast1s = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 2, 1, 17), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularStateMobileTxBpsLast1s.setStatus('mandatory')
teldatCellularStateMobileRxBpsLast1m = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 2, 1, 18), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularStateMobileRxBpsLast1m.setStatus('mandatory')
teldatCellularStateMobileTxBpsLast1m = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 2, 1, 19), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularStateMobileTxBpsLast1m.setStatus('mandatory')
teldatCellularStateMobileRxBpsLast5m = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 2, 1, 20), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularStateMobileRxBpsLast5m.setStatus('mandatory')
teldatCellularStateMobileTxBpsLast5m = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 2, 1, 21), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularStateMobileTxBpsLast5m.setStatus('mandatory')
teldatCellularStateMobileRxRSRP = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 2, 1, 22), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularStateMobileRxRSRP.setStatus('mandatory')
teldatCellularStateMobileRxRSRQ = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 2, 1, 23), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularStateMobileRxRSRQ.setStatus('mandatory')
teldatCellularStateMobileRxSINR = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 2, 1, 24), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularStateMobileRxSINR.setStatus('mandatory')
teldatCellularStateMobileLTECellId = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 2, 1, 25), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularStateMobileLTECellId.setStatus('mandatory')
teldatCellularSIMMngTable = MibTable((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 3), )
if mibBuilder.loadTexts: teldatCellularSIMMngTable.setStatus('mandatory')
teldatCellularSIMMngEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 3, 1), ).setIndexNames((0, "TELDAT-MON-INTERF-CELLULAR-MIB", "teldatCellularSIMMngIndex"))
if mibBuilder.loadTexts: teldatCellularSIMMngEntry.setStatus('mandatory')
teldatCellularSIMMngIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularSIMMngIndex.setStatus('mandatory')
teldatCellularSIMMngCurrentSIMSocket = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("external-socket1", 0), ("internal-socket2", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularSIMMngCurrentSIMSocket.setStatus('mandatory')
teldatCellularSIMMngMainSIMSocket = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("external-socket1", 0), ("internal-socket2", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularSIMMngMainSIMSocket.setStatus('mandatory')
teldatCellularSIMMngSupervisionSIMSocket = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularSIMMngSupervisionSIMSocket.setStatus('mandatory')
teldatCellularSIMMngSIMImsiInfoSocket1 = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 3, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularSIMMngSIMImsiInfoSocket1.setStatus('mandatory')
teldatCellularSIMMngSIMIdInfoSocket1 = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 3, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularSIMMngSIMIdInfoSocket1.setStatus('mandatory')
teldatCellularSIMMngSIMImsiInfoSocket2 = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 3, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularSIMMngSIMImsiInfoSocket2.setStatus('mandatory')
teldatCellularSIMMngSIMIdInfoSocket2 = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 3, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularSIMMngSIMIdInfoSocket2.setStatus('mandatory')
teldatCellularProfDialTable = MibTable((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 4), )
if mibBuilder.loadTexts: teldatCellularProfDialTable.setStatus('mandatory')
teldatCellularProfDialEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 4, 1), ).setIndexNames((0, "TELDAT-MON-INTERF-CELLULAR-MIB", "teldatCellularProfDialIfcIndex"))
if mibBuilder.loadTexts: teldatCellularProfDialEntry.setStatus('mandatory')
teldatCellularProfDialIfcIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularProfDialIfcIndex.setStatus('mandatory')
teldatCellularProfDialName1 = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 4, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularProfDialName1.setStatus('mandatory')
teldatCellularProfDialAPN1 = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 4, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularProfDialAPN1.setStatus('mandatory')
teldatCellularProfDialName2 = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 4, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularProfDialName2.setStatus('mandatory')
teldatCellularProfDialAPN2 = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 4, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularProfDialAPN2.setStatus('mandatory')
teldatCellularRecChangesTable = MibTable((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 5), )
if mibBuilder.loadTexts: teldatCellularRecChangesTable.setStatus('mandatory')
teldatCellularRecChangesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 5, 1), ).setIndexNames((0, "TELDAT-MON-INTERF-CELLULAR-MIB", "teldatCellularRecChangesIfcIndex"))
if mibBuilder.loadTexts: teldatCellularRecChangesEntry.setStatus('mandatory')
teldatCellularRecChangesIfcIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularRecChangesIfcIndex.setStatus('mandatory')
teldatCellularRecChangesPLMNTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 5, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularRecChangesPLMNTimeStamp.setStatus('mandatory')
teldatCellularRecChangesPLMNCode = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 5, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularRecChangesPLMNCode.setStatus('mandatory')
mibBuilder.exportSymbols("TELDAT-MON-INTERF-CELLULAR-MIB", teldatCellularStateMobileTxPackets=teldatCellularStateMobileTxPackets, teldatCellularInfoInterfaceModuleManufacturer=teldatCellularInfoInterfaceModuleManufacturer, teldatCellularSIMMngCurrentSIMSocket=teldatCellularSIMMngCurrentSIMSocket, teldatCellularStateInterfaceTable=teldatCellularStateInterfaceTable, teldatCellularSIMMngTable=teldatCellularSIMMngTable, teldatCellularProfDialName2=teldatCellularProfDialName2, teldatCellularStateMobileRxBpsLast1m=teldatCellularStateMobileRxBpsLast1m, teldatCellularInfoInterfaceTable=teldatCellularInfoInterfaceTable, teldatCellularStateMobilePublicLandMobileNtwCode=teldatCellularStateMobilePublicLandMobileNtwCode, teldatCellularStateMobileRegistrationState=teldatCellularStateMobileRegistrationState, teldatCellularProfDialAPN2=teldatCellularProfDialAPN2, teldatCellularStateMobileLTECellId=teldatCellularStateMobileLTECellId, teldatCellularStateInterfaceTime2Sp=teldatCellularStateInterfaceTime2Sp, teldatCellularStateMobileRxBytes=teldatCellularStateMobileRxBytes, teldatCellularStateMobileCellLocationAreaCode=teldatCellularStateMobileCellLocationAreaCode, teldatCellularSIMMngIndex=teldatCellularSIMMngIndex, teldatCellularSIMMngSIMIdInfoSocket1=teldatCellularSIMMngSIMIdInfoSocket1, teldatCellularRecChangesEntry=teldatCellularRecChangesEntry, teldatCellularSIMMngMainSIMSocket=teldatCellularSIMMngMainSIMSocket, teldatCellularProfDialIfcIndex=teldatCellularProfDialIfcIndex, teldatCellularStateMobileIndex=teldatCellularStateMobileIndex, teldatCellularInfoInterfaceModuleIMEI=teldatCellularInfoInterfaceModuleIMEI, teldatCellularStateInterfaceDestination=teldatCellularStateInterfaceDestination, teldatCellularStatObject=teldatCellularStatObject, teldatCellularSIMMngEntry=teldatCellularSIMMngEntry, teldatCellularRecChangesPLMNCode=teldatCellularRecChangesPLMNCode, teldatCellularStateMobileRxRSRP=teldatCellularStateMobileRxRSRP, teldatCellularStateInterfaceTConnTime=teldatCellularStateInterfaceTConnTime, teldatCellularStateMobileTxBytes=teldatCellularStateMobileTxBytes, teldatCellularStateInterfaceDropTrace=teldatCellularStateInterfaceDropTrace, teldatCellularProfDialName1=teldatCellularProfDialName1, teldatCellularRecChangesIfcIndex=teldatCellularRecChangesIfcIndex, teldatCellularInfoInterfaceEntry=teldatCellularInfoInterfaceEntry, teldatCellularSIMMngSIMImsiInfoSocket2=teldatCellularSIMMngSIMImsiInfoSocket2, teldatCellularProfDialAPN1=teldatCellularProfDialAPN1, teldatCellularStateMobileRxRSRQ=teldatCellularStateMobileRxRSRQ, teldatCellularStateMobileRxBpsLast1s=teldatCellularStateMobileRxBpsLast1s, teldatCellularStateMobileEnergyChipByPwrdnsty=teldatCellularStateMobileEnergyChipByPwrdnsty, teldatCellularStateMobileTemperature=teldatCellularStateMobileTemperature, teldatCellularInfoInterfaceSIMId=teldatCellularInfoInterfaceSIMId, teldatCellularStateInterfaceDropTraffic=teldatCellularStateInterfaceDropTraffic, teldatCellularProfDialEntry=teldatCellularProfDialEntry, teldatCellularRecChangesPLMNTimeStamp=teldatCellularRecChangesPLMNTimeStamp, teldatCellularStateInterfaceEntry=teldatCellularStateInterfaceEntry, telProdNpMonInterfCellular=telProdNpMonInterfCellular, teldatCellularStateInterfaceDropPing=teldatCellularStateInterfaceDropPing, teldatCellularInfoInterfaceIndex=teldatCellularInfoInterfaceIndex, teldatCellularStateMobileSignalQuality=teldatCellularStateMobileSignalQuality, teldatCellularStateInterfaceIndex=teldatCellularStateInterfaceIndex, teldatCellularInfoInterfaceModuleFirmware=teldatCellularInfoInterfaceModuleFirmware, teldatCellularStateInterfaceNCall=teldatCellularStateInterfaceNCall, teldatCellularStateMobileTxBpsLast1m=teldatCellularStateMobileTxBpsLast1m, teldatCellularProfDialTable=teldatCellularProfDialTable, teldatCellularInfoInterfaceModuleIMSI=teldatCellularInfoInterfaceModuleIMSI, teldatCellularSIMMngSupervisionSIMSocket=teldatCellularSIMMngSupervisionSIMSocket, teldatCellularStateMobileRxBpsLast5m=teldatCellularStateMobileRxBpsLast5m, teldatCellularStateMobileTxBpsLast5m=teldatCellularStateMobileTxBpsLast5m, teldatCellularInfoInterfaceSIMIcc=teldatCellularInfoInterfaceSIMIcc, teldatCellularStateMobileEntry=teldatCellularStateMobileEntry, teldatCellularStateMobileRxSignalCodePwr=teldatCellularStateMobileRxSignalCodePwr, teldatCellularStateMobileRxPackets=teldatCellularStateMobileRxPackets, teldatCellularStateMobileTxBpsLast1s=teldatCellularStateMobileTxBpsLast1s, teldatCellularStateMobileRxSINR=teldatCellularStateMobileRxSINR, teldatCellularStateInterfaceCConnTime=teldatCellularStateInterfaceCConnTime, teldatCellularStateInterfaceCurDial=teldatCellularStateInterfaceCurDial, teldatCellularStateInterfaceState=teldatCellularStateInterfaceState, teldatCellularStateMobileTable=teldatCellularStateMobileTable, teldatCellularStateMobileRadioTechnology=teldatCellularStateMobileRadioTechnology, teldatCellularStateMobileRadioBand=teldatCellularStateMobileRadioBand, teldatCellularRecChangesTable=teldatCellularRecChangesTable, teldatCellularStateMobileCellId=teldatCellularStateMobileCellId, teldatCellularSIMMngSIMImsiInfoSocket1=teldatCellularSIMMngSIMImsiInfoSocket1, teldatCellularInfoInterfaceModuleModel=teldatCellularInfoInterfaceModuleModel, teldatCellularSIMMngSIMIdInfoSocket2=teldatCellularSIMMngSIMIdInfoSocket2)
