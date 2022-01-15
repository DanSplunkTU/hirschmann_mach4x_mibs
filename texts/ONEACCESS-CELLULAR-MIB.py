#
# PySNMP MIB module ONEACCESS-CELLULAR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/oneaccess/ONEACCESS-CELLULAR-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 18:15:13 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
oacExpIMCellRadio, oacMIBModules = mibBuilder.importSymbols("ONEACCESS-GLOBAL-REG", "oacExpIMCellRadio", "oacMIBModules")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, Counter64, Counter32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, MibIdentifier, TimeTicks, IpAddress, iso, ModuleIdentity, Unsigned32, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Counter64", "Counter32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "MibIdentifier", "TimeTicks", "IpAddress", "iso", "ModuleIdentity", "Unsigned32", "Bits", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
oacCellularMIBModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 13191, 1, 100, 1000))
oacCellularMIBModule.setRevisions(('2014-04-07 00:00', '2013-10-15 00:00', '2011-10-27 00:00', '2010-07-08 00:01',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: oacCellularMIBModule.setRevisionsDescriptions(('Add RSSI table', 'Contact updated', 'Fixed some minor corrections.', 'This MIB module describes Cellular Radio Managed objects.',))
if mibBuilder.loadTexts: oacCellularMIBModule.setLastUpdated('201310150000Z')
if mibBuilder.loadTexts: oacCellularMIBModule.setOrganization(' OneAccess ')
if mibBuilder.loadTexts: oacCellularMIBModule.setContactInfo('Pascal KESTELOOT\n            Postal: ONE ACCESS\n                    381 Avenue du General de Gaulle\n                    92140 Clamart, France\n            FRANCE\n\n            Tel: (+33) 01 41 87 70 00\n            Fax: (+33) 01 41 87 74 00\n\n            E-mail: pascal.kesteloot@oneaccess-net.com')
if mibBuilder.loadTexts: oacCellularMIBModule.setDescription('Add cellular equipment and network info')
oacCellRadioRssi = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 1))
oacCellRssiLastHourTable = MibTable((1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 1, 1), )
if mibBuilder.loadTexts: oacCellRssiLastHourTable.setStatus('current')
if mibBuilder.loadTexts: oacCellRssiLastHourTable.setDescription('RSSI values of the last hour.')
oacCellRssiLastHourEntry = MibTableRow((1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 1, 1, 1), ).setIndexNames((0, "ONEACCESS-CELLULAR-MIB", "oacCellRssiLastHourMinutes"))
if mibBuilder.loadTexts: oacCellRssiLastHourEntry.setStatus('current')
if mibBuilder.loadTexts: oacCellRssiLastHourEntry.setDescription('An index into the table oacCellRssiLastHour')
oacCellRssiLastHourMinutes = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 1, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacCellRssiLastHourMinutes.setStatus('current')
if mibBuilder.loadTexts: oacCellRssiLastHourMinutes.setDescription('Timestamp (in minutes)')
oacCellRssiLastHourMin = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacCellRssiLastHourMin.setStatus('current')
if mibBuilder.loadTexts: oacCellRssiLastHourMin.setDescription('RSSI Minimum')
oacCellRssiLastHourAvg = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 1, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacCellRssiLastHourAvg.setStatus('current')
if mibBuilder.loadTexts: oacCellRssiLastHourAvg.setDescription('RSSI Average')
oacCellRssiLastHourMax = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 1, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacCellRssiLastHourMax.setStatus('current')
if mibBuilder.loadTexts: oacCellRssiLastHourMax.setDescription('RSSI Maximum')
oacCellRssiLastDayTable = MibTable((1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 1, 2), )
if mibBuilder.loadTexts: oacCellRssiLastDayTable.setStatus('current')
if mibBuilder.loadTexts: oacCellRssiLastDayTable.setDescription('RSSI values of the last day.')
oacCellRssiLastDayEntry = MibTableRow((1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 1, 2, 1), ).setIndexNames((0, "ONEACCESS-CELLULAR-MIB", "oacCellRssiLastDayHours"))
if mibBuilder.loadTexts: oacCellRssiLastDayEntry.setStatus('current')
if mibBuilder.loadTexts: oacCellRssiLastDayEntry.setDescription('An index into the table oacCellRssiLastDay')
oacCellRssiLastDayHours = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 1, 2, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacCellRssiLastDayHours.setStatus('current')
if mibBuilder.loadTexts: oacCellRssiLastDayHours.setDescription('Timestamp (in hours)')
oacCellRssiLastDayMin = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 1, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacCellRssiLastDayMin.setStatus('current')
if mibBuilder.loadTexts: oacCellRssiLastDayMin.setDescription('RSSI Minimum')
oacCellRssiLastDayAvg = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 1, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacCellRssiLastDayAvg.setStatus('current')
if mibBuilder.loadTexts: oacCellRssiLastDayAvg.setDescription('RSSI Average')
oacCellRssiLastDayMax = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 1, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacCellRssiLastDayMax.setStatus('current')
if mibBuilder.loadTexts: oacCellRssiLastDayMax.setDescription('RSSI Maximum')
oacCellRssiLastMonthTable = MibTable((1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 1, 3), )
if mibBuilder.loadTexts: oacCellRssiLastMonthTable.setStatus('current')
if mibBuilder.loadTexts: oacCellRssiLastMonthTable.setDescription('RSSI values of the last month.')
oacCellRssiLastMonthEntry = MibTableRow((1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 1, 3, 1), ).setIndexNames((0, "ONEACCESS-CELLULAR-MIB", "oacCellRssiLastMonthDays"))
if mibBuilder.loadTexts: oacCellRssiLastMonthEntry.setStatus('current')
if mibBuilder.loadTexts: oacCellRssiLastMonthEntry.setDescription('An index into the table oacCellRssiLastMonth')
oacCellRssiLastMonthDays = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 1, 3, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacCellRssiLastMonthDays.setStatus('current')
if mibBuilder.loadTexts: oacCellRssiLastMonthDays.setDescription('Timestamp (in days)')
oacCellRssiLastMonthMin = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 1, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacCellRssiLastMonthMin.setStatus('current')
if mibBuilder.loadTexts: oacCellRssiLastMonthMin.setDescription('RSSI Minimum')
oacCellRssiLastMonthAvg = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 1, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacCellRssiLastMonthAvg.setStatus('current')
if mibBuilder.loadTexts: oacCellRssiLastMonthAvg.setDescription('RSSI Average')
oacCellRssiLastMonthMax = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 1, 3, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacCellRssiLastMonthMax.setStatus('current')
if mibBuilder.loadTexts: oacCellRssiLastMonthMax.setDescription('RSSI Maximum')
oacCellRadioModuleTable = MibTable((1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 2), )
if mibBuilder.loadTexts: oacCellRadioModuleTable.setStatus('current')
if mibBuilder.loadTexts: oacCellRadioModuleTable.setDescription('Table of cellular modules.')
oacCellRadioModuleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 2, 1), ).setIndexNames((0, "ONEACCESS-CELLULAR-MIB", "oacCellModuleIndex"))
if mibBuilder.loadTexts: oacCellRadioModuleEntry.setStatus('current')
if mibBuilder.loadTexts: oacCellRadioModuleEntry.setDescription('An index into the table oacCellRadioModule')
oacCellModuleIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 2, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacCellModuleIndex.setStatus('current')
if mibBuilder.loadTexts: oacCellModuleIndex.setDescription('Index')
oacCellManufacturer = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 2, 1, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacCellManufacturer.setStatus('current')
if mibBuilder.loadTexts: oacCellManufacturer.setDescription('Manufacturer identification')
oacCellEquipment = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 2, 1, 11), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacCellEquipment.setStatus('current')
if mibBuilder.loadTexts: oacCellEquipment.setDescription('Equipment information')
oacCellBootRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 2, 1, 12), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacCellBootRevision.setStatus('current')
if mibBuilder.loadTexts: oacCellBootRevision.setDescription('Boot revision identification')
oacCellRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 2, 1, 13), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacCellRevision.setStatus('current')
if mibBuilder.loadTexts: oacCellRevision.setDescription('Revision identification')
oacCellIMEI = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 2, 1, 14), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacCellIMEI.setStatus('current')
if mibBuilder.loadTexts: oacCellIMEI.setDescription('Equipment information (IMEI)')
oacCellMEID = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 2, 1, 15), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacCellMEID.setStatus('current')
if mibBuilder.loadTexts: oacCellMEID.setDescription('CDMA Mobile Equipment Id (MEID)')
oacCellSIMStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 2, 1, 20), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacCellSIMStatus.setStatus('current')
if mibBuilder.loadTexts: oacCellSIMStatus.setDescription('SIM card status')
oacCellIMSI = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 2, 1, 21), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacCellIMSI.setStatus('current')
if mibBuilder.loadTexts: oacCellIMSI.setDescription('SIM International Mobile Subscriber Identity IMSI')
oacCellICCI = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 2, 1, 22), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacCellICCI.setStatus('current')
if mibBuilder.loadTexts: oacCellICCI.setDescription('Integrated Circuit Card ID')
oacCellPinStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 2, 1, 30), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacCellPinStatus.setStatus('current')
if mibBuilder.loadTexts: oacCellPinStatus.setDescription('PIN code status')
oacCellSelectedOperator = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 2, 1, 40), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacCellSelectedOperator.setStatus('current')
if mibBuilder.loadTexts: oacCellSelectedOperator.setDescription('Current selected operator')
oacCellSignalStrength = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 2, 1, 41), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacCellSignalStrength.setStatus('current')
if mibBuilder.loadTexts: oacCellSignalStrength.setDescription('Signal strength (dBm)')
oacCellEcIo = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 2, 1, 42), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacCellEcIo.setStatus('current')
if mibBuilder.loadTexts: oacCellEcIo.setDescription('Total Ec/Io')
oacCellRSRQ = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 2, 1, 43), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacCellRSRQ.setStatus('current')
if mibBuilder.loadTexts: oacCellRSRQ.setDescription('RSRQ (dB)')
oacCellRSRP = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 2, 1, 44), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacCellRSRP.setStatus('current')
if mibBuilder.loadTexts: oacCellRSRP.setDescription('RSRP (dBm)')
oacCellSNR = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 2, 1, 45), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacCellSNR.setStatus('current')
if mibBuilder.loadTexts: oacCellSNR.setDescription('SNR (dB)')
oacCellRadioAccessTechnology = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 2, 1, 46), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacCellRadioAccessTechnology.setStatus('current')
if mibBuilder.loadTexts: oacCellRadioAccessTechnology.setDescription('Current radio access technology')
oacCellCircuitSwitchedState = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 2, 1, 47), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacCellCircuitSwitchedState.setStatus('current')
if mibBuilder.loadTexts: oacCellCircuitSwitchedState.setDescription('Circuit-switched register state')
oacCellPacketSwitchedState = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 2, 1, 48), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacCellPacketSwitchedState.setStatus('current')
if mibBuilder.loadTexts: oacCellPacketSwitchedState.setDescription('Packet-switched attach state')
oacCellResetOnLossOfRegistration = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 2, 1, 60), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacCellResetOnLossOfRegistration.setStatus('current')
if mibBuilder.loadTexts: oacCellResetOnLossOfRegistration.setDescription('Reset on loss of GPRS registration')
oacCellResetOnFailedRegistration = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 2, 1, 61), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacCellResetOnFailedRegistration.setStatus('current')
if mibBuilder.loadTexts: oacCellResetOnFailedRegistration.setDescription('Reset on failed initial registration')
oacCellHardwareReset = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 2, 1, 62), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacCellHardwareReset.setStatus('current')
if mibBuilder.loadTexts: oacCellHardwareReset.setDescription('Hardware reset of modem')
oacCellLAC = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 2, 1, 70), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacCellLAC.setStatus('current')
if mibBuilder.loadTexts: oacCellLAC.setDescription('Location Area Code (LAC)')
oacCellCellID = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 2, 1, 71), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacCellCellID.setStatus('current')
if mibBuilder.loadTexts: oacCellCellID.setDescription('Cell ID')
oacCellTAC = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 2, 1, 72), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacCellTAC.setStatus('current')
if mibBuilder.loadTexts: oacCellTAC.setDescription('Tracking Area Code (TAC)')
oacCellPLMN = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 2, 1, 73), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacCellPLMN.setStatus('current')
if mibBuilder.loadTexts: oacCellPLMN.setDescription('Public Land Mobile Network (PLMN = MCC+MNC)')
mibBuilder.exportSymbols("ONEACCESS-CELLULAR-MIB", oacCellRevision=oacCellRevision, oacCellRssiLastDayTable=oacCellRssiLastDayTable, oacCellSNR=oacCellSNR, oacCellRssiLastDayAvg=oacCellRssiLastDayAvg, oacCellEquipment=oacCellEquipment, oacCellRssiLastDayMin=oacCellRssiLastDayMin, oacCellICCI=oacCellICCI, oacCellBootRevision=oacCellBootRevision, oacCellModuleIndex=oacCellModuleIndex, oacCellHardwareReset=oacCellHardwareReset, oacCellRssiLastHourEntry=oacCellRssiLastHourEntry, oacCellRssiLastMonthMax=oacCellRssiLastMonthMax, oacCellRadioAccessTechnology=oacCellRadioAccessTechnology, PYSNMP_MODULE_ID=oacCellularMIBModule, oacCellCircuitSwitchedState=oacCellCircuitSwitchedState, oacCellRssiLastMonthMin=oacCellRssiLastMonthMin, oacCellRssiLastDayEntry=oacCellRssiLastDayEntry, oacCellRssiLastHourMinutes=oacCellRssiLastHourMinutes, oacCellRssiLastDayHours=oacCellRssiLastDayHours, oacCellLAC=oacCellLAC, oacCellRSRP=oacCellRSRP, oacCellMEID=oacCellMEID, oacCellularMIBModule=oacCellularMIBModule, oacCellRadioModuleEntry=oacCellRadioModuleEntry, oacCellEcIo=oacCellEcIo, oacCellRssiLastMonthDays=oacCellRssiLastMonthDays, oacCellIMSI=oacCellIMSI, oacCellRssiLastHourMax=oacCellRssiLastHourMax, oacCellSignalStrength=oacCellSignalStrength, oacCellRssiLastHourTable=oacCellRssiLastHourTable, oacCellCellID=oacCellCellID, oacCellSelectedOperator=oacCellSelectedOperator, oacCellPLMN=oacCellPLMN, oacCellRadioModuleTable=oacCellRadioModuleTable, oacCellRssiLastHourAvg=oacCellRssiLastHourAvg, oacCellResetOnFailedRegistration=oacCellResetOnFailedRegistration, oacCellRssiLastMonthTable=oacCellRssiLastMonthTable, oacCellPacketSwitchedState=oacCellPacketSwitchedState, oacCellManufacturer=oacCellManufacturer, oacCellSIMStatus=oacCellSIMStatus, oacCellPinStatus=oacCellPinStatus, oacCellResetOnLossOfRegistration=oacCellResetOnLossOfRegistration, oacCellRssiLastMonthAvg=oacCellRssiLastMonthAvg, oacCellRssiLastMonthEntry=oacCellRssiLastMonthEntry, oacCellRSRQ=oacCellRSRQ, oacCellIMEI=oacCellIMEI, oacCellRssiLastDayMax=oacCellRssiLastDayMax, oacCellRssiLastHourMin=oacCellRssiLastHourMin, oacCellTAC=oacCellTAC, oacCellRadioRssi=oacCellRadioRssi)
