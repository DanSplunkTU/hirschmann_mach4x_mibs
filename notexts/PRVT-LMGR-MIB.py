#
# PySNMP MIB module PRVT-LMGR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/telco-systems/binos/PRVT-LMGR-MIB
# Produced by pysmi-1.1.3 at Sun Nov 28 20:26:40 2021
# On host fv-az77-612 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
InetAddressIPv4, InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressIPv4", "InetAddressType", "InetAddress")
mpls, = mibBuilder.importSymbols("PRVT-CR-LDP-MIB", "mpls")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
NotificationType, Gauge32, TimeTicks, Integer32, Bits, Counter64, Unsigned32, iso, MibIdentifier, ObjectIdentity, ModuleIdentity, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Gauge32", "TimeTicks", "Integer32", "Bits", "Counter64", "Unsigned32", "iso", "MibIdentifier", "ObjectIdentity", "ModuleIdentity", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress")
RowStatus, TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TruthValue", "TextualConvention", "DisplayString")
prvtLmgr = ModuleIdentity((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 4))
prvtLmgr.setRevisions(('2006-06-11 00:00',))
if mibBuilder.loadTexts: prvtLmgr.setLastUpdated('200606110000Z')
if mibBuilder.loadTexts: prvtLmgr.setOrganization('BATM Advanced Communication')
prvtLmgrObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 4, 1))
class PrvtLmgrAdminStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("up", 1), ("down", 2))

class PrvtLmgrOperStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("up", 1), ("down", 2), ("goingUp", 3), ("goingDown", 4), ("actFailed", 5))

class PrvtLmgrPartnerStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("initial", 0), ("activating", 1), ("active", 2), ("deactivating", 3), ("failedOver", 4), ("failed", 5), ("unavailable", 6))

class PrvtLmgrIndex(TextualConvention, Unsigned32):
    status = 'current'

class PrvtLmgrControlModes(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("ordered", 1), ("independent", 2))

