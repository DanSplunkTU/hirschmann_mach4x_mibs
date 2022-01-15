#
# PySNMP MIB module T11-FC-SP-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/T11-FC-SP-TC-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 17:49:35 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, iso, ObjectIdentity, IpAddress, Counter64, mib_2, Bits, Counter32, NotificationType, Unsigned32, Gauge32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "iso", "ObjectIdentity", "IpAddress", "Counter64", "mib-2", "Bits", "Counter32", "NotificationType", "Unsigned32", "Gauge32", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
t11FcTcMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 175))
t11FcTcMIB.setRevisions(('2008-08-20 00:00',))
if mibBuilder.loadTexts: t11FcTcMIB.setLastUpdated('200808200000Z')
if mibBuilder.loadTexts: t11FcTcMIB.setOrganization('This MIB module was developed through the coordinated effort of two organizations: T11 began the development and the IETF (in the IMSS Working Group) finished it.')
t11FcSpIdentities = MibIdentifier((1, 3, 6, 1, 2, 1, 175, 1))
t11FcSpAlgorithms = MibIdentifier((1, 3, 6, 1, 2, 1, 175, 1, 1))
class T11FcSpPolicyHashFormat(TextualConvention, OctetString):
    reference = '- ANSI INCITS 426-2007, T11/Project 1570-D, Fibre Channel - Security Protocols (FC-SP), February 2007, section 7.1.3.1 and table 106. - FIPS PUB 180-2.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class T11FcSpPolicyHashValue(TextualConvention, OctetString):
    reference = '- ANSI INCITS 426-2007, T11/Project 1570-D, Fibre Channel - Security Protocols (FC-SP), February 2007, section 7.1.3.1 and table 106.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

class T11FcSpHashCalculationStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("calculate", 1), ("correct", 2), ("stale", 3))

class T11FcSpAuthRejectReasonCode(TextualConvention, Integer32):
    reference = '- ANSI INCITS 426-2007, T11/Project 1570-D, Fibre Channel - Security Protocols (FC-SP), February 2007, Table 17, 48, 52.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("authFailure", 1), ("logicalError", 2), ("logicalBusy", 3), ("authILSNotSupported", 4), ("authELSNotSupported", 5), ("notLoggedIn", 6))

class T11FcSpAuthRejReasonCodeExp(TextualConvention, Integer32):
    reference = '- ANSI INCITS 426-2007, T11/Project 1570-D, Fibre Channel - Security Protocols (FC-SP), February 2007, Tables 18, 48, 52.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14))
    namedValues = NamedValues(("authMechanismNotUsable", 1), ("dhGroupNotUsable", 2), ("hashFunctionNotUsable", 3), ("authTransactionAlreadyStarted", 4), ("authenticationFailed", 5), ("incorrectPayload", 6), ("incorrectAuthProtocolMessage", 7), ("restartAuthProtocol", 8), ("authConcatNotSupported", 9), ("unsupportedProtocolVersion", 10), ("logicalBusy", 11), ("authILSNotSupported", 12), ("authELSNotSupported", 13), ("notLoggedIn", 14))

class T11FcSpHashFunctions(TextualConvention, Bits):
    reference = '- ANSI INCITS 426-2007, T11/Project 1570-D, Fibre Channel - Security Protocols (FC-SP), February 2007, Table 14.'
    status = 'current'
    namedValues = NamedValues(("md5", 0), ("sha1", 1))

class T11FcSpSignFunctions(TextualConvention, Bits):
    reference = '- ANSI INCITS 426-2007, T11/Project 1570-D, Fibre Channel - Security Protocols (FC-SP), February 2007, tables 38 & 39.'
    status = 'current'
    namedValues = NamedValues(("rsaSha1", 0))

class T11FcSpDhGroups(TextualConvention, Bits):
    reference = '- ANSI INCITS 426-2007, T11/Project 1570-D, Fibre Channel - Security Protocols (FC-SP), February 2007, Table 15.'
    status = 'current'
    namedValues = NamedValues(("null", 0), ("group1024", 1), ("group1280", 2), ("group1536", 3), ("group2048", 4), ("group3072", 5), ("group4096", 6), ("group6144", 7), ("group8192", 8))

class T11FcSpPolicyObjectType(TextualConvention, Integer32):
    reference = '- ANSI INCITS 426-2007, T11/Project 1570-D, Fibre Channel - Security Protocols (FC-SP), February 2007, Table 102.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("summary", 1), ("switchMemberList", 2), ("nodeMemberList", 3), ("switchConnectivity", 4), ("ipMgmtList", 5), ("attribute", 6))

