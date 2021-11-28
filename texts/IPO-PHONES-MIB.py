#
# PySNMP MIB module IPO-PHONES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/avaya/IPO-PHONES-MIB.mib
# Produced by pysmi-1.1.3 at Sun Nov 28 20:15:36 2021
# On host fv-az77-612 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
IndexInteger, = mibBuilder.importSymbols("DIFFSERV-MIB", "IndexInteger")
ipoGTEventDevID, ipoGTEventDateTime, ipoGTEventStdSeverity, ipoGTEventEntityName, ipoGTEventSeverity, ipoGenMibs = mibBuilder.importSymbols("IPO-MIB", "ipoGTEventDevID", "ipoGTEventDateTime", "ipoGTEventStdSeverity", "ipoGTEventEntityName", "ipoGTEventSeverity", "ipoGenMibs")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
sysDescr, = mibBuilder.importSymbols("SNMPv2-MIB", "sysDescr")
Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Gauge32, ObjectIdentity, Bits, TimeTicks, Integer32, MibIdentifier, NotificationType, IpAddress, Counter32, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Gauge32", "ObjectIdentity", "Bits", "TimeTicks", "Integer32", "MibIdentifier", "NotificationType", "IpAddress", "Counter32", "Unsigned32", "iso")
DisplayString, PhysAddress, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "PhysAddress", "TextualConvention")
ipoPhonesMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 1, 1))
ipoPhonesMIB.setRevisions(('2011-02-09 15:21', '2009-02-18 13:09', '2008-06-12 15:06', '2008-04-17 16:30', '2007-03-28 12:09', '2007-02-24 12:09', '2006-06-29 00:00', '2006-01-31 00:00', '2005-11-22 00:00', '2005-07-21 10:50', '2005-07-21 10:30', '2005-03-04 00:00', '2005-01-06 00:00', '2004-12-20 00:00', '2004-03-03 00:00', '2003-10-10 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ipoPhonesMIB.setRevisionsDescriptions(('Rev 2.00.06\n        PhoneType: adding more original Nortel phone sets.', 'Rev 2.00.05\n        PhoneType enumerations for a number of SIP phones,\n        the 1400 phones and PhoneManager IP SoftPhone added.', 'Rev 2.00.04\n        PhoneType enumerations for the 1700 phones added.', 'Rev 2.00.03\n        Added descriptions for new PhoneType enumerations\n        and corrected versioning.', 'Rev 2.00.02\n        Added the port number, module number, ip address,\n        and physical address, to the ipoPhonesTable', 'Rev 2.00.01\n        Added descriptions for new PhoneType enumerations\n        and corrected versioning.', 'Rev 2.00.00\n        Traps/notifications revised to provide more information about\n        the entity and device concerned.', 'Rev 1.00.08\n        Corrected enumeration for 5621 IP phones.', 'Rev 1.00.07\n        Revised for 5621 IP phones.', 'Rev 1.00.06\n        Revised for 4621 IP phones.', 'Rev 1.00.05\n        Revised for 5601 and 5602 Phones', 'Rev 1.00.04\n        Revised for IP Soft Phones', 'Rev 1.00.03\n        Revised for 5610/5620 IP phones.', 'Rev 1.00.02\n        Revised for additional phone support.', 'Rev 1.00.01\n        Revised for external publication.', 'Rev 1.0.0\n        The first published version of this MIB module.',))
if mibBuilder.loadTexts: ipoPhonesMIB.setLastUpdated('201102091521Z')
if mibBuilder.loadTexts: ipoPhonesMIB.setOrganization('Avaya Inc.')
if mibBuilder.loadTexts: ipoPhonesMIB.setContactInfo('Avaya Customer Services\n         Postal: Avaya, Inc.\n                 211 Mt Airy Rd.\n                 Basking Ridge, NJ 07920\n                 USA\n         Tel:    +1 908 953 6000\n\n         WWW:    http://www.avaya.com')
if mibBuilder.loadTexts: ipoPhonesMIB.setDescription('Avaya IP Office Phones MIB\n\n         The MIB module for representing the phones present on a Avaya\n         IP Office stack.')
ipoPhonesMibNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 1, 1, 0))
ipoPhonesMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 1, 1, 1))
ipoPhonesConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 1, 1, 2))
class PhoneType(TextualConvention, Integer32):
    description = 'This data type is used as the syntax of the ipoPhoneType\n        object in the ipoPhonesTable.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170))
    namedValues = NamedValues(("noPhone", 1), ("genericPhone", 2), ("potPhone", 3), ("dtPhone", 4), ("a4406Dplus", 5), ("a4412Dplus", 6), ("a4424Dplus", 7), ("a4424LDplus", 8), ("a9040TransTalk", 9), ("a6408Dplus", 10), ("a6416Dplus", 11), ("a6424Dplus", 12), ("a4606ip", 13), ("a4612ip", 14), ("a4624ip", 15), ("a4620ip", 16), ("a4602ip", 17), ("a2420", 18), ("a2010dt", 19), ("a2020dt", 20), ("a2030dt", 21), ("a2050dt", 22), ("act5", 23), ("att3", 24), ("att5", 25), ("a5420", 26), ("a5410", 27), ("a4601ip", 28), ("a4610ip", 29), ("ablf", 30), ("a2402", 31), ("a2410", 32), ("a5610ip", 33), ("a5620ip", 34), ("softIPPhone", 35), ("a5601ip", 36), ("a5602ip", 37), ("a4621ip", 38), ("a5621ip", 39), ("a4625ip", 40), ("a5402", 41), ("h323Phone", 42), ("sipPhone", 43), ("t3Compact", 44), ("t3Classic", 45), ("t3Comfort", 46), ("t3Phone", 47), ("t3compactIP", 48), ("t3classicIP", 49), ("t3comfortIP", 50), ("avayaSip", 51), ("admmPhone", 52), ("a9620ip", 53), ("a9630ip", 54), ("telecommuter", 55), ("mobiletwin", 56), ("a9640ip", 57), ("a9650ip", 58), ("a9610ip", 59), ("a1603ip", 60), ("a1608ip", 61), ("a1616ip", 62), ("a1703ip", 63), ("a1708ip", 64), ("a1716ip", 65), ("s60Sip", 66), ("sp320Sip", 67), ("sp601Sip", 68), ("a10ataSip", 69), ("pmataSip", 70), ("ip22Sip", 71), ("ip24Sip", 72), ("gxp2000Sip", 73), ("gxp2020Sip", 74), ("eyebeamSip", 75), ("a1403", 76), ("a1408", 77), ("a1416", 78), ("a1450", 79), ("ip28Sip", 80), ("phoneManagerIP", 81), ("a1503", 82), ("a1508", 83), ("a1516", 84), ("a1550", 85), ("a1603Lip", 86), ("a1608Lip", 87), ("a1616Lip", 88), ("softPhoneSip", 89), ("etr34d", 90), ("etr18d", 91), ("etr6d", 92), ("etr34", 93), ("etr18", 94), ("etr6", 95), ("etrpots", 96), ("doorphone1", 97), ("doorphone2", 98), ("bstT7316e", 99), ("a9620Sip", 100), ("a9630Sip", 101), ("a9640Sip", 102), ("a9650Sip", 103), ("a96xxSip", 104), ("a1603Sip", 105), ("a9404", 106), ("a9408", 107), ("a9504", 108), ("a9508", 109), ("a9608ip", 110), ("a9611ip", 111), ("a9621ip", 112), ("a9641ip", 113), ("a3720Admm", 114), ("a3725Admm", 115), ("a1010Sip", 116), ("a1040Sip", 117), ("a1120ESip", 118), ("a1140ESip", 119), ("a1220Sip", 120), ("a1230Sip", 121), ("a1692Sip", 122), ("pvvxSip", 123), ("gxv3140Sip", 124), ("a3740Admm", 125), ("a3749Admm", 126), ("bstT7316", 127), ("bstT7208", 128), ("bstM7208", 129), ("bstM7310", 130), ("bstM7310blf", 131), ("bstM7324", 132), ("bstM7100", 133), ("bstT7100", 134), ("bstT7000", 135), ("bstDectA", 136), ("bstDectB", 137), ("bstDectC", 138), ("bstDoorphone", 139), ("bstT7406", 140), ("bstT7406E", 141), ("bstM7310N", 142), ("bstAcu", 143), ("bstM7100N", 144), ("bstM7324N", 145), ("bstM7208N", 146), ("aB179Sip", 147), ("bstAta", 148), ("aA175Sip", 149), ("aOneXSip", 150), ("aFlareSip", 151), ("aD100", 152), ("aRadvisionXT1000", 153), ("aRadvisionXT1200", 154), ("aRadvisionXT4000", 155), ("aRadvisionXT4200", 156), ("aRadvisionXT5000", 157), ("aRadvisionXTPiccolo", 158), ("aRadvisionScopiaMCU", 159), ("aRadvisionScopiaVC240", 160), ("aOneXSipMobile", 161), ("aACCSServer", 162), ("aCIEServer", 163), ("aE129SIP", 164), ("aE159SIP", 165), ("aE169SIP", 166), ("aOneXMsiSIP", 167), ("aRadvisionXT240", 168), ("aWebRTCSIP", 169), ("softPhoneSipMac", 170))

