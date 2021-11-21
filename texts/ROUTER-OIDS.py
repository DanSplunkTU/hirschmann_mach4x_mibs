#
# PySNMP MIB module ROUTER-OIDS (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/ROUTER-OIDS
# Produced by pysmi-1.1.3 at Sun Nov 21 00:45:13 2021
# On host fv-az39-63 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ctronExp, ctNetwork = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctronExp", "ctNetwork")
networkType, = mibBuilder.importSymbols("CTRON-OIDS", "networkType")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, IpAddress, Counter64, Integer32, Counter32, ObjectIdentity, NotificationType, Gauge32, MibIdentifier, Bits, Unsigned32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "IpAddress", "Counter64", "Integer32", "Counter32", "ObjectIdentity", "NotificationType", "Gauge32", "MibIdentifier", "Bits", "Unsigned32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ntProtoSuites = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 3, 7, 1))
ntIpRouter = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 1))
ntIpxRouter = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 2))
ntDecIVRouter = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 3))
ntAtRouter = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 4))
ntAppnRouter = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 5))
ntIpRip = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 1, 1))
ntIpOspf = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 1, 2))
ntIpFib = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 1, 3))
ntIpArp = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 1, 4))
ntIpAc1 = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 1, 5))
ntIpFwdEng = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 1, 6))
ntIpPortRedirect = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 1, 7))
ntIpEventLog = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 1, 8))
ntIpAddressTable = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 1, 9))
ntIpxRip = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 2, 1))
ntIpxSap = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 2, 2))
ntIpxFib = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 2, 3))
ntIpxAc1 = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 2, 5))
ntIpxFwdEng = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 2, 6))
ntIpxPortRedirect = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 2, 7))
ntIpxEventLog = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 2, 8))
ntIpxAddressTable = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 2, 9))
ntIpxEcho = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 2, 10))
ntIpxBroadcast = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 2, 11))
ntIpxNetbios = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 2, 12))
ntDecIVLevel1 = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 3, 1))
ntDecIVLevel2 = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 3, 2))
ntDecIVFib = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 3, 3))
ntDecIVAcl = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 3, 5))
ntDecIVFwdEng = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 3, 6))
ntDecIVPportRedirect = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 3, 7))
ntDecIVEventLog = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 3, 8))
ntDecIVAddressTable = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 3, 9))
ntAtRtgProt = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 4, 1))
ntAtFib = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 4, 3))
ntAtArp = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 4, 4))
ntAtAcl = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 4, 5))
ntAtFwdEng = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 4, 6))
ntAtEventLog = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 4, 8))
ntAtAddressTable = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 4, 9))
ntAppnFwdEng = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 5, 6))
ntAppnEventLog = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 5, 8))
ntAppnExtensionTable = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 5, 9))
ntAppnIsr = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 5, 10))
ctRouter = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 2))
ctHighLevelView = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 2, 2))
ctProtoSuites = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 2, 3))
ctApplicationView = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 2, 2, 1))
ctIpRouter = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 2, 3, 1))
ctIpxRouter = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 2, 3, 2))
ctDecIVRouter = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 2, 3, 3))
ctAtRouter = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 2, 3, 4))
ctAppnRouter = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 2, 3, 5))
ctronRouterExp = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 2))
nwRouter = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2))
nwRtrMibs = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 1))
nwRtrHighLevelView = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 2))
nwRtrProtoSuites = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3))
mibBuilder.exportSymbols("ROUTER-OIDS", ntIpPortRedirect=ntIpPortRedirect, ntIpRip=ntIpRip, ntIpFwdEng=ntIpFwdEng, ntAtFib=ntAtFib, ntIpxSap=ntIpxSap, ctHighLevelView=ctHighLevelView, nwRouter=nwRouter, ntDecIVRouter=ntDecIVRouter, ntDecIVPportRedirect=ntDecIVPportRedirect, ntDecIVEventLog=ntDecIVEventLog, nwRtrMibs=nwRtrMibs, nwRtrHighLevelView=nwRtrHighLevelView, ntDecIVLevel1=ntDecIVLevel1, ntProtoSuites=ntProtoSuites, ntDecIVLevel2=ntDecIVLevel2, ntAtArp=ntAtArp, ntAtRtgProt=ntAtRtgProt, ntIpFib=ntIpFib, ctRouter=ctRouter, ntIpAddressTable=ntIpAddressTable, ntIpOspf=ntIpOspf, ntIpEventLog=ntIpEventLog, ctProtoSuites=ctProtoSuites, ntIpRouter=ntIpRouter, ctIpxRouter=ctIpxRouter, ntIpxBroadcast=ntIpxBroadcast, ntIpxEcho=ntIpxEcho, ntAppnEventLog=ntAppnEventLog, ctronRouterExp=ctronRouterExp, ntIpxFib=ntIpxFib, ntDecIVFwdEng=ntDecIVFwdEng, ctAtRouter=ctAtRouter, ctIpRouter=ctIpRouter, ntAppnExtensionTable=ntAppnExtensionTable, ntDecIVFib=ntDecIVFib, ctDecIVRouter=ctDecIVRouter, ntIpArp=ntIpArp, ntIpxEventLog=ntIpxEventLog, ntIpAc1=ntIpAc1, ntIpxNetbios=ntIpxNetbios, ntAppnIsr=ntAppnIsr, ntAtRouter=ntAtRouter, ntIpxRip=ntIpxRip, ntIpxAddressTable=ntIpxAddressTable, ntIpxFwdEng=ntIpxFwdEng, ntDecIVAcl=ntDecIVAcl, ntAtEventLog=ntAtEventLog, ntIpxPortRedirect=ntIpxPortRedirect, ntAtAcl=ntAtAcl, ntAtFwdEng=ntAtFwdEng, ntIpxRouter=ntIpxRouter, ctApplicationView=ctApplicationView, ntAppnRouter=ntAppnRouter, ntDecIVAddressTable=ntDecIVAddressTable, ntAtAddressTable=ntAtAddressTable, ntIpxAc1=ntIpxAc1, ntAppnFwdEng=ntAppnFwdEng, nwRtrProtoSuites=nwRtrProtoSuites, ctAppnRouter=ctAppnRouter)
