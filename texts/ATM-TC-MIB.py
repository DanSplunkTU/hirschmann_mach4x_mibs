#
# PySNMP MIB module ATM-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/output/asn1/ATM-TC-MIB
# Produced by pysmi-1.1.8 at Sun Jan 16 00:41:52 2022
# On host fv-az42-839 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, Counter64, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, mib_2, Gauge32, ObjectIdentity, Unsigned32, IpAddress, Integer32, Bits, MibIdentifier, ModuleIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Counter64", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "mib-2", "Gauge32", "ObjectIdentity", "Unsigned32", "IpAddress", "Integer32", "Bits", "MibIdentifier", "ModuleIdentity", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
atmTCMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 37, 3))
if mibBuilder.loadTexts: atmTCMIB.setLastUpdated('9810190200Z')
if mibBuilder.loadTexts: atmTCMIB.setOrganization('IETF AToMMIB Working Group')
if mibBuilder.loadTexts: atmTCMIB.setContactInfo('          Michael Noto\n              Postal:  3Com Corporation\n                       5400 Bayfront Plaza, M/S 3109\n                       Santa Clara, CA 95052\n                       USA\n              Tel:     +1 408 326 2218\n              E-mail:  mike_noto@3com.com\n\n                       Ethan Mickey Spiegel\n              Postal:  Cisco Systems\n                       170 W. Tasman Dr.\n                       San Jose, CA 95134\n                       USA\n              Tel:     +1 408 526 6408\n              E-mail:  mspiegel@cisco.com\n\n                       Kaj Tesink\n              Postal:  Bellcore\n                       331 Newman Springs Road\n                       Red Bank, NJ 07701\n                       USA\n              Tel:     +1 732 758 5254\n              Fax:     +1 732 758 4177\n              E-mail:  kaj@bellcore.com')
if mibBuilder.loadTexts: atmTCMIB.setDescription('This MIB Module provides Textual Conventions\n           and OBJECT-IDENTITY Objects to be used by\n           ATM systems.')
class AtmAddr(TextualConvention, OctetString):
    description = 'An ATM address. The semantics are implied by\n                 the length. The address types are: - no\n                 address (0 octets) - E.164 (8 octets) - NSAP\n                 (20 octets) In addition, when subaddresses\n                 are used the AtmAddr may represent the\n                 concatenation of address and subaddress. The\n                 associated address types are: - E.164, E.164\n                 (16 octets) - E.164, NSAP (28 octets) - NSAP,\n                 NSAP (40 octets) Address lengths other than\n                 defined in this definition imply address\n                 types defined elsewhere.  Note: The E.164\n                 address is encoded in BCD format.'
    status = 'current'
    displayHint = '1x'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 40)

class AtmConnCastType(TextualConvention, Integer32):
    description = 'The type of topology of a connection (point-\n              to-point, point-to-multipoint). In the case\n              of point-to-multipoint, the orientation of\n              this VPL or VCL in the connection.\n              On a host:\n              - p2mpRoot indicates that the host\n                is the root of the p2mp connection.\n              - p2mpLeaf indicates that the host\n                is a leaf of the p2mp connection.\n              On a switch interface:\n              - p2mpRoot indicates that cells received\n                by the switching fabric from the interface\n                are from the root of the p2mp connection.\n              - p2mpLeaf indicates that cells transmitted\n                to the interface from the switching fabric\n                are to the leaf of the p2mp connection.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("p2p", 1), ("p2mpRoot", 2), ("p2mpLeaf", 3))

