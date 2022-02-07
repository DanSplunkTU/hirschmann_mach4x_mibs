#
# PySNMP MIB module AV-SME-PLATFORM-PROD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/avaya/AV-SME-PLATFORM-PROD-MIB.mib
# Produced by pysmi-1.1.8 at Mon Feb  7 16:07:52 2022
# On host fv-az42-619 platform Linux version 5.11.0-1028-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
products, = mibBuilder.importSymbols("AVAYAGEN-MIB", "products")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, MibIdentifier, TimeTicks, Unsigned32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Counter32, Counter64, NotificationType, Integer32, ObjectIdentity, Gauge32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "MibIdentifier", "TimeTicks", "Unsigned32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Counter32", "Counter64", "NotificationType", "Integer32", "ObjectIdentity", "Gauge32", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
avSMEPlatformProdMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 48))
avSMEPlatformProdMIB.setRevisions(('2014-05-30 12:00', '2014-04-03 12:00', '2013-01-23 16:00', '2012-11-29 12:00', '2012-05-10 12:35', '2012-04-09 10:25', '2012-03-05 10:05', '2011-12-16 13:30', '2011-12-14 15:35', '2011-12-07 14:10', '2011-05-03 13:30', '2011-03-30 09:22', '2010-07-07 13:50', '2010-07-06 13:45', '2010-07-02 15:06',))
if mibBuilder.loadTexts: avSMEPlatformProdMIB.setLastUpdated('201405301200Z')
if mibBuilder.loadTexts: avSMEPlatformProdMIB.setOrganization('Avaya Inc.')
smepProdVariants = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 1, 48, 1))
smepProdServices = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 1, 48, 2))
smepProdPorts = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 1, 48, 3))
smepProdDongleModules = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 1, 48, 4))
smepCfg1 = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 48, 1, 1))
if mibBuilder.loadTexts: smepCfg1.setStatus('current')
smepCfg2 = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 48, 1, 2))
if mibBuilder.loadTexts: smepCfg2.setStatus('current')
smepCfg3 = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 48, 1, 3))
if mibBuilder.loadTexts: smepCfg3.setStatus('current')
smepCfg4 = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 48, 1, 4))
if mibBuilder.loadTexts: smepCfg4.setStatus('current')
smepCfg5 = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 48, 1, 5))
if mibBuilder.loadTexts: smepCfg5.setStatus('current')
smepCfg6 = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 48, 1, 6))
if mibBuilder.loadTexts: smepCfg6.setStatus('current')
smepCfg7 = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 48, 1, 7))
if mibBuilder.loadTexts: smepCfg7.setStatus('current')
smepCfg8 = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 48, 1, 8))
if mibBuilder.loadTexts: smepCfg8.setStatus('current')
smepCfg9 = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 48, 1, 9))
if mibBuilder.loadTexts: smepCfg9.setStatus('current')
smepCfg10 = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 48, 1, 10))
if mibBuilder.loadTexts: smepCfg10.setStatus('current')
smepCfg11 = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 48, 1, 11))
if mibBuilder.loadTexts: smepCfg11.setStatus('current')
smepCfg12 = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 48, 1, 12))
if mibBuilder.loadTexts: smepCfg12.setStatus('current')
smepCfg13 = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 48, 1, 13))
if mibBuilder.loadTexts: smepCfg13.setStatus('current')
smepProdServiceOneXPortal = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 48, 2, 1))
if mibBuilder.loadTexts: smepProdServiceOneXPortal.setStatus('current')
smepProdServiceVoicemailPro = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 48, 2, 2))
if mibBuilder.loadTexts: smepProdServiceVoicemailPro.setStatus('current')
smepProdServiceContactRecorder = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 48, 2, 3))
if mibBuilder.loadTexts: smepProdServiceContactRecorder.setStatus('current')
smepProdPortLAN = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 48, 3, 1))
if mibBuilder.loadTexts: smepProdPortLAN.setStatus('current')
smepProdGenericDongle = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 48, 4, 1))
if mibBuilder.loadTexts: smepProdGenericDongle.setStatus('current')
mibBuilder.exportSymbols("AV-SME-PLATFORM-PROD-MIB", smepProdServiceVoicemailPro=smepProdServiceVoicemailPro, smepCfg11=smepCfg11, smepCfg7=smepCfg7, smepCfg1=smepCfg1, smepProdDongleModules=smepProdDongleModules, smepCfg6=smepCfg6, smepProdServiceContactRecorder=smepProdServiceContactRecorder, smepProdVariants=smepProdVariants, smepCfg2=smepCfg2, smepCfg8=smepCfg8, PYSNMP_MODULE_ID=avSMEPlatformProdMIB, smepCfg10=smepCfg10, smepCfg4=smepCfg4, smepProdPortLAN=smepProdPortLAN, smepCfg12=smepCfg12, smepCfg3=smepCfg3, smepProdServices=smepProdServices, avSMEPlatformProdMIB=avSMEPlatformProdMIB, smepProdServiceOneXPortal=smepProdServiceOneXPortal, smepCfg13=smepCfg13, smepProdPorts=smepProdPorts, smepProdGenericDongle=smepProdGenericDongle, smepCfg5=smepCfg5, smepCfg9=smepCfg9)
