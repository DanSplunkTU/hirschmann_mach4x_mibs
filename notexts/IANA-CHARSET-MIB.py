#
# PySNMP MIB module IANA-CHARSET-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/IANA-CHARSET-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 17:49:36 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, iso, ObjectIdentity, IpAddress, Counter64, Bits, mib_2, Counter32, NotificationType, Unsigned32, Gauge32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "iso", "ObjectIdentity", "IpAddress", "Counter64", "Bits", "mib-2", "Counter32", "NotificationType", "Unsigned32", "Gauge32", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ianaCharsetMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 106))
ianaCharsetMIB.setRevisions(('2007-05-14 00:00', '2006-12-07 00:00', '2004-06-08 00:00',))
if mibBuilder.loadTexts: ianaCharsetMIB.setLastUpdated('200705140000Z')
if mibBuilder.loadTexts: ianaCharsetMIB.setOrganization('IANA')
class IANACharset(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 1000, 1001, 1002, 1003, 1005, 1006, 1007, 1008, 1009, 1010, 1011, 1012, 1013, 1014, 1015, 1016, 1017, 1018, 1019, 1020, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030, 2031, 2032, 2033, 2034, 2035, 2036, 2037, 2038, 2039, 2040, 2041, 2042, 2043, 2044, 2045, 2046, 2047, 2048, 2049, 2050, 2051, 2052, 2053, 2054, 2055, 2056, 2057, 2058, 2059, 2060, 2061, 2062, 2063, 2064, 2065, 2066, 2067, 2068, 2069, 2070, 2071, 2072, 2073, 2074, 2075, 2076, 2077, 2078, 2079, 2080, 2081, 2082, 2083, 2084, 2085, 2086, 2087, 2088, 2089, 2090, 2091, 2092, 2093, 2094, 2095, 2096, 2097, 2098, 2099, 2100, 2101, 2102, 2103, 2104, 2105, 2106, 2107, 2250, 2251, 2252, 2253, 2254, 2255, 2256, 2257, 2258, 2259), SingleValueConstraint(3000))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("csASCII", 3), ("csISOLatin1", 4), ("csISOLatin2", 5), ("csISOLatin3", 6), ("csISOLatin4", 7), ("csISOLatinCyrillic", 8), ("csISOLatinArabic", 9), ("csISOLatinGreek", 10), ("csISOLatinHebrew", 11), ("csISOLatin5", 12), ("csISOLatin6", 13), ("csISOTextComm", 14), ("csHalfWidthKatakana", 15), ("csJISEncoding", 16), ("csShiftJIS", 17), ("csEUCPkdFmtJapanese", 18), ("csEUCFixWidJapanese", 19), ("csISO4UnitedKingdom", 20), ("csISO11SwedishForNames", 21), ("csISO15Italian", 22), ("csISO17Spanish", 23), ("csISO21German", 24), ("csISO60DanishNorwegian", 25), ("csISO69French", 26), ("csISO10646UTF1", 27), ("csISO646basic1983", 28), ("csINVARIANT", 29), ("csISO2IntlRefVersion", 30), ("csNATSSEFI", 31), ("csNATSSEFIADD", 32), ("csNATSDANO", 33), ("csNATSDANOADD", 34), ("csISO10Swedish", 35), ("csKSC56011987", 36), ("csISO2022KR", 37), ("csEUCKR", 38), ("csISO2022JP", 39), ("csISO2022JP2", 40), ("csISO13JISC6220jp", 41), ("csISO14JISC6220ro", 42), ("csISO16Portuguese", 43), ("csISO18Greek7Old", 44), ("csISO19LatinGreek", 45), ("csISO25French", 46), ("csISO27LatinGreek1", 47), ("csISO5427Cyrillic", 48), ("csISO42JISC62261978", 49), ("csISO47BSViewdata", 50), ("csISO49INIS", 51), ("csISO50INIS8", 52), ("csISO51INISCyrillic", 53), ("csISO54271981", 54), ("csISO5428Greek", 55), ("csISO57GB1988", 56), ("csISO58GB231280", 57), ("csISO61Norwegian2", 58), ("csISO70VideotexSupp1", 59), ("csISO84Portuguese2", 60), ("csISO85Spanish2", 61), ("csISO86Hungarian", 62), ("csISO87JISX0208", 63), ("csISO88Greek7", 64), ("csISO89ASMO449", 65), ("csISO90", 66), ("csISO91JISC62291984a", 67), ("csISO92JISC62991984b", 68), ("csISO93JIS62291984badd", 69), ("csISO94JIS62291984hand", 70), ("csISO95JIS62291984handadd", 71), ("csISO96JISC62291984kana", 72), ("csISO2033", 73), ("csISO99NAPLPS", 74), ("csISO102T617bit", 75), ("csISO103T618bit", 76), ("csISO111ECMACyrillic", 77), ("csa71", 78), ("csa72", 79), ("csISO123CSAZ24341985gr", 80), ("csISO88596E", 81), ("csISO88596I", 82), ("csISO128T101G2", 83), ("csISO88598E", 84), ("csISO88598I", 85), ("csISO139CSN369103", 86), ("csISO141JUSIB1002", 87), ("csISO143IECP271", 88), ("csISO146Serbian", 89), ("csISO147Macedonian", 90), ("csISO150", 91), ("csISO151Cuba", 92), ("csISO6937Add", 93), ("csISO153GOST1976874", 94), ("csISO8859Supp", 95), ("csISO10367Box", 96), ("csISO158Lap", 97), ("csISO159JISX02121990", 98), ("csISO646Danish", 99), ("csUSDK", 100), ("csDKUS", 101), ("csKSC5636", 102), ("csUnicode11UTF7", 103), ("csISO2022CN", 104), ("csISO2022CNEXT", 105), ("csUTF8", 106), ("csISO885913", 109), ("csISO885914", 110), ("csISO885915", 111), ("csISO885916", 112), ("csGBK", 113), ("csGB18030", 114), ("csOSDEBCDICDF0415", 115), ("csOSDEBCDICDF03IRV", 116), ("csOSDEBCDICDF041", 117), ("csISO115481", 118), ("csKZ1048", 119), ("csUnicode", 1000), ("csUCS4", 1001), ("csUnicodeASCII", 1002), ("csUnicodeLatin1", 1003), ("csUnicodeIBM1261", 1005), ("csUnicodeIBM1268", 1006), ("csUnicodeIBM1276", 1007), ("csUnicodeIBM1264", 1008), ("csUnicodeIBM1265", 1009), ("csUnicode11", 1010), ("csSCSU", 1011), ("csUTF7", 1012), ("csUTF16BE", 1013), ("csUTF16LE", 1014), ("csUTF16", 1015), ("csCESU8", 1016), ("csUTF32", 1017), ("csUTF32BE", 1018), ("csUTF32LE", 1019), ("csBOCU1", 1020), ("csWindows30Latin1", 2000), ("csWindows31Latin1", 2001), ("csWindows31Latin2", 2002), ("csWindows31Latin5", 2003), ("csHPRoman8", 2004), ("csAdobeStandardEncoding", 2005), ("csVenturaUS", 2006), ("csVenturaInternational", 2007), ("csDECMCS", 2008), ("csPC850Multilingual", 2009), ("csPCp852", 2010), ("csPC8CodePage437", 2011), ("csPC8DanishNorwegian", 2012), ("csPC862LatinHebrew", 2013), ("csPC8Turkish", 2014), ("csIBMSymbols", 2015), ("csIBMThai", 2016), ("csHPLegal", 2017), ("csHPPiFont", 2018), ("csHPMath8", 2019), ("csHPPSMath", 2020), ("csHPDesktop", 2021), ("csVenturaMath", 2022), ("csMicrosoftPublishing", 2023), ("csWindows31J", 2024), ("csGB2312", 2025), ("csBig5", 2026), ("csMacintosh", 2027), ("csIBM037", 2028), ("csIBM038", 2029), ("csIBM273", 2030), ("csIBM274", 2031), ("csIBM275", 2032), ("csIBM277", 2033), ("csIBM278", 2034), ("csIBM280", 2035), ("csIBM281", 2036), ("csIBM284", 2037), ("csIBM285", 2038), ("csIBM290", 2039), ("csIBM297", 2040), ("csIBM420", 2041), ("csIBM423", 2042), ("csIBM424", 2043), ("csIBM500", 2044), ("csIBM851", 2045), ("csIBM855", 2046), ("csIBM857", 2047), ("csIBM860", 2048), ("csIBM861", 2049), ("csIBM863", 2050), ("csIBM864", 2051), ("csIBM865", 2052), ("csIBM868", 2053), ("csIBM869", 2054), ("csIBM870", 2055), ("csIBM871", 2056), ("csIBM880", 2057), ("csIBM891", 2058), ("csIBM903", 2059), ("csIBBM904", 2060), ("csIBM905", 2061), ("csIBM918", 2062), ("csIBM1026", 2063), ("csIBMEBCDICATDE", 2064), ("csEBCDICATDEA", 2065), ("csEBCDICCAFR", 2066), ("csEBCDICDKNO", 2067), ("csEBCDICDKNOA", 2068), ("csEBCDICFISE", 2069), ("csEBCDICFISEA", 2070), ("csEBCDICFR", 2071), ("csEBCDICIT", 2072), ("csEBCDICPT", 2073), ("csEBCDICES", 2074), ("csEBCDICESA", 2075), ("csEBCDICESS", 2076), ("csEBCDICUK", 2077), ("csEBCDICUS", 2078), ("csUnknown8BiT", 2079), ("csMnemonic", 2080), ("csMnem", 2081), ("csVISCII", 2082), ("csVIQR", 2083), ("csKOI8R", 2084), ("csHZGB2312", 2085), ("csIBM866", 2086), ("csPC775Baltic", 2087), ("csKOI8U", 2088), ("csIBM00858", 2089), ("csIBM00924", 2090), ("csIBM01140", 2091), ("csIBM01141", 2092), ("csIBM01142", 2093), ("csIBM01143", 2094), ("csIBM01144", 2095), ("csIBM01145", 2096), ("csIBM01146", 2097), ("csIBM01147", 2098), ("csIBM01148", 2099), ("csIBM01149", 2100), ("csBig5HKSCS", 2101), ("csIBM1047", 2102), ("csPTCP154", 2103), ("csAmiga1251", 2104), ("csKOI7switched", 2105), ("csBRF", 2106), ("csTSCII", 2107), ("cswindows1250", 2250), ("cswindows1251", 2251), ("cswindows1252", 2252), ("cswindows1253", 2253), ("cswindows1254", 2254), ("cswindows1255", 2255), ("cswindows1256", 2256), ("cswindows1257", 2257), ("cswindows1258", 2258), ("csTIS620", 2259)) + NamedValues(("reserved", 3000))

mibBuilder.exportSymbols("IANA-CHARSET-MIB", PYSNMP_MODULE_ID=ianaCharsetMIB, ianaCharsetMIB=ianaCharsetMIB, IANACharset=IANACharset)
