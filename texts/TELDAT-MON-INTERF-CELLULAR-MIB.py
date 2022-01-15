#
# PySNMP MIB module TELDAT-MON-INTERF-CELLULAR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/teldat/TELDAT-MON-INTERF-CELLULAR-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 18:20:27 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, NotificationType, Counter64, Bits, iso, TimeTicks, Gauge32, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, IpAddress, ModuleIdentity, MibIdentifier, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "NotificationType", "Counter64", "Bits", "iso", "TimeTicks", "Gauge32", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "IpAddress", "ModuleIdentity", "MibIdentifier", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
telProdNpMonInterfRouter, = mibBuilder.importSymbols("TELDAT-SW-STRUCTURE-MIB", "telProdNpMonInterfRouter")
telProdNpMonInterfCellular = MibIdentifier((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18))
teldatCellularInfoInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 1), )
if mibBuilder.loadTexts: teldatCellularInfoInterfaceTable.setStatus('mandatory')
if mibBuilder.loadTexts: teldatCellularInfoInterfaceTable.setDescription('Table of information available for Cellular interfaces.\n        Each row represents an interface')
teldatCellularInfoInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 1, 1), ).setIndexNames((0, "TELDAT-MON-INTERF-CELLULAR-MIB", "teldatCellularInfoInterfaceIndex"))
if mibBuilder.loadTexts: teldatCellularInfoInterfaceEntry.setStatus('mandatory')
if mibBuilder.loadTexts: teldatCellularInfoInterfaceEntry.setDescription('A base list of objects that are information about a Cellular interface.\n        The inex is the number of the interface')
teldatCellularInfoInterfaceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularInfoInterfaceIndex.setStatus('mandatory')
if mibBuilder.loadTexts: teldatCellularInfoInterfaceIndex.setDescription('Interface index')
teldatCellularInfoInterfaceModuleManufacturer = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularInfoInterfaceModuleManufacturer.setStatus('mandatory')
if mibBuilder.loadTexts: teldatCellularInfoInterfaceModuleManufacturer.setDescription('Cellular module manufacturer.')
teldatCellularInfoInterfaceModuleModel = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularInfoInterfaceModuleModel.setStatus('mandatory')
if mibBuilder.loadTexts: teldatCellularInfoInterfaceModuleModel.setDescription('Cellular module model.')
teldatCellularInfoInterfaceModuleFirmware = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularInfoInterfaceModuleFirmware.setStatus('mandatory')
if mibBuilder.loadTexts: teldatCellularInfoInterfaceModuleFirmware.setDescription('Cellular module firmware release.')
teldatCellularInfoInterfaceModuleIMEI = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularInfoInterfaceModuleIMEI.setStatus('mandatory')
if mibBuilder.loadTexts: teldatCellularInfoInterfaceModuleIMEI.setDescription('Cellular module IMEI.')
teldatCellularInfoInterfaceModuleIMSI = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularInfoInterfaceModuleIMSI.setStatus('mandatory')
if mibBuilder.loadTexts: teldatCellularInfoInterfaceModuleIMSI.setDescription('Cellular module IMSI.')
teldatCellularInfoInterfaceSIMId = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 1, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularInfoInterfaceSIMId.setStatus('mandatory')
if mibBuilder.loadTexts: teldatCellularInfoInterfaceSIMId.setDescription('Cellular active SIM ID.')
teldatCellularInfoInterfaceSIMIcc = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 1, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularInfoInterfaceSIMIcc.setStatus('mandatory')
if mibBuilder.loadTexts: teldatCellularInfoInterfaceSIMIcc.setDescription('Cellular active SIM ICC.')
teldatCellularStatObject = MibIdentifier((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3))
teldatCellularStateInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 1), )
if mibBuilder.loadTexts: teldatCellularStateInterfaceTable.setStatus('mandatory')
if mibBuilder.loadTexts: teldatCellularStateInterfaceTable.setDescription('Table of Cellular interface state information.')
teldatCellularStateInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 1, 1), ).setIndexNames((0, "TELDAT-MON-INTERF-CELLULAR-MIB", "teldatCellularStateInterfaceIndex"))
if mibBuilder.loadTexts: teldatCellularStateInterfaceEntry.setStatus('mandatory')
if mibBuilder.loadTexts: teldatCellularStateInterfaceEntry.setDescription('A base list of objects that are interface state information.')
teldatCellularStateInterfaceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularStateInterfaceIndex.setStatus('mandatory')
if mibBuilder.loadTexts: teldatCellularStateInterfaceIndex.setDescription('Cellular Interface index.')
teldatCellularStateInterfaceState = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularStateInterfaceState.setStatus('mandatory')
if mibBuilder.loadTexts: teldatCellularStateInterfaceState.setDescription('Call state.')
teldatCellularStateInterfaceDropPing = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 1, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularStateInterfaceDropPing.setStatus('mandatory')
if mibBuilder.loadTexts: teldatCellularStateInterfaceDropPing.setDescription('Number of calls dropped due to ping supervision.')
teldatCellularStateInterfaceDropTrace = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 1, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularStateInterfaceDropTrace.setStatus('mandatory')
if mibBuilder.loadTexts: teldatCellularStateInterfaceDropTrace.setDescription('Number of calls dropped due to traceroute supervision.')
teldatCellularStateInterfaceDropTraffic = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 1, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularStateInterfaceDropTraffic.setStatus('mandatory')
if mibBuilder.loadTexts: teldatCellularStateInterfaceDropTraffic.setDescription('Number of calls dropped due to traffic supervision.')
teldatCellularStateInterfaceTConnTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 1, 1, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularStateInterfaceTConnTime.setStatus('mandatory')
if mibBuilder.loadTexts: teldatCellularStateInterfaceTConnTime.setDescription('Total connection time .')
teldatCellularStateInterfaceCConnTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 1, 1, 7), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularStateInterfaceCConnTime.setStatus('mandatory')
if mibBuilder.loadTexts: teldatCellularStateInterfaceCConnTime.setDescription('Current connection time.')
teldatCellularStateInterfaceCurDial = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 1, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularStateInterfaceCurDial.setStatus('mandatory')
if mibBuilder.loadTexts: teldatCellularStateInterfaceCurDial.setDescription('Current dial-profile used.')
teldatCellularStateInterfaceNCall = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 1, 1, 9), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularStateInterfaceNCall.setStatus('mandatory')
if mibBuilder.loadTexts: teldatCellularStateInterfaceNCall.setDescription('Number of processed calls.')
teldatCellularStateInterfaceDestination = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 1, 1, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularStateInterfaceDestination.setStatus('mandatory')
if mibBuilder.loadTexts: teldatCellularStateInterfaceDestination.setDescription('Connection destination.')
teldatCellularStateInterfaceTime2Sp = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 1, 1, 11), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularStateInterfaceTime2Sp.setStatus('mandatory')
if mibBuilder.loadTexts: teldatCellularStateInterfaceTime2Sp.setDescription('Time to establish the call.')
teldatCellularStateMobileTable = MibTable((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 2), )
if mibBuilder.loadTexts: teldatCellularStateMobileTable.setStatus('mandatory')
if mibBuilder.loadTexts: teldatCellularStateMobileTable.setDescription('Table of Cellular mobile state information.')
teldatCellularStateMobileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 2, 1), ).setIndexNames((0, "TELDAT-MON-INTERF-CELLULAR-MIB", "teldatCellularStateMobileIndex"))
if mibBuilder.loadTexts: teldatCellularStateMobileEntry.setStatus('mandatory')
if mibBuilder.loadTexts: teldatCellularStateMobileEntry.setDescription('A base list of objects that are mobile state information.')
teldatCellularStateMobileIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularStateMobileIndex.setStatus('mandatory')
if mibBuilder.loadTexts: teldatCellularStateMobileIndex.setDescription('Cellular mobile state index.')
teldatCellularStateMobileRegistrationState = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("searching", 0), ("home-network", 1), ("attaching", 2), ("denied", 3), ("unknown", 4), ("roaming", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularStateMobileRegistrationState.setStatus('mandatory')
if mibBuilder.loadTexts: teldatCellularStateMobileRegistrationState.setDescription('Cellular mobile registration state ().')
teldatCellularStateMobilePublicLandMobileNtwCode = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularStateMobilePublicLandMobileNtwCode.setStatus('mandatory')
if mibBuilder.loadTexts: teldatCellularStateMobilePublicLandMobileNtwCode.setDescription('Public land mobile network used (+COPS).')
teldatCellularStateMobileCellLocationAreaCode = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 2, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularStateMobileCellLocationAreaCode.setStatus('mandatory')
if mibBuilder.loadTexts: teldatCellularStateMobileCellLocationAreaCode.setDescription('Cellular mobile cell location area code (+CGREG).')
teldatCellularStateMobileCellId = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 2, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularStateMobileCellId.setStatus('mandatory')
if mibBuilder.loadTexts: teldatCellularStateMobileCellId.setDescription('Cellular mobile used cell id (+CGREG).')
teldatCellularStateMobileRadioTechnology = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 2, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularStateMobileRadioTechnology.setStatus('mandatory')
if mibBuilder.loadTexts: teldatCellularStateMobileRadioTechnology.setDescription('Cellular mobile current radio access tecnology used (!GETRAT).')
teldatCellularStateMobileRadioBand = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 2, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularStateMobileRadioBand.setStatus('mandatory')
if mibBuilder.loadTexts: teldatCellularStateMobileRadioBand.setDescription('Cellular mobile current active band (!GETBAND).')
teldatCellularStateMobileRxSignalCodePwr = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 2, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularStateMobileRxSignalCodePwr.setStatus('mandatory')
if mibBuilder.loadTexts: teldatCellularStateMobileRxSignalCodePwr.setDescription('Cellular mobile received signal code power (RSCP).')
teldatCellularStateMobileEnergyChipByPwrdnsty = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 2, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularStateMobileEnergyChipByPwrdnsty.setStatus('mandatory')
if mibBuilder.loadTexts: teldatCellularStateMobileEnergyChipByPwrdnsty.setDescription('Cellular mobile total energy per chip per power density (EcNo).')
teldatCellularStateMobileSignalQuality = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 2, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularStateMobileSignalQuality.setStatus('mandatory')
if mibBuilder.loadTexts: teldatCellularStateMobileSignalQuality.setDescription('Cellular mobile reception signal quality (+CSQ).')
teldatCellularStateMobileTemperature = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 2, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularStateMobileTemperature.setStatus('mandatory')
if mibBuilder.loadTexts: teldatCellularStateMobileTemperature.setDescription('Cellular mobile temperature (!PCTEMP).')
teldatCellularStateMobileRxPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 2, 1, 12), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularStateMobileRxPackets.setStatus('mandatory')
if mibBuilder.loadTexts: teldatCellularStateMobileRxPackets.setDescription('Number of data packtes received by the radio interface')
teldatCellularStateMobileRxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 2, 1, 13), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularStateMobileRxBytes.setStatus('mandatory')
if mibBuilder.loadTexts: teldatCellularStateMobileRxBytes.setDescription('Number of data bytes received by the radio interface')
teldatCellularStateMobileTxPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 2, 1, 14), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularStateMobileTxPackets.setStatus('mandatory')
if mibBuilder.loadTexts: teldatCellularStateMobileTxPackets.setDescription('Number of data packtes sent by the radio interface')
teldatCellularStateMobileTxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 2, 1, 15), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularStateMobileTxBytes.setStatus('mandatory')
if mibBuilder.loadTexts: teldatCellularStateMobileTxBytes.setDescription('Number of data packtes sent by the radio interface')
teldatCellularStateMobileRxBpsLast1s = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 2, 1, 16), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularStateMobileRxBpsLast1s.setStatus('mandatory')
if mibBuilder.loadTexts: teldatCellularStateMobileRxBpsLast1s.setDescription('Rx througput measured in the last second in bps')
teldatCellularStateMobileTxBpsLast1s = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 2, 1, 17), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularStateMobileTxBpsLast1s.setStatus('mandatory')
if mibBuilder.loadTexts: teldatCellularStateMobileTxBpsLast1s.setDescription('Tx througput measured in the last second in bps')
teldatCellularStateMobileRxBpsLast1m = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 2, 1, 18), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularStateMobileRxBpsLast1m.setStatus('mandatory')
if mibBuilder.loadTexts: teldatCellularStateMobileRxBpsLast1m.setDescription('Rx througput measured in the last minute in bps')
teldatCellularStateMobileTxBpsLast1m = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 2, 1, 19), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularStateMobileTxBpsLast1m.setStatus('mandatory')
if mibBuilder.loadTexts: teldatCellularStateMobileTxBpsLast1m.setDescription('Tx througput measured in the last minute in bps')
teldatCellularStateMobileRxBpsLast5m = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 2, 1, 20), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularStateMobileRxBpsLast5m.setStatus('mandatory')
if mibBuilder.loadTexts: teldatCellularStateMobileRxBpsLast5m.setDescription('Rx througput measured in the last five minutes in bps')
teldatCellularStateMobileTxBpsLast5m = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 2, 1, 21), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularStateMobileTxBpsLast5m.setStatus('mandatory')
if mibBuilder.loadTexts: teldatCellularStateMobileTxBpsLast5m.setDescription('Tx througput measured in the last five minutes in bps')
teldatCellularStateMobileRxRSRP = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 2, 1, 22), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularStateMobileRxRSRP.setStatus('mandatory')
if mibBuilder.loadTexts: teldatCellularStateMobileRxRSRP.setDescription('Cellular mobile reference symbol received power (RSRP).')
teldatCellularStateMobileRxRSRQ = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 2, 1, 23), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularStateMobileRxRSRQ.setStatus('mandatory')
if mibBuilder.loadTexts: teldatCellularStateMobileRxRSRQ.setDescription('Cellular mobile reference signal received quality (RSRQ).')
teldatCellularStateMobileRxSINR = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 2, 1, 24), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularStateMobileRxSINR.setStatus('mandatory')
if mibBuilder.loadTexts: teldatCellularStateMobileRxSINR.setDescription('Cellular mobile signal versus noise ratio (SINR).')
teldatCellularStateMobileLTECellId = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 2, 1, 25), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularStateMobileLTECellId.setStatus('mandatory')
if mibBuilder.loadTexts: teldatCellularStateMobileLTECellId.setDescription('Cellular mobile used LTE cell id.')
teldatCellularSIMMngTable = MibTable((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 3), )
if mibBuilder.loadTexts: teldatCellularSIMMngTable.setStatus('mandatory')
if mibBuilder.loadTexts: teldatCellularSIMMngTable.setDescription('Table of Cellular SIM Management information.')
teldatCellularSIMMngEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 3, 1), ).setIndexNames((0, "TELDAT-MON-INTERF-CELLULAR-MIB", "teldatCellularSIMMngIndex"))
if mibBuilder.loadTexts: teldatCellularSIMMngEntry.setStatus('mandatory')
if mibBuilder.loadTexts: teldatCellularSIMMngEntry.setDescription('A base list of objects that are sim management information.')
teldatCellularSIMMngIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularSIMMngIndex.setStatus('mandatory')
if mibBuilder.loadTexts: teldatCellularSIMMngIndex.setDescription('Cellular mobile state index.')
teldatCellularSIMMngCurrentSIMSocket = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("external-socket1", 0), ("internal-socket2", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularSIMMngCurrentSIMSocket.setStatus('mandatory')
if mibBuilder.loadTexts: teldatCellularSIMMngCurrentSIMSocket.setDescription('Current SIM Socket.')
teldatCellularSIMMngMainSIMSocket = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("external-socket1", 0), ("internal-socket2", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularSIMMngMainSIMSocket.setStatus('mandatory')
if mibBuilder.loadTexts: teldatCellularSIMMngMainSIMSocket.setDescription('Main SIM Socket.')
teldatCellularSIMMngSupervisionSIMSocket = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularSIMMngSupervisionSIMSocket.setStatus('mandatory')
if mibBuilder.loadTexts: teldatCellularSIMMngSupervisionSIMSocket.setDescription('Supervision SIM Socket state.')
teldatCellularSIMMngSIMImsiInfoSocket1 = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 3, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularSIMMngSIMImsiInfoSocket1.setStatus('mandatory')
if mibBuilder.loadTexts: teldatCellularSIMMngSIMImsiInfoSocket1.setDescription('IMSI of the SIM inserted in Socket1')
teldatCellularSIMMngSIMIdInfoSocket1 = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 3, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularSIMMngSIMIdInfoSocket1.setStatus('mandatory')
if mibBuilder.loadTexts: teldatCellularSIMMngSIMIdInfoSocket1.setDescription('SIM ID of the SIM inserted in Socket1')
teldatCellularSIMMngSIMImsiInfoSocket2 = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 3, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularSIMMngSIMImsiInfoSocket2.setStatus('mandatory')
if mibBuilder.loadTexts: teldatCellularSIMMngSIMImsiInfoSocket2.setDescription('IMSI of the SIM inserted in Socket2')
teldatCellularSIMMngSIMIdInfoSocket2 = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 3, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularSIMMngSIMIdInfoSocket2.setStatus('mandatory')
if mibBuilder.loadTexts: teldatCellularSIMMngSIMIdInfoSocket2.setDescription('SIM ID of the SIM inserted in Socket2')
teldatCellularProfDialTable = MibTable((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 4), )
if mibBuilder.loadTexts: teldatCellularProfDialTable.setStatus('mandatory')
if mibBuilder.loadTexts: teldatCellularProfDialTable.setDescription('Table of Cellular Dial Profile information.')
teldatCellularProfDialEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 4, 1), ).setIndexNames((0, "TELDAT-MON-INTERF-CELLULAR-MIB", "teldatCellularProfDialIfcIndex"))
if mibBuilder.loadTexts: teldatCellularProfDialEntry.setStatus('mandatory')
if mibBuilder.loadTexts: teldatCellularProfDialEntry.setDescription('A list of objects that show Dial Profile information')
teldatCellularProfDialIfcIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularProfDialIfcIndex.setStatus('mandatory')
if mibBuilder.loadTexts: teldatCellularProfDialIfcIndex.setDescription('Interface index.')
teldatCellularProfDialName1 = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 4, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularProfDialName1.setStatus('mandatory')
if mibBuilder.loadTexts: teldatCellularProfDialName1.setDescription('Dial Profile Name(1) associated to cellular interface.')
teldatCellularProfDialAPN1 = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 4, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularProfDialAPN1.setStatus('mandatory')
if mibBuilder.loadTexts: teldatCellularProfDialAPN1.setDescription('Access Point Name(1) associated to cellular interface.')
teldatCellularProfDialName2 = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 4, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularProfDialName2.setStatus('mandatory')
if mibBuilder.loadTexts: teldatCellularProfDialName2.setDescription('Dial Profile Name(2) associated to cellular interface.')
teldatCellularProfDialAPN2 = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 4, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularProfDialAPN2.setStatus('mandatory')
if mibBuilder.loadTexts: teldatCellularProfDialAPN2.setDescription('Access Point Name(2) associated to cellular interface.')
teldatCellularRecChangesTable = MibTable((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 5), )
if mibBuilder.loadTexts: teldatCellularRecChangesTable.setStatus('mandatory')
if mibBuilder.loadTexts: teldatCellularRecChangesTable.setDescription('Table of Cellular record-changes information.')
teldatCellularRecChangesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 5, 1), ).setIndexNames((0, "TELDAT-MON-INTERF-CELLULAR-MIB", "teldatCellularRecChangesIfcIndex"))
if mibBuilder.loadTexts: teldatCellularRecChangesEntry.setStatus('mandatory')
if mibBuilder.loadTexts: teldatCellularRecChangesEntry.setDescription('A list of objects that show information about cellular record-changes')
teldatCellularRecChangesIfcIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularRecChangesIfcIndex.setStatus('mandatory')
if mibBuilder.loadTexts: teldatCellularRecChangesIfcIndex.setDescription('Interface index.')
teldatCellularRecChangesPLMNTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 5, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularRecChangesPLMNTimeStamp.setStatus('mandatory')
if mibBuilder.loadTexts: teldatCellularRecChangesPLMNTimeStamp.setDescription('Display the timestamp of the latest change of Public Land Mobile Network (PLMN) code.')
teldatCellularRecChangesPLMNCode = MibTableColumn((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 5, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCellularRecChangesPLMNCode.setStatus('mandatory')
if mibBuilder.loadTexts: teldatCellularRecChangesPLMNCode.setDescription('Display the latest change of Public Land Mobile Network (PLMN) code.')
mibBuilder.exportSymbols("TELDAT-MON-INTERF-CELLULAR-MIB", teldatCellularStateMobileEnergyChipByPwrdnsty=teldatCellularStateMobileEnergyChipByPwrdnsty, teldatCellularInfoInterfaceSIMIcc=teldatCellularInfoInterfaceSIMIcc, teldatCellularStateInterfaceEntry=teldatCellularStateInterfaceEntry, teldatCellularStateMobileRadioBand=teldatCellularStateMobileRadioBand, teldatCellularStateInterfaceCurDial=teldatCellularStateInterfaceCurDial, teldatCellularStateMobileRxSignalCodePwr=teldatCellularStateMobileRxSignalCodePwr, teldatCellularStateMobileRxBpsLast1s=teldatCellularStateMobileRxBpsLast1s, teldatCellularStateMobileRxBpsLast5m=teldatCellularStateMobileRxBpsLast5m, teldatCellularInfoInterfaceModuleModel=teldatCellularInfoInterfaceModuleModel, teldatCellularStateInterfaceIndex=teldatCellularStateInterfaceIndex, teldatCellularStateMobileTxBytes=teldatCellularStateMobileTxBytes, teldatCellularInfoInterfaceSIMId=teldatCellularInfoInterfaceSIMId, teldatCellularProfDialIfcIndex=teldatCellularProfDialIfcIndex, teldatCellularRecChangesPLMNCode=teldatCellularRecChangesPLMNCode, teldatCellularStateMobileTxBpsLast1s=teldatCellularStateMobileTxBpsLast1s, teldatCellularStateInterfaceState=teldatCellularStateInterfaceState, teldatCellularStateInterfaceDropTrace=teldatCellularStateInterfaceDropTrace, teldatCellularStateInterfaceNCall=teldatCellularStateInterfaceNCall, teldatCellularStateMobileRegistrationState=teldatCellularStateMobileRegistrationState, teldatCellularProfDialName1=teldatCellularProfDialName1, teldatCellularStateMobileTxPackets=teldatCellularStateMobileTxPackets, teldatCellularRecChangesIfcIndex=teldatCellularRecChangesIfcIndex, teldatCellularSIMMngEntry=teldatCellularSIMMngEntry, teldatCellularSIMMngSupervisionSIMSocket=teldatCellularSIMMngSupervisionSIMSocket, teldatCellularStateMobileRxRSRP=teldatCellularStateMobileRxRSRP, teldatCellularSIMMngTable=teldatCellularSIMMngTable, teldatCellularInfoInterfaceModuleManufacturer=teldatCellularInfoInterfaceModuleManufacturer, teldatCellularStateMobileRxBytes=teldatCellularStateMobileRxBytes, teldatCellularStateMobilePublicLandMobileNtwCode=teldatCellularStateMobilePublicLandMobileNtwCode, teldatCellularStateMobileTxBpsLast1m=teldatCellularStateMobileTxBpsLast1m, teldatCellularInfoInterfaceTable=teldatCellularInfoInterfaceTable, teldatCellularProfDialAPN2=teldatCellularProfDialAPN2, teldatCellularStateInterfaceDropTraffic=teldatCellularStateInterfaceDropTraffic, teldatCellularStateMobileTemperature=teldatCellularStateMobileTemperature, teldatCellularStateInterfaceTable=teldatCellularStateInterfaceTable, teldatCellularProfDialTable=teldatCellularProfDialTable, teldatCellularStateMobileCellId=teldatCellularStateMobileCellId, teldatCellularStateInterfaceTime2Sp=teldatCellularStateInterfaceTime2Sp, teldatCellularStateMobileRxPackets=teldatCellularStateMobileRxPackets, teldatCellularSIMMngCurrentSIMSocket=teldatCellularSIMMngCurrentSIMSocket, teldatCellularStateMobileSignalQuality=teldatCellularStateMobileSignalQuality, teldatCellularInfoInterfaceEntry=teldatCellularInfoInterfaceEntry, teldatCellularInfoInterfaceModuleFirmware=teldatCellularInfoInterfaceModuleFirmware, teldatCellularStateInterfaceDestination=teldatCellularStateInterfaceDestination, teldatCellularStateInterfaceTConnTime=teldatCellularStateInterfaceTConnTime, teldatCellularStateMobileTxBpsLast5m=teldatCellularStateMobileTxBpsLast5m, teldatCellularProfDialEntry=teldatCellularProfDialEntry, teldatCellularStatObject=teldatCellularStatObject, teldatCellularStateMobileRxSINR=teldatCellularStateMobileRxSINR, teldatCellularStateMobileLTECellId=teldatCellularStateMobileLTECellId, teldatCellularProfDialName2=teldatCellularProfDialName2, telProdNpMonInterfCellular=telProdNpMonInterfCellular, teldatCellularStateInterfaceDropPing=teldatCellularStateInterfaceDropPing, teldatCellularInfoInterfaceIndex=teldatCellularInfoInterfaceIndex, teldatCellularRecChangesPLMNTimeStamp=teldatCellularRecChangesPLMNTimeStamp, teldatCellularInfoInterfaceModuleIMEI=teldatCellularInfoInterfaceModuleIMEI, teldatCellularRecChangesTable=teldatCellularRecChangesTable, teldatCellularStateMobileRadioTechnology=teldatCellularStateMobileRadioTechnology, teldatCellularStateMobileRxBpsLast1m=teldatCellularStateMobileRxBpsLast1m, teldatCellularInfoInterfaceModuleIMSI=teldatCellularInfoInterfaceModuleIMSI, teldatCellularStateMobileTable=teldatCellularStateMobileTable, teldatCellularStateMobileIndex=teldatCellularStateMobileIndex, teldatCellularSIMMngSIMImsiInfoSocket2=teldatCellularSIMMngSIMImsiInfoSocket2, teldatCellularProfDialAPN1=teldatCellularProfDialAPN1, teldatCellularStateMobileEntry=teldatCellularStateMobileEntry, teldatCellularStateMobileRxRSRQ=teldatCellularStateMobileRxRSRQ, teldatCellularStateMobileCellLocationAreaCode=teldatCellularStateMobileCellLocationAreaCode, teldatCellularSIMMngIndex=teldatCellularSIMMngIndex, teldatCellularSIMMngMainSIMSocket=teldatCellularSIMMngMainSIMSocket, teldatCellularSIMMngSIMImsiInfoSocket1=teldatCellularSIMMngSIMImsiInfoSocket1, teldatCellularSIMMngSIMIdInfoSocket1=teldatCellularSIMMngSIMIdInfoSocket1, teldatCellularSIMMngSIMIdInfoSocket2=teldatCellularSIMMngSIMIdInfoSocket2, teldatCellularRecChangesEntry=teldatCellularRecChangesEntry, teldatCellularStateInterfaceCConnTime=teldatCellularStateInterfaceCConnTime)
