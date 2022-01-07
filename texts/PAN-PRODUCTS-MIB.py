#
# PySNMP MIB module PAN-PRODUCTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/paloaltonetworks/PAN-PRODUCT-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:33:55 2022
# On host fv-az36-988 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
panProductsMibs, panModules = mibBuilder.importSymbols("PAN-GLOBAL-REG", "panProductsMibs", "panModules")
TcChassisType, = mibBuilder.importSymbols("PAN-GLOBAL-TC", "TcChassisType")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Unsigned32, iso, Counter64, MibIdentifier, ObjectIdentity, Bits, Integer32, TimeTicks, NotificationType, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Unsigned32", "iso", "Counter64", "MibIdentifier", "ObjectIdentity", "Bits", "Integer32", "TimeTicks", "NotificationType", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "IpAddress")
TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString")
panProductsMibsModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 25461, 1, 1, 4))
panProductsMibsModule.setRevisions(('2013-04-15 16:50', '2011-02-09 16:10',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: panProductsMibsModule.setRevisionsDescriptions(('\n\t\t\tRev 2.0\n\t\t\tUpdated with PA-7000, GP-100 and WF-500 products.', '\n\t\t\tRev 1.0\n\t\t\tInitial version of MIB module PAN-PRODUCTS-MIB.',))
if mibBuilder.loadTexts: panProductsMibsModule.setLastUpdated('201304151650Z')
if mibBuilder.loadTexts: panProductsMibsModule.setOrganization('Palo Alto Networks')
if mibBuilder.loadTexts: panProductsMibsModule.setContactInfo('\n\t\t\t\t\tCustomer Support\n\t\t\t\t\tPalo Alto Networks\n\t\t\t\t\t4401 Great America Pkwy\n\t\t\t\t\tSanta Clara, CA 95054-1211\n\n\t\t\t\t\t+1 866-898-9087\n\t\t\t\t\tsupport at paloaltonetworks dot com')
if mibBuilder.loadTexts: panProductsMibsModule.setDescription("\n\t\t\tA MIB module containing definitions of managed objects\n\t\t\timplemented by specific Palo Alto Networks' products.")
panPA_4050 = ObjectIdentity((1, 3, 6, 1, 4, 1, 25461, 2, 3, 1)).setLabel("panPA-4050")
if mibBuilder.loadTexts: panPA_4050.setStatus('current')
if mibBuilder.loadTexts: panPA_4050.setDescription('\n\t\t\tSub-tree for PA-4050 specific objects.')
panPA_4020 = ObjectIdentity((1, 3, 6, 1, 4, 1, 25461, 2, 3, 2)).setLabel("panPA-4020")
if mibBuilder.loadTexts: panPA_4020.setStatus('current')
if mibBuilder.loadTexts: panPA_4020.setDescription('\n\t\t\tSub-tree for PA-4020 specific objects.')
panPA_2050 = ObjectIdentity((1, 3, 6, 1, 4, 1, 25461, 2, 3, 3)).setLabel("panPA-2050")
if mibBuilder.loadTexts: panPA_2050.setStatus('current')
if mibBuilder.loadTexts: panPA_2050.setDescription('\n\t\t\tSub-tree for PA-2050 specific objects.')
panPA_2020 = ObjectIdentity((1, 3, 6, 1, 4, 1, 25461, 2, 3, 4)).setLabel("panPA-2020")
if mibBuilder.loadTexts: panPA_2020.setStatus('current')
if mibBuilder.loadTexts: panPA_2020.setDescription('\n\t\t\tSub-tree for PA-2020 specific objects.')
panPA_4060 = ObjectIdentity((1, 3, 6, 1, 4, 1, 25461, 2, 3, 5)).setLabel("panPA-4060")
if mibBuilder.loadTexts: panPA_4060.setStatus('current')
if mibBuilder.loadTexts: panPA_4060.setDescription('\n\t\t\tSub-tree for PA-4060 specific objects.')
panPA_500 = ObjectIdentity((1, 3, 6, 1, 4, 1, 25461, 2, 3, 6)).setLabel("panPA-500")
if mibBuilder.loadTexts: panPA_500.setStatus('current')
if mibBuilder.loadTexts: panPA_500.setDescription('\n\t\t\tSub-tree for PA-500 specific objects.')
panPanorama = ObjectIdentity((1, 3, 6, 1, 4, 1, 25461, 2, 3, 7))
if mibBuilder.loadTexts: panPanorama.setStatus('current')
if mibBuilder.loadTexts: panPanorama.setDescription('\n\t\t\tSub-tree for Panorama specific objects.')
panPA_5060 = ObjectIdentity((1, 3, 6, 1, 4, 1, 25461, 2, 3, 8)).setLabel("panPA-5060")
if mibBuilder.loadTexts: panPA_5060.setStatus('current')
if mibBuilder.loadTexts: panPA_5060.setDescription('\n\t\t\tSub-tree for PA-5060 specific objects.')
panPA_5050 = ObjectIdentity((1, 3, 6, 1, 4, 1, 25461, 2, 3, 9)).setLabel("panPA-5050")
if mibBuilder.loadTexts: panPA_5050.setStatus('current')
if mibBuilder.loadTexts: panPA_5050.setDescription('\n\t\t\tSub-tree for PA-5050 specific objects.')
panPA_5020 = ObjectIdentity((1, 3, 6, 1, 4, 1, 25461, 2, 3, 11)).setLabel("panPA-5020")
if mibBuilder.loadTexts: panPA_5020.setStatus('current')
if mibBuilder.loadTexts: panPA_5020.setDescription('\n\t\t\tSub-tree for PA-5020 specific objects.')
panPA_200 = ObjectIdentity((1, 3, 6, 1, 4, 1, 25461, 2, 3, 12)).setLabel("panPA-200")
if mibBuilder.loadTexts: panPA_200.setStatus('current')
if mibBuilder.loadTexts: panPA_200.setDescription('\n\t\t\tSub-tree for PA-200 specific objects.')
panPA_3050 = ObjectIdentity((1, 3, 6, 1, 4, 1, 25461, 2, 3, 17)).setLabel("panPA-3050")
if mibBuilder.loadTexts: panPA_3050.setStatus('current')
if mibBuilder.loadTexts: panPA_3050.setDescription('\n\t\t\tSub-tree for PA-3050 specific objects.')
panPA_3020 = ObjectIdentity((1, 3, 6, 1, 4, 1, 25461, 2, 3, 18)).setLabel("panPA-3020")
if mibBuilder.loadTexts: panPA_3020.setStatus('current')
if mibBuilder.loadTexts: panPA_3020.setDescription('\n\t\t\tSub-tree for PA-3020 specific objects.')
panPA_3060 = ObjectIdentity((1, 3, 6, 1, 4, 1, 25461, 2, 3, 19)).setLabel("panPA-3060")
if mibBuilder.loadTexts: panPA_3060.setStatus('current')
if mibBuilder.loadTexts: panPA_3060.setDescription('\n\t\t\tSub-tree for PA-3060 specific objects.')
panPA_3200 = ObjectIdentity((1, 3, 6, 1, 4, 1, 25461, 2, 3, 20)).setLabel("panPA-3200")
if mibBuilder.loadTexts: panPA_3200.setStatus('current')
if mibBuilder.loadTexts: panPA_3200.setDescription('\n            Sub-tree for PA-3200 specific objects.')
panPA_3250 = ObjectIdentity((1, 3, 6, 1, 4, 1, 25461, 2, 3, 21)).setLabel("panPA-3250")
if mibBuilder.loadTexts: panPA_3250.setStatus('current')
if mibBuilder.loadTexts: panPA_3250.setDescription('\n            Sub-tree for PA-3250 specific objects.')
panPA_5260 = ObjectIdentity((1, 3, 6, 1, 4, 1, 25461, 2, 3, 22)).setLabel("panPA-5260")
if mibBuilder.loadTexts: panPA_5260.setStatus('current')
if mibBuilder.loadTexts: panPA_5260.setDescription('\n\t\t\tSub-tree for PA-5260 specific objects.')
panPA_5250 = ObjectIdentity((1, 3, 6, 1, 4, 1, 25461, 2, 3, 23)).setLabel("panPA-5250")
if mibBuilder.loadTexts: panPA_5250.setStatus('current')
if mibBuilder.loadTexts: panPA_5250.setDescription('\n\t\t\tSub-tree for PA-5250 specific objects.')
panPA_5220 = ObjectIdentity((1, 3, 6, 1, 4, 1, 25461, 2, 3, 24)).setLabel("panPA-5220")
if mibBuilder.loadTexts: panPA_5220.setStatus('current')
if mibBuilder.loadTexts: panPA_5220.setDescription('\n\t\t\tSub-tree for PA-5220 specific objects.')
panPA_VM = ObjectIdentity((1, 3, 6, 1, 4, 1, 25461, 2, 3, 29)).setLabel("panPA-VM")
if mibBuilder.loadTexts: panPA_VM.setStatus('current')
if mibBuilder.loadTexts: panPA_VM.setDescription('\n\t\t\tSub-tree for PA-VM specific objects.')
panM_100 = ObjectIdentity((1, 3, 6, 1, 4, 1, 25461, 2, 3, 30)).setLabel("panM-100")
if mibBuilder.loadTexts: panM_100.setStatus('current')
if mibBuilder.loadTexts: panM_100.setDescription('\n\t\t\tSub-tree for M-100 specific objects.')
panPA_7050 = ObjectIdentity((1, 3, 6, 1, 4, 1, 25461, 2, 3, 31)).setLabel("panPA-7050")
if mibBuilder.loadTexts: panPA_7050.setStatus('current')
if mibBuilder.loadTexts: panPA_7050.setDescription('\n\t\t\tSub-tree for PA-7050 specific objects.')
panGP_100 = ObjectIdentity((1, 3, 6, 1, 4, 1, 25461, 2, 3, 32)).setLabel("panGP-100")
if mibBuilder.loadTexts: panGP_100.setStatus('current')
if mibBuilder.loadTexts: panGP_100.setDescription('\n\t\t\tSub-tree for GP-100 specific objects.')
panWF_500 = ObjectIdentity((1, 3, 6, 1, 4, 1, 25461, 2, 3, 33)).setLabel("panWF-500")
if mibBuilder.loadTexts: panWF_500.setStatus('current')
if mibBuilder.loadTexts: panWF_500.setDescription('\n\t\t\tSub-tree for WF-500 specific objects.')
panPA_7080 = ObjectIdentity((1, 3, 6, 1, 4, 1, 25461, 2, 3, 34)).setLabel("panPA-7080")
if mibBuilder.loadTexts: panPA_7080.setStatus('current')
if mibBuilder.loadTexts: panPA_7080.setDescription('\n\t\t\tSub-tree for PA-7080 specific objects.')
panM_500 = ObjectIdentity((1, 3, 6, 1, 4, 1, 25461, 2, 3, 35)).setLabel("panM-500")
if mibBuilder.loadTexts: panM_500.setStatus('current')
if mibBuilder.loadTexts: panM_500.setDescription('\n\t\t\tSub-tree for M-500 specific objects.')
panPA_820 = ObjectIdentity((1, 3, 6, 1, 4, 1, 25461, 2, 3, 36)).setLabel("panPA-820")
if mibBuilder.loadTexts: panPA_820.setStatus('current')
if mibBuilder.loadTexts: panPA_820.setDescription('\n\t\t\tSub-tree for PA-820 specific objects.')
panPA_850 = ObjectIdentity((1, 3, 6, 1, 4, 1, 25461, 2, 3, 37)).setLabel("panPA-850")
if mibBuilder.loadTexts: panPA_850.setStatus('current')
if mibBuilder.loadTexts: panPA_850.setDescription('\n\t\t\tSub-tree for PA-850 specific objects.')
panPA_220 = ObjectIdentity((1, 3, 6, 1, 4, 1, 25461, 2, 3, 38)).setLabel("panPA-220")
if mibBuilder.loadTexts: panPA_220.setStatus('current')
if mibBuilder.loadTexts: panPA_220.setDescription('\n\t\t\tSub-tree for PA-220 specific objects.')
panM_600 = ObjectIdentity((1, 3, 6, 1, 4, 1, 25461, 2, 3, 39)).setLabel("panM-600")
if mibBuilder.loadTexts: panM_600.setStatus('current')
if mibBuilder.loadTexts: panM_600.setDescription('\n\t\t\tSub-tree for M-600 specific objects.')
panM_200 = ObjectIdentity((1, 3, 6, 1, 4, 1, 25461, 2, 3, 40)).setLabel("panM-200")
if mibBuilder.loadTexts: panM_200.setStatus('current')
if mibBuilder.loadTexts: panM_200.setDescription('\n\t\t\tSub-tree for M-200 specific objects.')
panPA_220R = ObjectIdentity((1, 3, 6, 1, 4, 1, 25461, 2, 3, 41)).setLabel("panPA-220R")
if mibBuilder.loadTexts: panPA_220R.setStatus('current')
if mibBuilder.loadTexts: panPA_220R.setDescription('\n\t\t\tSub-tree for PA-220R specific objects.')
panPA_5280 = ObjectIdentity((1, 3, 6, 1, 4, 1, 25461, 2, 3, 42)).setLabel("panPA-5280")
if mibBuilder.loadTexts: panPA_5280.setStatus('current')
if mibBuilder.loadTexts: panPA_5280.setDescription('\n                       Sub-tree for PA-5280 specific objects.')
panPA_3220 = ObjectIdentity((1, 3, 6, 1, 4, 1, 25461, 2, 3, 43)).setLabel("panPA-3220")
if mibBuilder.loadTexts: panPA_3220.setStatus('current')
if mibBuilder.loadTexts: panPA_3220.setDescription('\n            Sub-tree for PA-3220 specific objects.')
panPA_3260 = ObjectIdentity((1, 3, 6, 1, 4, 1, 25461, 2, 3, 44)).setLabel("panPA-3260")
if mibBuilder.loadTexts: panPA_3260.setStatus('current')
if mibBuilder.loadTexts: panPA_3260.setDescription('\n           Sub-tree for PA-3260 specific objects.')
panWF_600 = ObjectIdentity((1, 3, 6, 1, 4, 1, 25461, 2, 3, 45)).setLabel("panWF-600")
if mibBuilder.loadTexts: panWF_600.setStatus('current')
if mibBuilder.loadTexts: panWF_600.setDescription('\n\t\t\tSub-tree for WF-600 specific objects.')
panProcessingCards = ObjectIdentity((1, 3, 6, 1, 4, 1, 25461, 2, 3, 100))
if mibBuilder.loadTexts: panProcessingCards.setStatus('current')
if mibBuilder.loadTexts: panProcessingCards.setDescription('\n\t\t\tSub-tree for Processing line card specific objects.')
panFans = ObjectIdentity((1, 3, 6, 1, 4, 1, 25461, 2, 3, 101))
if mibBuilder.loadTexts: panFans.setStatus('current')
if mibBuilder.loadTexts: panFans.setDescription('\n\t\t\tSub-tree for Fan specific objects.')
panPowerSupplies = ObjectIdentity((1, 3, 6, 1, 4, 1, 25461, 2, 3, 102))
if mibBuilder.loadTexts: panPowerSupplies.setStatus('current')
if mibBuilder.loadTexts: panPowerSupplies.setDescription('\n\t\t\tSub-tree for Power supply specific objects.')
panPA_7000_SMC = ObjectIdentity((1, 3, 6, 1, 4, 1, 25461, 2, 3, 100, 1)).setLabel("panPA-7000-SMC")
if mibBuilder.loadTexts: panPA_7000_SMC.setStatus('current')
if mibBuilder.loadTexts: panPA_7000_SMC.setDescription('\n\t\t\tPA-7000 series Switch management card.')
panPA_7000_LPC = ObjectIdentity((1, 3, 6, 1, 4, 1, 25461, 2, 3, 100, 2)).setLabel("panPA-7000-LPC")
if mibBuilder.loadTexts: panPA_7000_LPC.setStatus('current')
if mibBuilder.loadTexts: panPA_7000_LPC.setDescription('\n\t\t\tPA-7000 series Log Processing card.')
panPA_7000_20G_NPC = ObjectIdentity((1, 3, 6, 1, 4, 1, 25461, 2, 3, 100, 3)).setLabel("panPA-7000-20G-NPC")
if mibBuilder.loadTexts: panPA_7000_20G_NPC.setStatus('current')
if mibBuilder.loadTexts: panPA_7000_20G_NPC.setDescription('\n\t\t\tPA-7000 series 20G Network Processing card.')
panPA_7080_SMC = ObjectIdentity((1, 3, 6, 1, 4, 1, 25461, 2, 3, 100, 4)).setLabel("panPA-7080-SMC")
if mibBuilder.loadTexts: panPA_7080_SMC.setStatus('current')
if mibBuilder.loadTexts: panPA_7080_SMC.setDescription('\n\t\t\tPA-7080 Switch management card.')
panPA_7050_SMC_B = ObjectIdentity((1, 3, 6, 1, 4, 1, 25461, 2, 3, 100, 5)).setLabel("panPA-7050-SMC-B")
if mibBuilder.loadTexts: panPA_7050_SMC_B.setStatus('current')
if mibBuilder.loadTexts: panPA_7050_SMC_B.setDescription('\n\t\t\tPA-7050 Bennu Switch management card.')
panPA_7000_LFC = ObjectIdentity((1, 3, 6, 1, 4, 1, 25461, 2, 3, 100, 6)).setLabel("panPA-7000-LFC")
if mibBuilder.loadTexts: panPA_7000_LFC.setStatus('current')
if mibBuilder.loadTexts: panPA_7000_LFC.setDescription('\n\t\t\tPA-7000 series Log Forwarding card.')
panPA_7000_100G_NPC = ObjectIdentity((1, 3, 6, 1, 4, 1, 25461, 2, 3, 100, 7)).setLabel("panPA-7000-100G-NPC")
if mibBuilder.loadTexts: panPA_7000_100G_NPC.setStatus('current')
if mibBuilder.loadTexts: panPA_7000_100G_NPC.setDescription('\n\t\t\tPA-7000 series 100G Network Processing card.')
panPA_7080_SMC_B = ObjectIdentity((1, 3, 6, 1, 4, 1, 25461, 2, 3, 100, 8)).setLabel("panPA-7080-SMC-B")
if mibBuilder.loadTexts: panPA_7080_SMC_B.setStatus('current')
if mibBuilder.loadTexts: panPA_7080_SMC_B.setDescription('\n\t\t\tPA-7080 Bennu Switch management card.')
mibBuilder.exportSymbols("PAN-PRODUCTS-MIB", panPA_5220=panPA_5220, panPA_7050_SMC_B=panPA_7050_SMC_B, panM_500=panM_500, panPA_3260=panPA_3260, panPA_7000_LFC=panPA_7000_LFC, PYSNMP_MODULE_ID=panProductsMibsModule, panPA_5020=panPA_5020, panPA_7000_LPC=panPA_7000_LPC, panM_600=panM_600, panPA_5280=panPA_5280, panPA_3050=panPA_3050, panPA_5060=panPA_5060, panPA_7050=panPA_7050, panPA_220=panPA_220, panPA_4050=panPA_4050, panPA_5050=panPA_5050, panPA_VM=panPA_VM, panPA_7080=panPA_7080, panPA_220R=panPA_220R, panPA_7000_20G_NPC=panPA_7000_20G_NPC, panPA_7080_SMC_B=panPA_7080_SMC_B, panPA_500=panPA_500, panPA_2020=panPA_2020, panPA_850=panPA_850, panPA_2050=panPA_2050, panPA_4020=panPA_4020, panPA_5250=panPA_5250, panPA_7000_SMC=panPA_7000_SMC, panPA_200=panPA_200, panPA_3220=panPA_3220, panPA_4060=panPA_4060, panM_100=panM_100, panPA_5260=panPA_5260, panPA_7080_SMC=panPA_7080_SMC, panFans=panFans, panProcessingCards=panProcessingCards, panPA_820=panPA_820, panPanorama=panPanorama, panPA_3020=panPA_3020, panPowerSupplies=panPowerSupplies, panPA_3250=panPA_3250, panWF_600=panWF_600, panWF_500=panWF_500, panPA_3060=panPA_3060, panPA_3200=panPA_3200, panProductsMibsModule=panProductsMibsModule, panM_200=panM_200, panPA_7000_100G_NPC=panPA_7000_100G_NPC, panGP_100=panGP_100)