ipoPhones = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 1, 1, 1, 1))
ipoPhonesNumber = MibScalar((1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 1, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipoPhonesNumber.setStatus('current')
if mibBuilder.loadTexts: ipoPhonesNumber.setDescription('The number of phone interfaces (regardless of their current\n        state) present on this system.')
ipoPhonesTable = MibTable((1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 1, 1, 1, 1, 2), )
if mibBuilder.loadTexts: ipoPhonesTable.setStatus('current')
if mibBuilder.loadTexts: ipoPhonesTable.setDescription('A list of phone entries.  The number of entries is given by\n        the value of ipoPhonesNumber.')
ipoPhonesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 1, 1, 1, 1, 2, 1), ).setIndexNames((0, "IPO-PHONES-MIB", "ipoPhonesIndex"))
if mibBuilder.loadTexts: ipoPhonesEntry.setStatus('current')
if mibBuilder.loadTexts: ipoPhonesEntry.setDescription('An entry containing management information applicable to a\n        particular IP Office phone.')
ipoPhonesIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 1, 1, 1, 1, 2, 1, 1), IndexInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipoPhonesIndex.setStatus('current')
if mibBuilder.loadTexts: ipoPhonesIndex.setDescription("A unique value, greater than zero, for each phone.  It is\n         recommended that values are assigned contiguously starting\n         from 1.  The value for each phone sub-layer must remain\n         constant at least from one re-initialization of the entity's\n         network management system to the next re- initialization.")
ipoPhonesExtID = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 1, 1, 1, 1, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipoPhonesExtID.setStatus('current')
if mibBuilder.loadTexts: ipoPhonesExtID.setDescription('The numerical logical extension entity identifier assigned to\n         the phone on the IP Office entity.')
ipoPhonesExtNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 1, 1, 1, 1, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipoPhonesExtNumber.setStatus('current')
if mibBuilder.loadTexts: ipoPhonesExtNumber.setDescription('The number that should be dialed to reach this phone on the\n        IP Office entity.')
ipoPhonesUserShort = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 1, 1, 1, 1, 2, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipoPhonesUserShort.setStatus('current')
if mibBuilder.loadTexts: ipoPhonesUserShort.setDescription('The short form of the name of the user of this phone which is\n        used in caller display. This is quite often the forename of\n        the user.')
ipoPhonesUserLong = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 1, 1, 1, 1, 2, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipoPhonesUserLong.setStatus('current')
if mibBuilder.loadTexts: ipoPhonesUserLong.setDescription('The long form of the name of the user of this phone. This is\n        normally the full name (forename and surname) of the user.')
ipoPhonesType = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 1, 1, 1, 1, 2, 1, 6), PhoneType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipoPhonesType.setStatus('current')
if mibBuilder.loadTexts: ipoPhonesType.setDescription('The type of phone that is connected to this IP Office logical\n        phone extension.')
ipoPhonesPort = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 1, 1, 1, 1, 2, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipoPhonesPort.setStatus('current')
if mibBuilder.loadTexts: ipoPhonesPort.setDescription('A reference, by entPhysicalIndex value, to the\n        EntPhysicalEntry representing the physical port entity that\n        this phone entry is associated with in an entity MIB\n        instantiation within the IP Office agent. If no MIB\n        definitions specific to the particular media are available, or\n        the entry is for a IP phone which may not be connected to a\n        physical port on the IP Office, the value should be set to the\n        value 0.')
ipoPhonesPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 1, 1, 1, 1, 2, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipoPhonesPortNumber.setStatus('current')
if mibBuilder.loadTexts: ipoPhonesPortNumber.setDescription("The port number on the module that the operator uses to\n        identify the port.\n\n        The port numbers on the expansion modules will follow standard \n        numbering, beginning at 1 and incrementing until the last port.\n        The phone ports on the base units, however, are numbered \n        according to how they are collected into 'banks' on the unit.\n\n        IP Office IP500\n            The entire front of the product consists of 4 plug-in modules. \n            Each module has its own numbering from 1..12.\n            So from the left: 101..112, 201..212, etc.\n\n        IP Office IP412 \n            There is no way to plug phones into the unit, so only \n            expansion modules should be present. \n\n        IP Office IP406v2\n            The leftmost bank of ports are Digital (DS/DT) and labeled \n            as 1-8 on the product, and so are labelled ports 101..108 \n            in the mib.\n\n            The next bank of ports are Analogue and labeled as 1-2 \n            on the product and so are labelled ports 201..202 in the mib.\n\n            The next bank of phones are LAN and labeled as 1-8 on the \n            product. Not phones, so not in this mib.\n\n        IP Office Small Office Edition\n            The leftmost bank of 4 ports are Trunk ports, and so are not \n            available in this mib.\n\n            The next bank of 8 ports are Digital (DS/DT), and so are \n            labelled ports 101..108 in the mib.\n\n            The next bank of 4 ports are Analogue, and so are labelled \n            ports 201..204 in the mib.\n\n            The next bank of ports are LAN, and so are not available in \n            this mib.")
ipoPhonesModuleNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 1, 1, 1, 1, 2, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipoPhonesModuleNumber.setStatus('current')
if mibBuilder.loadTexts: ipoPhonesModuleNumber.setDescription("The number that the operator uses to\n        identify the module.\n\n        The module numbers are assigned according to the expansion \n        port number that it's plugged into on the Control unit.\n\n        Example: Module number '2' = Expansion unit plugged into \n        expansion port 2 on the Control unit.\n\n        Module number '0' is reserved for the Control unit itself.")
ipoPhonesIPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 1, 1, 1, 1, 2, 1, 10), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipoPhonesIPAddress.setStatus('current')
if mibBuilder.loadTexts: ipoPhonesIPAddress.setDescription('The IP Address of the phone. In network-byte order. In the usual\n        IP Address format - xxx.xxx.xxx.xxx.\n\n        The IP address will only be present if the phone is an IP phone. If\n        it is not, it will contain zeros (0.0.0.0).')
ipoPhonesPhysAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 1, 1, 1, 1, 2, 1, 11), PhysAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipoPhonesPhysAddress.setStatus('current')
if mibBuilder.loadTexts: ipoPhonesPhysAddress.setDescription('The Physical Address of the phone, such as the MAC Address.\n\n        The physical address will only be present if the phone is an IP \n        phone. If it is not, it will contain zeros (00.00.00.00.00.00).')
ipoPhonesChangeEvent = NotificationType((1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 1, 1, 0, 1)).setObjects(("IPO-MIB", "ipoGTEventSeverity"), ("IPO-MIB", "ipoGTEventDateTime"), ("IPO-PHONES-MIB", "ipoPhonesExtID"), ("IPO-PHONES-MIB", "ipoPhonesType"), ("IPO-PHONES-MIB", "ipoPhonesPort"))
if mibBuilder.loadTexts: ipoPhonesChangeEvent.setStatus('deprecated')
if mibBuilder.loadTexts: ipoPhonesChangeEvent.setDescription('This notification is generated whenever the type of phone\n\tconnected to a logical extension entity is detected as having\n\tchanged after completion of normal start up of the Agent\n\tentity.\n\n\tIts purpose is to allow a management application to identify\n\tthe removal or switching of phone types on the IP Office\n\tentity.\n\n        **NOTE: This notification is deprecated and replaced by\n          ipoPhonesChangeSvcEvent.')
ipoPhonesChangeSvcEvent = NotificationType((1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 1, 1, 0, 2)).setObjects(("IPO-MIB", "ipoGTEventStdSeverity"), ("IPO-MIB", "ipoGTEventDateTime"), ("IPO-MIB", "ipoGTEventDevID"), ("SNMPv2-MIB", "sysDescr"), ("IPO-PHONES-MIB", "ipoPhonesExtID"), ("IPO-PHONES-MIB", "ipoPhonesType"), ("IPO-PHONES-MIB", "ipoPhonesPort"), ("IPO-MIB", "ipoGTEventEntityName"))
if mibBuilder.loadTexts: ipoPhonesChangeSvcEvent.setStatus('current')
if mibBuilder.loadTexts: ipoPhonesChangeSvcEvent.setDescription('This notification is generated whenever the type of phone\n\tconnected to a logical extension entity is detected as having\n\tchanged after completion of normal start up of the Agent\n\tentity.\n\n\tIts purpose is to allow a management application to identify\n\tthe removal or switching of phone types on the IP Office\n\tentity.\n\n        Newer implementations of this MIB should put in place this\n        event in favour of ipoPhonesChangeEvent.')
ipoPhonesCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 1, 1, 2, 1))
ipoPhonesGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 1, 1, 2, 2))
ipoPhonesCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 1, 1, 2, 1, 1)).setObjects(("IPO-PHONES-MIB", "ipoPhonesGroup"), ("IPO-PHONES-MIB", "ipoPhonesNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ipoPhonesCompliance = ipoPhonesCompliance.setStatus('deprecated')
if mibBuilder.loadTexts: ipoPhonesCompliance.setDescription('The compliance statement for the IP Office Phones MIB')
ipoPhonesv2Compliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 1, 1, 2, 1, 2)).setObjects(("IPO-PHONES-MIB", "ipoPhonesGroup"), ("IPO-PHONES-MIB", "ipoPhonesv2NotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ipoPhonesv2Compliance = ipoPhonesv2Compliance.setStatus('deprecated')
if mibBuilder.loadTexts: ipoPhonesv2Compliance.setDescription('The compliance statement for the IP Office Phones MIB')
ipoPhonesv3Compliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 1, 1, 2, 1, 3)).setObjects(("IPO-PHONES-MIB", "ipoPhonesGroup"), ("IPO-PHONES-MIB", "ipoPhones2Group"), ("IPO-PHONES-MIB", "ipoPhonesv2NotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ipoPhonesv3Compliance = ipoPhonesv3Compliance.setStatus('current')
if mibBuilder.loadTexts: ipoPhonesv3Compliance.setDescription('The compliance statement for the IP Office Phones MIB')
ipoPhonesGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 1, 1, 2, 2, 1)).setObjects(("IPO-PHONES-MIB", "ipoPhonesNumber"), ("IPO-PHONES-MIB", "ipoPhonesIndex"), ("IPO-PHONES-MIB", "ipoPhonesExtID"), ("IPO-PHONES-MIB", "ipoPhonesExtNumber"), ("IPO-PHONES-MIB", "ipoPhonesUserShort"), ("IPO-PHONES-MIB", "ipoPhonesUserLong"), ("IPO-PHONES-MIB", "ipoPhonesType"), ("IPO-PHONES-MIB", "ipoPhonesPort"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ipoPhonesGroup = ipoPhonesGroup.setStatus('current')
if mibBuilder.loadTexts: ipoPhonesGroup.setDescription('The collection of objects which are used to represent IP\n\tOffice phones, for which a single agent provides management\n\tinformation.')
ipoPhonesNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 1, 1, 2, 2, 2)).setObjects(("IPO-PHONES-MIB", "ipoPhonesChangeEvent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ipoPhonesNotificationsGroup = ipoPhonesNotificationsGroup.setStatus('deprecated')
if mibBuilder.loadTexts: ipoPhonesNotificationsGroup.setDescription('The notifications which indicate specific changes in the\n\tstate of IP Office phones.')
ipoPhonesv2NotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 1, 1, 2, 2, 3)).setObjects(("IPO-PHONES-MIB", "ipoPhonesChangeSvcEvent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ipoPhonesv2NotificationsGroup = ipoPhonesv2NotificationsGroup.setStatus('current')
if mibBuilder.loadTexts: ipoPhonesv2NotificationsGroup.setDescription('The notifications which indicate specific changes in the\n\tstate of IP Office phones for newer implementations of this\n\tMIB.')
ipoPhones2Group = ObjectGroup((1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 1, 1, 2, 2, 4)).setObjects(("IPO-PHONES-MIB", "ipoPhonesPortNumber"), ("IPO-PHONES-MIB", "ipoPhonesModuleNumber"), ("IPO-PHONES-MIB", "ipoPhonesIPAddress"), ("IPO-PHONES-MIB", "ipoPhonesPhysAddress"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ipoPhones2Group = ipoPhones2Group.setStatus('current')
if mibBuilder.loadTexts: ipoPhones2Group.setDescription('Additional collection of objects which are used to represent\n\tphysical information about IP Office phones, for which a\n\tsingle agent provides management information.  These objects\n\tprovide more information on where phones are directly\n\tconnected to an IP Office and further details on IP Phones for\n\ttheir identification.')
mibBuilder.exportSymbols("IPO-PHONES-MIB", ipoPhonesCompliance=ipoPhonesCompliance, ipoPhonesGroup=ipoPhonesGroup, ipoPhonesIPAddress=ipoPhonesIPAddress, ipoPhonesPortNumber=ipoPhonesPortNumber, ipoPhonesNotificationsGroup=ipoPhonesNotificationsGroup, ipoPhonesConformance=ipoPhonesConformance, ipoPhonesExtNumber=ipoPhonesExtNumber, ipoPhones2Group=ipoPhones2Group, ipoPhonesExtID=ipoPhonesExtID, ipoPhonesPhysAddress=ipoPhonesPhysAddress, PhoneType=PhoneType, ipoPhonesPort=ipoPhonesPort, ipoPhonesNumber=ipoPhonesNumber, ipoPhonesMibObjects=ipoPhonesMibObjects, ipoPhonesGroups=ipoPhonesGroups, ipoPhonesUserLong=ipoPhonesUserLong, ipoPhonesTable=ipoPhonesTable, ipoPhonesv2NotificationsGroup=ipoPhonesv2NotificationsGroup, ipoPhonesv3Compliance=ipoPhonesv3Compliance, ipoPhonesUserShort=ipoPhonesUserShort, ipoPhonesMIB=ipoPhonesMIB, ipoPhonesIndex=ipoPhonesIndex, ipoPhonesChangeSvcEvent=ipoPhonesChangeSvcEvent, ipoPhones=ipoPhones, ipoPhonesCompliances=ipoPhonesCompliances, ipoPhonesType=ipoPhonesType, ipoPhonesMibNotifications=ipoPhonesMibNotifications, ipoPhonesChangeEvent=ipoPhonesChangeEvent, ipoPhonesv2Compliance=ipoPhonesv2Compliance, ipoPhonesEntry=ipoPhonesEntry, ipoPhonesModuleNumber=ipoPhonesModuleNumber, PYSNMP_MODULE_ID=ipoPhonesMIB)
