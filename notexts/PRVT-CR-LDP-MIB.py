#
# PySNMP MIB module PRVT-CR-LDP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/telco-systems/binos/PRVT-CR-LDP-MIB
# Produced by pysmi-1.1.3 at Sun Nov 28 20:26:40 2021
# On host fv-az77-612 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
ipSwitch, = mibBuilder.importSymbols("PRVT-SWITCH-MIB", "ipSwitch")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, Gauge32, TimeTicks, Integer32, Bits, Counter64, Unsigned32, iso, MibIdentifier, ObjectIdentity, ModuleIdentity, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Gauge32", "TimeTicks", "Integer32", "Bits", "Counter64", "Unsigned32", "iso", "MibIdentifier", "ObjectIdentity", "ModuleIdentity", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress")
RowStatus, TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TruthValue", "TextualConvention", "DisplayString")
prvtCrLdp = ModuleIdentity((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 3))
prvtCrLdp.setRevisions(('2008-01-01 00:00',))
if mibBuilder.loadTexts: prvtCrLdp.setLastUpdated('200801010000Z')
if mibBuilder.loadTexts: prvtCrLdp.setOrganization('BATM Advanced Communication')
mpls = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 6, 5))
prvtCrLdpObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 3, 1))
class PrvtCrldpAdminStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("up", 1), ("down", 2))

class PrvtCrldpOperStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("up", 1), ("down", 2), ("goingUp", 3), ("goingDown", 4), ("actFailed", 5))

