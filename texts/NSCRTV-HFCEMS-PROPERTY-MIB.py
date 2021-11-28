#
# PySNMP MIB module NSCRTV-HFCEMS-PROPERTY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/glassway/NSCRTV-HFCEMS-PROPERTY-MIB
# Produced by pysmi-1.1.3 at Sun Nov 28 20:10:16 2021
# On host fv-az77-612 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
propertyIdent, = mibBuilder.importSymbols("NSCRTV-ROOT", "propertyIdent")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, Unsigned32, Bits, MibIdentifier, Counter64, Counter32, NotificationType, Gauge32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, IpAddress, ObjectIdentity, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Unsigned32", "Bits", "MibIdentifier", "Counter64", "Counter32", "NotificationType", "Gauge32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "IpAddress", "ObjectIdentity", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
analogPropertyTable = MibTable((1, 3, 6, 1, 4, 1, 17409, 1, 1, 1), )
if mibBuilder.loadTexts: analogPropertyTable.setStatus('mandatory')
if mibBuilder.loadTexts: analogPropertyTable.setDescription('ģԱ')
analogPropertyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 17409, 1, 1, 1, 1), ).setIndexNames((0, "NSCRTV-HFCEMS-PROPERTY-MIB", "analogParameterOID"))
if mibBuilder.loadTexts: analogPropertyEntry.setStatus('mandatory')
if mibBuilder.loadTexts: analogPropertyEntry.setDescription('ģԱĿ\n        OIDΪĿ뷽ǡȣOIDOIDǰ2Ա1.3ǰ1͡3\n        룬ͨOID뷽ʽ(0x2B)')
analogParameterOID = MibTableColumn((1, 3, 6, 1, 4, 1, 17409, 1, 1, 1, 1, 1), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: analogParameterOID.setStatus('mandatory')
if mibBuilder.loadTexts: analogParameterOID.setDescription('')
alarmEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 17409, 1, 1, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alarmEnable.setStatus('mandatory')
if mibBuilder.loadTexts: alarmEnable.setDescription("澯ʹֽܿڣӦλΪ'1'ʾ澯,'0'ʾֹ澯\n            Bit 0 : \u0378澯ʹ\n            Bit 1 : \u0378澯ʹ\n            Bit 2 : ߸澯ʹ\n            Bit 3 : ߸澯ʹ\n            Bit 47 ,ӦΪ0\n        ˶ӦڷʧԴ洢С")
analogAlarmState = MibTableColumn((1, 3, 6, 1, 4, 1, 17409, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("aasNominal", 1), ("aasHIHI", 2), ("aasHI", 3), ("aasLO", 4), ("aasLOLO", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: analogAlarmState.setStatus('mandatory')
if mibBuilder.loadTexts: analogAlarmState.setDescription('ĵǰ澯״̬')
analogAlarmHIHI = MibTableColumn((1, 3, 6, 1, 4, 1, 17409, 1, 1, 1, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: analogAlarmHIHI.setStatus('mandatory')
if mibBuilder.loadTexts: analogAlarmHIHI.setDescription('߸澯HIHIֵ˶ӦڷʧԴ洢С')
analogAlarmHI = MibTableColumn((1, 3, 6, 1, 4, 1, 17409, 1, 1, 1, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: analogAlarmHI.setStatus('mandatory')
if mibBuilder.loadTexts: analogAlarmHI.setDescription('߸澯HIֵ˶ӦڷʧԴ洢С')
analogAlarmLO = MibTableColumn((1, 3, 6, 1, 4, 1, 17409, 1, 1, 1, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: analogAlarmLO.setStatus('mandatory')
if mibBuilder.loadTexts: analogAlarmLO.setDescription('\u0378澯LOֵ˶ӦڷʧԴ洢С')
analogAlarmLOLO = MibTableColumn((1, 3, 6, 1, 4, 1, 17409, 1, 1, 1, 1, 7), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: analogAlarmLOLO.setStatus('mandatory')
if mibBuilder.loadTexts: analogAlarmLOLO.setDescription('\u0378澯LOLOֵ˶ӦڷʧԴ洢С')
analogAlarmDeadband = MibTableColumn((1, 3, 6, 1, 4, 1, 17409, 1, 1, 1, 1, 8), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: analogAlarmDeadband.setStatus('mandatory')
if mibBuilder.loadTexts: analogAlarmDeadband.setDescription('澯ֵ澯\U000e3b32ֵӦָ澯\n        澯֮ľֵֵø澯\n        ˶ӦڷʧԴ洢С')
discretePropertyTable = MibTable((1, 3, 6, 1, 4, 1, 17409, 1, 1, 2), )
if mibBuilder.loadTexts: discretePropertyTable.setStatus('mandatory')
if mibBuilder.loadTexts: discretePropertyTable.setDescription('ɢԱ')
discretePropertyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 17409, 1, 1, 2, 1), ).setIndexNames((0, "NSCRTV-HFCEMS-PROPERTY-MIB", "discreteParameterOID"), (0, "NSCRTV-HFCEMS-PROPERTY-MIB", "discreteAlarmValue"))
if mibBuilder.loadTexts: discretePropertyEntry.setStatus('mandatory')
if mibBuilder.loadTexts: discretePropertyEntry.setDescription('ɢԱĿOIDı뷽ʽͬģԱ')
discreteParameterOID = MibTableColumn((1, 3, 6, 1, 4, 1, 17409, 1, 1, 2, 1, 1), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: discreteParameterOID.setStatus('mandatory')
if mibBuilder.loadTexts: discreteParameterOID.setDescription('ɢԱ1OID')
discreteAlarmValue = MibTableColumn((1, 3, 6, 1, 4, 1, 17409, 1, 1, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: discreteAlarmValue.setStatus('mandatory')
if mibBuilder.loadTexts: discreteAlarmValue.setDescription('ɢԱ2ֵ\n        豸Ĳֵڴֵи澯')
discreteAlarmEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 17409, 1, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("disable", 1), ("enableMajor", 2), ("enableMinor", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: discreteAlarmEnable.setStatus('mandatory')
if mibBuilder.loadTexts: discreteAlarmEnable.setDescription('澯ʹܴ(23)д˲ĸ澯\n        澯ʹܹر(1)澯С\n        ˶ȱʡֵΪdisable(1)\n        ˶ӦڷʧԴ洢С')
discreteAlarmState = MibTableColumn((1, 3, 6, 1, 4, 1, 17409, 1, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 6, 7))).clone(namedValues=NamedValues(("dasNominal", 1), ("dasDiscreteMajor", 6), ("dasDiscreteMinor", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: discreteAlarmState.setStatus('mandatory')
if mibBuilder.loadTexts: discreteAlarmState.setDescription('ĵǰ澯״̬')
currentAlarmTable = MibTable((1, 3, 6, 1, 4, 1, 17409, 1, 1, 3), )
if mibBuilder.loadTexts: currentAlarmTable.setStatus('mandatory')
if mibBuilder.loadTexts: currentAlarmTable.setDescription('ǰ澯')
currentAlarmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 17409, 1, 1, 3, 1), ).setIndexNames((0, "NSCRTV-HFCEMS-PROPERTY-MIB", "currentAlarmOID"))
if mibBuilder.loadTexts: currentAlarmEntry.setStatus('mandatory')
if mibBuilder.loadTexts: currentAlarmEntry.setDescription('ǰ澯Ŀ\n        OIDı뷽ʽͬģԱ')
currentAlarmOID = MibTableColumn((1, 3, 6, 1, 4, 1, 17409, 1, 1, 3, 1, 1), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: currentAlarmOID.setStatus('mandatory')
if mibBuilder.loadTexts: currentAlarmOID.setDescription('NEǰڸ澯״̬ĲOID,Աеĸ澯OIDӦ')
currentAlarmState = MibTableColumn((1, 3, 6, 1, 4, 1, 17409, 1, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("caasHIHI", 2), ("caasHI", 3), ("caasLO", 4), ("caasLOLO", 5), ("caasDiscreteMajor", 6), ("caasDiscreteMinor", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: currentAlarmState.setStatus('mandatory')
if mibBuilder.loadTexts: currentAlarmState.setDescription('澯ĵǰ澯״̬')
currentAlarmValue = MibTableColumn((1, 3, 6, 1, 4, 1, 17409, 1, 1, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: currentAlarmValue.setStatus('mandatory')
if mibBuilder.loadTexts: currentAlarmValue.setDescription('澯ֵ')
mibBuilder.exportSymbols("NSCRTV-HFCEMS-PROPERTY-MIB", currentAlarmValue=currentAlarmValue, currentAlarmTable=currentAlarmTable, analogAlarmHIHI=analogAlarmHIHI, currentAlarmState=currentAlarmState, alarmEnable=alarmEnable, analogPropertyEntry=analogPropertyEntry, analogAlarmHI=analogAlarmHI, currentAlarmOID=currentAlarmOID, analogAlarmLOLO=analogAlarmLOLO, discreteAlarmValue=discreteAlarmValue, currentAlarmEntry=currentAlarmEntry, analogAlarmState=analogAlarmState, discreteParameterOID=discreteParameterOID, discreteAlarmState=discreteAlarmState, analogAlarmLO=analogAlarmLO, analogAlarmDeadband=analogAlarmDeadband, discreteAlarmEnable=discreteAlarmEnable, analogPropertyTable=analogPropertyTable, analogParameterOID=analogParameterOID, discretePropertyEntry=discretePropertyEntry, discretePropertyTable=discretePropertyTable)