class T11FcSpPolicyNameType(TextualConvention, Integer32):
    reference = '- ANSI INCITS 426-2007, T11/Project 1570-D, Fibre Channel - Security Protocols (FC-SP), February 2007, Table 103.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("nodeName", 1), ("restrictedNodeName", 2), ("portName", 3), ("restrictedPortName", 4), ("wildcard", 5), ("restrictedWildcard", 6), ("alphaNumericName", 7), ("ipv6AddressRange", 8), ("ipv4AddressRange", 9))

class T11FcSpPolicyName(TextualConvention, OctetString):
    reference = '- ANSI INCITS 426-2007, T11/Project 1570-D, Fibre Channel - Security Protocols (FC-SP), February 2007, Table 103.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 64)

class T11FcSpAlphaNumName(TextualConvention, OctetString):
    reference = '- ANSI INCITS 426-2007, T11/Project 1570-D, Fibre Channel - Security Protocols (FC-SP), February 2007, Table 103.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 64)

class T11FcSpAlphaNumNameOrAbsent(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

class T11FcSaDirection(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("ingress", 1), ("egress", 2))

class T11FcSpiIndex(TextualConvention, Unsigned32):
    reference = '- ANSI INCITS 426-2007, T11/Project 1570-D, Fibre Channel - Security Protocols (FC-SP), February 2007, section 4.7.2 and 4.7.3.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class T11FcSpPrecedence(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class T11FcRoutingControl(TextualConvention, OctetString):
    reference = '- Fibre Channel - Framing and Signaling-2 (FC-FS-2), ANSI INCITS 424-2007, Project T11/1619-D, February 2007, section 9.3. - Fibre Channel - Generic Services-5 (FC-GS-5), ANSI INCITS 427-2006, sections 4.5.2.4.2, 4.5.2.4.3 and table 12.'
    status = 'current'
    displayHint = '1x'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 1)
    fixedLength = 1

class T11FcSpType(TextualConvention, OctetString):
    reference = '- Fibre Channel - Framing and Signaling-2 (FC-FS-2), ANSI INCITS 424-2007, Project T11/1619-D, February 2007, section 9.6. - Fibre Channel - Generic Services-5 (FC-GS-5), ANSI INCITS 427-2006, sections 4.3.2.4 and 4.3.2.5.'
    status = 'current'
    displayHint = '2x'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(2, 2)
    fixedLength = 2

class T11FcSpTransforms(TextualConvention, Bits):
    reference = '- ANSI INCITS 426-2007, T11/Project 1570-D, Fibre Channel - Security Protocols (FC-SP), February 2007, Appendix A.3.1, tables A.23, A.24, A.25, A.26.'
    status = 'current'
    namedValues = NamedValues(("encrNull", 0), ("encrAesCbc", 1), ("encrAesCtr", 2), ("encrAesGcm", 3), ("encr3Des", 4), ("prfHmacMd5", 5), ("prfHmacSha1", 6), ("prfAesCbc", 7), ("authHmacMd5L96", 8), ("authHmacSha1L96", 9), ("authHmacMd5L128", 10), ("authHmacSha1L160", 11), ("encrNullAuthAesGmac", 12), ("dhGroups1024bit", 13), ("dhGroups2048bit", 14))

class T11FcSpSecurityProtocolId(TextualConvention, Integer32):
    reference = '- ANSI INCITS 426-2007, T11/Project 1570-D, Fibre Channel - Security Protocols (FC-SP), February 2007, section 6.3.2.2 and table 67.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("espHeader", 1), ("ctAuth", 2))

class T11FcSpLifetimeLeft(TextualConvention, Unsigned32):
    status = 'current'

class T11FcSpLifetimeLeftUnits(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("seconds", 1), ("kiloBytes", 2), ("megaBytes", 3), ("gigaBytes", 4), ("teraBytes", 5), ("petaBytes", 6), ("exaBytes", 7), ("zettaBytes", 8), ("yottaBytes", 9))

