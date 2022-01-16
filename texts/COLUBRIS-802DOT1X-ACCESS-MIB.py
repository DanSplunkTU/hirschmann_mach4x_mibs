#
# PySNMP MIB module COLUBRIS-802DOT1X-ACCESS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/hpmsm/COLUBRIS-802DOT1X-MIB.my
# Produced by pysmi-1.1.8 at Sun Jan 16 00:37:55 2022
# On host fv-az42-839 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
colubrisMgmtV2, = mibBuilder.importSymbols("COLUBRIS-SMI", "colubrisMgmtV2")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Bits, Integer32, Gauge32, Unsigned32, ModuleIdentity, Counter64, NotificationType, iso, IpAddress, MibIdentifier, TimeTicks, Counter32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "Gauge32", "Unsigned32", "ModuleIdentity", "Counter64", "NotificationType", "iso", "IpAddress", "MibIdentifier", "TimeTicks", "Counter32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
colubris802Dot1xMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 8744, 5, 8))
if mibBuilder.loadTexts: colubris802Dot1xMIB.setLastUpdated('200601090000Z')
if mibBuilder.loadTexts: colubris802Dot1xMIB.setOrganization('Colubris Networks, Inc.')
if mibBuilder.loadTexts: colubris802Dot1xMIB.setContactInfo('Colubris Networks\n                     Postal: 200 West Street Ste 300\n                             Waltham, Massachusetts 02451-1121\n                             UNITED STATES\n                     Phone:  +1 781 684 0001\n                     Fax:    +1 781 684 0009\n\n                     E-mail: cn-snmp@colubris.com')
if mibBuilder.loadTexts: colubris802Dot1xMIB.setDescription('Colubris Networks 802.1x Extention MIB.')
coPaeMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 8, 1))
coDot1xPaeSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 8, 1, 1))
coDot1xPaeAuthenticator = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 8, 1, 2))
coDot1xPaeSystemModifyKey = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 8, 1, 1, 1), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDot1xPaeSystemModifyKey.setStatus('current')
if mibBuilder.loadTexts: coDot1xPaeSystemModifyKey.setDescription("Indicates if WEP and TKIP group keys are updated at\n                 regular intervals.                \n                   'true': Group key update is enabled.\n                   'false': Group key update is disabled.")
coDot1xPaeSystemModifyKeyInterval = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 8, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(30, 65535)).clone(300)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: coDot1xPaeSystemModifyKeyInterval.setStatus('current')
if mibBuilder.loadTexts: coDot1xPaeSystemModifyKeyInterval.setDescription('Specifies the interval (in seconds) between updates of the WEP transmit keys.')
coDot1xAuthQuietPeriod = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 8, 1, 2, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(60)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: coDot1xAuthQuietPeriod.setStatus('current')
if mibBuilder.loadTexts: coDot1xAuthQuietPeriod.setDescription('Specifies the initial value of the quietPeriod constant used\n                 by the Authenticator PAE state machine.')
coDot1xAuthTxPeriod = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 8, 1, 2, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(30)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: coDot1xAuthTxPeriod.setStatus('current')
if mibBuilder.loadTexts: coDot1xAuthTxPeriod.setDescription('Specifies the initial value of the txPeriod constant used by\n                 the Authenticator PAE state machine.')
coDot1xAuthSuppTimeout = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 8, 1, 2, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(3)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: coDot1xAuthSuppTimeout.setStatus('current')
if mibBuilder.loadTexts: coDot1xAuthSuppTimeout.setDescription('Specifies the initial value of the suppTimeout constant used\n                 by the Backend Authentication state machine.')
coDot1xAuthServerTimeout = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 8, 1, 2, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(30)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: coDot1xAuthServerTimeout.setStatus('current')
if mibBuilder.loadTexts: coDot1xAuthServerTimeout.setDescription('Specifies the initial value of the serverTimeout constant used\n                 by the Backend Authentication state machine.')
coDot1xAuthMaxReq = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 8, 1, 2, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 10)).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: coDot1xAuthMaxReq.setStatus('current')
if mibBuilder.loadTexts: coDot1xAuthMaxReq.setDescription('Specifies the initial value of the maxReq constant used by\n                 the Backend Authentication state machine.')
coDot1xAuthReAuthPeriod = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 8, 1, 2, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(3600)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: coDot1xAuthReAuthPeriod.setStatus('current')
if mibBuilder.loadTexts: coDot1xAuthReAuthPeriod.setDescription('Specifies the initial value of the reAuthPeriod constant used\n                 by the Reauthentication Timer state machine.')
coDot1xAuthReAuthEnabled = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 8, 1, 2, 7), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: coDot1xAuthReAuthEnabled.setStatus('current')
if mibBuilder.loadTexts: coDot1xAuthReAuthEnabled.setDescription("Specifies the enable/disable control used by the\n                 Reauthentication Timer state machine (8.5.5.1).\n\n                   'true': Enables the control used by the\n                           re-authentication timer state machine.\n\n                   'false': Disables the control.")
coDot1xAuthKeyTxEnabled = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 8, 1, 2, 8), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: coDot1xAuthKeyTxEnabled.setStatus('current')
if mibBuilder.loadTexts: coDot1xAuthKeyTxEnabled.setDescription("Specifies the initial value of the keyTransmissionEnabled\n                 constant used by the Authenticator PAE state machine.\n\n                   'true': Enables the constant used by the Authenticator\n                           PAE state machine.\n\n                   'false': Disables the constant.")
coDot1xAuthReAuthMax = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 8, 1, 2, 9), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(8)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: coDot1xAuthReAuthMax.setStatus('current')
if mibBuilder.loadTexts: coDot1xAuthReAuthMax.setDescription('Specifies the number of reauthentication attempts that are\n                 permitted before the Port becomes Unauthorized.')
coDot1xPaeConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 8, 2))
coDot1xPaeGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 8, 2, 1))
coDot1xPaeCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 8, 2, 2))
coDot1xPaeSystemGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8744, 5, 8, 2, 1, 1)).setObjects(("COLUBRIS-802DOT1X-ACCESS-MIB", "coDot1xPaeSystemModifyKey"), ("COLUBRIS-802DOT1X-ACCESS-MIB", "coDot1xPaeSystemModifyKeyInterval"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    coDot1xPaeSystemGroup = coDot1xPaeSystemGroup.setStatus('current')
if mibBuilder.loadTexts: coDot1xPaeSystemGroup.setDescription('A collection of objects providing extended system information\n                 about, and control over, a PAE.')
coDot1xPaeAuthenticatorGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8744, 5, 8, 2, 1, 2)).setObjects(("COLUBRIS-802DOT1X-ACCESS-MIB", "coDot1xAuthQuietPeriod"), ("COLUBRIS-802DOT1X-ACCESS-MIB", "coDot1xAuthTxPeriod"), ("COLUBRIS-802DOT1X-ACCESS-MIB", "coDot1xAuthSuppTimeout"), ("COLUBRIS-802DOT1X-ACCESS-MIB", "coDot1xAuthServerTimeout"), ("COLUBRIS-802DOT1X-ACCESS-MIB", "coDot1xAuthMaxReq"), ("COLUBRIS-802DOT1X-ACCESS-MIB", "coDot1xAuthReAuthPeriod"), ("COLUBRIS-802DOT1X-ACCESS-MIB", "coDot1xAuthReAuthEnabled"), ("COLUBRIS-802DOT1X-ACCESS-MIB", "coDot1xAuthKeyTxEnabled"), ("COLUBRIS-802DOT1X-ACCESS-MIB", "coDot1xAuthReAuthMax"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    coDot1xPaeAuthenticatorGroup = coDot1xPaeAuthenticatorGroup.setStatus('current')
if mibBuilder.loadTexts: coDot1xPaeAuthenticatorGroup.setDescription('A collection of objects providing configuration information\n                 about all Authenticator PAE.')
coDot1xPaeCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 8744, 5, 8, 2, 2, 1)).setObjects(("COLUBRIS-802DOT1X-ACCESS-MIB", "coDot1xPaeSystemGroup"), ("COLUBRIS-802DOT1X-ACCESS-MIB", "coDot1xPaeAuthenticatorGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    coDot1xPaeCompliance = coDot1xPaeCompliance.setStatus('current')
if mibBuilder.loadTexts: coDot1xPaeCompliance.setDescription('The compliance statement for extended device support of Port\n                 Access Control.')
mibBuilder.exportSymbols("COLUBRIS-802DOT1X-ACCESS-MIB", coDot1xAuthMaxReq=coDot1xAuthMaxReq, colubris802Dot1xMIB=colubris802Dot1xMIB, coDot1xPaeSystemGroup=coDot1xPaeSystemGroup, coDot1xPaeGroups=coDot1xPaeGroups, coDot1xPaeCompliance=coDot1xPaeCompliance, coDot1xAuthSuppTimeout=coDot1xAuthSuppTimeout, coDot1xPaeSystem=coDot1xPaeSystem, coDot1xAuthReAuthPeriod=coDot1xAuthReAuthPeriod, PYSNMP_MODULE_ID=colubris802Dot1xMIB, coDot1xAuthKeyTxEnabled=coDot1xAuthKeyTxEnabled, coDot1xPaeAuthenticator=coDot1xPaeAuthenticator, coDot1xAuthTxPeriod=coDot1xAuthTxPeriod, coPaeMIBObjects=coPaeMIBObjects, coDot1xPaeAuthenticatorGroup=coDot1xPaeAuthenticatorGroup, coDot1xPaeSystemModifyKeyInterval=coDot1xPaeSystemModifyKeyInterval, coDot1xPaeConformance=coDot1xPaeConformance, coDot1xAuthQuietPeriod=coDot1xAuthQuietPeriod, coDot1xAuthServerTimeout=coDot1xAuthServerTimeout, coDot1xAuthReAuthEnabled=coDot1xAuthReAuthEnabled, coDot1xPaeSystemModifyKey=coDot1xPaeSystemModifyKey, coDot1xPaeCompliances=coDot1xPaeCompliances, coDot1xAuthReAuthMax=coDot1xAuthReAuthMax)
