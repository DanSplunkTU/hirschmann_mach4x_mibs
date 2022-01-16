#
# PySNMP MIB module S5-CHASSIS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/nortel/S5-CHASSIS-MIB
# Produced by pysmi-1.1.8 at Sun Jan 16 00:41:34 2022
# On host fv-az42-839 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
Ipv6AddressPrefix, Ipv6Address = mibBuilder.importSymbols("IPV6-TC", "Ipv6AddressPrefix", "Ipv6Address")
s5Chassis, = mibBuilder.importSymbols("S5-ROOT-MIB", "s5Chassis")
LocChan, AttId = mibBuilder.importSymbols("S5-TCS-MIB", "LocChan", "AttId")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, NotificationType, Counter32, Unsigned32, MibIdentifier, iso, ObjectIdentity, Bits, Gauge32, Integer32, IpAddress, ModuleIdentity, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "NotificationType", "Counter32", "Unsigned32", "MibIdentifier", "iso", "ObjectIdentity", "Bits", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "Counter64")
TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString")
s5ChasMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 10))
s5ChasMib.setRevisions(('2015-04-07 00:00', '2013-11-26 00:00', '2013-10-18 00:00', '2013-10-16 00:00', '2013-10-10 00:00', '2013-09-09 00:00', '2013-08-27 00:00', '2012-12-20 00:00', '2012-06-01 00:00', '2012-02-21 00:00', '2011-10-11 00:00', '2011-04-22 00:00', '2010-10-18 00:00', '2008-05-22 00:00', '2008-02-20 00:00', '2005-05-11 00:00', '2005-05-05 00:00', '2004-10-29 00:00', '2004-07-20 00:00',))
if mibBuilder.loadTexts: s5ChasMib.setLastUpdated('201504070000Z')
if mibBuilder.loadTexts: s5ChasMib.setOrganization('Avaya')
s5ChasGen = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 1))
s5ChasGrp = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 2))
s5ChasCom = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 3))
s5ChasBrd = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 4))
s5ChasStore = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 5))
s5ChasSm = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 6))
s5ChasTmpSnr = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 7))
s5ChasUtil = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 8))
s5ChasPs = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 9))
s5ChasNotify = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 11))
s5ChasPluggables = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 12))
s5ChasType = MibScalar((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 1, 1), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5ChasType.setStatus('current')
s5ChasDescr = MibScalar((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5ChasDescr.setStatus('current')
s5ChasLocation = MibScalar((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: s5ChasLocation.setStatus('current')
s5ChasContact = MibScalar((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: s5ChasContact.setStatus('current')
s5ChasVer = MibScalar((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5ChasVer.setStatus('current')
s5ChasSerNum = MibScalar((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5ChasSerNum.setStatus('current')
s5ChasGblPhysChngs = MibScalar((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5ChasGblPhysChngs.setStatus('current')
s5ChasGblPhysLstChng = MibScalar((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 1, 8), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5ChasGblPhysLstChng.setStatus('current')
s5ChasGblAttChngs = MibScalar((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5ChasGblAttChngs.setStatus('current')
s5ChasGblAttLstChng = MibScalar((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 1, 10), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5ChasGblAttLstChng.setStatus('current')
s5ChasGblConfChngs = MibScalar((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5ChasGblConfChngs.setStatus('current')
s5ChasGblConfLstChng = MibScalar((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 1, 12), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5ChasGblConfLstChng.setStatus('current')
s5ChasGrpTable = MibTable((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 2, 1), )
if mibBuilder.loadTexts: s5ChasGrpTable.setStatus('current')
s5ChasGrpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 2, 1, 1), ).setIndexNames((0, "S5-CHASSIS-MIB", "s5ChasGrpIndx"))
if mibBuilder.loadTexts: s5ChasGrpEntry.setStatus('current')
s5ChasGrpIndx = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32767))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5ChasGrpIndx.setStatus('current')
s5ChasGrpType = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 2, 1, 1, 2), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5ChasGrpType.setStatus('current')
s5ChasGrpDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 2, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5ChasGrpDescr.setStatus('current')
s5ChasGrpMaxEnts = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 32767))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5ChasGrpMaxEnts.setStatus('current')
s5ChasGrpNumEnts = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 32767))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5ChasGrpNumEnts.setStatus('current')
s5ChasGrpPhysChngs = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 2, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5ChasGrpPhysChngs.setStatus('current')
s5ChasGrpPhysLstChng = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 2, 1, 1, 7), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5ChasGrpPhysLstChng.setStatus('current')
s5ChasGrpEncodeFactor = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 2, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5ChasGrpEncodeFactor.setStatus('current')
s5ChasComTable = MibTable((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 3, 1), )
if mibBuilder.loadTexts: s5ChasComTable.setStatus('current')
s5ChasComEntry = MibTableRow((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 3, 1, 1), ).setIndexNames((0, "S5-CHASSIS-MIB", "s5ChasComGrpIndx"), (0, "S5-CHASSIS-MIB", "s5ChasComIndx"), (0, "S5-CHASSIS-MIB", "s5ChasComSubIndx"))
if mibBuilder.loadTexts: s5ChasComEntry.setStatus('current')
s5ChasComGrpIndx = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32767))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5ChasComGrpIndx.setStatus('current')
s5ChasComIndx = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32767))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5ChasComIndx.setStatus('current')
s5ChasComSubIndx = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 32767))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5ChasComSubIndx.setStatus('current')
s5ChasComType = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 3, 1, 1, 4), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5ChasComType.setStatus('current')
s5ChasComDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 3, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5ChasComDescr.setStatus('current')
s5ChasComVer = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 3, 1, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5ChasComVer.setStatus('current')
s5ChasComSerNum = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 3, 1, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5ChasComSerNum.setStatus('current')
s5ChasComLstChng = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 3, 1, 1, 8), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5ChasComLstChng.setStatus('current')
s5ChasComAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 3, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("other", 1), ("notAvail", 2), ("disable", 3), ("enable", 4), ("reset", 5), ("test", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: s5ChasComAdminState.setStatus('current')
s5ChasComOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 3, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))).clone(namedValues=NamedValues(("other", 1), ("notAvail", 2), ("removed", 3), ("disabled", 4), ("normal", 5), ("resetInProg", 6), ("testing", 7), ("warning", 8), ("nonFatalErr", 9), ("fatalErr", 10), ("notConfig", 11), ("obsoleted", 12)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5ChasComOperState.setStatus('current')
s5ChasComMaxSubs = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 3, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 32767))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5ChasComMaxSubs.setStatus('current')
s5ChasComNumSubs = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 3, 1, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 32767))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5ChasComNumSubs.setStatus('current')
s5ChasComRelPos = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 3, 1, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 32767))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5ChasComRelPos.setStatus('current')
s5ChasComLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 3, 1, 1, 14), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: s5ChasComLocation.setStatus('current')
s5ChasComGroupMap = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 3, 1, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 32767))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5ChasComGroupMap.setStatus('current')
s5ChasComBaseNumPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 3, 1, 1, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 32767))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5ChasComBaseNumPorts.setStatus('current')
s5ChasComTotalNumPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 3, 1, 1, 17), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 32767))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5ChasComTotalNumPorts.setStatus('current')
s5ChasComIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 3, 1, 1, 18), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: s5ChasComIpAddress.setStatus('current')
s5ChasComRunningSoftwareVer = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 3, 1, 1, 19), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5ChasComRunningSoftwareVer.setStatus('current')
s5ChasComIpv6Address = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 3, 1, 1, 20), Ipv6Address()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: s5ChasComIpv6Address.setStatus('current')
s5ChasComIpv6NetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 3, 1, 1, 21), Ipv6AddressPrefix()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: s5ChasComIpv6NetMask.setStatus('current')
s5ChasComIpMgmtAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 3, 1, 1, 22), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: s5ChasComIpMgmtAddress.setStatus('current')
s5ChasComIpMgmtNetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 3, 1, 1, 23), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: s5ChasComIpMgmtNetMask.setStatus('current')
s5ChasComIpMgmtGateway = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 3, 1, 1, 24), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: s5ChasComIpMgmtGateway.setStatus('current')
s5ChasComIpv6MgmtAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 3, 1, 1, 25), Ipv6Address()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: s5ChasComIpv6MgmtAddress.setStatus('current')
s5ChasComIpv6MgmtNetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 3, 1, 1, 26), Ipv6AddressPrefix()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: s5ChasComIpv6MgmtNetMask.setStatus('current')
s5ChasComIpMgmtLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 3, 1, 1, 27), Integer32().subtype(subtypeSpec=ValueRangeConstraint(50, 10000)).clone(7000)).setUnits('packets per second').setMaxAccess("readwrite")
if mibBuilder.loadTexts: s5ChasComIpMgmtLimit.setStatus('current')
s5ChasComIpMgmtTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 3, 1, 1, 28), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 180)).clone(180)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: s5ChasComIpMgmtTimeout.setStatus('current')
s5ChasComIpMgmtShutdown = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 3, 1, 1, 29), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: s5ChasComIpMgmtShutdown.setStatus('current')
s5ChasComUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 3, 1, 1, 30), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5ChasComUpTime.setStatus('current')
s5ChasBrdTable = MibTable((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 4, 1), )
if mibBuilder.loadTexts: s5ChasBrdTable.setStatus('current')
s5ChasBrdEntry = MibTableRow((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 4, 1, 1), ).setIndexNames((0, "S5-CHASSIS-MIB", "s5ChasBrdIndx"))
if mibBuilder.loadTexts: s5ChasBrdEntry.setStatus('current')
s5ChasBrdIndx = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5ChasBrdIndx.setStatus('current')
s5ChasBrdLeds = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 4, 1, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5ChasBrdLeds.setStatus('current')
s5ChasBrdNumAtt = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 4, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5ChasBrdNumAtt.setStatus('current')
s5ChasBrdAttChngs = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 4, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5ChasBrdAttChngs.setStatus('current')
s5ChasBrdAttLstChng = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 4, 1, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5ChasBrdAttLstChng.setStatus('current')
s5ChasBrdStatusDsply = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 4, 1, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 48))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5ChasBrdStatusDsply.setStatus('current')
s5ChasBrdDateCode = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 4, 1, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5ChasBrdDateCode.setStatus('current')
s5ChasBrdCfgSrc = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 4, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("other", 1), ("dfltJmpr", 2), ("prmMem", 3), ("brdCfg", 4), ("sm", 5), ("smDfltJmpr", 6), ("smPrmMem", 7), ("smBrdCfg", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5ChasBrdCfgSrc.setStatus('current')
s5ChasBrdCfgChngs = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 4, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5ChasBrdCfgChngs.setStatus('current')
s5ChasBrdFanLeds = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 4, 1, 1, 10), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5ChasBrdFanLeds.setStatus('current')
s5ChasAttTable = MibTable((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 4, 2), )
if mibBuilder.loadTexts: s5ChasAttTable.setStatus('current')
s5ChasAttEntry = MibTableRow((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 4, 2, 1), ).setIndexNames((0, "S5-CHASSIS-MIB", "s5ChasAttBrdIndx"), (0, "S5-CHASSIS-MIB", "s5ChasAttIndx"))
if mibBuilder.loadTexts: s5ChasAttEntry.setStatus('current')
s5ChasAttBrdIndx = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 4, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5ChasAttBrdIndx.setStatus('current')
s5ChasAttIndx = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 4, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5ChasAttIndx.setStatus('current')
s5ChasAttDfltAtt = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 4, 2, 1, 3), AttId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5ChasAttDfltAtt.setStatus('current')
s5ChasAttCurAtt = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 4, 2, 1, 4), AttId()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: s5ChasAttCurAtt.setStatus('current')
s5ChasAttChngs = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 4, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5ChasAttChngs.setStatus('current')
s5ChasAttLstChng = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 4, 2, 1, 6), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5ChasAttLstChng.setStatus('current')
s5ChasAttClusterConnCapability = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 4, 2, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8)).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5ChasAttClusterConnCapability.setStatus('current')
s5ChasLocChanTable = MibTable((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 4, 3), )
if mibBuilder.loadTexts: s5ChasLocChanTable.setStatus('current')
s5ChasLocChanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 4, 3, 1), ).setIndexNames((0, "S5-CHASSIS-MIB", "s5ChasLocChanBrdIndx"), (0, "S5-CHASSIS-MIB", "s5ChasLocChanIndx"))
if mibBuilder.loadTexts: s5ChasLocChanEntry.setStatus('current')
s5ChasLocChanBrdIndx = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 4, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5ChasLocChanBrdIndx.setStatus('current')
s5ChasLocChanIndx = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 4, 3, 1, 2), LocChan()).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5ChasLocChanIndx.setStatus('current')
s5ChasLocChanBkplMode = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 4, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("connected", 2), ("notConnected", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: s5ChasLocChanBkplMode.setStatus('current')
s5ChasStoreTable = MibTable((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 5, 1), )
if mibBuilder.loadTexts: s5ChasStoreTable.setStatus('current')
s5ChasStoreEntry = MibTableRow((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 5, 1, 1), ).setIndexNames((0, "S5-CHASSIS-MIB", "s5ChasStoreGrpIndx"), (0, "S5-CHASSIS-MIB", "s5ChasStoreComIndx"), (0, "S5-CHASSIS-MIB", "s5ChasStoreSubIndx"), (0, "S5-CHASSIS-MIB", "s5ChasStoreIndx"))
if mibBuilder.loadTexts: s5ChasStoreEntry.setStatus('current')
s5ChasStoreGrpIndx = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 5, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32767))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5ChasStoreGrpIndx.setStatus('current')
s5ChasStoreComIndx = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 5, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32767))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5ChasStoreComIndx.setStatus('current')
s5ChasStoreSubIndx = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 5, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 32767))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5ChasStoreSubIndx.setStatus('current')
s5ChasStoreIndx = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 5, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5ChasStoreIndx.setStatus('current')
s5ChasStoreType = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 5, 1, 1, 5), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5ChasStoreType.setStatus('current')
s5ChasStoreCurSize = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 5, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5ChasStoreCurSize.setStatus('current')
s5ChasStoreCntntVer = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 5, 1, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5ChasStoreCntntVer.setStatus('current')
s5ChasStoreFilename = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 5, 1, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: s5ChasStoreFilename.setStatus('current')
s5ChasStoreUsedSize = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 5, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5ChasStoreUsedSize.setStatus('current')
s5ChasStoreDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 5, 1, 1, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5ChasStoreDescription.setStatus('current')
s5ChasStoreAge = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 5, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5ChasStoreAge.setStatus('current')
s5ChasSmLeds = MibScalar((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 6, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5ChasSmLeds.setStatus('current')
s5ChasSmDateCode = MibScalar((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 6, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5ChasSmDateCode.setStatus('current')
s5ChasTmpSnrTable = MibTable((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 7, 1), )
if mibBuilder.loadTexts: s5ChasTmpSnrTable.setStatus('current')
s5ChasTmpSnrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 7, 1, 1), ).setIndexNames((0, "S5-CHASSIS-MIB", "s5ChasTmpSnrGrpIndx"), (0, "S5-CHASSIS-MIB", "s5ChasTmpSnrIndx"), (0, "S5-CHASSIS-MIB", "s5ChasTmpSnrSubIndx"))
if mibBuilder.loadTexts: s5ChasTmpSnrEntry.setStatus('current')
s5ChasTmpSnrGrpIndx = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 7, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32767))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5ChasTmpSnrGrpIndx.setStatus('current')
s5ChasTmpSnrIndx = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 7, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32767))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5ChasTmpSnrIndx.setStatus('current')
s5ChasTmpSnrSubIndx = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 7, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 32767))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5ChasTmpSnrSubIndx.setStatus('current')
s5ChasTmpSnrValue = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 7, 1, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5ChasTmpSnrValue.setStatus('deprecated')
s5ChasTmpSnrTmpValue = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 7, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-32768, 32767))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5ChasTmpSnrTmpValue.setStatus('current')
s5ChasUtilTable = MibTable((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 8, 1), )
if mibBuilder.loadTexts: s5ChasUtilTable.setStatus('current')
s5ChasUtilEntry = MibTableRow((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 8, 1, 1), ).setIndexNames((0, "S5-CHASSIS-MIB", "s5ChasUtilGrpIndx"), (0, "S5-CHASSIS-MIB", "s5ChasUtilIndx"), (0, "S5-CHASSIS-MIB", "s5ChasUtilSubIndx"))
if mibBuilder.loadTexts: s5ChasUtilEntry.setStatus('current')
s5ChasUtilGrpIndx = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 8, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32767))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5ChasUtilGrpIndx.setStatus('current')
s5ChasUtilIndx = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 8, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32767))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5ChasUtilIndx.setStatus('current')
s5ChasUtilSubIndx = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 8, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 32767))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5ChasUtilSubIndx.setStatus('current')
s5ChasUtilTotalCPUUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 8, 1, 1, 4), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5ChasUtilTotalCPUUsage.setStatus('current')
s5ChasUtilCPUUsageLast1Minute = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 8, 1, 1, 5), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5ChasUtilCPUUsageLast1Minute.setStatus('current')
s5ChasUtilCPUUsageLast10Minutes = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 8, 1, 1, 6), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5ChasUtilCPUUsageLast10Minutes.setStatus('current')
s5ChasUtilCPUUsageLast1Hour = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 8, 1, 1, 7), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5ChasUtilCPUUsageLast1Hour.setStatus('current')
s5ChasUtilCPUUsageLast24Hours = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 8, 1, 1, 8), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5ChasUtilCPUUsageLast24Hours.setStatus('current')
s5ChasUtilMemoryAvailable = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 8, 1, 1, 9), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5ChasUtilMemoryAvailable.setStatus('current')
s5ChasUtilMemoryMinAvailable = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 8, 1, 1, 10), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5ChasUtilMemoryMinAvailable.setStatus('current')
s5ChasUtilCPUUsageLast10Seconds = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 8, 1, 1, 11), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5ChasUtilCPUUsageLast10Seconds.setStatus('current')
s5ChasUtilMemoryTotalMB = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 8, 1, 1, 12), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 1024))).setUnits('MegaBytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: s5ChasUtilMemoryTotalMB.setStatus('current')
s5ChasUtilMemoryAvailableMB = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 8, 1, 1, 13), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 1024))).setUnits('MegaBytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: s5ChasUtilMemoryAvailableMB.setStatus('current')
s5ChasPsRpsuTable = MibTable((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 9, 1), )
if mibBuilder.loadTexts: s5ChasPsRpsuTable.setStatus('current')
s5ChasPsRpsuEntry = MibTableRow((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 9, 1, 1), ).setIndexNames((0, "S5-CHASSIS-MIB", "s5ChasPsRpsuGrpIndx"), (0, "S5-CHASSIS-MIB", "s5ChasPsRpsuIndx"), (0, "S5-CHASSIS-MIB", "s5ChasPsRpsuSubIndx"))
if mibBuilder.loadTexts: s5ChasPsRpsuEntry.setStatus('current')
s5ChasPsRpsuGrpIndx = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 9, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32767))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5ChasPsRpsuGrpIndx.setStatus('current')
s5ChasPsRpsuIndx = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 9, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32767))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5ChasPsRpsuIndx.setStatus('current')
s5ChasPsRpsuSubIndx = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 9, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 32767))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5ChasPsRpsuSubIndx.setStatus('current')
s5ChasPsRpsuType = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 9, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("bayStack10", 1), ("nes", 2), ("bayStack15", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: s5ChasPsRpsuType.setStatus('current')
s5ChasPsRpsuSourceConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 9, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ups", 1), ("rpsu", 2), ("powerSharing", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: s5ChasPsRpsuSourceConfig.setStatus('current')
s5ChasNotifyFanDirection = MibScalar((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 11, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("left", 1), ("right", 2)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: s5ChasNotifyFanDirection.setStatus('current')
s5ChasGbicInfoTable = MibTable((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 12, 1), )
if mibBuilder.loadTexts: s5ChasGbicInfoTable.setStatus('current')
s5ChasGbicInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 12, 1, 1), ).setIndexNames((0, "S5-CHASSIS-MIB", "s5ChasGbicInfoIfIndex"))
if mibBuilder.loadTexts: s5ChasGbicInfoEntry.setStatus('current')
s5ChasGbicInfoIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 12, 1, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5ChasGbicInfoIfIndex.setStatus('current')
s5ChasGbicInfoGbicType = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 12, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5ChasGbicInfoGbicType.setStatus('current')
s5ChasGbicInfoWavelength = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 12, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5ChasGbicInfoWavelength.setStatus('current')
s5ChasGbicInfoVendorName = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 12, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5ChasGbicInfoVendorName.setStatus('current')
s5ChasGbicInfoVendorOui = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 12, 1, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(3, 3)).setFixedLength(3)).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5ChasGbicInfoVendorOui.setStatus('current')
s5ChasGbicInfoVendorPartNo = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 12, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5ChasGbicInfoVendorPartNo.setStatus('current')
s5ChasGbicInfoVendorRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 12, 1, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5ChasGbicInfoVendorRevision.setStatus('current')
s5ChasGbicInfoVendorSerial = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 12, 1, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5ChasGbicInfoVendorSerial.setStatus('current')
s5ChasGbicInfoHwOptions = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 12, 1, 1, 9), Bits().clone(namedValues=NamedValues(("rxLoss", 0), ("txFault", 1), ("txDisable", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5ChasGbicInfoHwOptions.setStatus('current')
s5ChasGbicInfoDateCode = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 12, 1, 1, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5ChasGbicInfoDateCode.setStatus('current')
s5ChasGbicInfoCleiCode = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 12, 1, 1, 11), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5ChasGbicInfoCleiCode.setStatus('current')
s5ChasGbicInfoProductCode = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 6, 3, 12, 1, 1, 12), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: s5ChasGbicInfoProductCode.setStatus('current')
mibBuilder.exportSymbols("S5-CHASSIS-MIB", s5ChasStoreUsedSize=s5ChasStoreUsedSize, s5ChasStoreTable=s5ChasStoreTable, s5ChasGrpPhysLstChng=s5ChasGrpPhysLstChng, s5ChasComIpMgmtTimeout=s5ChasComIpMgmtTimeout, s5ChasUtilMemoryMinAvailable=s5ChasUtilMemoryMinAvailable, s5ChasGbicInfoVendorPartNo=s5ChasGbicInfoVendorPartNo, s5ChasAttDfltAtt=s5ChasAttDfltAtt, s5ChasPsRpsuEntry=s5ChasPsRpsuEntry, s5ChasStoreType=s5ChasStoreType, s5ChasStoreEntry=s5ChasStoreEntry, s5ChasAttLstChng=s5ChasAttLstChng, s5ChasStoreCurSize=s5ChasStoreCurSize, s5ChasSmDateCode=s5ChasSmDateCode, s5ChasUtilCPUUsageLast24Hours=s5ChasUtilCPUUsageLast24Hours, s5ChasTmpSnrTable=s5ChasTmpSnrTable, s5ChasType=s5ChasType, s5ChasAttEntry=s5ChasAttEntry, s5ChasUtilCPUUsageLast1Hour=s5ChasUtilCPUUsageLast1Hour, s5ChasLocChanIndx=s5ChasLocChanIndx, s5ChasUtilTable=s5ChasUtilTable, s5ChasComNumSubs=s5ChasComNumSubs, s5ChasTmpSnrValue=s5ChasTmpSnrValue, s5ChasComIpMgmtNetMask=s5ChasComIpMgmtNetMask, s5ChasNotifyFanDirection=s5ChasNotifyFanDirection, s5ChasGen=s5ChasGen, s5ChasComDescr=s5ChasComDescr, s5ChasUtilEntry=s5ChasUtilEntry, s5ChasUtilCPUUsageLast10Minutes=s5ChasUtilCPUUsageLast10Minutes, s5ChasNotify=s5ChasNotify, s5ChasLocChanBkplMode=s5ChasLocChanBkplMode, s5ChasBrdDateCode=s5ChasBrdDateCode, s5ChasAttTable=s5ChasAttTable, s5ChasComLocation=s5ChasComLocation, s5ChasGrpTable=s5ChasGrpTable, s5ChasComTable=s5ChasComTable, s5ChasComIpAddress=s5ChasComIpAddress, s5ChasBrdAttLstChng=s5ChasBrdAttLstChng, s5ChasBrdNumAtt=s5ChasBrdNumAtt, s5ChasUtilTotalCPUUsage=s5ChasUtilTotalCPUUsage, s5ChasLocChanEntry=s5ChasLocChanEntry, s5ChasPsRpsuIndx=s5ChasPsRpsuIndx, s5ChasGrp=s5ChasGrp, s5ChasComEntry=s5ChasComEntry, s5ChasUtilIndx=s5ChasUtilIndx, s5ChasGblConfLstChng=s5ChasGblConfLstChng, s5ChasGrpEntry=s5ChasGrpEntry, s5ChasGbicInfoWavelength=s5ChasGbicInfoWavelength, s5ChasContact=s5ChasContact, s5ChasGrpIndx=s5ChasGrpIndx, s5ChasPsRpsuSourceConfig=s5ChasPsRpsuSourceConfig, s5ChasSerNum=s5ChasSerNum, s5ChasBrdIndx=s5ChasBrdIndx, s5ChasGblPhysLstChng=s5ChasGblPhysLstChng, s5ChasUtilCPUUsageLast1Minute=s5ChasUtilCPUUsageLast1Minute, s5ChasUtilMemoryTotalMB=s5ChasUtilMemoryTotalMB, s5ChasPsRpsuGrpIndx=s5ChasPsRpsuGrpIndx, s5ChasComType=s5ChasComType, s5ChasComIpMgmtLimit=s5ChasComIpMgmtLimit, s5ChasGbicInfoEntry=s5ChasGbicInfoEntry, s5ChasUtilSubIndx=s5ChasUtilSubIndx, s5ChasBrdTable=s5ChasBrdTable, s5ChasPsRpsuType=s5ChasPsRpsuType, s5ChasAttBrdIndx=s5ChasAttBrdIndx, s5ChasAttCurAtt=s5ChasAttCurAtt, s5ChasStoreComIndx=s5ChasStoreComIndx, s5ChasTmpSnrSubIndx=s5ChasTmpSnrSubIndx, s5ChasComSerNum=s5ChasComSerNum, s5ChasBrdAttChngs=s5ChasBrdAttChngs, s5ChasGrpDescr=s5ChasGrpDescr, s5ChasGbicInfoVendorName=s5ChasGbicInfoVendorName, s5ChasStoreSubIndx=s5ChasStoreSubIndx, PYSNMP_MODULE_ID=s5ChasMib, s5ChasComGrpIndx=s5ChasComGrpIndx, s5ChasUtilGrpIndx=s5ChasUtilGrpIndx, s5ChasComMaxSubs=s5ChasComMaxSubs, s5ChasDescr=s5ChasDescr, s5ChasComLstChng=s5ChasComLstChng, s5ChasBrdEntry=s5ChasBrdEntry, s5ChasUtil=s5ChasUtil, s5ChasBrdCfgChngs=s5ChasBrdCfgChngs, s5ChasComTotalNumPorts=s5ChasComTotalNumPorts, s5ChasStoreFilename=s5ChasStoreFilename, s5ChasStoreIndx=s5ChasStoreIndx, s5ChasBrdStatusDsply=s5ChasBrdStatusDsply, s5ChasComBaseNumPorts=s5ChasComBaseNumPorts, s5ChasGbicInfoVendorOui=s5ChasGbicInfoVendorOui, s5ChasUtilMemoryAvailable=s5ChasUtilMemoryAvailable, s5ChasAttClusterConnCapability=s5ChasAttClusterConnCapability, s5ChasCom=s5ChasCom, s5ChasGbicInfoDateCode=s5ChasGbicInfoDateCode, s5ChasVer=s5ChasVer, s5ChasGbicInfoIfIndex=s5ChasGbicInfoIfIndex, s5ChasLocChanBrdIndx=s5ChasLocChanBrdIndx, s5ChasComIpMgmtGateway=s5ChasComIpMgmtGateway, s5ChasComSubIndx=s5ChasComSubIndx, s5ChasGbicInfoTable=s5ChasGbicInfoTable, s5ChasComRelPos=s5ChasComRelPos, s5ChasComUpTime=s5ChasComUpTime, s5ChasTmpSnr=s5ChasTmpSnr, s5ChasComOperState=s5ChasComOperState, s5ChasGbicInfoGbicType=s5ChasGbicInfoGbicType, s5ChasLocation=s5ChasLocation, s5ChasComRunningSoftwareVer=s5ChasComRunningSoftwareVer, s5ChasStoreGrpIndx=s5ChasStoreGrpIndx, s5ChasPluggables=s5ChasPluggables, s5ChasComIpv6MgmtNetMask=s5ChasComIpv6MgmtNetMask, s5ChasStoreAge=s5ChasStoreAge, s5ChasGbicInfoVendorSerial=s5ChasGbicInfoVendorSerial, s5ChasBrdFanLeds=s5ChasBrdFanLeds, s5ChasComIpMgmtAddress=s5ChasComIpMgmtAddress, s5ChasPsRpsuSubIndx=s5ChasPsRpsuSubIndx, s5ChasComIndx=s5ChasComIndx, s5ChasGrpType=s5ChasGrpType, s5ChasComIpv6Address=s5ChasComIpv6Address, s5ChasGblPhysChngs=s5ChasGblPhysChngs, s5ChasComIpv6MgmtAddress=s5ChasComIpv6MgmtAddress, s5ChasPsRpsuTable=s5ChasPsRpsuTable, s5ChasGrpNumEnts=s5ChasGrpNumEnts, s5ChasUtilMemoryAvailableMB=s5ChasUtilMemoryAvailableMB, s5ChasGbicInfoCleiCode=s5ChasGbicInfoCleiCode, s5ChasBrd=s5ChasBrd, s5ChasComIpMgmtShutdown=s5ChasComIpMgmtShutdown, s5ChasTmpSnrIndx=s5ChasTmpSnrIndx, s5ChasBrdCfgSrc=s5ChasBrdCfgSrc, s5ChasMib=s5ChasMib, s5ChasTmpSnrTmpValue=s5ChasTmpSnrTmpValue, s5ChasComAdminState=s5ChasComAdminState, s5ChasStoreCntntVer=s5ChasStoreCntntVer, s5ChasGblConfChngs=s5ChasGblConfChngs, s5ChasUtilCPUUsageLast10Seconds=s5ChasUtilCPUUsageLast10Seconds, s5ChasPs=s5ChasPs, s5ChasBrdLeds=s5ChasBrdLeds, s5ChasGblAttChngs=s5ChasGblAttChngs, s5ChasAttChngs=s5ChasAttChngs, s5ChasStoreDescription=s5ChasStoreDescription, s5ChasAttIndx=s5ChasAttIndx, s5ChasGbicInfoVendorRevision=s5ChasGbicInfoVendorRevision, s5ChasGbicInfoHwOptions=s5ChasGbicInfoHwOptions, s5ChasStore=s5ChasStore, s5ChasGrpMaxEnts=s5ChasGrpMaxEnts, s5ChasComVer=s5ChasComVer, s5ChasComIpv6NetMask=s5ChasComIpv6NetMask, s5ChasTmpSnrGrpIndx=s5ChasTmpSnrGrpIndx, s5ChasTmpSnrEntry=s5ChasTmpSnrEntry, s5ChasGblAttLstChng=s5ChasGblAttLstChng, s5ChasGbicInfoProductCode=s5ChasGbicInfoProductCode, s5ChasGrpPhysChngs=s5ChasGrpPhysChngs, s5ChasGrpEncodeFactor=s5ChasGrpEncodeFactor, s5ChasSm=s5ChasSm, s5ChasLocChanTable=s5ChasLocChanTable, s5ChasComGroupMap=s5ChasComGroupMap, s5ChasSmLeds=s5ChasSmLeds)
