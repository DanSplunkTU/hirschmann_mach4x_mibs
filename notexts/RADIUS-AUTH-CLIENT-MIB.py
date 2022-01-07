#
# PySNMP MIB module RADIUS-AUTH-CLIENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/RADIUS-AUTH-CLIENT-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:07:39 2022
# On host fv-az36-988 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
MibIdentifier, ObjectIdentity, ModuleIdentity, iso, Unsigned32, TimeTicks, Gauge32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, mib_2, Bits, NotificationType, IpAddress, Counter64, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "ObjectIdentity", "ModuleIdentity", "iso", "Unsigned32", "TimeTicks", "Gauge32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "mib-2", "Bits", "NotificationType", "IpAddress", "Counter64", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
radiusAuthClientMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 67, 1, 2))
radiusAuthClientMIB.setRevisions(('1999-06-11 00:00',))
if mibBuilder.loadTexts: radiusAuthClientMIB.setLastUpdated('9906110000Z')
if mibBuilder.loadTexts: radiusAuthClientMIB.setOrganization('IETF RADIUS Working Group.')
radiusMIB = ObjectIdentity((1, 3, 6, 1, 2, 1, 67))
if mibBuilder.loadTexts: radiusMIB.setStatus('current')
radiusAuthentication = MibIdentifier((1, 3, 6, 1, 2, 1, 67, 1))
radiusAuthClientMIBObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 67, 1, 2, 1))
radiusAuthClient = MibIdentifier((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1))
radiusAuthClientInvalidServerAddresses = MibScalar((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthClientInvalidServerAddresses.setStatus('current')
radiusAuthClientIdentifier = MibScalar((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthClientIdentifier.setStatus('current')
radiusAuthServerTable = MibTable((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3), )
if mibBuilder.loadTexts: radiusAuthServerTable.setStatus('current')
radiusAuthServerEntry = MibTableRow((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3, 1), ).setIndexNames((0, "RADIUS-AUTH-CLIENT-MIB", "radiusAuthServerIndex"))
if mibBuilder.loadTexts: radiusAuthServerEntry.setStatus('current')
radiusAuthServerIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: radiusAuthServerIndex.setStatus('current')
radiusAuthServerAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthServerAddress.setStatus('current')
radiusAuthClientServerPortNumber = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthClientServerPortNumber.setStatus('current')
radiusAuthClientRoundTripTime = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3, 1, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthClientRoundTripTime.setStatus('current')
radiusAuthClientAccessRequests = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthClientAccessRequests.setStatus('current')
radiusAuthClientAccessRetransmissions = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthClientAccessRetransmissions.setStatus('current')
radiusAuthClientAccessAccepts = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthClientAccessAccepts.setStatus('current')
radiusAuthClientAccessRejects = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthClientAccessRejects.setStatus('current')
radiusAuthClientAccessChallenges = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthClientAccessChallenges.setStatus('current')
radiusAuthClientMalformedAccessResponses = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthClientMalformedAccessResponses.setStatus('current')
radiusAuthClientBadAuthenticators = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthClientBadAuthenticators.setStatus('current')
radiusAuthClientPendingRequests = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3, 1, 12), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthClientPendingRequests.setStatus('current')
radiusAuthClientTimeouts = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthClientTimeouts.setStatus('current')
radiusAuthClientUnknownTypes = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthClientUnknownTypes.setStatus('current')
radiusAuthClientPacketsDropped = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthClientPacketsDropped.setStatus('current')
radiusAuthClientMIBConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 67, 1, 2, 2))
radiusAuthClientMIBCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 67, 1, 2, 2, 1))
radiusAuthClientMIBGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 67, 1, 2, 2, 2))
radiusAuthClientMIBCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 67, 1, 2, 2, 1, 1)).setObjects(("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    radiusAuthClientMIBCompliance = radiusAuthClientMIBCompliance.setStatus('current')
radiusAuthClientMIBGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 67, 1, 2, 2, 2, 1)).setObjects(("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientIdentifier"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientInvalidServerAddresses"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthServerAddress"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientServerPortNumber"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientRoundTripTime"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientAccessRequests"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientAccessRetransmissions"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientAccessAccepts"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientAccessRejects"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientAccessChallenges"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientMalformedAccessResponses"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientBadAuthenticators"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientPendingRequests"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientTimeouts"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientUnknownTypes"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientPacketsDropped"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    radiusAuthClientMIBGroup = radiusAuthClientMIBGroup.setStatus('current')
mibBuilder.exportSymbols("RADIUS-AUTH-CLIENT-MIB", radiusAuthClientMIBCompliances=radiusAuthClientMIBCompliances, radiusAuthClientMIBConformance=radiusAuthClientMIBConformance, radiusAuthClientMIBObjects=radiusAuthClientMIBObjects, radiusAuthClientAccessRequests=radiusAuthClientAccessRequests, radiusAuthClientMalformedAccessResponses=radiusAuthClientMalformedAccessResponses, radiusAuthServerTable=radiusAuthServerTable, PYSNMP_MODULE_ID=radiusAuthClientMIB, radiusAuthClient=radiusAuthClient, radiusAuthServerAddress=radiusAuthServerAddress, radiusAuthClientUnknownTypes=radiusAuthClientUnknownTypes, radiusAuthClientBadAuthenticators=radiusAuthClientBadAuthenticators, radiusAuthClientMIB=radiusAuthClientMIB, radiusAuthClientTimeouts=radiusAuthClientTimeouts, radiusAuthServerIndex=radiusAuthServerIndex, radiusAuthClientAccessChallenges=radiusAuthClientAccessChallenges, radiusAuthClientMIBCompliance=radiusAuthClientMIBCompliance, radiusAuthClientPendingRequests=radiusAuthClientPendingRequests, radiusAuthClientRoundTripTime=radiusAuthClientRoundTripTime, radiusAuthClientAccessRejects=radiusAuthClientAccessRejects, radiusAuthClientIdentifier=radiusAuthClientIdentifier, radiusAuthClientMIBGroup=radiusAuthClientMIBGroup, radiusAuthClientAccessAccepts=radiusAuthClientAccessAccepts, radiusAuthServerEntry=radiusAuthServerEntry, radiusAuthClientMIBGroups=radiusAuthClientMIBGroups, radiusAuthClientServerPortNumber=radiusAuthClientServerPortNumber, radiusAuthClientInvalidServerAddresses=radiusAuthClientInvalidServerAddresses, radiusMIB=radiusMIB, radiusAuthClientPacketsDropped=radiusAuthClientPacketsDropped, radiusAuthClientAccessRetransmissions=radiusAuthClientAccessRetransmissions, radiusAuthentication=radiusAuthentication)
