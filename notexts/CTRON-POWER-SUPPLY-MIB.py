#
# PySNMP MIB module CTRON-POWER-SUPPLY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-POWER-SUPPLY-MIB
# Produced by pysmi-1.1.8 at Sun Jan 16 00:36:31 2022
# On host fv-az42-839 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ctps, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctps")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, ObjectIdentity, MibIdentifier, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, IpAddress, Bits, Counter64, ModuleIdentity, NotificationType, Counter32, Gauge32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "ObjectIdentity", "MibIdentifier", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "IpAddress", "Bits", "Counter64", "ModuleIdentity", "NotificationType", "Counter32", "Gauge32", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
chPower = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 1))
boardPower = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 2))
psPower = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 3))
bbuPower = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 4))
termPower = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 5))
chPowerOperationalStatus = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("powerAC", 1), ("powerACRedundant", 2), ("powerDC", 3), ("powerDCRedundant", 4), ("battery", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chPowerOperationalStatus.setStatus('mandatory')
chPowerMainVoltageStatus = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("powerOK", 1), ("overCurrent", 2), ("overVoltage", 3), ("underVoltage", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chPowerMainVoltageStatus.setStatus('mandatory')
chPowerMainVoltage = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chPowerMainVoltage.setStatus('mandatory')
chPowerTotalSupply = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chPowerTotalSupply.setStatus('mandatory')
chPowerTotalLoad = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chPowerTotalLoad.setStatus('mandatory')
chPowerMaxSupply = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chPowerMaxSupply.setStatus('mandatory')
chPowerMaxLoad = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chPowerMaxLoad.setStatus('mandatory')
chPowerTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 1, 8), )
if mibBuilder.loadTexts: chPowerTable.setStatus('mandatory')
chPowerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 1, 8, 1), ).setIndexNames((0, "CTRON-POWER-SUPPLY-MIB", "chPowerLineID"))
if mibBuilder.loadTexts: chPowerEntry.setStatus('mandatory')
chPowerLineID = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 1, 8, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chPowerLineID.setStatus('mandatory')
chPowerLineType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 1, 8, 1, 2), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chPowerLineType.setStatus('mandatory')
chPowerLineTotalSupply = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 1, 8, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chPowerLineTotalSupply.setStatus('mandatory')
chPowerLineTotalLoad = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 1, 8, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chPowerLineTotalLoad.setStatus('mandatory')
chPowerLineMaxSupply = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 1, 8, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chPowerLineMaxSupply.setStatus('mandatory')
chPowerLineMaxLoad = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 1, 8, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chPowerLineMaxLoad.setStatus('mandatory')
chPowerDiagVoltageStatus = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("powerOK", 1), ("overCurrent", 2), ("overVoltage", 3), ("underVoltage", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chPowerDiagVoltageStatus.setStatus('mandatory')
chPowerDiagVoltage = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chPowerDiagVoltage.setStatus('mandatory')
boardPowerSlotStatusTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 2, 1), )
if mibBuilder.loadTexts: boardPowerSlotStatusTable.setStatus('mandatory')
boardPowerSlotStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 2, 1, 1), ).setIndexNames((0, "CTRON-POWER-SUPPLY-MIB", "boardPowerSlotStatusID"))
if mibBuilder.loadTexts: boardPowerSlotStatusEntry.setStatus('mandatory')
boardPowerSlotStatusID = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: boardPowerSlotStatusID.setStatus('mandatory')
boardPowerOperationalStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))).clone(namedValues=NamedValues(("powerOn", 1), ("powerOff", 2), ("reset", 3), ("overVoltage", 4), ("underVoltage", 5), ("overCurrent", 6), ("overCurrentShutdown", 7), ("temperatureShutdown", 8), ("remotePowerOff", 9), ("powerConservationShutdown", 10), ("frontPanelPowerOff", 11)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: boardPowerOperationalStatus.setStatus('mandatory')
boardPowerAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("powerOn", 1), ("powerOff", 2), ("reset", 3))).clone('powerOn')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: boardPowerAdminStatus.setStatus('mandatory')
boardPowerLocalAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("localMode", 1), ("secureMode", 2))).clone('localMode')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: boardPowerLocalAdminStatus.setStatus('mandatory')
boardPowerLocalStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("resetRequest", 1), ("powerDownRequest", 2), ("powerOnRequest", 3), ("normal", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: boardPowerLocalStatus.setStatus('mandatory')
boardPowerShutdownAdmin = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: boardPowerShutdownAdmin.setStatus('mandatory')
boardPowerPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 2, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 14)).clone(14)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: boardPowerPriority.setStatus('mandatory')
boardPowerMaxInputPower = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 2, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: boardPowerMaxInputPower.setStatus('mandatory')
boardPowerManagement = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 2, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 7))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2), ("not-supported", 7))).clone('not-supported')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: boardPowerManagement.setStatus('mandatory')
boardPowerSlotTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 2, 2), )
if mibBuilder.loadTexts: boardPowerSlotTable.setStatus('mandatory')
boardPowerSlotEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 2, 2, 1), ).setIndexNames((0, "CTRON-POWER-SUPPLY-MIB", "boardPowerSlotID"), (0, "CTRON-POWER-SUPPLY-MIB", "boardPowerID"))
if mibBuilder.loadTexts: boardPowerSlotEntry.setStatus('mandatory')
boardPowerSlotID = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 2, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: boardPowerSlotID.setStatus('mandatory')
boardPowerID = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 2, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: boardPowerID.setStatus('mandatory')
boardPowerType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 2, 2, 1, 3), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: boardPowerType.setStatus('mandatory')
boardPowerStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 2, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("powerOK", 1), ("powerOff", 2), ("overCurrent", 3), ("overVoltage", 4), ("underVoltage", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: boardPowerStatus.setStatus('mandatory')
boardPowerVoltage = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 2, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: boardPowerVoltage.setStatus('mandatory')
boardPowerCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 2, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: boardPowerCurrent.setStatus('mandatory')
boardPowerMaxVoltage = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 2, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: boardPowerMaxVoltage.setStatus('mandatory')
boardPowerMinVoltage = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 2, 2, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: boardPowerMinVoltage.setStatus('mandatory')
boardPowerMaxPower = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 2, 2, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: boardPowerMaxPower.setStatus('mandatory')
psPowerSlotStatusTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 3, 1), )
if mibBuilder.loadTexts: psPowerSlotStatusTable.setStatus('mandatory')
psPowerSlotStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 3, 1, 1), ).setIndexNames((0, "CTRON-POWER-SUPPLY-MIB", "psPowerSlotStatusID"))
if mibBuilder.loadTexts: psPowerSlotStatusEntry.setStatus('mandatory')
psPowerSlotStatusID = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 3, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psPowerSlotStatusID.setStatus('mandatory')
psPowerOperationalStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("powerOn", 1), ("powerOff", 2), ("reset", 3), ("overVoltage", 4), ("underVoltage", 5), ("overCurrent", 6), ("overCurrentShutdown", 7), ("temperatureShutdown", 8), ("remotePowerOff", 9)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psPowerOperationalStatus.setStatus('mandatory')
psPowerAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("powerOn", 1), ("powerOff", 2))).clone('powerOn')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: psPowerAdminStatus.setStatus('mandatory')
psPowerMaxOutputPower = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 3, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psPowerMaxOutputPower.setStatus('mandatory')
psPowerSlotTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 3, 2), )
if mibBuilder.loadTexts: psPowerSlotTable.setStatus('mandatory')
psPowerSlotEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 3, 2, 1), ).setIndexNames((0, "CTRON-POWER-SUPPLY-MIB", "psPowerSlotID"), (0, "CTRON-POWER-SUPPLY-MIB", "psPowerID"))
if mibBuilder.loadTexts: psPowerSlotEntry.setStatus('mandatory')
psPowerSlotID = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 3, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psPowerSlotID.setStatus('mandatory')
psPowerID = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 3, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psPowerID.setStatus('mandatory')
psPowerType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 3, 2, 1, 3), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psPowerType.setStatus('mandatory')
psPowerStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 3, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("powerOK", 1), ("powerOff", 2), ("overCurrent", 3), ("overVoltage", 4), ("underVoltage", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psPowerStatus.setStatus('mandatory')
psPowerAdmin = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 3, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("powerOn", 1), ("powerOff", 2))).clone('powerOn')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: psPowerAdmin.setStatus('mandatory')
psPowerVoltage = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 3, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psPowerVoltage.setStatus('mandatory')
psPowerCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 3, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psPowerCurrent.setStatus('mandatory')
psPowerLineFrequency = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 3, 2, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psPowerLineFrequency.setStatus('mandatory')
psPowerMaxVoltage = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 3, 2, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psPowerMaxVoltage.setStatus('mandatory')
psPowerMinVoltage = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 3, 2, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psPowerMinVoltage.setStatus('mandatory')
psPowerMaxPower = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 3, 2, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psPowerMaxPower.setStatus('mandatory')
termPowerStatus = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 5, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("powerOK", 1), ("overCurrent", 2), ("overVoltage", 3), ("underVolatge", 4), ("overPower", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: termPowerStatus.setStatus('mandatory')
termPowerVoltage = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 5, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: termPowerVoltage.setStatus('mandatory')
termPowerCurrent = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 5, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: termPowerCurrent.setStatus('mandatory')
termPowerModule1Status = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 5, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("normal", 1), ("iNBaFault", 2), ("iNBbFault", 3), ("fault", 4), ("termModuleNotInstalled", 5), ("unknown", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: termPowerModule1Status.setStatus('mandatory')
termPowerModule2Status = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 5, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("normal", 1), ("iNBaFault", 2), ("iNBbFault", 3), ("fault", 4), ("termModuleNotInstalled", 5), ("unknown", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: termPowerModule2Status.setStatus('mandatory')
mibBuilder.exportSymbols("CTRON-POWER-SUPPLY-MIB", boardPowerMaxInputPower=boardPowerMaxInputPower, boardPowerSlotStatusEntry=boardPowerSlotStatusEntry, boardPowerSlotStatusTable=boardPowerSlotStatusTable, chPowerLineTotalLoad=chPowerLineTotalLoad, termPower=termPower, boardPowerMaxVoltage=boardPowerMaxVoltage, psPowerSlotID=psPowerSlotID, boardPowerStatus=boardPowerStatus, psPower=psPower, boardPowerShutdownAdmin=boardPowerShutdownAdmin, chPowerMaxLoad=chPowerMaxLoad, psPowerCurrent=psPowerCurrent, boardPowerPriority=boardPowerPriority, psPowerSlotStatusEntry=psPowerSlotStatusEntry, psPowerAdminStatus=psPowerAdminStatus, chPowerTable=chPowerTable, psPowerSlotTable=psPowerSlotTable, psPowerType=psPowerType, termPowerVoltage=termPowerVoltage, psPowerSlotStatusTable=psPowerSlotStatusTable, psPowerVoltage=psPowerVoltage, chPowerOperationalStatus=chPowerOperationalStatus, chPowerTotalLoad=chPowerTotalLoad, chPowerEntry=chPowerEntry, bbuPower=bbuPower, psPowerOperationalStatus=psPowerOperationalStatus, boardPower=boardPower, psPowerMinVoltage=psPowerMinVoltage, boardPowerSlotEntry=boardPowerSlotEntry, chPowerLineType=chPowerLineType, boardPowerMinVoltage=boardPowerMinVoltage, chPowerTotalSupply=chPowerTotalSupply, boardPowerID=boardPowerID, chPowerDiagVoltageStatus=chPowerDiagVoltageStatus, chPowerDiagVoltage=chPowerDiagVoltage, chPowerLineMaxSupply=chPowerLineMaxSupply, boardPowerSlotTable=boardPowerSlotTable, termPowerStatus=termPowerStatus, boardPowerLocalStatus=boardPowerLocalStatus, psPowerMaxPower=psPowerMaxPower, psPowerSlotEntry=psPowerSlotEntry, termPowerCurrent=termPowerCurrent, boardPowerOperationalStatus=boardPowerOperationalStatus, chPowerLineID=chPowerLineID, boardPowerManagement=boardPowerManagement, boardPowerSlotID=boardPowerSlotID, boardPowerVoltage=boardPowerVoltage, boardPowerCurrent=boardPowerCurrent, psPowerAdmin=psPowerAdmin, chPowerMaxSupply=chPowerMaxSupply, boardPowerSlotStatusID=boardPowerSlotStatusID, boardPowerMaxPower=boardPowerMaxPower, psPowerLineFrequency=psPowerLineFrequency, boardPowerAdminStatus=boardPowerAdminStatus, chPowerLineMaxLoad=chPowerLineMaxLoad, psPowerSlotStatusID=psPowerSlotStatusID, psPowerID=psPowerID, psPowerStatus=psPowerStatus, chPowerMainVoltageStatus=chPowerMainVoltageStatus, termPowerModule1Status=termPowerModule1Status, boardPowerType=boardPowerType, chPower=chPower, psPowerMaxOutputPower=psPowerMaxOutputPower, boardPowerLocalAdminStatus=boardPowerLocalAdminStatus, psPowerMaxVoltage=psPowerMaxVoltage, chPowerMainVoltage=chPowerMainVoltage, chPowerLineTotalSupply=chPowerLineTotalSupply, termPowerModule2Status=termPowerModule2Status)
