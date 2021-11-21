#
# PySNMP MIB module PRVT-ROUTE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/telco-systems/binox/PRVT-ROUTE-MIB
# Produced by pysmi-1.1.3 at Sun Nov 21 00:45:53 2021
# On host fv-az39-63 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
Ipv6Address, = mibBuilder.importSymbols("IPV6-TC", "Ipv6Address")
routingProtocols, = mibBuilder.importSymbols("PRVT-SWITCH-MIB", "routingProtocols")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, Counter64, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Gauge32, IpAddress, TimeTicks, NotificationType, Counter32, MibIdentifier, Bits, ModuleIdentity, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Counter64", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Gauge32", "IpAddress", "TimeTicks", "NotificationType", "Counter32", "MibIdentifier", "Bits", "ModuleIdentity", "Integer32")
TextualConvention, DisplayString, TruthValue, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TruthValue", "RowStatus")
prvtRouteMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 3))
prvtRouteMIB.setRevisions(('2009-01-27 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: prvtRouteMIB.setRevisionsDescriptions(('Initial version',))
if mibBuilder.loadTexts: prvtRouteMIB.setLastUpdated('200901270000Z')
if mibBuilder.loadTexts: prvtRouteMIB.setOrganization('BATM Advanced Communication')
if mibBuilder.loadTexts: prvtRouteMIB.setContactInfo('BATM/Telco Systems Support team\n         Email:\n         For North America: techsupport@telco.com\n         For North Europe: support@batm.de, info@batm.de\n         For the rest of the world: techsupport@telco.com')
if mibBuilder.loadTexts: prvtRouteMIB.setDescription('Mib containing information about\n         dynamic and configurable routes in the system.')
class NetPrefix(TextualConvention, OctetString):
    description = 'Prefix'
    status = 'current'
    displayHint = '1d.1d.1d.1d/1d'

prvtRouteMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 3, 1))
prvtDynamicRouteTable = MibTable((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 3, 1, 1), )
if mibBuilder.loadTexts: prvtDynamicRouteTable.setStatus('current')
if mibBuilder.loadTexts: prvtDynamicRouteTable.setDescription('System dynamic routes.')
prvtDynamicRouteEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 3, 1, 1, 1), ).setIndexNames((0, "PRVT-ROUTE-MIB", "prvtDynamicRoutePrefix"), (0, "PRVT-ROUTE-MIB", "prvtDynamicRouteNextHop"), (0, "PRVT-ROUTE-MIB", "prvtDynamicRouteType"), (0, "PRVT-ROUTE-MIB", "prvtDynamicRouteDistance"))
if mibBuilder.loadTexts: prvtDynamicRouteEntry.setStatus('current')
if mibBuilder.loadTexts: prvtDynamicRouteEntry.setDescription('The conceptual row represents a routing entry.')
prvtDynamicRoutePrefix = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 3, 1, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(5, 5)).setFixedLength(5))
if mibBuilder.loadTexts: prvtDynamicRoutePrefix.setStatus('current')
if mibBuilder.loadTexts: prvtDynamicRoutePrefix.setDescription('Dynamic route prefix.')
prvtDynamicRouteNextHop = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 3, 1, 1, 1, 2), IpAddress())
if mibBuilder.loadTexts: prvtDynamicRouteNextHop.setStatus('current')
if mibBuilder.loadTexts: prvtDynamicRouteNextHop.setDescription('Dynamic route next hop.')
prvtDynamicRouteType = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 3, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19))).clone(namedValues=NamedValues(("system", 1), ("kernel", 2), ("connect", 3), ("static", 4), ("rip", 5), ("ripng", 6), ("ospf", 7), ("ospf6", 8), ("bgp", 9), ("fib", 10), ("vrrp", 11), ("irdp", 12), ("dhcp", 13), ("pimd", 14), ("isis1", 15), ("isis2", 16), ("bfd", 17), ("test", 18), ("max", 19))))
if mibBuilder.loadTexts: prvtDynamicRouteType.setStatus('current')
if mibBuilder.loadTexts: prvtDynamicRouteType.setDescription('Dynamic route type.')
prvtDynamicRouteDistance = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 3, 1, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)))
if mibBuilder.loadTexts: prvtDynamicRouteDistance.setStatus('current')
if mibBuilder.loadTexts: prvtDynamicRouteDistance.setDescription('Dynamic route distance.')
prvtDynamicRouteFlags = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 3, 1, 1, 1, 5), Bits().clone(namedValues=NamedValues(("internal", 0), ("selfroute", 1), ("blackhole", 2), ("ibgp", 3), ("selected", 4), ("changed", 5), ("static", 6), ("deleted", 7), ("staticarp", 8), ("mplsIngress", 9), ("mplsEgress", 10), ("outband", 11), ("selfIp", 12), ("vrrpIp", 13)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtDynamicRouteFlags.setStatus('current')
if mibBuilder.loadTexts: prvtDynamicRouteFlags.setDescription('Dynamic route flags.')
prvtDynamicRouteNextHopType = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 3, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("ifindex", 1), ("ifname", 2), ("ipv4", 3), ("ipv4Ifindex", 4), ("ipv4Ifname", 5), ("ipv6", 6), ("ipv6Ifindex", 7), ("ipv6Ifname", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtDynamicRouteNextHopType.setStatus('current')
if mibBuilder.loadTexts: prvtDynamicRouteNextHopType.setDescription('Dynamic route hop type.')
prvtDynamicRouteNextHopFlags = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 3, 1, 1, 1, 7), Bits().clone(namedValues=NamedValues(("active", 0), ("fib", 1), ("recursive", 2), ("notready", 3), ("outband", 4), ("fibsetOutband", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtDynamicRouteNextHopFlags.setStatus('current')
if mibBuilder.loadTexts: prvtDynamicRouteNextHopFlags.setDescription('Dynamic route hop flags.')
prvtDynamicRouteMetrics = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 3, 1, 1, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtDynamicRouteMetrics.setStatus('current')
if mibBuilder.loadTexts: prvtDynamicRouteMetrics.setDescription('Dynamic route metrics.')
prvtDynamicRouteUptime = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 3, 1, 1, 1, 9), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtDynamicRouteUptime.setStatus('current')
if mibBuilder.loadTexts: prvtDynamicRouteUptime.setDescription("A length of time.\n         \n         Duration values are in the ISO 8601 duration format, where\n         P represents 'Period',\n         nY represents the number of years,\n         nM the number of months,\n         nD the number of days,\n         T is the date/time separator,\n         nH the number of hours,\n         nM the number of minutes,\n         nS the number of seconds.\n         So P2DT23H32M51S means 'A period of 2 days, 23 hours, 32 minutes, and 51 seconds'.\n         \n         PnYnMnDTnH nMnS (e.g., P2DT23H32M51S)\n         \n         We use the duration data type to convey values like\n         the time left until a listing ends.\n         For ended listings, the time left is PT0S (zero seconds).\n         \n         xs:duration is part of the XML schema namespace defined as:\n         \n         xmlns:xs='http://www.w3.org/2001/XMLSchema' ")
prvtDynamicRouteIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 3, 1, 1, 1, 10), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtDynamicRouteIfName.setStatus('current')
if mibBuilder.loadTexts: prvtDynamicRouteIfName.setDescription('Dynamic route name.')
prvtCfgRouteTable = MibTable((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 3, 1, 2), )
if mibBuilder.loadTexts: prvtCfgRouteTable.setStatus('current')
if mibBuilder.loadTexts: prvtCfgRouteTable.setDescription('Table with configurable routes. To create entry in\n         this table use prvtCfgRouteRowStatus with\n         createAndGo(4) or createAndWait(5).\n         For example static route :\n         static-route 88.65.85.4/32 43.13.15.18 3\n         will be represented as :\n         prvtCfgRouteRowStatus.88.65.85.4.32.43.13.15.18.3')
prvtCfgRouteEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 3, 1, 2, 1), ).setIndexNames((0, "PRVT-ROUTE-MIB", "prvtCfgRoutePrefix"), (0, "PRVT-ROUTE-MIB", "prvtCfgRouteNextHop"), (0, "PRVT-ROUTE-MIB", "prvtCfgRouteDistance"))
if mibBuilder.loadTexts: prvtCfgRouteEntry.setStatus('current')
if mibBuilder.loadTexts: prvtCfgRouteEntry.setDescription('The conceptual row represents a routing entry.')
prvtCfgRoutePrefix = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 3, 1, 2, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(5, 5)).setFixedLength(5))
if mibBuilder.loadTexts: prvtCfgRoutePrefix.setStatus('current')
if mibBuilder.loadTexts: prvtCfgRoutePrefix.setDescription('Route prefix.')
prvtCfgRouteNextHop = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 3, 1, 2, 1, 2), IpAddress())
if mibBuilder.loadTexts: prvtCfgRouteNextHop.setStatus('current')
if mibBuilder.loadTexts: prvtCfgRouteNextHop.setDescription('Route next hop.')
prvtCfgRouteDistance = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 3, 1, 2, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)))
if mibBuilder.loadTexts: prvtCfgRouteDistance.setStatus('current')
if mibBuilder.loadTexts: prvtCfgRouteDistance.setDescription('Route distance.')
prvtCfgRouteRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 3, 1, 2, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtCfgRouteRowStatus.setStatus('current')
if mibBuilder.loadTexts: prvtCfgRouteRowStatus.setDescription('Create static route.')
prvtCfgIPv6RouteTable = MibTable((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 3, 1, 3), )
if mibBuilder.loadTexts: prvtCfgIPv6RouteTable.setStatus('current')
if mibBuilder.loadTexts: prvtCfgIPv6RouteTable.setDescription('Table with configurable routes. To create entry in\n         this table use prvtCfgIPv6RouteRowStatus with\n         createAndGo(4) or createAndWait(5).\n         For example static route :\n         router static-ipv6-route ::/0 2001:fd8::7 10\n         will be represented as :\n         prvtCfgIPv6RouteRowStatus.4.58.58.47.48.32.1.15.216.0.0.0.0.0.0.0.0.0.0.0.7.10 \n         or\n         1.3.6.1.4.1.738.10.6.4.3.1.3.1.4 --> prvtCfgIPv6RouteRowStatus OID\n         v --> Value --> createAndGo(4) \n         prvtCfgIPv6RouteRowStatus    <--|v  :  :  /  0 2001:0f  d8: 00: 00: 00: 00: 00: 07|10 \n         1.3.6.1.4.1.738.10.6.4.3.1.3.1.4.4.58.58.47.48.32.1.15.216.0.0.0.0.0.0.0.0.0.0.0.7.10')
prvtCfgIPv6RouteEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 3, 1, 3, 1), ).setIndexNames((0, "PRVT-ROUTE-MIB", "prvtCfgIPv6RoutePrefix"), (0, "PRVT-ROUTE-MIB", "prvtCfgIPv6RouteNextHop"), (0, "PRVT-ROUTE-MIB", "prvtCfgIPv6RouteDistance"))
if mibBuilder.loadTexts: prvtCfgIPv6RouteEntry.setStatus('current')
if mibBuilder.loadTexts: prvtCfgIPv6RouteEntry.setDescription('The conceptual row represents a IPv6 routing entry.')
prvtCfgIPv6RoutePrefix = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 3, 1, 3, 1, 1), OctetString())
if mibBuilder.loadTexts: prvtCfgIPv6RoutePrefix.setStatus('current')
if mibBuilder.loadTexts: prvtCfgIPv6RoutePrefix.setDescription('IPv6 route prefix.')
prvtCfgIPv6RouteNextHop = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 3, 1, 3, 1, 2), Ipv6Address())
if mibBuilder.loadTexts: prvtCfgIPv6RouteNextHop.setStatus('current')
if mibBuilder.loadTexts: prvtCfgIPv6RouteNextHop.setDescription('IPv6 route next hop.')
prvtCfgIPv6RouteDistance = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 3, 1, 3, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)))
if mibBuilder.loadTexts: prvtCfgIPv6RouteDistance.setStatus('current')
if mibBuilder.loadTexts: prvtCfgIPv6RouteDistance.setDescription('IPv6 route distance.')
prvtCfgIPv6RouteRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 3, 1, 3, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtCfgIPv6RouteRowStatus.setStatus('current')
if mibBuilder.loadTexts: prvtCfgIPv6RouteRowStatus.setDescription('Create static IPv6 route.')
prvtGlobalIPv6Forwarding = MibScalar((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("host", 1), ("router", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtGlobalIPv6Forwarding.setStatus('current')
if mibBuilder.loadTexts: prvtGlobalIPv6Forwarding.setDescription('Configure IPv6 behavior.')
prvtGlobalIPv6Disable = MibScalar((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 3, 1, 5), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtGlobalIPv6Disable.setStatus('current')
if mibBuilder.loadTexts: prvtGlobalIPv6Disable.setDescription('Configure IPv6 behavior.')
mibBuilder.exportSymbols("PRVT-ROUTE-MIB", prvtDynamicRouteNextHop=prvtDynamicRouteNextHop, prvtCfgIPv6RouteRowStatus=prvtCfgIPv6RouteRowStatus, prvtGlobalIPv6Disable=prvtGlobalIPv6Disable, prvtDynamicRouteFlags=prvtDynamicRouteFlags, prvtDynamicRouteDistance=prvtDynamicRouteDistance, prvtCfgRouteRowStatus=prvtCfgRouteRowStatus, prvtCfgIPv6RouteEntry=prvtCfgIPv6RouteEntry, prvtCfgRoutePrefix=prvtCfgRoutePrefix, prvtCfgRouteEntry=prvtCfgRouteEntry, prvtDynamicRouteType=prvtDynamicRouteType, prvtCfgIPv6RouteDistance=prvtCfgIPv6RouteDistance, NetPrefix=NetPrefix, prvtCfgIPv6RouteTable=prvtCfgIPv6RouteTable, prvtDynamicRouteUptime=prvtDynamicRouteUptime, prvtDynamicRouteIfName=prvtDynamicRouteIfName, prvtGlobalIPv6Forwarding=prvtGlobalIPv6Forwarding, prvtRouteMIB=prvtRouteMIB, prvtCfgRouteTable=prvtCfgRouteTable, prvtCfgRouteNextHop=prvtCfgRouteNextHop, prvtCfgRouteDistance=prvtCfgRouteDistance, prvtDynamicRouteMetrics=prvtDynamicRouteMetrics, prvtRouteMIBObjects=prvtRouteMIBObjects, prvtDynamicRouteTable=prvtDynamicRouteTable, prvtCfgIPv6RouteNextHop=prvtCfgIPv6RouteNextHop, PYSNMP_MODULE_ID=prvtRouteMIB, prvtCfgIPv6RoutePrefix=prvtCfgIPv6RoutePrefix, prvtDynamicRouteNextHopType=prvtDynamicRouteNextHopType, prvtDynamicRouteEntry=prvtDynamicRouteEntry, prvtDynamicRouteNextHopFlags=prvtDynamicRouteNextHopFlags, prvtDynamicRoutePrefix=prvtDynamicRoutePrefix)
