#
# PySNMP MIB module RADIUS-DYNAUTH-SERVER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/output/asn1/RADIUS-DYNAUTH-SERVER-MIB
# Produced by pysmi-1.1.8 at Mon Feb  7 16:17:03 2022
# On host fv-az42-619 platform Linux version 5.11.0-1028-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter64, mib_2, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, ObjectIdentity, Unsigned32, TimeTicks, Integer32, MibIdentifier, iso, IpAddress, NotificationType, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter64", "mib-2", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "ObjectIdentity", "Unsigned32", "TimeTicks", "Integer32", "MibIdentifier", "iso", "IpAddress", "NotificationType", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
radiusDynAuthServerMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 146))
radiusDynAuthServerMIB.setRevisions(('2006-08-29 00:00',))
if mibBuilder.loadTexts: radiusDynAuthServerMIB.setLastUpdated('200608290000Z')
if mibBuilder.loadTexts: radiusDynAuthServerMIB.setOrganization('IETF RADEXT Working Group')
radiusDynAuthServerMIBObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 146, 1))
radiusDynAuthServerScalars = MibIdentifier((1, 3, 6, 1, 2, 1, 146, 1, 1))
radiusDynAuthServerDisconInvalidClientAddresses = MibScalar((1, 3, 6, 1, 2, 1, 146, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusDynAuthServerDisconInvalidClientAddresses.setStatus('current')
radiusDynAuthServerCoAInvalidClientAddresses = MibScalar((1, 3, 6, 1, 2, 1, 146, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusDynAuthServerCoAInvalidClientAddresses.setStatus('current')
radiusDynAuthServerIdentifier = MibScalar((1, 3, 6, 1, 2, 1, 146, 1, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusDynAuthServerIdentifier.setStatus('current')
radiusDynAuthClientTable = MibTable((1, 3, 6, 1, 2, 1, 146, 1, 2), )
if mibBuilder.loadTexts: radiusDynAuthClientTable.setStatus('current')
radiusDynAuthClientEntry = MibTableRow((1, 3, 6, 1, 2, 1, 146, 1, 2, 1), ).setIndexNames((0, "RADIUS-DYNAUTH-SERVER-MIB", "radiusDynAuthClientIndex"))
if mibBuilder.loadTexts: radiusDynAuthClientEntry.setStatus('current')
radiusDynAuthClientIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 146, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: radiusDynAuthClientIndex.setStatus('current')
radiusDynAuthClientAddressType = MibTableColumn((1, 3, 6, 1, 2, 1, 146, 1, 2, 1, 2), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusDynAuthClientAddressType.setStatus('current')
radiusDynAuthClientAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 146, 1, 2, 1, 3), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusDynAuthClientAddress.setStatus('current')
radiusDynAuthServDisconRequests = MibTableColumn((1, 3, 6, 1, 2, 1, 146, 1, 2, 1, 4), Counter32()).setUnits('requests').setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusDynAuthServDisconRequests.setStatus('current')
radiusDynAuthServDisconAuthOnlyRequests = MibTableColumn((1, 3, 6, 1, 2, 1, 146, 1, 2, 1, 5), Counter32()).setUnits('requests').setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusDynAuthServDisconAuthOnlyRequests.setStatus('current')
radiusDynAuthServDupDisconRequests = MibTableColumn((1, 3, 6, 1, 2, 1, 146, 1, 2, 1, 6), Counter32()).setUnits('requests').setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusDynAuthServDupDisconRequests.setStatus('current')
radiusDynAuthServDisconAcks = MibTableColumn((1, 3, 6, 1, 2, 1, 146, 1, 2, 1, 7), Counter32()).setUnits('replies').setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusDynAuthServDisconAcks.setStatus('current')
radiusDynAuthServDisconNaks = MibTableColumn((1, 3, 6, 1, 2, 1, 146, 1, 2, 1, 8), Counter32()).setUnits('replies').setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusDynAuthServDisconNaks.setStatus('current')
radiusDynAuthServDisconNakAuthOnlyRequests = MibTableColumn((1, 3, 6, 1, 2, 1, 146, 1, 2, 1, 9), Counter32()).setUnits('replies').setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusDynAuthServDisconNakAuthOnlyRequests.setStatus('current')
radiusDynAuthServDisconNakSessNoContext = MibTableColumn((1, 3, 6, 1, 2, 1, 146, 1, 2, 1, 10), Counter32()).setUnits('replies').setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusDynAuthServDisconNakSessNoContext.setStatus('current')
radiusDynAuthServDisconUserSessRemoved = MibTableColumn((1, 3, 6, 1, 2, 1, 146, 1, 2, 1, 11), Counter32()).setUnits('sessions').setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusDynAuthServDisconUserSessRemoved.setStatus('current')
radiusDynAuthServMalformedDisconRequests = MibTableColumn((1, 3, 6, 1, 2, 1, 146, 1, 2, 1, 12), Counter32()).setUnits('requests').setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusDynAuthServMalformedDisconRequests.setStatus('current')
radiusDynAuthServDisconBadAuthenticators = MibTableColumn((1, 3, 6, 1, 2, 1, 146, 1, 2, 1, 13), Counter32()).setUnits('requests').setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusDynAuthServDisconBadAuthenticators.setStatus('current')
radiusDynAuthServDisconPacketsDropped = MibTableColumn((1, 3, 6, 1, 2, 1, 146, 1, 2, 1, 14), Counter32()).setUnits('requests').setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusDynAuthServDisconPacketsDropped.setStatus('current')
radiusDynAuthServCoARequests = MibTableColumn((1, 3, 6, 1, 2, 1, 146, 1, 2, 1, 15), Counter32()).setUnits('requests').setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusDynAuthServCoARequests.setStatus('current')
radiusDynAuthServCoAAuthOnlyRequests = MibTableColumn((1, 3, 6, 1, 2, 1, 146, 1, 2, 1, 16), Counter32()).setUnits('requests').setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusDynAuthServCoAAuthOnlyRequests.setStatus('current')
radiusDynAuthServDupCoARequests = MibTableColumn((1, 3, 6, 1, 2, 1, 146, 1, 2, 1, 17), Counter32()).setUnits('requests').setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusDynAuthServDupCoARequests.setStatus('current')
radiusDynAuthServCoAAcks = MibTableColumn((1, 3, 6, 1, 2, 1, 146, 1, 2, 1, 18), Counter32()).setUnits('replies').setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusDynAuthServCoAAcks.setStatus('current')
radiusDynAuthServCoANaks = MibTableColumn((1, 3, 6, 1, 2, 1, 146, 1, 2, 1, 19), Counter32()).setUnits('replies').setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusDynAuthServCoANaks.setStatus('current')
radiusDynAuthServCoANakAuthOnlyRequests = MibTableColumn((1, 3, 6, 1, 2, 1, 146, 1, 2, 1, 20), Counter32()).setUnits('replies').setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusDynAuthServCoANakAuthOnlyRequests.setStatus('current')
radiusDynAuthServCoANakSessNoContext = MibTableColumn((1, 3, 6, 1, 2, 1, 146, 1, 2, 1, 21), Counter32()).setUnits('replies').setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusDynAuthServCoANakSessNoContext.setStatus('current')
radiusDynAuthServCoAUserSessChanged = MibTableColumn((1, 3, 6, 1, 2, 1, 146, 1, 2, 1, 22), Counter32()).setUnits('sessions').setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusDynAuthServCoAUserSessChanged.setStatus('current')
radiusDynAuthServMalformedCoARequests = MibTableColumn((1, 3, 6, 1, 2, 1, 146, 1, 2, 1, 23), Counter32()).setUnits('requests').setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusDynAuthServMalformedCoARequests.setStatus('current')
radiusDynAuthServCoABadAuthenticators = MibTableColumn((1, 3, 6, 1, 2, 1, 146, 1, 2, 1, 24), Counter32()).setUnits('requests').setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusDynAuthServCoABadAuthenticators.setStatus('current')
radiusDynAuthServCoAPacketsDropped = MibTableColumn((1, 3, 6, 1, 2, 1, 146, 1, 2, 1, 25), Counter32()).setUnits('requests').setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusDynAuthServCoAPacketsDropped.setStatus('current')
radiusDynAuthServUnknownTypes = MibTableColumn((1, 3, 6, 1, 2, 1, 146, 1, 2, 1, 26), Counter32()).setUnits('requests').setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusDynAuthServUnknownTypes.setStatus('current')
radiusDynAuthServerCounterDiscontinuity = MibTableColumn((1, 3, 6, 1, 2, 1, 146, 1, 2, 1, 27), TimeTicks()).setUnits('hundredths of a second').setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusDynAuthServerCounterDiscontinuity.setStatus('current')
radiusDynAuthServerMIBConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 146, 2))
radiusDynAuthServerMIBCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 146, 2, 1))
radiusDynAuthServerMIBGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 146, 2, 2))
radiusAuthServerMIBCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 146, 2, 1, 1)).setObjects(("RADIUS-DYNAUTH-SERVER-MIB", "radiusDynAuthServerMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    radiusAuthServerMIBCompliance = radiusAuthServerMIBCompliance.setStatus('current')
radiusDynAuthServerMIBGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 146, 2, 2, 1)).setObjects(("RADIUS-DYNAUTH-SERVER-MIB", "radiusDynAuthServerDisconInvalidClientAddresses"), ("RADIUS-DYNAUTH-SERVER-MIB", "radiusDynAuthServerCoAInvalidClientAddresses"), ("RADIUS-DYNAUTH-SERVER-MIB", "radiusDynAuthServerIdentifier"), ("RADIUS-DYNAUTH-SERVER-MIB", "radiusDynAuthClientAddressType"), ("RADIUS-DYNAUTH-SERVER-MIB", "radiusDynAuthClientAddress"), ("RADIUS-DYNAUTH-SERVER-MIB", "radiusDynAuthServDisconRequests"), ("RADIUS-DYNAUTH-SERVER-MIB", "radiusDynAuthServDupDisconRequests"), ("RADIUS-DYNAUTH-SERVER-MIB", "radiusDynAuthServDisconAcks"), ("RADIUS-DYNAUTH-SERVER-MIB", "radiusDynAuthServDisconNaks"), ("RADIUS-DYNAUTH-SERVER-MIB", "radiusDynAuthServDisconUserSessRemoved"), ("RADIUS-DYNAUTH-SERVER-MIB", "radiusDynAuthServMalformedDisconRequests"), ("RADIUS-DYNAUTH-SERVER-MIB", "radiusDynAuthServDisconBadAuthenticators"), ("RADIUS-DYNAUTH-SERVER-MIB", "radiusDynAuthServDisconPacketsDropped"), ("RADIUS-DYNAUTH-SERVER-MIB", "radiusDynAuthServCoARequests"), ("RADIUS-DYNAUTH-SERVER-MIB", "radiusDynAuthServDupCoARequests"), ("RADIUS-DYNAUTH-SERVER-MIB", "radiusDynAuthServCoAAcks"), ("RADIUS-DYNAUTH-SERVER-MIB", "radiusDynAuthServCoANaks"), ("RADIUS-DYNAUTH-SERVER-MIB", "radiusDynAuthServCoAUserSessChanged"), ("RADIUS-DYNAUTH-SERVER-MIB", "radiusDynAuthServMalformedCoARequests"), ("RADIUS-DYNAUTH-SERVER-MIB", "radiusDynAuthServCoABadAuthenticators"), ("RADIUS-DYNAUTH-SERVER-MIB", "radiusDynAuthServCoAPacketsDropped"), ("RADIUS-DYNAUTH-SERVER-MIB", "radiusDynAuthServUnknownTypes"), ("RADIUS-DYNAUTH-SERVER-MIB", "radiusDynAuthServerCounterDiscontinuity"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    radiusDynAuthServerMIBGroup = radiusDynAuthServerMIBGroup.setStatus('current')
radiusDynAuthServerAuthOnlyGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 146, 2, 2, 2)).setObjects(("RADIUS-DYNAUTH-SERVER-MIB", "radiusDynAuthServDisconAuthOnlyRequests"), ("RADIUS-DYNAUTH-SERVER-MIB", "radiusDynAuthServDisconNakAuthOnlyRequests"), ("RADIUS-DYNAUTH-SERVER-MIB", "radiusDynAuthServCoAAuthOnlyRequests"), ("RADIUS-DYNAUTH-SERVER-MIB", "radiusDynAuthServCoANakAuthOnlyRequests"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    radiusDynAuthServerAuthOnlyGroup = radiusDynAuthServerAuthOnlyGroup.setStatus('current')
radiusDynAuthServerNoSessGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 146, 2, 2, 3)).setObjects(("RADIUS-DYNAUTH-SERVER-MIB", "radiusDynAuthServDisconNakSessNoContext"), ("RADIUS-DYNAUTH-SERVER-MIB", "radiusDynAuthServCoANakSessNoContext"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    radiusDynAuthServerNoSessGroup = radiusDynAuthServerNoSessGroup.setStatus('current')
mibBuilder.exportSymbols("RADIUS-DYNAUTH-SERVER-MIB", radiusDynAuthClientAddress=radiusDynAuthClientAddress, radiusDynAuthServCoANaks=radiusDynAuthServCoANaks, radiusDynAuthServerScalars=radiusDynAuthServerScalars, radiusDynAuthServCoABadAuthenticators=radiusDynAuthServCoABadAuthenticators, radiusDynAuthServerMIBCompliances=radiusDynAuthServerMIBCompliances, radiusDynAuthServCoAAuthOnlyRequests=radiusDynAuthServCoAAuthOnlyRequests, radiusDynAuthServUnknownTypes=radiusDynAuthServUnknownTypes, radiusDynAuthServerMIBObjects=radiusDynAuthServerMIBObjects, radiusDynAuthServCoAUserSessChanged=radiusDynAuthServCoAUserSessChanged, radiusDynAuthServerIdentifier=radiusDynAuthServerIdentifier, radiusDynAuthServCoAAcks=radiusDynAuthServCoAAcks, radiusDynAuthClientTable=radiusDynAuthClientTable, radiusDynAuthServDisconAcks=radiusDynAuthServDisconAcks, radiusDynAuthServCoARequests=radiusDynAuthServCoARequests, radiusDynAuthServerNoSessGroup=radiusDynAuthServerNoSessGroup, radiusAuthServerMIBCompliance=radiusAuthServerMIBCompliance, radiusDynAuthServDisconNakAuthOnlyRequests=radiusDynAuthServDisconNakAuthOnlyRequests, radiusDynAuthServDisconBadAuthenticators=radiusDynAuthServDisconBadAuthenticators, radiusDynAuthServCoAPacketsDropped=radiusDynAuthServCoAPacketsDropped, radiusDynAuthClientAddressType=radiusDynAuthClientAddressType, radiusDynAuthServDisconRequests=radiusDynAuthServDisconRequests, radiusDynAuthServerMIBGroups=radiusDynAuthServerMIBGroups, radiusDynAuthClientIndex=radiusDynAuthClientIndex, radiusDynAuthServDisconAuthOnlyRequests=radiusDynAuthServDisconAuthOnlyRequests, radiusDynAuthServerMIBConformance=radiusDynAuthServerMIBConformance, radiusDynAuthServMalformedDisconRequests=radiusDynAuthServMalformedDisconRequests, PYSNMP_MODULE_ID=radiusDynAuthServerMIB, radiusDynAuthServerMIB=radiusDynAuthServerMIB, radiusDynAuthServDupCoARequests=radiusDynAuthServDupCoARequests, radiusDynAuthServCoANakSessNoContext=radiusDynAuthServCoANakSessNoContext, radiusDynAuthServDisconUserSessRemoved=radiusDynAuthServDisconUserSessRemoved, radiusDynAuthServCoANakAuthOnlyRequests=radiusDynAuthServCoANakAuthOnlyRequests, radiusDynAuthServMalformedCoARequests=radiusDynAuthServMalformedCoARequests, radiusDynAuthServerMIBGroup=radiusDynAuthServerMIBGroup, radiusDynAuthServerDisconInvalidClientAddresses=radiusDynAuthServerDisconInvalidClientAddresses, radiusDynAuthServerCoAInvalidClientAddresses=radiusDynAuthServerCoAInvalidClientAddresses, radiusDynAuthServerAuthOnlyGroup=radiusDynAuthServerAuthOnlyGroup, radiusDynAuthClientEntry=radiusDynAuthClientEntry, radiusDynAuthServDisconNaks=radiusDynAuthServDisconNaks, radiusDynAuthServDisconNakSessNoContext=radiusDynAuthServDisconNakSessNoContext, radiusDynAuthServDisconPacketsDropped=radiusDynAuthServDisconPacketsDropped, radiusDynAuthServerCounterDiscontinuity=radiusDynAuthServerCounterDiscontinuity, radiusDynAuthServDupDisconRequests=radiusDynAuthServDupDisconRequests)