class AtmConnKind(TextualConvention, Integer32):
    description = 'The type of call control used for an ATM\n                connection at a particular interface. The use\n                is as follows:\n                   pvc(1)\n                      Virtual link of a PVC. Should not be\n                      used for an PVC/SVC (i.e., Soft PVC)\n                      crossconnect.\n                   svcIncoming(2)\n                      Virtual link established after a\n                      received signaling request to setup\n                      an SVC.\n                   svcOutgoing(3)\n                      Virtual link established after a\n                      transmitted or forwarded signaling\n                      request to setup an SVC.\n                   spvcInitiator(4)\n                      Virtual link at the PVC side of an\n                      SVC/PVC crossconnect, where the\n                      switch is the initiator of the Soft PVC\n                      setup.\n                   spvcTarget(5)\n                      Virtual link at the PVC side of an\n                      SVC/PVC crossconnect, where the\n                      switch is the target of the Soft PVC\n                      setup.\n\n                For PVCs, a pvc virtual link is always cross-\n                connected to a pvc virtual link.\n\n                For SVCs, an svcIncoming virtual link is always cross-\n                connected to an svcOutgoing virtual link.\n\nFor Soft PVCs, an spvcInitiator is either cross-connected to\nan svcOutgoing or an spvcTarget, and an spvcTarget is either\ncross-connected to an svcIncoming or an spvcInitiator.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("pvc", 1), ("svcIncoming", 2), ("svcOutgoing", 3), ("spvcInitiator", 4), ("spvcTarget", 5))

class AtmIlmiNetworkPrefix(TextualConvention, OctetString):
    reference = 'ATM Forum, Integrated Local Management Interface\n               (ILMI) Specification, Version 4.0,\n               af-ilmi-0065.000, September 1996, Section 9\n             ATM Forum, ATM User-Network Interface Signalling\n               Specification, Version 4.0 (UNI 4.0),\n               af-sig-0061.000, June 1996, Section 3'
    description = 'A network prefix used for ILMI address\n            registration.  In the case of ATM endsystem\n            addresses (AESAs), the network prefix is the first\n            13 octets of the address which includes the AFI,\n            IDI, and HO-DSP fields.  In the case of native\n            E.164 addresses, the network prefix is the entire\n            E.164 address encoded in 8 octets, as if it were\n            an E.164 IDP in an ATM endsystem address\n            structure.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(8, 8), ValueSizeConstraint(13, 13), )
class AtmInterfaceType(TextualConvention, Integer32):
    description = 'The connection setup procedures used for the\n            identified interface.\n\n            Other: Connection setup procedures other than\n               those listed below.\n\n            Auto-configuration:\n               Indicates that the connection setup\n               procedures are to be determined dynamically,\n               or that determination has not yet been\n               completed. One such mechanism is via ATM\n               Forum ILMI auto-configuration procedures.\n\n            ITU-T DSS2:\n            -  ITU-T Recommendation Q.2931, Broadband\n               Integrated Service Digital Network (B-ISDN)\n               Digital Subscriber Signalling System No.2\n               (DSS2) User-Network Interface (UNI) Layer 3\n               Specification for Basic Call/Connection\n               Control (September 1994)\n            -  ITU-T Draft Recommendation Q.2961,\n               B-ISDN DSS 2 Support of Additional Traffic\n               Parameters (May 1995)\n\n            -  ITU-T Draft Recommendation Q.2971,\n               B-ISDN DSS 2 User Network Interface Layer 3\n               Specification for Point-to-multipoint\n               Call/connection Control (May 1995)\n\n            ATM Forum UNI 3.0:\n               ATM Forum, ATM User-Network Interface,\n               Version 3.0 (UNI 3.0) Specification,\n               (1994).\n\n            ATM Forum UNI 3.1:\n               ATM Forum, ATM User-Network Interface,\n               Version 3.1 (UNI 3.1) Specification,\n               (November 1994).\n\n            ATM Forum UNI Signalling 4.0:\n               ATM Forum, ATM User-Network Interface (UNI)\n               Signalling Specification Version 4.0,\n               af-sig-0061.000 (June 1996).\n\n            ATM Forum IISP (based on UNI 3.0 or UNI 3.1) :\n               Interim Inter-switch Signaling Protocol\n               (IISP) Specification, Version 1.0,\n               af-pnni-0026.000, (December 1994).\n\n            ATM Forum PNNI 1.0 :\n               ATM Forum, Private Network-Network Interface\n               Specification, Version 1.0, af-pnni-0055.000,\n               (March 1996).\n\n            ATM Forum B-ICI:\n               ATM Forum, B-ICI Specification, Version 2.0,\n               af-bici-0013.002, (November 1995).\n\n            ATM Forum UNI PVC Only:\n               An ATM Forum compliant UNI with the\n               signalling disabled.\n            ATM Forum NNI PVC Only:\n               An ATM Forum compliant NNI with the\n               signalling disabled.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13))
    namedValues = NamedValues(("other", 1), ("autoConfig", 2), ("ituDss2", 3), ("atmfUni3Dot0", 4), ("atmfUni3Dot1", 5), ("atmfUni4Dot0", 6), ("atmfIispUni3Dot0", 7), ("atmfIispUni3Dot1", 8), ("atmfIispUni4Dot0", 9), ("atmfPnni1Dot0", 10), ("atmfBici2Dot0", 11), ("atmfUniPvcOnly", 12), ("atmfNniPvcOnly", 13))

