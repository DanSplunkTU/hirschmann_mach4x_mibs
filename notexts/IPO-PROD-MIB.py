#
# PySNMP MIB module IPO-PROD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/avaya/IPO-PROD-MIB.mib
# Produced by pysmi-1.1.3 at Sun Nov 28 20:15:33 2021
# On host fv-az77-612 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
products, = mibBuilder.importSymbols("AVAYAGEN-MIB", "products")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, Counter32, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, TimeTicks, ModuleIdentity, Integer32, Counter64, Bits, ObjectIdentity, NotificationType, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Counter32", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "TimeTicks", "ModuleIdentity", "Integer32", "Counter64", "Bits", "ObjectIdentity", "NotificationType", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ipoProdMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2))
ipoProdMIB.setRevisions(('2014-08-06 00:00', '2014-05-30 00:00', '2014-02-27 00:00', '2013-12-10 00:00', '2012-07-23 00:00', '2012-03-26 00:00', '2011-11-14 11:28', '2011-08-11 16:58', '2011-02-10 14:57', '2011-02-01 14:57', '2011-01-11 16:30', '2010-06-09 15:15', '2010-04-28 16:26', '2009-08-26 17:13', '2009-08-05 10:48', '2006-08-16 11:00', '2006-08-02 17:52', '2006-07-13 22:20', '2006-06-10 14:16', '2006-06-07 10:14', '2006-05-24 16:20', '2006-05-24 16:15', '2006-04-04 00:00', '2004-08-06 00:00', '2004-03-03 00:00', '2004-01-06 00:00', '2003-10-10 00:00',))
if mibBuilder.loadTexts: ipoProdMIB.setLastUpdated('201408060000Z')
if mibBuilder.loadTexts: ipoProdMIB.setOrganization('Avaya Inc.')
ipoProdControllers = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 1, 2, 1))
ipoProdExpModules = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 1, 2, 2))
ipoProdSlots = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 1, 2, 3))
ipoProdSlotModules = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 1, 2, 4))
ipoProdPorts = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 1, 2, 5))
ipoProdDongleModules = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 1, 2, 6))
ipoProdSubModules = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 1, 2, 7))
ipoProdUCModules = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 1, 2, 8))
ipoProd401Family = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 1, 2, 1, 1))
ipoProd403Family = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 1, 2, 1, 2))
ipoProd406Family = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 1, 2, 1, 3))
ipoProd412Family = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 1, 2, 1, 4))
ipoProdSmallOfficeEditionFamily = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 1, 2, 1, 5))
ipoProdR403Family = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 1, 2, 1, 6))
ipoProdR406Family = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 1, 2, 1, 7))
ipoProdSogFamily = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 1, 2, 1, 8))
ipoProd500Family = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 1, 2, 1, 9))
ipoProd500v2Family = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 1, 2, 1, 10))
ipoProd401DT2 = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 1, 1, 1))
if mibBuilder.loadTexts: ipoProd401DT2.setStatus('current')
ipoProd401DT4 = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 1, 1, 2))
if mibBuilder.loadTexts: ipoProd401DT4.setStatus('current')
ipoProd401DS2 = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 1, 1, 3))
if mibBuilder.loadTexts: ipoProd401DS2.setStatus('current')
ipoProd401DS4 = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 1, 1, 4))
if mibBuilder.loadTexts: ipoProd401DS4.setStatus('current')
ipoProd403DT = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 1, 2, 1))
if mibBuilder.loadTexts: ipoProd403DT.setStatus('current')
ipoProd403DS = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 1, 2, 2))
if mibBuilder.loadTexts: ipoProd403DS.setStatus('current')
ipoProd406 = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 1, 3, 1))
if mibBuilder.loadTexts: ipoProd406.setStatus('current')
ipoProd412 = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 1, 4, 1))
if mibBuilder.loadTexts: ipoProd412.setStatus('current')
ipoProdSmallOfficeEditionPOTS4 = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 1, 5, 1))
if mibBuilder.loadTexts: ipoProdSmallOfficeEditionPOTS4.setStatus('current')
ipoProdSmallOfficeEditionPOTS8 = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 1, 5, 2))
if mibBuilder.loadTexts: ipoProdSmallOfficeEditionPOTS8.setStatus('current')
ipoProdSmallOfficeEditionDT8 = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 1, 5, 3))
if mibBuilder.loadTexts: ipoProdSmallOfficeEditionDT8.setStatus('current')
ipoProdSmallOfficeEditionDS8 = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 1, 5, 4))
if mibBuilder.loadTexts: ipoProdSmallOfficeEditionDS8.setStatus('current')
ipoProdR403DT = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 1, 6, 1))
if mibBuilder.loadTexts: ipoProdR403DT.setStatus('current')
ipoProdR403DS = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 1, 6, 2))
if mibBuilder.loadTexts: ipoProdR403DS.setStatus('current')
ipoProdR406 = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 1, 7, 1))
if mibBuilder.loadTexts: ipoProdR406.setStatus('current')
ipoProdR406DT = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 1, 7, 2))
if mibBuilder.loadTexts: ipoProdR406DT.setStatus('current')
ipoProdR406DS = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 1, 7, 3))
if mibBuilder.loadTexts: ipoProdR406DS.setStatus('current')
ipoProdR406Full = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 1, 7, 4))
if mibBuilder.loadTexts: ipoProdR406Full.setStatus('current')
ipoProdSogSOEPOTS4 = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 1, 8, 1))
if mibBuilder.loadTexts: ipoProdSogSOEPOTS4.setStatus('current')
ipoProdSogSOEPOTS8 = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 1, 8, 2))
if mibBuilder.loadTexts: ipoProdSogSOEPOTS8.setStatus('current')
ipoProdSogSOEDT8 = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 1, 8, 3))
if mibBuilder.loadTexts: ipoProdSogSOEDT8.setStatus('current')
ipoProdSogSOEDS8 = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 1, 8, 4))
if mibBuilder.loadTexts: ipoProdSogSOEDS8.setStatus('current')
ipoProd500Slot4 = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 1, 9, 1))
if mibBuilder.loadTexts: ipoProd500Slot4.setStatus('current')
ipoProd500Slot8 = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 1, 9, 2))
if mibBuilder.loadTexts: ipoProd500Slot8.setStatus('current')
ipoProd500v2IPOffice = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 1, 10, 1))
if mibBuilder.loadTexts: ipoProd500v2IPOffice.setStatus('current')
ipoProd500v2Partner = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 1, 10, 2))
if mibBuilder.loadTexts: ipoProd500v2Partner.setStatus('current')
ipoProd500v2Norstar = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 1, 10, 3))
if mibBuilder.loadTexts: ipoProd500v2Norstar.setStatus('current')
ipoProd500v2Branch = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 1, 10, 4))
if mibBuilder.loadTexts: ipoProd500v2Branch.setStatus('current')
ipoProd500v2Quick = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 1, 10, 5))
if mibBuilder.loadTexts: ipoProd500v2Quick.setStatus('current')
ipoProd500v2SEditionExpansion = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 1, 10, 6))
if mibBuilder.loadTexts: ipoProd500v2SEditionExpansion.setStatus('current')
ipoProd500v2IPOfficeSelect = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 1, 10, 7))
if mibBuilder.loadTexts: ipoProd500v2IPOfficeSelect.setStatus('current')
ipoProd500v2SEditionExpansionSelect = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 1, 10, 8))
if mibBuilder.loadTexts: ipoProd500v2SEditionExpansionSelect.setStatus('current')
ipoProdExpModDT = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 1, 2, 2, 1))
ipoProdExpModDS = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 1, 2, 2, 2))
ipoProdExpModPhone = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 1, 2, 2, 3))
ipoProdExpModS0 = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 1, 2, 2, 4))
ipoProdExpModAnalog = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 1, 2, 2, 5))
ipoProdExpModWAN = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 1, 2, 2, 6))
ipoProdExpModRDS = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 1, 2, 2, 7))
ipoProdExpModRPhone = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 1, 2, 2, 8))
ipoProdExpModDSA = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 1, 2, 2, 9))
ipoProdExpModDT16 = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 2, 1, 1))
if mibBuilder.loadTexts: ipoProdExpModDT16.setStatus('current')
ipoProdExpModDT30 = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 2, 1, 2))
if mibBuilder.loadTexts: ipoProdExpModDT30.setStatus('current')
ipoProdExpModDS16 = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 2, 2, 1))
if mibBuilder.loadTexts: ipoProdExpModDS16.setStatus('current')
ipoProdExpModDS30 = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 2, 2, 2))
if mibBuilder.loadTexts: ipoProdExpModDS30.setStatus('current')
ipoProdExpModPhone8 = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 2, 3, 1))
if mibBuilder.loadTexts: ipoProdExpModPhone8.setStatus('current')
ipoProdExpModPhone16 = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 2, 3, 2))
if mibBuilder.loadTexts: ipoProdExpModPhone16.setStatus('current')
ipoProdExpModPhone30 = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 2, 3, 3))
if mibBuilder.loadTexts: ipoProdExpModPhone30.setStatus('current')
ipoProdExpModS08 = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 2, 4, 1))
if mibBuilder.loadTexts: ipoProdExpModS08.setStatus('current')
ipoProdExpModS016 = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 2, 4, 2))
if mibBuilder.loadTexts: ipoProdExpModS016.setStatus('current')
ipoProdExpModATM8 = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 2, 5, 1))
if mibBuilder.loadTexts: ipoProdExpModATM8.setStatus('current')
ipoProdExpModATM16 = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 2, 5, 2))
if mibBuilder.loadTexts: ipoProdExpModATM16.setStatus('current')
ipoProdExpModWAN3 = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 2, 6, 1))
if mibBuilder.loadTexts: ipoProdExpModWAN3.setStatus('current')
ipoProdExpModRDS16 = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 2, 7, 1))
if mibBuilder.loadTexts: ipoProdExpModRDS16.setStatus('current')
ipoProdExpModRDS30 = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 2, 7, 2))
if mibBuilder.loadTexts: ipoProdExpModRDS30.setStatus('current')
ipoProdExpModRPhone8 = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 2, 8, 1))
if mibBuilder.loadTexts: ipoProdExpModRPhone8.setStatus('current')
ipoProdExpModRPhone16 = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 2, 8, 2))
if mibBuilder.loadTexts: ipoProdExpModRPhone16.setStatus('current')
ipoProdExpModRPhone30 = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 2, 8, 3))
if mibBuilder.loadTexts: ipoProdExpModRPhone30.setStatus('current')
ipoProdExpModDSA16RJ21 = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 2, 9, 1))
if mibBuilder.loadTexts: ipoProdExpModDSA16RJ21.setStatus('current')
ipoProdExpModDSA30RJ21 = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 2, 9, 2))
if mibBuilder.loadTexts: ipoProdExpModDSA30RJ21.setStatus('current')
ipoProdExpModDSA16RJ45 = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 2, 9, 3))
if mibBuilder.loadTexts: ipoProdExpModDSA16RJ45.setStatus('current')
ipoProdExpModDSA30RJ45 = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 2, 9, 4))
if mibBuilder.loadTexts: ipoProdExpModDSA30RJ45.setStatus('current')
ipoProdSlotVCM = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 3, 1))
if mibBuilder.loadTexts: ipoProdSlotVCM.setStatus('current')
ipoProdSlotModems = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 3, 2))
if mibBuilder.loadTexts: ipoProdSlotModems.setStatus('current')
ipoProdSlotVmailMemory = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 3, 3))
if mibBuilder.loadTexts: ipoProdSlotVmailMemory.setStatus('current')
ipoProdSlotWAN = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 3, 4))
if mibBuilder.loadTexts: ipoProdSlotWAN.setStatus('current')
ipoProdSlotPCCard = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 3, 5))
if mibBuilder.loadTexts: ipoProdSlotPCCard.setStatus('current')
ipoProdSlotTrunks = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 3, 6))
if mibBuilder.loadTexts: ipoProdSlotTrunks.setStatus('current')
ipoProdSlotExpansion = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 3, 7))
if mibBuilder.loadTexts: ipoProdSlotExpansion.setStatus('current')
ipoProdSlot500Generic = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 3, 8))
if mibBuilder.loadTexts: ipoProdSlot500Generic.setStatus('current')
ipoProdSlotMezzanine = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 3, 9))
if mibBuilder.loadTexts: ipoProdSlotMezzanine.setStatus('current')
ipoProdSlotCarrierVCM = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 3, 10))
if mibBuilder.loadTexts: ipoProdSlotCarrierVCM.setStatus('current')
ipoProdSlotCarrierTrunk = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 3, 11))
if mibBuilder.loadTexts: ipoProdSlotCarrierTrunk.setStatus('current')
ipoProdIntegralModules = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 1))
ipoProdTrunkModules = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 2))
ipoProdPCCardModules = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 3))
ipoProdCarrierModules = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 4))
ipoProdPhonePortModules = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 5))
ipoProdVCMModules = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 6))
ipoProdExpansionModules = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 7))
ipoProdUCPModules = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 8))
ipoProdIntModVCM = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 1, 1))
ipoProdIntModModem = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 1, 2))
ipoProdIntModWAN = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 1, 3))
ipoProdIntModMem = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 1, 4))
ipoProdIntModVCM3 = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 1, 1, 1))
if mibBuilder.loadTexts: ipoProdIntModVCM3.setStatus('current')
ipoProdIntModVCM5 = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 1, 1, 2))
if mibBuilder.loadTexts: ipoProdIntModVCM5.setStatus('current')
ipoProdIntModVCM6 = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 1, 1, 3))
if mibBuilder.loadTexts: ipoProdIntModVCM6.setStatus('current')
ipoProdIntModVCM8 = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 1, 1, 4))
if mibBuilder.loadTexts: ipoProdIntModVCM8.setStatus('current')
ipoProdIntModVCM10 = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 1, 1, 5))
if mibBuilder.loadTexts: ipoProdIntModVCM10.setStatus('current')
ipoProdIntModVCM12 = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 1, 1, 6))
if mibBuilder.loadTexts: ipoProdIntModVCM12.setStatus('current')
ipoProdIntModVCM16 = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 1, 1, 7))
if mibBuilder.loadTexts: ipoProdIntModVCM16.setStatus('current')
ipoProdIntModVCM20 = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 1, 1, 8))
if mibBuilder.loadTexts: ipoProdIntModVCM20.setStatus('current')
ipoProdIntModVCM30 = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 1, 1, 9))
if mibBuilder.loadTexts: ipoProdIntModVCM30.setStatus('current')
ipoProdIntModVCM24 = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 1, 1, 10))
if mibBuilder.loadTexts: ipoProdIntModVCM24.setStatus('current')
ipoProdIntModVCM4 = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 1, 1, 11))
if mibBuilder.loadTexts: ipoProdIntModVCM4.setStatus('current')
ipoProdIntModModemDual = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 1, 2, 1))
if mibBuilder.loadTexts: ipoProdIntModModemDual.setStatus('current')
ipoProdIntModModemMulti = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 1, 2, 2))
if mibBuilder.loadTexts: ipoProdIntModModemMulti.setStatus('current')
ipoProdIntModWANModule = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 1, 3, 1))
if mibBuilder.loadTexts: ipoProdIntModWANModule.setStatus('current')
ipoProdIntModMemVmail = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 1, 4, 1))
if mibBuilder.loadTexts: ipoProdIntModMemVmail.setStatus('current')
ipoProdTrunkAnalogQuad = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 2, 1))
if mibBuilder.loadTexts: ipoProdTrunkAnalogQuad.setStatus('current')
ipoProdTrunkBRIQuad = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 2, 2))
if mibBuilder.loadTexts: ipoProdTrunkBRIQuad.setStatus('current')
ipoProdTrunkE1PRISingle = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 2, 3))
if mibBuilder.loadTexts: ipoProdTrunkE1PRISingle.setStatus('current')
ipoProdTrunkE1PRIDual = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 2, 4))
if mibBuilder.loadTexts: ipoProdTrunkE1PRIDual.setStatus('current')
ipoProdTrunkJ1PRISingle = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 2, 5))
if mibBuilder.loadTexts: ipoProdTrunkJ1PRISingle.setStatus('current')
ipoProdTrunkJ1PRIDual = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 2, 6))
if mibBuilder.loadTexts: ipoProdTrunkJ1PRIDual.setStatus('current')
ipoProdTrunkT1PRISingle = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 2, 7))
if mibBuilder.loadTexts: ipoProdTrunkT1PRISingle.setStatus('current')
ipoProdTrunkT1PRIDual = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 2, 8))
if mibBuilder.loadTexts: ipoProdTrunkT1PRIDual.setStatus('current')
ipoProdTrunkIndex = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 2, 9))
if mibBuilder.loadTexts: ipoProdTrunkIndex.setStatus('current')
ipoProdTrunkR2Single = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 2, 10))
if mibBuilder.loadTexts: ipoProdTrunkR2Single.setStatus('current')
ipoProdTrunkR2Dual = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 2, 11))
if mibBuilder.loadTexts: ipoProdTrunkR2Dual.setStatus('current')
ipoProdTrunkR2CoAxSingle = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 2, 12))
if mibBuilder.loadTexts: ipoProdTrunkR2CoAxSingle.setStatus('current')
ipoProdTrunkR2CoAxDual = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 2, 13))
if mibBuilder.loadTexts: ipoProdTrunkR2CoAxDual.setStatus('current')
ipoProdTrunkRAnalogQuad = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 2, 14))
if mibBuilder.loadTexts: ipoProdTrunkRAnalogQuad.setStatus('current')
ipoProdTrunk500AnalogQuad = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 2, 15))
if mibBuilder.loadTexts: ipoProdTrunk500AnalogQuad.setStatus('current')
ipoProdTrunk500BRIDual = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 2, 16))
if mibBuilder.loadTexts: ipoProdTrunk500BRIDual.setStatus('current')
ipoProdTrunk500BRIQuad = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 2, 17))
if mibBuilder.loadTexts: ipoProdTrunk500BRIQuad.setStatus('current')
ipoProdTrunkUniversalPRIDS0Single = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 2, 18))
if mibBuilder.loadTexts: ipoProdTrunkUniversalPRIDS0Single.setStatus('current')
ipoProdTrunkUniversalPRIDS0Dual = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 2, 19))
if mibBuilder.loadTexts: ipoProdTrunkUniversalPRIDS0Dual.setStatus('current')
ipoProdTrunk500AnalogQuadV2 = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 2, 20))
if mibBuilder.loadTexts: ipoProdTrunk500AnalogQuadV2.setStatus('current')
ipoProdPCCardMemVmail = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 3, 1))
if mibBuilder.loadTexts: ipoProdPCCardMemVmail.setStatus('current')
ipoProdPCCardWLAN = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 3, 2))
if mibBuilder.loadTexts: ipoProdPCCardWLAN.setStatus('current')
ipoProdCarrier = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 4, 1))
if mibBuilder.loadTexts: ipoProdCarrier.setStatus('current')
ipoProdPhonePortPOT8 = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 5, 1))
if mibBuilder.loadTexts: ipoProdPhonePortPOT8.setStatus('current')
ipoProdPhonePortDS8 = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 5, 2))
if mibBuilder.loadTexts: ipoProdPhonePortDS8.setStatus('current')
ipoProdPhonePortPOT2 = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 5, 3))
if mibBuilder.loadTexts: ipoProdPhonePortPOT2.setStatus('current')
ipoProdPhonePortCombo = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 5, 4))
if mibBuilder.loadTexts: ipoProdPhonePortCombo.setStatus('current')
ipoProdPhonePortETR6 = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 5, 5))
if mibBuilder.loadTexts: ipoProdPhonePortETR6.setStatus('current')
ipoProdPhonePortTCM8 = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 5, 6))
if mibBuilder.loadTexts: ipoProdPhonePortTCM8.setStatus('current')
ipoProdVCMMod32 = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 6, 1))
if mibBuilder.loadTexts: ipoProdVCMMod32.setStatus('current')
ipoProdVCMMod64 = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 6, 2))
if mibBuilder.loadTexts: ipoProdVCMMod64.setStatus('current')
ipoProdVCMMod32V2 = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 6, 3))
if mibBuilder.loadTexts: ipoProdVCMMod32V2.setStatus('current')
ipoProdVCMMod64V2 = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 6, 4))
if mibBuilder.loadTexts: ipoProdVCMMod64V2.setStatus('current')
ipoProdExpMod4Port = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 7, 1))
if mibBuilder.loadTexts: ipoProdExpMod4Port.setStatus('current')
ipoProdPortBRI = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 5, 1))
if mibBuilder.loadTexts: ipoProdPortBRI.setStatus('current')
ipoProdPortE1PRI = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 5, 2))
if mibBuilder.loadTexts: ipoProdPortE1PRI.setStatus('current')
ipoProdPortJ1PRI = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 5, 3))
if mibBuilder.loadTexts: ipoProdPortJ1PRI.setStatus('current')
ipoProdPortT1PRI = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 5, 4))
if mibBuilder.loadTexts: ipoProdPortT1PRI.setStatus('current')
ipoProdPortR2 = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 5, 5))
if mibBuilder.loadTexts: ipoProdPortR2.setStatus('current')
ipoProdPortR2CoAx = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 5, 6))
if mibBuilder.loadTexts: ipoProdPortR2CoAx.setStatus('current')
ipoProdPortWAN = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 5, 7))
if mibBuilder.loadTexts: ipoProdPortWAN.setStatus('current')
ipoProdPortAnalog = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 5, 8))
if mibBuilder.loadTexts: ipoProdPortAnalog.setStatus('current')
ipoProdPortPower = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 5, 9))
if mibBuilder.loadTexts: ipoProdPortPower.setStatus('current')
ipoProdPortDT = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 5, 10))
if mibBuilder.loadTexts: ipoProdPortDT.setStatus('current')
ipoProdPortDS = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 5, 11))
if mibBuilder.loadTexts: ipoProdPortDS.setStatus('current')
ipoProdPortPOT = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 5, 12))
if mibBuilder.loadTexts: ipoProdPortPOT.setStatus('current')
ipoProdPortS0 = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 5, 13))
if mibBuilder.loadTexts: ipoProdPortS0.setStatus('current')
ipoProdPortLAN = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 5, 14))
if mibBuilder.loadTexts: ipoProdPortLAN.setStatus('current')
ipoProdPortWLAN = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 5, 15))
if mibBuilder.loadTexts: ipoProdPortWLAN.setStatus('current')
ipoProdPortDTE = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 5, 16))
if mibBuilder.loadTexts: ipoProdPortDTE.setStatus('current')
ipoProdPortUSB = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 5, 17))
if mibBuilder.loadTexts: ipoProdPortUSB.setStatus('current')
ipoProdPortAudio = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 5, 18))
if mibBuilder.loadTexts: ipoProdPortAudio.setStatus('current')
ipoProdPortEtherWANLink = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 5, 19))
if mibBuilder.loadTexts: ipoProdPortEtherWANLink.setStatus('current')
ipoProdPortExtOP = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 5, 20))
if mibBuilder.loadTexts: ipoProdPortExtOP.setStatus('current')
ipoProdPortNet1 = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 5, 21))
if mibBuilder.loadTexts: ipoProdPortNet1.setStatus('current')
ipoProdPortNet2 = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 5, 22))
if mibBuilder.loadTexts: ipoProdPortNet2.setStatus('current')
ipoProdGenericDongle = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 6, 1))
if mibBuilder.loadTexts: ipoProdGenericDongle.setStatus('current')
ipoProdSubModVCM10 = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 7, 1))
if mibBuilder.loadTexts: ipoProdSubModVCM10.setStatus('current')
ipoProdC110UCM = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 8, 1))
if mibBuilder.loadTexts: ipoProdC110UCM.setStatus('current')
ipoProdC110UCMV2 = ObjectIdentity((1, 3, 6, 1, 4, 1, 6889, 1, 2, 8, 2))
if mibBuilder.loadTexts: ipoProdC110UCMV2.setStatus('current')
mibBuilder.exportSymbols("IPO-PROD-MIB", ipoProdExpModDT16=ipoProdExpModDT16, ipoProdExpModDSA16RJ45=ipoProdExpModDSA16RJ45, ipoProdPortAnalog=ipoProdPortAnalog, ipoProdGenericDongle=ipoProdGenericDongle, ipoProdSlotVCM=ipoProdSlotVCM, ipoProdPhonePortModules=ipoProdPhonePortModules, ipoProdExpModRDS=ipoProdExpModRDS, ipoProdPCCardMemVmail=ipoProdPCCardMemVmail, ipoProdSmallOfficeEditionDT8=ipoProdSmallOfficeEditionDT8, ipoProdExpModRPhone=ipoProdExpModRPhone, ipoProdPortS0=ipoProdPortS0, ipoProdUCModules=ipoProdUCModules, ipoProdSmallOfficeEditionFamily=ipoProdSmallOfficeEditionFamily, ipoProdSogSOEPOTS4=ipoProdSogSOEPOTS4, ipoProdSogSOEDS8=ipoProdSogSOEDS8, ipoProdSogFamily=ipoProdSogFamily, ipoProdTrunkUniversalPRIDS0Dual=ipoProdTrunkUniversalPRIDS0Dual, ipoProdSmallOfficeEditionPOTS4=ipoProdSmallOfficeEditionPOTS4, ipoProdR403DS=ipoProdR403DS, ipoProdPortE1PRI=ipoProdPortE1PRI, ipoProdTrunkUniversalPRIDS0Single=ipoProdTrunkUniversalPRIDS0Single, ipoProdPortExtOP=ipoProdPortExtOP, ipoProdIntModVCM30=ipoProdIntModVCM30, ipoProdExpModWAN=ipoProdExpModWAN, ipoProd406=ipoProd406, ipoProdExpModDT30=ipoProdExpModDT30, ipoProdIntModVCM3=ipoProdIntModVCM3, ipoProdSogSOEDT8=ipoProdSogSOEDT8, ipoProd500v2Norstar=ipoProd500v2Norstar, ipoProdIntModVCM5=ipoProdIntModVCM5, ipoProdControllers=ipoProdControllers, ipoProdPortPower=ipoProdPortPower, ipoProdExpModPhone=ipoProdExpModPhone, ipoProd412=ipoProd412, ipoProdExpansionModules=ipoProdExpansionModules, ipoProdPortEtherWANLink=ipoProdPortEtherWANLink, ipoProd412Family=ipoProd412Family, ipoProdTrunkR2Dual=ipoProdTrunkR2Dual, ipoProdR403Family=ipoProdR403Family, ipoProdPhonePortDS8=ipoProdPhonePortDS8, ipoProdPhonePortPOT8=ipoProdPhonePortPOT8, ipoProd403DS=ipoProd403DS, ipoProdTrunkT1PRIDual=ipoProdTrunkT1PRIDual, ipoProdTrunkIndex=ipoProdTrunkIndex, ipoProdVCMMod32V2=ipoProdVCMMod32V2, ipoProdSlotWAN=ipoProdSlotWAN, ipoProdPortWLAN=ipoProdPortWLAN, ipoProdPortDS=ipoProdPortDS, ipoProd500v2SEditionExpansionSelect=ipoProd500v2SEditionExpansionSelect, ipoProdSubModVCM10=ipoProdSubModVCM10, ipoProdPhonePortPOT2=ipoProdPhonePortPOT2, ipoProdTrunkModules=ipoProdTrunkModules, ipoProdVCMMod64=ipoProdVCMMod64, ipoProdPortJ1PRI=ipoProdPortJ1PRI, ipoProdTrunkE1PRISingle=ipoProdTrunkE1PRISingle, ipoProdExpModS016=ipoProdExpModS016, ipoProdTrunkR2CoAxDual=ipoProdTrunkR2CoAxDual, ipoProdR406DS=ipoProdR406DS, ipoProdPortR2=ipoProdPortR2, ipoProdPortWAN=ipoProdPortWAN, ipoProdExpModDSA30RJ45=ipoProdExpModDSA30RJ45, ipoProdPortR2CoAx=ipoProdPortR2CoAx, ipoProdPCCardModules=ipoProdPCCardModules, ipoProdPhonePortTCM8=ipoProdPhonePortTCM8, ipoProdSlotPCCard=ipoProdSlotPCCard, ipoProdSlotModems=ipoProdSlotModems, ipoProd500Slot4=ipoProd500Slot4, ipoProdTrunkE1PRIDual=ipoProdTrunkE1PRIDual, ipoProdIntModWANModule=ipoProdIntModWANModule, ipoProdTrunkJ1PRIDual=ipoProdTrunkJ1PRIDual, ipoProdTrunkR2CoAxSingle=ipoProdTrunkR2CoAxSingle, ipoProdTrunk500BRIDual=ipoProdTrunk500BRIDual, ipoProdTrunk500AnalogQuad=ipoProdTrunk500AnalogQuad, ipoProdTrunkJ1PRISingle=ipoProdTrunkJ1PRISingle, ipoProdSmallOfficeEditionDS8=ipoProdSmallOfficeEditionDS8, ipoProdIntModModemDual=ipoProdIntModModemDual, ipoProdIntModMemVmail=ipoProdIntModMemVmail, ipoProdCarrier=ipoProdCarrier, ipoProdExpModules=ipoProdExpModules, ipoProdPortUSB=ipoProdPortUSB, ipoProdIntegralModules=ipoProdIntegralModules, ipoProdIntModVCM20=ipoProdIntModVCM20, ipoProdTrunkT1PRISingle=ipoProdTrunkT1PRISingle, ipoProdExpModS0=ipoProdExpModS0, ipoProd401DS4=ipoProd401DS4, ipoProdPortNet2=ipoProdPortNet2, ipoProdExpModWAN3=ipoProdExpModWAN3, ipoProdPortDTE=ipoProdPortDTE, ipoProdR406Full=ipoProdR406Full, ipoProd500v2Partner=ipoProd500v2Partner, ipoProdPortBRI=ipoProdPortBRI, ipoProdIntModModemMulti=ipoProdIntModModemMulti, ipoProdVCMMod64V2=ipoProdVCMMod64V2, ipoProd500Slot8=ipoProd500Slot8, ipoProdExpModATM8=ipoProdExpModATM8, ipoProd500v2SEditionExpansion=ipoProd500v2SEditionExpansion, ipoProdR406=ipoProdR406, ipoProdTrunkBRIQuad=ipoProdTrunkBRIQuad, ipoProdSlotExpansion=ipoProdSlotExpansion, ipoProdPortNet1=ipoProdPortNet1, ipoProd500v2Quick=ipoProd500v2Quick, ipoProdIntModVCM4=ipoProdIntModVCM4, ipoProd401DT2=ipoProd401DT2, ipoProd406Family=ipoProd406Family, ipoProdTrunk500AnalogQuadV2=ipoProdTrunk500AnalogQuadV2, ipoProdExpModRDS16=ipoProdExpModRDS16, ipoProdPhonePortETR6=ipoProdPhonePortETR6, ipoProdTrunkRAnalogQuad=ipoProdTrunkRAnalogQuad, ipoProdPortDT=ipoProdPortDT, ipoProdSlots=ipoProdSlots, ipoProdIntModVCM24=ipoProdIntModVCM24, ipoProdExpModDT=ipoProdExpModDT, ipoProdExpModPhone8=ipoProdExpModPhone8, ipoProdTrunkR2Single=ipoProdTrunkR2Single, ipoProdExpModRDS30=ipoProdExpModRDS30, ipoProdExpModDSA16RJ21=ipoProdExpModDSA16RJ21, ipoProdExpModRPhone8=ipoProdExpModRPhone8, ipoProdExpModDSA30RJ21=ipoProdExpModDSA30RJ21, ipoProdSlotMezzanine=ipoProdSlotMezzanine, ipoProdCarrierModules=ipoProdCarrierModules, ipoProdTrunk500BRIQuad=ipoProdTrunk500BRIQuad, ipoProdPCCardWLAN=ipoProdPCCardWLAN, ipoProdIntModWAN=ipoProdIntModWAN, ipoProdPortPOT=ipoProdPortPOT, ipoProdR406DT=ipoProdR406DT, ipoProd500v2IPOffice=ipoProd500v2IPOffice, ipoProdIntModVCM8=ipoProdIntModVCM8, ipoProdExpModAnalog=ipoProdExpModAnalog, ipoProd500Family=ipoProd500Family, ipoProdUCPModules=ipoProdUCPModules, ipoProdExpMod4Port=ipoProdExpMod4Port, ipoProdSlotCarrierTrunk=ipoProdSlotCarrierTrunk, ipoProdExpModS08=ipoProdExpModS08, ipoProdMIB=ipoProdMIB, PYSNMP_MODULE_ID=ipoProdMIB, ipoProdPorts=ipoProdPorts, ipoProdR406Family=ipoProdR406Family, ipoProdExpModDS16=ipoProdExpModDS16, ipoProdExpModPhone16=ipoProdExpModPhone16, ipoProdSogSOEPOTS8=ipoProdSogSOEPOTS8, ipoProdSlot500Generic=ipoProdSlot500Generic, ipoProdTrunkAnalogQuad=ipoProdTrunkAnalogQuad, ipoProd403Family=ipoProd403Family, ipoProdExpModPhone30=ipoProdExpModPhone30, ipoProdSlotCarrierVCM=ipoProdSlotCarrierVCM, ipoProdIntModVCM16=ipoProdIntModVCM16, ipoProdVCMModules=ipoProdVCMModules, ipoProdSmallOfficeEditionPOTS8=ipoProdSmallOfficeEditionPOTS8, ipoProd401Family=ipoProd401Family, ipoProdExpModDSA=ipoProdExpModDSA, ipoProdVCMMod32=ipoProdVCMMod32, ipoProdC110UCM=ipoProdC110UCM, ipoProdIntModVCM=ipoProdIntModVCM, ipoProd500v2Branch=ipoProd500v2Branch, ipoProd401DS2=ipoProd401DS2, ipoProd401DT4=ipoProd401DT4, ipoProdIntModVCM10=ipoProdIntModVCM10, ipoProdSlotModules=ipoProdSlotModules, ipoProdExpModRPhone16=ipoProdExpModRPhone16, ipoProdC110UCMV2=ipoProdC110UCMV2, ipoProdExpModDS30=ipoProdExpModDS30, ipoProdPortT1PRI=ipoProdPortT1PRI, ipoProdExpModATM16=ipoProdExpModATM16, ipoProd500v2Family=ipoProd500v2Family, ipoProdSlotTrunks=ipoProdSlotTrunks, ipoProdIntModModem=ipoProdIntModModem, ipoProdIntModMem=ipoProdIntModMem, ipoProdIntModVCM6=ipoProdIntModVCM6, ipoProdIntModVCM12=ipoProdIntModVCM12, ipoProdPortLAN=ipoProdPortLAN, ipoProdSubModules=ipoProdSubModules, ipoProd403DT=ipoProd403DT, ipoProdSlotVmailMemory=ipoProdSlotVmailMemory, ipoProd500v2IPOfficeSelect=ipoProd500v2IPOfficeSelect, ipoProdExpModDS=ipoProdExpModDS, ipoProdPhonePortCombo=ipoProdPhonePortCombo, ipoProdPortAudio=ipoProdPortAudio, ipoProdDongleModules=ipoProdDongleModules, ipoProdExpModRPhone30=ipoProdExpModRPhone30, ipoProdR403DT=ipoProdR403DT)
