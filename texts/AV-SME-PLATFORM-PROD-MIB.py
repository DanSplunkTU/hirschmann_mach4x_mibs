#
# PySNMP MIB module AV-SME-PLATFORM-PROD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/avaya/AV-SME-PLATFORM-PROD-MIB.mib
# Produced by pysmi-1.1.8 at Mon Feb  7 16:07:53 2022
# On host fv-az42-619 platform Linux version 5.11.0-1028-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
products, = mibBuilder.importSymbols("AVAYAGEN-MIB", "products")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, iso, TimeTicks, ObjectIdentity, Counter64, ModuleIdentity, Integer32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Counter32, IpAddress, Bits, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "iso", "TimeTicks", "ObjectIdentity", "Counter64", "ModuleIdentity", "Integer32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Counter32", "IpAddress", "Bits", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
avSMEPlatformProdMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 48))
avSMEPlatformProdMIB.setRevisions(('2014-05-30 12:00', '2014-04-03 12:00', '2013-01-23 16:00', '2012-11-29 12:00', '2012-05-10 12:35', '2012-04-09 10:25', '2012-03-05 10:05', '2011-12-16 13:30', '2011-12-14 15:35', '2011-12-07 14:10', '2011-05-03 13:30', '2011-03-30 09:22', '2010-07-07 13:50', '2010-07-06 13:45', '2010-07-02 15:06',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: avSMEPlatformProdMIB.setRevisionsDescriptions(('Rev 0.14.00\n         Added configuration 11, 12, 13 for IP Office Server Edition Primary,\n         IP Office Server Edition Secondary and\n         IP Office Server Edition Expansion System (L) Select Mode', 'Rev 0.13.00\n         Updated service vendor values\n         Added Contact Recorder service', 'Rev 0.12.00\n         Updated branding for configuration 1 and 10', 'Rev 0.11.00\n         Updated branding for configuration 1.\n         Added configuration 10.', 'Rev 0.10.00\n        Updated branding for configurations 7, 8 and 9.', 'Rev 0.09.00\n        Updated branding for configurations 7, 8 and 9.', 'Rev 0.08.00\n        Updated configurations 7, 8 and 9.', 'Rev 0.07.01\n        Updated configuration 6.', 'Rev 0.07.00\n        Added configuration 9, updated configurations 7 and 8.', 'Rev 0.06.00\n        Added configurations 7 and 8.', 'Rev 0.05.00\n        Added configuration 6.', 'Rev 0.04.00\n        Added configuration 4 and 5.', 'Rev 0.03.00\n        Simplified the structure.', 'Rev 0.02.00\n        Corrected base OID to one properly allocated in Avaya tree.', 'Rev 0.01.00\n        The first rough draft of this MIB module.',))
if mibBuilder.loadTexts: avSMEPlatformProdMIB.setLastUpdated('201405301200Z')
if mibBuilder.loadTexts: avSMEPlatformProdMIB.setOrganization('Avaya Inc.')
if mibBuilder.loadTexts: avSMEPlatformProdMIB.setContactInfo('Avaya Customer Services\n         Postal: Avaya, Inc.\n                 211 Mt Airy Rd.\n                 Basking Ridge, NJ 07920\n                 USA\n         Tel:    +1 908 953 6000\n\n         WWW:    http://www.avaya.com')
if mibBuilder.loadTexts: avSMEPlatformProdMIB.setDescription('Avaya IP Office Products OID tree.\n\n         This MIB module defines the product/sysObjectID values for\n         use with Avaya IP Office family of telephone switches.')
smepProdVariants = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 1, 48, 1))
smepProdServices = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 1, 48, 2))
smepProdPorts = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 1, 48, 3))
smepProdDongleModules = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 1, 48, 4))
smepCfg1 = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 48, 1, 1))
if mibBuilder.loadTexts: smepCfg1.setStatus('current')
if mibBuilder.loadTexts: smepCfg1.setDescription('The authoritative reference for Configuration 1\n\tof the SME Embedded Platform.\n        Configuration 1 = IP Office Application Server on Linux PC')
smepCfg2 = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 48, 1, 2))
if mibBuilder.loadTexts: smepCfg2.setStatus('current')
if mibBuilder.loadTexts: smepCfg2.setDescription('The authoritative reference for Configuration 2\n\tof the SME Embedded Platform.\n        Configuration 2 = IP Office on PC.')
smepCfg3 = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 48, 1, 3))
if mibBuilder.loadTexts: smepCfg3.setStatus('current')
if mibBuilder.loadTexts: smepCfg3.setDescription('The authoritative reference for Configuration 3\n\tof the SME Embedded Platform.\n        Configuration 3 = IP Office on HP ProCurve')
smepCfg4 = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 48, 1, 4))
if mibBuilder.loadTexts: smepCfg4.setStatus('current')
if mibBuilder.loadTexts: smepCfg4.setDescription('The authoritative reference for Configuration 4\n\tof the SME Embedded Platform.\n        Configuration 4 = IP Office on Dell')
smepCfg5 = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 48, 1, 5))
if mibBuilder.loadTexts: smepCfg5.setStatus('current')
if mibBuilder.loadTexts: smepCfg5.setDescription('The authoritative reference for Configuration 5\n\tof the SME Embedded Platform.\n        Configuration 5 = Branch installations')
smepCfg6 = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 48, 1, 6))
if mibBuilder.loadTexts: smepCfg6.setStatus('current')
if mibBuilder.loadTexts: smepCfg6.setDescription('The authoritative reference for Configuration 6\n\tof the SME Embedded Platform.\n        Configuration 6 = Standalone Voice Mail')
smepCfg7 = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 48, 1, 7))
if mibBuilder.loadTexts: smepCfg7.setStatus('current')
if mibBuilder.loadTexts: smepCfg7.setDescription('The authoritative reference for Configuration 7\n\tof the SME Embedded Platform.\n        Configuration 7 = IP Office Server Edition Primary')
smepCfg8 = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 48, 1, 8))
if mibBuilder.loadTexts: smepCfg8.setStatus('current')
if mibBuilder.loadTexts: smepCfg8.setDescription('The authoritative reference for Configuration 8\n\tof the SME Embedded Platform.\n        Configuration 8 = IP Office Server Edition Secondary')
smepCfg9 = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 48, 1, 9))
if mibBuilder.loadTexts: smepCfg9.setStatus('current')
if mibBuilder.loadTexts: smepCfg9.setDescription('The authoritative reference for Configuration 9\n\tof the SME Embedded Platform.\n        Configuration 9 = IP Office Server Edition Expansion System (L)')
smepCfg10 = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 48, 1, 10))
if mibBuilder.loadTexts: smepCfg10.setStatus('current')
if mibBuilder.loadTexts: smepCfg10.setDescription('The authoritative reference for Configuration 10\n        of the SME Embedded Platform.\n        Configuration 10 = IP Office Application Server on UCM')
smepCfg11 = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 48, 1, 11))
if mibBuilder.loadTexts: smepCfg11.setStatus('current')
if mibBuilder.loadTexts: smepCfg11.setDescription('The authoritative reference for Configuration 11\n        of the SME Embedded Platform.\n        Configuration 11 = IP Office Server Edition Primary Select Mode')
smepCfg12 = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 48, 1, 12))
if mibBuilder.loadTexts: smepCfg12.setStatus('current')
if mibBuilder.loadTexts: smepCfg12.setDescription('The authoritative reference for Configuration 12\n        of the SME Embedded Platform.\n        Configuration 12 = IP Office Server Edition Secondary Select Mode')
smepCfg13 = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 48, 1, 13))
if mibBuilder.loadTexts: smepCfg13.setStatus('current')
if mibBuilder.loadTexts: smepCfg13.setDescription('The authoritative reference for Configuration 13\n        of the SME Embedded Platform.\n        Configuration 13 = IP Office Server Edition Expansion System (L) Select Mode')
smepProdServiceOneXPortal = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 48, 2, 1))
if mibBuilder.loadTexts: smepProdServiceOneXPortal.setStatus('current')
if mibBuilder.loadTexts: smepProdServiceOneXPortal.setDescription('The authoritative reference for Avaya one-X Portal service\n         resident on Avaya IP Office on Linux server.')
smepProdServiceVoicemailPro = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 48, 2, 2))
if mibBuilder.loadTexts: smepProdServiceVoicemailPro.setStatus('current')
if mibBuilder.loadTexts: smepProdServiceVoicemailPro.setDescription('The authoritative reference for Avaya Voicemail Pro service\n        resident on Avaya IP Office on Linux server.')
smepProdServiceContactRecorder = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 48, 2, 3))
if mibBuilder.loadTexts: smepProdServiceContactRecorder.setStatus('current')
if mibBuilder.loadTexts: smepProdServiceContactRecorder.setDescription('The authoritative reference for Avaya Contact Recorder service\n        resident on Avaya IP Office on Linux server.')
smepProdPortLAN = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 48, 3, 1))
if mibBuilder.loadTexts: smepProdPortLAN.setStatus('current')
if mibBuilder.loadTexts: smepProdPortLAN.setDescription('The authoritative reference for Avaya IP Office LAN\n        (10BASE-T/100BASE-TX) Ports')
smepProdGenericDongle = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 48, 4, 1))
if mibBuilder.loadTexts: smepProdGenericDongle.setStatus('current')
if mibBuilder.loadTexts: smepProdGenericDongle.setDescription('The authoritative reference for the Avaya IP Office License\n        Dongle - A single representation for three dongle types,\n        Parallel, Serial and USB. The Parallel and USB ones not truly\n        connected directly to the IP Office but the managing PC.')
mibBuilder.exportSymbols("AV-SME-PLATFORM-PROD-MIB", smepProdDongleModules=smepProdDongleModules, smepCfg11=smepCfg11, smepCfg5=smepCfg5, smepCfg12=smepCfg12, smepProdServiceOneXPortal=smepProdServiceOneXPortal, smepCfg13=smepCfg13, smepCfg6=smepCfg6, smepCfg9=smepCfg9, smepCfg7=smepCfg7, smepProdVariants=smepProdVariants, smepCfg8=smepCfg8, smepProdPortLAN=smepProdPortLAN, smepProdPorts=smepProdPorts, smepCfg4=smepCfg4, PYSNMP_MODULE_ID=avSMEPlatformProdMIB, smepCfg2=smepCfg2, smepProdServiceContactRecorder=smepProdServiceContactRecorder, smepProdServices=smepProdServices, smepCfg3=smepCfg3, smepCfg10=smepCfg10, smepProdServiceVoicemailPro=smepProdServiceVoicemailPro, smepCfg1=smepCfg1, smepProdGenericDongle=smepProdGenericDongle, avSMEPlatformProdMIB=avSMEPlatformProdMIB)
