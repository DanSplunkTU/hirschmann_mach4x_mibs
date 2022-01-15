#
# PySNMP MIB module CADANT-PRODUCTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/arris/CADANT-PRODUCTS-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 17:51:50 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, TimeTicks, NotificationType, Gauge32, enterprises, ObjectIdentity, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, iso, Unsigned32, Integer32, Counter32, ModuleIdentity, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "Gauge32", "enterprises", "ObjectIdentity", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "iso", "Unsigned32", "Integer32", "Counter32", "ModuleIdentity", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cadant = ModuleIdentity((1, 3, 6, 1, 4, 1, 4998))
cadant.setRevisions(('2000-11-18 00:00', '2002-02-01 00:00', '2002-05-07 00:00', '2002-06-26 00:00', '2002-12-10 00:00', '2003-06-30 00:00', '2007-06-04 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: cadant.setRevisionsDescriptions(('Initial version. Added c4cmts.', 'Added c4ccmts.', 'Added cadPolicy.', 'Added AAA support.', 'Added IKE.', 'Added G2 IMS.', 'Added cadTopology.',))
if mibBuilder.loadTexts: cadant.setLastUpdated('200306300000Z')
if mibBuilder.loadTexts: cadant.setOrganization('Arris International')
if mibBuilder.loadTexts: cadant.setContactInfo('support@arrisi.com')
if mibBuilder.loadTexts: cadant.setDescription('The object identifiers of Cadant products.')
cadObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4998, 1))
cadProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 4998, 2))
cadCable = MibIdentifier((1, 3, 6, 1, 4, 1, 4998, 1, 1))
cadSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 4998, 1, 1, 5))
cadNotification = MibIdentifier((1, 3, 6, 1, 4, 1, 4998, 1, 1, 6))
cadEquipment = MibIdentifier((1, 3, 6, 1, 4, 1, 4998, 1, 1, 10))
cadSpectrum = MibIdentifier((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15))
cadLayer2 = MibIdentifier((1, 3, 6, 1, 4, 1, 4998, 1, 1, 20))
cadLayer3 = MibIdentifier((1, 3, 6, 1, 4, 1, 4998, 1, 1, 25))
cadSubscriber = MibIdentifier((1, 3, 6, 1, 4, 1, 4998, 1, 1, 30))
cadPolicy = MibIdentifier((1, 3, 6, 1, 4, 1, 4998, 1, 1, 35))
cadAuthentication = MibIdentifier((1, 3, 6, 1, 4, 1, 4998, 1, 1, 40))
cadIke = MibIdentifier((1, 3, 6, 1, 4, 1, 4998, 1, 1, 45))
cadSchema = MibIdentifier((1, 3, 6, 1, 4, 1, 4998, 1, 1, 50))
cadCmRemoteQuery = MibIdentifier((1, 3, 6, 1, 4, 1, 4998, 1, 1, 55))
cadExperimental = MibIdentifier((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100))
cadTopology = MibIdentifier((1, 3, 6, 1, 4, 1, 4998, 1, 1, 105))
cadCmtsIf3 = MibIdentifier((1, 3, 6, 1, 4, 1, 4998, 1, 1, 110))
cadL2vpn = MibIdentifier((1, 3, 6, 1, 4, 1, 4998, 1, 1, 120))
cadNms = MibIdentifier((1, 3, 6, 1, 4, 1, 4998, 1, 2))
c4cmts = MibIdentifier((1, 3, 6, 1, 4, 1, 4998, 2, 1))
c4ccmts = MibIdentifier((1, 3, 6, 1, 4, 1, 4998, 2, 2))
g2ims = MibIdentifier((1, 3, 6, 1, 4, 1, 4998, 2, 3))
mibBuilder.exportSymbols("CADANT-PRODUCTS-MIB", cadCable=cadCable, cadL2vpn=cadL2vpn, cadLayer3=cadLayer3, cadObjects=cadObjects, cadEquipment=cadEquipment, cadLayer2=cadLayer2, cadNms=cadNms, cadSubscriber=cadSubscriber, c4ccmts=c4ccmts, cadant=cadant, cadSpectrum=cadSpectrum, cadTopology=cadTopology, cadIke=cadIke, cadCmtsIf3=cadCmtsIf3, cadAuthentication=cadAuthentication, cadSchema=cadSchema, cadProducts=cadProducts, PYSNMP_MODULE_ID=cadant, g2ims=g2ims, cadNotification=cadNotification, c4cmts=c4cmts, cadPolicy=cadPolicy, cadSystem=cadSystem, cadExperimental=cadExperimental, cadCmRemoteQuery=cadCmRemoteQuery)
