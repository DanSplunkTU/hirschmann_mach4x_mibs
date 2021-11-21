#
# PySNMP MIB module UDP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/UDP-MIB
# Produced by pysmi-1.1.3 at Sun Nov 21 00:25:42 2021
# On host fv-az39-63 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
InetPortNumber, InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetPortNumber", "InetAddress", "InetAddressType")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
mib_2, iso, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, ModuleIdentity, Bits, IpAddress, Gauge32, Unsigned32, ObjectIdentity, MibIdentifier, NotificationType, Integer32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "mib-2", "iso", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "ModuleIdentity", "Bits", "IpAddress", "Gauge32", "Unsigned32", "ObjectIdentity", "MibIdentifier", "NotificationType", "Integer32", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
udpMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 50))
udpMIB.setRevisions(('2005-05-20 00:00', '1994-11-01 00:00', '1991-03-31 00:00',))
if mibBuilder.loadTexts: udpMIB.setLastUpdated('200505200000Z')
if mibBuilder.loadTexts: udpMIB.setOrganization('IETF IPv6 Working Group http://www.ietf.org/html.charters/ipv6-charter.html')
udp = MibIdentifier((1, 3, 6, 1, 2, 1, 7))
udpInDatagrams = MibScalar((1, 3, 6, 1, 2, 1, 7, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: udpInDatagrams.setStatus('current')
udpNoPorts = MibScalar((1, 3, 6, 1, 2, 1, 7, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: udpNoPorts.setStatus('current')
udpInErrors = MibScalar((1, 3, 6, 1, 2, 1, 7, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: udpInErrors.setStatus('current')
udpOutDatagrams = MibScalar((1, 3, 6, 1, 2, 1, 7, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: udpOutDatagrams.setStatus('current')
udpHCInDatagrams = MibScalar((1, 3, 6, 1, 2, 1, 7, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: udpHCInDatagrams.setStatus('current')
udpHCOutDatagrams = MibScalar((1, 3, 6, 1, 2, 1, 7, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: udpHCOutDatagrams.setStatus('current')
udpEndpointTable = MibTable((1, 3, 6, 1, 2, 1, 7, 7), )
if mibBuilder.loadTexts: udpEndpointTable.setStatus('current')
udpEndpointEntry = MibTableRow((1, 3, 6, 1, 2, 1, 7, 7, 1), ).setIndexNames((0, "UDP-MIB", "udpEndpointLocalAddressType"), (0, "UDP-MIB", "udpEndpointLocalAddress"), (0, "UDP-MIB", "udpEndpointLocalPort"), (0, "UDP-MIB", "udpEndpointRemoteAddressType"), (0, "UDP-MIB", "udpEndpointRemoteAddress"), (0, "UDP-MIB", "udpEndpointRemotePort"), (0, "UDP-MIB", "udpEndpointInstance"))
if mibBuilder.loadTexts: udpEndpointEntry.setStatus('current')
udpEndpointLocalAddressType = MibTableColumn((1, 3, 6, 1, 2, 1, 7, 7, 1, 1), InetAddressType())
if mibBuilder.loadTexts: udpEndpointLocalAddressType.setStatus('current')
udpEndpointLocalAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 7, 7, 1, 2), InetAddress())
if mibBuilder.loadTexts: udpEndpointLocalAddress.setStatus('current')
udpEndpointLocalPort = MibTableColumn((1, 3, 6, 1, 2, 1, 7, 7, 1, 3), InetPortNumber())
if mibBuilder.loadTexts: udpEndpointLocalPort.setStatus('current')
udpEndpointRemoteAddressType = MibTableColumn((1, 3, 6, 1, 2, 1, 7, 7, 1, 4), InetAddressType())
if mibBuilder.loadTexts: udpEndpointRemoteAddressType.setStatus('current')
udpEndpointRemoteAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 7, 7, 1, 5), InetAddress())
if mibBuilder.loadTexts: udpEndpointRemoteAddress.setStatus('current')
udpEndpointRemotePort = MibTableColumn((1, 3, 6, 1, 2, 1, 7, 7, 1, 6), InetPortNumber())
if mibBuilder.loadTexts: udpEndpointRemotePort.setStatus('current')
udpEndpointInstance = MibTableColumn((1, 3, 6, 1, 2, 1, 7, 7, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: udpEndpointInstance.setStatus('current')
udpEndpointProcess = MibTableColumn((1, 3, 6, 1, 2, 1, 7, 7, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: udpEndpointProcess.setStatus('current')
udpTable = MibTable((1, 3, 6, 1, 2, 1, 7, 5), )
if mibBuilder.loadTexts: udpTable.setStatus('deprecated')
udpEntry = MibTableRow((1, 3, 6, 1, 2, 1, 7, 5, 1), ).setIndexNames((0, "UDP-MIB", "udpLocalAddress"), (0, "UDP-MIB", "udpLocalPort"))
if mibBuilder.loadTexts: udpEntry.setStatus('deprecated')
udpLocalAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 7, 5, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: udpLocalAddress.setStatus('deprecated')
udpLocalPort = MibTableColumn((1, 3, 6, 1, 2, 1, 7, 5, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: udpLocalPort.setStatus('deprecated')
udpMIBConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 50, 2))
udpMIBCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 50, 2, 1))
udpMIBGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 50, 2, 2))
udpMIBCompliance2 = ModuleCompliance((1, 3, 6, 1, 2, 1, 50, 2, 1, 2)).setObjects(("UDP-MIB", "udpBaseGroup"), ("UDP-MIB", "udpEndpointGroup"), ("UDP-MIB", "udpHCGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    udpMIBCompliance2 = udpMIBCompliance2.setStatus('current')
udpMIBCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 50, 2, 1, 1)).setObjects(("UDP-MIB", "udpGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    udpMIBCompliance = udpMIBCompliance.setStatus('deprecated')
udpGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 50, 2, 2, 1)).setObjects(("UDP-MIB", "udpInDatagrams"), ("UDP-MIB", "udpNoPorts"), ("UDP-MIB", "udpInErrors"), ("UDP-MIB", "udpOutDatagrams"), ("UDP-MIB", "udpLocalAddress"), ("UDP-MIB", "udpLocalPort"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    udpGroup = udpGroup.setStatus('deprecated')
udpBaseGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 50, 2, 2, 2)).setObjects(("UDP-MIB", "udpInDatagrams"), ("UDP-MIB", "udpNoPorts"), ("UDP-MIB", "udpInErrors"), ("UDP-MIB", "udpOutDatagrams"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    udpBaseGroup = udpBaseGroup.setStatus('current')
udpHCGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 50, 2, 2, 3)).setObjects(("UDP-MIB", "udpHCInDatagrams"), ("UDP-MIB", "udpHCOutDatagrams"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    udpHCGroup = udpHCGroup.setStatus('current')
udpEndpointGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 50, 2, 2, 4)).setObjects(("UDP-MIB", "udpEndpointProcess"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    udpEndpointGroup = udpEndpointGroup.setStatus('current')
mibBuilder.exportSymbols("UDP-MIB", udpHCInDatagrams=udpHCInDatagrams, udpMIBCompliance2=udpMIBCompliance2, udpEndpointProcess=udpEndpointProcess, udpEndpointGroup=udpEndpointGroup, udpBaseGroup=udpBaseGroup, udpMIBGroups=udpMIBGroups, udpEndpointTable=udpEndpointTable, udpMIBCompliance=udpMIBCompliance, PYSNMP_MODULE_ID=udpMIB, udpEndpointLocalAddressType=udpEndpointLocalAddressType, udpMIB=udpMIB, udpLocalAddress=udpLocalAddress, udpGroup=udpGroup, udpEndpointLocalAddress=udpEndpointLocalAddress, udpEndpointRemoteAddress=udpEndpointRemoteAddress, udpOutDatagrams=udpOutDatagrams, udpInErrors=udpInErrors, udpHCGroup=udpHCGroup, udpInDatagrams=udpInDatagrams, udpEndpointInstance=udpEndpointInstance, udpTable=udpTable, udpEndpointEntry=udpEndpointEntry, udpEndpointLocalPort=udpEndpointLocalPort, udpEndpointRemotePort=udpEndpointRemotePort, udpEntry=udpEntry, udpLocalPort=udpLocalPort, udpMIBConformance=udpMIBConformance, udpMIBCompliances=udpMIBCompliances, udpHCOutDatagrams=udpHCOutDatagrams, udpEndpointRemoteAddressType=udpEndpointRemoteAddressType, udpNoPorts=udpNoPorts, udp=udp)
