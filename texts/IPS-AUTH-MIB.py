#
# PySNMP MIB module IPS-AUTH-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/equallogic/IPS-AUTH-MIB
# Produced by pysmi-1.1.3 at Sun Nov 28 20:18:06 2021
# On host fv-az77-612 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Unsigned32, NotificationType, Gauge32, IpAddress, Integer32, Bits, MibIdentifier, iso, ModuleIdentity, experimental, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Counter32, TimeTicks, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "NotificationType", "Gauge32", "IpAddress", "Integer32", "Bits", "MibIdentifier", "iso", "ModuleIdentity", "experimental", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Counter32", "TimeTicks", "ObjectIdentity")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
ipsAuthModule = ModuleIdentity((1, 3, 6, 1, 3, 99999))
ipsAuthModule.setRevisions(('2002-06-26 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ipsAuthModule.setRevisionsDescriptions(('Initial revision published as RFC xxxx.',))
if mibBuilder.loadTexts: ipsAuthModule.setLastUpdated('200206260000Z')
if mibBuilder.loadTexts: ipsAuthModule.setOrganization('IETF IPS Working Group')
if mibBuilder.loadTexts: ipsAuthModule.setContactInfo('\n    Mark Bakke\n    Postal: Cisco Systems, Inc\n    6450 Wedgwood Road, Suite 130\n    Maple Grove, MN\n    USA 55311\n\n    Tel: +1 763-398-1000\n    Fax: +1 763-398-1001\n\n    E-mail: mbakke@cisco.com')
if mibBuilder.loadTexts: ipsAuthModule.setDescription('The IP Storage Authorization MIB module.')
ipsAuthObjects = MibIdentifier((1, 3, 6, 1, 3, 99999, 1))
ipsAuthNotifications = MibIdentifier((1, 3, 6, 1, 3, 99999, 2))
ipsAuthConformance = MibIdentifier((1, 3, 6, 1, 3, 99999, 3))
class IpsAuthAddress(TextualConvention, OctetString):
    reference = 'IANA-ADDRESS-FAMILY-NUMBERS-MIB;\n         INET-ADDRESS-MIB (RFC 2851);\n         Fibre Channel Management MIB (presently defined in\n         draft-ietf-ips-fcmgmt-mib-01.txt).'
    description = 'IP Storage requires the use of address information\n        that uses not only the InetAddress type defined in the\n     INET-ADDRESS-MIB, but also Fibre Channel type defined\n        in the Fibre Channel Management MIB. Although these\n        address types are recognized in the IANA Address Family\n        Numbers MIB, the addressing mechanisms have not been\n        merged into a well-known, common type. This data type,\n        the IpsAuthAddress, performs this function for this MIB.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

ipsAuthDescriptors = MibIdentifier((1, 3, 6, 1, 3, 99999, 1, 1))
ipsAuthMethodTypes = MibIdentifier((1, 3, 6, 1, 3, 99999, 1, 1, 1))
ipsAuthMethodNone = ObjectIdentity((1, 3, 6, 1, 3, 99999, 1, 1, 1, 1))
if mibBuilder.loadTexts: ipsAuthMethodNone.setStatus('current')
if mibBuilder.loadTexts: ipsAuthMethodNone.setDescription('The authoritative identifier when no authentication\n     method is used.')
if mibBuilder.loadTexts: ipsAuthMethodNone.setReference('iSCSI Protocol Specification.')
ipsAuthMethodSrp = ObjectIdentity((1, 3, 6, 1, 3, 99999, 1, 1, 1, 2))
if mibBuilder.loadTexts: ipsAuthMethodSrp.setStatus('current')
if mibBuilder.loadTexts: ipsAuthMethodSrp.setDescription('The authoritative identifier when the authentication\n\n\n\n     method is SRP.')
if mibBuilder.loadTexts: ipsAuthMethodSrp.setReference('iSCSI Protocol Specification.')
ipsAuthMethodChap = ObjectIdentity((1, 3, 6, 1, 3, 99999, 1, 1, 1, 3))
if mibBuilder.loadTexts: ipsAuthMethodChap.setStatus('current')
if mibBuilder.loadTexts: ipsAuthMethodChap.setDescription('The authoritative identifier when the authentication\n     method is CHAP.')
if mibBuilder.loadTexts: ipsAuthMethodChap.setReference('iSCSI Protocol Specification.')
ipsAuthInstance = MibIdentifier((1, 3, 6, 1, 3, 99999, 1, 2))
ipsAuthInstanceAttributesTable = MibTable((1, 3, 6, 1, 3, 99999, 1, 2, 2), )
if mibBuilder.loadTexts: ipsAuthInstanceAttributesTable.setStatus('current')
if mibBuilder.loadTexts: ipsAuthInstanceAttributesTable.setDescription('A Dynamic list of iSCSI instances present on the system.')
ipsAuthInstanceAttributesEntry = MibTableRow((1, 3, 6, 1, 3, 99999, 1, 2, 2, 1), ).setIndexNames((0, "IPS-AUTH-MIB", "ipsAuthInstIndex"))
if mibBuilder.loadTexts: ipsAuthInstanceAttributesEntry.setStatus('current')
if mibBuilder.loadTexts: ipsAuthInstanceAttributesEntry.setDescription('An entry (row) containing managment information applicable\n        to a particular iSCSI instance.')
ipsAuthInstIndex = MibTableColumn((1, 3, 6, 1, 3, 99999, 1, 2, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: ipsAuthInstIndex.setStatus('current')
if mibBuilder.loadTexts: ipsAuthInstIndex.setDescription('An arbitrary integer used to uniquely identify a particular\n        authentication instance.')
ipsAuthInstDescr = MibTableColumn((1, 3, 6, 1, 3, 99999, 1, 2, 2, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipsAuthInstDescr.setStatus('current')
if mibBuilder.loadTexts: ipsAuthInstDescr.setDescription('An octet string, determined by the implementation to describe\n     the authentication instance.  When only a single instance is present,\n     this object may be set to the zero-length string; with multiple\n     authentication instances, it may be used in an implementation-dependent\n     manner to describe the purpose of the respective instance.')
ipsAuthIdentity = MibIdentifier((1, 3, 6, 1, 3, 99999, 1, 3))
ipsAuthIdentAttributesTable = MibTable((1, 3, 6, 1, 3, 99999, 1, 3, 1), )
if mibBuilder.loadTexts: ipsAuthIdentAttributesTable.setStatus('current')
if mibBuilder.loadTexts: ipsAuthIdentAttributesTable.setDescription('A list of user identities, each belonging to a particular\n     ipsAuthInstance.')
ipsAuthIdentAttributesEntry = MibTableRow((1, 3, 6, 1, 3, 99999, 1, 3, 1, 1), ).setIndexNames((0, "IPS-AUTH-MIB", "ipsAuthInstIndex"), (0, "IPS-AUTH-MIB", "ipsAuthIdentIndex"))
if mibBuilder.loadTexts: ipsAuthIdentAttributesEntry.setStatus('current')
if mibBuilder.loadTexts: ipsAuthIdentAttributesEntry.setDescription('An entry (row) containing management information\n        describing a user identity\n        within an authentication instance on this node.')
ipsAuthIdentIndex = MibTableColumn((1, 3, 6, 1, 3, 99999, 1, 3, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: ipsAuthIdentIndex.setStatus('current')
if mibBuilder.loadTexts: ipsAuthIdentIndex.setDescription('An arbitrary integer used to uniquely identify a particular\n        identity instance within an authentication instance present\n     on the node.')
ipsAuthIdentDescription = MibTableColumn((1, 3, 6, 1, 3, 99999, 1, 3, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsAuthIdentDescription.setStatus('current')
if mibBuilder.loadTexts: ipsAuthIdentDescription.setDescription('An octet string describing this particular identity.')
ipsAuthIdentRowStatus = MibTableColumn((1, 3, 6, 1, 3, 99999, 1, 3, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsAuthIdentRowStatus.setStatus('current')
if mibBuilder.loadTexts: ipsAuthIdentRowStatus.setDescription('This field allows entries to be dynamically added and\n     removed from this table via SNMP.')
ipsAuthIdentityName = MibIdentifier((1, 3, 6, 1, 3, 99999, 1, 4))
ipsAuthIdentNameAttributesTable = MibTable((1, 3, 6, 1, 3, 99999, 1, 4, 1), )
if mibBuilder.loadTexts: ipsAuthIdentNameAttributesTable.setStatus('current')
if mibBuilder.loadTexts: ipsAuthIdentNameAttributesTable.setDescription('A list of unique names that can be used to positively\n     identify a particular user identity.')
ipsAuthIdentNameAttributesEntry = MibTableRow((1, 3, 6, 1, 3, 99999, 1, 4, 1, 1), ).setIndexNames((0, "IPS-AUTH-MIB", "ipsAuthInstIndex"), (0, "IPS-AUTH-MIB", "ipsAuthIdentIndex"), (0, "IPS-AUTH-MIB", "ipsAuthIdentNameIndex"))
if mibBuilder.loadTexts: ipsAuthIdentNameAttributesEntry.setStatus('current')
if mibBuilder.loadTexts: ipsAuthIdentNameAttributesEntry.setDescription('An entry (row) containing management information\n        applicable to a unique identity name which can be used\n     to uniquely identify a user identity within a particular\n     authentication instance.')
ipsAuthIdentNameIndex = MibTableColumn((1, 3, 6, 1, 3, 99999, 1, 4, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: ipsAuthIdentNameIndex.setStatus('current')
if mibBuilder.loadTexts: ipsAuthIdentNameIndex.setDescription('An arbitrary integer used to uniquely identify a particular\n        identity name instance within an ipsAuthIdentity within an\n     authentication instance.')
ipsAuthIdentName = MibTableColumn((1, 3, 6, 1, 3, 99999, 1, 4, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsAuthIdentName.setStatus('current')
if mibBuilder.loadTexts: ipsAuthIdentName.setDescription('A character string which is the unique name of an\n     identity that may be used to identify this\n     ipsAuthIdent entry.')
ipsAuthIdentNameRowStatus = MibTableColumn((1, 3, 6, 1, 3, 99999, 1, 4, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsAuthIdentNameRowStatus.setStatus('current')
if mibBuilder.loadTexts: ipsAuthIdentNameRowStatus.setDescription('This field allows entries to be dynamically added and\n     removed from this table via SNMP.')
ipsAuthIdentityAddress = MibIdentifier((1, 3, 6, 1, 3, 99999, 1, 5))
ipsAuthIdentAddrAttributesTable = MibTable((1, 3, 6, 1, 3, 99999, 1, 5, 1), )
if mibBuilder.loadTexts: ipsAuthIdentAddrAttributesTable.setStatus('current')
if mibBuilder.loadTexts: ipsAuthIdentAddrAttributesTable.setDescription('A list of address ranges that are allowed to serve\n\n\n\n     as the endpoint addresses of a particular identity.\n     An address range includes a starting and ending address\n     and an optional netmask, and an address type indicator,\n     which can specify whether the address is IPv4, IPv6,\n     FC-WWPN, or FC-WWNN.')
ipsAuthIdentAddrAttributesEntry = MibTableRow((1, 3, 6, 1, 3, 99999, 1, 5, 1, 1), ).setIndexNames((0, "IPS-AUTH-MIB", "ipsAuthInstIndex"), (0, "IPS-AUTH-MIB", "ipsAuthIdentIndex"), (0, "IPS-AUTH-MIB", "ipsAuthIdentAddrIndex"))
if mibBuilder.loadTexts: ipsAuthIdentAddrAttributesEntry.setStatus('current')
if mibBuilder.loadTexts: ipsAuthIdentAddrAttributesEntry.setDescription('An entry (row) containing management information\n        applicable to an address range which is used as part\n     of the authentication of an identity\n        within an authentication instance on this node.')
ipsAuthIdentAddrIndex = MibTableColumn((1, 3, 6, 1, 3, 99999, 1, 5, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: ipsAuthIdentAddrIndex.setStatus('current')
if mibBuilder.loadTexts: ipsAuthIdentAddrIndex.setDescription('An arbitrary integer used to uniquely identify a particular\n        ipsAuthIdentAddress instance within an ipsAuthIdentity within an\n     authentication instance present on the node.')
ipsAuthIdentAddrType = MibTableColumn((1, 3, 6, 1, 3, 99999, 1, 5, 1, 1, 2), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsAuthIdentAddrType.setStatus('current')
if mibBuilder.loadTexts: ipsAuthIdentAddrType.setDescription('The type of Address in the ipsAuthIdentAddress start, end,\n     and mask fields.  This type is taken from the IANA address\n     family types; more types may be registered independently\n     of this MIB.')
ipsAuthIdentAddrStart = MibTableColumn((1, 3, 6, 1, 3, 99999, 1, 5, 1, 1, 3), IpsAuthAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsAuthIdentAddrStart.setStatus('current')
if mibBuilder.loadTexts: ipsAuthIdentAddrStart.setDescription('The starting address of the allowed address range.')
ipsAuthIdentAddrEnd = MibTableColumn((1, 3, 6, 1, 3, 99999, 1, 5, 1, 1, 4), IpsAuthAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsAuthIdentAddrEnd.setStatus('current')
if mibBuilder.loadTexts: ipsAuthIdentAddrEnd.setDescription('The ending address of the allowed address range.  If the\n         ipsAuthIdentAddrEntry specifies a single address, this shall\n         match the ipsAuthIdentAddrStart.')
ipsAuthIdentAddrRowStatus = MibTableColumn((1, 3, 6, 1, 3, 99999, 1, 5, 1, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsAuthIdentAddrRowStatus.setStatus('current')
if mibBuilder.loadTexts: ipsAuthIdentAddrRowStatus.setDescription('This field allows entries to be dynamically added and\n     removed from this table via SNMP.')
ipsAuthCredential = MibIdentifier((1, 3, 6, 1, 3, 99999, 1, 6))
ipsAuthCredentialAttributesTable = MibTable((1, 3, 6, 1, 3, 99999, 1, 6, 1), )
if mibBuilder.loadTexts: ipsAuthCredentialAttributesTable.setStatus('current')
if mibBuilder.loadTexts: ipsAuthCredentialAttributesTable.setDescription('A list of credentials related to user identities\n     that are allowed as valid authenticators of the\n     particular identity.')
ipsAuthCredentialAttributesEntry = MibTableRow((1, 3, 6, 1, 3, 99999, 1, 6, 1, 1), ).setIndexNames((0, "IPS-AUTH-MIB", "ipsAuthInstIndex"), (0, "IPS-AUTH-MIB", "ipsAuthIdentIndex"), (0, "IPS-AUTH-MIB", "ipsAuthCredIndex"))
if mibBuilder.loadTexts: ipsAuthCredentialAttributesEntry.setStatus('current')
if mibBuilder.loadTexts: ipsAuthCredentialAttributesEntry.setDescription('An entry (row) containing management information\n        applicable to a credential which authenticates a user\n        identity within an authentication instance.')
ipsAuthCredIndex = MibTableColumn((1, 3, 6, 1, 3, 99999, 1, 6, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: ipsAuthCredIndex.setStatus('current')
if mibBuilder.loadTexts: ipsAuthCredIndex.setDescription('An arbitrary integer used to uniquely identify a particular\n        iSCSI Credential instance within an iSCSI instance present on the\n        node.')
ipsAuthCredAuthMethod = MibTableColumn((1, 3, 6, 1, 3, 99999, 1, 6, 1, 1, 2), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsAuthCredAuthMethod.setStatus('current')
if mibBuilder.loadTexts: ipsAuthCredAuthMethod.setDescription('This object contains an OBJECT IDENTIFIER\n     which identifies the authentication method\n     used with this credential.\n\n     Some standardized values for this object are defined\n     within the ipsAuthMethods subtree.')
ipsAuthCredRowStatus = MibTableColumn((1, 3, 6, 1, 3, 99999, 1, 6, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsAuthCredRowStatus.setStatus('current')
if mibBuilder.loadTexts: ipsAuthCredRowStatus.setDescription('This field allows entries to be dynamically added and\n     removed from this table via SNMP.')
ipsAuthCredChap = MibIdentifier((1, 3, 6, 1, 3, 99999, 1, 7))
ipsAuthCredChapAttributesTable = MibTable((1, 3, 6, 1, 3, 99999, 1, 7, 1), )
if mibBuilder.loadTexts: ipsAuthCredChapAttributesTable.setStatus('current')
if mibBuilder.loadTexts: ipsAuthCredChapAttributesTable.setDescription('A list of CHAP attributes for credentials that\n     have their ipsAuthCredAuthMethod == ipsAuthMethodChap.\n     -ReplicateOnCreate')
ipsAuthCredChapAttributesEntry = MibTableRow((1, 3, 6, 1, 3, 99999, 1, 7, 1, 1), ).setIndexNames((0, "IPS-AUTH-MIB", "ipsAuthInstIndex"), (0, "IPS-AUTH-MIB", "ipsAuthIdentIndex"), (0, "IPS-AUTH-MIB", "ipsAuthCredIndex"))
if mibBuilder.loadTexts: ipsAuthCredChapAttributesEntry.setStatus('current')
if mibBuilder.loadTexts: ipsAuthCredChapAttributesEntry.setDescription('An entry (row) containing management information\n        applicable to a credential which has the ipsAuthCredAuthMethod\n     set to the OID of ipsAuthMethodChap.')
ipsAuthCredChapUserName = MibTableColumn((1, 3, 6, 1, 3, 99999, 1, 7, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsAuthCredChapUserName.setStatus('current')
if mibBuilder.loadTexts: ipsAuthCredChapUserName.setDescription('EQL-SECONDARY-KEY\n         An octet string containing the CHAP user name for this\n     credential.')
ipsAuthCredChapPassword = MibTableColumn((1, 3, 6, 1, 3, 99999, 1, 7, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsAuthCredChapPassword.setStatus('current')
if mibBuilder.loadTexts: ipsAuthCredChapPassword.setDescription('An octet string containing the password for this\n     credential.  If written, it changes the password for\n     the credential.  If read, it returns a zero-length\n     string.')
ipsAuthCredChapRowStatus = MibTableColumn((1, 3, 6, 1, 3, 99999, 1, 7, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsAuthCredChapRowStatus.setStatus('current')
if mibBuilder.loadTexts: ipsAuthCredChapRowStatus.setDescription('This field allows entries to be dynamically added and\n     removed from this table via SNMP.')
ipsAuthCredSrp = MibIdentifier((1, 3, 6, 1, 3, 99999, 1, 8))
ipsAuthCredSrpAttributesTable = MibTable((1, 3, 6, 1, 3, 99999, 1, 8, 1), )
if mibBuilder.loadTexts: ipsAuthCredSrpAttributesTable.setStatus('current')
if mibBuilder.loadTexts: ipsAuthCredSrpAttributesTable.setDescription('A list of SRP-specific attributes for credentials that\n     have their ipsAuthCredAuthMethod == ipsAuthMethodSrp.')
ipsAuthCredSrpAttributesEntry = MibTableRow((1, 3, 6, 1, 3, 99999, 1, 8, 1, 1), ).setIndexNames((0, "IPS-AUTH-MIB", "ipsAuthInstIndex"), (0, "IPS-AUTH-MIB", "ipsAuthIdentIndex"), (0, "IPS-AUTH-MIB", "ipsAuthCredIndex"))
if mibBuilder.loadTexts: ipsAuthCredSrpAttributesEntry.setStatus('current')
if mibBuilder.loadTexts: ipsAuthCredSrpAttributesEntry.setDescription('An entry (row) containing management information\n        applicable to a credential which has the ipsAuthCredAuthMethod\n     set to the OID of ipsAuthMethodSrp.')
ipsAuthCredSrpUserName = MibTableColumn((1, 3, 6, 1, 3, 99999, 1, 8, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsAuthCredSrpUserName.setStatus('current')
if mibBuilder.loadTexts: ipsAuthCredSrpUserName.setDescription('An octet string containing the CHAP user name for this\n     credential.')
ipsAuthCredSrpPassword = MibTableColumn((1, 3, 6, 1, 3, 99999, 1, 8, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsAuthCredSrpPassword.setStatus('current')
if mibBuilder.loadTexts: ipsAuthCredSrpPassword.setDescription('An octet string containing the password for this\n     credential.  If written, it changes the password for\n     the credential.  If read, it returns a zero-length\n     string.')
ipsAuthCredSrpRowStatus = MibTableColumn((1, 3, 6, 1, 3, 99999, 1, 8, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsAuthCredSrpRowStatus.setStatus('current')
if mibBuilder.loadTexts: ipsAuthCredSrpRowStatus.setDescription('This field allows entries to be dynamically added and\n     removed from this table via SNMP.')
ipsAuthGroups = MibIdentifier((1, 3, 6, 1, 3, 99999, 3, 1))
ipsAuthInstanceAttributesGroup = ObjectGroup((1, 3, 6, 1, 3, 99999, 3, 1, 1)).setObjects(("IPS-AUTH-MIB", "ipsAuthInstDescr"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ipsAuthInstanceAttributesGroup = ipsAuthInstanceAttributesGroup.setStatus('current')
if mibBuilder.loadTexts: ipsAuthInstanceAttributesGroup.setDescription('A collection of objects providing information about\n     authentication instances.')
ipsAuthIdentAttributesGroup = ObjectGroup((1, 3, 6, 1, 3, 99999, 3, 1, 2)).setObjects(("IPS-AUTH-MIB", "ipsAuthIdentDescription"), ("IPS-AUTH-MIB", "ipsAuthIdentRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ipsAuthIdentAttributesGroup = ipsAuthIdentAttributesGroup.setStatus('current')
if mibBuilder.loadTexts: ipsAuthIdentAttributesGroup.setDescription('A collection of objects providing information about\n\n\n\n     user identities within an authentication instance.')
ipsAuthIdentNameAttributesGroup = ObjectGroup((1, 3, 6, 1, 3, 99999, 3, 1, 3)).setObjects(("IPS-AUTH-MIB", "ipsAuthIdentName"), ("IPS-AUTH-MIB", "ipsAuthIdentNameRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ipsAuthIdentNameAttributesGroup = ipsAuthIdentNameAttributesGroup.setStatus('current')
if mibBuilder.loadTexts: ipsAuthIdentNameAttributesGroup.setDescription('A collection of objects providing information about\n     user names within user identities within an authentication\n     instance.')
ipsAuthIdentAddrAttributesGroup = ObjectGroup((1, 3, 6, 1, 3, 99999, 3, 1, 4)).setObjects(("IPS-AUTH-MIB", "ipsAuthIdentAddrType"), ("IPS-AUTH-MIB", "ipsAuthIdentAddrStart"), ("IPS-AUTH-MIB", "ipsAuthIdentAddrEnd"), ("IPS-AUTH-MIB", "ipsAuthIdentAddrRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ipsAuthIdentAddrAttributesGroup = ipsAuthIdentAddrAttributesGroup.setStatus('current')
if mibBuilder.loadTexts: ipsAuthIdentAddrAttributesGroup.setDescription('A collection of objects providing information about\n     address ranges within user identities within an authentication\n     instance.')
ipsAuthIdentCredAttributesGroup = ObjectGroup((1, 3, 6, 1, 3, 99999, 3, 1, 5)).setObjects(("IPS-AUTH-MIB", "ipsAuthCredAuthMethod"), ("IPS-AUTH-MIB", "ipsAuthCredRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ipsAuthIdentCredAttributesGroup = ipsAuthIdentCredAttributesGroup.setStatus('current')
if mibBuilder.loadTexts: ipsAuthIdentCredAttributesGroup.setDescription('A collection of objects providing information about\n     credentials within user identities within an authentication\n     instance.')
ipsAuthIdentChapAttrGroup = ObjectGroup((1, 3, 6, 1, 3, 99999, 3, 1, 6)).setObjects(("IPS-AUTH-MIB", "ipsAuthCredChapUserName"), ("IPS-AUTH-MIB", "ipsAuthCredChapPassword"), ("IPS-AUTH-MIB", "ipsAuthCredChapRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ipsAuthIdentChapAttrGroup = ipsAuthIdentChapAttrGroup.setStatus('current')
if mibBuilder.loadTexts: ipsAuthIdentChapAttrGroup.setDescription('A collection of objects providing information about CHAP\n     credentials within user identities within an authentication\n     instance.')
ipsAuthIdentSrpAttrGroup = ObjectGroup((1, 3, 6, 1, 3, 99999, 3, 1, 7)).setObjects(("IPS-AUTH-MIB", "ipsAuthCredSrpUserName"), ("IPS-AUTH-MIB", "ipsAuthCredSrpPassword"), ("IPS-AUTH-MIB", "ipsAuthCredSrpRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ipsAuthIdentSrpAttrGroup = ipsAuthIdentSrpAttrGroup.setStatus('current')
if mibBuilder.loadTexts: ipsAuthIdentSrpAttrGroup.setDescription('A collection of objects providing information about SRP\n     credentials within user identities within an authentication\n     instance.')
ipsAuthCompliances = MibIdentifier((1, 3, 6, 1, 3, 99999, 3, 2))
ipsAuthComplianceV1 = ModuleCompliance((1, 3, 6, 1, 3, 99999, 3, 2, 1)).setObjects(("IPS-AUTH-MIB", "ipsAuthInstanceAttributesGroup"), ("IPS-AUTH-MIB", "ipsAuthIdentAttributesGroup"), ("IPS-AUTH-MIB", "ipsAuthIdentNameAttributesGroup"), ("IPS-AUTH-MIB", "ipsAuthIdentAddrAttributesGroup"), ("IPS-AUTH-MIB", "ipsAuthIdentCredAttributesGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ipsAuthComplianceV1 = ipsAuthComplianceV1.setStatus('current')
if mibBuilder.loadTexts: ipsAuthComplianceV1.setDescription('Initial version of compliance statement based on\n        initial version of MIB.\n\n     The Instance and Identity groups are mandatory;\n     at least one of the other groups (Name, Address,\n     Credential, Certificate) is also mandatory for\n     any given implementation.')
mibBuilder.exportSymbols("IPS-AUTH-MIB", ipsAuthCredChapAttributesEntry=ipsAuthCredChapAttributesEntry, ipsAuthIdentAddrType=ipsAuthIdentAddrType, IpsAuthAddress=IpsAuthAddress, ipsAuthMethodChap=ipsAuthMethodChap, ipsAuthIdentNameAttributesEntry=ipsAuthIdentNameAttributesEntry, ipsAuthIdentNameIndex=ipsAuthIdentNameIndex, ipsAuthCredChap=ipsAuthCredChap, ipsAuthIdentAddrAttributesEntry=ipsAuthIdentAddrAttributesEntry, ipsAuthCredChapPassword=ipsAuthCredChapPassword, ipsAuthModule=ipsAuthModule, ipsAuthIdentName=ipsAuthIdentName, ipsAuthCredChapRowStatus=ipsAuthCredChapRowStatus, ipsAuthMethodTypes=ipsAuthMethodTypes, ipsAuthNotifications=ipsAuthNotifications, ipsAuthIdentAddrIndex=ipsAuthIdentAddrIndex, ipsAuthCredSrpAttributesTable=ipsAuthCredSrpAttributesTable, ipsAuthCompliances=ipsAuthCompliances, ipsAuthCredentialAttributesTable=ipsAuthCredentialAttributesTable, ipsAuthComplianceV1=ipsAuthComplianceV1, ipsAuthCredSrpUserName=ipsAuthCredSrpUserName, ipsAuthObjects=ipsAuthObjects, ipsAuthInstanceAttributesEntry=ipsAuthInstanceAttributesEntry, ipsAuthIdentityAddress=ipsAuthIdentityAddress, ipsAuthIdentSrpAttrGroup=ipsAuthIdentSrpAttrGroup, ipsAuthCredential=ipsAuthCredential, ipsAuthInstanceAttributesTable=ipsAuthInstanceAttributesTable, ipsAuthCredSrpRowStatus=ipsAuthCredSrpRowStatus, ipsAuthIdentAttributesGroup=ipsAuthIdentAttributesGroup, ipsAuthInstDescr=ipsAuthInstDescr, ipsAuthCredRowStatus=ipsAuthCredRowStatus, ipsAuthIdentAddrAttributesGroup=ipsAuthIdentAddrAttributesGroup, ipsAuthIdentityName=ipsAuthIdentityName, ipsAuthInstanceAttributesGroup=ipsAuthInstanceAttributesGroup, ipsAuthCredChapUserName=ipsAuthCredChapUserName, ipsAuthCredIndex=ipsAuthCredIndex, ipsAuthIdentChapAttrGroup=ipsAuthIdentChapAttrGroup, ipsAuthCredentialAttributesEntry=ipsAuthCredentialAttributesEntry, ipsAuthIdentCredAttributesGroup=ipsAuthIdentCredAttributesGroup, ipsAuthIdentity=ipsAuthIdentity, ipsAuthIdentAttributesTable=ipsAuthIdentAttributesTable, ipsAuthCredSrpAttributesEntry=ipsAuthCredSrpAttributesEntry, ipsAuthIdentIndex=ipsAuthIdentIndex, ipsAuthCredChapAttributesTable=ipsAuthCredChapAttributesTable, PYSNMP_MODULE_ID=ipsAuthModule, ipsAuthIdentAddrAttributesTable=ipsAuthIdentAddrAttributesTable, ipsAuthIdentAddrRowStatus=ipsAuthIdentAddrRowStatus, ipsAuthDescriptors=ipsAuthDescriptors, ipsAuthIdentAttributesEntry=ipsAuthIdentAttributesEntry, ipsAuthInstIndex=ipsAuthInstIndex, ipsAuthCredAuthMethod=ipsAuthCredAuthMethod, ipsAuthGroups=ipsAuthGroups, ipsAuthCredSrpPassword=ipsAuthCredSrpPassword, ipsAuthConformance=ipsAuthConformance, ipsAuthIdentNameRowStatus=ipsAuthIdentNameRowStatus, ipsAuthIdentRowStatus=ipsAuthIdentRowStatus, ipsAuthIdentAddrStart=ipsAuthIdentAddrStart, ipsAuthIdentNameAttributesGroup=ipsAuthIdentNameAttributesGroup, ipsAuthIdentAddrEnd=ipsAuthIdentAddrEnd, ipsAuthMethodSrp=ipsAuthMethodSrp, ipsAuthIdentDescription=ipsAuthIdentDescription, ipsAuthMethodNone=ipsAuthMethodNone, ipsAuthCredSrp=ipsAuthCredSrp, ipsAuthIdentNameAttributesTable=ipsAuthIdentNameAttributesTable, ipsAuthInstance=ipsAuthInstance)
