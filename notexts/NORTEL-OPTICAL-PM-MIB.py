#
# PySNMP MIB module NORTEL-OPTICAL-PM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/nortel/NORTEL-OPTICAL-PM-MIB
# Produced by pysmi-1.1.8 at Sun Jan 16 00:41:34 2022
# On host fv-az42-839 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
nnOpticalGenericMIBs, = mibBuilder.importSymbols("NORTEL-OPTICAL-GENERIC-MIB", "nnOpticalGenericMIBs")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, NotificationType, Counter32, Unsigned32, MibIdentifier, iso, ObjectIdentity, Bits, Gauge32, Integer32, IpAddress, ModuleIdentity, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "NotificationType", "Counter32", "Unsigned32", "MibIdentifier", "iso", "ObjectIdentity", "Bits", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "Counter64")
TextualConvention, DisplayString, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "DateAndTime")
nnOpticalPmMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 562, 68, 10, 1))
nnOpticalPmMIB.setRevisions(('2005-08-16 00:00', '2006-04-12 00:00', '2006-07-12 00:00', '2007-05-21 00:00', '2008-02-07 00:00', '2008-03-25 00:00', '2008-04-02 00:00', '2008-08-27 00:00', '2009-03-18 00:00', '2009-06-15 00:00', '2010-06-18 00:00', '2010-12-31 00:00', '2011-01-18 00:00', '2012-06-26 00:00', '2012-10-18 00:00', '2012-11-06 00:00', '2013-02-26 00:00', '2013-06-23 00:00', '2014-03-14 00:00', '2014-05-14 00:00', '2015-11-24 00:00', '2015-12-03 00:00', '2016-01-05 00:00', '2017-01-31 00:00', '2017-08-16 00:00', '2018-04-05 00:00', '2019-06-11 00:00', '2019-07-05 00:00',))
if mibBuilder.loadTexts: nnOpticalPmMIB.setLastUpdated('201907050000Z')
if mibBuilder.loadTexts: nnOpticalPmMIB.setOrganization('Nortel')
nnOpticalPmObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1))
class NnOpticalPmMonType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255), SingleValueConstraint(256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276))
    namedValues = NamedValues(("cvSectionRxNe", 1), ("esSectionRxNe", 2), ("sesSectionRxNe", 3), ("sefsSectionRxNe", 4), ("cvSectionTxNe", 5), ("esSectionTxNe", 6), ("sesSectionTxNe", 7), ("cvLineRxNe", 8), ("esLineRxNe", 9), ("sesLineRxNe", 10), ("uasLineRxNe", 11), ("fcLineRxNe", 12), ("cvLineTxNe", 13), ("esLineTxNe", 14), ("sesLineTxNe", 15), ("uasLineTxNe", 16), ("fcLineTxNe", 17), ("inframesEthRxNe", 18), ("fcserrEthRxNe", 19), ("frtoolongsEthRxNe", 20), ("frtooshortsEthRxNe", 21), ("outframesEthTxNe", 22), ("fcserrEthTxNe", 23), ("cvPCSRxNe", 24), ("esPCSRxNe", 25), ("sesPCSRxNe", 26), ("uasPCSRxNe", 27), ("cvPCSTxNe", 28), ("esPCSTxNe", 29), ("sesPCSTxNe", 30), ("uasPCSTxNe", 31), ("oprOCHRxNe", 32), ("oprnOCHRxNe", 33), ("optOCHTxNe", 34), ("optnOCHTxNe", 35), ("cvOTURxNe", 36), ("esOTURxNe", 37), ("sesOTURxNe", 38), ("sefsOTURxNe", 39), ("fecOTURxNe", 40), ("hccsOTURxNe", 41), ("pfbereOTURxNe", 42), ("prfberOTURxNe", 43), ("cvODURxNe", 44), ("esODURxNe", 45), ("sesODURxNe", 46), ("uasODURxNe", 47), ("fcODURxNe", 48), ("oprOTSRxNe", 49), ("optOTSTxNe", 50), ("orlOTSNaNe", 51), ("opinOTSNaNe", 52), ("grpopinOTSNaNe", 53), ("grpgainOTSNaNe", 54), ("opoutOTSNaNe", 55), ("grpoptOTSTxNe", 56), ("grpopoutOTSNaNe", 57), ("esEthRxNe", 58), ("sesEthRxNe", 59), ("uasEthRxNe", 60), ("dfrEthRxNe", 61), ("inframeserrEthRxNe", 62), ("inframesdiscdsEthRxNe", 63), ("esEthTxNe", 64), ("sesEthTxNe", 65), ("uasEthTxNe", 66), ("dfrEthTxNe", 67), ("outframeserrEthTxNe", 68), ("outframesdiscdsEthTxNe", 69), ("esWanRxNe", 70), ("sesWanRxNe", 71), ("uasWanRxNe", 72), ("inframesWanRxNe", 73), ("inframeserrWanRxNe", 74), ("outframesWanTxNe", 75), ("oprMinOTSRxNe", 76), ("oprMaxOTSRxNe", 77), ("oprAvgOTSRxNe", 78), ("optMinOTSTxNe", 79), ("optMaxOTSTxNe", 80), ("optAvgOTSTxNe", 81), ("orlMinOTSNaNe", 82), ("orlMaxOTSNaNe", 83), ("orlAvgOTSNaNe", 84), ("opinMinOTSNaNe", 85), ("opinMaxOTSNaNe", 86), ("opinAvgOTSNaNe", 87), ("grpopinMinOTSNaNe", 88), ("grpopinMaxOTSNaNe", 89), ("grpopinAvgOTSNaNe", 90), ("grpgainMinOTSNaNe", 91), ("grpgainMaxOTSNaNe", 92), ("grpgainAvgOTSNaNe", 93), ("opoutMinOTSNaNe", 94), ("opoutMaxOTSNaNe", 95), ("opoutAvgOTSNaNe", 96), ("grpoptMinOTSTxNe", 97), ("grpoptMaxOTSTxNe", 98), ("grpoptAvgOTSTxNe", 99), ("grpopoutMinOTSNaNe", 100), ("grpopoutMaxOTSNaNe", 101), ("grpopoutAvgOTSNaNe", 102), ("dfrWanRxNe", 103), ("pscwODURxNe", 104), ("pscpODURxNe", 105), ("psdODURxNe", 106), ("cvLineRxFe", 107), ("esLineRxFe", 108), ("sesLineRxFe", 109), ("uasLineRxFe", 110), ("fcLineRxFe", 111), ("cvOTUTxNe", 112), ("esOTUTxNe", 113), ("sesOTUTxNe", 114), ("cvODUTxNe", 115), ("esODUTxNe", 116), ("sesODUTxNe", 117), ("uasODUTxNe", 118), ("fcODUTxNe", 119), ("oproscOTSNaNe", 120), ("oproscMinOTSNaNe", 121), ("oproscMaxOTSNaNe", 122), ("oproscAvgOTSNaNe", 123), ("pscwLineRxNe", 124), ("pscpLineRxNe", 125), ("psdLineRxNe", 126), ("dropgainOTSNaNe", 127), ("dropgainMinOTSNaNe", 128), ("dropgainMaxOTSNaNe", 129), ("dropgainAvgOTSNaNe", 130), ("dgdMaxOCHRxNe", 131), ("dgdAvgOCHRxNe", 132), ("optMinOCHTxNe", 133), ("optMaxOCHTxNe", 134), ("optAvgOCHTxNe", 135), ("prfBerMaxOTURxNe", 136), ("oprLowOCHRxNe", 137), ("oprHighOCHRxNe", 138), ("oprnLowOCHRxNe", 139), ("oprnHighOCHRxNe", 140), ("optLowOCHTxNe", 141), ("optHighOCHTxNe", 142), ("optnLowOCHTxNe", 143), ("optnHighOCHTxNe", 144), ("cvOTURxFe", 145), ("esOTURxFe", 146), ("sesOTURxFe", 147), ("cvODURxFe", 148), ("esODURxFe", 149), ("sesODURxFe", 150), ("uasODURxFe", 151), ("fcODURxFe", 152), ("oprnOTSRxNe", 153), ("sefsSectionTxNe", 154), ("spanLossOCH", 155), ("spanLossMinOCH", 156), ("spanLossMaxOCH", 157), ("spanLossAvgOCH", 158), ("qMinOTU", 159), ("qMaxOTU", 160), ("qAvgOTU", 161), ("qStdevOTU", 162), ("oprMinOCHRxNe", 163), ("oprMaxOCHRxNe", 164), ("oprAvgOCHRxNe", 165), ("optOCHRxNe", 166), ("optMinOCHRxNe", 167), ("optMaxOCHRxNe", 168), ("optAvgOCHRxNe", 169), ("orlInOTSNaNe", 170), ("orlInMinOTSNaNe", 171), ("orlInMaxOTSNaNe", 172), ("orlInAvgOTSNaNe", 173), ("orlOutOTSNaNe", 174), ("orlOutMinOTSNaNe", 175), ("orlOutMaxOTSNaNe", 176), ("orlOutAvgOTSNaNe", 177), ("dmMinODURxNe", 178), ("dmMaxODURxNe", 179), ("dmAvgODURxNe", 180), ("pscwEthRxNe", 181), ("pscpEthRxNe", 182), ("psdEthRxNe", 183), ("remoteInframesEthRxNe", 184), ("remoteInframesErrEthRxNe", 185), ("remoteFcsErrEthRxNe", 186), ("remoteOutframesEthTxNe", 187), ("remoteOutframesDiscdsEthTxNe", 188), ("uncfecblkOtuRxNe", 189), ("iaeOtuRxNe", 190), ("iaeOtuRxFe", 191), ("esWanTxNe", 192), ("sesWanTxNe", 193), ("uasWanTxNe", 194), ("outframeserrWanTxNe", 195), ("cvODUTxFe", 196), ("esODUTxFe", 197), ("sesODUTxFe", 198), ("uasODUTxFe", 199), ("fcODUTxFe", 200), ("fecPMARxNe", 201), ("fecccwPMARxNe", 202), ("fecunccwPMARxNe", 203), ("hccsPMARxNe", 204), ("prfberAvgPMARxNe", 205), ("prfberMaxPMARxNe", 206), ("fecLane0PMARxNe", 207), ("prfberAvgLane0PMARxNe", 208), ("prfberMaxLane0cPMARxNe", 209), ("fecLane1PMARxNe", 210), ("prfberAvgLane1PMARxNe", 211), ("prfberMaxLane1cPMARxNe", 212), ("fecLane2PMARxNe", 213), ("prfberAvgLane2PMARxNe", 214), ("prfberMaxLane2PMARxNe", 215), ("fecLane3PMARxNe", 216), ("prfberAvgLane3PMARxNe", 217), ("prfberMaxLane3PMARxNe", 218), ("dgdMinOCHRxNe", 219), ("prfberPMARxNe", 220), ("oprOTSIRxNe", 221), ("optOTSITxNe", 222), ("oprnOTSIRxNe", 223), ("optnOTSITxNe", 224), ("oprAvgOTSIRxNe", 225), ("oprMinOTSIRxNe", 226), ("oprMaxOTSIRxNe", 227), ("optAvgOTSITxNe", 228), ("optMinOTSITxNe", 229), ("optMaxOTSITxNe", 230), ("dgdAvgOTSIRxNe", 231), ("dgdMaxOTSIRxNe", 232), ("pdlAvgOTSIRxNe", 233), ("pdlMaxOTSIRxNe", 234), ("hccsOTSIRxNe", 235), ("fecOTSIRxNe", 236), ("prfberOTSIRxNe", 237), ("prfbereOTSIRxNe", 238), ("prfberMaxOTSIRxNe", 239), ("qMinOTSIRxNe", 240), ("qMaxOTSIRxNe", 241), ("qAvgOTSIRxNe", 242), ("qstdevOTSIRxNe", 243), ("uncfecblkOTSIRxNe", 244), ("dmMinLRxNe", 245), ("dmMaxLRxNe", 246), ("dmAvgLRxNe", 247), ("hccsPCSRxNe", 248), ("prfBerPCSRxNe", 249), ("prfBerMaxPCSRxNe", 250), ("fecPCSRxNe", 251), ("fecCcuPCSRxNe", 252), ("fecUnCcuPCSRxNe", 253), ("osnrAvgOTSIRxNe", 254), ("osnrMinOTSIRxNe", 255)) + NamedValues(("osnrMaxOTSIRxNe", 256), ("esnrAvgOTSIRxNe", 257), ("esnrMinOTSIRxNe", 258), ("esnrMaxOTSIRxNe", 259), ("cdAvgOTSIRxNe", 260), ("cdMinOTSIRxNe", 261), ("cdMaxOTSIRxNe", 262), ("pscwOTSRxNe", 263), ("pscpOTSRxNe", 264), ("psdOTSRxNe", 265), ("pdlAvgOCHRxNe", 266), ("pdlMaxOCHRxNe", 267), ("cdAvgOCHRxNe", 268), ("cdMinOCHRxNe", 269), ("cdMaxOCHRxNe", 270), ("csiMinOTSIRxNe", 271), ("csiMaxOTSIRxNe", 272), ("csiAvgOTSIRxNe", 273), ("snrExtMinOTSIRxNe", 274), ("snrExtMaxOTSIRxNe", 275), ("snrExtAvgOTSIRxNe", 276))