prvtLsrId = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 4, 1, 1), InetAddressIPv4()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtLsrId.setStatus('current')
prvtLmgrLsrEntityTable = MibTable((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 4, 1, 2), )
if mibBuilder.loadTexts: prvtLmgrLsrEntityTable.setStatus('current')
prvtLmgrLsrEntityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 4, 1, 2, 1), ).setIndexNames((0, "PRVT-LMGR-MIB", "prvtlmgrLsrEntityLsrIndex"))
if mibBuilder.loadTexts: prvtLmgrLsrEntityEntry.setStatus('current')
prvtlmgrLsrEntityLsrIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 4, 1, 2, 1, 1), PrvtLmgrIndex())
if mibBuilder.loadTexts: prvtlmgrLsrEntityLsrIndex.setStatus('current')
prvtLmgrLsrEntityAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 4, 1, 2, 1, 2), PrvtLmgrAdminStatus().clone('up')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtLmgrLsrEntityAdminStatus.setStatus('current')
prvtLmgrLsrEntityOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 4, 1, 2, 1, 3), PrvtLmgrOperStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtLmgrLsrEntityOperStatus.setStatus('current')
prvtLmgrLsrEntityRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 4, 1, 2, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtLmgrLsrEntityRowStatus.setStatus('current')
prvtLmgrLsrEntityMinLsiBuffers = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 4, 1, 2, 1, 5), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtLmgrLsrEntityMinLsiBuffers.setStatus('current')
prvtLmgrLsrEntityMaxLsiBuffers = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 4, 1, 2, 1, 6), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtLmgrLsrEntityMaxLsiBuffers.setStatus('current')
prvtLmgrLscStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 4, 1, 2, 1, 7), PrvtLmgrPartnerStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtLmgrLscStatus.setStatus('current')
prvtLmgrLdbCount = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 4, 1, 2, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtLmgrLdbCount.setStatus('current')
prvtLmgrLsrEntityLsrId = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 4, 1, 2, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtLmgrLsrEntityLsrId.setStatus('current')
prvtLmgrLsrEntityTranAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 4, 1, 2, 1, 10), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtLmgrLsrEntityTranAddrType.setStatus('current')
prvtLmgrLsrEntityTranAddrLen = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 4, 1, 2, 1, 11), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtLmgrLsrEntityTranAddrLen.setStatus('current')
prvtLmgrLsrEntityTranAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 4, 1, 2, 1, 12), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtLmgrLsrEntityTranAddr.setStatus('current')
prvtLmgrLsrEntityControlMode = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 4, 1, 2, 1, 13), PrvtLmgrControlModes()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtLmgrLsrEntityControlMode.setStatus('current')
prvtLmgrLsrEntityMergeLsps = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 4, 1, 2, 1, 14), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtLmgrLsrEntityMergeLsps.setStatus('current')
prvtLmgrLsrEntityLoopDetection = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 4, 1, 2, 1, 15), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtLmgrLsrEntityLoopDetection.setStatus('current')
prvtLmgrLsrEntityPerformGrouping = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 4, 1, 2, 1, 16), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtLmgrLsrEntityPerformGrouping.setStatus('current')
prvtLmgrLsrAutoStaticLsps = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 4, 1, 2, 1, 17), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtLmgrLsrAutoStaticLsps.setStatus('current')
prvtLmgrLsrDisplayPhpXCs = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 4, 1, 2, 1, 18), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtLmgrLsrDisplayPhpXCs.setStatus('current')
prvtLmgrLsrEntityIpv6TranAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 4, 1, 2, 1, 19), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtLmgrLsrEntityIpv6TranAddr.setStatus('current')
prvtLmgrLsrLspXcTable = MibTable((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 4, 1, 3), )
if mibBuilder.loadTexts: prvtLmgrLsrLspXcTable.setStatus('current')
prvtLmgrLsrLspXcEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 4, 1, 3, 1), ).setIndexNames((0, "PRVT-LMGR-MIB", "prvtlmgrLsrEntityLsrIndex"), (0, "PRVT-LMGR-MIB", "prvtLmgrLsrLspXcIndex"), (0, "PRVT-LMGR-MIB", "prvtLmgrLsrLspInSegLabel"), (0, "PRVT-LMGR-MIB", "prvtLmgrLsrLspOutSegIndex"))
if mibBuilder.loadTexts: prvtLmgrLsrLspXcEntry.setStatus('current')
prvtLmgrLsrLspXcIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 4, 1, 3, 1, 2), Unsigned32())
if mibBuilder.loadTexts: prvtLmgrLsrLspXcIndex.setStatus('current')
prvtLmgrLsrLspInSegIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 4, 1, 3, 1, 3), Unsigned32())
if mibBuilder.loadTexts: prvtLmgrLsrLspInSegIndex.setStatus('current')
prvtLmgrLsrLspInSegIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 4, 1, 3, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtLmgrLsrLspInSegIfIndex.setStatus('current')
prvtLmgrLsrLspInSegLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 4, 1, 3, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtLmgrLsrLspInSegLabel.setStatus('current')
prvtLmgrLsrLspOutSegIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 4, 1, 3, 1, 6), Unsigned32())
if mibBuilder.loadTexts: prvtLmgrLsrLspOutSegIndex.setStatus('current')
prvtLmgrLsrLspOutSegIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 4, 1, 3, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtLmgrLsrLspOutSegIfIndex.setStatus('current')
prvtLmgrLsrLspOutSegLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 4, 1, 3, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtLmgrLsrLspOutSegLabel.setStatus('current')
prvtLmgrLsrLspOutSegNextHopAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 4, 1, 3, 1, 9), InetAddressIPv4()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtLmgrLsrLspOutSegNextHopAddr.setStatus('current')
prvtLmgrConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 4, 2))
prvtLmgrCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 4, 2, 1))
prvtLmgrGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 4, 2, 2))
prvtLmgrCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 4, 2, 1, 1)).setObjects(("PRVT-LMGR-MIB", "prvtLmgrEntityGroup"), ("PRVT-LMGR-MIB", "prvtLmgrMiscGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    prvtLmgrCompliance = prvtLmgrCompliance.setStatus('current')
prvtLmgrEntityGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 4, 2, 2, 2)).setObjects(("PRVT-LMGR-MIB", "prvtLmgrLsrEntityAdminStatus"), ("PRVT-LMGR-MIB", "prvtLmgrLsrEntityOperStatus"), ("PRVT-LMGR-MIB", "prvtLmgrLsrEntityRowStatus"), ("PRVT-LMGR-MIB", "prvtLmgrLsrEntityMinLsiBuffers"), ("PRVT-LMGR-MIB", "prvtLmgrLsrEntityMaxLsiBuffers"), ("PRVT-LMGR-MIB", "prvtLmgrLsrEntityLsrId"), ("PRVT-LMGR-MIB", "prvtLmgrLsrEntityTranAddrType"), ("PRVT-LMGR-MIB", "prvtLmgrLsrEntityTranAddrLen"), ("PRVT-LMGR-MIB", "prvtLmgrLsrEntityTranAddr"), ("PRVT-LMGR-MIB", "prvtLmgrLsrEntityControlMode"), ("PRVT-LMGR-MIB", "prvtLmgrLsrEntityMergeLsps"), ("PRVT-LMGR-MIB", "prvtLmgrLsrEntityLoopDetection"), ("PRVT-LMGR-MIB", "prvtLmgrLsrEntityPerformGrouping"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    prvtLmgrEntityGroup = prvtLmgrEntityGroup.setStatus('current')
prvtLmgrMiscGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 4, 2, 2, 3)).setObjects(("PRVT-LMGR-MIB", "prvtLmgrLscStatus"), ("PRVT-LMGR-MIB", "prvtLmgrLdbCount"), ("PRVT-LMGR-MIB", "prvtLmgrLsrAutoStaticLsps"), ("PRVT-LMGR-MIB", "prvtLmgrLsrDisplayPhpXCs"), ("PRVT-LMGR-MIB", "prvtLmgrLsrLspInSegIfIndex"), ("PRVT-LMGR-MIB", "prvtLmgrLsrLspInSegLabel"), ("PRVT-LMGR-MIB", "prvtLmgrLsrLspOutSegIfIndex"), ("PRVT-LMGR-MIB", "prvtLmgrLsrLspOutSegLabel"), ("PRVT-LMGR-MIB", "prvtLmgrLsrLspOutSegNextHopAddr"), ("PRVT-LMGR-MIB", "prvtLmgrLsrEntityIpv6TranAddr"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    prvtLmgrMiscGroup = prvtLmgrMiscGroup.setStatus('current')
mibBuilder.exportSymbols("PRVT-LMGR-MIB", prvtLmgrLsrEntityMinLsiBuffers=prvtLmgrLsrEntityMinLsiBuffers, prvtLmgrCompliance=prvtLmgrCompliance, prvtLmgrMiscGroup=prvtLmgrMiscGroup, prvtLmgrCompliances=prvtLmgrCompliances, prvtLmgrLsrLspInSegIndex=prvtLmgrLsrLspInSegIndex, prvtLmgrLsrEntityRowStatus=prvtLmgrLsrEntityRowStatus, prvtLmgr=prvtLmgr, prvtLmgrLscStatus=prvtLmgrLscStatus, PrvtLmgrControlModes=PrvtLmgrControlModes, prvtLmgrLsrEntityTranAddrType=prvtLmgrLsrEntityTranAddrType, PrvtLmgrOperStatus=PrvtLmgrOperStatus, prvtLmgrLsrEntityAdminStatus=prvtLmgrLsrEntityAdminStatus, prvtLsrId=prvtLsrId, PrvtLmgrAdminStatus=PrvtLmgrAdminStatus, prvtLmgrLsrEntityControlMode=prvtLmgrLsrEntityControlMode, prvtLmgrLsrEntityLsrId=prvtLmgrLsrEntityLsrId, prvtLmgrLsrEntityPerformGrouping=prvtLmgrLsrEntityPerformGrouping, prvtLmgrConformance=prvtLmgrConformance, prvtLmgrLsrEntityTable=prvtLmgrLsrEntityTable, prvtLmgrLsrEntityTranAddrLen=prvtLmgrLsrEntityTranAddrLen, prvtLmgrObjects=prvtLmgrObjects, prvtLmgrLsrLspXcTable=prvtLmgrLsrLspXcTable, prvtLmgrLsrEntityMaxLsiBuffers=prvtLmgrLsrEntityMaxLsiBuffers, prvtLmgrGroups=prvtLmgrGroups, PrvtLmgrPartnerStatus=PrvtLmgrPartnerStatus, prvtLmgrLsrLspOutSegLabel=prvtLmgrLsrLspOutSegLabel, prvtLmgrLsrLspInSegIfIndex=prvtLmgrLsrLspInSegIfIndex, prvtLmgrLdbCount=prvtLmgrLdbCount, prvtLmgrLsrEntityOperStatus=prvtLmgrLsrEntityOperStatus, prvtLmgrLsrEntityTranAddr=prvtLmgrLsrEntityTranAddr, prvtLmgrLsrLspOutSegIfIndex=prvtLmgrLsrLspOutSegIfIndex, prvtLmgrLsrLspXcIndex=prvtLmgrLsrLspXcIndex, prvtLmgrLsrLspXcEntry=prvtLmgrLsrLspXcEntry, prvtlmgrLsrEntityLsrIndex=prvtlmgrLsrEntityLsrIndex, prvtLmgrLsrEntityEntry=prvtLmgrLsrEntityEntry, prvtLmgrLsrDisplayPhpXCs=prvtLmgrLsrDisplayPhpXCs, prvtLmgrLsrLspOutSegNextHopAddr=prvtLmgrLsrLspOutSegNextHopAddr, prvtLmgrLsrEntityIpv6TranAddr=prvtLmgrLsrEntityIpv6TranAddr, prvtLmgrLsrEntityMergeLsps=prvtLmgrLsrEntityMergeLsps, prvtLmgrEntityGroup=prvtLmgrEntityGroup, PrvtLmgrIndex=PrvtLmgrIndex, prvtLmgrLsrAutoStaticLsps=prvtLmgrLsrAutoStaticLsps, PYSNMP_MODULE_ID=prvtLmgr, prvtLmgrLsrLspInSegLabel=prvtLmgrLsrLspInSegLabel, prvtLmgrLsrLspOutSegIndex=prvtLmgrLsrLspOutSegIndex, prvtLmgrLsrEntityLoopDetection=prvtLmgrLsrEntityLoopDetection)
