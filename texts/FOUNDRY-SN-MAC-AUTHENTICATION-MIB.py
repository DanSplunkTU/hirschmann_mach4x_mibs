#
# PySNMP MIB module FOUNDRY-SN-MAC-AUTHENTICATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/foundry/FOUNDRY-SN-MAC-AUTHENTICATION-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:06:51 2022
# On host fv-az135-792 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, TimeTicks, ObjectIdentity, NotificationType, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Counter64, MibIdentifier, Gauge32, Unsigned32, ModuleIdentity, iso, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "TimeTicks", "ObjectIdentity", "NotificationType", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Counter64", "MibIdentifier", "Gauge32", "Unsigned32", "ModuleIdentity", "iso", "IpAddress")
DisplayString, MacAddress, TextualConvention, TimeStamp = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "TextualConvention", "TimeStamp")
snMacAuth = ModuleIdentity((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 28))
snMacAuth.setRevisions(('2007-06-25 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: snMacAuth.setRevisionsDescriptions(('',))
if mibBuilder.loadTexts: snMacAuth.setLastUpdated('200706250000Z')
if mibBuilder.loadTexts: snMacAuth.setOrganization('Foundry Networks, Inc')
if mibBuilder.loadTexts: snMacAuth.setContactInfo('')
if mibBuilder.loadTexts: snMacAuth.setDescription('Management Information Base module for MAC authentication\n            configuration and statistics.')
snMacAuthGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 28, 1))
snMacAuthClearGlobalCmd = MibScalar((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 28, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("valid", 0), ("clear", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snMacAuthClearGlobalCmd.setStatus('current')
if mibBuilder.loadTexts: snMacAuthClearGlobalCmd.setDescription('valid(0) - a SNMP-GET of this mib shows that it is valid command to use. \n\t\t clear(1) - represents clear MAC Authentication table for all ports.')
snMacAuthGlobalConfigState = MibScalar((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 28, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snMacAuthGlobalConfigState.setStatus('current')
if mibBuilder.loadTexts: snMacAuthGlobalConfigState.setDescription('Enable/disable MAC authentication on the global level.')
snMacAuthClearIfCmdTable = MibTable((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 28, 2), )
if mibBuilder.loadTexts: snMacAuthClearIfCmdTable.setStatus('current')
if mibBuilder.loadTexts: snMacAuthClearIfCmdTable.setDescription('The status of clearing an MAC Authentication entry for an interface.')
snMacAuthClearIfCmdEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 28, 2, 1), ).setIndexNames((0, "FOUNDRY-SN-MAC-AUTHENTICATION-MIB", "snMacAuthClearIfCmdIfIndex"))
if mibBuilder.loadTexts: snMacAuthClearIfCmdEntry.setStatus('current')
if mibBuilder.loadTexts: snMacAuthClearIfCmdEntry.setDescription('An entry of clearing an MAC Authentication entry for an interface.')
snMacAuthClearIfCmdIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 28, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: snMacAuthClearIfCmdIfIndex.setStatus('current')
if mibBuilder.loadTexts: snMacAuthClearIfCmdIfIndex.setDescription('ifIndex value of the local interface on which a clear command is issued and monitored.')
snMacAuthClearIfCmdAction = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 28, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("valid", 0), ("clear", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snMacAuthClearIfCmdAction.setStatus('current')
if mibBuilder.loadTexts: snMacAuthClearIfCmdAction.setDescription('valid(0) - a SNMP-GET of this mib shows that it is valid command to use. \n\t\t clear(1) - represents clearing an MAC Authentication entry for an interface.')
snMacAuthTable = MibTable((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 28, 3), )
if mibBuilder.loadTexts: snMacAuthTable.setStatus('current')
if mibBuilder.loadTexts: snMacAuthTable.setDescription('MAC Authentication table.')
snMacAuthEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 28, 3, 1), ).setIndexNames((0, "FOUNDRY-SN-MAC-AUTHENTICATION-MIB", "snMacAuthIfIndex"), (0, "FOUNDRY-SN-MAC-AUTHENTICATION-MIB", "snMacAuthVlanId"), (0, "FOUNDRY-SN-MAC-AUTHENTICATION-MIB", "snMacAuthMac"))
if mibBuilder.loadTexts: snMacAuthEntry.setStatus('current')
if mibBuilder.loadTexts: snMacAuthEntry.setDescription('An entry in the MAC Authentication table.')
snMacAuthIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 28, 3, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: snMacAuthIfIndex.setStatus('current')
if mibBuilder.loadTexts: snMacAuthIfIndex.setDescription('In order to identify a particular interface, this\n\t\tobject shall identify the instance of the ifIndex\n\t\tobject, defined in RFC 2863.')
snMacAuthVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 28, 3, 1, 2), Integer32())
if mibBuilder.loadTexts: snMacAuthVlanId.setStatus('current')
if mibBuilder.loadTexts: snMacAuthVlanId.setDescription('The ID of a VLAN of which this port is a member. Port must\n        be untagged. For tagged port which belongs to multiple\n        VLANs, this object return 0 which is an invalid VLAN ID\n        value.')
snMacAuthMac = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 28, 3, 1, 3), MacAddress())
if mibBuilder.loadTexts: snMacAuthMac.setStatus('current')
if mibBuilder.loadTexts: snMacAuthMac.setDescription('MAC Address to be authenticated.')
snMacAuthState = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 28, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("authenticate", 1), ("unauthenticate", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snMacAuthState.setStatus('current')
if mibBuilder.loadTexts: snMacAuthState.setDescription('.')
snMacAuthTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 28, 3, 1, 5), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snMacAuthTimeStamp.setStatus('current')
if mibBuilder.loadTexts: snMacAuthTimeStamp.setDescription('Timestamp at which the MAC was authenticated or failed to be authenticated.')
snMacAuthAge = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 28, 3, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snMacAuthAge.setStatus('current')
if mibBuilder.loadTexts: snMacAuthAge.setDescription('Age of the mac session in which the MAC address is authenticated.')
snMacAuthDot1x = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 28, 3, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snMacAuthDot1x.setStatus('current')
if mibBuilder.loadTexts: snMacAuthDot1x.setDescription('Indicates whether the Dot1x is enabled or not.')
snMacAuthClearMacSessionTable = MibTable((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 28, 4), )
if mibBuilder.loadTexts: snMacAuthClearMacSessionTable.setStatus('current')
if mibBuilder.loadTexts: snMacAuthClearMacSessionTable.setDescription('The status of clearing an MAC Session entry indexed by a MAC address.')
snMacAuthClearMacSessionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 28, 4, 1), ).setIndexNames((0, "FOUNDRY-SN-MAC-AUTHENTICATION-MIB", "snMacAuthClearMacSessionIfIndex"), (0, "FOUNDRY-SN-MAC-AUTHENTICATION-MIB", "snMacAuthClearMacSessionMac"))
if mibBuilder.loadTexts: snMacAuthClearMacSessionEntry.setStatus('current')
if mibBuilder.loadTexts: snMacAuthClearMacSessionEntry.setDescription('An entry of clearing an MAC Session entry indexed by a MAC address.')
snMacAuthClearMacSessionIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 28, 4, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: snMacAuthClearMacSessionIfIndex.setStatus('current')
if mibBuilder.loadTexts: snMacAuthClearMacSessionIfIndex.setDescription('ifIndex value of the local interface on which a clear command is issued and monitored.')
snMacAuthClearMacSessionMac = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 28, 4, 1, 2), MacAddress())
if mibBuilder.loadTexts: snMacAuthClearMacSessionMac.setStatus('current')
if mibBuilder.loadTexts: snMacAuthClearMacSessionMac.setDescription('An MAC Session entry indexed by a MAC address.')
snMacAuthClearMacSessionAction = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 28, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("valid", 0), ("clear", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snMacAuthClearMacSessionAction.setStatus('current')
if mibBuilder.loadTexts: snMacAuthClearMacSessionAction.setDescription('valid(0) - a SNMP-GET of this mib shows that it is valid command to use. \n\t\t clear(1) - represents clearing an MAC Session entry indexed by a MAC address.')
mibBuilder.exportSymbols("FOUNDRY-SN-MAC-AUTHENTICATION-MIB", snMacAuthTimeStamp=snMacAuthTimeStamp, snMacAuthClearMacSessionIfIndex=snMacAuthClearMacSessionIfIndex, snMacAuthClearMacSessionEntry=snMacAuthClearMacSessionEntry, snMacAuthTable=snMacAuthTable, snMacAuthIfIndex=snMacAuthIfIndex, snMacAuthClearIfCmdIfIndex=snMacAuthClearIfCmdIfIndex, snMacAuthGlobal=snMacAuthGlobal, snMacAuthEntry=snMacAuthEntry, snMacAuth=snMacAuth, snMacAuthClearMacSessionMac=snMacAuthClearMacSessionMac, snMacAuthClearMacSessionAction=snMacAuthClearMacSessionAction, snMacAuthClearMacSessionTable=snMacAuthClearMacSessionTable, snMacAuthMac=snMacAuthMac, snMacAuthGlobalConfigState=snMacAuthGlobalConfigState, snMacAuthVlanId=snMacAuthVlanId, snMacAuthState=snMacAuthState, snMacAuthClearIfCmdAction=snMacAuthClearIfCmdAction, snMacAuthClearGlobalCmd=snMacAuthClearGlobalCmd, snMacAuthAge=snMacAuthAge, snMacAuthClearIfCmdEntry=snMacAuthClearIfCmdEntry, snMacAuthDot1x=snMacAuthDot1x, PYSNMP_MODULE_ID=snMacAuth, snMacAuthClearIfCmdTable=snMacAuthClearIfCmdTable)
