#
# PySNMP MIB module FOUNDRY-SN-MAC-AUTHENTICATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/foundry/FOUNDRY-SN-MAC-AUTHENTICATION-MIB
# Produced by pysmi-1.1.3 at Sun Nov 28 20:21:16 2021
# On host fv-az77-612 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, iso, Integer32, NotificationType, Unsigned32, Bits, TimeTicks, ModuleIdentity, Counter32, Counter64, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "iso", "Integer32", "NotificationType", "Unsigned32", "Bits", "TimeTicks", "ModuleIdentity", "Counter32", "Counter64", "IpAddress")
MacAddress, TimeStamp, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "TimeStamp", "TextualConvention", "DisplayString")
snMacAuth = ModuleIdentity((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 28))
snMacAuth.setRevisions(('2007-06-25 00:00',))
if mibBuilder.loadTexts: snMacAuth.setLastUpdated('200706250000Z')
if mibBuilder.loadTexts: snMacAuth.setOrganization('Foundry Networks, Inc')
snMacAuthGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 28, 1))
snMacAuthClearGlobalCmd = MibScalar((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 28, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("valid", 0), ("clear", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snMacAuthClearGlobalCmd.setStatus('current')
snMacAuthGlobalConfigState = MibScalar((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 28, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snMacAuthGlobalConfigState.setStatus('current')
snMacAuthClearIfCmdTable = MibTable((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 28, 2), )
if mibBuilder.loadTexts: snMacAuthClearIfCmdTable.setStatus('current')
snMacAuthClearIfCmdEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 28, 2, 1), ).setIndexNames((0, "FOUNDRY-SN-MAC-AUTHENTICATION-MIB", "snMacAuthClearIfCmdIfIndex"))
if mibBuilder.loadTexts: snMacAuthClearIfCmdEntry.setStatus('current')
snMacAuthClearIfCmdIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 28, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: snMacAuthClearIfCmdIfIndex.setStatus('current')
snMacAuthClearIfCmdAction = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 28, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("valid", 0), ("clear", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snMacAuthClearIfCmdAction.setStatus('current')
snMacAuthTable = MibTable((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 28, 3), )
if mibBuilder.loadTexts: snMacAuthTable.setStatus('current')
snMacAuthEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 28, 3, 1), ).setIndexNames((0, "FOUNDRY-SN-MAC-AUTHENTICATION-MIB", "snMacAuthIfIndex"), (0, "FOUNDRY-SN-MAC-AUTHENTICATION-MIB", "snMacAuthVlanId"), (0, "FOUNDRY-SN-MAC-AUTHENTICATION-MIB", "snMacAuthMac"))
if mibBuilder.loadTexts: snMacAuthEntry.setStatus('current')
snMacAuthIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 28, 3, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: snMacAuthIfIndex.setStatus('current')
snMacAuthVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 28, 3, 1, 2), Integer32())
if mibBuilder.loadTexts: snMacAuthVlanId.setStatus('current')
snMacAuthMac = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 28, 3, 1, 3), MacAddress())
if mibBuilder.loadTexts: snMacAuthMac.setStatus('current')
snMacAuthState = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 28, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("authenticate", 1), ("unauthenticate", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snMacAuthState.setStatus('current')
snMacAuthTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 28, 3, 1, 5), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snMacAuthTimeStamp.setStatus('current')
snMacAuthAge = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 28, 3, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snMacAuthAge.setStatus('current')
snMacAuthDot1x = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 28, 3, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snMacAuthDot1x.setStatus('current')
snMacAuthClearMacSessionTable = MibTable((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 28, 4), )
if mibBuilder.loadTexts: snMacAuthClearMacSessionTable.setStatus('current')
snMacAuthClearMacSessionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 28, 4, 1), ).setIndexNames((0, "FOUNDRY-SN-MAC-AUTHENTICATION-MIB", "snMacAuthClearMacSessionIfIndex"), (0, "FOUNDRY-SN-MAC-AUTHENTICATION-MIB", "snMacAuthClearMacSessionMac"))
if mibBuilder.loadTexts: snMacAuthClearMacSessionEntry.setStatus('current')
snMacAuthClearMacSessionIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 28, 4, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: snMacAuthClearMacSessionIfIndex.setStatus('current')
snMacAuthClearMacSessionMac = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 28, 4, 1, 2), MacAddress())
if mibBuilder.loadTexts: snMacAuthClearMacSessionMac.setStatus('current')
snMacAuthClearMacSessionAction = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 28, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("valid", 0), ("clear", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snMacAuthClearMacSessionAction.setStatus('current')
mibBuilder.exportSymbols("FOUNDRY-SN-MAC-AUTHENTICATION-MIB", snMacAuthAge=snMacAuthAge, snMacAuthGlobalConfigState=snMacAuthGlobalConfigState, snMacAuthClearMacSessionTable=snMacAuthClearMacSessionTable, snMacAuth=snMacAuth, snMacAuthClearMacSessionAction=snMacAuthClearMacSessionAction, snMacAuthIfIndex=snMacAuthIfIndex, snMacAuthClearMacSessionIfIndex=snMacAuthClearMacSessionIfIndex, snMacAuthClearIfCmdAction=snMacAuthClearIfCmdAction, snMacAuthTable=snMacAuthTable, snMacAuthClearIfCmdTable=snMacAuthClearIfCmdTable, snMacAuthClearMacSessionEntry=snMacAuthClearMacSessionEntry, PYSNMP_MODULE_ID=snMacAuth, snMacAuthMac=snMacAuthMac, snMacAuthState=snMacAuthState, snMacAuthClearMacSessionMac=snMacAuthClearMacSessionMac, snMacAuthClearGlobalCmd=snMacAuthClearGlobalCmd, snMacAuthEntry=snMacAuthEntry, snMacAuthTimeStamp=snMacAuthTimeStamp, snMacAuthDot1x=snMacAuthDot1x, snMacAuthVlanId=snMacAuthVlanId, snMacAuthGlobal=snMacAuthGlobal, snMacAuthClearIfCmdIfIndex=snMacAuthClearIfCmdIfIndex, snMacAuthClearIfCmdEntry=snMacAuthClearIfCmdEntry)
