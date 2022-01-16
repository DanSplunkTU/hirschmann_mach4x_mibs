#
# PySNMP MIB module OPENBSD-CARP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/openbsd/OPENBSD-CARP-MIB
# Produced by pysmi-1.1.8 at Sun Jan 16 00:42:12 2022
# On host fv-az42-839 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
openBSD, = mibBuilder.importSymbols("OPENBSD-BASE-MIB", "openBSD")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
IpAddress, Counter64, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ModuleIdentity, iso, TimeTicks, Bits, ObjectIdentity, enterprises, MibIdentifier, Gauge32, Counter32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Counter64", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ModuleIdentity", "iso", "TimeTicks", "Bits", "ObjectIdentity", "enterprises", "MibIdentifier", "Gauge32", "Counter32", "Unsigned32")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
carpMIBObjects = ModuleIdentity((1, 3, 6, 1, 4, 1, 30155, 6))
carpMIBObjects.setRevisions(('2012-01-31 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: carpMIBObjects.setRevisionsDescriptions(('Add the OPENBSD-CARP-MIB to snmpd.',))
if mibBuilder.loadTexts: carpMIBObjects.setLastUpdated('201201310000Z')
if mibBuilder.loadTexts: carpMIBObjects.setOrganization('OpenBSD')
if mibBuilder.loadTexts: carpMIBObjects.setContactInfo('\n                  Author:     Joel Knight\n                  email:      knight.joel@gmail.com\n                  www:        www.packetmischief.ca/openbsd-snmp-mibs/\n                 ')
if mibBuilder.loadTexts: carpMIBObjects.setDescription('The MIB module for gathering information about\n\t\t Common Address Redundancy Protocol (CARP) interfaces.')
carpSysctl = MibIdentifier((1, 3, 6, 1, 4, 1, 30155, 6, 1))
carpIf = MibIdentifier((1, 3, 6, 1, 4, 1, 30155, 6, 2))
carpStats = MibIdentifier((1, 3, 6, 1, 4, 1, 30155, 6, 3))
carpAllow = MibScalar((1, 3, 6, 1, 4, 1, 30155, 6, 1, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: carpAllow.setStatus('current')
if mibBuilder.loadTexts: carpAllow.setDescription('Indicates whether the node will respond to CARP packets.')
carpPreempt = MibScalar((1, 3, 6, 1, 4, 1, 30155, 6, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: carpPreempt.setStatus('current')
if mibBuilder.loadTexts: carpPreempt.setDescription('Indicates whether preemption is enabled.')
carpLog = MibScalar((1, 3, 6, 1, 4, 1, 30155, 6, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: carpLog.setStatus('current')
if mibBuilder.loadTexts: carpLog.setDescription('Indicates whether logging of invalid CARP packets is enabled.')
carpIfNumber = MibScalar((1, 3, 6, 1, 4, 1, 30155, 6, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: carpIfNumber.setStatus('current')
if mibBuilder.loadTexts: carpIfNumber.setDescription('The number of CARP interfaces present on this system.')
carpIfTable = MibTable((1, 3, 6, 1, 4, 1, 30155, 6, 2, 2), )
if mibBuilder.loadTexts: carpIfTable.setStatus('current')
if mibBuilder.loadTexts: carpIfTable.setDescription('A list of individual CARP interfaces. The number of entries is\n\tgiven by the value of carpIfNumber.')
carpIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30155, 6, 2, 2, 1), ).setIndexNames((0, "OPENBSD-CARP-MIB", "carpIfIndex"))
if mibBuilder.loadTexts: carpIfEntry.setStatus('current')
if mibBuilder.loadTexts: carpIfEntry.setDescription('An entry containing management information applicable to a\n\tparticular CARP interface.')
carpIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 30155, 6, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: carpIfIndex.setStatus('current')
if mibBuilder.loadTexts: carpIfIndex.setDescription('A unique value, greater than zero, for each CARP interface.')
carpIfDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 30155, 6, 2, 2, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: carpIfDescr.setStatus('current')
if mibBuilder.loadTexts: carpIfDescr.setDescription('The name of the CARP interface.')
carpIfVhid = MibTableColumn((1, 3, 6, 1, 4, 1, 30155, 6, 2, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: carpIfVhid.setStatus('current')
if mibBuilder.loadTexts: carpIfVhid.setDescription('The Virtual HostID of the CARP interface.')
carpIfDev = MibTableColumn((1, 3, 6, 1, 4, 1, 30155, 6, 2, 2, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: carpIfDev.setStatus('current')
if mibBuilder.loadTexts: carpIfDev.setDescription('The parent interface that the CARP interface is bound to.')
carpIfAdvbase = MibTableColumn((1, 3, 6, 1, 4, 1, 30155, 6, 2, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: carpIfAdvbase.setStatus('current')
if mibBuilder.loadTexts: carpIfAdvbase.setDescription('The advbase value of the CARP interface.')
carpIfAdvskew = MibTableColumn((1, 3, 6, 1, 4, 1, 30155, 6, 2, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: carpIfAdvskew.setStatus('current')
if mibBuilder.loadTexts: carpIfAdvskew.setDescription('The advskew value of the CARP interface.')
carpIfState = MibTableColumn((1, 3, 6, 1, 4, 1, 30155, 6, 2, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("init", 0), ("backup", 1), ("master", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: carpIfState.setStatus('current')
if mibBuilder.loadTexts: carpIfState.setDescription('Indicates the operational state of the CARP interface.')
carpIpPktsRecv = MibScalar((1, 3, 6, 1, 4, 1, 30155, 6, 3, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: carpIpPktsRecv.setStatus('current')
if mibBuilder.loadTexts: carpIpPktsRecv.setDescription('Number of IPv4 CARP packets received on all interfaces.')
carpIp6PktsRecv = MibScalar((1, 3, 6, 1, 4, 1, 30155, 6, 3, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: carpIp6PktsRecv.setStatus('current')
if mibBuilder.loadTexts: carpIp6PktsRecv.setDescription('Number of IPv6 CARP packets received on all interfaces.')
carpPktDiscardsForBadInterface = MibScalar((1, 3, 6, 1, 4, 1, 30155, 6, 3, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: carpPktDiscardsForBadInterface.setStatus('current')
if mibBuilder.loadTexts: carpPktDiscardsForBadInterface.setDescription('Number of packets discarded due to being received on a\n\tnon-CARP interface.')
carpPktDiscardsForWrongTtl = MibScalar((1, 3, 6, 1, 4, 1, 30155, 6, 3, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: carpPktDiscardsForWrongTtl.setStatus('current')
if mibBuilder.loadTexts: carpPktDiscardsForWrongTtl.setDescription('Number of packets discarded due to having a TTL less\n\tthan 255.')
carpPktShorterThanHeader = MibScalar((1, 3, 6, 1, 4, 1, 30155, 6, 3, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: carpPktShorterThanHeader.setStatus('current')
if mibBuilder.loadTexts: carpPktShorterThanHeader.setDescription('Number of packets received on any interface that is\n\tshorter than the size of the CARP packet header.')
carpPktDiscardsForBadChecksum = MibScalar((1, 3, 6, 1, 4, 1, 30155, 6, 3, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: carpPktDiscardsForBadChecksum.setStatus('current')
if mibBuilder.loadTexts: carpPktDiscardsForBadChecksum.setDescription('Number of packets discarded due to bad checksum.')
carpPktDiscardsForBadVersion = MibScalar((1, 3, 6, 1, 4, 1, 30155, 6, 3, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: carpPktDiscardsForBadVersion.setStatus('current')
if mibBuilder.loadTexts: carpPktDiscardsForBadVersion.setDescription('Number of packets discarded due to bad version in\n\tthe packet header.')
carpPktDiscardsForTooShort = MibScalar((1, 3, 6, 1, 4, 1, 30155, 6, 3, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: carpPktDiscardsForTooShort.setStatus('current')
if mibBuilder.loadTexts: carpPktDiscardsForTooShort.setDescription('Number of packets discarded due to being too short.')
carpPktDiscardsForBadAuth = MibScalar((1, 3, 6, 1, 4, 1, 30155, 6, 3, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: carpPktDiscardsForBadAuth.setStatus('current')
if mibBuilder.loadTexts: carpPktDiscardsForBadAuth.setDescription('Number of packets discarded because they failed the\n\tHMAC authentication check.')
carpPktDiscardsForBadVhid = MibScalar((1, 3, 6, 1, 4, 1, 30155, 6, 3, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: carpPktDiscardsForBadVhid.setStatus('current')
if mibBuilder.loadTexts: carpPktDiscardsForBadVhid.setDescription('Number of packets discarded due to incorrect VHID in\n\tthe packet header.')
carpPktDiscardsForBadAddressList = MibScalar((1, 3, 6, 1, 4, 1, 30155, 6, 3, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: carpPktDiscardsForBadAddressList.setStatus('current')
if mibBuilder.loadTexts: carpPktDiscardsForBadAddressList.setDescription('Number of packets discarded due to bad addresses in\n\tthe CARP packet.')
carpIpPktsSent = MibScalar((1, 3, 6, 1, 4, 1, 30155, 6, 3, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: carpIpPktsSent.setStatus('current')
if mibBuilder.loadTexts: carpIpPktsSent.setDescription('Number of IPv4 CARP packets sent on all interfaces.')
carpIp6PktsSent = MibScalar((1, 3, 6, 1, 4, 1, 30155, 6, 3, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: carpIp6PktsSent.setStatus('current')
if mibBuilder.loadTexts: carpIp6PktsSent.setDescription('Number of IPv6 CARP packets sent on all interfaces.')
carpNoMemory = MibScalar((1, 3, 6, 1, 4, 1, 30155, 6, 3, 14), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: carpNoMemory.setStatus('current')
if mibBuilder.loadTexts: carpNoMemory.setDescription('Number of CARP advertisements that failed because memory\n\tcould not be allocated.')
carpTransitionsToMaster = MibScalar((1, 3, 6, 1, 4, 1, 30155, 6, 3, 15), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: carpTransitionsToMaster.setStatus('current')
if mibBuilder.loadTexts: carpTransitionsToMaster.setDescription('Number of times the host has transitioned to MASTER state\n\tfor any CARP group.')
mibBuilder.exportSymbols("OPENBSD-CARP-MIB", carpIfNumber=carpIfNumber, carpIfVhid=carpIfVhid, carpIfTable=carpIfTable, carpStats=carpStats, carpSysctl=carpSysctl, carpPktDiscardsForBadAddressList=carpPktDiscardsForBadAddressList, carpPktDiscardsForTooShort=carpPktDiscardsForTooShort, carpIf=carpIf, carpIp6PktsSent=carpIp6PktsSent, carpTransitionsToMaster=carpTransitionsToMaster, carpIfDescr=carpIfDescr, carpIfDev=carpIfDev, carpLog=carpLog, carpPktDiscardsForBadChecksum=carpPktDiscardsForBadChecksum, carpMIBObjects=carpMIBObjects, carpPreempt=carpPreempt, carpIpPktsRecv=carpIpPktsRecv, PYSNMP_MODULE_ID=carpMIBObjects, carpPktDiscardsForBadVhid=carpPktDiscardsForBadVhid, carpPktShorterThanHeader=carpPktShorterThanHeader, carpIfAdvbase=carpIfAdvbase, carpIfIndex=carpIfIndex, carpIfAdvskew=carpIfAdvskew, carpAllow=carpAllow, carpPktDiscardsForBadAuth=carpPktDiscardsForBadAuth, carpPktDiscardsForWrongTtl=carpPktDiscardsForWrongTtl, carpIfState=carpIfState, carpIpPktsSent=carpIpPktsSent, carpPktDiscardsForBadVersion=carpPktDiscardsForBadVersion, carpIp6PktsRecv=carpIp6PktsRecv, carpIfEntry=carpIfEntry, carpPktDiscardsForBadInterface=carpPktDiscardsForBadInterface, carpNoMemory=carpNoMemory)
