#
# PySNMP MIB module UCD-IPFWACC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/UCD-IPFWACC-MIB
# Produced by pysmi-1.1.0 at Mon Nov 15 18:46:22 2021
# On host fv-az77-248 platform Linux version 5.11.0-1020-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Bits, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, iso, Integer32, Counter32, Counter64, TimeTicks, ObjectIdentity, NotificationType, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Bits", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "iso", "Integer32", "Counter32", "Counter64", "TimeTicks", "ObjectIdentity", "NotificationType", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ucdExperimental, = mibBuilder.importSymbols("UCD-SNMP-MIB", "ucdExperimental")
ucdIpFwAccMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2021, 13, 1))
ucdIpFwAccMIB.setRevisions(('1999-12-16 00:00',))
if mibBuilder.loadTexts: ucdIpFwAccMIB.setLastUpdated('9912160000Z')
if mibBuilder.loadTexts: ucdIpFwAccMIB.setOrganization('University of California, Davis')
ipFwAccTable = MibTable((1, 3, 6, 1, 4, 1, 2021, 13, 1, 1), )
if mibBuilder.loadTexts: ipFwAccTable.setStatus('current')
ipFwAccEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 1), ).setIndexNames((0, "UCD-IPFWACC-MIB", "ipFwAccIndex"))
if mibBuilder.loadTexts: ipFwAccEntry.setStatus('current')
ipFwAccIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipFwAccIndex.setStatus('current')
ipFwAccSrcAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipFwAccSrcAddr.setStatus('current')
ipFwAccSrcNetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipFwAccSrcNetMask.setStatus('current')
ipFwAccDstAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipFwAccDstAddr.setStatus('current')
ipFwAccDstNetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipFwAccDstNetMask.setStatus('current')
ipFwAccViaName = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipFwAccViaName.setStatus('current')
ipFwAccViaAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 1, 7), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipFwAccViaAddr.setStatus('current')
ipFwAccProto = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("all", 2), ("tcp", 3), ("udp", 4), ("icmp", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipFwAccProto.setStatus('current')
ipFwAccBidir = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("unidirectional", 1), ("bidirectional", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipFwAccBidir.setStatus('current')
ipFwAccDir = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("both", 1), ("in", 2), ("out", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipFwAccDir.setStatus('current')
ipFwAccBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipFwAccBytes.setStatus('current')
ipFwAccPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipFwAccPackets.setStatus('current')
ipFwAccNrSrcPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipFwAccNrSrcPorts.setStatus('current')
ipFwAccNrDstPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipFwAccNrDstPorts.setStatus('current')
ipFwAccSrcIsRange = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("srchasrange", 1), ("srchasnorange", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipFwAccSrcIsRange.setStatus('current')
ipFwAccDstIsRange = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("dsthasrange", 1), ("dsthasnorange", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipFwAccDstIsRange.setStatus('current')
ipFwAccPort1 = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 1, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipFwAccPort1.setStatus('current')
ipFwAccPort2 = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 1, 18), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipFwAccPort2.setStatus('current')
ipFwAccPort3 = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 1, 19), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipFwAccPort3.setStatus('current')
ipFwAccPort4 = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 1, 20), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipFwAccPort4.setStatus('current')
ipFwAccPort5 = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 1, 21), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipFwAccPort5.setStatus('current')
ipFwAccPort6 = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 1, 22), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipFwAccPort6.setStatus('current')
ipFwAccPort7 = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 1, 23), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipFwAccPort7.setStatus('current')
ipFwAccPort8 = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 1, 24), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipFwAccPort8.setStatus('current')
ipFwAccPort9 = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 1, 25), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipFwAccPort9.setStatus('current')
ipFwAccPort10 = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 1, 26), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipFwAccPort10.setStatus('current')
mibBuilder.exportSymbols("UCD-IPFWACC-MIB", ucdIpFwAccMIB=ucdIpFwAccMIB, PYSNMP_MODULE_ID=ucdIpFwAccMIB, ipFwAccDstIsRange=ipFwAccDstIsRange, ipFwAccBidir=ipFwAccBidir, ipFwAccPort4=ipFwAccPort4, ipFwAccBytes=ipFwAccBytes, ipFwAccEntry=ipFwAccEntry, ipFwAccViaAddr=ipFwAccViaAddr, ipFwAccPort8=ipFwAccPort8, ipFwAccDstAddr=ipFwAccDstAddr, ipFwAccViaName=ipFwAccViaName, ipFwAccDir=ipFwAccDir, ipFwAccSrcIsRange=ipFwAccSrcIsRange, ipFwAccNrSrcPorts=ipFwAccNrSrcPorts, ipFwAccPort2=ipFwAccPort2, ipFwAccPort6=ipFwAccPort6, ipFwAccPort9=ipFwAccPort9, ipFwAccPort10=ipFwAccPort10, ipFwAccPort5=ipFwAccPort5, ipFwAccDstNetMask=ipFwAccDstNetMask, ipFwAccPort3=ipFwAccPort3, ipFwAccTable=ipFwAccTable, ipFwAccPackets=ipFwAccPackets, ipFwAccSrcNetMask=ipFwAccSrcNetMask, ipFwAccProto=ipFwAccProto, ipFwAccSrcAddr=ipFwAccSrcAddr, ipFwAccNrDstPorts=ipFwAccNrDstPorts, ipFwAccPort7=ipFwAccPort7, ipFwAccPort1=ipFwAccPort1, ipFwAccIndex=ipFwAccIndex)