class PrvtCrldpIndex(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'

prvtcrldpSigTable = MibTable((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 3, 1, 1), )
if mibBuilder.loadTexts: prvtcrldpSigTable.setStatus('current')
prvtcrldpSigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 3, 1, 1, 1), ).setIndexNames((0, "PRVT-CR-LDP-MIB", "prvtcrldpSigIndex"))
if mibBuilder.loadTexts: prvtcrldpSigEntry.setStatus('current')
prvtcrldpSigIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 3, 1, 1, 1, 1), PrvtCrldpIndex())
if mibBuilder.loadTexts: prvtcrldpSigIndex.setStatus('current')
prvtcrldpSigPathManagerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 3, 1, 1, 1, 2), PrvtCrldpIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtcrldpSigPathManagerIndex.setStatus('current')
prvtcrldpSigLsrIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 3, 1, 1, 1, 3), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtcrldpSigLsrIndex.setStatus('current')
prvtcrldpSigSocketIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 3, 1, 1, 1, 4), InterfaceIndexOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtcrldpSigSocketIfIndex.setStatus('current')
prvtcrldpSigSessionBufPoolSize = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 3, 1, 1, 1, 5), Integer32().clone(8)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtcrldpSigSessionBufPoolSize.setStatus('current')
prvtcrldpSigEMBufPoolSize = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 3, 1, 1, 1, 6), Integer32().clone(8)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtcrldpSigEMBufPoolSize.setStatus('current')
prvtcrldpSigAMBufPoolSize = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 3, 1, 1, 1, 7), Integer32().clone(8)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtcrldpSigAMBufPoolSize.setStatus('current')
prvtcrldpSigAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 3, 1, 1, 1, 8), PrvtCrldpAdminStatus().clone('up')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtcrldpSigAdminStatus.setStatus('current')
prvtcrldpSigOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 3, 1, 1, 1, 9), PrvtCrldpOperStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtcrldpSigOperStatus.setStatus('current')
prvtcrldpSigRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 3, 1, 1, 1, 10), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtcrldpSigRowStatus.setStatus('current')
prvtcrldpSigUseI3Interface = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 3, 1, 1, 1, 11), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtcrldpSigUseI3Interface.setStatus('current')
prvtcrldpSigConformanceFlags = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 3, 1, 1, 1, 12), Bits().clone(namedValues=NamedValues(("maxPduLen", 0)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtcrldpSigConformanceFlags.setStatus('current')
prvtcrldpSigUseIPv6Transport = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 3, 1, 1, 1, 13), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtcrldpSigUseIPv6Transport.setStatus('current')
prvtcrldpSigSessStatusTrapEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 3, 1, 1, 1, 14), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtcrldpSigSessStatusTrapEnable.setStatus('current')
prvtcrldpSigSessThreshTrapEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 3, 1, 1, 1, 15), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtcrldpSigSessThreshTrapEnable.setStatus('current')
prvtcrldpSigPathVecLimitTrapEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 3, 1, 1, 1, 16), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtcrldpSigPathVecLimitTrapEnable.setStatus('current')
prvtcrldpPmTable = MibTable((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 3, 1, 2), )
if mibBuilder.loadTexts: prvtcrldpPmTable.setStatus('current')
prvtcrldpPmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 3, 1, 2, 1), ).setIndexNames((0, "PRVT-CR-LDP-MIB", "prvtcrldpPmIndex"))
if mibBuilder.loadTexts: prvtcrldpPmEntry.setStatus('current')
prvtcrldpPmIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 3, 1, 2, 1, 1), PrvtCrldpIndex())
if mibBuilder.loadTexts: prvtcrldpPmIndex.setStatus('current')
prvtcrldpPmLsrIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 3, 1, 2, 1, 2), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtcrldpPmLsrIndex.setStatus('current')
prvtcrldpPmLdpEntityAutoCreate = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 3, 1, 2, 1, 3), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtcrldpPmLdpEntityAutoCreate.setStatus('current')
prvtcrldpPmLdpEntityAutoStart = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 3, 1, 2, 1, 4), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtcrldpPmLdpEntityAutoStart.setStatus('current')
prvtcrldpPmLdpEntityReuse = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 3, 1, 2, 1, 5), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtcrldpPmLdpEntityReuse.setStatus('current')
prvtcrldpPmLdpVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 3, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("version1", 1))).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtcrldpPmLdpVersion.setStatus('current')
prvtcrldpPmUseLdpFt = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 3, 1, 2, 1, 7), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtcrldpPmUseLdpFt.setStatus('current')
prvtcrldpPmAsNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 3, 1, 2, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtcrldpPmAsNumber.setStatus('current')
prvtcrldpPmIprBufPoolSize = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 3, 1, 2, 1, 9), Integer32().clone(8)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtcrldpPmIprBufPoolSize.setStatus('current')
prvtcrldpPmLdpSupported = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 3, 1, 2, 1, 10), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtcrldpPmLdpSupported.setStatus('current')
prvtcrldpPmCrLdpSupported = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 3, 1, 2, 1, 11), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtcrldpPmCrLdpSupported.setStatus('current')
prvtcrldpPmQueryFECSupported = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 3, 1, 2, 1, 12), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtcrldpPmQueryFECSupported.setStatus('current')
prvtcrldpPmAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 3, 1, 2, 1, 13), PrvtCrldpAdminStatus().clone('up')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtcrldpPmAdminStatus.setStatus('current')
prvtcrldpPmOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 3, 1, 2, 1, 14), PrvtCrldpOperStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtcrldpPmOperStatus.setStatus('current')
prvtcrldpPmRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 3, 1, 2, 1, 15), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtcrldpPmRowStatus.setStatus('current')
prvtcrldpPmRestartCapable = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 3, 1, 2, 1, 16), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtcrldpPmRestartCapable.setStatus('current')
prvtcrldpPmReconnectTime = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 3, 1, 2, 1, 17), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)).clone(10000)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtcrldpPmReconnectTime.setStatus('current')
prvtcrldpPmRecoveryTime = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 3, 1, 2, 1, 18), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)).clone(10000)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtcrldpPmRecoveryTime.setStatus('current')
prvtcrldpPmMaxPeerReconnect = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 3, 1, 2, 1, 19), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)).clone(10000)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtcrldpPmMaxPeerReconnect.setStatus('current')
prvtcrldpPmMaxPeerRecovery = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 3, 1, 2, 1, 20), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)).clone(10000)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtcrldpPmMaxPeerRecovery.setStatus('current')
prvtcrldpPmAdjDwnHoldTime = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 3, 1, 2, 1, 21), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)).clone(3000)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtcrldpPmAdjDwnHoldTime.setStatus('current')
prvtcrldpPmOutSegProgOrder = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 3, 1, 2, 1, 22), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("default", 0), ("connFirst", 1))).clone('default')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtcrldpPmOutSegProgOrder.setStatus('current')
prvtcrldpPmSupportIpv6 = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 3, 1, 2, 1, 23), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtcrldpPmSupportIpv6.setStatus('current')
prvtcrldpPmPolicySupportFlags = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 3, 1, 2, 1, 24), Bits().clone(namedValues=NamedValues(("policySupported", 0), ("perFecOptimizationSupported", 1), ("suppressAddressPolicy", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtcrldpPmPolicySupportFlags.setStatus('current')
prvtcrldpPmCheckOutSegIntfaceStat = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 3, 1, 2, 1, 25), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtcrldpPmCheckOutSegIntfaceStat.setStatus('current')
mibBuilder.exportSymbols("PRVT-CR-LDP-MIB", prvtcrldpPmQueryFECSupported=prvtcrldpPmQueryFECSupported, prvtcrldpPmPolicySupportFlags=prvtcrldpPmPolicySupportFlags, prvtcrldpSigPathVecLimitTrapEnable=prvtcrldpSigPathVecLimitTrapEnable, prvtcrldpPmUseLdpFt=prvtcrldpPmUseLdpFt, prvtcrldpPmSupportIpv6=prvtcrldpPmSupportIpv6, prvtcrldpPmRecoveryTime=prvtcrldpPmRecoveryTime, prvtcrldpPmMaxPeerReconnect=prvtcrldpPmMaxPeerReconnect, prvtcrldpPmLdpEntityReuse=prvtcrldpPmLdpEntityReuse, prvtcrldpSigLsrIndex=prvtcrldpSigLsrIndex, prvtcrldpSigIndex=prvtcrldpSigIndex, prvtcrldpSigUseI3Interface=prvtcrldpSigUseI3Interface, prvtcrldpPmIndex=prvtcrldpPmIndex, prvtCrLdp=prvtCrLdp, prvtcrldpSigEMBufPoolSize=prvtcrldpSigEMBufPoolSize, prvtcrldpSigSessThreshTrapEnable=prvtcrldpSigSessThreshTrapEnable, prvtcrldpPmCheckOutSegIntfaceStat=prvtcrldpPmCheckOutSegIntfaceStat, PrvtCrldpIndex=PrvtCrldpIndex, prvtcrldpSigSessionBufPoolSize=prvtcrldpSigSessionBufPoolSize, prvtcrldpSigEntry=prvtcrldpSigEntry, PrvtCrldpAdminStatus=PrvtCrldpAdminStatus, prvtcrldpPmIprBufPoolSize=prvtcrldpPmIprBufPoolSize, prvtcrldpPmLdpVersion=prvtcrldpPmLdpVersion, prvtcrldpPmEntry=prvtcrldpPmEntry, prvtcrldpPmLsrIndex=prvtcrldpPmLsrIndex, prvtcrldpSigAdminStatus=prvtcrldpSigAdminStatus, prvtcrldpPmCrLdpSupported=prvtcrldpPmCrLdpSupported, prvtcrldpSigOperStatus=prvtcrldpSigOperStatus, prvtCrLdpObjects=prvtCrLdpObjects, prvtcrldpPmAdjDwnHoldTime=prvtcrldpPmAdjDwnHoldTime, prvtcrldpPmAsNumber=prvtcrldpPmAsNumber, prvtcrldpPmAdminStatus=prvtcrldpPmAdminStatus, prvtcrldpPmRestartCapable=prvtcrldpPmRestartCapable, prvtcrldpSigSocketIfIndex=prvtcrldpSigSocketIfIndex, prvtcrldpSigPathManagerIndex=prvtcrldpSigPathManagerIndex, prvtcrldpPmOutSegProgOrder=prvtcrldpPmOutSegProgOrder, prvtcrldpSigConformanceFlags=prvtcrldpSigConformanceFlags, prvtcrldpSigSessStatusTrapEnable=prvtcrldpSigSessStatusTrapEnable, prvtcrldpPmOperStatus=prvtcrldpPmOperStatus, prvtcrldpSigUseIPv6Transport=prvtcrldpSigUseIPv6Transport, mpls=mpls, prvtcrldpPmReconnectTime=prvtcrldpPmReconnectTime, prvtcrldpSigAMBufPoolSize=prvtcrldpSigAMBufPoolSize, prvtcrldpPmRowStatus=prvtcrldpPmRowStatus, prvtcrldpPmMaxPeerRecovery=prvtcrldpPmMaxPeerRecovery, PYSNMP_MODULE_ID=prvtCrLdp, prvtcrldpPmTable=prvtcrldpPmTable, PrvtCrldpOperStatus=PrvtCrldpOperStatus, prvtcrldpPmLdpEntityAutoStart=prvtcrldpPmLdpEntityAutoStart, prvtcrldpSigTable=prvtcrldpSigTable, prvtcrldpPmLdpSupported=prvtcrldpPmLdpSupported, prvtcrldpSigRowStatus=prvtcrldpSigRowStatus, prvtcrldpPmLdpEntityAutoCreate=prvtcrldpPmLdpEntityAutoCreate)
