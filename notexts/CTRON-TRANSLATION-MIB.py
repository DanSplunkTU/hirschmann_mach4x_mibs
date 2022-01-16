#
# PySNMP MIB module CTRON-TRANSLATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-TRANSLATION-MIB
# Produced by pysmi-1.1.8 at Sun Jan 16 00:36:31 2022
# On host fv-az42-839 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
MacAddress, = mibBuilder.importSymbols("BRIDGE-MIB", "MacAddress")
ctTranslation, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctTranslation")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, ObjectIdentity, MibIdentifier, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, IpAddress, Bits, Counter64, ModuleIdentity, NotificationType, Counter32, Gauge32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "ObjectIdentity", "MibIdentifier", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "IpAddress", "Bits", "Counter64", "ModuleIdentity", "NotificationType", "Counter32", "Gauge32", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ctTransFddiAtm = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 1))
ctTransFddiEthernet = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 2))
ctTransEthernetFddi = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 3))
ctTransRifDb = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 4))
ctTransBcastX = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 5))
ctTransIbmLlc = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 6))
ctTransSr = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 7))
ctTransNovellCfg = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 8))
ctTransIPCfg = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 9))
ctTransA2Cfg = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 10))
ctTransOtherCfg = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 11))
ctTranslfpsCfg = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 12))
ctTransFddiAtmMtu = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("greater1518MTU", 1), ("less1518MTU", 2))).clone('greater1518MTU')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTransFddiAtmMtu.setStatus('mandatory')
ctTransFddiAtmIPFrag = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTransFddiAtmIPFrag.setStatus('mandatory')
ctTransFddiEthernetIPFrag = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTransFddiEthernetIPFrag.setStatus('mandatory')
ctTransFddiSnapEthernetType = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ethernetII", 1), ("ethernetSnap", 2))).clone('ethernetII')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTransFddiSnapEthernetType.setStatus('mandatory')
ctTransFddiEthernetAuto = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 2, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ("notSupported", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTransFddiEthernetAuto.setStatus('mandatory')
ctTransFddiEthernetSnapIPX = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 2, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("ethernetII", 1), ("ethernetSnap", 2), ("ethernet802dot3", 3), ("ethernet802dot3Raw", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTransFddiEthernetSnapIPX.setStatus('mandatory')
ctTransFddiEthernet802dot2IPX = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 2, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("ethernetII", 1), ("ethernetSnap", 2), ("ethernet802dot3", 3), ("ethernet802dot3Raw", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTransFddiEthernet802dot2IPX.setStatus('mandatory')
ctTransFddiEthernetMACIPX = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 2, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("ethernetII", 1), ("ethernetSnap", 2), ("ethernet802dot3", 3), ("ethernet802dot3Raw", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTransFddiEthernetMACIPX.setStatus('mandatory')
ctTransEthernetFddiRAW = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("fDDI802dot2", 1), ("fDDISnap", 2), ("fDDIMAC", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTransEthernetFddiRAW.setStatus('mandatory')
ctTransEthernetFddiPadVerify = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 3, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ("not-supported", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTransEthernetFddiPadVerify.setStatus('mandatory')
ctTransRifDbTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 4, 1), )
if mibBuilder.loadTexts: ctTransRifDbTable.setStatus('mandatory')
ctTransRifDbEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 4, 1, 1), ).setIndexNames((0, "CTRON-TRANSLATION-MIB", "ctTransRifDbMacAddr"))
if mibBuilder.loadTexts: ctTransRifDbEntry.setStatus('mandatory')
ctTransRifDbMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 4, 1, 1, 1), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctTransRifDbMacAddr.setStatus('mandatory')
ctTransRifDbSrcPort = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 4, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctTransRifDbSrcPort.setStatus('mandatory')
ctTransRifDbLength = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 4, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctTransRifDbLength.setStatus('mandatory')
ctTransRifDbRIF = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 4, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctTransRifDbRIF.setStatus('mandatory')
ctTransRifDbCtrlTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 4, 2), )
if mibBuilder.loadTexts: ctTransRifDbCtrlTable.setStatus('mandatory')
ctTransRifDbCtrlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 4, 2, 1), ).setIndexNames((0, "CTRON-TRANSLATION-MIB", "ctTransRifDbCtrlPort"))
if mibBuilder.loadTexts: ctTransRifDbCtrlEntry.setStatus('mandatory')
ctTransRifDbCtrlPort = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 4, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctTransRifDbCtrlPort.setStatus('mandatory')
ctTransRifDbWeightState = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 4, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("notsupported", 1), ("shortestpath", 2), ("quickestpath", 3), ("largestmtu", 4), ("lastseen", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTransRifDbWeightState.setStatus('mandatory')
ctTransRifDbCtrlType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 4, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("explorer", 1), ("all", 2), ("notsupported", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTransRifDbCtrlType.setStatus('mandatory')
ctTransRifDbAgingTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 4, 2, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTransRifDbAgingTimer.setStatus('mandatory')
ctTransBcastXTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 5, 1), )
if mibBuilder.loadTexts: ctTransBcastXTable.setStatus('mandatory')
ctTransBcastXEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 5, 1, 1), ).setIndexNames((0, "CTRON-TRANSLATION-MIB", "ctTransBcastXPort"))
if mibBuilder.loadTexts: ctTransBcastXEntry.setStatus('mandatory')
ctTransBcastXPort = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 5, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctTransBcastXPort.setStatus('mandatory')
ctTransBcastXMode = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 5, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTransBcastXMode.setStatus('mandatory')
ctTransBcastXMedia = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 5, 1, 1, 3), MacAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTransBcastXMedia.setStatus('mandatory')
ctTransBcastXCanonical = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 5, 1, 1, 4), MacAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTransBcastXCanonical.setStatus('mandatory')
ctTransIbmLlcTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 6, 1), )
if mibBuilder.loadTexts: ctTransIbmLlcTable.setStatus('mandatory')
ctTransIbmLlcEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 6, 1, 1), ).setIndexNames((0, "CTRON-TRANSLATION-MIB", "ctTransIbmLlcPort"))
if mibBuilder.loadTexts: ctTransIbmLlcEntry.setStatus('mandatory')
ctTransIbmLlcPort = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 6, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctTransIbmLlcPort.setStatus('mandatory')
ctTransIbmLlcNullMode = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 6, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ("notsupported", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTransIbmLlcNullMode.setStatus('mandatory')
ctTransIbmLlcSnaPathMode = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 6, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ("notsupported", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTransIbmLlcSnaPathMode.setStatus('mandatory')
ctTransIbmLlcSnaMode = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 6, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ("notsupported", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTransIbmLlcSnaMode.setStatus('mandatory')
ctTransIbmLlcNbMode = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 6, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ("notsupported", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTransIbmLlcNbMode.setStatus('mandatory')
ctTransIbmLlcLnmMode = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 6, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ("notsupported", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTransIbmLlcLnmMode.setStatus('mandatory')
ctTransIbmLlcDscMode = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 6, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ("notsupported", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTransIbmLlcDscMode.setStatus('mandatory')
ctTransIbmLlcOtherMode = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 6, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ("notsupported", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTransIbmLlcOtherMode.setStatus('mandatory')
ctTransIbmLlcOtherValue = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 6, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTransIbmLlcOtherValue.setStatus('mandatory')
ctTransSrTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 7, 1), )
if mibBuilder.loadTexts: ctTransSrTable.setStatus('mandatory')
ctTransSrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 7, 1, 1), ).setIndexNames((0, "CTRON-TRANSLATION-MIB", "ctTransSrPort"))
if mibBuilder.loadTexts: ctTransSrEntry.setStatus('mandatory')
ctTransSrPort = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 7, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctTransSrPort.setStatus('mandatory')
ctTransSrIfMode = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 7, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("tp", 1), ("sr", 2), ("srt", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTransSrIfMode.setStatus('mandatory')
ctTransSrExpMode = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 7, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("notsupported", 1), ("are", 2), ("ste", 3), ("inboundtype", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTransSrExpMode.setStatus('mandatory')
ctTransSrIP = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 7, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("tp", 1), ("sr", 2), ("auto", 3), ("notsupported", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTransSrIP.setStatus('mandatory')
ctTransSrIPX = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 7, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("tp", 1), ("sr", 2), ("auto", 3), ("notsupported", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTransSrIPX.setStatus('mandatory')
ctTransSrNetBIOS = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 7, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("tp", 1), ("sr", 2), ("auto", 3), ("notsupported", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTransSrNetBIOS.setStatus('mandatory')
ctTransSrSNA = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 7, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("tp", 1), ("sr", 2), ("auto", 3), ("notsupported", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTransSrSNA.setStatus('mandatory')
ctTransSrOther = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 7, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("tp", 1), ("sr", 2), ("auto", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTransSrOther.setStatus('mandatory')
ctTransSRLocalSegment = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 7, 1, 1, 9), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTransSRLocalSegment.setStatus('mandatory')
ctTransSrSRLF = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 7, 1, 1, 10), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTransSrSRLF.setStatus('mandatory')
ctTransSRAutoRingNumberDetect = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 7, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notsupported", 1), ("enable", 2), ("disable", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTransSRAutoRingNumberDetect.setStatus('mandatory')
ctTransNovellCfgTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 8, 1), )
if mibBuilder.loadTexts: ctTransNovellCfgTable.setStatus('mandatory')
ctTransNovellCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 8, 1, 1), ).setIndexNames((0, "CTRON-TRANSLATION-MIB", "ctTransNovellCfgPort"))
if mibBuilder.loadTexts: ctTransNovellCfgEntry.setStatus('mandatory')
ctTransNovellCfgPort = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 8, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctTransNovellCfgPort.setStatus('mandatory')
ctTransNovellCfgMode = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 8, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ("enabledType2", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTransNovellCfgMode.setStatus('mandatory')
ctTransNovellGroupMode = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 8, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ("notsupported", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTransNovellGroupMode.setStatus('mandatory')
ctTransIPCfgTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 9, 1), )
if mibBuilder.loadTexts: ctTransIPCfgTable.setStatus('mandatory')
ctTransIPCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 9, 1, 1), ).setIndexNames((0, "CTRON-TRANSLATION-MIB", "ctTransIPCfgPort"))
if mibBuilder.loadTexts: ctTransIPCfgEntry.setStatus('mandatory')
ctTransIPCfgPort = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 9, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctTransIPCfgPort.setStatus('mandatory')
ctTransIPDataCfgMode = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 9, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTransIPDataCfgMode.setStatus('mandatory')
ctTransIPArpCfgMode = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 9, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTransIPArpCfgMode.setStatus('mandatory')
ctTransIPRarpCfgMode = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 9, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTransIPRarpCfgMode.setStatus('mandatory')
ctTransA2CfgTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 10, 1), )
if mibBuilder.loadTexts: ctTransA2CfgTable.setStatus('mandatory')
ctTransA2CfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 10, 1, 1), ).setIndexNames((0, "CTRON-TRANSLATION-MIB", "ctTransA2CfgPort"))
if mibBuilder.loadTexts: ctTransA2CfgEntry.setStatus('mandatory')
ctTransA2CfgPort = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 10, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctTransA2CfgPort.setStatus('mandatory')
ctTransA2DataCfgMode = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 10, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTransA2DataCfgMode.setStatus('mandatory')
ctTransA2ArpCfgMode = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 10, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTransA2ArpCfgMode.setStatus('mandatory')
ctTransA2McastCfgMode = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 10, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTransA2McastCfgMode.setStatus('mandatory')
ctTransOtherTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 11, 1), )
if mibBuilder.loadTexts: ctTransOtherTable.setStatus('mandatory')
ctTransOtherEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 11, 1, 1), ).setIndexNames((0, "CTRON-TRANSLATION-MIB", "ctTransOtherPort"))
if mibBuilder.loadTexts: ctTransOtherEntry.setStatus('mandatory')
ctTransOtherPort = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 11, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctTransOtherPort.setStatus('mandatory')
ctTransOtherUnknownSap = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 11, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTransOtherUnknownSap.setStatus('mandatory')
ctTransOtherUnknownSnap = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 11, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTransOtherUnknownSnap.setStatus('mandatory')
ctTransOtherSapDsap1Mode = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 11, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTransOtherSapDsap1Mode.setStatus('mandatory')
ctTransOtherSapDsap1Val = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 11, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTransOtherSapDsap1Val.setStatus('mandatory')
ctTransOtherSapDsap2Mode = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 11, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTransOtherSapDsap2Mode.setStatus('mandatory')
ctTransOtherSapDsap2Val = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 11, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTransOtherSapDsap2Val.setStatus('mandatory')
ctTransOtherSapDsap3Mode = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 11, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTransOtherSapDsap3Mode.setStatus('mandatory')
ctTransOtherSapDsap3Val = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 11, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTransOtherSapDsap3Val.setStatus('mandatory')
ctTransOtherSnap1Mode = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 11, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTransOtherSnap1Mode.setStatus('mandatory')
ctTransOtherSnap1Val = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 11, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTransOtherSnap1Val.setStatus('mandatory')
ctTransOtherSnap2Mode = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 11, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTransOtherSnap2Mode.setStatus('mandatory')
ctTransOtherSnap2Val = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 11, 1, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTransOtherSnap2Val.setStatus('mandatory')
ctTransLfpsTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 12, 1), )
if mibBuilder.loadTexts: ctTransLfpsTable.setStatus('mandatory')
ctTransLfpsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 12, 1, 1), ).setIndexNames((0, "CTRON-TRANSLATION-MIB", "ctTransLfpsPort"))
if mibBuilder.loadTexts: ctTransLfpsEntry.setStatus('mandatory')
ctTransLfpsPort = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 12, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctTransLfpsPort.setStatus('mandatory')
ctTransLfpsAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 12, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("large", 1), ("fragment-if-possible", 2), ("small", 3), ("auto", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTransLfpsAdminStatus.setStatus('mandatory')
ctTransLfpsOperationalStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 12, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("large", 1), ("fragment-if-possible", 2), ("small", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctTransLfpsOperationalStatus.setStatus('mandatory')
mibBuilder.exportSymbols("CTRON-TRANSLATION-MIB", ctTransIPCfgEntry=ctTransIPCfgEntry, ctTransIbmLlcNbMode=ctTransIbmLlcNbMode, ctTransRifDbCtrlPort=ctTransRifDbCtrlPort, ctTransIPCfg=ctTransIPCfg, ctTransRifDbTable=ctTransRifDbTable, ctTransOtherSapDsap1Mode=ctTransOtherSapDsap1Mode, ctTransIbmLlcPort=ctTransIbmLlcPort, ctTransNovellCfgPort=ctTransNovellCfgPort, ctTransLfpsEntry=ctTransLfpsEntry, ctTransFddiAtmIPFrag=ctTransFddiAtmIPFrag, ctTransLfpsAdminStatus=ctTransLfpsAdminStatus, ctTransSRLocalSegment=ctTransSRLocalSegment, ctTransRifDbAgingTimer=ctTransRifDbAgingTimer, ctTransSrIfMode=ctTransSrIfMode, ctTransOtherSapDsap2Mode=ctTransOtherSapDsap2Mode, ctTransSr=ctTransSr, ctTransRifDbCtrlType=ctTransRifDbCtrlType, ctTransOtherEntry=ctTransOtherEntry, ctTransIbmLlcDscMode=ctTransIbmLlcDscMode, ctTransA2CfgEntry=ctTransA2CfgEntry, ctTransRifDbCtrlEntry=ctTransRifDbCtrlEntry, ctTransFddiEthernetSnapIPX=ctTransFddiEthernetSnapIPX, ctTransLfpsPort=ctTransLfpsPort, ctTransSrSNA=ctTransSrSNA, ctTransBcastXPort=ctTransBcastXPort, ctTransIbmLlcSnaPathMode=ctTransIbmLlcSnaPathMode, ctTransFddiEthernet=ctTransFddiEthernet, ctTransOtherCfg=ctTransOtherCfg, ctTransSrIPX=ctTransSrIPX, ctTransFddiAtmMtu=ctTransFddiAtmMtu, ctTransIbmLlcOtherValue=ctTransIbmLlcOtherValue, ctTransRifDbEntry=ctTransRifDbEntry, ctTransBcastXMode=ctTransBcastXMode, ctTransIPArpCfgMode=ctTransIPArpCfgMode, ctTransIbmLlc=ctTransIbmLlc, ctTransFddiAtm=ctTransFddiAtm, ctTransOtherSapDsap3Mode=ctTransOtherSapDsap3Mode, ctTransOtherPort=ctTransOtherPort, ctTransOtherSnap2Mode=ctTransOtherSnap2Mode, ctTransIbmLlcNullMode=ctTransIbmLlcNullMode, ctTransNovellGroupMode=ctTransNovellGroupMode, ctTransSrPort=ctTransSrPort, ctTransSrNetBIOS=ctTransSrNetBIOS, ctTransIPDataCfgMode=ctTransIPDataCfgMode, ctTransOtherSapDsap1Val=ctTransOtherSapDsap1Val, ctTransFddiEthernet802dot2IPX=ctTransFddiEthernet802dot2IPX, ctTransRifDbLength=ctTransRifDbLength, ctTransA2McastCfgMode=ctTransA2McastCfgMode, ctTransLfpsOperationalStatus=ctTransLfpsOperationalStatus, ctTransIbmLlcSnaMode=ctTransIbmLlcSnaMode, ctTransRifDbRIF=ctTransRifDbRIF, ctTransFddiEthernetMACIPX=ctTransFddiEthernetMACIPX, ctTransIbmLlcLnmMode=ctTransIbmLlcLnmMode, ctTransNovellCfg=ctTransNovellCfg, ctTransOtherSapDsap3Val=ctTransOtherSapDsap3Val, ctTransOtherSnap1Mode=ctTransOtherSnap1Mode, ctTransOtherUnknownSap=ctTransOtherUnknownSap, ctTransA2DataCfgMode=ctTransA2DataCfgMode, ctTransEthernetFddiRAW=ctTransEthernetFddiRAW, ctTransSrIP=ctTransSrIP, ctTransA2Cfg=ctTransA2Cfg, ctTransRifDbWeightState=ctTransRifDbWeightState, ctTransFddiEthernetIPFrag=ctTransFddiEthernetIPFrag, ctTransLfpsTable=ctTransLfpsTable, ctTransNovellCfgMode=ctTransNovellCfgMode, ctTransOtherSnap2Val=ctTransOtherSnap2Val, ctTransIbmLlcEntry=ctTransIbmLlcEntry, ctTransRifDbSrcPort=ctTransRifDbSrcPort, ctTransOtherSapDsap2Val=ctTransOtherSapDsap2Val, ctTransIbmLlcOtherMode=ctTransIbmLlcOtherMode, ctTransIbmLlcTable=ctTransIbmLlcTable, ctTransSrSRLF=ctTransSrSRLF, ctTransNovellCfgEntry=ctTransNovellCfgEntry, ctTransIPRarpCfgMode=ctTransIPRarpCfgMode, ctTransBcastXCanonical=ctTransBcastXCanonical, ctTransBcastX=ctTransBcastX, ctTransBcastXEntry=ctTransBcastXEntry, ctTransA2CfgPort=ctTransA2CfgPort, ctTransSRAutoRingNumberDetect=ctTransSRAutoRingNumberDetect, ctTransRifDbMacAddr=ctTransRifDbMacAddr, ctTranslfpsCfg=ctTranslfpsCfg, ctTransEthernetFddi=ctTransEthernetFddi, ctTransSrEntry=ctTransSrEntry, ctTransEthernetFddiPadVerify=ctTransEthernetFddiPadVerify, ctTransA2CfgTable=ctTransA2CfgTable, ctTransBcastXMedia=ctTransBcastXMedia, ctTransA2ArpCfgMode=ctTransA2ArpCfgMode, ctTransRifDbCtrlTable=ctTransRifDbCtrlTable, ctTransOtherTable=ctTransOtherTable, ctTransSrTable=ctTransSrTable, ctTransRifDb=ctTransRifDb, ctTransIPCfgTable=ctTransIPCfgTable, ctTransOtherUnknownSnap=ctTransOtherUnknownSnap, ctTransFddiSnapEthernetType=ctTransFddiSnapEthernetType, ctTransSrOther=ctTransSrOther, ctTransIPCfgPort=ctTransIPCfgPort, ctTransFddiEthernetAuto=ctTransFddiEthernetAuto, ctTransSrExpMode=ctTransSrExpMode, ctTransNovellCfgTable=ctTransNovellCfgTable, ctTransOtherSnap1Val=ctTransOtherSnap1Val, ctTransBcastXTable=ctTransBcastXTable)
