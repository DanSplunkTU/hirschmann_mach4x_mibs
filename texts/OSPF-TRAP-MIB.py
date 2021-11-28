#
# PySNMP MIB module OSPF-TRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/OSPF-TRAP-MIB
# Produced by pysmi-1.1.3 at Sun Nov 28 20:09:06 2021
# On host fv-az77-612 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
ospfVirtIfState, ospfLsdbType, ospfLsdbAreaId, ospfExtLsdbLimit, ospfLsdbLsid, ospfLsdbRouterId, ospfAddressLessIf, ospfVirtNbrRtrId, ospfNbrState, ospfNbrIpAddr, ospfNbrAddressLessIndex, ospfVirtIfAreaId, ospfVirtNbrArea, ospfIfState, ospfVirtNbrState, ospfRouterId, ospfVirtIfNeighbor, ospf, ospfIfIpAddress, ospfNbrRtrId = mibBuilder.importSymbols("OSPF-MIB", "ospfVirtIfState", "ospfLsdbType", "ospfLsdbAreaId", "ospfExtLsdbLimit", "ospfLsdbLsid", "ospfLsdbRouterId", "ospfAddressLessIf", "ospfVirtNbrRtrId", "ospfNbrState", "ospfNbrIpAddr", "ospfNbrAddressLessIndex", "ospfVirtIfAreaId", "ospfVirtNbrArea", "ospfIfState", "ospfVirtNbrState", "ospfRouterId", "ospfVirtIfNeighbor", "ospf", "ospfIfIpAddress", "ospfNbrRtrId")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
TimeTicks, Integer32, Counter64, Gauge32, ModuleIdentity, MibIdentifier, iso, ObjectIdentity, Unsigned32, NotificationType, Counter32, Bits, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Integer32", "Counter64", "Gauge32", "ModuleIdentity", "MibIdentifier", "iso", "ObjectIdentity", "Unsigned32", "NotificationType", "Counter32", "Bits", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ospfTrap = ModuleIdentity((1, 3, 6, 1, 2, 1, 14, 16))
if mibBuilder.loadTexts: ospfTrap.setLastUpdated('9501201225Z')
if mibBuilder.loadTexts: ospfTrap.setOrganization('IETF OSPF Working Group')
if mibBuilder.loadTexts: ospfTrap.setContactInfo('                      Fred Baker\n           Postal:                Cisco Systems\n                                  519 Lado Drive\n                                  Santa Barbara, California 93111\n           Tel:                   +1 805 681 0115\n           E-Mail:                fred@cisco.com\n\n                                  Rob Coltun\n           Postal:                RainbowBridge Communications\n           Tel:                   (301) 340-9416\n           E-Mail:                rcoltun@rainbow-bridge.com')
if mibBuilder.loadTexts: ospfTrap.setDescription('The MIB module to describe traps for  the  OSPF\n          Version 2 Protocol.')
ospfTrapControl = MibIdentifier((1, 3, 6, 1, 2, 1, 14, 16, 1))
ospfTraps = MibIdentifier((1, 3, 6, 1, 2, 1, 14, 16, 2))
ospfSetTrap = MibScalar((1, 3, 6, 1, 2, 1, 14, 16, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(4, 4)).setFixedLength(4)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ospfSetTrap.setStatus('current')
if mibBuilder.loadTexts: ospfSetTrap.setDescription('A four-octet string serving as a bit  map  for\n           the trap events defined by the OSPF traps. This\n           object is used to enable and  disable  specific\n           OSPF   traps   where  a  1  in  the  bit  field\n           represents enabled.  The right-most bit  (least\n           significant) represents trap 0.')
ospfConfigErrorType = MibScalar((1, 3, 6, 1, 2, 1, 14, 16, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("badVersion", 1), ("areaMismatch", 2), ("unknownNbmaNbr", 3), ("unknownVirtualNbr", 4), ("authTypeMismatch", 5), ("authFailure", 6), ("netMaskMismatch", 7), ("helloIntervalMismatch", 8), ("deadIntervalMismatch", 9), ("optionMismatch", 10)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ospfConfigErrorType.setStatus('current')
if mibBuilder.loadTexts: ospfConfigErrorType.setDescription('Potential types  of  configuration  conflicts.\n           Used  by the ospfConfigError and ospfConfigVir-\n           tError traps.')
ospfPacketType = MibScalar((1, 3, 6, 1, 2, 1, 14, 16, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("hello", 1), ("dbDescript", 2), ("lsReq", 3), ("lsUpdate", 4), ("lsAck", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ospfPacketType.setStatus('current')
if mibBuilder.loadTexts: ospfPacketType.setDescription('OSPF packet types.')
ospfPacketSrc = MibScalar((1, 3, 6, 1, 2, 1, 14, 16, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ospfPacketSrc.setStatus('current')
if mibBuilder.loadTexts: ospfPacketSrc.setDescription('The IP address of an inbound packet that  can-\n           not be identified by a neighbor instance.')
ospfIfStateChange = NotificationType((1, 3, 6, 1, 2, 1, 14, 16, 2, 16)).setObjects(("OSPF-MIB", "ospfRouterId"), ("OSPF-MIB", "ospfIfIpAddress"), ("OSPF-MIB", "ospfAddressLessIf"), ("OSPF-MIB", "ospfIfState"))
if mibBuilder.loadTexts: ospfIfStateChange.setStatus('current')
if mibBuilder.loadTexts: ospfIfStateChange.setDescription('An ospfIfStateChange trap signifies that there\n           has been a change in the state of a non-virtual\n           OSPF interface. This trap should  be  generated\n           when  the interface state regresses (e.g., goes\n           from Dr to Down) or progresses  to  a  terminal\n           state  (i.e.,  Point-to-Point, DR Other, Dr, or\n           Backup).')
ospfVirtIfStateChange = NotificationType((1, 3, 6, 1, 2, 1, 14, 16, 2, 1)).setObjects(("OSPF-MIB", "ospfRouterId"), ("OSPF-MIB", "ospfVirtIfAreaId"), ("OSPF-MIB", "ospfVirtIfNeighbor"), ("OSPF-MIB", "ospfVirtIfState"))
if mibBuilder.loadTexts: ospfVirtIfStateChange.setStatus('current')
if mibBuilder.loadTexts: ospfVirtIfStateChange.setDescription('An ospfIfStateChange trap signifies that there\n           has  been a change in the state of an OSPF vir-\n           tual interface.\n           This trap should be generated when  the  inter-\n           face  state  regresses  (e.g., goes from Point-\n           to-Point to Down) or progresses to  a  terminal\n           state (i.e., Point-to-Point).')
ospfNbrStateChange = NotificationType((1, 3, 6, 1, 2, 1, 14, 16, 2, 2)).setObjects(("OSPF-MIB", "ospfRouterId"), ("OSPF-MIB", "ospfNbrIpAddr"), ("OSPF-MIB", "ospfNbrAddressLessIndex"), ("OSPF-MIB", "ospfNbrRtrId"), ("OSPF-MIB", "ospfNbrState"))
if mibBuilder.loadTexts: ospfNbrStateChange.setStatus('current')
if mibBuilder.loadTexts: ospfNbrStateChange.setDescription('An  ospfNbrStateChange  trap  signifies   that\n           there  has been a change in the state of a non-\n           virtual OSPF neighbor.   This  trap  should  be\n           generated  when  the  neighbor  state regresses\n           (e.g., goes from Attempt or Full  to  1-Way  or\n           Down)  or progresses to a terminal state (e.g.,\n           2-Way or Full).  When an  neighbor  transitions\n           from  or  to Full on non-broadcast multi-access\n           and broadcast networks, the trap should be gen-\n           erated  by the designated router.  A designated\n           router transitioning to Down will be  noted  by\n           ospfIfStateChange.')
ospfVirtNbrStateChange = NotificationType((1, 3, 6, 1, 2, 1, 14, 16, 2, 3)).setObjects(("OSPF-MIB", "ospfRouterId"), ("OSPF-MIB", "ospfVirtNbrArea"), ("OSPF-MIB", "ospfVirtNbrRtrId"), ("OSPF-MIB", "ospfVirtNbrState"))
if mibBuilder.loadTexts: ospfVirtNbrStateChange.setStatus('current')
if mibBuilder.loadTexts: ospfVirtNbrStateChange.setDescription('An ospfIfStateChange trap signifies that there\n           has  been a change in the state of an OSPF vir-\n           tual neighbor.  This trap should  be  generated\n           when  the  neighbor state regresses (e.g., goes\n           from Attempt or  Full  to  1-Way  or  Down)  or\n           progresses to a terminal state (e.g., Full).')
ospfIfConfigError = NotificationType((1, 3, 6, 1, 2, 1, 14, 16, 2, 4)).setObjects(("OSPF-MIB", "ospfRouterId"), ("OSPF-MIB", "ospfIfIpAddress"), ("OSPF-MIB", "ospfAddressLessIf"), ("OSPF-TRAP-MIB", "ospfPacketSrc"), ("OSPF-TRAP-MIB", "ospfConfigErrorType"), ("OSPF-TRAP-MIB", "ospfPacketType"))
if mibBuilder.loadTexts: ospfIfConfigError.setStatus('current')
if mibBuilder.loadTexts: ospfIfConfigError.setDescription("An ospfIfConfigError  trap  signifies  that  a\n           packet  has  been received on a non-virtual in-\n           terface  from  a  router  whose   configuration\n           parameters  conflict  with this router's confi-\n           guration parameters.  Note that the  event  op-\n           tionMismatch  should  cause  a  trap only if it\n           prevents an adjacency from forming.")
ospfVirtIfConfigError = NotificationType((1, 3, 6, 1, 2, 1, 14, 16, 2, 5)).setObjects(("OSPF-MIB", "ospfRouterId"), ("OSPF-MIB", "ospfVirtIfAreaId"), ("OSPF-MIB", "ospfVirtIfNeighbor"), ("OSPF-TRAP-MIB", "ospfConfigErrorType"), ("OSPF-TRAP-MIB", "ospfPacketType"))
if mibBuilder.loadTexts: ospfVirtIfConfigError.setStatus('current')
if mibBuilder.loadTexts: ospfVirtIfConfigError.setDescription("An ospfConfigError trap signifies that a pack-\n           et  has  been  received  on a virtual interface\n           from a router  whose  configuration  parameters\n           conflict   with   this  router's  configuration\n           parameters.  Note that the event optionMismatch\n           should  cause a trap only if it prevents an ad-\n           jacency from forming.")
ospfIfAuthFailure = NotificationType((1, 3, 6, 1, 2, 1, 14, 16, 2, 6)).setObjects(("OSPF-MIB", "ospfRouterId"), ("OSPF-MIB", "ospfIfIpAddress"), ("OSPF-MIB", "ospfAddressLessIf"), ("OSPF-TRAP-MIB", "ospfPacketSrc"), ("OSPF-TRAP-MIB", "ospfConfigErrorType"), ("OSPF-TRAP-MIB", "ospfPacketType"))
if mibBuilder.loadTexts: ospfIfAuthFailure.setStatus('current')
if mibBuilder.loadTexts: ospfIfAuthFailure.setDescription("An ospfIfAuthFailure  trap  signifies  that  a\n           packet  has  been received on a non-virtual in-\n           terface from a router whose authentication  key\n           or  authentication  type  conflicts  with  this\n           router's authentication key  or  authentication\n           type.")
ospfVirtIfAuthFailure = NotificationType((1, 3, 6, 1, 2, 1, 14, 16, 2, 7)).setObjects(("OSPF-MIB", "ospfRouterId"), ("OSPF-MIB", "ospfVirtIfAreaId"), ("OSPF-MIB", "ospfVirtIfNeighbor"), ("OSPF-TRAP-MIB", "ospfConfigErrorType"), ("OSPF-TRAP-MIB", "ospfPacketType"))
if mibBuilder.loadTexts: ospfVirtIfAuthFailure.setStatus('current')
if mibBuilder.loadTexts: ospfVirtIfAuthFailure.setDescription("An ospfVirtIfAuthFailure trap signifies that a\n           packet has been received on a virtual interface\n           from a router whose authentication key  or  au-\n           thentication  type conflicts with this router's\n           authentication key or authentication type.")
ospfIfRxBadPacket = NotificationType((1, 3, 6, 1, 2, 1, 14, 16, 2, 8)).setObjects(("OSPF-MIB", "ospfRouterId"), ("OSPF-MIB", "ospfIfIpAddress"), ("OSPF-MIB", "ospfAddressLessIf"), ("OSPF-TRAP-MIB", "ospfPacketSrc"), ("OSPF-TRAP-MIB", "ospfPacketType"))
if mibBuilder.loadTexts: ospfIfRxBadPacket.setStatus('current')
if mibBuilder.loadTexts: ospfIfRxBadPacket.setDescription('An ospfIfRxBadPacket trap  signifies  that  an\n           OSPF  packet has been received on a non-virtual\n           interface that cannot be parsed.')
ospfVirtIfRxBadPacket = NotificationType((1, 3, 6, 1, 2, 1, 14, 16, 2, 9)).setObjects(("OSPF-MIB", "ospfRouterId"), ("OSPF-MIB", "ospfVirtIfAreaId"), ("OSPF-MIB", "ospfVirtIfNeighbor"), ("OSPF-TRAP-MIB", "ospfPacketType"))
if mibBuilder.loadTexts: ospfVirtIfRxBadPacket.setStatus('current')
if mibBuilder.loadTexts: ospfVirtIfRxBadPacket.setDescription('An ospfRxBadPacket trap signifies that an OSPF\n           packet has been received on a virtual interface\n           that cannot be parsed.')
ospfTxRetransmit = NotificationType((1, 3, 6, 1, 2, 1, 14, 16, 2, 10)).setObjects(("OSPF-MIB", "ospfRouterId"), ("OSPF-MIB", "ospfIfIpAddress"), ("OSPF-MIB", "ospfAddressLessIf"), ("OSPF-MIB", "ospfNbrRtrId"), ("OSPF-TRAP-MIB", "ospfPacketType"), ("OSPF-MIB", "ospfLsdbType"), ("OSPF-MIB", "ospfLsdbLsid"), ("OSPF-MIB", "ospfLsdbRouterId"))
if mibBuilder.loadTexts: ospfTxRetransmit.setStatus('current')
if mibBuilder.loadTexts: ospfTxRetransmit.setDescription('An ospfTxRetransmit  trap  signifies  than  an\n           OSPF  packet  has  been retransmitted on a non-\n           virtual interface.  All packets that may be re-\n           transmitted  are associated with an LSDB entry.\n           The LS type, LS ID, and Router ID are  used  to\n           identify the LSDB entry.')
ospfVirtIfTxRetransmit = NotificationType((1, 3, 6, 1, 2, 1, 14, 16, 2, 11)).setObjects(("OSPF-MIB", "ospfRouterId"), ("OSPF-MIB", "ospfVirtIfAreaId"), ("OSPF-MIB", "ospfVirtIfNeighbor"), ("OSPF-TRAP-MIB", "ospfPacketType"), ("OSPF-MIB", "ospfLsdbType"), ("OSPF-MIB", "ospfLsdbLsid"), ("OSPF-MIB", "ospfLsdbRouterId"))
if mibBuilder.loadTexts: ospfVirtIfTxRetransmit.setStatus('current')
if mibBuilder.loadTexts: ospfVirtIfTxRetransmit.setDescription('An ospfTxRetransmit  trap  signifies  than  an\n           OSPF packet has been retransmitted on a virtual\n           interface.  All packets that may be retransmit-\n           ted  are  associated with an LSDB entry. The LS\n           type, LS ID, and Router ID are used to identify\n           the LSDB entry.')
ospfOriginateLsa = NotificationType((1, 3, 6, 1, 2, 1, 14, 16, 2, 12)).setObjects(("OSPF-MIB", "ospfRouterId"), ("OSPF-MIB", "ospfLsdbAreaId"), ("OSPF-MIB", "ospfLsdbType"), ("OSPF-MIB", "ospfLsdbLsid"), ("OSPF-MIB", "ospfLsdbRouterId"))
if mibBuilder.loadTexts: ospfOriginateLsa.setStatus('current')
if mibBuilder.loadTexts: ospfOriginateLsa.setDescription('An ospfOriginateLsa trap signifies that a  new\n           LSA  has  been originated by this router.  This\n           trap should not be invoked for simple refreshes\n           of  LSAs  (which happesn every 30 minutes), but\n           instead will only be invoked  when  an  LSA  is\n           (re)originated due to a topology change.  Addi-\n           tionally, this trap does not include LSAs  that\n           are  being  flushed  because  they have reached\n           MaxAge.')
ospfMaxAgeLsa = NotificationType((1, 3, 6, 1, 2, 1, 14, 16, 2, 13)).setObjects(("OSPF-MIB", "ospfRouterId"), ("OSPF-MIB", "ospfLsdbAreaId"), ("OSPF-MIB", "ospfLsdbType"), ("OSPF-MIB", "ospfLsdbLsid"), ("OSPF-MIB", "ospfLsdbRouterId"))
if mibBuilder.loadTexts: ospfMaxAgeLsa.setStatus('current')
if mibBuilder.loadTexts: ospfMaxAgeLsa.setDescription("An ospfMaxAgeLsa trap signifies  that  one  of\n           the LSA in the router's link-state database has\n           aged to MaxAge.")
ospfLsdbOverflow = NotificationType((1, 3, 6, 1, 2, 1, 14, 16, 2, 14)).setObjects(("OSPF-MIB", "ospfRouterId"), ("OSPF-MIB", "ospfExtLsdbLimit"))
if mibBuilder.loadTexts: ospfLsdbOverflow.setStatus('current')
if mibBuilder.loadTexts: ospfLsdbOverflow.setDescription("An ospfLsdbOverflow trap  signifies  that  the\n           number of LSAs in the router's link-state data-\n           base has exceeded ospfExtLsdbLimit.")
ospfLsdbApproachingOverflow = NotificationType((1, 3, 6, 1, 2, 1, 14, 16, 2, 15)).setObjects(("OSPF-MIB", "ospfRouterId"), ("OSPF-MIB", "ospfExtLsdbLimit"))
if mibBuilder.loadTexts: ospfLsdbApproachingOverflow.setStatus('current')
if mibBuilder.loadTexts: ospfLsdbApproachingOverflow.setDescription("An ospfLsdbApproachingOverflow trap  signifies\n           that  the  number of LSAs in the router's link-\n           state database has exceeded ninety  percent  of\n           ospfExtLsdbLimit.")
ospfTrapConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 14, 16, 3))
ospfTrapGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 14, 16, 3, 1))
ospfTrapCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 14, 16, 3, 2))
ospfTrapCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 14, 16, 3, 2, 1)).setObjects(("OSPF-TRAP-MIB", "ospfTrapControlGroup"), ("OSPF-TRAP-MIB", "ospfTrapControlGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ospfTrapCompliance = ospfTrapCompliance.setStatus('current')
if mibBuilder.loadTexts: ospfTrapCompliance.setDescription('The compliance statement ')
ospfTrapControlGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 14, 16, 3, 1, 1)).setObjects(("OSPF-TRAP-MIB", "ospfSetTrap"), ("OSPF-TRAP-MIB", "ospfConfigErrorType"), ("OSPF-TRAP-MIB", "ospfPacketType"), ("OSPF-TRAP-MIB", "ospfPacketSrc"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ospfTrapControlGroup = ospfTrapControlGroup.setStatus('current')
if mibBuilder.loadTexts: ospfTrapControlGroup.setDescription('These objects are required  to  control  traps\n           from OSPF systems.')
mibBuilder.exportSymbols("OSPF-TRAP-MIB", ospfTrap=ospfTrap, ospfIfConfigError=ospfIfConfigError, ospfIfAuthFailure=ospfIfAuthFailure, PYSNMP_MODULE_ID=ospfTrap, ospfVirtIfTxRetransmit=ospfVirtIfTxRetransmit, ospfNbrStateChange=ospfNbrStateChange, ospfTrapGroups=ospfTrapGroups, ospfIfRxBadPacket=ospfIfRxBadPacket, ospfVirtIfRxBadPacket=ospfVirtIfRxBadPacket, ospfTrapCompliances=ospfTrapCompliances, ospfPacketSrc=ospfPacketSrc, ospfIfStateChange=ospfIfStateChange, ospfPacketType=ospfPacketType, ospfTraps=ospfTraps, ospfLsdbApproachingOverflow=ospfLsdbApproachingOverflow, ospfOriginateLsa=ospfOriginateLsa, ospfTrapControlGroup=ospfTrapControlGroup, ospfTrapCompliance=ospfTrapCompliance, ospfVirtIfAuthFailure=ospfVirtIfAuthFailure, ospfConfigErrorType=ospfConfigErrorType, ospfVirtIfStateChange=ospfVirtIfStateChange, ospfMaxAgeLsa=ospfMaxAgeLsa, ospfLsdbOverflow=ospfLsdbOverflow, ospfTrapConformance=ospfTrapConformance, ospfVirtNbrStateChange=ospfVirtNbrStateChange, ospfTrapControl=ospfTrapControl, ospfSetTrap=ospfSetTrap, ospfVirtIfConfigError=ospfVirtIfConfigError, ospfTxRetransmit=ospfTxRetransmit)