class NnOpticalPmUnits(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("none", 1), ("dB", 2), ("dBm", 3), ("percent", 4), ("ber", 5), ("pS", 6))

class NnOpticalPmValidity(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("notApplicable", 1), ("complete", 2), ("partial", 3), ("adjusted", 4))

nnOpticalPmRecent = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 1))
nnOpticalPmRecentTable = MibTable((1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 1, 1), )
if mibBuilder.loadTexts: nnOpticalPmRecentTable.setStatus('current')
nnOpticalPmRecentEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 1, 1, 1), ).setIndexNames((0, "NORTEL-OPTICAL-PM-MIB", "nnOpticalPmRecentIfIndex"), (0, "NORTEL-OPTICAL-PM-MIB", "nnOpticalPmRecentMonType"))
if mibBuilder.loadTexts: nnOpticalPmRecentEntry.setStatus('current')
nnOpticalPmRecentIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nnOpticalPmRecentIfIndex.setStatus('current')
nnOpticalPmRecentMonType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 1, 1, 1, 2), NnOpticalPmMonType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nnOpticalPmRecentMonType.setStatus('current')
nnOpticalPmRecentIfIndexDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 1, 1, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nnOpticalPmRecentIfIndexDescr.setStatus('current')
nnOpticalPmRecentMonTypeDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 1, 1, 1, 4), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nnOpticalPmRecentMonTypeDescr.setStatus('current')
nnOpticalPmRecentUnits = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 1, 1, 1, 5), NnOpticalPmUnits()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nnOpticalPmRecentUnits.setStatus('current')
nnOpticalPmCurr15MinValue = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 1, 1, 1, 6), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nnOpticalPmCurr15MinValue.setStatus('current')
nnOpticalPmCurr15MinValidity = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 1, 1, 1, 7), NnOpticalPmValidity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nnOpticalPmCurr15MinValidity.setStatus('current')
nnOpticalPmCurr15MinDateAndTime = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 1, 1, 1, 8), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nnOpticalPmCurr15MinDateAndTime.setStatus('current')
nnOpticalPmPrev15MinValue = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 1, 1, 1, 9), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nnOpticalPmPrev15MinValue.setStatus('current')
nnOpticalPmPrev15MinValidity = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 1, 1, 1, 10), NnOpticalPmValidity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nnOpticalPmPrev15MinValidity.setStatus('current')
nnOpticalPmPrev15MinDateAndTime = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 1, 1, 1, 11), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nnOpticalPmPrev15MinDateAndTime.setStatus('current')
nnOpticalPmCurrDayValue = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 1, 1, 1, 12), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nnOpticalPmCurrDayValue.setStatus('current')
nnOpticalPmCurrDayValidity = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 1, 1, 1, 13), NnOpticalPmValidity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nnOpticalPmCurrDayValidity.setStatus('current')
nnOpticalPmCurrDayDateAndTime = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 1, 1, 1, 14), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nnOpticalPmCurrDayDateAndTime.setStatus('current')
nnOpticalPmPrevDayValue = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 1, 1, 1, 15), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nnOpticalPmPrevDayValue.setStatus('current')
nnOpticalPmPrevDayValidity = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 1, 1, 1, 16), NnOpticalPmValidity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nnOpticalPmPrevDayValidity.setStatus('current')
nnOpticalPmPrevDayDateAndTime = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 1, 1, 1, 17), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nnOpticalPmPrevDayDateAndTime.setStatus('current')
nnOpticalPmUntimed = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 2))
nnOpticalPmUntTable = MibTable((1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 2, 1), )
if mibBuilder.loadTexts: nnOpticalPmUntTable.setStatus('current')
nnOpticalPmUntEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 2, 1, 1), ).setIndexNames((0, "NORTEL-OPTICAL-PM-MIB", "nnOpticalPmUntIfIndex"), (0, "NORTEL-OPTICAL-PM-MIB", "nnOpticalPmUntMonType"))
if mibBuilder.loadTexts: nnOpticalPmUntEntry.setStatus('current')
nnOpticalPmUntIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nnOpticalPmUntIfIndex.setStatus('current')
nnOpticalPmUntMonType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 2, 1, 1, 2), NnOpticalPmMonType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nnOpticalPmUntMonType.setStatus('current')
nnOpticalPmUntIfIndexDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 2, 1, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nnOpticalPmUntIfIndexDescr.setStatus('current')
nnOpticalPmUntMonTypeDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 2, 1, 1, 4), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nnOpticalPmUntMonTypeDescr.setStatus('current')
nnOpticalPmUntUnits = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 2, 1, 1, 5), NnOpticalPmUnits()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nnOpticalPmUntUnits.setStatus('current')
nnOpticalPmUntValue = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 2, 1, 1, 6), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nnOpticalPmUntValue.setStatus('current')
nnOpticalPmUntValidity = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 2, 1, 1, 7), NnOpticalPmValidity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nnOpticalPmUntValidity.setStatus('current')
nnOpticalPmUntDateAndTime = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 2, 1, 1, 8), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nnOpticalPmUntDateAndTime.setStatus('current')
nnOpticalPmBaseline = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 3))
nnOpticalPmBaslnTable = MibTable((1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 3, 1), )
if mibBuilder.loadTexts: nnOpticalPmBaslnTable.setStatus('current')
nnOpticalPmBaslnEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 3, 1, 1), ).setIndexNames((0, "NORTEL-OPTICAL-PM-MIB", "nnOpticalPmBaslnIfIndex"), (0, "NORTEL-OPTICAL-PM-MIB", "nnOpticalPmBaslnMonType"))
if mibBuilder.loadTexts: nnOpticalPmBaslnEntry.setStatus('current')
nnOpticalPmBaslnIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 3, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nnOpticalPmBaslnIfIndex.setStatus('current')
nnOpticalPmBaslnMonType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 3, 1, 1, 2), NnOpticalPmMonType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nnOpticalPmBaslnMonType.setStatus('current')
nnOpticalPmBaslnIfIndexDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 3, 1, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nnOpticalPmBaslnIfIndexDescr.setStatus('current')
nnOpticalPmBaslnMonTypeDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 3, 1, 1, 4), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nnOpticalPmBaslnMonTypeDescr.setStatus('current')
nnOpticalPmBaslnUnits = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 3, 1, 1, 5), NnOpticalPmUnits()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nnOpticalPmBaslnUnits.setStatus('current')
nnOpticalPmBaslnValue = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 3, 1, 1, 6), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nnOpticalPmBaslnValue.setStatus('current')
nnOpticalPmBaslnValidity = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 3, 1, 1, 7), NnOpticalPmValidity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nnOpticalPmBaslnValidity.setStatus('current')
nnOpticalPmBaslnDateAndTime = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 3, 1, 1, 8), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nnOpticalPmBaslnDateAndTime.setStatus('current')
nnOpticalPmTimed = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 4))
nnOpticalPm15Min = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 4, 1))
nnOpticalPm15MinTable = MibTable((1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 4, 1, 1), )
if mibBuilder.loadTexts: nnOpticalPm15MinTable.setStatus('current')
nnOpticalPm15MinEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 4, 1, 1, 1), ).setIndexNames((0, "NORTEL-OPTICAL-PM-MIB", "nnOpticalPm15MinIfIndex"), (0, "NORTEL-OPTICAL-PM-MIB", "nnOpticalPm15MinIntIndex"), (0, "NORTEL-OPTICAL-PM-MIB", "nnOpticalPm15MinMonType"))
if mibBuilder.loadTexts: nnOpticalPm15MinEntry.setStatus('current')
nnOpticalPm15MinIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 4, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nnOpticalPm15MinIfIndex.setStatus('current')
nnOpticalPm15MinIntIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 4, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nnOpticalPm15MinIntIndex.setStatus('current')
nnOpticalPm15MinMonType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 4, 1, 1, 1, 3), NnOpticalPmMonType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nnOpticalPm15MinMonType.setStatus('current')
nnOpticalPm15MinIfIndexDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 4, 1, 1, 1, 4), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nnOpticalPm15MinIfIndexDescr.setStatus('current')
nnOpticalPm15MinMonTypeDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 4, 1, 1, 1, 5), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nnOpticalPm15MinMonTypeDescr.setStatus('current')
nnOpticalPm15MinUnits = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 4, 1, 1, 1, 6), NnOpticalPmUnits()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nnOpticalPm15MinUnits.setStatus('current')
nnOpticalPm15MinValue = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 4, 1, 1, 1, 7), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nnOpticalPm15MinValue.setStatus('current')
nnOpticalPm15MinValidity = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 4, 1, 1, 1, 8), NnOpticalPmValidity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nnOpticalPm15MinValidity.setStatus('current')
nnOpticalPm15MinDateAndTime = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 4, 1, 1, 1, 9), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nnOpticalPm15MinDateAndTime.setStatus('current')
nnOpticalPmDay = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 4, 2))
nnOpticalPmDayTable = MibTable((1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 4, 2, 1), )
if mibBuilder.loadTexts: nnOpticalPmDayTable.setStatus('current')
nnOpticalPmDayEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 4, 2, 1, 1), ).setIndexNames((0, "NORTEL-OPTICAL-PM-MIB", "nnOpticalPmDayIfIndex"), (0, "NORTEL-OPTICAL-PM-MIB", "nnOpticalPmDayIntIndex"), (0, "NORTEL-OPTICAL-PM-MIB", "nnOpticalPmDayMonType"))
if mibBuilder.loadTexts: nnOpticalPmDayEntry.setStatus('current')
nnOpticalPmDayIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 4, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nnOpticalPmDayIfIndex.setStatus('current')
nnOpticalPmDayIntIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 4, 2, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nnOpticalPmDayIntIndex.setStatus('current')
nnOpticalPmDayMonType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 4, 2, 1, 1, 3), NnOpticalPmMonType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nnOpticalPmDayMonType.setStatus('current')
nnOpticalPmDayIfIndexDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 4, 2, 1, 1, 4), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nnOpticalPmDayIfIndexDescr.setStatus('current')
nnOpticalPmDayMonTypeDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 4, 2, 1, 1, 5), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nnOpticalPmDayMonTypeDescr.setStatus('current')
nnOpticalPmDayUnits = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 4, 2, 1, 1, 6), NnOpticalPmUnits()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nnOpticalPmDayUnits.setStatus('current')
nnOpticalPmDayValue = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 4, 2, 1, 1, 7), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nnOpticalPmDayValue.setStatus('current')
nnOpticalPmDayValidity = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 4, 2, 1, 1, 8), NnOpticalPmValidity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nnOpticalPmDayValidity.setStatus('current')
nnOpticalPmDayDateAndTime = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 4, 2, 1, 1, 9), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nnOpticalPmDayDateAndTime.setStatus('current')
mibBuilder.exportSymbols("NORTEL-OPTICAL-PM-MIB", nnOpticalPmCurr15MinValidity=nnOpticalPmCurr15MinValidity, nnOpticalPmCurrDayDateAndTime=nnOpticalPmCurrDayDateAndTime, nnOpticalPmUntEntry=nnOpticalPmUntEntry, nnOpticalPmBaslnMonType=nnOpticalPmBaslnMonType, nnOpticalPmRecent=nnOpticalPmRecent, nnOpticalPm15MinDateAndTime=nnOpticalPm15MinDateAndTime, nnOpticalPmPrev15MinDateAndTime=nnOpticalPmPrev15MinDateAndTime, nnOpticalPmCurrDayValue=nnOpticalPmCurrDayValue, nnOpticalPmPrevDayDateAndTime=nnOpticalPmPrevDayDateAndTime, nnOpticalPmBaslnValidity=nnOpticalPmBaslnValidity, nnOpticalPmDayValue=nnOpticalPmDayValue, nnOpticalPmMIB=nnOpticalPmMIB, nnOpticalPm15MinIfIndexDescr=nnOpticalPm15MinIfIndexDescr, nnOpticalPmBaslnEntry=nnOpticalPmBaslnEntry, nnOpticalPmDayUnits=nnOpticalPmDayUnits, nnOpticalPm15MinTable=nnOpticalPm15MinTable, nnOpticalPmUntValidity=nnOpticalPmUntValidity, nnOpticalPmDay=nnOpticalPmDay, nnOpticalPmRecentMonType=nnOpticalPmRecentMonType, PYSNMP_MODULE_ID=nnOpticalPmMIB, nnOpticalPmUntIfIndexDescr=nnOpticalPmUntIfIndexDescr, nnOpticalPmDayMonTypeDescr=nnOpticalPmDayMonTypeDescr, nnOpticalPmDayIntIndex=nnOpticalPmDayIntIndex, nnOpticalPmBaslnIfIndexDescr=nnOpticalPmBaslnIfIndexDescr, nnOpticalPm15MinValidity=nnOpticalPm15MinValidity, nnOpticalPmDayEntry=nnOpticalPmDayEntry, nnOpticalPmDayMonType=nnOpticalPmDayMonType, NnOpticalPmValidity=NnOpticalPmValidity, nnOpticalPmPrev15MinValidity=nnOpticalPmPrev15MinValidity, nnOpticalPm15MinMonTypeDescr=nnOpticalPm15MinMonTypeDescr, nnOpticalPmBaslnTable=nnOpticalPmBaslnTable, nnOpticalPm15MinUnits=nnOpticalPm15MinUnits, nnOpticalPmDayValidity=nnOpticalPmDayValidity, nnOpticalPmUntMonTypeDescr=nnOpticalPmUntMonTypeDescr, nnOpticalPmTimed=nnOpticalPmTimed, nnOpticalPmUntUnits=nnOpticalPmUntUnits, nnOpticalPmUntDateAndTime=nnOpticalPmUntDateAndTime, nnOpticalPmUntimed=nnOpticalPmUntimed, NnOpticalPmMonType=NnOpticalPmMonType, nnOpticalPmUntMonType=nnOpticalPmUntMonType, nnOpticalPmObjects=nnOpticalPmObjects, nnOpticalPmUntValue=nnOpticalPmUntValue, nnOpticalPmPrev15MinValue=nnOpticalPmPrev15MinValue, nnOpticalPmBaslnUnits=nnOpticalPmBaslnUnits, nnOpticalPmRecentUnits=nnOpticalPmRecentUnits, nnOpticalPmBaslnValue=nnOpticalPmBaslnValue, nnOpticalPmDayTable=nnOpticalPmDayTable, nnOpticalPmBaslnDateAndTime=nnOpticalPmBaslnDateAndTime, nnOpticalPmUntIfIndex=nnOpticalPmUntIfIndex, nnOpticalPmBaslnMonTypeDescr=nnOpticalPmBaslnMonTypeDescr, nnOpticalPmRecentMonTypeDescr=nnOpticalPmRecentMonTypeDescr, NnOpticalPmUnits=NnOpticalPmUnits, nnOpticalPm15MinEntry=nnOpticalPm15MinEntry, nnOpticalPm15MinIfIndex=nnOpticalPm15MinIfIndex, nnOpticalPmBaseline=nnOpticalPmBaseline, nnOpticalPmRecentIfIndex=nnOpticalPmRecentIfIndex, nnOpticalPmCurr15MinValue=nnOpticalPmCurr15MinValue, nnOpticalPmPrevDayValidity=nnOpticalPmPrevDayValidity, nnOpticalPmBaslnIfIndex=nnOpticalPmBaslnIfIndex, nnOpticalPm15MinValue=nnOpticalPm15MinValue, nnOpticalPmRecentIfIndexDescr=nnOpticalPmRecentIfIndexDescr, nnOpticalPmDayDateAndTime=nnOpticalPmDayDateAndTime, nnOpticalPmRecentEntry=nnOpticalPmRecentEntry, nnOpticalPmDayIfIndex=nnOpticalPmDayIfIndex, nnOpticalPmDayIfIndexDescr=nnOpticalPmDayIfIndexDescr, nnOpticalPmCurr15MinDateAndTime=nnOpticalPmCurr15MinDateAndTime, nnOpticalPmUntTable=nnOpticalPmUntTable, nnOpticalPmCurrDayValidity=nnOpticalPmCurrDayValidity, nnOpticalPm15MinIntIndex=nnOpticalPm15MinIntIndex, nnOpticalPm15Min=nnOpticalPm15Min, nnOpticalPmPrevDayValue=nnOpticalPmPrevDayValue, nnOpticalPmRecentTable=nnOpticalPmRecentTable, nnOpticalPm15MinMonType=nnOpticalPm15MinMonType)
