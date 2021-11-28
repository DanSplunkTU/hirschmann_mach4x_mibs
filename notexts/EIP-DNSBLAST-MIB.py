#
# PySNMP MIB module EIP-DNSBLAST-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/efficientip/EIP-DNSBLAST-MIB
# Produced by pysmi-1.1.3 at Sun Nov 28 20:18:25 2021
# On host fv-az77-612 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
enterprises, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, IpAddress, ModuleIdentity, Counter32, Unsigned32, MibIdentifier, NotificationType, Integer32, iso, Gauge32, TimeTicks, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "IpAddress", "ModuleIdentity", "Counter32", "Unsigned32", "MibIdentifier", "NotificationType", "Integer32", "iso", "Gauge32", "TimeTicks", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
eip = ModuleIdentity((1, 3, 6, 1, 4, 1, 2440))
eip.setRevisions(('2015-11-30 00:00',))
if mibBuilder.loadTexts: eip.setLastUpdated('201511300000Z')
if mibBuilder.loadTexts: eip.setOrganization('EfficientIP')
products = MibIdentifier((1, 3, 6, 1, 4, 1, 2440, 1))
eipDNSGUARDIAN = MibIdentifier((1, 3, 6, 1, 4, 1, 2440, 1, 11))
eipDNSGUARDIANStat = MibIdentifier((1, 3, 6, 1, 4, 1, 2440, 1, 11, 2))
eipDNSGUARDIANViewStatTable = MibTable((1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 3), )
if mibBuilder.loadTexts: eipDNSGUARDIANViewStatTable.setStatus('current')
eipDNSGUARDIANViewStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 3, 1), ).setIndexNames((0, "EIP-DNSBLAST-MIB", "eipDNSGUARDIANViewStatViewID"))
if mibBuilder.loadTexts: eipDNSGUARDIANViewStatEntry.setStatus('current')
eipDNSGUARDIANViewStatViewID = MibTableColumn((1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7)))
if mibBuilder.loadTexts: eipDNSGUARDIANViewStatViewID.setStatus('current')
eipDNSGUARDIANViewStatViewName = MibTableColumn((1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 3, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDNSGUARDIANViewStatViewName.setStatus('current')
eipDNSGUARDIANViewStatCacheHit = MibTableColumn((1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 3, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDNSGUARDIANViewStatCacheHit.setStatus('current')
eipDNSGUARDIANViewStatCacheMiss = MibTableColumn((1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 3, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDNSGUARDIANViewStatCacheMiss.setStatus('current')
eipDNSGUARDIANViewStatCacheSize = MibTableColumn((1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 3, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDNSGUARDIANViewStatCacheSize.setStatus('current')
eipDNSGUARDIANViewStatSendDNSPacket = MibTableColumn((1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 3, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDNSGUARDIANViewStatSendDNSPacket.setStatus('current')
eipDNSGUARDIANViewStatSendDNSByte = MibTableColumn((1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 3, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDNSGUARDIANViewStatSendDNSByte.setStatus('current')
eipDNSGUARDIANViewStatRecvDNSPacket = MibTableColumn((1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 3, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDNSGUARDIANViewStatRecvDNSPacket.setStatus('current')
eipDNSGUARDIANViewStatRecvDNSByte = MibTableColumn((1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 3, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDNSGUARDIANViewStatRecvDNSByte.setStatus('current')
eipDNSGUARDIANViewStatCacheMissExist = MibTableColumn((1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 3, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDNSGUARDIANViewStatCacheMissExist.setStatus('current')
eipDNSGUARDIANViewStatCacheMissNotExist = MibTableColumn((1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 3, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDNSGUARDIANViewStatCacheMissNotExist.setStatus('current')
eipDNSGUARDIANViewStatSendRescueDNSPacket = MibTableColumn((1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 3, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDNSGUARDIANViewStatSendRescueDNSPacket.setStatus('current')
eipDNSGUARDIANViewStatSendRescueDNSByte = MibTableColumn((1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 3, 1, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDNSGUARDIANViewStatSendRescueDNSByte.setStatus('current')
eipDNSGUARDIANViewStatRecvInvalidDNSPacket = MibTableColumn((1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 3, 1, 14), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDNSGUARDIANViewStatRecvInvalidDNSPacket.setStatus('current')
eipDNSGUARDIANViewStatRecvInvalidDNSByte = MibTableColumn((1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 3, 1, 15), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDNSGUARDIANViewStatRecvInvalidDNSByte.setStatus('current')
eipDNSGUARDIANViewStatRecvInvalidClass = MibTableColumn((1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 3, 1, 16), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDNSGUARDIANViewStatRecvInvalidClass.setStatus('current')
eipDNSGUARDIANViewStatRecvInvalidOverflow = MibTableColumn((1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 3, 1, 17), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDNSGUARDIANViewStatRecvInvalidOverflow.setStatus('current')
eipDNSGUARDIANViewStatRecvInvalidEtherSource = MibTableColumn((1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 3, 1, 18), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDNSGUARDIANViewStatRecvInvalidEtherSource.setStatus('current')
eipDNSGUARDIANViewStatRecvInvalidUDPSource = MibTableColumn((1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 3, 1, 19), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDNSGUARDIANViewStatRecvInvalidUDPSource.setStatus('current')
eipDNSGUARDIANViewStatRecvInvalidIPSrcEqDst = MibTableColumn((1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 3, 1, 20), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDNSGUARDIANViewStatRecvInvalidIPSrcEqDst.setStatus('current')
eipDNSGUARDIANViewStatRecvInvalidQDCount = MibTableColumn((1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 3, 1, 21), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDNSGUARDIANViewStatRecvInvalidQDCount.setStatus('current')
eipDNSGUARDIANViewStatRecvInvalidOPCode = MibTableColumn((1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 3, 1, 22), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDNSGUARDIANViewStatRecvInvalidOPCode.setStatus('current')
eipDNSGUARDIANViewStatRecvSharedPacket = MibTableColumn((1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 3, 1, 30), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDNSGUARDIANViewStatRecvSharedPacket.setStatus('current')
eipDNSGUARDIANViewStatRecvSharedByte = MibTableColumn((1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 3, 1, 31), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDNSGUARDIANViewStatRecvSharedByte.setStatus('current')
eipDNSGUARDIANViewStatSendSharedPacket = MibTableColumn((1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 3, 1, 32), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDNSGUARDIANViewStatSendSharedPacket.setStatus('current')
eipDNSGUARDIANViewStatSendSharedByte = MibTableColumn((1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 3, 1, 33), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDNSGUARDIANViewStatSendSharedByte.setStatus('current')
eipDNSGUARDIANViewStatCacheMissQuarantine = MibTableColumn((1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 3, 1, 34), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDNSGUARDIANViewStatCacheMissQuarantine.setStatus('current')
eipDNSGUARDIANViewStatCacheMissExistQuarantine = MibTableColumn((1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 3, 1, 35), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDNSGUARDIANViewStatCacheMissExistQuarantine.setStatus('current')
eipDNSGUARDIANViewStatCacheMissNotExistQuarantine = MibTableColumn((1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 3, 1, 36), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDNSGUARDIANViewStatCacheMissNotExistQuarantine.setStatus('current')
eipDNSGUARDIANViewStatCacheHitQuarantine = MibTableColumn((1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 3, 1, 37), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDNSGUARDIANViewStatCacheHitQuarantine.setStatus('current')
eipDNSGUARDIANViewStatQuarantineSendDNSPacket = MibTableColumn((1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 3, 1, 38), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDNSGUARDIANViewStatQuarantineSendDNSPacket.setStatus('current')
eipDNSGUARDIANViewStatQuarantineSendDNSByte = MibTableColumn((1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 3, 1, 39), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDNSGUARDIANViewStatQuarantineSendDNSByte.setStatus('current')
eipDNSGUARDIANViewStatCacheMissRescue = MibTableColumn((1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 3, 1, 40), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDNSGUARDIANViewStatCacheMissRescue.setStatus('current')
eipDNSGUARDIANViewStatCacheMissExistRescue = MibTableColumn((1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 3, 1, 41), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDNSGUARDIANViewStatCacheMissExistRescue.setStatus('current')
eipDNSGUARDIANViewStatCacheMissNotExistRescue = MibTableColumn((1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 3, 1, 42), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDNSGUARDIANViewStatCacheMissNotExistRescue.setStatus('current')
eipDNSGUARDIANViewStatCacheHitRescue = MibTableColumn((1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 3, 1, 43), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDNSGUARDIANViewStatCacheHitRescue.setStatus('current')
eipDNSGUARDIANViewStatBlockedQuery = MibTableColumn((1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 3, 1, 44), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDNSGUARDIANViewStatBlockedQuery.setStatus('current')
eipDNSGUARDIANViewStatRatelimitedQuery = MibTableColumn((1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 3, 1, 47), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDNSGUARDIANViewStatRatelimitedQuery.setStatus('current')
eipDNSGUARDIANViewStatRTT10 = MibTableColumn((1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 3, 1, 48), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDNSGUARDIANViewStatRTT10.setStatus('current')
eipDNSGUARDIANViewStatRTT100 = MibTableColumn((1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 3, 1, 49), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDNSGUARDIANViewStatRTT100.setStatus('current')
eipDNSGUARDIANViewStatRTT500 = MibTableColumn((1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 3, 1, 50), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDNSGUARDIANViewStatRTT500.setStatus('current')
eipDNSGUARDIANViewStatRTT800 = MibTableColumn((1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 3, 1, 51), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDNSGUARDIANViewStatRTT800.setStatus('current')
eipDNSGUARDIANViewStatRTT1600 = MibTableColumn((1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 3, 1, 52), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDNSGUARDIANViewStatRTT1600.setStatus('current')
eipDNSGUARDIANViewStatRTTMax = MibTableColumn((1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 3, 1, 53), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDNSGUARDIANViewStatRTTMax.setStatus('current')
eipDNSGUARDIANViewStatCacheMissQuarantineRedirect = MibTableColumn((1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 3, 1, 54), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDNSGUARDIANViewStatCacheMissQuarantineRedirect.setStatus('current')
eipDNSGUARDIANViewStatQuarantineRedirectSendDNSPacket = MibTableColumn((1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 3, 1, 55), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDNSGUARDIANViewStatQuarantineRedirectSendDNSPacket.setStatus('current')
eipDNSGUARDIANViewStatQuarantineRedirectSendDNSByte = MibTableColumn((1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 3, 1, 56), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDNSGUARDIANViewStatQuarantineRedirectSendDNSByte.setStatus('current')
eipDNSGUARDIANGlobalStat = MibIdentifier((1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4))
eipDNSGUARDIANStatCacheHit = MibScalar((1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDNSGUARDIANStatCacheHit.setStatus('current')
eipDNSGUARDIANStatCacheMiss = MibScalar((1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDNSGUARDIANStatCacheMiss.setStatus('current')
eipDNSGUARDIANStatCacheSize = MibScalar((1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDNSGUARDIANStatCacheSize.setStatus('current')
eipDNSGUARDIANStatSendDNSPacket = MibScalar((1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDNSGUARDIANStatSendDNSPacket.setStatus('current')
eipDNSGUARDIANStatSendDNSByte = MibScalar((1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDNSGUARDIANStatSendDNSByte.setStatus('current')
eipDNSGUARDIANStatRecvDNSPacket = MibScalar((1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDNSGUARDIANStatRecvDNSPacket.setStatus('current')
eipDNSGUARDIANStatRecvDNSByte = MibScalar((1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDNSGUARDIANStatRecvDNSByte.setStatus('current')
eipDNSGUARDIANStatCacheMissExist = MibScalar((1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDNSGUARDIANStatCacheMissExist.setStatus('current')
eipDNSGUARDIANStatCacheMissNotExist = MibScalar((1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDNSGUARDIANStatCacheMissNotExist.setStatus('current')
eipDNSGUARDIANStatSendRescueDNSPacket = MibScalar((1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDNSGUARDIANStatSendRescueDNSPacket.setStatus('current')
eipDNSGUARDIANStatSendRescueDNSByte = MibScalar((1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDNSGUARDIANStatSendRescueDNSByte.setStatus('current')
eipDNSGUARDIANStatRecvInvalidDNSPacket = MibScalar((1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 14), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDNSGUARDIANStatRecvInvalidDNSPacket.setStatus('current')
eipDNSGUARDIANStatRecvInvalidDNSByte = MibScalar((1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 15), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDNSGUARDIANStatRecvInvalidDNSByte.setStatus('current')
eipDNSGUARDIANStatRecvInvalidClass = MibScalar((1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 16), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDNSGUARDIANStatRecvInvalidClass.setStatus('current')
eipDNSGUARDIANStatRecvInvalidOverflow = MibScalar((1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 17), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDNSGUARDIANStatRecvInvalidOverflow.setStatus('current')
eipDNSGUARDIANStatRecvInvalidEtherSource = MibScalar((1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 18), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDNSGUARDIANStatRecvInvalidEtherSource.setStatus('current')
eipDNSGUARDIANStatRecvInvalidUDPSource = MibScalar((1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 19), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDNSGUARDIANStatRecvInvalidUDPSource.setStatus('current')
eipDNSGUARDIANStatRecvInvalidIPSrcEqDst = MibScalar((1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 20), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDNSGUARDIANStatRecvInvalidIPSrcEqDst.setStatus('current')
eipDNSGUARDIANStatRecvInvalidQDCount = MibScalar((1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 21), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDNSGUARDIANStatRecvInvalidQDCount.setStatus('current')
eipDNSGUARDIANStatRecvInvalidOPCode = MibScalar((1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 22), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDNSGUARDIANStatRecvInvalidOPCode.setStatus('current')
eipDNSGUARDIANStatRecvSharedPacket = MibScalar((1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 30), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDNSGUARDIANStatRecvSharedPacket.setStatus('current')
eipDNSGUARDIANStatRecvSharedByte = MibScalar((1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 31), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDNSGUARDIANStatRecvSharedByte.setStatus('current')
eipDNSGUARDIANStatSendSharedPacket = MibScalar((1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 32), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDNSGUARDIANStatSendSharedPacket.setStatus('current')
eipDNSGUARDIANStatSendSharedByte = MibScalar((1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 33), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDNSGUARDIANStatSendSharedByte.setStatus('current')
eipDNSGUARDIANStatCacheMissQuarantine = MibScalar((1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 34), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDNSGUARDIANStatCacheMissQuarantine.setStatus('current')
eipDNSGUARDIANStatCacheMissExistQuarantine = MibScalar((1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 35), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDNSGUARDIANStatCacheMissExistQuarantine.setStatus('current')
eipDNSGUARDIANStatCacheMissNotExistQuarantine = MibScalar((1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 36), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDNSGUARDIANStatCacheMissNotExistQuarantine.setStatus('current')
eipDNSGUARDIANStatCacheHitQuarantine = MibScalar((1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 37), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDNSGUARDIANStatCacheHitQuarantine.setStatus('current')
eipDNSGUARDIANStatQuarantineSendDNSPacket = MibScalar((1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 38), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDNSGUARDIANStatQuarantineSendDNSPacket.setStatus('current')
eipDNSGUARDIANStatQuarantineSendDNSByte = MibScalar((1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 39), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDNSGUARDIANStatQuarantineSendDNSByte.setStatus('current')
eipDNSGUARDIANStatCacheMissRescue = MibScalar((1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 40), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDNSGUARDIANStatCacheMissRescue.setStatus('current')
eipDNSGUARDIANStatCacheMissExistRescue = MibScalar((1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 41), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDNSGUARDIANStatCacheMissExistRescue.setStatus('current')
eipDNSGUARDIANStatCacheMissNotExistRescue = MibScalar((1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 42), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDNSGUARDIANStatCacheMissNotExistRescue.setStatus('current')
eipDNSGUARDIANStatCacheHitRescue = MibScalar((1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 43), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDNSGUARDIANStatCacheHitRescue.setStatus('current')
eipDNSGUARDIANStatBlockedQuery = MibScalar((1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 44), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDNSGUARDIANStatBlockedQuery.setStatus('current')
eipDNSGUARDIANStatClientsSize = MibScalar((1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 45), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDNSGUARDIANStatClientsSize.setStatus('current')
eipDNSGUARDIANStatClientsUpdated = MibScalar((1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 46), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDNSGUARDIANStatClientsUpdated.setStatus('current')
eipDNSGUARDIANStatRatelimitedQuery = MibScalar((1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 47), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDNSGUARDIANStatRatelimitedQuery.setStatus('current')
eipDNSGUARDIANStatRTT10 = MibScalar((1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 48), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDNSGUARDIANStatRTT10.setStatus('current')
eipDNSGUARDIANStatRTT100 = MibScalar((1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 49), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDNSGUARDIANStatRTT100.setStatus('current')
eipDNSGUARDIANStatRTT500 = MibScalar((1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 50), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDNSGUARDIANStatRTT500.setStatus('current')
eipDNSGUARDIANStatRTT800 = MibScalar((1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 51), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDNSGUARDIANStatRTT800.setStatus('current')
eipDNSGUARDIANStatRTT1600 = MibScalar((1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 52), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDNSGUARDIANStatRTT1600.setStatus('current')
eipDNSGUARDIANStatRTTMax = MibScalar((1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 53), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDNSGUARDIANStatRTTMax.setStatus('current')
eipDNSGUARDIANStatCacheMissQuarantineRedirect = MibScalar((1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 54), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDNSGUARDIANStatCacheMissQuarantineRedirect.setStatus('current')
eipDNSGUARDIANStatQuarantineRedirectSendDNSPacket = MibScalar((1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 55), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDNSGUARDIANStatQuarantineRedirectSendDNSPacket.setStatus('current')
eipDNSGUARDIANStatQuarantineRedirectSendDNSByte = MibScalar((1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 56), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDNSGUARDIANStatQuarantineRedirectSendDNSByte.setStatus('current')
eipDNSGUARDIANStatReplyNOERROR = MibScalar((1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 101), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDNSGUARDIANStatReplyNOERROR.setStatus('current')
eipDNSGUARDIANStatReplyFORMERR = MibScalar((1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 102), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDNSGUARDIANStatReplyFORMERR.setStatus('current')
eipDNSGUARDIANStatReplySERVFAIL = MibScalar((1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 103), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDNSGUARDIANStatReplySERVFAIL.setStatus('current')
eipDNSGUARDIANStatReplyNXDOMAIN = MibScalar((1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 104), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDNSGUARDIANStatReplyNXDOMAIN.setStatus('current')
eipDNSGUARDIANStatReplyNOTIMP = MibScalar((1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 105), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDNSGUARDIANStatReplyNOTIMP.setStatus('current')
eipDNSGUARDIANStatReplyREFUSED = MibScalar((1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 106), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDNSGUARDIANStatReplyREFUSED.setStatus('current')
eipDNSGUARDIANStatReplyYXDOMAIN = MibScalar((1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 107), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDNSGUARDIANStatReplyYXDOMAIN.setStatus('current')
eipDNSGUARDIANStatReplyYXRRSET = MibScalar((1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 108), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDNSGUARDIANStatReplyYXRRSET.setStatus('current')
eipDNSGUARDIANStatReplyNXRRSET = MibScalar((1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 109), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDNSGUARDIANStatReplyNXRRSET.setStatus('current')
eipDNSGUARDIANStatReplyNOTAUTH = MibScalar((1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 120), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDNSGUARDIANStatReplyNOTAUTH.setStatus('current')
eipDNSGUARDIANStatReplyNOTZONE = MibScalar((1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 121), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDNSGUARDIANStatReplyNOTZONE.setStatus('current')
mibBuilder.exportSymbols("EIP-DNSBLAST-MIB", eipDNSGUARDIANStatRTT1600=eipDNSGUARDIANStatRTT1600, eipDNSGUARDIANStatRTT100=eipDNSGUARDIANStatRTT100, eipDNSGUARDIANViewStatTable=eipDNSGUARDIANViewStatTable, eipDNSGUARDIANViewStatRecvInvalidUDPSource=eipDNSGUARDIANViewStatRecvInvalidUDPSource, eipDNSGUARDIANViewStatCacheMissExist=eipDNSGUARDIANViewStatCacheMissExist, eipDNSGUARDIANStatSendRescueDNSByte=eipDNSGUARDIANStatSendRescueDNSByte, eipDNSGUARDIANStatRatelimitedQuery=eipDNSGUARDIANStatRatelimitedQuery, eipDNSGUARDIANStatClientsSize=eipDNSGUARDIANStatClientsSize, eipDNSGUARDIANStatQuarantineRedirectSendDNSByte=eipDNSGUARDIANStatQuarantineRedirectSendDNSByte, eipDNSGUARDIANViewStatViewID=eipDNSGUARDIANViewStatViewID, PYSNMP_MODULE_ID=eip, eipDNSGUARDIANViewStatRecvDNSByte=eipDNSGUARDIANViewStatRecvDNSByte, eipDNSGUARDIANStatSendDNSPacket=eipDNSGUARDIANStatSendDNSPacket, eipDNSGUARDIANViewStatQuarantineRedirectSendDNSPacket=eipDNSGUARDIANViewStatQuarantineRedirectSendDNSPacket, eipDNSGUARDIANStatRecvInvalidQDCount=eipDNSGUARDIANStatRecvInvalidQDCount, eipDNSGUARDIANStatRecvSharedPacket=eipDNSGUARDIANStatRecvSharedPacket, eipDNSGUARDIANStatReplyREFUSED=eipDNSGUARDIANStatReplyREFUSED, eipDNSGUARDIANViewStatCacheSize=eipDNSGUARDIANViewStatCacheSize, eipDNSGUARDIANStatCacheMissNotExistQuarantine=eipDNSGUARDIANStatCacheMissNotExistQuarantine, eipDNSGUARDIANViewStatRTT800=eipDNSGUARDIANViewStatRTT800, eipDNSGUARDIAN=eipDNSGUARDIAN, eipDNSGUARDIANStatRecvInvalidClass=eipDNSGUARDIANStatRecvInvalidClass, eipDNSGUARDIANViewStatSendRescueDNSPacket=eipDNSGUARDIANViewStatSendRescueDNSPacket, eipDNSGUARDIANViewStatQuarantineSendDNSByte=eipDNSGUARDIANViewStatQuarantineSendDNSByte, eipDNSGUARDIANViewStatRecvInvalidIPSrcEqDst=eipDNSGUARDIANViewStatRecvInvalidIPSrcEqDst, eipDNSGUARDIANViewStatQuarantineRedirectSendDNSByte=eipDNSGUARDIANViewStatQuarantineRedirectSendDNSByte, products=products, eipDNSGUARDIANViewStatCacheHitQuarantine=eipDNSGUARDIANViewStatCacheHitQuarantine, eipDNSGUARDIANStatReplyNOERROR=eipDNSGUARDIANStatReplyNOERROR, eipDNSGUARDIANStatSendSharedByte=eipDNSGUARDIANStatSendSharedByte, eipDNSGUARDIANStatCacheMissQuarantineRedirect=eipDNSGUARDIANStatCacheMissQuarantineRedirect, eipDNSGUARDIANStatReplyNOTAUTH=eipDNSGUARDIANStatReplyNOTAUTH, eipDNSGUARDIANStatQuarantineSendDNSPacket=eipDNSGUARDIANStatQuarantineSendDNSPacket, eipDNSGUARDIANStatRecvInvalidOverflow=eipDNSGUARDIANStatRecvInvalidOverflow, eipDNSGUARDIANStatRecvInvalidDNSByte=eipDNSGUARDIANStatRecvInvalidDNSByte, eipDNSGUARDIANViewStatRecvInvalidOPCode=eipDNSGUARDIANViewStatRecvInvalidOPCode, eipDNSGUARDIANStatSendDNSByte=eipDNSGUARDIANStatSendDNSByte, eipDNSGUARDIANViewStatRecvInvalidEtherSource=eipDNSGUARDIANViewStatRecvInvalidEtherSource, eipDNSGUARDIANViewStatRecvInvalidClass=eipDNSGUARDIANViewStatRecvInvalidClass, eipDNSGUARDIANViewStatViewName=eipDNSGUARDIANViewStatViewName, eipDNSGUARDIANStatRecvSharedByte=eipDNSGUARDIANStatRecvSharedByte, eipDNSGUARDIANStatCacheMissNotExistRescue=eipDNSGUARDIANStatCacheMissNotExistRescue, eipDNSGUARDIANStatRTTMax=eipDNSGUARDIANStatRTTMax, eipDNSGUARDIANViewStatCacheHit=eipDNSGUARDIANViewStatCacheHit, eipDNSGUARDIANStatReplySERVFAIL=eipDNSGUARDIANStatReplySERVFAIL, eipDNSGUARDIANStatRecvInvalidDNSPacket=eipDNSGUARDIANStatRecvInvalidDNSPacket, eipDNSGUARDIANStatClientsUpdated=eipDNSGUARDIANStatClientsUpdated, eipDNSGUARDIANStatReplyNXRRSET=eipDNSGUARDIANStatReplyNXRRSET, eipDNSGUARDIANStatCacheHit=eipDNSGUARDIANStatCacheHit, eipDNSGUARDIANViewStatQuarantineSendDNSPacket=eipDNSGUARDIANViewStatQuarantineSendDNSPacket, eipDNSGUARDIANGlobalStat=eipDNSGUARDIANGlobalStat, eipDNSGUARDIANViewStatRecvDNSPacket=eipDNSGUARDIANViewStatRecvDNSPacket, eipDNSGUARDIANStatCacheMissNotExist=eipDNSGUARDIANStatCacheMissNotExist, eipDNSGUARDIANViewStatCacheMissQuarantineRedirect=eipDNSGUARDIANViewStatCacheMissQuarantineRedirect, eipDNSGUARDIANViewStatSendDNSPacket=eipDNSGUARDIANViewStatSendDNSPacket, eipDNSGUARDIANStatRecvInvalidIPSrcEqDst=eipDNSGUARDIANStatRecvInvalidIPSrcEqDst, eipDNSGUARDIANStatRecvInvalidOPCode=eipDNSGUARDIANStatRecvInvalidOPCode, eipDNSGUARDIANStatBlockedQuery=eipDNSGUARDIANStatBlockedQuery, eipDNSGUARDIANViewStatEntry=eipDNSGUARDIANViewStatEntry, eipDNSGUARDIANViewStatSendRescueDNSByte=eipDNSGUARDIANViewStatSendRescueDNSByte, eipDNSGUARDIANStatCacheSize=eipDNSGUARDIANStatCacheSize, eipDNSGUARDIANStatReplyYXRRSET=eipDNSGUARDIANStatReplyYXRRSET, eip=eip, eipDNSGUARDIANStatCacheMissExistQuarantine=eipDNSGUARDIANStatCacheMissExistQuarantine, eipDNSGUARDIANStatRecvInvalidUDPSource=eipDNSGUARDIANStatRecvInvalidUDPSource, eipDNSGUARDIANViewStatRTT1600=eipDNSGUARDIANViewStatRTT1600, eipDNSGUARDIANViewStatSendDNSByte=eipDNSGUARDIANViewStatSendDNSByte, eipDNSGUARDIANViewStatRecvSharedByte=eipDNSGUARDIANViewStatRecvSharedByte, eipDNSGUARDIANViewStatRTTMax=eipDNSGUARDIANViewStatRTTMax, eipDNSGUARDIANViewStatRecvInvalidDNSByte=eipDNSGUARDIANViewStatRecvInvalidDNSByte, eipDNSGUARDIANViewStatRatelimitedQuery=eipDNSGUARDIANViewStatRatelimitedQuery, eipDNSGUARDIANStatCacheMissQuarantine=eipDNSGUARDIANStatCacheMissQuarantine, eipDNSGUARDIANViewStatCacheMissNotExist=eipDNSGUARDIANViewStatCacheMissNotExist, eipDNSGUARDIANViewStatRTT10=eipDNSGUARDIANViewStatRTT10, eipDNSGUARDIANViewStatRecvSharedPacket=eipDNSGUARDIANViewStatRecvSharedPacket, eipDNSGUARDIANStatRecvDNSByte=eipDNSGUARDIANStatRecvDNSByte, eipDNSGUARDIANStatRecvInvalidEtherSource=eipDNSGUARDIANStatRecvInvalidEtherSource, eipDNSGUARDIANStat=eipDNSGUARDIANStat, eipDNSGUARDIANStatRTT800=eipDNSGUARDIANStatRTT800, eipDNSGUARDIANStatRTT10=eipDNSGUARDIANStatRTT10, eipDNSGUARDIANStatSendSharedPacket=eipDNSGUARDIANStatSendSharedPacket, eipDNSGUARDIANViewStatCacheMissExistRescue=eipDNSGUARDIANViewStatCacheMissExistRescue, eipDNSGUARDIANStatQuarantineSendDNSByte=eipDNSGUARDIANStatQuarantineSendDNSByte, eipDNSGUARDIANStatRTT500=eipDNSGUARDIANStatRTT500, eipDNSGUARDIANViewStatCacheMiss=eipDNSGUARDIANViewStatCacheMiss, eipDNSGUARDIANViewStatCacheMissNotExistRescue=eipDNSGUARDIANViewStatCacheMissNotExistRescue, eipDNSGUARDIANViewStatSendSharedPacket=eipDNSGUARDIANViewStatSendSharedPacket, eipDNSGUARDIANStatCacheHitRescue=eipDNSGUARDIANStatCacheHitRescue, eipDNSGUARDIANStatCacheMissExist=eipDNSGUARDIANStatCacheMissExist, eipDNSGUARDIANViewStatBlockedQuery=eipDNSGUARDIANViewStatBlockedQuery, eipDNSGUARDIANViewStatCacheMissRescue=eipDNSGUARDIANViewStatCacheMissRescue, eipDNSGUARDIANStatReplyNOTIMP=eipDNSGUARDIANStatReplyNOTIMP, eipDNSGUARDIANViewStatRecvInvalidDNSPacket=eipDNSGUARDIANViewStatRecvInvalidDNSPacket, eipDNSGUARDIANStatCacheMiss=eipDNSGUARDIANStatCacheMiss, eipDNSGUARDIANStatCacheMissRescue=eipDNSGUARDIANStatCacheMissRescue, eipDNSGUARDIANStatSendRescueDNSPacket=eipDNSGUARDIANStatSendRescueDNSPacket, eipDNSGUARDIANViewStatCacheMissQuarantine=eipDNSGUARDIANViewStatCacheMissQuarantine, eipDNSGUARDIANStatReplyNOTZONE=eipDNSGUARDIANStatReplyNOTZONE, eipDNSGUARDIANStatReplyYXDOMAIN=eipDNSGUARDIANStatReplyYXDOMAIN, eipDNSGUARDIANViewStatRecvInvalidOverflow=eipDNSGUARDIANViewStatRecvInvalidOverflow, eipDNSGUARDIANStatQuarantineRedirectSendDNSPacket=eipDNSGUARDIANStatQuarantineRedirectSendDNSPacket, eipDNSGUARDIANStatReplyNXDOMAIN=eipDNSGUARDIANStatReplyNXDOMAIN, eipDNSGUARDIANViewStatCacheMissNotExistQuarantine=eipDNSGUARDIANViewStatCacheMissNotExistQuarantine, eipDNSGUARDIANStatReplyFORMERR=eipDNSGUARDIANStatReplyFORMERR, eipDNSGUARDIANViewStatRecvInvalidQDCount=eipDNSGUARDIANViewStatRecvInvalidQDCount, eipDNSGUARDIANStatRecvDNSPacket=eipDNSGUARDIANStatRecvDNSPacket, eipDNSGUARDIANViewStatSendSharedByte=eipDNSGUARDIANViewStatSendSharedByte, eipDNSGUARDIANViewStatCacheHitRescue=eipDNSGUARDIANViewStatCacheHitRescue, eipDNSGUARDIANViewStatCacheMissExistQuarantine=eipDNSGUARDIANViewStatCacheMissExistQuarantine, eipDNSGUARDIANViewStatRTT100=eipDNSGUARDIANViewStatRTT100, eipDNSGUARDIANViewStatRTT500=eipDNSGUARDIANViewStatRTT500, eipDNSGUARDIANStatCacheMissExistRescue=eipDNSGUARDIANStatCacheMissExistRescue, eipDNSGUARDIANStatCacheHitQuarantine=eipDNSGUARDIANStatCacheHitQuarantine)
