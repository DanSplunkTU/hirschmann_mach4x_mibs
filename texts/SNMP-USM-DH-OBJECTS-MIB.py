#
# PySNMP MIB module SNMP-USM-DH-OBJECTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/SNMP-USM-DH-OBJECTS-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 17:49:47 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
usmUserEntry, = mibBuilder.importSymbols("SNMP-USER-BASED-SM-MIB", "usmUserEntry")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ObjectIdentity, Integer32, experimental, Gauge32, IpAddress, Bits, NotificationType, Counter32, Unsigned32, MibIdentifier, ModuleIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ObjectIdentity", "Integer32", "experimental", "Gauge32", "IpAddress", "Bits", "NotificationType", "Counter32", "Unsigned32", "MibIdentifier", "ModuleIdentity", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
snmpUsmDHObjectsMIB = ModuleIdentity((1, 3, 6, 1, 3, 101))
snmpUsmDHObjectsMIB.setRevisions(('2000-03-06 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: snmpUsmDHObjectsMIB.setRevisionsDescriptions(('Initial version published as RFC 2786.',))
if mibBuilder.loadTexts: snmpUsmDHObjectsMIB.setLastUpdated('200003060000Z')
if mibBuilder.loadTexts: snmpUsmDHObjectsMIB.setOrganization('Excite@Home')
if mibBuilder.loadTexts: snmpUsmDHObjectsMIB.setContactInfo('Author: Mike StJohns\n                  Postal: Excite@Home\n                          450 Broadway\n                          Redwood City, CA 94063\n                  Email:  stjohns@corp.home.net\n                  Phone:  +1-650-556-5368')
if mibBuilder.loadTexts: snmpUsmDHObjectsMIB.setDescription("The management information definitions for providing forward\n    secrecy for key changes for the usmUserTable, and for providing a\n    method for 'kickstarting' access to the agent via a Diffie-Helman\n    key agreement.")
usmDHKeyObjects = MibIdentifier((1, 3, 6, 1, 3, 101, 1))
usmDHKeyConformance = MibIdentifier((1, 3, 6, 1, 3, 101, 2))
class DHKeyChange(TextualConvention, OctetString):
    reference = '-- Diffie-Hellman Key-Agreement Standard, PKCS #3;\n            RSA Laboratories, November 1993'
    description = "Upon initialization, or upon creation of a row containing an\n    object of this type, and after any successful SET of this value, a\n    GET of this value returns 'y' where y = g^xa MOD p, and where g is\n    the base from usmDHParameters, p is the prime from\n    usmDHParameters, and xa is a new random integer selected by the\n    agent in the interval 2^(l-1) <= xa < 2^l < p-1.  'l' is the\n    optional privateValueLength from usmDHParameters in bits.  If 'l'\n    is omitted, then xa (and xr below) is selected in the interval 0\n    <= xa < p-1.  y is expressed as an OCTET STRING 'PV' of length 'k'\n    which satisfies\n\n              k\n        y =  SUM   2^(8(k-i)) PV'i\n             i=1\n\n        where PV1,...,PVk are the octets of PV from first to last, and\n        where PV1 <> 0.\n\n    A successful SET consists of the value 'y' expressed as an OCTET\n    STRING as above concatenated with the value 'z'(expressed as an\n    OCTET STRING in the same manner as y) where z = g^xr MOD p, where\n    g, p and l are as above, and where xr is a new random integer\n    selected by the manager in the interval 2^(l-1) <= xr < 2^l <\n    p-1. A SET to an object of this type will fail with the error\n    wrongValue if the current 'y' does not match the 'y' portion of\n    the value of the varbind for the object. (E.g. GET yout, SET\n    concat(yin, z), yout <> yin).\n\n    Note that the private values xa and xr are never transmitted from\n    manager to device or vice versa, only the values y and z.\n    Obviously, these values must be retained until a successful SET on\n    the associated object.\n\n    The shared secret 'sk' is calculated at the agent as sk = z^xa MOD\n    p, and at the manager as sk = y^xr MOD p.\n\n    Each object definition of this type MUST describe how to map from\n    the shared secret 'sk' to the operational key value used by the\n    protocols and operations related to the object.  In general, if n\n    bits of key are required, the author suggests using the n\n    right-most bits of the shared secret as the operational key value."
    status = 'current'

usmDHPublicObjects = MibIdentifier((1, 3, 6, 1, 3, 101, 1, 1))
usmDHParameters = MibScalar((1, 3, 6, 1, 3, 101, 1, 1, 1), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: usmDHParameters.setReference('-- Diffie-Hellman Key-Agreement Standard, PKCS #3,\n            RSA Laboratories, November 1993\n         -- The Internet Key Exchange, RFC 2409, November 1998,\n            Sec 6.1, 6.2')
if mibBuilder.loadTexts: usmDHParameters.setStatus('current')
if mibBuilder.loadTexts: usmDHParameters.setDescription('The public Diffie-Hellman parameters for doing a Diffie-Hellman\n    key agreement for this device.  This is encoded as an ASN.1\n    DHParameter per PKCS #3, section 9.  E.g.\n\n        DHParameter ::= SEQUENCE {\n           prime   INTEGER,   -- p\n           base    INTEGER,   -- g\n           privateValueLength  INTEGER OPTIONAL }\n\n    Implementors are encouraged to use either the values from\n    Oakley Group 1  or the values of from Oakley Group 2 as specified\n    in RFC-2409, The Internet Key Exchange, Section 6.1, 6.2 as the\n    default for this object.  Other values may be used, but the\n    security properties of those values MUST be well understood and\n    MUST meet the requirements of PKCS #3 for the selection of\n    Diffie-Hellman primes.\n\n        In addition, any time usmDHParameters changes, all values of\n    type DHKeyChange will change and new random numbers MUST be\n    generated by the agent for each DHKeyChange object.')
usmDHUserKeyTable = MibTable((1, 3, 6, 1, 3, 101, 1, 1, 2), )
if mibBuilder.loadTexts: usmDHUserKeyTable.setStatus('current')
if mibBuilder.loadTexts: usmDHUserKeyTable.setDescription("This table augments and extends the usmUserTable and provides\n    4 objects which exactly mirror the objects in that table with the\n    textual convention of 'KeyChange'.  This extension allows key\n    changes to be done in a manner where the knowledge of the current\n    secret plus knowledge of the key change data exchanges (e.g. via\n    wiretapping)  will not reveal the new key.")
usmDHUserKeyEntry = MibTableRow((1, 3, 6, 1, 3, 101, 1, 1, 2, 1), )
usmUserEntry.registerAugmentions(("SNMP-USM-DH-OBJECTS-MIB", "usmDHUserKeyEntry"))
usmDHUserKeyEntry.setIndexNames(*usmUserEntry.getIndexNames())
if mibBuilder.loadTexts: usmDHUserKeyEntry.setStatus('current')
if mibBuilder.loadTexts: usmDHUserKeyEntry.setDescription('A row of DHKeyChange objects which augment or replace the\n    functionality of the KeyChange objects in the base table row.')
usmDHUserAuthKeyChange = MibTableColumn((1, 3, 6, 1, 3, 101, 1, 1, 2, 1, 1), DHKeyChange()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usmDHUserAuthKeyChange.setStatus('current')
if mibBuilder.loadTexts: usmDHUserAuthKeyChange.setDescription("The object used to change any given user's Authentication Key\n    using a Diffie-Hellman key exchange.\n\n    The right-most n bits of the shared secret 'sk', where 'n' is the\n    number of bits required for the protocol defined by\n    usmUserAuthProtocol, are installed as the operational\n    authentication key for this row after a successful SET.")
usmDHUserOwnAuthKeyChange = MibTableColumn((1, 3, 6, 1, 3, 101, 1, 1, 2, 1, 2), DHKeyChange()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usmDHUserOwnAuthKeyChange.setStatus('current')
if mibBuilder.loadTexts: usmDHUserOwnAuthKeyChange.setDescription("The object used to change the agents own Authentication Key\n    using a Diffie-Hellman key exchange.\n\n    The right-most n bits of the shared secret 'sk', where 'n' is the\n    number of bits required for the protocol defined by\n    usmUserAuthProtocol, are installed as the operational\n    authentication key for this row after a successful SET.")
usmDHUserPrivKeyChange = MibTableColumn((1, 3, 6, 1, 3, 101, 1, 1, 2, 1, 3), DHKeyChange()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usmDHUserPrivKeyChange.setStatus('current')
if mibBuilder.loadTexts: usmDHUserPrivKeyChange.setDescription("The object used to change any given user's Privacy Key using\n    a Diffie-Hellman key exchange.\n\n    The right-most n bits of the shared secret 'sk', where 'n' is the\n    number of bits required for the protocol defined by\n    usmUserPrivProtocol, are installed as the operational privacy key\n    for this row after a successful SET.")
usmDHUserOwnPrivKeyChange = MibTableColumn((1, 3, 6, 1, 3, 101, 1, 1, 2, 1, 4), DHKeyChange()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usmDHUserOwnPrivKeyChange.setStatus('current')
if mibBuilder.loadTexts: usmDHUserOwnPrivKeyChange.setDescription("The object used to change the agent's own Privacy Key using a\n    Diffie-Hellman key exchange.\n\n    The right-most n bits of the shared secret 'sk', where 'n' is the\n    number of bits required for the protocol defined by\n    usmUserPrivProtocol, are installed as the operational privacy key\n    for this row after a successful SET.")
usmDHKickstartGroup = MibIdentifier((1, 3, 6, 1, 3, 101, 1, 2))
usmDHKickstartTable = MibTable((1, 3, 6, 1, 3, 101, 1, 2, 1), )
if mibBuilder.loadTexts: usmDHKickstartTable.setStatus('current')
if mibBuilder.loadTexts: usmDHKickstartTable.setDescription("A table of mappings between zero or more Diffie-Helman key\n    agreement values and entries in the usmUserTable.  Entries in this\n    table are created by providing the associated device with a\n    Diffie-Helman public value and a usmUserName/usmUserSecurityName\n    pair during initialization. How these values are provided is\n    outside the scope of this MIB, but could be provided manually, or\n    through a configuration file.  Valid public value/name pairs\n    result in the creation of a row in this table as well as the\n    creation of an associated row (with keys derived as indicated) in\n    the usmUserTable.  The actual access the related usmSecurityName\n    has is dependent on the entries in the VACM tables.  In general,\n    an implementor will specify one or more standard security names\n    and will provide entries in the VACM tables granting various\n    levels of access to those names.  The actual content of the VACM\n\n    table is beyond the scope of this MIB.\n\n    Note: This table is expected to be readable without authentication\n    using the usmUserSecurityName 'dhKickstart'.  See the conformance\n    statements for details.")
usmDHKickstartEntry = MibTableRow((1, 3, 6, 1, 3, 101, 1, 2, 1, 1), ).setIndexNames((0, "SNMP-USM-DH-OBJECTS-MIB", "usmDHKickstartIndex"))
if mibBuilder.loadTexts: usmDHKickstartEntry.setStatus('current')
if mibBuilder.loadTexts: usmDHKickstartEntry.setDescription("An entry in the usmDHKickstartTable.  The agent SHOULD either\n    delete this entry or mark it as inactive upon a successful SET of\n    any of the KeyChange-typed objects in the usmUserEntry or upon a\n    successful SET of any of the DHKeyChange-typed objects in the\n    usmDhKeyChangeEntry where the related usmSecurityName (e.g. row of\n    usmUserTable or row of ushDhKeyChangeTable) equals this entry's\n    usmDhKickstartSecurityName.  In otherwords, once you've changed\n    one or more of the keys for a row in usmUserTable with a\n    particular security name, the row in this table with that same\n    security name is no longer useful or meaningful.")
usmDHKickstartIndex = MibTableColumn((1, 3, 6, 1, 3, 101, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: usmDHKickstartIndex.setStatus('current')
if mibBuilder.loadTexts: usmDHKickstartIndex.setDescription('Index value for this row.')
usmDHKickstartMyPublic = MibTableColumn((1, 3, 6, 1, 3, 101, 1, 2, 1, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usmDHKickstartMyPublic.setReference('-- Diffie-Hellman Key-Agreement Standard, PKCS#3v1.4;\n            RSA Laboratories, November 1993\n         -- The Internet Key Exchange, RFC2409;\n            Harkins, D., Carrel, D.; November 1998')
if mibBuilder.loadTexts: usmDHKickstartMyPublic.setStatus('current')
if mibBuilder.loadTexts: usmDHKickstartMyPublic.setDescription("The agent's Diffie-Hellman public value for this row.  At\n\n    initialization, the agent generates a random number and derives\n    its public value from that number.  This public value is published\n    here.  This public value 'y' equals g^r MOD p where g is the from\n    the set of Diffie-Hellman parameters, p is the prime from those\n    parameters, and r is a random integer selected by the agent in the\n    interval 2^(l-1) <= r < p-1 < 2^l.  If l is unspecified, then r is\n    a random integer selected in the interval 0 <= r < p-1\n\n    The public value is expressed as an OCTET STRING 'PV' of length\n    'k' which satisfies\n\n              k\n        y =  SUM   2^(8(k-i)) PV'i\n             i = 1\n\n        where PV1,...,PVk are the octets of PV from first to last, and\n        where PV1 != 0.\n\n    The following DH parameters (Oakley group #2, RFC 2409, sec 6.1,\n    6.2) are used for this object:\n\n    g = 2\n    p = FFFFFFFF FFFFFFFF C90FDAA2 2168C234 C4C6628B 80DC1CD1\n        29024E08 8A67CC74 020BBEA6 3B139B22 514A0879 8E3404DD\n        EF9519B3 CD3A431B 302B0A6D F25F1437 4FE1356D 6D51C245\n        E485B576 625E7EC6 F44C42E9 A637ED6B 0BFF5CB6 F406B7ED\n        EE386BFB 5A899FA5 AE9F2411 7C4B1FE6 49286651 ECE65381\n        FFFFFFFF FFFFFFFF\n    l=1024\n    ")
usmDHKickstartMgrPublic = MibTableColumn((1, 3, 6, 1, 3, 101, 1, 2, 1, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usmDHKickstartMgrPublic.setReference('-- Password-Based Cryptography Standard, PKCS#5v2.0;\n            RSA Laboratories, March 1999\n         -- Applied Cryptography, 2nd Ed.; B. Schneier,\n            Counterpane Systems; John Wiley & Sons, 1996')
if mibBuilder.loadTexts: usmDHKickstartMgrPublic.setStatus('current')
if mibBuilder.loadTexts: usmDHKickstartMgrPublic.setDescription("The manager's Diffie-Hellman public value for this row.  Note\n    that this value is not set via the SNMP agent, but may be set via\n    some out of band method, such as the device's configuration file.\n\n    The manager calculates this value in the same manner and using the\n    same parameter set as the agent does.  E.g. it selects a random\n    number 'r', calculates y = g^r mod p and provides 'y' as the\n    public number expressed as an OCTET STRING.  See\n    usmDHKickstartMyPublic for details.\n\n    When this object is set with a valid value during initialization,\n    a row is created in the usmUserTable with the following values:\n\n    usmUserEngineID             localEngineID\n    usmUserName                 [value of usmDHKickstartSecurityName]\n    usmUserSecurityName         [value of usmDHKickstartSecurityName]\n    usmUserCloneFrom            ZeroDotZero\n    usmUserAuthProtocol         usmHMACMD5AuthProtocol\n    usmUserAuthKeyChange        -- derived from set value\n    usmUserOwnAuthKeyChange     -- derived from set value\n    usmUserPrivProtocol         usmDESPrivProtocol\n    usmUserPrivKeyChange        -- derived from set value\n    usmUserOwnPrivKeyChange     -- derived from set value\n    usmUserPublic               ''\n    usmUserStorageType          permanent\n    usmUserStatus               active\n\n    A shared secret 'sk' is calculated at the agent as sk =\n    mgrPublic^r mod p where r is the agents random number and p is the\n    DH prime from the common parameters.  The underlying privacy key\n    for this row is derived from sk by applying the key derivation\n    function PBKDF2 defined in PKCS#5v2.0 with a salt of 0xd1310ba6,\n    and iterationCount of 500, a keyLength of 16 (for\n    usmDESPrivProtocol), and a prf (pseudo random function) of\n    'id-hmacWithSHA1'.  The underlying authentication key for this row\n    is derived from sk by applying the key derivation function PBKDF2\n    with a salt of 0x98dfb5ac , an interation count of 500, a\n    keyLength of 16 (for usmHMAC5AuthProtocol), and a prf of\n    'id-hmacWithSHA1'.  Note: The salts are the first two words in the\n    ks0 [key schedule 0] of the BLOWFISH cipher from 'Applied\n    Cryptography' by Bruce Schnier - they could be any relatively\n    random string of bits.\n\n    The manager can use its knowledge of its own random number and the\n    agent's public value to kickstart its access to the agent in a\n    secure manner.  Note that the security of this approach is\n    directly related to the strength of the authorization security of\n    the out of band provisioning of the managers public value\n    (e.g. the configuration file), but is not dependent at all on the\n    strength of the confidentiality of the out of band provisioning\n    data.")
usmDHKickstartSecurityName = MibTableColumn((1, 3, 6, 1, 3, 101, 1, 2, 1, 1, 4), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usmDHKickstartSecurityName.setStatus('current')
if mibBuilder.loadTexts: usmDHKickstartSecurityName.setDescription("The usmUserName and usmUserSecurityName in the usmUserTable\n    associated with this row.  This is provided in the same manner and\n    at the same time as the usmDHKickstartMgrPublic value -\n    e.g. possibly manually, or via the device's configuration file.")
usmDHKeyMIBCompliances = MibIdentifier((1, 3, 6, 1, 3, 101, 2, 1))
usmDHKeyMIBGroups = MibIdentifier((1, 3, 6, 1, 3, 101, 2, 2))
usmDHKeyMIBCompliance = ModuleCompliance((1, 3, 6, 1, 3, 101, 2, 1, 1)).setObjects(("SNMP-USM-DH-OBJECTS-MIB", "usmDHKeyMIBBasicGroup"), ("SNMP-USM-DH-OBJECTS-MIB", "usmDHKeyParamGroup"), ("SNMP-USM-DH-OBJECTS-MIB", "usmDHKeyKickstartGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usmDHKeyMIBCompliance = usmDHKeyMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: usmDHKeyMIBCompliance.setDescription('The compliance statement for this module.')
usmDHKeyMIBBasicGroup = ObjectGroup((1, 3, 6, 1, 3, 101, 2, 2, 1)).setObjects(("SNMP-USM-DH-OBJECTS-MIB", "usmDHUserAuthKeyChange"), ("SNMP-USM-DH-OBJECTS-MIB", "usmDHUserOwnAuthKeyChange"), ("SNMP-USM-DH-OBJECTS-MIB", "usmDHUserPrivKeyChange"), ("SNMP-USM-DH-OBJECTS-MIB", "usmDHUserOwnPrivKeyChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usmDHKeyMIBBasicGroup = usmDHKeyMIBBasicGroup.setStatus('current')
if mibBuilder.loadTexts: usmDHKeyMIBBasicGroup.setDescription('')
usmDHKeyParamGroup = ObjectGroup((1, 3, 6, 1, 3, 101, 2, 2, 2)).setObjects(("SNMP-USM-DH-OBJECTS-MIB", "usmDHParameters"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usmDHKeyParamGroup = usmDHKeyParamGroup.setStatus('current')
if mibBuilder.loadTexts: usmDHKeyParamGroup.setDescription('The mandatory object for all MIBs which use the DHKeyChange\n    textual convention.')
usmDHKeyKickstartGroup = ObjectGroup((1, 3, 6, 1, 3, 101, 2, 2, 3)).setObjects(("SNMP-USM-DH-OBJECTS-MIB", "usmDHKickstartMyPublic"), ("SNMP-USM-DH-OBJECTS-MIB", "usmDHKickstartMgrPublic"), ("SNMP-USM-DH-OBJECTS-MIB", "usmDHKickstartSecurityName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usmDHKeyKickstartGroup = usmDHKeyKickstartGroup.setStatus('current')
if mibBuilder.loadTexts: usmDHKeyKickstartGroup.setDescription('The objects used for kickstarting one or more SNMPv3 USM\n    associations via a configuration file or other out of band,\n    non-confidential access.')
mibBuilder.exportSymbols("SNMP-USM-DH-OBJECTS-MIB", usmDHUserPrivKeyChange=usmDHUserPrivKeyChange, usmDHKeyParamGroup=usmDHKeyParamGroup, usmDHKickstartGroup=usmDHKickstartGroup, PYSNMP_MODULE_ID=snmpUsmDHObjectsMIB, usmDHKickstartSecurityName=usmDHKickstartSecurityName, usmDHUserAuthKeyChange=usmDHUserAuthKeyChange, usmDHKickstartEntry=usmDHKickstartEntry, usmDHKeyMIBCompliances=usmDHKeyMIBCompliances, usmDHUserKeyEntry=usmDHUserKeyEntry, usmDHKeyObjects=usmDHKeyObjects, snmpUsmDHObjectsMIB=snmpUsmDHObjectsMIB, usmDHKeyMIBBasicGroup=usmDHKeyMIBBasicGroup, usmDHKeyKickstartGroup=usmDHKeyKickstartGroup, usmDHKeyMIBCompliance=usmDHKeyMIBCompliance, usmDHParameters=usmDHParameters, DHKeyChange=DHKeyChange, usmDHKeyConformance=usmDHKeyConformance, usmDHKickstartMgrPublic=usmDHKickstartMgrPublic, usmDHKickstartIndex=usmDHKickstartIndex, usmDHUserOwnAuthKeyChange=usmDHUserOwnAuthKeyChange, usmDHUserKeyTable=usmDHUserKeyTable, usmDHKickstartMyPublic=usmDHKickstartMyPublic, usmDHKeyMIBGroups=usmDHKeyMIBGroups, usmDHKickstartTable=usmDHKickstartTable, usmDHUserOwnPrivKeyChange=usmDHUserOwnPrivKeyChange, usmDHPublicObjects=usmDHPublicObjects)