class AtmServiceCategory(TextualConvention, Integer32):
    reference = 'ATM Forum Traffic Management Specification,\n            Version 4.0, af-tm-0056.000, June 1996.'
    description = 'The service category for a connection.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("other", 1), ("cbr", 2), ("rtVbr", 3), ("nrtVbr", 4), ("abr", 5), ("ubr", 6))

class AtmSigDescrParamIndex(TextualConvention, Integer32):
    description = 'The value of this object identifies a row in the\n            atmSigDescrParamTable. The value 0 signifies that\n            none of the signalling parameters defined in the\n            atmSigDescrParamTable are applicable.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class AtmTrafficDescrParamIndex(TextualConvention, Integer32):
    description = 'The value of this object identifies a row in the\n            atmTrafficDescrParamTable.  The value 0 signifies\n            that no row has been identified.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class AtmVcIdentifier(TextualConvention, Integer32):
    description = 'The VCI value for a VCL. The maximum VCI value\n            cannot exceed the value allowable by\n            atmInterfaceMaxVciBits defined in ATM-MIB.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 65535)

class AtmVpIdentifier(TextualConvention, Integer32):
    description = 'The VPI value for a VPL or VCL. The value VPI=0\n            is only allowed for a VCL. For ATM UNIs supporting\n            VPCs the VPI value ranges from 0 to 255.  The VPI\n            value 0 is supported for ATM UNIs conforming to\n            the ATM Forum UNI 4.0 Annex 8 (Virtual UNIs)\n            specification. For ATM UNIs supporting VCCs the\n            VPI value ranges from 0 to 255.  For ATM NNIs the\n            VPI value ranges from 0 to 4095.  The maximum VPI\n            value cannot exceed the value allowable by\n            atmInterfaceMaxVpiBits defined in ATM-MIB.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 4095)

class AtmVorXAdminStatus(TextualConvention, Integer32):
    description = 'The value determines the desired administrative\n            status of a virtual link or cross-connect. The up\n            and down states indicate that the traffic flow is\n            enabled or disabled respectively on the virtual\n            link or cross-connect.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("up", 1), ("down", 2))

class AtmVorXLastChange(TextualConvention, TimeTicks):
    description = "The value of MIB II's sysUpTime at the time a\n            virtual link or cross-connect entered its current\n            operational state. If the current state was\n            entered prior to the last re-initialization of the\n            agent then this object contains a zero value."
    status = 'current'

class AtmVorXOperStatus(TextualConvention, Integer32):
    description = 'The value determines the operational status of a\n            virtual link or cross-connect. The up and down\n            states indicate that the traffic flow is enabled\n            or disabled respectively on the virtual link or\n            cross-connect. The unknown state indicates that\n            the state of it cannot be determined. The state\n            will be down or unknown if the supporting ATM\n            interface(s) is down or unknown respectively.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("up", 1), ("down", 2), ("unknown", 3))

