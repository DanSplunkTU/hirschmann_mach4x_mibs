#
# PySNMP MIB module CTRON-ROUTERS-INTERNAL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-ROUTERS-INTERNAL-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:20:21 2022
# On host fv-az36-988 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, Gauge32, Counter32, iso, NotificationType, MibIdentifier, TimeTicks, enterprises, ModuleIdentity, IpAddress, Bits, ObjectIdentity, Unsigned32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Gauge32", "Counter32", "iso", "NotificationType", "MibIdentifier", "TimeTicks", "enterprises", "ModuleIdentity", "IpAddress", "Bits", "ObjectIdentity", "Unsigned32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
cabletron = MibIdentifier((1, 3, 6, 1, 4, 1, 52))
mibs = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4))
ctron = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1))
ctronExp = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2))
ctronRouterExp = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 2))
ctNetwork = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 3))
nwRouter = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2))
nwRtrTemp = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 99))
nwRtrTemp1 = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 99, 2))
nwRtrTemp2 = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 99, 2, 2))
nwRtrSoftReset = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 99, 2, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0))).clone(namedValues=NamedValues(("reset", 0)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nwRtrSoftReset.setStatus('mandatory')
mibBuilder.exportSymbols("CTRON-ROUTERS-INTERNAL-MIB", cabletron=cabletron, nwRtrTemp2=nwRtrTemp2, ctronRouterExp=ctronRouterExp, nwRtrSoftReset=nwRtrSoftReset, ctronExp=ctronExp, ctNetwork=ctNetwork, nwRtrTemp=nwRtrTemp, mibs=mibs, nwRtrTemp1=nwRtrTemp1, ctron=ctron, nwRouter=nwRouter)
