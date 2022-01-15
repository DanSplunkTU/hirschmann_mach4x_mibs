#
# PySNMP MIB module DOCS-MCAST-AUTH-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/DOCS-MCAST-AUTH-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 17:49:46 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
clabProjDocsis, = mibBuilder.importSymbols("CLAB-DEF-MIB", "clabProjDocsis")
docsIf3CmtsCmRegStatusId, = mibBuilder.importSymbols("DOCS-IF3-MIB", "docsIf3CmtsCmRegStatusId")
InetAddressType, InetAddress, InetAddressPrefixLength = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress", "InetAddressPrefixLength")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
SnmpTagList, = mibBuilder.importSymbols("SNMP-TARGET-MIB", "SnmpTagList")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ObjectIdentity, Integer32, IpAddress, Gauge32, Bits, Unsigned32, Counter32, NotificationType, MibIdentifier, ModuleIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ObjectIdentity", "Integer32", "IpAddress", "Gauge32", "Bits", "Unsigned32", "Counter32", "NotificationType", "MibIdentifier", "ModuleIdentity", "iso")
TextualConvention, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "RowStatus")
docsMcastAuthMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 4491, 2, 1, 19))
docsMcastAuthMib.setRevisions(('2007-12-06 00:00', '2006-12-07 17:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: docsMcastAuthMib.setRevisionsDescriptions(('Revised version includes ECN\n         OSSIv3.0-N-07.0551-4 and published as I05.', 'Initial version, published as part of the CableLabs\n        OSSIv3.0 specification CM-SP-OSSIv3.0-I01-061207.',))
if mibBuilder.loadTexts: docsMcastAuthMib.setLastUpdated('200712060000Z')
if mibBuilder.loadTexts: docsMcastAuthMib.setOrganization('Cable Television Laboratories, Inc.')
if mibBuilder.loadTexts: docsMcastAuthMib.setContactInfo('\n         Postal: Cable Television Laboratories, Inc.\n         858 Coal Creek Circle\n         Louisville, Colorado 80027-9750\n         U.S.A.\n         Phone: +1 303-661-9100\n         Fax:   +1 303-661-9199\n         E-mail: mibs@cablelabs.com')
if mibBuilder.loadTexts: docsMcastAuthMib.setDescription('This MIB module contains the management objects for the\n        management of the CMTS Multicast Authorization Module.\n        Copyright 1999-2007 Cable Television Laboratories, Inc.\n        All rights reserved.')
docsMcastAuthMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 1, 19, 1))
docsMcastAuthCtrl = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 1, 19, 1, 1))
docsMcastAuthCtrlEnable = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 1, 19, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: docsMcastAuthCtrlEnable.setReference('DOCSIS 3.0 MAC and Upper Layer Protocols Interface\n         Specification CM-SP-MULPIv3.0-I01-060804, IP Multicast\n         Join Authorization section.')
if mibBuilder.loadTexts: docsMcastAuthCtrlEnable.setStatus('current')
if mibBuilder.loadTexts: docsMcastAuthCtrlEnable.setDescription("This attribute enables the enforcement of Multicast\n        Autorization feature. When this attribute is set\n        to 'enable' Multicast Authorization is enforced;\n        otherwise clients are permitted to join any IP multicast\n        session. The factory default value of this attribute\n        is 'disable'.")
docsMcastAuthCtrlDefProfileNameList = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 1, 19, 1, 1, 2), SnmpTagList().clone(hexValue="")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: docsMcastAuthCtrlDefProfileNameList.setReference('DOCSIS 3.0 MAC and Upper Layer Protocols Interface\n         Specification CM-SP-MULPIv3.0-I01-060804, IP Multicast \n         Profile Name Subtype section.')
if mibBuilder.loadTexts: docsMcastAuthCtrlDefProfileNameList.setStatus('current')
if mibBuilder.loadTexts: docsMcastAuthCtrlDefProfileNameList.setDescription("When IP Multicast Authorization is enforced, this\n        attribute provides the default set of Multicast Authorization\n        Profiles the CMTS enforces for a CM in the\n        case that this CM didn't signal a set of profiles during\n        the registration process.  If the Default Multicast\n        Authorization Group Name is zero length string,\n        the DefAction attribute determines whether a join request\n        is authorized when a CM registers without a Multicast\n        Authorization Profile Set or a list of config\n        File Session Rules. If the CMTS supports more than 1\n        profile name as a default, the CMTS enforces each of the\n        profiles in order until the maximum number of profiles\n        is reached. This attribute indicates one or more\n        Multicast Authorization Profiles.")
docsMcastAuthCtrlDefAction = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 1, 19, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("permit", 1), ("deny", 2))).clone('deny')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: docsMcastAuthCtrlDefAction.setReference('DOCSIS 3.0 MAC and Upper Layer Protocols Interface\n         Specification CM-SP-MULPIv3.0-I01-060804, Session Rules\n         section.')
if mibBuilder.loadTexts: docsMcastAuthCtrlDefAction.setStatus('current')
if mibBuilder.loadTexts: docsMcastAuthCtrlDefAction.setDescription("This attribute defines the default authorization\n        action when no IP Multicast Session Rule is determined\n        to match a client's IP multicast join request.")
docsMcastAuthCtrlDefMaxNumSess = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 1, 19, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: docsMcastAuthCtrlDefMaxNumSess.setReference('DOCSIS 3.0 MAC and Upper Layer Protocols Interface\n         Specification CM-SP-MULPIv3.0-I01-060804, Maximum Multicast \n         Sessions section.')
if mibBuilder.loadTexts: docsMcastAuthCtrlDefMaxNumSess.setStatus('current')
if mibBuilder.loadTexts: docsMcastAuthCtrlDefMaxNumSess.setDescription('This attribute indicates the default maximum number\n        of multicast sessions that clients reached through\n        a CM are allowed to join. If set to zero, the maximum\n        number of sessions is not limited by the CMTS. A DefMaxNumSess\n        value of 0 indicates that no dynamic joins\n        are permitted.')
docsMcastAuthCmtsCmStatusTable = MibTable((1, 3, 6, 1, 4, 1, 4491, 2, 1, 19, 1, 2), )
if mibBuilder.loadTexts: docsMcastAuthCmtsCmStatusTable.setStatus('current')
if mibBuilder.loadTexts: docsMcastAuthCmtsCmStatusTable.setDescription("This object maintains per-CM status of Multicast\n        Authorization policies to be applied to this CM. The\n        CM acquires these policy parameters through the CM registration\n        process, or in the absence of some or all\n        of those parameters, from the Ctrl Object.\n        This object is meaningful when the Control Enable attribute\n        is set to 'enable'.\n        In the process of authorizing a CM client's session request\n        the CMTS must check rules defined in StaticSessRule\n        object and then rules defined in ProfileSessRule\n        object. In the case of multiple multicast session\n        matches, the rule priority attribute defines the\n        final selected session rule. The selection of a session\n        rules when multiple matches have the same priority\n        is vendor specific.\n        The CMTS MAY report in the CmtsCmStatus object CMs that\n        do not signal any IP Multicast Authorization Encodings\n        in the registration process. ")
docsMcastAuthCmtsCmStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4491, 2, 1, 19, 1, 2, 1), ).setIndexNames((0, "DOCS-IF3-MIB", "docsIf3CmtsCmRegStatusId"))
if mibBuilder.loadTexts: docsMcastAuthCmtsCmStatusEntry.setStatus('current')
if mibBuilder.loadTexts: docsMcastAuthCmtsCmStatusEntry.setDescription('The conceptual row of docsMcastAuthCmtsCmStatus.')
docsMcastAuthCmtsCmStatusCfgProfileNameList = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 19, 1, 2, 1, 1), SnmpTagList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: docsMcastAuthCmtsCmStatusCfgProfileNameList.setStatus('current')
if mibBuilder.loadTexts: docsMcastAuthCmtsCmStatusCfgProfileNameList.setDescription("This attribute indicates the set of Profile Names\n        associated with the CM.\n        This attribute indicates the CM signaled 'IP Multicast\n        Authorization Profile Name' encodings during the\n        CM registration process, or in the absence of instances\n        of that config file parameter, the DefProfileNameList\n        attribute from the Ctrl object.")
docsMcastAuthCmtsCmStatusCfgListId = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 19, 1, 2, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: docsMcastAuthCmtsCmStatusCfgListId.setReference('DOCSIS 3.0 MAC and Upper Layer Protocols Interface\n         Specification CM-SP-MULPIv3.0-I01-060804,IP Multicast Join \n         Authorization Static Session Rule Subtype section in the \n         Common Radio Frequency Interface Encodings Annex.')
if mibBuilder.loadTexts: docsMcastAuthCmtsCmStatusCfgListId.setStatus('current')
if mibBuilder.loadTexts: docsMcastAuthCmtsCmStatusCfgListId.setDescription("This attribute identifies the reference to a CMTS\n        created Session Rule List based on the CM signaled 'IP\n        Multicast Authorization Static Session Rule' encodings.\n        The CMTS may reuse this attribute value to reference\n        more than one CM that have signaled the same list\n        of Session Rules to the CMTS.\n        The value zero indicates that the CM did not signal Multicast\n        Session Rules to the CMTS or the CMTS does not\n        support the StaticSessRule, in which case, the CMTS\n        ignores any CM signalled Session Rule endocings during\n        registration.")
docsMcastAuthCmtsCmStatusMaxNumSess = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 19, 1, 2, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setUnits('sessions').setMaxAccess("readonly")
if mibBuilder.loadTexts: docsMcastAuthCmtsCmStatusMaxNumSess.setReference('DOCSIS 3.0 MAC and Upper Layer Protocols Interface\n         Specification CM-SP-MULPIv3.0-I01-060804, Maximum Multicast\n         Sessions Encoding section in the Common Radio Frequency\n         Interface Encodings Annex.')
if mibBuilder.loadTexts: docsMcastAuthCmtsCmStatusMaxNumSess.setStatus('current')
if mibBuilder.loadTexts: docsMcastAuthCmtsCmStatusMaxNumSess.setDescription('This attribute indicates the CM signaled value in\n        Maximum Multicast Sessions Encoding during the CM registration\n        process. If this value is missing the DefMaxNumSess\n        attribute of the Ctrl object is used to determine\n        the maximum number of multicast sessions this\n        client may forward. The value 0 indicates that no\n        dynamic joins are permitted. The value 65535 (the largest\n        valid value) indicates that the CMTS permits any\n        number of sessions to be joined by clients reached\n        through the CM.')
docsMcastAuthCmtsCmStatusCfgParamFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 19, 1, 2, 1, 4), Bits().clone(namedValues=NamedValues(("profile", 0), ("staticMulticast", 1), ("maxNumSessions", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: docsMcastAuthCmtsCmStatusCfgParamFlag.setReference('DOCSIS 3.0 MAC and Upper Layer Protocols Interface\n         Specification CM-SP-MULPIv3.0-I01-060804')
if mibBuilder.loadTexts: docsMcastAuthCmtsCmStatusCfgParamFlag.setStatus('current')
if mibBuilder.loadTexts: docsMcastAuthCmtsCmStatusCfgParamFlag.setDescription("This attribute represents the functions that are\n        activated through the registration process.\n        The bit 'profile' indicates whether the CM signaled\n        'IP Multicast Authorization Profile Name Subtype'\n        encodings.\n        The bit 'staticMulticast' indicates whether the CM\n        signaled 'IP Multicast Authorization Static Session\n        Rule Subtype' encodings.\n        The bit 'maxNumSess' indicates whether the CM signaled\n        the ' Maximum Multicast Sessions' encoding.")
docsMcastAuthProfileSessRuleTable = MibTable((1, 3, 6, 1, 4, 1, 4491, 2, 1, 19, 1, 3), )
if mibBuilder.loadTexts: docsMcastAuthProfileSessRuleTable.setStatus('current')
if mibBuilder.loadTexts: docsMcastAuthProfileSessRuleTable.setDescription('This object defines Operator configured profiles\n        to be matched during the authorization process.\n        This object supports the creation and deletion of multiple\n        instances.\n        Creation of a new instance of this object requires the\n        following attributes to be set:\n        PrefixAddrType\n        SrcPrefixAddr\n        SrcPrefixLen\n        GrpPrefixAddr\n        GrpPrefixLen.')
docsMcastAuthProfileSessRuleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4491, 2, 1, 19, 1, 3, 1), ).setIndexNames((0, "DOCS-MCAST-AUTH-MIB", "docsMcastAuthProfilesName"), (0, "DOCS-MCAST-AUTH-MIB", "docsMcastAuthProfileSessRuleId"))
if mibBuilder.loadTexts: docsMcastAuthProfileSessRuleEntry.setStatus('current')
if mibBuilder.loadTexts: docsMcastAuthProfileSessRuleEntry.setDescription('The conceptual row of docsMcastAuthProfileSessRule.\n         The CMTS persists all instances of the ProfileSessRule\n         object across reinitializations.')
docsMcastAuthProfileSessRuleId = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 19, 1, 3, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: docsMcastAuthProfileSessRuleId.setStatus('current')
if mibBuilder.loadTexts: docsMcastAuthProfileSessRuleId.setDescription('This attribute provides a unique identifier for each\n        CMTS configured Multicast Authorization Profile\n        Session rule within a Multicast Authorization Profile\n        Name.')
docsMcastAuthProfileSessRulePriority = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 19, 1, 3, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: docsMcastAuthProfileSessRulePriority.setReference('DOCSIS 3.0 MAC and Upper Layer Protocols Interface\n         Specification CM-SP-MULPIv3.0-I01-060804, Session Rules\n         section.')
if mibBuilder.loadTexts: docsMcastAuthProfileSessRulePriority.setStatus('current')
if mibBuilder.loadTexts: docsMcastAuthProfileSessRulePriority.setDescription('This attribute configures the rule priority for the\n        static session rule. Permitted values for this attribute\n        range from 0..255. Higher values indicate a\n        higher priority. If more than one session rule matches\n        a joined session, the session rule with the highest\n        rule priority determines the authorization action.')
docsMcastAuthProfileSessRulePrefixAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 19, 1, 3, 1, 3), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: docsMcastAuthProfileSessRulePrefixAddrType.setReference('DOCSIS 3.0 MAC and Upper Layer Protocols Interface\n         Specification CM-SP-MULPIv3.0-I01-060804, Session Rules\n         section.')
if mibBuilder.loadTexts: docsMcastAuthProfileSessRulePrefixAddrType.setStatus('current')
if mibBuilder.loadTexts: docsMcastAuthProfileSessRulePrefixAddrType.setDescription('This attribute identifies the address family for\n        the multicast session (S,G) which corresponds to the\n        SrcPrefixAddr and GrpPrefixAddr attributes respectively.')
docsMcastAuthProfileSessRuleSrcPrefixAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 19, 1, 3, 1, 4), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: docsMcastAuthProfileSessRuleSrcPrefixAddr.setReference('RFC 3569.\n         RFC 3306')
if mibBuilder.loadTexts: docsMcastAuthProfileSessRuleSrcPrefixAddr.setStatus('current')
if mibBuilder.loadTexts: docsMcastAuthProfileSessRuleSrcPrefixAddr.setDescription("This attribute identifies a specific Multicast Source\n        Address defined for  this rule.  A Source Address\n        that is all zeros is defined as 'all source addresses'\n         (*, G).   Source prefix addresses are unicast addresses.")
docsMcastAuthProfileSessRuleSrcPrefixLen = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 19, 1, 3, 1, 5), InetAddressPrefixLength()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: docsMcastAuthProfileSessRuleSrcPrefixLen.setReference('DOCSIS 3.0 MAC and Upper Layer Protocols Interface\n         Specification CM-SP-MULPIv3.0-I01-060804, Session Rules\n         section.')
if mibBuilder.loadTexts: docsMcastAuthProfileSessRuleSrcPrefixLen.setStatus('current')
if mibBuilder.loadTexts: docsMcastAuthProfileSessRuleSrcPrefixLen.setDescription('This attribute identifies the prefix of a range of\n        Source (S) IP multicast group addresses. For Group or\n        ASM based sessions this attribute is set to 0.')
docsMcastAuthProfileSessRuleGrpPrefixAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 19, 1, 3, 1, 6), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: docsMcastAuthProfileSessRuleGrpPrefixAddr.setStatus('current')
if mibBuilder.loadTexts: docsMcastAuthProfileSessRuleGrpPrefixAddr.setDescription('This attribute identifies the prefix of a range of\n        destination IP multicast group addresses.')
docsMcastAuthProfileSessRuleGrpPrefixLen = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 19, 1, 3, 1, 7), InetAddressPrefixLength()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: docsMcastAuthProfileSessRuleGrpPrefixLen.setStatus('current')
if mibBuilder.loadTexts: docsMcastAuthProfileSessRuleGrpPrefixLen.setDescription('This attribute identifies the prefix of a range of\n        IP multicast group addresses.')
docsMcastAuthProfileSessRuleAction = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 19, 1, 3, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("accept", 1), ("deny", 2))).clone('deny')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: docsMcastAuthProfileSessRuleAction.setReference('DOCSIS 3.0 MAC and Upper Layer Protocols Interface\n         Specification CM-SP-MULPIv3.0-I01-060804, Session Rules\n         section.')
if mibBuilder.loadTexts: docsMcastAuthProfileSessRuleAction.setStatus('current')
if mibBuilder.loadTexts: docsMcastAuthProfileSessRuleAction.setDescription("This attribute specifies the authorization action\n        for a session join attempt that matches the session\n        rule.\n        The value 'accept' indicates that the rule permits a\n        matching multicast join request is allowed .  The value\n        'deny' indicates that a matching multicast join request\n        is denied.")
docsMcastAuthProfileSessRuleRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 19, 1, 3, 1, 9), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: docsMcastAuthProfileSessRuleRowStatus.setStatus('current')
if mibBuilder.loadTexts: docsMcastAuthProfileSessRuleRowStatus.setDescription('The status of this instance.')
docsMcastAuthStaticSessRuleTable = MibTable((1, 3, 6, 1, 4, 1, 4491, 2, 1, 19, 1, 4), )
if mibBuilder.loadTexts: docsMcastAuthStaticSessRuleTable.setStatus('current')
if mibBuilder.loadTexts: docsMcastAuthStaticSessRuleTable.setDescription('This object defines the Session authorization Rules\n        based on the CM or group of CMs signaled in IP Multicast\n        Join Authorization Static Session Subtype encoding\n         This object reflects the Static Session rules\n        that were included in the CM registration request message.')
docsMcastAuthStaticSessRuleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4491, 2, 1, 19, 1, 4, 1), ).setIndexNames((0, "DOCS-MCAST-AUTH-MIB", "docsMcastAuthStaticSessRuleCfgListId"), (0, "DOCS-MCAST-AUTH-MIB", "docsMcastAuthStaticSessRuleId"))
if mibBuilder.loadTexts: docsMcastAuthStaticSessRuleEntry.setStatus('current')
if mibBuilder.loadTexts: docsMcastAuthStaticSessRuleEntry.setDescription('The conceptual row of docsMcastAuthStaticSessRule.\n         The CMTS may persist all instances of the StaticSessRule\n         object across reinitializations.')
docsMcastAuthStaticSessRuleCfgListId = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 19, 1, 4, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: docsMcastAuthStaticSessRuleCfgListId.setStatus('current')
if mibBuilder.loadTexts: docsMcastAuthStaticSessRuleCfgListId.setDescription('This attribute contains a CMTS-derived value for\n        a set of multicast static session rules associated to\n        one or more CMs.')
docsMcastAuthStaticSessRuleId = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 19, 1, 4, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: docsMcastAuthStaticSessRuleId.setStatus('current')
if mibBuilder.loadTexts: docsMcastAuthStaticSessRuleId.setDescription('This attribute provides an identifier for each Multicast\n        Authorization Static Session rule in the IP\n        Multicast Join Authorization Static Session SubType\n        communicated by a CM or group of CMs during registration.')
docsMcastAuthStaticSessRulePriority = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 19, 1, 4, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: docsMcastAuthStaticSessRulePriority.setReference('DOCSIS 3.0 MAC and Upper Layer Protocols Interface\n         Specification CM-SP-MULPIv3.0-I01-060804, RulePriority\n         section in the Common Radio Frequency Interface Encodings\n         Annex.')
if mibBuilder.loadTexts: docsMcastAuthStaticSessRulePriority.setStatus('current')
if mibBuilder.loadTexts: docsMcastAuthStaticSessRulePriority.setDescription('This attribute defines the rule priority for the static\n        session rule. Higher values indicate a higher\n        priority. If more than one session rule matches a joined\n        session, the session rule with the highest rule priority\n        determines the authorization action.')
docsMcastAuthStaticSessRulePrefixAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 19, 1, 4, 1, 4), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: docsMcastAuthStaticSessRulePrefixAddrType.setStatus('current')
if mibBuilder.loadTexts: docsMcastAuthStaticSessRulePrefixAddrType.setDescription('This attribute identifies the address family for\n        the multicast session (S,G) which corresponds to the\n        SrcPrefixAddr and GrpPrefixAddr attributes respectively.')
docsMcastAuthStaticSessRuleSrcPrefixAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 19, 1, 4, 1, 5), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: docsMcastAuthStaticSessRuleSrcPrefixAddr.setReference('RFC 3569.\n         RFC 3306.')
if mibBuilder.loadTexts: docsMcastAuthStaticSessRuleSrcPrefixAddr.setStatus('current')
if mibBuilder.loadTexts: docsMcastAuthStaticSessRuleSrcPrefixAddr.setDescription("This attribute identifies a specific Multicast Source\n        Address defined for  this rule.  A Source Address\n        that is all zeros is defined as 'all source addresses\n         (*, G)'. Source Prefix Addresses are unicast host addresses.")
docsMcastAuthStaticSessRuleSrcPrefixLen = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 19, 1, 4, 1, 6), InetAddressPrefixLength()).setMaxAccess("readonly")
if mibBuilder.loadTexts: docsMcastAuthStaticSessRuleSrcPrefixLen.setStatus('current')
if mibBuilder.loadTexts: docsMcastAuthStaticSessRuleSrcPrefixLen.setDescription('This attribute identifies the prefix of a range of\n        Source (S) IP multicast group addresses. For ASM-based\n        sessions, this attribute is set to 0.')
docsMcastAuthStaticSessRuleGrpPrefixAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 19, 1, 4, 1, 7), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: docsMcastAuthStaticSessRuleGrpPrefixAddr.setStatus('current')
if mibBuilder.loadTexts: docsMcastAuthStaticSessRuleGrpPrefixAddr.setDescription('This attribute identifies the prefix of a range of\n        destination IP multicast group addresses.')
docsMcastAuthStaticSessRuleGrpPrefixLen = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 19, 1, 4, 1, 8), InetAddressPrefixLength()).setMaxAccess("readonly")
if mibBuilder.loadTexts: docsMcastAuthStaticSessRuleGrpPrefixLen.setReference('DOCSIS 3.0 MAC and Upper Layer Protocols Interface\n         Specification CM-SP-MULPIv3.0-I01-060804,Group Prefix\n         Length Subtype section in the Common Radio Frequency\n         Interface Encodings Annex.')
if mibBuilder.loadTexts: docsMcastAuthStaticSessRuleGrpPrefixLen.setStatus('current')
if mibBuilder.loadTexts: docsMcastAuthStaticSessRuleGrpPrefixLen.setDescription('This attribute identifies the prefix of a range of\n        IP multicast group addresses.')
docsMcastAuthStaticSessRuleAction = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 19, 1, 4, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("permit", 1), ("deny", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: docsMcastAuthStaticSessRuleAction.setReference('DOCSIS 3.0 MAC and Upper Layer Protocols Interface\n         Specification CM-SP-MULPIv3.0-I01-060804, Authorization \n         Action section in the Common Radio Frequency Interface\n          Encodings Annex.')
if mibBuilder.loadTexts: docsMcastAuthStaticSessRuleAction.setStatus('current')
if mibBuilder.loadTexts: docsMcastAuthStaticSessRuleAction.setDescription("This attribute specifies the authorization action\n        for a session join attempt that matches the session\n        rule.\n        The value 'accept' indicates that the rule permits a\n        matching multicast join request is allowed.  The value\n        'deny' indicates that a matching multicast join request\n        is denied.")
docsMcastAuthProfilesTable = MibTable((1, 3, 6, 1, 4, 1, 4491, 2, 1, 19, 1, 5), )
if mibBuilder.loadTexts: docsMcastAuthProfilesTable.setStatus('current')
if mibBuilder.loadTexts: docsMcastAuthProfilesTable.setDescription('This object contains the description of the Multicast\n        Authorization profiles for administrative purposes.\n\n        This object supports the creation and deletion of multiple\n        instances.\n        Creation of a new instance of this object requires the\n        Description attribute to be set.')
docsMcastAuthProfilesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4491, 2, 1, 19, 1, 5, 1), ).setIndexNames((0, "DOCS-MCAST-AUTH-MIB", "docsMcastAuthProfilesName"))
if mibBuilder.loadTexts: docsMcastAuthProfilesEntry.setStatus('current')
if mibBuilder.loadTexts: docsMcastAuthProfilesEntry.setDescription('The conceptual row of docsMcastAuthProfiles.\n         The CMTS persists all instances of the Profiles\n         object across reinitializations')
docsMcastAuthProfilesName = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 19, 1, 5, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 15)))
if mibBuilder.loadTexts: docsMcastAuthProfilesName.setStatus('current')
if mibBuilder.loadTexts: docsMcastAuthProfilesName.setDescription('This attribute is a unique name or identifier for a\n        Multicast Authorization Profile.')
docsMcastAuthProfilesDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 19, 1, 5, 1, 2), SnmpAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: docsMcastAuthProfilesDescription.setReference('DOCSIS 3.0 MAC and Upper Layer Protocols Interface\n         Specification CM-SP-MULPIv3.0-I01-060804, IP Multicast \n         Profile Name Subtype section.')
if mibBuilder.loadTexts: docsMcastAuthProfilesDescription.setStatus('current')
if mibBuilder.loadTexts: docsMcastAuthProfilesDescription.setDescription('This attribute is a human readable description of\n        the Multicast Authorization Profile.')
docsMcastAuthProfilesRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 19, 1, 5, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: docsMcastAuthProfilesRowStatus.setStatus('current')
if mibBuilder.loadTexts: docsMcastAuthProfilesRowStatus.setDescription('The status of this instance.')
docsMcastAuthMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 1, 19, 2))
docsMcastAuthMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 1, 19, 2, 1))
docsMcastAuthMibGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 1, 19, 2, 2))
docsMcastAuthCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4491, 2, 1, 19, 2, 1, 1)).setObjects(("DOCS-MCAST-AUTH-MIB", "docsMcastAuthGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    docsMcastAuthCompliance = docsMcastAuthCompliance.setStatus('current')
if mibBuilder.loadTexts: docsMcastAuthCompliance.setDescription('The compliance statement for devices that implement the DOCSIS\n         Multicast Authorization MIB.')
docsMcastAuthGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4491, 2, 1, 19, 2, 2, 1)).setObjects(("DOCS-MCAST-AUTH-MIB", "docsMcastAuthCtrlEnable"), ("DOCS-MCAST-AUTH-MIB", "docsMcastAuthCtrlDefProfileNameList"), ("DOCS-MCAST-AUTH-MIB", "docsMcastAuthCtrlDefAction"), ("DOCS-MCAST-AUTH-MIB", "docsMcastAuthCtrlDefMaxNumSess"), ("DOCS-MCAST-AUTH-MIB", "docsMcastAuthCmtsCmStatusCfgProfileNameList"), ("DOCS-MCAST-AUTH-MIB", "docsMcastAuthCmtsCmStatusCfgListId"), ("DOCS-MCAST-AUTH-MIB", "docsMcastAuthCmtsCmStatusMaxNumSess"), ("DOCS-MCAST-AUTH-MIB", "docsMcastAuthCmtsCmStatusCfgParamFlag"), ("DOCS-MCAST-AUTH-MIB", "docsMcastAuthProfileSessRulePriority"), ("DOCS-MCAST-AUTH-MIB", "docsMcastAuthProfileSessRulePrefixAddrType"), ("DOCS-MCAST-AUTH-MIB", "docsMcastAuthProfileSessRuleSrcPrefixAddr"), ("DOCS-MCAST-AUTH-MIB", "docsMcastAuthProfileSessRuleSrcPrefixLen"), ("DOCS-MCAST-AUTH-MIB", "docsMcastAuthProfileSessRuleGrpPrefixAddr"), ("DOCS-MCAST-AUTH-MIB", "docsMcastAuthProfileSessRuleGrpPrefixLen"), ("DOCS-MCAST-AUTH-MIB", "docsMcastAuthProfileSessRuleAction"), ("DOCS-MCAST-AUTH-MIB", "docsMcastAuthProfileSessRuleRowStatus"), ("DOCS-MCAST-AUTH-MIB", "docsMcastAuthStaticSessRulePriority"), ("DOCS-MCAST-AUTH-MIB", "docsMcastAuthStaticSessRulePrefixAddrType"), ("DOCS-MCAST-AUTH-MIB", "docsMcastAuthStaticSessRuleSrcPrefixAddr"), ("DOCS-MCAST-AUTH-MIB", "docsMcastAuthStaticSessRuleSrcPrefixLen"), ("DOCS-MCAST-AUTH-MIB", "docsMcastAuthStaticSessRuleGrpPrefixAddr"), ("DOCS-MCAST-AUTH-MIB", "docsMcastAuthStaticSessRuleGrpPrefixLen"), ("DOCS-MCAST-AUTH-MIB", "docsMcastAuthStaticSessRuleAction"), ("DOCS-MCAST-AUTH-MIB", "docsMcastAuthProfilesDescription"), ("DOCS-MCAST-AUTH-MIB", "docsMcastAuthProfilesRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    docsMcastAuthGroup = docsMcastAuthGroup.setStatus('current')
if mibBuilder.loadTexts: docsMcastAuthGroup.setDescription('Group of objects implemented in the CMTS.')
mibBuilder.exportSymbols("DOCS-MCAST-AUTH-MIB", docsMcastAuthProfileSessRuleSrcPrefixLen=docsMcastAuthProfileSessRuleSrcPrefixLen, docsMcastAuthStaticSessRuleSrcPrefixLen=docsMcastAuthStaticSessRuleSrcPrefixLen, docsMcastAuthProfileSessRulePriority=docsMcastAuthProfileSessRulePriority, docsMcastAuthStaticSessRuleTable=docsMcastAuthStaticSessRuleTable, docsMcastAuthCtrl=docsMcastAuthCtrl, docsMcastAuthStaticSessRuleEntry=docsMcastAuthStaticSessRuleEntry, docsMcastAuthProfileSessRuleId=docsMcastAuthProfileSessRuleId, docsMcastAuthProfileSessRuleEntry=docsMcastAuthProfileSessRuleEntry, docsMcastAuthProfileSessRuleSrcPrefixAddr=docsMcastAuthProfileSessRuleSrcPrefixAddr, docsMcastAuthStaticSessRulePrefixAddrType=docsMcastAuthStaticSessRulePrefixAddrType, docsMcastAuthCtrlEnable=docsMcastAuthCtrlEnable, docsMcastAuthStaticSessRuleCfgListId=docsMcastAuthStaticSessRuleCfgListId, PYSNMP_MODULE_ID=docsMcastAuthMib, docsMcastAuthProfilesDescription=docsMcastAuthProfilesDescription, docsMcastAuthProfileSessRuleGrpPrefixLen=docsMcastAuthProfileSessRuleGrpPrefixLen, docsMcastAuthCtrlDefMaxNumSess=docsMcastAuthCtrlDefMaxNumSess, docsMcastAuthCmtsCmStatusMaxNumSess=docsMcastAuthCmtsCmStatusMaxNumSess, docsMcastAuthProfilesName=docsMcastAuthProfilesName, docsMcastAuthCmtsCmStatusCfgListId=docsMcastAuthCmtsCmStatusCfgListId, docsMcastAuthStaticSessRuleGrpPrefixLen=docsMcastAuthStaticSessRuleGrpPrefixLen, docsMcastAuthProfileSessRulePrefixAddrType=docsMcastAuthProfileSessRulePrefixAddrType, docsMcastAuthMibConformance=docsMcastAuthMibConformance, docsMcastAuthStaticSessRuleAction=docsMcastAuthStaticSessRuleAction, docsMcastAuthCmtsCmStatusCfgProfileNameList=docsMcastAuthCmtsCmStatusCfgProfileNameList, docsMcastAuthProfileSessRuleRowStatus=docsMcastAuthProfileSessRuleRowStatus, docsMcastAuthStaticSessRuleGrpPrefixAddr=docsMcastAuthStaticSessRuleGrpPrefixAddr, docsMcastAuthCtrlDefAction=docsMcastAuthCtrlDefAction, docsMcastAuthStaticSessRuleSrcPrefixAddr=docsMcastAuthStaticSessRuleSrcPrefixAddr, docsMcastAuthProfileSessRuleTable=docsMcastAuthProfileSessRuleTable, docsMcastAuthMib=docsMcastAuthMib, docsMcastAuthProfilesEntry=docsMcastAuthProfilesEntry, docsMcastAuthCmtsCmStatusCfgParamFlag=docsMcastAuthCmtsCmStatusCfgParamFlag, docsMcastAuthGroup=docsMcastAuthGroup, docsMcastAuthCtrlDefProfileNameList=docsMcastAuthCtrlDefProfileNameList, docsMcastAuthProfileSessRuleAction=docsMcastAuthProfileSessRuleAction, docsMcastAuthStaticSessRulePriority=docsMcastAuthStaticSessRulePriority, docsMcastAuthProfilesRowStatus=docsMcastAuthProfilesRowStatus, docsMcastAuthProfilesTable=docsMcastAuthProfilesTable, docsMcastAuthMibObjects=docsMcastAuthMibObjects, docsMcastAuthMibCompliances=docsMcastAuthMibCompliances, docsMcastAuthCompliance=docsMcastAuthCompliance, docsMcastAuthCmtsCmStatusTable=docsMcastAuthCmtsCmStatusTable, docsMcastAuthMibGroups=docsMcastAuthMibGroups, docsMcastAuthStaticSessRuleId=docsMcastAuthStaticSessRuleId, docsMcastAuthCmtsCmStatusEntry=docsMcastAuthCmtsCmStatusEntry, docsMcastAuthProfileSessRuleGrpPrefixAddr=docsMcastAuthProfileSessRuleGrpPrefixAddr)
