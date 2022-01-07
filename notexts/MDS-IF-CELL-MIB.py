#
# PySNMP MIB module MDS-IF-CELL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/gemds/MDS-IF-CELL-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:22:30 2022
# On host fv-az36-988 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
mdsInterfaces, = mibBuilder.importSymbols("MDS-ORBIT-SMI-MIB", "mdsInterfaces")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Integer32, Counter32, IpAddress, Unsigned32, MibIdentifier, Bits, NotificationType, TimeTicks, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Counter64, ObjectIdentity, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Counter32", "IpAddress", "Unsigned32", "MibIdentifier", "Bits", "NotificationType", "TimeTicks", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Counter64", "ObjectIdentity", "ModuleIdentity")
TextualConvention, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TruthValue")
mdsIfCellMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4130, 10, 2, 1))
mdsIfCellMIB.setRevisions(('2019-12-23 00:00', '2019-10-11 00:00', '2018-05-16 00:00', '2018-02-28 00:00', '2016-10-11 00:00', '2016-02-25 00:00', '2015-09-15 00:00', '2015-08-03 00:00', '2015-07-23 00:00', '2015-01-29 00:00', '2014-11-25 00:00', '2014-10-20 00:00', '2013-04-22 00:00',))
if mibBuilder.loadTexts: mdsIfCellMIB.setLastUpdated('201805160000Z')
if mibBuilder.loadTexts: mdsIfCellMIB.setOrganization('GE MDS LLC http://www.gemds.com')
mIfCellMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1))
mIfCellConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 1))
mIfCellStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 2))
mIfCellFwStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 3))
class UnsignedByte(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 255)

class SimSlotState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("notInserted", 0), ("inserted", 1))

