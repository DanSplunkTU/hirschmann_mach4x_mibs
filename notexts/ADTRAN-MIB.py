#
# PySNMP MIB module ADTRAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/adtran/ADTRAN-MIB
# Produced by pysmi-1.1.3 at Sun Nov 21 00:41:04 2021
# On host fv-az39-63 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Counter32, Counter64, Integer32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ObjectIdentity, NotificationType, MibIdentifier, Bits, ModuleIdentity, IpAddress, enterprises, Unsigned32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Counter64", "Integer32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ObjectIdentity", "NotificationType", "MibIdentifier", "Bits", "ModuleIdentity", "IpAddress", "enterprises", "Unsigned32", "TimeTicks")
DisplayString, PhysAddress, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "PhysAddress", "TextualConvention")
adtran = ModuleIdentity((1, 3, 6, 1, 4, 1, 664))
if mibBuilder.loadTexts: adtran.setLastUpdated('0208090000Z')
if mibBuilder.loadTexts: adtran.setOrganization('ADTRAN, Inc.')
adProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 1))
adMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 2))
adAdmin = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 3))
adPerform = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 4))
adShared = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5))
adIdentity = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 6))
adIdentityShared = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 6, 10000))
adAgentCapModule = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 7))
adAgentCapProduct = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 7, 1))
adAgentCapShared = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 7, 2))
adConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 99))
adComplianceShared = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 99, 10000))
adProductInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 3, 1))
adProdName = MibScalar((1, 3, 6, 1, 4, 1, 664, 3, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adProdName.setStatus('current')
adProdPartNumber = MibScalar((1, 3, 6, 1, 4, 1, 664, 3, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adProdPartNumber.setStatus('current')
adProdCLEIcode = MibScalar((1, 3, 6, 1, 4, 1, 664, 3, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adProdCLEIcode.setStatus('current')
adProdSerialNumber = MibScalar((1, 3, 6, 1, 4, 1, 664, 3, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adProdSerialNumber.setStatus('current')
adProdRevision = MibScalar((1, 3, 6, 1, 4, 1, 664, 3, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adProdRevision.setStatus('current')
adProdSwVersion = MibScalar((1, 3, 6, 1, 4, 1, 664, 3, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adProdSwVersion.setStatus('current')
adProdPhysAddress = MibScalar((1, 3, 6, 1, 4, 1, 664, 3, 1, 7), PhysAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adProdPhysAddress.setStatus('current')
adProdProductID = MibScalar((1, 3, 6, 1, 4, 1, 664, 3, 1, 8), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adProdProductID.setStatus('current')
adProdTransType = MibScalar((1, 3, 6, 1, 4, 1, 664, 3, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adProdTransType.setStatus('current')
adCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 99, 1))
adMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 99, 2))
adCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 664, 99, 1, 1)).setObjects(("ADTRAN-MIB", "adBaseGroup"), ("ADTRAN-MIB", "adCNDGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adCompliance = adCompliance.setStatus('current')
adBaseGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 664, 99, 2, 1)).setObjects(("ADTRAN-MIB", "adProdName"), ("ADTRAN-MIB", "adProdPartNumber"), ("ADTRAN-MIB", "adProdCLEIcode"), ("ADTRAN-MIB", "adProdSerialNumber"), ("ADTRAN-MIB", "adProdRevision"), ("ADTRAN-MIB", "adProdSwVersion"), ("ADTRAN-MIB", "adProdPhysAddress"), ("ADTRAN-MIB", "adProdProductID"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adBaseGroup = adBaseGroup.setStatus('current')
adCNDGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 664, 99, 2, 2)).setObjects(("ADTRAN-MIB", "adProdTransType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adCNDGroup = adCNDGroup.setStatus('current')
mibBuilder.exportSymbols("ADTRAN-MIB", adtran=adtran, adAgentCapModule=adAgentCapModule, adComplianceShared=adComplianceShared, adBaseGroup=adBaseGroup, adProdName=adProdName, adCompliances=adCompliances, adProdTransType=adProdTransType, adMgmt=adMgmt, adAgentCapProduct=adAgentCapProduct, adPerform=adPerform, adCNDGroup=adCNDGroup, adConformance=adConformance, adProdCLEIcode=adProdCLEIcode, adIdentity=adIdentity, adProdSwVersion=adProdSwVersion, PYSNMP_MODULE_ID=adtran, adAgentCapShared=adAgentCapShared, adProdPartNumber=adProdPartNumber, adAdmin=adAdmin, adProdSerialNumber=adProdSerialNumber, adProdPhysAddress=adProdPhysAddress, adProdRevision=adProdRevision, adShared=adShared, adProducts=adProducts, adProductInfo=adProductInfo, adProdProductID=adProdProductID, adMIBGroups=adMIBGroups, adIdentityShared=adIdentityShared, adCompliance=adCompliance)