atmTrafficDescriptorTypes = MibIdentifier((1, 3, 6, 1, 2, 1, 37, 1, 1))
atmObjectIdentities = MibIdentifier((1, 3, 6, 1, 2, 1, 37, 3, 1))
atmNoTrafficDescriptor = ObjectIdentity((1, 3, 6, 1, 2, 1, 37, 1, 1, 1))
if mibBuilder.loadTexts: atmNoTrafficDescriptor.setStatus('deprecated')
if mibBuilder.loadTexts: atmNoTrafficDescriptor.setDescription('This identifies the no ATM traffic\n        descriptor type.  Parameters 1, 2, 3, 4,\n        and 5 are not used.  This traffic descriptor\n        type can be used for best effort traffic.')
atmNoClpNoScr = ObjectIdentity((1, 3, 6, 1, 2, 1, 37, 1, 1, 2))
if mibBuilder.loadTexts: atmNoClpNoScr.setStatus('current')
if mibBuilder.loadTexts: atmNoClpNoScr.setDescription('This traffic descriptor type is for no CLP\n        and no Sustained Cell Rate.  The use of the\n        parameter vector for this type:\n        Parameter 1: peak cell rate in cells/second\n                     for CLP=0+1 traffic\n        Parameter 2: not used\n        Parameter 3: not used\n        Parameter 4: not used\n        Parameter 5: not used.')
if mibBuilder.loadTexts: atmNoClpNoScr.setReference('ATM Forum,ATM User-Network Interface,\n           Version 3.0 (UNI 3.0) Specification, 1994.\n         ATM Forum, ATM User-Network Interface,\n           Version 3.1 (UNI 3.1) Specification,\n           November 1994.')
atmClpNoTaggingNoScr = ObjectIdentity((1, 3, 6, 1, 2, 1, 37, 1, 1, 3))
if mibBuilder.loadTexts: atmClpNoTaggingNoScr.setStatus('deprecated')
if mibBuilder.loadTexts: atmClpNoTaggingNoScr.setDescription('This traffic descriptor is for CLP without\n        tagging and no Sustained Cell Rate.  The use\n        of the parameter vector for this type:\n        Parameter 1: peak cell rate in cells/second\n                     for CLP=0+1 traffic\n        Parameter 2: peak cell rate in cells/second\n                     for CLP=0 traffic\n        Parameter 3: not used\n        Parameter 4: not used\n        Parameter 5: not used.')
atmClpTaggingNoScr = ObjectIdentity((1, 3, 6, 1, 2, 1, 37, 1, 1, 4))
if mibBuilder.loadTexts: atmClpTaggingNoScr.setStatus('deprecated')
if mibBuilder.loadTexts: atmClpTaggingNoScr.setDescription('This traffic descriptor is for CLP with\n        tagging and no Sustained Cell Rate.  The use\n        of the parameter vector for this type:\n        Parameter 1: peak cell rate in cells/second\n                     for CLP=0+1 traffic\n        Parameter 2: peak cell rate in cells/second\n                     for CLP=0 traffic, excess\n                     tagged as CLP=1\n        Parameter 3: not used\n        Parameter 4: not used\n        Parameter 5: not used.')
atmNoClpScr = ObjectIdentity((1, 3, 6, 1, 2, 1, 37, 1, 1, 5))
if mibBuilder.loadTexts: atmNoClpScr.setStatus('current')
if mibBuilder.loadTexts: atmNoClpScr.setDescription('This traffic descriptor type is for no CLP\n        with Sustained Cell Rate.  The use of the\n        parameter vector for this type:\n        Parameter 1: peak cell rate in cells/second\n                     for CLP=0+1 traffic\n        Parameter 2: sustainable cell rate in cells/second\n                     for CLP=0+1 traffic\n        Parameter 3: maximum burst size in cells\n        Parameter 4: not used\n        Parameter 5: not used.')
if mibBuilder.loadTexts: atmNoClpScr.setReference('ATM Forum,ATM User-Network Interface,\n           Version 3.0 (UNI 3.0) Specification, 1994.\n         ATM Forum, ATM User-Network Interface,\n           Version 3.1 (UNI 3.1) Specification,\n           November 1994.')
atmClpNoTaggingScr = ObjectIdentity((1, 3, 6, 1, 2, 1, 37, 1, 1, 6))
if mibBuilder.loadTexts: atmClpNoTaggingScr.setStatus('current')
if mibBuilder.loadTexts: atmClpNoTaggingScr.setDescription('This traffic descriptor type is for CLP with\n        Sustained Cell Rate and no tagging.  The use\n        of the parameter vector for this type:\n        Parameter 1: peak cell rate in cells/second\n                     for CLP=0+1 traffic\n        Parameter 2: sustainable cell rate in cells/second\n                     for CLP=0 traffic\n        Parameter 3: maximum burst size in cells\n        Parameter 4: not used\n        Parameter 5: not used.')
if mibBuilder.loadTexts: atmClpNoTaggingScr.setReference('ATM Forum,ATM User-Network Interface,\n           Version 3.0 (UNI 3.0) Specification, 1994.\n         ATM Forum, ATM User-Network Interface,\n           Version 3.1 (UNI 3.1) Specification,\n           November 1994.')
atmClpTaggingScr = ObjectIdentity((1, 3, 6, 1, 2, 1, 37, 1, 1, 7))
if mibBuilder.loadTexts: atmClpTaggingScr.setStatus('current')
if mibBuilder.loadTexts: atmClpTaggingScr.setDescription('This traffic descriptor type is for CLP with\n        tagging and Sustained Cell Rate.  The use of\n        the parameter vector for this type:\n        Parameter 1: peak cell rate in cells/second\n                     for CLP=0+1 traffic\n        Parameter 2: sustainable cell rate in cells/second\n                     for CLP=0 traffic, excess tagged as\n                     CLP=1\n        Parameter 3: maximum burst size in cells\n        Parameter 4: not used\n        Parameter 5: not used.')
if mibBuilder.loadTexts: atmClpTaggingScr.setReference('ATM Forum,ATM User-Network Interface,\n           Version 3.0 (UNI 3.0) Specification, 1994.\n         ATM Forum, ATM User-Network Interface,\n           Version 3.1 (UNI 3.1) Specification,\n           November 1994.')
atmClpNoTaggingMcr = ObjectIdentity((1, 3, 6, 1, 2, 1, 37, 1, 1, 8))
if mibBuilder.loadTexts: atmClpNoTaggingMcr.setStatus('current')
if mibBuilder.loadTexts: atmClpNoTaggingMcr.setDescription('This traffic descriptor type is for CLP with\n        Minimum Cell Rate and no tagging.  The use of\n        the parameter vector for this type:\n        Parameter 1: peak cell rate in cells/second\n                     for CLP=0+1 traffic\n        Parameter 2: CDVT in tenths of microseconds\n        Parameter 3: minimum cell rate in cells/second\n        Parameter 4: unused\n        Parameter 5: unused.')
if mibBuilder.loadTexts: atmClpNoTaggingMcr.setReference('ATM Forum,ATM User-Network Interface,\n           Version 3.0 (UNI 3.0) Specification, 1994.\n         ATM Forum, ATM User-Network Interface,\n           Version 3.1 (UNI 3.1) Specification,\n           November 1994.')
atmClpTransparentNoScr = ObjectIdentity((1, 3, 6, 1, 2, 1, 37, 1, 1, 9))
if mibBuilder.loadTexts: atmClpTransparentNoScr.setStatus('current')
if mibBuilder.loadTexts: atmClpTransparentNoScr.setDescription('This traffic descriptor type is for the CLP-\n        transparent model and no Sustained Cell Rate.\n        The use of the parameter vector for this type:\n        Parameter 1: peak cell rate in cells/second\n                     for CLP=0+1 traffic\n        Parameter 2: CDVT in tenths of microseconds\n        Parameter 3: not used\n        Parameter 4: not used\n        Parameter 5: not used.\n\n        This traffic descriptor type is applicable to\n        connections following the CBR.1 conformance\n        definition.\n\n        Connections specifying this traffic descriptor\n        type will be rejected at UNI 3.0 or UNI 3.1\n        interfaces.  For a similar traffic descriptor\n        type that can be accepted at UNI 3.0 and\n        UNI 3.1 interfaces, see atmNoClpNoScr.')
if mibBuilder.loadTexts: atmClpTransparentNoScr.setReference('ATM Forum,ATM User-Network Interface,\n           Version 3.0 (UNI 3.0) Specification, 1994.\n         ATM Forum, ATM User-Network Interface,\n           Version 3.1 (UNI 3.1) Specification,\n           November 1994.\n         ATM Forum, Traffic Management Specification,\n           Version 4.0, af-tm-0056.000, June 1996.')
atmClpTransparentScr = ObjectIdentity((1, 3, 6, 1, 2, 1, 37, 1, 1, 10))
if mibBuilder.loadTexts: atmClpTransparentScr.setStatus('current')
if mibBuilder.loadTexts: atmClpTransparentScr.setDescription('This traffic descriptor type is for the CLP-\n        transparent model with Sustained Cell Rate.\n        The use of the parameter vector for this type:\n        Parameter 1: peak cell rate in cells/second\n                     for CLP=0+1 traffic\n        Parameter 2: sustainable cell rate in cells/second\n                     for CLP=0+1 traffic\n        Parameter 3: maximum burst size in cells\n        Parameter 4: CDVT in tenths of microseconds\n        Parameter 5: not used.\n\n        This traffic descriptor type is applicable to\n        connections following the VBR.1 conformance\n        definition.\n\n        Connections specifying this traffic descriptor\n        type will be rejected at UNI 3.0 or UNI 3.1\n        interfaces.  For a similar traffic descriptor\n        type that can be accepted at UNI 3.0 and\n        UNI 3.1 interfaces, see atmNoClpScr.')
if mibBuilder.loadTexts: atmClpTransparentScr.setReference('ATM Forum,ATM User-Network Interface,\n           Version 3.0 (UNI 3.0) Specification, 1994.\n         ATM Forum, ATM User-Network Interface,\n           Version 3.1 (UNI 3.1) Specification,\n           November 1994.\n         ATM Forum, Traffic Management Specification,\n           Version 4.0, af-tm-0056.000, June 1996.')
atmNoClpTaggingNoScr = ObjectIdentity((1, 3, 6, 1, 2, 1, 37, 1, 1, 11))
if mibBuilder.loadTexts: atmNoClpTaggingNoScr.setStatus('current')
if mibBuilder.loadTexts: atmNoClpTaggingNoScr.setDescription('This traffic descriptor type is for no CLP\n        with tagging and no Sustained Cell Rate.  The\n        use of the parameter vector for this type:\n        Parameter 1: peak cell rate in cells/second\n                     for CLP=0+1 traffic\n        Parameter 2: CDVT in tenths of microseconds\n        Parameter 3: not used\n        Parameter 4: not used\n        Parameter 5: not used.\n\n        This traffic descriptor type is applicable to\n        connections following the UBR.2 conformance\n        definition .')
if mibBuilder.loadTexts: atmNoClpTaggingNoScr.setReference('ATM Forum,ATM User-Network Interface,\n           Version 3.0 (UNI 3.0) Specification, 1994.\n         ATM Forum, ATM User-Network Interface,\n           Version 3.1 (UNI 3.1) Specification,\n           November 1994.\n         ATM Forum, Traffic Management Specification,\n           Version 4.0, af-tm-0056.000, June 1996.')
atmNoClpNoScrCdvt = ObjectIdentity((1, 3, 6, 1, 2, 1, 37, 1, 1, 12))
if mibBuilder.loadTexts: atmNoClpNoScrCdvt.setStatus('current')
if mibBuilder.loadTexts: atmNoClpNoScrCdvt.setDescription('This traffic descriptor type is for no CLP\n        and no Sustained Cell Rate.  The use of the\n        parameter vector for this type:\n        Parameter 1: peak cell rate in cells/second\n                     for CLP=0+1 traffic\n        Parameter 2: CDVT in tenths of microseconds\n        Parameter 3: not used\n        Parameter 4: not used\n        Parameter 5: not used.\n\n        This traffic descriptor type is applicable to\n        CBR connections following the UNI 3.0/3.1\n        conformance definition for PCR CLP=0+1.\n        These CBR connections differ from CBR.1\n        connections in that the CLR objective\n        applies only to the CLP=0 cell flow.\n\n        This traffic descriptor type is also\n        applicable to connections following the UBR.1\n        conformance definition.')
if mibBuilder.loadTexts: atmNoClpNoScrCdvt.setReference('ATM Forum,ATM User-Network Interface,\n           Version 3.0 (UNI 3.0) Specification, 1994.\n         ATM Forum, ATM User-Network Interface,\n           Version 3.1 (UNI 3.1) Specification,\n           November 1994.\n         ATM Forum, Traffic Management Specification,\n           Version 4.0, af-tm-0056.000, June 1996.')
atmNoClpScrCdvt = ObjectIdentity((1, 3, 6, 1, 2, 1, 37, 1, 1, 13))
if mibBuilder.loadTexts: atmNoClpScrCdvt.setStatus('current')
if mibBuilder.loadTexts: atmNoClpScrCdvt.setDescription('This traffic descriptor type is for no CLP\n        with Sustained Cell Rate.  The use of the\n        parameter vector for this type:\n        Parameter 1: peak cell rate in cells/second\n                     for CLP=0+1 traffic\n        Parameter 2: sustainable cell rate in cells/second\n                     for CLP=0+1 traffic\n        Parameter 3: maximum burst size in cells\n        Parameter 4: CDVT in tenths of microseconds\n        Parameter 5: not used.\n\n        This traffic descriptor type is applicable\n        to VBR connections following the UNI 3.0/3.1\n        conformance definition for PCR CLP=0+1 and\n        SCR CLP=0+1.  These VBR connections\n        differ from VBR.1 connections in that\n        the CLR objective applies only to the CLP=0\n        cell flow.')
if mibBuilder.loadTexts: atmNoClpScrCdvt.setReference('ATM Forum,ATM User-Network Interface,\n           Version 3.0 (UNI 3.0) Specification, 1994.\n         ATM Forum, ATM User-Network Interface,\n           Version 3.1 (UNI 3.1) Specification,\n           November 1994.\n         ATM Forum, Traffic Management Specification,\n           Version 4.0, af-tm-0056.000, June 1996.')
atmClpNoTaggingScrCdvt = ObjectIdentity((1, 3, 6, 1, 2, 1, 37, 1, 1, 14))
if mibBuilder.loadTexts: atmClpNoTaggingScrCdvt.setStatus('current')
if mibBuilder.loadTexts: atmClpNoTaggingScrCdvt.setDescription('This traffic descriptor type is for CLP with\n        Sustained Cell Rate and no tagging.  The use\n        of the parameter vector for this type:\n        Parameter 1: peak cell rate in cells/second\n                     for CLP=0+1 traffic\n        Parameter 2: sustainable cell rate in cells/second\n                     for CLP=0 traffic\n        Parameter 3: maximum burst size in cells\n        Parameter 4: CDVT in tenths of microseconds\n        Parameter 5: not used.\n\n        This traffic descriptor type is applicable to\n        connections following the VBR.2 conformance\n        definition.')
if mibBuilder.loadTexts: atmClpNoTaggingScrCdvt.setReference('ATM Forum,ATM User-Network Interface,\n           Version 3.0 (UNI 3.0) Specification, 1994.\n         ATM Forum, ATM User-Network Interface,\n           Version 3.1 (UNI 3.1) Specification,\n           November 1994.\n         ATM Forum, Traffic Management Specification,\n           Version 4.0, af-tm-0056.000, June 1996.')
atmClpTaggingScrCdvt = ObjectIdentity((1, 3, 6, 1, 2, 1, 37, 1, 1, 15))
if mibBuilder.loadTexts: atmClpTaggingScrCdvt.setStatus('current')
if mibBuilder.loadTexts: atmClpTaggingScrCdvt.setDescription('This traffic descriptor type is for CLP with\n        tagging and Sustained Cell Rate.  The use of\n        the parameter vector for this type:\n        Parameter 1: peak cell rate in cells/second\n                     for CLP=0+1 traffic\n        Parameter 2: sustainable cell rate in cells/second\n                     for CLP=0 traffic, excess tagged as\n                     CLP=1\n        Parameter 3: maximum burst size in cells\n        Parameter 4: CDVT in tenths of microseconds\n        Parameter 5: not used.\n\n        This traffic descriptor type is applicable to\n        connections following the VBR.3 conformance\n        definition.')
if mibBuilder.loadTexts: atmClpTaggingScrCdvt.setReference('ATM Forum,ATM User-Network Interface,\n           Version 3.0 (UNI 3.0) Specification, 1994.\n         ATM Forum, ATM User-Network Interface,\n           Version 3.1 (UNI 3.1) Specification,\n           November 1994.\n         ATM Forum, Traffic Management Specification,\n           Version 4.0, af-tm-0056.000, June 1996.')
mibBuilder.exportSymbols("ATM-TC-MIB", AtmAddr=AtmAddr, atmNoClpScrCdvt=atmNoClpScrCdvt, atmNoClpNoScr=atmNoClpNoScr, atmClpTaggingScrCdvt=atmClpTaggingScrCdvt, atmClpNoTaggingNoScr=atmClpNoTaggingNoScr, atmClpNoTaggingScrCdvt=atmClpNoTaggingScrCdvt, AtmInterfaceType=AtmInterfaceType, AtmServiceCategory=AtmServiceCategory, atmTrafficDescriptorTypes=atmTrafficDescriptorTypes, atmClpTransparentNoScr=atmClpTransparentNoScr, AtmVorXLastChange=AtmVorXLastChange, AtmVpIdentifier=AtmVpIdentifier, atmNoTrafficDescriptor=atmNoTrafficDescriptor, AtmIlmiNetworkPrefix=AtmIlmiNetworkPrefix, atmNoClpScr=atmNoClpScr, atmClpNoTaggingScr=atmClpNoTaggingScr, atmClpTransparentScr=atmClpTransparentScr, atmTCMIB=atmTCMIB, atmNoClpNoScrCdvt=atmNoClpNoScrCdvt, AtmConnKind=AtmConnKind, AtmSigDescrParamIndex=AtmSigDescrParamIndex, atmNoClpTaggingNoScr=atmNoClpTaggingNoScr, atmClpTaggingScr=atmClpTaggingScr, atmClpNoTaggingMcr=atmClpNoTaggingMcr, atmObjectIdentities=atmObjectIdentities, atmClpTaggingNoScr=atmClpTaggingNoScr, AtmTrafficDescrParamIndex=AtmTrafficDescrParamIndex, PYSNMP_MODULE_ID=atmTCMIB, AtmConnCastType=AtmConnCastType, AtmVcIdentifier=AtmVcIdentifier, AtmVorXOperStatus=AtmVorXOperStatus, AtmVorXAdminStatus=AtmVorXAdminStatus)
