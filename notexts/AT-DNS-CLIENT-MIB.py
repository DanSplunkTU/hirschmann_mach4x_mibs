#
# PySNMP MIB module AT-DNS-CLIENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/awplus/AT-DNS-CLIENT
# Produced by pysmi-1.1.8 at Fri Jan  7 16:10:57 2022
# On host fv-az36-988 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
modules, = mibBuilder.importSymbols("AT-SMI-MIB", "modules")
InetAddressType, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, iso, Integer32, ModuleIdentity, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Unsigned32, Counter64, NotificationType, IpAddress, TimeTicks, Counter32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "iso", "Integer32", "ModuleIdentity", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Unsigned32", "Counter64", "NotificationType", "IpAddress", "TimeTicks", "Counter32", "MibIdentifier")
TextualConvention, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "RowStatus")
atDNSClient = ModuleIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 501, 1))
atDNSClient.setRevisions(('2010-06-14 04:45', '2008-09-18 12:00',))
if mibBuilder.loadTexts: atDNSClient.setLastUpdated('201006140445Z')
if mibBuilder.loadTexts: atDNSClient.setOrganization('Allied Telesis, Inc')
atDns = ObjectIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 501))
if mibBuilder.loadTexts: atDns.setStatus('current')
atDNSServerIndexNext = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 501, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atDNSServerIndexNext.setStatus('current')
atDNSServerTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 501, 1, 2), )
if mibBuilder.loadTexts: atDNSServerTable.setStatus('current')
atDNSServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 501, 1, 2, 1), ).setIndexNames((0, "AT-DNS-CLIENT-MIB", "atDNSServerIndex"))
if mibBuilder.loadTexts: atDNSServerEntry.setStatus('current')
atDNSServerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 501, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: atDNSServerIndex.setStatus('current')
atDNSServerAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 501, 1, 2, 1, 2), InetAddressType().clone('ipv4')).setMaxAccess("readonly")
if mibBuilder.loadTexts: atDNSServerAddrType.setStatus('current')
atDNSServerAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 501, 1, 2, 1, 3), IpAddress().clone(hexValue="00000000")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atDNSServerAddr.setStatus('current')
atDNSServerStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 501, 1, 2, 1, 4), RowStatus().clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atDNSServerStatus.setStatus('current')
mibBuilder.exportSymbols("AT-DNS-CLIENT-MIB", atDNSServerAddr=atDNSServerAddr, atDNSServerIndexNext=atDNSServerIndexNext, atDNSServerEntry=atDNSServerEntry, atDNSServerAddrType=atDNSServerAddrType, atDns=atDns, atDNSServerTable=atDNSServerTable, atDNSServerIndex=atDNSServerIndex, atDNSClient=atDNSClient, atDNSServerStatus=atDNSServerStatus, PYSNMP_MODULE_ID=atDNSClient)
