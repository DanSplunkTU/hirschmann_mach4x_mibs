#
# PySNMP MIB module CTRON-COMMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-COMMON-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 18:01:45 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
dl, ups, subSysMMAC, commonRev1, subSysDevice = mibBuilder.importSymbols("IRM-OIDS", "dl", "ups", "subSysMMAC", "commonRev1", "subSysDevice")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, Gauge32, ModuleIdentity, MibIdentifier, TimeTicks, Unsigned32, Integer32, Bits, Counter32, Counter64, NotificationType, IpAddress, iso, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Gauge32", "ModuleIdentity", "MibIdentifier", "TimeTicks", "Unsigned32", "Integer32", "Bits", "Counter32", "Counter64", "NotificationType", "IpAddress", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
PhysAddress, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "PhysAddress", "DisplayString", "TextualConvention")
fnb2 = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 6, 1, 2))
chassis = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 6, 1, 3))
environment = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 6, 1, 4))
fnbTR = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 6, 1, 2, 1))
fnbCSMACD = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 6, 1, 2, 2))
fnbPortConnect = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 6, 1, 2, 3))
nB55 = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 6, 2, 3))
mRXI = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 6, 2, 6))
iRM3 = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 6, 2, 7))
tRMM = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 6, 2, 8))
eMME = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 6, 2, 9))
fPRedundancy = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 6, 2, 10))
upsVersion = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 6, 3, 1))
upsRevision = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 6, 3, 1, 1))
deviceType = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 176, 177, 178, 179, 180, 185, 187, 190, 65569, 65570, 65571, 65572))).clone(namedValues=NamedValues(("other", 1), ("iRM2", 176), ("iRBM", 177), ("iRM3", 178), ("tRMBM-R", 179), ("tRMBM-S", 180), ("emm-E", 185), ("tRMM", 187), ("trmMim", 190), ("mrxi24", 65569), ("mrxi22", 65570), ("mrxi34", 65571), ("mrxi38", 65572)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceType.setStatus('mandatory')
deviceName = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 1, 1, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: deviceName.setStatus('mandatory')
deviceIPAddress = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 1, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: deviceIPAddress.setStatus('mandatory')
deviceTime = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: deviceTime.setStatus('mandatory')
deviceDate = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: deviceDate.setStatus('mandatory')
fnbTRTable = MibTable((1, 3, 6, 1, 4, 1, 52, 1, 6, 1, 2, 1, 1), )
if mibBuilder.loadTexts: fnbTRTable.setStatus('mandatory')
fnbTREntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 1, 6, 1, 2, 1, 1, 1), ).setIndexNames((0, "CTRON-COMMON-MIB", "fnbTRIndex"))
if mibBuilder.loadTexts: fnbTREntry.setStatus('mandatory')
fnbTRIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1, 6, 1, 2, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fnbTRIndex.setStatus('mandatory')
fnbConnectLeft = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1, 6, 1, 2, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("detached", 1), ("attached", 2), ("faulted", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fnbConnectLeft.setStatus('mandatory')
fnbConnectRight = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1, 6, 1, 2, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("detached", 1), ("attached", 2), ("faulted", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fnbConnectRight.setStatus('mandatory')
fnbBypass = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1, 6, 1, 2, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("off", 1), ("on", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fnbBypass.setStatus('mandatory')
fnbRPBypass = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1, 6, 1, 2, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fnbRPBypass.setStatus('mandatory')
fnbCSMACDTable = MibTable((1, 3, 6, 1, 4, 1, 52, 1, 6, 1, 2, 2, 1), )
if mibBuilder.loadTexts: fnbCSMACDTable.setStatus('mandatory')
fnbCSMACDEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 1, 6, 1, 2, 2, 1, 1), ).setIndexNames((0, "CTRON-COMMON-MIB", "fnbCSMACDIndex"))
if mibBuilder.loadTexts: fnbCSMACDEntry.setStatus('mandatory')
fnbCSMACDIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1, 6, 1, 2, 2, 1, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fnbCSMACDIndex.setStatus('mandatory')
fnbConnect = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1, 6, 1, 2, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("connectB", 1), ("connectC", 2), ("disconnect", 3), ("connectA", 4), ("subnetB", 5), ("subnetC", 6), ("multiChannel", 7), ("frontPanel", 8)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fnbConnect.setStatus('mandatory')
fnbPortChanges = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1, 6, 1, 2, 2, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fnbPortChanges.setStatus('mandatory')
fnbPortConnectTable = MibTable((1, 3, 6, 1, 4, 1, 52, 1, 6, 1, 2, 3, 1), )
if mibBuilder.loadTexts: fnbPortConnectTable.setStatus('mandatory')
fnbPortConnectEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 1, 6, 1, 2, 3, 1, 1), ).setIndexNames((0, "CTRON-COMMON-MIB", "fnbPortConnectBoardIndex"), (0, "CTRON-COMMON-MIB", "fnbPortConnectPortIndex"))
if mibBuilder.loadTexts: fnbPortConnectEntry.setStatus('mandatory')
fnbPortConnectBoardIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1, 6, 1, 2, 3, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fnbPortConnectBoardIndex.setStatus('mandatory')
fnbPortConnectPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1, 6, 1, 2, 3, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fnbPortConnectPortIndex.setStatus('mandatory')
fnbPortConnectPortAssignment = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1, 6, 1, 2, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("connectA", 1), ("connectB", 2), ("connectC", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fnbPortConnectPortAssignment.setStatus('mandatory')
fnbPortConnectCompID = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1, 6, 1, 2, 3, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fnbPortConnectCompID.setStatus('mandatory')
fnbPortConnectionChanges = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 1, 2, 3, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fnbPortConnectionChanges.setStatus('mandatory')
chassisHWRev = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 1, 3, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisHWRev.setStatus('mandatory')
chassisType = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 1, 3, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14))).clone(namedValues=NamedValues(("other", 1), ("mMAC8FNB", 2), ("mMAC5FNB", 3), ("mMAC3FNB", 4), ("mINIMMAC", 5), ("mRXI", 6), ("m3FNB", 7), ("m5FNB", 8), ("m8FNB", 9), ("nonFNB", 10), ("mMAC3FNBS", 11), ("mMAC5FNBS", 12), ("mMAC8FNBS", 13), ("m8FNBS", 14)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisType.setStatus('mandatory')
chassisSlots = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 1, 3, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisSlots.setStatus('mandatory')
chassisFNB = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 1, 3, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("absent", 1), ("present", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisFNB.setStatus('mandatory')
chassisAlarmEna = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 1, 3, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: chassisAlarmEna.setStatus('mandatory')
chassisAlarmState = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 1, 3, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("chassisNoFaultCondition", 1), ("chassisFaultCondition", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: chassisAlarmState.setStatus('mandatory')
powerTable = MibTable((1, 3, 6, 1, 4, 1, 52, 1, 6, 1, 4, 1), )
if mibBuilder.loadTexts: powerTable.setStatus('mandatory')
powerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 1, 6, 1, 4, 1, 1), ).setIndexNames((0, "CTRON-COMMON-MIB", "powerSupplyNum"))
if mibBuilder.loadTexts: powerEntry.setStatus('mandatory')
powerSupplyNum = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1, 6, 1, 4, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: powerSupplyNum.setStatus('mandatory')
powerSupplyState = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1, 6, 1, 4, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("infoNotAvailable", 1), ("notInstalled", 2), ("installedAndOperating", 3), ("installedAndNotOperating", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: powerSupplyState.setStatus('mandatory')
powerSupplyId = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1, 6, 1, 4, 1, 1, 3), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: powerSupplyId.setStatus('mandatory')
powerSupplyRedun = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1, 6, 1, 4, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("redundancyAvail", 1), ("redundancyNotAvail", 2), ("infoNotAvailable", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: powerSupplyRedun.setStatus('mandatory')
powerSupplyRemoteDisable = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1, 6, 1, 4, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2), ("infoNotAvailable", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: powerSupplyRemoteDisable.setStatus('mandatory')
nB55HWAddress = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 2, 3, 1), PhysAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nB55HWAddress.setStatus('mandatory')
nB55HWRev = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 2, 3, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nB55HWRev.setStatus('mandatory')
nB55FWRev = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 2, 3, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: nB55FWRev.setStatus('mandatory')
mRXIHWAddress = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 2, 6, 1), PhysAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mRXIHWAddress.setStatus('mandatory')
mRXIHWRev = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 2, 6, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mRXIHWRev.setStatus('mandatory')
mRXIFWRev = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 2, 6, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: mRXIFWRev.setStatus('mandatory')
iRM3HWAddress = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 2, 7, 1), PhysAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iRM3HWAddress.setStatus('mandatory')
iRM3HWRev = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 2, 7, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iRM3HWRev.setStatus('mandatory')
iRM3FWRev = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 2, 7, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: iRM3FWRev.setStatus('mandatory')
iRM3PortAssoc = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 2, 7, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(5, 6))).clone(namedValues=NamedValues(("aoffFrp", 5), ("arpFoff", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: iRM3PortAssoc.setStatus('mandatory')
iRM3BPSupport = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 2, 7, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("notSupported", 1), ("supported", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: iRM3BPSupport.setStatus('mandatory')
tRMMHWAddress = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 2, 8, 1), PhysAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tRMMHWAddress.setStatus('mandatory')
tRMMHWRev = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 2, 8, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tRMMHWRev.setStatus('mandatory')
tRMMFWRev = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 2, 8, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: tRMMFWRev.setStatus('mandatory')
eMMEHWAddress = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 2, 9, 1), PhysAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eMMEHWAddress.setStatus('mandatory')
eMMEHWRev = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 2, 9, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eMMEHWRev.setStatus('mandatory')
eMMEFWRev = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 2, 9, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 10))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eMMEFWRev.setStatus('mandatory')
eMMEBoardMap = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 2, 9, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eMMEBoardMap.setStatus('mandatory')
fPRedund = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 6, 2, 10, 1))
fPRedundReset = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 2, 10, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noReset", 1), ("reset", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fPRedundReset.setStatus('mandatory')
fPRedundPollInterval = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 2, 10, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fPRedundPollInterval.setStatus('mandatory')
fPRedundRetrys = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 2, 10, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fPRedundRetrys.setStatus('mandatory')
fPRedundNumAddr = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 2, 10, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fPRedundNumAddr.setStatus('mandatory')
fPRedundAddAddr = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 2, 10, 1, 5), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fPRedundAddAddr.setStatus('mandatory')
fPRedundDelAddr = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 2, 10, 1, 6), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fPRedundDelAddr.setStatus('mandatory')
fPRedundActivePort = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 2, 10, 1, 7), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fPRedundActivePort.setStatus('mandatory')
fPRedundEnable = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 2, 10, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fPRedundEnable.setStatus('mandatory')
fPRedundAddrTable = MibTable((1, 3, 6, 1, 4, 1, 52, 1, 6, 2, 10, 2), )
if mibBuilder.loadTexts: fPRedundAddrTable.setStatus('mandatory')
fPRedundAddrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 1, 6, 2, 10, 2, 1), ).setIndexNames((0, "CTRON-COMMON-MIB", "fPRedundAddrId"))
if mibBuilder.loadTexts: fPRedundAddrEntry.setStatus('mandatory')
fPRedundAddrId = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1, 6, 2, 10, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fPRedundAddrId.setStatus('mandatory')
fPRedundAddrIPAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1, 6, 2, 10, 2, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fPRedundAddrIPAddr.setStatus('mandatory')
upsID = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 257, 258, 259, 260, 261, 262))).clone(namedValues=NamedValues(("other", 1), ("aPCModel370", 257), ("aPCModel400", 258), ("aPCModel600", 259), ("aPCModel900", 260), ("aPCModel1250", 261), ("aPCModel2000", 262)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: upsID.setStatus('mandatory')
upsUpTime = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 3, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: upsUpTime.setStatus('mandatory')
upsDisable = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 3, 1, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: upsDisable.setStatus('deprecated')
upsDisconnect = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 3, 1, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: upsDisconnect.setStatus('mandatory')
upsTest = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 3, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("unitOK", 1), ("unitFailed", 2), ("badBattery", 3), ("noRecentTest", 4), ("underTest", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: upsTest.setStatus('mandatory')
upsBatteryCapacity = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 3, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: upsBatteryCapacity.setStatus('mandatory')
upsACLineVoltsIn = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 3, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: upsACLineVoltsIn.setStatus('mandatory')
upsBatteryVoltsOut = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 3, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: upsBatteryVoltsOut.setStatus('mandatory')
dlForceOnBoot = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 4, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dlForceOnBoot.setStatus('mandatory')
dlCommitRAMToFlash = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 4, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dlCommitRAMToFlash.setStatus('mandatory')
dlInitiateColdBoot = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 4, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dlInitiateColdBoot.setStatus('mandatory')
dlTFTPRequestHost = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 4, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dlTFTPRequestHost.setStatus('mandatory')
dlTFTPRequest = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 4, 5), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dlTFTPRequest.setStatus('mandatory')
dlLastImageFilename = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 4, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dlLastImageFilename.setStatus('mandatory')
dlLastServerIPAddress = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 4, 7), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dlLastServerIPAddress.setStatus('mandatory')
dlFlashSize = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 4, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dlFlashSize.setStatus('mandatory')
dlFlashCount = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 4, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dlFlashCount.setStatus('mandatory')
dlFirmwareBase = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 4, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dlFirmwareBase.setStatus('mandatory')
dlFirmwareTop = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 4, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dlFirmwareTop.setStatus('mandatory')
dlFirmwareStart = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 4, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dlFirmwareStart.setStatus('mandatory')
dlBootRev = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 4, 13), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 10))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dlBootRev.setStatus('mandatory')
dlForceBootp = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 4, 14), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dlForceBootp.setStatus('mandatory')
dlServerName = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 4, 15), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dlServerName.setStatus('mandatory')
dlOnLineDownLoad = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 4, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("normalOperation", 1), ("forceDownLoad", 2), ("forceDownLoadReset", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dlOnLineDownLoad.setStatus('mandatory')
dlOperStatus = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 4, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("unknown", 2), ("normalOperation", 3), ("downLoadActive", 4), ("downLoadCompleteError", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dlOperStatus.setStatus('mandatory')
dlNetAddress = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 4, 18), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dlNetAddress.setStatus('mandatory')
dlFileName = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 4, 19), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dlFileName.setStatus('mandatory')
dlErrorString = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 4, 20), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dlErrorString.setStatus('mandatory')
dlTftpServerGatewayIPAddress = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 4, 21), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dlTftpServerGatewayIPAddress.setStatus('mandatory')
mibBuilder.exportSymbols("CTRON-COMMON-MIB", nB55HWRev=nB55HWRev, fnbCSMACDIndex=fnbCSMACDIndex, chassisFNB=chassisFNB, fPRedundEnable=fPRedundEnable, fnbConnectLeft=fnbConnectLeft, tRMMHWRev=tRMMHWRev, upsTest=upsTest, fPRedund=fPRedund, mRXIHWAddress=mRXIHWAddress, chassisSlots=chassisSlots, powerSupplyId=powerSupplyId, fnbTR=fnbTR, fnbCSMACDTable=fnbCSMACDTable, upsDisable=upsDisable, fnbCSMACD=fnbCSMACD, eMMEBoardMap=eMMEBoardMap, dlFlashSize=dlFlashSize, dlCommitRAMToFlash=dlCommitRAMToFlash, chassisType=chassisType, nB55=nB55, powerSupplyRedun=powerSupplyRedun, iRM3HWAddress=iRM3HWAddress, fnb2=fnb2, fnbBypass=fnbBypass, fPRedundNumAddr=fPRedundNumAddr, iRM3FWRev=iRM3FWRev, fPRedundDelAddr=fPRedundDelAddr, dlTftpServerGatewayIPAddress=dlTftpServerGatewayIPAddress, fnbPortConnectBoardIndex=fnbPortConnectBoardIndex, deviceName=deviceName, fPRedundAddAddr=fPRedundAddAddr, powerSupplyNum=powerSupplyNum, fnbPortConnectTable=fnbPortConnectTable, tRMMHWAddress=tRMMHWAddress, upsBatteryVoltsOut=upsBatteryVoltsOut, deviceDate=deviceDate, fnbPortChanges=fnbPortChanges, dlTFTPRequest=dlTFTPRequest, tRMM=tRMM, eMMEHWRev=eMMEHWRev, upsRevision=upsRevision, deviceTime=deviceTime, iRM3HWRev=iRM3HWRev, dlFirmwareBase=dlFirmwareBase, deviceIPAddress=deviceIPAddress, fnbPortConnect=fnbPortConnect, chassisAlarmState=chassisAlarmState, upsVersion=upsVersion, nB55FWRev=nB55FWRev, fnbConnectRight=fnbConnectRight, fPRedundActivePort=fPRedundActivePort, fnbRPBypass=fnbRPBypass, dlBootRev=dlBootRev, chassisHWRev=chassisHWRev, dlForceOnBoot=dlForceOnBoot, environment=environment, dlTFTPRequestHost=dlTFTPRequestHost, upsUpTime=upsUpTime, upsDisconnect=upsDisconnect, powerSupplyState=powerSupplyState, powerSupplyRemoteDisable=powerSupplyRemoteDisable, fnbPortConnectCompID=fnbPortConnectCompID, upsID=upsID, fnbTREntry=fnbTREntry, fnbConnect=fnbConnect, eMMEFWRev=eMMEFWRev, dlOnLineDownLoad=dlOnLineDownLoad, powerEntry=powerEntry, fPRedundAddrTable=fPRedundAddrTable, eMMEHWAddress=eMMEHWAddress, dlServerName=dlServerName, dlInitiateColdBoot=dlInitiateColdBoot, dlFirmwareTop=dlFirmwareTop, dlErrorString=dlErrorString, mRXIFWRev=mRXIFWRev, fPRedundReset=fPRedundReset, dlLastImageFilename=dlLastImageFilename, tRMMFWRev=tRMMFWRev, nB55HWAddress=nB55HWAddress, chassis=chassis, upsACLineVoltsIn=upsACLineVoltsIn, fPRedundAddrId=fPRedundAddrId, fnbPortConnectionChanges=fnbPortConnectionChanges, mRXI=mRXI, fnbPortConnectEntry=fnbPortConnectEntry, iRM3BPSupport=iRM3BPSupport, dlNetAddress=dlNetAddress, dlFileName=dlFileName, fnbPortConnectPortAssignment=fnbPortConnectPortAssignment, dlLastServerIPAddress=dlLastServerIPAddress, dlOperStatus=dlOperStatus, fnbCSMACDEntry=fnbCSMACDEntry, deviceType=deviceType, mRXIHWRev=mRXIHWRev, chassisAlarmEna=chassisAlarmEna, dlForceBootp=dlForceBootp, fPRedundancy=fPRedundancy, upsBatteryCapacity=upsBatteryCapacity, fPRedundAddrIPAddr=fPRedundAddrIPAddr, iRM3=iRM3, fnbPortConnectPortIndex=fnbPortConnectPortIndex, iRM3PortAssoc=iRM3PortAssoc, dlFlashCount=dlFlashCount, dlFirmwareStart=dlFirmwareStart, fPRedundPollInterval=fPRedundPollInterval, fPRedundRetrys=fPRedundRetrys, fnbTRTable=fnbTRTable, powerTable=powerTable, fPRedundAddrEntry=fPRedundAddrEntry, eMME=eMME, fnbTRIndex=fnbTRIndex)