t11FcSpEncryptAlgorithms = MibIdentifier((1, 3, 6, 1, 2, 1, 175, 1, 1, 1))
t11FcSpEncrNull = ObjectIdentity((1, 3, 6, 1, 2, 1, 175, 1, 1, 1, 1))
if mibBuilder.loadTexts: t11FcSpEncrNull.setStatus('current')
t11FcSpEncrAesCbc = ObjectIdentity((1, 3, 6, 1, 2, 1, 175, 1, 1, 1, 2))
if mibBuilder.loadTexts: t11FcSpEncrAesCbc.setStatus('current')
t11FcSpEncrAesCtr = ObjectIdentity((1, 3, 6, 1, 2, 1, 175, 1, 1, 1, 3))
if mibBuilder.loadTexts: t11FcSpEncrAesCtr.setStatus('current')
t11FcSpEncrAesGcm = ObjectIdentity((1, 3, 6, 1, 2, 1, 175, 1, 1, 1, 4))
if mibBuilder.loadTexts: t11FcSpEncrAesGcm.setStatus('current')
t11FcSpEncr3Des = ObjectIdentity((1, 3, 6, 1, 2, 1, 175, 1, 1, 1, 5))
if mibBuilder.loadTexts: t11FcSpEncr3Des.setStatus('current')
t11FcSpAuthAlgorithms = MibIdentifier((1, 3, 6, 1, 2, 1, 175, 1, 1, 2))
t11FcSpAuthNull = ObjectIdentity((1, 3, 6, 1, 2, 1, 175, 1, 1, 2, 1))
if mibBuilder.loadTexts: t11FcSpAuthNull.setStatus('current')
t11FcSpAuthHmacMd5L96 = ObjectIdentity((1, 3, 6, 1, 2, 1, 175, 1, 1, 2, 2))
if mibBuilder.loadTexts: t11FcSpAuthHmacMd5L96.setStatus('current')
t11FcSpAuthHmacSha1L96 = ObjectIdentity((1, 3, 6, 1, 2, 1, 175, 1, 1, 2, 3))
if mibBuilder.loadTexts: t11FcSpAuthHmacSha1L96.setStatus('current')
t11FcSpAuthHmacMd5L128 = ObjectIdentity((1, 3, 6, 1, 2, 1, 175, 1, 1, 2, 4))
if mibBuilder.loadTexts: t11FcSpAuthHmacMd5L128.setStatus('current')
t11FcSpAuthHmacSha1L160 = ObjectIdentity((1, 3, 6, 1, 2, 1, 175, 1, 1, 2, 5))
if mibBuilder.loadTexts: t11FcSpAuthHmacSha1L160.setStatus('current')
t11FcSpEncrNullAuthAesGmac = ObjectIdentity((1, 3, 6, 1, 2, 1, 175, 1, 1, 1, 6))
if mibBuilder.loadTexts: t11FcSpEncrNullAuthAesGmac.setStatus('current')
mibBuilder.exportSymbols("T11-FC-SP-TC-MIB", T11FcSpSecurityProtocolId=T11FcSpSecurityProtocolId, T11FcSpAlphaNumNameOrAbsent=T11FcSpAlphaNumNameOrAbsent, T11FcSpAlphaNumName=T11FcSpAlphaNumName, T11FcSpAuthRejectReasonCode=T11FcSpAuthRejectReasonCode, T11FcSpType=T11FcSpType, T11FcSpTransforms=T11FcSpTransforms, t11FcSpEncr3Des=t11FcSpEncr3Des, t11FcSpAlgorithms=t11FcSpAlgorithms, T11FcSpDhGroups=T11FcSpDhGroups, T11FcSpHashCalculationStatus=T11FcSpHashCalculationStatus, T11FcSpPolicyHashValue=T11FcSpPolicyHashValue, t11FcSpEncryptAlgorithms=t11FcSpEncryptAlgorithms, T11FcSpAuthRejReasonCodeExp=T11FcSpAuthRejReasonCodeExp, t11FcSpEncrNull=t11FcSpEncrNull, T11FcRoutingControl=T11FcRoutingControl, T11FcSpPolicyObjectType=T11FcSpPolicyObjectType, t11FcSpAuthHmacSha1L160=t11FcSpAuthHmacSha1L160, T11FcSpSignFunctions=T11FcSpSignFunctions, t11FcSpEncrAesCtr=t11FcSpEncrAesCtr, t11FcSpAuthHmacSha1L96=t11FcSpAuthHmacSha1L96, t11FcSpEncrNullAuthAesGmac=t11FcSpEncrNullAuthAesGmac, T11FcSpHashFunctions=T11FcSpHashFunctions, t11FcSpAuthHmacMd5L128=t11FcSpAuthHmacMd5L128, T11FcSpLifetimeLeftUnits=T11FcSpLifetimeLeftUnits, T11FcSpPrecedence=T11FcSpPrecedence, t11FcSpAuthHmacMd5L96=t11FcSpAuthHmacMd5L96, PYSNMP_MODULE_ID=t11FcTcMIB, t11FcSpAuthAlgorithms=t11FcSpAuthAlgorithms, T11FcSpPolicyHashFormat=T11FcSpPolicyHashFormat, T11FcSpLifetimeLeft=T11FcSpLifetimeLeft, t11FcTcMIB=t11FcTcMIB, T11FcSpPolicyNameType=T11FcSpPolicyNameType, T11FcSpPolicyName=T11FcSpPolicyName, T11FcSaDirection=T11FcSaDirection, t11FcSpAuthNull=t11FcSpAuthNull, T11FcSpiIndex=T11FcSpiIndex, t11FcSpEncrAesCbc=t11FcSpEncrAesCbc, t11FcSpEncrAesGcm=t11FcSpEncrAesGcm, t11FcSpIdentities=t11FcSpIdentities)