mIfCellStatusTable = MibTable((1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 2, 1), )
if mibBuilder.loadTexts: mIfCellStatusTable.setStatus('current')
mIfCellStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: mIfCellStatusEntry.setStatus('current')
mIfCellImsi = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 2, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfCellImsi.setStatus('current')
mIfCellImei = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 2, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfCellImei.setStatus('current')
mIfCellIccid = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 2, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfCellIccid.setStatus('current')
mIfCellMdn = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 2, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfCellMdn.setStatus('current')
mIfCellApn = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 2, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfCellApn.setStatus('current')
mIfCellAppSwVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 2, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfCellAppSwVersion.setStatus('current')
mIfCellModemSwVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 2, 1, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfCellModemSwVersion.setStatus('current')
mIfCellSimState = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 2, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("notInserted", 0), ("locked", 1), ("ready", 2), ("failed", 3), ("unknown", 4))).clone('notInserted')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfCellSimState.setStatus('current')
mIfCellModemState = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 2, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("unknown", 0), ("notRegistered", 1), ("searching", 2), ("registrationDenied", 3), ("idle", 4), ("connected", 5), ("fwRequired", 6))).clone('unknown')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfCellModemState.setStatus('current')
mIfCellRoamingState = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 2, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("unknown", 0), ("home", 1), ("roaming", 2))).clone('unknown')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfCellRoamingState.setStatus('current')
mIfCellServiceState = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 2, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14))).clone(namedValues=NamedValues(("none", 0), ("gprs", 1), ("edge", 2), ("umts", 3), ("hsdpa", 4), ("hsupa", 5), ("hspaPlus", 6), ("is95a", 7), ("is95b", 8), ("onexRtt", 9), ("evdoRev0", 10), ("evdoReva", 11), ("evdoRevb", 12), ("evdoEhrpd", 13), ("lte", 14))).clone('none')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfCellServiceState.setStatus('current')
mIfCellRssi = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 2, 1, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfCellRssi.setStatus('current')
mIfCellRsrp = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 2, 1, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfCellRsrp.setStatus('current')
mIfCellRsrq = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 2, 1, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfCellRsrq.setStatus('current')
mIfCellSnr = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 2, 1, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfCellSnr.setStatus('current')
mIfCellEcio = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 2, 1, 1, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfCellEcio.setStatus('current')
mIfCellModemType = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 2, 1, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))).clone(namedValues=NamedValues(("typeUnknown", 0), ("typeE4VLteNaVerizon", 1), ("type3G1GsmGlobal", 2), ("typeE4xLteEmea", 3), ("type4GxLteNa", 4), ("type4GPLteNa", 5), ("typeEZ1LteEmea", 6), ("type4GyLteNaEu", 7), ("type4GzLteApac", 8), ("type4GaLteGlobal", 9), ("type4GbLteAmericas", 10), ("type4GcLteEu", 11), ("type4GdLteGlobal", 12))).clone('typeUnknown')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfCellModemType.setStatus('current')
mIfCellModemPackageVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 2, 1, 1, 18), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfCellModemPackageVersion.setStatus('current')
mIfCellTac = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 2, 1, 1, 19), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfCellTac.setStatus('current')
mIfCellGlobalCellId = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 2, 1, 1, 20), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfCellGlobalCellId.setStatus('current')
mIfCellPhysicalCellId = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 2, 1, 1, 21), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfCellPhysicalCellId.setStatus('current')
mIfCellBand = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 2, 1, 1, 22), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfCellBand.setStatus('current')
mIfCellBandwidth = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 2, 1, 1, 23), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("bwUnknown", 0), ("bw1dot4Mhz", 1), ("bw3Mhz", 2), ("bw5Mhz", 3), ("bw10Mhz", 4), ("bw15Mhz", 5), ("bw20Mhz", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfCellBandwidth.setStatus('current')
mIfCellTxChan = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 2, 1, 1, 24), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfCellTxChan.setStatus('current')
mIfCellRxChan = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 2, 1, 1, 25), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfCellRxChan.setStatus('current')
mIfCellEmmState = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 2, 1, 1, 26), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("emmUnknown", 0), ("emmDeregistered", 1), ("emmRegInitiated", 2), ("emmRegistered", 3), ("emmTauInitiated", 4), ("emmSrInitiated", 5), ("emmDeregInitiated", 6), ("emmInvalid", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfCellEmmState.setStatus('current')
mIfCellRrcState = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 2, 1, 1, 27), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("rrcUnknown", 0), ("rrcIdle", 1), ("rrcWaiting", 2), ("rrcConnected", 3), ("rrcReleasing", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfCellRrcState.setStatus('current')
mIfCellActiveSimSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 2, 1, 1, 28), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("simA", 0), ("simB", 1))).clone('simA')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfCellActiveSimSlot.setStatus('current')
mIfCellSimASlotState = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 2, 1, 1, 29), SimSlotState().clone('notInserted')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfCellSimASlotState.setStatus('current')
mIfCellSimBSlotState = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 2, 1, 1, 30), SimSlotState().clone('notInserted')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfCellSimBSlotState.setStatus('current')
mIfCellFwStatusTable = MibTable((1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 3, 1), )
if mibBuilder.loadTexts: mIfCellFwStatusTable.setStatus('current')
mIfCellFwStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 3, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "MDS-IF-CELL-MIB", "mIfCellFwId"))
if mibBuilder.loadTexts: mIfCellFwStatusEntry.setStatus('current')
mIfCellFwId = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 3, 1, 1, 1), UnsignedByte()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfCellFwId.setStatus('current')
mIfCellFwVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 3, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfCellFwVersion.setStatus('current')
mIfCellFwActive = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 1, 3, 1, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfCellFwActive.setStatus('current')
mdsIfCellMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 3))
mdsIfCellMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 3, 1))
mdsIfCellMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 3, 2))
mIfCellCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 3, 1, 1)).setObjects(("MDS-IF-CELL-MIB", "mIfCellStatusGroup"), ("MDS-IF-CELL-MIB", "mIfCellFwStatusGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mIfCellCompliance = mIfCellCompliance.setStatus('current')
mIfCellStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 3, 2, 1)).setObjects(("MDS-IF-CELL-MIB", "mIfCellImsi"), ("MDS-IF-CELL-MIB", "mIfCellImei"), ("MDS-IF-CELL-MIB", "mIfCellIccid"), ("MDS-IF-CELL-MIB", "mIfCellMdn"), ("MDS-IF-CELL-MIB", "mIfCellApn"), ("MDS-IF-CELL-MIB", "mIfCellAppSwVersion"), ("MDS-IF-CELL-MIB", "mIfCellModemSwVersion"), ("MDS-IF-CELL-MIB", "mIfCellSimState"), ("MDS-IF-CELL-MIB", "mIfCellModemState"), ("MDS-IF-CELL-MIB", "mIfCellRoamingState"), ("MDS-IF-CELL-MIB", "mIfCellServiceState"), ("MDS-IF-CELL-MIB", "mIfCellRssi"), ("MDS-IF-CELL-MIB", "mIfCellRsrp"), ("MDS-IF-CELL-MIB", "mIfCellRsrq"), ("MDS-IF-CELL-MIB", "mIfCellSnr"), ("MDS-IF-CELL-MIB", "mIfCellEcio"), ("MDS-IF-CELL-MIB", "mIfCellModemType"), ("MDS-IF-CELL-MIB", "mIfCellModemPackageVersion"), ("MDS-IF-CELL-MIB", "mIfCellTac"), ("MDS-IF-CELL-MIB", "mIfCellGlobalCellId"), ("MDS-IF-CELL-MIB", "mIfCellPhysicalCellId"), ("MDS-IF-CELL-MIB", "mIfCellBand"), ("MDS-IF-CELL-MIB", "mIfCellBandwidth"), ("MDS-IF-CELL-MIB", "mIfCellTxChan"), ("MDS-IF-CELL-MIB", "mIfCellRxChan"), ("MDS-IF-CELL-MIB", "mIfCellEmmState"), ("MDS-IF-CELL-MIB", "mIfCellRrcState"), ("MDS-IF-CELL-MIB", "mIfCellActiveSimSlot"), ("MDS-IF-CELL-MIB", "mIfCellSimASlotState"), ("MDS-IF-CELL-MIB", "mIfCellSimBSlotState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mIfCellStatusGroup = mIfCellStatusGroup.setStatus('current')
mIfCellFwStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4130, 10, 2, 1, 3, 2, 2)).setObjects(("MDS-IF-CELL-MIB", "mIfCellFwId"), ("MDS-IF-CELL-MIB", "mIfCellFwVersion"), ("MDS-IF-CELL-MIB", "mIfCellFwActive"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mIfCellFwStatusGroup = mIfCellFwStatusGroup.setStatus('current')
mibBuilder.exportSymbols("MDS-IF-CELL-MIB", mIfCellSnr=mIfCellSnr, mIfCellFwStatus=mIfCellFwStatus, mIfCellTxChan=mIfCellTxChan, mdsIfCellMIBGroups=mdsIfCellMIBGroups, mIfCellGlobalCellId=mIfCellGlobalCellId, mIfCellModemType=mIfCellModemType, mIfCellBandwidth=mIfCellBandwidth, mIfCellModemState=mIfCellModemState, mIfCellTac=mIfCellTac, mIfCellApn=mIfCellApn, mIfCellStatusGroup=mIfCellStatusGroup, mIfCellRxChan=mIfCellRxChan, mIfCellSimBSlotState=mIfCellSimBSlotState, mIfCellActiveSimSlot=mIfCellActiveSimSlot, mdsIfCellMIBCompliances=mdsIfCellMIBCompliances, mdsIfCellMIB=mdsIfCellMIB, mIfCellRsrp=mIfCellRsrp, mIfCellFwActive=mIfCellFwActive, mIfCellAppSwVersion=mIfCellAppSwVersion, mIfCellModemSwVersion=mIfCellModemSwVersion, mIfCellRssi=mIfCellRssi, mIfCellFwId=mIfCellFwId, PYSNMP_MODULE_ID=mdsIfCellMIB, mIfCellFwStatusTable=mIfCellFwStatusTable, mIfCellMIBObjects=mIfCellMIBObjects, mIfCellFwStatusGroup=mIfCellFwStatusGroup, UnsignedByte=UnsignedByte, mIfCellCompliance=mIfCellCompliance, mIfCellServiceState=mIfCellServiceState, mIfCellEcio=mIfCellEcio, mIfCellRrcState=mIfCellRrcState, mIfCellPhysicalCellId=mIfCellPhysicalCellId, mIfCellStatus=mIfCellStatus, mIfCellImei=mIfCellImei, mIfCellSimState=mIfCellSimState, mIfCellFwVersion=mIfCellFwVersion, mIfCellEmmState=mIfCellEmmState, mIfCellIccid=mIfCellIccid, mIfCellImsi=mIfCellImsi, mIfCellSimASlotState=mIfCellSimASlotState, mIfCellBand=mIfCellBand, mIfCellRsrq=mIfCellRsrq, mIfCellFwStatusEntry=mIfCellFwStatusEntry, mIfCellConfig=mIfCellConfig, mIfCellStatusTable=mIfCellStatusTable, mIfCellRoamingState=mIfCellRoamingState, mdsIfCellMIBConformance=mdsIfCellMIBConformance, mIfCellStatusEntry=mIfCellStatusEntry, mIfCellMdn=mIfCellMdn, SimSlotState=SimSlotState, mIfCellModemPackageVersion=mIfCellModemPackageVersion)
