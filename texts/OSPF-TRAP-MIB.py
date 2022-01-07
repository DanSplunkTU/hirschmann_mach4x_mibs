#
# PySNMP MIB module OSPF-TRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/OSPF-TRAP-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:07:49 2022
# On host fv-az36-988 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ospfVirtNbrRestartHelperStatus, ospfLsdbType, ospfNbrRestartHelperAge, ospfRestartStatus, ospfAreaId, ospfVirtNbrRestartHelperExitReason, ospfVirtNbrArea, ospfRouterId, ospfNbrRestartHelperExitReason, ospfVirtIfNeighbor, ospfVirtNbrRestartHelperAge, ospfIfState, ospfVirtIfAreaId, ospfVirtNbrRtrId, ospfNbrRestartHelperStatus, ospfLsdbAreaId, ospfAddressLessIf, ospfIfIpAddress, ospfVirtIfState, ospfNbrRtrId, ospfNbrIpAddr, ospf, ospfExtLsdbLimit, ospfLsdbRouterId, ospfNbrAddressLessIndex, ospfVirtNbrState, ospfRestartInterval, ospfRestartExitReason, ospfLsdbLsid, ospfNbrState, ospfAreaNssaTranslatorState = mibBuilder.importSymbols("OSPF-MIB", "ospfVirtNbrRestartHelperStatus", "ospfLsdbType", "ospfNbrRestartHelperAge", "ospfRestartStatus", "ospfAreaId", "ospfVirtNbrRestartHelperExitReason", "ospfVirtNbrArea", "ospfRouterId", "ospfNbrRestartHelperExitReason", "ospfVirtIfNeighbor", "ospfVirtNbrRestartHelperAge", "ospfIfState", "ospfVirtIfAreaId", "ospfVirtNbrRtrId", "ospfNbrRestartHelperStatus", "ospfLsdbAreaId", "ospfAddressLessIf", "ospfIfIpAddress", "ospfVirtIfState", "ospfNbrRtrId", "ospfNbrIpAddr", "ospf", "ospfExtLsdbLimit", "ospfLsdbRouterId", "ospfNbrAddressLessIndex", "ospfVirtNbrState", "ospfRestartInterval", "ospfRestartExitReason", "ospfLsdbLsid", "ospfNbrState", "ospfAreaNssaTranslatorState")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Bits, Counter64, Unsigned32, ModuleIdentity, NotificationType, TimeTicks, Counter32, IpAddress, Integer32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, iso, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter64", "Unsigned32", "ModuleIdentity", "NotificationType", "TimeTicks", "Counter32", "IpAddress", "Integer32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "iso", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ospfTrap = ModuleIdentity((1, 3, 6, 1, 2, 1, 14, 16))
ospfTrap.setRevisions(('2006-11-10 00:00', '1995-01-20 12:25',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ospfTrap.setRevisionsDescriptions(('Updated for latest changes to OSPFv2:\n              -added graceful restart related traps\n              -added new config error types\n              -added ospfNssaTranslatorStatusChange trap.\n              See Appendix B of RFC 4750 for more details.\n\n             This version published as part of RFC 4750', 'The initial SMIv2 revision of this MIB module, published\n             in RFC 1850.',))
if mibBuilder.loadTexts: ospfTrap.setLastUpdated('200611100000Z')
if mibBuilder.loadTexts: ospfTrap.setOrganization('IETF OSPF Working Group')
if mibBuilder.loadTexts: ospfTrap.setContactInfo('WG E-Mail: ospf@ietf.org\n\n           WG Chairs: acee@cisco.com\n                      rohit@gmail.com\n\n           Editors:   Dan Joyal\n                      Nortel\n                      600 Technology Park Drive\n                      Billerica, MA  01821\n                      djoyal@nortel.com\n\n                      Piotr Galecki\n                      Airvana\n                      19 Alpha Road\n                      Chelmsford, MA 01824\n                      pgalecki@airvana.com\n\n                      Spencer Giacalone\n                      CSFB\n                      Eleven Madison Ave\n                      New York, NY 10010-3629\n\n                      spencer.giacalone@gmail.com')
if mibBuilder.loadTexts: ospfTrap.setDescription('The MIB module to describe traps for the OSPF\n             Version 2 Protocol.\n\n             Copyright (C) The IETF Trust (2006).\n             This version of this MIB module is part of\n             RFC 4750;  see the RFC itself for full legal\n             notices.')
ospfTrapControl = MibIdentifier((1, 3, 6, 1, 2, 1, 14, 16, 1))
ospfTraps = MibIdentifier((1, 3, 6, 1, 2, 1, 14, 16, 2))
ospfSetTrap = MibScalar((1, 3, 6, 1, 2, 1, 14, 16, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(4, 4)).setFixedLength(4)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ospfSetTrap.setStatus('current')
if mibBuilder.loadTexts: ospfSetTrap.setDescription('A 4-octet string serving as a bit map for\n             the trap events defined by the OSPF traps.  This\n             object is used to enable and disable specific\n             OSPF traps where a 1 in the bit field\n             represents enabled.  The right-most bit (least\n             significant) represents trap 0.\n\n             This object is persistent and when written\n\n             the entity SHOULD save the change to non-volatile\n             storage.')
ospfConfigErrorType = MibScalar((1, 3, 6, 1, 2, 1, 14, 16, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13))).clone(namedValues=NamedValues(("badVersion", 1), ("areaMismatch", 2), ("unknownNbmaNbr", 3), ("unknownVirtualNbr", 4), ("authTypeMismatch", 5), ("authFailure", 6), ("netMaskMismatch", 7), ("helloIntervalMismatch", 8), ("deadIntervalMismatch", 9), ("optionMismatch", 10), ("mtuMismatch", 11), ("duplicateRouterId", 12), ("noError", 13)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ospfConfigErrorType.setStatus('current')
if mibBuilder.loadTexts: ospfConfigErrorType.setDescription('Potential types of configuration conflicts.\n             Used by the ospfConfigError and\n             ospfConfigVirtError traps.  When the last value\n             of a trap using this object is needed, but no\n             traps of that type have been sent, this value\n             pertaining to this object should be returned as\n             noError.')
ospfPacketType = MibScalar((1, 3, 6, 1, 2, 1, 14, 16, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("hello", 1), ("dbDescript", 2), ("lsReq", 3), ("lsUpdate", 4), ("lsAck", 5), ("nullPacket", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ospfPacketType.setStatus('current')
if mibBuilder.loadTexts: ospfPacketType.setDescription('OSPF packet types.  When the last value of a trap\n             using this object is needed, but no traps of\n             that type have been sent, this value pertaining\n             to this object should be returned as nullPacket.')
ospfPacketSrc = MibScalar((1, 3, 6, 1, 2, 1, 14, 16, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ospfPacketSrc.setStatus('current')
if mibBuilder.loadTexts: ospfPacketSrc.setDescription('The IP address of an inbound packet that cannot\n             be identified by a neighbor instance.  When\n             the last value of a trap using this object is\n             needed, but no traps of that type have been sent,\n             this value pertaining to this object should\n             be returned as 0.0.0.0.')
ospfVirtIfStateChange = NotificationType((1, 3, 6, 1, 2, 1, 14, 16, 2, 1)).setObjects(("OSPF-MIB", "ospfRouterId"), ("OSPF-MIB", "ospfVirtIfAreaId"), ("OSPF-MIB", "ospfVirtIfNeighbor"), ("OSPF-MIB", "ospfVirtIfState"))
if mibBuilder.loadTexts: ospfVirtIfStateChange.setStatus('current')
if mibBuilder.loadTexts: ospfVirtIfStateChange.setDescription('An ospfVirtIfStateChange trap signifies that there\n             has been a change in the state of an OSPF virtual\n             interface.\n\n             This trap should be generated when the interface\n             state regresses (e.g., goes from Point-to-Point to Down)\n             or progresses to a terminal state\n             (i.e., Point-to-Point).')
ospfNbrStateChange = NotificationType((1, 3, 6, 1, 2, 1, 14, 16, 2, 2)).setObjects(("OSPF-MIB", "ospfRouterId"), ("OSPF-MIB", "ospfNbrIpAddr"), ("OSPF-MIB", "ospfNbrAddressLessIndex"), ("OSPF-MIB", "ospfNbrRtrId"), ("OSPF-MIB", "ospfNbrState"))
if mibBuilder.loadTexts: ospfNbrStateChange.setStatus('current')
if mibBuilder.loadTexts: ospfNbrStateChange.setDescription('An ospfNbrStateChange trap signifies that\n             there has been a change in the state of a\n             non-virtual OSPF neighbor.  This trap should be\n             generated when the neighbor state regresses\n             (e.g., goes from Attempt or Full to 1-Way or\n             Down) or progresses to a terminal state (e.g.,\n\n             2-Way or Full).  When an neighbor transitions\n             from or to Full on non-broadcast multi-access\n             and broadcast networks, the trap should be\n             generated by the designated router.  A designated\n             router transitioning to Down will be noted by\n             ospfIfStateChange.')
ospfVirtNbrStateChange = NotificationType((1, 3, 6, 1, 2, 1, 14, 16, 2, 3)).setObjects(("OSPF-MIB", "ospfRouterId"), ("OSPF-MIB", "ospfVirtNbrArea"), ("OSPF-MIB", "ospfVirtNbrRtrId"), ("OSPF-MIB", "ospfVirtNbrState"))
if mibBuilder.loadTexts: ospfVirtNbrStateChange.setStatus('current')
if mibBuilder.loadTexts: ospfVirtNbrStateChange.setDescription('An ospfVirtNbrStateChange trap signifies that there\n             has been a change in the state of an OSPF virtual\n             neighbor.  This trap should be generated\n             when the neighbor state regresses (e.g., goes\n             from Attempt or Full to 1-Way or Down) or\n             progresses to a terminal state (e.g., Full).')
ospfIfConfigError = NotificationType((1, 3, 6, 1, 2, 1, 14, 16, 2, 4)).setObjects(("OSPF-MIB", "ospfRouterId"), ("OSPF-MIB", "ospfIfIpAddress"), ("OSPF-MIB", "ospfAddressLessIf"), ("OSPF-TRAP-MIB", "ospfPacketSrc"), ("OSPF-TRAP-MIB", "ospfConfigErrorType"), ("OSPF-TRAP-MIB", "ospfPacketType"))
if mibBuilder.loadTexts: ospfIfConfigError.setStatus('current')
if mibBuilder.loadTexts: ospfIfConfigError.setDescription("An ospfIfConfigError trap signifies that a\n             packet has been received on a non-virtual\n             interface from a router whose configuration\n             parameters conflict with this router's\n             configuration parameters.  Note that the event\n             optionMismatch should cause a trap only if it\n             prevents an adjacency from forming.")
ospfVirtIfConfigError = NotificationType((1, 3, 6, 1, 2, 1, 14, 16, 2, 5)).setObjects(("OSPF-MIB", "ospfRouterId"), ("OSPF-MIB", "ospfVirtIfAreaId"), ("OSPF-MIB", "ospfVirtIfNeighbor"), ("OSPF-TRAP-MIB", "ospfConfigErrorType"), ("OSPF-TRAP-MIB", "ospfPacketType"))
if mibBuilder.loadTexts: ospfVirtIfConfigError.setStatus('current')
if mibBuilder.loadTexts: ospfVirtIfConfigError.setDescription("An ospfVirtIfConfigError trap signifies that a\n             packet has been received on a virtual interface\n             from a router whose configuration parameters\n             conflict with this router's configuration\n             parameters.  Note that the event optionMismatch\n             should cause a trap only if it prevents an\n             adjacency from forming.")
ospfIfAuthFailure = NotificationType((1, 3, 6, 1, 2, 1, 14, 16, 2, 6)).setObjects(("OSPF-MIB", "ospfRouterId"), ("OSPF-MIB", "ospfIfIpAddress"), ("OSPF-MIB", "ospfAddressLessIf"), ("OSPF-TRAP-MIB", "ospfPacketSrc"), ("OSPF-TRAP-MIB", "ospfConfigErrorType"), ("OSPF-TRAP-MIB", "ospfPacketType"))
if mibBuilder.loadTexts: ospfIfAuthFailure.setStatus('current')
if mibBuilder.loadTexts: ospfIfAuthFailure.setDescription("An ospfIfAuthFailure trap signifies that a\n             packet has been received on a non-virtual\n             interface from a router whose authentication key\n             or authentication type conflicts with this\n             router's authentication key or authentication\n             type.")
ospfVirtIfAuthFailure = NotificationType((1, 3, 6, 1, 2, 1, 14, 16, 2, 7)).setObjects(("OSPF-MIB", "ospfRouterId"), ("OSPF-MIB", "ospfVirtIfAreaId"), ("OSPF-MIB", "ospfVirtIfNeighbor"), ("OSPF-TRAP-MIB", "ospfConfigErrorType"), ("OSPF-TRAP-MIB", "ospfPacketType"))
if mibBuilder.loadTexts: ospfVirtIfAuthFailure.setStatus('current')
if mibBuilder.loadTexts: ospfVirtIfAuthFailure.setDescription("An ospfVirtIfAuthFailure trap signifies that a\n             packet has been received on a virtual interface\n             from a router whose authentication key or\n             authentication type conflicts with this router's\n             authentication key or authentication type.")
ospfIfRxBadPacket = NotificationType((1, 3, 6, 1, 2, 1, 14, 16, 2, 8)).setObjects(("OSPF-MIB", "ospfRouterId"), ("OSPF-MIB", "ospfIfIpAddress"), ("OSPF-MIB", "ospfAddressLessIf"), ("OSPF-TRAP-MIB", "ospfPacketSrc"), ("OSPF-TRAP-MIB", "ospfPacketType"))
if mibBuilder.loadTexts: ospfIfRxBadPacket.setStatus('current')
if mibBuilder.loadTexts: ospfIfRxBadPacket.setDescription('An ospfIfRxBadPacket trap signifies that an\n             OSPF packet has been received on a non-virtual\n             interface that cannot be parsed.')
ospfVirtIfRxBadPacket = NotificationType((1, 3, 6, 1, 2, 1, 14, 16, 2, 9)).setObjects(("OSPF-MIB", "ospfRouterId"), ("OSPF-MIB", "ospfVirtIfAreaId"), ("OSPF-MIB", "ospfVirtIfNeighbor"), ("OSPF-TRAP-MIB", "ospfPacketType"))
if mibBuilder.loadTexts: ospfVirtIfRxBadPacket.setStatus('current')
if mibBuilder.loadTexts: ospfVirtIfRxBadPacket.setDescription('An ospfVirtIfRxBadPacket trap signifies that an OSPF\n             packet has been received on a virtual interface\n             that cannot be parsed.')
ospfTxRetransmit = NotificationType((1, 3, 6, 1, 2, 1, 14, 16, 2, 10)).setObjects(("OSPF-MIB", "ospfRouterId"), ("OSPF-MIB", "ospfIfIpAddress"), ("OSPF-MIB", "ospfAddressLessIf"), ("OSPF-MIB", "ospfNbrRtrId"), ("OSPF-TRAP-MIB", "ospfPacketType"), ("OSPF-MIB", "ospfLsdbType"), ("OSPF-MIB", "ospfLsdbLsid"), ("OSPF-MIB", "ospfLsdbRouterId"))
if mibBuilder.loadTexts: ospfTxRetransmit.setStatus('current')
if mibBuilder.loadTexts: ospfTxRetransmit.setDescription('An ospfTxRetransmit trap signifies than an\n              OSPF packet has been retransmitted on a\n              non-virtual interface.  All packets that may be\n              retransmitted are associated with an LSDB entry.\n              The LS type, LS ID, and Router ID are used to\n              identify the LSDB entry.')
ospfVirtIfTxRetransmit = NotificationType((1, 3, 6, 1, 2, 1, 14, 16, 2, 11)).setObjects(("OSPF-MIB", "ospfRouterId"), ("OSPF-MIB", "ospfVirtIfAreaId"), ("OSPF-MIB", "ospfVirtIfNeighbor"), ("OSPF-TRAP-MIB", "ospfPacketType"), ("OSPF-MIB", "ospfLsdbType"), ("OSPF-MIB", "ospfLsdbLsid"), ("OSPF-MIB", "ospfLsdbRouterId"))
if mibBuilder.loadTexts: ospfVirtIfTxRetransmit.setStatus('current')
if mibBuilder.loadTexts: ospfVirtIfTxRetransmit.setDescription('An ospfVirtIfTxRetransmit trap signifies than an\n             OSPF packet has been retransmitted on a virtual\n             interface.  All packets that may be retransmitted\n             are associated with an LSDB entry.  The LS\n             type, LS ID, and Router ID are used to identify\n             the LSDB entry.')
ospfOriginateLsa = NotificationType((1, 3, 6, 1, 2, 1, 14, 16, 2, 12)).setObjects(("OSPF-MIB", "ospfRouterId"), ("OSPF-MIB", "ospfLsdbAreaId"), ("OSPF-MIB", "ospfLsdbType"), ("OSPF-MIB", "ospfLsdbLsid"), ("OSPF-MIB", "ospfLsdbRouterId"))
if mibBuilder.loadTexts: ospfOriginateLsa.setStatus('current')
if mibBuilder.loadTexts: ospfOriginateLsa.setDescription('An ospfOriginateLsa trap signifies that a new\n             LSA has been originated by this router.  This\n             trap should not be invoked for simple refreshes\n             of LSAs (which happens every 30 minutes), but\n             instead will only be invoked when an LSA is\n             (re)originated due to a topology change.\n             Additionally, this trap does not include LSAs that\n             are being flushed because they have reached\n             MaxAge.')
ospfMaxAgeLsa = NotificationType((1, 3, 6, 1, 2, 1, 14, 16, 2, 13)).setObjects(("OSPF-MIB", "ospfRouterId"), ("OSPF-MIB", "ospfLsdbAreaId"), ("OSPF-MIB", "ospfLsdbType"), ("OSPF-MIB", "ospfLsdbLsid"), ("OSPF-MIB", "ospfLsdbRouterId"))
if mibBuilder.loadTexts: ospfMaxAgeLsa.setStatus('current')
if mibBuilder.loadTexts: ospfMaxAgeLsa.setDescription("An ospfMaxAgeLsa trap signifies that one of\n             the LSAs in the router's link state database has\n             aged to MaxAge.")
ospfLsdbOverflow = NotificationType((1, 3, 6, 1, 2, 1, 14, 16, 2, 14)).setObjects(("OSPF-MIB", "ospfRouterId"), ("OSPF-MIB", "ospfExtLsdbLimit"))
if mibBuilder.loadTexts: ospfLsdbOverflow.setStatus('current')
if mibBuilder.loadTexts: ospfLsdbOverflow.setDescription("An ospfLsdbOverflow trap signifies that the\n             number of LSAs in the router's link state\n             database has exceeded ospfExtLsdbLimit.")
ospfLsdbApproachingOverflow = NotificationType((1, 3, 6, 1, 2, 1, 14, 16, 2, 15)).setObjects(("OSPF-MIB", "ospfRouterId"), ("OSPF-MIB", "ospfExtLsdbLimit"))
if mibBuilder.loadTexts: ospfLsdbApproachingOverflow.setStatus('current')
if mibBuilder.loadTexts: ospfLsdbApproachingOverflow.setDescription("An ospfLsdbApproachingOverflow trap signifies\n             that the number of LSAs in the router's\n             link state database has exceeded ninety percent of\n             ospfExtLsdbLimit.")
ospfIfStateChange = NotificationType((1, 3, 6, 1, 2, 1, 14, 16, 2, 16)).setObjects(("OSPF-MIB", "ospfRouterId"), ("OSPF-MIB", "ospfIfIpAddress"), ("OSPF-MIB", "ospfAddressLessIf"), ("OSPF-MIB", "ospfIfState"))
if mibBuilder.loadTexts: ospfIfStateChange.setStatus('current')
if mibBuilder.loadTexts: ospfIfStateChange.setDescription('An ospfIfStateChange trap signifies that there\n             has been a change in the state of a non-virtual\n             OSPF interface.  This trap should be generated\n             when the interface state regresses (e.g., goes\n             from Dr to Down) or progresses to a terminal\n             state (i.e., Point-to-Point, DR Other, Dr, or\n             Backup).')
ospfNssaTranslatorStatusChange = NotificationType((1, 3, 6, 1, 2, 1, 14, 16, 2, 17)).setObjects(("OSPF-MIB", "ospfRouterId"), ("OSPF-MIB", "ospfAreaId"), ("OSPF-MIB", "ospfAreaNssaTranslatorState"))
if mibBuilder.loadTexts: ospfNssaTranslatorStatusChange.setStatus('current')
if mibBuilder.loadTexts: ospfNssaTranslatorStatusChange.setDescription("An ospfNssaTranslatorStatusChange trap indicates that\n             there has been a change in the router's ability to\n             translate OSPF type-7 LSAs into OSPF type-5 LSAs.\n             This trap should be generated when the translator\n             status transitions from or to any defined status on\n             a per-area basis.")
ospfRestartStatusChange = NotificationType((1, 3, 6, 1, 2, 1, 14, 16, 2, 18)).setObjects(("OSPF-MIB", "ospfRouterId"), ("OSPF-MIB", "ospfRestartStatus"), ("OSPF-MIB", "ospfRestartInterval"), ("OSPF-MIB", "ospfRestartExitReason"))
if mibBuilder.loadTexts: ospfRestartStatusChange.setStatus('current')
if mibBuilder.loadTexts: ospfRestartStatusChange.setDescription('An ospfRestartStatusChange trap signifies that\n             there has been a change in the graceful restart\n             state for the router.  This trap should be\n             generated when the router restart status\n             changes.')
ospfNbrRestartHelperStatusChange = NotificationType((1, 3, 6, 1, 2, 1, 14, 16, 2, 19)).setObjects(("OSPF-MIB", "ospfRouterId"), ("OSPF-MIB", "ospfNbrIpAddr"), ("OSPF-MIB", "ospfNbrAddressLessIndex"), ("OSPF-MIB", "ospfNbrRtrId"), ("OSPF-MIB", "ospfNbrRestartHelperStatus"), ("OSPF-MIB", "ospfNbrRestartHelperAge"), ("OSPF-MIB", "ospfNbrRestartHelperExitReason"))
if mibBuilder.loadTexts: ospfNbrRestartHelperStatusChange.setStatus('current')
if mibBuilder.loadTexts: ospfNbrRestartHelperStatusChange.setDescription('An ospfNbrRestartHelperStatusChange trap signifies that\n             there has been a change in the graceful restart\n             helper state for the neighbor.  This trap should be\n             generated when the neighbor restart helper status\n             transitions for a neighbor.')
ospfVirtNbrRestartHelperStatusChange = NotificationType((1, 3, 6, 1, 2, 1, 14, 16, 2, 20)).setObjects(("OSPF-MIB", "ospfRouterId"), ("OSPF-MIB", "ospfVirtNbrArea"), ("OSPF-MIB", "ospfVirtNbrRtrId"), ("OSPF-MIB", "ospfVirtNbrRestartHelperStatus"), ("OSPF-MIB", "ospfVirtNbrRestartHelperAge"), ("OSPF-MIB", "ospfVirtNbrRestartHelperExitReason"))
if mibBuilder.loadTexts: ospfVirtNbrRestartHelperStatusChange.setStatus('current')
if mibBuilder.loadTexts: ospfVirtNbrRestartHelperStatusChange.setDescription('An ospfVirtNbrRestartHelperStatusChange trap signifies\n             that there has been a change in the graceful restart\n             helper state for the virtual neighbor.  This trap should\n             be generated when the virtual neighbor restart helper\n             status transitions for a virtual neighbor.')
ospfTrapConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 14, 16, 3))
ospfTrapGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 14, 16, 3, 1))
ospfTrapCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 14, 16, 3, 2))
ospfTrapCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 14, 16, 3, 2, 1)).setObjects(("OSPF-TRAP-MIB", "ospfTrapControlGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ospfTrapCompliance = ospfTrapCompliance.setStatus('obsolete')
if mibBuilder.loadTexts: ospfTrapCompliance.setDescription('The compliance statement.')
ospfTrapCompliance2 = ModuleCompliance((1, 3, 6, 1, 2, 1, 14, 16, 3, 2, 2)).setObjects(("OSPF-TRAP-MIB", "ospfTrapControlGroup"), ("OSPF-TRAP-MIB", "ospfTrapEventGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ospfTrapCompliance2 = ospfTrapCompliance2.setStatus('current')
if mibBuilder.loadTexts: ospfTrapCompliance2.setDescription('The compliance statement.')
ospfTrapControlGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 14, 16, 3, 1, 1)).setObjects(("OSPF-TRAP-MIB", "ospfSetTrap"), ("OSPF-TRAP-MIB", "ospfConfigErrorType"), ("OSPF-TRAP-MIB", "ospfPacketType"), ("OSPF-TRAP-MIB", "ospfPacketSrc"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ospfTrapControlGroup = ospfTrapControlGroup.setStatus('current')
if mibBuilder.loadTexts: ospfTrapControlGroup.setDescription('These objects are required to control traps\n             from OSPF systems.')
ospfTrapEventGroup = NotificationGroup((1, 3, 6, 1, 2, 1, 14, 16, 3, 1, 2)).setObjects(("OSPF-TRAP-MIB", "ospfVirtIfStateChange"), ("OSPF-TRAP-MIB", "ospfNbrStateChange"), ("OSPF-TRAP-MIB", "ospfVirtNbrStateChange"), ("OSPF-TRAP-MIB", "ospfIfConfigError"), ("OSPF-TRAP-MIB", "ospfVirtIfConfigError"), ("OSPF-TRAP-MIB", "ospfIfAuthFailure"), ("OSPF-TRAP-MIB", "ospfVirtIfAuthFailure"), ("OSPF-TRAP-MIB", "ospfIfRxBadPacket"), ("OSPF-TRAP-MIB", "ospfVirtIfRxBadPacket"), ("OSPF-TRAP-MIB", "ospfTxRetransmit"), ("OSPF-TRAP-MIB", "ospfVirtIfTxRetransmit"), ("OSPF-TRAP-MIB", "ospfOriginateLsa"), ("OSPF-TRAP-MIB", "ospfMaxAgeLsa"), ("OSPF-TRAP-MIB", "ospfLsdbOverflow"), ("OSPF-TRAP-MIB", "ospfLsdbApproachingOverflow"), ("OSPF-TRAP-MIB", "ospfIfStateChange"), ("OSPF-TRAP-MIB", "ospfNssaTranslatorStatusChange"), ("OSPF-TRAP-MIB", "ospfRestartStatusChange"), ("OSPF-TRAP-MIB", "ospfNbrRestartHelperStatusChange"), ("OSPF-TRAP-MIB", "ospfVirtNbrRestartHelperStatusChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ospfTrapEventGroup = ospfTrapEventGroup.setStatus('current')
if mibBuilder.loadTexts: ospfTrapEventGroup.setDescription('A grouping of OSPF trap events, as specified\n             in NOTIFICATION-TYPE constructs.')
mibBuilder.exportSymbols("OSPF-TRAP-MIB", ospfConfigErrorType=ospfConfigErrorType, ospfLsdbOverflow=ospfLsdbOverflow, ospfOriginateLsa=ospfOriginateLsa, ospfIfStateChange=ospfIfStateChange, ospfIfConfigError=ospfIfConfigError, ospfNbrStateChange=ospfNbrStateChange, ospfVirtIfConfigError=ospfVirtIfConfigError, ospfMaxAgeLsa=ospfMaxAgeLsa, ospfTrapControl=ospfTrapControl, ospfLsdbApproachingOverflow=ospfLsdbApproachingOverflow, ospfVirtIfAuthFailure=ospfVirtIfAuthFailure, ospfTrapCompliance=ospfTrapCompliance, ospfPacketSrc=ospfPacketSrc, ospfRestartStatusChange=ospfRestartStatusChange, ospfIfRxBadPacket=ospfIfRxBadPacket, ospfTrapGroups=ospfTrapGroups, ospfTrapCompliances=ospfTrapCompliances, ospfTraps=ospfTraps, ospfVirtNbrStateChange=ospfVirtNbrStateChange, ospfPacketType=ospfPacketType, ospfTrapConformance=ospfTrapConformance, ospfVirtIfTxRetransmit=ospfVirtIfTxRetransmit, ospfVirtIfStateChange=ospfVirtIfStateChange, ospfTrapControlGroup=ospfTrapControlGroup, ospfTrap=ospfTrap, ospfSetTrap=ospfSetTrap, ospfNssaTranslatorStatusChange=ospfNssaTranslatorStatusChange, ospfTrapEventGroup=ospfTrapEventGroup, ospfNbrRestartHelperStatusChange=ospfNbrRestartHelperStatusChange, ospfVirtIfRxBadPacket=ospfVirtIfRxBadPacket, ospfTxRetransmit=ospfTxRetransmit, ospfIfAuthFailure=ospfIfAuthFailure, PYSNMP_MODULE_ID=ospfTrap, ospfTrapCompliance2=ospfTrapCompliance2, ospfVirtNbrRestartHelperStatusChange=ospfVirtNbrRestartHelperStatusChange)
